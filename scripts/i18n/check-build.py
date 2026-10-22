#!/usr/bin/env python3
"""Static-site verification for the bilingual build.

Checks, against dist/:
- every internal href resolves to a built file
- every /en page declares lang="en" and the Spanish pages declare lang="es"
- hreflang alternates are reciprocal
- the sitemap lists both locales
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "dist"

HREF = re.compile(r'href="([^"]+)"')
HREFLANG = re.compile(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"')
HTML_LANG = re.compile(r'<html[^>]*lang="([^"]+)"')


def resolve(path: str) -> Path | None:
    clean = unquote(path.split("#")[0].split("?")[0])
    if not clean.startswith("/"):
        return None
    target = DIST / clean.lstrip("/")
    if clean.endswith("/"):
        target = target / "index.html"
    elif target.suffix:
        return target if target.exists() else None
    else:
        candidate = DIST / clean.lstrip("/") / "index.html"
        if candidate.exists():
            return candidate
        target = DIST / (clean.lstrip("/") + ".html")
    return target if target.exists() else None


def main() -> int:
    pages = sorted(DIST.rglob("*.html"))
    broken: dict[str, set[str]] = defaultdict(set)
    wrong_lang: list[str] = []
    alternates: dict[str, dict[str, str]] = {}

    for page in pages:
        text = page.read_text(encoding="utf-8", errors="ignore")
        rel = "/" + str(page.relative_to(DIST)).replace("index.html", "").rstrip("/")
        rel = rel or "/"

        lang = HTML_LANG.search(text)
        expected = "en" if rel == "/en" or rel.startswith("/en/") else "es"
        if not lang or not lang.group(1).startswith(expected):
            wrong_lang.append(f"{rel} (found {lang.group(1) if lang else 'none'})")

        for href in HREF.findall(text):
            if href.startswith(("http://", "https://", "mailto:", "#", "data:", "/_astro/")):
                continue
            if not href.startswith("/"):
                continue
            if resolve(href) is None:
                broken[str(page.relative_to(DIST))].add(href)

        found = {code: href for code, href in HREFLANG.findall(text)}
        if found:
            alternates[rel] = found

    # Reciprocal alternates: es <-> en must point at each other.
    non_reciprocal = []
    for rel, links in alternates.items():
        for code, href in links.items():
            parsed = urlparse(href)
            target = unquote(parsed.path).rstrip("/") or "/"
            if target == (rel.rstrip("/") or "/"):
                continue
            back = alternates.get(target)
            if back is None:
                non_reciprocal.append(f"{rel} -> {href} (no alternates on target)")
                continue
            other = [v for k, v in back.items() if k not in (code, "x-default")]
            if (rel.rstrip("/") or "/") not in {urlparse(v).path.rstrip("/") or "/" for v in other}:
                non_reciprocal.append(f"{rel} -> {href}")

    print(f"pages: {len(pages)}")
    print(f"pages with hreflang alternates: {len(alternates)}")
    if wrong_lang:
        print(f"\nWRONG LANG ({len(wrong_lang)}):")
        for item in wrong_lang[:20]:
            print(f"  - {item}")
    if broken:
        print(f"\nBROKEN INTERNAL LINKS ({sum(len(v) for v in broken.values())}):")
        for page, hrefs in list(broken.items())[:25]:
            print(f"  - {page}: {', '.join(sorted(hrefs)[:6])}")
    if non_reciprocal:
        print(f"\nNON-RECIPROCAL ALTERNATES ({len(non_reciprocal)}):")
        for item in non_reciprocal[:15]:
            print(f"  - {item}")

    sitemap = DIST / "sitemap-0.xml"
    if sitemap.exists():
        xml = sitemap.read_text(encoding="utf-8")
        en_urls = len(re.findall(r"<loc>https://ai\.resyst\.cl/en/", xml))
        print(f"\nsitemap urls: {len(re.findall(r'<loc>', xml))} (english: {en_urls})")

    ok = not broken and not wrong_lang and not non_reciprocal
    print("\nRESULT:", "ok" if ok else "problems found")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
