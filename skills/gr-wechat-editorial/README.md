---
license: mit
viewer: false
language:
- en
- zh
tags:
- agent-skills
- marketing
- wechat-editorial-skill
- chinese-article-workflow
pretty_name: WeChat Editorial Workflow Skill
---

# WeChat Editorial Workflow Skill / 微信公众号内容工作流

Turn source material into a reviewed Chinese article, formatted HTML and a traceable draft handoff. **`gr-wechat-editorial`** is an installable Gingiris agent instruction workflow, not a hosted application or a trained model.

将真实素材整理为经过审稿的中文文章、排版 HTML 和可回读的草稿交付。这是可安装的 Agent 工作流，安装后在支持 Skills 的助手中调用。

## Quick start / 快速开始

Use an agent environment with Agent Skills support and Node.js/npm for this CLI route. Select the target agent in the installer; loading behavior depends on the host.

```bash
npx skills@1.7.4 add Gingiris-1031/gingiris-skills --skill gr-wechat-editorial
```

Then ask your agent to use `gr-wechat-editorial` with the following task. The example inputs are illustrative; replace them with your own material.

```text
Use gr-wechat-editorial. Use these notes to draft a Chinese article for our Official Account. Preserve source ownership and prepare a local review package; do not publish.
```

```text
请使用 gr-wechat-editorial。用这些笔记写公众号文章，保留观点来源，交付本地审阅包，不正式发布。
```

安装后先确认助手能找到本 Skill，再用上面的示例提交真实材料。若无法发现，请检查安装器所选 Agent 和安装位置，再重新开启会话。

## When to use it / 适用场景

Authors turning interviews, meetings or original notes into WeChat Official Account articles.

将真实素材整理为经过审稿的中文文章、排版 HTML 和可回读的草稿交付。先提供下面的最少信息；已有上下文无需重复填写。

| Provide / 输入 | Receive / 输出 |
|---|---|
| Sources, speaker identities, reader, voice references, publication boundaries and delivery stage. | Article Markdown and HTML; source map; review notes; asset checklist; draft receipt when access is available |
| 素材、说话人、目标读者、文风参考、可公开范围和交付阶段 | 文章 Markdown/HTML；来源表；审稿记录；素材清单；具备权限时的草稿回执 |

## What a useful result looks like / 产出示意

> **Illustrative output structure, not a customer result:** article.md + article.html + source-map.md + review notes. Draft creation and draft readback are reported separately.

The deliverable should connect the supplied evidence to a decision or usable artifact. Missing source access, unverified claims and incomplete assets remain visible in the handoff. The example demonstrates structure; it does not claim a measured improvement.

以上是交付结构示意，不是客户业绩。输出应保留来源、未确认事实和下一步动作，方便你判断是否可用。

## Workflow and source material / 方法与材料

1. Supply the context above and name the decision or deliverable you need.
2. The agent follows [SKILL.md](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-wechat-editorial/SKILL.md), using the included references when relevant.
3. Review the artifact and evidence gaps before any external action. Live research, analytics or publishing may require additional tools and permissions.

- [templates](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-wechat-editorial/references/templates.md)
- [review and delivery](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-wechat-editorial/references/review-and-delivery.md)
- [provenance](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-wechat-editorial/references/provenance.md)

## Scope and common questions / 范围与常见问题

**What are the limits?** The included packager runs locally; it is not a WeChat API client. Live draft upload requires an authorized connection.

**Do I need paid tools?** Supplied material can support drafting and planning. Fresh web research, private analytics and account operations depend on the tools available in your agent environment; installation alone does not grant access.

**Does installation publish anything?** No. Instructions and templates do not create a publishing connection. External actions follow the task authorization and must be verified separately.

**需要准备什么？** 素材、说话人、目标读者、文风参考、可公开范围和交付阶段。材料不足时保留假设和缺口，不补造数据。

**会交付什么？** 文章 Markdown/HTML；来源表；审稿记录；素材清单；具备权限时的草稿回执。具体范围以你的请求为准，不强制输出全部模板。

## Related workflows / 相关工作流

Choose by the next task, rather than installing every related package:

- [gr-brand-voice-calibration](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-brand-voice-calibration)
- [gr-ai-content-ops](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-ai-content-ops)
- [gr-social-distill](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-social-distill)

## Maintenance, license and support / 维护、许可与支持

Maintained by Iris Wei / Gingiris. [Source and issue tracker](https://github.com/Gingiris-1031/gingiris-skills) · [Browse the Skills directory](https://tools.gingiris.com/skills/) · [MIT License](https://github.com/Gingiris-1031/gingiris-skills/blob/main/LICENSE).

Documentation reviewed: **2026-11-17**. This is a documentation update; workflow version is recorded in SKILL.md where available. No installation count, star count or historical case is a guarantee of your result.

<!-- gingiris-community-cta:start -->
### Optional community and resources / 可选社群与资料

Add **staywildgrow** on WeChat and send **“加入社群”** to join the growth community. A separate resource pack is available for **CNY 599**; neither is required to install or use the open-source Skill.

微信添加 **staywildgrow**，留言「**加入社群**」。也可咨询 **599 元资料包**；社群与资料包均为可选入口，不影响开源 Skill 使用。
<!-- gingiris-community-cta:end -->
