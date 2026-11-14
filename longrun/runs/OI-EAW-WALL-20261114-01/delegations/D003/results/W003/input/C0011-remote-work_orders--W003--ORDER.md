# W003｜D003 Phase-0 三阻断恢复与条件性八 EP 工程续作

## 0. 运输身份

- `run_id`：`OI-EAW-WALL-20261114-01`
- `work_order_id`：`W003`
- `issuer_call_id`：`C0011`
- `issuer`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `worker`：`codex:OI-EAW-WALL-20261114-01:worker:W1`
- `return_to`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `delegation_ref`：`daowei2026/observe-iterate@b7200816f86395cd1475ea3a482fc2e63086b967:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`
- `stage_instance_id`：`M-SCENARIO-PRECONDITION-001`
- `work_item_id`：`WI-WALL-SCENARIO-PRECONDITION-001`

本 W 是 W002 正式 STOP 后的**新方法、独立子根、精确阻断恢复**，不是 W002 重发、重开或证据覆盖。沿用本 Run 已绑定的原 W1 物理聊天，不创建或重建 Worker 聊天；但在 W003 派发前必须重新实核当前 owner、thread/session、model/effort、cwd、无旧写者与新独占。W002 的锁会话、执行资格、命令资格、工程目录和冻结原件均不复用。

本 C0011 修签只替代从未派发、从未建锁、从未启动 Worker 的 C0010 W003 候选：

- 原 ORDER MD：`daowei2026/observe-iterate@f3d4b60ee499875c02b1fa7ebe8d15666a4951c2:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W003/ORDER.md`
- 原 ORDER JSON：`daowei2026/observe-iterate@35eeb0414cf71963938bcbf97afc744bff72ef8c:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W003/ORDER.json`

本 W 仍不是 `ARUN-WALL-SCENARIO-001`。禁止运行九场景／部分场景／单场景 evidence action，禁止 normal、DBA、wrapper、native-reader，禁止修改共享源码或 push。

## 1. 派发前主控必须核真

主控只有在以下全部成立时才可发送本 W：

1. `W003` 未被占用；
2. 真实 Worker 逻辑身份为 Binding 批准的 W1，且使用本 Run 已绑定的原 W1 物理聊天；不得新建或重建 Worker 聊天；
3. 对当前 W003 重新实核实际 owner、thread/session、model、effort、cwd；请求配置为 GPT-6.1 Sol Max，但以主控实测为准，不得继承 W002 的资格记录；
4. cwd 为 `/dwdhome/fy/BASE_E6_2`；
5. W002 已封存、无活跃写者、旧锁已释放，W002 锁会话和执行资格不延续；
6. W003 新 single-writer lock 覆盖 W003 实际子根，并证明当前没有旧写者；
7. Owner grant、当前 D003、W003 JSON/MD 字面路由通过 V2 Gate；
8. D003/W003 子根没有并发写者；
9. 当前真实 `HOME` 与 `CODEX_HOME` 已记录并保持不变；二者不承载本任务新增业务写入。

任一无法核真，不派发。Worker 收到后发现不一致则 `STOP`。

## 2. Owner grant 与唯一实际写根

### 2.1 Owner grant 原文——必须逐字使用

```text
operation=wall-observation-work execution_context=linux:/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01
```

### 2.2 W003 唯一实际排他写根

```text
WORK_ROOT=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W003
```

所有本任务新增的 source、fixture、tool script、tmp、task cache、tool config、build、logs、audit、receipts 和 artifacts 必须位于规范化真实 `WORK_ROOT` 内。Owner root 中其他位置也禁止写。

现有执行绑定中的 `HOME` 与 `CODEX_HOME` 必须保持真实值不变，不得重设、迁移或伪装成 `WORK_ROOT`；它们仅可按既有执行绑定读取，不得承载本任务新增业务文件、tmp、cache、config、log 或结果。所有可配置的任务临时目录、缓存与工具配置必须通过工具支持的显式选项定向到 `WORK_ROOT`。若任一工具无法同时满足“真实 `HOME/CODEX_HOME` 保持不变”和“新增写入只发生在 `WORK_ROOT`”，立即准确 `STOP`；不得通过改写 HOME、增加外写例外或放宽 cap 绕过。

禁止通过 symlink、bind mount、相对路径、继承 writable fd 或工具默认目录逃逸。发现任何实际外写，立即停止并保留证据。

### 2.3 只读路径

- shared FRP：`/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp`
- W002 frozen local/evidence root：只读；不得覆盖、清理或新增
- 当前真实 `HOME`／`CODEX_HOME`：保持原值、业务只读；不得写本任务新增内容
- 其他 BASE local-package roots：仅在明确 closure 调查范围内只读
- `/m3varK`、production products：禁止 stat/traverse/read/write，除非 D003 已明确的单文件 before/after proof；本 W 默认完全不访问
- production wrapper：只允许既定 hash/mtime before/after，不生成、不 import

## 3. 精确输入

### 3.1 C0011 修签与当前 D003

- `daowei2026/observe-iterate@84551f72b3a5dda03b4fb98434cb854168518fa6:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0011/FULL_ASSIGNMENT.md`
- `daowei2026/observe-iterate@32684eb7a9a65e494d2f8853b1110fff6d37a74e:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0011/INVOCATION.json`
- `daowei2026/observe-iterate@9ca270a900560993a176e864b5a3841e54fe332d:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0011/W003_EXECUTION_BINDING_FEEDBACK.json`
- `daowei2026/observe-iterate@62f4c2feca9cf0922522a1c05a8cc1695d062395:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0010/PRO_RETURN.json`
- `daowei2026/observe-iterate@461a420bbacc5d24ee093f9f20f2f86653973041:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.md`
- `daowei2026/observe-iterate@b7200816f86395cd1475ea3a482fc2e63086b967:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`

### 3.2 W002 正式 STOP——不可覆盖输入

- `daowei2026/observe-iterate@9bce93fcd7bbd0c91a08c0ace86b332e55b9f629:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W002/WORKER_RETURN.json`
- `daowei2026/observe-iterate@2af8a364b4157958b59d68ab4fc24eb6a95f5593:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W002/WORKER_EXECUTION_REPORT.md`
- 同 commit 的 `DRY_DEPENDENCY_PREFLIGHT.json`、`WRITE_SURFACE_PLAN.json`、`WRITE_SURFACE_AUDIT.json`、`SOURCE_BASELINE_REPORT.md`、`EP_ACCEPTANCE_MATRIX.md`、`ENGINEERING_STOP_REPORT.md`、`KNOWN_CONTRACT_CONFLICTS.md`、`LOCAL_STAGE_HANDOFF.json`

### 3.3 E1 专业处理与恢复合同

- `daowei2026/observe-iterate@ce5844e7f860d4fea17c14645fcf53ac43fac26c:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/D003_W002_PROFESSIONAL_REVIEW.md`
- `daowei2026/observe-iterate@f38f697992feb015b7eeba5858d35c39692665c2:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/EP_ACCEPTANCE_MATRIX_C0010.md`
- `daowei2026/observe-iterate@b5a14228d13f317ad415ef939caa61d29e145a78:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/PHASE0_RECOVERY_PLAN_C0010.md`

### 3.4 D002 原始工程合同与 exact source

- `daowei2026/observe-iterate@2b872fb3f65d1b40a6f4beb75bff783deac758e6:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/ADDITIONAL_ENGINEERING_PRECONDITION.md`
- `daowei2026/observe-iterate@d8ae5332c94c535d330263ec59bddfbfa3bc52b0:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/CONTROLLED_SCENARIO_ACTION_DESIGN.md`
- `daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13`

## 4. 不得重复 W002 的方法

禁止：

- 再跑两个已失败 bwrap probe；
- 用缺少 write-family 的 trace 声称零外写；
- 只查版本就声称 build 预算；
- 浅层 cache index 后声称 closure 完整；
- 把 exact lts-18.28 与 BASE lts-22.24 的部分信息拼成一个环境；
- 重用 W002 source/fixture/tests/build/stack-root；
- 修改或补写 W002 原件；
- 在 Phase-0 未通过时进入 staged source construction。

## 5. Recovery Phase R0-A｜kernel write confinement 与完整写审计

### 5.1 Run-local launcher

优先使用 W002 已核 ABI=6 的 Landlock。允许在 `WORK_ROOT/tools/` 创建 Python `-I -S -B` + stdlib `ctypes` launcher；禁止编译 helper、安装包或联网。

launcher 必须：

- `PR_SET_NO_NEW_PRIVS`；
- handled rights覆盖 write/create/remove/rename/refer/truncate 等适用于 ABI6 的写能力；
- 只对 `WORK_ROOT` 增加 write allow rule；
- 全局 read保持可用；
- restriction 在 exec 前生效并由 child/grandchild继承；
- 不给 `/proc`、`/tmp`、真实 `HOME`、真实 `CODEX_HOME`、其他cache、shared checkout、production path 增加写例外；
- 任务专用 tmp/cache/config 通过显式工具选项落到 `WORK_ROOT`；
- 输出 ABI、rules、realpath、syscall return/errno 和自身 hash。

如 Landlock 方法不可行，可用**不同于 bwrap 且能直接证明相同性质**的 kernel-enforced等价方案；须先写明方法和证据。仅靠环境变量或事后抽样不等价。

### 5.2 必须通过的正反 probe

在任何 Haskell/Stack/Cabal/GHC metadata命令前：

1. inside-root create/write/rename/remove成功；
2. outside-root不存在 sentinel 的 create/write 在kernel处被拒绝且不留下文件；
3. shared FRP 下不存在临时名的create在open阶段被拒绝，不接触既有文件；
4. 真实 `HOME` 和 `CODEX_HOME` 保持原值，读取允许，本任务新增 create/write 必须被拒绝且不留下文件；
5. child和grandchild继承限制；
6. symlink escape被拒绝；
7. inherited writable fd检查通过；
8. network socket/connect被禁或可证明整个后继为offline；
9. probe全程受完整trace覆盖。

任一失败：`RECOVERY_STOP_WRITE_CONFINEMENT`，不进入 R0-B/C。

### 5.3 Full trace

绑定绝对 `strace`/等价工具和hash。`-ff -yy`，覆盖至少：

```text
open/openat/openat2/creat
read/write/writev/pread/pwrite/ftruncate/truncate
mmap/mprotect/msync
rename/link/symlink/unlink/rmdir/mkdir/mknod
chmod/chown/utime/xattr
fcntl/flock
clone/fork/vfork/execve
socket/connect/send/recv
```

必须将每个成功 descriptor write回溯到路径；无法回溯即 unknown并STOP。

特别处理 `/proc/self/task/*/comm`：

- 仅open、无write：记录事实，不当外写；
- write尝试被kernel拒绝且工具成功：记录attempt/denial；
- 成功write：outside write非零，立即STOP；
- 不得自行将procfs从合同排除。

## 6. Recovery Phase R0-B｜唯一离线 closure

### 6.1 候选环境

```text
E: exact frp stack.yaml / lts-18.28
B: BASE overlay / lts-22.24 / observed GHC 9.4.8
```

只可选择一套。每套独立检查，不能拼接。

### 6.2 PASS 必需事实

- resolver/compiler exact version与hash；
- Stack/Cabal/GHC absolute path与hash；
- snapshot/global/local package DB absolute path、hash/size；
- all required local package root、HEAD/tree和cabal hash；
- transitive package ids/versions；
- proposed scenario target的最小 rebuild set；
- offline/no-network proof；
- exact base staged source与closure的兼容依据；
- 缺失依赖列表必须为空。

所有命令只在 R0-A confinement下执行。真实 `HOME/CODEX_HOME` 保持不变且不得写入；命令必须使用工具支持的显式任务目录选项，把 tmp/cache/config/log 定向 `WORK_ROOT`。允许package DB dump、声明parse、真正offline的dry-run/dependency plan和有界既有artifact/log索引。禁止build、compile、test、download、install或无界cache扫描。

两套均不能闭合：`RECOVERY_STOP_CLOSURE`。

## 7. Recovery Phase R0-C｜四项预算与持续监测

四项必须有非空 predicted upper bound、证据来源和实际monitor：

```text
new disk        <= 2 GiB
peak RSS        <= 4 GiB
post-preflight  <= 25 min
new files       <= 50,000
```

预测须基于 dry-run rebuild set + 同compiler/closure的可比真实 artifact/log；无可比实测则STOP。版本查询不能替代。

进入后继前必须验证：

- 单一 monotonic deadline；
- process-group peak RSS monitor；
- WORK_ROOT disk/file monitor；
- child/grandchild纳入；
- 超阈值能停止process group并保留receipt；
- writes outside root持续由kernel+trace双重覆盖；
- 真实 `HOME/CODEX_HOME` 保持不变且本任务新增写入为0；任务 tmp/cache/config 的实际路径均在 `WORK_ROOT`。

固定：

```text
outside writes = 0
scenario evidence runs = 0
```

## 8. Phase-0 verdict

只有以下四项同时为PASS：

```text
WRITE_CONFINEMENT_PASS
OFFLINE_CLOSURE_PASS
FOUR_BUDGETS_KNOWN_WITHIN_CAP
CONTINUOUS_MONITORS_PASS
```

才写：`ELIGIBLE_FOR_STAGED_CONSTRUCTION`。

任一失败写 `PREFLIGHT_STOP`，保留已独立成功的子证据，不自动重试、不放宽cap、不进入Phase1/2。

## 9. 条件性 Phase 1/2｜仅 recovery PASS 后

完整实施原八 EP：

```text
EP-WALL-SHARED-01..03
EP-SCENARIO-01..05
```

仍按 D003 和 D002原合同：

- exact-base clean staged source；
- snapshot直接投影production `wallViews` / current-update state；
- versioned one-record-per-firing DTO/schema；
- rejected formal post=pre、O/C空，中途state只能标UNCOMMITTED_DEBUG；
- dedicated `frp:eaw-p1-wall-scenario-evidence` target只建设；
- complete controlled fixture精确9 scenarios / 18 firings / 22 inputs；
- fixture只做parse/count/order/hash，不送production decoder/lifecycle；
- exact-error records用直接构造的 synthetic serialization验证；
- W002 conflict ledger必须进入target manifest；
- patch/local commit标 `NOT_UPSTREAM_PUBLISHED`；
- compile-only/serialization可在cap内执行；
- shared source、production lifecycle、旧test assertions不改业务语义；
- 真实 `HOME/CODEX_HOME` 在全部阶段保持不变且本任务新增写入为0，所有任务 tmp/cache/config/log 仍在 `WORK_ROOT`。

永久禁止：

```text
single/partial/full scenario execution
SCENARIO_TRACE current business evidence
normal action
DBA writer
Wall wrapper
Python native reader
production data/material generation
shared repo push
```

## 10. Worker 原生产物

发布目标：

```text
longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W003/
```

最低产物：

```text
WORKER_EXECUTION_REPORT.md
W003_BINDING.json
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

`W003_BINDING.json` 必须同时记录：沿用原 W1 物理聊天的事实、针对本 W 重新核真的 owner/thread/session/model/effort/cwd/no-writer/new-lock，以及未改变的真实 `HOME/CODEX_HOME` 和它们的本任务新增写入为0合同。

若 Phase0 PASS 并进入后继，再交：

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
COMPILE_ONLY_REPORT.json                 # 仅实际compile-only
SERIALIZATION_TEST_REPORT.json           # 仅实际允许工程测试
STAGED_LOCAL_COMMIT_REPORT.json          # 仅实际local commit；NOT_UPSTREAM_PUBLISHED
```

任一STOP再交 `ENGINEERING_STOP_REPORT.md`。不生成不适用的空文件。

## 11. Worker Return

正式 `WORKER_RETURN.json` 必须：

- V2 schema；
- `work_order_id=W003`；
- `return_to=chatgpt:OI-EAW-WALL-20261114-01:executor:E1`；
- outcome如实 `EXECUTED/PARTIAL/STOP/FAILED`；
- result_ref引用真实出版的报告；
- manifest只列实际产物及sha256；
- 不把 staged local commit伪装成GitHub ref；
- 不宣称E1已接受、action已执行或G-RUN通过。

Worker无GitHub写权限时，冻结原件后交主控逐字出版；主控返回真实refs/hash后，同一W3形成正式Return。不得捏造future/self ref。

## 12. 硬停止

- Binding／lock／grant／WORK_ROOT不一致；
- 未沿用本 Run 原 W1 物理聊天，或试图新建／重建 Worker聊天；
- 当前 owner/thread/session/model/effort/cwd/no-writer/new-lock 未针对 W003 重新实核；
- 真实 `HOME/CODEX_HOME` 被重设、迁移或承载本任务新增写入；
- 任一工具无法在保持真实 `HOME/CODEX_HOME` 的同时把新增 tmp/cache/config/log/write 限于 `WORK_ROOT`；
- Landlock/等价方案没有kernel enforcement；
- outside probe没有被拒绝或留下外部文件；
- 成功outside write；
- write path无法回溯；
- closure需联网、安装或拼接两套resolver；
- 任一预算unknown、不可监测或超cap；
- 必须改production lifecycle语义；
- 必须运行任何scenario来证明前置；
- staged source来源不明或shared checkout被写；
- fixture被送入production路径；
- normal/DBA/wrapper/native-reader被触发；
- 输出可能含凭据、大型cache/binary/生产数据。

## 13. 接收目标

E1 应能据W003真实Return判断：

1. W002三类blocker是否逐项解除；
2. 若未解除，哪个事实仍阻断且是否可有界收束；
3. 若解除，八EP哪些满足／部分／未满足；
4. patch是否只增加observer/evidence/harness能力；
5. fixture是否精确9/18/22且scenario run=0；
6. shared/production path是否零写；
7. 是否真实沿用原W1物理聊天但对W003重新核真资格和新独占；
8. 真实 `HOME/CODEX_HOME` 是否保持不变、本任务新增写入为0，所有任务tmp/cache/config是否在W003根；
9. manager可选择接受前置、修唯一EP、拒绝package或有界停止。

Worker不判断专业接受、G-RUN、H3、三个父Q或父任务完成。
