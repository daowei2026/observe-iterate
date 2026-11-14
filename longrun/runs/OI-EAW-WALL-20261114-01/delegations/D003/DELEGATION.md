# D003｜Run-local scenario-first 工程前置实现、隔离验证与可执行性封口

## 0. 运输身份

- `run_id`：`OI-EAW-WALL-20261114-01`
- `delegation_id`：`D003`
- `issuer_call_id`：`C0007`
- `issuer`：`chatgpt:OI-EAW-WALL-20261114-01:manager`
- `recipient`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `return_to`：`chatgpt:OI-EAW-WALL-20261114-01:manager`
- 管理决定：`daowei2026/observe-iterate@11fce23f543b000425350153d9cb1eda5e78453c:longrun/runs/OI-EAW-WALL-20261114-01/business_control/decisions/MD-C0007-001.md`

本 D 是 D002 被接受后的新工程前置专业任务，不是 D002 返修，也不是 `ARUN-WALL-SCENARIO-001` 的实际运行。

本 D 只在本 Run 隔离目录中建设并验证 shared + scenario prerequisite package。它不能修改共享源码 checkout，不能 push `daowei2026/frp`，不能生成并消费九场景的正式 O/C/A/D evidence，也不取得 current scenario G-RUN。

## 1. 业务连接、阶段和完成目的

### 1.1 所服务的父问题

```text
Q-WALL-IDENTITY-LIFECYCLE
Q-WALL-PUBLICATION-STATE
Q-WALL-BUSINESS-SUITABILITY
```

D003 不直接回答这些问题。它解除以下当前材料能力缺口：

- 无法只读观察真实 FRP full active map；
- 无稳定 one-record-per-firing evidence schema；
- 无精确 error/transaction trace；
- 无独立、结构化、可隔离运行的 scenario evidence target；
- 无可证明所有写入都落在 Run root 的 clean build closure。

### 1.2 Workflow 位置

- `stage_instance_id`：`M-SCENARIO-PRECONDITION-001`
- `work_item_id`：`WI-WALL-SCENARIO-PRECONDITION-001`
- 对应节点：ActionPreflight 后的**工程能力建设与有限工程验证**；不进入 `ARUN-WALL-SCENARIO-001` evidence execution。
- 当前 action classification：

```text
ARUN-WALL-SCENARIO-001 = NEEDS_PRECONDITION
G-RUN                   = NOT PASSED
```

### 1.3 D003 完成目的

形成一个可由下一轮 manager 独立判断的 prerequisite package：

```text
shared state observer
+ structured evidence schema
+ isolated clean build closure
+ dedicated scenario target
+ exact error/transaction trace
+ conflict ledger
+ fixture schema/provenance
+ patch/manifest/hash/audit
```

D003 完成后，manager 只能决定 prerequisite 是否满足以及 action 是否可重分类为 `ELIGIBLE_WITH_LIMITS`；仍需另一个明确 `G-RUN` 才能执行九场景 action。

## 2. 必须采用的精确输入

### 2.1 运行、专业与控制合同

- `daowei2026/observe-iterate@1e00424349ce8a5d72c9fccf74585d18630b62b8:longrun/runs/OI-EAW-WALL-20261114-01/BusinessTaskInput.md`
- `daowei2026/observe-iterate@11fce23f543b000425350153d9cb1eda5e78453c:longrun/runs/OI-EAW-WALL-20261114-01/business_control/decisions/MD-C0007-001.md`
- `daowei2026/observe-iterate@ca7fdae84f65265332e3a53865724a2615508766:longrun/professional/PRO_EXECUTOR_GUIDE.md`
- `daowei2026/observe-iterate@ca7fdae84f65265332e3a53865724a2615508766:longrun/contracts/LONGRUN_PROTOCOL_V2.md`
- `daowei2026/observe-iterate@ca7fdae84f65265332e3a53865724a2615508766:control/02_L1_观察材料准备流程.md`
- `daowei2026/observe-iterate@ca7fdae84f65265332e3a53865724a2615508766:control/05_三级Gate及后继路由.md`

### 2.2 D002 正式成果

- `daowei2026/observe-iterate@602c53c5602840d14068110a92bd90e80af6a306:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/D002_EXECUTOR_REPORT.md`
- `daowei2026/observe-iterate@d8ae5332c94c535d330263ec59bddfbfa3bc52b0:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/CONTROLLED_SCENARIO_ACTION_DESIGN.md`
- `daowei2026/observe-iterate@faaa2f2f13c65979d423f584746167aa1ead2117:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/ACTION_ELIGIBILITY_MATRIX.md`
- `daowei2026/observe-iterate@2b872fb3f65d1b40a6f4beb75bff783deac758e6:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/ADDITIONAL_ENGINEERING_PRECONDITION.md`

### 2.3 Exact source baseline

```text
repository = daowei2026/frp
base_commit = cac6c912dd65a14acbd591ca57e0afd8ddb4ef13
shared checkout for read-only reference = /dwdhome/fy/BASE_E6_2/edh-universe/frp/frp
```

相关基线文件：

```text
src/Frp/Instance/ISL/Eaw/P1/WallLifecycle.hs
src/Frp/Instance/ISL/Eaw/P1/FaoIngress.hs
src/Frp/Instance/ISL/Eaw/P1/Products.hs
src/Frp/Instance/ISL/Eaw/P1/Publication.hs
src/Frp/Instance/ISL/Eaw/P1/Internal/OccurrenceLedger.hs
test/Frp/Instance/ISL/Eaw/P1/P1EndToEndSpec.hs
package/component declarations needed by an isolated test target
```

共享 checkout 只能读。所有新代码、component declaration、fixture、build output和 local commit只能存在于 D003 root 的 staged source。

## 3. 工程前置范围

### 3.1 必须实现并逐项验收

#### Shared

```text
EP-WALL-SHARED-01  read-only lifecycle state snapshot
EP-WALL-SHARED-02  structured one-record-per-firing evidence schema
EP-WALL-SHARED-03  isolated clean build closure
```

#### Scenario

```text
EP-SCENARIO-01  dedicated scenario-evidence target
EP-SCENARIO-02  exact error assertions
EP-SCENARIO-03  transaction trace integrity
EP-SCENARIO-04  existing test-contract conflict ledger
EP-SCENARIO-05  fixture schema and provenance
```

完整语义和 acceptance 以 D002 的 `ADDITIONAL_ENGINEERING_PRECONDITION.md` 为准，本 D 不缩减。

### 3.2 明确不在本 D

```text
EP-NORMAL-01..05
DBA writer materialization
Wall wrapper generation
Python native reader
current End measurement readback
ARUN-WALL-SCENARIO-001 nine-scenario execution
ARUN-WALL-NORMAL-001 execution
production source patch/push
business expectation freeze/comparison/diagnosis
```

normal prerequisite 继续独立 OPEN；scenario-first 不取消 normal 路线。

## 4. 分阶段执行合同

## Phase 0｜Binding、dry preflight 与外部写面证明

在任何 staged source 修改、build 或 test 前，必须产生：

```text
D003_BINDING.json
DRY_DEPENDENCY_PREFLIGHT.json
WRITE_SURFACE_PLAN.json
SOURCE_BASELINE_REPORT.md
```

至少固定：

- base commit、只读 shared paths；
- staged source path；
- 所有 local package path/commit；
- absolute Stack/Cabal/GHC executable path和 hash；
- overlay/resolver/package closure；
- cache/tmp/home/build/log paths；
- predicted disk/RSS/wall/file-count；
- filesystem audit 方法；
- actual Worker/thread/model/effort/cwd 和 single-writer lock（若签 W）。

只有以下 cap 均可监测且预计不超限，才可进入 Phase 2 的 compile-only/serialization verification：

```text
new build/cache/staged-source disk <= 2 GiB
peak RSS                          <= 4 GiB
wall clock after preflight        <= 25 min
new files under D003 root         <= 50,000
writes outside D003 root          = 0
scenario evidence fixture run     = 0
```

任一项未知、无法重定向/监测或预计超限：停止在 preflight；仍交付已完成的专业分析、patch design和最小解除条件。

## Phase 1｜Run-local staged prerequisite construction

### 4.1 隔离 source

唯一 Linux 根：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/
```

建议结构：

```text
D003/
├── source/              # exact-base isolated copy/worktree; may contain local commit
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

不得对 shared checkout 使用 `git add/commit/reset/checkout/clean` 或任何写操作。staged local commit SHA只是本 Run 工程 artifact，不是 GitHub `frp` ref，不得写成“已提交上游”。

### 4.2 Shared observer

实现不改变状态、不引入新业务逻辑的 snapshot：

```haskell
data WallLifecycleStateSnapshot = WallLifecycleStateSnapshot
  { activeViews        :: Map WallIdentity WallCurrentView
  , currentUpdateViews :: Map WallIdentity WallCurrentView
  }

snapshotWallLifecycleState
  :: WallLifecycleState
  -> WallLifecycleStateSnapshot
```

名称可按现有规范调整；字段语义不能缩减。A 必须来自真实 lifecycle state，不得从 C 累积或 producer trace伪造。

### 4.3 Evidence schema

形成 versioned canonical schema，至少含：

```text
schema_version
fixture/scenario_id
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

要求 deterministic ordering、JSON roundtrip、stable hash；rejected firing 的 formal post-state不能暴露中途 fold state。

### 4.4 Dedicated scenario target

在 staged tree 中形成目标：

```text
component candidate:
  frp:eaw-p1-wall-scenario-evidence

main candidate:
  test/Frp/Instance/ISL/Eaw/P1/WallLifecycleScenarioEvidenceMain.hs
```

它必须只读取固定 fixture schema，使用 production decoder/partition/lifecycle paths，支持 exact error和transaction trace，且所有输出路径由 caller提供。

**本 D 只构建该能力，不运行九场景 fixture。**

### 4.5 Fixture schema/provenance

形成 `FX-WALL-SCENARIO-001` 的 schema和完整输入文件：

```text
9 scenarios
18 logical firings
22 input occurrences/rows
Dormant/restore outside core action
origin = CONTROLLED
```

所有 identity/ref/UTI/payload/firing order、business question、source prediction、distinction和 non-goal必须固定并进入 hash manifest。该文件在 D003 中只能做 schema/static validation，不能送入 scenario target执行。

### 4.6 Existing test conflict ledger

至少登记：

1. cross-firing Start replay旧测试期待 idempotence；
2. current firing-local ledger静态预测 `WallStartedTwice`；
3. after-End旧测试只接受任意 `Left`；
4. exact source/test commit、函数和 assertion；
5. dedicated harness不决定改 implementation还是改旧 test。

## Phase 2｜有限工程验证，不执行证据动作

若 Phase 0 cap 合格，允许：

1. compile-only/build target existence verification；
2. snapshot accessor的类型/纯只读性质测试；
3. evidence DTO/JSON schema roundtrip、ordering、hash稳定性测试；
4. fixture schema/static count/order/hash validation；
5. rejected/accepted record serialization的 synthetic unit/property test；
6. staged tree和 action-root write audit。

明确禁止：

- 把完整9场景 fixture送入 production lifecycle并输出 `SCENARIO_TRACE.jsonl`；
- 生成可供业务 comparison 的 current O/C/A/D package；
- 使用工程 unit test结果填写 `SUPPORTS/COUNTERS`；
- 修改 production transition/identity/error/transaction语义来让测试通过；
- 运行 normal action、DBA、wrapper或native reader。

若 compile/test 需要运行完整 action fixture或越出写面，停止并返回 `PARTIAL_WITH_LIMITS`。

## 5. 必须交付的原生结果

GitHub 结果只发布到：

```text
longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/
```

最低交付：

1. `D003_EXECUTOR_REPORT.md`
2. `PRECONDITION_REPORT.md`
3. `SOURCE_BASELINE_AND_STAGING_REPORT.md`
4. `SOURCE_CHANGE_MANIFEST.json`
5. `PREREQUISITE_PATCHSET.diff`
6. `EP_ACCEPTANCE_MATRIX.md`
7. `D003_BINDING_CANDIDATE.json`
8. `DRY_DEPENDENCY_PREFLIGHT.json`
9. `WRITE_SURFACE_AUDIT.json`
10. `FIXTURE_SCHEMA_AND_PROVENANCE.md`
11. `KNOWN_CONTRACT_CONFLICTS.md`
12. `HASHES.sha256`

条件交付：

13. `COMPILE_ONLY_REPORT.json`——只有实际进入 compile-only 阶段时产生；
14. `SERIALIZATION_TEST_REPORT.json`——只有实际执行允许的工程测试时产生；
15. `STAGED_LOCAL_COMMIT_REPORT.json`——只有 staged tree形成 local commit时产生，必须标明 `NOT_UPSTREAM_PUBLISHED`；
16. `ENGINEERING_STOP_REPORT.md`——preflight/cap/写面/依赖阻断时产生。

不得发布大型 build/cache、二进制、凭据或生产数据。GitHub patch和manifest必须足以审查 staged source改动；Linux source tree仍留在授权 D003 root。

## 6. 接收标准

### 6.1 专业完整性

- 八个 EP 每项都有 `SATISFIED / PARTIAL / UNSATISFIED / NOT_ATTEMPTED` 和直接证据；
- base commit、staged tree、patch、local commit（如有）、hash可互相对账；
- snapshot语义不由 C 或 producer trace替代；
- exact error和transaction evidence contract完整；
- fixture精确为9/18/22，未被执行；
- old test conflict不被隐去；
- normal prerequisite没有被夹带。

### 6.2 权限和写面

- shared FRP/TIS/worker checkout字节、git status和mtime无 D003 造成的改变；
- `/m3varK`、现役 product、production wrapper和源码 GitHub repo无写入；
- 所有新文件在 D003 root或本 Run GitHub path；
- build/cache/tmp/home/log全部显式重定向；
- 无法证明零外写即不能把 EP-WALL-SHARED-03判满足。

### 6.3 工程验证边界

- compile-only/serialization测试通过可支持“prerequisite capability ready”；
- 它们不能支持 current lifecycle business semantics；
- 任何9场景实际执行都属于越界，不能在 D003 中接受；
- D003 结果不得自行把 `ARUN-WALL-SCENARIO-001` 标成已运行或 G-RUN通过。

### 6.4 Manager 可判定性

最终报告必须使 manager无需再次要求“继续细化”，即可选择：

```text
ACCEPT_PREREQUISITES_AND_RECLASSIFY_ACTION
ACCEPT_PARTIAL_AND_REPAIR_EXACT_EP
REJECT_PREREQUISITE_PACKAGE
OWNER_AUTHORIZATION_REQUIRED
```

## 7. Worker 边界

E1 可以零 Worker完成专业设计和审查；需要 Linux staged source、patch、compile或test时可签新的 Worker order。

- 下一 order id 必须先核本 Run 未占用；当前候选为 `W002`；
- Worker recipient只能是 Binding 已批准的 `codex:OI-EAW-WALL-20261114-01:worker:W1`；
- Worker只执行 D003 已明确的 preflight/staged engineering/limited verification；
- Worker不能决定 EP 是否专业接受、action eligibility、G-RUN、业务预期或父任务完成；
- Worker Return先回 E1，由 E1消费、审查 patch和验证证据后再回 manager；
- 主控在实际派发前核物理 thread、模型/effort、cwd、single-writer lock和写面；旧 W001 的锁、thread和资格不延续。

允许操作仍仅为：

```text
wall-observation-work
run-record-publish
```

Linux 写面严格收窄为：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003
```

GitHub 写面严格收窄为：

```text
longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003
```

## 8. 硬停止和结果分流

### 硬停止

- 需要写 shared source checkout或 push源码 repo；
- 无法固定 exact base/absolute tool/hash；
- staged source不干净或来源不明；
- 任一 cache/build/log不能重定向；
- dry preflight超 cap或不可监测；
- 必须修改 production lifecycle语义才能编译；
- 必须运行9场景才能证明前置；
- 发现 D003 root外写入；
- 外部动作可能已发生但回执未知。

### 结果分流

- **全部前置满足**：回交 prerequisite package；建议 manager把 scenario action重分类为 `ELIGIBLE_WITH_LIMITS`，但不自行通过 G-RUN。
- **部分满足**：保留已验收 EP和patch，准确指出唯一未满足 EP、影响、最小修复；不整包失败。
- **preflight阻断**：返回成本/写面事实和恢复条件；不启动 build。
- **需要额外源码权限**：形成具名 Owner authorization candidate；不修改共享 repo。
- **发现 product semantic问题**：只登记新问题候选；不在 prerequisite package修产品行为。

最终 `EXECUTOR_RETURN` 必须引用 D003、全部真实结果、已接受 Worker（如有）、remaining scope和准确后继。`REPORTED_COMPLETE` 只表示 D003 合同完整交付，不表示 scenario action、三个父问题或父任务完成。
