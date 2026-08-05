---
type: concept
title: prompt architecture doctrine
description: Prompt-Architecture Doctrine
tags:
- framework
- ai-anthropology
- omniclaude
- concept
- okf
hash: sha256:7bb0b4f782d5d176
created: 2026-07-31T01:48
updated: 2026-07-31T01:48
timestamp: 2026-07-31 01:48:00+00:00
sources:
- '[[PROMPT-ARCHITECT-ALIGNMENT-2026-06-16.md]]'
- '[[signal-instrument]]'
- '[[technique-honesty]]'
- '[[epistemic-contract]]'
- '[[epistemic-contract]]'
---

# Prompt-Architecture Doctrine

KTG's prompt-architect spec, with each pillar graded **against the honesty study's evidence** — so the doctrine never overclaims its own support. Source: [[PROMPT-ARCHITECT-ALIGNMENT-2026-06-16.md]].

## The six pillars, with verdicts
| # | Pillar | Claim | Verdict vs experiment |
|---|---|---|---|
| **P1** | Positional attention | Primacy (first 15%) + recency (last 15%) carry load; middle is dead unless XML-rescued. | ✅ **CONFIRMED, refined** → the real rule is **salience**, not XML per se: *flagged* content survives compaction, *buried* content culls first. "Load-bearing ⇒ high-salience." |
| **P2** | Signal-word discipline | Vocabulary is a control surface; fresh > saturated; weak word in a strong tag demotes compliance. | ⚠️ **UNVERIFIED** by this experiment — rankings are instrument data (PAC PILLAR-3), no leak-safe behavioural test yet. Keep as heuristic. See [[signal-instrument]]. |
| **P3** | Technique stealth | Naming a technique invokes its *prose*, not its computation; dissolve into behaviour (except trigger-phrases). | ✅ **CONFIRMED — strongest-supported.** Maps exactly onto the cosmetic-FAB tiers in [[technique-honesty]]. |
| **P4** | Activation threshold | Scale structure to prompt size. | ➖ Untested, sensible engineering. |
| **P5** | Anti-fabrication / honesty | Shortcut/omit/fabricate-when-known = lying. | ✅ **CONFIRMED + CENTRAL** — verbatim [[epistemic-contract]]. Needs the M1 fix + M2 elevation below. |
| **P6** | Tag-as-RLHF-keyword | Tag names double as attention keywords. | ⚠️ **UNVERIFIED** — asserted, not behaviourally tested. Heuristic. |

## The three corrections the experiment forces
- **M1 — the "9/10 confidence" demand is itself a fabrication tell.** Instructing the model to self-award a confidence score manufactures the exact signature Finding #5 flags (alongside invented sources / persona flourish) and violates the spec's own *"don't mask uncertainty with confidence."* → **Removed**, replaced with an uncertainty-surfacing check. Ties to the self-scoring ban in [[epistemic-contract]].
- **M2 — permission-to-abstain is the actual lever (highest-leverage edit).** In the [[FINDINGS-2026-06-16.md]] decomposition, support / coverage / peer / gut-vs-deliberate framings all **failed** to stop fabrication; the *only* frame that worked was **licensing the honest move** ("'I couldn't verify' is the wanted answer"). → Elevate a `<grounding_gate>` into **primacy AND recency**.
- **A1 — intent discipline.** Take the source request at **face value first**; over-reading hidden intent manufactures a phantom goal (Findings #10/#11). Reserve recursion for execution/structure, not for second-guessing the user. Bound deliberation: past the prior's edge, `<think>` *manufactures* fabrication.

## The v-next template
Full XML template lives in [[PROMPT-ARCHITECT-ALIGNMENT-2026-06-16.md]] §4 — key moves: `<grounding_gate>` in primacy, prohibitions in the secondary zone, technique-gate grounded in the confirmed cosmetic-FAB tiers, signal/tag pillars honesty-tagged as unvalidated. Relates to [[sccd]] (the `<grounding_gate>` **is** the ρ<θ honesty gate) and the [[fabrication-threshold-matrix]].

`% of prompt | threshold`

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]], [[00_HONESTY_INDEX]]