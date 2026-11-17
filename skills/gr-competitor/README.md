---
license: mit
viewer: false
language:
- en
- zh
tags:
- agent-skills
- marketing
- competitor-analysis-agent-skill
- early-customer-research
pretty_name: Competitor Analysis Skill
---

# Competitor Analysis Skill / 竞品分析执行入口

Run a focused competitor scan and connect the findings to customer hypotheses and a concrete next decision. **`gr-competitor`** is an installable Gingiris agent instruction workflow, not a hosted application or a trained model.

执行聚焦的竞品扫描，把发现交接为用户假设和下一步决策。这是可安装的 Agent 工作流，安装后在支持 Skills 的助手中调用。

## Quick start / 快速开始

Use an agent environment with Agent Skills support and Node.js/npm for this CLI route. Select the target agent in the installer; loading behavior depends on the host.

```bash
npx skills@1.7.4 add Gingiris-1031/gingiris-skills --skill gr-competitor
```

Then ask your agent to use `gr-competitor` with the following task. The example inputs are illustrative; replace them with your own material.

```text
Use gr-competitor. Investigate who appears to buy this competitor. Distinguish named case studies, free users and verified payment evidence, then suggest whom we should interview.
```

```text
请使用 gr-competitor。研究这个竞品的客户证据，区分案例客户、免费用户与有付款证据的买方，再建议我们该访谈谁。
```

安装后先确认助手能找到本 Skill，再用上面的示例提交真实材料。若无法发现，请检查安装器所选 Agent 和安装位置，再重新开启会话。

## When to use it / 适用场景

Operators who have a specific competitor question and want the research workflow with local references in one package.

执行聚焦的竞品扫描，把发现交接为用户假设和下一步决策。先提供下面的最少信息；已有上下文无需重复填写。

| Provide / 输入 | Receive / 输出 |
|---|---|
| Product and competitor URLs, user task, business model, decision and time limit. | Scope and selection rationale; dated sources; unknowns and counterevidence; experiment handoff |
| 产品与竞品网址、用户任务、商业模式、决策问题和时间上限 | 范围与选取理由；带日期来源；未知与反证；实验交接卡 |

## What a useful result looks like / 产出示意

> **Illustrative output structure, not a customer result:** Public logo → payment status unknown → dated case study → buyer-role hypothesis → interview screening question.

The deliverable should connect the supplied evidence to a decision or usable artifact. Missing source access, unverified claims and incomplete assets remain visible in the handoff. The example demonstrates structure; it does not claim a measured improvement.

以上是交付结构示意，不是客户业绩。输出应保留来源、未确认事实和下一步动作，方便你判断是否可用。

## Workflow and source material / 方法与材料

1. Supply the context above and name the decision or deliverable you need.
2. The agent follows [SKILL.md](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-competitor/SKILL.md), using the included references when relevant.
3. Review the artifact and evidence gaps before any external action. Live research, analytics or publishing may require additional tools and permissions.

- [early customer evidence](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-competitor/references/early-customer-evidence.md)
- [research workflow](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-competitor/references/research-workflow.md)

## Scope and common questions / 范围与常见问题

**What are the limits?** This is a compact entry to the maintained competitor method; it does not provide a separate dataset or hidden customer records.

**Do I need paid tools?** Supplied material can support drafting and planning. Fresh web research, private analytics and account operations depend on the tools available in your agent environment; installation alone does not grant access.

**Does installation publish anything?** No. Instructions and templates do not create a publishing connection. External actions follow the task authorization and must be verified separately.

**需要准备什么？** 产品与竞品网址、用户任务、商业模式、决策问题和时间上限。材料不足时保留假设和缺口，不补造数据。

**会交付什么？** 范围与选取理由；带日期来源；未知与反证；实验交接卡。具体范围以你的请求为准，不强制输出全部模板。

## Related workflows / 相关工作流

Choose by the next task, rather than installing every related package:

- [competitor-research-playbook](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/competitor-research-playbook)
- [gr-user-interview](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-user-interview)
- [gr-opc-service-validation](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-opc-service-validation)

## Maintenance, license and support / 维护、许可与支持

Maintained by Iris Wei / Gingiris. [Source and issue tracker](https://github.com/Gingiris-1031/gingiris-skills) · [Browse the Skills directory](https://tools.gingiris.com/skills/) · [MIT License](https://github.com/Gingiris-1031/gingiris-skills/blob/main/LICENSE).

Documentation reviewed: **2026-11-17**. This is a documentation update; workflow version is recorded in SKILL.md where available. No installation count, star count or historical case is a guarantee of your result.

<!-- gingiris-community-cta:start -->
### Optional community and resources / 可选社群与资料

Add **staywildgrow** on WeChat and send **“加入社群”** to join the growth community. A separate resource pack is available for **CNY 599**; neither is required to install or use the open-source Skill.

微信添加 **staywildgrow**，留言「**加入社群**」。也可咨询 **599 元资料包**；社群与资料包均为可选入口，不影响开源 Skill 使用。
<!-- gingiris-community-cta:end -->
