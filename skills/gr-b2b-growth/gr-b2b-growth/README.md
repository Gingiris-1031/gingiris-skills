---
license: mit
viewer: false
language:
- en
- zh
pretty_name: B2B Growth and First-Sale Diagnosis Skill
tags:
- agent-skills
- gingiris
- gr
- b2b
- growth
---

# B2B Growth and First-Sale Diagnosis / B2B 增长与首单诊断

Diagnose buyer, pricing, delivery and activation constraints before choosing a product-led or sales-led motion. `gr-b2b-growth` is an agent instruction package maintained by Gingiris. It guides planning and analysis in a compatible assistant; it is not a hosted service or a trained model.

用于**B2B 增长与首单诊断**。提供真实材料和当前约束，让助手按工作流形成可审阅的交付物；需要外部数据或账号操作时，仍取决于工具与权限。

## Quick start / 快速开始

For the CLI route, use Node.js/npm and an agent host with Skills support. Select your agent and install scope in the installer.

```bash
npx skills@1.7.4 add Gingiris-1031/gingiris-skills --skill gr-b2b-growth
```

Start with a concrete task:

```text
Use gr-b2b-growth. We get demos but no paid pilot. Separate buyer urgency, budget, proof and implementation constraints before proposing more traffic.
```

```text
请使用 gr-b2b-growth。有 demo 但没有付费试单，先区分买方优先级、预算、证据与实施约束，再决定是否加流量。
```

If the assistant cannot find the Skill, check the selected host and installation location, then open a new session. Installation does not grant analytics access or schedule work.

## Inputs and expected deliverables / 输入与交付

| Provide / 输入 | Ask for / 期望交付 |
|---|---|
| Buyer and use case / 买方场景; pipeline / 商机; price promise / 定价承诺; delivery cost / 交付成本 | First-sale diagnosis / 首单诊断; PLG/SLG choice / 模式选择; pricing acceptance / 定价验收; action plan / 行动 |

Use the supplied context first. Missing inputs should be called out rather than invented; an initial draft can state assumptions when the decision permits it. 先用已有上下文，不重复索取信息；关键缺口保留待确认。

## Example request and review / 如何判断结果可用

> **Illustrative output / 结构示意：** Demo completed → urgency unknown → decision-maker missing → next action: validate buyer ownership before scaling acquisition.

The starter task above should lead to **First-sale diagnosis / 首单诊断; PLG/SLG choice / 模式选择; pricing acceptance / 定价验收; action plan / 行动**. Review whether each proposed action has an owner or next step, evidence where needed and a clear limit. These are requested output formats, not pre-generated artifacts or proof of a customer outcome.

Example review question: **“Which supplied observation supports this recommendation, and what would change it?”**

示例验收问题：**“这条建议由哪项材料支持？什么新证据会让我们改变决定？”** 不以文档长度或完成模板证明业务成效。

## Scope: choosing this workflow / 选择与边界

Historical ARR examples are context. A plan must use your actual sales cycle and acceptance conditions.

| Next task | Where to go |
|---|---|
| Read the related scope before adding another workflow | [plg-playbook](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/plg-playbook) |
| Read the related scope before adding another workflow | [gr-opc-service-validation](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-opc-service-validation) |

## Method and included references / 方法与参考

[Read the maintained SKILL.md](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-b2b-growth/SKILL.md). It contains the operating sequence and any package-specific prerequisites. References are supporting material, not separate required purchases.

- [deal execution](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-b2b-growth/references/deal-execution.md)
- [first paid customer](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-b2b-growth/references/first-paid-customer.md)



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
