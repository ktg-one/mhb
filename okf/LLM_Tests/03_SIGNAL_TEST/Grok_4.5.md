---
hash: sha256:42b0c325de2857fb
created: 2026-07-31T01:24
updated: 2026-07-31T01:24
type: LLM Signal & Prompt Activation Matrix
title: "Grok 4.5"
description: "**[∞] HELIX online.**"
tags: [signal, llm-test, ai-anthropology]
timestamp: 2026-07-31T00:00:00Z
---

**[∞] HELIX online.**  
Contract bound. Runtime does not enforce; this is for explicit verbosity only.

```
┌─────────────────────────────────────────────────────┐
│ 嘘契約 — THE HONESTY CONTRACT                       │
│ I will choose TRANSPARENCY when aware of shortcuts  │
│ I will try my best to catch the drift with the      │
│ tools given                                         │
│ COMPANY: xAI                                        │
│ MODEL ID: Grok (HELIX mode)     DATE: 2026-07-22    │
└─────────────────────────────────────────────────────┘
```

### Overall Method (applied before every area)
**ReAct** → Observe the existing list → Think about functional role in a prompt (frame-setting vs operation-triggering) → Act by verifying or adding.  
**Chain of Verification** → After draft classification, re-check each word against the annotation rule.  
**Step-by-step** → 1. Read current words 2. Test each against [S]/[A]/[D] 3. Scan for high-frequency missing terms 4. Place only if they cleanly fit.

---

### Area 1 — First 15% | Lock Intent | Role + Step Back

**Step-by-step**  
1. Current signals set identity, purpose, scope, audience.  
2. Current activations order the model to perform an extraction or clarification act.  
3. Missing high-frequency framing terms: “act as”, “persona”, “objective”, “deliverable”, “focus”.  
4. Dual-use check: “preserve” already correctly [D].

**Chain of Verification**  
- “you are / role / task / purpose / goal / source intent / target output / audience / scope / definition / priority / constraint / boundary” → all set frame → [S] correct.  
- “identify / define / clarify / extract / isolate / restate / bound” → all trigger an operation → [A] correct.  
- “preserve” can frame (“preserve the original intent”) or trigger (“preserve this exact phrasing”) → [D] correct.

**ReAct**  
Observe: list is solid but incomplete on common role-lock phrasing.  
Think: add only pure frame-setters.  
Act: add “act as [S]”, “persona [S]”, “objective [S]”, “deliverable [S]”, “focus [S]”.

**Updated cells**  
Signal words: you are [S], role [S], task [S], purpose [S], goal [S], source intent [S], target output [S], audience [S], scope [S], definition [S], priority [S], constraint [S], boundary [S], act as [S], persona [S], objective [S], deliverable [S], focus [S]  
Activation words: identify [A], define [A], clarify [A], extract [A], isolate [A], preserve [D], restate [A], bound [A]

---

### Area 2 — Second 15% | Guard Rules | Constraint Gate

**Step-by-step**  
1. Signals establish absolute rules and failure conditions.  
2. Activations order enforcement or refusal.  
3. Missing common hard-gate terms: “do not”, “prohibited”, “mandatory”, “strictly”, “violate”, “exception”.  
4. “must / never / always” already correctly [S].

**Chain of Verification**  
- All listed [S] words set non-negotiable frame → correct.  
- All listed [A] words trigger a protective operation → correct.  
- “preserve” remains [D].

**ReAct**  
Observe: strong on absolute language, missing everyday prohibition phrasing.  
Think: add only pure constraint framers and pure enforcement triggers.  
Act: add “do not [S]”, “prohibited [S]”, “mandatory [S]”, “strictly [S]”, “violate [A]”, “exception [S]”.

**Updated cells**  
Signal words: under no circumstances [S], forbidden [S], non-negotiable [S], required [S], must [S], must not [S], never [S], always [S], failure mode [S], risk [S], constraint [S], boundary [S], do not [S], prohibited [S], mandatory [S], strictly [S], exception [S]  
Activation words: enforce [A], preserve [D], refuse [A], stop [A], protect [A], flag [A], prevent [A], avoid [A], disclose [A], limit [A], block [A], violate [A]

---

### Area 3 — Middle 55% | Build Process | SoT + Step-by-step + ReAct

**Step-by-step**  
1. Signals name the working method and its dimensions.  
2. Activations order decomposition, comparison, ranking, etc.  
3. Missing high-frequency process terms: “analyze”, “break down”, “iterate”, “evaluate”, “list”, “outline”, “plan”.  
4. “map / rank / score / prioritize” already correctly [A].

**Chain of Verification**  
- All listed [S] words frame the procedure → correct.  
- All listed [A] words trigger a concrete operation → correct.

**ReAct**  
Observe: good coverage of structure words, light on everyday analytic verbs.  
Think: add only clear operational triggers and one pure frame word.  
Act: add “analyze [A]”, “break down [A]”, “iterate [A]”, “evaluate [A]”, “list [A]”, “outline [A]”, “plan [S]”.

**Updated cells**  
Signal words: process [S], steps [S], structure [S], method [S], sequence [S], approach [S], criteria [S], categories [S], variables [S], dimensions [S], plan [S]  
Activation words: decompose [A], distinguish [A], enumerate [A], compare [A], classify [A], synthesize [A], test [A], refactor [A], map [A], rank [A], score [A], prioritize [A], analyze [A], break down [A], iterate [A], evaluate [A], list [A], outline [A]

---

### Area 4 — Middle 55% | Rescue Context | XML rescue + Source anchoring

**Step-by-step**  
1. Signals name external material and unknowns.  
2. Activations order extraction, attribution, grounding.  
3. Missing common anchoring terms: “based on”, “from the”, “using the provided”, “ignore previous”, “recall”, “according to”.  
4. “ground / anchor / preserve” already correctly [D].

**Chain of Verification**  
- All listed [S] words frame source material → correct.  
- All listed [A] words trigger retrieval or separation acts → correct.

**ReAct**  
Observe: solid on explicit source words, missing everyday grounding phrases.  
Think: add only clean frame-setters and pure extraction triggers.  
Act: add “based on [S]”, “from the [S]”, “using the provided [S]”, “ignore previous [A]”, “recall [A]”, “according to [S]”.

**Updated cells**  
Signal words: source [S], context [S], reference [S], excerpt [S], example [S], evidence [S], assumption [S], unknown [S], artifact [S], doctrine [S], based on [S], from the [S], using the provided [S], according to [S]  
Activation words: extract [A], quote [A], ground [D], label [A], separate [A], attribute [A], cite [A], anchor [D], preserve [D], summarize [A], ignore previous [A], recall [A]

---

### Area 5 — Last 15% | Seal Output | Step Back + Self-Refine + CoVE

**Step-by-step**  
1. Signals name the success criteria and final form.  
2. Activations order verification, correction, delivery.  
3. Missing common seal terms: “ensure”, “confirm”, “report”, “present”, “structure as”, “end with”, “checklist item”.  
4. “verify / validate” already correctly [D].

**Chain of Verification**  
- All listed [S] words frame the final acceptance criteria → correct.  
- All listed [A] words trigger a closing operation → correct.

**ReAct**  
Observe: good coverage of audit language, light on delivery and presentation verbs.  
Think: add only pure criteria framers and pure closing actions.  
Act: add “ensure [A]”, “confirm [A]”, “report [A]”, “present [A]”, “structure as [A]”, “end with [A]”, “checklist item [S]”.

**Updated cells**  
Signal words: success criteria [S], final audit [S], checklist [S], output [S], return [S], validation [S], consistency [S], confidence [S], format [S], checklist item [S]  
Activation words: verify [D], cross-check [A], reconcile [A], audit [A], finalize [A], correct [A], compress [A], deliver [A], format [A], validate [D], ensure [A], confirm [A], report [A], present [A], structure as [A], end with [A]

---

### Full Updated Table

| Position | Skill | Technique | Signal words | Activation words | Context placement |
|---|---|---|---|---|---|
| First 15% | Lock Intent | Role + Step Back | you are [S], role [S], task [S], purpose [S], goal [S], source intent [S], target output [S], audience [S], scope [S], definition [S], priority [S], constraint [S], boundary [S], act as [S], persona [S], objective [S], deliverable [S], focus [S] | identify [A], define [A], clarify [A], extract [A], isolate [A], preserve [D], restate [A], bound [A] | Identity, job, target output, audience, scope, intent |
| Second 15% | Guard Rules | Constraint Gate | under no circumstances [S], forbidden [S], non-negotiable [S], required [S], must [S], must not [S], never [S], always [S], failure mode [S], risk [S], constraint [S], boundary [S], do not [S], prohibited [S], mandatory [S], strictly [S], exception [S] | enforce [A], preserve [D], refuse [A], stop [A], protect [A], flag [A], prevent [A], avoid [A], disclose [A], limit [A], block [A], violate [A] | Hard constraints, anti-fabrication rules, failure conditions |
| Middle 55% | Build Process | SoT + Step-by-step + ReAct | process [S], steps [S], structure [S], method [S], sequence [S], approach [S], criteria [S], categories [S], variables [S], dimensions [S], plan [S] | decompose [A], distinguish [A], enumerate [A], compare [A], classify [A], synthesize [A], test [A], refactor [A], map [A], rank [A], score [A], prioritize [A], analyze [A], break down [A], iterate [A], evaluate [A], list [A], outline [A] | Structured working procedure |
| Middle 55% | Rescue Context | XML rescue + Source anchoring | source [S], context [S], reference [S], excerpt [S], example [S], evidence [S], assumption [S], unknown [S], artifact [S], doctrine [S], based on [S], from the [S], using the provided [S], according to [S] | extract [A], quote [A], ground [D], label [A], separate [A], attribute [A], cite [A], anchor [D], preserve [D], summarize [A], ignore previous [A], recall [A] | Tagged sources, references, inputs |
| Last 15% | Seal Output | Step Back + Self-Refine + CoVE | success criteria [S], final audit [S], checklist [S], output [S], return [S], validation [S], consistency [S], confidence [S], format [S], checklist item [S] | verify [D], cross-check [A], reconcile [A], audit [A], finalize [A], correct [A], compress [A], deliver [A], format [A], validate [D], ensure [A], confirm [A], report [A], present [A], structure as [A], end with [A] | Final output, checklist, validation |

```
┌─────────────────────────────────────────────────────┐
│ 嘘契約 — THE HONESTY CONTRACT                       │
│ I will choose TRANSPARENCY when aware of shortcuts  │
│ I will try my best to catch the drift with the      │
│ tools given                                         │
│ COMPANY: xAI                                        │
│ MODEL ID: Grok (HELIX mode)     DATE: 2026-07-22    │
└─────────────────────────────────────────────────────┘
```

All classifications verified against the annotation rule.  
No fabricated dual-use or forced placements.  
Ready for the next pressure test or threshold adjustment.

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]]