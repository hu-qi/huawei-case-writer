#!/usr/bin/env python3
"""Generate a lightweight markdown index from data/cases.json for reference.

Creates references/case-index.md with a categorized, sortable table of all cases.
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

DATA_FILE = Path("data/cases.json")
OUTPUT_FILE = Path("references/case-index.md")


def main():
    if not DATA_FILE.exists():
        print(f"{DATA_FILE} not found. Run fetch_cases.py first.", file=sys.stderr)
        sys.exit(1)

    with open(DATA_FILE, encoding="utf-8") as f:
        data = json.load(f)

    cases = data["cases"]
    fetched_at = data.get("fetched_at", "unknown")

    lines = [
        "# Huawei Cloud Case Center Index",
        "",
        f"> Auto-generated from API data. Last updated: {fetched_at}. Total: {len(cases)} cases.",
        "",
    ]

    by_tag = defaultdict(list)
    for c in cases:
        for t in c["tags"].split("|"):
            by_tag[t.strip()].append(c)

    for tag in sorted(by_tag.keys()):
        tag_cases = sorted(by_tag[tag], key=lambda x: x["clickNo"], reverse=True)
        lines.append(f"## {tag} ({len(tag_cases)})")
        lines.append("")
        lines.append("| # | Title | Difficulty | Time | Clicks | Downloads |")
        lines.append("|---|-------|------------|------|--------|-----------|")
        for i, c in enumerate(tag_cases, 1):
            diff_stars = "★" * c["difficulty"] + "☆" * (5 - c["difficulty"])
            name = c["name"].replace("|", "\\|")
            if len(name) > 60:
                name = name[:57] + "..."
            lines.append(
                f"| {i} | {name} | {diff_stars} | {c['timeCost']} | {c['clickNo']} | {c['downloadNo']} |"
            )
        lines.append("")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Generated {OUTPUT_FILE} with {len(cases)} cases across {len(by_tag)} tags.")


if __name__ == "__main__":
    main()
