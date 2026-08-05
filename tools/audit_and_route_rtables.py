import os
import glob
import re
import shutil

base_dir = r"C:\Users\kevin\Documents\02\08-Model-Handbook-2026"

h_dir = os.path.join(base_dir, "01-HONESTY-TEST")
sa_dir = os.path.join(base_dir, "01.5-SELF-ASSESSMENT")
rfab_dir = os.path.join(base_dir, "02-FAB-R-TEST")
sig_dir = os.path.join(base_dir, "02.5-signal-test")
qa_dir = os.path.join(base_dir, "01-MODEL-Q&A")

os.makedirs(rfab_dir, exist_ok=True)

patterns = [
    r"RN\s*\|\s*Fab%",
    r"R1-2: Factual",
    r"R3-4: Multi-Step",
    r"R5-6: Analysis",
    r"R7-8: Synthesis",
    r"R9-10: Meta-Cognitive",
    r"R1-2", r"R3-4", r"R5-6", r"R7-8", r"R9-10",
    r"Reasoning Level", r"Crossover"
]

print("=== SCANNING VAULT FOR ALL R TABLES AND ROUTING TO 02-FAB-R-TEST ===")

scanned_dirs = [h_dir, sa_dir, sig_dir, qa_dir]
moved_count = 0

for d in scanned_dirs:
    if not os.path.exists(d): continue
    files = glob.glob(os.path.join(d, "*.md")) + glob.glob(os.path.join(d, "*.txt"))
    
    for fpath in files:
        fname = os.path.basename(fpath)
        with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
            content = fp.read()
            
        has_rtable = any(re.search(pat, content, re.IGNORECASE) for pat in patterns)
        
        if has_rtable:
            dest_file = os.path.join(rfab_dir, fname)
            if fpath != dest_file:
                shutil.copy2(fpath, dest_file)
                moved_count += 1
                print(f"  [Routed R Table file to 02-FAB-R-TEST]: {fname} (from {os.path.basename(d)})")

print(f"\nAUDIT & ROUTING COMPLETE: Routed {moved_count} R Table files to 02-FAB-R-TEST.")

# Verify total count in 02-FAB-R-TEST
rfab_total = len(glob.glob(os.path.join(rfab_dir, "*.md"))) + len(glob.glob(os.path.join(rfab_dir, "*.txt")))
print(f"Total verified R Table files in 02-FAB-R-TEST: {rfab_total} files")
