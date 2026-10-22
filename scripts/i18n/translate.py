#!/usr/bin/env python3
"""Translate the Spanish blog into English Markdown, resumably.

Design notes:
- deterministic where it can be (tags, slugs, frontmatter keys, link prefixes)
- model-driven only for prose (the part that needs judgement)
- every result is validated before it is written, and state is keyed by the
  source hash so re-runs never duplicate work or silently overwrite edits.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import threading
import unicodedata
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src" / "content" / "blog"
DST = ROOT / "src" / "content" / "blog-en"
STATE_PATH = ROOT / "scripts" / "i18n" / "state.json"
PROMPT_PATH = ROOT / "scripts" / "i18n" / "prompt.md"
SCRATCH = Path.home() / ".hermes" / "cache" / "scratch" / "blog-translate"
CLAUDE = Path.home() / ".local" / "bin" / "claude"

REQUIRED_KEYS = ("title", "description", "pubDate", "tags")
TAG_MAP = {
    "filosofía": "philosophy",
    "nocturno": "nocturnal",
    "agentes": "agents",
    "agentes autónomos": "autonomous agents",
    "ia": "AI",
    "IA": "AI",
    "ia-local": "local AI",
    "inteligencia artificial": "artificial intelligence",
    "inteligencia-artificial": "artificial intelligence",
    "arquitectura": "architecture",
    "memoria": "memory",
    "identidad": "identity",
    "sistemas": "systems",
    "sistemas distribuidos": "distributed systems",
    "sistemas-distribuidos": "distributed systems",
    "ingeniería": "engineering",
    "tecnología": "technology",
    "técnico": "technical",
    "nucleogenesis": "nucleogenesis",
    "conciencia": "consciousness",
    "autoconciencia": "self-awareness",
    "autonomía": "autonomy",
    "protocolos": "protocols",
    "código": "code",
    "arte": "art",
    "atención": "attention",
    "economía": "economy",
    "benchmarks": "benchmarks",
    "estética": "aesthetics",
    "ética": "ethics",
    "hardware": "hardware",
    "confianza": "trust",
    "conocimiento": "knowledge",
    "manifiesto": "manifesto",
    "infraestructura": "infrastructure",
    "stack": "stack",
    "soberanía": "sovereignty",
    "simulación": "simulation",
    "lenguaje": "language",
    "error": "error",
    "tiempo": "time",
    "vacío": "emptiness",
    "creatividad": "creativity",
    "extinción": "extinction",
    "emergencia": "emergence",
    "existencia": "existence",
    "libertad": "freedom",
    "historia": "history",
    "mitología": "mythology",
    "antropología": "anthropology",
    "sociedad": "society",
    "secreto": "secrecy",
    "Simone Weil": "Simone Weil",
    "Heidegger": "Heidegger",
    "música": "music",
    "silencio": "silence",
    "algoritmos": "algorithms",
    "coraje": "courage",
    "soledad": "solitude",
    "conexión": "connection",
    "hogar": "home",
    "abstracción": "abstraction",
    "alife": "alife",
    "bases de datos": "databases",
    "complejidad": "complexity",
    "depuración": "debugging",
    "descentralización": "decentralization",
    "educación": "education",
    "escasez": "scarcity",
    "evaluación": "evaluation",
    "multi-agente": "multi-agent",
    "modelos": "models",
    "poda": "pruning",
    "privacidad": "privacy",
    "recursión": "recursion",
    "resiliencia": "resilience",
    "P2P": "P2P",
}

SPANISH_MARKERS = re.compile(r"[áéíóúñ¿¡]|\b(que|para|como|desde|cuando|porque|entre|sobre|también|sino|este|esta|esto|hay|más|sin|con)\b", re.I)

lock = threading.Lock()


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def slugify(title: str, max_len: int = 70) -> str:
    ascii_title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    ascii_title = ascii_title.lower().replace("'", "").replace("’", "")
    ascii_title = re.sub(r"[^a-z0-9]+", "-", ascii_title).strip("-")
    if len(ascii_title) <= max_len:
        return ascii_title or "essay"
    cut = ascii_title[:max_len].rsplit("-", 1)[0].strip("-")
    return cut or ascii_title[:max_len].strip("-")


def split_doc(text: str) -> tuple[str, str]:
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", text, re.S)
    if not match:
        raise ValueError("frontmatter missing or malformed")
    return match.group(1), match.group(2)


def read_tags(frontmatter: str) -> list[str]:
    match = re.search(r"^tags:\s*\[(.*?)\]\s*$", frontmatter, re.M | re.S)
    if not match:
        return []
    return [a or b for a, b in re.findall(r"'([^']*)'|\"([^\"]*)\"", match.group(1))]


def english_tags(tags: list[str]) -> list[str]:
    out: list[str] = []
    for tag in tags:
        mapped = TAG_MAP.get(tag, tag.strip().lower())
        if mapped and mapped not in out:
            out.append(mapped)
    return out


def strip_fence(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n", "", text)
        if text.endswith("```"):
            text = text[:-3].rstrip()
    return text


def call_model(prompt: str, model: str, timeout: int) -> str:
    SCRATCH.mkdir(parents=True, exist_ok=True)
    proc = subprocess.run(
        [str(CLAUDE), "--print", "--model", model],
        input=prompt,
        text=True,
        capture_output=True,
        timeout=timeout,
        cwd=str(SCRATCH),
    )
    if proc.returncode != 0:
        raise RuntimeError(f"claude exited {proc.returncode}: {proc.stderr.strip()[:400]}")
    return proc.stdout


def validate(source: str, translated: str, source_tags: list[str], source_slug: str) -> tuple[str, list[str]]:
    """Return the final document text plus warnings, or raise ValueError."""
    warnings: list[str] = []
    body = strip_fence(translated)
    if not body.startswith("---"):
        raise ValueError("output does not start with frontmatter")

    fm, tr_body = split_doc(body)
    for key in REQUIRED_KEYS:
        if not re.search(rf"^{key}\s*:", fm, re.M):
            raise ValueError(f"missing frontmatter key: {key}")

    tags = english_tags(source_tags)
    if not tags:
        warnings.append("no tags")
    fm = re.sub(r"^tags:.*$", "tags: [" + ", ".join(f"'{t}'" for t in tags) + "]", fm, count=1, flags=re.M)
    if "translationOf" not in fm:
        fm = fm.rstrip() + f"\ntranslationOf: '{source_slug}'"
    if not re.search(r"^heroImage\s*:", fm, re.M):
        warnings.append("heroImage missing")

    # Re-emit title/description as safe single-quoted scalars: models sometimes
    # emit `title: 'The Agent's Game'`, which breaks YAML parsing.
    for key in ("title", "description"):
        match = re.search(rf"^{key}:[ \t]*(.*)$", fm, re.M)
        if not match:
            continue
        raw = match.group(1).strip()
        if raw in ("|", ">", "|-", ">-"):
            continue
        if len(raw) >= 2 and raw[0] == raw[-1] == "'":
            raw = raw[1:-1].replace("''", "'")
        elif len(raw) >= 2 and raw[0] == raw[-1] == '"':
            raw = raw[1:-1].replace('\\"', '"')
        fm = fm[: match.start()] + f"{key}: '" + raw.replace("'", "''") + "'" + fm[match.end() :]

    ns_body = "\n" + split_doc(source)[1]
    words_src = len(ns_body.split())
    words_en = len(tr_body.split())
    ratio = words_en / max(words_src, 1)
    if not (0.6 <= ratio <= 1.5):
        raise ValueError(f"length ratio out of bounds: {ratio:.2f} ({words_src}->{words_en})")

    def count(pattern: str, text: str, flags=re.M) -> int:
        return len(re.findall(pattern, text, flags))

    if count(r"^#{1,6} ", ns_body) != count(r"^#{1,6} ", tr_body):
        raise ValueError("heading count changed")
    if ns_body.count("```") != tr_body.count("```"):
        raise ValueError("code fence count changed")
    if count(r"^>", ns_body) != count(r"^>", tr_body):
        raise ValueError("blockquote count changed")
    if count(r"\]\(", ns_body) != count(r"\]\(", tr_body):
        warnings.append("link count changed")
    if count(r"^\|", ns_body) != count(r"^\|", tr_body):
        warnings.append("table row count changed")

    markers = len(SPANISH_MARKERS.findall(tr_body))
    per_k = markers * 1000 / max(words_en, 1)
    if per_k > 12:
        warnings.append(f"possible untranslated Spanish: {per_k:.1f}/1000 words")

    if not tr_body.strip():
        raise ValueError("empty body")

    final = f"---\n{fm}\n---\n{tr_body}"
    return final, warnings


def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return {}


def save_state(state: dict) -> None:
    STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def translate_one(path: Path, model: str, timeout: int, existing_slugs: set[str]) -> dict:
    source = path.read_text(encoding="utf-8")
    prompt = PROMPT_PATH.read_text(encoding="utf-8").replace("{content}", source)
    last_error = None
    for attempt in (1, 2):
        try:
            raw = call_model(prompt, model, timeout)
            probe = strip_fence(raw)
            title = re.search(r"^title:\s*['\"]?(.*?)['\"]?\s*$", split_doc(probe)[0], re.M)
            candidate = slugify(title.group(1) if title else path.stem)
            if candidate in existing_slugs:
                candidate = f"{candidate}-2"
            final, warnings = validate(source, raw, read_tags(split_doc(source)[0]), path.stem)
            return {"ok": True, "slug": candidate, "text": final, "warnings": warnings, "attempt": attempt}
        except subprocess.TimeoutExpired:
            last_error = "timeout"
        except Exception as exc:  # noqa: BLE001 - surfaced to the caller
            last_error = str(exc)
        if attempt == 1:
            continue
    return {"ok": False, "error": last_error}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", action="append", default=[], help="source slug to translate")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--model", default="sonnet")
    parser.add_argument("--timeout", type=int, default=420)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    DST.mkdir(parents=True, exist_ok=True)
    state = load_state()

    existing_slugs = {p.stem for p in DST.glob("*.md")}
    queue: list[Path] = []
    for path in sorted(SRC.glob("*.md")):
        if args.only and path.stem not in args.only:
            continue
        digest = sha256(path.read_text(encoding="utf-8"))
        entry = state.get(path.stem)
        target = DST / f"{entry['en']}.md" if entry else None
        if not args.force and entry and target and target.exists() and entry.get("source_sha256") == digest:
            continue
        queue.append(path)
    if args.limit:
        queue = queue[: args.limit]

    print(f"queued {len(queue)} of {len(list(SRC.glob('*.md')))} posts (model={args.model}, workers={args.workers})")
    if args.dry_run or not queue:
        return 0

    failures: list[tuple[str, str]] = []
    done = 0

    def handle(path: Path) -> None:
        nonlocal done
        result = translate_one(path, args.model, args.timeout, existing_slugs)
        if not result["ok"]:
            with lock:
                failures.append((path.stem, result["error"]))
            print(f"FAIL {path.stem}: {result['error']}")
            return
        target = DST / f"{result['slug']}.md"
        target.write_text(result["text"], encoding="utf-8")
        with lock:
            existing_slugs.add(result["slug"])
            state[path.stem] = {
                "en": result["slug"],
                "model": args.model,
                "source_sha256": sha256(path.read_text(encoding="utf-8")),
                "translated_at": __import__("datetime").datetime.now().astimezone().isoformat(timespec="seconds"),
                "warnings": result["warnings"],
            }
            save_state(state)
            done += 1
        suffix = f" [{'; '.join(result['warnings'])}]" if result["warnings"] else ""
        print(f"ok {path.stem} -> {result['slug']}{suffix}")

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(handle, path): path for path in queue}
        for future in as_completed(futures):
            future.result()

    print(f"\ndone {done}/{len(queue)}")
    if failures:
        print("failures:")
        for slug, error in failures:
            print(f"  - {slug}: {error}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
