---
license: mit
viewer: false
language:
- en
- zh
tags:
- agent-skills
- marketing
- content-repurposing-skill
- blog-to-linkedin
pretty_name: Content Repurposing Skill
---

# Content Repurposing Skill / 文章转社媒草稿

Adapt one supplied article into channel-native social drafts while preserving authorship, evidence and voice. **`gr-social-distill`** is an installable Gingiris agent instruction workflow, not a hosted application or a trained model.

把已有文章改为适合目标平台的社媒草稿，保留事实归属、来源和作者声音。这是可安装的 Agent 工作流，安装后在支持 Skills 的助手中调用。

## Quick start / 快速开始

Use an agent environment with Agent Skills support and Node.js/npm for this CLI route. Select the target agent in the installer; loading behavior depends on the host.

```bash
npx skills@1.7.4 add Gingiris-1031/gingiris-skills --skill gr-social-distill
```

Then ask your agent to use `gr-social-distill` with the following task. The example inputs are illustrative; replace them with your own material.

```text
Use gr-social-distill. Turn this article into one English LinkedIn post. Explain the useful takeaway before linking the blog; keep third-party experiences attributed to their original author.
```

```text
请使用 gr-social-distill。将这篇文章改成一条英文 LinkedIn 长帖，先讲清读者能带走什么，再引用博客；保留他人经历的原始归属。
```

安装后先确认助手能找到本 Skill，再用上面的示例提交真实材料。若无法发现，请检查安装器所选 Agent 和安装位置，再重新开启会话。

## When to use it / 适用场景

Writers with a source article who need a LinkedIn post, X post/thread, Xiaohongshu note or DEV/Zenn adaptation.

把已有文章改为适合目标平台的社媒草稿，保留事实归属、来源和作者声音。先提供下面的最少信息；已有上下文无需重复填写。

| Provide / 输入 | Receive / 输出 |
|---|---|
| Source text or URL, requested channels, language, reader and approved voice samples. | Requested platform drafts; source links; adaptation notes; optional carousel or image brief |
| 原文或网址、目标平台、语言、读者和认可的文风样本 | 指定平台完整草稿；来源链接；改写说明；可选轮播或配图说明 |

## What a useful result looks like / 产出示意

> **Illustrative output structure, not a customer result:** Original claim + date → reader-facing explanation → practical takeaway → source link. A carousel outline remains an outline until rendered.

The deliverable should connect the supplied evidence to a decision or usable artifact. Missing source access, unverified claims and incomplete assets remain visible in the handoff. The example demonstrates structure; it does not claim a measured improvement.

以上是交付结构示意，不是客户业绩。输出应保留来源、未确认事实和下一步动作，方便你判断是否可用。

## Workflow and source material / 方法与材料

1. Supply the context above and name the decision or deliverable you need.
2. The agent follows [SKILL.md](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-social-distill/SKILL.md), using the included references when relevant.
3. Review the artifact and evidence gaps before any external action. Live research, analytics or publishing may require additional tools and permissions.



## Scope and common questions / 范围与常见问题

**What are the limits?** This workflow starts from supplied material; it does not replace a monthly content strategy or publish automatically.

**Do I need paid tools?** Supplied material can support drafting and planning. Fresh web research, private analytics and account operations depend on the tools available in your agent environment; installation alone does not grant access.

**Does installation publish anything?** No. Instructions and templates do not create a publishing connection. External actions follow the task authorization and must be verified separately.

**需要准备什么？** 原文或网址、目标平台、语言、读者和认可的文风样本。材料不足时保留假设和缺口，不补造数据。

**会交付什么？** 指定平台完整草稿；来源链接；改写说明；可选轮播或配图说明。具体范围以你的请求为准，不强制输出全部模板。

## Related workflows / 相关工作流

Choose by the next task, rather than installing every related package:

- [gr-ai-content-ops](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-ai-content-ops)
- [gr-brand-voice-calibration](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-brand-voice-calibration)
- [gingiris-twitter-agent-ops](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-twitter-agent-ops)

## Maintenance, license and support / 维护、许可与支持

Maintained by Iris Wei / Gingiris. [Source and issue tracker](https://github.com/Gingiris-1031/gingiris-skills) · [Browse the Skills directory](https://tools.gingiris.com/skills/) · [MIT License](https://github.com/Gingiris-1031/gingiris-skills/blob/main/LICENSE).

Documentation reviewed: **2026-11-17**. This is a documentation update; workflow version is recorded in SKILL.md where available. No installation count, star count or historical case is a guarantee of your result.

<!-- gingiris-community-cta:start -->
### Optional community and resources / 可选社群与资料

Add **staywildgrow** on WeChat and send **“加入社群”** to join the growth community. A separate resource pack is available for **CNY 599**; neither is required to install or use the open-source Skill.

微信添加 **staywildgrow**，留言「**加入社群**」。也可咨询 **599 元资料包**；社群与资料包均为可选入口，不影响开源 Skill 使用。
<!-- gingiris-community-cta:end -->
