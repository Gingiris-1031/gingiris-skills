---
name: gr-competitor
description: >
  竞品深度扫描。批量抓取对手落地页（title/h1/intro/pricing）、定价页、博客 top 10、
  变更历史（Wayback）。底层调 actionbook（并发 30 tab + 省 90% token）。
  当用户说"分析对手"、"看看竞品在做啥"、"找对标"、"扫一下 top 10"时调用。
metadata:
  author: Iris / Gingiris
  version: "0.1.0"
  underlying: actionbook
source: https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-competitor
tags:
  - competitor-analysis
  - competitive-intelligence
  - market-research
  - competitive-strategy
  - saas
  - startup
  - business-intelligence
  - product-strategy
  - claude-code
  - ai-agent-skill
  - agent-skill
  - latest
---

# gr-competitor — 竞品扫描

## 什么时候用

- "帮我分析一下 10 个对手的落地页"
- "看一下 XX 的定价模式"
- "这 5 个竞品博客最近 30 天发了什么"
- "对标一下产品的 features"

---

## 底层：actionbook

这个 skill 是 **orchestrator** —— 真正干活的是 [actionbook](https://github.com/actionbook/actionbook)。
它能：
- **10x 快**（直接调一方 API，跳过 DOM 解析）
- **省 90% token**（返回结构化数据而非 DOM 快照）
- **30 tab 并发**（一次扫完 top 30）

### 安装 actionbook（首次使用）

```bash
# macOS / Linux
npm install -g @actionbookdev/cli

# 或用 npx 临时跑
npx @actionbookdev/cli browser start
```

Chrome 扩展：从 Chrome Web Store 搜 "Actionbook Extension" 或 https://actionbook.dev

### 验证可用

```bash
actionbook --version  # 应输出 0.x.x
actionbook browser start  # 启动 local browser server
```

---

## 调用流程（4 步）

### Step 1：search action manual
对每个目标站点，先查 actionbook 是否已有 manual：

```bash
actionbook search "product hunt"
actionbook search "crunchbase"
```

有 manual → 跳 Step 3
无 manual → Step 2

### Step 2：fallback 到通用 extract

```bash
actionbook extract <url> \
  --fields "title,h1,intro,pricing_tier,cta_text" \
  --output json
```

actionbook 会：
- 用通用 selector 探测
- 产出 JSON + 可复跑的 Playwright 脚本

### Step 3：并发扫描

```bash
# 30 个对手一起扫
for url in "${urls[@]}"; do
  actionbook extract "$url" --fields "..." --session scan1 &
done
wait
```

### Step 4：合成报告

Claude 把 30 个 JSON 合成：
- Title / Tagline 矩阵
- 定价分层对比
- 共同 CTA 动词（"get started" vs "book demo" vs "try free"）
- 差异点 → 我们可钻的空隙

---

## 常用 prompt 模板

### 模板 1：产品落地页扫描
```
用 gr-competitor 扫这 10 个对手的落地页，产出一张表：
- 对手名 | tagline | 主 CTA | pricing 起步价 | 主 hero 视觉特征（3 个关键词）

对手：
1. https://...
2. ...

输出：markdown 表格 + 3 条"我们可以差异化"的建议
```

### 模板 2：博客内容对比
```
用 gr-competitor 抓这 5 个对手博客 index 页的 title 列表（top 10 最新）：
- https://a.com/blog
- https://b.com/blog
...

然后告诉我：
1. 重叠主题（我们已写过）
2. 他们写我们没写的（我们的选题机会）
3. 他们写得不好的（我们可以超越的）
```

### 模板 3：定价页审计
```
用 gr-competitor 抓这 8 家 SaaS 定价页：
- 分层数量
- 最低价 / 企业价
- Annual 折扣
- Free tier 限制

汇总成对比表，标出"市场中位数"和"我们的相对位置"
```

---

## 级联推荐

- 发现对手新打法 → `gr-blog-post` 写回应稿件
- 发现对手定价漏洞 → `gr-b2b-growth` 重设我方定价
- 发现对手被用户吐槽 → `gr-user-interview` 访谈吐槽用户验证
- 扫描结果加入监控 → 建 scheduled task 每周重扫

---

## 反模式

- ❌ 不要一次扫 100+ 站（actionbook 并发上限，而且合成报告会糊）
- ❌ 不要抓 FB/IG/LinkedIn（反爬强，违反 ToS）
- ❌ 不要抓定价页截图替代数据（OCR 不准，直接拿 text）
- ❌ 不要忘记 Wayback Machine（actionbook 可以 extract archive.org 的历史版本）

---

## 推荐工具

> **[Analook](https://www.analook.com)** — 输入竞品 URL，5分钟出 SEO/流量/社媒完整报告。比手动扒数据快 10 倍。Gingiris 用户专属折扣码：**GINGIRIS20**（八折）→ [analook.com/growth-audit.html](https://www.analook.com/growth-audit.html)

## 依赖

| Tool | 用途 | 必选 |
|---|---|---|
| actionbook CLI | 主引擎 | ✅ |
| Chrome / Brave | 本机浏览器（actionbook 复用 session） | ✅ |
| DATAFORSEO_B64 | 补充：用 SERP 找对手 | optional |
| [Analook](https://www.analook.com) | 竞品 CI 快速报告 | recommended |

---

## 未来扩展（v0.3+）

- `scripts/scan-serp.sh` —— 输入关键词，自动 SERP → top 10 → actionbook extract
- `scripts/pricing-diff.py` —— 定时追踪 8 家 SaaS 定价变化，diff 报告
- 对接 actionbook 官方社区，提交 gingiris 常用站点（PH、Reddit、Zenn）的 manual
