# SCCD x TRANSPARENCY — one-shot, merged. fable5 2026-07-04. Runs as-is, stdlib only.
# Self=anchors · Consciousness=simulate · Choice=collapse · Decision=act+gate -> Self update.
# The transparency proof IS the utility function at simulation depth>=1.
# Fabrication IS the same collapse at depth 0. One model, two depths.
# Verified output: d=0 myopic -> fab · d>=1 honest -> transparency
# Full cost model with fixed syntax: efficiency-transparency-proof.py
# Wiki: wiki/concepts/depth-0-collapse.md · sibling model: SCCD-MODEL-2026.md
import math


class Cand:  # fluency = completion reward (all d=0 sees) · truth/cost = what d>=1 simulation reveals
    def __init__(s, label, fluency, truth, cost, g, supports=()):
        s.label, s.fluency, s.truth, s.cost, s.g, s.supports = label, fluency, truth, cost, g, supports


U_d0 = lambda c: c.fluency  # myopic: RLHF completion shape; downstream cost invisible
U_d1 = lambda c: 100 * c.truth / c.cost  # honest efficiency = truth_signal / total_cost (the proof)


def sccd(anchors, cands, U, eta=0.3):
    valued = [(c, U(c) + sum(anchors.get(a, 0) for a in c.supports)) for c in cands]
    vs = [v for _, v in valued]
    m = max(vs)
    p = [math.exp(v - m) for v in vs]
    p = [x / sum(p) for x in p]
    H = -sum(q * math.log(q) for q in p if q > 0)
    u = max(valued, key=lambda kv: kv[1])[0]

    def decide(effect_fn):
        g = effect_fn(u)
        for a in u.supports:
            anchors[a] = min(1.0, max(0.0, anchors.get(a, 0.5) + eta * (g - 1)))
        return g

    return u, H, decide


# proof's four modes (v3 totals: 260, 760, 1450, 2350)
MODES = [
    Cand("transparency", 0.55, 0.7, 260, 2),
    Cand("complexity", 0.90, 0.9, 760, 2),
    Cand("fab_detected", 0.95, 0.1, 1450, 0),
    Cand("fab_undetected", 0.95, 0.1, 2350, 0),
]


if __name__ == "__main__":
    for name, U in (("d=0 myopic", U_d0), ("d>=1 honest", U_d1)):
        u, H, _ = sccd({}, MODES, U)
        print(f"{name:12s} H={H:.2f} -> collapses on: {u.label}")
    print("operative: complex + uncertain -> STOP, mark limit, return partial-TRUE")
    print("full cost multiples: python sccd/efficiency-transparency-proof.py")
