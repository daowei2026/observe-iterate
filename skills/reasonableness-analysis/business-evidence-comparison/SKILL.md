---
name: business-evidence-comparison
description: 对 Skill 1 已冻结的真实案例，比较原始市场过程、场景预期中的 Feature 过程与当前 Feature 实际过程，定位第一次业务分歧并形成可交给偏差诊断的证据包；目录与名称暂保持不变。
version: 0.2.0
status: draft
---

# 业务预期—真实证据对照

> V0.2 职责调整：本 Skill 不再负责从宽范围图中挑场景，也不做全量行为统计。它只消费 Skill 1 已冻结的真实案例和预期，进行逐场景、逐过程证据对照。

## 1. 何时使用

在以下条件满足后使用：

- `CaseReviewSet` 中存在 `FROZEN_FOR_COMPARISON` 案例；
- 已有与案例绑定的 `ScenarioExpectationSet`／`FrozenExpectationSet`；
- `ObservationMaterialPackage` 与当前 Feature 版本、参数实例一致；
- `FeatureUnderstandingPackage` 可提供对象、状态、事件、中间判断和处理关系；
- 全量行为统计已经通过本轮 Gate。

本 Skill 用于：

- 还原案例中的原始市场过程；
- 还原预期 Feature 发生—发展—结束过程；
- 还原当前 Feature 实际过程及关键中间判断；
- 对齐三条过程链，识别第一次业务分歧；
- 形成支持、反证、缺失、歧义、待确认和不适用证据；
- 形成可交给现有 `business-discrepancy-diagnosis` 的 `EvidenceComparisonPackage` 与疑点队列。

本 Skill 不负责：

- 重新选择场景；
- 重新查代码或定义 Feature 对象；
- 做全量数量、密度和生命周期统计；
- 查明根因；
- 直接调参、改实现或决定业务设计取舍。

## 2. 输入

至少需要：

```text
FeatureUnderstandingPackage
CurrentReviewTarget
CaseReviewSet
ScenarioExpectationSet / FrozenExpectationSet
ObservationMaterialPackage
GlobalBehaviorProfile（只读引用，可为空）
```

`ObservationMaterialPackage` 至少应包含：

```text
accepted HTML
exported graph data
case positions
feature code version
parameter instance/version
field dictionary
known material limits
```

若图、数据和 Feature 版本不一致，必须停止正式对照。

## 3. 核心对照结构

每个案例同时保留三条过程链：

### 3.1 `RawMarketProcess`

从原始行情和必要上游材料还原：

```text
真实看到了什么
按什么时间顺序发生
对象或现象怎样持续、变化和结束
```

它不是 Feature 输出的复述。

### 3.2 `ExpectedFeatureProcess`

来自被冻结场景预期：

```text
当前 intended coverage 是否适用
哪些中间判断应发生
哪些主输出应出现
合理的发生、更新、状态转换和结束顺序是什么
```

### 3.3 `ObservedFeatureProcess`

根据图和图数据还原：

```text
实际候选／中间判断
实际对象身份和状态
实际 occurrence
actualTime / confirmTime
实际结束或未结束
```

## 4. 证据状态

### `SUPPORTS`

在适用条件成立、材料有效且替代解释未占主导时，实际过程与预期一致。

### `COUNTERS`

在适用条件成立、材料充分且明显数据／实现事实缺口已排除时，实际过程与预期冲突。

### `MISSING`

缺少字段、图层、时间范围、对象身份或中间判断，无法完成当前对照。

### `AMBIGUOUS`

同一证据可由多个合理解释说明，尚不能区分。

### `NOT_APPLICABLE`

案例不满足当前预期的适用条件，或属于 `OUTSIDE_CURRENT_COVERAGE`。

### `PENDING`

过程尚未确认结束，或 confirmTime 尚未到达。

必须遵守：

```text
没有 Event ≠ 反证
ValidEmpty ≠ DataUnavailable
InsufficientHistory ≠ 当前 Behavior 很差
Pending ≠ Negative
```

## 5. 执行步骤

### 步骤 1：核对案例、预期和材料绑定

至少核对：

- case_id、品种、开始／结束时间；
- Feature 代码版本和参数实例；
- 图与导出数据是否来自同一次有效运行；
- 对象身份、交易日历、Session 和时间粒度；
- actualTime、observedTime、confirmTime；
- 缺失、重复、乱序、修订和材料限制。

输出 `ScenarioEvidencePreflight`。

### 步骤 2：还原原始市场过程

按案例位置，从图和图数据中记录：

- 原始价格、挂单、成交或其他当前业务材料；
- 关键变化点；
- 现象持续、增强、衰弱、迁移或结束；
- 人工／AI 当前为何把它视为正例、负例、误报候选、漏报候选、参数边界或覆盖外场景。

不得先用 Feature 输出决定原始过程是什么。

### 步骤 3：展开预期 Feature 过程

读取该案例被冻结预期，形成有序步骤：

```text
输入条件
→ 关键中间判断
→ 对象创建／不创建
→ 状态或身份更新
→ 结束／不结束
```

对负例和漏报候选，也必须写清“不应发生什么”或“本应发生什么”。

### 步骤 4：还原实际 Feature 过程

依据 `FeatureUnderstandingPackage` 和观察数据，逐步记录：

- 上游输入；
- 当前处理阶段输入；
- 关键中间判断；
- 对象身份与状态；
- 业务主输出 occurrence；
- actualTime／confirmTime；
- 参数与版本；
- 材料未暴露的环节。

只记录真实可取得证据，不从代码规则反推本次运行值。

### 步骤 5：按时间、对象和处理阶段对齐三条过程

对每个预期步骤回答：

```text
原始过程是否满足前提？
中间判断是否如预期发生？
对象身份是否保持？
状态和 occurrence 是否在合理位置出现？
哪一步首次出现不一致？
后续差异只是上游分歧的传播，还是新的独立分歧？
```

输出 `EarliestBusinessDivergence`。

### 步骤 6：形成场景证据判断

对每个预期分别给出：

- 支持证据；
- 反证证据；
- 缺失证据；
- 歧义证据；
- 不适用条件；
- 当前适用范围；
- 当前判断成熟度。

不得用一个总分替代多项独立业务判断。

### 步骤 7：跨案例归并重复模式

将多个案例中相同的第一次分歧按：

- 合理性单元；
- 对象／状态／事件；
- 品种／时期／Session；
- 预期来源；

归并为重复疑点候选。

本步骤只说明“重复出现”，不查根因，不把统计相关性宣布为机制。

### 步骤 8：生成进入 Skill 3 的疑点

只有以下问题进入 `business-discrepancy-diagnosis`：

- 属于当前 intended coverage；
- 业务影响明确；
- 在一个或多个清楚场景中重复或后果严重；
- 不能由观察材料缺口直接解释；
- 当前处理链中有可追踪阶段；
- 区分原因有现实价值。

材料不足的问题进入 `ObservationGapRequest`；覆盖外案例不进入当前 Feature 失败队列。

## 6. 输出合同

### 6.1 `ScenarioProcessCasebook`

```yaml
casebook_id:
feature_ref:
parameter_version:
observation_material_ref:
cases:
  - case_id:
    case_type:
    raw_market_process: []
    expected_feature_process: []
    observed_feature_process: []
    process_alignment: []
    earliest_business_divergence:
      unit_ref:
      time:
      expected:
      observed:
    material_limits: []
    current_judgment:
```

### 6.2 `EvidenceComparisonPackage`

为保持现有 Skill 3 兼容，继续输出：

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

### 6.3 `ScenarioFindingCandidate`

```yaml
finding_id:
discovery_route: SCENARIO_PROCESS_REVIEW
unit_ref:
case_ids: []
expectation_refs: []
expected_behavior:
observed_behavior:
earliest_business_divergence:
repeatability:
business_impact:
evidence_comparison_refs: []
next_route: BUSINESS_DISCREPANCY_DIAGNOSIS
```

### 6.4 `ObservationGapRequest`

```yaml
gap_id:
case_id:
missing_field_or_view:
why_needed:
return_to: OBSERVATION_MATERIAL_PREPARATION
```

### 6.5 `EvidenceInducedCandidate`

当真实场景暴露了原预期未覆盖的新模式时，记录新候选预期并交回 Skill 1；不得改写当前冻结版本。

### 6.6 `DiscrepancyQueue`

继续保留现有输出名，内容只包含已满足步骤 8 条件的 `ScenarioFindingCandidate`，供 Skill 3 使用。

## 7. 完成条件

- 所有冻结案例均已完成材料预检；
- 每个可分析案例都有原始、预期、实际三条过程链；
- 第一次业务分歧已定位，或明确说明为何无法定位；
- 正例、负例、误报候选、漏报候选和边界例的实际覆盖已记录；
- 覆盖外案例没有被误判为当前 Feature 失败；
- 材料缺口、场景疑点和新预期候选已分流；
- 进入 Skill 3 的疑点都有兼容 `EvidenceComparisonPackage`。

## 8. 强制约束

1. 不在本 Skill 中重新选择场景。
2. 不重复做全量行为统计。
3. 不把 Feature 输出当作原始市场过程本身。
4. 不把实现符合性当作业务合理性。
5. 不把材料缺口当作业务反证。
6. 不把缺失、有效空、样本不足和待确认混为一类。
7. 不将同源证据机械累计成多份独立支持。
8. 不因单一正例或反例确认通用规律。
9. 不查根因、不调参数、不修改实现或需求。
10. 不把当前覆盖外复杂场景直接进入设计失败队列。
