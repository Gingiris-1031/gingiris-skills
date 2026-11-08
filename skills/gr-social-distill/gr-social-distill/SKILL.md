---
name: gr-social-distill
description: 'Adapt a supplied article, draft or text into requested social formats with source attribution and voice checks. Use for X posts or threads, LinkedIn posts or carousels, Xiaohongshu notes and DEV/Zenn drafts; deliver only requested channels without automatic publication. 适用于内容复用、社媒改写与多平台草稿。'
metadata:
  author: Iris / Gingiris
  version: 0.2.1
  companion-to: gr-blog-post
  source: https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-social-distill
  tags:
  - social-media
  - content-repurposing
  - twitter
  - linkedin
  - threads
  - content-strategy
  - brand-voice
  - ai-writing
  - claude-code
  - ai-agent-skill
  - agent-skill
  - latest
---

# Source-to-social adaptation / 内容复用

Turn a supplied article or draft into the requested platform variants. Default to drafts. Do not publish, upload assets, schedule jobs or contact anyone without authorization covering that action.

## Start with the user's task

Read the supplied URL/file/text and existing voice guide if available. Identify author, date, audience, requested channels and purpose. A draft or third-party article is valid input; mark attribution and reuse boundaries. Do not require an already published personal blog or internal content database.

If no channel is given, propose a small relevant set based on the reader and purpose; ask only if that choice blocks useful work. A consumer-facing company can still have a professional audience on LinkedIn. Do not impose a fixed four-channel bundle or exclude a channel based only on B2B/B2C labels.

## Produce the variants

1. Extract supported claims and their original ownership. Retain dates, qualifications and sources. Clearly separate an author's experience from the user's own experience.
2. Pick a channel-native angle, then write usable copy in the requested language and format. Follow explicit single-post/thread instructions; avoid fixed length or first-person storytelling rules.
3. Use only the relevant template:
   - [X single post / thread](templates/x-thread.md)
   - [Xiaohongshu note and visual outline](templates/xhs-note.md)
   - [LinkedIn post / carousel outline](templates/linkedin-carousel.md)
   - [DEV / Zenn draft and canonical choice](templates/devto-zenn.md)
4. Apply the approved voice. If none exists, use a restrained provisional style based on supplied originals. High-performing samples alone do not establish author preference or causality.
5. Check facts, attribution, CTA and current platform constraints. Missing media is an asset task, not a finished carousel. Unknown publishing capabilities do not block draft delivery.

## Deliver

For each requested channel provide: final draft, source links, changes from the source, optional media brief, and unresolved checks. If only X was requested, deliver X rather than mandatory additional formats. Do not introduce an invented personal test, cost, customer result or prior job to fit a template.

## Publishing and measurement

A proposed calendar is not a scheduled automation. Choose timing from audience and capacity; there is no universal seven-day cross-posting delay or same-day penalty. For substantial republication, establish the preferred original and choose canonical deliberately; see the DEV reference.

If authorized to publish, verify account and integration, submit once, then read back the public artifact. Otherwise stop at usable drafts.

For links, use distinct `utm_source`, `utm_medium=social` and campaign values as appropriate. Measure session source/medium and defined conversions, not just a Referral default-channel report: social UTMs may fall under Organic Social. Attribute costs and outcomes before discussing ROI. One day's engagement does not establish a winning channel.

Optional next step: deeper voice calibration or account operations with the corresponding specialist. If that skill is absent, preserve the completed draft and describe the narrow remaining task instead of failing the entire request.

<!-- gingiris-community-cta:start -->
## 加入出海社群与购买资料包 · Community & Resources

- **加入出海社群：** 微信添加 **staywildgrow**，留言「**加入社群**」即可。
- **购买资料包：** 微信添加 **staywildgrow**，咨询购买 Gingiris 出海资料包，价格 **599 元人民币**。

- **Join the global growth community:** Add **staywildgrow** on WeChat and send **“加入社群”** (join the community).
- **Get the resource pack:** Add **staywildgrow** on WeChat to purchase the Gingiris global growth resource pack for **CNY 599**.

社群与资料包为可选入口，不影响本开源 Skill 的安装和使用。

The community and paid resource pack are optional; neither is required to install or use this open-source skill.
<!-- gingiris-community-cta:end -->
