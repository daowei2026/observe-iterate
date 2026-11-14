# C0008 管理 Pro 报告｜D003 字面 scope 修签、业务状态保持与准确后继

## 1. 调用身份与连续性

- `run_id / call_id`：`OI-EAW-WALL-20261114-01 / C0008`
- role / sender：`manager / chatgpt:OI-EAW-WALL-20261114-01:manager`
- invocation token：`oiwall-C0008-9af1a4491419e5654b27dad7`
- 完整任务：`daowei2026/observe-iterate@3e6ead1648ccee8364eac315c705e07ba8e938ac:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0008/FULL_ASSIGNMENT.md`
- Invocation：`daowei2026/observe-iterate@e18fe8e8cb8726314067e9adaa921405a954e4a7:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0008/INVOCATION.json`
- origin：`daowei2026/observe-iterate@f586fb76b8245fd739d50f80b4f585d9379b11b3:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0007/PRO_RETURN.json`

本调用继续原 manager，只修复尚未送达 D003 的运输表示。C0007 的完整管理报告、决定、TASK_PROGRESS、D002 消费、legacy narrow comparison、三个 scoped QCR、scenario-first 和父任务状态均已保留；没有重做 D002、改变 Owner 目标或申请新权限。

## 2. 修签触发事实

静态审计原件：

`daowei2026/observe-iterate@a8a5952a696b2857a6b2a02b296b32503decc2a5:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0008/D003_LITERAL_SCOPE_AUDIT.json`

采用版 Gate：

`daowei2026/observe-iterate@ca7fdae84f65265332e3a53865724a2615508766:longrun/tools/longrun_gate.py`

Owner Binding：

`daowei2026/observe-iterate@1e00424349ce8a5d72c9fccf74585d18630b62b8:longrun/runs/OI-EAW-WALL-20261114-01/RUN_BINDING.json`

采用版 `order()` 要求 W 的 `allowed_writes` 字面集合包含于 D 的 `allowed_writes`；`grant_covers()` 又要求同一 W grant 字面包含于 Owner grant。Gate 不进行目录父子关系归一化。

Owner 的两个 token 是：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01
longrun/runs/OI-EAW-WALL-20261114-01
```

C0007 D003 使用的是：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003
longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003
```

虽然后者物理上位于 Owner 根内，但字符串交集为空，导致无法形成同时通过 D scope 与 Owner grant 的非空 W write grant。审计是静态运输预检，不是 Worker 执行、模拟通过或运行回执。

## 3. 管理判断

具名决定：

`daowei2026/observe-iterate@147770cb63bc0de3b9a97eee1c6aa4abd6fbbbff:longrun/runs/OI-EAW-WALL-20261114-01/business_control/decisions/MD-C0008-001.md`

决定：

```text
TRANSPORT_REPRESENTATION_REPAIR_ACCEPTED
```

原因：

1. C0007 D003 从未送达，无 receipt、W、工程动作或外部副作用；
2. 子目录本身位于原 Owner 根内，不缺 Owner 授权；
3. 机械合同要求根 token字面匹配，而专业执行仍可由正文和 W instructions收窄到 D003子根；
4. 修签不改变专业任务、成本、禁令、Gate或父任务状态。

## 4. 当前唯一可派发 D003

### 4.1 精确原件

- Markdown：`daowei2026/observe-iterate@461a420bbacc5d24ee093f9f20f2f86653973041:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.md`
- JSON：`daowei2026/observe-iterate@b7200816f86395cd1475ea3a482fc2e63086b967:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`

回读后的运输身份：

```text
issuer_call_id = C0008
issuer          = chatgpt:OI-EAW-WALL-20261114-01:manager
recipient       = chatgpt:OI-EAW-WALL-20261114-01:executor:E1
return_to       = chatgpt:OI-EAW-WALL-20261114-01:manager
```

### 4.2 机读 delegated tokens

```text
allowed_writes = [
  "/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01",
  "longrun/runs/OI-EAW-WALL-20261114-01"
]
```

它们逐字对应 Owner Binding，用于 Gate 集合包含与 authority quote 对齐。

### 4.3 实际排他写面

D003 正文继续严格限制：

```text
Linux actual exclusive write root:
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003

GitHub actual publish root:
longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003
```

根 token 不是额外实际写权限。未来 W 必须逐字采用相应 Owner grant token/authority quote，但 instructions、cwd、output paths 与 write audit 必须锁死 actual subroot；actual subroot 外任何写入都触发硬停止。

### 4.4 被替代历史

以下 C0007 候选继续保留为历史，但从未送达、不得派发：

- `daowei2026/observe-iterate@adda66cf75e672fc16e3f0d327f315d5af81f09d:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.md`
- `daowei2026/observe-iterate@2f0a3003da25c8d63d349c47a23b58057b77047e:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`

状态：`SUPERSEDED_BEFORE_SEND`。

## 5. 完全保留的 D003 专业合同

### 5.1 顺序和前置

仍为 scenario-first，只建设：

```text
EP-WALL-SHARED-01..03
EP-SCENARIO-01..05
```

normal `EP-NORMAL-01..05` 独立 OPEN，不夹带进 D003，也不因 scenario-first 被取消。

### 5.2 exact baseline

```text
repository = daowei2026/frp
base_commit = cac6c912dd65a14acbd591ca57e0afd8ddb4ef13
shared checkout = read-only
```

### 5.3 cap

```text
new disk <= 2 GiB
peak RSS <= 4 GiB
wall clock after dry preflight <= 25 min
new files <= 50,000
writes outside D003 actual root = 0
nine-scenario evidence execution = 0
```

必须先完成 dependency/write/cost dry preflight。只有全部 cap 可监测且预计不超限时，才允许 compile-only 与 serialization engineering verification。

### 5.4 禁令

继续禁止：

- 九场景 evidence fixture execution；
- `ARUN-WALL-SCENARIO-001` 和 normal action；
- DBA、wrapper、native reader；
- 共享 FRP/TIS/worker checkout 写入；
- `daowei2026/frp` 写入或 push；
- production lifecycle 语义修改；
- 把工程测试结果当 current O/C/A/D、formal comparison 或 G-RUN；
- 把 staged local commit 写成上游实现。

## 6. Gate 与父任务保持不变

本轮没有重新进行专业 Gate。C0007 的状态完整保留：

```text
G-COMPARISON / EC-WALL-LEGACY-NORMAL-001 = PASS_WITH_SCOPE
three scoped QCRs                        = accepted
EV-WALL-WORKING-v0.2                    = WORKING / NOT FROZEN
G-DIAGNOSIS                             = NOT TRIGGERED
ARUN-WALL-SCENARIO-001                  = NEEDS_PRECONDITION
scenario G-RUN                          = NOT PASSED
ARUN-WALL-NORMAL-001                    = NEEDS_PRECONDITION
normal G-RUN                            = NOT PASSED
D003 prerequisite construction          = ELIGIBLE_WITH_LIMITS
parent questions                        = OPEN
parent task / H3                        = incomplete / NOT ELIGIBLE
```

运输修签不产生材料、业务发现、工程能力或 action execution。

## 7. 最新全景与资源状态

最新全景：

`daowei2026/observe-iterate@31c35e5a270ae28e9f553934faeec3a583e6ef14:longrun/runs/OI-EAW-WALL-20261114-01/business_control/TASK_PROGRESS.md`

当前真实状态：

```text
D001 = accepted / closed
D002 = accepted / closed
C0007 D003 = SUPERSEDED_BEFORE_SEND
C0008 D003 = READY_NOT_SENT
E1 D003 receipt = none
W002 = none
build/test/run = none
owner request = none
parent task = incomplete
```

W001 已消费、idle、旧锁释放。manager C0008 没有直接签 W，也没有接受 Worker Return：

```text
issued_order_refs   = []
accepted_worker_refs = []
```

## 8. 准确后继与恢复条件

主控下一步应使用 C0008 修订 D003 MD/JSON，向原 E1 实际派发并登记 receipt。不得派发 C0007 候选；状态 UNKNOWN 时先对账，不重复派发。

E1 如需 Linux staged engineering，必须先签新的合法 W（当前候选 W002）：

1. grant逐字复制相应 Owner grant；
2. instructions锁定 D003 actual root；
3. 主控核 physical worker/thread、model/effort、cwd、single-writer、token/authority quote与实际子根；
4. Worker Return先回E1，经E1专业消费后再回manager。

manager恢复条件：

- D003完整或部分正式回交；
- dry preflight证明cap、依赖或actual write root不可闭合；
- 确认需要共享源码写入、源码repo push或其他Owner未授权能力；
- D003送达、identity、权限或外部动作状态异常。

下一轮才判断八个EP的WorkQuality/UseEligibility、scenario action是否可重分类，以及是否另作G-RUN。D003本身不自动执行scenario action。

- `professional_state`：`IN_PROGRESS`
- `issued_delegations`：C0008 D003 一项
- `issued_orders`：空
- `accepted_worker_refs`：空
- `remaining_scope`：最新 `TASK_PROGRESS.md`
- `continuation`：C0008 D003 Markdown
- `owner_request`：无
