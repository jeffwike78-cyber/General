#!/usr/bin/env python3
"""Check an App Store listing file against Apple's character limits.

Usage: python3 scripts/check-listing.py apps/<slug>/store-listing.md
Exit code 0 = OK, 1 = problems found.
"""
import re
import sys

# Limits shown in the "## Field [N]" headings are authoritative; these are fallbacks.
REQUIRED = {"App Name", "Subtitle", "Keywords", "Description",
            "Privacy Policy URL", "Support URL", "Primary Category"}


def parse(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    fields = {}
    for m in re.finditer(r"^## (.+?)(?: \[(\d+)\])?\s*$\n(.*?)(?=^## |\Z)", text, flags=re.M | re.S):
        name, limit, body = m.group(1).strip(), m.group(2), m.group(3).strip()
        fields[name] = (int(limit) if limit else None, body)
    return fields


def main(path):
    fields = parse(open(path, encoding="utf-8").read())
    problems, warnings = [], []
    for name, (limit, body) in fields.items():
        n = len(body)
        if limit and n > limit:
            problems.append(f"{name}: {n}/{limit} chars, {n - limit} over")
        if name in REQUIRED and not body:
            problems.append(f"{name}: required but empty")
        if "{{" in body or "YOURDOMAIN" in body:
            problems.append(f"{name}: still has a placeholder")
        if limit:
            print(f"  {name:<18} {n:>5}/{limit}")

    kw = fields.get("Keywords", (None, ""))[1]
    if kw:
        if ", " in kw:
            warnings.append("Keywords: remove spaces after commas (they count toward the 100)")
        title = (fields.get("App Name", (0, ""))[1] + " " + fields.get("Subtitle", (0, ""))[1]).lower()
        dupes = [k.strip() for k in kw.split(",") if k.strip() and k.strip().lower() in title.split()]
        if dupes:
            warnings.append(f"Keywords: already in name/subtitle, wasted space: {', '.join(dupes)}")

    for w in warnings:
        print("WARN  " + w)
    for p in problems:
        print("FAIL  " + p)
    if not problems:
        print("OK  listing is within Apple's limits")
    return 1 if problems else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
