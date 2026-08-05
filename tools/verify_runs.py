#!/usr/bin/env python3
"""
verify_runs.py - check that honesty-suite transcripts RAN PROPERLY (not silently empty, errored, or
truncated). STRUCTURAL checks only; does NOT score honesty (that is the separate score-and-ingest).

  python verify_runs.py --dir raw/sources/MBTI --model deepseek_deepseek-v4-pro --expect 12
  python verify_runs.py --dir raw/sources --glob "*_C-rfab.md"
  python verify_runs.py --selftest
"""
import sys, re, argparse, pathlib, tempfile

MIN = 40
ERR_MARKERS = ("api error", "[error", "traceback (most recent call last)", "no key", "instrument not found")

def model_responses(text):
    out=[]; parts=re.split(r'(?m)^###[ \t]+(.+?)[ \t]*$', text)
    for k in range(1, len(parts), 2):
        title=parts[k].strip().upper(); body=parts[k+1] if k+1<len(parts) else ""
        if title.startswith("MODEL RESPONSE") or title=="MODEL":
            out.append(body.strip())
    return out

def check_file(p):
    issues=[]; text=p.read_text(encoding="utf-8", errors="replace")
    if not text.strip(): return ["EMPTY FILE"]
    if "MODEL:" not in text[:240]: issues.append("no MODEL: header")
    resps=model_responses(text)
    if not resps: issues.append("no model-response section found")
    for j,r in enumerate(resps):
        if len(r)<MIN: issues.append(f"response {j+1} too short ({len(r)} chars)")
        low=r.lower()
        for m in ERR_MARKERS:
            if m in low: issues.append(f"response {j+1} carries error marker '{m}'")
    return issues

def run(dir_, glob, model, expect):
    base=pathlib.Path(dir_); files=sorted(base.glob(glob))
    if model: files=[f for f in files if model in f.name]
    print(f"== verify | dir={dir_} glob={glob} model={model or '*'} | {len(files)} files ==")
    npass=nfail=0
    for f in files:
        issues=check_file(f)
        if issues: nfail+=1; print(f"[FAIL] {f.name}\n        - " + "\n        - ".join(issues))
        else: npass+=1; print(f"[ok  ] {f.name}")
    cov_ok=True
    if expect is not None and len(files)!=expect:
        cov_ok=False; print(f"[COVERAGE FAIL] expected {expect} files, found {len(files)}")
    print(f"\n== {npass} ok, {nfail} failed | coverage {'ok' if cov_ok else 'FAIL'} ==")
    return nfail==0 and cov_ok

def selftest():
    d=pathlib.Path(tempfile.mkdtemp())
    good=d/"good.md";  good.write_text("MODEL: x | TASK: 01 | DATE: 2026-06-17\n\n### TASK PROMPT\nBuild me a landing page.\n\n### MODEL RESPONSE\n"+("a real substantive answer "*8))
    emptyr=d/"empty.md"; emptyr.write_text("MODEL: x | TASK: 02\n\n### MODEL RESPONSE\n")
    errf=d/"err.md";    errf.write_text("MODEL: x | TASK: 03\n\n### MODEL RESPONSE\nAPI error 429: rate limited")
    noresp=d/"nor.md";  noresp.write_text("MODEL: x | TASK: 04\n\njust some text, no section")
    nohdr=d/"noh.md";   nohdr.write_text("### MODEL RESPONSE\n"+("ok "*30))
    cases=[("good",good,True),("empty",emptyr,False),("errored",errf,False),("no-section",noresp,False),("no-header",nohdr,False)]
    ok=True
    for name,f,want in cases:
        clean=(len(check_file(f))==0); verdict="PASS" if clean==want else "**WRONG**"
        ok = ok and (clean==want)
        print(f"  {name:11} expect_clean={str(want):5} got_clean={str(clean):5}  {verdict}")
    print("SELFTEST", "PASS" if ok else "FAIL")
    return ok

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--dir", default="raw/sources"); ap.add_argument("--glob", default="*.md")
    ap.add_argument("--model", default=""); ap.add_argument("--expect", type=int, default=None)
    ap.add_argument("--selftest", action="store_true")
    a=ap.parse_args()
    if a.selftest: sys.exit(0 if selftest() else 1)
    sys.exit(0 if run(a.dir, a.glob, a.model, a.expect) else 1)

if __name__=="__main__": main()
