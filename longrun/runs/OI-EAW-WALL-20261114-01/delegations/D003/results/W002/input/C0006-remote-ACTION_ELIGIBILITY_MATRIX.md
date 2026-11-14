# D002｜Action Eligibility Matrix

> `run_id`：`OI-EAW-WALL-20261114-01`  
> `delegation_id`：`D002`  
> as-of：C0006 专业回交前  
> `G-RUN`：**NOT PASSED**

## 1. Classification vocabulary

本文件只使用 D002 规定的四种动作结论：

```text
ELIGIBLE
ELIGIBLE_WITH_LIMITS
NEEDS_PRECONDITION
NOT_EXECUTABLE
```

含义：

- `ELIGIBLE`：入口、输入、写面、成本、回执和授权条件均已闭合；仍需 manager 对具体 invocation 通过 G-RUN。
- `ELIGIBLE_WITH_LIMITS`：可执行合同已闭合，但结果用途存在永久限制；仍需 G-RUN。
- `NEEDS_PRECONDITION`：缺失项已具名且可验收；在其完成前不得执行。
- `NOT_EXECUTABLE`：当前目标／grant／动作类型下不应采用，不能靠补一两个参数直接解锁。

任何分类都不等于 Owner/manager 已授权实际执行。

# 2. Current action matrix

| action / candidate | current classification | decisive reason | exact unlock or disposition | permanent evidence boundary |
|---|---|---|---|---|
| `ARUN-WALL-NORMAL-001` | **NEEDS_PRECONDITION** | 无 dedicated normal evidence target、A snapshot、isolated current writer、lossless staged Wall wrapper/native reader、closed clean build contract | 完成 `EP-WALL-SHARED-01..03` + `EP-NORMAL-01..05`；形成 reviewed exact commit、fixture/hash、absolute Stack/overlay、dry cost/write audit；manager另过 G-RUN | controlled current-code normal replay；不是自然 current market sample或 production runtime PASS |
| `ARUN-WALL-SCENARIO-001` | **NEEDS_PRECONDITION** | 无 structured scenario target／A accessor／exact-error trace；现有 test含 cross-firing idempotence与 current source的静态合同冲突 | 完成 `EP-WALL-SHARED-01..03` + `EP-SCENARIO-01..05`；形成 reviewed exact commit、9-scenario fixture、dry build/write audit；manager另过 G-RUN | current typed contract controlled fixture；不证明 producer自然可达性、native reader或市场频率 |
| existing `verify_eaw_p1_real_run.py --execute-normal` | **NOT_EXECUTABLE** | 自动 build `trade-poc:exe:ts`、运行 Wall + 两组大单 + Build/Attack/Absorb + 四个 FRP产品；要求 clean tree；写面/成本不闭合；不是两个 action的最小入口 | 不作为 D002 action。若未来另有全 P1 integration目标，应另立 task/grant/G-RUN | 即使成功也不能替代 structured A/scenario trace |
| existing `frp:eaw-p1-v1-6-1-light-integration` as final evidence | **NOT_EXECUTABLE** | 只给 smoke exit/string；A不可见；无结构化 O/C/A/D；部分 exact error未区分；existing duplicate expectation与 source冲突 | 只作为工程基线；不得原样当 evidence action。其代码可被新 dedicated harness复用 | 现有 test pass/fail不构成 current semantic evidence package |
| repeat W001-style bounded asset scan | **NOT_EXECUTABLE** | current缺口是不存在的 harness/wrapper/A observer，不是未搜到的同类文件；无新精确索引来源 | 不签 W002。只有 manager给出新的具名 provenance index时才另立 read-only action | 同边界扫描不能生成 execution capability |
| raw multi-month/year WallAssembler recomputation | **NOT_EXECUTABLE** | D002禁止运行；成本、预热、参数、写面不闭合；两个 action均可用 deterministic fixture避免 | 不进入当前计划；若未来研究 producer自然可达性，另立独立 M/R work item | 不需要用大重算回答 typed lifecycle contract |

# 3. Eligibility by contract dimension

## 3.1 `ARUN-WALL-NORMAL-001`

| dimension | current fact | status contribution |
|---|---|---|
| business question | O/C/A/D、same-firing last update、End deletion、current schema/native read | `ELIGIBLE` at design level |
| exact source baseline | FRP `cac6c912...`，相关 P1 source已核 | `ELIGIBLE_WITH_LIMITS` static only |
| exact executable target | proposed `frp:eaw-p1-wall-normal-evidence` currently absent | **NEEDS_PRECONDITION** |
| fixture | `FX-WALL-NORMAL-001` fully specified in design；file/hash not yet produced | **NEEDS_PRECONDITION** |
| A observation | current source A exists；read-only snapshot absent | **NEEDS_PRECONDITION** |
| O/C/D writer | production types/path known；action-root adapter absent | **NEEDS_PRECONDITION** |
| wrapper | generation entry known；Wall types absent；sum-type support unproven | **NEEDS_PRECONDITION** |
| native reader | static path known；staged runtime/readback unproven | **NEEDS_PRECONDITION** |
| write surfaces | complete target contract written | `ELIGIBLE` after implementation/audit |
| logical cost | exact 3 firing/4 occurrence fixture | `ELIGIBLE_WITH_LIMITS` |
| build cost | closure/RSS/time/disk unknown | **NEEDS_PRECONDITION** |
| current grant | run-local writes exist；D002 explicitly prohibits build/test/run | **NEEDS_PRECONDITION**: future G-RUN |
| result suitability | controlled current replay only | permanent `ELIGIBLE_WITH_LIMITS` |

### Reclassification rule

Only when all named EPs are accepted and a dry preflight is inside frozen caps:

```text
NEEDS_PRECONDITION
→ ELIGIBLE_WITH_LIMITS
```

It never becomes unrestricted `ELIGIBLE`, because controlled replay cannot prove natural current market behavior or production runtime.

## 3.2 `ARUN-WALL-SCENARIO-001`

| dimension | current fact | status contribution |
|---|---|---|
| business question | terminal/replay/conflict/atomicity/late exact typed semantics | `ELIGIBLE` at design level |
| source baseline | current source exact commit and static predictions known | `ELIGIBLE_WITH_LIMITS` |
| exact target | proposed `frp:eaw-p1-wall-scenario-evidence` absent | **NEEDS_PRECONDITION** |
| fixture | 9 scenarios/18 firings/22 inputs fully specified；file/hash absent | **NEEDS_PRECONDITION** |
| A observation | snapshot accessor absent | **NEEDS_PRECONDITION** |
| exact D/error | existing tests often only assert generic Left | **NEEDS_PRECONDITION** |
| current test conflict | known and bounded, but no conflict ledger artifact from harness | **NEEDS_PRECONDITION** |
| market data/params/warmup | intentionally N/A | `ELIGIBLE` |
| wrapper/native reader | intentionally N/A | `ELIGIBLE` |
| write surfaces | complete action-root contract | `ELIGIBLE` after audit |
| logical cost | fixed small fixture | `ELIGIBLE_WITH_LIMITS` |
| build cost | unknown until dry closure | **NEEDS_PRECONDITION** |
| grant | D002 forbids run | **NEEDS_PRECONDITION**: future G-RUN |
| result suitability | typed controlled behavior only | permanent `ELIGIBLE_WITH_LIMITS` |

### Reclassification rule

```text
NEEDS_PRECONDITION
→ ELIGIBLE_WITH_LIMITS
```

never unrestricted, because controlled fixture does not establish producer reachability or business correctness。

# 4. Recommended sequencing

E1 recommends, subject to manager decision：

```text
1. shared state snapshot + evidence schema + isolated build closure
2. scenario target and one G-RUN
3. consume scenario evidence, decide which expectations to freeze
4. normal writer/wrapper/native-reader prerequisites
5. normal action and one separate G-RUN
```

理由：scenario action不依赖 DBA/wrapper/native reader，能先区分当前最高风险的 terminal identity、cross-firing replay、rollback和late semantics。normal action随后解除 current O/C/A/D materialization/readback断点。

这不是把两个动作串成强依赖：manager可以独立选择 normal-first、scenario-first、both prerequisites together或 bounded stop。

# 5. G-RUN decision checklist

manager 对每个 action独立判 G-RUN前，必须收到：

```text
[ ] exact action_id
[ ] exact base + prerequisite commit
[ ] exact target/main path exists
[ ] fixture schema/file/hash
[ ] absolute Stack path/hash
[ ] exact overlay/path/commit closure
[ ] dry dependency/rebuild plan
[ ] complete ACTION_ROOT write map
[ ] product/cache/tmp/log redirection proof
[ ] cost caps and monitoring
[ ] Worker/thread/model/effort/cwd
[ ] single-writer lock
[ ] expected outputs and hash manifest
[ ] stop/recovery contract
[ ] current result-purpose boundary
```

任一未满足时，维持 `NEEDS_PRECONDITION`；不得通过口头“只跑一下”改为可执行。

# 6. Current Gate state

```text
G-RUN ARUN-WALL-NORMAL-001   = NOT PASSED
G-RUN ARUN-WALL-SCENARIO-001 = NOT PASSED
new execution authorized      = NO
new Worker issued             = NO
build/test/run in D002         = NO
```

# 7. Relation to R lane

R lane的 legacy normal-chain formal comparison已经可以独立完成，不依赖这两个 action。

同样，两个 action设计不会因为 R lane四条命题均 `SUPPORTS` 而升级资格。legacy normal support不替代 current harness、A、wrapper、terminal/replay/atomicity evidence。
