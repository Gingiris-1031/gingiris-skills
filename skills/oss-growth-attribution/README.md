---
license: mit
viewer: false
language:
- en
- zh
tags:
- agent-skills
- marketing
- open-source-growth-attribution
- github-star-research
pretty_name: Open-Source Growth Attribution Skill
---

# Open-Source Growth Attribution Skill / 开源增长渠道归因

Reconstruct a repository’s growth timeline and representative content from public evidence, with explicit attribution limits. **`oss-growth-attribution`** is an installable Gingiris agent instruction workflow, not a hosted application or a trained model.

用公开证据还原仓库增长阶段与代表内容，并明确渠道归因的限度。这是可安装的 Agent 工作流，安装后在支持 Skills 的助手中调用。

## Quick start / 快速开始

Use an agent environment with Agent Skills support and Node.js/npm for this CLI route. Select the target agent in the installer; loading behavior depends on the host.

```bash
npx skills@1.7.4 add Gingiris-1031/gingiris-skills --skill oss-growth-attribution
```

Then ask your agent to use `oss-growth-attribution` with the following task. The example inputs are illustrative; replace them with your own material.

```text
Use oss-growth-attribution. Reconstruct this repo’s first three months. Align star spikes with original launch posts, label inference and list channels you searched without finding evidence.
```

```text
请使用 oss-growth-attribution。还原这个仓库前三个月，把 Star 峰值与原始发布内容对齐，标明推断，并列出查过但没找到证据的渠道。
```

安装后先确认助手能找到本 Skill，再用上面的示例提交真实材料。若无法发现，请检查安装器所选 Agent 和安装位置，再重新开启会话。

## When to use it / 适用场景

Teams studying which launch, community or content activities plausibly contributed to an OSS project’s growth.

用公开证据还原仓库增长阶段与代表内容，并明确渠道归因的限度。先提供下面的最少信息；已有上下文无需重复填写。

| Provide / 输入 | Receive / 输出 |
|---|---|
| Repository and product URLs, analysis window, channels of interest and any first-party traffic records. | Stage timeline; original content links; evidence grades; modeled ranges; next-stage research and measurement plan |
| 仓库与产品网址、分析窗口、关注渠道和可用的一方流量记录 | 阶段时间线；原始内容链接；证据等级；估算区间；下一阶段研究与测量计划 |

## What a useful result looks like / 产出示意

> **Illustrative output structure, not a customer result:** Observed: dated post and star spike → inferred: possible amplification → unknown: attributable installs without referral logs.

The deliverable should connect the supplied evidence to a decision or usable artifact. Missing source access, unverified claims and incomplete assets remain visible in the handoff. The example demonstrates structure; it does not claim a measured improvement.

以上是交付结构示意，不是客户业绩。输出应保留来源、未确认事实和下一步动作，方便你判断是否可用。

## Workflow and source material / 方法与材料

1. Supply the context above and name the decision or deliverable you need.
2. The agent follows [SKILL.md](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/oss-growth-attribution/SKILL.md), using the included references when relevant.
3. Review the artifact and evidence gaps before any external action. Live research, analytics or publishing may require additional tools and permissions.

- [evidence schema](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/oss-growth-attribution/references/evidence-schema.md)
- [api playbook](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/oss-growth-attribution/references/api-playbook.md)
- [attribution model](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/oss-growth-attribution/references/attribution-model.md)

## Scope and common questions / 范围与常见问题

**What are the limits?** Temporal correlation is not exact causal attribution. Public absence does not prove that a channel was unused.

**Do I need paid tools?** Supplied material can support drafting and planning. Fresh web research, private analytics and account operations depend on the tools available in your agent environment; installation alone does not grant access.

**Does installation publish anything?** No. Instructions and templates do not create a publishing connection. External actions follow the task authorization and must be verified separately.

**需要准备什么？** 仓库与产品网址、分析窗口、关注渠道和可用的一方流量记录。材料不足时保留假设和缺口，不补造数据。

**会交付什么？** 阶段时间线；原始内容链接；证据等级；估算区间；下一阶段研究与测量计划。具体范围以你的请求为准，不强制输出全部模板。

## Related workflows / 相关工作流

Choose by the next task, rather than installing every related package:

- [competitor-research-playbook](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/competitor-research-playbook)
- [gr-readme](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-readme)
- [gr](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr)

## Maintenance, license and support / 维护、许可与支持

Maintained by Iris Wei / Gingiris. [Source and issue tracker](https://github.com/Gingiris-1031/gingiris-skills) · [Browse the Skills directory](https://tools.gingiris.com/skills/) · [MIT License](https://github.com/Gingiris-1031/gingiris-skills/blob/main/LICENSE).

Documentation reviewed: **2026-11-17**. This is a documentation update; workflow version is recorded in SKILL.md where available. No installation count, star count or historical case is a guarantee of your result.

<!-- gingiris-community-cta:start -->
### Optional community and resources / 可选社群与资料

Add **staywildgrow** on WeChat and send **“加入社群”** to join the growth community. A separate resource pack is available for **CNY 599**; neither is required to install or use the open-source Skill.

微信添加 **staywildgrow**，留言「**加入社群**」。也可咨询 **599 元资料包**；社群与资料包均为可选入口，不影响开源 Skill 使用。
<!-- gingiris-community-cta:end -->
