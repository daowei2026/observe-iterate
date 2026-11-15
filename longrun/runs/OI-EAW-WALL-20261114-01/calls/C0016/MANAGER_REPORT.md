# C0016 管理 Pro 报告｜A001 方法变更复审、旧工程收束与直接 BASE 后继

## 1. 调用身份与连续性

- `run_id / call_id`：`OI-EAW-WALL-20261114-01 / C0016`
- role / sender：`manager / chatgpt:OI-EAW-WALL-20261114-01:manager`
- invocation token：`oiwall-C0016-46ba9be6ddf5f86f77ad344d`
- 完整任务：`daowei2026/observe-iterate@096ee45c5c41a6afee5bed99ce634ee52ed3761a:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0016/FULL_ASSIGNMENT.md`
- Invocation：`daowei2026/observe-iterate@673896390068648fe25706c5d17207ed08d5ac51:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0016/INVOCATION.json`
- Owner变更原文：`daowei2026/observe-iterate@33c7a222687186c1e1c8c685993a341513820d8d:longrun/runs/OI-EAW-WALL-20261114-01/authority_changes/A001/OWNER_CHANGE.md`
- 有效授权增量：`daowei2026/observe-iterate@b8514dbc38e3589fc01c9a7667899ee2059e814f:longrun/runs/OI-EAW-WALL-20261114-01/authority_changes/A001/EFFECTIVE_AUTHORITY.json`

本调用继续原 Run、原 manager 和原 Owner目标。它不是新GO、Run或测试；没有追溯改写C0015、D001～D003、W001～W007的历史原件。

## 2. 本轮完整读取和实际消费

本轮实际读取并消费：

1. Owner A001逐字方法/授权变更；
2. 新固定版 `control/01～06`、review/06～07、manager/executor指南和V2合同；
3. 主控真实状态审计；
4. W007本地执行报告；
5. C0015 E1正式Return及D003进度报告；
6. 旧D003和W007 ORDER；
7. D001专业报告和材料manifest；
8. D002正式comparison、QCR和C0007管理接受。

因此本决定不是从旧TASK_PROGRESS或聊天摘要推测，而是把C0008之后的C0015/W007事实补入了当前管理全景。

## 3. Owner A001 带来的专业方法变化

后续新专业工作采用：

```text
observe-iterate@dc18a7251b8d433bd8c16ccd0f9cbdf230b1819c
cgpterm@becfbcbc7eec3e4fc6a44cd0b0a7a934ec666ff8
```

观察材料准备只使用新版 `control/02` 原Skill步骤0～7：

```text
0 入口与资产
1 处理骨架及输出核对
2 材料取舍
3 观察方法
4 最小落地
5 实际取得材料
6 质量检查
7 交接
```

以下旧控制/工程顺序取消：

```text
S0～S5独立执行链
S2/M05硬前置
独立G-RUN执行链
先建设独立源码副本、Landlock/seccomp、全局零外写、clean closure
```

新Linux授权为：

```text
operation=wall-observation-work
execution_context=linux:/dwdhome/fy/BASE_E6_2
allowed_writes=/dwdhome/fy/BASE_E6_2
```

它要求优先直接复用BASE现有源码、数据、构建环境和工具；按需新增脚本、数据和结果，必要小范围本地修改先核差异，不覆盖他人未提交修改。破坏性Git、现役成果覆盖、无关写和正式源码push仍禁止。

## 4. D001/D002 的资格保持

### 4.1 D001

D001继续为：

```text
REPORTED_COMPLETE for D001 contract
PARTIAL_WITH_LIMITS for business result
```

保留：

- current TIS/FRP working-tree静态事实；
- historical O/C/D、bounded reader和exact normal chain；
- current tuple、native reader、A、异常/时间场景等缺口；
- `EV-WALL-WORKING-v0.2 = WORKING / NOT FROZEN`。

不重做W001，也不把legacy current化。

### 4.2 D002

继续保留：

```text
G-COMPARISON / EC-WALL-LEGACY-NORMAL-001 = PASS_WITH_SCOPE
FN-IDENTITY-01 = SUPPORTS
FN-START-01    = SUPPORTS
FN-BAND-01     = SUPPORTS
FN-END-01      = SUPPORTS
```

四项共享同一physical chain，不是四份独立共证。三个scoped QCR继续有效：

```text
QCR-LEGACY-IDENTITY-NORMAL-001 = COMPLETE_FOR_SCOPE
QCR-LEGACY-OC-PUBLICATION-NORMAL-001 = COMPLETE_FOR_SCOPE
QCR-LEGACY-TO-CURRENT-NONEXTRAPOLATION-001 = COMPLETE_AS_BOUNDARY
```

current terminal/replay/conflict/transaction/UTI仍只是高价值候选，不能直接判bug。

## 5. C0015 与 W007 真实状态复审

### 5.1 C0015

C0015是原E1正式Return：

```text
professional_state = IN_PROGRESS
accepted workers   = W002～W006
issued successor   = W007
```

C0015的专业接受和历史判断保留。它签发W007时只知道W007 ORDER已发布，不能用当时时点覆盖后来已发生的物理派发/STOP事实。

### 5.2 W007不是未发送

主控对账确认：

```text
physical thread = 01a1da55-5881-7590-94a1-0661f0236977
physical turn   = 01a1dd15-f35a-7892-bca9-6de6721263b5
started         = 2026-11-15T02:42:45.760143Z
local terminal  = STOP at 2026-11-15T03:17:08.140Z
thread state    = notLoaded
goal            = null
queue           = empty
```

本次没有resume/start/steer，也禁止恢复或重派W007。

### 5.3 W007取得和未取得什么

已发生：

- fresh/carry-forward evaluator、FIOCLEX和组合锁证明；
- 唯一R0-A1 current实测exit0；
- R0-B首次Git `cat-file`启动时，旧policy拒绝`openat("/dev/null", O_RDWR)`，Git128/driver1并STOP；
- 85份本地原件、2,075,599 bytes；主控已独立核具名hash；
- reservation holder/lock仍在。

未发生：

- 两个offline closure实际评估；
- R0-C和四budget/monitor；
- 八EP建设；
- staged source、patch、local commit；
- 9/18/22 fixture执行或current scenario；
- compile-only/serialization；
- current O/C/A/D业务材料；
- W007 formal Worker Return。

W007 local report只能作为status/evidence source。manager没有跳过E1专业接受，也没有把它列入`accepted_worker_refs`。

## 6. D003/W007 的管理结论

具名管理决定：

`daowei2026/observe-iterate@02f7a2139e193aae6d9257363a82d72cc2502f1a:longrun/runs/OI-EAW-WALL-20261114-01/business_control/decisions/MD-C0016-001.md`

### 6.1 旧工程不再是业务依赖

以下内容不再要求补齐：

- isolated/staged source；
- Landlock/seccomp和全局零外写；
- independent clean/offline closure；
- 四PASS链和旧固定cap/monitor；
- 在真实取数前完成八EP整包；
- 为继续旧工程而修`/dev/null`、procfs或sandbox。

W007 STOP是旧工程动作终态，不是Wall业务失败。

### 6.2 当前状态

```text
W007 = PHYSICALLY_STOPPED / DO_NOT_RESUME / NO_FORMAL_RETURN
D003 prospective eligibility = WITHDRAWN_BY_A001_METHOD_CHANGE
D003 current state = STOPPED_FOR_PROSPECTIVE_WORK / PENDING_E1_PROFESSIONAL_CLOSEOUT
```

D003不再作为活跃IN_FLIGHT业务路线，但尚不能伪装原合同完成；原E1需要在D004里给最终closeout。

### 6.3 证据和锁

W007 evidence root和关键manifest/hash/trace必须保留。旧锁：

```text
path       = /dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/.D003-writer.lock
holder     = 251010
startticks = 48763578
inode      = 14806399
```

E1需先核Worker终态、queue、锁pre-state和关键证据，然后通过新合法动作释放holder/lock并保存post receipt；不得删除W007 evidence root。该动作是资源收束，不是W007 resume。

## 7. Gate与父问题决定

| 对象 | C0016结果 |
|---|---|
| historical `G-COMPARISON` | 保持`PASS_WITH_SCOPE` |
| historical scoped QCR | 保持完成 |
| `EV-WALL-WORKING-v0.2` | 保持`WORKING / NOT FROZEN` |
| `G-DIAGNOSIS` | `NOT TRIGGERED` |
| old D003 prerequisite route | `SUPERSEDED_BY_A001` |
| old scenario/normal G-RUN | 历史保留，不构成新M门禁 |
| current M method | `control/02`步骤0～7 |
| H3 | `NOT ELIGIBLE` |

三个父问题仍OPEN：

- historical normal identity scoped完成，但current identity/terminal/replay/time仍缺；
- historical normal O/C scoped完成，但current O/C/D/A/transaction/read path仍缺；
- legacy→current不可外推边界完成，但current suitability仍缺。

## 8. 实际签发 D004

### 8.1 正式原件

- Markdown：`daowei2026/observe-iterate@00c789154caee5a7a0c17bf7567292d5ac32aec1:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D004/DELEGATION.md`
- JSON：`daowei2026/observe-iterate@f1e6b6ddf6a8d5d8e46077eace034d0d53657d08:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D004/DELEGATION.json`

运输身份：

```text
issuer_call_id = C0016
issuer          = original manager
recipient       = original E1
return_to       = original manager
```

D004 allowed_writes与A001一致：

```text
/dwdhome/fy/BASE_E6_2
longrun/runs/OI-EAW-WALL-20261114-01
```

### 8.2 D004三个lane

#### Lane A：closeout

原E1消费W007状态证据、保留关键原件、释放旧锁并把D003合法标成：

```text
SUPERSEDED_STOPPED_WITH_RETAINED_EVIDENCE
```

不补造W007 formal Return，不继续旧工程。

#### Lane B：直接BASE材料

按control/02步骤0～7：

- 复用D001/D002；
- 直接查BASE现有source/data/test/trace/reader/Notebook/工具；
- 重新判必需/条件/可选/暂不准备材料；
- 实际取得current绑定的upstream/O/C/D，A和异常场景按必要性最小补；
- 可以短窗口运行、小脚本和先核差异后的必要小修改；
- 不要求独立副本、sandbox、zero-write或clean closure；
- 输出真实`DATA_READY/PARTIAL_WITH_LIMITS/BLOCKED`。

#### Lane C：current分析

```text
analysis_round_id = AR-WALL-003
expectation seed  = EV-WALL-CURRENT-WORKING-v0.1
```

探索可使用WORKING；正式comparison前只冻结证据可覆盖的最小子集，按六种状态逐场景判断。只有正式COUNTERS值得且可区分时才诊断，不强制调参或修代码。

## 9. Worker与授权边界

manager没有签W。E1如需Linux动作可签下一未占用新W（候选W008）：

```text
worker    = original W1
return_to = original E1
grant     = A001 literal Linux grant
```

默认新增中间/导出放在：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/
```

但Owner允许在BASE内做业务必要的小范围修改；前提是先核status/diff/hash、保护未提交修改、可回退、无破坏性Git/production覆盖/push。主控派发前仍需核physical thread、model/effort、cwd、single-writer和A001机械有效授权。

Worker只交事实/实物，不能决定closeout、材料必要性、freeze、formal comparison、diagnosis、父问题或H3；Return先回E1。

## 10. 最新全景

最新全景：

`daowei2026/observe-iterate@6fe06f38e2706b78c8c079a1f9979f5b3c912431:longrun/runs/OI-EAW-WALL-20261114-01/business_control/TASK_PROGRESS.md`

当前真实状态：

```text
D001 = accepted / closed
D002 = accepted / closed
D003 = stopped for prospective work / E1 closeout pending
W007 = physical STOP / no formal Return / do not resume
old lock = held pending legal closeout
D004 = READY_NOT_SENT
new W = none
new material = none
current analysis result = none
parent questions = OPEN
parent task = incomplete
owner request = none
```

## 11. 准确后继与恢复条件

主控下一步应使用D004 MD/JSON向原E1实际派发并登记receipt。不得恢复或重派W007；状态UNKNOWN先对账。

E1可在同一D004内先完成closeout，也可并行开展不竞争旧锁的专业分析；新Linux写动作必须使用新W身份并在资源冲突解除后执行。E1正式回交后，manager分别判断：

1. D003/W007 closeout和锁释放是否完成；
2. current MaterialPackage的WorkQuality/UseEligibility；
3. current expectation freeze/comparison是否合格；
4. 三个父问题哪些可新建scoped QCR；
5. 是否需要诊断、定向补证或有界结束。

- `professional_state`：`IN_PROGRESS`
- `issued_delegations`：D004一项
- `issued_orders`：空
- `accepted_worker_refs`：空
- `remaining_scope`：最新TASK_PROGRESS
- `continuation`：D004 Markdown
- `owner_request`：无
