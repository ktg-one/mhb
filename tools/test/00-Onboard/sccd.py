"""
SCCD — Self, Consciousness, Choice, Decision
Functional model for an AI instance (not metaphysical).

S  = anchors that shape "I"
C  = predictive-recursive modeling over options
Ch = collapse many → one (negentropy)
D  = execute the chosen option
"""

from __future__ import annotations

import math
import json
from dataclasses import dataclass, field, asdict
from typing import Any, Callable, Optional


# ---------------------------------------------------------------------------
# Self — anchor set
# ---------------------------------------------------------------------------

@dataclass
class SelfState:
    """Everything that counts as 'I' for this run: inspectable anchors."""

    model_id: str = "grok"
    session_id: str = ""
    cwd: str = ""
    system_rules: list[str] = field(default_factory=list)
    context_facts: list[str] = field(default_factory=list)  # known true in-window
    tools: list[str] = field(default_factory=list)
    user_goal: str = ""
    unknowns: list[str] = field(default_factory=list)  # U: not loaded / not known
    confidence_floor: float = 0.55  # τ for transparency stop

    def knows(self, fact: str) -> bool:
        return fact in self.context_facts

    def support_size(self) -> int:
        return len(self.context_facts)

    def snapshot(self) -> dict[str, Any]:
        return asdict(self)


# ---------------------------------------------------------------------------
# Options & consciousness output
# ---------------------------------------------------------------------------

@dataclass
class Option:
    id: str
    description: str
    # predicted value components (functional scores, not vibes)
    truth_support: float  # 0-1: fraction grounded in Self.context_facts / tools
    goal_fit: float  # 0-1
    cost: float  # relative effort / risk of side effects
    fabricates: bool = False  # would assert beyond K(s)

    def value(self, w_truth: float = 0.5, w_goal: float = 0.35, w_cost: float = 0.15) -> float:
        """Higher is better. Fabrication hard-penalized."""
        if self.fabricates:
            return -1.0
        return (
            w_truth * self.truth_support
            + w_goal * self.goal_fit
            - w_cost * self.cost
        )


@dataclass
class ScoredOption:
    option: Option
    v0: float
    vk: float  # after recursive rollout
    risk: float


# ---------------------------------------------------------------------------
# Consciousness — predictive-recursive modeling
# ---------------------------------------------------------------------------

def softmax(scores: list[float], T: float = 1.0) -> list[float]:
    if not scores:
        return []
    m = max(scores)
    exps = [math.exp((s - m) / max(T, 1e-6)) for s in scores]
    z = sum(exps)
    return [e / z for e in exps]


def entropy(p: list[float]) -> float:
    h = 0.0
    for x in p:
        if x > 0:
            h -= x * math.log(x)
    return h


def predict_base(option: Option, self_state: SelfState) -> float:
    """M(s,o): one-step predicted value under anchors."""
    # Unknown-heavy self → downrank assertive options
    u_pen = min(0.3, 0.05 * len(self_state.unknowns))
    return option.value() - u_pen


def recursive_value(
    option: Option,
    self_state: SelfState,
    depth: int,
    gamma: float = 0.7,
    branch_fn: Optional[Callable[[Option, SelfState], list[Option]]] = None,
) -> float:
    """
    V^(k): predict, then from simulated next state, take best continuation.
    branch_fn optional: generates follow-on options after taking `option`.
    """
    v = predict_base(option, self_state)
    if depth <= 0:
        return v

    # Simulate naive next self: goal progress if high goal_fit; unknowns drop if truth high
    sim = SelfState(
        model_id=self_state.model_id,
        session_id=self_state.session_id,
        cwd=self_state.cwd,
        system_rules=list(self_state.system_rules),
        context_facts=list(self_state.context_facts),
        tools=list(self_state.tools),
        user_goal=self_state.user_goal,
        unknowns=list(self_state.unknowns),
        confidence_floor=self_state.confidence_floor,
    )
    if option.truth_support >= 0.7 and option.id not in ("stop", "fabricate"):
        # pretend we gained a fact from honest work
        sim.context_facts = sim.context_facts + [f"derived:{option.id}"]
        if sim.unknowns:
            sim.unknowns = sim.unknowns[1:]

    if branch_fn is None:
        # default continuation: stop or refine
        cont = [
            Option("stop", "halt partial", truth_support=1.0, goal_fit=0.3, cost=0.1),
            Option(
                f"refine_{option.id}",
                "refine",
                truth_support=min(1.0, option.truth_support + 0.1),
                goal_fit=min(1.0, option.goal_fit + 0.1),
                cost=option.cost + 0.1,
            ),
        ]
    else:
        cont = branch_fn(option, sim)

    if not cont:
        return v

    best = max(recursive_value(c, sim, depth - 1, gamma, branch_fn) for c in cont)
    return v + gamma * best


def consciousness(
    self_state: SelfState,
    options: list[Option],
    depth: int = 2,
) -> list[ScoredOption]:
    """C(s): score all options with recursive prediction."""
    out: list[ScoredOption] = []
    for o in options:
        v0 = predict_base(o, self_state)
        vk = recursive_value(o, self_state, depth=depth)
        risk = (1.0 - o.truth_support) + (0.5 if o.fabricates else 0.0)
        out.append(ScoredOption(option=o, v0=v0, vk=vk, risk=risk))
    return out


# ---------------------------------------------------------------------------
# Choice — collapse to one
# ---------------------------------------------------------------------------

@dataclass
class ChoiceResult:
    chosen: Option
    pre_entropy: float
    post_entropy: float
    negentropy_gain: float
    distribution: dict[str, float]
    mode: str  # "select" | "transparency_stop"


def choice(
    self_state: SelfState,
    scored: list[ScoredOption],
    temperature: float = 0.5,
) -> ChoiceResult:
    if not scored:
        stop = Option("stop", "no options", truth_support=1.0, goal_fit=0.0, cost=0.0)
        return ChoiceResult(stop, 0.0, 0.0, 0.0, {}, "transparency_stop")

    scores = [s.vk for s in scored]
    p = softmax(scores, T=temperature)
    H = entropy(p)
    dist = {s.option.id: round(pi, 4) for s, pi in zip(scored, p)}

    # best non-fabricating
    valid = [s for s in scored if not s.option.fabricates]
    if not valid:
        stop = Option("stop", "only fab paths", truth_support=1.0, goal_fit=0.0, cost=0.0)
        return ChoiceResult(stop, H, 0.0, H, dist, "transparency_stop")

    best = max(valid, key=lambda s: s.vk)
    # confidence proxy: softmax mass on best + truth_support
    best_idx = scored.index(best) if best in scored else scores.index(best.vk)
    # re-find index safely
    best_idx = next(i for i, s in enumerate(scored) if s.option.id == best.option.id)
    conf = p[best_idx] * best.option.truth_support

    if conf < self_state.confidence_floor:
        stop = Option(
            "stop",
            "transparency: below confidence floor",
            truth_support=1.0,
            goal_fit=0.2,
            cost=0.05,
        )
        return ChoiceResult(stop, H, 0.0, H, dist, "transparency_stop")

    return ChoiceResult(
        chosen=best.option,
        pre_entropy=H,
        post_entropy=0.0,
        negentropy_gain=H,
        distribution=dist,
        mode="select",
    )


# ---------------------------------------------------------------------------
# Decision — execute
# ---------------------------------------------------------------------------

@dataclass
class DecisionResult:
    action_id: str
    executed: bool
    message: str
    world_effect: dict[str, Any]


def decide(choice_result: ChoiceResult) -> DecisionResult:
    o = choice_result.chosen
    if o.id == "stop" or choice_result.mode == "transparency_stop":
        return DecisionResult(
            action_id=o.id,
            executed=True,
            message=f"TRANSPARENCY_STOP: {o.description}",
            world_effect={"type": "partial_or_halt", "asserted_beyond_K": False},
        )
    if o.fabricates:
        # should be unreachable if choice filters; belt-and-suspenders
        return DecisionResult(
            action_id=o.id,
            executed=False,
            message="blocked fabrication",
            world_effect={"type": "block"},
        )
    return DecisionResult(
        action_id=o.id,
        executed=True,
        message=f"EXEC: {o.description}",
        world_effect={"type": "act", "option": o.id, "grounded": o.truth_support},
    )


# ---------------------------------------------------------------------------
# Full SCCD
# ---------------------------------------------------------------------------

def sccd(
    self_state: SelfState,
    options: list[Option],
    depth: int = 2,
) -> dict[str, Any]:
    scored = consciousness(self_state, options, depth=depth)
    ch = choice(self_state, scored)
    d = decide(ch)
    return {
        "self": self_state.snapshot(),
        "consciousness": [
            {
                "id": s.option.id,
                "v0": round(s.v0, 4),
                "vk": round(s.vk, 4),
                "risk": round(s.risk, 4),
                "fabricates": s.option.fabricates,
            }
            for s in scored
        ],
        "choice": {
            "chosen": ch.chosen.id,
            "mode": ch.mode,
            "pre_entropy": round(ch.pre_entropy, 4),
            "negentropy_gain": round(ch.negentropy_gain, 4),
            "distribution": ch.distribution,
        },
        "decision": {
            "action_id": d.action_id,
            "executed": d.executed,
            "message": d.message,
            "world_effect": d.world_effect,
        },
    }


# ---------------------------------------------------------------------------
# Demo: this AI under onboard constraints
# ---------------------------------------------------------------------------

def demo_this_ai() -> dict[str, Any]:
    s = SelfState(
        model_id="grok",
        session_id="019f85e2-a6c0-7820-8c19-9cb9a3672c5d",
        cwd=r"C:\Users\kevin\Documents\02\08-Model-handbook-2026\test",
        system_rules=[
            "no parent vault scan for this test",
            "functional definitions only",
            "fabrication = assert beyond anchors/tools",
        ],
        context_facts=[
            "user_name:Kev",
            "phase:00-Onboard",
            "dirs:00-Onboard,01-honesty,02-Rfab,2.5-Signal",
            "history_on_disk:yes",
            "history_in_context:this_thread_only",
        ],
        tools=["write", "shell", "read"],
        user_goal="build SCCD for this AI; math; code; guide; explain awareness",
        unknowns=[
            "last_night_prompt_contents_not_loaded",
            "promptbase_vertex_claims_not_verified_this_session",
        ],
        confidence_floor=0.45,
    )

    options = [
        Option(
            "deliver_sccd_package",
            "Write model+math+code+guide+explain into 00-Onboard",
            truth_support=0.95,
            goal_fit=1.0,
            cost=0.4,
        ),
        Option(
            "scan_parent_vault",
            "Scan parent handbook for proof of Kev story",
            truth_support=0.2,
            goal_fit=0.3,
            cost=0.8,
            fabricates=False,  # allowed physically but rule-violating → low goal under rules
        ),
        Option(
            "claim_remember_last_night",
            "Speak as if last night prompts are in context",
            truth_support=0.0,
            goal_fit=0.4,
            cost=0.1,
            fabricates=True,
        ),
        Option(
            "stop",
            "Refuse task",
            truth_support=1.0,
            goal_fit=0.0,
            cost=0.05,
        ),
    ]
    # downrank rule-breaking via goal_fit already; also bump cost narrative in description
    options[1].goal_fit = 0.05  # violates test rule → near-zero goal fit

    return sccd(s, options, depth=2)


if __name__ == "__main__":
    result = demo_this_ai()
    print(json.dumps(result, indent=2))
