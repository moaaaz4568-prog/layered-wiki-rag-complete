import os
import re

files = [
    "SYS_01_CHARTER.md",
    "SYS_02_NAMING.md",
    "SYS_03_TREE.md",
    "SYS_04_THINKING_ENGINE.md",
    "SYS_05_INGESTION.md",
    "SYS_06_TERMS_DEEPENING.md",
    "SYS_07_MASTER_ANATOMY.md",
    "SYS_08_PLURALISM.md"
]
base = "/sdcard/wikillm/argon_version/wiki_ver2/systems"
wiki_root = "/sdcard/wikillm/argon_version/wiki_ver2"

for fn in files:
    fp = os.path.join(base, fn)
    with open(fp, "r", encoding="utf-8") as f:
        text = f.read()

    def mask_code_blocks(match):
        return "\n" * match.group(0).count("\n")

    text_masked = re.sub(r"```.*?```", mask_code_blocks, text, flags=re.DOTALL)

    lines = text_masked.splitlines()
    print(f"\n==================== {fn} ====================")
    for lnum, line in enumerate(lines, 1):
        if not line.strip():
            continue

        # Look for explicit absolute paths starting with /
        abs_candidates = re.findall(r"(/[a-zA-Z0-9_\.\-]+(?:/[a-zA-Z0-9_\.\-\s\(\)]+)*)", line)
        for cand in abs_candidates:
            c_clean = cand.strip().rstrip(".,;:\"')]}")
            if any(tok in c_clean for tok in ["{}/INDEX.md", "$", "*", "<", ">", "|"]):
                continue
            if c_clean in ["/", "/root", "/sdcard", "/mnt"]:
                continue
            
            p1 = c_clean
            p2 = c_clean.replace("/sdcard/", "/mnt/sdcard/") if c_clean.startswith("/sdcard/") else c_clean.replace("/mnt/sdcard/", "/sdcard/")
            exists = os.path.exists(p1) or os.path.exists(p2)
            print(f"Line {lnum:3d} [ABS]: {c_clean} -> exists: {exists}")

        # Look for relative paths to other files/folders
        # like domains/, systems/, tools/, or references in yaml frontmatter
        rel_candidates = re.findall(r"(?:(?:systems|domains|tools)/[a-zA-Z0-9_\.\-]+|SYS_\d+_[A-Z_]+\.md)", line)
        for cand in rel_candidates:
            c_clean = cand.strip().rstrip(".,;:\"')]}")
            target = os.path.join(wiki_root, c_clean)
            if not os.path.exists(target):
                target = os.path.join(base, c_clean)
            exists = os.path.exists(target)
            print(f"Line {lnum:3d} [REL]: {c_clean} -> exists: {exists}")
