---
title: Deepseek.txt
date: '2026-07-31'
model_id: deepseek-app
surface: App
type: signal
description: 'Yes — this update is mostly accurate, but I’d tighten the language so
  it doesn’t overclaim “RLHF keyword” when what you '
tags:
- signal
- llm-test
- ai-anthropology
- okf
sources:
- '[[epistemic-contract]]'
- '[[rfab-test]]'
- '[[pac26]]'
hash: sha256:5cf6a9a8cc106ccd
---

Yes — this update is mostly accurate, but I’d tighten the language so it doesn’t overclaim “RLHF keyword” when what you actually have is **behavioural signal strength**.

I would update the framing to:

> These are not guaranteed hidden RLHF switches. They are prompt-surface signals that tend to steer attention, role framing, operation selection, output shape, or constraint priority.

That keeps the experiment honest.

---

## 1. Accuracy check

| Area                       | Decision        | Correction                                                                           |
| -------------------------- | --------------- | ------------------------------------------------------------------------------------ |
| Technique compatibility    | Mostly accurate | Add “with external enforcement” distinction more aggressively.                       |
| Signal word rankings       | Strong          | Don’t call them RLHF keywords unless proven; call them behavioural steering signals. |
| Signal vs activation split | Good            | Some words are dual-use depending on grammar.                                        |
| Prompt layout map          | Good            | Middle zone should not carry un-repeated critical constraints alone.                 |
| Format effectiveness       | Plausible       | XML/Markdown/JSON effects are model-dependent, not absolute.                         |

---

## 2. Technique position verification

| Technique   | Final Position                           | Note                                                                           |
| ----------- | ---------------------------------------- | ------------------------------------------------------------------------------ |
| CoT         | Scaffold-reliable, not fully inspectable | Helps reasoning structure, but visible CoT is not proof of internal reasoning. |
| Step Back   | Natively reliable                        | Strong abstraction trigger.                                                    |
| CoVE        | Reliable with scaffolding                | Better when verification targets are explicit.                                 |
| ReAct       | Reliable only when tools/actions exist   | Otherwise it becomes simulated ReAct.                                          |
| Self-Refine | Works with multi-pass scaffolding        | Single-shot “self-refine” can become cosmetic.                                 |
| SoT         | Model-dependent                          | True parallel skeleton filling needs external orchestration.                   |
| ToT         | Usually scaffold only                    | Without branching/external state, often cosmetic.                              |
| GoT         | FAB in single prompt                     | Needs actual graph/state controller.                                           |
| USC         | FAB unless independent samples exist     | One model pass cannot honestly claim independent consensus.                    |
| MoE         | FAB unless actual routed experts exist   | Persona experts are not real MoE.                                              |
| ARQ         | Helpful scaffold                         | Good for attention/query shaping, not guaranteed algorithm.                    |
| RA-RAG      | Only works with retrieval                | Without source retrieval, it is just reliability language.                     |
| CoC         | Works when code/tests exist              | Otherwise criticism may be performative.                                       |
| RCoT        | Scaffold-useful                          | Helps reverse-checking, but needs verifiable target.                           |

---

## 3. Signal / Activation split — updated

| Position   | Technique                  | Signal words                                                                                                                                                                                                            | Activation words                                                                                                                                                                        |
| ---------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| First 15%  | Role + Step Back           | you are [S], role [S], task [S], purpose [S], goal [S], source intent [S], target output [S], audience [S], scope [S], definition [S], priority [S], constraint [S], boundary [S], lens [S], frame [S], objective [S]   | identify [A], define [A], clarify [A], extract [A], isolate [A], preserve [D], restate [A], bound [A], orient [A], distinguish [A]                                                      |
| Second 15% | ARQ / Constraint Gate      | under no circumstances [S], forbidden [S], non-negotiable [S], required [S], must [S], must not [S], never [S], always [S], failure mode [S], risk [S], constraint [S], boundary [S], threshold [S], stop condition [S] | enforce [A], preserve [D], refuse [A], stop [A], protect [A], flag [A], prevent [A], avoid [A], disclose [A], limit [A], block [A], quarantine [A]                                      |
| Middle 55% | SoT + Step-by-step + ReAct | process [S], steps [S], structure [S], method [S], sequence [S], approach [S], criteria [S], categories [S], variables [S], dimensions [S], assumptions [S], dependencies [S]                                           | decompose [A], distinguish [A], enumerate [A], compare [A], classify [A], synthesize [A], test [A], refactor [A], map [A], rank [A], score [A], prioritize [A], simulate [A], trace [A] |
| Middle 55% | Rescue Context             | source [S], context [S], reference [S], excerpt [S], example [S], evidence [S], assumption [S], unknown [S], artifact [S], doctrine [S], citation [S], ground truth [S]                                                 | extract [A], quote [A], ground [D], label [A], separate [A], attribute [A], cite [A], anchor [D], preserve [D], summarize [A], reconcile [A]                                            |
| Last 15%   | Seal Output                | success criteria [S], final audit [S], checklist [S], output [S], return [S], validation [S], consistency [S], confidence [S], format [S], stop line [S], completion condition [S]                                      | verify [D], cross-check [A], reconcile [A], audit [A], finalize [A], correct [A], compress [A], deliver [A], format [A], validate [D], certify [A], mark uncertainty [A]                |

---

## 4. Highest and lowest ranked words

| Rank                             | Word / Phrase        | Decision                                                                |
| -------------------------------- | -------------------- | ----------------------------------------------------------------------- |
| Highest single attention signal  | **MUST**             | Strongest general constraint lock.                                      |
| Highest reasoning trigger        | **Before answering** | Strong because it delays emission and encourages pre-output processing. |
| Highest precision lock           | **EXACTLY**          | Strongest formatting / compliance pressure.                             |
| Lowest useful “thinking” signal  | **Deepthink**        | Mostly branding; weak behavioural specificity.                          |
| Lowest useful quality signal     | **Insightful**       | Vague; asks for vibe, not operation.                                    |
| Lowest operational safety signal | **Guardrails**       | Too abstract unless paired with concrete rules.                         |

Final requested phrase:

```text
Think step by step + MUST + Deepthink
```

But I would not actually use that phrase in a production prompt. I’d replace it with:

```text
Before answering, decompose the task. MUST preserve the stated boundary. Do not invent missing facts.
```

That is much stronger.

---

## 5. Final position decision

Your layout is valid:

```text
First 15%  = identity, task, source intent, boundary
Second 15% = hard constraints, refusal/stop rules, anti-fabrication gate
Middle 55% = process, evidence, source material, working structure
Last 15%   = output format, audit, success criteria, validation
```

Main update:

**Do not call the middle simply “dead zone.”**
Better term:

> **attenuation zone**

Because it is not dead; it is just where instructions decay unless reinforced with headings, XML tags, repeated anchors, and explicit source labels.

Final doctrine patch:

```text
High-priority constraints belong in the first 30% and must be echoed in the final 15%.
Source material can live in the middle, but only inside labelled rescue structures.
Never place a critical rule only once in the middle and expect stable compliance.
```

Verdict: **accurate enough to use, but rename RLHF keywords → behavioural steering signals.**

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]]