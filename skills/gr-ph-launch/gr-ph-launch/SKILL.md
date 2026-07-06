---
name: gr-ph-launch
description: >
  Product Hunt 发布剧本。从 30x 日冠经验提炼的完整 GTM 流程：T-14 预热 → T-0 发布日 → T+7 post-launch。
  覆盖 hunter 选择、maker comment、community seeding、评论节奏、防踩雷。当用户说"我要发 PH"、
  "Product Hunt 准备"、"找 hunter"、"写 maker comment"时调用。
when_to_use: |
  Use this skill when you need to: execute a Product Hunt launch (T-14 to T+7), select a
  hunter, write maker comments, seed community upvotes, set 00:01 PST timing, or avoid
  PH shadowban and maximize upvote velocity on launch day.
  Trigger phrases: "发PH" | "Product Hunt准备" | "hunter选择" | "maker comment" |
  "PH发布" | "Product Hunt launch" | "community seeding" | "PH打榜方法"
metadata:
  author: Iris / Gingiris
  version: "0.1.0"
  source: https://github.com/Gingiris/gingiris-launch
---

## ⚠️ 2C 产品慎用 Product Hunt

本 skill 默认 dev / maker / B2B 受众。**2C 消费品 / 教育 / 应用 / 游戏**：Product Hunt 受众是 maker/科技人，与普通消费者错配、ROI 极低——最多发一次拿个 badge。请把精力换到 **垂类社区（Reddit / 小红书 / 知乎 / Naver 카페）+ 短视频（TikTok / 抖音 / YouTube）+ 垂直 KOL**，并用"免费产品当钩子"做转化。完整 2C 渠道数据库（各国 MAU + 公开来源）+ 三路 Launch 分叉见 → `gingiris-seo-geo/references/2c-adaptation.md`（及 `gingiris-launch`）。

---

# gr-ph-launch — Product Hunt 发布

## 深度参考

详细方法论与案例库见：
- `references/framework.md` —— 14 天时间线 + 5 大板块
- `references/hunter-playbook.md` —— hunter 选择矩阵
- `references/maker-comment.md` —— maker comment 6 种模板

> 注：首次使用时 Claude 应读 `references/framework.md` 再开始。

---

## 14 天时间线（精简版）

### T-14：准备
- 产品页面就绪（落地页、定价、FAQ）
- 已有 ≥ 100 早鸟用户 + 邮箱列表
- 选 1 个 hunter（优先级：活跃 > follower 数）
- 筹备 3 张主 gallery 图 + 1 个 30 秒 demo video

### T-7 到 T-2：预热
- PH discussion 板块发 1 篇"we're launching, AMA"
- Twitter / LinkedIn / Reddit 预告（**不贴 launch 页面链接**，避免抢流量）
- Newsletter 给用户打招呼
- 确认 hunter 时区 + 发布时间（**PST 00:01**）

### T-1：终检
- 所有 asset 最终版锁定
- 准备 first comment 文稿（500 字以内）
- 准备 10 条可能的 FAQ 回复模板
- 联系 10-20 个核心支持者提醒明早

### T-0：发布日
- **00:01 PST** hunter 发布
- **00:15** maker（你）发 first comment
- **整天**：每 30 分钟回一批评论；不刷 upvote
- **14:00 PST**：peak time，推 second wave（通讯录 + community）
- **23:00 PST**：总结发一条感谢帖

### T+1 到 T+7：momentum
- 回完所有评论（包括差评）
- 把 PH featured 截图 + 数据做成 case study
- 若进入 daily #1 → 做一篇"how we won"博客（`gr-blog-post`）
- 将所有 upvoter 邮箱导入用户池

---

## Hunter 选择矩阵

| 优先级 | 标准 |
|---|---|
| P0 | 最近 30 天有成功 hunt 且产品领域相似 |
| P1 | Follower 1k+ 且活跃（每周发帖） |
| P2 | 跟你有真实社交关系（聊过、共同朋友） |
| ❌  | Follower > 50k 但已 6 个月没 hunt |

搜 hunter：`https://www.producthunt.com/@<category>-hunters`

---

## Maker Comment 6 种模板

（详见 `references/maker-comment.md`）

1. **Founder story**：为什么做 → 你的痛 → 解法
2. **Before / After**：有你的产品前 vs 后，对比鲜明
3. **Key stats hook**：一个爆炸性数据开头
4. **Honest limitation**：承认产品还不完美，显得真实
5. **Community thanks**：感谢参与测试的用户（点名 @）
6. **Tech stack pride**：讲技术选型（适合开发者向产品）

选哪个：看目标受众。To dev → 6；to general → 1 或 3。

---

## 反踩雷清单

- ❌ 不要在 launch 当天还在改产品（flaky）
- ❌ 不要让家人朋友刷 upvote（PH shadowban 很快）
- ❌ 不要在 first comment 留外部链接（触发审核降权）
- ❌ 不要忘记 mobile 截图（40% 流量来自手机）
- ❌ 不要硬撑 daily #1，#2-#3 也是成功（且少被喷）

---

## 上票控速红线（2026 实测更新）

- **总量 ≤100 票/小时、单一渠道 ≤30 票/小时**——PH 约每 2 小时清一次可疑票，突刺会被剥掉
- 支持者用**手机 + 蜂窝数据（4G）**投票，别挤同一个办公室 Wi-Fi
- **badge 曝光分层：周榜 ≈ 日榜 7 倍、月榜 ≈ 30 倍**——先定冲哪个榜再定节奏；冲月榜选每月第二/三周的周二

---

## Go / no-go：预算分级基准

| 预算 | 现实产出 |
|---|---|
| ~$1K | 小几百注册（跳过 PH，直接 KOC + 垂直社区） |
| $5K | 24h 约 1,800 票可达——实战案例：冲上日榜第一后被 PH 事后清票收回。控速红线必须遵守 |
| $1–2 万 | ~100 万曝光 + 小几千注册 |

**预算不高别卷 PH**：同预算给 ~10 个 Twitter KOL/KOC 曝光和注册都更高——PH 曝光→upvote 转化仅 ~1%，Reddit 开源宣发曝光→star 转化 5–8%。

---

## 发布日流量倒排法

先定总流量盘子 → 拆每渠道硬数字 → 每渠道 UTM 短链归因。
实测（某 AI Agent 产品，2025-12）：50 万流量 = 40 万 Twitter（40 红人 quote）+ 2 万 Reddit + 2 万 YouTube 投流 + 2 万群组 + 其余 → **约 800 注册、CAC $6.25**。

进阶节奏：**双日结构**（发布日一半红人导官网、打榜日另一半导 PH）；**KOL 集中爆破**（50–100 个 KOL 约定 24–48h 内密集发布）。

---

## 级联推荐

- 发布日 + 24h → `gr-seo-patrol` 监控"<product name> product hunt"等关键词排名
- 上 daily #1 后 → `gr-blog-post` 写一篇"how we won"并设 canonical 为主
- 评论有大量质疑 → `gr-user-interview` 启动正式访谈

---

## API 依赖

| Service | Env var |
|---|---|
| Product Hunt（公开页爬取）| 无（用 web-access skill） |
| GitHub PAT（博客联动） | `GITHUB_TOKEN` |
