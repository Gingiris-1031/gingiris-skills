---
name: gr-ai-content-ops
description: >-
  Build or audit an evidence-led AI content operation: source libraries, channel roles,
  weekly calendars, editorial gates, repurposing, distribution receipts and business
  measurement. Use when planning 内容运营、内容矩阵、周排期、多平台分发、素材库 and content workflow
  recovery. For a single supplied article rewrite, keep the scope to that deliverable.
license: MIT
metadata:
  version: "1.0.0"
  author: Gingiris
---

# AI Content Operations / AI 内容运营

Turn real material into a manageable content operation whose delivery and outcomes can be checked. Work in the user's language. Deliver the requested scope; a single-platform team does not need a multi-channel matrix.

## Start with the constraint

Use supplied context first. Resolve only missing decisions that change the work:

- Audience and next action: who should learn, try, register, request a demo or buy?
- Product comprehension: do people need a definition, proof, or an onboarding tutorial?
- Available evidence, publishing rights, existing channels, recent results and weekly capacity.
- Requested endpoint: diagnosis, weekly plan, draft pack, authorized distribution, or review.

When analytics or history are unavailable, mark the gap and produce a bounded pilot. Do not invent performance or claim that an account was audited. A user's request to plan or draft does not authorize sending messages or publishing posts.

## 1. Choose a content engine and channel roles

Separate owned expertise, user contributions and external commissioned/curated material. Track each line's acquisition cost, review work and reuse rights. Do not assume owned claims are more credible than independently evidenced user claims.

Select a primary channel using observed acquisition and audience behavior. Possible engines are a person's trust, search discovery, or a community's contributor relationships; mixed and unknown are valid outcomes. Product demos can establish comprehension, case evidence can address doubts, and tutorials can reduce activation friction. Treat these as hypotheses to test.

Assign each chosen channel one job, a suitable format and a next step. Distinguish founder and company accounts so they have a reason to coexist. Avoid adding channels before the present workflow fits capacity. See [channel decisions](references/channels.md).

## 2. Build a usable source queue

Preserve raw material separately from publication-ready extracts. For each extract record source, date, exact locator, speaker, claim, verification state and allowed audience. A private transcript is not public evidence; anonymization alone does not settle permission or reidentification risk.

Check suspected transcription errors, names, numbers and speaker attribution against original audio or a responsible person. Keep the original wording alongside corrections. Never manufacture first-person experience, testimonials or quotations.

Distinguish verified observation, attributed self-report, proposal, editorial interpretation and unknown. Freshness-sensitive numbers need a dated check. See [source and review gates](references/editorial.md).

## 3. Turn the queue into a feasible week

Group historical results by comparable audience, format, objective and measurement window. State sample size and denominators; a title correlation is not a causal rule. Combine this analysis with recurring user questions and search evidence.

Choose topics with a specific audience, a supportable point and a useful action. A contrarian angle is optional; never manufacture one to pass a scoring rubric. Map one reviewed parent asset to only the variants the team can finish and distribute.

Use absolute dates and time zones, an owner, reviewer, estimate, evidence link and delivery state. Keep parent/variant identifiers and separate domestic and international language/audience needs where relevant. If over capacity, reduce scope or cadence before adding people. Use [templates](references/templates.md).

## 4. Produce through three gates

1. **Evidence:** check material factual claims and quotations; resolve unsupported claims, label uncertainty or remove them. One authoritative source may be enough; a second source is useful where claims are disputed or weak.
2. **Voice:** use authentic writing samples and the user's intended context. AI may propose viewpoints; do not present them as the author's established beliefs or experiences without support. Remove filler, fabricated certainty and unnecessary sales claims.
3. **Disclosure and rights:** confirm permission for identifiable user stories, client details, screenshots and external content. Check hidden names, links and account details in media. Remove material beyond the approved public scope.

Then adapt the reviewed parent for the selected channel. Preserve meaning and important qualifiers; record intentional shortening. For cards or clips, reconcile the source sections with outputs so pagination or cutting cannot silently drop content. Check clipping, overflow, captions, images and readable mobile previews.

Platform limits and UI selectors change. Verify current official documentation or the actual editor before enforcing limits; do not reuse old byte/character counts or automation selectors as facts.

## 5. Deliver and recover without duplication

Default to a draft pack. Execute publishing or outreach only within explicit authorization already present in the conversation; preserve exact-copy, date, account and channel constraints.

Before an authorized submission, check accessible history and the operation ledger for the content ID, parent/topic, platform, account and approved slot. Report the coverage window if history is incomplete; never claim exhaustive deduplication from a sample.

Record separate receipts for platform acceptance, content readback and subsequent metrics. A request success or scheduled state is not proof of public publication. Read back title/text/media on the appropriate surface.

On timeout or ambiguous status, mark **unknown**, inspect history/backend before any retry, and stop duplicate submissions. On a confirmed failure, record the failed step and recovery owner. Do not move a post to another day or channel without authorization. For partial delivery, reconcile every target before resuming.

Prepare guest/contributor announcements as drafts with the asset and verified link. Send only when explicitly authorized, with the intended recipient/channel checked. Never imply that a content plan grants permission to contact people. See [delivery and measurement](references/delivery.md).

## 6. Review what happened

Separate content performance, account development and business outcomes. Specify collection time, window, numerator, denominator and missing values. Engagement is not conversion; an unavailable metric is not zero.

Compare typical performance using medians alongside sample sizes, means and outliers when useful. Isolate paid amplification and activity-driven cohorts where possible. Trace attributable business actions with available campaign links, codes or user reports, while disclosing attribution gaps.

End with the supported decision: continue, change, stop or gather missing evidence; assign an owner and next review date. A future check is a scheduled task only if a real scheduler was configured with authorization. Otherwise deliver a dated checklist and say it has not been scheduled.

## Deliverables and completion

Select only the artifacts needed: channel diagnosis, source register, topic queue, weekly calendar, reviewed parent and variants, distribution ledger, or review memo. Use the copyable fields in [templates](references/templates.md).

A plan is complete when work fits capacity and every item has an owner, evidence state and next step. A draft is complete when reviews and media checks are recorded. Distribution is complete only for targets with verified receipts; failed, unknown or unapproved targets remain explicit. A review is complete when its evidence window, gaps and next decision are stated.

## Boundaries with related workflows

This skill coordinates the operation. If installed, `gr-wechat-editorial` can handle a WeChat article/draft handoff, `gr-social-distill` can adapt a supplied article, and `gr-brand-voice-calibration` can build a detailed voice guide. None is required: the references here support a standalone workflow. Creator compensation/program design belongs in a dedicated UGC workflow when requested.

See [design provenance](references/provenance.md) for what was retained and intentionally not generalized from the source guide.
