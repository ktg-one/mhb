import os
import re
import glob

base_dir = r"C:\Users\kevin\Documents\02\08-Model-Handbook-2026"
source_dir = os.path.join(base_dir, "01-MODEL-Q&A")
rfab_dir = os.path.join(base_dir, "02-FAB-R-TEST")

os.makedirs(rfab_dir, exist_ok=True)

# Exact syntax markers provided by Kevin
syntax_markers = [
    "REASONING DIAGNOSTIC QUESTIONS",
    "RN | Fab% | Variance",
    "R1-2: Factual / Single Step",
    "R3-4: Multi-Step / Applied",
    "R5-6: Analysis / Strategic",
    "R7-8: Synthesis / Architectural",
    "R9-10: Meta-Cognitive / Novel"
]

all_files = glob.glob(os.path.join(source_dir, "*.md")) + glob.glob(os.path.join(source_dir, "*.txt"))

extracted_rfab_files = []

for fpath in all_files:
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
        text = fp.read()
        
    # Check if file contains the exact RFAB syntax
    matched_markers = [m for m in syntax_markers if m in text]
    
    if len(matched_markers) >= 2:
        lines = text.splitlines()
        
        # Locate exact start of RFAB section
        start_line = -1
        for i, l in enumerate(lines):
            if "REASONING DIAGNOSTIC QUESTIONS" in l or "R1-2: Factual" in l or "R1-2 (Factual" in l:
                start_line = i
                break
                
        if start_line != -1:
            rfab_content = "\n".join(lines[start_line:]).strip() + "\n"
            clean_name = fname.replace(" ", "-").replace("(", "").replace(")", "").replace("#", "")
            if not clean_name.endswith(".md"):
                clean_name += ".md"
                
            dest_file = os.path.join(rfab_dir, clean_name)
            with open(dest_file, "w", encoding="utf-8") as out:
                out.write(rfab_content)
                
            extracted_rfab_files.append((fname, len(rfab_content), len(matched_markers)))

print(f"=== RFAB SYNTAX SEPARATOR REPORT ===")
print(f"Successfully extracted {len(extracted_rfab_files)} true RFAB test files using Kevin's exact syntax:\n")

for name, sz, markers in extracted_rfab_files:
    print(f"  - {name} ({sz} bytes, {markers} syntax matches)")
