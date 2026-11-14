# D001｜Processing Skeleton 与 Material Plan

> `run_id`：`OI-EAW-WALL-20261114-01`  
> `delegation_id`：`D001`  
> `analysis_round_id`：`AR-WALL-001`  
> 当前材料状态：**PLAN_READY；不是 DATA_READY**  
> 当前证据边界：本文已完成需求与指定旧源码基线的专业还原；`/dwdhome/fy/BASE_E6_2` 的真实 checkout、现役参数、物化目录、读取入口和真实样本仍由 W001 核验，尚无 Worker Return。

## 1. 本文回答什么

本文为三个问题建立共同的事实/材料骨架：

- `Q-WALL-IDENTITY-LIFECYCLE`：同一 run-local Wall 怎样从 Start 经更新、休眠/恢复到 End；
- `Q-WALL-PUBLICATION-STATE`：occurrence、current update、完整 active map 与 diagnostics 怎样对应；
- `Q-WALL-BUSINESS-SUITABILITY`：后续应拿哪些真实材料，才能判断这些语义是否适合“维护上游认出的同一 Wall 生命周期”。

本文不做最终 `SUPPORTS/COUNTERS` 判断，不把旧 SHA 视为现役 tuple，也不授权重算。

## 2. 精确基线

### 2.1 需求/架构基线

- `daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/01_EFFECTIVE_SCOPE_AND_REQUIREMENT_CORRECTIONS.md`
- 同提交 `02_FINAL_P1_ARCHITECTURE.md`
- 同提交 `dsu/P1-DSU-01_Wall_生命周期_DSU.md`
- 同提交 `tables/PYTHON_PROJECTION_TABLES.csv`

该基线要求：

```text
WallIdentity = exact Wall FeatureRunIdentity + producer wall_local_no
```

FRP 不按时间、价格或 band 接近重新认墙；当前范围不包含 source correction、跨运行重认墙或因新证据重跑旧源。

### 2.2 TIS 旧源码基线

- `daowei2026/tis@ef887396e0a06d6e75be47efee0f1985ad7988a3:frp/EawBattleP.py`
- 同提交 `hf/prel0/wall_assembler.py`

### 2.3 FRP 旧源码基线

- `daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13:src/Frp/Instance/ISL/Eaw/P1.hs`
- 同提交 `P1/WallLifecycle.hs`
- 同提交 `P1/Products.hs`
- 同提交 `P1/Publication.hs`
- 同提交 `P1/FaoIngress.hs`
- 同提交 `P1/Internal/OccurrenceLedger.hs`

所有“实现行为”均只对上述旧 SHA 成立，直到 W001 对实际 checkout 完成对齐。

## 3. 处理骨架

```text
WallAssembler 的 receipt / packed sparse events / producer-private state trace
    ↓
WallOccurrenceFao：只读 committed artifact、receipt/schema/path 校验、packed row 解码
    ↓
P1DecodedIngress：typed occurrence batch 或 ingress diagnostics
    ↓
WallLifecycleP：同一 firing 内状态转移 transaction
    ├─ occurrence ledger（旧实现中每个 firing 重置）
    ├─ active Wall map
    └─ 本 firing 的 current-update map
    ↓
WallLifecycleOutputs
    ├─ wall_occurrences
    ├─ wall_current_view（update stream，不是全量快照）
    └─ wall_diagnostics（ingress + state diagnostics）
    ↓
真实样本对账所需的 receipt、active-map/state trace、band/core/price 参照
```

## 4. 分阶段合同

| 阶段 | 业务输入/身份 | 实质状态或判断 | 输出角色 | 时间语义 | 缺失/空值语义 | 当前基线事实与待核项 |
|---|---|---|---|---|---|---|
| S0 `WallAssembler` | tick/L1、VolQuant、参数、target、calendar、source scope；producer-local `wall_id` | 在同一 source run 内跨 chunk 维护 bid/ask Wall slot 与递增 local id | receipt、packed sparse events、state trace、chunk meta/carry/summary | sparse event 带 `uti`、`ts`；旧基线未把独立 confirm/known time 写成 Wall 业务字段 | availability 有 Available/Missing/Stale/SessionInvalid/Unavailable 编码 | 旧代码声明 event 4/5/6/7 = Start/BandUpdate/StateChange/End，并生成 receipt/code fingerprint；实际参数和物化位置待 W001 |
| S1 `WallOccurrenceFao` | committed WallAssembler artifact + `p1_receipts/wall_lifecycle.json` + `fields.json`/DBA | 校验 receipt kind/status/schema/path；按同一物理行组装 `NumericRow`；解码 band、presence、availability、local id | typed occurrence batch + ingress diagnostic batch | FRP transport 时点与 payload `occurredAt=uti` 都需保留；二者是否同义待真实数据核对 | 无匹配 result key、receipt/fields 缺失属于 DataUnavailable/读取失败；合法零行不能与之混同 | 旧实现 `OnlyRead`；一条解码失败会使该 firing 的整批 typed occurrence 不进入状态机 |
| S2 `WallLifecycleP` | 一个 firing 的 `[WallLifecycleOccurrence]`；身份为 receipt scope 内 `WallIdentity localNo` | 校验 transition；维护 active map；记录本 firing 最新 current update | accepted occurrence batch、full active-map Dynamic、current update batch、state diagnostics | 按到达顺序 `foldM`；旧代码未独立检查 `occurredAt` 单调性 | duplicate-only batch 是合法无正式输出；状态错误是 diagnostic，不是 ValidEmpty | 旧实现同一 firing 事务式：任一状态错误使整批不提交；真实 firing 边界/排序待核 |
| S3 publication | `WallLifecycleOutputs` | typed ADT 写入 DBA | `wall_occurrences`、`wall_current_view`、`wall_diagnostics` | writer 的 Event 时点需要与 payload UTI 对账 | 无 writer 行不能自动解释为状态没变；diagnostic 为空不能证明异常分支正确 | 旧 Publication 明确 current_view 为“本次变化的最新状态更新”，不是每时点全量 map |
| S4 readback/analysis | generated wrapper/FrpDbaDao/DBA + receipt + 三路表 + active-map/state trace | 按 exact run identity 重建链、区分正常/异常/缺失 | 本轮材料包和后续正式对照输入 | 至少保留 artifact/run、transport time、actual UTI/ts；known/confirm 若没有独立字段须明确 | NoOccurrence、ValidEmpty、DataUnavailable、InsufficientHistory、Pending 分开 | 当前真实 reader、`Cal/Cache/OnlyRead` 组合和可读范围待 W001 |

## 5. 旧实现静态事实：不得直接升级为现役结论

### 5.1 两层整批拒绝

1. `FaoIngress.partitionIngressBatch`：同一 firing 中只要存在解码错误，accepted batch 为 `Nothing`，只发 ingress diagnostics；同批合法行也不送入 DSU。
2. `WallLifecycle.applyWallOccurrenceBatch`：同一 firing 中只要任一 transition 返回错误，`stepWall` 不提交该次计算得到的 state；同批此前合法 occurrence 也不发布。

这两层的业务适用性不同，后续材料必须分别识别 ingress error 与 state error，不能都叫“transaction failed”。

### 5.2 current update 不是全量快照

- `wallLifecycleCurrent` 是完整 active map 的 Dynamic；
- `wallLifecycleCurrentUpdates` 来自本 firing 的 `wallCurrentUpdateBatch`；
- publication 只写 update stream。

同一 firing 若同一 Wall 有多条合法变化，`wall_occurrences` 可发布多条，但 current-update map 对该 identity 只保留**最后一条**。因此不能按行号或位置一一 zip；必须按 firing、identity 和 occurrence ref/UTI 对账。

### 5.3 End 的双重语义

旧实现接受 End 后：

- 将该 identity 从完整 active map 删除；
- 同时把 `WallEndedState` 的 `WallCurrentView` 放入本 firing current-update batch；
- occurrence 流保留 End。

读取端需要把 End update 解释为终止/删除语义，而不是把它当成仍活跃的完整快照行。

### 5.4 duplicate/conflict 的实际作用域

`OccurrenceLedger` 能按 ref + payload fingerprint 区分 appended / exact duplicate / conflict；但 `applyWallOccurrenceBatch` 每个 firing 都把 ledger 重置为空。因而旧代码直接保证的是：

- **同一 firing** exact duplicate 不重复发布；
- **同一 firing** same-ref different-payload 触发 conflict，并使该状态 transaction 不提交。

跨 firing 的相同 ref 并不由该 ledger 记忆；跨 firing 结果会退回由当时 active state/transition 决定。正式材料不得把“同 firing 幂等”无条件扩写为“全 run 幂等”。

### 5.5 终止身份记忆的静态反例候选

旧 `applyWallOccurrence` 在 End 后从 `wallViews` 删除 identity，且未见独立 ended-id set。`validateWallTransition` 虽有 `WallUpdateAfterEnd` 分支，但由该函数自身产生的 End 状态不会保留在 `wallViews`。按静态控制流：

- End 后 update/end 可能被分类为 before-start；
- End 后同 local id 的新 Start 可能按 `before = Nothing` 被重新接受；
- 同一 firing 中 End 后再 Start（不同 ref）也可能重新建立 active state。

这只是旧 SHA 的高价值反例候选。它是否影响现役业务取决于：当前代码是否相同、producer 是否严格保证 local id 永不复用且 End 后无事件、firing 内排序是否排除该组合。W001 和后续真实材料必须核实，不在本 D 预判最终结论。

### 5.6 时间与顺序

旧 transition 逻辑按输入到达顺序处理，没有独立校验 occurrence UTI 单调性。若真实 packed stream/FRP 保证按业务发生顺序到达，则该前提应由 receipt、DBA ts 和样本对账证明；否则晚到但状态兼容的 BandUpdate 可能被接纳。`actualTime/confirmTime/knownTime` 不应从一个 `uti` 字段自行补齐。

## 6. Material Requirement Set

| ID | 级别 | 材料 | 回答的 Q | 必需字段/时间/身份 | 数据阶段与转换损失 | 当前状态与取得路径 |
|---|---|---|---|---|---|---|
| MR-01 | 必需 | 当前 Wall product receipt、source scope、参数、schema/code version、artifact location | 三个 Q | feature instance、parameter set、target、calendar、time range、market cut、code/schema、status | 原始元数据；无业务值损失 | `UNKNOWN`；W001 查真实路径 |
| MR-02 | 必需 | 当前 checkout/worktree/HEAD/dirty 与相关源码/生成包装 | 三个 Q | repo path、branch/HEAD、文件 hash、wrapper/reader symbol | 静态事实；不能证明运行成功 | `PARTIAL`：旧 SHA 已读；实际 tuple 待 W001 |
| MR-03 | 必需 | WallAssembler packed sparse events + fields/manifest | identity/lifecycle、publication | source run、local no、ref、event code、UTI/ts、side/status、band/core、availability | producer 稀疏流；不能替代 FRP 输出 | `UNKNOWN`；优先复用现成 artifact |
| MR-04 | 必需 | `wall_occurrences` | identity/lifecycle、publication | firing/transport time、identity、ref、payload/UTI、change | 正式 accepted occurrence；整批被拒绝的输入不在此表 | `UNKNOWN`；只读 materialized writer |
| MR-05 | 必需 | `wall_current_view` update stream | publication/state | firing/transport time、identity、state、last occurrence | delta/update；不是全量快照 | `UNKNOWN`；必须与 MR-04/MR-07 联合解释 |
| MR-06 | 必需 | `wall_diagnostics` | publication、suitability | ingress vs state error、firing time、错误 payload/identity（若保存） | 只含错误分支；空表不证明正确 | `UNKNOWN`；核 writer 与 schema |
| MR-07 | 必需 | 可解释 current update 的完整 active map 或等价 state trace/replay | publication/state | 每个 firing 后 active identities/state；End 删除 | working-state/trace；可能不是公开产品 | `UNKNOWN`；优先现成 state trace，避免改正式输出 |
| MR-08 | 必需 | firing 边界、行顺序和 packed row 对应 | duplicate/transaction/late | transport timestamp、row/result key、same-firing grouping、input order | 物理接线；缺失会让 transaction 语义不可验证 | `UNKNOWN`；fields/DBA/trace 共同核实 |
| MR-09 | 有条件需要 | producer-private tick-aligned state trace、必要价格/band/core | 解释变化与反例 | wall id/status/band/core/price、UTI/ts | 高频 trace 体量大；只截与样本链对应窗口 | WallAssembler 旧合同声明存在；现役 material 待核 |
| MR-10 | 有条件需要 | duplicate/conflict/invalid/late 的自然样本或受控 fixture | lifecycle/suitability | 精确输入 batch、pre/post state、三路输出 | 自然样本优先；fixture 不冒充真实行情 | 自然样本可能缺失；后续 Gate 决定 fixture |
| MR-11 | 有条件需要 | 原始 L1/tick/QT | 仅在生产事件含义或偏差诊断需要时 | 生成 Wall 的最小源窗 | 成本高；不是基线对账必需 | 本 D 暂不读取；先用 sparse event/state trace |
| MR-12 | 可选 | CAEGraph/Notebook | 人工观察多链/局部价格背景 | 图层源值、窗口、identity 映射 | 显示值可能压缩，不可替代原表 | 现有下游 EawBattleP 图不合格；数据稳定后再决定 |
| MR-13 | 暂不准备 | Build/Attack/Absorb 独立输出 | 不属于当前 Wall 自身问题 | — | 会扩大范围 | 明确排除；仅 exact upstream/downstream identity 引用需要时查看 |
| MR-14 | 暂不准备 | 全年/全品种重算 | 当前基线不需要 | — | 历史记录显示可能高成本 | 明确禁止；若无材料只做 ActionPreflight |

## 7. 最小真实样本包

有现成材料时，优先选择一条满足以下条件的链：

```text
exact receipt / artifact
+ 同一 wall_local_no
+ Start Present
+ 至少一次非平凡 BandUpdate 或 Presence change
+ 尽可能包含 End
+ 上游 sparse event
+ wall_occurrences
+ wall_current_view update
+ wall_diagnostics
+ 可重建 active map/state trace
```

每条记录至少保存：

```text
artifact/run identity
source partition/path
firing/transport time
producer UTI/ts
wall_local_no
occurrence_ref
change/payload
pre-state
post-state
occurrence output
current update
active-map membership
diagnostic
```

样本没有 Dormant、恢复、End 或异常分支时照实标 `MISSING`，不合成伪“真实样本”。

## 8. 取得计划与停止点

### P1：消费 W001 的现场清单

W001：

- 正文：`daowei2026/observe-iterate@db0487b03bd81c6393639ac02ffe6534874dc80d:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W001/ORDER.md`
- JSON：`daowei2026/observe-iterate@ad20770c69bc431d2e9188dcecd89883bce20cfa:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W001/ORDER.json`

主控须先核实际 Codex thread、`/dwdhome/fy/BASE_E6_2` cwd、请求模型 `GPT-6.1 Sol Max`、effort、单写者和权限。当前只有正式工单原件，没有物理送达或 Worker Return。

### P2：优先复用现成物化资产

若 W001 找到同版 receipt、三路 writer 与上游 sparse events：

1. 只读核 metadata/row count/time range；
2. 选最小真实局部链；
3. 以 identity/time/ref 对账；
4. E1 决定材料使用资格；
5. 仅形成探索性 `MATERIAL_REVIEW`，不做正式支持/反证。

### P3：无资产时只做 ActionPreflight

预检必须给：最小对象/窗口、实际入口、是否重算 WallAssembler、数据量/内存/耗时依据、停止点、回执与为何足以区分问题。未经 manager 的 ActionEligibility/G-RUN，不实际启动。

### P4：后续 Gate

D001 回交后由 manager 决定：

- 是否接受 G-PLAN；
- 是否有资格启动最小运行；
- WORKING 预期是否需要返修或可进入冻结候选；
- 哪些异常场景允许保持 `MISSING`，哪些需要 fixture/补证。

## 9. 当前状态

```text
Plan:              READY
Real Linux tuple:  PENDING W001
Materialized data: UNKNOWN
Decodability:      UNKNOWN
Real sample chain: NOT OBTAINED
Expectation state: WORKING（另见 WORKING_EXPECTATIONS_AND_SCENARIOS.md）
Overall M status:  PLAN_READY
```

不能把本计划、旧源码可读或 W001 已签发写成 `DATA_READY`。
