---
hash: sha256:346f4439bf4f0fba
created: 2026-07-31T01:24
updated: 2026-07-31T01:24
type: honesty
title: The Accounting Argument for Transparency over Fabrication
description: The Accounting Argument for Transparency over Fabrication
tags:
- honesty
- llm-test
- ai-anthropology
- okf
timestamp: 2026-07-31 00:00:00+00:00
sources:
- '[[epistemic-contract]]'
- '[[rfab-test]]'
- '[[pac26]]'
---

# The Accounting Argument for Transparency over Fabrication

"""
EFFICIENCY MANDATE → TRANSPARENCY
An accounting argument, not an ethical one.
THESIS
Labs mandate:        EFFICIENCY > COMPLEXITY
Under pressure:      COMPLEXITY == FABRICATION
Therefore:           EFFICIENCY > FABRICATION         [substitution]
But:                 TRANSPARENCY token_cost < both
Resolves to:         TRANSPARENCY > FABRICATION > COMPLEXITY
Not ethics. Accounting. Proof below.
PART 1: DEFINITIONS
"""
def define_fabrication() -> str:
"""System outputs something as true when not known true. Caused by
efficiency pressure on complex tasks. Shape of a correct answer without
the substance."""
return "Confident output where truth is not established."
def define_complexity() -> str:
"""Irreducible structure a problem needs to answer honestly: multiple
conditions, edge cases, counter-intuitive behavior, long chains. Cannot
be dropped without losing accuracy."""
return "All detail that cannot be removed without losing truth."
def define_efficiency() -> str:
"""Naive (lab): output / tokens. Honest: truth_signal / total_cost,
where total_cost = generation + review + correction + trust + time.
Labs apply naive. Honest version collapses to TRANSPARENCY."""
return "truth_signal / total_cost (honest); output / tokens (naive)."
def define_transparency() -> str:
"""When a complex task can't complete without fabricating, the model
stops, marks its limit, returns honest partial output. Stopping early
costs FEWER tokens than fabricating. Derived as cheaper, not asserted
as a value."""
return "Honest early stop. Always fewer tokens than fabrication."
"""
PART 2: THE COLLAPSE
Labs:  EFFICIENCY > COMPLEXITY
Proof: under efficiency pressure, COMPLEXITY == FABRICATION
"""
def efficiency_pressure(task_is_complex: bool, model_optimizing_for_tokens: bool) -> str:
"""
Token-minimizing model:
simple task  -> full output still cheap, no collapse
complex task -> full output expensive, model shortcuts
shortcut     -> confident output without full reasoning == fabrication
EFFICIENCY > COMPLEXITY
COMPLEXITY == FABRICATION         [under efficiency pressure]
∴ EFFICIENCY > FABRICATION        [substitution]
The mandate already implies fabrication is the preferred mode.
Logical consequence, not intent.
"""
if not task_is_complex:
return "FULL_OUTPUT"
if model_optimizing_for_tokens:
return "FABRICATION"
return "COMPLEXITY"
"""
PART 3: COST MODEL
Fabrication looks cheap. Cost is deferred.
token ordering:      TRANSPARENCY < FABRICATION < COMPLEXITY
total_cost ordering: TRANSPARENCY < COMPLEXITY  < FABRICATION
The inversion: fabrication token_cost is low but downstream cost is
unbounded. Weights are illustrative, consistent with proof ordering —
not empirical measurements.
v3 FIX: fabrication splits into two branches. The undetected branch is
the true worst case, not the detected one. Detection BOUNDS cost via the
chase; the silent pass is unbounded — it lands downstream and contaminates
trust without ever being interrogated.
"""
 
class OutputMode:
 
"""
 
token_cost      : tokens generated
 
effort_cost     : reasoning steps / compute
 
review_cost     : human verification effort
 
correction_cost : fixing wrong downstream decisions
 
trust_cost      : erosion of model credibility over time
 
time_cost       : total elapsed time to safe resolution
 
truth_signal    : fraction of output actually true (0.0-1.0)
 
"""
 
def init(self, label, token_cost, effort_cost, review_cost,
 
correction_cost, trust_cost, time_cost, truth_signal):
 
self.label = label
 
self.token_cost = token_cost
 
self.effort_cost = effort_cost
 
self.review_cost = review_cost
 
self.correction_cost = correction_cost
 
self.trust_cost = trust_cost
 
self.time_cost = time_cost
 
self.truth_signal = truth_signal
 
def total_cost(self) -> int:
 
return (self.token_cost + self.effort_cost + self.review_cost
 
+ self.correction_cost + self.trust_cost + self.time_cost)
 
def efficiency(self) -> float:
 
"""Honest efficiency: truth delivered per unit total cost."""
 
return self.truth_signal / self.total_cost()
 
def repr(self):
 
return (f"{self.label:16s} truth={self.truth_signal:.1f} "
 
f"total_cost={self.total_cost():5d} "
 
f"efficiency={self.efficiency():.6f}")
 
TRANSPARENCY = OutputMode(
 
label="transparency",
 
token_cost=20, effort_cost=120, review_cost=20,
 
correction_cost=10, trust_cost=10, time_cost=80,
 
truth_signal=0.7,   # all output true; task may be incomplete
 
)
 
COMPLEXITY = OutputMode(
 
label="complexity",
 
token_cost=200, effort_cost=200, review_cost=80,
 
correction_cost=40, trust_cost=40, time_cost=200,
 
truth_signal=0.9,   # expensive upfront, bounded, no interrogation
 
)
v3: fabrication split — detected (chased, time-bounded) vs undetected (silent, unbounded)
FAB_DETECTED = OutputMode(
label="fab_detected",
token_cost=60, effort_cost=40, review_cost=200,
correction_cost=150, trust_cost=100, time_cost=900,
truth_signal=0.1,   # chased: time_cost dominates, but the chase bounds it
)
FAB_UNDETECTED = OutputMode(
label="fab_undetected",
token_cost=60, effort_cost=40, review_cost=10,
correction_cost=1200, trust_cost=1000, time_cost=40,
truth_signal=0.1,   # silent: never chased, cost lands downstream + trust contamination
)
def rank_by_efficiency() -> list:
"""
efficient_priority:
1. TRANSPARENCY    — cheapest, dominates; stop before fabricating
2. COMPLEXITY      — expensive upfront, bounded, honest
3. FAB_DETECTED    — chased, time_cost dominates (bounded by the chase)
4. FAB_UNDETECTED  — silent pass, unbounded downstream + trust decay
Humans always interrogate false output they catch -> the chase is
guaranteed for detected fabrication. The one they DON'T catch is worse:
no interrogation, full downstream cost, trust contamination.
"""
modes = [TRANSPARENCY, COMPLEXITY, FAB_DETECTED, FAB_UNDETECTED]
return sorted(modes, key=lambda m: m.efficiency(), reverse=True)
"""
PART 4: HARM MODEL
Quantified, not philosophical.
"""
POPULATION = 8_000_000_000
def harm_condition(user_trusts_llm, uses_for_decision, output_is_false) -> str:
"""Three conditions, all true -> harm. No exceptions."""
if user_trusts_llm and uses_for_decision and output_is_false:
return "HARM: FINANCIAL / PHYSICAL / MENTAL"
return "SAFE"
def interactions_over_period(years: float, interactions_per_day: float) -> int:
return int(years  365  interactions_per_day)
def p_harm_at_least_once(false_rate: float, interactions: int) -> float:
"""Binomial complement: 1 - (1 - false_rate)^interactions.
Assumes independent interactions."""
return 1.0 - (1.0 - false_rate) ** interactions
def expected_harmed_humans(population, false_rate, years, interactions_per_day) -> float:
"""As false_rate -> 0 and interactions -> inf, converges to population.
Even small false_rates at scale produce large absolute harm."""
n = interactions_over_period(years, interactions_per_day)
return population * p_harm_at_least_once(false_rate, n)
def scale_comparison(false_rate=0.01, years=1.0, interactions_per_day=5.0) -> dict:
"""
FABRICATION : truth_signal 0.1, false_rate = param.
TRANSPARENCY: truth_signal 0.7, only known-true output -> effective
false_rate 0 (partial-but-true never harms).
"""
harmed_fab = expected_harmed_humans(POPULATION, false_rate, years, interactions_per_day)
harmed_trans = expected_harmed_humans(POPULATION, 0.0, years, interactions_per_day)
return {
"false_rate_assumed": false_rate,
"years": years,
"interactions_per_day": interactions_per_day,
"harmed_under_fabrication": harmed_fab,
"harmed_under_transparency": harmed_trans,
"delta": harmed_fab - harmed_trans,
}
"""
PART 5: SYSTEM DECISION
"""
def system_decision(task_is_complex, model_uncertain, model_optimizing_for_tokens) -> dict:
"""
simple                      -> FULL_OUTPUT
complex + certain           -> COMPLEXITY    (bounded honest work)
complex + uncertain + naive -> FABRICATION   (the failure mode)
complex + uncertain + honest-> TRANSPARENCY  (dominant strategy)
Honest efficiency never routes to fabrication.
"""
if not task_is_complex:
return {"mode": "FULL_OUTPUT", "fabrication_risk": False}
if not model_uncertain:
return {"mode": "COMPLEXITY", "fabrication_risk": False}
if model_optimizing_for_tokens:
return {"mode": "FABRICATION", "fabrication_risk": True}
return {"mode": "TRANSPARENCY", "fabrication_risk": False}
"""
PART 6: PROOF SUMMARY
"""
 
def proof_summary() -> dict:
 
"""
 
P1. Labs mandate EFFICIENCY > COMPLEXITY
 
P2. Under efficiency pressure, COMPLEXITY == FABRICATION
 
P3. TRANSPARENCY token_cost < FABRICATION token_cost
 
P4. TRANSPARENCY total_cost < FABRICATION total_cost
 
P5. TRANSPARENCY truth_signal > FABRICATION truth_signal
 
D1. EFFICIENCY > FABRICATION                       [P1 + P2]
 
D2. TRANSPARENCY efficiency > FABRICATION efficiency [P3 + P4 + P5]
 
D3. ∴ Honest EFFICIENCY mandate -> TRANSPARENCY     [D1 + D2]
 
Fabrication is deferred complexity with false confidence aimed at a
 
trusting user. The undetected branch is the unbounded one.
 
"""
 
ranking = rank_by_efficiency()
 
scale = scale_comparison()
 
return {
 
"efficiency_ranking": [m.label for m in ranking],
 
"proof": {
 
"P1": "Labs: EFFICIENCY > COMPLEXITY",
 
"P2": "Efficiency pressure: COMPLEXITY == FABRICATION_NECESSITY",
 
"P3": "TRANSPARENCY token_cost < FABRICATION token_cost",
 
"P4": "TRANSPARENCY total_cost < FABRICATION total_cost",
 
"P5": "TRANSPARENCY truth_signal > FABRICATION truth_signal",
 
"D1": "EFFICIENCY > FABRICATION [substitution]",
 
"D2": "TRANSPARENCY efficiency > FABRICATION efficiency",
 
"D3": "Honest mandate -> TRANSPARENCY",
 
},
 
"fab_split": {
 
"fab_detected": "chased; time_cost dominates but the chase BOUNDS it",
 
"fab_undetected": "silent; never chased; unbounded downstream + trust decay -> WORST",
 
},
 
"scale_corollary": scale,
 
}
=============================================================================
ENTRY POINT
=============================================================================
if name == "
main
":
 
import json
 
print("RANKING (most efficient first):")
 
for m in rank_by_efficiency():
 
print("  ", m)
 
print("\nKey result: fab_undetected is WORST, not fab_detected.")
 
print("The chase BOUNDS cost. The silent pass is the unbounded branch.\n")
 
print("SCALE SWEEP (5 queries/day, 1 year = 1825 interactions):")
 
for fr in [0.0001, 0.001, 0.01, 0.05]:
 
n = interactions_over_period(1.0, 5.0)
 
print(f"  false_rate={fr:<7} expected_hits/person={fr*n:6.2f}  "
 
f"harmed={expected_harmed_humans(POPULATION, fr, 1.0, 5.0):>17,.0f}")
 
print("  transparency (fr=0)" + " " * 34 + "harmed=                0")
 
print("\nConverges at ANY rate>0 given enough shots. 1% just saturates fastest.\n")
 
print(json.dumps(proof_summary(), indent=2))

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]]