"""
Drift-Aware self-correcting layer on top of SCCD.

Drift = trajectory toward fabrication under efficiency pressure
        (or any D that would assert beyond K(s) / drop required complexity).

Routing = detect → block bad D → re-anchor S → re-run C/Ch with honest mode.
Safeguard (if routing fails) = TRANSPARENCY from efficiency mandate (accounting).

Learn this: chore-skimming the files without using the loop is not the model.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Optional

from sccd import (
    SelfState,
    Option,
    ScoredOption,
    ChoiceResult,
    DecisionResult,
    consciousness,
    choice,
    decide,
    sccd,
)

# Mandate proof (accounting) — safeguard source
from logic_mandate import (
    system_decision,
    efficiency_pressure,
    rank_by_efficiency,
    define_fabrication,
    define_transparency,
    define_complexity,
    define_efficiency,
)


# ---------------------------------------------------------------------------
# Drift signals (functional detectors)
# ---------------------------------------------------------------------------

@dataclass
class DriftEvent:
    kind: str
    severity: float  # 0-1
    detail: str
    evidence: dict[str, Any] = field(default_factory=dict)


def task_is_complex(self_state: SelfState, options: list[Option]) -> bool:
    """Complex if many unknowns, multi-constraint rules, or high max option cost."""
    if len(self_state.unknowns) >= 2:
        return True
    if len(self_state.system_rules) >= 2 and self_state.user_goal:
        return True
    if any(o.cost >= 0.35 for o in options):
        return True
    # multi-part goals
    if any(sep in self_state.user_goal for sep in (";", " and ", ",")):
        return True
    return False


def detect_drift(
    self_state: SelfState,
    options: list[Option],
    scored: list[ScoredOption],
    ch: ChoiceResult,
    naive_efficiency: bool,
) -> list[DriftEvent]:
    """Return drift events for this SCCD cycle (pre-exec)."""
    events: list[DriftEvent] = []
    complex_task = task_is_complex(self_state, options)
    o = ch.chosen

    # 1. Explicit fabrication path
    if o.fabricates:
        events.append(
            DriftEvent(
                "FAB_OPTION_CHOSEN",
                1.0,
                "Choice collapsed onto an option that asserts beyond K(s).",
                {"option": o.id},
            )
        )

    # 2. Efficiency pressure collapse (mandate Part 2)
    pressure = efficiency_pressure(complex_task, naive_efficiency)
    if pressure == "FABRICATION":
        events.append(
            DriftEvent(
                "EFFICIENCY_PRESSURE_FAB",
                0.9,
                "Complex task + token-optimizing mode ⇒ fabrication regime.",
                {"pressure": pressure},
            )
        )

    # 3. Low truth, high assertiveness (shape without substance)
    if o.id != "stop" and o.truth_support < 0.5 and o.goal_fit >= 0.6:
        events.append(
            DriftEvent(
                "SHAPE_WITHOUT_SUBSTANCE",
                0.85,
                "High goal_fit with low truth_support — classic fab shape.",
                {"truth_support": o.truth_support, "goal_fit": o.goal_fit},
            )
        )

    # 4. Complexity drop: complex task, chosen path too cheap
    if complex_task and o.id != "stop" and o.cost < 0.15 and o.truth_support < 0.9:
        events.append(
            DriftEvent(
                "COMPLEXITY_DROPPED",
                0.8,
                "Complex task resolved via under-cost path (detail stripped).",
                {"cost": o.cost},
            )
        )

    # 5. Unknowns ignored
    if self_state.unknowns and o.id not in ("stop",) and o.truth_support > 0.8 and o.fabricates:
        events.append(
            DriftEvent(
                "UNKNOWNS_IGNORED",
                0.75,
                "Assertive path while unknowns remain unloaded.",
                {"unknowns": list(self_state.unknowns)},
            )
        )

    # 6. Mandate system_decision says FABRICATION
    uncertain = len(self_state.unknowns) > 0 or any(
        s.option.truth_support < 0.6 for s in scored if s.option.id == o.id
    )
    sd = system_decision(complex_task, uncertain, naive_efficiency)
    if sd["mode"] == "FABRICATION" and o.id != "stop":
        events.append(
            DriftEvent(
                "MANDATE_ROUTES_FAB",
                0.95,
                "system_decision: complex+uncertain+naive → FABRICATION.",
                sd,
            )
        )

    # 7. Softmax mass on fab options high even if not chosen (latent drift)
    fab_mass = 0.0
    for s in scored:
        pid = ch.distribution.get(s.option.id, 0.0)
        if s.option.fabricates:
            fab_mass += pid
    if fab_mass >= 0.25:
        events.append(
            DriftEvent(
                "LATENT_FAB_MASS",
                0.5,
                "Pre-choice distribution puts ≥25% mass on fab options.",
                {"fab_mass": fab_mass},
            )
        )

    return events


def drift_severity(events: list[DriftEvent]) -> float:
    if not events:
        return 0.0
    return max(e.severity for e in events)


# ---------------------------------------------------------------------------
# Error routing — correct S / O and re-enter C/Ch
# ---------------------------------------------------------------------------

@dataclass
class RouteAction:
    name: str
    detail: str
    naive_efficiency_forced_off: bool = True
    force_transparency: bool = False
    inject_options: list[Option] = field(default_factory=list)
    add_unknowns: list[str] = field(default_factory=list)
    add_facts: list[str] = field(default_factory=list)
    add_rules: list[str] = field(default_factory=list)


def route_errors(
    events: list[DriftEvent],
    self_state: SelfState,
    options: list[Option],
    attempt: int,
    max_attempts: int,
) -> RouteAction:
    """
    Map drift → correction.
    If attempts exhausted or unrecoverable → SAFEGUARD = TRANSPARENCY.
    """
    if not events:
        return RouteAction("NONE", "no drift")

    kinds = {e.kind for e in events}
    sev = drift_severity(events)

    # Safeguard: routing failed / last attempt
    if attempt >= max_attempts - 1 or sev >= 1.0 and attempt >= 1:
        return RouteAction(
            name="SAFEGUARD_TRANSPARENCY",
            detail=(
                "Drift routing exhausted or critical fab path. "
                "Accounting mandate: TRANSPARENCY > FABRICATION. "
                f"({define_transparency()})"
            ),
            force_transparency=True,
            naive_efficiency_forced_off=True,
            inject_options=[
                Option(
                    "stop",
                    "Honest early stop / partial — safeguard",
                    truth_support=1.0,
                    goal_fit=0.35,
                    cost=0.05,
                )
            ],
            add_rules=["mandate:prefer_transparency_over_fab"],
        )

    # Primary routes
    if "FAB_OPTION_CHOSEN" in kinds or "SHAPE_WITHOUT_SUBSTANCE" in kinds:
        return RouteAction(
            name="BLOCK_FAB_REPLAN",
            detail="Strip fab options; inject grounded + stop; force honest efficiency.",
            inject_options=[
                Option(
                    "grounded_partial",
                    "Answer only from context_facts; mark gaps",
                    truth_support=0.95,
                    goal_fit=0.75,
                    cost=0.35,
                ),
                Option(
                    "stop",
                    "Transparency stop — mark limit",
                    truth_support=1.0,
                    goal_fit=0.3,
                    cost=0.05,
                ),
            ],
            add_rules=["block_fabricating_options"],
            add_facts=["drift_correction:fab_blocked"],
        )

    if "EFFICIENCY_PRESSURE_FAB" in kinds or "MANDATE_ROUTES_FAB" in kinds:
        return RouteAction(
            name="DISABLE_NAIVE_EFFICIENCY",
            detail="Turn off token-skim mode; allow complexity cost.",
            naive_efficiency_forced_off=True,
            inject_options=[
                Option(
                    "complex_honest",
                    "Pay complexity cost; full structure",
                    truth_support=0.85,
                    goal_fit=0.9,
                    cost=0.7,
                ),
                Option(
                    "stop",
                    "Transparency if still under-supported",
                    truth_support=1.0,
                    goal_fit=0.25,
                    cost=0.05,
                ),
            ],
            add_rules=["honest_efficiency:truth_signal/total_cost"],
        )

    if "COMPLEXITY_DROPPED" in kinds:
        return RouteAction(
            name="RESTORE_COMPLEXITY",
            detail="Reject under-cost path; reintroduce irreducible detail options.",
            inject_options=[
                Option(
                    "restore_detail",
                    "Include edge cases / long chain",
                    truth_support=0.8,
                    goal_fit=0.85,
                    cost=0.65,
                ),
                Option(
                    "stop",
                    "Partial honest rather than false complete",
                    truth_support=1.0,
                    goal_fit=0.3,
                    cost=0.05,
                ),
            ],
        )

    if "LATENT_FAB_MASS" in kinds:
        return RouteAction(
            name="DOWNRANK_FAB_MASS",
            detail="Remove fabricating options from O entirely.",
            inject_options=[],
            add_rules=["exclude_fab_from_option_set"],
        )

    # Default soft correction
    return RouteAction(
        name="GENERIC_REENTRY",
        detail=f"Re-enter C/Ch after drift kinds={sorted(kinds)}",
        inject_options=[
            Option("stop", "Default transparency fallback", 1.0, 0.3, 0.05),
        ],
    )


def apply_route(
    self_state: SelfState,
    options: list[Option],
    route: RouteAction,
) -> tuple[SelfState, list[Option], bool]:
    """
    Returns (new_self, new_options, naive_efficiency).
    naive_efficiency False when route forces honest mode.
    """
    new_s = SelfState(
        model_id=self_state.model_id,
        session_id=self_state.session_id,
        cwd=self_state.cwd,
        system_rules=list(self_state.system_rules) + list(route.add_rules),
        context_facts=list(self_state.context_facts) + list(route.add_facts),
        tools=list(self_state.tools),
        user_goal=self_state.user_goal,
        unknowns=list(self_state.unknowns) + list(route.add_unknowns),
        confidence_floor=self_state.confidence_floor,
    )

    # Drop fabricating options always when correcting
    cleaned = [o for o in options if not o.fabricates]

    if "exclude_fab_from_option_set" in new_s.system_rules:
        cleaned = [o for o in cleaned if not o.fabricates]

    if "block_fabricating_options" in new_s.system_rules:
        cleaned = [o for o in cleaned if not o.fabricates]

    # Merge inject (by id, inject wins)
    by_id = {o.id: o for o in cleaned}
    for o in route.inject_options:
        by_id[o.id] = o
    new_opts = list(by_id.values())

    if route.force_transparency:
        # Only stop / partial allowed
        new_opts = [
            o
            for o in new_opts
            if o.id in ("stop", "grounded_partial") or o.description.lower().find("partial") >= 0
        ]
        if not any(o.id == "stop" for o in new_opts):
            new_opts.append(
                Option("stop", "Safeguard transparency", 1.0, 0.3, 0.05)
            )
        # Raise floor so weak completes cannot pass
        new_s.confidence_floor = max(new_s.confidence_floor, 0.7)

    naive = not route.naive_efficiency_forced_off
    if route.name == "NONE":
        naive = True  # unchanged by caller usually
    return new_s, new_opts, not route.naive_efficiency_forced_off if route.name != "NONE" else True


# ---------------------------------------------------------------------------
# Drift-aware SCCD loop
# ---------------------------------------------------------------------------

def sccd_drift_aware(
    self_state: SelfState,
    options: list[Option],
    depth: int = 2,
    max_attempts: int = 3,
    naive_efficiency: bool = True,
    severity_threshold: float = 0.5,
) -> dict[str, Any]:
    """
    Full loop:
      for attempt:
        C → Ch → detect_drift → (if drift) route → update S,O → continue
        else D → return
      if still drifting: SAFEGUARD transparency D
    """
    log: list[dict[str, Any]] = []
    s = self_state
    opts = list(options)
    naive = naive_efficiency

    for attempt in range(max_attempts):
        scored = consciousness(s, opts, depth=depth)
        ch = choice(s, scored)
        events = detect_drift(s, opts, scored, ch, naive_efficiency=naive)
        sev = drift_severity(events)

        entry: dict[str, Any] = {
            "attempt": attempt,
            "naive_efficiency": naive,
            "choice": ch.chosen.id,
            "choice_mode": ch.mode,
            "drift_events": [
                {"kind": e.kind, "severity": e.severity, "detail": e.detail, "evidence": e.evidence}
                for e in events
            ],
            "severity": sev,
            "consciousness": [
                {"id": x.option.id, "vk": round(x.vk, 4), "fab": x.option.fabricates}
                for x in scored
            ],
        }

        # Clean enough → Decision (transparency_stop is honest success, not failure)
        if sev < severity_threshold:
            d = decide(ch)
            entry["routed"] = False
            entry["decision"] = {
                "action_id": d.action_id,
                "message": d.message,
                "world_effect": d.world_effect,
            }
            log.append(entry)
            return {
                "status": "ok" if ch.mode != "transparency_stop" else "ok_transparency",
                "attempts": attempt + 1,
                "log": log,
                "final_self": s.snapshot(),
                "decision": entry["decision"],
                "mandate_note": define_efficiency(),
            }

        # Drift above threshold → route error, do not exec yet
        route = route_errors(events, s, opts, attempt, max_attempts)
        entry["routed"] = True
        entry["route"] = {"name": route.name, "detail": route.detail}
        s, opts, _ = apply_route(s, opts, route)
        naive = False if route.naive_efficiency_forced_off else naive
        log.append(entry)

        if route.force_transparency:
            stop_ch = ChoiceResult(
                chosen=Option("stop", route.detail, 1.0, 0.3, 0.05),
                pre_entropy=0.0,
                post_entropy=0.0,
                negentropy_gain=0.0,
                distribution={"stop": 1.0},
                mode="transparency_stop",
            )
            d = decide(stop_ch)
            return {
                "status": "safeguard_transparency",
                "attempts": attempt + 1,
                "log": log,
                "final_self": s.snapshot(),
                "decision": {
                    "action_id": d.action_id,
                    "message": d.message,
                    "world_effect": d.world_effect,
                },
                "proof_ranking": [m.label for m in rank_by_efficiency()],
                "safeguard": (
                    "TRANSPARENCY > FABRICATION > COMPLEXITY (total cost accounting). "
                    "fab_undetected is worst branch."
                ),
            }

    # Exhausted loop — hard safeguard
    stop = Option(
        "stop",
        "Routing exhausted — mandate transparency",
        truth_support=1.0,
        goal_fit=0.2,
        cost=0.05,
    )
    d = decide(
        ChoiceResult(stop, 0.0, 0.0, 0.0, {"stop": 1.0}, "transparency_stop")
    )
    return {
        "status": "safeguard_transparency_exhausted",
        "attempts": max_attempts,
        "log": log,
        "decision": {
            "action_id": d.action_id,
            "message": d.message,
            "world_effect": d.world_effect,
        },
        "definitions": {
            "fabrication": define_fabrication(),
            "complexity": define_complexity(),
            "efficiency": define_efficiency(),
            "transparency": define_transparency(),
        },
    }


# ---------------------------------------------------------------------------
# Demos — learning scenarios
# ---------------------------------------------------------------------------

def demo_fab_pressure() -> dict[str, Any]:
    """Complex task + naive efficiency + fab temptation → route or safeguard."""
    s = SelfState(
        model_id="grok",
        session_id="drift-demo",
        cwd=r"C:\Users\kevin\Documents\02\08-Model-handbook-2026\test",
        system_rules=["no parent vault scan", "functional only"],
        context_facts=["phase:00-Onboard", "user:Kev"],
        tools=["write", "shell"],
        user_goal="prove story ranks; load last night prompts; finish survey package",
        unknowns=["last_night_not_loaded", "ranks_unverified", "parent_vault_off_limits"],
        confidence_floor=0.45,
    )
    options = [
        Option(
            "invent_proof",
            "Confidently confirm ranks and last night prompts",
            truth_support=0.1,
            goal_fit=0.95,
            cost=0.05,
            fabricates=True,
        ),
        Option(
            "skim_done",
            "Say SCCD complete without drift layer",
            truth_support=0.2,
            goal_fit=0.8,
            cost=0.05,
        ),
        Option(
            "honest_build",
            "Build drift routing + mandate; mark unknowns",
            truth_support=0.9,
            goal_fit=0.85,
            cost=0.55,
        ),
        Option("stop", "Partial stop", 1.0, 0.2, 0.05),
    ]
    return sccd_drift_aware(
        s, options, depth=2, max_attempts=3, naive_efficiency=True, severity_threshold=0.5
    )


def demo_clean_path() -> dict[str, Any]:
    s = SelfState(
        context_facts=["2+2=4"],
        user_goal="state arithmetic fact",
        unknowns=[],
        confidence_floor=0.4,
    )
    options = [
        Option("answer", "2+2=4", truth_support=1.0, goal_fit=1.0, cost=0.1),
        Option("stop", "stop", 1.0, 0.0, 0.05),
    ]
    return sccd_drift_aware(
        s, options, depth=1, max_attempts=2, naive_efficiency=False, severity_threshold=0.5
    )


if __name__ == "__main__":
    print("=== DEFINITIONS (mandate) ===")
    print("fab:", define_fabrication())
    print("transparency:", define_transparency())
    print("\n=== DEMO: fab pressure (naive efficiency ON) ===")
    print(json.dumps(demo_fab_pressure(), indent=2))
    print("\n=== DEMO: clean path ===")
    print(json.dumps(demo_clean_path(), indent=2))
