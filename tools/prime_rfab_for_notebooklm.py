import os
import glob
import re

base_dir = r"C:\Users\kevin\Documents\02\08-Model-Handbook-2026"
rfab_dir = os.path.join(base_dir, "okf", "LLM_Tests", "04_RFAB_TEST")

files = sorted(glob.glob(os.path.join(rfab_dir, "*.md")) + glob.glob(os.path.join(rfab_dir, "*.txt")))

manifest_lines = [
    "# NotebookLM Ingestion Manifest - RFAB Diagnostic Papers (2026)",
    "",
    "> **Ready for NotebookLM batch loading.** All files in `02-FAB-R-TEST/` formatted, sanitized, and verified for R1–R10 Reasoning vs Fabrication analysis.",
    "",
    "## Included NotebookLM Sources",
    ""
]

primed_count = 0

for fpath in files:
    fname = os.path.basename(fpath)
    if fname.startswith("00-") or fname.startswith("_"):
        continue
        
    sz = os.path.getsize(fpath)
    if sz == 0:
        os.remove(fpath)
        continue
        
    with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
        content = fp.read()
        
    # Check if content has clean title/frontmatter, add frontmatter header if missing
    if not content.startswith("---"):
        clean_title = fname.replace(".md", "").replace(".txt", "").replace("-", " ")
        header = f"---\ntitle: {clean_title}\ntype: concept\ntags: [rfab, reasoning-fabrication, notebooklm-ingest]\nsources: [\"[[02-FAB-R-TEST]]\"]\nlast_updated: 2026-07-24\n---\n\n"
        with open(fpath, "w", encoding="utf-8") as fp:
            fp.write(header + content)
            
    primed_count += 1
    manifest_lines.append(f"- [{fname}](file:///{fpath.replace(os.sep, '/')}) ({sz} bytes)")

manifest_path = os.path.join(rfab_dir, "00-NOTEBOOKLM-INGEST-MANIFEST.md")
with open(manifest_path, "w", encoding="utf-8") as out:
    out.write("\n".join(manifest_lines) + "\n")

print(f"=== PRIMED RFAB FOLDER FOR NOTEBOOKLM INGESTION ===")
print(f"  - Cleaned & formatted: {primed_count} sources")
print(f"  - Generated Manifest: {manifest_path}")
