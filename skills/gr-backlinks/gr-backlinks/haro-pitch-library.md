# HARO Pitch Library (Iris-specific credentials matrix)

> For each incoming HARO query, match topic to the appropriate credential.
> Build response from `templates/haro-response.md` skeleton, swap in matching opener + data.

## Iris Credential Matrix

| Topic | Use this credential opening | Specific data to cite |
|---|---|---|
| Product Hunt launches | "Across our 30 PH #1 wins (2020-2026)..." | hunter activity r=0.61 / 60% LinkedIn DM open / Wed 12:01 PST sweet spot |
| GitHub stars / OSS growth | "Running AFFiNE from 0 to 60K GitHub stars..." | 43 days to 10k / Day 5 Trending +1,100 / 28 Trending appearances |
| SEO for indie founders | "Auditing 58 indie SaaS blogs in Q2 2026..." | 0.035% baseline CTR / 43 titles needed shortening / Layout-level fixes 20 pages |
| GEO / AI search | "Our 2026 GEO audit measured 71k sites..." | 0.29% AI traffic / 40% AIO click loss / 18% Perplexity grounds Quora |
| Social listening tools | "Our 27-tool 2026 audit showed..." | 22% multilingual / $79 median / 35% 90-day churn |
| Community building | "Tracking 47 dev Meetup groups in 2026..." | 30-80 hand-raisers per Meetup talk / Reddit r/selfhosted leads |
| B2B SaaS growth | "PLG vs SLG decision data from..." | [add specific numbers when available] |

## Quote-rate boosters (combine ALL for ~25% rate)

1. Reply within 4 hours of HARO email (2x multiplier)
2. Specific number in first sentence (2x)
3. Personal anecdote (1.5x)
4. Credential in signature (1.5x)
5. Disclosure paragraph (1.2x)
6. Niche match — skip off-topic queries (3x)

## What NOT to respond to

- Generic "any expert" requests
- Topics outside Iris's 7 credential areas above
- Queries from outlets with DR < 30 (low backlink value)
- Queries due in < 30 min (high pressure = low quality response)

## Weekly target

- Read 15-20 HARO emails (about 3 daily HAROs × 7 days)
- Respond to 3-5 highest-fit
- Expected: 1-2 quotes published per month at 15-25% rate

## Tracking — log every response

```jsonl
{"date":"YYYY-MM-DD","channel":"HARO","query":"...","outlet":"...","credential_used":"PH/OSS/SEO/GEO/Social/Community/B2B","response_word_count":N,"published":false,"url_if_published":""}
```
