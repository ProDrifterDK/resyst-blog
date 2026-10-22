# Bilingual pipeline (Spanish → English)

Spanish is the source of truth and lives at the site root (`/`). English is a
translation layer under `/en/`. Nothing about the Spanish URLs changed.

## Layout

| Piece | Where |
|---|---|
| UI strings | `src/i18n/ui.ts` |
| Tag vocabulary and editorial groups | `src/i18n/tag-categories.ts` |
| Long-form About copy | `src/i18n/about-copy.ts` |
| Locale helpers | `src/i18n/utils.ts` |
| Spanish posts | `src/content/blog/*.md` |
| English posts | `src/content/blog-en/*.md` |
| Translation state (source hash, slug, warnings) | `scripts/i18n/state.json` |

English posts carry `translationOf: '<spanish-file-stem>'`. That single field
drives the language switcher, the `hreflang` alternates and cross-links, even
though the two languages use different slugs.

## Translating

```sh
python3 scripts/i18n/translate.py                 # translate everything missing or stale
python3 scripts/i18n/translate.py --only <stem>   # one post
python3 scripts/i18n/rewrite-links.py             # remap internal links to English slugs
```

`translate.py` is idempotent: it skips posts whose source hash is unchanged, so
re-runs only touch new or edited posts. `--force` retranslates on demand.

Prose goes through the model; everything mechanical is deterministic:

- tags are mapped from `TAG_MAP` in `translate.py`
- slugs are derived from the translated title
- `title` and `description` are re-quoted as safe YAML scalars
- structure is compared before writing (headings, code fences, blockquotes,
  tables, length ratio, leftover Spanish markers)

## Verifying

```sh
npm run build
python3 scripts/i18n/check-build.py
```

`check-build.py` fails on broken internal links, wrong `<html lang>`, or
non-reciprocal `hreflang` alternates. `fix-frontmatter.py` repairs quoting if a
hand-edited post ever breaks YAML.

## Adding a post

Write it in Spanish under `src/content/blog/`, then run `translate.py` for that
stem and `rewrite-links.py`. The daily publisher cron does this automatically.
