# D002｜Additional Engineering Preconditions

> `run_id`：`OI-EAW-WALL-20261114-01`  
> `delegation_id`：`D002`  
> 适用动作：`ARUN-WALL-NORMAL-001`、`ARUN-WALL-SCENARIO-001`  
> 性质：**具名最小工程前置；不是执行授权，不是实现提交，不是新 W**

# 1. 为什么需要工程前置，而不是再做只读扫描

D001/W001 与 C0006 的 current-source 核验已经确定：

- exact source/test files存在；
- current lifecycle、ingress、publication逻辑可静态阅读；
- 现有 light integration test存在；
- 现有 real-run runner存在；
- current Wall generated wrapper、结构化 A trace、wall-only current evidence target不存在；
- existing runner 会 build、多产品运行并要求 clean tree，不是本问题的最小动作；
- existing test只给 process pass/fail，部分断言与 current source 语义冲突或不区分 exact error。

另一轮相同边界的 Linux read-only扫描不能生成这些能力。因此 C0006 不签 W002。下一步若继续，必须先完成以下具名工程前置，然后由 manager 再判 G-RUN。

# 2. Shared precondition set

## `EP-WALL-SHARED-01`｜Read-only lifecycle state snapshot

### Problem

`WallLifecycleState` 在 current public export中是 opaque；动作需要按 firing 观察真实 full active map和 current update batch，不能由 C row 累积伪造，也不能用 producer trace替代。

### Minimum change

在 current FRP source中提供不改变状态的只读 snapshot：

```haskell
data WallLifecycleStateSnapshot = WallLifecycleStateSnapshot
  { activeViews       :: Map WallIdentity WallCurrentView
  , currentUpdateViews :: Map WallIdentity WallCurrentView
  }

snapshotWallLifecycleState
  :: WallLifecycleState
  -> WallLifecycleStateSnapshot
```

名称可按项目规范调整，但语义和字段不能缩减。

### Acceptance

- Start 后 activeViews 含 identity；
- same-firing two-update 后 active/currentUpdate 都是最后 update；
- End 后 activeViews 不含 identity，但 currentUpdate含 Ended；
- rejected batch snapshot 与 pre-state相等；
- accessor无写入、无时间采样、无新业务逻辑；
- 编译测试证明 snapshot 与 production state同源。

### Non-goal

不把 A 增加为新的 production writer，不改变当前 O/C/D public contract。

---

## `EP-WALL-SHARED-02`｜Structured firing evidence schema

### Problem

现有 tests主要通过 `unless/fail` 和最终 smoke string表达结果，不能作为可消费 evidence package。

### Minimum contract

新增稳定 evidence DTO／JSON schema：

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
exact_error
source_commit
harness_commit
```

### Acceptance

- one record per firing；
- deterministic key/order；
- exact error constructor + parameters，不只写 `Left`；
- rejected firing 不暴露中途 fold state为 committed state；
- JSON roundtrip + schema validation；
- evidence hash稳定；
- actual fixture origin（real seed／controlled extension）可追溯。

---

## `EP-WALL-SHARED-03`｜Isolated clean build closure

### Problem

BASE 共享 TIS／FRP/worker存在 unrelated dirty；Stack overlay引用多个本地 package，默认 build可能在 Run写面外生成 `.stack-work`、cache或日志。

### Minimum contract

每个未来 action 建立：

```text
<ACTION_ROOT>/source/         clean staged packages
<ACTION_ROOT>/stack-root/
<ACTION_ROOT>/build/
<ACTION_ROOT>/tmp/
<ACTION_ROOT>/xdg-cache/
<ACTION_ROOT>/home/
```

`ACTION_BINDING.json` 固定：

- base commit；
- prerequisite commit；
- all local package paths/commits；
- Stack executable absolute path/hash；
- overlay absolute path/hash；
- work-dir/cache/tmp/log roots；
- single-writer lock。

### Acceptance

- no shared checkout changes；
- no `/m3varK` writes；
- build前后 action root外 filesystem audit为零新增／修改；
- dependency closure dry preflight可审计；
- failure leaves logs and exact exit code。

# 3. Preconditions for `ARUN-WALL-NORMAL-001`

## `EP-NORMAL-01`｜Dedicated normal-evidence target

### Required target

```text
component:
  frp:eaw-p1-wall-normal-evidence

main:
  test/Frp/Instance/ISL/Eaw/P1/WallNormalEvidenceMain.hs
```

### Required behavior

- reads only `FX-WALL-NORMAL-001.json`；
- constructs exactly F1 Start、F2 two legal BandUpdates、F3 End；
- executes production current ingress/lifecycle paths appropriate to fixture；
- emits structured O/C/A/D trace；
- uses production `dumpWallOutputs` for O/C/D materialization；
- writes only caller-provided `--output-dir` and `--product-root`；
- rejects unknown fields、extra firings、changed order or unresolved placeholders；
- no TIS import、no market data、no WallAssembler、no other P1 product。

### Acceptance

- fixture count exactly 3 firings/4 occurrences；
- expected normal-path counts are asserted but actual output is always preserved；
- nonzero exit on schema/write escape/hash mismatch；
- `--dry-run` emits build/input/write/cost plan without execution。

---

## `EP-NORMAL-02`｜Action-root current writer materialization

### Problem

production `dumpWallOutputs` normally uses Fao dump context; evidence action must not write a production store path.

### Required capability

A test/evidence owner or store adapter that invokes the same `dumpAdtEvent'` path but binds product root to:

```text
<ACTION_ROOT>/product
```

### Acceptance

- writer names exactly `wall_occurrences / wall_current_view / wall_diagnostics`；
- types exactly `WallOccurrenceBatch / WallCurrentBatch / WallDiagnostic`；
- trigger axes and list anchors preserved；
- fields/schema marker generated；
- no production store or task-linker writes；
- D valid-empty state is distinguishable from reader failure。

### Non-goal

不修改 production storage location policy，不把 A 变成 public writer。

---

## `EP-NORMAL-03`｜Lossless staged Wall wrapper generation

### Current gap

current `frp/dbaw/Main.hs` 未列三类 Wall top-level type；inspected worker `dbaw.py` 不含它们。`WallDiagnostic` 又嵌套 sum-type error，现有 generator能否完整处理未证明。

### Required capability

在 isolated prerequisite commit中，使以下 current types能够生成**lossless** Python wrapper：

```text
WallOccurrenceBatch
WallCurrentBatch
WallDiagnostic
```

并将输出写到 caller path：

```text
--wrapper-out <ACTION_ROOT>/wrapper/dbaw.py
```

### Acceptance

- top-level及全部 nested types存在；
- Start/BandUpdate/End和至少一个 diagnostic roundtrip；
- identity/ref/UTI/change/state/error constructor不丢失；
- compact schema marker保留；
- sum type不降级成不可逆 text；
- generation失败即显式失败，不写半成品；
- production `/mquant/worker/adt/dbaw.py` 未改变。

若现有 generator不能满足，应先实现 generator支持或正式无损 storage projection。不得在 action script中临时解析 `show` 文本。

---

## `EP-NORMAL-04`｜Staged native reader binding

### Required behavior

以 isolated Python import root加载 staged wrapper，并用现有 `FrpDbaDao`／DBA read chain读取 action-root current writer material。

### Acceptance

- import不会加载 production wrapper；
- all settings/store paths显式绑定 action root；
- O/C/D fields和trigger axes读回；
- D空时给 `VALID_EMPTY` + schema/read-success，不给 missing；
- Haskell trace vs native readback逐字段 comparison；
- reader任何 cache/log仅写 action root；
- 输出 `NATIVE_READBACK.jsonl` 和 `ROUNDTRIP_COMPARISON.json`。

---

## `EP-NORMAL-05`｜Current End measurement assertion

### Required assertion

harness必须原样导出 current End occurrence payload和 preceding last measurement，并明确：

```text
current End payload
≠ legacy storage projection
≠ imputed last band/core
```

### Acceptance

- current schema实际字段清单；
- legacy `0 + not_present`只作为 comparison context；
- 无填补、无字段重命名；
- consumer可区分“End不携带 measurement”与“真实 measurement=0”。

# 4. Preconditions for `ARUN-WALL-SCENARIO-001`

## `EP-SCENARIO-01`｜Dedicated scenario-evidence target

### Required target

```text
component:
  frp:eaw-p1-wall-scenario-evidence

main:
  test/Frp/Instance/ISL/Eaw/P1/WallLifecycleScenarioEvidenceMain.hs
```

### Required behavior

- reads exactly 9 named scenarios；
- each scenario starts from independent empty state；
- preserves firing and within-firing order；
- calls production `decodeWallNumericRow`/`partitionIngressBatch` for decode-invalid case；
- calls production `applyWallOccurrenceBatch`/transaction semantics for typed cases；
- uses `EP-WALL-SHARED-01` snapshot；
- writes structured trace only to action root。

### Acceptance

- exactly 18 firings／22 input occurrences；
- unexpected scenario／row rejected；
- no market/TIS/DBA/native reader dependencies；
- no hidden retries or state reuse；
- deterministic replay produces byte-stable canonical JSON aside from declared timestamps。

---

## `EP-SCENARIO-02`｜Exact error assertions

### Problem

现有 test多处只确认任意 `Left`。

### Required behavior

逐场景记录并断言 exact constructor／payload：

```text
WallUpdateBeforeStart
WallEndBeforeStart
WallStartedTwice
WallOccurrenceRefConflict
WallInvalidPresenceTransition
MissingNumericField "core_price"
```

### Acceptance

- constructor mismatch保留 actual，不被 generic fail覆盖；
- source prediction comparison独立输出；
- actual result不被称为业务 expected；
- diagnostics source（ingress/state）分开。

---

## `EP-SCENARIO-03`｜Transaction trace integrity

### Required behavior

对 mixed-valid-invalid scenarios，同时保存：

```text
pre A
ordered input
fold result
committed post A
O/C/D
```

### Acceptance

- intermediate state只能放 debug subsection，并标 `UNCOMMITTED`；
- formal post A必须等于 pre A on rejected batch；
- no O/C on rejected firing；
- exact offending ref/identity可追溯。

---

## `EP-SCENARIO-04`｜Existing test-contract conflict ledger

### Required record

至少登记：

1. existing cross-firing Start replay test期待 idempotence；
2. current source firing-local ledger预测 `WallStartedTwice`；
3. existing after-End test只接受任意 Left，不能区分 before-start／after-end。

### Acceptance

- `EXISTING_TEST_CONTRACT_CONFLICTS.md` 指向 exact source/test commit and function；
- 不在 evidence action中擅自决定改 implementation还是改 test；
- dedicated action不以“旧 suite未运行”隐藏冲突；
- manager可据 evidence另立 expectation/diagnosis。

---

## `EP-SCENARIO-05`｜Fixture schema and provenance

### Required fields

```text
scenario_id
business_question
source_prediction
firings
ordered occurrences/rows
identity/ref/UTI/payload
origin=CONTROLLED
expected distinction
non-goals
```

### Acceptance

fixture hash、schema version、base/precondition commit均进入 manifest；Dormant/restore明确在 core action外。

# 5. Prerequisite dependency graph

```text
EP-WALL-SHARED-01 ─┬─> EP-NORMAL-01 ─> EP-NORMAL-02 ─> EP-NORMAL-03 ─> EP-NORMAL-04
                    │                    └──────────────> EP-NORMAL-05
                    └─> EP-SCENARIO-01 ─> EP-SCENARIO-02 ─> EP-SCENARIO-03
                                             └──────────> EP-SCENARIO-04/05

EP-WALL-SHARED-02 supports both targets
EP-WALL-SHARED-03 gates both actions before execution
```

normal与scenario target可以在同一 reviewed prerequisite commit交付，但它们的 G-RUN、fixture、action root、cost cap和结果必须分开。

# 6. Engineering delivery contract

完成这些前置时，应交付：

```text
PRECONDITION_REPORT.md
SOURCE_CHANGE_MANIFEST.json
base_commit / prerequisite_commit
new component declarations
fixture schemas
compile-only result
unit/property tests for observer/evidence serialization
write-surface audit
wrapper generation test
native reader roundtrip test (normal prereq only)
KNOWN_CONTRACT_CONFLICTS.md
HASHES.sha256
```

工程前置本身不能顺便运行 D002 action fixtures；“build capability ready”和“evidence action executed”必须是两个 Gate。

# 7. What does not qualify as satisfying prerequisites

以下均不合格：

- 直接修改现有 `P1EndToEndSpec.hs` 多打印几行；
- 用 `show WallLifecycleState` 解析 A；
- 用 C rows累积伪造 A；
- 用 producer state trace替代 FRP A；
- 把 current types手写成 Python dict而不经 storage/native reader；
- 覆盖 production `dbaw.py`；
- 调用现有 multi-product runner后只取 Wall结果；
- 让 Stack/global cache写出 Run目录；
- 只断言任意 `Left`；
- 为使旧 test通过而在 evidence action中临时改变实现；
- 把 controlled fixture称为 real current market material。

# 8. Manager decision points

manager可分别选择：

1. **Scenario-first**：先建设 shared + scenario prereq，以更小成本取得 terminal/replay/atomicity/late事实；
2. **Normal-readback-first**：先建设 full normal prereq，优先解除 current schema/native reader/A断点；
3. **One prerequisite commit, two later G-RUNs**：共享 observer/evidence/build closure，但动作分别执行；
4. **Bounded stop**：不建设前置，接受 current questions继续 OPEN。

E1建议优先级：

```text
shared observer/evidence schema
→ scenario target
→ normal isolated writer/wrapper/native reader
```

理由：scenario target不依赖 Python wrapper/DBA，能先以较小工程面区分最高风险的 terminal、cross-firing dedup、atomicity和late语义；但这只是优先建议，最终由 manager决定。

# 9. Current status

```text
engineering preconditions implemented: NO
source modified in C0006:            NO
build/test/run in C0006:              NO
new Worker issued:                    NO
normal action eligibility:            NEEDS_PRECONDITION
scenario action eligibility:          NEEDS_PRECONDITION
```
