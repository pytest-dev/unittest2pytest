#!/usr/bin/env python3
"""
make_changelog.py — Update CHANGELOG.rst for releases.

Usage:
    python make_changelog.py 0.6          Replace UNRELEASED with a dated section.
    python make_changelog.py --minor      Bump minor version from latest tag.
    python make_changelog.py --major      Bump major version from latest tag.
    python make_changelog.py --micro      Bump micro version from latest tag.
    python make_changelog.py --post       Bump post version from latest tag.
    python make_changelog.py UNRELEASED   Add a new UNRELEASED section.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

from packaging.version import Version


def _find_changelog() -> Path:
    d = Path(__file__).resolve().parent
    while d != d.parent:
        p = d / "CHANGELOG.rst"
        if p.exists():
            return p
        d = d.parent
    raise FileNotFoundError("CHANGELOG.rst not found")


CHANGELOG = _find_changelog()
REPO_ROOT = CHANGELOG.parent

UNRELEASED_SECTION = """\
UNRELEASED
----------

*UNRELEASED*

"""


def _latest_tag_version() -> Version:
    """Get the latest vX.Y.Z tag as a packaging Version."""
    result = subprocess.run(
        ["git", "tag", "-l", "v*", "--sort=-v:refname"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    for line in result.stdout.strip().splitlines():
        tag = line.strip().removeprefix("v")
        try:
            return Version(tag)
        except Exception:
            continue
    print("ERROR: No version tags found", file=sys.stderr)
    sys.exit(1)


def _bump_version(bump: str) -> str:
    """Compute the next version string from the latest tag."""
    v = _latest_tag_version()

    if bump == "major":
        return f"{v.major + 1}.0"
    elif bump == "minor":
        return f"{v.major}.{v.minor + 1}"
    elif bump == "micro":
        return f"{v.major}.{v.minor}.{v.micro + 1}"
    elif bump == "post":
        post = (v.post or 0) + 1
        base = f"{v.major}.{v.minor}.{v.micro}" if v.micro else f"{v.major}.{v.minor}"
        return f"{base}.post{post}"
    else:
        raise ValueError(f"Unknown bump: {bump}")


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
        print(
            "ERROR: Could not find UNRELEASED section in CHANGELOG.rst", file=sys.stderr
        )
        return 1

    underline = "-" * len(version)
    replacement = f"{version}\n{underline}\n\n*{today}*\n"

    new_text = text[: match.start()] + replacement + text[match.end() :]
    CHANGELOG.write_text(new_text)

    print(f"CHANGELOG.rst updated: UNRELEASED → {version} ({today})", file=sys.stderr)
    print(version)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "version", nargs="?", help="Release version (e.g. 0.6) or UNRELEASED"
    )

    bump = parser.add_mutually_exclusive_group()
    bump.add_argument("--major", action="store_const", const="major", dest="bump")
    bump.add_argument("--minor", action="store_const", const="minor", dest="bump")
    bump.add_argument("--micro", action="store_const", const="micro", dest="bump")
    bump.add_argument("--post", action="store_const", const="post", dest="bump")

    args = parser.parse_args()

    if args.version and args.bump:
        parser.error("Cannot specify both a version and a bump flag")

    if args.bump:
        version = _bump_version(args.bump)
        return cut_release(version)

    if args.version == "UNRELEASED":
        return add_unreleased()

    if args.version:
        return cut_release(args.version)

    parser.error(
        "Provide a version, UNRELEASED, or a bump flag (--major/--minor/--micro/--post)"
    )


if __name__ == "__main__":
    sys.exit(main())
