# Delivery, recovery and measurement

## State model

`source-needed → draft → review-needed → ready → authorized → submitted/scheduled → published-verified → measured`

Additional states: `blocked`, `failed`, `unknown`, `cancelled`. Draft upload has its own `draft-uploaded-verified` state; it is not public publication. Missing analytics do not undo a verified publication but prevent a completed measurement claim.

Before action, record the approved content revision, account, channel, absolute slot/time zone and action type. A scheduling request authorizes the specified schedule, not unlimited retries or cross-channel distribution.

Use a stable operation key such as content ID + platform + account + approved slot. Read accessible platform history and the local ledger. Same subject is not always a duplicate: distinguish an identical repost from a new supported angle; preserve the user's repetition constraints. Record the search window and pagination limits.

| Failure | Recovery |
|---|---|
| Timeout after submit | Mark unknown; inspect platform record/history; do not submit again while uncertain |
| Draft exists but readback mismatches | Record mismatch; correct only the authorized draft and reread |
| One channel succeeds, another fails | Keep separate receipts; retry only a confirmed failed operation within authorization |
| Machine slept or scheduled job did not run | Verify whether a platform schedule exists; report missed slot; do not silently move dates |
| Login, permission or media block | Preserve draft and exact blocker; request only the needed user action |
| Metrics unavailable | Record unavailable with collection attempt/time; never write zero |

Three separate receipts:
1. Acceptance: platform content/draft/schedule ID and timestamp.
2. Correctness/visibility: observed text/title/media and verified public or draft URL/state.
3. Outcome: metrics collected at a defined elapsed window; 24 hours is one optional checkpoint, not a promise of automatic follow-up.

For contributors, prepare a message including their approved asset, credit, link and optional sharing context. Messaging is a separate authorized action; do not send to everyone mentioned in a transcript.

## Metrics

| Level | Examples | Interpretation limits |
|---|---|---|
| Content | Impressions, views, clicks, saves, engagement rate | Define eligible impressions/views and exact rate numerator |
| Account | Relevant followers, returning readers, search discovery | Growth does not prove buyer fit |
| Business | Qualified leads, activation, paid conversions, retained customers | State attribution method and overlap/missing data |

Compare like windows, formats and audiences; split organic/paid when available. Report sample size, median and meaningful outliers. A high max/median ratio can motivate investigation but does not prove luck, causality or a broken strategy. Historical title analyses and internal rates are account-specific observations, not universal benchmarks.

Review memo: observation → plausible explanation → uncertainty → next controlled change → owner → review date. Do not change several factors and claim the observed result isolates one cause.
