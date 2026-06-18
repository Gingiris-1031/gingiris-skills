---
name: gr-oss-marketing
description: >
  开源项目发布整合营销。覆盖 GitHub star 增长、KOL 合作、Reddit / HN / Discord / Telegram 社群分发、
  多语言落地（中英日韩）。从 gingiris-opensource 提炼。适用场景：要发布一个开源项目，
  想在 6 个月内冲 10k star，或已发布但流量卡住要破局。
metadata:
  author: Iris / Gingiris
  version: "0.1.0"
  source: https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-oss-marketing
tags:
  - open-source-marketing
  - github-stars
  - oss
  - developer-marketing
  - product-hunt
  - show-hn
  - cold-start
  - community
  - kol-outreach
  - launch-strategy
  - claude-code
  - ai-agent-skill
  - agent-skill
  - latest
---

# gr-oss-marketing — 开源营销

## 什么时候用

- "我要发一个开源项目，从 0 怎么起"
- "GitHub star 增长卡在 xxx 不动了"
- "如何找开发者 KOL 合作"
- "Reddit / HN 怎么发不被 ban"
- "如何做 dev.to / Zenn / CSDN 内容矩阵"

---

## 核心框架（3 阶段）

### 阶段 1：Pre-launch（T-30 到 T-0）
- [ ] README 起好（英文主，首屏截图 < 3s 读懂）
- [ ] Demo video ≤ 60s，有字幕
- [ ] License 选对（MIT/Apache-2/AGPL 各有陷阱）
- [ ] 3-5 个早鸟 maintainer / contributor
- [ ] 社群频道就位（Discord 或 Telegram，英文为主）

### 阶段 2：Launch（T-0 到 T+14）
- [ ] Product Hunt 发（联动 `gr-ph-launch`）
- [ ] Hacker News Show HN（周二美东 9am 或周六）
- [ ] Reddit：选 3 个相关 sub（r/selfhosted / r/programming / 细分技术 sub）
- [ ] Dev.to / Zenn / CSDN 发技术深度文
- [ ] 找 3-5 个 KOL 转（优先活跃度 > follower 数）

### 阶段 3：Growth（T+14 到 T+180）
- [ ] 每周 1 篇技术 blog（联动 `gr-blog-post`）
- [ ] GitHub Issues → 内容素材（用户问题变 FAQ）
- [ ] 每月发 1 次 update（邮件列表 + Discord）
- [ ] 出海本地化（日韩先，联动 gr-blog-post i18n 流程）

---

## 深度参考

所有细节、KOL 清单、话术模板、案例库在 upstream repo：

📂 **https://github.com/Gingiris/gingiris-opensource**

- `references/preparation.md` — Pre-launch 完整清单
- `references/channels.md` — 分发渠道矩阵
- `references/templates.md` — KOL 接触话术 / Reddit 模板 / HN Show HN 模板
- `references/seo-geo-guide.md` — 开源项目 SEO/GEO

首次调用时 Claude 应 fetch 这些文件作为深度参考。

---

## 级联推荐

- 阶段 1 完成 → `gr-ph-launch`（统一走 PH 发布流程）
- 阶段 2 Show HN 成功 → `gr-seo-patrol` 加监控 "<project> github"
- 阶段 3 需要产内容 → `gr-blog-post`
- 发现对手新打法 → `gr-competitor` 深挖

---

## 反模式

- ❌ 刷 star（GitHub 很快能检测，后果是搜不到）
- ❌ Reddit 只发一次就跑（社群反感，被 ban 风险高）
- ❌ 中文社群先发英文项目（除非你目标就是中文用户，否则英文 > 多语言 > 中文的顺序）
- ❌ README 放太多 emoji / badge（降低可信度）
