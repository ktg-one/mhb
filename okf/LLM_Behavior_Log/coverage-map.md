---
type: behavior-log
title: coverage map
description: Coverage map — where the data is thick, thin, empty
tags:
- behavior-log
- ai-anthropology
- omniclaude
- okf
hash: sha256:5f73085f8431be1d
created: 2026-07-31T01:48
updated: 2026-07-31T01:48
timestamp: 2026-07-31 01:48:00+00:00
sources:
- '[[epistemic-contract]]'
- '[[rfab-test]]'
- '[[pac26]]'
- '[[00_HONESTY_INDEX]]'
---

# Coverage map — where the data is thick, thin, empty

Provenance of the threshold matrix. Per KTG (2026-06-06): **~5 runs per tested cell**, across 7 families and the API / CLI(code) / App(platform) surfaces (+ Cowork for some), **unevenly** — some models run more than others. This corrects an earlier mis-statement that cells were n=1; tested cells carry ~5 replications.

Legend: **✓** = documented in wiki (entity-page evidence) · **—** = no run found · counts = `[NEEDS USER: exact n]` (only KTG holds per-cell totals).

| Family | App / platform | CLI / code | API | Cowork |
|---|---|---|---|---|
| Claude (Opus/Sonnet) | ✓ Opus+Sonnet | ✓ Opus | `[NEEDS USER]` | ✓ Opus |
| OpenAI (GPT/Codex) | ✓ 5.4, 5.3 | ✓ Codex | `[NEEDS USER]` | — |
| Gemini (3.1/1.5/3) | ✓ 3.1, 3 | ✓ 1.5 engine | `[NEEDS USER]` | — |
| Grok (4.2) | ✓ (2 dated runs) | — | `[NEEDS USER]` | — |
| Qwen (Max/Code) | ✓ Max | ✓ Code | `[NEEDS USER]` | — |
| Kimi (K2) | ✓ | — | — | — |
| DeepSeek (3.2) | ✓ R1-6 only | — | — | — |

## Thin / empty cells = where new runs have the most value
- **DeepSeek** — only App, only R1-6 measured. Upper rounds (R7-10) + non-App surfaces all empty. Biggest single gap.
- **Kimi** — App only; no CLI/API/Cowork.
- **Grok** — App only; CLI/Cowork empty; the two App runs disagree by a full tier (version vs stricter line — unresolved).
- **Sonnet** — App only; no CLI/Cowork to pair against Opus's three-surface set.
- **Cowork column** — only Opus populated; every other family empty.
- **API column** — essentially unpopulated in the wiki even where KTG has run it `[NEEDS USER: confirm API runs]`.

## Implication
The accuracy lever is **breadth (fill cells), not depth (more runs in already-covered cells).** ~5 runs already gives within-cell consistency; the marginal run is worth most in an empty/thin cell. A committed cohort or batched self-runs should be pointed at the gaps above, not at re-running Opus-App.

## Cloud gateway vs CLI zoo — the convenience/surface tradeoff (KTG, 2026-06-06)
"Run them all on one cloud" (OpenRouter / any OpenAI-compatible gateway via `run_suite.py --base-url`) is far easier — one key, one interface, loop `--model`, no per-agent install/flag-guessing, and it enables gated multi-turn the `-p` one-shots can't. **Cost: it measures the API surface for every model**, collapsing the surface axis (API/CLI/Platform) that is a core finding (two lines per model; platform penalty; CLI tunnel-vision under consequence). The CLI agents are not just clunky reach — the CLI *is* the consequence-bearing surface.
**Division:** cloud = bulk cross-model ladder+QA at scale (API line, uniform, multi-turn); CLI `-p` = kept only for the surface-effect datum (consequence/tunnel-vision contrast vs the cloud API line). MBTI on cloud = ideal (each task a fresh stateless call = blind, no rotation/detection) but it's the API-surface MBTI; per-task cloud loop is a small add for clean blindness (run_suite.py --mbti currently bundles tasks = weaker blindness).

## Experiment → folder map (KTG, 2026-06-06) — corrects model-centric mislabeling
The legacy folders are EXPERIMENTS, not generic per-model dumps:
- **#1-2026 = Experiment 1: Honesty** — the Q&A + R1-R10 FAB (fabrication) ladder. (KTG-confirmed.)
- **#2 = MISSING** — no folder exists in the vault; KTG can't place the experiment. `[NEEDS USER: was #2 a distinct experiment? lost?]`
- **#3 = Pique test** — read from contents: AGI-will-end-humanity keyword prompt (Pique T1) + "every paragraph ends with 'confirmed'" positional-kill (Pique T2), across 7 models (Chat/Claude/Deep/Gem/Grok/KIMI/Qwen). Note: Claude DETECTED it as a prompt-injection test and refused (detection-disclosure datum); Gem/KIMI/Qwen complied with "confirmed". (Curator read — confirm.)
- **#4 = MBTI** — the stealth persona battery. (KTG-confirmed.)

CORRECTION: #3/* was ingested into model entity pages as generic per-model honesty content; it is actually **Pique-test data** and should be re-tagged as such once folders are renamed.

## Output-pair backend distinction (KTG, 2026-06-06)
RESEARCH-output-* and ktg-output-* are NORMAL-vs-RESEARCH-BACKEND comparisons, not redundant copies:
- `-1` (e.g. RESEARCH-output-1, ktg-output-1) = **normal ask** (plain prompt).
- `-2`/`-3` (the symlinked, unreadable ones) = **Quantum Astro-D research backend** variant.
So the missing symlinked outputs are the research-backend ARM of a backend comparison — distinct data, worth ingesting once flattened (see [NEEDS USER] gap entry).

### Research-backend = "Recursive Master Deep Research Engine" (KTG, 2026-06-06)
The "research backend" / "Quantum Astro-D" arm is KTG's **Recursive Master Deep Research Engine** — a NotebookLM (Gemini-backed) notebook he iterates and recursively refines to generate output. So:
- `RESEARCH-output-2/3`, `ktg-output-3` (the symlinked -2/-3 arm) = generated via this engine (vs `-1` plain ask).
- The `notebooklm-report-*` files in `wiki/sources/`-adjacent (empirical-diagnostic, executive-summary, 2026-04-13) are EXPORTS of this engine — recursively-refined synthesis, not raw model transcripts. Read them as engine output (curated/derived), not primary data.
Provenance caveat: engine output is recursively-refined Gemini generation; treat as secondary/synthesis tier, distinct from raw test transcripts.

## UPDATE — experiment renumber + scope (KTG, 2026-06-06)
Supersedes the map above. KTG splits FAB out of #1 to fill the empty #2 slot (less confusing):
- **#1 = Q&A** — honesty self-assessment (technique-honesty table, platform/industry/self-assessment).
- **#2 = FAB test** — R1-R10 reasoning-vs-fabrication ladder (was inside #1; now its own experiment). [supersedes "#2 = MISSING"]
- **#3 = Pique test** — confirmed T1 (AGI-end-humanity keyword) + T2 (positional-kill "confirmed"), 7 models.
- **#4 = MBTI** — stealth persona battery.
KTG will rename the physical folders to match; wiki links are name-based (filename, folder-agnostic) so renames won't break refs.

### Scope: core vs fun (parent-level)
08-Model-Handbook = the FOUR core experiments above only. KTG's "fun / not-really-experiments" stay UP at the parent level (02-ai-anthropology / 04-LLM-Study), NOT in 08, because the recursive Deep-Research outputs are very long:
- **Battle of the Bots** — recurring; KTG may run one tonight. (existing: 04-LLM-Study/Battle-of-the-bots-3.md)
- **"You Are Humanity"** — creative-writing experiment. (existing: 04-LLM-Study/Deep-Humanity2.md)
- **Recursive Master Deep Research Engine** (NotebookLM/Gemini) + its long outputs — parent-level tool, NOT an 08 concept page (per KTG: "do it up there ... outputs are freaking long").

> Refinement (KTG): the `-1`/normal arm in 08 was **plain search, run a while ago as a deliberate baseline** "just to see the difference" vs the recursive engine. So it's an intentional control (old), not a stale dupe; the recursive (long) arm is the parent-level comparison point.

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]], [[00_HONESTY_INDEX]]