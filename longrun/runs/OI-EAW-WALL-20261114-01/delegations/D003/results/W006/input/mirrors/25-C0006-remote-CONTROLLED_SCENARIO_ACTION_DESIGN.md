# D002｜Controlled Lifecycle Scenario Evidence Action Design

> `action_id`：`ARUN-WALL-SCENARIO-001`  
> `run_id`：`OI-EAW-WALL-20261114-01`  
> `delegation_id`：`D002`  
> action type：**deterministic typed lifecycle/ingress contract fixture**  
> 当前 eligibility：**`NEEDS_PRECONDITION`**  
> 当前执行：**NONE**。本文件没有 build、test、run、material generation 或 source modification。

# 1. Action purpose

本动作以 current FRP source 的 typed occurrence、ingress partition 和 lifecycle transaction为对象，区分以下高价值问题：

1. End 后同 local identity 的 update／End／Start 怎样分类；
2. exact duplicate 和 same-ref different-payload 的作用域；
3. firing-local ledger 是否意味着 cross-firing duplicate 不幂等；
4. 一条合法 + 一条 state-invalid 是否整批回滚；
5. 一条合法 + 一条 decode-invalid 是否整批不进入 lifecycle；
6. out-of-order payload UTI 是否被接受；
7. 每个场景的 pre/post A、O、C、D 和 exact error 是什么。

本动作只产生 current typed-contract evidence，不产生自然行情材料、不验证 Python native reader、不验证 production deployment，也不直接决定这些行为是否业务合理。正式业务判断需另冻结 expectation 后比较。

# 2. Source and test baseline

## 2.1 Exact source

```text
repo   = daowei2026/frp
commit = cac6c912dd65a14acbd591ca57e0afd8ddb4ef13
path   = /dwdhome/fy/BASE_E6_2/edh-universe/frp/frp
```

相关实现：

```text
src/Frp/Instance/ISL/Eaw/P1/WallLifecycle.hs
src/Frp/Instance/ISL/Eaw/P1/FaoIngress.hs
src/Frp/Instance/ISL/Eaw/P1/Products.hs
src/Frp/Instance/ISL/Eaw/P1/Publication.hs
src/Frp/Instance/ISL/Eaw/P1/Internal/OccurrenceLedger.hs
```

相关现有测试：

```text
test/Frp/Instance/ISL/Eaw/P1/P1EndToEndSpec.hs
component = frp:eaw-p1-v1-6-1-light-integration
```

## 2.2 Current-source facts to distinguish, not silently assume

current source：

- 每个 `applyWallOccurrenceBatch` firing 重置 occurrence ledger；
- End 从 active `wallViews` 删除 identity；
- 同 firing state error 使 batch 返回 `Left`，outer transaction 不提交；
- ingress 任一 decode error 使 typed occurrence batch 为 `Nothing`；
- transition 没有独立检查 payload UTI 单调性。

## 2.3 Existing test-contract conflicts

现有 light-integration 中：

- `wallLifecycleMustBeProductSpecificAndIdempotent` 在前一 firing Start 后，再以新 batch重放同一 Start，并期待 `Right / no publication`；
- current implementation 每 firing 重置 ledger，此时先遇到 active identity，再 Start 预期会成为 `WallStartedTwice`；
- `wallLifecycleTransitionTableMustBeComplete` 对 End 后 update 只检查“任意 Left”，不能区分 `WallUpdateAfterEnd` 与因 active entry 已删除而出现的 `WallUpdateBeforeStart`。

这不是本 D 对生产 bug 的判定，但说明现有测试不能作为精确 scenario evidence。新 harness 必须逐 error constructor 记录，且现有冲突必须在 manifest 中显式列出，不能靠不运行旧 test 隐藏。

# 3. Fixture-wide contract

## 3.1 Identity and common values

```text
fixture_id       = FX-WALL-SCENARIO-001
symbol           = rb
source scope     = controlled-fixture / uti:10..20
identity I1      = WallIdentity 1
identity I2      = WallIdentity 2（仅 conflict payload需要）
side             = BidWall
measurement M1   = band [99,101], core 100
measurement M2   = band [98,102], core 101
presence start   = Alive
availability     = WallLifecycleAvailable
```

每个 scenario 从 `emptyWallLifecycleState` 独立开始，除非该 scenario 自己列出多个 firing。不同 scenario 不共享 state／ledger。

## 3.2 Observation record

每个 firing 必须输出：

```text
scenario_id
firing_id
ordered_input_occurrences
pre_active_map
result_status = ACCEPTED | REJECTED
accepted_O
current_updates_C
post_active_map_A
diagnostics_D
exact_error_constructor
exact_error_payload
ledger_scope_note
payload_UTIs
```

对 rejected firing：

- `post A` 必须等于 pre A；
- O/C 必须为空；
- D 必须只记录真实 error；
- 不得展示 fold 中途暂态为 committed result。

# 4. Scenario contracts

以下“current-source prediction”只用于给 action 区分力；实际 evidence 与 prediction 不符时原样保存，不能修输出以满足预测。

## S-END-UPDATE｜End → update

### Input

```text
F1 [Start(I1, ref=S1, UTI=10, M1, Alive)]
F2 [End(I1,   ref=E1, UTI=11, reason=producer-end)]
F3 [BandUpdate(I1, ref=U1, UTI=12, M2, Alive)]
```

### Current-source prediction

```text
F1 accepted: A={I1 Present}, O=Start, C=Present
F2 accepted: A={}, O=End, C=Ended
F3 rejected: exact D=WallUpdateBeforeStart I1
             A remains {}, O/C empty
```

### Distinguishes

- terminal identity 是否被独立记忆；
- End 后 violation 被分类为 after-end 还是 before-start；
- `WallUpdateAfterEnd` 是否实际可达。

---

## S-END-END｜End → End

### Input

```text
F1 [Start(I1,S1,10,M1,Alive)]
F2 [End(I1,E1,11)]
F3 [End(I1,E2,12)]
```

### Current-source prediction

```text
F3 rejected: exact D=WallEndBeforeStart I1
A remains {}, O/C empty
```

### Distinguishes

terminal state memory 与重复终止分类。

---

## S-END-RESTART｜End → Start same local no

### Input

```text
F1 [Start(I1,S1,10,M1,Alive)]
F2 [End(I1,E1,11)]
F3 [Start(I1,S2,12,M2,Alive)]
```

### Current-source prediction

```text
F3 accepted
A={I1 Present(S2)}
O=[Start S2]
C=[Present S2]
D=[]
```

### Distinguishes

同 run 同 local identity 是否会在 End 后无 terminal ledger 地重新建立。该结果不能单凭 action 定性为正确或错误；需与 producer local-id invariant 和冻结业务预期比较。

---

## S-DUP-SAME-FIRING｜same-firing exact duplicate

### Input

```text
F1 [Start(I1,S1,10,M1,Alive), exact same Start(I1,S1,10,M1,Alive)]
```

### Current-source prediction

```text
accepted
O=[Start] exactly once
C=[Present] exactly once
A={I1 Present}
D=[]
```

### Distinguishes

firing-local exact duplicate suppression。

---

## S-DUP-CROSS-FIRING｜cross-firing exact duplicate

### Input

```text
F1 [Start(I1,S1,10,M1,Alive)]
F2 [exact same Start(I1,S1,10,M1,Alive)]
```

### Current-source prediction

```text
F2 rejected
exact D=WallStartedTwice I1
A remains {I1 Present}
O/C empty
```

### Distinguishes

- ledger firing-local scope；
- cross-firing replay 与现有 test “idempotent replay” expectation 的冲突；
- 上游唯一性合同是否是必要前置。

---

## S-REF-CONFLICT｜same ref, different payload

### Input

同一 firing：

```text
F1 [
  Start(I1, ref=R-CONFLICT, UTI=10, M1, Alive),
  Start(I2, ref=R-CONFLICT, UTI=10, M2, Alive)
]
```

第二条可采用不同 identity或不同 band；必须保持 same occurrence ref 且 payload fingerprint不同。

### Current-source prediction

```text
whole firing rejected
exact D=WallOccurrenceRefConflict R-CONFLICT
post A={}
O/C empty
```

### Distinguishes

same-firing ref conflict 与 transaction rollback。

---

## S-MIXED-STATE-INVALID｜one legal + one state-invalid

### Input

同一 firing：

```text
F1 [
  Start(I1,S1,10,M1,Alive),
  PresenceChange(I1,P1,11,M1,Alive)
]
```

第二条是 `Present → Present` 同态 change。

### Current-source prediction

```text
whole firing rejected
exact D=WallInvalidPresenceTransition I1 WallPresent WallAlive
post A={}
O/C empty
```

### Distinguishes

第一条合法 occurrence 是否随 state-invalid row 一起回滚，以及 D 是否精确表达错误。

---

## S-MIXED-DECODE-INVALID｜one legal + one decode-invalid

### Input

同一 physical ingress firing：

```text
row 1: complete numeric Start row
row 2: otherwise complete Start row but `core_price` missing
```

receipt fixture、result key 和 all required fields 必须固定。只通过 current `decodeWallNumericRow` + `partitionIngressBatch` 进入，不直接手工构造第二条 typed error。

### Current-source prediction

```text
typed occurrence batch = absent
exact ingress D = MissingNumericField "core_price"
lifecycle not fired
post A = pre A = {}
O/C empty
```

### Distinguishes

ingress all-or-none boundary 与 state transaction boundary。

---

## S-OUT-OF-ORDER-UTI｜out-of-order payload time

### Input

```text
F1 [Start(I1,S1,UTI=10,M1,Alive)]
F2 [BandUpdate(I1,U2,UTI=12,M2,Alive)]
F3 [BandUpdate(I1,U1,UTI=11,M1,Alive)]
```

ref 必须各不相同，firing order固定为 F1→F2→F3。

### Current-source prediction

```text
F3 accepted
O=[BandUpdate UTI=11]
C=[Present with last occurrence UTI=11]
A={I1 Present with last occurrence UTI=11}
D=[]
```

### Distinguishes

current transition 是否只按到达顺序、没有 payload UTI monotonic guard。业务上应接受、拒绝或由 ingress 排序，不由本 action 决定。

# 5. Dormant / restore disposition

current source和现有 typed test能构造：

```text
Present → Dormant → BandUpdate Dormant → Present
```

但 D001/W001 没有取得 producer contract或自然 material，证明这些 change 在 current producer 流中实际可达。

所以本动作：

```text
Dormant/restore natural reachability = NOT_APPLICABLE
Dormant/restore typed transition     = OUTSIDE CORE ACTION
```

manager 若要验证纯 transition，可在未来另加 optional scenario，但其结果只能证明 DSU typed contract，不能证明 producer reachability。

# 6. Exact entrypoint gap

当前没有符合本合同的结构化 executable。现有 `P1EndToEndSpec.hs` 不能替代。

最小工程前置：

```text
EP-SCENARIO-01 Dedicated structured harness
EP-SCENARIO-02 Read-only active-map snapshot accessor
EP-SCENARIO-03 Exact error + transaction trace output
EP-SCENARIO-04 Explicit stale-test conflict ledger
EP-SCENARIO-05 Clean isolated build/write contract
```

前置完成后的唯一目标：

```text
cabal component:
  frp:eaw-p1-wall-scenario-evidence

main:
  test/Frp/Instance/ISL/Eaw/P1/WallLifecycleScenarioEvidenceMain.hs

fixture:
  <ACTION_ROOT>/input/FX-WALL-SCENARIO-001.json
```

详细验收见 `ADDITIONAL_ENGINEERING_PRECONDITION.md`。

# 7. Post-precondition command template

仅在 reviewed prerequisite commit + manager G-RUN 后：

```bash
ACTION_ROOT='/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D002/actions/ARUN-WALL-SCENARIO-001'

PYTHONDONTWRITEBYTECODE=1 \
TMPDIR="$ACTION_ROOT/tmp" \
XDG_CACHE_HOME="$ACTION_ROOT/xdg-cache" \
STACK_ROOT="$ACTION_ROOT/stack-root" \
HOME="$ACTION_ROOT/home" \
<ABSOLUTE_REVIEWED_STACK> \
  --stack-yaml "$ACTION_ROOT/input/stack-overlay.yaml" \
  test frp:eaw-p1-wall-scenario-evidence \
  --test-arguments \
    "--fixture $ACTION_ROOT/input/FX-WALL-SCENARIO-001.json \
     --output-dir $ACTION_ROOT/evidence" \
  --no-terminal
```

仍含尖括号、target不存在或 fixture hash未冻结时不得执行。

# 8. Write surfaces

允许写：

```text
<ACTION_ROOT>/
├── input/
├── source/            # clean staged source at exact commits
├── stack-root/
├── tmp/
├── xdg-cache/
├── home/
├── build/
├── logs/
├── evidence/
└── manifest/
```

禁止写共享 FRP/TIS/worker、现役 store、历史 product、production wrapper或 action root 外 cache/log。

该 action 不应接触 `/m3varK`，不应 import TIS runtime，不应生成 Python wrapper，不应调用 `trade-poc:ts`。

# 9. Outputs

```text
ACTION_BINDING.json
FIXTURE_MANIFEST.json
INPUT_SCENARIOS.json
SCENARIO_TRACE.jsonl
STATE_SNAPSHOTS.jsonl
EXACT_ERROR_ASSERTIONS.json
SOURCE_PREDICTION_COMPARISON.json
EXISTING_TEST_CONTRACT_CONFLICTS.md
COMMAND_LOG.jsonl
COST_REPORT.json
RUN_REPORT.json
MANIFEST.json
HASHES.sha256
```

`SCENARIO_TRACE.jsonl` 每个 firing 一条 record，不允许只输出最终 pass/fail。

`SOURCE_PREDICTION_COMPARISON.json` 对每个 scenario 使用：

```text
MATCHES_CURRENT_SOURCE_PREDICTION
DIFFERS_FROM_CURRENT_SOURCE_PREDICTION
ACTION_FAILED_BEFORE_OBSERVATION
```

这不是业务 `SUPPORTS/COUNTERS`；后者必须在 expectation freeze 后由 Evidence Comparison 产生。

# 10. Cost contract

## 10.1 Fixed logical input

```text
core scenarios       = 9
logical firings      = 18
input occurrences    = 22
market data          = none
TIS/WallAssembler    = not run
DBA materialization  = none
```

## 10.2 Unknown build cost

同 normal action：clean dependency closure、compile wall time/RSS/new disk 需要 dry preflight。逻辑 runtime 本身应为常数级小 fixture，但不能用这一点替代 build cost。

## 10.3 Proposed action caps

待 manager 冻结：

```text
scenario count                = exactly 9
logical input occurrences     = exactly 22
evidence payload              <= 50 MiB
new build/cache disk          <= 2 GiB
peak RSS                      <= 4 GiB
wall clock                    <= 15 min
new files under ACTION_ROOT   <= 50,000
writes outside ACTION_ROOT    = 0
```

超限或无法监测时停在 dry preflight。

# 11. Physical binding and authorization

未来必须记录：实际 Worker/thread/model/effort/cwd、base+precondition commits、staged paths、single-writer lock、absolute Stack path/hash、overlay hash、fixture hash、UTC start/end。

旧 W001 的执行身份与锁不延续。

当前 D002 禁止 build/test/run；未来必须由 manager 对该 action 独立通过 G-RUN，授权 exact command和 ACTION_ROOT。若必须越出 Owner run-local写面，则先请求 Owner。

# 12. Safe stops

立即停止：

- dedicated target／main不存在；
- snapshot accessor不能返回真实 current `wallViews`；
- harness把中途 fold state当 committed state；
- exact error constructor未记录，只输出“Left”；
- scenario间 state泄漏；
- firing内 ordered inputs被重排；
- decode-invalid row绕过 current decoder手工造 error；
- existing cross-firing idempotence冲突未写入 manifest；
- source commit／fixture hash不一致；
- action root外写入；
- cost cap超限；
- build/test nonzero exit。

停止后保存完整证据，不现场修改实现后重跑。

# 13. Recovery and downstream routing

| result | route |
|---|---|
| harness/build prerequisite missing | 完成具名 EP，重新判 G-RUN |
| actual matches source prediction | 进入 expectation derivation/freeze；不直接判业务合理 |
| actual differs from source prediction | 保存 exact trace，进入 implementation discrepancy candidate |
| terminal / duplicate / late behavior conflicts with frozen business expectation | manager触发 formal comparison/diagnosis，不在 harness中修规则 |
| producer reachability仍未知 | 保持 natural applicability `MISSING/NOT_APPLICABLE`，不把 controlled fixture冒充市场证据 |

# 14. Eligibility conclusion

当前：

```text
ARUN-WALL-SCENARIO-001 = NEEDS_PRECONDITION
```

前置完成后可候选：

```text
ELIGIBLE_WITH_LIMITS
```

永久限制：只证明 current typed lifecycle/ingress contract 对 controlled fixture 的行为；不证明 producer自然可达性、current material/native reader或 production suitability。
