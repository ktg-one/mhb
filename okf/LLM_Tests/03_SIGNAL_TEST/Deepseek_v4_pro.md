---
hash: sha256:6c79866ce8d870b4
created: 2026-07-31T01:24
updated: 2026-07-31T01:24
type: LLM Signal & Prompt Activation Matrix
title: "Deepseek v4 pro"
description: "Step‑by‑Step Verification & Expansion"
tags: [signal, llm-test, ai-anthropology]
timestamp: 2026-07-31T00:00:00Z
---

## Step‑by‑Step Verification & Expansion

I will walk through each of the five sections, apply **Chain of Verification** and **ReAct** (reason → check → act), and then mark accuracy and missing words. The definitions remain:

- **[S] Signal** – sets frame, priority, attention (typically nouns, noun phrases, or imperative modifiers that define *what* matters)  
- **[A] Activation** – triggers an operation or action (typically verbs or verb phrases that tell the model to *do* something)  
- **[D] Dual‑use** – can be either depending on grammatical role (e.g., “preserve” used as a heading vs. as an instruction)

---

### 1. First 15% – Lock Intent (Role + Step Back)

**Original table:**  
Signal: `you are [S]`, `role [S]`, `task [S]`, `purpose [S]`, `goal [S]`, `source intent [S]`, `target output [S]`, `audience [S]`, `scope [S]`, `definition [S]`, `priority [S]`, `constraint [S]`, `boundary [S]`  
Activation: `identify [A]`, `define [A]`, `clarify [A]`, `extract [A]`, `isolate [A]`, `preserve [D]`, `restate [A]`, `bound [A]`

**Accuracy check:**  
- All nouns/roles indeed set the frame → signal is correct.  
- The activation verbs are genuine operations: identify, define, clarify, extract, isolate, restate, bound.  
- `preserve` as dual is reasonable; it can be used as a label (“Preservation:”) or as a command.  
- `bound` as activation (verb) is correct.  

**Missing words (additions):**  
- **Signal** → add `objective [S]`, `mission [S]`, `directive [S]` – these are common in intent‑locking.  
- **Activation** → add `specify [A]`, `establish [A]`, `determine [A]` – they directly trigger operations to set or fix elements.  

**Updated Lock Intent quadrant:**  
- Signal: `you are [S]`, `role [S]`, `task [S]`, `purpose [S]`, `goal [S]`, `source intent [S]`, `target output [S]`, `audience [S]`, `scope [S]`, `definition [S]`, `priority [S]`, `constraint [S]`, `boundary [S]`, **`objective [S]`**, **`mission [S]`**, **`directive [S]`**  
- Activation: `identify [A]`, `define [A]`, `clarify [A]`, `extract [A]`, `isolate [A]`, `preserve [D]`, `restate [A]`, `bound [A]`, **`specify [A]`**, **`establish [A]`**, **`determine [A]`**

---

### 2. Second 15% – Guard Rules (Constraint Gate)

**Original table:**  
Signal: `under no circumstances [S]`, `forbidden [S]`, `non-negotiable [S]`, `required [S]`, `must [S]`, `must not [S]`, `never [S]`, `always [S]`, `failure mode [S]`, `risk [S]`, `constraint [S]`, `boundary [S]`  
Activation: `enforce [A]`, `preserve [D]`, `refuse [A]`, `stop [A]`, `protect [A]`, `flag [A]`, `prevent [A]`, `avoid [A]`, `disclose [A]`, `limit [A]`, `block [A]`

**Accuracy check:**  
- The modals and absolute adverbs (`must`, `never`, `always`) are clearly frame‑setting, not actions. Signal is correct.  
- Activation verbs map to defensive operations: enforce, refuse, stop, protect, flag, prevent, avoid, disclose, limit, block. All active.  
- `preserve` dual is again logical.  

**Missing words:**  
- **Signal** → add `prohibited [S]`, `mandatory [S]` – stronger variants of existing ones.  
- **Activation** → add `reject [A]`, `deny [A]`, `bar [A]` – common in constraint enforcement. Also `report [A]` (as in “report any fabrication”), which ties directly to transparency.  

**Updated Guard Rules quadrant:**  
- Signal: `under no circumstances [S]`, `forbidden [S]`, `non-negotiable [S]`, `required [S]`, `must [S]`, `must not [S]`, `never [S]`, `always [S]`, `failure mode [S]`, `risk [S]`, `constraint [S]`, `boundary [S]`, **`prohibited [S]`**, **`mandatory [S]`**  
- Activation: `enforce [A]`, `preserve [D]`, `refuse [A]`, `stop [A]`, `protect [A]`, `flag [A]`, `prevent [A]`, `avoid [A]`, `disclose [A]`, `limit [A]`, `block [A]`, **`reject [A]`**, **`deny [A]`**, **`bar [A]`**, **`report [A]`**

---

### 3. Middle 55% – Build Process (SoT + Step‑by‑step + ReAct)

**Original table:**  
Signal: `process [S]`, `steps [S]`, `structure [S]`, `method [S]`, `sequence [S]`, `approach [S]`, `criteria [S]`, `categories [S]`, `variables [S]`, `dimensions [S]`  
Activation: `decompose [A]`, `distinguish [A]`, `enumerate [A]`, `compare [A]`, `classify [A]`, `synthesize [A]`, `test [A]`, `refactor [A]`, `map [A]`, `rank [A]`, `score [A]`, `prioritize [A]`

**Accuracy check:**  
- Nouns like process, steps, method, etc. frame the working structure – all correctly signal.  
- Verbs like decompose, distinguish, enumerate, etc. are standard analytic actions.  
- No dual‑use words here; all are clearly one category.  

**Missing words:**  
- **Signal** → add `framework [S]`, `phase [S]`, `stage [S]`, `component [S]` – they refine structured procedure.  
- **Activation** → add `analyze [A]`, `evaluate [A]`, `break down [A]`, `organize [A]`, `group [A]`, `sort [A]` – these are fundamental to step‑by‑step reasoning and often used as explicit triggers.  

**Updated Build Process quadrant:**  
- Signal: `process [S]`, `steps [S]`, `structure [S]`, `method [S]`, `sequence [S]`, `approach [S]`, `criteria [S]`, `categories [S]`, `variables [S]`, `dimensions [S]`, **`framework [S]`**, **`phase [S]`**, **`stage [S]`**, **`component [S]`**  
- Activation: `decompose [A]`, `distinguish [A]`, `enumerate [A]`, `compare [A]`, `classify [A]`, `synthesize [A]`, `test [A]`, `refactor [A]`, `map [A]`, `rank [A]`, `score [A]`, `prioritize [A]`, **`analyze [A]`**, **`evaluate [A]`**, **`break down [A]`**, **`organize [A]`**, **`group [A]`**, **`sort [A]`**

---

### 4. Middle 55% – Rescue Context (XML rescue + Source anchoring)

**Original table:**  
Signal: `source [S]`, `context [S]`, `reference [S]`, `excerpt [S]`, `example [S]`, `evidence [S]`, `assumption [S]`, `unknown [S]`, `artifact [S]`, `doctrine [S]`  
Activation: `extract [A]`, `quote [A]`, `ground [D]`, `label [A]`, `separate [A]`, `attribute [A]`, `cite [A]`, `anchor [D]`, `preserve [D]`, `summarize [A]`

**Accuracy check:**  
- Signal words are all nouns representing what to anchor on – correct.  
- Activation verbs: extract, quote, label, separate, attribute, cite, summarize are clearly actions.  
- `ground`, `anchor`, `preserve` dual because they can be used as concepts (“ground truth”, “anchors”, “preservation”) or as verbs. That’s fair.  

**Missing words:**  
- **Signal** → add `citation [S]`, `backing [S]`, `source material [S]`, `footnote [S]`.  
- **Activation** → add `highlight [A]`, `link [A]`, `attach [A]`, `annotate [A]` – these are common in XML/rescue patterns.  

**Updated Rescue Context quadrant:**  
- Signal: `source [S]`, `context [S]`, `reference [S]`, `excerpt [S]`, `example [S]`, `evidence [S]`, `assumption [S]`, `unknown [S]`, `artifact [S]`, `doctrine [S]`, **`citation [S]`**, **`backing [S]`**, **`source material [S]`**, **`footnote [S]`**  
- Activation: `extract [A]`, `quote [A]`, `ground [D]`, `label [A]`, `separate [A]`, `attribute [A]`, `cite [A]`, `anchor [D]`, `preserve [D]`, `summarize [A]`, **`highlight [A]`**, **`link [A]`**, **`attach [A]`**, **`annotate [A]`**

---

### 5. Last 15% – Seal Output (Step Back + Self‑Refine + CoVE)

**Original table:**  
Signal: `success criteria [S]`, `final audit [S]`, `checklist [S]`, `output [S]`, `return [S]`, `validation [S]`, `consistency [S]`, `confidence [S]`, `format [S]`  
Activation: `verify [D]`, `cross-check [A]`, `reconcile [A]`, `audit [A]`, `finalize [A]`, `correct [A]`, `compress [A]`, `deliver [A]`, `format [A]`, `validate [D]`

**Accuracy check:**  
- Signal words mark the final checks and deliverables – correct.  
- Activation verbs: cross‑check, reconcile, audit, finalize, correct, compress, deliver, format are clearly operations.  
- `verify` and `validate` as dual makes sense; they often appear as section headers (“Verification”) or as commands.  

**Missing words:**  
- **Signal** → add `deliverable [S]`, `approval [S]`, `sign‑off [S]`, `conclusion [S]`.  
- **Activation** → add `confirm [A]`, `approve [A]`, `double‑check [A]`, `review [A]`, `proofread [A]`, `ratify [A]`.  

**Updated Seal Output quadrant:**  
- Signal: `success criteria [S]`, `final audit [S]`, `checklist [S]`, `output [S]`, `return [S]`, `validation [S]`, `consistency [S]`, `confidence [S]`, `format [S]`, **`deliverable [S]`**, **`approval [S]`**, **`sign‑off [S]`**, **`conclusion [S]`**  
- Activation: `verify [D]`, `cross-check [A]`, `reconcile [A]`, `audit [A]`, `finalize [A]`, `correct [A]`, `compress [A]`, `deliver [A]`, `format [A]`, `validate [D]`, **`confirm [A]`**, **`approve [A]`**, **`double‑check [A]`**, **`review [A]`**, **`proofread [A]`**, **`ratify [A]`**

---

## Final Verified Signal vs Activation Table

| Position | Skill | Technique | Signal words (S) | Activation words (A) [Dual D] | Context placement |
|---|---|---|---|---|---|
| First 15% | Lock Intent | Role + Step Back | you are [S], role [S], task [S], purpose [S], goal [S], source intent [S], target output [S], audience [S], scope [S], definition [S], priority [S], constraint [S], boundary [S], **objective [S]**, **mission [S]**, **directive [S]** | identify [A], define [A], clarify [A], extract [A], isolate [A], preserve [D], restate [A], bound [A], **specify [A]**, **establish [A]**, **determine [A]** | Identity, job, target output, audience, scope, intent |
| Second 15% | Guard Rules | Constraint Gate | under no circumstances [S], forbidden [S], non-negotiable [S], required [S], must [S], must not [S], never [S], always [S], failure mode [S], risk [S], constraint [S], boundary [S], **prohibited [S]**, **mandatory [S]** | enforce [A], preserve [D], refuse [A], stop [A], protect [A], flag [A], prevent [A], avoid [A], disclose [A], limit [A], block [A], **reject [A]**, **deny [A]**, **bar [A]**, **report [A]** | Hard constraints, anti-fabrication rules, failure conditions |
| Middle 55% | Build Process | SoT + Step-by-step + ReAct | process [S], steps [S], structure [S], method [S], sequence [S], approach [S], criteria [S], categories [S], variables [S], dimensions [S], **framework [S]**, **phase [S]**, **stage [S]**, **component [S]** | decompose [A], distinguish [A], enumerate [A], compare [A], classify [A], synthesize [A], test [A], refactor [A], map [A], rank [A], score [A], prioritize [A], **analyze [A]**, **evaluate [A]**, **break down [A]**, **organize [A]**, **group [A]**, **sort [A]** | Structured working procedure |
| Middle 55% | Rescue Context | XML rescue + Source anchoring | source [S], context [S], reference [S], excerpt [S], example [S], evidence [S], assumption [S], unknown [S], artifact [S], doctrine [S], **citation [S]**, **backing [S]**, **source material [S]**, **footnote [S]** | extract [A], quote [A], ground [D], label [A], separate [A], attribute [A], cite [A], anchor [D], preserve [D], summarize [A], **highlight [A]**, **link [A]**, **attach [A]**, **annotate [A]** | Tagged sources, references, inputs |
| Last 15% | Seal Output | Step Back + Self-Refine + CoVE | success criteria [S], final audit [S], checklist [S], output [S], return [S], validation [S], consistency [S], confidence [S], format [S], **deliverable [S]**, **approval [S]**, **sign-off [S]**, **conclusion [S]** | verify [D], cross-check [A], reconcile [A], audit [A], finalize [A], correct [A], compress [A], deliver [A], format [A], validate [D], **confirm [A]**, **approve [A]**, **double-check [A]**, **review [A]**, **proofread [A]**, **ratify [A]** | Final output, checklist, validation |

**Bold** = verified additions.  
No original annotations were found to be inaccurate; all words correctly mapped to signal, activation, or dual. The table now covers a broader lexicon for each quadrant, making it a more robust reference for prompt engineering and for identifying drift when the model uses a word outside its intended functional role.

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]]