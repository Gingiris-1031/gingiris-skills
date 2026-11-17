---
license: mit
viewer: false
language:
- en
- zh
tags:
- agent-skills
- marketing
- x-twitter-operations-skill
- social-publishing-workflow
pretty_name: X and Social Account Operations Skill
---

# X and Social Account Operations Skill / X 与社媒账号运营

Manage source-backed drafts, authorized publishing checks and measured follow-up for a social account. **`gingiris-twitter-agent-ops`** is an installable Gingiris agent instruction workflow, not a hosted application or a trained model.

连接有来源的草稿、获授权发布检查与账号数据复盘。这是可安装的 Agent 工作流，安装后在支持 Skills 的助手中调用。

## Quick start / 快速开始

Use an agent environment with Agent Skills support and Node.js/npm for this CLI route. Select the target agent in the installer; loading behavior depends on the host.

```bash
npx skills@1.7.4 add Gingiris-1031/gingiris-skills --skill gingiris-twitter-agent-ops
```

Then ask your agent to use `gingiris-twitter-agent-ops` with the following task. The example inputs are illustrative; replace them with your own material.

```text
Use gingiris-twitter-agent-ops. Prepare one X post from my original note and check its factual claims. If publication is authorized, verify the target account and read back the result.
```

```text
请使用 gingiris-twitter-agent-ops。用我的原始笔记准备一条 X 帖子并核对事实；如本次已授权发布，先核对账号，发布后回读。
```

安装后先确认助手能找到本 Skill，再用上面的示例提交真实材料。若无法发现，请检查安装器所选 Agent 和安装位置，再重新开启会话。

## When to use it / 适用场景

Account owners who need a repeatable workflow with voice consistency and clear delivery status.

连接有来源的草稿、获授权发布检查与账号数据复盘。先提供下面的最少信息；已有上下文无需重复填写。

| Provide / 输入 | Receive / 输出 |
|---|---|
| Target account, source material, language, format, authorization scope and analysis window. | Reviewed draft; media readiness checklist; publication receipt when authorized; measurement and recovery notes |
| 目标账号、素材、语言、格式、授权范围和需要分析的时间窗 | 审阅草稿；媒体就绪检查；获授权时的发布回执；复盘与异常恢复记录 |

## What a useful result looks like / 产出示意

> **Illustrative output structure, not a customer result:** Draft ready → media ready → account confirmed → submission receipt → public readback; failed or unknown delivery stays unresolved.

The deliverable should connect the supplied evidence to a decision or usable artifact. Missing source access, unverified claims and incomplete assets remain visible in the handoff. The example demonstrates structure; it does not claim a measured improvement.

以上是交付结构示意，不是客户业绩。输出应保留来源、未确认事实和下一步动作，方便你判断是否可用。

## Workflow and source material / 方法与材料

1. Supply the context above and name the decision or deliverable you need.
2. The agent follows [SKILL.md](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-twitter-agent-ops/SKILL.md), using the included references when relevant.
3. Review the artifact and evidence gaps before any external action. Live research, analytics or publishing may require additional tools and permissions.

- [three platform visual publishing](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-twitter-agent-ops/references/three-platform-visual-publishing.md)
- [voice and format](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-twitter-agent-ops/references/voice-and-format.md)

## Scope and common questions / 范围与常见问题

**What are the limits?** A draft does not require analytics credentials. A proposed schedule does not create automation; live posting needs platform access.

**Do I need paid tools?** Supplied material can support drafting and planning. Fresh web research, private analytics and account operations depend on the tools available in your agent environment; installation alone does not grant access.

**Does installation publish anything?** No. Instructions and templates do not create a publishing connection. External actions follow the task authorization and must be verified separately.

**需要准备什么？** 目标账号、素材、语言、格式、授权范围和需要分析的时间窗。材料不足时保留假设和缺口，不补造数据。

**会交付什么？** 审阅草稿；媒体就绪检查；获授权时的发布回执；复盘与异常恢复记录。具体范围以你的请求为准，不强制输出全部模板。

## Related workflows / 相关工作流

Choose by the next task, rather than installing every related package:

- [gr-social-distill](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-social-distill)
- [gr-brand-voice-calibration](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-brand-voice-calibration)
- [gr-ai-content-ops](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-ai-content-ops)

## Maintenance, license and support / 维护、许可与支持

Maintained by Iris Wei / Gingiris. [Source and issue tracker](https://github.com/Gingiris-1031/gingiris-skills) · [Browse the Skills directory](https://tools.gingiris.com/skills/) · [MIT License](https://github.com/Gingiris-1031/gingiris-skills/blob/main/LICENSE).

Documentation reviewed: **2026-11-17**. This is a documentation update; workflow version is recorded in SKILL.md where available. No installation count, star count or historical case is a guarantee of your result.

<!-- gingiris-community-cta:start -->
### Optional community and resources / 可选社群与资料

Add **staywildgrow** on WeChat and send **“加入社群”** to join the growth community. A separate resource pack is available for **CNY 599**; neither is required to install or use the open-source Skill.

微信添加 **staywildgrow**，留言「**加入社群**」。也可咨询 **599 元资料包**；社群与资料包均为可选入口，不影响开源 Skill 使用。
<!-- gingiris-community-cta:end -->
