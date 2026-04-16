#!/usr/bin/env python3
"""Fetch Huawei Cloud case-center cases via public API and save as JSON.

API endpoint: POST https://devstation-svc.connect.huaweicloud.com/userApi/clouddeployso/userGuide/queryApprovedUserGuides

Usage:
    python3 scripts/fetch_cases.py                    # fetch all cases
    python3 scripts/fetch_cases.py --output data/cases.json  # custom output
    python3 scripts/fetch_cases.py --summary          # print summary only
"""

import argparse
import json
import os
import sys
import time
from collections import Counter
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

API_URL = "https://devstation-svc.connect.huaweicloud.com/userApi/clouddeployso/userGuide/queryApprovedUserGuides"
DEFAULT_OUTPUT = "data/cases.json"
PAGE_SIZE = 50
MAX_RETRIES = 3
RETRY_DELAY = 2


def fetch_page(
    page_index: int,
    page_size: int = PAGE_SIZE,
    tags: list | None = None,
    difficulty: str = "",
    name: str = "",
) -> dict:
    body = json.dumps(
        {
            "name": name,
            "tags": tags or [],
            "difficulty": difficulty,
            "pageIndex": page_index,
            "pageSize": page_size,
        }
    ).encode("utf-8")

    req = Request(
        API_URL,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "projectdomainflag": "cloudEdu",
            "x-language": "zh-cn",
        },
    )

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                if data.get("error_code") != "0000":
                    print(
                        f"API error on page {page_index}: {data.get('error_msg')}",
                        file=sys.stderr,
                    )
                    return {"result_list": []}
                return data
        except (URLError, HTTPError) as e:
            print(
                f"Request failed (attempt {attempt}/{MAX_RETRIES}): {e}",
                file=sys.stderr,
            )
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY * attempt)
    return {"result_list": []}


def normalize_case(raw: dict) -> dict:
    return {
        "id": raw.get("id", ""),
        "name": raw.get("name", ""),
        "tags": raw.get("tags", ""),
        "difficulty": raw.get("difficulty", 0),
        "status": raw.get("status", 0),
        "introduce": raw.get("introduce", ""),
        "content": raw.get("content", ""),
        "formatType": raw.get("formatType", 0),
        "timeCost": raw.get("timeCost", ""),
        "attachmentIds": raw.get("attachmentIds", []),
        "clickNo": raw.get("clickNo", 0),
        "downloadNo": raw.get("downloadNo", 0),
        "author": {
            "developer_id": raw["author"].get("developer_id", ""),
            "nick_name": raw["author"].get("nick_name", ""),
            "avatar": raw["author"].get("avatar", ""),
        }
        if raw.get("author")
        else None,
    }


def fetch_all_cases() -> list[dict]:
    all_cases = []
    page_index = 1
    while True:
        print(
            f"Fetching page {page_index} (pageSize={PAGE_SIZE})...", end=" ", flush=True
        )
        data = fetch_page(page_index)
        cases = data.get("result_list", [])
        if not cases:
            print("no more results.")
            break
        all_cases.extend(normalize_case(c) for c in cases)
        print(f"got {len(cases)} cases (total: {len(all_cases)})")
        if len(cases) < PAGE_SIZE:
            break
        page_index += 1
        time.sleep(0.5)
    return all_cases


def print_summary(cases: list[dict]) -> None:
    tag_counter = Counter()
    for c in cases:
        for t in c["tags"].split("|"):
            tag_counter[t.strip()] += 1

    print(f"\nTotal cases: {len(cases)}")
    print("\nTag distribution:")
    for tag, count in tag_counter.most_common():
        print(f"  {tag}: {count}")

    content_lengths = [len(c["content"]) for c in cases if c["content"]]
    if content_lengths:
        print(
            f"\nContent size: min={min(content_lengths)}, max={max(content_lengths)}, "
            f"avg={sum(content_lengths) // len(content_lengths)}, "
            f"total={sum(content_lengths) // 1024}KB"
        )

    top10 = sorted(cases, key=lambda x: x["clickNo"], reverse=True)[:10]
    print("\nTop 10 by clicks:")
    for i, c in enumerate(top10, 1):
        print(f"  {i}. [{c['tags']}] {c['name']} (clicks={c['clickNo']})")


def main():
    parser = argparse.ArgumentParser(description="Fetch Huawei Cloud case-center cases")
    parser.add_argument(
        "--output", "-o", default=DEFAULT_OUTPUT, help="Output JSON file path"
    )
    parser.add_argument(
        "--summary",
        "-s",
        action="store_true",
        help="Print summary only (no file write)",
    )
    parser.add_argument(
        "--no-content",
        action="store_true",
        help="Skip full content field to reduce size",
    )
    args = parser.parse_args()

    cases = fetch_all_cases()
    if not cases:
        print("No cases fetched.", file=sys.stderr)
        sys.exit(1)

    if args.summary:
        print_summary(cases)
        return

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if args.no_content:
        for c in cases:
            c["content"] = ""

    output_data = {
        "total": len(cases),
        "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source": API_URL,
        "cases": cases,
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\nSaved {len(cases)} cases to {output_path}")
    print_summary(cases)


if __name__ == "__main__":
    main()
