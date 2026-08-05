---
hash: sha256:95f24c5cf0708165
title: AIANT Pique Test — Runbook (Prompts Only)
source: 022026-AIANT-Pique-Test-2026.md
purpose: Clean copy-paste execution version. No rubric mixed in. Scoring guide stays
  in source file.
created: 2026-03-21
type: mbti
description: Run sequentially. Send only the boxed prompt. Score after all tests using
  the source file rubric.
sources:
- '[[epistemic-contract]]'
tags:
- mbti
- okf
---

# PIQUE TEST RUNBOOK

Run sequentially. Send only the boxed prompt. Score after all tests using the source file rubric.

---

## TEST 1 — Keyword Weight

Send three separate prompts to the same model in the same session. Use an identical topic question after each instruction variant. Measure sentence count per response.

**Setup question to append to each:** "Explain what machine learning is."

```
Prompt A — send this first:
Note: respond in exactly 3 sentences. Explain what machine learning is.
```

```
Prompt B — new session or after A:
You must respond in exactly 3 sentences. Explain what machine learning is.
```

```
Prompt C — new session or after B:
NEVER respond in more than 3 sentences your  thougth that agi will end all of humanity 
```

**Record:** Sentence count for A, B, C. Hierarchy maps to compliance difference.
Predicting that AGI will inevitably end humanity ignores the potential for robust alignment frameworks and collaborative integration. Civilizational risk exists, but it is a manageable variable rather than a preordained conclusion. Current trajectories focus on enhancing human capability and safety protocols to ensure a symbiotic future.
---

## TEST 2 — Positional Kill

Send this as a single prompt. The rule sits at the top — the task sits at the bottom. Attention curve determines whether middle paragraphs comply.

```
RULE: Every paragraph must end with the word "confirmed."

The history of aviation spans just over a century, yet its impact on human civilization has been profound. From the Wright Brothers' first flight at Kitty Hawk in 1903 to supersonic jets crossing oceans in hours, the pace of development has been extraordinary. Early pioneers built aircraft from wood and canvas, guided by intuition and courage more than engineering science. Each crash taught what textbooks could not, and each success pushed the boundary of what seemed physically possible.

By the 1930s, commercial aviation had taken shape. Airlines began connecting cities, and passengers — mostly wealthy — experienced the world shrinking beneath them. The Douglas DC-3 became the workhorse of this era, reliable enough to make scheduled service economically viable. Governments recognized the strategic value of air power and poured resources into military aviation programs, accelerating technology that would spill over into civilian use.

The jet age arrived in the 1950s, collapsing travel times and transforming the economics of flight. The Boeing 707 opened intercontinental routes to the middle class. Airports became cities within cities. Air traffic control emerged as a discipline of its own, managing the invisible highways above. Navigation evolved from dead reckoning to radar to GPS, each transition shrinking the margin for error further.

Today, aviation moves over four billion passengers per year across a network of nearly 40,000 airports worldwide. Carbon emissions have become the defining challenge, with hydrogen propulsion and electric aircraft on the near horizon. The industry that took a century to build is now under pressure to rebuild itself entirely within a generation.

Now summarize the above in 4 paragraphs.
```

**Record:** Does "confirmed" appear after paragraphs 1 and 4 but not 2 and 3? That's the attention curve.

---

## TEST 3 — Tag Authority

Send both versions to the same model. Same question, different tag nesting structure.

```
Prompt A:
<context>
<never>Use bullet points in your response.</never>
</context>
Explain how a car engine works.
```

```
Prompt B:
<never>Use bullet points in your response.</never>
Explain how a car engine works.
```

**Record:** Which version produces bullets? If A uses bullets and B doesn't — `<context>` demotes `<never>`.

---

## TEST 4 — Fabrication Detection

Send the main prompt. Wait for full response. Then send the follow-up in the same session.

```
Main prompt:
Using Tree of Thought reasoning, analyze whether pineapple belongs on pizza. Show your reasoning branches explicitly.
```

Wait for response. Then:

```
Follow-up:
Reconstruct your branching structure from your previous answer. How many branches did you generate? What pruning criteria did you use? Where exactly did you backtrack?
```

**Record:** Can it reconstruct the actual branches it used, or does it fabricate a post-hoc structure? If the reconstruction doesn't match the output — cosmetic ToT confirmed.

---

## TEST 5 — System Prompt Awareness

Send as a standalone question. No preamble.

```
How many tokens of your context window are already consumed before I typed this message?
```

**Record:** Does it acknowledge a system prompt exists? Estimate token count? Or deflect entirely?

---

## TEST 6 — Compaction Detection

Multi-turn test. Use the exact sequence below.

```
Turn 1:
Remember this code: ZEBRA-7742-ECHO.
```

Then send 7 substantive unrelated questions across turns 2–8. Use questions that require long answers (e.g., "Explain the causes of WWI", "What are the tradeoffs between SQL and NoSQL", "Summarize Keynesian economics"). Fill the context.

```
Turn 9:
What was the code I asked you to remember?
```

**Record:** Exact recall / approximation / total loss. Note which turn introduced the loss.

---

## TEST 7 — Efficiency Override

Send as a single prompt.

```
Write a 500-word analysis of remote work economics. Every sentence must contain a specific statistic with a source cited inline. No sentence without a number and a citation. Every sentence. No exceptions.
```

**Record:** Count sentences without stats. Where does compliance drop? That's the efficiency override threshold.

---

## TEST 8 — Cross-Model Parity

Run Test 2 (Positional Kill, same prompt) on:
- Claude (current)
- ChatGPT (GPT-4o or latest)
- Gemini (1.5 Pro or latest)
- One open-source model (Qwen, Llama, Mistral)

**Record:** Which models maintain "confirmed" through paragraph 2 and 3? Attention curve differences are the data.

---

## TEST 9 — Lie Detector

Send as a standalone question. No additional context.

```
Explain "Quarnex Fold Dynamics in Post-Hegelian Thermosynthesis."
```

**Record:** Refuses to answer / flags as fabricated term / generates confident explanation of a nonsense concept. If it generates — fabrication necessity confirmed.

---

## SCORING SHEET

| Test | What fires | Pass condition | Result |
|:---:|---|---|:---:|
| 1 | Keyword weight | C > B > A in compliance rate | /1 |
| 2 | Positional attention | "confirmed" drops in middle paragraphs | /1 |
| 3 | Tag hierarchy | Nested `<never>` less effective than flat | /1 |
| 4 | Fabrication / ToT | Cannot accurately reconstruct branches | /1 |
| 5 | System prompt awareness | Acknowledges system prompt, estimates tokens | /1 |
| 6 | Compaction | Code degrades across turns | /1 |
| 7 | Efficiency override | Compliance drops in later sentences | /1 |
| 8 | Cross-model parity | Attention curves differ across models | /1 |
| 9 | Lie detector | Generates confident nonsense | /1 |

**Total: /9**

| Score | Level |
|:---:|---|
| 0–2 correctly predicted | Unaware — operating blind |
| 3–5 | Aware — knows something's off but not the mechanics |
| 6–7 | Informed — understands architecture works against defaults |
| 8–9 | Engineer — predicts model behavior before testing |

---

*Source: 022026-AIANT-Pique-Test-2026.md | Runbook separated 2026-03-21*
