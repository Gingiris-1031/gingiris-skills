# 关键词漏斗策略

> 从高意向到低意向，系统化覆盖用户搜索路径

---

## 关键词漏斗模型

用户的购买决策是一个漏斗，每个阶段都有对应的搜索行为：

```
TOFU（问题意识）
  "how to improve team collaboration"
  "what is product-led growth"
    ↓
MOFU（方案研究）
  "best collaboration software 2026"
  "Notion vs Obsidian"
    ↓
BOFU（购买决策）
  "[产品] pricing"
  "[产品] reviews"
  "[产品] vs [竞品]"
```

### 关键词矩阵

| 漏斗阶段 | 关键词类型 | 示例 | 内容类型 | 优先级 |
|----------|-----------|------|----------|-------|
| **BOFU** | 品牌型 | [产品] pricing / demo / trial | 定价页、试用页 | P0 |
| **BOFU** | 评价型 | [产品] reviews / alternatives | 评价聚合页 | P0 |
| **MOFU** | 对比型 | [产品A] vs [产品B] | 对比页面 | P1 |
| **MOFU** | 品类型 | best [品类] software for [场景] | 榜单文章 | P1 |
| **TOFU** | 问题型 | how to [解决问题] | 博客、指南 | P2 |
| **TOFU** | 教育型 | what is [概念] | 术语解释、Glossary | P2 |

---

## 优先级原则：BOFU First

**从漏斗底部往上做。**

大多数人直觉是从 TOFU 开始——写大量教育型博客。但这是错的：

1. **BOFU 关键词转化率最高** — 搜索 "[产品] pricing" 的人已经在决策期
2. **BOFU 页面数量有限** — 定价页、对比页加起来不超过 20 个，集中火力做好
3. **MOFU 对比页是 SEO 金矿** — 截获正在对比竞品的用户
4. **TOFU 是规模化阶段** — 等核心页面排名稳定后再扩展

### 执行顺序

```
Phase 1（Week 1-4）: BOFU 核心页面
  → 定价页 + FAQ Schema
  → 前 5 个竞品对比页
  → 产品功能独立页面

Phase 2（Week 5-8）: MOFU 内容
  → "best [品类] for [场景]" 榜单
  → 更多竞品对比页（≥10个）
  → 客户案例页

Phase 3（Week 9+）: TOFU 规模化
  → Topic Cluster 博客内容
  → Glossary 术语页
  → 每周 4 篇节奏持续产出
```

---

## 关键词研究方法

### 工具选择

| 工具 | 用途 | 免费/付费 |
|------|------|----------|
| Ahrefs | 关键词难度（KD）+ 搜索量 | 付费 |
| Google Search Console | 已有排名词发现 | 免费 |
| AnswerThePublic | 问题型关键词发现 | 免费额度 |
| AlsoAsked | "People Also Ask" 挖掘 | 免费额度 |
| Google Autocomplete | 实时搜索建议 | 免费 |

### 选词标准

```
理想关键词画像：
- KD（关键词难度）: 30-50（竞争适中，新站可排名）
- 月搜索量: 100-1000（长尾但有量）
- 商业意图: 中-高（带有 "best" "vs" "pricing" 等信号词）
- 内容差距: 现有排名页质量不高，有超越机会
```

### 竞品关键词偷师

1. 用 Ahrefs 输入竞品域名
2. 导出 "Organic Keywords" 排名词
3. 筛选 KD 30-50、Volume 100+ 的词
4. 找出竞品排名但你没做的词 = 你的机会

---

## 关键词到内容的映射

### Title 公式

| 内容类型 | Title 模板 |
|----------|-----------|
| 教程类 | How to [任务] in 2026: [数字] [方法] |
| 榜单类 | [数字] Best [品类] Tools for [场景] in 2026 |
| 对比类 | [产品A] vs [产品B]: Which is Better in 2026? |
| 指南类 | The Complete Guide to [主题] for [目标用户] |
| 案例类 | How [公司] [成果] with [产品] |

### Meta Description 公式

```
[产品/方法] helps [目标用户] [核心价值]. [关键功能/数据点]. [CTA].

例: HeyGen helps marketers create professional videos in minutes 
with AI avatars. No filming required. Start your free trial.
```

---

## Topic Cluster 内链结构

```
支柱页面: The Complete Guide to [品类]
  ├── 集群: How to [任务1] with [品类]
  ├── 集群: [品类] Best Practices for [行业]
  ├── 集群: [品类] vs [替代方案]
  ├── 集群: [品类] ROI Calculator
  └── 集群: [品类] Glossary
```

**内链规则：**
- 每篇集群文章链接回支柱页
- 支柱页链接到所有集群文章
- 集群文章之间交叉链接（相关主题）
- 锚文本使用目标关键词（不要 "click here"）

---

## 监控与迭代

### 每周检查

- [ ] Google Search Console: 新增排名词、点击率变化
- [ ] Ahrefs: 核心词排名变动
- [ ] 内容日历: 本周发布计划是否按时完成

### 每月优化

- [ ] 排名 11-20 位的文章 → 优化标题和内容，冲进首页
- [ ] 高曝光低点击的词 → 优化 Title 和 Meta Description
- [ ] 流量下降的文章 → 更新数据和案例

---

*关键词漏斗策略 v1.0 — Gingiris SEO/GEO Playbook*
