#!/usr/bin/env python3
"""Normalize title/description quoting in translated frontmatter.

Models occasionally emit `title: 'The Agent's Game'`, which is invalid YAML.
Re-emitting both fields as single-quoted scalars with doubled apostrophes makes
the frontmatter valid regardless of what the model produced.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DST = ROOT / "src" / "content" / "blog-en"
KEYS = ("title", "description")


def unquote(raw: str) -> str:
    raw = raw.strip()
    if len(raw) >= 2 and raw[0] == raw[-1] == "'":
        return raw[1:-1].replace("''", "'")
    if len(raw) >= 2 and raw[0] == raw[-1] == '"':
        return raw[1:-1].replace('\\"', '"')
    return raw


def normalize(frontmatter: str) -> str:
    for key in KEYS:
        match = re.search(rf"^{key}:[ \t]*(.*)$", frontmatter, re.M)
        if not match:
            continue
        raw = match.group(1)
        if raw.strip() in ("|", ">", "|-", ">-"):
            continue
        value = unquote(raw)
        replacement = f"{key}: '" + value.replace("'", "''") + "'"
        frontmatter = frontmatter[: match.start()] + replacement + frontmatter[match.end() :]
    return frontmatter


def main() -> int:
    fixed = 0
    for path in sorted(DST.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", text, re.S)
        if not match:
            print(f"SKIP (no frontmatter): {path.name}")
            continue
        fm, body = match.groups()
        new_fm = normalize(fm)
        if new_fm != fm:
            path.write_text(f"---\n{new_fm}\n---\n{body}", encoding="utf-8")
            fixed += 1
            print(f"fixed {path.name}")
    print(f"files fixed: {fixed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
