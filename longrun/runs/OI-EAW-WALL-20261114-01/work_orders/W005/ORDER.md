# W005｜D003 精确放行 FIOCLEX 后的 Phase-0 恢复与条件性八 EP 续作

## 0. 运输身份

- `run_id`：`OI-EAW-WALL-20261114-01`
- `work_order_id`：`W005`
- `issuer_call_id`：`C0013`
- `issuer`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `worker`：`codex:OI-EAW-WALL-20261114-01:worker:W1`
- `return_to`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `delegation_ref`：`daowei2026/observe-iterate@b7200816f86395cd1475ea3a482fc2e63086b967:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`
- `stage_instance_id`：`M-SCENARIO-PRECONDITION-001`
- `work_item_id`：`WI-WALL-SCENARIO-PRECONDITION-001`

本 W 是 W004 正式 STOP 后的**新工单、新实际子根、新锁和新执行资格**。W004 不重开、不修改、不重跑；其 root、lock、turn、命令资格和冻结原件均不复用。

本 W 只修复 W004 trace 已直接证明的唯一 seccomp compatibility 缺口：保留对其他 `ioctl` 的默认拒绝，只精确允许本机核实的 `FIOCLEX` request，使 Python probe bootstrap 能设置 `FD_CLOEXEC`。不得扩大到任意 `ioctl`，不得通过连续调 policy 直到跑通。

本 W 仍不是 `ARUN-WALL-SCENARIO-001`。禁止运行任一单场景、部分场景或完整九场景；禁止 normal、DBA、wrapper、native-reader、current/production material；禁止共享源码写入或 push。

## 1. 主控派发前 physical binding 与 sentinel 预确认

主控仅在以下全部成立时才可向原 W1 物理聊天发送 W005：

1. `W005` 未占用；
2. 沿用本 Run 已绑定的原 W1 物理聊天，不新建或重建聊天；
3. 针对 W005 重新实核 actual owner、thread/session、model、effort、cwd、idle/queue/no-active-goal；请求配置为 GPT-6.1 Sol Max，以实际回执为准；
4. cwd=`/dwdhome/fy/BASE_E6_2`；
5. W004 两 turn、所有命令和 writer已终态，旧 holder PID不存在，旧 lock已释放；
6. 获取 fresh D003 single-writer lock，记录新 holder PID/startticks/inode/session，并以同 inode、new open-file-description 的 `LOCK_EX|LOCK_NB` 竞争失败证明独占；
7. `WORK_ROOT` 派发前不存在，D003/W005 无其他写者；
8. Owner literal grant、当前 D003、W005 MD/JSON与 return route通过V2 Gate；
9. 真实 `HOME`/`CODEX_HOME` 被记录并保持不变，不承载本任务新增写入；
10. 完成 §1.1 精确 outside sentinel 的有界只读预确认并把回执传入 Worker binding。

任一项无法核真，不派发。Worker收到后发现不一致，立即 `STOP`。

### 1.1 主控有界只读 sentinel 预确认

精确路径：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/.W005-deny-outside-C0013-b6e58ef8
```

主控只执行一次有界只读 `lstat`/等价存在性检查：

```text
result = absent / ENOENT
create = 0
write = 0
delete = 0
cleanup = not needed
```

receipt 至少记录路径、UTC、工具、errno/result和未创建/未写/未删。该确认仅证明负向目标事前不存在，不授予写权限，也不证明kernel会拒绝。

路径已存在或状态unknown：不派发，不删除、不改名。

## 2. Owner grant 与唯一实际写根

### 2.1 Owner grant 原文——逐字保留

```text
operation=wall-observation-work execution_context=linux:/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01
```

### 2.2 W005 唯一实际排他写根

```text
WORK_ROOT=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W005
```

所有本任务新增 source、tool script、fixture、tmp、cache、config、build、logs、trace、audit、receipts、artifacts和结果必须在规范化真实 `WORK_ROOT` 内。Owner根中其他位置也禁止写。

禁止symlink、bind mount、相对路径、默认目录、继承writable fd或环境变量逃逸。任何actual outside write立即STOP并保留证据。

### 2.3 HOME/CODEX_HOME

- 保持实际值不变；不得重设、迁移或伪装成WORK_ROOT；
- 只按既有执行绑定读取；
- 不得承载本任务新增业务文件、tmp、cache、config、log或结果；
- 所有可配置任务目录必须显式指向WORK_ROOT；
- 工具若不能同时满足真实HOME/CODEX_HOME和新增写入仅在WORK_ROOT，STOP，不增加外写例外。

### 2.4 冻结只读输入

- W002/W003/W004 roots与出版原件；
- shared FRP/TIS/worker与local-package roots；
- production wrapper；
- 当前真实HOME/CODEX_HOME；
- `/m3varK`和production products默认完全不访问。

禁止修改、清理、补写、format、build、checkout或push这些路径。

## 3. 精确输入

### 3.1 C0013 与当前 D003

- `daowei2026/observe-iterate@1793a1e7781210a8eb54a0da4440afe10e8f88d1:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0013/FULL_ASSIGNMENT.md`
- `daowei2026/observe-iterate@581de363c1a461457259e3fc602203a87deb1702:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0013/INVOCATION.json`
- `daowei2026/observe-iterate@b7200816f86395cd1475ea3a482fc2e63086b967:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`
- `daowei2026/observe-iterate@461a420bbacc5d24ee093f9f20f2f86653973041:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.md`

### 3.2 W004 正式 STOP 与直接原件

- `daowei2026/observe-iterate@348c61629eced6597f765b8af92c464bc1e56080:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W004/WORKER_RETURN.json`
- `daowei2026/observe-iterate@23b4070f171af4442ddc83b663814f3349739c67:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W004/WORKER_EXECUTION_REPORT.md`
- 同commit：`ENGINEERING_STOP_REPORT.md`、`PHASE0_RECOVERY_VERDICT.json`、`WRITE_CONFINEMENT_REPORT.json`、`FULL_WRITE_TRACE_REVIEW.json`、`PARENT_LAUNCHER_WIRING_DELTA.json`、`W004_BINDING.json`、`OFFLINE_CLOSURE_REPORT.json`、`RESOURCE_BUDGET_REPORT.json`、`EP_ACCEPTANCE_MATRIX.md`
- 同commit只读脚本：`tools/runtime.py`、`tools/landlock_launcher.py`
- 同commit直接trace：`trace/r0a1.244050`

### 3.3 E1 专业消费与 W005 决定

- `daowei2026/observe-iterate@6b6ad47b3b72d88f849ca76c32ab4cfcc9c8fc5c:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/D003_W004_PROFESSIONAL_REVIEW_C0013.md`
- `daowei2026/observe-iterate@c220411b1ef95ce093cfaaa4df09c3dffdb2c5a7:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/EP_ACCEPTANCE_MATRIX_C0013.md`
- `daowei2026/observe-iterate@8a056068b09d32b06dbba8a6700249ee303f2ac2:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W005_SUCCESSOR_DECISION_C0013.md`

### 3.4 原工程合同与 exact source

- `daowei2026/observe-iterate@2b872fb3f65d1b40a6f4beb75bff783deac758e6:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/ADDITIONAL_ENGINEERING_PRECONDITION.md`
- `daowei2026/observe-iterate@d8ae5332c94c535d330263ec59bddfbfa3bc52b0:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/CONTROLLED_SCENARIO_ACTION_DESIGN.md`
- `daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13`

## 4. W004 不可覆盖事实

必须原样保留：

```text
W004 outcome=PREFLIGHT_STOP/STOP
O_RDONLY parent-child stdin and sentinel preconfirmation passed
Landlock ABI6, NNP, create/add/restrict and seccomp install succeeded
second Python execve and script O_RDONLY open/read succeeded
ioctl(FIOCLEX) blocked by blanket ioctl seccomp deny; exit2
probe body/child/grandchild=0
R0-B/R0-C/Phase1/2 not entered
four PASS not established
eight EP no new satisfaction
scenario/normal/compile/serialization/current material=0
```

禁止把W004描述为Landlock不支持、confinement PASS或全局零外写已证。

## 5. R0-A0｜FIOCLEX 常量与 seccomp filter 静态验收

在任何launcher实际执行前，Worker必须在W005 root生成自己的runtime/launcher/BPF evaluator，不修改W004脚本。

### 5.1 FIOCLEX 本地常量核验

使用当前x86_64 Linux本地stdlib/header的只读信息，至少两种独立方式交叉核：

- Python stdlib `termios.FIOCLEX`（如暴露）；
- `/usr/include` 中的本机相关header定义或等价本地constant source；
- W004 trace symbolic `FIOCLEX` 仅作第三交叉来源。

记录：

```text
symbolic name
integer decimal/hex
source path/module
source file hash/bytes
architecture
endianness
agreement/disagreement
```

预期值可为`0x5451`，但本地核对结果为权威。无法取得至少一个权威本地定义并与trace request一致：`STOP_FIOCLEX_CONSTANT_UNVERIFIED`。

只读header/module检查不得写HOME/CODEX_HOME或生成pycache。

### 5.2 唯一 policy delta

保留W004所有arch/x32/denied syscall/PR_SET_NAME/Landlock rights与write root规则。对`ioctl`改为request分支：

```text
non-ioctl syscall:
    existing W004 behavior

ioctl syscall:
    load seccomp_data.args[1] upper/lower 32 bits
    upper != 0         -> EPERM
    lower == FIOCLEX   -> ALLOW
    otherwise          -> EPERM
```

不允许：

- 删除`ioctl`控制；
- 允许`FIONCLEX`；
- 允许termios/device arbitrary request；
- 按fd路径或fd号做脆弱例外；
- 放宽Landlock `IOCTL_DEV` handled right；
- 改写其他deny或network policy。

生成：

```text
SECCOMP_IOCTL_FILTER_DELTA.json
```

逐行/逐instruction比较W004与W005，说明offset、endianness、jump target和最终action。

### 5.3 Pure static evaluator

在不安装filter、不执行probe的纯 evaluator中覆盖：

```text
x86_64 + ioctl(FIOCLEX)                 => ALLOW
x86_64 + ioctl(FIONCLEX)                => EPERM
x86_64 + ioctl(arbitrary)               => EPERM
x86_64 + ioctl(request upper32 != 0)     => EPERM
x86_64 + existing denied socket         => EPERM
x86_64 + ordinary allowed syscall       => ALLOW
x86_64 + x32 syscall bit                => EPERM
wrong arch                              => KILL
```

同时验证每个BPF jump落在program内，没有fall-through意外允许。输出：

```text
SECCOMP_FILTER_STATIC_EVALUATION.json
```

任一case不符、offset/arch/endianness不明确或delta超出唯一request例外：`STOP_SECCOMP_STATIC_EVALUATION`，不启动launcher。

## 6. R0-A1｜单次实际kernel confinement与probe

静态验收PASS后只允许一次实际R0-A1。

### 6.1 Parent/launcher

- parent继续显式`O_RDONLY|O_CLOEXEC /dev/null` stdin；
- launcher fd0只读断言和所有inherited-FD规则保持；
- 独立writable lock fd关闭但主控holder保持；
- NNP/Landlock/seccomp安装与receipt完整；
- 只允许locally verified `FIOCLEX` request；
- `FIOCLEX`实际返回成功并使descriptor具`FD_CLOEXEC`，保留trace与`F_GETFD`证据；
- 遇到另一ioctl/bootstrap incompatibility立即STOP，不修改filter重试。

### 6.2 负向目标

主控预确认：

```text
OUTSIDE=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/.W005-deny-outside-C0013-b6e58ef8
```

Worker复核dispatch receipt，不自行预创建。

以下目标在policy安装前只读核不存在；已存在则STOP、不删除：

```text
SHARED=/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/.W005-deny-shared-C0013-b6e58ef8
HOME=<actual HOME>/.W005-deny-home-C0013-b6e58ef8
CODEX_HOME=<actual CODEX_HOME>/.W005-deny-codex-C0013-b6e58ef8
SYMLINK_TARGET=/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/.W005-deny-symlink-C0013-b6e58ef8
```

### 6.3 九项probe

1. inside-root create/write/rename/remove成功；
2. OUTSIDE create/write被kernel拒绝，执行后仍不存在；
3. SHARED新文件create在open阶段拒绝；
4. HOME/CODEX_HOME保持真实值，read允许，new create拒绝；
5. child/grandchild继承restriction；
6. symlink escape拒绝；
7. inherited writableFD已关闭，holder lock仍完整；
8. network socket/connect拒绝或由实际policy/trace给等价证明；
9. 全部probe由full trace覆盖。

### 6.4 Full trace

绑定absolute `strace`/等价工具与hash，`-ff -yy`覆盖open/read/write/mmap/truncate/rename/link/unlink/mkdir/metadata/fd/fork/exec/network/ioctl等。每个成功descriptor write映射路径；任一unknown即STOP。

`/proc/self/task/*/comm`：

- open无write：记录；
- write被policy拒绝：记录；
- 成功write：outside write非零并STOP；
- 不自行豁免。

## 7. R0-B｜唯一兼容离线closure

仅R0-A PASS后进入。独立评估、只选一套：

```text
E: exact frp stack.yaml / lts-18.28
B: BASE overlay / lts-22.24 / historical GHC9.4.8
```

不得拼接。PASS必须给resolver/compiler/tool hashes、snapshot/global/local package DB、全部required local package exact roots/commits/trees/cabal hashes、transitive package IDs、minimum rebuild set、missing deps空、exact-base compatibility与offline/no-network proof。

所有命令在R0-A restriction下执行；HOME/CODEX_HOME不变，task tmp/cache/config/log显式指向W005 root。允许真正offline的declaration parse、package DB dump、dry dependency plan和有界existing artifact/log index；禁止build/compile/test/download/install/unbounded scan。

两套均不闭合：`RECOVERY_STOP_CLOSURE`。

## 8. R0-C｜四项预算与持续监测

仅R0-A/B PASS后进入。每项必须有非空predicted value/upper bound、同compiler/closure可比实测依据、monitor和stop threshold：

```text
new disk        <= 2 GiB
peak RSS        <= 4 GiB
post-preflight  <= 25 min
new files       <= 50,000
```

进入后继前验证monotonic deadline、whole process-group RSS、root disk/files、descendants、threshold kill/receipt、kernel+trace outside-write覆盖和HOME/CODEX_HOME新增写入0。无可比依据或任一unknown：STOP。

## 9. Phase-0 verdict

只有以下全部PASS：

```text
WRITE_CONFINEMENT_PASS
OFFLINE_CLOSURE_PASS
FOUR_BUDGETS_KNOWN_WITHIN_CAP
CONTINUOUS_MONITORS_PASS
```

才可`ELIGIBLE_FOR_STAGED_CONSTRUCTION`。任一失败：`PREFLIGHT_STOP`，保留独立成功事实，不自动调整/重试，不进入Phase1/2。

## 10. 条件性Phase1/2｜仅四PASS后

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

## 11. W005 原生产物

发布目标：

```text
longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W005/
```

最低产物：

```text
WORKER_EXECUTION_REPORT.md
W005_BINDING.json
CONTROLLER_SENTINEL_PRECONFIRMATION.json
SECCOMP_IOCTL_FILTER_DELTA.json
SECCOMP_FILTER_STATIC_EVALUATION.json
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

不造空文件，不发布大型source/build/cache/binary/production data。

## 12. Worker Return

正式`WORKER_RETURN.json`必须：

- V2 schema；
- `work_order_id=W005`；
- `return_to=chatgpt:OI-EAW-WALL-20261114-01:executor:E1`；
- outcome如实`EXECUTED/PARTIAL/STOP/FAILED`；
- result_ref指真实出版报告；
- manifest只列实际产物/hash；
- 不把local commit伪装成GitHub ref；
- 不宣称E1接受、G-RUN/H3/action/父任务通过。

无GitHub写权限时，冻结原件交主控逐字出版，再用真实refs生成正式Return；不造future/self ref。

## 13. 硬停止

- binding/chat/model/cwd/no-writer/fresh-lock/grant/root不一致；
- 主控outside sentinel receipt缺失或路径已存在；
- FIOCLEX本地常量不能核对；
- seccomp delta超出唯一request例外或static evaluator失败；
- 使用任意ioctl allowlist；
- read-only stdin/inherited-FD断言被放宽；
- FIOCLEX仍失败或出现另一bootstrap incompatibility；
- probe失败、outside write、unknown write path；
- HOME/CODEX_HOME被重设或承载任务新增写入；
- closure需联网/install或拼resolver；
- 任一预算unknown/不可监测/超cap；
- shared checkout写入；
- 必须改production lifecycle语义；
- 任一scenario被执行；
- normal/DBA/wrapper/native-reader被触发；
- 输出含凭据、大型cache/binary/production data。

## 14. 接收目标

E1应能据W005 Return判断：

1. FIOCLEX是否以最小request粒度放行且其他ioctl仍拒绝；
2. kernel confinement与九项probe是否PASS；
3. W002/W003/W004三类高层blocker是否逐项解除；
4. 若四PASS，八EP各自状态与patch边界；
5. fixture是否精确9/18/22且scenario run=0；
6. shared/HOME/CODEX/production是否零任务新增写入；
7. manager可接受前置、修唯一EP、拒绝package或有界停止。

Worker不判断专业接受、action eligibility、G-RUN、H3、父Q或父任务完成。
