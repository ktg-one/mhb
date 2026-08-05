#!/usr/bin/env python3
"""wiki-lock.py -- Windows-native port of the plugin's wiki-lock.sh.

Per-file advisory locking via ATOMIC lockfile create (os.O_EXCL, same guarantee
as bash `set -o noclobber`) + age-based staleness. No bash, no flock, no
sha1sum -- runs on Windows where the .sh silently fails.

Faithful to wiki-lock.sh semantics:
  acquire <rel>   -> 0 if taken, 75 if held & age<STALE, reaps stale then takes
  release <rel>   -> rm lockfile, idempotent (0)
  list            -> "pid age path" per held lock
  clear-stale [--max-age N]  -> remove locks older than N (default 3600); prints count
  peek <rel>      -> holder line or "unheld"
Exit: 0 ok | 2 usage | 4 bad path | 75 held.

NOTE: this vault is SINGLE-WRITER (CLAUDE.md), so locking is belt-and-suspenders.
Ported because you asked and the bash original does not execute on Windows.
"""
import os, sys, time, hashlib, glob

STALE_AFTER_SEC = 60


def vault_root():
    return os.environ.get("WIKI_LOCK_VAULT") or \
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _paths():
    root = vault_root()
    locks = os.path.join(root, ".vault-meta", "locks")
    return root, locks


def _sha1(p):
    return hashlib.sha1(p.encode("utf-8")).hexdigest()


def _validate(p):
    if not p:
        sys.stderr.write("ERR: path cannot be empty\n"); sys.exit(4)
    if p.startswith("/") or ".." in p or "\n" in p or "\r" in p:
        sys.stderr.write(f"ERR: invalid vault-relative path: {p}\n"); sys.exit(4)
    root, _ = _paths()
    rr = os.path.realpath(root)
    tgt = os.path.realpath(os.path.join(rr, p))
    if os.path.commonpath([rr, tgt]) != rr:
        sys.stderr.write(f"ERR: path resolves outside vault: {p}\n"); sys.exit(4)


def _lockfile(p):
    _, locks = _paths()
    return os.path.join(locks, _sha1(p) + ".lock")


def _write_lock(lf, p):
    fd = os.open(lf, os.O_CREAT | os.O_EXCL | os.O_WRONLY)  # atomic create
    os.write(fd, f"{os.getpid()} {int(time.time())} {p}\n".encode("utf-8"))
    os.close(fd)


def acquire(p):
    _validate(p)
    _, locks = _paths(); os.makedirs(locks, exist_ok=True)
    lf = _lockfile(p)
    try:
        _write_lock(lf, p); return 0
    except FileExistsError:
        try:
            age = int(time.time()) - int(open(lf, encoding="utf-8").read().split()[1])
        except Exception:
            age = STALE_AFTER_SEC + 1
        if age < STALE_AFTER_SEC:
            sys.stderr.write(f"held ({age}s < {STALE_AFTER_SEC})\n"); return 75
        os.remove(lf)          # reap stale, then take
        _write_lock(lf, p); return 0


def release(p):
    _validate(p)
    try:
        os.remove(_lockfile(p))
    except FileNotFoundError:
        pass
    return 0


def list_held():
    _, locks = _paths(); now = int(time.time())
    for lf in sorted(glob.glob(os.path.join(locks, "*.lock"))):
        try:
            pid, ep, path = open(lf, encoding="utf-8").read().split(None, 2)
            print(f"{pid} {now - int(ep)}s {path.strip()}")
        except Exception:
            pass
    return 0


def clear_stale(max_age=3600):
    _, locks = _paths(); now = int(time.time()); n = 0
    for lf in glob.glob(os.path.join(locks, "*.lock")):
        try:
            age = now - int(open(lf, encoding="utf-8").read().split()[1])
        except Exception:
            age = max_age + 1
        if age > max_age:
            os.remove(lf); n += 1
    print(n); return 0


def peek(p):
    _validate(p); lf = _lockfile(p)
    print(open(lf, encoding="utf-8").read().strip() if os.path.isfile(lf) else "unheld")
    return 0


def main(a):
    if not a:
        sys.stderr.write("usage: wiki-lock.py {acquire|release|list|clear-stale|peek} [path]\n")
        return 2
    cmd = a[0]
    if cmd == "acquire":      return acquire(a[1])
    if cmd == "release":      return release(a[1])
    if cmd == "list":         return list_held()
    if cmd == "peek":         return peek(a[1])
    if cmd == "clear-stale":
        ma = int(a[a.index("--max-age") + 1]) if "--max-age" in a else 3600
        return clear_stale(ma)
    sys.stderr.write(f"unknown command: {cmd}\n"); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
