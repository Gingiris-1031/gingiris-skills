# Gingiris Skills — AI Agent Workflows for Growth Teams

Installable workflows for founders and operators working on content, customer research, SEO/GEO, launches and community. Start with one concrete task: provide your product context and evidence, then receive a draft, research report or decision plan you can review.

面向创始人与增长运营团队的 Agent Skills：围绕内容、用户研究、SEO/GEO、发布与社区任务，交付可审阅的草稿、研究和行动方案。

## Start with one task / 从一个任务开始

Requires Node.js/npm for this installation route and an agent host that supports Skills. Choose the target agent in the installer.

```bash
npx skills@1.7.4 add Gingiris-1031/gingiris-skills --skill gr
```

```text
Use gr. We have an early-stage SaaS and trial signups, but users do not finish setup.
Choose the next workflow and explain what evidence we need before proposing a campaign.
```

Already know the task? Install one specialist instead:

```bash
npx skills@1.7.4 add Gingiris-1031/gingiris-skills --skill gr-ai-content-ops
```

Ask the agent to use the selected Skill and supply the inputs in its README. If it cannot find the Skill, check the selected agent and install scope, then start a fresh session. Installation does not connect analytics or publish content.

## Choose by the result you need / 按交付目标选择

| Task / 任务 | Skill | Result / 交付 |
|---|---|---|
| 增长任务路由 | [gr](skills/gr/README.md) | Route and rationale; minimal missing inputs; one specialist handoff |
| AI 内容运营 | [gr-ai-content-ops](skills/gr-ai-content-ops/README.md) | Audience and angle brief; SEO/GEO page intent; full drafts; visual briefs; calendar and review ledger |
| 文章转社媒草稿 | [gr-social-distill](skills/gr-social-distill/README.md) | Requested platform drafts; source links; adaptation notes; optional carousel or image brief |
| 个人与品牌文风校准 | [gr-brand-voice-calibration](skills/gr-brand-voice-calibration/README.md) | Source index; contextual voice rules; counterexamples; test draft; unresolved preferences |
| 微信公众号内容工作流 | [gr-wechat-editorial](skills/gr-wechat-editorial/README.md) | Article Markdown and HTML; source map; review notes; asset checklist; draft receipt when access is available |
| OPC 服务与试单验证 | [gr-opc-service-validation](skills/gr-opc-service-validation/README.md) | Offer definition; client-fit checklist; pilot card; capacity and pricing assumptions; continue/change/stop decision |
| 竞品研究与决策 | [competitor-research-playbook](skills/competitor-research-playbook/README.md) | Benchmark rationale; historical timeline; evidence register; counterevidence; action card |
| 竞品分析执行入口 | [gr-competitor](skills/gr-competitor/README.md) | Scope and selection rationale; dated sources; unknowns and counterevidence; experiment handoff |
| 用户访谈与需求验收 | [gr-user-interview](skills/gr-user-interview/README.md) | Screening and interview plan; evidence synthesis; requirement and acceptance card; follow-up plan |
| 用户研究与冷启动运营 | [gingiris-user-interview](skills/gingiris-user-interview/README.md) | Research plan; task-based Beta design; adoption barriers; cohort follow-up and cold-start decision card |
| UGC 创作者与素材实验 | [gingiris-ugc-matrix](skills/gingiris-ugc-matrix/README.md) | Goal card; creator criteria; brief and acceptance rules; asset ledger; attribution and settlement plan |
| X 与社媒账号运营 | [gingiris-twitter-agent-ops](skills/gingiris-twitter-agent-ops/README.md) | Reviewed draft; media readiness checklist; publication receipt when authorized; measurement and recovery notes |
| GitHub README 写作 | [gr-readme](skills/gr-readme/README.md) | Positioning sentence; rewritten README; quick-start and expected output; review checklist |
| 外链研究与合作准备 | [gr-backlinks](skills/gr-backlinks/README.md) | Opportunity shortlist; relevance checks; pitch drafts; submission ledger; measurement plan |
| 开源增长渠道归因 | [oss-growth-attribution](skills/oss-growth-attribution/README.md) | Stage timeline; original content links; evidence grades; modeled ranges; next-stage research and measurement plan |
| 开发者与用户社区运营 | [community-building-playbook](skills/community-building-playbook/README.md) | Readiness review; platform and onboarding plan; event brief; content rhythm; community health measures |

## How the workflows connect

Research a buyer or competitor → decide what the audience needs → produce a useful source asset → adapt it to selected channels → review delivery and outcomes. Use only the steps relevant to your request.

- **Content planning vs repurposing:** `gr-ai-content-ops` chooses topics and operating scope; `gr-social-distill` adapts a supplied article.
- **Voice vs facts:** `gr-brand-voice-calibration` learns expression from originals; it does not supply factual claims.
- **Research vs execution:** competitor and attribution reports support decisions; they do not automatically contact users or launch campaigns.
- **Playbook vs compact entry:** some packages share a method or serve as compatibility names. The count below is packages, not independent strategies.

## What is in this repository?

Each package contains a `SKILL.md` instruction file, with references, templates or scripts where available. The human-readable README explains when to use it, what to provide and what to expect. These are workflows for an agent, not trained models or a hosted automation service.

核心说明支持中英使用；部分历史包另有日语、韩语参考，具体以各包文件为准。不会把部分翻译说成全库完整四语覆盖。

## Complete package index

**65 source packages**, checked 2026-11-17. Related and compatibility entries are retained; use the task table above to choose a starting point.

[agent-workflow-playbook](skills/agent-workflow-playbook/README.md) | [ai-launch-playbook](skills/ai-launch-playbook/README.md) | [ai-product-launch](skills/ai-product-launch/README.md) | [aso-playbook](skills/aso-playbook/README.md) | [b2b-marketing-playbook](skills/b2b-marketing-playbook/README.md) | [community-ambassador-playbook](skills/community-ambassador-playbook/README.md) | [community-building-playbook](skills/community-building-playbook/README.md) | [competitor-research-playbook](skills/competitor-research-playbook/README.md) | [developer-marketing-playbook](skills/developer-marketing-playbook/README.md) | [devrel-playbook](skills/devrel-playbook/README.md) | [gingiris-aso-growth](skills/gingiris-aso-growth/README.md) | [gingiris-b2b-growth](skills/gingiris-b2b-growth/README.md) | [gingiris-github-star-growth](skills/gingiris-github-star-growth/README.md) | [gingiris-go-global](skills/gingiris-go-global/README.md) | [gingiris-growth-finder](skills/gingiris-growth-finder/README.md) | [gingiris-kol-outreach](skills/gingiris-kol-outreach/README.md) | [gingiris-launch](skills/gingiris-launch/README.md) | [gingiris-opensource](skills/gingiris-opensource/README.md) | [gingiris-seo-geo](skills/gingiris-seo-geo/README.md) | [gingiris-seo-geo-agent](skills/gingiris-seo-geo-agent/README.md) | [gingiris-twitter-agent-ops](skills/gingiris-twitter-agent-ops/README.md) | [gingiris-ugc-matrix](skills/gingiris-ugc-matrix/README.md) | [gingiris-user-interview](skills/gingiris-user-interview/README.md) | [github-stars-playbook](skills/github-stars-playbook/README.md) | [go-to-market-playbook](skills/go-to-market-playbook/README.md) | [gr](skills/gr/README.md) | [gr-ai-content-ops](skills/gr-ai-content-ops/README.md) | [gr-aso](skills/gr-aso/README.md) | [gr-b2b-growth](skills/gr-b2b-growth/README.md) | [gr-backlinks](skills/gr-backlinks/README.md) | [gr-blog-post](skills/gr-blog-post/README.md) | [gr-brand-voice-calibration](skills/gr-brand-voice-calibration/README.md) | [gr-community-ambassador](skills/gr-community-ambassador/README.md) | [gr-competitor](skills/gr-competitor/README.md) | [gr-competitor-research](skills/gr-competitor-research/README.md) | [gr-core](skills/gr-core/README.md) | [gr-geo-cite](skills/gr-geo-cite/README.md) | [gr-opc-service-validation](skills/gr-opc-service-validation/README.md) | [gr-oss-marketing](skills/gr-oss-marketing/README.md) | [gr-ph-launch](skills/gr-ph-launch/README.md) | [gr-product-dev-ops](skills/gr-product-dev-ops/README.md) | [gr-readme](skills/gr-readme/README.md) | [gr-seo-geo-agent](skills/gr-seo-geo-agent/README.md) | [gr-seo-patrol](skills/gr-seo-patrol/README.md) | [gr-social-distill](skills/gr-social-distill/README.md) | [gr-user-interview](skills/gr-user-interview/README.md) | [gr-wechat-editorial](skills/gr-wechat-editorial/README.md) | [growth-hacking-playbook](skills/growth-hacking-playbook/README.md) | [hardware-saas-gtm](skills/hardware-saas-gtm/README.md) | [kol-outreach](skills/kol-outreach/README.md) | [open-source-marketing-playbook](skills/open-source-marketing-playbook/README.md) | [oss-growth-attribution](skills/oss-growth-attribution/README.md) | [plg-playbook](skills/plg-playbook/README.md) | [product-hunt-launch-guide](skills/product-hunt-launch-guide/README.md) | [product-hunt-launch-playbook-win-1-daily](skills/product-hunt-launch-playbook-win-1-daily/README.md) | [product-hunt-playbook](skills/product-hunt-playbook/README.md) | [saas-growth-playbook](skills/saas-growth-playbook/README.md) | [saas-marketing-playbook](skills/saas-marketing-playbook/README.md) | [startup-consultant](skills/startup-consultant/README.md) | [startup-growth-playbook](skills/startup-growth-playbook/README.md) | [startup-launch](skills/startup-launch/README.md) | [startup-launch-playbook](skills/startup-launch-playbook/README.md) | [startup-marketing-playbook](skills/startup-marketing-playbook/README.md) | [team-motivation-ops](skills/team-motivation-ops/README.md) | [viral-marketing-playbook](skills/viral-marketing-playbook/README.md)

## Sources, limits and maintenance

Maintained by Iris Wei / Gingiris. Package examples distinguish observed facts, external claims, assumptions and illustrative outputs. Historical company results are not promises of future performance. Research requires access to its sources; analytics and publishing require the relevant tools and authorization.

For a reproducible issue, include the package name, agent environment, minimal non-private input, expected artifact and actual behavior in a [GitHub issue](https://github.com/Gingiris-1031/gingiris-skills/issues). Do not include credentials or private customer records.

[Browse the website](https://tools.gingiris.com/skills/) · [Hugging Face distribution](https://huggingface.co/Gingiris) · [MIT License](LICENSE)

The source repository is the maintenance home. Marketplace indexing, review and version display can lag behind a source release. Check each destination rather than assuming all mirrors are identical.

## Community and optional resources / 社群与可选资料

微信添加 **staywildgrow**，留言「**加入社群**」；也可咨询 **599 元资料包**。
Add **staywildgrow** on WeChat and send **“加入社群”**. The separate resource pack costs **CNY 599**. Neither is required to use the open-source Skills; hosted and managed services are separate.

## Additional workflow guides / 更多工作流说明

Documentation completed in three review batches on 2026-11-17. Package aliases and deprecated pointers remain explicitly labelled.

### Acquisition and operations / 获客与运营

| Workflow | Choose it for |
|---|---|
| [Agent Workflow Design / Agent 工作流设计](skills/agent-workflow-playbook/README.md) | Turn a recurring expert task into an evaluable agent workflow with input contracts, review gates and recovery. |
| [Developer Marketing / 开发者营销](skills/developer-marketing-playbook/README.md) | Help developers reach a first useful result through documentation, demos, tutorials and relevant community distribution. |
| [Developer Relations Operations / 开发者关系运营](skills/devrel-playbook/README.md) | Connect developer documentation, community activity and events to product adoption with a measurable program. |
| [GitHub Growth Sprint / GitHub 增长冲刺](skills/github-stars-playbook/README.md) | Plan a bounded repository discovery sprint using README readiness, relevant channels and downstream activation checks. |
| [Open-Source Campaign Execution / 开源场景营销执行](skills/gr-oss-marketing/README.md) | Prepare a concrete open-source campaign around a user task, working demo and evidence-backed distribution choices. |
| [Open-Source Launch Readiness / 开源发布准备](skills/open-source-marketing-playbook/README.md) | Help non-technical maintainers assemble a usable launch packet and a post-launch contributor and user loop. |
| [Community Ambassador Operations / 社区大使运营](skills/gr-community-ambassador/README.md) | Design ambassador recruitment, roles, incentives, events and retention around what members can actually contribute. |
| [Creator Outreach Drafting / 创作者邀约草稿](skills/kol-outreach/README.md) | Prepare relevant creator pitches, follow-up copy and a negotiation brief grounded in a specific audience and collaboration. |
| [Product Engineering Operations Alignment / 产研运协同](skills/gr-product-dev-ops/README.md) | Turn user feedback and delivery constraints into a shared backlog, decision ownership and a reviewable iteration plan. |
| [Growth Router Compatibility Entry / 增长路由兼容入口](skills/gr-core/README.md) | Explain the older growth router and direct new users to the maintained gr entry point. |
| [Technical SEO Audit and Monitoring / 技术 SEO 巡检](skills/gr-seo-patrol/README.md) | Inspect site health, search evidence and metadata issues, then separate verified findings from missing observations. |
| [AI Search Citation Tracking / AI 搜索引用追踪](skills/gr-geo-cite/README.md) | Check whether selected AI answers cite your pages and prepare evidence-grounded improvements to those pages. |

### Launch and publishing / 发布与内容

| Workflow | Choose it for |
|---|---|
| [AI Product Launch Strategy / AI 产品发布策略](skills/ai-launch-playbook/README.md) | Plan an AI-specific launch around a demonstrable task, credible positioning and an audience-matched rollout. |
| [First AI Product Launch Roadmap / 首个 AI 产品发布路线](skills/ai-product-launch/README.md) | Organize validation, MVP scope, Beta learning and launch preparation into a practical first-product roadmap. |
| [Go-to-Market Positioning and Channel Plan / GTM 定位与渠道规划](skills/go-to-market-playbook/README.md) | Connect the target buyer, category, differentiator and channel choices in a reusable launch strategy brief. |
| [Product Hunt Execution Checklist / Product Hunt 执行清单](skills/gr-ph-launch/README.md) | Prepare launch assets, maker copy, responsibilities and follow-up for a scoped Product Hunt launch. |
| [Product Hunt First-Time Guide / Product Hunt 首发指南](skills/product-hunt-launch-guide/README.md) | Help first-time makers understand the preparation choices, assets and follow-up involved in a Product Hunt launch. |
| [Product Hunt Launch-Day Operations / Product Hunt 发布日运营](skills/product-hunt-playbook/README.md) | Organize launch-day readiness, feedback response, operational checkpoints and post-launch review. |
| [Multi-Channel Launch-Day Runbook / 多渠道发布日手册](skills/startup-launch/README.md) | Coordinate channel sequence, owners, tracking and incident response for a product launch day. |
| [Early Startup Launch Planning / 早期创业发布规划](skills/startup-launch-playbook/README.md) | Plan MVP validation, initial traction and founder-led user acquisition within limited resources. |
| [Hardware and Subscription Go-to-Market / 硬件与订阅 GTM](skills/hardware-saas-gtm/README.md) | Plan the connection between device acquisition, software activation and subscription value for a hardware product. |
| [Jekyll Blog Publishing Workflow / Jekyll 博客发布工作流](skills/gr-blog-post/README.md) | Prepare a source-backed blog article with Jekyll metadata, deliberate canonical links and the requested localization. |
| [SEO/GEO Agent Migration Guide / SEO/GEO Agent 迁移说明](skills/gr-seo-geo-agent/README.md) | Direct users of the deprecated gr-seo-geo-agent name to the maintained gingiris-seo-geo-agent package. |

### Revenue and experiments / 收入与实验

| Workflow | Choose it for |
|---|---|
| [App Store Optimization Starter / ASO 入门工作流](skills/aso-playbook/README.md) | Review keywords, store copy, screenshots and ratings as a focused store-listing improvement plan. |
| [App Discovery and Cold-Start Execution / App 发现与冷启执行](skills/gr-aso/README.md) | Connect store optimization, localization and creator distribution in a bounded app cold-start plan. |
| [B2B Demand Generation Planning / B2B 需求获取规划](skills/b2b-marketing-playbook/README.md) | Build a buyer-specific marketing plan connecting LinkedIn content, outreach drafts and webinar follow-up to qualified demand. |
| [B2B Growth and First-Sale Diagnosis / B2B 增长与首单诊断](skills/gr-b2b-growth/README.md) | Diagnose buyer, pricing, delivery and activation constraints before choosing a product-led or sales-led motion. |
| [Product-Led Growth Measurement / PLG 测量与激活](skills/plg-playbook/README.md) | Evaluate self-serve onboarding, activation and pricing using a verified Web or CLI measurement path. |
| [SaaS Revenue and Retention Planning / SaaS 收入与留存规划](skills/saas-growth-playbook/README.md) | Choose a revenue-stage priority across willingness to pay, activation, pricing, churn and expansion. |
| [SaaS Marketing Stack and Channels / SaaS 营销工具与渠道](skills/saas-marketing-playbook/README.md) | Choose a manageable marketing stack and channel mix from the product’s stage, buyer journey and reporting needs. |
| [Startup Growth Diagnosis / 创业增长诊断](skills/startup-consultant/README.md) | Produce a decision-focused growth review with evidence gaps, alternatives and a feasible next action. |
| [Seed-Stage Channel Prioritization / 种子期渠道优先级](skills/startup-growth-playbook/README.md) | Prioritize the next growth channel using product readiness, team capacity and evidence of customer value. |
| [Low-Budget Startup Marketing / 低预算创业营销](skills/startup-marketing-playbook/README.md) | Build an organic marketing plan constrained by founder time, useful assets and audience access. |
| [Growth Experiment Design / 增长实验设计](skills/growth-hacking-playbook/README.md) | Turn a funnel bottleneck into a prioritized experiment with a metric, comparison window and stop rule. |
| [Referral and Sharing Loop Design / 推荐与分享循环设计](skills/viral-marketing-playbook/README.md) | Model a referral, invitation or sharing loop around a real moment of user value and observable conversions. |
