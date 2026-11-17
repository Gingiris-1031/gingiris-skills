# Topic Map 与 Page Owner 运营规范

> 在新内容规划、站点结构改造、工具页优化、蚇食排查或“每周写 N 篇”任务时读取。

## 决策顺序

1. **Entity boundary**：记录网站是什么、能完成什么、服务谁、明确不做什么。
2. **Search ICP**：记录搜索者、要完成的任务、主意图、证据偏好和合理 CTA。
3. **Topic Map**：合并 GSC/SERP/关键词工具/竞品等外部需求，与用户访谈/工单/售前/站内搜索/流失等内部需求。
4. **Topic scoring**：按品牌相关度、业务价值、词簇需求和当前可竞争性排序。Volume/KD/TP 未当前核验就标“待验证”。
5. **Keyword Cluster**：按主要任务/搜索意图分组，不按字面相似度机械分组。
6. **Unique Page Owner**：每个主意图词簇只指定一个主 canonical URL。先查旧页，再决定优化、合并、重定向、新建或不做。
7. **SERP validation**：对比目标市场 Top 10/20 的 URL 重合、Content Type、Format、Angle 与必要内容组件。
8. **Last-task completion**：页面必须让搜索者完成任务。工具意图优先可操作功能和结果；商业意图提供选择依据、局限和下一步；信息意图提供可执行答案。

## 新页门禁

新建 URL 前必须回答：

- 现有 Page Owner 为什么不能承接？
- SERP 是否把该需求视为独立意图？
- 新页能否提供不同功能、输入/输出、证据或决策结果，而不是仅替换关键词？
- canonical、内链、导航、sitemap 和 CTA 如何进入既有信息架构？

任一答案不清楚，默认优化旧 Page Owner，不新建。

## 词簇运营台账

| Topic | Search ICP / task | Intent | Top keyword | Secondary / questions | Source/date | Volume/KD/TP status | Page Owner | SERP type/format/angle | Current stage | CTA event | 14/30-day result |
|---|---|---|---|---|---|---|---|---|---|---|---|

Current stage 必须从下列取值，不跳步声称：

`draft` → `landed` → `committed` → `deployed` → `live-verified` → `in-sitemap` → `submitted` → `crawled` → `in-gsc` → `impressions` → `clicks` → `conversion` / `verified-ai-citation`

## 内链与页面层级

- 频道/集合页 → 相关 Page Owner。
- 支撑内容 → 对应 Money Page / Tool / Service Page。
- 同一用户任务中的相关页面水平互链。
- anchor 描述目标任务，不用“点击这里”或强制重复 exact match。
- 不设每段内链数量硬阈值；以相关性、可发现性和可用性验收。

## 周度复盘

用 GSC `dataState=final` 比较最近完整 7 天与前 7 天，且分开品牌/非品牌：

1. 整站与目录级的页面数、新增非品牌查询、曝光、点击、CTR 和排名。
2. Page Owner 的 Top 10/20/100、高曝光低 CTR、查询意图偏移与蚇食。
3. 真实产品/转化事件：工具生成、拷贝、下载、注册、联系、购买等。
4. GEO 单独记录品牌提及、精确来源 URL 和 referral；“有回答”不等于“引用我们”。

样本少于 10 次曝光、单日波动或未 final 数据不触发标题/内容改写。优化优先级是：技术故障 → 索引阻塞 → 排名 4–20 的意图/snippet → 内链/页面任务/CTA → 内容缺口。

## 方法来源

该框架吸收了 [Bysocket SaaS SEO Playbook](https://bysocket.com/saas-seo-playbook/) 的 Entity、搜索 ICP、Topic Map、Keyword-to-Page、Last-Click、工具页和目录级复盘思路。这些属于实践方法，不是 Google 官方排名公式；因果声称需另行验证。
