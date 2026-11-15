# W008｜D004 旧锁资源收束、W007证据只读核验与直接 BASE current 材料取得

## 0. 运输身份

- `run_id`：`OI-EAW-WALL-20261114-01`
- `work_order_id`：`W008`
- `issuer_call_id`：`C0017`
- `issuer`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `worker`：`codex:OI-EAW-WALL-20261114-01:worker:W1`
- `return_to`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `delegation_ref`：`daowei2026/observe-iterate@f1e6b6ddf6a8d5d8e46077eace034d0d53657d08:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D004/DELEGATION.json`
- work items：
  - `WI-WALL-D003-CLOSEOUT-001`
  - `WI-WALL-DIRECT-MATERIAL-001`

本 W 是 D004 下的新工具动作。它不是 W007 resume、redispatch、steer 或历史 Return 补造；不继续旧 Landlock/seccomp、clean closure、四 PASS、八 EP 或 scenario 工程路线。

Worker只交执行事实和实际材料，不决定 D003 专业关闭、材料必要性、expectation freeze、formal comparison、父问题、H3 或 G-RUN。

## 1. 主控派发前必须完成的资源动作

W008 只有在主控完成以下 pre-dispatch 动作并生成真实回执后才能物理发送。

### 1.1 重新核 W007 终态

不得只沿用 03:57:50 的历史审计。当前重新核：

- 原 W1 W007 turn 已 completed；
- Goal 为空、queue 为空；
- 无 W007 command / writer 运行；
- W007 evidence root存在；
- 85文件/2,075,599 bytes及关键hash仍可核；
- 没有 resume/start/steer。

### 1.2 保存旧锁 PRE receipt

旧对象：

```text
path       = /dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/.D003-writer.lock
historical holder PID  = 251010
historical startticks  = 48763578
historical inode       = 14806399
historical session     = 7861
```

生成并传给 Worker：

```text
W007_LOCK_RELEASE_PRE.json
```

记录当前 PID/startticks/inode/fd/flock、独立同inode nonblocking competition、queue/goal、evidence root状态和UTC。若历史值已变化，记录当前真实值，不伪造一致。

### 1.3 安全释放旧 reservation lock

- 由真实控制侧在原lockkeeper/session中正常关闭holder FD或结束只承担该锁的keeper；
- Worker不得声称自己持有/释放；
- 不kill无关进程；
- 不unlink/覆盖 evidence root；
- 锁文件可保留，核心是kernel FLOCK解除；
- 若当前已自然释放，记录`ALREADY_RELEASED_AT_CURRENT_CHECK`，不伪造主动动作。

生成：

```text
W007_LOCK_RELEASE_POST.json
```

成功标准：old holder不再拥有FLOCK，独立contender可安全取得并释放，W007 evidence root完整，W007没有被恢复。

### 1.4 建立 fresh D004 writer

精确新锁：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/.D004-writer.lock
```

记录 fresh holder PID/startticks/inode/fd/session，独立同inode竞争必须失败。生成：

```text
D004_W008_LOCK_BINDING.json
```

旧W007 holder/turn/thread eligibility和command authority不延续。

若旧锁无法安全释放且不能建立合法fresh单写者，不派发W008；主控把精确阻断返回原E1，不做破坏性处理。

## 2. Owner grant 与实际写面

### 2.1 A001 Linux grant原文

```text
operation=wall-observation-work execution_context=linux:/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2
```

### 2.2 W008主要新增根

```text
WORK_ROOT=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008
```

新增脚本、数据、日志、trace、export、manifest、review和Worker原件优先写入WORK_ROOT。

本 W 不授权编辑现有业务源码文件。若唯一材料缺口需要小范围源码修改，记录候选目标、status/diff/hash/mtime、必要性、patch建议和回退方式，停止该子动作并回E1决定；不得擅改。

允许既有低成本工具在 BASE 内更新其正常 build/cache 目录，但必须：

- 事前列出路径和预计影响；
- 不clean/reset/delete；
- 不覆盖现役product；
- 事后记录新增/变化；
- 不向正式源码分支push。

### 2.3 冻结只读路径

- W007 evidence root：只读；
- W002～W006 roots：只读，不需重复扫描；
- shared source tree：本 W 只读；
- production/current product：只读，不覆盖；
- HOME/CODEX_HOME：保持真实值，不承载本任务新增业务文件。

## 3. 精确输入

### 3.1 当前 D004 与 A001

- `daowei2026/observe-iterate@c51dd1b180b7f27d13b5a334f9ff1f5647305b60:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0017/FULL_ASSIGNMENT.md`
- `daowei2026/observe-iterate@e9bd379fd0efb1b114b21debe8624be70a6e73a6:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0017/INVOCATION.json`
- `daowei2026/observe-iterate@00c789154caee5a7a0c17bf7567292d5ac32aec1:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D004/DELEGATION.md`
- `daowei2026/observe-iterate@f1e6b6ddf6a8d5d8e46077eace034d0d53657d08:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D004/DELEGATION.json`
- `daowei2026/observe-iterate@33c7a222687186c1e1c8c685993a341513820d8d:longrun/runs/OI-EAW-WALL-20261114-01/authority_changes/A001/OWNER_CHANGE.md`
- `daowei2026/observe-iterate@b8514dbc38e3589fc01c9a7667899ee2059e814f:longrun/runs/OI-EAW-WALL-20261114-01/authority_changes/A001/EFFECTIVE_AUTHORITY.json`
- `daowei2026/observe-iterate@02f7a2139e193aae6d9257363a82d72cc2502f1a:longrun/runs/OI-EAW-WALL-20261114-01/business_control/decisions/MD-C0016-001.md`

### 3.2 Closeout

- `daowei2026/observe-iterate@64c2c923503bd86883cb39731d235dc811b42843:longrun/runs/OI-EAW-WALL-20261114-01/authority_changes/A001/CONTROLLER_STATUS_AUDIT.json`
- `daowei2026/observe-iterate@db7cc8a0c7337641017aef1b9fc980a23959dbfd:longrun/runs/OI-EAW-WALL-20261114-01/authority_changes/A001/W007_LOCAL_STAGE_REPORT.md`
- `daowei2026/observe-iterate@e788e36c8e4c18e4888f1d8a225950f51c9a695c:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W007/ORDER.json`
- `daowei2026/observe-iterate@8a856782b1e0550cdd6b877ab0203d40a2d2a9a5:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D004/results/D003_W007_CLOSEOUT_REVIEW.md`
- `daowei2026/observe-iterate@535973f200bbcc0d9935bbf187bcb6d6a9c8f733:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D004/results/W007_EVIDENCE_RETENTION_AND_LOCK_RELEASE.md`

### 3.3 既有业务成果与新方法

- `daowei2026/observe-iterate@b03a3b43497fce8c10f9dd539a4f623225dce237:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D001/results/D001_EXECUTOR_REPORT.md`
- `daowei2026/observe-iterate@2b4d60f868ef715d12ba14131871227ba95517ea:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D001/results/MATERIAL_MANIFEST.json`
- `daowei2026/observe-iterate@602c53c5602840d14068110a92bd90e80af6a306:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/D002_EXECUTOR_REPORT.md`
- `daowei2026/observe-iterate@d66906a58144a190257eef4c5e45d0a4fccdddcc:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/FORMAL_LEGACY_NORMAL_CHAIN_COMPARISON.md`
- `daowei2026/observe-iterate@f3645545d3f12294918832e47c8cdd2d3f4f86e9:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/QUESTION_COMPLETION_RECORDS.md`
- `daowei2026/observe-iterate@dc18a7251b8d433bd8c16ccd0f9cbdf230b1819c:control/02_L1_观察材料准备流程.md`
- `daowei2026/observe-iterate@dc18a7251b8d433bd8c16ccd0f9cbdf230b1819c:control/03_L1_合理性分析流程.md`
- `daowei2026/observe-iterate@dc18a7251b8d433bd8c16ccd0f9cbdf230b1819c:longrun/professional/PRO_EXECUTOR_GUIDE.md`
- `daowei2026/observe-iterate@60746c4cab457a42cf3cf302e65107f525121c20:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D004/results/DIRECT_BASE_MATERIAL_PLAN_AND_EXECUTION.md`
- `daowei2026/observe-iterate@c815c65e3d212f4aa4ca16ee933419c4cd3b506c:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D004/results/CURRENT_EXPECTATIONS_AND_SCENARIOS.md`

## 4. Lane A｜W007 closeout事实核验

Worker只读完成：

1. 消费主控PRE/POST和fresh D004 lock receipts；
2. 核 W007 root、PUBLICATION_MANIFEST、HASHES、FREEZE_RECEIPT、LOCAL_STAGE_HANDOFF；
3. 核85文件/2,075,599 bytes与关键R0-A/R0-B命令/trace在本地仍存在；
4. 核W007没有formal Return；不得生成、补写或模拟；
5. 核旧D003 lock已释放、新D004 lock为fresh；
6. 输出哪些事实来自controller，哪些来自W007 local files，哪些未专业判断；
7. 不修改W007 root，不运行W007 command。

交付：

```text
W007_CLOSEOUT_EXECUTION_FACTS.md
W007_EVIDENCE_RETENTION_MANIFEST.json
W007_LOCK_RELEASE_PRE.json                  # 主控真实receipt逐字副本/引用
W007_LOCK_RELEASE_POST.json                 # 主控真实receipt逐字副本/引用
D004_W008_LOCK_BINDING.json                 # 主控真实receipt逐字副本/引用
```

## 5. Lane B｜control/02 Step 0～7 直接 BASE 取材

### Step 0｜资产调查

直接核当前 BASE：

- TIS/FRP/frp-core repo、HEAD、branch、status/diff；
- current Wall source/build/test/Fao入口；
- data/product/trace/reader/Notebook/CAEGraph/历史结果；
- 可复用现有target/test/runner；
- current actual material存在性。

输出：`BASE_ASSET_INVENTORY.json`。

### Step 1｜处理骨架

按真实当前实现更新：

```text
upstream / WallAssembler
→ ingress/decode
→ occurrence ledger / lifecycle state / active/current update
→ O/C/D
→ reader/consumer/material
```

区分业务输入、实质阶段、预期输出、working-state/debug、根本缺失。输出：`CURRENT_PROCESSING_SKELETON.md`。

### Step 2｜材料取舍

按三个父问题逐项写：

```text
必需 / 有条件需要 / 可选建议 / 暂不准备
```

不得把A和全部九场景预设为开工前置。输出：`MATERIAL_REQUIREMENTS_AND_SELECTION.md`。

### Step 3～4｜方法与最小增量

优先：existing reader/test/trace/runner、targeted selector、窄窗口 controlled input。只在WORK_ROOT新建小脚本/转换/导出。

本W不编辑existing source。若被唯一缺口阻断，输出 `BASE_CHANGE_CANDIDATE.md`，不实际修改。

### Step 5｜实际材料

按顺序执行，保留可独立合格子集：

#### P1 current binding

- current exact source/data/build/test binding；
- params/calendar/object/time/data stage；
- exact command/cwd/input/output/exit/elapsed/bytes。

#### P2 normal chain

利用现有 target/test/runner实际取得最小current controlled normal chain：

```text
Start → one/two legal updates → End
```

尽可能取得 upstream、O、C、D 和 A/等价pre-post state。没有A时仍保留合格O/C并准确限域。

#### P3 reader/consumer

实际执行 current reader/consumer或最接近的现有读取路径。若失败，区分：material不存在、entrypoint不存在、schema/wrapper不匹配、环境不可执行或本轮未尝试。

#### P4 高区分度现有场景

只有existing targeted test/低成本入口存在时，最多取得两个，优先：

1. cross-firing exact duplicate Start；
2. after-End现有test最接近的一项；
3. legal+invalid same firing；
4. out-of-order UTI。

不建设九场景fixture或dedicated target。

### Step 6｜质量核验

至少核：

- current/legacy版本；
- identity、object、calendar、params、data stage；
- actual/confirm/known/firing time；
- O/C/D/A output role；
- `ValidEmpty/NoOccurrence/DataUnavailable/InsufficientHistory/Pending`；
- original/postprocessed/display转换；
- controlled/static/natural evidence类别；
- side effects和existing BASE path changes。

### Step 7｜交接

必须返回真实标签之一：

```text
DATA_READY
PARTIAL_WITH_LIMITS
BLOCKED
```

不得只交计划或用source definition冒充数据。

## 6. 动作成本与停止

本W不沿用旧四PASS或旧2GiB/4GiB/25min合同，但每个动作仍需有界：

- 不运行full-year/unbounded重算；
- 在运行前记录输入范围、预计输出位置和停止方法；
- 单命令实际超过30分钟或新增数据超过5GiB时安全停止，除非更早已证明该动作必要且无窄替代；
- 发现覆盖未提交修改、现役product、生产写入、破坏性Git或身份/版本混淆时停止对应动作；
- 局部失败不冻结其他可继续子项；
- 外部动作状态不明时不盲目重试。

## 7. 必交产物

本地结果根：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008
```

GitHub出版目标：

```text
longrun/runs/OI-EAW-WALL-20261114-01/delegations/D004/results/W008/
```

最低交付：

```text
WORKER_EXECUTION_REPORT.md
W008_BINDING.json
W007_CLOSEOUT_EXECUTION_FACTS.md
W007_EVIDENCE_RETENTION_MANIFEST.json
W007_LOCK_RELEASE_PRE.json
W007_LOCK_RELEASE_POST.json
D004_W008_LOCK_BINDING.json
BASE_ASSET_INVENTORY.json
CURRENT_PROCESSING_SKELETON.md
MATERIAL_REQUIREMENTS_AND_SELECTION.md
CURRENT_MATERIAL_EXECUTION_REPORT.md
CURRENT_MATERIAL_REVIEW.md
CURRENT_MATERIAL_MANIFEST.json
BASE_SIDE_EFFECTS_AND_DIFF_REPORT.json
COMMAND_LOG.jsonl
PUBLICATION_MANIFEST.json
HASHES.sha256
```

按实际材料增加：

```text
materials/current_normal_chain/*
materials/current_reader/*
materials/current_scenarios/*
BASE_CHANGE_CANDIDATE.md                # 只在真实需要小改时，不实施
```

没有材料时不造空数据文件；review/manifest准确写缺失。

## 8. Worker Return

正式 `WORKER_RETURN.json` 必须：

- V2 schema；
- `work_order_id=W008`；
- `return_to=chatgpt:OI-EAW-WALL-20261114-01:executor:E1`；
- outcome如实 `EXECUTED/PARTIAL/STOP/FAILED`；
- result_ref指真实出版的`WORKER_EXECUTION_REPORT.md`；
- manifest只列实际产物和hash；
- 不把W007 local report冒充formal Return；
- 不宣称材料业务适用、expectation frozen、SUPPORTS/COUNTERS、父问题或H3/G-RUN完成。

Worker无GitHub写权限时，冻结原件后交主控逐字出版；取得真实refs后形成正式Return。不得造future/self ref。

## 9. 硬停止

- W007被resume/steer/redispatch；
- 旧锁未安全释放却建立冲突writer；
- binding/grant/cwd/model/effort/single-writer不一致；
- 修改W007 evidence root；
- 补造W007 formal Return；
- 需要破坏性Git、覆盖未提交修改、覆盖现役成果或正式push；
- 需要未授权写面或生产覆盖；
- 版本/身份无法区分，继续会制造伪current证据；
- 动作高成本/不可逆/效果未知且无安全停止。

## 10. 接收目标

E1应能据W008 Return判断：

1. W007关键证据是否保留，旧锁是否有真实pre/post释放receipt；
2. current BASE真实入口、版本和处理骨架；
3. 实际取得哪些current normal/O/C/D/A/reader/scenario材料；
4. 哪些材料可进入探索，哪些具备最小freeze资格，哪些只能算static/controlled技术输出；
5. 三个父问题分别能回答到什么深度；
6. 是否需要最小补证、formal comparison或有界未决；
7. 是否存在正式COUNTERS值得R3，而不是继续旧工程。
