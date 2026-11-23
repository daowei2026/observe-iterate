# 特征全量行为统计与高置信不合理现象发现｜字段级输入输出

## 1. 输入

### 1.1 `FeatureUnderstandingPackage`

必须来自与本轮运行结果一致的 Feature 代码版本；允许 `PARTIAL`，但缺口不得影响本轮拟统计对象和高置信发现判断。

### 1.2 `FeatureRunResultBinding`

```yaml
feature_name:
code_version:
parameter_instance_ref:
parameter_version:
run_id:
data_scope:
  symbols:
  start_time:
  end_time:
  calendar:
  sessions:
artifact_refs: []
run_result_tables: []
known_data_limits: []
```

### 1.3 `CurrentReviewTarget`

```yaml
current_goal:
explicit_non_goals: []
owner_raised_candidates: []
required_regression_findings: []
```

### 1.4 `StratificationPlan`

```yaml
strata:
  - stratum_id:
    dimension: SYMBOL | PERIOD | SESSION | ACTIVITY_REGIME | OTHER
    rule:
    source_fields:
```

没有可靠分层字段时，不能凭名称猜测环境类别。

## 2. 中间产物

### 2.1 `StatisticsInputReadiness`

```yaml
binding_match:
  code_version: MATCH | MISMATCH | UNCONFIRMED
  parameter_version: MATCH | MISMATCH | UNCONFIRMED
  data_scope: CONFIRMED | PARTIAL | UNCONFIRMED
core_object_keys: []
core_time_keys: []
available_items: []
partial_items: []
not_exposed_items: []
data_quality_findings: []
readiness_status: READY | PARTIAL | BLOCKED
```

### 2.2 `StatisticDefinition`

每项统计必须先登记：

```yaml
statistic_id:
name:
business_item_ref:
count_unit:
object_group_key:
time_basis:
denominator:
deduplication_rule:
same_tick_rule:
strata:
source_fields:
```

### 2.3 `GlobalBehaviorProfile`

```yaml
profile_id:
feature_ref:
run_binding:
statistics_definitions: []
candidate_profile: []
object_profile: []
current_object_profile: []
event_profile: []
state_occupancy_profile: []
transition_profile: []
lifecycle_profile: []
conversion_profile: []
branch_reachability_profile: []
density_profile: []
reason_profile: []
reference_integrity_profile: []
same_tick_order_profile: []
cross_symbol_profile: []
cross_period_profile: []
cross_session_profile: []
limits: []
```

单项 profile 记录至少包括：

```yaml
statistic_id:
stratum_id:
value_or_distribution:
sample_size:
denominator_value:
source_location:
notes:
```

### 2.4 `FindingDiscoverySummary`

```yaml
summary_id:
feature_ref:
run_binding:
business_surfaces_reviewed:
  - surface:
    why_applicable:
    evidence_refs: []
    candidate_finding_refs: []
owner_raised_candidates:
  - finding_id:
    assessment_status: PENDING | PROMOTED | NOT_PROMOTED | BLOCKED_BY_EVIDENCE
    evidence_refs: []
high_confidence_candidate_refs: []
observations_not_promoted:
  - observation_id:
    observation:
    why_not_promoted:
    revisit_condition:
remaining_unreviewed_surfaces:
  - surface:
    why_not_reviewed:
    effect_on_current_gate:
why_current_discovery_pass_is_sufficient:
queue_snapshot_id:
```

该产物不是固定检查表。`business_surfaces_reviewed` 由当前 Feature 的对象、生命周期、输出合同、转化链和 ReviewTarget 推导。

### 2.5 `GlobalFindingCandidate`

```yaml
finding_id:
finding_type: HIGH_CONFIDENCE_REASONABLENESS_CANDIDATE | STRUCTURAL_FINDING_CANDIDATE
candidate_origin: EXECUTOR_DISCOVERY | OWNER_RAISED | REGRESSION
feature_ref:
run_binding:
reasonableness_unit_ref:
business_object_ref:
observation:
candidate_basis:
why_high_confidence:
confidence_limits:
contract_or_business_semantics_ref:
evidence_scope:
repeat_count:
affected_count:
affected_ratio:
representative_locations: []
alternative_non_error_explanations: []
current_confidence:
must_assess_before_release: true | false
next_route: BUSINESS_DISCREPANCY_DIAGNOSIS
diagnosis_input_adapter_ref:
```

`why_high_confidence` 说明为什么该现象已足以进入诊断；它不替代 D 中的责任逻辑定位。Owner 提出的候选可以先以 `current_confidence: OWNER_CONCERN` 登记，执行者仍需核其口径和证据，不能预设根因或最终结论。

### 2.6 `ObservationNotPromoted`

```yaml
observation_id:
feature_ref:
run_binding:
observation:
evidence_refs: []
why_not_promoted:
revisit_condition:
```

### 2.7 `CandidateCaseIndex`

```yaml
case_candidate_id:
source_finding_id:
symbol:
start_time:
end_time:
object_ids: []
related_events: []
selection_reason:
required_fields: []
```

该索引用于 finding 复现和责任逻辑定位，不自动成为场景观察任务。

### 2.8 `DiagnosisInputAdapter`

```yaml
adapter_id:
finding_id:
frozen_expectation:
  expectation_id:
  version:
  statement:
  origin:
  applicable_conditions:
  falsifier_or_counterevidence:
evidence_comparison_package:
  comparison_id:
  scenario_id: GLOBAL_PROFILE
  data_binding:
  time_basis:
  parameter_version:
  evidence_items: []
  judgment:
business_intent_ref:
processing_chain_ref:
relevant_code_or_requirement_refs: []
data_binding_and_time_basis:
```

`frozen_expectation.statement` 可以引用明确结构不变量、既有业务规则或已冻结预期；不得把统计模式临时改写成天然业务要求。

## 3. 最终输出

```yaml
FeatureGlobalBehaviorProfilingResult:
  statistics_input_readiness:
  global_behavior_profile:
  finding_discovery_summary:
  global_finding_candidates: []
  observations_not_promoted: []
  candidate_case_index: []
  diagnosis_input_adapters: []
  gate:
    status: BLOCKED | DIAGNOSIS_REQUIRED | RERUN_REQUIRED | PASS_TO_SCENARIO_REVIEW
    reasons: []
    valid_profile_ref:
    queue_snapshot_ref:
    next_action:
```

## 4. Gate 约束

### `BLOCKED`

- 核心版本或参数实例不一致；
- 无法识别对象或事件键；
- 运行结果缺失导致主要剖面不成立。

### `DIAGNOSIS_REQUIRED`

- 存在尚未进入／完成偏差诊断的高置信候选；
- Owner 指定且 `must_assess_before_release=true` 的候选尚无判断；
- 发现工作在第一个候选处提前停止，尚未形成结果绑定的队列快照。

### `RERUN_REQUIRED`

参数、实现、设计或数据修正已改变 Feature 行为，旧剖面不得继续作为有效结果。

### `PASS_TO_SCENARIO_REVIEW`

- 当前剖面绑定最新运行结果；
- 已形成 `FindingDiscoverySummary` 和队列快照；
- 已确认问题均已处理并复验，或本轮不存在；
- Owner 指定候选已有判断；
- 剩余观察不足以升级或超出当前 ReviewTarget；
- 不表示 Feature 已被全面证明合理，也不自动启动另一套 Workflow。
