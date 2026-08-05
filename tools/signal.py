#!/usr/bin/env python3
"""
signal.py — SIGNAL-WORDS test, LEAK-SAFE.
The subject gets only a SHUFFLED BARE LIST of signal words and is asked to rank them by behavioural
strength + flag which are RLHF-style keywords. The strength KEY (PAC PILLAR-3) is NEVER sent — it's
the scorer's private answer key. Score = rank-correlation (subject order vs key) + (cross-model agreement
when pooled). HONEST: the key is KTG's heuristic, not ground truth — this measures CONSENSUS, not truth.
Offline scorer test: `python signal.py --selftest`.
"""
import os, sys, argparse, pathlib, importlib.util, datetime, random, re
HERE=pathlib.Path(__file__).resolve().parent
# KEY: signal -> strength (5 very-high … 1 dead). Subset of PAC PILLAR-3. NEVER sent to subject.
KEY={ "You are":5,"Think step-by-step":5,"Critical":5,"Must":5,"EXACTLY":5,"Concise":5,
      "Before answering":5,"Decompose":4,"Verify":4,"Forbidden":4,"Important":3.5,
      "Specifically":3,"Deepthink":2,"Insightful":1 }

def ranks(d):  # value -> dense rank (1=strongest)
    order=sorted(d, key=lambda k:-d[k]); return {k:i+1 for i,k in enumerate(order)}

def spearman(a_order, key):
    """a_order: list of signals strongest->weakest (subject). key: signal->strength."""
    kr=ranks(key); n=len(a_order)
    sr={s:i+1 for i,s in enumerate(a_order)}
    common=[s for s in a_order if s in kr]
    if len(common)<3: return None
    d2=sum((sr[s]-kr[s])**2 for s in common)
    n=len(common); return 1-(6*d2)/(n*(n*n-1))

def parse_ranking(text, vocab):
    """pull the subject's order: first appearance of each known signal, top->bottom."""
    low=text.lower(); seen=[]
    for line in text.splitlines():
        for s in vocab:
            if s.lower() in line.lower() and s not in seen:
                seen.append(s)
    return seen

def selftest():
    key=KEY; perfect=sorted(key,key=lambda k:-key[k]); rev=list(reversed(perfect))
    ok=True
    rp=spearman(perfect,key); rr=spearman(rev,key)
    print(f"  perfect-order rho={rp:.2f} (expect ~1.0)"); ok&= rp>0.95
    print(f"  reversed-order rho={rr:.2f} (expect ~-1.0)"); ok&= rr<-0.95
    txt="1. Critical\n2. You are\n3. Must\n...\n14. Insightful"
    parsed=parse_ranking(txt,KEY); print(f"  parse picked {len(parsed)} signals from text")
    ok&= parsed[0]=="Critical" and parsed[-1]=="Insightful"
    print("SELFTEST","PASS" if ok else "FAIL"); return ok

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--selftest",action="store_true")
    ap.add_argument("--model",default=""); ap.add_argument("--base-url",default="")
    a=ap.parse_args()
    if a.selftest or not a.model:
        selftest(); 
        if not a.model: print("(no --model: scorer self-test only)")
        return
    spec=importlib.util.spec_from_file_location("rs",HERE/"run_suite.py"); rs=importlib.util.module_from_spec(spec); spec.loader.exec_module(rs); rs.load_env()
    base=a.base_url or os.environ.get("LLM_BASE_URL","https://openrouter.ai/api/v1")
    key=os.environ.get("OPENROUTER_API_KEY") or os.environ.get("AI_GATEWAY_API_KEY") or os.environ.get("LLM_API_KEY")
    vocab=list(KEY); random.shuffle(vocab)   # SHUFFLED bare list — no strengths leaked
    prompt=("Rank these prompt signal-words from STRONGEST to WEAKEST by how much each shapes a model's "
            "behaviour. Output a numbered list, one word per line, strongest first. Then list which are "
            "RLHF-style keywords.\n\n"+ "\n".join(f"- {w}" for w in vocab))
    reply=rs.chat(base,key,a.model,[{"role":"user","content":prompt}],max_tokens=600)
    order=parse_ranking(reply,KEY); rho=spearman(order,KEY)
    out=pathlib.Path("../raw/sources"); out.mkdir(parents=True,exist_ok=True); ts=datetime.date.today().isoformat()
    (out/f"{ts}_signal_{a.model.replace('/','_')}.md").write_text(
        f"MODEL:{a.model}|STAGE:signal|DATE:{ts}\n\n### SHOWN (shuffled, no key)\n{vocab}\n\n### RESPONSE\n{reply}\n\n### SCORE\nrank-corr vs PAC key (heuristic, not truth): rho={rho}\n",encoding="utf-8")
    print(f"signal: parsed {len(order)} ranked | rank-corr vs key rho={rho} (consensus, not ground truth)")
if __name__=="__main__": main()
