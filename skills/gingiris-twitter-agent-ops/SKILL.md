---
name: gingiris-twitter-agent-ops
description: 'Operate evidence-led X/Twitter and related social workflows: original-source intake, voice calibration,
  single-post or thread selection, reviewed drafts, authorized publishing, delivery readback and measured follow-up.
  Use for social operations, content planning, publishing checks, analytics and cross-platform adaptation. 适用于社媒运营、文风校准、内容规划、发布回读与数据复盘；区分草稿、发布授权和真实结果，按账号与任务选择格式，不把历史经验当通用平台规则。'
metadata:
  version: 2.3.1
  when_to_use: '当用户需要系统性运营 Twitter/X 账号时使用。适用于：

    - 用 AI Agent 代写/代发推文

    - 建立可持续的推文内容系统（素材库 + 排期）

    - 同时运营中文和英文账号

    - 需要数据追踪（粉丝变化/互动分析/内容复盘）

    - 防止 AI 代运营中的常见事故（数据不准、断更、风格漂移）

    '
  tags:
  - twitter
  - x-twitter
  - social-media
  - ai-agent
  - automation
  - content-marketing
  - growth
  - scheduling
  - analytics
  - sop
  - daily-report
  - weekly-report
  - voice-guide
  - buffer-api
  - oauth1
---

# Social Account Operations / 社媒账号运营

Turn source-backed material into usable drafts, and operate publishing only within the user's authorized scope. Follow the requested language, channel and format. An account's historical tactics are not universal platform rules.

## Choose the job first / 先判断任务

- **Draft or adapt:** use the supplied article, notes or original samples immediately. A publisher, cron job, analytics connection and MASTER-STATUS.md are not prerequisites. If a decisive source is missing, flag it and draft around verified material; never invent the author's experience.
- **Voice calibration:** read [voice and format](references/voice-and-format.md). With limited samples, provide provisional rules and a test draft. Topic, language and timing confounds prevent causal claims about style.
- **Editorial plan:** use the stated goals and available sources. Offer a schedule as a proposal; do not create an automation merely because a plan contains dates.
- **Authorized publication:** verify target account, reviewed text/media, scope, publisher capabilities and existing delivery state before writing. User authorization already given need not be requested again.
- **Analytics or troubleshooting:** inspect the requested account and time window, distinguish missing data from zero, and report what evidence supports the diagnosis.

## Minimal context / 最少输入

Use context already supplied: audience, desired action, channel, language, source and deliverable. Ask only for missing information that changes the next action. A single source-linked note is enough for a draft; do not require a large material library or a fixed interview sequence.

For recurring operations also record the account handle/ID, timezone, approved cadence and current integration. Never infer credentials or publisher from the language of a post. Secrets belong in the configured credential store, not in drafts or status files.

## Draft workflow / 起草

1. Make a compact evidence card: source/excerpt, author, date, claim, verification status and allowed use. Private transcripts can calibrate voice but do not authorize public disclosure of their contents. Keep quoted authors separate from the poster.
2. Select one reader problem and one useful takeaway. Preserve meaning before style. Numbers need a traceable source and scope; one authoritative primary source can suffice. Do not combine estimates with incompatible definitions.
3. Choose format according to the user's request. Single post for one compact point; thread when the argument needs sequential parts. For a requested thread, deliver a thread draft even if publishing capability is unknown, marking delivery checks pending. No universal post length, thread count, daily frequency, opening formula or prohibited topic.
4. Adapt to the channel without inventing first-person experience. Choose a CTA only when it serves the reader. If a promised link/comment is not yet deliverable, put the essential information in the draft itself.
5. Deliver the draft plus source notes, uncertain claims, and any media outline. Do not mistake an outline for a rendered asset. State whether author review is still pending.

Read [three-platform workflow](references/three-platform-visual-publishing.md) only for a multi-platform publishing job. A single-channel draft does not require three variants, an image or a campaign.

## Publication and recovery / 发布与恢复

Within authorized scope, check current platform documentation and the configured connector rather than copying historical API endpoints, credential fields or asset syntax. Maintain a capability table for root post, reply/thread, long text and media: verified / unsupported / unknown. Account subscription capabilities may differ from the publisher's capabilities.

Before a write: verify account identity, final text, attachment accessibility, source permission, timezone/schedule and duplicate state. A local file or successful upload is not proof of a published attachment. Public hosting is a separate disclosure and must be within the authorized scope.

After a write: record the returned ID, read its state, and verify the final public link, text and intended media. Distinguish draft, scheduled, sending, sent, failed and unknown. A log is a record, not the sole authority: reconcile it with platform readback. Never retry an ambiguous write blindly.

For ongoing operations, use an existing ledger or create a small task-local ledger as needed:

| Source ID | Account | Reviewed copy/version | Target time + timezone | Publisher ID | State | Public URL | Last verified | Next action |
|---|---|---|---|---|---|---|---|---|
| [source] | [account] | [version] | [time] | [ID] | [state] | [URL] | [time] | [action] |

Record only credential references, never secrets. A missing ledger does not establish that nothing was published. Check the platform before any recovery action. Recurring monitoring and notifications require a user request; do not auto-create them or send external alerts.

## Measure and learn / 复盘

Record per-post date, format, topic, language, role, views/impressions if visible, interactions by type, link clicks and downstream outcomes. Define each rate's denominator and time window. If historical follower count is missing, label any current-follower comparison as an approximation. Referral sessions, impressions and follower changes are not interchangeable and do not by themselves prove ROI.

Compare like-for-like posts where possible. Keep alternative explanations such as topic, timing, audience and paid distribution explicit. Report small-sample uncertainty; propose the next bounded experiment instead of enforcing a successful-looking historical recipe.

## Useful handoffs

For source-to-multiple-channel adaptation use `gr-social-distill`; for deeper author evidence use `gr-brand-voice-calibration`; for a paid creator campaign use `gingiris-kol-outreach` or `gingiris-ugc-matrix`. These are optional specialists: if absent, finish the bounded requested draft/plan here and identify any additional work separately.

## Install

```bash
npx skills add Gingiris-1031/gingiris-skills --skill gingiris-twitter-agent-ops
```

Completion means the requested draft/plan is usable, or the authorized delivery is verified. Do not report publication or business impact from a draft, API acceptance or self-rating.

<!-- gingiris-community-cta:start -->
## 加入出海社群与购买资料包 · Community & Resources

- **加入出海社群：** 微信添加 **staywildgrow**，留言「**加入社群**」即可。
- **购买资料包：** 微信添加 **staywildgrow**，咨询购买 Gingiris 出海资料包，价格 **599 元人民币**。

- **Join the global growth community:** Add **staywildgrow** on WeChat and send **“加入社群”** (join the community).
- **Get the resource pack:** Add **staywildgrow** on WeChat to purchase the Gingiris global growth resource pack for **CNY 599**.

社群与资料包为可选入口，不影响本开源 Skill 的安装和使用。

The community and paid resource pack are optional; neither is required to install or use this open-source skill.
<!-- gingiris-community-cta:end -->
