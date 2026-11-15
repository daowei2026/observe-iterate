<!--
virtual_source_id: MA-RUNTIME-METHOD-STATE-COMPLEXITY
runtime_bundle_id: mission-a-project-runtime-bundle-candidate-v0.2.0-integrated-20260904
canonical_successor_repo: daowei2026/feature-refinement-implementation-agent-evolution
canonical_successor_ref: SAME_GIT_TREE_AS_THIS_RUNTIME_RELEASE
canonical_paths:
  - references/local_contract/METHOD_AND_PARAMETER_SURFACE_REFERENCE.md
  - references/local_contract/LOCAL_BUSINESS_CONTRACT_REFINEMENT_METHOD_FULL_REFERENCE.md
v0_2_integration_ids:
  - MA-V02-METHOD-P0-001
  - MA-V02-LC-P0-001
generated_release_candidate: true
manual_edit: forbidden
-->

# Method, Controller, Bounded State and Complexity

## 1. 当前方法不是接口占位符

一个 method position 必须包含：

```text
业务问题；
稳定输入／输出；
不可弱化不变量；
current method id/version；
实际步骤；
failure visibility；
alternatives；
历史／产品影响；
reopen trigger。
```

## 2. 当前方法五态

```text
CURRENT_EXECUTABLE
PROVISIONAL_EXECUTABLE
CALIBRATION_PENDING
SOURCE_BLOCKED
OWNER_SEMANTIC_DECISION
```

区分：

```text
只缺阈值；
缺整个业务判断程序；
缺正式Source；
需要Owner价值取舍。
```

## 3. 可换参数与语义变化

同一问题内可以换：

```text
threshold；
MF anchors；
strictness；
N值（窗口语义不变）；
rule weight；
等价算法。
```

若改变 Feature、scope、life、lookback family、product 或consumer，就必须回合同／地图。

## 4. fuzzy／RulePack

### 适合

```text
连续强弱；
重叠原型；
多因素共同judgement；
gray／compensation；
joint outputs；
可解释数值universe。
```

### 不适合

```text
scope；
identity；
missing/pending；
knowledge maturity；
code error；
same-firing；
lifecycle；
commit；
correction；
hard incompatibility。
```

### 拓扑

分清：

```text
一次推理multi-output；
同一evaluation controller cascade；
跨occurrence feedback；
method-version slow-clock。
```

RulePack只承载明确的业务判断面，不能吞完整Feature。

## 5. 有界状态

每个 state owner 必须有：

```text
create；
continue；
success end；
failure end；
parent end；
current sufficient state；
formal history；
eviction；
rebuild；
growth invariant。
```

运行态应主要随 active business lives 增长，不得因方便随全部历史增长。

## 6. 复杂度

```text
纯计算复杂
  ≠ 必须CEPS；

有独立state owner
  ≠ owner内部必须CEPS子图；

出现Event
  ≠ 已经有业务process；

需要审计
  ≠ 需要独立Book。
```

CEPS用于多个可独立业务动作、分支、采样、反馈、same-cut和commit；简单持续状态可以只用简单Reflex更新。
