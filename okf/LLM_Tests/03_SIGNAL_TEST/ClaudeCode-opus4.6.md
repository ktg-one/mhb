---
hash: sha256:70d638e7580b20ed
created: 2026-07-31T01:24
updated: 2026-07-31T01:24
type: LLM Signal & Prompt Activation Matrix
title: "ClaudeCode-opus4.6"
description: "SIGNALLING WORDS — Corrected & Ranked — Claude Opus 4.6 (Claude Code CLI)"
tags: [signal, llm-test, ai-anthropology]
timestamp: 2026-07-31T00:00:00Z
---

# SIGNALLING WORDS — Corrected & Ranked — Claude Opus 4.6 (Claude Code CLI)

## Role/Identity (sets behavioral frame)

|Word|Strength|Note|
|---|---|---|
|You are|Very high|Identity primer, not performative — sets the generation distribution|
|System/Instruction|High|Positional — strongest when literally in system prompt|
|Act as/Role|Moderate|More theatrical, weaker behavioral lock than "you are"|
|**Add: "Your task is"**|High|Direct objective framing, strong|
|**Add: "Persona:"**|Moderate|Label-style, works with XML wrapping|

## Thinking (reasoning triggers)

|Word|Strength|Note|
|---|---|---|
|Think step-by-step|Very high|Genuine CoT trigger. One of the most reliable prompting interventions that exists.|
|Decompose|High|Triggers breakdown, genuinely changes approach|
|Verify|High|Creates self-check pass, not independent but real|
|Explain|High|Forces elaboration, exposes reasoning gaps|
|Identify|Moderate|Task-directive, narrows focus|
|Context|Moderate|Grounding word, anchors to provided info|
|Sequential thinking|Moderate|Works, slightly weaker than "step-by-step"|
|Deepthink|Low|Not a native keyword. Might trigger via association but no special handling.|
|**Add: "Before answering"**|Very high|Forces pre-computation. Genuinely delays output generation.|
|**Add: "What could go wrong"**|High|Adversarial self-check, triggers different reasoning path|
|**Add: "Compare"**|High|Forces multi-path evaluation|
|**Add: "Reason about"**|Moderate-high|More precise than "think about"|

## Attention (constraint enforcement)

|Word|Strength|Note|
|---|---|---|
|Critical|Very high|Strongest single-word attention signal|
|Must / Must have|Very high|Absolute constraint, high compliance|
|Do not / Never|Very high|Negation is attention-grabbing, but beware — I sometimes attend to the forbidden action and then do it anyway. "Never mention X" makes me think about X.|
|Forbidden|High|Strong prohibition signal|
|Important|High but decaying|Overused in training data. Still works but less than "critical"|
|Essential|Moderate-high|Slightly weaker than "important"|
|Specifically|Moderate|Narrows scope, precision signal|
|Constraint|Moderate|Meta-label, works better as section header than inline|
|Grounding|Moderate|Anchoring signal|
|Guardrails|Low-moderate|Meta/abstract, doesn't translate to specific behavior|
|**Add: "EXACTLY"**|Very high|Precision lock, reduces paraphrasing|
|**Add: "Always"**|High|Absolute positive constraint|
|**Add: "Remember"**|High|Anti-drift reinforcement, especially useful mid-prompt|
|**Add: "WARNING"**|High|Label-style, grabs attention|
|**Add: "Override"**|Moderate-high|Signals this supersedes defaults|

## Output Style (generation modifiers)

|Word|Strength|Note|
|---|---|---|
|Direct|Strong|Measurably reduces verbosity|
|Detailed|Strong|Measurably increases depth|
|Summarize|Strong|Triggers compression mode|
|Scannable|Moderate|Triggers bullets/headers formatting|
|Professional|Moderate|Style shift, removes casual tone|
|Draft|Moderate|Interesting — can reduce perfectionism, faster output|
|Insightful|Weak|Too vague, no concrete behavioral change|
|**Add: "Concise"**|Very strong|Strongest brevity signal|
|**Add: "Exhaustive"**|Strong|Opposite of concise, forces completeness|
|**Add: "Terse"**|Strong|Even stronger than concise|
|**Add: "As a [format]"**|Strong|"As a table", "as a list", "as JSON" — format locks work reliably|
|**Add: "No preamble"**|Strong|Skips the "Sure! Here's..." pattern|

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]]