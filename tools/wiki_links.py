#!/usr/bin/env python3
"""Shared Obsidian-style wikilink resolution for vault tools.

Single source of truth for how a wikilink target resolves to a page, used by
``lint_wiki.py`` and ``verify-ingest.py`` so the semantics cannot diverge.

Resolution semantics (Obsidian):
  1. an exact wiki-relative path match wins;
  2. otherwise a path-qualified link suffix-matches the tail of a page path
     (deterministic pick: shallowest path, then alphabetical);
  3. a bare link matches by stem (same deterministic pick).

Scalability: ``LinkResolver`` precomputes exact-match and path-suffix indexes
once at construction, so resolving N links is O(N) index lookups instead of
O(N x pages) full scans.
"""

import collections
import os
import re


def norm(value):
    """Lowercase, collapse whitespace/underscores/dashes to single dashes."""
    return re.sub(r"[\s_-]+", "-", value.lower())


def lower_only(value):
    """Lowercase-only normalization (verify-ingest's historical key space)."""
    return value.lower()


def _strip_md(name):
    """Strip only a trailing .md extension (a note named ``opus-4.6.md`` has
    stem ``opus-4.6`` — splitext would wrongly eat the ``.6``)."""
    return name[:-3] if name.lower().endswith(".md") else name


def target_keys(target, norm_fn=norm):
    """Normalized key variants for a raw wikilink target.

    Includes the full cleaned path, the path without a ``.md`` extension, the
    basename, and the basename stem, so links that carry (or omit) ``.md``
    both match.
    """
    clean = target.strip().replace("\\", "/").lstrip("./")
    basename = os.path.basename(clean)
    return {norm_fn(clean), norm_fn(_strip_md(clean)),
            norm_fn(basename), norm_fn(_strip_md(basename))}


def target_stem(target, norm_fn=norm):
    """Normalized basename stem of a raw wikilink target."""
    return norm_fn(_strip_md(os.path.basename(target.strip().replace("\\", "/"))))


class LinkResolver:
    """Precomputed index resolving wikilink targets to normalized page keys.

    ``page_keys`` must be normalized wiki-relative page paths (forward slashes,
    lowercase, no extension) — the same form wikilink targets are written in.
    ``norm_fn`` must be the same normalization used to produce those keys.
    """

    def __init__(self, page_keys, norm_fn=norm):
        self._norm_fn = norm_fn
        self._exact = set(page_keys)
        self._by_stem = collections.defaultdict(list)
        # suffix index: every tail segment of every page key -> full keys,
        # so a path-qualified link resolves with one dict lookup per candidate.
        self._by_suffix = collections.defaultdict(list)
        for key in page_keys:
            self._by_stem[key.split("/")[-1]].append(key)
            parts = key.split("/")
            for i in range(1, len(parts)):
                self._by_suffix["/".join(parts[i:])].append(key)
        for candidates in self._by_stem.values():
            candidates.sort(key=lambda k: (k.count("/"), k))
        for candidates in self._by_suffix.values():
            candidates.sort(key=lambda k: (k.count("/"), k))

    def resolve(self, target, stem_fallback_for_paths=True):
        """Resolve a raw wikilink target to a page key, or ``None``.

        With ``stem_fallback_for_paths=False``, a path-qualified target that
        matches nothing returns ``None`` instead of falling back to a bare-stem
        match (verify-ingest semantics: a path-qualified link names exactly one
        intended page).
        """
        keys = target_keys(target, self._norm_fn)
        path_qualified = sorted(k for k in keys if "/" in k)
        for key in path_qualified:
            if key in self._exact:
                return key
        for key in path_qualified:
            matches = self._by_suffix.get(key)
            if matches:
                return matches[0]
        if path_qualified and not stem_fallback_for_paths:
            return None
        candidates = self._by_stem.get(target_stem(target, self._norm_fn))
        return candidates[0] if candidates else None
