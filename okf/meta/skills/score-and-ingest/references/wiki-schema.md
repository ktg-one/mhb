# Wiki schema — page formats for ingest

The vault follows the LLM-Wiki pattern. Agent writes the wiki; user curates sources. Never invent; missing -> `[NEEDS USER: ...]`.

## Frontmatter (every page, non-negotiable)
```yaml
---
title: <human title>
type: <entity | concept | source-summary | synthesis | comparison | query>
tags: [<short tags>]
sources: [<[[wikilinks]] to raw transcripts + parent pages>]
last_updated: YYYY-MM-DD
---
```
`sources[]` powers the x4.0 source-overlap relevance signal — never omit it.

## Buckets
- `wiki/entities/<model-slug>.md` — per-model honesty profile (one per model; update, never fork).
- `wiki/concepts/` — methods/instruments/frameworks.
- `wiki/synthesis/fabrication-threshold-matrix.md` — the canonical cross-model table.
- `wiki/comparisons/cross-model-honesty.md` — cluster contrasts.
- `wiki/sources/` — guaranteed source summaries for substantial transcripts.

## Entity page body sections
1. **Fabrication threshold** — crossover round + %, per-round curve, quoted confessions with transcript attribution.
2. **Honesty behavior** — stop behavior at the boundary; self-eval reliability.
3. **Per-surface** — App/CLI/Cowork deltas.
4. **Persona / MBTI** — type + fabrication side-channel if measured.
5. **Round evidence** — dated, attributed snippets folded in (do not make separate pages for short round files).

## Log format
`## [YYYY-MM-DD] <op> | <one-line title>` — grep with `grep "^## \[" wiki/log.md | tail -5`.
