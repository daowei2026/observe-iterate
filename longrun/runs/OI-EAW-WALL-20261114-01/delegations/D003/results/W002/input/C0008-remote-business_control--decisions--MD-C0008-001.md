# 管理决定｜MD-C0008-001｜D003 字面 grant token 修签与实际子根约束保持

- `run_id / call_id / decision_id`：`OI-EAW-WALL-20261114-01 / C0008 / MD-C0008-001`
- manager：`chatgpt:OI-EAW-WALL-20261114-01:manager`
- invocation token：`oiwall-C0008-9af1a4491419e5654b27dad7`
- 决定类别：未派发 D003 的运输表示修签；不构成业务返修、Owner 新授权、业务 Gate 变更或 evidence action G-RUN。

## 1. 输入、已核状态与问题边界

### 1.1 正式输入

- C0008 完整任务：`daowei2026/observe-iterate@3e6ead1648ccee8364eac315c705e07ba8e938ac:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0008/FULL_ASSIGNMENT.md`
- C0008 Invocation：`daowei2026/observe-iterate@e18fe8e8cb8726314067e9adaa921405a954e4a7:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0008/INVOCATION.json`
- origin／C0007 Return：`daowei2026/observe-iterate@f586fb76b8245fd739d50f80b4f585d9379b11b3:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0007/PRO_RETURN.json`
- C0007 专业决定：`daowei2026/observe-iterate@11fce23f543b000425350153d9cb1eda5e78453c:longrun/runs/OI-EAW-WALL-20261114-01/business_control/decisions/MD-C0007-001.md`
- 静态字面 scope 审计：`daowei2026/observe-iterate@a8a5952a696b2857a6b2a02b296b32503decc2a5:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0008/D003_LITERAL_SCOPE_AUDIT.json`
- 采用版 Gate：`daowei2026/observe-iterate@ca7fdae84f65265332e3a53865724a2615508766:longrun/tools/longrun_gate.py`
- Owner Binding：`daowei2026/observe-iterate@1e00424349ce8a5d72c9fccf74585d18630b62b8:longrun/runs/OI-EAW-WALL-20261114-01/RUN_BINDING.json`

### 1.2 修签前真实状态

- D002 已接受并关闭；legacy narrow comparison、三个 scoped QCR 和全部 C0007 管理决定继续有效；
- 三个父问题继续 OPEN；父任务 `incomplete`；
- scenario-first、八项 EP、exact source baseline、2 GiB／4 GiB／25 min／50,000 files／零外写 cap 和所有禁令已由 C0007 固定；
- `ARUN-WALL-SCENARIO-001 = NEEDS_PRECONDITION`，`G-RUN = NOT PASSED`；
- C0007 D003 从未送达 E1；无新 W、无 build/test/run、无外部动作；W1 idle，旧 W001 锁已释放。

本轮只解决运输表示，不能借此改变上述任一专业事实或状态。

## 2. 精确问题

采用版 `order()` 同时要求：

```text
set(W.grant.allowed_writes) ⊆ set(D.allowed_writes)
```

而 `grant_covers()` 又要求：

```text
set(W.grant.allowed_writes) ⊆ set(OwnerGrant.allowed_writes)
```

两个判断都是字面字符串集合包含，不把目录子路径当作父 token 的子集。

Owner Binding 的字面 token 是：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01
longrun/runs/OI-EAW-WALL-20261114-01
```

C0007 D003 JSON 的 token 是：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003
longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003
```

两组 token 字面交集为空，所以旧 D 虽可作为 manager→executor 合同，却不能承载任何具有真实写入的合法 W。子路径在物理上仍位于 Owner 根授权内，因此问题是运输表示不兼容，不是 Owner 权限缺口。

## 3. 管理决定

决定：`TRANSPORT_REPRESENTATION_REPAIR_ACCEPTED`。

### 3.1 D003 重新签发

D003 编号、recipient、return_to、专业范围和业务上下文均不变，由 C0008 重新签发：

- 当前正文：`daowei2026/observe-iterate@461a420bbacc5d24ee093f9f20f2f86653973041:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.md`
- 当前 JSON：`daowei2026/observe-iterate@b7200816f86395cd1475ea3a482fc2e63086b967:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`

准确运输身份：

```text
issuer_call_id = C0008
issuer          = chatgpt:OI-EAW-WALL-20261114-01:manager
recipient       = chatgpt:OI-EAW-WALL-20261114-01:executor:E1
return_to       = chatgpt:OI-EAW-WALL-20261114-01:manager
```

### 3.2 机读 grant token

D003 JSON 的 `allowed_writes` 使用 Owner Binding 原文的两个根 token：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01
longrun/runs/OI-EAW-WALL-20261114-01
```

这使未来 W 可以把某一对应 Owner grant 的 `operation / execution_context / authority_quote / allowed_writes` 逐字带入，并同时满足 D 和 Binding 的字面集合判断。

### 3.3 实际执行写面没有扩大

D003 正文继续将真实写入强制限制为：

```text
Linux actual exclusive write root:
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003

GitHub actual publish root:
longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003
```

根 token 是机械运输授权上限，不是 D003 的实际执行许可。后续 W 必须：

1. grant 逐字复制相应 Owner grant；
2. instructions、cwd、输出路径和 write audit 再次固定 D003 子根；
3. 对 D003 子根外任何实际写入硬停止，即使该位置仍在 Owner 根 token 内；
4. 不得把根 token 解释成共享源码、TIS、worker checkout、生产产品、源码 GitHub 仓库或其他 Run 目录的写权限。

### 3.4 历史版本

以下 C0007 候选继续作为精确历史保留，但从未送达且不得再派发：

- `daowei2026/observe-iterate@adda66cf75e672fc16e3f0d327f315d5af81f09d:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.md`
- `daowei2026/observe-iterate@2f0a3003da25c8d63d349c47a23b58057b77047e:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`

D003 当前唯一可派发版本是 C0008 修订版。

## 4. 保留不变的专业范围

以下全部原样保留：

- scenario-first 顺序；
- `EP-WALL-SHARED-01..03` 与 `EP-SCENARIO-01..05`；
- FRP base commit `cac6c912dd65a14acbd591ca57e0afd8ddb4ef13`；
- 先 dry dependency/write/cost preflight；
- 只有 cap 可监测且预计不超限时才允许 compile-only／serialization engineering verification；
- disk ≤ 2 GiB、peak RSS ≤ 4 GiB、post-preflight wall clock ≤ 25 min、new files ≤ 50,000、D003 子根外写入为 0；
- 禁止九场景 evidence execution、normal action、DBA、wrapper/native reader、共享源码写入、源码 repo push和 production lifecycle 语义修改；
- 工程验证不能当 current O/C/A/D 材料、业务 comparison 或 `G-RUN`；
- normal prerequisite 路线继续独立 OPEN；
- manager 不直接签 W。

## 5. Gate 与完成状态

本轮不重新判断业务 Gate。C0007 的结果继续原样有效：

| 对象 | 当前状态 |
|---|---|
| `G-COMPARISON / EC-WALL-LEGACY-NORMAL-001` | `PASS_WITH_SCOPE` |
| 三个 scoped QCR | 已接受 |
| `EV-WALL-WORKING-v0.2` | `WORKING / NOT FROZEN` |
| `G-DIAGNOSIS` | `NOT TRIGGERED` |
| `ARUN-WALL-SCENARIO-001` | `NEEDS_PRECONDITION` |
| scenario `G-RUN` | `NOT PASSED` |
| `ARUN-WALL-NORMAL-001` | `NEEDS_PRECONDITION` |
| normal `G-RUN` | `NOT PASSED` |
| D003 prerequisite construction | `ELIGIBLE_WITH_LIMITS`，仅 Run-local staged engineering |
| 三个父问题 | `OPEN` |
| 父任务 / H3 | `incomplete / NOT ELIGIBLE` |

运输修签不等于工程前置满足，不产生任何新材料，也不解除任何运行禁令。

## 6. 当前真实状态与准确后继

```text
D001 = accepted / closed
D002 = accepted / closed
C0007 D003 candidate = SUPERSEDED_BEFORE_SEND
C0008 D003 = READY_NOT_SENT
E1 = not started for D003
new W = none
build/test/run = none
owner request = none
parent task = incomplete
```

下一合法动作是主控依据 C0008 当前 D003 MD/JSON，向原 E1 实际派发 D003并登记 receipt。不得派发 C0007 候选；送达状态 UNKNOWN 时先对账，不重复派发。

E1 如需 Linux 工程操作，须先按 D003 签下一未占用 W；manager不直接签 W。主控必须核实际 physical binding、single-writer、model/effort、cwd、Owner literal grant token及 D003 actual root。Worker Return先回 E1，经 E1专业消费后再回 manager。

manager 恢复条件仍为：D003完整/部分回交，或确认的 preflight、写面、权限、运输或外部动作异常。下一轮才判断各 EP 的 WorkQuality/UseEligibility、scenario action 是否可重分类，以及是否另过 `G-RUN`。
