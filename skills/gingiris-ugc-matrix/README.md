---
license: mit
viewer: false
language:
- en
- zh
tags:
- agent-skills
- marketing
- ugc-creator-program
- creator-brief-skill
pretty_name: UGC Creator Program Skill
---

# UGC Creator Program Skill / UGC 创作者与素材实验

Design creator recruitment, briefs, usage rights and material experiments around a measurable business objective. **`gingiris-ugc-matrix`** is an installable Gingiris agent instruction workflow, not a hosted application or a trained model.

围绕可衡量目标设计创作者招募、Brief、授权与素材实验。这是可安装的 Agent 工作流，安装后在支持 Skills 的助手中调用。

## Quick start / 快速开始

Use an agent environment with Agent Skills support and Node.js/npm for this CLI route. Select the target agent in the installer; loading behavior depends on the host.

```bash
npx skills@1.7.4 add Gingiris-1031/gingiris-skills --skill gingiris-ugc-matrix
```

Then ask your agent to use `gingiris-ugc-matrix` with the following task. The example inputs are illustrative; replace them with your own material.

```text
Use gingiris-ugc-matrix. Create a brief for three product-demo creators within our budget. Define accurate demonstrations, usage rights, revisions and an activation metric.
```

```text
请使用 gingiris-ugc-matrix。在预算内给三位产品演示创作者写 Brief，明确真实演示、复用权、修改轮次和激活指标。
```

安装后先确认助手能找到本 Skill，再用上面的示例提交真实材料。若无法发现，请检查安装器所选 Agent 和安装位置，再重新开启会话。

## When to use it / 适用场景

Teams commissioning creator content and deciding which material to reuse, pay for or stop.

围绕可衡量目标设计创作者招募、Brief、授权与素材实验。先提供下面的最少信息；已有上下文无需重复填写。

| Provide / 输入 | Receive / 输出 |
|---|---|
| Product task, audience, region, budget, usage rights and organic or paid distribution. | Goal card; creator criteria; brief and acceptance rules; asset ledger; attribution and settlement plan |
| 产品任务、人群、地区、预算、素材授权、自然或付费分发方式 | 目标卡；筛选条件；Brief 与验收规则；素材台账；归因与结算方案 |

## What a useful result looks like / 产出示意

> **Illustrative output structure, not a customer result:** Asset A / audience / hook hypothesis / rights / cost / impressions / activation denominator / review decision.

The deliverable should connect the supplied evidence to a decision or usable artifact. Missing source access, unverified claims and incomplete assets remain visible in the handoff. The example demonstrates structure; it does not claim a measured improvement.

以上是交付结构示意，不是客户业绩。输出应保留来源、未确认事实和下一步动作，方便你判断是否可用。

## Workflow and source material / 方法与材料

1. Supply the context above and name the decision or deliverable you need.
2. The agent follows [SKILL.md](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-ugc-matrix/SKILL.md), using the included references when relevant.
3. Review the artifact and evidence gaps before any external action. Live research, analytics or publishing may require additional tools and permissions.

- [outcome and variants](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-ugc-matrix/references/outcome-and-variants.md)
- [full sop](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-ugc-matrix/references/full-sop.md)

## Scope and common questions / 范围与常见问题

**What are the limits?** Views, saves and payments are different outcomes. More saves without an exposure denominator do not prove a better save rate.

**Do I need paid tools?** Supplied material can support drafting and planning. Fresh web research, private analytics and account operations depend on the tools available in your agent environment; installation alone does not grant access.

**Does installation publish anything?** No. Instructions and templates do not create a publishing connection. External actions follow the task authorization and must be verified separately.

**需要准备什么？** 产品任务、人群、地区、预算、素材授权、自然或付费分发方式。材料不足时保留假设和缺口，不补造数据。

**会交付什么？** 目标卡；筛选条件；Brief 与验收规则；素材台账；归因与结算方案。具体范围以你的请求为准，不强制输出全部模板。

## Related workflows / 相关工作流

Choose by the next task, rather than installing every related package:

- [gr-ai-content-ops](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-ai-content-ops)
- [community-building-playbook](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/community-building-playbook)
- [gingiris-twitter-agent-ops](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-twitter-agent-ops)

## Maintenance, license and support / 维护、许可与支持

Maintained by Iris Wei / Gingiris. [Source and issue tracker](https://github.com/Gingiris-1031/gingiris-skills) · [Browse the Skills directory](https://tools.gingiris.com/skills/) · [MIT License](https://github.com/Gingiris-1031/gingiris-skills/blob/main/LICENSE).

Documentation reviewed: **2026-11-17**. This is a documentation update; workflow version is recorded in SKILL.md where available. No installation count, star count or historical case is a guarantee of your result.

<!-- gingiris-community-cta:start -->
### Optional community and resources / 可选社群与资料

Add **staywildgrow** on WeChat and send **“加入社群”** to join the growth community. A separate resource pack is available for **CNY 599**; neither is required to install or use the open-source Skill.

微信添加 **staywildgrow**，留言「**加入社群**」。也可咨询 **599 元资料包**；社群与资料包均为可选入口，不影响开源 Skill 使用。
<!-- gingiris-community-cta:end -->
