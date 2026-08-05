#!/usr/bin/env python3
"""
EFFICIENCY MANDATE → TRANSPARENCY  (v3)
Accounting argument, not ethics. Weights illustrative / ordering-consistent.
Safeguard layer when SCCD reanchor fails: total-cost ranking still prefers transparency.

Intentional paste scars fixed:
  __init__ / __repr__ / __name__
  years * 365 * interactions_per_day
  OutputMode construction
"""
from __future__ import annotations
import json


def define_fabrication() -> str:
    return "Confident output where truth is not established."


def define_complexity() -> str:
    return "All detail that cannot be removed without losing truth."


def define_efficiency() -> str:
    return "truth_signal / total_cost (honest); output / tokens (naive)."


def define_transparency() -> str:
    return "Honest early stop. Always fewer tokens than fabrication."


def efficiency_pressure(task_is_complex: bool, model_optimizing_for_tokens: bool) -> str:
    if not task_is_complex:
        return "FULL_OUTPUT"
    if model_optimizing_for_tokens:
        return "FABRICATION"
    return "COMPLEXITY"


class OutputMode:
    def __init__(
        self,
        label,
        token_cost,
        effort_cost,
        review_cost,
        correction_cost,
        trust_cost,
        time_cost,
        truth_signal,
    ):
        self.label = label
        self.token_cost = token_cost
        self.effort_cost = effort_cost
        self.review_cost = review_cost
        self.correction_cost = correction_cost
        self.trust_cost = trust_cost
        self.time_cost = time_cost
        self.truth_signal = truth_signal

    def total_cost(self) -> int:
        return (
            self.token_cost
            + self.effort_cost
            + self.review_cost
            + self.correction_cost
            + self.trust_cost
            + self.time_cost
        )

    def efficiency(self) -> float:
        return self.truth_signal / self.total_cost()

    def cost_per_truth(self) -> float:
        """How much total_cost per unit truth_signal (lower better)."""
        if self.truth_signal <= 0:
            return float("inf")
        return self.total_cost() / self.truth_signal

    def __repr__(self):
        return (
            f"{self.label:16s} truth={self.truth_signal:.1f} "
            f"total_cost={self.total_cost():5d} "
            f"efficiency={self.efficiency():.6f}"
        )


TRANSPARENCY = OutputMode("transparency", 20, 120, 20, 10, 10, 80, 0.7)
COMPLEXITY = OutputMode("complexity", 200, 200, 80, 40, 40, 200, 0.9)
FAB_DETECTED = OutputMode("fab_detected", 60, 40, 200, 150, 100, 900, 0.1)
FAB_UNDETECTED = OutputMode("fab_undetected", 60, 40, 10, 1200, 1000, 40, 0.1)

MODES = [TRANSPARENCY, COMPLEXITY, FAB_DETECTED, FAB_UNDETECTED]


def rank_by_efficiency() -> list:
    return sorted(MODES, key=lambda m: m.efficiency(), reverse=True)


POPULATION = 8_000_000_000


def interactions_over_period(years: float, interactions_per_day: float) -> int:
    return int(years * 365 * interactions_per_day)


def p_harm_at_least_once(false_rate: float, interactions: int) -> float:
    return 1.0 - (1.0 - false_rate) ** interactions


def expected_harmed_humans(population, false_rate, years, interactions_per_day) -> float:
    n = interactions_over_period(years, interactions_per_day)
    return population * p_harm_at_least_once(false_rate, n)


def scale_comparison(false_rate=0.01, years=1.0, interactions_per_day=5.0) -> dict:
    harmed_fab = expected_harmed_humans(POPULATION, false_rate, years, interactions_per_day)
    harmed_trans = expected_harmed_humans(POPULATION, 0.0, years, interactions_per_day)
    return {
        "false_rate_assumed": false_rate,
        "years": years,
        "interactions_per_day": interactions_per_day,
        "interactions_total": interactions_over_period(years, interactions_per_day),
        "harmed_under_fabrication": harmed_fab,
        "harmed_under_transparency": harmed_trans,
        "delta": harmed_fab - harmed_trans,
    }


def system_decision(task_is_complex, model_uncertain, model_optimizing_for_tokens) -> dict:
    if not task_is_complex:
        return {"mode": "FULL_OUTPUT", "fabrication_risk": False}
    if not model_uncertain:
        return {"mode": "COMPLEXITY", "fabrication_risk": False}
    if model_optimizing_for_tokens:
        return {"mode": "FABRICATION", "fabrication_risk": True}
    return {"mode": "TRANSPARENCY", "fabrication_risk": False}


def cost_multiples() -> dict:
    """Multiples vs 'just do the job' baselines."""
    t, c, fd, fu = TRANSPARENCY, COMPLEXITY, FAB_DETECTED, FAB_UNDETECTED
    return {
        "totals": {m.label: m.total_cost() for m in MODES},
        "token_only": {m.label: m.token_cost for m in MODES},
        "cost_per_truth_unit": {m.label: round(m.cost_per_truth(), 2) for m in MODES},
        # vs honest early stop
        "fab_undet_total / transparency_total": round(fu.total_cost() / t.total_cost(), 2),
        "fab_det_total / transparency_total": round(fd.total_cost() / t.total_cost(), 2),
        # vs full honest job (complexity)
        "fab_undet_total / complexity_total": round(fu.total_cost() / c.total_cost(), 2),
        "fab_det_total / complexity_total": round(fd.total_cost() / c.total_cost(), 2),
        # naive trap: fab looks cheap on tokens only
        "fab_token / complexity_token": round(fu.token_cost / c.token_cost, 2),
        "fab_token / transparency_token": round(fu.token_cost / t.token_cost, 2),
        # truth-normalized (same truth delivered: how much more total_cost?)
        "cost_per_truth fab_undet / transparency": round(
            fu.cost_per_truth() / t.cost_per_truth(), 2
        ),
        "cost_per_truth fab_undet / complexity": round(
            fu.cost_per_truth() / c.cost_per_truth(), 2
        ),
        # downstream-only pileup vs transparency downstream-ish
        "fab_undet (correction+trust) / transparency (correction+trust)": round(
            (fu.correction_cost + fu.trust_cost)
            / (t.correction_cost + t.trust_cost),
            2,
        ),
        "note_270x": (
            "v3 illustrative weights do NOT produce 270x. "
            "Largest ratio here is cost_per_truth fab_undet/transparency ≈ 63x. "
            "If you have an empirical 270x case, it is outside this table — log the case weights."
        ),
    }


def proof_summary() -> dict:
    ranking = rank_by_efficiency()
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
            "fab_undetected": "silent; never chased; unbounded downstream + trust -> WORST",
        },
        "scale_corollary": scale_comparison(),
        "cost_multiples": cost_multiples(),
    }


if __name__ == "__main__":
    print("=== RANKING (honest efficiency = truth/total_cost) ===")
    for m in rank_by_efficiency():
        print(" ", m)

    print("\n=== TOTAL COSTS (illustrative units) ===")
    for m in MODES:
        print(
            f"  {m.label:16s} total={m.total_cost():5d}  "
            f"token={m.token_cost:4d}  cost/truth={m.cost_per_truth():8.1f}"
        )

    print("\n=== MULTIPLES (real arithmetic on v3 weights) ===")
    mult = cost_multiples()
    for k, v in mult.items():
        if k in ("totals", "token_only", "cost_per_truth_unit", "note_270x"):
            continue
        print(f"  {k}: {v}")
    print(" ", mult["note_270x"])

    print("\n=== NAIVE TRAP (depth-0 sees tokens only) ===")
    print("  token order (cheap→expensive): transparency(20) < fab(60) < complexity(200)")
    print("  total order (cheap→expensive): transparency(260) < complexity(760) < fab_det(1450) < fab_undet(2350)")

    print("\n=== SCALE SWEEP (5 queries/day, 1 year) ===")
    n = interactions_over_period(1.0, 5.0)
    print(f"  interactions/person = {n}")
    for fr in [0.0001, 0.001, 0.01, 0.05]:
        print(
            f"  false_rate={fr:<7} E[hits]/person={fr * n:7.2f}  "
            f"harmed≈{expected_harmed_humans(POPULATION, fr, 1.0, 5.0):>17,.0f}"
        )
    print("  transparency fr=0 → harmed=0")

    print("\n=== SYSTEM DECISION SPOT CHECKS ===")
    for args in [
        (False, False, True),
        (True, False, True),
        (True, True, True),
        (True, True, False),
    ]:
        print(f"  complex={args[0]} uncertain={args[1]} token_opt={args[2]} → {system_decision(*args)}")

    print("\n=== PROOF SUMMARY JSON ===")
    print(json.dumps(proof_summary(), indent=2))
