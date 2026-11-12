---
name: business-evidence-comparison
description: 将已标明来源和版本的业务预期绑定到真实数据、代码输出和局部场景，形成支持、反证、缺失与未决证据，并产出条件化效果对照；适用于输入、处理中间结果和最终输出的合理性分析。
version: 0.1.0
status: draft
---

# 业务预期—真实证据对照

## 1. 何时使用

在以下任务中使用：

- 已有最小可检验预期，准备查看真实数据；
- 需要判断输入、处理中间结果或输出是否符合预期；
- 需要比较方案 A／B、改动前／后或不同参数组；
- 需要从图、表、JSON、运行记录中提取可支持或反驳业务命题的证据；
- 需要找出哪些局部场景值得进入偏差诊断。

本 Skill 不负责：

- 无来源地发明业务预期；
- 仅凭数据相关性宣布业务机制；
- 在未查数据质量前把异常归因于算法；
- 直接决定真正的业务目标取舍。

---

## 2. 核心目标

对每一条冻结预期，形成：

```text
支持证据
反证证据
缺失证据
歧义证据
适用范围
不适用范围
当前判断成熟度
```

不追求“把所有数据都看完”，而追求：

> 用尽可能少但具有区分力的真实场景，判断当前预期能否成立、在哪些条件下成立，以及下一步最值得查什么。

---

## 3. 开始对照前必须拿到的输入

至少需要：

```text
FrozenExpectationSet
BusinessIntent
JudgmentTarget
DataBinding
FieldDictionary
TimeBasis
ParameterOrVersionInfo
EvidenceSources
```

若缺少字段或实现事实，先走事实准备轨道，不要急于判定业务合理性。

---

## 4. 输入证据仍需做三层检查

| 层次 | 具体问题 | 输出 |
|---|---|---|
| 输入有效性 | 是否缺失、错位、重复、版本错误、时间或参数错误 | `DataValidityFinding` |
| 输入业务合理性 | 输入是否表达它声称的业务概念 | `InputMeaningFinding` |
| 输入对当前目的的适用性 | 输入即使正确，是否足以回答本次问题 | `PurposeSuitabilityFinding` |

对照时可以出现：

```text
有效但不适用
业务上合理但样本不足
数据完整但时间语义不支持当前结论
局部适用而非全局适用
```

---

## 5. 预期与证据可以迭代，但必须版本化

### 5.1 允许先看小样本

在预期处于 `WORKING` 状态时，可以看少量样本，用于：

- 发现场景；
- 理解数据形状；
- 补充适用条件；
- 判断需要哪些图表和字段。

这叫**探索性观察**，不能直接作为正式效果结论。

### 5.2 正式对照只绑定被冻结版本

每条证据必须记录：

```text
expectation_id
expectation_version
as_of_time
data_version
code_or_config_version
```

### 5.3 新证据诱发新预期

若数据中出现新模式：

- 记录为 `EvidenceInducedCandidate`；
- 交回 `business-expectation-derivation`；
- 不回写到当前被冻结预期；
- 新预期进入下一轮对照。

---

## 6. 证据状态

### 6.1 `SUPPORTS`

在预期适用条件成立、数据有效且替代解释未占主导时，证据与预期一致。

### 6.2 `COUNTERS`

在预期适用条件成立、证据充分且排除了明显数据／实现问题后，观察结果与预期冲突。

### 6.3 `MISSING`

无法取得预期需要的字段、时间范围、样本或中间结果。

### 6.4 `AMBIGUOUS`

同一证据可被多个合理解释说明，尚不能区分。

### 6.5 `NOT_APPLICABLE`

该场景不满足预期的适用条件。

### 6.6 `PENDING`

过程尚未确认结束，或 confirmTime 尚未到达。

必须遵守：

```text
没有 Event ≠ 反证
ValidEmpty ≠ DataUnavailable
InsufficientHistory ≠ 当前 Behavior 很差
Pending ≠ Negative
```

---

## 7. 执行步骤

### 步骤 1：核对数据与时间基础

至少核对：

- 对象范围和 DataBinding；
- 交易日历、Session、时间粒度；
- actualTime、observedTime、confirmTime；
- 参数组、配置和版本；
- 缺失、重复、乱序、修订；
- 数据读取和转换链。

输出 `EvidencePreflight`。

### 步骤 2：建立证据映射

对每条预期回答：

- 哪些字段直接支持判断？
- 哪些中间处理结果必须保留？
- 哪些是同源证据，不能重复计票？
- 哪些结果只能说明实现行为，不能说明业务合理性？
- 哪些证据需要 actual／confirm 双时间？

### 步骤 3：选择具有区分力的场景

优先选择：

- 预期最容易成立的正例；
- 预期最容易失败的反例；
- 两种解释给出不同预测的对照例；
- 边界场景；
- 高业务损失风险场景；
- 不同参数组或处理阶段结果明显不同的场景。

不建议只抽随机样本或只看极端值。

### 步骤 4：逐位置建立证据链

每个位置至少保留：

```text
原始输入
上游 Feature
当前处理阶段输入
中间状态／选择结果
当前处理阶段输出
actualTime / confirmTime
参数与版本
后续效果（如适用）
```

### 步骤 5：按预期逐条判断

禁止用一个总分替代多项独立业务判断。

每条预期分别给出：

- 支持位置；
- 反证位置；
- 缺失位置；
- 未决位置；
- 条件变化；
- 当前适用范围。

### 步骤 6：建立条件化效果对照

效果对照优先按场景和条件分层，而不是全局平均。

例如：

```text
有原始候选可覆盖的小转折
无原始候选的小转折
多参数重复局部
高频密集但价格变化弱的局部
交易小节结束附近
```

每一层分别看：

- 覆盖保留；
- 冗余减少；
- 时间偏差；
- 确认延迟；
- 信息损失；
- 样本充分性。

### 步骤 7：记录新发现但不改写当前预期

创建 `EvidenceInducedCandidate`，描述：

- 观察到什么；
- 为什么原预期没有覆盖；
- 可能的新适用条件；
- 下一轮怎样验证。

### 步骤 8：选择进入诊断的问题

只有以下问题进入 `business-discrepancy-diagnosis`：

- 业务影响大；
- 多次重复；
- 不能由数据质量直接解释；
- 当前处理链中有明确可追踪阶段；
- 区分原因有现实价值。

---

## 8. 输出合同

### 8.1 `EvidenceComparisonPackage`

```yaml
comparison_id:
business_intent:
expectation_id:
expectation_version:
scenario_id:
data_binding:
time_basis:
parameter_version:
evidence_items:
  - evidence_id:
    source:
    location:
    actual_time:
    confirm_time:
    evidence_status: SUPPORTS | COUNTERS | MISSING | AMBIGUOUS | NOT_APPLICABLE | PENDING
    observation:
    interpretation:
    alternative_explanations:
    data_quality:
judgment:
applicability_boundary:
confidence:
next_action:
```

### 8.2 `InputAssessment`

必须分开报告三层输入检查。

### 8.3 `ScenarioEffectTable`

按业务场景条件组织，不默认给全局总分。

### 8.4 `EvidenceInducedCandidates`

交回预期推导 Skill。

### 8.5 `DiscrepancyQueue`

只包含值得继续定位的问题。

---

## 9. 高频标准化示例

### 9.1 对照链

```text
大小转折
→ 各参数组原始高频
→ 分段选择结果 select
→ 选择应用后的高频
→ 紧密组更新／确认
→ merged
```

参数选择和应用选择结果必须分开观察；Apply 阶段只放行被选方案，不应被误解为再次评价。

### 9.2 可观察量候选

- 有候选可覆盖的小转折中，最终输出仍能表达的比例；
- 一个局部被多参数重复表达的程度；
- `select` 造成的信息变化；
- CloseGroup／merge 造成的信息变化；
- 代表事件相对实际转折点和确认点的时间距离；
- 不同活动环境下上述结果的差异。

这些量只有在“覆盖”“重复”“表达”得到业务定义后才能正式统计。

### 9.3 典型证据状态

```text
原始高频不存在
    → 不能直接归咎 merged

参数组未被选中
    → 检查历史分段关系约束及生效范围

参数已选中但事件未进入 CloseGroup
    → 检查临近、超时、Session 和同刻法律

进入 CloseGroup 但最终代表为另一事件
    → 比较代表性规则与当前业务目的

组尚未确认结束
    → PENDING，不是输出缺失
```

---

## 10. 强制约束

1. 不允许证据诱发的新预期无痕回写旧预期。
2. 不把数据质量问题当作业务反证。
3. 不把实现符合性当作业务合理性。
4. 不把缺失、有效空、样本不足、待确认混为一类。
5. 不只看最终输出，必须保留必要中间结果。
6. 不将同源证据机械累计成多份独立支持。
7. 不用全局平均掩盖条件差异。
8. 不在“覆盖”等业务词未定义时直接输出貌似精确的效果数字。
9. 不因单一正例或反例确认通用规律。
