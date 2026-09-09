---
name: gr-oss-marketing
description: >
  开源项目发布整合营销。覆盖 GitHub star 增长、KOL 合作、Reddit / HN / Discord / Telegram 社群分发、
  多语言落地（中英日韩）。从 gingiris-opensource 提炼。适用场景：要发布一个开源项目，
  想在 6 个月内冲 10k star，或已发布但流量卡住要破局。
when_to_use: |
  Use this skill when you need to: launch an open-source project for maximum GitHub star
  burst, distribute across Reddit / HN / Discord / Telegram, partner with developer KOLs,
  build multilingual content matrix (en/ja/ko), or break through a star-growth plateau.
  Trigger phrases: "开源项目发布" | "GitHub star增长" | "Show HN" | "Reddit launch" |
  "OSS marketing" | "dev.to" | "开发者KOL" | "open source growth" | "HN怎么发"
metadata:
  author: Iris / Gingiris
  version: "0.1.0"
  source: https://skills.sh/Gingiris-1031
---

# gr-oss-marketing — 开源营销

## 先执行：发布契约

在给渠道建议前，输出 `Go / Fix / No-Go` 表，检查：定位、陌生人 Quick Start、
可复现 Demo、License/安全/隐私、发布周响应 owner、Star 之后的激活与商业承接。
任何关键项为 No-Go 时先修复，不用铺量掩盖产品问题。

把源 TODO 表统一成 5 个视图：

1. 研究表：ICP、社区规则、近期高质量内容、风险、核验日期。
2. 内容表：原生角度、证据、素材、CTA、审批、状态。
3. 分发表：Owner、账号、当地时间与时区、UTM/source、实际链接。
4. 数据表：基线、2h、24h、72h、7d、成本、结论。
5. 总控表：依赖、Go/No-Go、事故 owner、停止条件、复盘日期。

统一漏斗为 `曝光 → repo 访问 → install/quickstart → activation → D7 →
contributor/qualified lead → paid`。Star 只是开发者兴趣信号。原生指标缺失时写
`数据不可用`，不得从曝光或互动推算。

红线：不买 Star/账号、不刷榜或协调虚假 Upvote、不隐藏付费合作、不批量骚扰、
不让 AI 冒充真人参与社区。Reddit/HN/Discord/群组逐个核对规则并披露关联。

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
- [ ] Hacker News Show HN（只有真实技术新意且团队能在线答疑时；发布时间按近期同类帖验证）
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

📂 **https://skills.sh/Gingiris-1031**

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

## Star 地区分布 & 发布时序

- 同一国家/地区 star 占比不超过 **20%**，否则难上 GitHub Trending。
- 工具：**star-history.com**（涨幅趋势）、**OSS Insight**（国家分布，国人开发）
- 发布时序：**第一周只做海外宣发**，第二周才做国内。顺序反了会破坏分布。
  - AFFiNE 真实案例：开源第一周拿 6000 star，故意不发朋友圈 / 不进国内社群。

## README 优化要点

- [ ] **不超过 8 屏**，开发者文档单独链接，不塞进 README
- [ ] 加**提醒点 star 小动图**（类比B站一键三连，用户需要被提醒）
- [ ] **backlinks 循环**：所有跳出链接（官网/博客/文档）必须能跳回 GitHub

## PR 文章策略

- 准备一篇完整阐述项目优势的文章（官网 Blog / Medium / dev.to）
- 目的：给所有想帮你传播的人一把枪
- 案例：德国用户主动发了40多个论坛，没打招呼就发了——能发出去是因为有参考文章

## 竞品 follower 私信

- 给竞品（Notion / Miro 等）的 Twitter follower 发私信
- 实战数据：几百条私信 → 几百个 star 转化
- 优先找吐槽竞品的用户，已有切换意愿

## 反模式

- ❌ 刷 star（GitHub 很快能检测，后果是搜不到）
- ❌ Reddit 只发一次就跑（社群反感，被 ban 风险高）
- ❌ 中文社群先发英文项目（除非你目标就是中文用户，否则英文 > 多语言 > 中文的顺序）
- ❌ README 放太多 emoji / badge（降低可信度）
