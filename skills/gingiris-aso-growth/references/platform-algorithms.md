# App Store vs Google Play 平台算法详解 · 速查手册

> 整理自：王恒加老师 ASO 学习会议纪要（2026年3月）+ 行业公开研究（Appfigures 2025、AppTweak 2025、Google Play Console Help）。
> 一句话记忆：**App Store 是"元数据精确匹配"，Google Play 是"文本理解 + 技术性能"**——同一套关键词策略不能双端复用。

## 核心差异总表

| 维度 | App Store | Google Play |
|:---|:---|:---|
| **算法核心** | 元数据精确匹配 | 文本内容理解 + 技术性能 |
| **关键词策略** | 精简、权重优先 | 全面、密度优先 |
| **描述作用** | 不影响搜索排名（只影响转化率） | **长描述是关键排名因素** |
| **技术指标** | 间接影响 | **Android Vitals 直接影响排名** |
| **A/B 测试** | PPO（Product Page Optimization，需审核） | 商店列表实验（无需审核） |

## App Store 侧要点

### 元数据权重
- **应用名称与副标题**：关键词权重最高，位置金贵，精简优先。
- **应用描述**：不参与搜索排名，只为转化率服务——把它当落地页文案写，不当关键词容器。
- **截图文字**：2025 年 6 月 Apple 算法更新后，**截图中的文字说明开始直接影响搜索排名**——截图文案要当元数据来规划。

### 排行榜规则（权重拆解）

| 排名因素 | 权重 |
|:---|:---|
| 下载速度（Download Velocity） | ~40% |
| 收入（Revenue） | ~30% |
| 用户参与度（Engagement） | ~30% |

含义：冲榜的本质是**短期下载集中度 + 变现 + 留存**三线一起推，单靠买量拉下载只覆盖 40% 的因子。

### A/B 测试
- 走 PPO（Product Page Optimization），**需要审核**，迭代慢——排期要预留审核时间。

## Google Play 侧要点

### 文本理解
- 算法读全文：**长描述是关键**，关键词要全面覆盖、注意密度，但服务于可读性。
- 策略与 App Store 相反：不是"挑最重的几个词"，而是"覆盖整个语义场"。

### Android Vitals 直接影响排名
- 崩溃率、ANR、耗电等技术指标**直接进排名公式**（来源：Google Play Console Help, *Android vitals*）。
- 含义：Google Play 的 ASO 有一半是工程活——性能退化 = 排名退化。

### A/B 测试
- 商店列表实验（Store Listing Experiments）**无需审核**，迭代快——多版本测试策略优先在 Google Play 跑，验证过的素材再搬去 App Store 走 PPO。

## 双端执行差异速查

| 动作 | App Store | Google Play |
|:---|:---|:---|
| 关键词铺设 | 名称/副标题 + 截图文字 | 长描述全文覆盖 |
| 优先优化项 | 元数据 + 转化素材 | 长描述 + 技术性能 |
| 测试节奏 | 慢（需审核） | 快（无需审核），先跑 GP 再迁移 |
| 工程配合 | 低 | 高（Android Vitals 监控进日常） |

## 评分与评论（双端通用）

- 评分评论影响用户信任与转化，双端都要运营。
- 合规方式：App 内提示引导真实评分、邮件跟进活跃用户、回复所有评论。
- ❌ 购买虚假评论 / 评分操纵服务——检测后下架。

## 参考文献

1. Appfigures. (2025). *The Biggest App Store Algorithm Change is Here*
2. AppTweak. (2025). *Key ASO differences between App Store and Google Play*
3. Google Play Console Help. *Monitor your app's technical quality with Android vitals*
