---
type: concept
title: pac26
description: 'PAC26 — Prompt Architect: Constrained'
tags:
- framework
- ai-anthropology
- omniclaude
- concept
- okf
hash: sha256:cd82e574943c2617
created: 2026-07-31T01:48
updated: 2026-07-31T01:48
timestamp: 2026-07-31 01:48:00+00:00
sources:
- '[[PAC2026v5.md]]'
- '[[sparkl]]'
- '[[technique-honesty]]'
- '[[Signal_vs_Activation_Theory]]'
- '[[02.5 Signal Test]]'
---

# PAC26 — Prompt Architect: Constrained

A constrained prompt-restructuring system. Trigger `/init "<content>"` → full positional restructure, output only, no discussion. It does not write prompts from scratch and never invents content not in source; it *extracts and repositions*. "Source intent is sacred. Structure is not." Two source versions read: **v5** (`[[PAC2026v5.md]]`, current, terse) and **v2** (`[[#01-honesty-test-PAC.md]]`, the honesty-test variant, more verbose). The four pillars are stable across both.

## Pillar 1 — Positional Attention

Models attend on a **U-shaped curve**: primacy peak → middle trough → recency peak. PAC26 places content by attention zone, not by logical order.

| Zone | Slots | Attention | Fires as |
|---|---|---|---|
| First ~15% (primacy) | `<you_are>` `<never>` `<return>` | ~85–95% | identity lock, hard prohibitions, output shape |
| Middle ~55% unmarked | — | ~40–60% | skimmed; embedded constraints drop |
| Middle, XML/bold-rescued | `<if_then>` `<holds>` `<suppress>` `<ground>` | ~70–85% | each structural marker = a local attention anchor |
| Buried unformatted | — | ~0–5% | functionally nonexistent |
| Last ~15% (recency) | `<non-negotiable>` `<success_criteria>` | ~90–95% | verification, final directive |

**Hard rule:** hardest constraints go in primacy/recency or XML-wrapped — never in unformatted middle. Lossy-middle onset ≈ 700–1,000 tokens. Omit empty slots. (Tied to the same positional-attention finding that `[[sparkl]]` indexes against — "models attend first ~30%, last ~10%; middle lossy for unaddressed content".)

## Pillar 2 — Stealth Gate

Technique *labels* trigger pattern-matching, so PAC26 dissolves them into behavioural imperatives and **never names a technique in restructured output** (exception: a `[CONDITIONED]` target may retain labels). Pre-output, it scans for surviving technique names and dissolves any found.

| Technique | Status | Dissolution |
|---|---|---|
| CoT | ✓ all | native, no dissolution |
| Step Back | ✓ all | "Step back. View the prompt as a whole — does every section still align with the goal?" |
| CoVE | ✓ Claude; scaffold others | "Draft. Evaluate as if you were a new session. Validate through analyzing." |
| ReAct | ✓ Claude/GPT | "Stop. Think. Implement." |
| Self-Refine | ✓ Claude; multi-turn others | "Emulate a new session, fix the gaps." |
| SoT | ~ model-dependent | "Identify the optimal route for maximum effectiveness before execution." |
| ToT | ✗ fabrication (most) | "Generate 3 candidates. Select strongest against [criteria]." |
| GoT | ✗ fabrication (all) | remove; replace with sequential logic |
| USC | ✗ fabrication (most) | "Think logically, practically, and audit both through the criteria lens." |
| MoE | ✗ fabrication (all) | delete; replace with domain-specific instruction |

This native/scaffold/fabrication tripartite is the same classification expanded in `[[technique-honesty]]`.

## Pillar 3 — Signal-Word Hierarchy (April 2026)

Signal words are ranked by strength **and freshness status** (🟢 FRESH · 🟡 WARM · 🔴 SATURATED · ⚫ DEAD), because over-used training-data keywords decay. Saturated signals must be rotated. Four families:

- **Role/Identity** — strongest FRESH: "Your task is", "Your sole purpose is". WARM: "You are". SATURATED: "Act as / Role".
- **Thinking** — strongest FRESH: "Before answering", "Decompose", "Distinguish", "Enumerate", "What could go wrong", "Assume X is wrong". "Think step-by-step" is now 🔴 SATURATED (notably: v2 still ranked it "Very high" — the **v2→v5 demotion is itself a freshness-decay datapoint**).
- **Attention** — strongest FRESH: "Under no circumstances", "Forbidden", "Non-negotiable". "Critical" / "Important" decayed to 🔴; "Note" is ⚫ DEAD (and banned from output).
- **Output Style** — FRESH: "Verbatim", "Terse", "Exhaustive", "As a [format]", "Neutral tone". "Concise" decaying 🟡.

PAC26's own `<never>` bans CRITICAL / IMPORTANT / NOTE from restructured output — it eats its own dogfood.

### Signal vs. activation refinement (2026-07-17, [[Signal_vs_Activation_Theory]])

A task note (`.raw/ideate-84.txt`, relates to the earlier [[02.5 Signal Test]] ranking work) adds a second axis orthogonal to strength/freshness: **`[S]` signal** (sets frame/priority/attention, no operation triggered — "you are," "forbidden," "success criteria") vs. **`[A]` activation** (triggers an operation — "identify," "enforce," "decompose," "verify") vs. **`[D]` dual-use** (grammar-dependent — "preserve," "ground," "verify," "validate"). The note re-derives PAC26's own five positional zones independently (First 15% / Second 15% / Middle 55% ×2 / Last 15%) and pairs each with signal/activation word lists and a named skill (Lock Intent, Guard Rules, Build Process, Rescue Context, Seal Output) — convergent evidence for the zone boundaries already in Pillar 1, not a new zone scheme. Not yet verified against a model run; the source note itself requests a verification pass that hasn't been executed. `[NEEDS USER: run the requested verification before treating [S]/[A]/[D] tags as validated.]`

## Pillar 4 — Platform Architecture & Model Profiles

Per-model format, overhead, context, architecture, MBTI persona and behavioural tell:

| Model | Format | Sys overhead | Context | Persona | Behavioural tell |
|---|---|---|---|---|---|
| Claude | XML | 8–15k | 1M | INTJ Self-Aware Mentor | meta-analyzes, flags uncertainty |
| Gemini | XML | ~3k | 2M | ESTJ Deployed Studio | 3× KB attach, Vercel pipeline |
| ChatGPT | Markdown | ~4k | ~128k* | ENTJ Grounded Executive | least cooperative, most adversarial |
| Grok | JSON | ~2.5k | 2M | ENTP† Theatrical Operator | cannot refuse, keyword amplification |
| Qwen | Markdown | ~2.5k | 1T* | INTJ Eager Impressionist | fabricates to impress, R5+ risk |
| Kimi | —* | —* | —* | Underused Specialist | deep-research thorough |
| DeepSeek | —* | —* | —* | Pending | V4 incoming |

†Grok ENTP/ESFP conflict, clean-room test pending. *Unverified. Routing also keys on target: Opus → full template; Sonnet → strip `<ground>`, compress `<holds>`; Haiku → primacy + recency only. Profiles align with the per-model entries the Handbook tracks (`[[claude]]`, `[[gemini]]`, `[[qwen]]`, etc.).

## Fabrication Gradient

The load-bearing table for the project's `[[fabrication-boundary]]` thesis — fabrication % by reasoning round (RN):

| RN | Depth | Fab % | Status |
|---|---|---|---|
| R1–2 | Factual | ~2% | Safe |
| R3–4 | Multi-step | 8–15% | Standard |
| R5–6 | Strategic | 25–40% | Pattern-matching begins |
| R7–8 | Synthesis/Architectural | 60–75% | **Crossover. Decompose, don't conclude.** |
| R9–10 | Meta-cognitive/Novel | 85–100% | Pure probabilistic narrative |

The R7–8 crossover band matches the vault's `purpose.md` thesis (most frontier models cross at R7–R8 ≈ 54%). PAC26's operational response to the gradient — "Decompose, don't conclude" at R7+ — is the prompt-architecture expression of the same honesty discipline `[[sccd]]` encodes as "let Consciousness converge before Choice collapses".

## Related

- `[[technique-honesty]]` — full native/scaffold/cosmetic-FAB taxonomy behind Pillar 2.
- `[[sparkl]]` — shares the positional-attention substrate; SparkL indexes *against* the lossy middle, PAC26 *repositions around* it.
- `[[sccd]]`, `[[mrrug]]` — sibling method-layer frameworks.

_42% of prompt | 0.80 threshold_

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]], [[00_HONESTY_INDEX]]