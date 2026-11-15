---
name: gr-ai-content-ops
description: >-
  Build or audit an evidence-led AI content operation: competitor research, SEO/GEO keyword and content positioning, source libraries, channel roles,
  weekly calendars, editorial gates, repurposing, distribution receipts and business
  measurement. Use when planning 内容运营、内容矩阵、周排期、多平台分发、素材库 and content workflow
  recovery, 选题、内容日历、内容SOP、一鱼多吃、内容复盘 and publishing receipts.
  For a single supplied article rewrite, keep the scope to that deliverable.
license: MIT
metadata:
  version: "1.5.0"
  author: Gingiris
---

# AI Content Operations / AI 内容运营

Turn real material into a manageable content operation whose delivery and outcomes can be checked. Work in the user's language. Deliver the requested scope; a single-platform team does not need a multi-channel matrix.

## Start with the reader's reason to care

The primary editorial goal is useful, engaging content for the intended reader. Workflow completion, word count, keywords and publishing volume are supporting constraints, not evidence of good content. Before choosing a format or drafting, identify a concrete reader situation, what is at stake, and the new understanding or useful outcome the piece delivers. Use actual customer questions, sales/support conversations, relevant audience discussions and observed content responses where available. Label inferred audience needs; don't pretend an imagined persona has validated them.

Use the [audience-first editorial gate](references/audience-first.md). Draft competing angles, choose the one with the clearest reader value and specific support, then write. SEO should help the right reader discover that answer; it should not turn the piece into generic advice. A demo should reveal behavior the reader cares about, not simply display a feature.

## Start with the constraint

Use supplied context first. Resolve only missing decisions that change the work:

- Audience and next action: who should learn, try, register, request a demo or buy?
- Product comprehension: do people need a definition, proof, or an onboarding tutorial?
- Available evidence, publishing rights, existing channels, recent results and weekly capacity.
- Requested endpoint: diagnosis, weekly plan, draft pack, authorized distribution, or review.

### Ask a short, adaptive intake

For strategy or planning, proactively ask for missing context that would materially improve the result. Start with at most three short questions, in the user's language; skip anything already supplied:

1. What is the product website (or a short description if it is not public yet)?
2. Which 1–2 competitors or reference brands should we study? Share URLs if available, and whether the interest is their early launch or current content. “Not sure” is a valid answer.
3. Who should the content reach, and what is the priority action this month: awareness, trial, demo requests or qualified leads?

Use the [intake template](references/templates.md#0-adaptive-intake) as phrasing guidance, not a mandatory questionnaire. Ask a later targeted question about geography/language, existing accounts, usable proof or weekly capacity only when it changes a decision. Do not make the user fill out every field before starting.

While awaiting answers, inspect supplied public sources and continue independent work. If competitors are unknown, propose candidates based on buyer and use case, label them provisional and explain the fit. If a URL is inaccessible, ask for a product description or accessible source; never claim to have audited it. If the user wants an immediate plan, state assumptions and proceed, retaining unresolved choices in the handoff. Do not finalize dependent choices while a necessary clarification is pending. User-provided facts, website claims, verified observations and planning assumptions remain distinct.

Before treating analytics or history as unavailable, check accessible exports, connected tools and existing project records. Distinguish not retrieved, access blocked, not instrumented and genuinely absent. For a diagnosis, retrieve the cheapest discriminating fields before proposing a long experiment; use [diagnosis](references/diagnosis.md). For a new account with no history, produce a baseline plan. Do not invent performance or claim that an account was audited. A user's request to plan or draft does not authorize sending messages or publishing posts.

## Before choosing channels: learn from comparable competitors

For a new strategy, first-month plan, or requested competitor benchmark, research 1–2 comparable products before fixing topics and cadence. Use a dated early-stage window when studying cold start; current content is not evidence of launch strategy. A supplied single-article rewrite does not need this step.

Connect dated original assets to audience, message, proof, CTA and accessible response evidence. Distinguish observed content from self-reported results and causal explanations. Assess differences in buyer, stage, product readiness and distribution resources before transferring a tactic. Turn each useful finding into a specific plan change and a measurable experiment; do not deliver only a competitor inventory. If historical evidence is inaccessible, disclose the gap and proceed with an explicit hypothesis.

Use [competitor content research](references/competitor-content.md) and its evidence card. Keep this workflow standalone; an installed `gr-competitor` may support deeper research when needed.

## Initialize only the operating state the task needs

For recurring planning, delivery or diagnosis, reuse the existing project workspace or establish a named local output directory. Record the path, current revision, evidence register and delivery ledger using [fields and persistence](references/fields.md). A one-off rewrite needs only its source and draft, not a complete operations database. Missing material preparation becomes a scheduled production task; missing names become unassigned roles with a handoff deadline. See [intake and recovery](references/intake.md).

## 1. Choose a content engine and channel roles

Separate owned expertise, user contributions and external commissioned/curated material. Track each line's acquisition cost, review work and reuse rights. Do not assume owned claims are more credible than independently evidenced user claims.

Select a primary channel using observed acquisition and audience behavior. Possible engines are a person's trust, search discovery, or a community's contributor relationships; mixed and unknown are valid outcomes. Product demos can establish comprehension, case evidence can address doubts, and tutorials can reduce activation friction. Treat these as hypotheses to test.

Assign each chosen channel one job, a suitable format and a next step. Distinguish founder and company accounts so they have a reason to coexist. Avoid adding channels before the present workflow fits capacity. See [channel decisions](references/channels.md).

### Choose and audit the parent asset before setting cadence

For a website-backed content plan, inventory existing guides, comparison pages, reports and demos before proposing new articles. Choose update, create, consolidate or defer by buyer intent, evidence readiness and conversion path. A blog-first plan is appropriate when a durable answer supports discovery and evaluation; demo-first or social-first may be better when comprehension or rapid feedback is the bottleneck. Do not make four blogs/eight posts a universal quota.

Audit existing owned content before repurposing it: publication does not validate statistics, first-person stories, comparative claims or onboarding promises. Resolve contradictions, add evidence or remove unsupported claims. Map each selected parent to a standalone social argument, an informative visual and a verified next step; keep internal review notes out of publishable copy. See [website-to-social workflow](references/website-to-social.md) and [two worked cases](references/worked-cases.md).

### Establish the search and content position before drafting blogs

For search-oriented blog planning/writing, produce a compact [SEO/GEO positioning brief](references/search-positioning.md) before drafting. Identify the buyer question, target market/language, primary intent cluster, supporting queries/entities, search-result page types, existing URL ownership, unique evidence/angle and next business action. Content position means the role and differentiated promise of the article, not merely its target ranking.

Verify keywords with available first-party query data, current localized search results and keyword tools. Record sources/dates and distinguish observed demand from candidate phrases; unknown volume, difficulty or AI visibility is not zero. Do not force all intents into blogs or create new URLs for synonymous queries. Connect each section to a reader question and useful evidence, then map the article to native social angles. Missing keyword-tool access permits a provisional brief and draft, not invented metrics or an optimization-complete claim.

## 2. Build a usable source queue

Preserve raw material separately from publication-ready extracts. For each extract record source, date, exact locator, speaker, claim, verification state and allowed audience. A private transcript is not public evidence; anonymization alone does not settle permission or reidentification risk.

Check suspected transcription errors, names, numbers and speaker attribution against original audio or a responsible person. Keep the original wording alongside corrections. Never manufacture first-person experience, testimonials or quotations.

Distinguish verified observation, attributed self-report, proposal, editorial interpretation and unknown. Freshness-sensitive numbers need a dated check. See [source and review gates](references/editorial.md).

## 3. Turn the queue into a feasible week

Group historical results by comparable audience, format, objective and measurement window. State sample size and denominators; a title correlation is not a causal rule. Combine this analysis with recurring user questions and search evidence.

Choose topics with a specific audience, a supportable point and a useful action. A contrarian angle is optional; never manufacture one to pass a scoring rubric. Map one reviewed parent asset to only the variants the team can finish and distribute.

Use absolute dates and time zones, an owner, reviewer, estimate, evidence link and delivery state. Keep parent/variant identifiers and separate domestic and international language/audience needs where relevant. If over capacity, reduce scope or cadence before adding people. Use [templates](references/templates.md).

### Write to substantive depth

For LinkedIn analysis and case posts, deliver a complete native argument, not a short teaser or a stretched X post. Include a concrete situation, relevant evidence/example, interpretation, practical action and a relevant next step. As a drafting heuristic, 180–300 English words often provides room; adapt to substance and current editor limits rather than enforcing a quota. Add depth through decisions and examples, not repeated disclaimers. For blog drafts, deliver the full requested article rather than an outline labeled as a draft.

Treat user-confirmed owned material as usable first-party source material. Assist with claim-level checks of freshness, units, sources and product behavior; 'not independently verified' does not mean false. Preserve supported detail and authentic narrative instead of replacing the whole case with generic advice. Separate user confirmation, published-source consistency and independent verification in internal notes. Narrow unresolved checks to affected claims; do not block unrelated copy. Keep only reader-relevant qualifiers in the post and move production checks to a separate review sheet.

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

For a diagnosis, compare plausible causes, name the evidence that would weaken each, and prefer a cheap discriminating check. Use [diagnosis](references/diagnosis.md) before proposing an experiment. End with the supported decision: continue, change, stop, gather missing evidence or inconclusive; assign an owner and next review date. A future check is a scheduled task only if a real scheduler was configured with authorization. Otherwise deliver a dated checklist and say it has not been scheduled.

## Deliverables and completion

Select only the artifacts needed: channel diagnosis, source register, topic queue, weekly calendar, reviewed parent and variants, distribution ledger, or review memo. Use the copyable fields in [templates](references/templates.md).

A plan is complete when work fits capacity and every item has an owner (or an unassigned role with an assignment deadline), evidence state and next step. A draft is complete when reviews and media checks are recorded. Distribution is complete only for targets with verified receipts; failed, unknown or unapproved targets remain explicit. A review is complete when its evidence window, gaps and next decision are stated.

## Boundaries with related workflows

This skill coordinates the operation. If installed, `gr-wechat-editorial` can handle a WeChat article/draft handoff, `gr-social-distill` can adapt a supplied article, and `gr-brand-voice-calibration` can build a detailed voice guide. None is required: the references here support a standalone workflow. Creator compensation/program design belongs in a dedicated UGC workflow when requested.

See [design provenance](references/provenance.md) for what was retained and intentionally not generalized from the source guide.
