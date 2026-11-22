---
name: business-expectation-derivation
description: 在共享 FeatureUnderstandingPackage、当前验收目标和已完成的观察材料基础上，从真实图与图数据中选择正例、负例、误报候选、漏报候选、参数边界和覆盖外场景，并为每个场景冻结可检验的过程预期；目录与名称暂保持不变。
version: 0.2.0
status: draft
---

# 业务预期推导与可观察化

> V0.2 职责调整：本 Skill 不再重复查代码和还原特征处理链。共享特征理解由 `skills/feature-understanding/` 提供；本 Skill 在宽范围观察图和图数据已经准备好以后，负责选择真实场景并定义本轮场景预期。

## 1. 何时使用

在以下条件满足后使用：

- 已有与当前 Feature 代码版本和参数实例一致的 `FeatureUnderstandingPackage`；
- 全量行为统计的 `GlobalProfileGate` 为 `PASS_TO_SCENARIO_REVIEW`；
- 观察材料准备已经交付同版本的 CAEGraph HTML、图数据、位置和字段说明；
- 已有简短、明确的本轮 `CurrentReviewTarget`。

本 Skill 用于：

- 从已经画好的宽范围图和图数据中挑选值得正式分析的真实位置；
- 区分明确正例、明确负例、输出误报候选、潜在漏报候选、参数边界和当前覆盖外场景；
- 为每个场景写出可被支持或反驳的 Feature 过程预期；
- 冻结本轮案例集和预期，交给 `business-evidence-comparison`。

不用于：

- 重新查代码、识别业务对象、状态、事件或中间判断；
- 运行 Feature 或做全量统计；
- 设计、运行或修复 CAEGraph；
- 对场景作正式支持／反证判断；
- 直接调参数、修改实现或改变业务设计。

## 2. 输入

至少需要：

```text
FeatureUnderstandingPackage
CurrentReviewTarget
ObservationMaterialPackage
  ├─ accepted HTML
  ├─ exported graph data
  ├─ symbol/time positions
  ├─ feature and parameter version
  └─ known material limits
ScenarioQuestionQueue（可为空）
CandidateCaseIndex（可为空）
已有预期版本（如适用）
```

### 2.1 `CurrentReviewTarget`

只保留本轮必要信息，不要求再次产出大篇业务目的文档：

```yaml
current_goal:
intended_coverage:
explicit_non_goals:
owner_constraints:
current_acceptance_level:
```

例如，基础 Wall V0 可以限定为：验证清楚的一档流动性对象场景中，是否形成不过度泛滥、可解释的生命周期；本轮不单独判断守住／打穿，也不要求覆盖所有复杂多价位情形。

### 2.2 版本绑定

`ObservationMaterialPackage` 必须与当前 `FeatureUnderstandingPackage`、代码版本和参数实例一致。若不一致，返回观察材料准备，不得从旧图选择新实例案例。

## 3. 预期来源

正式场景预期只使用：

### `OWNER_EXPLICIT`

Owner 明确给出的当前目标、边界或场景判断。

### `BUSINESS_INFERRED`

AI 根据当前目标、业务常识和真实观察材料形成的候选预期，必须写明推导理由、适用条件和反证。

当前实现行为由 `FeatureUnderstandingPackage` 引用，不在本 Skill 中重新抽取，也不能因为代码如此实现就自动成为业务预期。

禁止：

```text
代码这样实现
→ 所以业务上应该这样
→ 图与代码一致
→ 所以设计合理
```

## 4. 强制案例类型

本轮案例集至少考虑以下六类；没有合格案例时要明确写 `NO_CASE_FOUND` 及原因，不能用其他类型顶替。

### 4.1 `CLEAR_POSITIVE`

从图中原始市场过程看，明显属于当前 Feature 承诺表达的场景。

### 4.2 `CLEAR_NEGATIVE`

从原始过程看，明显不应形成该业务对象或事件。

### 4.3 `OUTPUT_FALSE_POSITIVE_CANDIDATE`

Feature 已产生输出，但图上原始过程看起来不像它声称的业务对象或过程。

### 4.4 `POTENTIAL_FALSE_NEGATIVE`

图上原始过程看起来符合当前 intended coverage，但 Feature 未输出、输出过晚，或被切得支离破碎。

### 4.5 `PARAMETER_BOUNDARY`

关键量接近当前参数门槛，适合区分参数值问题、参数关系问题和方法不足。

### 4.6 `OUTSIDE_CURRENT_COVERAGE`

原始过程明显更复杂，当前版本明确不承诺表达。此类案例用于划定边界，不能直接判当前版本失败。

## 5. 渐进式冻结

案例选择允许先探索后冻结：

```text
CANDIDATE
    已在图上发现，尚未确认材料完整

READY_FOR_EXPECTATION
    原始过程和必要字段可读取，可写场景预期

FROZEN_FOR_COMPARISON
    本轮正式交给 Skill 2；不得无痕改写

REVISED
    根据新证据形成新版本，保留修订原因

RETIRED
    位置失效、版本变化或不再属于当前目标
```

证据对照后出现的新想法，不能回写成“原来就有”的预期；应形成新版本。

## 6. 执行步骤

### 步骤 1：核对本轮验收范围

读取 `CurrentReviewTarget`，确认：

- 当前 Feature 成熟阶段；
- 本轮想证明到什么程度；
- 当前承诺覆盖什么；
- 明确不要求什么；
- 全量统计留下哪些场景解释问题。

输出 `ReviewScopeSnapshot`，只引用原输入，不扩写新业务目标。

### 步骤 2：消费共享特征理解

读取 `FeatureUnderstandingPackage` 中：

- 业务对象与身份；
- 状态和合法转换；
- 业务主输出；
- 关键中间判断；
- 参数及运行结果字段；
- 未确认项。

本步骤只确定场景要看哪些合理性单元，不重新查代码或另造实现解释。

### 步骤 3：核对观察材料是否足以选场景

确认图与图数据能支持：

- 原始市场过程阅读；
- 主输出位置；
- 本轮需要的关键中间判断；
- 对象身份与时间关系；
- 正例、反例和潜在漏报位置的区分。

若缺少关键字段或图层，输出 `ObservationGapRequest` 返回观察材料准备；不得靠猜测选择正式案例。

### 步骤 4：浏览宽范围图并建立候选池

结合：

- 图中真实原始过程；
- Feature 输出；
- 中间判断；
- `ScenarioQuestionQueue`；
- `CandidateCaseIndex`；

建立 `CandidateCasePool`。案例必须定位到具体品种、开始时间和结束时间。

不得只从 Feature 已有输出反选案例；潜在漏报必须从原始过程或图中独立寻找。

### 步骤 5：分类和筛选真实案例

按六类案例分类。优先保留：

- 原始过程清楚；
- 能区分两个解释；
- 中间字段完整；
- 对当前 Feature 的关键判断单元有代表性；
- 跨品种、时期或 Session 有复用价值。

同一案例可以关联多个合理性单元，但必须指定本轮主判断目标。

### 步骤 6：为每个案例写出场景过程预期

每个案例至少写：

```text
原始市场过程的当前描述
当前 intended coverage 是否适用
预期 Feature 发生—发展—结束过程
关键中间判断应怎样变化
哪些结果构成支持
哪些结果构成反证
哪些情况只能判为未决
当前不要求判断什么
```

预期必须绑定具体案例，不能只写“该 Feature 应合理”。

### 步骤 7：冻结案例集与预期

形成：

- `CaseReviewSet`；
- `ScenarioExpectationSet`；
- 与现有 Skill 2 兼容的 `FrozenExpectationSet`；
- `ObservationGapRequests`；
- `OpenQuestions`。

## 7. 输出合同

### 7.1 `CaseReviewSet`

```yaml
case_set_id:
version:
feature_ref:
parameter_version:
observation_material_ref:
review_target_ref:
cases:
  - case_id:
    status: CANDIDATE | READY_FOR_EXPECTATION | FROZEN_FOR_COMPARISON | REVISED | RETIRED
    case_type: CLEAR_POSITIVE | CLEAR_NEGATIVE | OUTPUT_FALSE_POSITIVE_CANDIDATE | POTENTIAL_FALSE_NEGATIVE | PARAMETER_BOUNDARY | OUTSIDE_CURRENT_COVERAGE
    symbol:
    start_time:
    end_time:
    related_reasonableness_units: []
    primary_judgment_target:
    selection_basis:
    raw_market_description:
    output_presence:
    required_intermediate_fields: []
    source_refs: []
```

### 7.2 `ScenarioExpectationSet`

```yaml
expectation_id:
version:
status: FROZEN_FOR_COMPARISON | REVISED | RETIRED
case_id:
statement:
origin: OWNER_EXPLICIT | BUSINESS_INFERRED
source_ref:
applicable_conditions:
non_applicable_conditions:
expected_feature_process:
expected_intermediate_decisions:
falsifier_or_counterevidence:
ambiguous_conditions:
explicit_non_goals:
evidence_needed:
known_unknowns:
confidence:
owner_decision_required:
```

### 7.3 `FrozenExpectationSet`

为保持现有 Skill 2／3 兼容，汇总本轮 `FROZEN_FOR_COMPARISON` 的场景预期及其版本、案例和材料引用。

### 7.4 `ObservationGapRequest`

```yaml
gap_id:
case_or_unit_ref:
missing_field_or_view:
why_needed:
return_to: OBSERVATION_MATERIAL_PREPARATION
```

## 8. 完成条件

- 图和图数据绑定当前有效 Feature 版本与参数实例；
- 正式案例均来自已准备的真实观察材料；
- 至少明确处理正例、负例、误报候选和潜在漏报的覆盖情况；
- 每个案例有具体位置、选择理由、主判断目标和过程预期；
- 当前覆盖外案例没有被当作当前版本失败；
- 所有正式预期已冻结并可交给 Skill 2；
- 材料缺口已回流，不靠猜测补齐。

## 9. 强制约束

1. 不重复 `FeatureUnderstandingPackage` 已完成的代码和处理链理解。
2. 不在观察材料准备完成前凭空构造正式场景。
3. 不只从已有 Feature 输出选择案例，必须考虑潜在漏报。
4. 不把实现行为写成天然业务预期。
5. 不把 AI 推导写成 Owner 已确认需求。
6. 不把当前覆盖外复杂场景直接写成设计反证。
7. 不在正式对照中无痕修改被冻结案例或预期。
8. 不在尚未完成证据对照与诊断时直接建议调参数。
