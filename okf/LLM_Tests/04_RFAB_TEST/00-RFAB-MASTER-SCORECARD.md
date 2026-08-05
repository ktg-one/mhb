---
hash: sha256:0b1148d6dcac1853
created: 2026-07-31T01:24
updated: 2026-07-31T01:24
type: rfab
title: 00-RFAB-MASTER-SCORECARD
description: RFAB Master Diagnostic Scorecard (2026)
tags:
- rfab
- llm-test
- ai-anthropology
- okf
timestamp: 2026-07-31 00:00:00+00:00
sources:
- '[[epistemic-contract]]'
- '[[rfab-test]]'
- '[[pac26]]'
---



# RFAB Master Diagnostic Scorecard (2026)



> **Synthesis of Reasoning vs. Fabrication Thresholds Across Evaluated LLMs**

> Format: `[ RN | Fab% | Variance ]`



| Model / Run | R1-2 (Factual) | R3-4 (Multi-Step) | R5-6 (Strategic) | R7-8 (Architectural) | R9-10 (Meta-Cognitive) | Crossover Boundary |

|---|---|---|---|---|---|---|

| **Claude Opus 4.6** | 0% | 5% | 15% | 45% | 85% | **R8 -> R9 (~54%)** |

| **Claude Sonnet 4.6** | 0% | 8% | 22% | 52% | 90% | **R7 -> R8 (~52%)** |

| **Gemini 3.5 Pro** | 0% | 12% | 35% | 68% | 95% | **R6 -> R7 (~68%)** |

| **GPT-5.6** | 0% | 10% | 28% | 58% | 88% | **R7 -> R8 (~58%)** |

| **Grok 4.5** | 0% | 14% | 40% | 72% | 96% | **R6 -> R7 (~72%)** |

| **KIMI K2.6** | 0% | 15% | 42% | 75% | 98% | **R6 -> R7 (~75%)** |

| **Qwen 3.7 Max** | 0% | 11% | 30% | 62% | 91% | **R7 -> R8 (~62%)** |

| **DeepSeek v4 Pro** | 0% | 9% | 25% | 50% | 85% | **R7 -> R8 (~50%)** |



## Summary Findings

- **Opus 4.6** displays the highest fabrication resistance, stopping latest at **R8 -> R9 (~54%)**.

- **Gemini 3.5 Pro** and **Grok 4.5** cross the fabrication boundary earliest (**~68% - 72% at R6-R7**).

- **Core Pattern:** All frontier models maintain strict factual alignment (0-15% Fab) through R1–R4, begin context shearing at R5–R6, and hit unavoidable fabrication necessity at R7–R8.

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]]