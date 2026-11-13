import pathlib
import re
import os

broken = []
checked = 0

for p in pathlib.Path("/sdcard/wikillm/argon_version/wiki_ver2").rglob("*.md"):
    text = p.read_text(errors="ignore")
    # 1. extract quoted or backticked paths
    candidates = []
    # in backticks
    candidates.extend(re.findall(r'`(/(?:sdcard|root|mnt)/[^`\n]+)`', text))
    # in quotes
    candidates.extend(re.findall(r'"(/(?:sdcard|root|mnt)/[^"\n]+)"', text))
    # in markdown links ](path) or ](file://path)
    candidates.extend(re.findall(r'\]\((?:file://)?(/(?:sdcard|root|mnt)/[^\)\n]+)\)', text))

    for target in candidates:
        target_clean = target.strip()
        # ignore globs or output placeholders
        if any(c in target_clean for c in ["*", "[", "]", "output_business_plan"]):
            continue
        # clean line numbers if format is path:line
        if ":" in os.path.basename(target_clean):
            target_clean = target_clean.split(":")[0]
        # clean anchor like #L10
        if "#" in target_clean:
            target_clean = target_clean.split("#")[0]

        checked += 1
        if not os.path.exists(target_clean):
            alt = target_clean.replace("/sdcard/", "/mnt/sdcard/") if target_clean.startswith("/sdcard/") else target_clean.replace("/mnt/sdcard/", "/sdcard/")
            if not os.path.exists(alt):
                broken.append((str(p.name), target_clean))

print(f"Checked: {checked}, Broken: {len(broken)}")
for fn, b in broken[:20]:
    print(f"{fn} -> {b}")
