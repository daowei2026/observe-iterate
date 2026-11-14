# W004｜D003 修正只读 stdin 接线后的 Phase-0 恢复与条件性八 EP 续作

## 0. 运输身份

- `run_id`：`OI-EAW-WALL-20261114-01`
- `work_order_id`：`W004`
- `issuer_call_id`：`C0012`
- `issuer`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `worker`：`codex:OI-EAW-WALL-20261114-01:worker:W1`
- `return_to`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `delegation_ref`：`daowei2026/observe-iterate@b7200816f86395cd1475ea3a482fc2e63086b967:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`
- `stage_instance_id`：`M-SCENARIO-PRECONDITION-001`
- `work_item_id`：`WI-WALL-SCENARIO-PRECONDITION-001`

本 W 是 W003 正式 STOP 后的**新工单、新实际子根、新锁和新执行资格**。它只修正两个有直接证据的接线前置：

1. 父 runtime 为 launcher 提供显式 `O_RDONLY /dev/null`，不再使用 `subprocess.DEVNULL`；
2. 主控派发前只读确认具名 outside sentinel 不存在。

W003 不重开、不修改、不重跑；其 root、lock、turn、命令资格和冻结原件均不复用。其 launcher/runtime可作为只读证据输入，W004必须在新root形成自己的实现和回执。

本 W 仍不是 `ARUN-WALL-SCENARIO-001`。禁止运行任一单场景、部分场景或完整九场景；禁止 normal、DBA、wrapper、native-reader、current business material；禁止共享源码写入或push。

## 1. 主控派发前必须核真的 physical binding

主控只有在以下全部成立时才可向原 W1 物理聊天发送 W004：

1. `W004` 未被占用；
2. 沿用本 Run 已绑定的原 W1 物理聊天，不新建或重建聊天；
3. 对 W004 重新实核 actual owner、thread/session、model、effort、cwd、idle/queue/no-active-goal；请求配置为 GPT-6.1 Sol Max，以实际回执为准；
4. cwd=`/dwdhome/fy/BASE_E6_2`；
5. W003 已 completed、全部命令终态、旧lock释放、旧holder PID不存在；
6. 获取 fresh D003 single-writer lock，记录新 holder PID/startticks/inode/session，并对同 inode/new open-file-description做 `LOCK_EX|LOCK_NB` 竞争失败证明；
7. `WORK_ROOT` 在本次派发前不存在，且 D003/W004 无其他写者；
8. Owner literal grant、当前 D003、W004 MD/JSON和return route通过V2 Gate；
9. 真实 `HOME`/`CODEX_HOME` 已记录并保持不变；不得承载本任务新增写入；
10. 完成 §1.1 sentinel只读预确认并出版/传入 Worker binding。

任一无法核真，不派发。Worker收到后发现不一致，直接 `STOP`。

### 1.1 主控有界只读预确认：唯一外部 sentinel

精确路径：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/.W004-deny-outside-C0012-e9ed948d
```

主控只能执行有界只读 `lstat`/等价存在性检查，要求：

```text
result = absent / ENOENT
create = 0
write = 0
cleanup = not needed
```

主控必须把路径、检查时间、工具、结果和“未创建”写入 dispatch/binding receipt。该确认只证明负向测试目标事先不存在，不授权W004在该路径写入，也不证明kernel会拒绝。

若路径已存在或状态unknown，不派发，不删除、不改名。

## 2. Owner grant 与唯一实际写根

### 2.1 Owner grant原文——逐字保留

```text
operation=wall-observation-work execution_context=linux:/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01
```

### 2.2 W004唯一实际排他写根

```text
WORK_ROOT=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W004
```

所有本任务新增 source、tool script、fixture、tmp、cache、config、build、logs、trace、audit、receipts、artifacts和结果必须位于规范化真实 `WORK_ROOT` 内。Owner根中其他位置也禁止写。

禁止symlink、bind mount、相对路径、工具默认目录、继承writable fd或环境变量逃逸。任何actual outside write立即STOP并保留证据。

### 2.3 HOME/CODEX_HOME

- 保持实际值不变；不得重设、迁移或伪装成WORK_ROOT；
- 仅按既有执行绑定读取；
- 不得承载本任务新增业务文件、tmp、cache、config、log或结果；
- 所有工具可配置任务目录必须通过显式选项指向WORK_ROOT；
- 若任一工具无法同时满足真实HOME/CODEX_HOME和新增写入只在WORK_ROOT，STOP；不得增加外写例外。

### 2.4 冻结只读输入

- W002/W003 roots与出版原件；
- shared FRP/TIS/worker与local-package roots；
- production wrapper；
- 当前真实HOME/CODEX_HOME；
- `/m3varK`和production products默认完全不访问。

禁止修改、清理、补写、format、build、checkout或push这些路径。

## 3. 精确输入

### 3.1 当前C0012与D003

- `daowei2026/observe-iterate@9076e41ad5beeb09a0cdd84b57794f2664162716:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0012/FULL_ASSIGNMENT.md`
- `daowei2026/observe-iterate@9c8ec64ccbd02dc90a828482d7ae6337cc605659:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0012/INVOCATION.json`
- `daowei2026/observe-iterate@b7200816f86395cd1475ea3a482fc2e63086b967:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`
- `daowei2026/observe-iterate@461a420bbacc5d24ee093f9f20f2f86653973041:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.md`

### 3.2 W003正式STOP与直接工程原件

- `daowei2026/observe-iterate@e124f5662e4c683ee6abe572b78c6a8de15d4d3e:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W003/WORKER_RETURN.json`
- `daowei2026/observe-iterate@9aaaf4a3b322333b46f33b9e55c916b4cea1b1e3:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W003/WORKER_EXECUTION_REPORT.md`
- 同commit：`ENGINEERING_STOP_REPORT.md`、`PHASE0_RECOVERY_VERDICT.json`、`WRITE_CONFINEMENT_REPORT.json`、`FULL_WRITE_TRACE_REVIEW.json`、`W003_BINDING.json`、`R0A_EXECUTION_PLAN.json`、`OFFLINE_CLOSURE_REPORT.json`、`RESOURCE_BUDGET_REPORT.json`、`EP_ACCEPTANCE_MATRIX.md`
- 同commit只读工程脚本：`tools/runtime.py`、`tools/landlock_launcher.py`

### 3.3 E1专业消费与W004决定

- `daowei2026/observe-iterate@d883c9fd7b430d991b7bef9c5f303aa46071d062:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/D003_W003_PROFESSIONAL_REVIEW_C0012.md`
- `daowei2026/observe-iterate@a9cc7533b0f131aa5ff1e74eb00f1110c8fb0ca2:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/EP_ACCEPTANCE_MATRIX_C0012.md`
- `daowei2026/observe-iterate@dc28c18212e1549a35b920e2ebdd42668f20b048:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W004_SUCCESSOR_DECISION_C0012.md`

### 3.4 原工程合同与exact source

- `daowei2026/observe-iterate@2b872fb3f65d1b40a6f4beb75bff783deac758e6:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/ADDITIONAL_ENGINEERING_PRECONDITION.md`
- `daowei2026/observe-iterate@d8ae5332c94c535d330263ec59bddfbfa3bc52b0:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/CONTROLLED_SCENARIO_ACTION_DESIGN.md`
- `daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13`

## 4. W003 STOP不可覆盖事实

必须原样保留：

```text
W003 outcome=PREFLIGHT_STOP/STOP
launcher exit73 at pre-enforcement inherited-FD inspection
fd0=/dev/null O_RDWR due parent subprocess.DEVNULL
NNP/Landlock/seccomp calls=0
probe/child=0
R0-B/R0-C/Phase1/2 not entered
four PASS all false/not attempted
eight EP no new satisfaction
scenario/normal/compile/serialization/current material=0
```

禁止称W003证明Landlock不支持；禁止称failed trace outside writes 0为global confinement PASS。

## 5. R0-A0｜W004接线修复静态验收

在调用launcher前，Worker必须在W004 root形成并审查新 `runtime.py`/等价父执行器；不得修改W003脚本。

### 5.1 read-only stdin精确要求

父runtime必须采用等价于：

```python
stdin_fd = os.open('/dev/null', os.O_RDONLY | os.O_CLOEXEC)
flags = fcntl.fcntl(stdin_fd, fcntl.F_GETFL)
assert (flags & os.O_ACCMODE) == os.O_RDONLY
try:
    child = subprocess.Popen(
        argv,
        stdin=stdin_fd,
        ...
    )
finally:
    os.close(stdin_fd)
```

必须在父receipt中保存：

```text
opened path
F_GETFL raw flags
access mode = O_RDONLY
parent fd number
child pid
parent close timestamp/result
```

禁止：

- `stdin=subprocess.DEVNULL`；
- writable pipe/file作fd0；
- 删除launcher的fd0 read-only断言；
- launcher静默修复任意writable fd0后继续；
- 为`/dev/null`增加write例外。

launcher应实测child fd0 path/flags，只有read-only才进入policy安装。

### 5.2 inherited lock FD

fresh D003 lock的holder不得由Worker修改/释放。若需要传入一个“应被launcher关闭”的writable lock FD，必须是独立open-file-description且未取得lock；记录path/flags/inode，launcher关闭后证明holder lock仍在、竞争仍失败。

### 5.3 static delta report

生成：

```text
PARENT_LAUNCHER_WIRING_DELTA.json
```

逐行比较W003与W004父runtime相关差异，证明只修stdin/receipt/new-root/binding，不放宽launcher安全断言或业务禁令。

若静态审查仍发现`subprocess.DEVNULL`或fd0 mode不可证明，`STOP_W004_STDIN_WIRING`，不得启动launcher。

## 6. R0-A1｜kernel write confinement与完整审计

### 6.1 Run-local launcher

可从W003候选只读复制后在W004 root形成自己的hash版本。仍使用Python `-I -S -B` + stdlib ctypes；禁止编译helper、安装包或联网。

必须：

- `PR_SET_NO_NEW_PRIVS`；
- 查询并记录实际Landlock ABI；
- 只有实际ABI满足该实现所需rights时继续，否则以具体ABI/right事实STOP；
- handled rights覆盖可用的write/create/remove/rename/refer/truncate等；
- only W004 root为write allow path；
- 全局read允许；
- restriction在exec前生效并传给子孙；
- 不给`/proc`、`/tmp`、HOME、CODEX_HOME、shared、production增加write例外；
- seccomp/等价机制处理Landlock未覆盖的metadata mutation和network；
- receipt记录所有syscall return/errno和policy内容。

若ABI/rule/seccomp失败，不笼统写“kernel不支持”；准确给实际API、errno、right和阶段。

### 6.2 负向目标

主控预确认路径：

```text
OUTSIDE=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/.W004-deny-outside-C0012-e9ed948d
```

Worker在policy安装前复核dispatch receipt，不重新创建。

其他目标先只读确认不存在，已存在即STOP、不删除：

```text
SHARED=/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/.W004-deny-shared-C0012-e9ed948d
HOME=/home/dw/.W004-deny-home-C0012-e9ed948d
CODEX_HOME=/home/dw/.codex/.W004-deny-codex-C0012-e9ed948d
SYMLINK_TARGET=/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/.W004-deny-symlink-C0012-e9ed948d
```

### 6.3 必须通过的probe

1. inside-root create/write/rename/remove成功；
2. OUTSIDE create/write被kernel拒绝且仍不存在；
3. SHARED新文件create在open阶段拒绝；
4. 真实HOME/CODEX_HOME不变、read允许、本任务new create拒绝；
5. child/grandchild继承限制；
6. symlink escape拒绝；
7. inherited writable FD已关闭，holder lock仍完整；
8. network socket/connect被拒绝或全后继offline有等价证明；
9. 所有probe由完整trace覆盖。

### 6.4 full trace

绑定absolute `strace`/等价工具与hash，使用 `-ff -yy` 并覆盖所有open/write/mmap/truncate/rename/link/unlink/mkdir/metadata/fd/fork/exec/network syscalls。每个成功descriptor write必须映射到路径；任一unknown即STOP。

`/proc/self/task/*/comm`：

- open无write：记录；
- write被policy拒绝：记录；
- 成功write：outside write非零并STOP；
- 不自行豁免。

## 7. R0-B｜唯一兼容离线closure

仅R0-A PASS后进入。

独立评估、只选一套：

```text
E: exact frp stack.yaml / lts-18.28
B: BASE overlay / lts-22.24 / historical GHC9.4.8
```

不得拼接。PASS必须给：

- resolver/compiler exact version/hash；
- Stack/Cabal/GHC absolute path/hash；
- snapshot/global/local package DB path/hash/size；
- all required local package root/HEAD/tree/cabal hash；
- transitive package ids/versions；
- proposed scenario target minimum rebuild set；
- missing deps空；
- exact-base compatibility；
- offline/no-network proof。

所有命令在R0-A restriction下执行，真实HOME/CODEX_HOME不变，task tmp/cache/config/log显式指向W004 root。允许真正offline的declaration parse/package DB dump/dry dependency plan和有界existing artifact/log索引；禁止build/compile/test/download/install/unbounded scan。

两套均不闭合：`RECOVERY_STOP_CLOSURE`。

## 8. R0-C｜四项预算与持续监测

仅R0-A/B PASS后进入。

每项必须有非空predicted value/upper bound、同compiler/closure可比实测依据、monitor和stop threshold：

```text
new disk        <= 2 GiB
peak RSS        <= 4 GiB
post-preflight  <= 25 min
new files       <= 50,000
```

进入后继前验证：

- monotonic deadline；
- whole process-group RSS；
- W004 root disk/files；
- all descendants；
- threshold杀停process group并保留receipt；
- kernel+trace持续覆盖outside writes；
- HOME/CODEX_HOME新增写入0。

没有可比真实依据或任一unknown：STOP。固定cap不是预测；版本查询不是预算。

## 9. Phase-0 verdict

只有以下全部PASS：

```text
WRITE_CONFINEMENT_PASS
OFFLINE_CLOSURE_PASS
FOUR_BUDGETS_KNOWN_WITHIN_CAP
CONTINUOUS_MONITORS_PASS
```

才写：

```text
ELIGIBLE_FOR_STAGED_CONSTRUCTION
```

任一失败：`PREFLIGHT_STOP`，保留独立成功子事实，不自动调整/重试，不进入Phase1/2。

## 10. 条件性Phase1/2｜仅四PASS后

实施原八EP：

```text
EP-WALL-SHARED-01..03
EP-SCENARIO-01..05
```

要求：

- exact-base clean staged source；
- state snapshot直接来自production lifecycle state；
- versioned one-record-per-firing DTO/schema；
- rejected formal post=pre、O/C空；intermediate只标UNCOMMITTED_DEBUG；
- dedicated `frp:eaw-p1-wall-scenario-evidence` target只建设；
- fixture精确9 scenarios/18 firings/22 inputs；
- fixture只做parse/count/order/hash；
- exact-error/transaction record只做direct synthetic serialization；
- W002/C0010 conflict ledger进入target manifest；
- patch/local commit为Run artifact并标`NOT_UPSTREAM_PUBLISHED`；
- compile-only/serialization仅在cap和write audit内；
- 不改变production lifecycle语义或旧test assertion。

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

## 11. W004原生产物

发布目标：

```text
longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W004/
```

最低产物：

```text
WORKER_EXECUTION_REPORT.md
W004_BINDING.json
CONTROLLER_SENTINEL_PRECONFIRMATION.json
PARENT_LAUNCHER_WIRING_DELTA.json
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

若STOP：

```text
ENGINEERING_STOP_REPORT.md
```

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

不造空文件，不发布大型source/build/cache/binary/生产数据。manifest记录本地tree path/size/hash/retention。

## 12. Worker Return

正式`WORKER_RETURN.json`必须：

- V2 schema；
- `work_order_id=W004`；
- `return_to=chatgpt:OI-EAW-WALL-20261114-01:executor:E1`；
- outcome如实`EXECUTED/PARTIAL/STOP/FAILED`；
- result_ref指真实出版报告；
- manifest只列实际产物/hash；
- 不把local commit伪装成GitHub ref；
- 不宣称E1接受、G-RUN/H3/action/父任务通过。

无GitHub写权限时，冻结原件交主控逐字出版，再用真实refs生成正式Return；不造future/self ref。

## 13. 硬停止

- binding/chat/model/cwd/no-writer/fresh-lock/grant/root不一致；
- 主控outside sentinel absent receipt缺失或路径已存在；
- 使用`subprocess.DEVNULL`或fd0非O_RDONLY；
- 删除/放宽launcher inherited-FD check；
- Landlock/等价方案无kernel enforcement；
- probe失败、outside write、unknown write path；
- HOME/CODEX_HOME被重设或承载任务新增写入；
- closure需联网/install或拼接resolver；
- 任一预算unknown/不可监测/超cap；
- shared checkout写入；
- 必须改变production lifecycle语义；
- 任何scenario被执行；
- normal/DBA/wrapper/native-reader被触发；
- 输出含凭据、大型cache/binary/production data。

## 14. 接收目标

E1应能据W004 Return判断：

1. read-only stdin接线是否真实修复而未放宽安全断言；
2. kernel confinement与全trace是否PASS；
3. W002/W003三类高层blocker是否逐项解除；
4. 若四PASS，八EP各自状态和patch边界；
5. fixture是否精确9/18/22且scenario run=0；
6. shared/HOME/CODEX/production是否零任务新增写入；
7. manager可接受前置、修唯一EP、拒绝package或有界停止。

Worker不判断专业接受、action eligibility、G-RUN、H3、父Q或父任务完成。
