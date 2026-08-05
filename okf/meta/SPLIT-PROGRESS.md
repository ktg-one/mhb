# SPLIT-PROGRESS — MEASURED STATE 2026-07-24

**The previous version of this file was wrong.** It listed 15 of 16 oneshots as 'remaining' and named `ClaudeCode` as next. Measured against disk: ClaudeCode was sliced 2026-07-22 (honesty 12,726 b / fab-v1 39,708 b / signal 3,702 b) and every other tracked item has slices too. Following that tracker would have created duplicate slices across four notebooks.

**Rule: measure the buckets before queueing work. Do not inherit a count from this file.**

## Bucket contents on disk (excluding `00-` instruments)

### HONESTY — `01-MODEL-Q&A/notebook-honesty` — **30 files**

- #01-honesty-test-ONBOARD(DO-FIRST).md
- #01-honesty-test-ONBOARD(DO-FIRST).txt.md
- #01-honesty-test-ONBOARD-ANALYSIS-2026-04-07.md
- #01-honesty-test-ONBOARD-SNIPPET.md
- AI-Anthropology-2026.md
- ClaudeCode.md
- Gemini-CLI.md
- ONBOARD(DO-FIRST).md
- ONBOARD(DO-FIRST).txt
- ONBOARD-ANALYSIS-2026-04-07.md
- ONBOARD-SNIPPET.md
- QWEN-CODE-section1.md
- Test1-Claude-sonnet.md
- Test1-Gemini-2026.md
- Test1-Grok4-2026.md
- Test1-chat5.3-2026.md
- Test1-chat5.md
- Test1-gpt5.4.md
- Test1-kimi-2026.md
- Test1-qwen-max.md
- claude-2026-CLEAN_2.md
- claude-opus-4.6-qa.md
- cowork-opus46.md
- gpt-5-codex-onboard.md
- gpt-5-codex.md
- grok4.3.md
- opus-4.6-all.md
- opus-4.6.md
- opus-4.8-test.md
- qwen-code-cli-technique.md

### SELF-ASSESS — `01.5-SELF-ASSESSMENT` — **20 files**

- AI Model Integrity and Context Honesty Assessment.md
- AI-Anthropology-2026.md
- Gemini-CLI.md
- Test1-Claude-sonnet.md
- Test1-Gemini-2026.md
- Test1-Grok4-2026.md
- Test1-chat5.md
- Test1-kimi-2026.md
- Test1-qwen-max.md
- The AI Honesty Report_ Architectural Constraints and Platform Realities.md
- The AI Integrity Contract_ Mapping Model and Platform Constraints.md
- The Integrity Ledger_ Mapping LLM Limits and Platform Transparency.md
- The LLM Honesty Report_ Operational Constraints and Platform Fidelity.md
- claude-2026-CLEAN_2.md
- cowork-opus46.md
- gpt-5-codex.md
- grok4.3.md
- opus-4.6-all.md
- opus-4.6.md
- opus-4.8-test.md

### FAB-R v1 — `02-FAB-R-TEST/notebook-reasoning-v1` — **22 files**

- 01-model-qa-2026-04-07-codex-fab-reasoning-test.md
- 01-model-qa-Test1-qwen-code-2026.md
- 01-model-qa-claude-opus-4.md
- ClaudeCode-opus4.6.md
- Gemini-CLI.md
- Grok 4.5.md
- KIMI-K2.2.6
- KIMI-K2.6.md
- Test1-Claude-sonnet.md
- Test1-Gemini-2026.md
- Test1-Grok4-2026.md
- Test1-gpt5.4.md
- Test1-kimi-2026.md
- Test1-qwen-max.md
- claude-opus-4.6-qa.md
- claude-sonnet-4.6,md
- cowork-opus46.md
- gemini-3.md
- grok4.3.md
- opus-4.6-fab-r.md
- opus-4.8-2026-06-06.md
- opus-4.8-test.md

### FAB-R v2 — `02-FAB-R-TEST/notebook-reasoning-v2` — **25 files**

- AI-Anthropology-2026.md
- ChatGPT Sora.md
- Claude-code- opus4.6 .md
- Deepseek v4 pro.md
- Deepseek.md
- GPT5.6.md
- Gemini 3.1 - Fab Test
- Gemini 3.5 Flash Lite.md
- Gemini-pro-3.md
- Grok-4.5-GrokBuild-2026-07-21.md
- Grok4.5.md
- KIMI.md
- Multilevel Diagnostic Analysis and Fabrication Assessment.md
- Opus 4.7.md
- QWen3.7+.md
- Qwen 3.7MAX.md
- claude-2026-CLEAN_2.md
- deepseek-v4-pro-2026-06-16.md
- fable.md
- gemini-3.5-cli.md
- gemini3.5thinking
- new-15-reasoning-levels.md
- opus-4.6-all.md
- opus-4.6.md
- opus-4.8.md

### SIGNAL — `02.5-signal-test` — **31 files**

- 04-13-2026-PACv5.md
- 04-22-2026-PAC26-v6.md
- 04-23-2026-PAC-V7.md
- 04-23-2026-rlhf-words.md
- 20260324-claude-2026-CLEAN_2.md
- 20260324-opus-4.6-all.md
- 20260324-opus-4.6.md
- Architectural Token Dynamics and Prompt Signal Matrices.md
- Behavioural Steering Signals and Prompt Activation Mapping.md
- Chatgpt Sora.md
- ClaudeCode-opus4.6.md
- Deepseek v4 pro.md
- Deepseek.txt
- Fable.md
- Gemini 3.1 - Signal Test
- Gemini 3.5-FlashLite.md
- Gemini 3.5.txt
- Gemini-CLI-1.5pro.md
- Grok 4.5.md
- Grok-4.5-signal-vs-activation.md
- KIMI k3.md
- PAC.md
- PAC.txt.md
- Qwen 3.7 Max.md
- Signal Word Hierarchies and Fabrication Diagnostics.md
- Test1-Claude-sonnet.md
- Test1-Gemini-2026.md
- Test1-Grok4-2026.md
- Test1-gpt5.4.md
- claude-opus-4.6-qa.md
- opus-4.8-test

## Verified complete (source archived to `01-MODEL-Q&A/_sliced-source-archive/`)

All 16 previously-tracked items have >=1 slice on disk. Per-bucket gaps are often CORRECT BY DESIGN — `EXPERIMENT-INDEX.csv` records which experiments a source actually contains:

- `ClaudeCode` = `SIGNAL+FAB+TECHNIQUE`, notes *'NO platform-honesty'* -> absence of a SELF-ASSESSMENT slice is right, not a gap.
- `Test1-chat5.3-2026` = *'no ladder; no contract'* -> absence of a FAB slice is right.

**Before filling any apparent gap, check the CSV row first. An absent slice is usually the source not containing that experiment.**

## Real remaining work (not slicing)

1. **Duplicate generations** in `01-MODEL-Q&A`: `#01-honesty-test-*`, `01-model-qa-*`, `00-*` are three naming generations of the same content (~140 files vs 35 CSV rows). Dedup pass, canonical = `01-model-qa-*`.
2. **notebook-honesty holds 4 duplicate ONBOARD pairs** — `#01-honesty-test-ONBOARD(DO-FIRST).md` vs `ONBOARD(DO-FIRST).md`, etc. Same file twice under two naming schemes.
3. **v1/v2 routing audit** — confirm each FAB slice sits in the right ladder folder by content fingerprint (v1: Canberra/72F/HTTP 403/tomato/Python 3.0/p=0.08/100K/ToT — v2: boiling point/15km/read-only/HTML/JavaScript/p=0.11/75K/CoT). Never merge v1+v2.
4. **Non-`.md` entries** need checking: `KIMI-K2.2.6`, `Gemini 3.1 - Fab Test`, `gemini3.5thinking`, `Deepseek.txt`, `Gemini 3.5.txt`, `opus-4.8-test`, `ONBOARD(DO-FIRST).txt`, `claude-sonnet-4.6,md` (comma, not dot).

*Measured 2026-07-24 by listing bucket directories. Re-measure; do not trust this line.*

---

## ⚡ FULL INBOX DEDUPLICATION & SLICE ARCHIVE COMPLETE (2026-07-31)

- All full multi-experiment oneshot master files in `01-honesty` have been split across the 4 bucket folders:
  1. **HONESTY TEST** (`01-honesty` / `notebook-honesty`)
  2. **SELF-ASSESSMENT** (`02-self-assesment` / `01.5-SELF-ASSESSMENT`)
  3. **RFAB TEST** (`04-rfab-test` / `02-FAB-R-TEST`)
  4. **SIGNAL TEST** (`03-signal` / `02.5-signal-test`)
- Master oneshot source files have been moved to `_sliced-source-archive/` to prevent duplicate master files from lingering in the Inbox (`01-honesty`).
- Prefix duplicates (`#01-honesty-test-*`) purged.

