# 出海创业融资 Playbook（播客一手复盘 2026-07）

> 来源：Iris 2026 年多档播客访谈复盘（AFFiNE 2020-2024 融资亲历 + 150+ AI startup 咨询）。
> 口径说明：Pre-A 金额以 Iris 本人口径 **$8M** 为准；两年三轮累计**约 $10M**；
> 口述回忆数字均标注 ≈ 或"播客口径"。反面案例只保留方法论，不涉及可识别人事细节。

---

## 1. 一手融资时间线（增长信号 > pitch 技巧）

| 节点 | 事实（播客口径） |
|---|---|
| 种子轮 | 入营奇绩创坛获得（≈$300K，2021 年） |
| 天使轮 | 耗时约一整年（2021-2022），见/被拒 ≈400 个投资人；期间靠借贷支撑；曾在材料齐备后被临时撕毁 SPA，最终靠加速器介绍的个人天使 close |
| 开源 | 2022-08-03 开源，一周 ≈6,000 star，一个月 ≈1 万 star |
| Pre-A | 开源后约一个月锁定领投、快速 close **$8M**（Iris 本人口径） |
| 累计 | 两年三轮共约 **$10M** |

核心结论：**融资难易的分水岭不是 pitch 技巧，而是可展示的增长信号**（star 增速、
用户曲线、转化率）。同一个团队、同一个产品主线，有无 traction 是"一年 400 拒"与
"一个月 close"的唯一变量。

配套常识（播客口径）：每一轮走到下一轮的公司概率约 ≈10%——预期管理用。

---

## 2. 融资叙事 pivot 框架（三步）

当原有故事融不动时，判断并重构叙事：

1. **查叙事饱和度**：目标叙事下投资人是否已投过多个同类？
   （案例：2022 年时 "notion-like" 故事在国内已被多家占满，不再 strong。）
2. **找赛道公认的技术壁垒**：懂赛道的投资人天然认可的难点
   （案例：协同工具的 OT/CRDT 选型难题 + local-first 与中央存储的矛盾 + privacy 趋势）。
3. **把产品拆成可复用 Infra 讲**，配一句量化叙事。
   范本（注意：这是融资叙事框架，非实测数据）：
   "过去需要 100 个人花三年才能造一个 Figma；现在用这两个 Infra + 1 个产品经理 +
   1 个设计师，就能构建自己的协同应用。"
4. 叠加 traction 佐证（开源 star 增速等），叙事才成立。

加分项：**关键 hire 的行业 credit 也是融资资产**——招到自带社区声望的核心负责人，
能让投资人在技术上 buy in 整个故事。

---

## 3. 投资人排期与"练手"策略

- **地推排程**（无 FA 时的土办法）：提前研究各家 VC 办公地点，把同一片区的投资人
  排进同一个上午/下午；单日上限 ≈6-8 场——要考虑合伙人的体力消耗。
- **FA 教的修正**：不是见得越多越好。先安排**低优先级投资人练手**，磨熟 pitch、
  收集异议，识别出成功率高的对象后再重点突破。
- **认知差定律**：你在自己赛道的认知必须高于投资人——"投资人给你上课 = 拿不到钱；
  你能反向给投资人上课 = 拿到钱概率高"。
- **to 用户而非 to VC**：投资人的钱只是加速器；PMF 之后再融资去 leverage 是更好的
  阶段——确信产品打磨出来了，再拿钱快速放大。
- **找投资人如结婚**：三观不合的钱再好也不要拿（条款卡你、姿态是管教而非支持的
  都不匹配）。理解 VC 结构：投资人背后是 GP/LP，也要"交作业"；基金周期短则耐心不足。

---

## 4. 流程链与法律避坑

标准流程链：
**见投资经理 → 项目上会 → 合伙人聊 → 备材料上会 → 出 TS（定估值/出让比例）→ DD → SPA & SHA 签署**
（部分机构有"银弹"机制：合伙人每年 1-2 次一票通过权。）

避坑清单：

- **TS 没有法律效力**，只是君子承诺，随时可反悔；SPA/SHA 才有法律效力——而且
  实践中连 SPA 也可能被撕（一手亲历）。
- TS 与 DD 之间可要求投资人出**过桥贷款/保证金**，确认钱能落袋。
- **DD 费用 ≈$10K-30K**（委托四大/红圈所），通常从投资款里扣、由创业者承担；
  天使轮 DD ≈1 个月，Pre-A ≈3 个月——现金流要预留。
- 签约必找靠谱律师，重点排查**个人无限连带责任**条款——公司关门后你个人要不要
  cover。
- **坚决不签对赌**："如果你对赌，你就不如去借贷"——借贷风险系数可能更低；最坏
  情况公司关门愿赌服输，但绝不牵连个人无限连带。

---

## 5. 拿钱后的资金与组织纪律（反面教训方法论）

大额融资到账不是终点，而是最危险的时刻。三大崩坏模式：

1. **报复性扩张**：前期吃苦后拿到钱容易过度膨胀——盲目扩招研发、PR 投入过大、
   频繁换血和换方向。真实成本（播客口径）：曾一年内开 ≈10 人又招 ≈10 人，
   N+1 赔偿 + 期权折现极贵。第一笔钱 ≈4 个月烧完的教训同源：乱招不需要的人。
2. **流量最好时不变现**：注意力从用户转向讨好投资人——投资人与用户的需求不同，
   按投资人喜好做产品必踩坑。流量峰值期就是变现窗口。
3. **产研运失衡**：只重研发轻运营，运营收集的用户需求长期进不了产品决策，
   既错失商业化又打击团队。产品/研发/运营必须强耦合：每次发布收上来的反馈要
   反哺产品迭代。

配套组织原则：

- **一家公司只需要一个意志**：单一方向不需要 3-4 个大牛——每个大牛带着个人
  理想进来，各要 headcount、各开业务线，资源撕裂。
- 招人唯一标准：这个阶段是否真的忙不过来；不要按"融资额对应团队规模"招人。
- C-level title 和股权发慢一点；关键合伙人先紧密合作 1-3 个月验证 match，
  再谈期权/股权，并做背调。

---

## EN Summary

**Timeline (self-reported)**: seed via an accelerator (~$300K) -> angel round took a
full year and ~400 investor meetings, survived on loans, even had a signed-ready SPA
torn up -> open-sourced 2022-08-03 (~6K stars in a week, ~10K in a month) -> closed
an $8M Pre-A in about one month (founder's own figure; ~$10M total over three rounds
in two years). The divide is a demonstrable growth signal, never pitch craft.

**Narrative pivot (3 steps)**: check narrative saturation -> identify the sector's
acknowledged technical moat -> reframe the product as reusable infrastructure with one
quantified pitch line, backed by traction. A key hire with community-level credibility
is itself a fundraising asset.

**Sequencing**: batch investors by office district (max ~6-8 meetings/day); warm up on
low-priority investors first, then concentrate on high-probability targets. If an
investor lectures you, you will not get the money; if you can teach them, odds rise.

**Process & legal**: TS is not legally binding — only SPA/SHA are, and even those can
be torn up. Ask for a bridge loan or deposit between TS and DD. DD costs ~$10K-30K,
usually borne by the founder. Have a lawyer screen for unlimited personal liability.
Never sign a valuation bet/ratchet — debt is often lower-risk.

**Post-money discipline**: the three failure modes after a big round are revenge
over-hiring, failing to monetize at peak traffic (pleasing investors instead of users),
and product/eng/ops imbalance. One company needs exactly one will: do not stack 3-4
star hires in one function. Hire only when the current stage genuinely overflows, and
vest titles/equity slowly after a 1-3 month working trial plus reference checks.
