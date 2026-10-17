<!--
virtual_source_id: MA-RUNTIME-PROBE-AUDIT
runtime_bundle_id: mission-a-project-runtime-bundle-candidate-v0.2.0-integrated-20260904
canonical_successor_repo: daowei2026/feature-refinement-implementation-agent-evolution
canonical_successor_ref: SAME_GIT_TREE_AS_THIS_RUNTIME_RELEASE
canonical_paths:
  - operations/IMPLEMENTER_PROBE_FINDING_DISPOSITION_AND_CROSS_CUT_RESCAN.md
  - profiles/INDEPENDENT_AUDIT_PROFILE.md
  - operations/AUDIT_VERDICT_AND_ISSUE_BUNDLE.md
v0_2_integration_ids:
  - MA-V02-HARNESS-P0-001
generated_release_candidate: true
manual_edit: forbidden
-->

# Implementer Probe and Independent Audit

## 1. 实现者探针

探针角色没有业务裁定权。它只模拟：

```text
我若真要实现，
仍被迫自行决定什么？
```

至少走一条：

```text
input
→ objective fact
→ Feature
→ method
→ state transition
→ product／consumer。
```

## 2. Finding 分类

```text
BUSINESS_NON_UNIQUE
FEATURE_FORMATION_INCOMPLETE
CURRENT_METHOD_MISSING
IDENTITY_LIFECYCLE_HISTORY_GAP
TIME_KNOWNNESS_CAUSALITY_GAP
BOUNDED_STATE_GAP
REALIZATION_COMPLEXITY_GAP
PRODUCT_CONSUMER_GAP
REPOFACT_REQUIRED
ENGINEERING_FREEDOM
IMPLEMENTER_OVERREACH
```

## 3. Pro 处置

```text
ACCEPT
PARTIAL_ACCEPT
REJECT_ENGINEERING_OVERREACH
RETURN_TO_WORK_MAP
RETURN_TO_LOCAL_CONTRACT
REPOFACT_REQUIRED
OWNER_DECISION_REQUIRED
```

每条必须有正文改动位置、影响面和re-probe要求。

## 4. 横切重扫

accepted finding 判断影响：

```text
当前字段／Action／Feature；
同类Action；
method family；
state/history；
地图子图；
product／consumer；
case；
下游handoff；
Agent method／Harness。
```

## 5. 独立 Auditor

Auditor不看Builder隐藏推理，不直接修artifact。它必须：

```text
独立重建一个Source→Feature；
独立追一个高层claim→下层Feature；
抽查current method；
抽查bounded state；
抽查Book/Life；
抽查source Use proof；
运行至少一个实质anti-gold。
```

只看字段存在或receipt齐全不能PASS。

## 6. 闭合

```text
finding有处置；
正文真实修改；
横切重扫完成；
re-probe通过；
fresh audit通过；
剩余事项只属于工程自由／RepoFact／Owner／Source blocker。
```
