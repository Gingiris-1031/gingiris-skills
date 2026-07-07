# Enterprise Deal Execution · Framework Reference
> Distilled from a multi-agent OSS commercialization retrospective ($0 → $500K ARR) and 2024-2026 client work across 105+ projects.
> This is the framework layer; the full operator layer (contract-clause quick cards, the 12-question pre-signing checklist, negotiation scripts) ships with the Gingiris paid field manual → https://gingiris.tools/playbook/2b-deals/

## The six-step deal flow

```
CEO-level contact → business owners confirm requirements → quote
→ contract (signed together with the SOW) + prepayment → phase-1 delivery → recurring reviews
```

- Review cadence: 1–2 reviews for a 10-day project; at least biweekly for month-long projects
- Map the org early: CEO owns the business case, CTO owns tech, procurement pushes process. Chase the tail payment through procurement — escalate to the CEO at most twice
- Sign contracts only after the **final requirement confirmation** is signed — never off meeting notes

## The four-part quote

Commercial license | private deployment (**quote the build fee and the deployment service fee separately**) | engineering support (person-days) | expert advisory

- **30% due the day the contract is signed** — a floor, not a target
- Requests you don't want: price them up (pad person-days) instead of refusing
- Seat-count gate: custom deployment only above N seats — small accounts route to standard SaaS

## SOR / SOW / CCB

- Keep the SOR (customer's raw asks) separate from the SOW (acceptance criteria + delivery milestones + change terms); **sign the SOW with the contract**
- SOW essentials: verifiable delivery descriptions / milestone table / change terms / per-item acceptance criteria / a named acceptance contact
- All changes go through a CCB: written initiation by the customer → both PMs assess cost/schedule impact → signed change confirmation. Verbal changes don't exist
- Paper-trail everything; **only paperwork counts**

## Payment structure & final-installment defense

- Staged payments: **3:4:3 or 4:4:2** (first features live / full deployment / after 3–6 months of ops)
- Late penalty in the contract: 0.5% per day overdue
- Leverage: keep 1–2 features running on **your own servers** until the final payment clears — disclosed before signing, written into the terms
- Collection path: highest-ranking contact → CEO (≤2 asks) → structural fallbacks
- Direction of travel: prepayment up, tail payment down, every deal
- During fundraising: standardized offering + channel distribution beats KA custom work (slow collection, weak narrative value)

## The only two real reasons for private deployment

Data privacy + internal permission-system integration. Everything else routes back to SaaS.
SaaS customization → sell a license; integrations → open API + standard docs, customer builds it; universal integrations (Google/GitHub sign-in) are product features, not custom projects.

## Commercial push-pull

Customer asks for 50 features, you could do 40 → "we can commit to 10 — and because we want this to succeed, we'll stretch to 15." Turn concessions into favors; the rest becomes phase two — another contract.

## Channel tiers

| Tier | Threshold | Terms |
|---|---|---|
| Reseller | — | 10–20% referral |
| Silver | $100k/yr sales | 15% |
| Gold | $300k/yr sales | 20% |

Supply at 20% off list; resale capped at 1.2× list. Due-diligence three questions: what did you resell before? where do your customers come from? reseller or service partner?

## Decomposing $1M ARR

9 × $100k enterprise accounts (standard service $30–50k + implementation $30k + training $20k) or ~5,000 × $200/yr subscribers (≈500 per $100k) — run a small closed loop on each leg before committing resources.
Pace benchmark: a $100k deal closing in 2 months is healthy; anything not serving revenue data gets deprioritized.
