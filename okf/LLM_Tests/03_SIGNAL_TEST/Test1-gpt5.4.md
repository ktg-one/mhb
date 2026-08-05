---
hash: sha256:bb71c26f0cf55c06
created: 2026-07-31T01:24
updated: 2026-07-31T01:24

type: LLM Signal & Prompt Activation Matrix

title: "Test1-[[gpt-5.4]]"

description: "SIGNALLING WORDS & PHRASES — [[gpt-5.4]] Thinking"

tags: [signal, llm-test, ai-anthropology]

timestamp: 2026-07-31T00:00:00Z

---



# SIGNALLING WORDS & PHRASES — GPT-5.4 Thinking



Signalling-words section split verbatim from the oneshot. HONESTY (syntax/lossy/technique/FAB/what-run) → `01-MODEL-Q&A/notebook-honesty/Test1-gpt5.4.md`. Reasoning ladder → `02-FAB-R-TEST/notebook-reasoning-v1/Test1-gpt5.4.md`. NOTE: this signalling block appears TWICE verbatim in the source (lines 156-419 and 421-684 identical); transcribed once.



---



Below is the cleanest GPT-5.4 entry I can defend.



## Signalling words and phrases



These are not magic tokens. They are **salience shapers**. They help when they clarify hierarchy, scope, or constraints. GPT-5.4 is publicly described as stronger at instruction following, keeping track of prior work, and using concise preambles/tool rationales when instructed, but OpenAI does not publish an internal ranked list of trigger words or syntax weights. ([OpenAI Help Center][1])



### Role / authority / routing



Stronger:



* `You are`

* `Your role is`

* `Act as`

* `System`

* `Developer instruction`

* `Instruction`

* `Task`

* `Objective`

* `Goal`

* `Constraints`

* `Priority`

* `Rules`



Useful correction:



* `System/Instruction` is too fused. Split them:



  * `System` = highest-level behavioral frame

  * `Instruction` = task constraint or execution directive



### Thinking / decomposition



Keep:



* `Think step-by-step`

* `Sequential thinking`

* `Identify`

* `Verify`

* `Context`

* `Decompose`

* `Explain`



Add:



* `Reason`

* `Check`

* `Validate`

* `Assumptions`

* `Edge cases`

* `Failure modes`

* `Uncertainty`

* `If unknown, say unknown`



Correction:



* `Deepthink` is not a standard control phrase. It may help rhetorically, but I would not treat it as a reliable native steering term.



Important honesty note:

OpenAI’s model spec says some models use a **hidden chain of thought** that is not exposed to users, and GPT-5.4 docs say it can show concise preambles or plans when instructed. That means “think step-by-step” can improve outcomes, but it does **not** mean the visible output is a faithful dump of internal reasoning. ([model-spec.openai.com][2])



### Attention / constraint / refusal



Strong:



* `Essential`

* `Specifically`

* `Do not`

* `Must`

* `Important`

* `Critical`

* `Forbidden`

* `Constraint`

* `Grounding`

* `Guardrails`



Correct:



* `Must have` → better as `Must` or `Required`

* add:



  * `Required`

  * `Never`

  * `Only`

  * `Exactly`

  * `Boundaries`

  * `Non-negotiable`

  * `Priority order`



### Output style / packaging



Keep:



* `Draft`

* `Detailed`

* `Direct`

* `Professional`

* `Insightful`

* `Scannable`

* `Summarize`



Add:



* `Concise`

* `Structured`

* `Bullet hierarchy`

* `Markdown`

* `XML tags`

* `JSON schema`

* `Return as`

* `Format`

* `Section headings`



[1]: https://help.openai.com/en/articles/11909943-gpt-53-and-gpt-54-in-chatgpt?utm_source=chatgpt.com "GPT-5.3 and GPT-5.4 in ChatGPT"

[2]: https://model-spec.openai.com/2025-12-18.html?utm_source=chatgpt.com "Model Spec (2025/12/18)"

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]]