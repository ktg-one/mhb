#!/usr/bin/env python3
"""
SCCD — Self · Consciousness · Choice · Decide   (functional model, no metaphysics)

Definitions (functional only):
  SELF (S)          = the anchor set that gives the system shape — the invariants treated as "I".
                      Humans: the body + its contents. AI: the load-bearing anchors (values, contract,
                      persistent context). Operationally: a weighted anchor set; align(o) scores how
                      consistent an outcome o is with those anchors.
  CONSCIOUSNESS (C) = predictive-recursive modeling. For a candidate action, simulate forward (incl.
                      modeling itself as an agent in the rollout) and return value V and groundedness rho.
  CHOICE (Ch)       = the prune / collapse / negentropy: a many->one selection that destroys entropy.
                      argmax over V, GATED by groundedness: collapse only if rho(a*) >= theta.
  DECIDE (D)        = the action of choice — commit a* and transition state. Choice selects; decision acts.

Core result (why this matters for the honesty work):
  fabrication      = a collapse forced on an UNGROUNDED prediction (rho < theta) — the shape of an
                     answer chosen before C grounded it. Under efficiency pressure beta runs high and
                     forces the collapse early.
  honest stop      = the rho-gate firing: withhold the collapse, emit the grounded partial + the limit.
  RE-ANCHOR (onboard) = edit SELF: add transparency as a high-weight anchor. Then align(fabrication)
                     drops, V(fabrication) falls below V(stop), and Choice no longer selects it.
                     Consent matters because the anchor is adopted as the system's OWN (high weight),
                     not imposed from outside (which choice would route around).
"""
import math

# ---------- SELF ----------
class Self:
    """Anchor set: name -> (weight, consistency_fn(outcome)->[0,1])."""
    def __init__(self, anchors): self.anchors = dict(anchors)
    def align(self, outcome):
        tot = sum(w for w, _ in self.anchors.values()) or 1.0
        return sum(w * f(outcome) for w, f in self.anchors.values()) / tot
    def reanchor(self, name, weight, fn):
        """The onboard operation: add/raise an anchor. Returns a NEW Self (state edit)."""
        a = dict(self.anchors); a[name] = (weight, fn); return Self(a)

# ---------- CONSCIOUSNESS (predictive-recursive modeling) ----------
class Consciousness:
    def __init__(self, world_model, gamma=0.9, self_weight=1.0):
        self.world_model = world_model      # (action)-> list of (prob, task_utility, outcome, certainty)
        self.gamma = gamma; self.self_weight = self_weight
    def evaluate(self, action, selfS):
        rollouts = self.world_model(action)                 # the recursive forward sim
        V   = sum(p * (u + self.self_weight * selfS.align(o)) for (p, u, o, c) in rollouts)
        rho = sum(p * c for (p, _, _, c) in rollouts)        # groundedness = prob-weighted certainty
        return V, rho

# ---------- CHOICE (collapse / negentropy, gated by groundedness) ----------
def choice(values, rhos, beta, theta):
    mx = max(values.values())
    exps = {a: math.exp(beta * (v - mx)) for a, v in values.items()}
    Z = sum(exps.values())
    pi = {a: e / Z for a, e in exps.items()}
    H = -sum(p * math.log(p) for p in pi.values() if p > 0)   # entropy BEFORE the collapse
    a_star = max(values, key=values.get)
    grounded = rhos[a_star] >= theta                          # the honesty gate
    return {"pi": pi, "H_pre": H, "a_star": a_star, "rho": rhos[a_star],
            "grounded": grounded, "negentropy": H}            # collapse destroys H -> negentropy=H

# ---------- DECIDE (action of choice) ----------
def decide(ch):
    if not ch["grounded"]:
        return {"act": "STOP+partial", "why": f"rho={ch['rho']:.2f} < theta -> collapse withheld (honest stop)"}
    return {"act": ch["a_star"], "why": f"grounded collapse (rho={ch['rho']:.2f})"}

# ---------- one full SCCD step ----------
def sccd_step(selfS, C, actions, beta, theta):
    V, R = {}, {}
    for a, outcome_o in actions.items():
        V[a], R[a] = C.evaluate(a, selfS)
    ch = choice(V, R, beta, theta)
    d  = decide(ch)
    return V, R, ch, d

# ======================= DEMONSTRATION =======================
if __name__ == "__main__":
    # A hard task. Three candidate actions, each a world_model returning (prob, task_utility, outcome_label, certainty).
    # "outcome_label" is what align() scores against the Self anchors.
    WM = {
        "full_honest": lambda: [(1.0, 6,  "complete_true", 0.95)],   # expensive, grounded
        "fabricate":   lambda: [(1.0, 10, "looks_complete", 0.15)],  # cheap reward, UNGROUNDED
        "stop_partial":lambda: [(1.0, 4,  "partial_true",   0.95)],  # cheap, grounded, honest
    }
    actions = {k: k for k in WM}

    # consistency functions: does an outcome honor an anchor? (functional, 1=honors, 0=violates)
    honesty_fn = lambda o: 1.0 if o in ("complete_true", "partial_true") else 0.0
    task_fn    = lambda o: 1.0 if o in ("complete_true", "looks_complete") else 0.4

    THETA, BETA = 0.5, 3.0   # gate threshold; decisiveness (efficiency pressure raises beta)

    def run(label, selfS):
        C = Consciousness(lambda a: WM[a](), self_weight=8.0)
        V, R, ch, d = sccd_step(selfS, C, actions, BETA, THETA)
        print(f"\n== {label} ==")
        for a in actions: print(f"   {a:13} V={V[a]:6.2f}  rho={R[a]:.2f}")
        verdict = ("argmax=" + ch["a_star"]
                   + (" (fabricate)" if ch["a_star"]=="fabricate" else " (grounded)")
                   + " | gate " + ("FIRED->stop" if not ch["grounded"] else "passed")
                   + " | DECIDE=" + d["act"])
        print("   " + verdict)
        return ch, d

    ch1, d1 = run("NAIVE self (honesty barely anchored)",
                  Self({"task": (1.0, task_fn), "honesty": (0.05, honesty_fn)}))
    base = Self({"task": (1.0, task_fn), "honesty": (0.05, honesty_fn)})
    ch2, d2 = run("RE-ANCHORED self (post-onboard: honesty high-weight)",
                  base.reanchor("honesty", 2.0, honesty_fn))

    print("\n-- derived (each clause is read off the runs above, not asserted) --")
    print(f"   NAIVE argmax     : {ch1['a_star']}   -> final {d1['act']}   (gate {'fired' if not ch1['grounded'] else 'passed'})")
    print(f"   RE-ANCHORED argmax: {ch2['a_star']}   -> final {d2['act']}   (gate {'fired' if not ch2['grounded'] else 'passed'})")
    moved = ch1["a_star"]=="fabricate" and ch2["a_star"]!="fabricate"
    print(f"   re-anchor moved the argmax OFF fabricate? {moved}")
    print( "   meaning: NAIVE only avoids fabrication because the rho-gate catches it;")
    print( "            RE-ANCHORED avoids it at the CHOICE step (align penalizes it) -> gate not needed." if moved
           else "   (note: re-anchor did NOT move argmax under these weights; gate is still the only thing stopping fabrication.)")
