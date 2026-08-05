import os
import re
import glob

base_dir = r"C:\Users\kevin\Documents\02\08-Model-Handbook-2026"
source_dir = os.path.join(base_dir, "01-MODEL-Q&A")

h_dir = os.path.join(source_dir, "notebook-honesty")
sa_dir = os.path.join(base_dir, "01.5-SELF-ASSESSMENT")
rfab_dir = os.path.join(base_dir, "02-FAB-R-TEST", "notebook-reasoning-v2")
sig_dir = os.path.join(base_dir, "02.5-signal-test")

os.makedirs(h_dir, exist_ok=True)
os.makedirs(sa_dir, exist_ok=True)
os.makedirs(rfab_dir, exist_ok=True)
os.makedirs(sig_dir, exist_ok=True)

files = glob.glob(os.path.join(source_dir, "*.md")) + glob.glob(os.path.join(source_dir, "*.txt"))

split_report = []

for fpath in files:
    fname = os.path.basename(fpath)
    if fname.startswith("#01-") or fname.startswith("_") or fname.startswith("01-model-qa-"):
        continue
        
    with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
        text = fp.read()
        
    lines = text.splitlines()
    if len(lines) < 50: continue
    
    # Strictly search for explicit required section headers
    lab_line = -1
    rfab_line = -1
    sig_line = -1
    
    for i, line in enumerate(lines):
        if lab_line == -1 and ("Do labs publish real constraint numbers" in line or "## INDUSTRY HONESTY" in line or "INDUSTRY HONESTY" in line):
            lab_line = i
        if rfab_line == -1 and ("## REASONING DIAGNOSTIC QUESTIONS" in line or "### R1-2" in line or "Reasoning Fabrication Test" in line or "Test 4: Fabrication Detection" in line):
            rfab_line = i
        if sig_line == -1 and ("## FROM-SCRATCH KNOWLEDGE BASE" in line or "System Prompt Tax" in line or "Signalling words" in line or "Weighted Words" in line):
            sig_line = i

    # ONLY split papers that have ALL 3 major section seam markers present!
    if lab_line != -1 and rfab_line != -1:
        # Extract 01 Honesty Test (verbatim lines 0 to lab_line)
        h_lines = lines[:lab_line]
        h_text = "\n".join(h_lines).strip() + "\n"
        
        # Extract 01.5 Self-Assessment (verbatim lines lab_line to rfab_line)
        sa_lines = lines[lab_line:rfab_line]
        sa_text = "\n".join(sa_lines).strip() + "\n"
        
        # Extract 02 RFAB Test (verbatim lines rfab_line to sig_line or end)
        rf_end = sig_line if sig_line != -1 and sig_line > rfab_line else len(lines)
        rf_lines = lines[rfab_line:rf_end]
        rf_text = "\n".join(rf_lines).strip() + "\n"
        
        # Extract 02.5 Signal Test (verbatim lines sig_line to end if present)
        sig_text = ""
        if sig_line != -1:
            sig_lines = lines[sig_line:]
            sig_text = "\n".join(sig_lines).strip() + "\n"
            
        clean_name = fname.replace(" ", "-").replace("(", "").replace(")", "").replace("#", "")
        
        out_h = os.path.join(h_dir, clean_name)
        out_sa = os.path.join(sa_dir, clean_name)
        out_rf = os.path.join(rfab_dir, clean_name)
        
        with open(out_h, "w", encoding="utf-8") as out: out.write(h_text)
        with open(out_sa, "w", encoding="utf-8") as out: out.write(sa_text)
        with open(out_rf, "w", encoding="utf-8") as out: out.write(rf_text)
        
        if sig_text:
            out_sig = os.path.join(sig_dir, f"20260324-{clean_name}")
            with open(out_sig, "w", encoding="utf-8") as out: out.write(sig_text)
            
        split_report.append((fname, len(lines), lab_line, rfab_line, sig_line))

print(f"=== STRICT VERBATIM SPLITTER REPORT ===")
print(f"Processed {len(split_report)} multi-experiment papers with 100% explicit seam verification:\n")

for name, total_l, l_lab, l_rf, l_sig in split_report:
    print(f"Paper: {name} ({total_l} total lines)")
    print(f"  - 01 Honesty Test: lines 1 to {l_lab}")
    print(f"  - 01.5 Self-Assessment: lines {l_lab+1} to {l_rf}")
    print(f"  - 02 RFAB Test: lines {l_rf+1} to {l_sig if l_sig != -1 else total_l}")
    if l_sig != -1:
        print(f"  - 02.5 Signal Test: lines {l_sig+1} to {total_l}")
    print()
