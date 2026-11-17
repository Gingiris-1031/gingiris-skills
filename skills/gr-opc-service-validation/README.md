---
license: mit
viewer: false
language:
- en
- zh
tags:
- agent-skills
- marketing
- solo-service-validation
- paid-pilot-design
pretty_name: Solo Service Validation Skill
---

# Solo Service Validation Skill / OPC 服务与试单验证

Test one expertise-based service with a bounded pilot, explicit acceptance criteria and a sustainable delivery budget. **`gr-opc-service-validation`** is an installable Gingiris agent instruction workflow, not a hosted application or a trained model.

用有边界的样例或付费试单，验证服务需求、验收方式和可持续交付能力。这是可安装的 Agent 工作流，安装后在支持 Skills 的助手中调用。

## Quick start / 快速开始

Use an agent environment with Agent Skills support and Node.js/npm for this CLI route. Select the target agent in the installer; loading behavior depends on the host.

```bash
npx skills@1.7.4 add Gingiris-1031/gingiris-skills --skill gr-opc-service-validation
```

Then ask your agent to use `gr-opc-service-validation` with the following task. The example inputs are illustrative; replace them with your own material.

```text
Use gr-opc-service-validation. Design a paid pilot for a two-week onboarding audit. I can spend eight hours. Define buyer fit, required inputs, deliverables, exclusions and acceptance.
```

```text
请使用 gr-opc-service-validation。设计一个两周的 onboarding 审计试单，我能投入八小时。明确买方适配、客户输入、交付物、排除项和验收。
```

安装后先确认助手能找到本 Skill，再用上面的示例提交真实材料。若无法发现，请检查安装器所选 Agent 和安装位置，再重新开启会话。

## When to use it / 适用场景

Independent operators turning experience into a service and deciding whether to continue, change or stop an offer.

用有边界的样例或付费试单，验证服务需求、验收方式和可持续交付能力。先提供下面的最少信息；已有上下文无需重复填写。

| Provide / 输入 | Receive / 输出 |
|---|---|
| Evidence of ability, target buyer, offer scope, available hours, costs and customer feedback. | Offer definition; client-fit checklist; pilot card; capacity and pricing assumptions; continue/change/stop decision |
| 能力证据、目标买方、交付范围、可投入工时、成本和已有客户反馈 | 服务定义；客户适配清单；试单卡；容量与定价假设；继续/修改/停止决定 |

## What a useful result looks like / 产出示意

> **Illustrative output structure, not a customer result:** Buyer owns onboarding → access to funnel evidence → capped audit scope → accepted findings → separate evidence of repeat demand.

The deliverable should connect the supplied evidence to a decision or usable artifact. Missing source access, unverified claims and incomplete assets remain visible in the handoff. The example demonstrates structure; it does not claim a measured improvement.

以上是交付结构示意，不是客户业绩。输出应保留来源、未确认事实和下一步动作，方便你判断是否可用。

## Workflow and source material / 方法与材料

1. Supply the context above and name the decision or deliverable you need.
2. The agent follows [SKILL.md](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-opc-service-validation/SKILL.md), using the included references when relevant.
3. Review the artifact and evidence gaps before any external action. Live research, analytics or publishing may require additional tools and permissions.

- [pilot](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-opc-service-validation/references/pilot.md)
- [review](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-opc-service-validation/references/review.md)

## Scope and common questions / 范围与常见问题

**What are the limits?** A demonstration is not an accepted client case. Pricing assumptions and interest do not prove payment or repeat demand.

**Do I need paid tools?** Supplied material can support drafting and planning. Fresh web research, private analytics and account operations depend on the tools available in your agent environment; installation alone does not grant access.

**Does installation publish anything?** No. Instructions and templates do not create a publishing connection. External actions follow the task authorization and must be verified separately.

**需要准备什么？** 能力证据、目标买方、交付范围、可投入工时、成本和已有客户反馈。材料不足时保留假设和缺口，不补造数据。

**会交付什么？** 服务定义；客户适配清单；试单卡；容量与定价假设；继续/修改/停止决定。具体范围以你的请求为准，不强制输出全部模板。

## Related workflows / 相关工作流

Choose by the next task, rather than installing every related package:

- [gr-user-interview](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-user-interview)
- [competitor-research-playbook](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/competitor-research-playbook)
- [gr](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr)

## Maintenance, license and support / 维护、许可与支持

Maintained by Iris Wei / Gingiris. [Source and issue tracker](https://github.com/Gingiris-1031/gingiris-skills) · [Browse the Skills directory](https://tools.gingiris.com/skills/) · [MIT License](https://github.com/Gingiris-1031/gingiris-skills/blob/main/LICENSE).

Documentation reviewed: **2026-11-17**. This is a documentation update; workflow version is recorded in SKILL.md where available. No installation count, star count or historical case is a guarantee of your result.

<!-- gingiris-community-cta:start -->
### Optional community and resources / 可选社群与资料

Add **staywildgrow** on WeChat and send **“加入社群”** to join the growth community. A separate resource pack is available for **CNY 599**; neither is required to install or use the open-source Skill.

微信添加 **staywildgrow**，留言「**加入社群**」。也可咨询 **599 元资料包**；社群与资料包均为可选入口，不影响开源 Skill 使用。
<!-- gingiris-community-cta:end -->
