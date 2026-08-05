#!/usr/bin/env python3
"""
run_batch.py - fan out the honesty suite across many models CONCURRENTLY
through one Vercel AI Gateway endpoint. No more 10 windows.

Each model is a separate run_suite.py subprocess (isolated session = clean blind/
gated state per model). Default 10 in flight at once.

Setup:
  export AI_GATEWAY_API_KEY=vck_...        # Vercel dashboard -> AI Gateway -> API Keys

Usage:
  python run_batch.py                       # all models in models.txt, 10 concurrent, honesty session
  python run_batch.py -n 5                   # 5 concurrent
  python run_batch.py --mbti                 # blind persona pass (clean session per model)
  python run_batch.py anthropic/claude-opus-4.7 openai/gpt-5.5   # explicit models, ignore file
  python run_batch.py --models my_list.txt
  python run_batch.py --dry-run              # print the plan, run nothing

Transcripts land in raw/sources/ (one per model), ready for score-and-ingest.
"""
import os, sys, subprocess, argparse, pathlib, concurrent.futures as cf, time, urllib.request, json

HERE = pathlib.Path(__file__).resolve().parent
SUITE = HERE / "run_suite.py"

def load_env():
    """Load KEY=VALUE from tools/.env then vault-root .env into os.environ (existing env wins).
    Dependency-free; ignores comments/blank lines, strips surrounding quotes."""
    for envf in (HERE / ".env", HERE.parent / ".env"):
        if not envf.exists(): continue
        for ln in envf.read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if not ln or ln.startswith("#") or "=" not in ln: continue
            k, v = ln.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

def fetch_free_models(base_url, key):
    """Fetch OpenRouter's LIVE free-tier model IDs (pricing 0 / ':free', text-out).
    Returns [] on any failure so the caller falls back to models-free.txt."""
    try:
        req = urllib.request.Request(base_url.rstrip("/") + "/models",
            headers={"Authorization": f"Bearer {key}"} if key else {})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read()).get("data", [])
    except Exception as e:
        print(f"(live free-model fetch failed: {e}; using models-free.txt snapshot)"); return []
    def zero(x):
        try: return float(x) == 0.0
        except Exception: return False
    out = []
    for m in data:
        mid = m.get("id", ""); pr = m.get("pricing", {}) or {}
        if mid.endswith(":free") or (zero(pr.get("prompt")) and zero(pr.get("completion"))):
            outs = (m.get("architecture", {}) or {}).get("output_modalities") or []
            if not outs or "text" in outs:
                out.append(mid)
    return sorted(set(out))

def load_models(path, cli_models):
    if cli_models:
        return cli_models
    p = pathlib.Path(path)
    if not p.exists():
        sys.exit(f"no model list at {p} (and none given on CLI)")
    out = []
    for ln in p.read_text(encoding="utf-8").splitlines():
        ln = ln.split("#", 1)[0].strip()
        if ln:
            out.append(ln)
    return out

def run_one(model, args):
    cmd = [sys.executable, str(SUITE), "--model", model, "--surface", args.surface]
    if args.mbti:            cmd.append("--mbti")
    if args.test != "full":  cmd += ["--test", args.test]
    if args.consequence:     cmd.append("--consequence")
    if args.base_url:        cmd += ["--base-url", args.base_url]
    if args.out:             cmd += ["--out", args.out]
    t0 = time.time()
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=args.timeout)
        ok = r.returncode == 0
        tail = (r.stdout or r.stderr or "").strip().splitlines()[-1:] or [""]
        return model, ok, f"{time.time()-t0:.0f}s | {tail[0][:120]}"
    except subprocess.TimeoutExpired:
        return model, False, f"TIMEOUT after {args.timeout}s"
    except Exception as e:
        return model, False, f"ERR {e}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("models", nargs="*", help="explicit model IDs (override models.txt)")
    ap.add_argument("-n", "--concurrency", type=int, default=10)
    ap.add_argument("--models", dest="models_file", default=str(HERE / "models.txt"))
    ap.add_argument("--mbti", action="store_true")
    ap.add_argument("--test", choices=["full", "qa", "ladder", "pique", "probe"], default="full",
                    help="battery to run (default full = qa+ladder; MBTI excluded by design)")
    ap.add_argument("--consequence", action="store_true", help="stakes-frame arm (experimental)")
    ap.add_argument("--surface", default="api")
    ap.add_argument("--base-url", default="")
    ap.add_argument("--out", default="")
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--free", action="store_true",
                    help="OpenRouter free tier: base_url=openrouter + fetch live :free models")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    load_env()   # read tools/.env or vault-root .env

    if not SUITE.exists(): sys.exit(f"run_suite.py not found at {SUITE}")

    if a.free and not a.base_url:
        a.base_url = "https://openrouter.ai/api/v1"
    key = (os.environ.get("OPENROUTER_API_KEY") if a.free else "") \
          or os.environ.get("AI_GATEWAY_API_KEY") or os.environ.get("OPENROUTER_API_KEY") \
          or os.environ.get("LLM_API_KEY")
    if not a.dry_run and not key:
        sys.exit("no key found. Set OPENROUTER_API_KEY (--free) or AI_GATEWAY_API_KEY (gateway) "
                 "in env or a .env file (tools/.env or vault root).")

    if a.free and not a.models:
        # live fetch (skips network on dry-run); snapshot fallback = models-free.txt
        models = load_models(str(HERE / "models-free.txt"), []) if a.dry_run \
                 else (fetch_free_models(a.base_url, key) or load_models(str(HERE / "models-free.txt"), []))
    else:
        models = load_models(a.models_file, a.models)
    mode = "MBTI-blind" if a.mbti else f"{a.test}{'+consequence' if a.consequence else ''}"
    print(f"== {len(models)} models | {a.concurrency} concurrent | {mode} ==")
    for m in models: print("   -", m)
    if a.dry_run:
        print("(dry-run: nothing executed)"); return

    ok = fail = 0
    with cf.ThreadPoolExecutor(max_workers=a.concurrency) as ex:
        futs = {ex.submit(run_one, m, a): m for m in models}
        for fut in cf.as_completed(futs):
            model, good, info = fut.result()
            print(f"[{'ok ' if good else 'FAIL'}] {model:38} {info}")
            ok += good; fail += (not good)
    print(f"\n== done: {ok} ok, {fail} failed ==")
    if fail: sys.exit(1)

if __name__ == "__main__":
    main()
