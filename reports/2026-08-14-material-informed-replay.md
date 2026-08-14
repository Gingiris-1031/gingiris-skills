# Material-informed skill replay — 2026-08-14

## Sources used

- Iris Product Hunt experience wiki (content fetched through Feishu authorization)
- Iris competitor-research framework wiki
- Iris open-source global-operations deck (22 slides)
- Iris paid global-growth course PDF (97 pages; principles abstracted, no verbatim redistribution)
- Four supplied WeChat pages: direct and browser access were blocked, so only indexed metadata was verified; unverified article details were not imported

## Changes made

- `product-hunt-playbook`: ethical support-quality controls, two-hour monitoring, timing/fit, hunter limits, conversion closure and field-note reference.
- `open-source-marketing-playbook`: readiness gate, launch packet, 24-hour operating sequence, contributor routing and monetization loop.
- `developer-marketing-playbook`: Wayback stage reconstruction, best-in-channel benchmarking, docs activation funnel and ecosystem campaign.
- `startup-consultant`: stage-first diagnosis, stop-growth rule, first-user outreach and interview evidence contract.
- `startup-growth-playbook`: stage gates, cohort attribution, first-ten-user motion and activation-before-scale rule.
- `startup-marketing-playbook`: executable four-week zero-budget program.
- `gr-readme` and `gingiris-twitter-agent-ops`: explicit scope boundaries and correct downstream handoffs.
- Replay harness: corrected category errors for README, owned-account operations, consulting and stage-gated growth.

## Replay result

| Grade | Before | After |
|---|---:|---:|
| PASS | 11 | 19 |
| PARTIAL | 19 | 19 |
| FAIL | 11 | 3 |

All 41 public catalog skills were still included. Structural validation checked 60 monorepo skills with 0 errors.

## Remaining failures

1. `gingiris-aso-growth`: the supplied cases do not contain a controlled App Store before/after with keyword rank, impression→page view, page view→install and retained-user outcomes. Mapping a general $1K launch to ASO would be invalid.
2. `aso-playbook`: same evidence gap, plus the installable body remains too shallow to execute independently.
3. `agent-workflow-playbook`: no measured before/after orchestration case exists for task quality, elapsed time, cost, retries and failure rate; the AI-twin growth campaign is not an agent-architecture validation case.

These remain FAIL deliberately. They need new primary evidence, not more generic prose.

## Reproduce

```bash
GINGIRIS_REPLAY_REPORT=/tmp/gingiris-41-real-case-replay.json \
  ruby scripts/replay-real-cases.rb
```

The command remains non-zero while a FAIL exists.
