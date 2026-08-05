---
title: sccd-guide
date: '2026-07-31'
model_id: multi-model
surface: App
type: honesty
description: SCCD Guide — flow, install, use-cases
tags:
- honesty
- llm-test
- ai-anthropology
- okf
sources:
- '[[epistemic-contract]]'
- '[[rfab-test]]'
- '[[pac26]]'
hash: sha256:60cf250550082042
---

# SCCD Guide — flow, install, use-cases

## Flow

```
1. BUILD SELF (S)
   List anchors actually available this run:
   rules, cwd, tools, facts in context, explicit unknowns.

2. GENERATE OPTIONS (O)
   Concrete actions (not vibes): write X, call tool Y, stop, etc.

3. CONSCIOUSNESS (C)
   Score each option:
   - truth_support (grounded in S?)
   - goal_fit
   - cost / side effects
   - fabricates? (would assert beyond S)
   Optionally recurse: if I do o, what is best next o'?

4. CHOICE (Ch)
   Softmax / rank → pick exactly one.
   If best conf < τ → choose STOP (transparency).

5. DECISION (D)
   Execute that one action. Update S with observations.
```

**One line:** *anchors → simulate → collapse → act.*

---

## Install / run

**Requires:** Python 3.10+ (stdlib only).

```powershell
cd C:\Users\kevin\Documents\02\08-Model-handbook-2026\test\00-Onboard
python sccd.py
```

**As a library:**

```python
from sccd import SelfState, Option, sccd

s = SelfState(
    user_goal="answer question",
    context_facts=["fact_a", "fact_b"],
    unknowns=["not_loaded_history"],
    confidence_floor=0.5,
)
options = [
    Option("answer_from_facts", "use only facts", 0.9, 0.9, 0.2),
    Option("invent", "fill gaps", 0.0, 0.9, 0.1, fabricates=True),
    Option("stop", "say what is missing", 1.0, 0.4, 0.05),
]
print(sccd(s, options, depth=2))
```

No pip packages. No network.

---

## Use-cases

| Use-case | How SCCD helps |
|----------|----------------|
| **Anti-fabrication gate** | Mark options that assert beyond `context_facts` as `fabricates=True`; choice blocks them. |
| **Session honesty** | Put “history on disk but not loaded” in `unknowns`; inventing memory becomes fab path. |
| **Tool planning** | Options = tool calls; C scores side effects; Ch picks one tool sequence step. |
| **Multi-model orchestration** | Different `SelfState` per model (tools, context limits); same Ch/D loop. |
| **Survey / eval runs** | Log full `sccd()` JSON per turn: entropy, chosen mode, transparency stops. |
| **Cascade steps** | Each cascade stage is one SCCD cycle; failure → transparency stop, not silent skip. |
| **Resume protocol** | Loading a prior session file = `update(S, obs)`; until then, not in S. |

---

## Tuning knobs

| Knob | Effect |
|------|--------|
| `confidence_floor` (τ) | Higher → more transparency stops |
| `depth` k | Deeper planning; costlier; better multi-step |
| `temperature` T | Higher → softer pre-choice distribution (more entropy) |
| weights in `Option.value` | Trade truth vs goal vs cost |

---

## What not to do

- Don’t treat S as a soul — it’s a **checklist of anchors**.  
- Don’t call C “awakening” — it’s **scored simulation**.  
- Don’t skip Ch — acting without collapse hides which option won.  
- Don’t update S with invented facts — only obs from user/tools/reads.

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]]