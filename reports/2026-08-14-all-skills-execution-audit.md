# All Skills Execution Audit — 2026-08-14

## Scope

- Canonical source: `Gingiris-1031/gingiris-skills`
- Skills executed through the release gate: **60/60**
- Flagship skills represented on gingiris.tools: launch, OSS/GitHub, SEO/GEO,
  B2B/PLG, ASO, KOL/UGC, community, competitor research, user interviews,
  go-global, Twitter operations, growth routing, and hardware + SaaS GTM
- Distribution targets: GitHub, Hugging Face, ClawHub, gingiris.tools, skills.sh

## Result

| Check | Result |
|---|---:|
| YAML frontmatter parsed | 60/60 |
| Directory name matches skill `name` | 60/60 |
| Required `description` present | 60/60 |
| Nested packages byte-identical | 12/12 |
| Private files excluded from public packages | PASS |
| Legacy GitHub identity / dead public references | 0 |
| Blocking errors | 0 |
| Trigger-language improvement warnings | 36 |

The 36 warnings are non-blocking: those skills already have valid descriptions
and install correctly, but their discovery text does not use explicit phrases
such as “use this skill when” or “triggers”. They should be improved in normal
content batches without inflating every agent's startup context at once.

## Context-specific improvements

1. The public count is now tied to the real top-level inventory: **60**, replacing
   the inconsistent “40+” website copy and “55+” repository copy.
2. The validator encodes Gingiris account safety: only `Gingiris-1031` is valid;
   legacy GitHub, Pages, ClawHub handle, and gingiris.com references block release.
3. Twitter private operations notes and backlink internal ledgers are checked for
   leakage before any public package is accepted.
4. The release gate emits a machine-readable JSON report so hosted skill runs and
   future CI can use the same source of truth.
5. Distribution remains source-first: edit the monorepo, rebuild nested/local
   artifacts, validate once, then publish mirrors. skills.sh indexes the GitHub
   source instead of becoming a separately edited copy.

## Re-run

```bash
bash scripts/sync-nested.sh
GINGIRIS_SKILL_REPORT=/tmp/gingiris-skill-report.json ruby scripts/validate-skills.rb
bash scripts/check-dead-refs.sh
```
