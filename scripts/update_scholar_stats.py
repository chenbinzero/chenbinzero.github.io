#!/usr/bin/env python3
"""Refresh _data/google_scholar_stats.json from the public Scholar profile.

Run from the repo root on a residential IP (i.e., the PI's Mac):

    python3 scripts/update_scholar_stats.py

A residential IP avoids Google's CAPTCHA wall that blocks datacenter
ranges (which is why the prior GitHub Actions workflow was unreliable).
The script is a single HTTP GET plus a regex over the gsc_rsb_std cells
on the profile page -- no third-party dependencies.

If the parser finds <6 numeric cells, the page was almost certainly a
CAPTCHA; the script exits non-zero without overwriting the cached JSON.
"""

import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SCHOLAR_ID = "H001jmIAAAAJ"
URL = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en"
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)
OUT = Path(__file__).resolve().parent.parent / "_data" / "google_scholar_stats.json"


def main() -> int:
    req = urllib.request.Request(URL, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        html = resp.read().decode("utf-8")

    nums = re.findall(r'<td class="gsc_rsb_std">(\d+)</td>', html)
    if len(nums) < 6:
        print(
            f"ERROR: expected >=6 stats cells, got {len(nums)}. "
            "Likely served a CAPTCHA. Cached JSON left unchanged.",
            file=sys.stderr,
        )
        return 1

    data = {
        "citations": int(nums[0]),
        "hindex": int(nums[2]),
        "i10index": int(nums[4]),
        "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }

    OUT.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Wrote {OUT.relative_to(OUT.parent.parent)}: {data}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
