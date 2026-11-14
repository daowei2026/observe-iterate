# D002｜Current Normal-Chain Evidence Action Design

> `action_id`：`ARUN-WALL-NORMAL-001`  
> `run_id`：`OI-EAW-WALL-20261114-01`  
> `delegation_id`：`D002`  
> action type：**deterministic current-code replay + isolated current-writer materialization + staged native readback**  
> 当前 eligibility：**`NEEDS_PRECONDITION`**  
> 本文件是动作合同，不是执行回执。C0006 未 build、未 test、未 run、未生成 current material、未修改源码或 wrapper。

# 1. 动作要区分的问题

## 1.1 Parent questions

```text
Q-WALL-IDENTITY-LIFECYCLE
Q-WALL-PUBLICATION-STATE
Q-WALL-BUSINESS-SUITABILITY
```

## 1.2 WORKING expectations / scenarios

```text
EV-WALL-END-001
EV-WALL-PUBLICATION-001
EV-WALL-TXN-001（仅正常路径不触发错误的基线）
EV-WALL-TIME-001（只保留 ordered fixture time，不判断 late policy）
S01 Start Present
S03 Present→BandUpdate Alive
S07 Present→End
S19 same identity multi-legal-update in one firing
EIC-02 End measurement contract
```

## 1.3 Distinguishing questions

本动作只回答：

1. current FRP checkout 下 normal Start／update／End 的 O/C/A/D 关系是什么；
2. 同一 firing 同一 identity 两条合法 update 时，O 是否保留两条、C 是否只保留最后 update、A 是否为最后 state；
3. End 是否形成 O End + C Ended，并使 A 删除；
4. current canonical writer 的真实 ADT/schema 能否被隔离物化；
5. staged generated wrapper + native Python reader 是否能无损读回 O/C/D；
6. current End occurrence 对最后 band/core 的合同与 legacy `0 + not_present` 是否相同。

本动作不回答：

- 真实行情中这些场景的频率；
- WallAssembler 当前参数或识别质量；
- duplicate/conflict/terminal replay/atomicity/late policy；
- current 生产环境或生产 reader PASS；
- full business suitability。

# 2. 为什么采用 deterministic replay，而不是现有 real-run runner

现有入口：

```text
/dwdhome/fy/BASE_E6_2/mquant/tis/test/integration/verify_eaw_p1_real_run.py
```

它会：

- Stack build `trade-poc:exe:ts`；
- 生成 Wall、两组大单、Build、Attack、Absorb；
- 执行四个 FRP product；
- 要求 clean TIS/FRP worktree；
- 只把 evidence-dir 约束为独立目录，不能保证 cache、product、task-linker、migration log 等全部写入 Run 写面。

当前真实工作区又有与 P1 Wall 无关的既有 dirty。该入口不是 wall-only，也不是本问题所需的最小动作，因此本合同**明确不调用它**。

本动作改用一个固定的正常链 replay fixture，只让 current Wall ingress／lifecycle／publication／storage/readback 参与。这样：

- 不重算 WallAssembler；
- 不需要市场数据大窗或预热；
- 可确定地制造 same-firing 两条合法 update；
- 可把 O/C/A/D 和 native readback 放入同一小型 evidence package；
- 不把 controlled fixture 冒充自然 current market material。

# 3. Current code baseline

## 3.1 Exact source baseline

```text
FRP repo  = daowei2026/frp
commit    = cac6c912dd65a14acbd591ca57e0afd8ddb4ef13
branch at W001 checkout = eaw/p123-integration-20260820
path      = /dwdhome/fy/BASE_E6_2/edh-universe/frp/frp
```

P1 Wall 相关路径在 W001 核验时与该 commit 一致；working tree 的其他 dirty 不进入本动作。未来执行必须使用**新的、隔离、clean、只写 action root 的 staged worktree**，不能直接复用共享 dirty checkout。

若工程前置形成新 commit，动作必须绑定：

```text
base_commit        = cac6c912...
precondition_commit = <reviewed exact descendant>
```

两者均写入 manifest；不得只写 branch 名。

## 3.2 Current typed contracts

current source 已存在：

```text
WallLifecycleOccurrence
WallCurrentView
WallLifecycleError
WallLifecycleOutputs
WallOccurrenceBatch
WallCurrentBatch
WallDiagnostic
```

当前 writer：

```text
wall_occurrences   : WallOccurrenceBatch
wall_current_view  : WallCurrentBatch
wall_diagnostics   : WallDiagnostic
```

current 代码明确：

- A=`wallLifecycleCurrent` 是 full active map Dynamic；
- C=`wallLifecycleCurrentUpdates` 是本 firing update rows；
- End 形成 Ended current update，并从 active map删除 identity；
- C writer不是 full snapshot。

## 3.3 Existing test baseline

现有 test target：

```text
cabal component = frp:eaw-p1-v1-6-1-light-integration
main             = test/Frp/Instance/ISL/Eaw/P1/P1EndToEndSpec.hs
```

它能调用 `applyWallOccurrenceBatch` 并检查部分 transition，但不能作为本动作入口，因为：

- 没有结构化 O/C/A/D trace；
- `WallLifecycleState` 字段未暴露，不能直接观察 A/update map；
- 没有 current writer 隔离物化与 native readback；
- 只输出 process exit／smoke string；
- 某些 assertion 只要求任意 `Left`，不能区分 exact terminal error；
- 现有 cross-firing duplicate test 预期与 current firing-local ledger 实现存在静态冲突，必须先单独校正测试合同。

所以不能把“已有轻量 test 文件”误写成 action-ready harness。

# 4. Exact replay fixture

## 4.1 Fixture identity

```text
fixture_id                 = FX-WALL-NORMAL-001
fixture_class              = CONTROLLED_REPLAY_WITH_REAL_CHAIN_SEED
business object            = rb
calendar label             = night_end_at_2300
wall identity              = WallIdentity 1
side                       = BidWall
source artifact reference  = exact D001 historical upstream artifact
raw market run             = NOT PERFORMED
WallAssembler params       = NOT APPLICABLE
market warmup              = NOT APPLICABLE
```

真实三行只提供 normal seed；额外的 second update 是显式 controlled row。fixture manifest 必须给每一行 `origin=REAL_SEED` 或 `origin=CONTROLLED_EXTENSION`。

## 4.2 Ordered firings

### F1｜Start

```text
firing_id     = F1
ordered input = [R-START]
identity      = WallIdentity 1
ref           = exact historical ref ...:72335299:1:4
UTI           = 72335299
change        = WallStarted
presence      = Alive
band          = [4270, 4270]
core          = 4270
origin        = REAL_SEED
```

Expected:

```text
O = [Start]
C = [Present(Start)]
A = {1 -> Present(Start)}
D = []
```

### F2｜Two legal updates in one firing

```text
firing_id = F2
ordered input:
  1. R-BAND-1
     ref      = exact historical ref ...:72335302:1:5
     UTI      = 72335302
     band     = [4269, 4270]
     core     = 4269.8527778236985
     presence = Alive
     origin   = REAL_SEED

  2. R-BAND-2
     ref      = controlled:wall__stream:72335303:1:5:second-update
     UTI      = 72335303
     band     = [4268, 4270]
     core     = 4269.4
     presence = Alive
     origin   = CONTROLLED_EXTENSION
```

Expected:

```text
O = [BandUpdate-1, BandUpdate-2] in input order
C = [Present(BandUpdate-2)] only
A = {1 -> Present(BandUpdate-2)}
D = []
```

该 firing 是本动作最关键的区分点。若实际 C 有两行、A 不是最后 update 或 O 顺序丢失，分别形成正式差异证据；不得通过后处理把结果改成 expected。

### F3｜End

```text
firing_id     = F3
ordered input = [R-END]
identity      = WallIdentity 1
ref           = exact historical ref ...:72335308:1:7
UTI           = 72335308
change        = WallEnded(producer-reason-code-2)
origin        = REAL_SEED
```

Expected:

```text
O = [End]
C = [Ended(End)]
A = {}
D = []
```

current typed End payload 的 measurement shape 必须原样导出，不能用 legacy storage projection 补 `band/core=0`。

## 4.3 Time contract

```text
fixture firing order = F1 < F2 < F3
within F2 order       = R-BAND-1 before R-BAND-2
payload UTI           = preserved independently
writer/test time      = deterministic fixture time chosen by harness
actual/confirm/known  = NOT CLAIMED unless explicitly represented by current type
```

同一 firing 的含义由 fixture batch boundary 决定，不靠 UTI 相等猜测。

# 5. Required observation surfaces

每个 firing 必须在一个 atomic evidence record 中保存：

```text
fixture_id
firing_id
ordered_inputs
pre_active_map
accepted_occurrences (O)
current_updates (C)
post_active_map (A)
diagnostics (D)
exact error, if any
writer rows
native readback rows
source/ref/UTI/origin
```

## 5.1 O/C/D

使用 production current types 和 production `dumpWallOutputs` storage path；禁止自造另一套“近似 writer”。

## 5.2 A

A 是 lifecycle full active map，不是 producer state trace，不是 C 累积伪造结果。

必须由 current `WallLifecycleState`／`wallLifecycleCurrent` 的只读观察面导出。A 只进入 test evidence，不改变 production writer contract。

## 5.3 End measurement

同时保留：

- current typed End occurrence 的原始 ADT/BSON／native readback；
- preceding current A/C 中最后 measurement；
- legacy seed 的 upstream End measurement，作为背景引用而不是 current output 字段。

不得把三者合并成一个“修正后的 End row”。

# 6. Current schema, wrapper and reader contract

## 6.1 Current schema

Haskell canonical types：

```text
WallOccurrenceBatch
WallCurrentBatch
WallDiagnostic
```

每份物化必须提供：

```text
fields.json
schema marker
BSON/ADT type name
writer trigger axis
row/list anchor
source commit
harness commit
```

## 6.2 Generated wrapper fact

已核 `/dwdhome/fy/BASE_E6_2/mquant/worker/adt/dbaw.py` 不含 legacy 或 current Wall classes；`frp/dbaw/Main.hs` 当前 `planPySchema` 也没有三类 Wall top-level type。

正式生成入口已知：

```text
stack run dbaw > <staged-output>/dbaw.py
```

但当前未证明 wrapper generator 能无损展开 `WallDiagnostic` 内嵌的 sum-type error。未来工程前置必须实际解决这一点，不能只把类名加到列表后宣称 reader ready。

## 6.3 Staged wrapper acceptance

staged wrapper 必须：

- 生成到 action root，不覆盖 `/mquant/worker/adt/dbaw.py`；
- 包含 O/C/D 三类 top-level wrapper 和全部嵌套类型；
- 对 Start／BandUpdate／End／diagnostic 做 roundtrip；
- 保留 compact occurrence schema marker、identity/ref/UTI/change/state；
- 对不支持的 sum type 显式失败，不降级为字符串或丢字段。

若现有 generator 不支持，应先建设一个 lossless current Wall storage projection或 generator sum-type support；该建设属于工程前置，不属于本动作临时 workaround。

## 6.4 Native reader

native read 必须使用 staging import root 指向 staged wrapper，并由现有 `FrpDbaDao`／DBA 路径读取 action-root product。

验收：

- O 读回 4 occurrence；
- C 读回 3 update batches／rows，其中 F2 对该 identity 只有最后 update；
- D 合法为空，但必须有 fields/schema/read success 证据；
- O/C 各字段与 Haskell evidence trace逐字段一致；
- 空 D 表只证明 normal fixture 没有 diagnostic，不证明异常机制。

# 7. Missing exact entrypoint and named engineering prerequisites

当前不存在符合本合同的 executable／test target。最小工程前置为：

```text
EP-NORMAL-01  Dedicated evidence harness
EP-NORMAL-02  Read-only active-state observation
EP-NORMAL-03  Isolated current writer storage root
EP-NORMAL-04  Staged current Wall wrapper + native reader binding
EP-NORMAL-05  Clean exact build closure and structured manifest
```

详细验收见 `ADDITIONAL_ENGINEERING_PRECONDITION.md`。

前置完成后的**唯一动作入口合同**：

```text
cabal component:
  frp:eaw-p1-wall-normal-evidence

main source:
  test/Frp/Instance/ISL/Eaw/P1/WallNormalEvidenceMain.hs

fixture:
  <ACTION_ROOT>/input/FX-WALL-NORMAL-001.json
```

这些名字是工程前置的验收目标；当前 commit 中不存在，因此当前 action 不能标 `ELIGIBLE`。

# 8. Post-precondition command template

下列命令只在 EP-NORMAL-01～05 已经形成 reviewed exact commit、manager 另行通过 G-RUN 后才可执行：

```bash
ACTION_ROOT='/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D002/actions/ARUN-WALL-NORMAL-001'

PYTHONDONTWRITEBYTECODE=1 \
TMPDIR="$ACTION_ROOT/tmp" \
XDG_CACHE_HOME="$ACTION_ROOT/xdg-cache" \
STACK_ROOT="$ACTION_ROOT/stack-root" \
HOME="$ACTION_ROOT/home" \
<ABSOLUTE_REVIEWED_STACK> \
  --stack-yaml "$ACTION_ROOT/input/stack-overlay.yaml" \
  test frp:eaw-p1-wall-normal-evidence \
  --test-arguments \
    "--fixture $ACTION_ROOT/input/FX-WALL-NORMAL-001.json \
     --output-dir $ACTION_ROOT/evidence \
     --product-root $ACTION_ROOT/product \
     --wrapper-out $ACTION_ROOT/wrapper/dbaw.py \
     --native-readback-out $ACTION_ROOT/evidence/NATIVE_READBACK.jsonl" \
  --no-terminal
```

`<ABSOLUTE_REVIEWED_STACK>` 不是可执行占位许可。未来 `ACTION_BINDING.json` 必须把它替换为经 hash 的绝对路径；仍有尖括号时立即停止。

# 9. Complete write-surface contract

未来执行只能写：

```text
<ACTION_ROOT>/
├── input/
├── source/                 # isolated clean staged worktrees
├── stack-root/
├── tmp/
├── xdg-cache/
├── home/
├── build/                  # staged .stack-work / artifacts
├── product/                # current O/C/D isolated DBA
├── wrapper/                # staged generated wrapper
├── tasks/
├── logs/
├── evidence/
├── receipts/
└── manifest/
```

必须显式封闭：

```text
Stack cache / .stack-work
GHC temp
Python bytecode/cache
DBA product root
Fao store_dirs
worker wrapper output
native-reader import path
task files / task linker
migration logs
command logs
```

禁止写：

- shared TIS／FRP／worker checkout；
- `/m3varK`、现役 product leaf 或历史 material；
- production wrapper；
- home/global Stack cache；
- action root 外 migration／task log。

任何依赖不能重定向时，动作停止为 `NOT_EXECUTABLE_UNDER_GRANT`。

# 10. Outputs and receipts

最低输出：

```text
ACTION_BINDING.json
FIXTURE_MANIFEST.json
INPUT_FIXTURE.json
LOGIC_TRACE.jsonl
ACTIVE_MAP_TRACE.jsonl
WRITER_SCHEMA_REPORT.json
wall_occurrences/*
wall_current_view/*
wall_diagnostics/*
STAGED_WRAPPER_REPORT.json
NATIVE_READBACK.jsonl
ROUNDTRIP_COMPARISON.json
COMMAND_LOG.jsonl
COST_REPORT.json
RUN_REPORT.json
MANIFEST.json
HASHES.sha256
```

`RUN_REPORT.json` 必须逐项给：

```text
source/base/precondition commits
build target + executable hash
fixture hash
input/output counts
O/C/A/D assertions
native reader status
write-surface audit
start/end/exit code
stop reason or success
```

# 11. Cost contract

## 11.1 Fixed logical scale

```text
firings              = 3
input occurrences     = 4
expected accepted O   = 4
expected C entries    = 3 (one identity per firing; F2 last update only)
expected A snapshots  = 3
expected D entries    = 0
market data bytes     = 0
WallAssembler run     = none
```

## 11.2 Currently unknown

```text
clean build dependency closure
compile wall time
compile peak RSS
new build file count / bytes
wrapper generation compatibility/cost
native-reader import side effects
```

因此当前 eligibility 不能越过 `NEEDS_PRECONDITION`。

## 11.3 Required dry preflight and stop thresholds

未来执行前，必须先生成 dry preflight：dependency packages、rebuild set、estimated new disk、available disk、exact paths。建议 manager 冻结以下**动作预算上限**；这些是 policy cap，不是本轮实测：

```text
logical input occurrences     <= 4
product/evidence payload      <= 100 MiB
new build/cache disk          <= 2 GiB
peak RSS                      <= 4 GiB
wall clock                    <= 20 min
new files under ACTION_ROOT   <= 50,000
writes outside ACTION_ROOT    = 0
```

任何 cap 未获 manager 批准、无法监测或预测超限，停止在 dry preflight。

# 12. Physical binding and lock

未来 G-RUN 必须记录：

```text
worker logical identity
actual thread/session
actual model + effort
cwd
base/precondition commit
staged worktree paths
single-writer lock owner
lock acquisition/release
host non-secret identifier
UTC start/end
```

旧 W001 的 thread、lock、模型和运行资格不延续。

# 13. Authorization mapping

当前 Owner grant 允许 `wall-observation-work` 且只写本 Run Linux 目录；但 D002 明确禁止 build/test/run。

未来运行必须同时满足：

1. manager 对 `ARUN-WALL-NORMAL-001` 作独立 `G-RUN=PASS`；
2. G-RUN 明确授权 exact command、build target、fixture hash 和 ACTION_ROOT；
3. 所有工程前置已经进入 reviewed commit；
4. 主控核真实物理 binding、single writer 和 write surfaces。

没有新的 Owner 目标变更时不自动请求 Owner；若 write surface 必须越出原 grant，则先请求 Owner 授权，不能由 manager 替代。

# 14. Safe stop points

在以下任一条件立即停止，不进入下一阶段：

- action target／main source不存在；
- source或precondition commit不匹配；
- staged worktree不干净；
- stack／overlay／dependency path未绝对绑定或 hash 缺失；
- fixture仍有占位符、输入数量/顺序不符；
- A observer不是 current lifecycle active map；
- writer没有使用 production current types；
- wrapper缺任一 top-level／nested type或发生有损降级；
- native reader导入会写 action root 外；
- product root未被重定向；
- dry cost超过 cap；
- 发现 action root 外写入；
- build/test exit nonzero；
- output counts与实际不一致且没有结构化错误记录。

失败时保留已生成的命令、exit、hash、stop reason；不清理覆盖证据，不重试改变输入。

# 15. Recovery entry

按 stop stage 恢复：

| stop stage | recovery |
|---|---|
| precondition missing | 完成具名 EP，形成 reviewed commit，重新由 manager 判 G-RUN |
| dry cost/write audit | 修改动作预算或隔离设计；不得直接执行 |
| build failure | 固定原日志和 exact closure，另立工程修复；不在证据动作中现场改源码 |
| wrapper failure | 完成 lossless wrapper/storage projection 前置 |
| runtime mismatch | 保留 COUNTERS/AMBIGUOUS evidence，交 manager 判断 comparison/diagnosis |
| native read mismatch | 保留 Haskell writer与Python reader两侧 evidence，进入 reader/schema diagnosis候选 |

# 16. Eligibility conclusion

当前判定：

```text
ARUN-WALL-NORMAL-001 = NEEDS_PRECONDITION
```

原因不是“仍需继续调查”，而是五项已具名工程能力当前不存在或未验收：dedicated harness、A observer、isolated current writer、lossless staged wrapper/native reader、clean closed build contract。

这些前置完成后，本动作可重新评为：

```text
ELIGIBLE_WITH_LIMITS
```

其限制将始终是：controlled current-code replay，不是自然 current market sample或生产 runtime PASS。
