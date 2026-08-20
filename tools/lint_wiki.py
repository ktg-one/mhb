#!/usr/bin/env python3
"""Deterministic Obsidian-link hygiene for the active OKF canon.

The active research graph excludes ``okf/meta`` mirrors and generated non-Markdown
artifacts. Targets may resolve to any vault file because Obsidian wikilinks can
point to CSV, PDF, canvas, and raw evidence as well as Markdown notes.
"""

import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wiki_links import LinkResolver, norm, target_keys


VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(VAULT, "okf")
EXCLUDED_DIRS = {".git", "meta"}
RESERVED_STEMS = {"index", "log", "hot", "overview", "dashboard", "claude"}
WIKILINK = re.compile(r"(?<!\[)\[\[([^\[\]]*)\]\](?!\])")
EMPTY_WIKILINK = re.compile(r"(?<!\[)\[\[\s*\]\](?!\])")


def page_key(path):
    """Normalized wiki-relative page path: forward slashes, lowercase, no .md.

    Based on WIKI (not VAULT): wikilink targets are written relative to the
    wiki root, so keys must share that root or path-qualified links never
    exact-match.
    """
    rel = os.path.relpath(path, WIKI).replace(os.sep, "/")
    key, _ = os.path.splitext(rel)
    return norm(key)


def active_markdown_files():
    files = []
    for directory, dirs, names in os.walk(WIKI):
        dirs[:] = [d for d in dirs if d.lower() not in EXCLUDED_DIRS]
        for name in names:
            if name.lower().endswith(".md"):
                files.append(os.path.join(directory, name))
    return files


def resolvable_targets():
    targets = set()
    for directory, dirs, names in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d.lower() != ".git"]
        for name in names:
            path = os.path.join(directory, name)
            rel = os.path.relpath(path, VAULT).replace(os.sep, "/")
            stem, _ = os.path.splitext(name)
            rel_stem, _ = os.path.splitext(rel)
            targets.update({norm(name), norm(stem), norm(rel), norm(rel_stem)})
    return targets


page_files = active_markdown_files()
target_norms = resolvable_targets()
links = []
empty = []
page_keys = collections.Counter()

for path in page_files:
    page_keys[page_key(path)] += 1
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        continue
    empty.extend((path, match.group(0)) for match in EMPTY_WIKILINK.finditer(text))
    for match in WIKILINK.finditer(text):
        target = match.group(1).split("|", 1)[0].split("#", 1)[0].strip()
        if target:
            links.append((path, target))

dangling = collections.Counter(
    target for _, target in links if target_keys(target).isdisjoint(target_norms)
)

# Resolve each link to an exact normalized wiki-relative page path, so a
# path-qualified link only marks its intended page as linked. Bare links
# resolve by stem with a deterministic pick (shallowest path, then alpha).
# The resolver precomputes exact/suffix/stem indexes once (see wiki_links.py).
resolver = LinkResolver(page_keys)


linked_pages = {resolved for resolved in (resolver.resolve(t) for _, t in links) if resolved}
orphans = [
    os.path.relpath(path, VAULT).replace(os.sep, "/")
    for path in page_files
    if page_key(path) not in linked_pages
    and page_key(path).split("/")[-1] not in RESERVED_STEMS
]
duplicate_stems = sum(
    1 for count in collections.Counter(k.split("/")[-1] for k in page_keys).values() if count > 1
)

print(
    f"pages={len(page_files)} links={len(links)} EMPTY=[[]]:{len(empty)} "
    f"dangling-targets:{len(dangling)} orphan-pages:{len(orphans)} "
    f"duplicate-stems:{duplicate_stems}"
)
for target, count in dangling.most_common(15):
    print(f"  dangling x{count}: [[{target}]]")
if orphans:
    print("  orphans (nothing links to them):", ", ".join(sorted(orphans)[:15]))
print("WIKI LINT " + ("FAIL — empty links carry zero meaning" if empty else "PASS (empties)"))
sys.exit(1 if empty else 0)
