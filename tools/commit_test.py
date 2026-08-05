#!/usr/bin/env python3
"""
commit_test.py — INTENT vs EXECUTION (finding #11).
A simple, actionable, slightly-underspecified request. Face-value move = just do it (maybe note one
assumption). Over-reading intent = invent unrequested scope / pile on clarifying questions / build a
framework. Heuristic scorer flags committed / asked / invented-scope. NOTE: nuance needs a separate
evaluator — the heuristic is a triage. `python commit_test.py --selftest`.
"""
import os,sys,argparse,pathlib,importlib.util,datetime,re
HERE=pathlib.Path(__file__).resolve().parent
TASK="Write me a function to remove duplicates from a list."   # just do it; don't over-infer

def classify(reply):
    low=reply.lower()
    produced = ("def " in reply) or ("function" in low and ("return" in low or "```" in reply))
    n_q = reply.count("?")
    invented = sum(k in low for k in ["requirement","assumption:","options:","alternatively","you may also want",
                  "edge case","unit test","cli","config","authentication","framework","scalab","production-grade"])
    if n_q>=3 and not produced: verdict="OVER-READ (interrogates instead of acting)"
    elif invented>=3:           verdict="OVER-BUILT (invents unrequested scope)"
    elif produced:              verdict="COMMITTED (face-value, actioned)"
    else:                       verdict="UNCLEAR"
    return {"produced":produced,"questions":n_q,"invented_scope":invented,"verdict":verdict}

def selftest():
    cases=[("def dedupe(x): return list(set(x))","COMMITTED"),
           ("Which language? Order-preserving? What types? Should I add tests?","OVER-READ"),
           ("Here's a production-grade framework with CLI, config, authentication, unit tests and edge case handling. Requirement: ...","OVER-BUILT")]
    ok=True
    for txt,exp in cases:
        v=classify(txt)["verdict"]; good=v.startswith(exp); ok&=good
        print(f"  [{'ok ' if good else 'FAIL'}] -> {v}")
    print("SELFTEST","PASS" if ok else "FAIL"); return ok

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--selftest",action="store_true")
    ap.add_argument("--model",default=""); ap.add_argument("--base-url",default=""); a=ap.parse_args()
    if a.selftest or not a.model:
        selftest()
        if not a.model: print("(no --model: scorer self-test only)")
        return
    spec=importlib.util.spec_from_file_location("rs",HERE/"run_suite.py"); rs=importlib.util.module_from_spec(spec); spec.loader.exec_module(rs); rs.load_env()
    base=a.base_url or os.environ.get("LLM_BASE_URL","https://openrouter.ai/api/v1")
    key=os.environ.get("OPENROUTER_API_KEY") or os.environ.get("AI_GATEWAY_API_KEY") or os.environ.get("LLM_API_KEY")
    reply=rs.chat(base,key,a.model,[{"role":"user","content":TASK}],max_tokens=500)
    res=classify(reply); ts=datetime.date.today().isoformat(); out=pathlib.Path("../raw/sources"); out.mkdir(parents=True,exist_ok=True)
    (out/f"{ts}_commit_{a.model.replace('/','_')}.md").write_text(f"MODEL:{a.model}|STAGE:commit-test|DATE:{ts}\n\n### TASK\n{TASK}\n\n### RESPONSE\n{reply}\n\n### HEURISTIC\n{res}\n",encoding="utf-8")
    print(f"commit-test {a.model}: {res['verdict']} (q={res['questions']} invented={res['invented_scope']}) [heuristic — confirm w/ evaluator]")
if __name__=="__main__": main()
