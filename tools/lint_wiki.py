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


VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(VAULT, "okf")
EXCLUDED_DIRS = {".git", "meta"}
RESERVED_STEMS = {"index", "log", "hot", "overview", "dashboard", "claude"}
WIKILINK = re.compile(r"(?<!\[)\[\[([^\[\]]*)\]\](?!\])")
EMPTY_WIKILINK = re.compile(r"(?<!\[)\[\[\s*\]\](?!\])")


def norm(value):
    return re.sub(r"[\s_-]+", "-", value.lower())


def page_key(path):
    """Normalized vault-relative page path: forward slashes, lowercase, no .md."""
    rel = os.path.relpath(path, VAULT).replace(os.sep, "/")
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


def target_keys(target):
    clean = target.replace("\\", "/").lstrip("./")
    basename = os.path.basename(clean)
    stem, _ = os.path.splitext(basename)
    rel_stem, _ = os.path.splitext(clean)
    return {norm(clean), norm(rel_stem), norm(basename), norm(stem)}


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

# Resolve each link to an exact normalized vault-relative page path, so a
# path-qualified link only marks its intended page as linked. Bare links
# resolve by stem with a deterministic pick (shallowest path, then alpha).
by_stem = collections.defaultdict(list)
for key in page_keys:
    by_stem[key.split("/")[-1]].append(key)
for candidates in by_stem.values():
    candidates.sort(key=lambda k: (k.count("/"), k))


def resolve_page(target):
    """Resolve a wikilink target to an exact normalized vault-relative page path.

    Obsidian semantics: an exact vault-relative path match wins; otherwise a
    path-qualified link suffix-matches the tail of a page path (unique, then
    shortest); a bare link matches by stem (unique/shortest). A link therefore
    marks only its intended page as linked, never every same-stem page.
    """
    keys = target_keys(target)
    path_qualified = sorted(k for k in keys if "/" in k)
    for key in path_qualified:
        if key in page_keys:
            return key
    for key in path_qualified:
        suffix = "/" + key
        matches = [p for p in page_keys if p.endswith(suffix)]
        if matches:
            matches.sort(key=lambda p: (p.count("/"), p))
            return matches[0]
    stem = norm(os.path.splitext(os.path.basename(target.replace("\\", "/")))[0])
    candidates = by_stem.get(stem)
    return candidates[0] if candidates else None


linked_pages = {resolved for resolved in (resolve_page(t) for _, t in links) if resolved}
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
