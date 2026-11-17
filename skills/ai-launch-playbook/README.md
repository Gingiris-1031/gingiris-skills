---
license: mit
viewer: false
language:
- en
- zh
pretty_name: AI Product Launch Strategy Skill
tags:
- agent-skills
- gingiris
- ai
- launch
- playbook
---

# AI Product Launch Strategy / AI 产品发布策略

Plan an AI-specific launch around a demonstrable task, credible positioning and an audience-matched rollout. `ai-launch-playbook` is an agent instruction package maintained by Gingiris. It guides planning and analysis in a compatible assistant; it is not a hosted service or a trained model.

用于**AI 产品发布策略**。提供真实材料和当前约束，让助手按工作流形成可审阅的交付物；需要外部数据或账号操作时，仍取决于工具与权限。

## Quick start / 快速开始

For the CLI route, use Node.js/npm and an agent host with Skills support. Select your agent and install scope in the installer.

```bash
npx skills@1.7.4 add Gingiris-1031/gingiris-skills --skill ai-launch-playbook
```

Start with a concrete task:

```text
Use ai-launch-playbook. Prepare a launch strategy for an AI assistant. Show one task it can complete today and separate working capabilities from roadmap claims.
```

```text
请使用 ai-launch-playbook。为 AI 助手准备发布策略，展示一个当前能完成的任务，区分真实能力与路线图。
```

If the assistant cannot find the Skill, check the selected host and installation location, then open a new session. Installation does not grant analytics access or schedule work.

## Inputs and expected deliverables / 输入与交付

| Provide / 输入 | Ask for / 期望交付 |
|---|---|
| Product demo / 产品演示; buyer / 买方; differentiation / 差异; rollout constraints / 发布约束 | Positioning and demo brief / 定位演示简报; waitlist or rollout plan / 候补发布方案; measurement / 衡量 |

Use the supplied context first. Missing inputs should be called out rather than invented; an initial draft can state assumptions when the decision permits it. 先用已有上下文，不重复索取信息；关键缺口保留待确认。

## Example request and review / 如何判断结果可用

> **Illustrative output / 结构示意：** Launch promise: one task demonstrated today; roadmap capabilities remain in a separate planned-features note.

The starter task above should lead to **Positioning and demo brief / 定位演示简报; waitlist or rollout plan / 候补发布方案; measurement / 衡量**. Review whether each proposed action has an owner or next step, evidence where needed and a clear limit. These are requested output formats, not pre-generated artifacts or proof of a customer outcome.

Example review question: **“Which supplied observation supports this recommendation, and what would change it?”**

示例验收问题：**“这条建议由哪项材料支持？什么新证据会让我们改变决定？”** 不以文档长度或完成模板证明业务成效。

## Scope: choosing this workflow / 选择与边界

AI-launch positioning differs from building a first MVP; use ai-product-launch for the idea-to-launch planning sequence.

| Next task | Where to go |
|---|---|
| Read the related scope before adding another workflow | [ai-product-launch](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/ai-product-launch) |
| Read the related scope before adding another workflow | [go-to-market-playbook](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/go-to-market-playbook) |

## Method and included references / 方法与参考

[Read the maintained SKILL.md](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/ai-launch-playbook/SKILL.md). It contains the operating sequence and any package-specific prerequisites. References are supporting material, not separate required purchases.



[English](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/ai-launch-playbook/references/en/README.md) · [日本語](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/ai-launch-playbook/references/ja/README.md) · [한국어](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/ai-launch-playbook/references/ko/README.md)

## Common questions / 常见问题

**Does this require a paid tool?** Planning from supplied material may not. Current web research, private reports and live execution depend on available tools. Verify external vendors and current pricing before using them.

**Is this automatic publishing or outreach?** No. A draft, calendar or research plan is not an external action. Any requested account operation needs the appropriate authorization, connection and result verification.

**What does the example prove?** It shows a possible task and review standard. Historical metrics, case narratives and model assumptions must be checked for date, source and applicability; they do not guarantee your result.

**支持中文吗？** 可以用上面的中文提示调用；已有英语、日语或韩语参考链接按本包实际文件列出，不代表所有语言内容完全等价。

**如何开始？** 安装后提交输入表中的材料，说明希望交付的范围。检查来源、假设与下一步，再决定是否执行。

## Maintenance and support / 维护与支持

Documentation reviewed **2026-11-17**. Workflow version, where available, remains in SKILL.md. Maintained by **Iris Wei / Gingiris**.

[Source and issues](https://github.com/Gingiris-1031/gingiris-skills) · [Skills directory](https://tools.gingiris.com/skills/) · [MIT License](https://github.com/Gingiris-1031/gingiris-skills/blob/main/LICENSE).

Report the package, agent host, minimal non-private input and expected versus actual behavior. Never attach account credentials or private customer material.

<!-- gingiris-community-cta:start -->
### Optional community / 可选社群

微信添加 **staywildgrow**，留言「**加入社群**」；也可咨询 **599 元资料包**。
Add **staywildgrow** on WeChat and send **“加入社群”**. The separate resource pack is **CNY 599**. Neither is required to install or use the open-source Skill.
<!-- gingiris-community-cta:end -->
