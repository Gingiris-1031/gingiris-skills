# Product × Engineering × Operations Alignment SOP

Everything serves commercialization. From unified backlog to 10-day sprint cadence to release veto power.

## Why the Three Teams Misalign

- **New features vs. user feedback**: dev chases new features while reported bugs sit for months — no unified priority mechanism
- **What eng wants vs. what ops needs**: eng thinks ops doesn't get tech, ops thinks eng ignores users — no shared goal
- **Fast vs. stable**: growing before the product form stabilizes piles up tech debt — no clear product-stage judgment

Four fixes: one unified board, a commercial metric per sprint (e.g., signup→paid 4.5% → 7%), ops veto on releases, tri-party alignment before every sprint.

## Dual-Layer Kanban

- **Master backlog**: every raw issue (user feedback / competitor / strategy) enters one pool first
- **Sprint board**: only reviewed, scheduled items flow downstream into it
- **Issue discipline**: every ops-filed issue must include reproduction steps — unreproducible means unfixable
- **Auto-escalation**: same issue reported 3+ times → `severe` tag, must be fixed in the next sprint
- **Triage**: Bugs go straight to the bug board; feature requests need a product spec before entering a sprint

## 10-Day Sprint Cadence

- Day 1 dev starts → Day 6 testable build (ops finishes testing within half a day) → Day 7 alignment meeting (20-30 min) → Day 9 launch assets ready → Day 10 ship
- Cycle by stage: PMF validation 1-2 weeks, growth 3-4 weeks, mature 6-8 weeks — modern web teams should compress to 10 days-2 weeks
- **Red line**: never ship on a Friday or weekend

## Meeting Rhythm

- **Daily standup**: 15 min, standing; each person covers yesterday / today / blockers; ops reports complaint hotspots
- **Sprint planning** (30-60 min): last-sprint retro → Top-3 goals tied to commercial value → scope confirmation
- **Sprint review** (30 min) + **monthly review** (60-90 min); any meeting over an hour means someone is coasting

## Ops Veto Power

If a P0 bug that hurts UX or paid conversion is unfixed before release, ops can propose delaying the ship. P0 = payment failures, core function down, data errors. Layout glitches are P1; copy typos are P2.

## Resources & Tech Debt

- Split: 50-60% new features / 20-30% bug fixes / 20-30% tech debt
- Refactors get a separate project (1-3 months), run parallel to normal releases, and end with full regression testing (3-5 core users)

## Sprint Health Benchmarks

| Check | Healthy | Warning |
|-------|---------|---------|
| Avg P0 fix time | ≤2 days | >3 days |
| Features shipped on time | ≥80% | <60% |
| Avg feedback response time | ≤24 h | >48 h |
| Same bug re-reported | ≤2 times | ≥3 times |
| Test report submitted | 100% by Day 6.5 | over half a day late |

## Related Gingiris Skills
- User interview SOP: https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-user-interview
- All skills: https://clawhub.ai/gingiris-1031
