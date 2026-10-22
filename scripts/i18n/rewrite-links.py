#!/usr/bin/env python3
"""Rewrite internal blog links in English posts to the translated slugs.

The translator keeps the original slug so prose stays readable mid-run; this
pass maps every `/en/blog/<spanish-slug>` to its English counterpart once all
slugs are known. Idempotent.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "scripts" / "i18n" / "state.json"
DST = ROOT / "src" / "content" / "blog-en"

EN_LINK = re.compile(r"(\(|\s)/en/blog/([^/)#\s]+)(/?)\)?")
ES_LINK = re.compile(r"(\(|\s)/blog/([^/)#\s]+)(/?)\)?")


def main() -> int:
    state = json.loads(STATE.read_text(encoding="utf-8"))
    mapping = {es: data["en"] for es, data in state.items()}
    final_slugs = set(mapping.values())
    unresolved: set[tuple[str, str]] = set()
    changed = 0

    for path in sorted(DST.glob("*.md")):
        text = path.read_text(encoding="utf-8")

        def rewrite(pattern: re.Pattern[str], localized: bool, text_in: str) -> str:
            def repl(match: re.Match[str]) -> str:
                lead, slug, slash = match.group(1), match.group(2), match.group(3)
                if slug in ("tags", "index") or slug in final_slugs:
                    return match.group(0)
                if slug not in mapping:
                    unresolved.add((path.name, slug))
                    return match.group(0)
                return f"{lead}/en/blog/{mapping[slug]}{slash})"

            return pattern.sub(repl, text_in)

        new = rewrite(EN_LINK, True, text)
        new = rewrite(ES_LINK, False, new)
        new = new.replace("(/en/blog/tags/", "(/en/blog/tags/")

        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1
            print(f"rewrote {path.name}")

    print(f"files changed: {changed}")
    if unresolved:
        print("unresolved slugs:")
        for name, slug in sorted(unresolved):
            print(f"  - {name}: {slug}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
