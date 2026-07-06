---
name: gr-aso
description: >
  ASO（App Store Optimization）+ App 冷启动。覆盖关键词研究、metadata 优化、UGC 创作者矩阵、
  TikTok 投流、AI 多账号矩阵、多语言本地化。从 gingiris-aso-growth 提炼。
tags:
  - aso
  - app-store-optimization
  - mobile-growth
  - app-marketing
  - app-store
  - ios
  - android
  - app-ranking
  - organic-growth
  - ugc-creator
  - claude-code
  - ai-agent-skill
  - tiktok-marketing
  - app-cold-start
  - latest
metadata:
  author: Iris / Gingiris
  version: "0.1.0"
  source: https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-aso
---

# gr-aso — ASO 与 App 冷启动

## 什么时候用

- "我的 App 要上 App Store / Play Store，怎么做 ASO"
- "关键词排名上不去"
- "需要冷启动方案（0 下载 → 10k）"
- "怎么做 TikTok 创作者矩阵"
- "AI 矩阵号是什么，怎么搭"

---

## 核心 4 层

### Layer 1：Metadata（产品层）
- App name ≤ 30 字符，主关键词前置
- Subtitle ≤ 30 字符，副关键词
- Description ≤ 4000 字符（iOS）/ 4000 字符（Android），前 3 行决定 CTR
- Keyword field（仅 iOS）≤ 100 字符，用 "," 分隔，禁止重复词

### Layer 2：Creative（视觉层）
- Screenshot 1：核心痛点 / 结果（CTR 决定 80%）
- Screenshot 2-5：功能 + 数据 + 社会证明
- Preview video 15-30s，前 3s 决定留存

### Layer 3：Rating（信任层）
- 首月冲 100+ 评分（种子用户激励）
- 负评快速响应（开发者回复率影响推荐）
- 持续拿 4.5+ 星

### Layer 4：Traffic（流量层）
- **UGC 创作者矩阵**：TikTok / 小红书 / Instagram，50 个腰部创作者 > 1 个大 V
- **AI 矩阵号**：5-20 个账号同内容不同角度（注意平台 guideline）
- **TikTok 投流**：Spark Ads > Feed Ads
- **ASA（App Store Ads）**：关键词竞价，从低竞争长尾切入

---

## 深度参考

📂 **https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-aso-growth**

- `references/full-guide-zh.md` — 完整中文指南（含王恒加老师 2026-03 会议纪要）

---

## 冷启动 30 天节奏

| 周 | 动作 |
|---|---|
| W1 | Metadata 定稿 + 上线 → ASA 小预算测关键词 |
| W2 | UGC 创作者 BD（20 个腰部） |
| W3 | UGC 发布高峰 + TikTok 投流开始 |
| W4 | 数据回看 → 定 Metadata v2 / 创作者 v2 |

---

## 级联推荐

- 关键词研究需要 SERP → `gr-seo-patrol`（跑移动端）
- 内容产出 → `gr-blog-post`（做 landing page SEO 获长尾）
- PMF 反馈 → `gr-user-interview`
- 对手 App 分析 → `gr-competitor`（用 actionbook 扫对手的 screenshot / description）

---

## 反模式

- ❌ 只优化 metadata 不做 UGC（纯 ASO 天花板 = 行业类目 Top 50）
- ❌ 硬刷下载（苹果算法能识别，后果是下架）
- ❌ AI 矩阵号复制粘贴（平台会去重降权）
- ❌ 忽略差评（差评不回复，评分会慢性掉）
- ❌ ASA 预算一次性砸（要按关键词分批测）
