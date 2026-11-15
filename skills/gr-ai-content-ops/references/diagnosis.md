# Diagnose before prescribing / 先诊断再开方案

## Retrieve before marking unknown

Check available project files, authorized connectors and backend exports before asking the user to supply data. Record field, location, window, availability, owner and next action. If retrieval requires access, request that missing access without asking for secrets in chat; progress independent work. Distinguish not-retrieved, access-blocked, not-instrumented, absent and unavailable-attempted. Retrieval cost is an estimate, not a universal two-hour promise.

Collect only fields that affect the decision: exposure/delivery denominator, source mix, meaningful reading or interactions, destination visits and business events. Platform definitions differ. A low read count could reflect fewer deliveries, a weak opening, a mismatch in audience or a tracking issue. A memory estimate can motivate checks but cannot substitute for an export.

## Compare causes and discriminate cheaply

| Hypothesis / 原因假设 | Expected signal / 预期信号 | Discriminating field / 判别字段 | What weakens it / 反证 | Access and cost / 获取成本 | Next check / 下一步 |
|---|---|---|---|---|---|
| Distribution fell | Lower deliveries or qualified reach | Delivery count/source mix | Reach stable with comparable cohort | Check existing export | Compare matched windows |
| Opening does not connect | Exposure stable, opening/click response lower | Platform-defined response rate | Response stable, drop occurs later | Check post detail | Inspect hook and audience fit |
| Promise and destination mismatch | Relevant visits, little next-step activity | Landing events, feedback | Visits never arrive or event is broken | Inspect analytics and flow | Check instrumentation and reader task |

These are possible concurrent causes, not forced mutually exclusive categories. Use as many hypotheses as evidence warrants. Check measurement definitions first; if exposure falls, inspect distribution before blaming the article. If exposure holds but engagement falls, examine audience/packaging with comparable samples. If visits arrive but conversion falls, inspect destination, offer and instrumentation. These signals narrow inquiry; none proves causation.

## Choose a test that can answer the question

Define the decision, unit of analysis, baseline, primary outcome, meaningful effect, expected sample, window and confounders. Posts/users are not interchangeable independent units. For a formal A/B test, justify sample size/power or detectable effect using an appropriate method and stated assumptions. If no defensible baseline/sample exists, use exploratory feedback or baseline collection rather than fabricated precision. A small sample or a 1.4x difference is inconclusive without uncertainty/context; it is not automatically proof or noise.

Prefer one interpretable change where feasible. When several changes are necessary, record them and limit attribution. Instrumentation repair can change comparability even if it is not the content treatment. Inconclusive is valid when data cannot discriminate: record the decision affected, missing evidence and cheapest next step. Do not require a fictional power calculation to admit uncertainty.

## Memo / 诊断交付

Observation + source/window → competing explanations → discriminating checks and results → supported decision or inconclusive → owner/deadline. For reader appeal, add the actual audience question and what the draft rewards the reader with. Operational metrics do not replace editorial judgment or target-reader feedback.
