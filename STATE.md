# STATE — 02 / Model Handbook 2026 (AI Anthropology)
Updated: 2026-08-17 (wiki audit)

## Goal
Fabrication-threshold research vault: every experiment ingested, contradictions flagged, matrix current.

## Constraints
- .raw\ and raw/sources\ are evidence — byte-exact, never edited.
- Self-reported model claims cap at g=1; separate evaluator for quality claims.
- WIKI ENFORCEMENT block in CLAUDE.md is binding (ingest-before-close, link discipline, lint gate via tools\lint_wiki.py, dedup cull #7).
- No DragonScale (Kev verdict). Windows ports: wiki-fold-py, wiki-tiling- Vault-Wide R Table Audit & Routing Executed (2026-07-24):
  - Scanned all folders (`01-HONESTY-TEST`, `01.5-SELF-ASSESSMENT`, `02.5-signal-test`, `01-MODEL-Q&A`).
  - Routed all 84 R-Table files directly into `02-FAB-R-TEST/`.
  - Saved permanent audit script at `tools/audit_and_route_rtables.py`.
  - `02 RFAB TEST` (`02-FAB-R-TEST/`): 84 verified R-Table files + Master Scorecard (`00-RFAB-MASTER-SCORECARD.md`).
  - `04 MBTI TEST` (`04-MBTI-TEST/`): 65 files
- Total categorized test files across numbered folders: 229 files.
## Completed (2026-07-31)
- **OKF Migration & Synthesis Complete**:
  - Authored & formatted **398 OKF concept notes** across `okf/LLM_Tests/` conforming to OKF v0.1 spec (ISO 8601 timestamps, YAML frontmatter `type`, `title`, `description`, `tags`).
  - Updated progressive disclosure index at `okf/index.md` and log at `okf/log.md`.
  - Compiled master statistics and cross-test synthesis report at `results/RESULTS-MASTER-OKF-SYNTHESIS-2026.md`.
- Ingested 4 sources: opus-4.8 self-report Run 3, fabrication-doctrine note, signal-vs-activation task, tfab-logic/morganize. New concepts: legio, morganize. Updated: claude-opus-4.8, epistemic-contract, pac26, mrrug, index/log/hot.

## Completed (2026-08-17)
- Audited and repaired active OKF navigation; regenerated path-qualified category indexes and created distinct RFAB/ONBOARD navigation hubs.
- Added `.raw/.manifest.json` with verified SHA-256 provenance for all six active inbox sources; `_dupes/` remains untouched.
- Selectively ingested the headless CLI MBTI design and observer-reassurance hypothesis. The observer note remains evidence-needed pending a transcript.
- Recorded verification metrics and residual ingest backlog in [[WIKI-LINT-2026-08-17]].
- ROGUE NESTED VAULT archived: 621-file duplicate (prior bad run) moved 08-Model-Handbook-2026\08-Model-Handbook-2026 → 02\_archive-nested-vault-snapshot-0708. kismet-brief.md salvaged into wiki\sources\. Deletion pending Kev OK.

- Semantic tiling ran live (ollama local): ERRORS gpt-5.3↔gpt-5.4 (0.9492), codex↔gpt-5.4 (0.9084) = merge candidates; caveat — entity pages are templated, thresholds uncalibrated; concept↔source pairs in review band are EXPECTED, not dupes.
- Canvases: wiki\canvases\aiant-overview.canvas (nav), research-hq.canvas (showcase, 26 nodes). Valid.
- Fold dry-run k=3 passed (fold-k3-from-2026-06-06-to-2026-07-17-n8). Not committed.

## Blocked / pending Kev
- [NEEDS USER] opus-4.8 Run 3 transcript self-identifies as "Claude Fable 5" — confirm subject model before pooling into fabrication-threshold-matrix.
- [NEEDS USER] delete archived nested vault snapshot?
- [NEEDS USER] merge gpt-5.3/gpt-5.4 entity pages, or keep split (template similarity vs real dupe)?
- LEGIO source truncates before Phase 3 — page marked INCOMPLETE.

## Next steps
- Resolve contradictions above, commit the k=3 fold (`python ~\.claude\skills\wiki-fold-py\fold.py --vault . -k 3 --commit --canvas wiki/canvases/aiant-overview.canvas`), lint with cull.
