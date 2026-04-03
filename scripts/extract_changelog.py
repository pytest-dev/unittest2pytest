#!/usr/bin/env python3
"""
extract_changelog.py — Extract a version's changelog section.

Usage:
    python scripts/extract_changelog.py 0.6
    python scripts/extract_changelog.py 0.6 --format gfm
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


def _find_changelog() -> Path:
    d = Path(__file__).resolve().parent
    while d != d.parent:
        p = d / "CHANGELOG.rst"
        if p.exists():
            return p
        d = d.parent
    raise FileNotFoundError("CHANGELOG.rst not found")


CHANGELOG = _find_changelog()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version", help="Version to extract (e.g. 0.6)")
    parser.add_argument(
        "--format",
        default="rst",
        help="Output format (default: rst). Use 'gfm' for GitHub Flavored Markdown.",
    )
    args = parser.parse_args()

    text = CHANGELOG.read_text()
    pattern = re.compile(
        rf"^{re.escape(args.version)}\n-+\n",
        re.MULTILINE,
    )
    match = pattern.search(text)
    if not match:
        print(f"ERROR: No section found for {args.version}", file=sys.stderr)
        return 1

    rest = text[match.end() :]
    next_section = re.search(r"^\S+\n[-=]+\n", rest, re.MULTILINE)
    body = rest[: next_section.start()].strip() if next_section else rest.strip()

    if args.format != "rst":
        result = subprocess.run(
            ["pandoc", "-f", "rst", "-t", args.format],
            input=body,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(f"ERROR: pandoc failed: {result.stderr}", file=sys.stderr)
            return 1
        body = result.stdout.rstrip()

    print(body)
    return 0


if __name__ == "__main__":
    sys.exit(main())
