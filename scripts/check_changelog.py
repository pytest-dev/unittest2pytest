#!/usr/bin/env python3
"""
check_changelog.py — Verify CHANGELOG.rst is up to date.

Usage:
    python check_changelog.py              Check UNRELEASED has new entries vs main.
    python check_changelog.py --tag v0.6   Check a version section exists for the tag.
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
REPO_ROOT = CHANGELOG.parent


def _unreleased_content(text: str) -> str | None:
    """Extract the body of the UNRELEASED section, or None if missing."""
    header = re.search(
        r"^UNRELEASED\n-+\n\n\*UNRELEASED\*\n",
        text,
        re.MULTILINE,
    )
    if not header:
        return None
    rest = text[header.end() :]
    next_section = re.search(r"^\S+\n[-=]+\n", rest, re.MULTILINE)
    content = rest[: next_section.start()] if next_section else rest
    return content.strip()


def _main_changelog() -> str | None:
    """Read CHANGELOG.rst from the main branch, or None if unavailable."""
    for ref in ("origin/main", "main"):
        result = subprocess.run(
            ["git", "show", f"{ref}:CHANGELOG.rst"],
            capture_output=True,
            text=True,
            cwd=REPO_ROOT,
        )
        if result.returncode == 0:
            return result.stdout
    return None


def check_unreleased() -> int:
    text = CHANGELOG.read_text()

    current = _unreleased_content(text)
    if current is None:
        print("ERROR: No UNRELEASED section found", file=sys.stderr)
        return 1

    if not current:
        print("ERROR: UNRELEASED section is empty — add a changelog entry", file=sys.stderr)
        return 1

    main_text = _main_changelog()
    if main_text is not None:
        main_content = _unreleased_content(main_text)
        if current == (main_content or ""):
            print(
                "ERROR: UNRELEASED section is unchanged from main — add a changelog entry",
                file=sys.stderr,
            )
            return 1

    print("OK: UNRELEASED section has new content")
    return 0


def check_tag(tag: str) -> int:
    text = CHANGELOG.read_text()

    # Strip leading v from tag
    version = tag.removeprefix("v")

    # Look for a section matching this version
    pattern = re.compile(
        rf"^{re.escape(version)}\n-+\n",
        re.MULTILINE,
    )
    if not pattern.search(text):
        print(
            f"ERROR: No changelog section found for {version}",
            file=sys.stderr,
        )
        return 1

    # UNRELEASED should not be present in a tagged release
    if re.search(r"^UNRELEASED\n-+\n", text, re.MULTILINE):
        print(
            "ERROR: UNRELEASED section still present in tagged release",
            file=sys.stderr,
        )
        return 1

    print(f"OK: Changelog has section for {version}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", help="Git tag to check against (e.g. v0.6)")
    args = parser.parse_args()

    if args.tag:
        return check_tag(args.tag)
    return check_unreleased()


if __name__ == "__main__":
    sys.exit(main())
