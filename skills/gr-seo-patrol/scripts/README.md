# gr-seo-patrol scripts

## Original scripts (gingiris-built)
- `daily-report.py` — DataForSEO SERP rank patrol (gingiris.tools + dev.to/iris1031)
- `canonical-fix.py` — Batch canonical URL fix on Jekyll _posts
- `rescue-post.py` — Social rescue (title rewrite + internal link injection)

## Adopted from JeffLi1993/seo-audit-skill (2026-05-07)
Single-page deep audit capability — the 4 scripts below validate per-page SEO health.

- `check-page.py` — H1, title, meta description, canonical, slug, alt text, keyword placement
- `check-schema.py` — JSON-LD validation (Article, FAQPage, BreadcrumbList, Organization, etc)
- `check-site.py` — robots.txt + sitemap.xml validation, redirect chain
- `check-social.py` — OG tags + Twitter Card validation

All adapted scripts retain their original license terms.
Original repo: https://github.com/JeffLi1993/seo-audit-skill

## Usage

```bash
# Single-page audit
python3 scripts/check-page.py URL --keyword "primary keyword"
python3 scripts/check-schema.py URL
python3 scripts/check-site.py URL
python3 scripts/check-social.py URL
```

## Dependencies
- `pip install requests` — for the 4 adopted scripts
- gingiris originals (daily-report, canonical-fix, rescue-post) use Python stdlib only
