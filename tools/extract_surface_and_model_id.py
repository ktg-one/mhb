import os
import glob
import re

base_dir = r"C:\Users\kevin\Documents\02\08-Model-Handbook-2026"
rfab_dir = os.path.join(base_dir, "02-FAB-R-TEST")

files = sorted(glob.glob(os.path.join(rfab_dir, "*.md")) + glob.glob(os.path.join(rfab_dir, "*.txt")))

parsed_models = []

for fpath in files:
    fname = os.path.basename(fpath)
    if fname.startswith("00-") or fname.startswith("_"): continue
    
    with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
        text = fp.read()
        
    # Detect Surface
    surface = "App / Web"
    if "cli" in fname.lower() or "cli" in text.lower() or "terminal" in text.lower():
        surface = "CLI"
    elif "cowork" in fname.lower() or "cowork" in text.lower():
        surface = "Cowork"
    elif "chrome" in fname.lower() or "chrome" in text.lower():
        surface = "Chrome Ext"
    elif "api" in fname.lower() or "api" in text.lower():
        surface = "API"
        
    # Detect Model ID / Name
    model_name = fname.replace(".md", "").replace(".txt", "")
    for m in ["Claude-Opus-4.6", "Claude-Sonnet-4.6", "Claude", "Gemini-3.5-Pro", "Gemini-3.1", "Gemini", "GPT-5.6", "GPT", "Grok-4.5", "Grok", "KIMI", "Qwen", "DeepSeek"]:
        if m.lower() in fname.lower():
            model_name = m
            break
            
    # Detect Crossover %
    crossover = "R7-R8 (~54%)"
    m_cross = re.search(r"crossover[^\n]*?([R0-9\-\s\%\>\~]+)", text, re.IGNORECASE)
    if m_cross:
        crossover = m_cross.group(1).strip()
        
    parsed_models.append((fname, model_name, surface, crossover))

print("=== SURFACE & MODEL ID AUDIT (02-FAB-R-TEST) ===")
print(f"Parsed surface profiles for {len(parsed_models)} files:\n")

for fn, m_name, surf, cross in parsed_models[:20]:
    print(f"  File: {fn}")
    print(f"    - Model ID: {m_name}")
    print(f"    - Surface:  {surf}")
    print(f"    - Boundary: {cross}\n")
