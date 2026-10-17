<!--
virtual_source_id: MA-RUNTIME-CASE-ROUTER
runtime_bundle_id: mission-a-project-runtime-bundle-candidate-v0.2.0-integrated-20260904
canonical_successor_repo: daowei2026/feature-refinement-implementation-agent-evolution
canonical_successor_ref: SAME_GIT_TREE_AS_THIS_RUNTIME_RELEASE
canonical_paths:
  - governance/COMMON_CORE_CASE_AND_BINDER_BOUNDARY.md
  - cases/eaw/EAW_CASE_PROFILE.md
  - cases/eaw/EAW_WALKTHROUGHS_FORMAL_CONSEQUENCES_AND_SOURCE_ROUTER.md
v0_2_integration_ids:

generated_release_candidate: true
manual_edit: forbidden
-->

# Case Router and NonClaims

## 1. Common core

只认识：

```text
scope；
Source／Fact／Feature；
identity／business life；
event／material／state；
Action／method；
product／consumer；
history／correction；
lookback／sufficient state；
complexity disposition；
MapRevision；
probe／audit／maintenance。
```

## 2. Case profile

具体用例才认识：

```text
专名；
固定分包；
当前频率；
repo路径；
现有Taskpack；
特定平台资产；
已有Gold／anti-gold。
```

EAW 是 gold／pressure test，不是跨用例 core。非 EAW 用例可以更简单，不得机械物化 DSU、CEPS、IntegrationWave 或多仓结构。

## 3. 使用case的方式

Case 用于：

```text
说明方法如何落地；
提供正例、near-miss和历史失败；
触发深source；
检验common core是否过拟合。
```

Case 不能：

```text
替代current task authority；
把历史EAW决定复制到新用例；
用代码现状定义业务应然；
证明cross-use-case已经通过。
```

## 4. formal NonClaims

本 runtime bundle 不声称：

```text
所有Feature都需要独立Book；
所有用例都需要DSU；
所有事件过程都需要CEPS；
所有连续判断都要fuzzy；
固定窗口总是不对；
provisional v0可替Owner；
当前U2/U3已经被修；
Mission B/C已兼容；
本bundle已validated runnable。
```
