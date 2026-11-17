---
license: mit
viewer: false
language:
- en
- zh
tags:
- agent-skills
- marketing
- developer-community-playbook
- community-operations-skill
pretty_name: Developer and User Community Playbook
---

# Developer and User Community Playbook / 开发者与用户社区运营

Plan a community around member value, onboarding, events and observable participation. **`community-building-playbook`** is an installable Gingiris agent instruction workflow, not a hosted application or a trained model.

围绕成员价值、入群引导、活动与可观察参与，设计社区运营。这是可安装的 Agent 工作流，安装后在支持 Skills 的助手中调用。

## Quick start / 快速开始

Use an agent environment with Agent Skills support and Node.js/npm for this CLI route. Select the target agent in the installer; loading behavior depends on the host.

```bash
npx skills@1.7.4 add Gingiris-1031/gingiris-skills --skill community-building-playbook
```

Then ask your agent to use `community-building-playbook` with the following task. The example inputs are illustrative; replace them with your own material.

```text
Use community-building-playbook. Our developer group has many silent members. Plan one useful event and an onboarding change within four operator hours per week; define participation measures.
```

```text
请使用 community-building-playbook。开发者群里大多数人沉默。按每周四小时设计一场有用的活动和入群引导改动，定义参与指标。
```

安装后先确认助手能找到本 Skill，再用上面的示例提交真实材料。若无法发现，请检查安装器所选 Agent 和安装位置，再重新开启会话。

## When to use it / 适用场景

Teams deciding whether to start a community or improve an existing developer or user group.

围绕成员价值、入群引导、活动与可观察参与，设计社区运营。先提供下面的最少信息；已有上下文无需重复填写。

| Provide / 输入 | Receive / 输出 |
|---|---|
| Product stage, member tasks, existing communities, operator capacity, event resources and current metrics. | Readiness review; platform and onboarding plan; event brief; content rhythm; community health measures |
| 产品阶段、成员任务、已有社区、负责人时间、活动资源和当前指标 | 准备度检查；平台与入群方案；活动 Brief；内容节奏；健康度指标 |

## What a useful result looks like / 产出示意

> **Illustrative output structure, not a customer result:** Member task → useful session → participation action → follow-up help → return participation; member count alone is insufficient.

The deliverable should connect the supplied evidence to a decision or usable artifact. Missing source access, unverified claims and incomplete assets remain visible in the handoff. The example demonstrates structure; it does not claim a measured improvement.

以上是交付结构示意，不是客户业绩。输出应保留来源、未确认事实和下一步动作，方便你判断是否可用。

## Workflow and source material / 方法与材料

1. Supply the context above and name the decision or deliverable you need.
2. The agent follows [SKILL.md](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/community-building-playbook/SKILL.md), using the included references when relevant.
3. Review the artifact and evidence gaps before any external action. Live research, analytics or publishing may require additional tools and permissions.

- [templates](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/community-building-playbook/references/templates.md)
- [benchmarks](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/community-building-playbook/references/benchmarks.md)

## Scope and common questions / 范围与常见问题

**What are the limits?** Named brand cases are reference material. They do not establish the same resources, stage or results for a new community.

**Do I need paid tools?** Supplied material can support drafting and planning. Fresh web research, private analytics and account operations depend on the tools available in your agent environment; installation alone does not grant access.

**Does installation publish anything?** No. Instructions and templates do not create a publishing connection. External actions follow the task authorization and must be verified separately.

**需要准备什么？** 产品阶段、成员任务、已有社区、负责人时间、活动资源和当前指标。材料不足时保留假设和缺口，不补造数据。

**会交付什么？** 准备度检查；平台与入群方案；活动 Brief；内容节奏；健康度指标。具体范围以你的请求为准，不强制输出全部模板。

## Related workflows / 相关工作流

Choose by the next task, rather than installing every related package:

- [gingiris-ugc-matrix](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-ugc-matrix)
- [gr-user-interview](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-user-interview)
- [gr](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr)

## Maintenance, license and support / 维护、许可与支持

Maintained by Iris Wei / Gingiris. [Source and issue tracker](https://github.com/Gingiris-1031/gingiris-skills) · [Browse the Skills directory](https://tools.gingiris.com/skills/) · [MIT License](https://github.com/Gingiris-1031/gingiris-skills/blob/main/LICENSE).

Documentation reviewed: **2026-11-17**. This is a documentation update; workflow version is recorded in SKILL.md where available. No installation count, star count or historical case is a guarantee of your result.

<!-- gingiris-community-cta:start -->
### Optional community and resources / 可选社群与资料

Add **staywildgrow** on WeChat and send **“加入社群”** to join the growth community. A separate resource pack is available for **CNY 599**; neither is required to install or use the open-source Skill.

微信添加 **staywildgrow**，留言「**加入社群**」。也可咨询 **599 元资料包**；社群与资料包均为可选入口，不影响开源 Skill 使用。
<!-- gingiris-community-cta:end -->
