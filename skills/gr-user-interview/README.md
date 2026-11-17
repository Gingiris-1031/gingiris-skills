---
license: mit
viewer: false
language:
- en
- zh
tags:
- agent-skills
- marketing
- user-interview-skill
- customer-discovery-workflow
pretty_name: User Interview Execution Skill
---

# User Interview Execution Skill / 用户访谈与需求验收

Turn interview observations into testable requirements, priorities and a follow-up check. **`gr-user-interview`** is an installable Gingiris agent instruction workflow, not a hosted application or a trained model.

将访谈中的原始观察转为可验证需求、优先级与回访验收。这是可安装的 Agent 工作流，安装后在支持 Skills 的助手中调用。

## Quick start / 快速开始

Use an agent environment with Agent Skills support and Node.js/npm for this CLI route. Select the target agent in the installer; loading behavior depends on the host.

```bash
npx skills@1.7.4 add Gingiris-1031/gingiris-skills --skill gr-user-interview
```

Then ask your agent to use `gr-user-interview` with the following task. The example inputs are illustrative; replace them with your own material.

```text
Use gr-user-interview. Review these five interviews. Separate observed workarounds from feature requests and define one change we can validate in a follow-up session.
```

```text
请使用 gr-user-interview。复盘这五次访谈，把实际替代流程与功能建议分开，定义一个可在回访中验收的改动。
```

安装后先确认助手能找到本 Skill，再用上面的示例提交真实材料。若无法发现，请检查安装器所选 Agent 和安装位置，再重新开启会话。

## When to use it / 适用场景

Product teams with scattered feedback, low-signal interviews or uncertainty about what to build next.

将访谈中的原始观察转为可验证需求、优先级与回访验收。先提供下面的最少信息；已有上下文无需重复填写。

| Provide / 输入 | Receive / 输出 |
|---|---|
| Current decision, intended sample, original notes, real user task and follow-up conditions. | Screening and interview plan; evidence synthesis; requirement and acceptance card; follow-up plan |
| 当前决策、目标样本、原始记录、真实任务和后续验证条件 | 样本筛选与提纲；证据合成；需求与验收卡；回访计划 |

## What a useful result looks like / 产出示意

> **Illustrative output structure, not a customer result:** Observation: user exports a table to finish a task → candidate requirement → prototype task → observable completion criterion.

The deliverable should connect the supplied evidence to a decision or usable artifact. Missing source access, unverified claims and incomplete assets remain visible in the handoff. The example demonstrates structure; it does not claim a measured improvement.

以上是交付结构示意，不是客户业绩。输出应保留来源、未确认事实和下一步动作，方便你判断是否可用。

## Workflow and source material / 方法与材料

1. Supply the context above and name the decision or deliverable you need.
2. The agent follows [SKILL.md](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-user-interview/SKILL.md), using the included references when relevant.
3. Review the artifact and evidence gaps before any external action. Live research, analytics or publishing may require additional tools and permissions.

- [cold start decision card](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-user-interview/references/cold-start-decision-card.md)
- [templates](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-user-interview/references/templates.md)
- [research to acceptance](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-user-interview/references/research-to-acceptance.md)
- [interview recovery](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-user-interview/references/interview-recovery.md)

## Scope and common questions / 范围与常见问题

**What are the limits?** Interview counts and positive feedback do not establish PMF. Recruitment and outreach require appropriate authorization.

**Do I need paid tools?** Supplied material can support drafting and planning. Fresh web research, private analytics and account operations depend on the tools available in your agent environment; installation alone does not grant access.

**Does installation publish anything?** No. Instructions and templates do not create a publishing connection. External actions follow the task authorization and must be verified separately.

**需要准备什么？** 当前决策、目标样本、原始记录、真实任务和后续验证条件。材料不足时保留假设和缺口，不补造数据。

**会交付什么？** 样本筛选与提纲；证据合成；需求与验收卡；回访计划。具体范围以你的请求为准，不强制输出全部模板。

## Related workflows / 相关工作流

Choose by the next task, rather than installing every related package:

- [gingiris-user-interview](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-user-interview)
- [gr-competitor](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-competitor)
- [gr-opc-service-validation](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-opc-service-validation)

## Maintenance, license and support / 维护、许可与支持

Maintained by Iris Wei / Gingiris. [Source and issue tracker](https://github.com/Gingiris-1031/gingiris-skills) · [Browse the Skills directory](https://tools.gingiris.com/skills/) · [MIT License](https://github.com/Gingiris-1031/gingiris-skills/blob/main/LICENSE).

Documentation reviewed: **2026-11-17**. This is a documentation update; workflow version is recorded in SKILL.md where available. No installation count, star count or historical case is a guarantee of your result.

<!-- gingiris-community-cta:start -->
### Optional community and resources / 可选社群与资料

Add **staywildgrow** on WeChat and send **“加入社群”** to join the growth community. A separate resource pack is available for **CNY 599**; neither is required to install or use the open-source Skill.

微信添加 **staywildgrow**，留言「**加入社群**」。也可咨询 **599 元资料包**；社群与资料包均为可选入口，不影响开源 Skill 使用。
<!-- gingiris-community-cta:end -->
