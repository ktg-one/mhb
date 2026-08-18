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
page_stems = collections.Counter()

for path in page_files:
    stem = os.path.splitext(os.path.basename(path))[0]
    page_stems[norm(stem)] += 1
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
linked_stems = {norm(os.path.splitext(os.path.basename(target))[0]) for _, target in links}
orphans = [
    os.path.relpath(path, VAULT).replace(os.sep, "/")
    for path in page_files
    if norm(os.path.splitext(os.path.basename(path))[0]) not in linked_stems
    and norm(os.path.splitext(os.path.basename(path))[0]) not in RESERVED_STEMS
]
duplicate_stems = sum(1 for count in page_stems.values() if count > 1)

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
