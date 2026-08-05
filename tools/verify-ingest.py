#!/usr/bin/env python3
"""verify-ingest.py -- reproducible ingest-integrity PROOF for a claude-obsidian vault.

Windows-native. Replaces the plugin's bash gate (wiki-lock.sh etc.) that does not
run on Windows -- that is itself a MITIGATION: the gate now actually executes here.

The disease this catches (per every failure log in CLAUDE.md): FAKED INGEST --
pages written, edges never drawn, or edges dumped into a `## Related` block that
satisfies a naive >=8 counter while producing nothing traversable.

TESTS (each link-target wiki page):
  1. >=8 inbound links from >=8 DISTINCT source pages   (kills the Related-dump)
  2. those links appear INLINE in prose, not only in a trailing Related/See-also
  3. edges from >=2 different classes (entity/concept/synthesis/source)  (no clique)
  4. hash present in .raw/.manifest.json                (provenance; warn if manifest absent)
  5. not a stub (body byte floor)

MITIGATIONS: per-page failure list naming the exact reason to fix.
PROOF: reproducible pass/fail counts + non-zero exit code on failure.
       Same vault in -> same numbers out. Numbers or it did not happen.

Usage:  python tools/verify-ingest.py [vault_dir]  [--min N] [--json]
Exit:   0 = all target pages pass ; 1 = one or more fail ; 2 = usage/error
"""
import os, re, sys, json, collections

VAULT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = "okf" if os.path.isdir(os.path.join(VAULT_DIR, "okf")) else "wiki"
TARGET_CLASSES = ("entities", "concepts", "synthesis", "sources", "comparisons", "LLM_Tests", "Principles_and_Frameworks", "Experiments")
META_NAMES = {"index.md", "log.md", "hot.md", "overview.md", "dashboard.md",
              "_index.md", "getting-started.md", "wiki map.md"}
RELATED_HDR = re.compile(r"\n#{1,4}\s*(related|see also|links|connections)\b", re.I)
WIKILINK = re.compile(r"\[\[([^\]|#]+)")
STUB_BODY_FLOOR = 400   # bytes of body (excluding frontmatter) below which = stub


def classify(path, vault):
    rel = os.path.relpath(path, os.path.join(vault, WIKI)).replace(os.sep, "/")
    return rel.split("/")[0] if "/" in rel else "_root"


def read(path):
    return open(path, encoding="utf-8", errors="replace").read()


def strip_fm(text):
    m = re.match(r"^---\r?\n.*?\r?\n---\r?\n", text, re.S)
    return text[m.end():] if m else text


def load_manifest(vault):
    p = os.path.join(vault, ".raw", ".manifest.json")
    if not os.path.isfile(p):
        return None
    try:
        d = json.load(open(p, encoding="utf-8"))
        hashed = set()
        for k, v in (d.get("sources") or {}).items():
            if isinstance(v, dict) and v.get("hash"):
                hashed.add(os.path.basename(k).lower())
        return hashed
    except Exception:
        return set()


def main(argv):
    vault = "."
    min_links = 8
    as_json = False
    for a in argv:
        if a == "--json":
            as_json = True
        elif a.startswith("--min"):
            try:
                min_links = int(a.split("=")[1]) if "=" in a else min_links
            except Exception:
                pass
        elif not a.startswith("-"):
            vault = a
    wiki_dir = os.path.join(vault, WIKI)
    if not os.path.isdir(wiki_dir):
        print(f"error: no {wiki_dir}/ -- not a claude-obsidian vault", file=sys.stderr)
        return 2

    manifest = load_manifest(vault)

    # index every .md: its class, its body, and the set of pages it links (inline)
    pages = {}       # stem-lower -> {path, cls, body_bytes}
    inline_src = collections.defaultdict(set)   # target-stem -> {source stems} (inline only)
    total_ref = collections.Counter()           # target-stem -> ALL inbound refs (anywhere, any file)
    for root, dirs, files in os.walk(wiki_dir):
        for n in files:
            if not n.endswith(".md"):
                continue
            p = os.path.join(root, n)
            body_full = strip_fm(read(p))
            # total inbound: every wikilink anywhere, including meta + Related dumps
            for tgt in WIKILINK.findall(body_full):
                total_ref[tgt.strip().split("/")[-1].lower()] += 1
            if os.sep + "meta" + os.sep in p or n.lower() in META_NAMES:
                continue
            stem = n[:-3].lower()
            pages[stem] = {"path": p, "cls": classify(p, vault),
                           "body_bytes": len(body_full.encode("utf-8", "replace"))}
            # split off trailing Related/See-also block -> only count links ABOVE it
            m = RELATED_HDR.search(body_full)
            above = body_full[:m.start()] if m else body_full
            for tgt in WIKILINK.findall(above):
                inline_src[tgt.strip().split("/")[-1].lower()].add(stem)

    rows, npass = [], 0
    targets = [(s, m) for s, m in pages.items() if m["cls"] in TARGET_CLASSES]
    for stem, meta in sorted(targets):
        srcs = inline_src.get(stem, set())
        distinct = len(srcs)
        classes = {pages[s]["cls"] for s in srcs if s in pages}
        cross = len(classes) >= 2
        hashed = (manifest is None) or (os.path.basename(meta["path"]).lower() in manifest)
        stub = meta["body_bytes"] < STUB_BODY_FLOOR
        ok = distinct >= min_links and cross and not stub and hashed
        total = total_ref.get(stem, 0)
        reasons = []
        if distinct < min_links: reasons.append(f"only {distinct} distinct inline sources (<{min_links})")
        if not cross:            reasons.append(f"clique: sources span {len(classes)} class(es), need >=2")
        if stub:                 reasons.append(f"stub: body {meta['body_bytes']}b (<{STUB_BODY_FLOOR})")
        if not hashed:           reasons.append("no hash in .raw/.manifest.json")
        # TRIAGE (resolves the sparse-vs-faked caveat): if edges EXIST in the corpus
        # (total refs >= gate) but aren't drawn inline from distinct sources -> FAKED,
        # redraw now. If the corpus barely references it at all -> SPARSE, needs sources.
        if ok:
            triage = "OK"
        elif not stub and total >= min_links and distinct < min_links:
            triage = f"FAKED-FIXABLE (refs exist: {total} total but only {distinct} distinct-inline -> REDRAW edges)"
        elif stub:
            triage = "STUB (write the page)"
        else:
            triage = f"SPARSE ({total} total refs in corpus -> NEEDS SOURCES, not a redraw)"
        rows.append({"page": os.path.relpath(meta["path"], vault).replace(os.sep, "/"),
                     "distinct_sources": distinct, "total_refs": total, "cross_class": cross,
                     "stub": stub, "hashed": hashed, "pass": ok, "reasons": reasons,
                     "triage": triage})
        if ok: npass += 1

    total = len(rows)
    fail = total - npass
    if as_json:
        print(json.dumps({"vault": vault, "min_links": min_links,
                          "manifest_present": manifest is not None,
                          "target_pages": total, "pass": npass, "fail": fail,
                          "rows": rows}, indent=2))
    else:
        print(f"INGEST-INTEGRITY PROOF -- {vault}  (gate: >={min_links} distinct inline sources, "
              f"cross-class, non-stub, hashed)")
        print(f"manifest present: {manifest is not None}\n")
        for r in sorted(rows, key=lambda x: (x["pass"], x["triage"], x["distinct_sources"])):
            mark = "PASS" if r["pass"] else "FAIL"
            tag = "" if r["pass"] else "  " + r["triage"]
            print(f"  [{mark}] {r['distinct_sources']:2}inline/{r['total_refs']:3}total  {r['page']}{tag}")
        tri = collections.Counter(r["triage"].split(" ")[0] for r in rows if not r["pass"])
        print(f"\n== PROOF: {npass}/{total} pass the real-ingest gate. {fail} fail. ==")
        print("== TRIAGE of failures (the actionable split): " +
              ", ".join(f"{k}={v}" for k, v in tri.most_common()) + " ==")
        print("  FAKED-FIXABLE = redraw edges now (corpus already has the refs).")
        print("  SPARSE = needs more source material, not a redraw. STUB = write the page.")
        print("Reproducible: same vault -> same numbers. Re-run after any ingest.")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
