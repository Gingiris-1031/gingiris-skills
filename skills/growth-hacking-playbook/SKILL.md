---
name: growth-hacking-playbook
description: Design, prioritize and run measurable growth experiments across acquisition, activation, retention, referral and revenue. Use when a startup needs an experiment backlog, ICE/RICE prioritization, referral or UGC loops, rapid weekly testing, causal measurement, or stop conditions without spam, fake accounts or dark patterns.
---

# Growth Experiment System — From Idea to Decision

Do not start from a list of hacks. Start from the constrained stage of the funnel and run the smallest experiment that can change a decision.

## 1. Define the growth model

Record:

```text
ICP | value event | acquisition source | activation event | retained-use event | paid event | referral event
```

Build the baseline funnel by cohort. For consumer products include D1/D7/D30 retention; for B2B include qualified pipeline, sales cycle and collected revenue. If the events are not instrumented, instrumentation is experiment zero.

## 2. Find the constraint

| Signal | Constraint | Do next |
|---|---|---|
| Low qualified traffic | acquisition | test one audience/channel-message pair |
| Signup but no value event | activation | remove the highest-friction step |
| Activation but low repeat use | retention | interview churned and retained cohorts |
| Retained but no payment | revenue | test packaging, price or sales assist |
| Happy retained users, low sharing | referral | add a value-aligned share loop |

Never scale acquisition into a broken activation or retention funnel.

## 3. Write testable hypotheses

Use:

```text
For [segment], changing [one variable] from [control] to [variant]
will move [primary metric] from [baseline] to [threshold] within [window],
because [evidence]. Guardrails: [retention, quality, complaints, cost].
```

Every experiment needs an owner, start/end date, audience, sample/decision rule, source tracking, maximum cost and rollback.

## 4. Prioritize without fake precision

Score Impact, Confidence and Ease from 1–10. Confidence must cite evidence:

- 9–10: repeated internal behavior or completed experiment;
- 6–8: interviews plus behavioral data or strong adjacent case;
- 3–5: external benchmark only;
- 1–2: opinion.

Use ICE only to order the backlog. It does not replace judgment about dependencies, ethics or sample size.

## 5. Experiment library

### Acquisition

- 200-person founder outreach with segment/source/reply/activation tracking;
- competitor comparison or migration page;
- community-native Reddit/HN/tutorial post with disclosed affiliation;
- creator/KOL pilot with individual UTMs;
- SEO/GEO evidence page answering one high-intent question.

### Activation

- shorten time to first value;
- replace generic onboarding with use-case routing;
- preload a safe example project;
- move permissions to the moment they are needed;
- trigger human help after a repeated failure.

### Retention

- interview retained and churned cohorts separately;
- improve the recurring job, not notification volume;
- lifecycle reminder tied to unfinished value;
- weekly progress artifact the user would miss;
- team collaboration only where it improves the job.

### Referral and UGC loops

Design the loop:

```text
retained user → natural share trigger → useful artifact/invite → qualified recipient → activation → new share trigger
```

UGC works when the output itself is valuable or identity-enhancing. Track share rate, recipient activation, viral coefficient `K = invites per user × invite conversion`, retention and incentive cost. Do not pay for empty invitations or reward low-quality accounts.

### Revenue

- willingness-to-pay interviews followed by real checkout behavior;
- packaging test around value/usage boundaries;
- sales assist triggered by team/product signals;
- annual-plan or expansion test with churn guardrails.

## 6. Weekly cadence

- Monday: review funnel and select at most three independent tests.
- Tuesday: QA instrumentation and launch.
- Wednesday–Thursday: monitor guardrails; do not change the variant mid-test.
- Friday: decide keep, iterate or kill and write the learning in the backlog.

Parallel tests must not target the same users or metric unless interaction effects are explicitly designed.

## 7. Decision rules

Keep only when the primary metric crosses the threshold and guardrails remain healthy. Iterate when direction is positive but the mechanism is unclear. Kill when the effect is below the minimum useful lift, cost exceeds the cap, quality declines or the channel creates policy/community risk.

Do not report impressions as growth. Report activated, retained, referred and paid cohorts plus CAC/LTV where mature enough.

## Historical evidence boundary

The Gingiris library contains a planning case with a ¥1M budget and 500K-registration target (implied CAC ¥2), using UGC/ambassador and referral loops. It is a target model, not a verified result. Use it to audit arithmetic and assumptions, never as proof of achieved CAC.

## Required output

Return:

1. funnel baseline and constraint;
2. ranked backlog with evidence-based confidence;
3. experiment cards with hypothesis, owner, metrics, guardrails and rollback;
4. weekly calendar;
5. decision log and next experiment.

## Compliance

Reject spam, bought engagement, sockpuppets, fake reviews, undisclosed promotion, scraping private data, coercive referrals and dark patterns. Optimize user value before virality.
