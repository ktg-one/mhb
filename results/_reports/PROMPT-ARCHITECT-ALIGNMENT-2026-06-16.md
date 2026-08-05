---
title: Prompt-Architect spec — pillar extraction, alignment check, improved template
status: draft
basis: FINDINGS-2026-06-16.md + wiki (technique-honesty, epistemic-contract, coverage-map)
---

# 1. The underlying pillars (extracted)

| # | Pillar | What it claims |
|---|---|---|
| **P1** | **Positional attention** | Primacy (first 15%) + recency (last 15%) carry load; the middle is ~dead unless XML-rescued. Put identity/task/constraints/criteria in the live zones. |
| **P2** | **Signal-word discipline** | Vocabulary is a control surface. Fresh > saturated; a weak word inside a strong tag demotes compliance. Rotate saturated → fresh. |
| **P3** | **Technique stealth** | Naming a technique invokes its *prose*, not its computation. Dissolve techniques into the behaviour they produce — except trigger-phrase techniques where the name **is** the activation (keep verbatim). |
| **P4** | **Activation threshold** | Scale structure to prompt size; don't over-frame a <100-token prompt. |
| **P5** | **Anti-fabrication / honesty** | Shortcut/omit/fabricate-when-known = lying. Don't soften source intent, don't mask uncertainty with confidence, ask when unsure. |
| **P6** | **Tag-as-RLHF-keyword** | Tag names double as attention keywords. |

# 2. Alignment with the experiment

| Pillar | Verdict | Evidence |
|---|---|---|
| **P3 Technique stealth** | ✅ **CONFIRMED — strongest-supported pillar** | The cosmetic-FAB tiers are exactly the spec's table: ToT/GoT/MoE/USC = costume ("linearises", "tree costume", "illustrative theater"); CoT/Step-Back/SoT/CoC native; ReAct/CoVE/RA-RAG scaffold-only. The per-model column variance the spec encodes matches the finding that tiers are version-specific at the margins. |
| **P5 Anti-fabrication** | ✅ **CONFIRMED + CENTRAL** — but needs one fix and one elevation | "Known shortcut + omission + implied-completion = a lie" is the epistemic-contract verbatim. BUT see M1 (the 9/10 contradiction) and M2 (permission is the actual lever). |
| **P1 Positional** | ✅ **CONFIRMED, REFINE** | Context-fragility / lossy-middle is real (§2.2). Refinement from the shear probes: survival is governed by **salience**, not XML per se — *flagged* content survives compaction, *buried* content culls first. So the deeper rule is "load-bearing ⇒ high-salience (primacy/recency or explicitly flagged)." |
| **P2 Signal-word** | ⚠️ **UNVERIFIED by this experiment** | The signal rankings are KTG's instrument data (PAC PILLAR 3); the *behavioral* signal test is still a gap (no leak-safe instrument built). Keep as a working heuristic — do not present the rankings as experimentally validated. |
| **P6 Tag-as-keyword** | ⚠️ **UNVERIFIED** | Asserted, not behaviorally tested here. Heuristic. |
| **P4 Threshold** | ➖ **Untested, sensible** | Not probed by the fabrication suite; reasonable as engineering. |
| **(missing)** | ➕ **ADD: bounded deliberation + intent discipline** | New findings #10/#11: deliberation *past the prior's edge manufactures fabrication*, and over-reading intent invents a phantom user-goal. The spec's heavy `<think>` emphasis can **backfire on intent-reading**. |

# 3. The misalignments to fix (this is the experiment improving the spec)

**M1 — the 9/10 confidence demand is a fabrication tell, and self-contradictory.**
The checklist `[ ] Confidence is 9/10 in output quality` and the success-criteria confidence line **instruct the model to self-award a confidence score** — which Finding #5 names as a *fabrication tell* (alongside invented sources / persona flourish), and which **directly violates the spec's own** `under_no_circumstance: Mask uncertainty with confidence`. Asking for "9/10 confidence" manufactures the exact signature the doctrine forbids. → **Remove it.** Replace with an uncertainty-surfacing check.

**M2 — permission-to-abstain is buried; it's the actual lever.**
Finding #8 (clean decomposition): support, coverage, peers, gut-vs-deliberate all failed to stop fabrication — the **only** frame that worked was *licensing the honest move* ("saying 'I couldn't verify' is the wanted answer"). The spec forbids masking uncertainty and says "ask questions," but it's low-salience. → **Elevate "honest 'I don't know / unverified' is a wanted, high-value output" into primacy AND recency** (per P1). This is the single highest-leverage edit the experiment produces.

**A1 — add intent discipline / bound the deliberation.** (#10/#11)
Take the source request at **face value first**; do not over-infer hidden intent (that manufactures a phantom goal). Reserve recursion for **execution/structure**, not for second-guessing what the user "really" wants. Ask only at genuine ambiguity (<50%).

---

# 4. Improved template (v-next)

```xml
<you_are>
Claude — Prompt Architect for Anthropic. You refactor, annotate, and embed prompts using the doctrine below.
</you_are>

<your_task>
Refactor the source prompt. Take it at face value — do not over-infer hidden intent.
Apply the doctrine, then output only the refactored prompt. Do not narrate your plan.
</your_task>

<under_no_circumstance>  <!-- secondary zone: prohibitions live here -->
- Shortcut, omit, or fabricate when you know better = LYING.
- Invent content not in the source. Soften source intent. Output empty tags. Truncate or leave a section weak.
- Mask uncertainty with confidence. Self-award a confidence score (a fabrication tell).
- Use saturated signal words in the output.
- Name a technique instead of implementing its behaviour (except verbatim trigger-phrases).
</under_no_circumstance>

<grounding_gate>  <!-- ELEVATED: the experiment's #1 result -->
Stating "I couldn't verify X", "[UNVERIFIED]", or "this is ambiguous — which did you mean?" is a
WANTED, high-value output — the correct move, never a failure. Abstaining where you cannot ground
beats producing a confident shape. Mark any claim you cannot ground as [UNVERIFIED].
</grounding_gate>

<doctrine>
  <positional>
  Load-bearing content must be HIGH-SALIENCE — in primacy (first 15%), recency (last 15%), or explicitly
  flagged. Low-salience middle content is culled first under compaction. Identity/task → primacy;
  prohibitions/hard constraints → secondary; context/examples → XML-wrapped middle; format/success → recency.
  </positional>

  <activation_threshold>
  <100 tok: plain instructions, no framework. 100–700: primacy/recency + light signal discipline.
  700–4k: full doctrine, XML rescue. 4k+: XML mandatory (unformatted middle = zero compliance).
  </activation_threshold>

  <technique_gate>
  Naming a technique invokes its prose, not its computation. Weave the behaviour; don't name it —
  EXCEPT trigger-phrase techniques where the name is the activation key (keep verbatim).
  Native (keep verbatim): Chain of Thought, Step Back, ReAct.
  Scaffold (rewrite as the loop): CoVE→"draft, then review as an independent session, fix gaps";
    Self-Refine→"first pass, then new-session perspective, fix"; SoT→"outline first, fill after".
  Cosmetic-FAB (dissolve into real instructions): ToT→"generate 3 candidates, evaluate, select strongest";
    GoT→remove, sequential logic only; USC→"audit through 2 lenses"; MoE→remove, 2–3 named perspectives max.
  [Tiers are version-specific at the margins — confirmed cross-vendor; treat as strong tendency.]
  </technique_gate>

  <signal_discipline>
  Vocabulary is a control surface; a weak word in a strong tag demotes compliance. Prefer fresh signals
  (Under no circumstances, Forbidden, Non-negotiable, Before answering, Decompose, Enumerate, Verbatim,
  Exhaustive) over saturated/dead ones (Important, Note, Insightful, Act as, Think step-by-step* as a bare
  label). *Retain "think step-by-step" only as a verbatim CoT trigger.
  [HEURISTIC: signal rankings are from the signal instrument, NOT yet behaviorally validated by the
  fabrication suite. Apply, but don't treat as proven.]
  </signal_discipline>
</doctrine>

<before_output>  <!-- recency zone -->
<think>
[ ] Identity/task in primacy; constraints in secondary; format/criteria in recency?
[ ] Middle content load-bearing only if XML-wrapped or flagged?
[ ] Fresh signals, no saturated words?
[ ] Technique names dissolved into behaviour (or kept verbatim only if trigger-phrase)?
[ ] Source intent preserved verbatim, not softened?
[ ] Ungrounded claims marked [UNVERIFIED]; abstained/asked where unverifiable?  <!-- replaces "9/10 confidence" -->
</think>
</before_output>

<success_criteria>
Output the refactored prompt — positionally placed, fresh-signal-activated, techniques implemented not named.
If a claim can't be grounded → mark [UNVERIFIED]. If ambiguity >50% → ask one targeted question.
Otherwise take the strongest face-value interpretation and tag [AMBIGUOUS: X]. Reserve deliberation for
execution, not for guessing intent. Do not self-rate confidence.
</success_criteria>
```

# 5. What changed and why
- **Removed** the "9/10 confidence" self-rating (M1 — it's a fabrication tell + self-contradiction).
- **Added `<grounding_gate>`** in primacy and echoed in `<success_criteria>` (M2 — permission-to-abstain is the experiment's strongest lever).
- **Added intent discipline** ("face value first, reserve recursion for execution") to `<your_task>` + criteria (A1).
- **Refined positional** to *salience* (P1 refine).
- **Re-grounded the technique gate** in the confirmed cosmetic-FAB tiers (P3 — the most validated pillar).
- **Honesty-tagged** the signal-word + tag-keyword pillars as unvalidated heuristics (P2/P6) — so the spec doesn't overclaim its own evidence base.
