# D004｜D003/W007 专业收束复审

## 0. 结论

- `run_id`：`OI-EAW-WALL-20261114-01`
- `call_id`：`C0017`
- executor：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- 当前 delegation：`D004`
- 专业收束决定：

```text
D003 = SUPERSEDED_STOPPED_WITH_RETAINED_EVIDENCE
W007 = PHYSICAL_STOP_NO_FORMAL_RETURN / DO_NOT_RESUME / DO_NOT_REDISPATCH
```

D003 没有完成其原八 EP／旧 Phase-0 合同；它因 Owner A001 对后续方法和 BASE 使用方式作出前瞻性变更而合法停止。该状态不是 `REPORTED_COMPLETE`，也不是 Wall 业务失败。

旧 reservation lock 的资源释放尚需新的合法动作和 pre/post receipt；因此 D004 仍为 `IN_PROGRESS`。资源收束不重新激活 D003 或 W007。

## 1. 权威来源

- Owner A001：`daowei2026/observe-iterate@33c7a222687186c1e1c8c685993a341513820d8d:longrun/runs/OI-EAW-WALL-20261114-01/authority_changes/A001/OWNER_CHANGE.md`
- 有效授权：`daowei2026/observe-iterate@b8514dbc38e3589fc01c9a7667899ee2059e814f:longrun/runs/OI-EAW-WALL-20261114-01/authority_changes/A001/EFFECTIVE_AUTHORITY.json`
- 管理决定：`daowei2026/observe-iterate@02f7a2139e193aae6d9257363a82d72cc2502f1a:longrun/runs/OI-EAW-WALL-20261114-01/business_control/decisions/MD-C0016-001.md`
- 当前 D004：`daowei2026/observe-iterate@f1e6b6ddf6a8d5d8e46077eace034d0d53657d08:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D004/DELEGATION.json`
- 主控状态审计：`daowei2026/observe-iterate@64c2c923503bd86883cb39731d235dc811b42843:longrun/runs/OI-EAW-WALL-20261114-01/authority_changes/A001/CONTROLLER_STATUS_AUDIT.json`
- W007 本地事实：`daowei2026/observe-iterate@db7cc8a0c7337641017aef1b9fc980a23959dbfd:longrun/runs/OI-EAW-WALL-20261114-01/authority_changes/A001/W007_LOCAL_STAGE_REPORT.md`
- C0015 E1 Return：`daowei2026/observe-iterate@946fa7931bf25b88c04c11b3a58cbcb3590841c5:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0015/PRO_RETURN.json`
- W007 ORDER：`daowei2026/observe-iterate@e788e36c8e4c18e4888f1d8a225950f51c9a695c:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W007/ORDER.json`

## 2. 为什么旧路线被取消

A001 明确取消了后续新工作中的旧 S0～S5 独立链、S2/M05 前置和独立 G-RUN 执行链，并要求直接复用 `/dwdhome/fy/BASE_E6_2` 的现有源码、数据、构建环境和工具。以下旧工程条件不再是取得 Wall 观察材料的业务前置：

- 独立源码副本或 staged source；
- Landlock/seccomp 组合隔离；
- 全局零外写证明；
- independent clean/offline closure；
- 四 PASS 与旧固定 cap/monitor；
- 在真实取材前完成八 EP 整包；
- 为旧隔离链继续修 `/dev/null`、procfs 或 sandbox policy。

这些历史调查仍可保留为工程事实，但不得换名重派或继续占据业务主线。

## 3. W002～W006 保留的专业事实

C0015 之前对 W002～W006 的限域专业接受继续有效。它们只说明旧路线调查到哪里，不构成 D004 材料前置。

| Worker | 可保留事实 | 不可外推 |
|---|---|---|
| W002 | closure/cap/全局零外写未证，按旧 Gate 合法 STOP | 不能称 BASE 不能直接取材 |
| W003 | inherited-FD fail-closed 与 writable `/dev/null` 接线事实 | 不能称 Landlock 不支持 |
| W004 | O_RDONLY stdin、NNP/Landlock/seccomp 安装链与 `FIOCLEX` stop | 不能称 confinement PASS |
| W005 | 本机 `FIOCLEX=0x5451`、准备器历史 trace 断言错误 | 不能称 filter/evaluator 已运行 |
| W006 | P0～P3、current kernel 安装、FIOCLEX 成功及 holder/procfs stop | 不能称完整 probe/global zero-write PASS |

这些事实的适用范围仍以各自 E1 专业报告为准，不需要在 D004 中重算或补齐。

## 4. W007 可保留的执行事实

W007 没有 formal Worker Return，故本 D 不把它放入 `accepted_worker_refs`。主控审计和本地报告可作为状态/执行事实来源保留：

```text
physical thread = 01a1da55-5881-7590-94a1-0661f0236977
physical turn   = 01a1dd15-f35a-7892-bca9-6de6721263b5
started         = 2026-11-15T02:42:45.760143Z
local STOP      = 2026-11-15T03:17:08.140Z
stop_code       = STOP_R0_B_GIT_DEV_NULL_O_RDWR_EACCES
local originals = 85 files / 2,075,599 bytes
formal Return   = absent
```

可保留：

- fresh/carry-forward evaluator、FIOCLEX、组合锁证明和唯一 R0-A1 本地结果；
- R0-B 首个 Git `cat-file` 在旧 policy 下 `openat("/dev/null", O_RDWR)=EACCES` 的直接 STOP；
- 两套 closure 未实际评估；
- R0-C、八 EP、staged source、patch、fixture、compile/serialization和所有 scenario/current evidence均未进入；
- 85 项原件、manifest/hash/freeze receipt及 reservation lock 是真实副作用。

不可使用为：

- formal Worker Return；
- E1 对 W007 的正式 Worker 结果接受；
- current Wall 业务 evidence；
- current runtime/reader PASS；
- 八 EP 完成；
- closure 两候选均失败；
- D003 或父任务完成。

## 5. 八 EP、closure、cap 与 scenario 的收束

旧 EP 矩阵和 Phase-0 结果作为历史审计保留，但在 D004 中统一标记：

```text
prospective execution status = RETIRED_BY_A001_METHOD_CHANGE
completion under old contract = NOT ACHIEVED
required for D004 material work = NO
```

没有发生的内容不得补造：

- 两个 offline closure 的实际评估；
- R0-C 四预算和 continuous monitors；
- 八 EP 工程建设；
- 9/18/22 fixture、scenario、normal action；
- compile-only、serialization、native reader或 current O/C/A/D。

## 6. 专业关闭判定

### 6.1 D003

```text
original contract completion = NO
prospective eligibility      = WITHDRAWN_BY_A001_METHOD_CHANGE
professional terminal state  = SUPERSEDED_STOPPED_WITH_RETAINED_EVIDENCE
```

D003 不再显示为活跃专业路线。它的未完成不转化成 D004 必做工程债。

### 6.2 W007

```text
physical dispatch  = YES
physical terminal  = STOP
formal Return      = NO
professional route = DO_NOT_RESUME / DO_NOT_REDISPATCH
```

不补造当时不存在的 Worker Return，也不让新 Worker冒充 W007 续作。

### 6.3 资源剩余

旧锁在主控最后审计时为：

```text
path       = /dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/.D003-writer.lock
holder PID = 251010
startticks = 48763578
inode      = 14806399
state      = HELD at historical audit time
```

必须在实际新动作前重新核当前状态。释放动作由持有该锁的控制侧安全完成，并形成 pre/post receipt；Worker不得伪造自己持有或释放该锁。W007 evidence root不得删除。

## 7. 当前专业状态

```text
D003 closeout decision         = COMPLETE
W007 evidence qualification    = COMPLETE_FOR_STATUS_SCOPE
W007 formal Worker acceptance  = NOT_APPLICABLE / NO FORMAL RETURN
old lock resource closeout     = PENDING RECEIPT
D004 overall                   = IN_PROGRESS
```

新的 Linux 事实和锁释放将由 D004 下的新合法 W008 接续；它是 closeout/resource action 与直接 BASE 取材，不是 W007 resume。
