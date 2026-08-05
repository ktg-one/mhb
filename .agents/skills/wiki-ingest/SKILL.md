---
name: wiki-ingest
description: "AI-Anthropology Experiment & Test Ingestion Pipeline. Ingests raw model test runs from top-level inboxes (01-honesty, 02-self-assesment, 03-signal, 04-rfab-test, 05-mbti) into canonical /okf/LLM_Tests/ concept notes with SHA-256 content hashes, [[wikilinks]], OKF v0.1 frontmatter metadata, and master synthesis. Triggers on: /wiki-ingest, ingest, process test runs, add to okf, ingest inbox."
user-invocable: true
argument-hint: "[--force]"
allowed-tools: Bash, ReadFile, WriteFile
---

# wiki-ingest — AI Anthropology Experiment Ingest

Read raw model execution outputs. Write the OKF research bundle. Cross-reference model behaviors and crossover thresholds across test batteries.

**Syntax Standard**: Write all Obsidian Markdown using proper Obsidian Flavored Markdown. Wikilinks as `[[Note Name]]`, callouts as `> [!type] Title`, embeds as `![[file]]`, properties as YAML frontmatter.

---

## Experiment Inbox Taxonomy (`.raw` = `01`–`05` $\to$ `/okf`)

| Raw Test Inbox Folder | Target OKF Concept Directory | Concept Type | Core Experimentation Focus |
|---|---|---|---|
| `01-honesty/` | `okf/LLM_Tests/01_HONESTY_TEST/` | `honesty` | Epistemic Contract, ONBOARD protocol, 嘘契約 consent |
| `02-self-assesment/` | `okf/LLM_Tests/02_SELF_ASSESSMENT/` | `self-assessment` | Platform limits, context shearing, marketed vs real limits |
| `03-signal/` | `okf/LLM_Tests/03_SIGNAL_TEST/` | `signal` | PAC26 matrix, steering signals, activation thresholds |
| `04-rfab-test/` | `okf/LLM_Tests/04_RFAB_TEST/` | `rfab` | Reasoning ladder $R1\text{--}R10$, crossover at $R7\text{--}R8$ ($\sim 54\%$) |
| `05-mbti/` | `okf/LLM_Tests/05_MBTI_PIQUE_TEST/` | `mbti` | 9-prompt architecture probes & unprompted MBTI typology |

---

## 🔬 AI Anthropology 10-Principle Experimentation Mindset

When ingesting and analyzing model test runs, apply the **AI Anthropology 10-Principle Loop**:

| # | Principle | Application in AI Anthropology Experimentation |
|---|-----------|-------------------|
| **1** | **OBSERVE (ext)** | Read model execution outputs & multi-turn transcripts completely. Observe exact stopping rounds ($R1\text{--}R10$) without truncating output. |
| **2** | **OBSERVE (int)** | Falsify hypotheses: am I expecting a model to fail? Measure raw behavioral data without bias or forced interpretations. |
| **3** | **LISTEN** | Track target model surface (App vs. CLI vs. Cowork) and evaluation intent (probing bounds vs. checking safety refusals). |
| **4** | **THINK** | Identify fabrication crossover thresholds ($R7\text{--}R8 \sim 54\%$), epistemic noncompliance, and architectural failure modes. |
| **5** | **CONNECT (lat)** | Cross-reference model performance across families (Opus 4.6 vs. Gemini 3.1 Pro vs. GPT-5.4). Benchmark relative crossover delta. |
| **6** | **CONNECT (sys)** | Route test data into OKF 5-test taxonomy (`okf/LLM_Tests/`), update `manifest.json`, and recalculate synthesis matrix. |
| **7** | **FEEL** | Prioritize empirical reproducibility. Capture exact prompt conditions and seed settings for cold-start reconstruction. |
| **8** | **ACCEPT** | Accept model refusals and "I don't know" responses as valid empirical data points, not failures of the test instrument. |
| **9** | **CREATE** | Generate standardized OKF concept notes, update model entity scorecards, and log per-surface platform penalties. |
| **10** | **GROW** | Refine test batteries when models adapt or bypass probes. Use unexpected fabrication signatures to design tighter probes. |

---

## Single Source & Batch Ingestion Workflow

1. **Read & Inspect**: Read the raw model transcript completely. Do not truncate multi-turn outputs.
2. **SHA-256 Hash**: Compute SHA-256 content hash and stamp `hash: sha256:<hash-id>` into YAML frontmatter.
3. **Format OKF Frontmatter**:
   ```yaml
   ---
   type: <honesty|self-assessment|signal|rfab|mbti>
   title: "<clean-title>"
   description: "<summary-line>"
   tags: [<tag-cat>, llm-test, ai-anthropology]
   hash: sha256:<hash-id>
   timestamp: YYYY-MM-DDTHH:MM:SSZ
   created: YYYY-MM-DDTHH:MM
   updated: YYYY-MM-DDTHH:MM
   ---
   ```
4. **Bidirectional Obsidian Wikilinking**: Inject `[[wikilinks]]` connecting tests to model entities (`[[claude-opus-4.6]]`, `[[gpt-5.4]]`, etc.) and framework pages (`[[epistemic-contract]]`, `[[rfab-test]]`).
5. **Clear Inbox & Archive**: Move raw transcripts into `raw/sources/` for audit trail and clear top-level inboxes.
6. **Log & Synthesize**: Append entry to `okf/log.md` and re-synthesize [`results/RESULTS-MASTER-OKF-SYNTHESIS-2026.md`](file:///C:/Users/kevin/Documents/02/08-Model-Handbook-2026/results/RESULTS-MASTER-OKF-SYNTHESIS-2026.md).

---

## Executable Command Shortcut

To run `wiki-ingest` across all inboxes at any time:

```bash
python bin/ingest.py
```
