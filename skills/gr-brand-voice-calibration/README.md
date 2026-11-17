---
license: mit
viewer: false
language:
- en
- zh
tags:
- agent-skills
- marketing
- brand-voice-calibration
- writing-voice-agent-skill
pretty_name: Brand Voice Calibration Skill
---

# Brand Voice Calibration Skill / 个人与品牌文风校准

Build a reusable voice guide from original writing, speech and the author’s own corrections. **`gr-brand-voice-calibration`** is an installable Gingiris agent instruction workflow, not a hosted application or a trained model.

以本人原文、原话和亲手修改为依据，提炼能复用、可试写验证的文风指南。这是可安装的 Agent 工作流，安装后在支持 Skills 的助手中调用。

## Quick start / 快速开始

Use an agent environment with Agent Skills support and Node.js/npm for this CLI route. Select the target agent in the installer; loading behavior depends on the host.

```bash
npx skills@1.7.4 add Gingiris-1031/gingiris-skills --skill gr-brand-voice-calibration
```

Then ask your agent to use `gr-brand-voice-calibration` with the following task. The example inputs are illustrative; replace them with your own material.

```text
Use gr-brand-voice-calibration. Compare these original posts with my edits. Build a provisional voice guide and test it on one English post without inventing personal experience.
```

```text
请使用 gr-brand-voice-calibration。对照这些原始动态和我的修改，建立暂定文风指南，再用一条英文试写验证，不添加我没经历过的故事。
```

安装后先确认助手能找到本 Skill，再用上面的示例提交真实材料。若无法发现，请检查安装器所选 Agent 和安装位置，再重新开启会话。

## When to use it / 适用场景

Authors whose AI drafts sound generic or lose their voice when adapted between Chinese and English.

以本人原文、原话和亲手修改为依据，提炼能复用、可试写验证的文风指南。先提供下面的最少信息；已有上下文无需重复填写。

| Provide / 输入 | Receive / 输出 |
|---|---|
| Authorized originals with context, liked/disliked examples and the current writing task. | Source index; contextual voice rules; counterexamples; test draft; unresolved preferences |
| 获准使用的原创样本、上下文、喜欢和不喜欢的例子、当前写作任务 | 来源索引；带场景的文风规则；反例；试写；待确认偏好 |

## What a useful result looks like / 产出示意

> **Illustrative output structure, not a customer result:** Observed trait: conclusions stay qualified → retain uncertainty in a test draft → ask the author whether the result feels accurate.

The deliverable should connect the supplied evidence to a decision or usable artifact. Missing source access, unverified claims and incomplete assets remain visible in the handoff. The example demonstrates structure; it does not claim a measured improvement.

以上是交付结构示意，不是客户业绩。输出应保留来源、未确认事实和下一步动作，方便你判断是否可用。

## Workflow and source material / 方法与材料

1. Supply the context above and name the decision or deliverable you need.
2. The agent follows [SKILL.md](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-brand-voice-calibration/SKILL.md), using the included references when relevant.
3. Review the artifact and evidence gaps before any external action. Live research, analytics or publishing may require additional tools and permissions.

- [performance hypotheses](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-brand-voice-calibration/references/performance-hypotheses.md)
- [calibration](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-brand-voice-calibration/references/calibration.md)

## Scope and common questions / 范围与常见问题

**What are the limits?** Engagement is not proof of authentic voice. Private source archives are not published with the guide.

**Do I need paid tools?** Supplied material can support drafting and planning. Fresh web research, private analytics and account operations depend on the tools available in your agent environment; installation alone does not grant access.

**Does installation publish anything?** No. Instructions and templates do not create a publishing connection. External actions follow the task authorization and must be verified separately.

**需要准备什么？** 获准使用的原创样本、上下文、喜欢和不喜欢的例子、当前写作任务。材料不足时保留假设和缺口，不补造数据。

**会交付什么？** 来源索引；带场景的文风规则；反例；试写；待确认偏好。具体范围以你的请求为准，不强制输出全部模板。

## Related workflows / 相关工作流

Choose by the next task, rather than installing every related package:

- [gr-social-distill](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-social-distill)
- [gr-wechat-editorial](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-wechat-editorial)
- [gr-ai-content-ops](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-ai-content-ops)

## Maintenance, license and support / 维护、许可与支持

Maintained by Iris Wei / Gingiris. [Source and issue tracker](https://github.com/Gingiris-1031/gingiris-skills) · [Browse the Skills directory](https://tools.gingiris.com/skills/) · [MIT License](https://github.com/Gingiris-1031/gingiris-skills/blob/main/LICENSE).

Documentation reviewed: **2026-11-17**. This is a documentation update; workflow version is recorded in SKILL.md where available. No installation count, star count or historical case is a guarantee of your result.

<!-- gingiris-community-cta:start -->
### Optional community and resources / 可选社群与资料

Add **staywildgrow** on WeChat and send **“加入社群”** to join the growth community. A separate resource pack is available for **CNY 599**; neither is required to install or use the open-source Skill.

微信添加 **staywildgrow**，留言「**加入社群**」。也可咨询 **599 元资料包**；社群与资料包均为可选入口，不影响开源 Skill 使用。
<!-- gingiris-community-cta:end -->
