#!/usr/bin/env python3
"""
make_changelog.py — Update CHANGELOG.rst for releases.

Usage:
    python make_changelog.py <version>    Replace UNRELEASED with a dated section.
    python make_changelog.py UNRELEASED   Add a new UNRELEASED section.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

CHANGELOG = Path(__file__).resolve().parent / "CHANGELOG.rst"

UNRELEASED_SECTION = """\
UNRELEASED
----------

*UNRELEASED*

"""


def add_unreleased() -> int:
    text = CHANGELOG.read_text()

    if re.search(r"^UNRELEASED\n-+\n", text, re.MULTILINE):
        print("ERROR: UNRELEASED section already exists", file=sys.stderr)
        return 1

    # Insert after the top-level heading
    match = re.search(r"^(Changelog\n=+\n)\n", text, re.MULTILINE)
    if not match:
        print("ERROR: Could not find Changelog heading", file=sys.stderr)
        return 1

    insert_at = match.end()
    new_text = text[:insert_at] + UNRELEASED_SECTION + "\n" + text[insert_at:]
    CHANGELOG.write_text(new_text)

    print("CHANGELOG.rst updated: added UNRELEASED section")
    return 0


def cut_release(version: str) -> int:
    today = date.today().strftime("%Y-%m-%d")
    text = CHANGELOG.read_text()

    pattern = re.compile(
        r"^UNRELEASED\n-+\n\n\*UNRELEASED\*\n",
        re.MULTILINE,
    )
    match = pattern.search(text)
    if not match:
        print("ERROR: Could not find UNRELEASED section in CHANGELOG.rst", file=sys.stderr)
        return 1

    underline = "-" * len(version)
    replacement = f"{version}\n{underline}\n\n*{today}*\n"

    new_text = text[: match.start()] + replacement + text[match.end() :]
    CHANGELOG.write_text(new_text)

    print(f"CHANGELOG.rst updated: UNRELEASED → {version} ({today})")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version", help="Release version (e.g. 0.6) or UNRELEASED")
    args = parser.parse_args()

    if args.version == "UNRELEASED":
        return add_unreleased()
    return cut_release(args.version)


if __name__ == "__main__":
    sys.exit(main())
