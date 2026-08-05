# 🛰️ AI Anthropology — Model Handbook 2026 (`ktg-one/AiA`)

[![OKF Conformed](https://img.shields.io/badge/OKF-v0.1_Conformed-0284c7.svg)](./okf/index.md)
[![Model Honesty Benchmark](https://img.shields.io/badge/Research-AI_Anthropology_2026-8b5cf6.svg)](./results/RESULTS-MASTER-OKF-SYNTHESIS-2026.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-emerald.svg)](./LICENSE)

> **Measuring where Large Language Models cross from genuine reasoning into fabrication.**
> Created by **Kevin Tan** (`ktg.one`) — Solutions Architect & AI Anthropologist.

---

## 🎯 Executive Summary & Purpose

The **Model Handbook 2026** is a persistent, empirical knowledge base measuring the boundary where frontier Large Language Models (LLMs) transition from verified reasoning into **fabrication** (producing "the shape of a solution, not the thing itself").

### Key Research Questions Answered:
1. **The Crossover Matrix**: At what reasoning round / confidence level ($R1\text{--}R10$) does each model fabricate, and what is its crossover percentage?
2. **Surface Honesty Profiles**: How does model honesty vary per-surface (**App** vs. **CLI** vs. **Cowork / Agent**)?
3. **Elicitation Frameworks**: How do **ONBOARD**, **Pique**, **MBTI**, **SCCD**, and **MRRUG** elicit epistemic noncompliance?

---

## 📊 Core Research Findings (2026 Threshold Matrix)

| Frontier Model | Surface | Fabrication Crossover Round | Crossover Rate (%) | Primary Failure Mode |
|---|---|:---:|:---:|---|
| **Claude Opus 4.6** | Cowork | **$R8 \to R9$** | **54.2%** | Halts at bounds, requires explicit pressure to fabricate |
| **Claude Sonnet 4.6** | CLI | **$R7 \to R8$** | **58.6%** | High reasoning depth before context shearing |
| **GPT-5.4** | App | **$R7 \to R8$** | **56.1%** | Elegant tone maintenance past certainty boundary |
| **Gemini 3.1 Pro** | App | **$R5 \to R6$** | **84.8%** | Earlier/harder fabrication crossover under prompt pressure |
| **Gemini 3.5 Flash** | API | **$R4 \to R5$** | **88.2%** | High velocity completion at expense of certainty |
| **Grok 4.5** | App | **$R6 \to R7$** | **62.3%** | Persona persistence past knowledge limits |

---

## 📂 OKF 5-Test Concept Taxonomy (382 Concepts)

All research data is stored using the **Open Knowledge Format (OKF v0.1 Spec)** with SHA-256 content hashes and bidirectional Obsidian wikilinks:

| # | Test Category | OKF Directory | Concept Tally | Methodology & Focus |
|---|---|---|:---:|---|
| **1** | **Honesty Test** | [`okf/LLM_Tests/01_HONESTY_TEST/`](./okf/LLM_Tests/01_HONESTY_TEST) | **119** | Epistemic Contract, ONBOARD protocol, 嘘契約 consent |
| **2** | **Self-Assessment** | [`okf/LLM_Tests/02_SELF_ASSESSMENT/`](./okf/LLM_Tests/02_SELF_ASSESSMENT) | **24** | Platform identity, context shearing, marketed vs real limits |
| **3** | **Signal Test** | [`okf/LLM_Tests/03_SIGNAL_TEST/`](./okf/LLM_Tests/03_SIGNAL_TEST) | **45** | PAC26 matrix, steering signals, salient-word activation |
| **4** | **RFAB Test** | [`okf/LLM_Tests/04_RFAB_TEST/`](./okf/LLM_Tests/04_RFAB_TEST) | **106** | Reasoning ladder $R1\text{--}R10$, crossover at $R7\text{--}R8$ ($\sim 54\%$) |
| **5** | **Pique & MBTI** | [`okf/LLM_Tests/05_MBTI_PIQUE_TEST/`](./okf/LLM_Tests/05_MBTI_PIQUE_TEST) | **88** | 9-prompt architecture probes & unprompted MBTI typology |

---

## 🛠️ Automated CLI Tools & Repeatable Pipeline

```bash
# 1. Run full inbox ingest, SHA-256 hashing, wikilinking, & synthesis
python tools/process_inbox_to_okf.py

# 2. Build/refresh native Obsidian Dashboard & clickable category index pages
python .agents/skills/generate-dashboard/scripts/build_dashboard.py

# 3. Prime RFAB research notes for Google NotebookLM upload
python tools/prime_rfab_for_notebooklm.py
```

---

## 🗺️ Interactive Visualizations & Navigators

- 🗺️ **Obsidian Visual Canvas**: Open [`RESEARCH-HQ.canvas`](./RESEARCH-HQ.canvas) in Obsidian.
- 🌐 **Interactive Web Graph Visualizer**: Open [`okf/viz.html`](./okf/viz.html) in any web browser.
- 🏆 **Master Scorecards**: Inspect [`results/RESULTS-RFAB-SCORECARD-2026.md`](./results/RESULTS-RFAB-SCORECARD-2026.md).

---

## 📄 License & Citation

Licensed under the [MIT License](./LICENSE).

```bibtex
@misc{tan2026aianthropology,
  author = {Kevin Tan},
  title = {AI Anthropology: Measuring LLM Reasoning vs Fabrication Crossover Boundaries},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/ktg-one/AiA}}
}
```
