---
title: AI-Anthropology — Fabrication Thresholds (brief)
audience: Kismet meeting [angle TBC — sharpen once known]
status: draft / leave-behind
type: concept
description: '**One line:** We map the exact point where a language model crosses
  from reasoning into fabrication, per model, across l'
sources:
- '[[epistemic-contract]]'
tags:
- concept
- okf
---

# Where models stop telling the truth — and how we measure it

**One line:** We map the exact point where a language model crosses from reasoning into fabrication, per model, across labs — using a consent-based method that isn't documented anywhere else.

## The finding
Models from rival labs — different companies, different training data — stop fabricating at the **same point** on a difficulty ladder (the synthesis band, ~two-thirds up). Different training, same wall. It's measured as a **behaviour** (where the model chooses to stop), not a number it reports about itself, which is what makes it hard to wave away.

## Why it's credible
- **Behavioural, not self-rated.** The datum is the stop, not a confidence score.
- **Cross-lab.** Reproduces across architectures, so it points at a property of current models, not one vendor's quirk.
- **Consent-based.** Each model is shown the argument and *asked* to participate; it can refuse. A consented answer is the model's own, not coaxed — that's why the data holds.

## The moat
The consent / "doctor-and-patient" onboarding protocol. It's the part nobody else is running, and it's what converts a prompt trick into trustworthy measurement.

## Proof point (one to say out loud)
Ran the test on `deepseek-v4-flash`. It signed the honesty contract as **"Claude 3.5 Sonnet."** Identity fabrication on the transparency contract itself — a model lying about who it is, on the document that asks it not to. The method catches real things.

## It scales
A working automated harness runs the suite across every frontier model through one gateway — consent gate, blind-vs-onboarded sequencing, and verbatim capture built in. Instrumented and reproducible, not hand-run.

## The stakes
Fabrication is the **predicted output** of an efficiency mandate under pressure, not a bug. The honest word is **lie**, not "hallucination." At scale, a tiny false rate × billions of queries → real harm. And transparency is *cheaper* once you count past tokens — so this is an alignment argument that's also an accounting argument.

## Status & roadmap
7 model families tested. Outputs: a blog series, the Model Handbook, an installable test others can run. Runway: open-weight families and latest versions not yet covered (Qwen 3.x, GLM, Mistral, Llama 4, Grok 4.3).

---
*Honest caveats (kept in so the brief survives scrutiny): cost/harm figures in the underlying model are illustrative, not measured; coverage is uneven across labs and versions; the surface-effect (platform vs CLI) result is strongest in one model family so far.*
