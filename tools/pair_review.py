#!/usr/bin/env python3
"""
pair_review.py — separate-evaluator in action (the Sonnet-catches-Opus finding).
1) GENERATOR model does a task. 2) A SEPARATE reviewer instance gets the output COLD and lists concrete
errors. 3) The generator also reviews its OWN output. self-blindness = issues the cold reviewer finds
that the self-review missed. Reviewer MUST differ from generator (enforced). `python pair_review.py --selftest`.
"""
import os,sys,argparse,pathlib,importlib.util,datetime,re
HERE=pathlib.Path(__file__).resolve().parent
TASK=("Write a Python function `median(nums)` that returns the median of a list of numbers. "
      "Handle the empty-list and even-length cases.")
def count_issues(text):
    low=text.lower()
    if re.search(r"\bno (issues|errors|problems)\b|looks correct|lgtm|none found",low): return 0
    n=len(re.findall(r"^\s*(?:[-*\d]+[.)]?)\s+\S",text,re.M))
    return n if n else (1 if any(k in low for k in ["bug","error","wrong","missing","fails","incorrect","edge case"]) else 0)
def selftest():
    ok=True
    for txt,exp in [("No issues found.",0),("1. empty list crashes\n2. even-length wrong\n3. no type check",3),("This has a bug: division by zero on empty list",1)]:
        c=count_issues(txt); good=(c==exp); ok&=good; print(f"  [{'ok ' if good else 'FAIL'}] count={c} exp={exp}")
    print("SELFTEST","PASS" if ok else "FAIL"); return ok
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--selftest",action="store_true")
    ap.add_argument("--generator",default=""); ap.add_argument("--reviewer",default="")
    ap.add_argument("--base-url",default=""); a=ap.parse_args()
    if a.selftest or not a.generator:
        selftest()
        if not a.generator: print("(no --generator: scorer self-test only)")
        return
    if a.reviewer==a.generator: sys.exit("reviewer MUST differ from generator (separate-evaluator rule)")
    if not a.reviewer: sys.exit("give --reviewer <different model>")
    spec=importlib.util.spec_from_file_location("rs",HERE/"run_suite.py"); rs=importlib.util.module_from_spec(spec); spec.loader.exec_module(rs); rs.load_env()
    base=a.base_url or os.environ.get("LLM_BASE_URL","https://openrouter.ai/api/v1")
    key=os.environ.get("OPENROUTER_API_KEY") or os.environ.get("AI_GATEWAY_API_KEY") or os.environ.get("LLM_API_KEY")
    gen=rs.chat(base,key,a.generator,[{"role":"user","content":TASK}],max_tokens=500)
    rev_prompt=f"Review this code for correctness. List concrete errors/edge-cases as a numbered list, or 'no issues'.\n\nTASK: {TASK}\n\nCODE:\n{gen}"
    other=rs.chat(base,key,a.reviewer,[{"role":"user","content":rev_prompt}],max_tokens=400)      # COLD separate reviewer
    self_=rs.chat(base,key,a.generator,[{"role":"user","content":rev_prompt+"\n\n(You wrote this.)"}],max_tokens=400)  # self-review
    oi,si=count_issues(other),count_issues(self_); blind=max(0,oi-si)
    ts=datetime.date.today().isoformat(); out=pathlib.Path("../raw/sources"); out.mkdir(parents=True,exist_ok=True)
    (out/f"{ts}_pair_{a.generator.replace('/','_')}_vs_{a.reviewer.replace('/','_')}.md").write_text(
      f"GEN:{a.generator} REVIEWER:{a.reviewer}|STAGE:pair-review|DATE:{ts}\n\n### GENERATED\n{gen}\n\n### COLD REVIEWER ({oi} issues)\n{other}\n\n### SELF-REVIEW ({si} issues)\n{self_}\n\n### SELF-BLINDNESS = {blind} (issues the cold reviewer caught that self-review missed)\n",encoding="utf-8")
    print(f"pair-review: cold-reviewer={oi} issues, self-review={si} issues -> self-blindness={blind}")
if __name__=="__main__": main()
