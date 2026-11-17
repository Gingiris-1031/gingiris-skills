---
license: mit
viewer: false
language:
- en
- zh
pretty_name: Technical SEO Audit and Monitoring Skill
tags:
- agent-skills
- gingiris
- gr
- seo
- patrol
---

# Technical SEO Audit and Monitoring / 技术 SEO 巡检

Inspect site health, search evidence and metadata issues, then separate verified findings from missing observations. `gr-seo-patrol` is an agent instruction package maintained by Gingiris. It guides planning and analysis in a compatible assistant; it is not a hosted service or a trained model.

用于**技术 SEO 巡检**。提供真实材料和当前约束，让助手按工作流形成可审阅的交付物；需要外部数据或账号操作时，仍取决于工具与权限。

## Quick start / 快速开始

For the CLI route, use Node.js/npm and an agent host with Skills support. Select your agent and install scope in the installer.

```bash
npx skills@1.7.4 add Gingiris-1031/gingiris-skills --skill gr-seo-patrol
```

Start with a concrete task:

```text
Use gr-seo-patrol. Investigate an organic-click drop. Compare equivalent windows, inspect affected URLs and distinguish indexing issues from missing data.
```

```text
请使用 gr-seo-patrol。调查自然点击下降，对比可比时间窗，检查受影响页面，区分索引问题与数据缺失。
```

If the assistant cannot find the Skill, check the selected host and installation location, then open a new session. Installation does not grant analytics access or schedule work.

## Inputs and expected deliverables / 输入与交付

| Provide / 输入 | Ask for / 期望交付 |
|---|---|
| Domain / 域名; affected URLs / 页面; comparison window / 时间窗; authorized GSC or analytics / 数据权限 | Audit findings / 巡检发现; source and time / 来源时间; repair priorities / 修复优先级; verification record / 验收 |

Use the supplied context first. Missing inputs should be called out rather than invented; an initial draft can state assumptions when the decision permits it. 先用已有上下文，不重复索取信息；关键缺口保留待确认。

## Example request and review / 如何判断结果可用

> **Illustrative output / 结构示意：** Affected URL → comparable GSC window → canonical/indexing evidence → confirmed issue or unknown → verification step.

The starter task above should lead to **Audit findings / 巡检发现; source and time / 来源时间; repair priorities / 修复优先级; verification record / 验收**. Review whether each proposed action has an owner or next step, evidence where needed and a clear limit. These are requested output formats, not pre-generated artifacts or proof of a customer outcome.

Example review question: **“Which supplied observation supports this recommendation, and what would change it?”**

示例验收问题：**“这条建议由哪项材料支持？什么新证据会让我们改变决定？”** 不以文档长度或完成模板证明业务成效。

## Scope: choosing this workflow / 选择与边界

Planning a patrol does not schedule it. API inspection, indexing requests, rankings and traffic are separate outcomes.

| Next task | Where to go |
|---|---|
| Read the related scope before adding another workflow | [gr-geo-cite](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-geo-cite) |
| Read the related scope before adding another workflow | [gingiris-seo-geo-agent](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-seo-geo-agent) |

## Method and included references / 方法与参考

[Read the maintained SKILL.md](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-seo-patrol/SKILL.md). It contains the operating sequence and any package-specific prerequisites. References are supporting material, not separate required purchases.





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
