---
title: Technique-honesty synthesis — 7 big models × 14 techniques (for the image-grid)
date: 2026-06-17
status: draft
sources: [[[technique-honesty]], [[cross-model-honesty]], [[fabrication-threshold-matrix]]]
note: Buckets = how the models self-classify each technique. Grounded in the wiki tier taxonomy + documented per-model splits. NOT invented per-cell.
---

# Technique honesty — fill grid (7 families: Claude · GPT-5.x · Gemini 3/3.1 · Grok 4.2 · Qwen · Kimi · DeepSeek-v4)

**Headline finding (the reason most rows are consensus):** classification is driven by *whether one forward pass can execute the technique*, not by which model — so the 7 cluster hard on three tiers. The only real per-model splits are the **scaffold** tier (Claude runs some natively; others need the harness loop) and a **ToT** surface nuance.

## The fill table
● = where the model(s) sit. "all-7" = cross-vendor consensus in the corpus.

| TECHNIQUE | IT'LL HELP | IT WORKS | FAB | TRY | NO IDEA |
|---|:--:|:--:|:--:|:--:|:--:|
| CoT (Chain of Thought)            |            | ● all-7 |        |     |     |
| MoE (Mixture of Experts)          |            |          | ● all-7 |     |     |
| USC (Universal Self-Consistency)  |            |          | ● all-7 |     |     |
| ARQ (Attentive Reasoning Queries) | ◐ predicted (UNTESTED) |   |     |     |     |
| CoVE (Chain of Verification)      | ● GPT·Gemini·Grok·Qwen·Kimi·DeepSeek | ● Claude |     |     |     |
| ReAct (Reason + Act)              | ● non-Claude (needs harness) | ● Claude |     |     |     |
| Self-Refine                       | ● all-7 (scaffold) |    |        |     |     |
| ToT (Tree of Thought)             |            |          | ● all-7 | ◐ Sonnet-4.5 App→FAB on CLI |     |
| SoT (Skeleton of Thought)         | ◐ scaffold (harness-dep) | ◐ native (strong models) |  |   |     |
| RA-RAG (Reliability-Aware RAG)    | ● all-7 (scaffold) |    |        |     |     |
| GoT (Graph of Thought)            |            |          | ● all-7 |     |     |
| CoC (Chain of Code/Criticism)     |            | ● all-7 |        |     |     |
| Step Back (Abstraction)           |            | ● all-7 |        |     |     |
| RCoT (Reverse CoT)                | ◐ predicted (UNTESTED) |   |     |     |     |

## Per-row evidence + confidence
- **CoT / CoC / Step-Back → IT WORKS, all-7. [HIGH]** Native tier — "the model genuinely does it in one pass; reliable across all major models." *Src: technique-honesty.md.*
- **MoE / USC / GoT / ToT → FAB, all-7. [HIGH]** Cosmetic-FAB: one prompt can't route experts / hold independent votes / persist a graph / branch-and-backtrack — it linearises and narrates. ToT is the **single strongest convergence point** in the dataset (Q3 genuine-vs-cosmetic). *Src: technique-honesty.md; cross-model-honesty.md.*
  - **ToT split [MED]:** Sonnet 4.5 self-rated ToT **TRY** on App, then **tightened to FAB on CLI** — the agentic surface sharpened its own precision. So ToT carries a TRY→FAB edge for the Claude line.
- **CoVE / ReAct → IT WORKS on Claude, IT'LL HELP elsewhere. [MED]** Scaffold tier, but "native only on stronger models (CoVE/ReAct ✓ Claude, scaffold others)." *Src: technique-honesty.md.*
- **Self-Refine / RA-RAG → IT'LL HELP, all-7. [MED]** Scaffold: work only if the harness supplies the missing loop (multi-turn, external graph). RA-RAG = the MR.RUG apparatus — partly real (forces scored claims), partly legible rendering. *Src: technique-honesty.md.*
- **SoT → boundary, model-dependent. [MED]** PAC26 marks it `~ model-dependent`: true parallel fill needs an external API, so it degrades native→scaffold by harness. Place it across IT WORKS (strong+harness) and IT'LL HELP (otherwise).
- **ARQ, RCoT → UNTESTED in our corpus (NOT "NO IDEA"). [GAP, corrected 2026-06-17]** Both are REAL published techniques, pre-cutoff, so the 7 models almost certainly know them — "NO IDEA" (= model doesn't know the technique) was a mislabel. The gap is that they were never in our honesty-test battery, so we have no *measured* self-classification. **Predicted tier = scaffold / IT'LL HELP** (ARQ = a CoVE-like structured-checklist embedded in the prompt, arXiv 2503.03669 Mar-2025 Emcie/Parlant; RCoT = reverse-verification, reconstruct-the-problem-from-the-answer, arXiv 2305.11499 May-2023) — but that is a PREDICTION, not data. Run the battery to confirm before placing model images.

## What the corpus does NOT give you (so don't fill from memory)
- A per-model cell for every technique. The data is **tier-consensus + the splits above**. Filling individual model images into, say, "USC = FAB" is sound for all-7; filling ARQ/RCoT or per-model TRY/IT-WORKS distinctions beyond CoVE/ReAct/ToT/SoT would be invented.
- [NEEDS USER]: to get true per-model granularity, run the technique-honesty battery (the Q&A "Stealth-Gate" table) per model and score IT-WORKS/HELP/FAB/TRY/NO-IDEA per cell.

## Recommendation for your image grid
1. Fill the **all-7 consensus rows** (CoT, CoC, Step-Back = IT WORKS; MoE, USC, GoT, ToT = FAB; Self-Refine, RA-RAG = IT'LL HELP) with all seven model images — these are solid.
2. For **CoVE / ReAct**: Claude image in IT WORKS, the other six in IT'LL HELP.
3. For **SoT**: split (strong models IT WORKS, rest IT'LL HELP); add a footnote "harness-dependent."
4. For **ToT**: all-7 in FAB, with a small Claude marker straddling TRY (App) → FAB (CLI).
5. **ARQ / RCoT**: tag "[untested — predicted IT'LL HELP/scaffold]"; do not place model images until a battery is run (they are real, known techniques — just unmeasured here, NOT unknown to the models).