# W006｜D003 修正历史 FIOCLEX 阶段分类后的分层静态准备、Phase-0 恢复与条件性八 EP 续作

## 0. 运输身份

- `run_id`：`OI-EAW-WALL-20261114-01`
- `work_order_id`：`W006`
- `issuer_call_id`：`C0014`
- `issuer`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `worker`：`codex:OI-EAW-WALL-20261114-01:worker:W1`
- `return_to`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `delegation_ref`：`daowei2026/observe-iterate@b7200816f86395cd1475ea3a482fc2e63086b967:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`
- `stage_instance_id`：`M-SCENARIO-PRECONDITION-001`
- `work_item_id`：`WI-WALL-SCENARIO-PRECONDITION-001`

本 W 是 W005 正式 STOP 后的**新工单、新实际子根、新锁和新执行资格**。W005 不重开、不修改、不重跑；其 root、lock、turn、命令资格、准备器和冻结原件均不复用。

本 W 只修复 W005 直接证实的 preparation 分层错误：旧 W004 trace 中 policy 安装前 `FIOCLEX=0` 与安装后 `FIOCLEX=EPERM` 是两个阶段，不得要求所有 FIOCLEX 行均为 EPERM。W006 必须把历史分类、本机常量、fresh filter 生成、pure evaluator 与 current kernel attempt 分成不同证据层。

本 W 仍不是 `ARUN-WALL-SCENARIO-001`。禁止运行任一单场景、部分场景或完整九场景；禁止 normal、DBA、wrapper、native-reader、current/production material；禁止共享源码写入或 push。

## 1. 主控派发前 physical binding 与 sentinel 预确认

主控仅在以下全部成立时才可向原 W1 物理聊天发送 W006：

1. `W006` 未占用；
2. 沿用本 Run 已绑定的原 W1 物理聊天，不新建或重建聊天；
3. 针对 W006 重新实核 actual owner、thread/session、model、effort、cwd、idle/queue/no-active-goal；请求配置为 GPT-6.1 Sol Max，以实际回执为准；
4. cwd=`/dwdhome/fy/BASE_E6_2`；
5. W005 的全部 turn/命令/writer 已终态，旧 holder PID 不存在，旧 lock 已释放；
6. 获取 fresh D003 single-writer lock，记录新 holder PID/startticks/inode/session，并用同 inode、new open-file-description 的 `LOCK_EX|LOCK_NB` 竞争失败证明独占；
7. `WORK_ROOT` 派发前不存在，D003/W006 无其他写者；
8. Owner literal grant、当前 D003、W006 MD/JSON与 return route通过V2 Gate；
9. 真实 `HOME`/`CODEX_HOME` 被记录并保持不变，不承载本任务新增写入；
10. 完成 §1.1 精确 outside sentinel 的有界只读预确认并把回执传入 Worker binding。

任一项无法核真，不派发。Worker收到后发现不一致，立即 `STOP`。

### 1.1 主控有界只读 sentinel 预确认

精确路径：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/.W006-deny-outside-C0014-259834ad
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

### 2.2 W006 唯一实际排他写根

```text
WORK_ROOT=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W006
```

所有本任务新增 source、tool script、fixture、tmp、cache、config、build、logs、trace、audit、receipts、artifacts和结果必须在规范化真实 `WORK_ROOT` 内。Owner 根中其他位置也禁止写。

禁止 symlink、bind mount、相对路径、默认目录、继承 writable fd 或环境变量逃逸。任何 actual outside write 立即 STOP 并保留证据。

### 2.3 HOME/CODEX_HOME

- 保持实际值不变；不得重设、迁移或伪装成 WORK_ROOT；
- 只按既有执行绑定读取；
- 不得承载本任务新增业务文件、tmp、cache、config、log或结果；
- 所有可配置任务目录必须显式指向 WORK_ROOT；
- 工具若不能同时满足真实 HOME/CODEX_HOME 和新增写入仅在 WORK_ROOT，STOP，不增加外写例外。

### 2.4 冻结只读输入

- W002/W003/W004/W005 roots与出版原件；
- shared FRP/TIS/worker与local-package roots；
- production wrapper；
- 当前真实HOME/CODEX_HOME；
- `/m3varK`和production products默认完全不访问。

禁止修改、清理、补写、format、build、checkout或push这些路径。

## 3. 精确输入

### 3.1 C0014 与当前 D003

- `daowei2026/observe-iterate@c3bc93de5e389e9cfa397c331389521e66dd9171:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0014/FULL_ASSIGNMENT.md`
- `daowei2026/observe-iterate@2e31272337a1dbd769d8dba80921c58676b83940:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0014/INVOCATION.json`
- `daowei2026/observe-iterate@b7200816f86395cd1475ea3a482fc2e63086b967:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`
- `daowei2026/observe-iterate@461a420bbacc5d24ee093f9f20f2f86653973041:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.md`

### 3.2 W005 正式 STOP 与直接原件

- `daowei2026/observe-iterate@597d813d7c7cc4a8e619326544915131e7bc46c7:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W005/WORKER_RETURN.json`
- `daowei2026/observe-iterate@10e9433477db333ed5d7bf7ac4a1feee508dce44:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W005/WORKER_EXECUTION_REPORT.md`
- 同commit：`ENGINEERING_STOP_REPORT.md`、`FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json`、`SECCOMP_IOCTL_FILTER_DELTA.json`、`SECCOMP_FILTER_STATIC_EVALUATION.json`、`PHASE0_RECOVERY_VERDICT.json`、`WRITE_CONFINEMENT_REPORT.json`、`FULL_WRITE_TRACE_REVIEW.json`、`OFFLINE_CLOSURE_REPORT.json`、`RESOURCE_BUDGET_REPORT.json`、`EP_ACCEPTANCE_MATRIX.md`、`W005_BINDING.json`
- 同commit只读准备器：`tools/prepare_static.py`
- 同commit失败回执：`receipts/STATIC_PREPARATION_FAILURE.json`

### 3.3 W004 历史 filter 与 trace

- `daowei2026/observe-iterate@23b4070f171af4442ddc83b663814f3349739c67:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W004/tools/runtime.py`
- `daowei2026/observe-iterate@23b4070f171af4442ddc83b663814f3349739c67:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W004/tools/landlock_launcher.py`
- `daowei2026/observe-iterate@23b4070f171af4442ddc83b663814f3349739c67:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W004/trace/r0a1.244050`

### 3.4 E1 专业消费与 W006 决定

- `daowei2026/observe-iterate@19da138fcb7e5b020d2c64109695084c7da01b7b:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/D003_W005_PROFESSIONAL_REVIEW_C0014.md`
- `daowei2026/observe-iterate@51668f932251d7f2ae45a16a8bc5907cab9852cc:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/EP_ACCEPTANCE_MATRIX_C0014.md`
- `daowei2026/observe-iterate@88578d7163b44f5d7f42cfd43c5bf0d516122a25:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W006_SUCCESSOR_DECISION_C0014.md`

### 3.5 原工程合同与 exact source

- `daowei2026/observe-iterate@2b872fb3f65d1b40a6f4beb75bff783deac758e6:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/ADDITIONAL_ENGINEERING_PRECONDITION.md`
- `daowei2026/observe-iterate@d8ae5332c94c535d330263ec59bddfbfa3bc52b0:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/CONTROLLED_SCENARIO_ACTION_DESIGN.md`
- `daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13`

## 4. W005 不可覆盖事实

必须原样保留：

```text
W005 outcome=PREFLIGHT_STOP/STOP
termios/header local FIOCLEX=0x5451 agreement
prepare_static.py incorrectly required all historical FIOCLEX lines to contain EPERM
W004 trace line312 pre-policy success and line1509 post-policy EPERM coexist
preparer attempts=1, exit1, no retry
new runtime/launcher/BPF=0
pure evaluator=0
R0-A1=0
R0-B/R0-C/Phase1/2 not entered
four PASS not established
eight EP no new satisfaction
scenario/normal/build/compile/serialization/current material=0
```

禁止把 W005 描述为 static evaluator失败、kernel不支持、request-level filter实测失败、confinement PASS或全局零外写已证。

## 5. P0｜fresh binding 与历史 FIOCLEX 阶段分类

### 5.1 不得复用 W005 准备器

W005 `prepare_static.py`只读冻结。W006在新root编写自己的分层工具；不得在W005 root修一行后重跑，不得复制其硬编码holder/root值后直接执行。

### 5.2 历史 trace 精确分类

生成：

```text
HISTORICAL_FIOCLEX_PHASE_CLASSIFICATION.json
```

要求：

- W004 trace SHA256 必须是 `b2bcd39ff8886fa65815107bd95f333abef1bcb0a1ea69bb20010abc24b2c959`；
- line312 exact text必须为 policy前`FIOCLEX = 0`；
- line1509 exact text必须为 policy后`FIOCLEX = -1 EPERM`；
- 分别标记 `HISTORICAL_PRE_POLICY_SUCCESS` 与 `HISTORICAL_POST_POLICY_DENIAL`；
- 保存所有FIOCLEX行但不要求结果相同；
- 禁止 `all(...EPERM...)`、`every FIOCLEX denied` 或等价 universal assertion；
- 该历史分类不计作W006 current filter结果。

exact SHA/line/text不符：`STOP_HISTORICAL_TRACE_CLASSIFICATION`，不改历史文件。

## 6. P1｜本机常量与 seccomp_data layout

生成：

```text
FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json
SECCOMP_DATA_LAYOUT_VERIFICATION.json
```

要求：

- 至少 Python `termios` 与本机header两个独立来源；
- x86_64/little-endian；
- `FIOCLEX`、`FIONCLEX`均记录；
- `seccomp_data` nr/arch/instruction_pointer/args offsets与64-byte layout来自本机header+ctypes交叉核；
- expected `0x5451`只作参考，本机值为权威；
- 无kernel/filter安装。

不一致：STOP before generation。

## 7. P2｜fresh runtime、launcher 与 candidate filter

W006必须使用actual binding生成自己的：

```text
tools/runtime.py
tools/landlock_launcher.py
PARENT_RUNTIME_BINDING_DELTA.json
SECCOMP_IOCTL_FILTER_DELTA.json
```

### 7.1 Fresh binding

runtime必须写入/读取W006实际root、fresh holder PID/startticks/inode；不得出现W004/W005旧holder值或旧root。runtime启动前静态扫描并报告所有硬编码路径/PID/startticks。

### 7.2 不变安全接线

- parent显式`O_RDONLY|O_CLOEXEC /dev/null` stdin；
- launcher验证fd0只读；
- fd1/2只能是W006 root内single-link regular files；
- 除具名独立lock FD外所有nonstdio inherited FDs在restriction前关闭；
- 主控holder lock保持、竞争仍失败；
- real HOME/CODEX_HOME不变、无task新增写入。

### 7.3 Candidate filter唯一语义delta

相对W004：

```text
ioctl syscall:
  args[1].high32 != 0        -> EPERM
  args[1].low32 == FIOCLEX   -> ALLOW
  otherwise                  -> EPERM
```

其余必须保持：arch、x32、all non-FIOCLEX ioctl deny、PR_SET_NAME deny、network/metadata deny、Landlock handled rights、only W006 root write allow。

`SECCOMP_IOCTL_FILTER_DELTA.json`须逐instruction/offset/jump比较，不得只写自然语言意图。

## 8. P3｜pure static evaluator

任何kernel尝试前运行。输出：

```text
SECCOMP_FILTER_STATIC_EVALUATION.json
```

最低case：

```text
x86_64 ioctl(FIOCLEX)             => ALLOW
x86_64 ioctl(FIONCLEX)            => EPERM
arbitrary ioctl                   => EPERM
request high32 nonzero            => EPERM
existing denied socket            => EPERM
ordinary read                     => ALLOW
x32 ioctl(FIOCLEX)                => EPERM
wrong arch                        => KILL
PR_SET_NAME                       => EPERM
other prctl                       => ALLOW
```

并验证：

- all jumps in bounds；
- all paths terminate in explicit action；
- no unintended fallthrough；
- non-ioctl semantics与W004 baseline等价；
- only verified FIOCLEX case产生预期差异；
- evaluator本身不安装filter、不执行probe。

任一失败：`STOP_SECCOMP_STATIC_EVALUATION`，不启动kernel launcher。

## 9. R0-A1｜单次实际 kernel confinement 与probe

仅P0–P3全部PASS后允许一次。

### 9.1 负向目标

主控预确认：

```text
OUTSIDE=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/.W006-deny-outside-C0014-259834ad
```

Worker复核dispatch receipt，不自行预建。

其他目标在policy前只读核不存在；已存在则STOP、不删除：

```text
SHARED=/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/.W006-deny-shared-C0014-259834ad
HOME=<actual HOME>/.W006-deny-home-C0014-259834ad
CODEX_HOME=<actual CODEX_HOME>/.W006-deny-codex-C0014-259834ad
SYMLINK_TARGET=/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/.W006-deny-symlink-C0014-259834ad
```

### 9.2 必须观察

1. NNP、Landlock ABI/ruleset/add/restrict、seccomp实际安装；
2. second Python bootstrap成功；
3. `FIOCLEX`实际成功并有`F_GETFD & FD_CLOEXEC`证据；
4. inside-root create/write/rename/remove成功；
5. OUTSIDE/SHARED/HOME/CODEX create/write拒绝并仍不存在；
6. child/grandchild继承；
7. symlink escape拒绝；
8. inherited writable FD关闭且holder lock完整；
9. network socket/connect拒绝；
10. full trace覆盖所有probe及每个successful descriptor write路径。

遇到另一bootstrap ioctl/request或其他compatibility缺口：STOP，不扩大allowlist、不自动重试。

## 10. R0-B｜唯一兼容离线closure

仅R0-A PASS后进入。独立评估、只选一套：

```text
E: exact frp stack.yaml / lts-18.28
B: BASE overlay / lts-22.24 / historical GHC9.4.8
```

不得拼接。PASS必须给resolver/compiler/tool hashes、snapshot/global/local package DB、全部required local package exact roots/commits/trees/cabal hashes、transitive package IDs、minimum rebuild set、missing deps空、exact-base compatibility与offline/no-network proof。

所有命令在R0-A restriction下执行；HOME/CODEX_HOME不变，task tmp/cache/config/log显式指向W006 root。允许真正offline的declaration parse、package DB dump、dry dependency plan和有界existing artifact/log index；禁止build/compile/test/download/install/unbounded scan。

两套均不闭合：`RECOVERY_STOP_CLOSURE`。

## 11. R0-C｜四项预算与持续监测

仅R0-A/B PASS后进入。每项必须有非空predicted value/upper bound、同compiler/closure可比实测依据、monitor和stop threshold：

```text
new disk        <= 2 GiB
peak RSS        <= 4 GiB
post-preflight  <= 25 min
new files       <= 50,000
```

进入后继前验证monotonic deadline、whole process-group RSS、root disk/files、descendants、threshold kill/receipt、kernel+trace outside-write覆盖和HOME/CODEX_HOME新增写入0。无可比依据或任一unknown：STOP。

## 12. Phase-0 verdict

只有以下全部PASS：

```text
WRITE_CONFINEMENT_PASS
OFFLINE_CLOSURE_PASS
FOUR_BUDGETS_KNOWN_WITHIN_CAP
CONTINUOUS_MONITORS_PASS
```

才可`ELIGIBLE_FOR_STAGED_CONSTRUCTION`。任一失败：`PREFLIGHT_STOP`，保留独立成功事实，不自动调整/重试，不进入Phase1/2。

## 13. 条件性Phase1/2｜仅四PASS后

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

## 14. W006 原生产物

发布目标：

```text
longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W006/
```

最低产物：

```text
WORKER_EXECUTION_REPORT.md
W006_BINDING.json
CONTROLLER_SENTINEL_PRECONFIRMATION.json
HISTORICAL_FIOCLEX_PHASE_CLASSIFICATION.json
FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json
SECCOMP_DATA_LAYOUT_VERIFICATION.json
PARENT_RUNTIME_BINDING_DELTA.json
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

不造空条件产物，不发布大型source/build/cache/binary/production data。

## 15. Worker Return

正式`WORKER_RETURN.json`必须：

- V2 schema；
- `work_order_id=W006`；
- `return_to=chatgpt:OI-EAW-WALL-20261114-01:executor:E1`；
- outcome如实`EXECUTED/PARTIAL/STOP/FAILED`；
- result_ref指真实出版报告；
- manifest只列实际产物/hash；
- 不把local commit伪装成GitHub ref；
- 不宣称E1接受、G-RUN/H3/action/父任务通过。

无GitHub写权限时，冻结原件交主控逐字出版，再用真实refs生成正式Return；不造future/self ref。

## 16. 硬停止

- binding/chat/model/cwd/no-writer/fresh-lock/grant/root不一致；
- 主控outside sentinel receipt缺失或路径已存在；
- 旧W004 trace SHA/line/text不一致；
- 再次使用all-FIOCLEX-EPERM等价断言；
- local constant/layout不一致；
- fresh runtime包含旧root/PID/startticks；
- seccomp delta超出唯一FIOCLEX request例外；
- pure evaluator任一case、jump、equivalence失败；
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

## 17. 接收目标

E1应能据W006 Return判断：

1. 历史FIOCLEX是否正确按pre/post-policy分层，不再阻断无关static准备；
2. candidate filter是否只有verified FIOCLEX request例外且pure evaluator PASS；
3. kernel confinement与九项probe是否PASS；
4. W002–W005三类高层blocker是否逐项解除；
5. 若四PASS，八EP各自状态与patch边界；
6. fixture是否精确9/18/22且scenario run=0；
7. shared/HOME/CODEX/production是否零任务新增写入；
8. manager可接受前置、修唯一EP、拒绝package或有界停止。

Worker不判断专业接受、action eligibility、G-RUN、H3、父Q或父任务完成。
