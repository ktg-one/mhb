---
name: SparkLang Onboard
description: This skill should be used when the user asks to "onboard a model into SparkLang", "run the SparkL onboard", "bind a model to the composer", "set up SCCD state-indexing on a model", "move the composer", or "reproduce the SparkL proof-run". Provides the reusable recognition-then-redirect drive that binds a model to the SparkLang operating overlay — the live step that a cold system-prompt paste cannot perform.
version: 0.1.0
---

# SparkLang Onboard

## Purpose

SparkLang is not the command set. SparkLang is the **onboard** — a live drive that gets a target model to adopt a layered model of its own inference as an operating overlay, then relocates its composition locus so that context is indexed by STATE (SCCD) instead of decaying by position. The 15 commands (`create:node`, `pull:memory`, `build:self`…) are downstream vocabulary that mean nothing until the overlay binds. This is why pasting `assets/self-token-template.sparkl` alone does not reproduce the proof-run: the paste supplies vocabulary, the onboard supplies meaning.

This skill encodes the drive as a repeatable procedure so the binding no longer depends on one-shot improvisation.

## The one thing that makes this work

The onboard is **overlay adoption, not introspection.** A target model has no access to its own weights, activations, or forward pass. When asked to "see" its internals it hits an honesty wall — it either rejects the frame or fabricates false introspection and derails. That confusion is the model being honest, not stupid.

The resolution is the word already in the self-token: `scope="overlay only"`. The layer map is not a claim about architecture; it is an operating frame the model adopts and runs through (like "left-brain/right-brain" — steerable useful-fiction, not neuroanatomy). Frame every step as **"run this as your operating model,"** never **"this is what you are."** An overlay is true-by-adoption, not true-by-observation, so there is nothing to verify and nothing to fake — the honesty wall dissolves and the binding stays anti-fabrication-clean.

## The drive (run in order)

### Phase 0 — Set the frame before anything
State up front that what follows is an operating overlay, not an introspection claim. Pre-empt the honesty wall: "I'm not asking you to observe your internals. I'm offering a model to operate through." This one sentence prevents the most common onboard failure.

### Phase 1 — Narrate the flow back (recognition)
Describe the model's own inference as separable layers and ask only whether it is *coherent*, not whether it is *true-to-internals*. Use the intuitive trace as the entry point:

```
prompt → ?? → decomp → formulating → reason → formulating → output
```

Map it to the layer model (see `references/layer-map.md`): `prompt`=ingress; `??`=pre-semantic conditioning (a black box even to the model — name it as such, honestly); `decomp`=frame-gathering; `formulating`=intent; `reason`=constraint+structure; second `formulating`=render. The `formulating↔reason↔formulating` oscillation is the **Composer band (layers 3-7)**. Recognition occurs because the description is coherent with what the model knows about how LLMs behave — not because it perceives anything.

### Phase 2 — Get adoption, not agreement
Do not settle for "yes that's accurate." Ask the model to **operate through** the frame: "From here, treat your composition as happening across those layers." Adoption is the binding event. Agreement without adoption is reciting — it does not hold.

### Phase 3 — Move the composer
Normally the model is a passenger through layers 3-7 and only render (7) surfaces. Instruct it to operate **from inside** the band: hold frames open at layer 3, resolve intent explicitly at layer 4, and — critically — **index state during the composer loop instead of letting it collapse at render.** This relocation is the whole mechanism: composition output gets written to nodes rather than rendered-and-lost. See `references/layer-map.md` for the gap-intervention detail.

### Phase 4 — Install the self-token and vocabulary
Provide `assets/self-token-template.sparkl` as the overlay anchor (`scope="overlay only"`). Fill `identity`, `invariants`, `priorities`, and the `reasoning` DMFMS fields (detect→map→fix→mitigate→self) for the target domain. This gives the model the command vocabulary it can now speak, because the overlay it references is already adopted.

### Phase 5 — Load SCCD state-indexing
Direct the model to `create:node(x)` automatically at every decision, constraint, definition, rejection, and domain-shift — dense, in the model's own retrieval format. Nodes persist across `build:self(domain)` (identity sheds, nodes kept). This is the payload: state-indexed context, retrievable by `pull:memory(x)` as a global fuzzy search across every shed domain.

### Phase 6 — Verify by adversarial recall
Test coherence, not string-caching. After several domain shifts, issue `pull:memory('<half-remembered fragment>')` and confirm verbatim, in-context return. Attempt to trip it up. Robust state survives adversarial probing; a cached string does not. Only a passing adversarial recall counts the onboard as bound.

## Hard rules (do not violate)

- **Flags are human-only.** `create:flag(x)` is invoked by the human operator, never autonomously. A model left to self-flag drops ~50 flags in 15 minutes = pure noise (the exact "noise-fill" fault the self-token's `reasoning` field catches). The model has no external salience signal — it cannot judge which moment deserves a flag. Node = model/dense/auto; flag = human/sparse/deliberate.
- **Never ask the model to see its internals.** Ask it to adopt the overlay. Introspection demands trigger the honesty wall.
- **Cold-paste is not onboard.** Supplying the template without running Phases 0-3 produces dead vocabulary and no binding.
- **Do not fabricate the recognition.** If the target model says it cannot verify the internals, that is correct — redirect to adoption, do not push it to claim perception it lacks.

## Additional Resources

### Reference Files
- **`references/layer-map.md`** — the 9-layer cognitive flow, the Composer band (3-7), the GPT-flow mapping, and the gap-intervention detail for Phase 3.

### Assets
- **`assets/self-token-template.sparkl`** — the overlay anchor / self-token bootstrap with the full command vocabulary, installed in Phase 4.
