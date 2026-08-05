#!/usr/bin/env python3
"""lint_wiki.py — deterministic wiki-link hygiene for this vault. Exit 1 on empty [[]] links.
Usage: python tools/lint_wiki.py   (run from vault root; complements llm-wiki:lint's LLM pass)
A wiki page nobody links, or a link pointing nowhere, carries no meaning — this makes that a number."""
import os, re, sys, collections

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(VAULT, "okf") if os.path.isdir(os.path.join(VAULT, "okf")) else os.path.join(VAULT, "wiki")
pages, links = {}, []
for d, _, fs in os.walk(WIKI):
    for f in fs:
        if f.endswith(".md"):
            stem = f[:-3].lower()
            pages[stem] = os.path.join(d, f)
for stem, path in pages.items():
    try: text = open(path, encoding="utf-8", errors="replace").read()
    except OSError: continue
    for m in re.finditer(r"\[\[([^\]\[]*)\]\]", text):
        target = m.group(1).split("|")[0].split("#")[0].strip()
        links.append((stem, target))

empty = [(s, t) for s, t in links if not t]
norm = lambda x: re.sub(r"[\s_-]+", "-", x.lower())
page_norms = {norm(p) for p in pages}
dangling = collections.Counter(t for s, t in links if t and norm(t) not in page_norms)
linked_targets = {norm(t) for _, t in links if t}
orphans = [p for p in pages if norm(p) not in linked_targets and p not in ("index", "log", "hot", "overview", "claude")]

print(f"pages={len(pages)} links={len(links)} EMPTY=[[]]:{len(empty)} dangling-targets:{len(dangling)} orphan-pages:{len(orphans)}")
for t, c in dangling.most_common(15): print(f"  dangling x{c}: [[{t}]]")
if orphans: print("  orphans (nothing links to them):", ", ".join(sorted(orphans)[:15]))
print("WIKI LINT " + ("FAIL — empty links carry zero meaning" if empty else "PASS (empties)"))
sys.exit(1 if empty else 0)
