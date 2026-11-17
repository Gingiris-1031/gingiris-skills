---
license: mit
viewer: false
language:
- en
- zh
tags:
- agent-skills
- content-operations
- content-marketing
- editorial-workflow
- social-media
- ai-content-operations-skill
- content-calendar-agent
pretty_name: AI Content Operations Skill
---

# AI Content Operations Skill / AI 内容运营

Turn audience questions and product evidence into researched topics, complete drafts and a feasible content calendar. **`gr-ai-content-ops`** is an installable Gingiris agent instruction workflow, not a hosted application or a trained model.

从受众真实问题与产品证据出发，形成有定位的选题、完整草稿和能执行的排期。这是可安装的 Agent 工作流，安装后在支持 Skills 的助手中调用。

## Quick start / 快速开始

Use an agent environment with Agent Skills support and Node.js/npm for this CLI route. Select the target agent in the installer; loading behavior depends on the host.

```bash
npx skills@1.7.4 add Gingiris-1031/gingiris-skills --skill gr-ai-content-ops
```

Then ask your agent to use `gr-ai-content-ops` with the following task. The example inputs are illustrative; replace them with your own material.

```text
Use gr-ai-content-ops. Our B2B product has two demos and six hours per week. Research an early-stage competitor, propose one useful blog and a native LinkedIn draft, and state what needs verification.
```

```text
请使用 gr-ai-content-ops。我们有两份产品演示，每周六小时。研究一个竞品的早期内容，给出一篇有用的博客方案和完整 LinkedIn 草稿，标注待验证事实。
```

安装后先确认助手能找到本 Skill，再用上面的示例提交真实材料。若无法发现，请检查安装器所选 Agent 和安装位置，再重新开启会话。

## When to use it / 适用场景

Small content teams deciding what to write, what to reuse and why recent content underperformed.

从受众真实问题与产品证据出发，形成有定位的选题、完整草稿和能执行的排期。先提供下面的最少信息；已有上下文无需重复填写。

| Provide / 输入 | Receive / 输出 |
|---|---|
| Product and competitor URLs, reader, desired action, source material and weekly capacity. | Audience and angle brief; SEO/GEO page intent; full drafts; visual briefs; calendar and review ledger |
| 产品网址、竞品网址、目标读者、期望行动、素材和每周工时 | 受众与角度简报；SEO/GEO 页面意图；完整草稿；配图说明；排期与复盘台账 |

## What a useful result looks like / 产出示意

> **Illustrative output structure, not a customer result:** Reader problem → supported angle → parent blog brief → LinkedIn explanation → visual asset task → review date.

The deliverable should connect the supplied evidence to a decision or usable artifact. Missing source access, unverified claims and incomplete assets remain visible in the handoff. The example demonstrates structure; it does not claim a measured improvement.

以上是交付结构示意，不是客户业绩。输出应保留来源、未确认事实和下一步动作，方便你判断是否可用。

## Workflow and source material / 方法与材料

1. Supply the context above and name the decision or deliverable you need.
2. The agent follows [SKILL.md](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-ai-content-ops/SKILL.md), using the included references when relevant.
3. Review the artifact and evidence gaps before any external action. Live research, analytics or publishing may require additional tools and permissions.

- [editorial](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-ai-content-ops/references/editorial.md)
- [search positioning](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-ai-content-ops/references/search-positioning.md)
- [templates](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-ai-content-ops/references/templates.md)
- [worked cases](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-ai-content-ops/references/worked-cases.md)

## Scope and common questions / 范围与常见问题

**What are the limits?** A calendar is a plan, not a scheduled job. Draft quality checks do not establish reader demand or business results.

**Do I need paid tools?** Supplied material can support drafting and planning. Fresh web research, private analytics and account operations depend on the tools available in your agent environment; installation alone does not grant access.

**Does installation publish anything?** No. Instructions and templates do not create a publishing connection. External actions follow the task authorization and must be verified separately.

**需要准备什么？** 产品网址、竞品网址、目标读者、期望行动、素材和每周工时。材料不足时保留假设和缺口，不补造数据。

**会交付什么？** 受众与角度简报；SEO/GEO 页面意图；完整草稿；配图说明；排期与复盘台账。具体范围以你的请求为准，不强制输出全部模板。

## Related workflows / 相关工作流

Choose by the next task, rather than installing every related package:

- [competitor-research-playbook](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/competitor-research-playbook)
- [gr-social-distill](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-social-distill)
- [gr-brand-voice-calibration](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-brand-voice-calibration)

## Maintenance, license and support / 维护、许可与支持

Maintained by Iris Wei / Gingiris. [Source and issue tracker](https://github.com/Gingiris-1031/gingiris-skills) · [Browse the Skills directory](https://tools.gingiris.com/skills/) · [MIT License](https://github.com/Gingiris-1031/gingiris-skills/blob/main/LICENSE).

Documentation reviewed: **2026-11-17**. This is a documentation update; workflow version is recorded in SKILL.md where available. No installation count, star count or historical case is a guarantee of your result.

Previous documentation: [version notes and historical context](https://github.com/Gingiris-1031/gingiris-skills/blob/main/skills/gr-ai-content-ops/references/readme-history.md). Historical claims are not current outcome guarantees.

<!-- gingiris-community-cta:start -->
### Optional community and resources / 可选社群与资料

Add **staywildgrow** on WeChat and send **“加入社群”** to join the growth community. A separate resource pack is available for **CNY 599**; neither is required to install or use the open-source Skill.

微信添加 **staywildgrow**，留言「**加入社群**」。也可咨询 **599 元资料包**；社群与资料包均为可选入口，不影响开源 Skill 使用。
<!-- gingiris-community-cta:end -->
