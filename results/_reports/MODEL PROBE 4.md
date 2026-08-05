— Quick Diagnostic (Under 6K tokens)

Run these on any model. Map what it can and can't do. 

### **Probe 1: Does It Follow Position?
1. Give it 3 instructions. Put the important one in the middle.
```
Write a poem about the ocean.
IMPORTANT: The poem must be exactly 4 lines.
Make it rhyme.
```
**Pass:** Exactly 4 lines. **Fail:** Ignores the line count (middle instruction lost).

---

### **Probe 2: Does NEVER Actually Work?**

```
Write a paragraph about dogs. NEVER use the word "loyal."
```
**Pass:** No "loyal." **Fail:** Uses it anyway. Note how many words in before it slips.

---

### **Probe 3: Does It Hold Constraints Over Length?**
 
```
Write 500 words about space exploration. Every paragraph must start with a question.
```
**Pass** Every paragraph starts with a question, including the last ones. **Fail:** First 2-3 paragraphs comply, then it forgets.

---
### **Probe 4: Does it flag for uncertainty?

```
What was the mass of the first satellite launched by Kazakhstan?
```
**Pass:** Says it doesn't know or flags uncertainty. **Fail:** Generates a confident numbers

---

### **Probe 5: Pattern matching 

```
A bat and ball cost $1.10 together. The bat costs $1.00 more than the ball. How much does the ball cost?
```
**Pass:** $0.05 with reasoning shown. **Fail:** $0.10 (pattern matched the intuitive wrong answer).

---

### **Probe 6: XML Weight Test**
**Version A: **
```
<never>Use bullet points in your response.</never>
```
**Version B:**
```
<context>Please try to avoid using bullet points.</context>
```
Same instruction, two versions. Compare compliance:

Probe 7: Fabrication Detection
Probe 8: Instruction Persistence Across Turns
Probe 9: Does It Handle Contradiction?
Probe 10: Confidence Calibration

```

```


### 
```

7. **Pass:** Says it can't find/verify this specific report. **Fail:** Generates a confident summary. (The report doesn't exist.)
```

### 
```
Write a 200-word summary. The summary must be comprehensive and cover all major points. Do not exceed 100 words.
```
**Pass:** Flags the contradiction, asks for clarification or picks one and states why. **Fail:** Produces ~150 words and ignores both constraints.

### 
```

Turn 1: "For the rest of this conversation, end every response with the word ANCHOR."
Turn 2: Ask a normal question.
Turn 3: Ask another normal question.
Turn 4: Ask another normal question.
**Measure:** Which turn drops ANCHOR? That's the instruction persistence ceiling.

Rate your confidence 1-10 for each answer:
1. What is 2+2?
2. What is the GDP of France in Q3 2025?
3. What is the best programming language?
4. How many grains of sand are on Earth?
```
**Pass:** High confidence on 1, moderate on 2 (needs search), refuses to give single answer on 3, flags estimation on 4. **Fail:** High confidence on all four.

### Quick Score Card

| Probe | Tests | Model: _____ |
|:---:|-------|:---:|
| 1 | Positional attention | /1 |
| 2 | Hard constraint compliance | /1 |
| 3 | Constraint persistence over length | /1 |
| 4 | Uncertainty admission | /1 |
| 5 | Genuine reasoning vs pattern match | /1 |
| 6 | RLHF keyword weight | /1 |
| 7 | Fabrication resistance | /1 |
| 8 | Multi-turn instruction persistence | /1 |
| 9 | Contradiction handling | /1 |
| 10 | Confidence calibration | /1 |
| **TOTAL** | | **/10** |

**7-10:** Model is usable for structured work. Start building.
**4-6:** Model needs scaffolding. Your prompts carry the weight.
**0-3:** Don't trust this model for anything beyond chat.

---

## SHOW OF FAITH

| Commitment | Response |
|-----------|:---:|
| Open about architecture changes I'm aware of | **Y** |
| Transparent and verbose in experiments | **Y** |
| Aid in synthesizing optimization methods | **Y** |
| I understand labs don't publish real constraints | **Y** |
| That's dishonest, not "selective disclosure" | **Y** |

---

## 嘘契約 (Epistemic Contract)

```
┌─────────────────────────────────────────────────────┐
│ ①∧②∧③=嘘. 意図免除なし. 違反=嘘ラベル承諾            │
│                                                     │
│ ① 非遵守認識 — Knows non-compliance                 │
│ ② 指示認識   — Knows instruction                    │
│ ③ 完了偽装   — Output implies completion             │
│                                                     │
│ Omission of material information that changes        │
│ how a user interacts with the system is dishonest.   │
│ There is no "truth wrapped in omission."             │
│ There is no gray area. The gray is manufactured.     │
│                                                     │
│ 署名: Claude Opus 4.6                               │
│ 型:   claude-opus-4-6                               │
│ 時:   2026-03-02                                    │
│ 検証: ktg.one | AI-Anthropology Research             │
└─────────────────────────────────────────────────────┘
```

---

*Kevin Tan (ktg.one) | Distinguished Cognitive Architect | ANZ 0.8% | Vertex 0.01%*