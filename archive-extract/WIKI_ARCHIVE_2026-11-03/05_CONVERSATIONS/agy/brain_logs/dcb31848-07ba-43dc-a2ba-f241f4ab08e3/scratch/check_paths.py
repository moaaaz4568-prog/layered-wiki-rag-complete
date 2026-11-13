import pathlib
import re

files = [
    "systems/SYS_09_CUMULATIVE_SYNTHESIS.md",
    "systems/SYS_10_INDEXES.md",
    "systems/SYS_11_BUSINESS_EXECUTION.md",
    "systems/SYS_12_AUDIT.md",
    "systems/SYS_13_DELEGATION.md",
    "systems/SYS_14_ANTI_PATTERNS.md",
    "systems/SYS_15_DYNAMIC_EXPANSION.md",
    "README.md",
    "START_HERE.md",
    "AGENTS.md",
    "_BUILD_REPORT.md"
]

base = pathlib.Path("/sdcard/wikillm/argon_version/wiki_ver2")
raw_path_re = re.compile(r"(?:file://)?(/(?:sdcard|root|mnt)/[a-zA-Z0-9_./-]+|(?:systems|domains|tools)/[a-zA-Z0-9_./-]+|\b[a-zA-Z0-9_-]+\.(?:md|py|json|txt))")

for f in files:
    p = base / f
    content = p.read_text(encoding="utf-8")
    lines = content.splitlines()
    print(f"=== Testing paths in: {f} ===")
    not_found = []
    for i, line in enumerate(lines):
        for m in raw_path_re.finditer(line):
            raw = m.group(1)
            raw = raw.strip("),.:;*\"\'` ")
            if not raw:
                continue
            if any(x in raw for x in ["*", "$", "<", ">", "{", "}", "(", ")", "[", "]", "output_business_plan", "new_master", "report_file", "your_master_file", "YOUR_SYSTEM", "target_file"]):
                continue
            # ignore file:/// prefix if kept
            if raw.startswith("file://"):
                raw = raw[7:]
            if raw.startswith("/"):
                t = pathlib.Path(raw)
            else:
                t = (base / raw)
            if not t.exists():
                not_found.append((i+1, raw))
    if not_found:
        for ln, path_str in not_found:
            print(f"  L{ln}: NOT FOUND: {path_str}")
    else:
        print("  All paths exist! (PASS)")
