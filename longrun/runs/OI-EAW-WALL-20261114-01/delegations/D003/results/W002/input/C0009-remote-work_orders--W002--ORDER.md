# W002｜D003 Run-local shared + scenario 八项工程前置：dry preflight、隔离构造与有限验证

## 0. 运输身份

- `run_id`：`OI-EAW-WALL-20261114-01`
- `work_order_id`：`W002`
- `issuer_call_id`：`C0009`
- `issuer`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `worker`：`codex:OI-EAW-WALL-20261114-01:worker:W1`
- `return_to`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `delegation_ref`：`daowei2026/observe-iterate@b7200816f86395cd1475ea3a482fc2e63086b967:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`
- `stage_instance_id`：`M-SCENARIO-PRECONDITION-001`
- `work_item_id`：`WI-WALL-SCENARIO-PRECONDITION-001`

本 W 只实施 D003 已批准的 **shared + scenario 八项工程前置**，不执行 `ARUN-WALL-SCENARIO-001`，不运行九场景证据 fixture，不生成可用于业务 comparison 的 current O/C/A/D package，不建设 normal／DBA／wrapper／native-reader 路线。

Worker 负责工程事实、patch、有限验证和可复核证据；不决定 EP 的最终专业接受、action eligibility、G-RUN、业务预期、三个父问题或父任务完成。

## 1. 派发前主控必须核真的物理绑定

主控在发送本 W 前必须独立记录并核真：

1. W002 当前未占用，且逻辑 Worker 为 `codex:OI-EAW-WALL-20261114-01:worker:W1`；
2. 实际 Codex thread／session、实际模型与 effort；不得以逻辑名或请求名代替真实配置；
3. 实际 cwd 为 `/dwdhome/fy/BASE_E6_2`；
4. 实际单写者锁覆盖本 W 的实际写根，旧 W001 锁／thread／资格不复用；
5. D003 actual root 没有另一个活跃写者；
6. Owner grant 原文与本 W grant 完全一致；
7. 当前磁盘、权限和路径允许建立本 W 子根。

任一项无法核真，主控不得派发；若 Worker 收到后发现不一致，返回 `STOP`，不得猜测修复。

## 2. Owner grant 原文与实际排他写面

### 2.1 机读 grant——必须逐字保留

```text
operation=wall-observation-work execution_context=linux:/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01
```

机读 `allowed_writes` 只能是 Owner 根 token：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01
```

### 2.2 本 W 实际唯一写根——比 grant 更窄

```text
WORK_ROOT=/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W002
```

所有真实新建、修改、cache、tmp、home、build、log、source、fixture、receipt 和 artifact 都必须位于 `WORK_ROOT` 的规范化真实路径内。禁止利用 symlink、bind mount、相对路径逃逸或工具默认目录写到 `WORK_ROOT` 外。

即使某路径仍位于 Owner 根 token 内，只要不在上述 `WORK_ROOT`，也属于本 W 越权写入并触发硬停止。

### 2.3 只读参考路径

```text
SHARED_FRP=/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp
BASE_COMMIT=cac6c912dd65a14acbd591ca57e0afd8ddb4ef13
```

共享 FRP checkout 只能读取。禁止对它执行会写 `.git`、working tree、index 或 mtime 的操作，包括但不限于：

```text
git add/commit/reset/checkout/clean/switch/merge/rebase/stash/worktree add
代码格式化、编辑、生成文件、编译、测试、cabal/stack build
```

`git status`、`git rev-parse`、`git diff --no-ext-diff`、`git show`、`git archive` 等只读命令仅在确认不会写共享 checkout 时可用。

## 3. 精确输入

### 3.1 当前 D003 与运输合同

- `daowei2026/observe-iterate@461a420bbacc5d24ee093f9f20f2f86653973041:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.md`
- `daowei2026/observe-iterate@b7200816f86395cd1475ea3a482fc2e63086b967:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`
- `daowei2026/observe-iterate@147770cb63bc0de3b9a97eee1c6aa4abd6fbbbff:longrun/runs/OI-EAW-WALL-20261114-01/business_control/decisions/MD-C0008-001.md`
- `daowei2026/observe-iterate@1e00424349ce8a5d72c9fccf74585d18630b62b8:longrun/runs/OI-EAW-WALL-20261114-01/RUN_BINDING.json`
- `daowei2026/observe-iterate@ca7fdae84f65265332e3a53865724a2615508766:longrun/contracts/LONGRUN_PROTOCOL_V2.md`

### 3.2 D002 工程合同

- `daowei2026/observe-iterate@2b872fb3f65d1b40a6f4beb75bff783deac758e6:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/ADDITIONAL_ENGINEERING_PRECONDITION.md`
- `daowei2026/observe-iterate@d8ae5332c94c535d330263ec59bddfbfa3bc52b0:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/CONTROLLED_SCENARIO_ACTION_DESIGN.md`
- `daowei2026/observe-iterate@faaa2f2f13c65979d423f584746167aa1ead2117:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/ACTION_ELIGIBILITY_MATRIX.md`

### 3.3 Exact source baseline

```text
daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13
```

至少核对：

```text
src/Frp/Instance/ISL/Eaw/P1/WallLifecycle.hs
src/Frp/Instance/ISL/Eaw/P1/FaoIngress.hs
src/Frp/Instance/ISL/Eaw/P1/Products.hs
src/Frp/Instance/ISL/Eaw/P1/Publication.hs
src/Frp/Instance/ISL/Eaw/P1/Internal/OccurrenceLedger.hs
test/Frp/Instance/ISL/Eaw/P1/P1EndToEndSpec.hs
frp.cabal
stack.yaml 及其实际 local-package closure
```

## 4. 总体阶段与不可跨越的 Gate

```text
Phase 0  dry dependency / write-surface / cost preflight
    ↓ only if all caps measurable and predicted within limits
Phase 1  run-local staged prerequisite construction
    ↓ only if source, closure and write isolation remain valid
Phase 2  limited compile-only / serialization engineering verification
    ↓
Phase 3  final write audit, patch/manifest/hash and Worker Return
```

Phase 0 不合格时不得进入 Phase 1/2；Phase 1 局部受阻时保留已完成的合格 EP，不因单个 EP 冻结其他独立合法工作；Phase 2 任何测试都不得执行完整九场景 action。

## 5. Phase 0｜Binding、dry preflight 与外部写面证明

### 5.1 首先生成的目录

仅在主控已完成物理绑定核验后，创建：

```text
$WORK_ROOT/
├── source/
├── input/
├── fixture/
├── stack-root/
├── build/
├── tmp/
├── xdg-cache/
├── home/
├── logs/
├── tests/
├── audit/
├── receipts/
└── artifacts/
```

不得在 D003 根的其他位置创建文件。

### 5.2 必须先形成的 preflight 原件

```text
$WORK_ROOT/artifacts/D003_BINDING.json
$WORK_ROOT/artifacts/DRY_DEPENDENCY_PREFLIGHT.json
$WORK_ROOT/artifacts/WRITE_SURFACE_PLAN.json
$WORK_ROOT/artifacts/SOURCE_BASELINE_REPORT.md
$WORK_ROOT/logs/COMMAND_LOG.jsonl
```

### 5.3 Binding 内容

`D003_BINDING.json` 至少记录：

- actual thread/session、model、effort、cwd、host非敏感标识、UTC；
- logical Worker 与 W002；
- Owner root grant 原文；
- actual `WORK_ROOT`；
- single-writer lock owner／acquire evidence；
- shared FRP realpath、repo root、HEAD、branch、dirty；
- exact base commit 可读性；
- source staging 方法；
- 所有计划使用的绝对工具路径与 sha256；
- 所有计划读取的 local package root／commit；
- 所有环境重定向根。

### 5.4 Dependency closure

只读调查并记录：

- `frp.cabal` 中拟新增 component 所需的 source-dirs、modules、build-depends；
- `stack.yaml`／resolver／extra-deps／local packages；
- 任何会导致 sibling package 被编译或读取的依赖；
- staged copy 中必须包含哪些 package；
- 是否存在可避免全栈 rebuild 的最小 compile target；
- compile-only 和 serialization test 分别需要的依赖闭包；
- 工具是否会隐式联网、写 HOME、写全局 Stack/Cabal/GHC cache或 shared `.stack-work`。

禁止联网下载、安装依赖或执行 build 来“测一下” closure。

### 5.5 Tool binding

定位并 hash 实际拟用工具，例如：

```text
git
tar/cp/rsync（实际采用者）
stack 或 cabal（只能选已核可隔离者）
ghc/ghc-pkg
python/jq（仅用于静态 schema/hash 辅助时）
time/timeout 或等价资源监测工具
find/du/stat/sha256sum
```

任一关键工具仍为 PATH 模糊名、无法取得绝对路径／hash，或会隐式写外部目录，preflight 不通过。

### 5.6 Source staging 方法

优先采用不会写共享 repo 的只读导出，例如从 `BASE_COMMIT` 产生 archive 到 `WORK_ROOT/source`，再在 staged copy 中建立独立 local git history。禁止 `git worktree add`，因为它会写共享 repo 的 `.git/worktrees`。

若 exact-base staged source 不能在不写 shared repo 的前提下构造，停止并报告。

### 5.7 Write audit 计划

`WRITE_SURFACE_PLAN.json` 必须给出可实际执行的审计方法，至少覆盖：

- shared FRP/TIS/worker checkout 的 before/after HEAD、status、相关文件 hash和必要 mtime；
- `/m3varK` 与生产 product/wrapper 的“不访问／不写”证明方式；
- Stack/Cabal/GHC/Python/TMP/HOME/XDG/cache/build/log 全部重定向；
- action 过程中实际创建文件只能位于 `WORK_ROOT` 的证明方式；
- symlink realpath 逃逸检查；
- build/test 子进程写入监测方法；
- 发现外写时的立即停止与证据保留。

如果只能“预计不会外写”而不能审计，`EP-WALL-SHARED-03` 不具备进入验证的条件。

### 5.8 成本 cap 与预测

必须可监测并预计不超：

```text
new build/cache/staged-source disk <= 2 GiB
peak RSS                           <= 4 GiB
post-preflight wall clock          <= 25 min
new files under WORK_ROOT          <= 50,000
writes outside WORK_ROOT           = 0
scenario evidence fixture run      = 0
```

`DRY_DEPENDENCY_PREFLIGHT.json` 必须分别给：预测值、证据来源、监测方式、阈值和决策：

```text
ELIGIBLE_FOR_STAGED_CONSTRUCTION
PREFLIGHT_STOP
```

只要任一 cap 未知、不可监测或预计超限，决策必须是 `PREFLIGHT_STOP`。

## 6. Phase 1｜Run-local staged prerequisite construction

仅在 Phase 0 明确 `ELIGIBLE_FOR_STAGED_CONSTRUCTION` 后进行。

### 6.1 Staged source

- 从 exact `BASE_COMMIT` 构造 clean staged source；
- 记录 staged baseline tree hash；
- 可在 staged source 内初始化独立 git repo并形成 local commits；
- local commit 仅是 Run artifact，必须标 `NOT_UPSTREAM_PUBLISHED`；
- 禁止添加 remote、push或修改共享 repo；
- 所有 patch必须能从 base commit或 staged baseline干净应用／审查。

### 6.2 必须建设的八项 EP

#### `EP-WALL-SHARED-01`｜Read-only lifecycle state snapshot

实现不改变状态、不引入业务规则的 snapshot：

```haskell
data WallLifecycleStateSnapshot = WallLifecycleStateSnapshot
  { activeViews        :: Map WallIdentity WallCurrentView
  , currentUpdateViews :: Map WallIdentity WallCurrentView
  }

snapshotWallLifecycleState
  :: WallLifecycleState
  -> WallLifecycleStateSnapshot
```

名称可按项目规范调整，字段语义不能缩减。A 必须直接来自 production lifecycle state；禁止从 C rows累积、从 producer trace映射或解析 `show` 文本。

#### `EP-WALL-SHARED-02`｜Structured one-record-per-firing evidence schema

形成 versioned canonical DTO／JSON schema，至少包含：

```text
schema_version
fixture_id / scenario_id
firing_id
ordered_inputs
pre_active_map
result_status
accepted_occurrences
current_updates
post_active_map
diagnostics
exact_error constructor + payload
source_commit
prerequisite_local_commit
input origin/provenance
```

要求：

- one record per firing；
- deterministic key和list ordering；
- exact error，不只写 `Left`；
- rejected firing 的 formal post-state不得暴露中途 fold state；
- schema validation和JSON roundtrip；
- canonical bytes/hash稳定；
- origin至少能区分 controlled input；
- DTO 是工程 evidence contract，不是 business assertion。

#### `EP-WALL-SHARED-03`｜Isolated clean build closure

建设并证明：

- clean staged package closure；
- Stack/Cabal/GHC/TMP/HOME/XDG/cache/log/build全部落在 `WORK_ROOT`；
- shared checkout零变更；
- `/m3varK`、现役 product、production wrapper零写入；
- build前后外部写面审计可执行；
- failure保留完整 log/exit/resource facts。

#### `EP-SCENARIO-01`｜Dedicated scenario-evidence target

在 staged source 中形成：

```text
component candidate:
  frp:eaw-p1-wall-scenario-evidence

main candidate:
  test/Frp/Instance/ISL/Eaw/P1/WallLifecycleScenarioEvidenceMain.hs
```

目标必须：

- 只读取固定 fixture schema；
- 预期处理恰好9个具名 scenario；
- 每个 scenario 独立 empty state；
- 保留 firing／within-firing order；
- decode-invalid路径调用 production `decodeWallNumericRow`／`partitionIngressBatch`；
- typed paths调用 production `applyWallOccurrenceBatch`／transaction semantics；
- 使用 shared snapshot；
- 输出结构化 trace到 caller提供路径；
- 无 market/TIS/DBA/native-reader依赖；
- 无隐藏 retry或跨 scenario state reuse；
- 拒绝未知 scenario／额外行／未解析占位符。

**本 W 只能构造并至多 compile-only 验证该 target，禁止把完整 fixture交给它执行。**

#### `EP-SCENARIO-02`｜Exact error assertions

结构化支持并保留 actual exact constructor／payload，至少覆盖未来场景所需：

```text
WallUpdateBeforeStart
WallEndBeforeStart
WallStartedTwice
WallOccurrenceRefConflict
WallInvalidPresenceTransition
MissingNumericField "core_price"
```

constructor mismatch必须保留 actual；source prediction与actual结果分开；ingress/state diagnostic来源分开。不得把 generic `Left` 当验收。

#### `EP-SCENARIO-03`｜Transaction trace integrity

对未来 mixed-valid-invalid firing支持记录：

```text
pre A
ordered inputs
fold result
committed post A
O/C/D
exact offending ref/identity
```

intermediate state只能标 `UNCOMMITTED_DEBUG`；rejected firing 的 formal post A 必须等于 pre A，formal O/C为空。工程前置只验证 schema／serialization和代码路径，不执行九场景。

#### `EP-SCENARIO-04`｜Existing test-contract conflict ledger

至少登记 exact commit、函数和 assertion：

1. cross-firing Start replay旧测试期待 idempotence；
2. current firing-local ledger静态预测 `WallStartedTwice`；
3. after-End旧测试只接受任意 `Left`，不能区分 before-start／after-end；
4. dedicated harness不决定改 implementation还是改旧 test。

文件必须保留冲突，不得为了 compile而修改 production lifecycle语义或无痕改旧断言。

#### `EP-SCENARIO-05`｜Fixture schema and provenance

形成完整 `FX-WALL-SCENARIO-001` schema与输入文件：

```text
9 scenarios
18 logical firings
22 input occurrences/rows
origin = CONTROLLED
Dormant/restore outside core action
```

每个 scenario必须含：

```text
scenario_id
business_question
source_prediction
firings
ordered occurrences/rows
identity/ref/UTI/payload
expected distinction
non-goals
```

fixture schema version、base commit、prerequisite local commit（若有）和fixture hash进入manifest。D003中只允许静态 parse/count/order/hash validation，禁止生命周期执行。

### 6.3 明确排除

禁止建设或夹带：

```text
EP-NORMAL-01..05
DBA writer materialization
Wall wrapper generation
Python native reader
current End measurement readback
normal action
production deployment
```

## 7. Phase 2｜有限工程验证

只有 Phase 0 cap合格、Phase 1写面仍闭合时才允许。

### 7.1 允许

1. compile-only／target existence verification；
2. snapshot accessor的类型、字段和纯只读性质测试；
3. evidence DTO／JSON schema roundtrip、deterministic ordering和hash稳定性测试；
4. fixture schema静态 parse、9/18/22 count、order和hash validation；
5. accepted／rejected record的**直接构造** synthetic serialization unit/property test；
6. staged source的静态 lint／typecheck；
7. build/test前后 write audit。

### 7.2 禁止

- 把9场景fixture送入 scenario target、production decoder或production lifecycle；
- 生成 `SCENARIO_TRACE.jsonl` 或其他 current O/C/A/D business package；
- 用单个／部分 scenario偷偷运行 production lifecycle来“测 harness”；
- 运行现有 real-run runner或旧 P1EndToEnd完整业务 suite来替代前置验收；
- 修改 transition、identity、error、ledger、transaction语义以使测试通过；
- 执行 normal／DBA／wrapper／native-reader路径；
- 把工程 serialization测试写成业务 `SUPPORTS/COUNTERS`。

### 7.3 资源执行约束

未来实际 compile/test命令必须：

- 使用 Phase 0 绑定的绝对工具和hash；
- 显式设置所有重定向环境；
- 由 `timeout`／等价机制保证 post-preflight 总时限；
- 用 `/usr/bin/time -v`／等价工具记录 max RSS；
- 持续检查 disk/file caps；
- 发现外写、超 cap或不可观测立即停止；
- 不联网、不安装依赖。

## 8. Phase 3｜最终审计、产物和 Return

### 8.1 Worker 原生产物

全部位于 `$WORK_ROOT/artifacts/`，最低包括：

```text
WORKER_EXECUTION_REPORT.md
D003_BINDING.json
DRY_DEPENDENCY_PREFLIGHT.json
WRITE_SURFACE_PLAN.json
SOURCE_BASELINE_REPORT.md
PRECONDITION_REPORT.md
SOURCE_CHANGE_MANIFEST.json
PREREQUISITE_PATCHSET.diff
EP_ACCEPTANCE_MATRIX.md
D003_BINDING_CANDIDATE.json
WRITE_SURFACE_AUDIT.json
FIXTURE_SCHEMA_AND_PROVENANCE.md
KNOWN_CONTRACT_CONFLICTS.md
COMMAND_LOG.jsonl
HASHES.sha256
```

条件产物：

```text
COMPILE_ONLY_REPORT.json
SERIALIZATION_TEST_REPORT.json
STAGED_LOCAL_COMMIT_REPORT.json   # 必须含 NOT_UPSTREAM_PUBLISHED
ENGINEERING_STOP_REPORT.md
```

### 8.2 EP_ACCEPTANCE_MATRIX

每项只能取：

```text
SATISFIED
PARTIAL
UNSATISFIED
NOT_ATTEMPTED
```

每项必须列：

- 直接 source／patch／test／audit evidence；
- 未满足部分；
- 是否阻断其他 EP；
- 最小解除条件；
- Worker只给工程事实，不替 E1作最终专业接受。

### 8.3 Patch 与 manifest

`SOURCE_CHANGE_MANIFEST.json` 至少记录：

- exact base commit；
- staged baseline tree/hash；
- 每个 changed/new/deleted file；
- file sha256；
- 所属 EP；
- 是否 production source、test-only、fixture或build declaration；
- local commit（如有）和 `NOT_UPSTREAM_PUBLISHED`；
- patch是否可从base干净审查；
- 没有 remote/push。

`PREREQUISITE_PATCHSET.diff` 必须是文本 patch，不包含 build artifact或二进制。

### 8.4 Write audit

`WRITE_SURFACE_AUDIT.json` 必须明确：

```text
writes_outside_WORK_ROOT = 0 | nonzero | unknown
shared_checkout_changed_by_W002 = false | true | unknown
m3varK_written = false | true | unknown
production_wrapper_written = false | true | unknown
```

任一值为 `nonzero/true/unknown` 时，`EP-WALL-SHARED-03` 不能标 SATISFIED；保留事实并停止，不得清理后掩盖。

### 8.5 Hashes

`HASHES.sha256` 覆盖本 W 所有可发布文本／JSON／patch／fixture／report。大型 build/cache/source tree不复制到GitHub，只在manifest中记录路径、大小、tree hash和保留策略。

## 9. Worker Return 合同

正式 `WORKER_RETURN.json`：

- schema按V2；
- `run_id=OI-EAW-WALL-20261114-01`；
- `work_order_id=W002`；
- `return_to=chatgpt:OI-EAW-WALL-20261114-01:executor:E1`；
- `outcome` 如实为 `EXECUTED / PARTIAL / STOP / FAILED`；
- `result_ref` 引用允许发布的 `WORKER_EXECUTION_REPORT.md`；
- manifest列真实产物及sha256；
- 不把 staged local commit写成GitHub ref；
- 不声称 E1 已接受、action 已可执行或G-RUN通过。

若 Worker 没有 GitHub 写工具，提供精确发布路径、完整正文、真实本地路径与hash，由主控逐字出版；不得捏造 commit。

### outcome 指引

- `EXECUTED`：八项EP均完成工程构造，允许的有限验证和write audit均完成；仍不表示G-RUN或九场景action执行；
- `PARTIAL`：至少一项合法EP有可审查成果，但有具名EP／compile／audit缺口；
- `STOP`：Phase 0 cap／写面／依赖／binding硬停止，或发现外写风险；
- `FAILED`：非预期执行失败且无可靠部分结果；优先保留可用部分并用 `PARTIAL`。

## 10. 硬停止

立即停止并回报，不自行扩大范围：

- Owner grant、D003、W002 actual root不一致；
- physical binding／single writer无法核真；
- exact base或工具绝对路径/hash无法固定；
- source staging会写shared repo；
- staged source来源不明或不clean；
- 任一cache/build/log/home/tmp无法重定向；
- dependency closure需要联网／安装依赖；
- cap未知、不可监测或预计超限；
- 必须改production lifecycle语义才能编译；
- 必须执行任一真实scenario才能证明前置；
- 9场景fixture被送入production路径；
- 发现`WORK_ROOT`外写入；
- 外部动作可能发生但回执不明；
- 凭据、私有原始数据或大型build artifact将被发布。

## 11. 接收目标

本 W 的目标不是“跑通 scenario”。目标是让 E1 能据真实证据逐项判断：

1. 八项EP哪些满足、部分或未满足；
2. staged patch是否只增加观察／evidence能力而未改业务语义；
3. fixture是否精确为9/18/22且从未执行；
4. compile-only／serialization验证是否真实在cap与写面内完成；
5. shared source和生产路径是否零改动；
6. manager是否可选择接受前置、返修唯一EP或有界停止。

D003、scenario action、三个父问题和父任务的最终判断仍由E1／manager按各自职责完成。
