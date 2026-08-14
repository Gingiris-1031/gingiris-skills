---
name: agent-workflow-playbook
description: |
  AI Agent Workflow & Skill Architecture Guide — turn expert work into measurable, reusable agent systems. Covers workflow discovery, skill decomposition, harness design, evaluation, human escalation, observability, cost control, and multi-agent orchestration. Includes a measured marketing-delivery case: 15 people × 3–4 weeks reduced to one strategist + AI in 5 days. By Gingiris.
source: https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/agent-workflow-playbook
tags:
  - agent-workflow
  - ai-agent
  - multi-agent
  - plugin-marketplace
  - workflow-automation
  - evaluation
  - human-in-the-loop
  - agent-orchestration
  - skill-architecture
  - latest
---

# AI Agent Workflow Playbook — 从专家经验到可规模化交付

> 适用于：把研究、营销、运营、分析、内容生产等高认知任务，改造成可测量、可纠错、可复用的 Agent 工作流。

## 先判断：这个任务该不该 Agent 化

只有同时满足以下多数条件才进入自动化：

- 输入和合格输出可以被描述；
- 专家能说清“什么是对、什么是错”；
- 任务重复发生，或交付成本随客户数近似线性增长；
- 关键数据能合法、稳定取得；
- 错误可以在发布、付款、删除或对外发送前被拦截；
- 结果能通过 rubric、样例集或业务指标复核。

如果任务低频、目标持续变化、没有验收口径，先做人工 SOP，不要先搭多 Agent。

## 1. 建立基线，不要直接写 Prompt

选择 10–30 个近期真实任务，记录人工基线：

| 指标 | 定义 |
|---|---|
| 任务成功率 | 首次交付通过验收的任务数 / 总任务数 |
| 一次通过率 | 无返工即通过的任务数 / 总任务数 |
| 周期 | 从收到完整输入到可交付输出的 elapsed time |
| 人工工时 | 研究、制作、复核、返工所花人时 |
| 单次成本 | 模型、工具、数据和人工复核成本之和 |
| 重试率 | 发生工具重试或整段重做的任务占比 |
| 严重错误率 | 错误发布、错误付款、数据泄露等高风险事件占比 |

没有这张基线表，就只能证明 Agent “能跑”，不能证明工作流变好了。

## 2. 从业务链路拆 Skill

先画业务链路，再按可验收结果拆 skill：

```text
需求澄清 → 数据获取 → 证据整理 → 分析 → 产出 → 质检 → 人工批准 → 交付 → 反馈沉淀
```

每个 skill 至少包含：

```yaml
name: competitor-evidence-pack
input_contract:
  required: [product, market, competitors, time_window]
output_contract:
  required: [claims, source_urls, captured_at, confidence, unknowns]
tools:
  allow: [search, fetch]
  deny: [publish, delete, payment]
acceptance:
  - every material claim has a source
  - source capture time is recorded
  - unknown facts are labeled, not guessed
escalate_when:
  - authenticated source is inaccessible
  - sources conflict on a decision-critical fact
```

优先做单一职责 skill。只有当步骤间存在清晰依赖时，才增加 orchestrator。

## 3. Harness：让系统知道边界、记住纠错、持续评测

Prompt 只描述一次交互；harness 管理长期运行环境。至少包含五层：

1. **Context**：品牌、客户、目标、禁区和数据权限；
2. **Skills**：通用技能与客户专属技能分离，按任务选择调用；
3. **Memory**：只沉淀经过确认的偏好、错误和纠正，不把猜测写成事实；
4. **Evaluation**：固定样例集、rubric、回归测试和业务指标；
5. **Observability**：每步输入摘要、工具调用、证据、成本、耗时、重试和最终批准人。

一次失败的正确处理方式不是无限加提示词，而是：记录失败类型 → 判断是数据、工具、推理还是验收问题 → 修改对应层 → 用旧样例集回归。

## 4. 选择编排方式

| 模式 | 适用情况 | 主要风险 |
|---|---|---|
| 顺序 | 后一步严格依赖前一步输出 | 上游错误级联 |
| 并行 | 多个独立来源或方案可同时产生 | 合并冲突、重复成本 |
| 路由 | 不同任务应调用不同专长 | 分类错误 |
| 主管—执行者 | 任务可拆成多个独立子任务 | 主管成为瓶颈 |
| 评审—修订 | 输出有明确 rubric，可迭代改进 | 无界循环、成本失控 |

默认从单 Agent + 多 skill 开始。只有观测数据证明吞吐或专长隔离确实需要并发，才升级为多 Agent。

## 5. 人工介入与权限

以下动作默认需要人工批准：

- 对外发布、群发、私信或代表个人表态；
- 付款、退款、采购和价格承诺；
- 删除、覆盖或批量修改数据；
- 使用未获授权的个人数据；
- 低置信度但会影响客户决策的结论。

连续任务不要重复索取同一授权；记录授权对象、范围和有效期。权限不足时返回缺失项和恢复路径，不要假装完成。

## 6. 上线门槛与回滚

按四阶段推进：

1. **Shadow**：Agent 生成结果但不影响人工交付；
2. **Copilot**：人工选择、修改并批准每次输出；
3. **Guarded automation**：低风险步骤自动执行，高风险动作审批；
4. **Autonomous**：仅用于已稳定通过回归测试、可完整审计且可回滚的边界任务。

每次版本变更比较同一批任务的成功率、周期、人工工时、成本和严重错误率。任一安全指标恶化，回滚到上一稳定版本。

## 真实案例：营销洞察交付从项目制走向产品化

来源：Gingiris 飞书会议纪要《AI agent实践落地困境与规模化尝试分析》，2026-05-10。以下是会议中的经验陈述，不是独立审计或随机对照实验。

### 旧链路

- 运营人员手动浏览小红书约 10 天到 2 周；
- 早期自动化把信息收集压缩到数小时，但报告仍依赖人工思考、迭代和制图；
- 一个高质量 PPT 交付需要约 15 人、3–4 周，难以复制到 100 或 1,000 家客户。

### 新链路

- 将达人筛选、赛道分析、人群识别、内容与投放建议拆成通用 skill 和客户专属 skill；
- 把正例、反例、验收标准、记忆和反馈链路放进 harness；
- 系统先识别任务，再组合调用技能；专家负责策略判断与最终验收；
- 结果、洞察过程和纠错留在系统中，供下一次复用。

### 已报告结果

- 约 **15 人 × 3–4 周** 的 PPT 项目，变为 **1 名策略师 + AI 系统，5 天一次通过**；
- 一份竞品分析与投放建议可在 **不到 1 天** 内交付；
- 会议报告的服务成本相较早期方式下降 **两个数量级**；
- 专业策略师仍需约 **2–3 个月** 学习并迁移到新工作方式，说明专家并没有被“零成本替代”。

### 这个案例真正验证了什么

它支持“把专家判断编码为 skill + harness，可以减少交付周期和边际人工”的判断；它不证明所有行业都能获得相同幅度，也没有披露统一口径下的错误率、模型成本和客户长期留存。因此复用时必须重新建立本团队基线，并补测质量、重试和严重错误率。

## 7 天落地清单

- Day 1：选一个高频任务，收集 10–30 个真实样例和人工基线；
- Day 2：定义输入、输出、rubric、禁区与人工审批点；
- Day 3：拆成 3–7 个单一职责 skill；
- Day 4：接入证据记录、日志、成本与失败分类；
- Day 5：Shadow replay，修复最高频失败；
- Day 6：Copilot 小流量运行，比较人工基线；
- Day 7：决定继续、回滚或只自动化其中一段。

## 最终输出模板

每次工作流评审必须交付：

1. 业务链路和自动化边界；
2. skill 清单与输入/输出 contract；
3. 编排图和工具权限；
4. 评测集、基线和本次结果；
5. 人工介入、失败恢复与回滚方案；
6. 下一轮只改一个变量的实验计划。

---

Built by Gingiris. Historical figures are labeled as reported case evidence; do not present them as guaranteed outcomes.
