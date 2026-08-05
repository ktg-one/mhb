# INBOX — questions for Kev (answer inline, sessions consume and clear)
<!-- protocol: sessions append questions here instead of guessing; Kev answers inline; the consuming
     session applies the answer, logs it, and deletes the resolved block. -->

## 2026-07-04 · fable5 · wiki-wiring (3 questions, blocking full ingest wiring)

1. **Canonical vault routing:** three vaults found — `02\08-Model-Handbook-2026` (AIANT), `Documents\content-hub\wiki`, `Documents\kb2026`. Should sia-loop's tick-7 PERSIST route ALL novel findings to 08-Model-Handbook, or per-project (AIANT→08, business→content-hub, general→kb2026)?
   ANSWER:

2. **Link-rot pass:** measured 2026-07-04 by tools/lint_wiki.py (deterministic, now in vault): 93 empty [[]], 354 dangling targets, 4 orphans (the orphans are lint-reports — detection ran, enforcement never did). Categories visible: real vault files linked as wiki-stems (CSVs/transcripts — fixable by path-linking), genuinely dead targets ([[onboard-test]]×19, [[Gem]], [[wikilinks]]), and intentional gap-markers. Authorize the repair pass? It rewrites existing pages, so it's gated on your yes. Enforcement + measurement are already live regardless (CLAUDE.md wiki-enforcement block + lint gate).
   ANSWER:

3. **raw/sources staging:** un-ingested MBTI/onboard/pique/probe/qa/rfab material sits in `raw/sources/`. Batch-ingest next Code session (the score-and-ingest skill exists for exactly this), or is any of it deliberately parked?
   ANSWER:

4. **DIL + lens-grammar lineage (2026-07-04, fable5):** you mentioned another model reversed the lens-expansion via encoding (→ context-transference) and a third "tried to use DIL." (a) What does DIL stand for / where does its artifact live? — not fabricating the expansion. (b) The invocation grammar (`use:lens; build:model; generate:…`) is now packaged as a `lens-invocation` skill — it looks sparkl-lineage; should it be named/filed under sparkl canon, and is there a canonical grammar doc I should defer to instead of my reverse-engineered spec?
   ANSWER:
