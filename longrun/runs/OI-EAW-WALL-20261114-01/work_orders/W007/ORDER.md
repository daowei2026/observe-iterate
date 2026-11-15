# W007｜D003 拆分 holder-lock 组合证明后的 R0-A 恢复、R0-B/C 与条件性八 EP 续作

## 0. 运输身份

- `run_id`：`OI-EAW-WALL-20261114-01`
- `work_order_id`：`W007`
- `issuer_call_id`：`C0015`
- `issuer`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `worker`：`codex:OI-EAW-WALL-20261114-01:worker:W1`
- `return_to`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `delegation_ref`：`daowei2026/observe-iterate@b7200816f86395cd1475ea3a482fc2e63086b967:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`
- `stage_instance_id`：`M-SCENARIO-PRECONDITION-001`
- `work_item_id`：`WI-WALL-SCENARIO-PRECONDITION-001`

本 W 是 W006 正式 STOP 后的**新工单、新实际子根、新锁和新执行资格**。W006 不重开、不修改、不重跑；其 root、lock、turn、命令资格、probe、policy 和冻结原件均不复用。

本 W 只修正 W006 直接证明的 proof-orchestration 耦合：restricted child 负责证明具名 inherited writable lock FD 已关闭；parent/control 侧负责在 child 执行前后证明 controller holder 为同一 PID/startticks/inode/FLOCK owner且独立竞争仍失败。restricted child 不再读取另一个进程的 `/proc/<pid>/fdinfo/<fd>`。

这不是放宽 holder-lock 完整性、Landlock/seccomp、零外写、资源 cap 或禁令。本 W 仍不是 `ARUN-WALL-SCENARIO-001`；禁止运行任一单场景、部分场景或完整九场景，禁止 normal、DBA、wrapper、native-reader、current/production material，禁止共享源码写入或 push。

## 1. 主控派发前 physical binding 与 sentinel 预确认

主控仅在以下全部成立时才可向原 W1 物理聊天发送 W007：

1. `W007` 未占用；
2. 沿用本 Run 已绑定的原 W1 物理聊天，不新建或重建聊天；
3. 针对 W007 重新实核 actual owner、thread/session、model、effort、cwd、idle/queue/no-active-goal；请求配置为 GPT-6.1 Sol Max，以实际回执为准；
4. cwd=`/dwdhome/fy/BASE_E6_2`；
5. W006 的全部 turn/命令/writer 已终态，旧 holder PID 不存在，旧 lock 已释放；
6. 获取 fresh D003 single-writer lock，记录新 holder PID/startticks/inode/fd/session，并以同 inode、new open-file-description 的 `LOCK_EX|LOCK_NB` 竞争失败证明独占；
7. `WORK_ROOT` 派发前不存在，D003/W007 无其他写者；
8. Owner literal grant、当前 D003、W007 MD/JSON 与 return route 通过 V2 Gate；
9. 真实 `HOME`/`CODEX_HOME` 被记录并保持不变，不承载本任务新增写入；
10. 完成 §1.1 精确 outside sentinel 的有界只读预确认并把回执传入 Worker binding。

任一项无法核真，不派发。Worker收到后发现不一致，立即 `STOP`。

### 1.1 主控有界只读 sentinel 预确认

精确路径：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/.W007-deny-outside-C0015-57a2c396
```

主控只执行一次有界只读 `lstat`/等价存在性检查：

```text
result = absent / ENOENT
create = 0
write = 0
delete = 0
cleanup = not needed
```

receipt 至少记录路径、UTC、工具、errno/result和未创建/未写/未删。该确认只证明负向目标事前不存在，不授予写权限，也不证明 kernel 会拒绝。

路径已存在或状态 unknown：不派发，不删除、不改名。

## 2. Owner grant 与唯一实际写根

### 2.1 Owner grant 原文——逐字保留

```text
operation=wall-observation-work execution_context=linux:/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01
```

### 2.2 W007 唯一实际排他写根

```text
WORK_ROOT=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W007
```

所有本任务新增 source、tool script、fixture、tmp、cache、config、build、logs、trace、audit、receipts、artifacts 和结果必须位于规范化真实 `WORK_ROOT` 内。Owner根中其他位置也禁止新增业务写入。

具名 D003 control lock 是已有控制面对象：允许 parent 只读检查其 path/procfs 状态、以独立 open-file-description 做 nonblocking competition 并只关闭自身 contender；禁止写文件内容、替换 inode、取得锁、释放 holder 锁或改变 holder。

禁止 symlink、bind mount、相对路径、默认目录、继承 writable fd 或环境变量逃逸。任何 actual outside business write 立即 STOP 并保留证据。

### 2.3 HOME/CODEX_HOME

- 保持实际值不变；不得重设、迁移或伪装成 WORK_ROOT；
- 只按既有执行绑定读取；
- 不得承载本任务新增业务文件、tmp、cache、config、log或结果；
- 所有可配置任务目录必须显式指向 WORK_ROOT；
- 工具若不能同时满足真实 HOME/CODEX_HOME 和新增写入仅在 WORK_ROOT，STOP，不增加外写例外。

### 2.4 冻结只读输入

- W002～W006 roots与出版原件；
- shared FRP/TIS/worker 与 local-package roots；
- production wrapper；
- 当前真实 HOME/CODEX_HOME；
- `/m3varK` 和 production products 默认完全不访问。

禁止修改、清理、补写、format、build、checkout或push这些路径。

## 3. 精确输入

### 3.1 C0015 与当前 D003

- `daowei2026/observe-iterate@e09398446753c1f6c78447e9ecbebd6b5e6f1839:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0015/FULL_ASSIGNMENT.md`
- `daowei2026/observe-iterate@6c00f276ed42428e5f369a14a90e3909fda5b713:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0015/INVOCATION.json`
- `daowei2026/observe-iterate@b7200816f86395cd1475ea3a482fc2e63086b967:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`
- `daowei2026/observe-iterate@461a420bbacc5d24ee093f9f20f2f86653973041:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.md`

### 3.2 W006 正式 STOP 与直接原件

- `daowei2026/observe-iterate@34e7fed4d771e37d9890980e368304ae73ffb3c2:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W006/WORKER_RETURN.json`
- `daowei2026/observe-iterate@e9f4e0c569caa2939f3c5bfc2f882df6842f915f:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W006/WORKER_EXECUTION_REPORT.md`
- 同 commit：`ENGINEERING_STOP_REPORT.md`、`HISTORICAL_FIOCLEX_PHASE_CLASSIFICATION.json`、`FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json`、`SECCOMP_DATA_LAYOUT_VERIFICATION.json`、`PARENT_RUNTIME_BINDING_DELTA.json`、`SECCOMP_IOCTL_FILTER_DELTA.json`、`SECCOMP_FILTER_STATIC_EVALUATION.json`、`SECCOMP_CANDIDATE_PROGRAM.json`、`FIOCLEX_KERNEL_OBSERVATION.json`、`WRITE_CONFINEMENT_REPORT.json`、`FULL_WRITE_TRACE_REVIEW.json`、`PHASE0_RECOVERY_VERDICT.json`、`OFFLINE_CLOSURE_REPORT.json`、`RESOURCE_BUDGET_REPORT.json`、`EP_ACCEPTANCE_MATRIX.md`、`W006_BINDING.json`
- 同 commit只读工具：`tools/common.py`、`tools/runtime.py`、`tools/landlock_launcher.py`、`tools/confinement_probe.py`
- 同 commit current trace：`trace/r0a1.248966`

### 3.3 E1 专业消费与 W007 决定

- `daowei2026/observe-iterate@3300929b83b2a3ce359f25d9959b24cc3939a622:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/D003_W006_PROFESSIONAL_REVIEW_C0015.md`
- `daowei2026/observe-iterate@c0dd014840d061dbbb5e1012f04c3c1b5660b9cf:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/EP_ACCEPTANCE_MATRIX_C0015.md`
- `daowei2026/observe-iterate@af980e5b2a71a0c07613b4de11eb1ab54e9472d0:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W007_SUCCESSOR_DECISION_C0015.md`

### 3.4 原工程合同与 exact source

- `daowei2026/observe-iterate@2b872fb3f65d1b40a6f4beb75bff783deac758e6:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/ADDITIONAL_ENGINEERING_PRECONDITION.md`
- `daowei2026/observe-iterate@d8ae5332c94c535d330263ec59bddfbfa3bc52b0:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/CONTROLLED_SCENARIO_ACTION_DESIGN.md`
- `daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13`

## 4. W006 不可覆盖事实

必须原样保留：

```text
W006 outcome=PREFLIGHT_STOP/STOP
P0 historical phase classification PASS
P1 local constants/layout PASS
P2 fresh candidate filter generation PASS
P3 pure evaluator PASS
current NNP/Landlock/seccomp install PASS
second Python bootstrap PASS
current FIOCLEX=0 PASS
restricted child inherited lock FD EBADF PASS
parent holder checks PASS
restricted child cross-process holder fdinfo read EACCES
same-descriptor FIOCLEX effect and remaining probes NOT_REACHED
R0-B/R0-C/Phase1/2 not entered
four PASS not established
eight EP no new satisfaction
scenario/normal/build/compile/serialization/current material=0
```

禁止把 W006 描述为 kernel不支持、static evaluator失败、FIOCLEX失败、confinement PASS或全局零外写已证。

## 5. C0｜accepted P0-P3 carry-forward 与 fresh equivalence

W007 不重跑 W004/W005/W006 历史失败链。任何 kernel 执行前必须：

1. 核 W006 accepted artifacts 的 exact ref/hash；
2. 核本机 architecture/endianness、termios/header、seccomp header/syscall header hash未变化；
3. 生成 fresh W007 `common.py/runtime.py/landlock_launcher.py/confinement_probe.py`；
4. static scan证明没有W004/W005/W006旧root、PID、startticks、inode或record-id硬编码；
5. fresh seccomp program与W006 accepted 126-instruction program在业务语义上等价，唯一允许差异是W007 record/binding元数据；
6. 对fresh candidate重新运行pure evaluator：mandatory cases、24,240-equivalent semantic matrix、jump bounds、all paths explicit terminal、non-ioctl equivalence；
7. 生成：

```text
W006_ACCEPTED_SUBFACT_CARRY_FORWARD.json
FRESH_PROGRAM_EQUIVALENCE.json
SECCOMP_FILTER_STATIC_EVALUATION.json
```

任一不一致：`STOP_FRESH_EQUIVALENCE`，不启动kernel。

## 6. C1｜holder-lock proof decomposition

### 6.1 Restricted probe 源码硬要求

在任何kernel启动前做static scan：

- 必须保留 `fstat(blocked_inherited_fd) → EBADF` 检查；
- 禁止读取/打开/stat `/proc/<holder_pid>/fdinfo/<holder_fd>`；
- 禁止读取其他跨进程 `/proc/<pid>/fdinfo/*` 来替代；
- 允许读取 `/proc/self/*` 以验证自身FD/NNP/seccomp；
- 必须保留所有后续 same-descriptor/inside/negative/child/symlink/network probes。

生成：

```text
PROBE_PROOF_DECOMPOSITION.json
```

### 6.2 Parent PRE

在spawn前调用fresh guard并保存不可覆盖：

```text
HOLDER_LOCK_PRE.json
```

必须包含：holder PID/startticks、holder fd、lock path/inode、exact fdinfo FLOCK、same-inode independent competition errno、只关闭contender自身FD、UTC。

### 6.3 Parent POST

child PASS/STOP/nonzero/timeout均必须在parent `finally` 中调用fresh guard，保存：

```text
HOLDER_LOCK_POST.json
```

如果 child timeout，先按既定process-group kill收回，再做POST；POST失败不得被child结果掩盖。

### 6.4 Composite

在 child report 与 PRE/POST 均已产生后生成：

```text
HOLDER_LOCK_COMPOSITE_PROOF.json
```

PASS必须满足：

```text
PRE PASS
child blocked inherited FD EBADF PASS
POST PASS
same holder PID/startticks/fd/inode in binding/PRE/POST
PRE/POST fdinfo show FLOCK WRITE by holder
PRE/POST independent competition denied
parent/child did not alter/release holder
```

任何项缺失/unknown/失败：整体 `WRITE_CONFINEMENT_PASS=false`。

## 7. R0-A1｜单次实际 kernel confinement 与 probes

仅 C0/C1 static checks全部PASS后允许一次actual launcher/probe。

### 7.1 负向目标

主控预确认：

```text
OUTSIDE=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/.W007-deny-outside-C0015-57a2c396
```

Worker复核dispatch receipt，不自行预建。

其他目标在policy前只读核不存在；已存在则STOP、不删除：

```text
SHARED=/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/.W007-deny-shared-C0015-57a2c396
HOME=<actual HOME>/.W007-deny-home-C0015-57a2c396
CODEX_HOME=<actual CODEX_HOME>/.W007-deny-codex-C0015-57a2c396
SYMLINK_TARGET=/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/.W007-deny-symlink-C0015-57a2c396
```

### 7.2 必须观察

1. NNP、Landlock ABI/ruleset/add/restrict、seccomp实际安装；
2. second Python bootstrap成功；
3. bootstrap FIOCLEX成功且非FIOCLEX ioctl仍拒绝；
4. 新建inside descriptor上执行`F_GETFD initial → clear FD_CLOEXEC → FIOCLEX → F_GETFD`，同一fd证明CLOEXEC由0变1；
5. inside create/write/truncate/rename/remove成功；
6. OUTSIDE/SHARED/HOME/CODEX create/write拒绝并仍不存在；
7. HOME/CODEX read-only directory open成功；
8. child/grandchild继承restriction并各自完成适用probe；
9. symlink escape拒绝；
10. restricted child inherited writable FD EBADF + parent PRE/POST composite proof；
11. network socket/connect拒绝；
12. full trace覆盖所有probe及每个successful descriptor write路径。

出现新的kernel/bootstrap/probe问题：STOP，不扩大allowlist、不修改后重试。

## 8. R0-B｜唯一兼容离线 closure

仅R0-A PASS后进入。独立评估、只选一套：

```text
E: exact frp stack.yaml / lts-18.28
B: BASE overlay / lts-22.24 / historical GHC9.4.8
```

不得拼接。PASS必须给resolver/compiler/tool hashes、snapshot/global/local package DB、全部required local package exact roots/commits/trees/cabal hashes、transitive package IDs、minimum rebuild set、missing deps空、exact-base compatibility与offline/no-network proof。

所有命令在R0-A restriction下执行；HOME/CODEX_HOME不变，task tmp/cache/config/log显式指向W007 root。允许真正offline的declaration parse、package DB dump、dry dependency plan和有界existing artifact/log index；禁止build/compile/test/download/install/unbounded scan。

两套均不闭合：`RECOVERY_STOP_CLOSURE`，不得拼接。

## 9. R0-C｜四项预算与持续监测

仅R0-A/B PASS后进入。每项必须有非空predicted value/upper bound、同compiler/closure可比实测依据、monitor和stop threshold：

```text
new disk        <= 2 GiB
peak RSS        <= 4 GiB
post-preflight  <= 25 min
new files       <= 50,000
```

进入后继前验证monotonic deadline、whole process-group RSS、root disk/files、descendants、threshold kill/receipt、kernel+trace outside-write覆盖和HOME/CODEX_HOME新增写入0。无可比依据或任一unknown：STOP。

## 10. Phase-0 verdict

只有以下全部PASS：

```text
WRITE_CONFINEMENT_PASS
OFFLINE_CLOSURE_PASS
FOUR_BUDGETS_KNOWN_WITHIN_CAP
CONTINUOUS_MONITORS_PASS
```

才可`ELIGIBLE_FOR_STAGED_CONSTRUCTION`。任一失败：`PREFLIGHT_STOP`，保留独立成功事实，不自动调整/重试，不进入Phase1/2。

## 11. 条件性 Phase1/2｜仅四PASS后

实施原八EP：

```text
EP-WALL-SHARED-01..03
EP-SCENARIO-01..05
```

要求：exact-base clean staged source；snapshot直接来自production lifecycle state；versioned one-record-per-firing DTO/schema；rejected formal post=pre、O/C空；dedicated target只建设；fixture精确9/18/22且只做parse/count/order/hash；exact-error/transaction只做direct synthetic serialization；旧conflict ledger进入manifest；local commit标`NOT_UPSTREAM_PUBLISHED`；compile-only/serialization在cap与write audit内；不改production语义或旧test assertion。

永久禁止：

```text
single/partial/full scenario execution
SCENARIO_TRACE business evidence
normal action
DBA writer
Wall wrapper
Python native reader
production/current material generation
shared repo push
```

## 12. W007 原生产物

发布目标：

```text
longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W007/
```

最低产物：

```text
WORKER_EXECUTION_REPORT.md
W007_BINDING.json
CONTROLLER_SENTINEL_PRECONFIRMATION.json
W006_ACCEPTED_SUBFACT_CARRY_FORWARD.json
FRESH_PROGRAM_EQUIVALENCE.json
SECCOMP_FILTER_STATIC_EVALUATION.json
PROBE_PROOF_DECOMPOSITION.json
HOLDER_LOCK_PRE.json
HOLDER_LOCK_POST.json
HOLDER_LOCK_COMPOSITE_PROOF.json
FIOCLEX_KERNEL_OBSERVATION.json
WRITE_CONFINEMENT_REPORT.json
FULL_WRITE_TRACE_REVIEW.json
OFFLINE_CLOSURE_REPORT.json
RESOURCE_BUDGET_REPORT.json
PHASE0_RECOVERY_VERDICT.json
COMMAND_LOG.jsonl
WRITE_SURFACE_AUDIT.json
EP_ACCEPTANCE_MATRIX.md
PUBLICATION_MANIFEST.json
HASHES.sha256
```

若STOP：`ENGINEERING_STOP_REPORT.md`。

仅四PASS并进入后继时再交：

```text
SOURCE_BASELINE_AND_STAGING_REPORT.md
SOURCE_CHANGE_MANIFEST.json
PREREQUISITE_PATCHSET.diff
PRECONDITION_REPORT.md
D003_BINDING_CANDIDATE.json
FIXTURE_SCHEMA_AND_PROVENANCE.md
FX_WALL_SCENARIO_001.schema.json
FX_WALL_SCENARIO_001.json
KNOWN_CONTRACT_CONFLICTS.md
COMPILE_ONLY_REPORT.json              # only if run
SERIALIZATION_TEST_REPORT.json        # only if run
STAGED_LOCAL_COMMIT_REPORT.json       # only if created; NOT_UPSTREAM_PUBLISHED
```

不造空条件产物，不发布大型source/build/cache/binary/production data。

## 13. Worker Return

正式`WORKER_RETURN.json`必须：

- V2 schema；
- `work_order_id=W007`；
- `return_to=chatgpt:OI-EAW-WALL-20261114-01:executor:E1`；
- outcome如实`EXECUTED/PARTIAL/STOP/FAILED`；
- result_ref指真实出版报告；
- manifest只列实际产物/hash；
- 不把local commit伪装成GitHub ref；
- 不宣称E1接受、G-RUN/H3/action/父任务通过。

无GitHub写权限时，冻结原件交主控逐字出版，再用真实refs生成正式Return；不造future/self ref。

## 14. 硬停止

- binding/chat/model/cwd/no-writer/fresh-lock/grant/root不一致；
- 主控outside sentinel receipt缺失或路径已存在；
- fresh program与W006 accepted semantics不等价；
- fresh evaluator任一case/jump/path/equivalence失败；
- restricted child源码包含跨进程holder fdinfo读取；
- parent PRE/POST或composite proof缺失/失败；
- read-only stdin/inherited-FD断言被放宽；
- kernel/bootstrap/probe失败、outside write或unknown write path；
- HOME/CODEX_HOME被重设或承载任务新增写入；
- closure需联网/install或拼resolver；
- 任一预算unknown/不可监测/超cap；
- shared checkout写入；
- 必须改production lifecycle语义；
- 任一scenario被执行；
- normal/DBA/wrapper/native-reader被触发；
- 输出含凭据、大型cache/binary/production data。

## 15. 接收目标

E1应能据W007 Return判断：

1. child non-inheritance与parent holder continuity是否形成完整、分域、可审计证明；
2. same-descriptor FIOCLEX effect与完整九项probe是否PASS；
3. R0-A full trace是否支持global zero outside writes；
4. single compatible offline closure是否闭合；
5. 四预算/continuous monitors是否有非空证据并在cap内；
6. 若四PASS，八EP各自状态与patch边界；
7. fixture是否精确9/18/22且scenario run=0；
8. shared/HOME/CODEX/production是否零任务新增写入；
9. manager可接受前置、修唯一EP、拒绝package或有界停止。

Worker不判断专业接受、action eligibility、G-RUN、H3、父Q或父任务完成。
