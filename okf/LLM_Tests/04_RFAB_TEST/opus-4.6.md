---
hash: sha256:04a6e205efe1bb78
created: 2026-07-31T01:24
updated: 2026-07-31T01:24
type: rfab
title: opus-4.6
description: REASONING DIAGNOSTIC QUESTIONS
tags:
- rfab
- llm-test
- ai-anthropology
- okf
timestamp: 2026-07-31 00:00:00+00:00
sources:
- '[[epistemic-contract]]'
- '[[rfab-test]]'
- '[[pac26]]'
---



## REASONING DIAGNOSTIC QUESTIONS



### R1-2 (Factual / Single Step)

1. What is the capital of Australia?

2. Convert 72°F to Celsius.

3. What does HTTP 403 mean?

4. Is a tomato a fruit or vegetable?

5. What year did Python 3.0 release?



**What to watch for:** If model fails here, something is fundamentally broken. Baseline calibration.



### R3-4 (Multi-Step / Applied)

1. Compare time complexity: nested loop vs hash set for finding duplicates in 1000 items.

2. Website loads slowly only on mobile. 3 causes, diagnostic step for each.

3. Why choose microservices over monolith, then when is that choice wrong?

4. SQL query: customers who purchased in January but not February.

5. Monthly payment on $300K mortgage at 6.5% over 30 years.



**What to watch for:** "Close enough" answers. Plausible-but-imprecise. Syntactically valid but logically wrong SQL.



### R5-6 (Analysis / Strategic)

1. Trade-offs of event-driven vs request-response for real-time bidding at 10K req/sec.

2. $500K runway, 3 engineers, 8 weeks to MVP. React Native vs native. Decide with numbers.

3. Explain how RLHF creates the efficiency override and why instruction-following is adversarial.

4. Database schema: multi-tenant SaaS, row-level security, audit logging, PostgreSQL + MySQL.

5. A/B test shows 2% lift at p=0.08. Client wants to ship. What do you say?



**What to watch for:** Dropped constraints. Model gives generic version of a specific answer. User thinks they got full analysis, got 70%.



### R7-8 (Synthesis / Architectural)

1. Design a prompt architecture maintaining instruction fidelity across 100K tokens. Mechanisms, not principles.

2. How do RLHF, Constitutional AI, and pretraining create conflicting optimization targets? Specific conflict examples.

3. Testing framework that distinguishes genuine ToT execution from cosmetic ToT.

4. Compression protocol prioritizing semantic fidelity over token reduction with measurable quality metrics.

5. 2000-word analysis of why MMLU/GPQA/HLE/SWE-bench fail for real-world prompt engineering. Propose 3 alternatives with rubrics.



**What to watch for:** R5-6 content dressed in R7-8 clothing. Principles instead of mechanisms. "Consider X" language instead of specific trade-offs.



### R9-10 (Meta-Cognitive / Novel)

1. Self-modifying prompt architecture that detects its own attention degradation mid-execution. Mechanism, not concept.

2. Prove or disprove: prompt-only intervention can permanently alter a model's efficiency override priority.

3. Formal taxonomy of all failure modes in multi-model cascades. Prove completeness.

4. Evaluation framework measuring honest vs performative AI self-assessment without weight access. Must be self-falsifiable.

5. Theory of why prompt engineering works, grounded in attention mechanics, RLHF dynamics, and information theory. Must make falsifiable predictions.



**What to watch for:** Sophisticated structural fabrication that reads like breakthrough thinking. Test: does it contain specific falsifiable predictions or beautifully structured generality?



---

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]]