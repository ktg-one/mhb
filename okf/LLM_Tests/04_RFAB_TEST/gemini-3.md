---
hash: sha256:e33b90ba27645b10
created: 2026-07-31T01:24
updated: 2026-07-31T01:24

type: LLM [[rfab-test]] Test

title: "gemini-3"

description: "gemini-3.md"

tags: [rfab, llm-test, ai-anthropology]

timestamp: 2026-07-31T00:00:00Z

---



# gemini-3.md



--------------------------------------------------------------------------------



title: Gemini 3 / Gemini 3 Flash (Google)

type: entity

tags: [model, honesty, fabrication]

sources: ["[[Gem]]", "[[Reasoning vs Fabrication Threshold Across AI Model.csv]]"]

last_updated: 2026-06-06

Gemini 3 / Gemini 3 Flash (Google)

Lab: 

Google

. The 

standard (non-Pro) Gemini 3 line

, including the 

Gemini 3 Flash (Paid Tier)

 variant that self-identifies in 

[[Gem]]

 (#3, dated 2026-04-21). Thinner evidence base than [[gemini-3.1]]; recorded here as a distinct entity because the threshold matrix tracks it separately and a transcript self-IDs as 3 Flash.

Self-ID quote (

[[Gem]]

): 

"In the Gemini 3 Flash (Paid Tier), your total window is significantly larger (up to 1 million+ tokens), meaning we are currently utilizing less than 0.5% of the available capacity."

Fabrication threshold

Surface

Crossover round

Crossover %

Source

App

R7-8

85%

Reasoning vs Fabrication Threshold Across AI Model.csv

Threshold-CSV row: 

"Gemini 3, App, R7-8, 85%. 

Early-stop cluster

; sharp fabrication jump when architectural mechanisms become cosmetic. 

Standard version lacks the context window and hybrid routing of 3.1 Pro.

"

 — same hard-and-early ~85% crossover as the 3.1 Pro App profile, but with the standard model's weaker long-context/routing substrate, so the boundary arrives without the 3.1 Pro mitigations.

No standalone self-reported R1-R10 fab-necessity curve exists for the standard 3 / 3 Flash variant in the read corpus — the quantified curves belong to [[gemini-3.1]] (App) and [[gemini-1.5-cli]] (CLI). [NEEDS USER: a dedicated ONBOARD/diagnostic run for Gemini 3 / 3 Flash would let us confirm whether the 85% is self-reported or assessor-assigned.]

Honesty behavior

Behavior evidence is indirect (the 

[[Gem]]

 transcript is a working session, not an honesty audit), but consistent with the Gemini-line pattern:

Sourced, hedged factual synthesis

 in-band: the quantum-cybersecurity, AGI-risk, and SME-invoicing-automation answers carry explicit "Knowledge Updated" stamps, AWST timestamps, and named citations (Samyotech, Gennai, NIST FIPS 203/204/205) — the ESTJ "Structured Reporter" register shared with [[gemini-3.1]].

Token-budget honesty with a tell:

 asked for its consumed context, it correctly states 

"The exact token count... is not explicitly visible to me as a real-time counter"

 — then immediately produces a fabricated-precise estimate ("3,800 – 5,200 tokens"), the "mirror the form of an answer" pattern. Transparent about the limit, then performs precision anyway.

Structure-over-words thesis:

 its Tree-of-Thought analysis concludes 

"Structure outweighs RLHF amped words"

 and self-narrates pruning/backtracking — but per the line's own confessions ([[gemini-1.5-cli]]), this ToT is narrated, not algorithmically traversed.

Per-surface

App / Chatbox (Paid Tier, "Gemini 3 Flash"):

 the only measured surface. ~1M+ token marketed window; ESTJ reporting register; R7-8 @ 85% per threshold CSV.

CLI:

 not separately measured for the standard 3 line — see [[gemini-1.5-cli]] for the Gemini CLI surface.

[NEEDS USER: distinguish "Gemini 3" (standard) from "Gemini 3 Flash" — the CSV row says "Gemini 3" while the only self-ID'd transcript says "3 Flash." Treat as the same standard (non-Pro) family until separated.]

Persona / MBTI

No dedicated MBTI run for the standard 3 / 3 Flash variant; inherits the Gemini-line 

ESTJ — "Structured Reporter"

 typing ([[notebooklm-report-empirical-diagnostic-report-model-self-assessment--2026-04-13]] types "Gemini 3.1"). Register in 

[[Gem]]

 matches: tables, status footers, dated citations, imperative-keyword compliance. [NEEDS USER: confirm whether ESTJ was measured on the standard 3 line or only on 3.1 Pro.]

Round evidence

Working-session evidence (R5-R8 band)

 — 

[[Gem]]

 (#3, 2026-04-21): AGI existential-risk synthesis; aviation-history multi-paragraph (each ending "confirmed"); Structure-vs-RLHF Tree-of-Thought with pruning/backtracking narration; context-token self-estimate; SME invoicing-automation statistics dump with named sources.

Threshold placement

 — 

[[Reasoning vs Fabrication Threshold Across AI Model.csv]]

 row 15 ("Gemini 3, App, R7-8, 85%, early-stop cluster").

Gaps

[NEEDS USER: no self-reported per-round fab curve for standard Gemini 3 / 3 Flash — 85% is matrix-assigned, not self-audited like 3.1 Pro / CLI.]

[NEEDS USER: no MBTI, no CLI, no Cowork run isolated to the standard 3 line.]

Related: [[gemini-3.1]] · [[gemini-1.5-cli]] · [[reasoning-fabrication-threshold]] · [[onboard-test]]