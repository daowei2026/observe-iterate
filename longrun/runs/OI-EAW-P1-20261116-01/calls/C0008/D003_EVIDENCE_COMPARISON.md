# C0008｜D003 冻结 v1 限域正式证据对照报告

> **run_id**：`OI-EAW-P1-20261116-01`  
> **call_id**：`C0008`  
> **invocation token**：`9cc095198c21939058b83f439ce0be62`  
> **delegation_id**：`D003`  
> **work_item_id**：`WI-D003-P1-FORMAL-COMPARISON`  
> **stage_instance_id**：`R-P1-COMPARISON-001`  
> **analysis_round_id**：`AR-P1-001`  
> **frozen_expectation_set_id**：`FZ-EAW-P1-AR-P1-001`  
> **executor**：`chatgpt:OI-EAW-P1-20261116-01:executor:E1`  
> **return_to**：`chatgpt:OI-EAW-P1-20261116-01:manager`  
> **专业节点**：R06 / R2 限域正式证据对照  
> **边界**：不重做 D001/D002，不修改 frozen v1，不生产新产品，不做 R3/R4，不替 manager 宣布 `G-COMPARISON` 或父任务完成。

---

# 0. 正式回交摘要

D003 原专业范围已经完成：

- 12 条冻结预期全部形成正式 `EvidenceComparisonPackage`；
- 14 个冻结场景全部形成正式 `ScenarioEffectTable` 条目；
- 八类 P1 产品全部进入结果全景；
- `DataValidityFinding`、`InputMeaningFinding`、`PurposeSuitabilityFinding` 三层输入评估已分开；
- D002 的三项 `EvidenceInducedCandidate` 已保留且未改写 frozen v1；
- `DiscrepancyQueue` 已按原标准筛选，结果为空；
- 同源、派生和绘图证据已去重；
- 未把 `PROVEN_UNAVAILABLE`、artifact defect 或图层差异写成业务 `COUNTERS`；
- 未签发 Worker，未运行上游，未修改业务源码或 Project Source。

## 0.1 12 条冻结预期的正式主判断

```text
SUPPORTS   2
AMBIGUOUS  4
MISSING    6
COUNTERS   0
NOT_APPLICABLE 0
PENDING    0
```

| 正式状态 | 冻结预期 |
|---|---|
| `SUPPORTS` | `E-OWN-WALL-001`、`E-OWN-WALL-002` |
| `AMBIGUOUS` | `E-OWN-WALL-004`、`E-BIZ-P1-001`、`E-BIZ-P1-002`、`E-BIZ-P1-004` |
| `MISSING` | `E-OWN-WALL-003`、`E-BIZ-P1-003`、`E-BIZ-P1-005`、`E-BIZ-P1-006`、`E-BIZ-P1-007`、`E-BIZ-P1-008` |

## 0.2 14 个场景的正式主判断

```text
SUPPORTS   3
AMBIGUOUS  4
MISSING    7
COUNTERS   0
NOT_APPLICABLE 0
PENDING    0
```

| 正式状态 | 场景 |
|---|---|
| `SUPPORTS` | `S-WALL-001`、`S-GRAPH-010`、`S-SCOPE-011` |
| `AMBIGUOUS` | `S-DECOUPLE-002`、`S-SWITCH-003`、`S-DORMANT-005`、`S-ABSORB-013` |
| `MISSING` | `S-DIRECTION-004`、`S-ATTACK-006`、`S-F4-007`、`S-F3F4-008`、`S-MISSING-009`、`S-REPLAY-012`、`S-TIME-014` |

其中：

- `S-GRAPH-010` 的 `SUPPORTS` 只支持“图层/窗口/图元不能替代产品合同”的材料方法 anti-gold；
- `S-SCOPE-011` 的 `SUPPORTS` 只支持“所有结论必须限于 rb/hc/i 与所给窗口，不能无代表性依据泛化”的适用边界；
- 两者都不是产品业务效果支持票。

## 0.3 八产品结果全景

| 产品 | 主状态 | 当前正式回答 | 仍不可回答 |
|---|---|---|---|
| Wall | `SUPPORTS`（限域） | local lifecycle identity、Start/中间状态/End 连续性、Dormant 保持同一 local Wall、source/display 分层 | run-scoped typed identity、完整 reason/time/availability、冻结 producer provenance |
| Build | `AMBIGUOUS` | Start→Milestone*→Stop 形态、local Wall join | milestone level/threshold、Stop reason、参数、typed identity |
| AttackSegment | `MISSING` | frozen artifact 的字段和可复现 mixed endpoint defect | corrected complete product、`closed_at`、TimeBasisContract、正式业务效果 |
| Absorb | `AMBIGUOUS` | lifecycle-like 行、同 UTI multiplicity、resolve-only、zero-Wall 事实 | milestone level、quote-track/interaction 边界、typed identity |
| AttackFormationEvidence | `MISSING` | direct frozen product 缺失、latent substitution 被禁止 | 全部正式产品行为 |
| WallRelationBarrier | `MISSING` | direct frozen product 缺失、glyph/migration 不可替代 | Barrier kind/source/order 与业务效果 |
| F3 | `MISSING` | frozen direct artifact 不存在，current path 为 transient-only | dense measurement、availability/capability 与正式边界 |
| F4 | `MISSING` | 两 lane overlap 与 anti-double-counting 要求 | canonical occurrence、typed identity、lane_mask+双 grade、availability |

## 0.4 一句话结论

冻结源足以正式支持 **Wall 的 local identity/lifecycle 两条高层预期**，并足以把 Build、Absorb、跨产品 local join 的真实边界登记为 `AMBIGUOUS`；其余完整 producer/port、Attack、Formation、Barrier、F3、canonical F4、replay 与 missingness 问题，当前只能有据登记为 `MISSING`。没有一条合格业务 `COUNTERS`，因此当前没有值得进入 R3 的业务偏差。

机器可读统一包：

`daowei2026/observe-iterate@2f6e8ba82581129c98f47992bbc0164194768a50:longrun/runs/OI-EAW-P1-20261116-01/calls/C0008/D003_EVIDENCE_COMPARISON.yaml`

---

# 1. 正式输入与版本绑定

## 1.1 冻结比较合同

本次只比较：

```text
FZ-EAW-P1-AR-P1-001
```

该集合在本 Run 中正式采用 V0.6 candidate taskpack 作为工作比较合同，但：

```text
permanent_owner_acceptance = false
included_does_not_mean_owner_accepted = true
```

正式预期文本、适用条件、反例和场景来自：

- `daowei2026/observe-iterate@c88c4836269e8412e88e9ea6e7e871c0ad44f96e:longrun/runs/OI-EAW-P1-20261116-01/business_control/frozen_expectations/FZ-EAW-P1-AR-P1-001.yaml`
- `daowei2026/observe-iterate@0fff57bcc2cb85907586704a67389c038cf5ffa3:longrun/runs/OI-EAW-P1-20261116-01/calls/C0003/D001_EXPECTATION_REGISTER.yaml`

`E-IMP-DATA-001..004` 只作为 DataBinding / implementation facts 使用，没有被计入 12 条业务预期或支持票。

## 1.2 已接受的 D001/D002 事实

本次消费、但不重复生产：

- D001 正式报告与机器审计；
- D002 五项具名补证、机器审计、逐产品/预期/场景 preflight；
- D002 review-only 审计原件；
- C0007 manager 对 D002、H2、R05 与限域 R06 的正式接受。

## 1.3 Project Source

```text
basename = caegraph-data-30tick.zip
bytes    = 16,654,307
sha256   = 73e7c5f289d7b25f08f11cffda7315ad2dad3f8c323715425afdd485e15c4233
ZIP CRC  = ALL_PASS
objects  = rb / hc / i
block    = blk@steel
calendar = night_end_at_2300
```

窗口范围：

```text
6 × 30m
18 × 1m
54 × 5s
30 个带 raw snapshot 的 Tick 窗
148 个 Tick locator（其余 118 个只有定位窗）
```

该范围不是全市场、随机样本或代表性样本证明。

## 1.4 版本与 TimeBasis 的真实缺口

冻结包没有：

- `P1RunManifest`；
- frozen receipt；
- source run id / `source_run_ref`；
- producer code/config/实际参数/input market cut；
- globally typed product/occurrence refs；
- timezone、session-policy version、same-timestamp ordering；
- authoritative producer `TimeBasisContract`；
- replay/correction fixture。

Current TIS/FRP contracts只能解释当前实现可能的产品语义，不能证明它们生产了 frozen ZIP，也不能把 current default 当 frozen 参数。

---

# 2. Evidence 状态与三层发现不得混用

## 2.1 正式状态

- `SUPPORTS`：适用条件成立，证据有效、含义清楚、目的适用，替代解释未占主导；
- `COUNTERS`：只有排除明显数据、时间、身份、实现和导出问题后，证据仍与命题冲突；
- `MISSING`：判断所需正式字段、产品、时间、版本或样本不可得；
- `AMBIGUOUS`：同一真实证据存在多个仍合理且当前不能区分的解释；
- `NOT_APPLICABLE`：场景不满足命题适用条件；
- `PENDING`：过程或确认时点尚未结束。

## 2.2 三层发现

### `ARTIFACT_CONFORMANCE`

当前 frozen export 是否满足字段、时间、identity、availability 合同。

### `MATERIAL_METHOD`

图、窗口、派生视图、审计派生物是否适合承担证据。

### `BUSINESS_REASONABLENESS`

只有正式产品身份与语义合格后，产品行为才可以进入业务支持/反证。

本次严格采用：

```text
Attack mixed timestamp binding
    = ARTIFACT_CONFORMANCE
    ≠ business COUNTERS

图元不能替代 occurrence
    = MATERIAL_METHOD anti-gold
    ≠ product behavior

Formation / Barrier / F3 缺失
    = MISSING
    ≠ product unreasonable
```

---

# 3. InputAssessment

## 3.1 DataValidityFinding

```text
status = PARTIAL
```

### 已确认

- ZIP 身份、字节数、SHA-256、CRC 正确；
- manifest、calendar、timespans、object universe 和主要表可读；
- Wall/Build lifecycle 统计可复核；
- Attack/F4/Absorb 的 D002 确定性审计可复现；
- 主表不存在完整行精确重复。

### 限制

- Attack 17,856 行中 10,115 行存在 mixed endpoint timestamp binding，且没有 `closed_at`；
- F4 只有 tactical/structural source lanes；
- Formation/Barrier/F3 direct products 不存在；
- Absorb 缺 milestone level，存在 resolve-only 和 zero-Wall；
- 没有 run manifest、typed refs 和完整 availability。

## 3.2 InputMeaningFinding

```text
status = PARTIAL
```

### 含义足够清楚

- Wall local lifecycle 形态；
- Build event shape；
- same-symbol local Wall refs；
- graph/source/window/display 数据阶段；
- F4 两 lane overlap；
- Absorb 行 multiplicity、resolve-only、zero-Wall 的事实本身。

### 含义不清或不可得

- frozen producer dependency 与 run-scoped identity；
- Attack 的 authoritative business_end / closed_at；
- Absorb quote-track termination 与 formal interaction 的边界；
- canonical F4、Formation、Barrier、F3；
- valid-empty / missing / stale / history / pending。

## 3.3 PurposeSuitabilityFinding

```text
bounded formal R06 = SUITABLE_WITH_PRODUCT_AND_PURPOSE_LIMITS
integrated eight-product business effect = NOT_SUITABLE
```

可用于：

- Wall local lifecycle 的正式支持；
- formal `MISSING/AMBIGUOUS`；
- artifact-conformance 发现；
- graph/product anti-gold；
- scope/applicability boundary。

不可用于：

- 完整 producer→FRP 合同；
- Attack/F4/Formation/Barrier/F3 的产品业务效果；
- replay/correction；
- complete missingness；
- 全市场泛化。

---

# 4. 同源证据与证据阶段控制

本次对照执行下列去重规则：

1. `window_evidence` 与 source frame 是同一 lineage；
2. `wall_segments` 是 lifecycle 的显示派生，不能作为第二份独立 Wall evidence；
3. F4 tactical/structural overlap 是同一 half-second material；
4. review-only union 派生自两 lane，不是独立 source，更不是产品；
5. current TIS/FRP contracts 未与 frozen ZIP 绑定；
6. local numeric IDs 只能在 symbol/package scope 使用；
7. 图、legend、glyph 只用于定位和解释，不建立 producer authority。

因此，以下没有被重复计票：

```text
source row + window row
Wall lifecycle + wall segment
F4 tactical + structural overlap
两 lane + review-only union
current contract + frozen behavior
```

---

# 5. 12 条冻结预期正式对照

## 5.1 总表

| Expectation | 主判断 | 直接回答 | 限制或解除条件 |
|---|---|---|---|
| `E-OWN-WALL-001` | `SUPPORTS` | Wall 在包内以持续 local lifecycle 表达，而非每 tick 重建或一条显示线 | 只限 local/package identity；global typed identity 仍缺 |
| `E-OWN-WALL-002` | `SUPPORTS` | Start/State/Band/End 形态与 `wall_id=57427` 的 Start→Dormant→End 支持中间状态连续 | 完整 reason、confirm/close time 仍缺 |
| `E-OWN-WALL-003` | `MISSING` | 只能支持“图层不等于产品”的方法边界 | frozen typed ports/receipt/producer-consumer trace 缺失 |
| `E-OWN-WALL-004` | `AMBIGUOUS` | Wall 与下游表分开、refs 可 local join，与解耦一致 | 无 frozen dependency graph，hidden coupling 不能排除 |
| `E-BIZ-P1-001` | `AMBIGUOUS` | nonzero dependent refs 都能命中 same-symbol Wall，产品形态不同 | canonical run-scoped Wall identity 与独立 optionality 未建立 |
| `E-BIZ-P1-002` | `AMBIGUOUS` | Build 的 Start→Milestone*→Stop shape 得到支持 | milestone level/threshold、Stop reason、参数、typed refs 缺失 |
| `E-BIZ-P1-003` | `MISSING` | mixed endpoint defect 被准确核定 | corrected complete Attack、closed_at、TimeBasisContract 缺失 |
| `E-BIZ-P1-004` | `AMBIGUOUS` | Absorb lifecycle-like rows、多 milestone、resolve-only、zero-Wall 是真实事实 | level/typed identity 缺失，多个解释仍成立 |
| `E-BIZ-P1-005` | `MISSING` | 可以确认图层、gap、migration 不能替代 formal products | direct FormationEvidence / Barrier 缺失 |
| `E-BIZ-P1-006` | `MISSING` | 可以确认 direct F3 缺失、F4 只是 lane sources | direct F3、canonical F4、availability 缺失 |
| `E-BIZ-P1-007` | `MISSING` | overlap 事实支持不得 concat、不得丢双 grade | canonical public F4 product 不存在，无法判断产品行为 |
| `E-BIZ-P1-008` | `MISSING` | 当前包身份可固定 | run identity、typed refs、revision/replay/correction fixture 全部缺失 |

## 5.2 `E-OWN-WALL-001`｜`SUPPORTS`

### 证据

Wall 表共 45,698 行：

```text
Start       18,182
End         18,182
StateChange  8,452
BandUpdate     882
```

每个 supplied local `wall_id` 有一个 Start 和一个 End；source lifecycle、window snapshot、wall display segment 被明确区分。

### 正式解释

在当前包的 rb/hc/i 与 supplied windows 范围内，Wall 是有持续 local identity 的 lifecycle object，而不是每个 tick 重建的对象，也不是一条显示线。

### 限制

- 无 `source_run_ref`；
- 无 globally typed Wall ref；
- 无 frozen producer receipt；
- 因此不泛化为跨 run canonical identity。

## 5.3 `E-OWN-WALL-002`｜`SUPPORTS`

### 证据

`tick_000023 / i / wall_id=57427`：

```text
Start → Dormant → End
```

同一 local identity 跨中间状态保持。package-wide lifecycle closure 与该局部场景一致。

### 正式解释

Dormant 在该场景中是同一 Wall 的中间状态，并未静默变成新 Wall；Start、重要中间变化与 End 都有表达。

### 限制

完整 reason vocabulary、actual/confirm/close time 和 missing/technical state 仍不可得，因此不对完整结束原因合同下结论。

## 5.4 `E-OWN-WALL-003`｜`MISSING`

当前材料能够正式支持：

```text
source occurrence ≠ window view ≠ display segment ≠ glyph
```

但冻结包没有：

- producer receipt；
- typed public product port trace；
- frozen FRP ingress/output trace；
- source-run binding。

Current typed ports 只能说明 current implementation contract，不证明 frozen run 的 pre-L0→FRP 路径。因此本命题需要的 frozen boundary evidence 为 `MISSING`。

## 5.5 `E-OWN-WALL-004`｜`AMBIGUOUS`

### 已知

- Wall、Attack、F4-lane 分表；
- nonzero Build/Attack/Absorb `wall_local_no` 均可命中 same-symbol Wall；
- direct F3 不存在。

### 两个仍合理的解释

1. Wall 与 Attack/F3/F4 的定义确实解耦；
2. frozen producer 内存在隐藏依赖，只是 export 分表。

没有 frozen dependency graph、receipt 或 decoupling fixture，当前不能区分。因此是 `AMBIGUOUS`，不是 partial support，也不是 counter。

## 5.6 `E-BIZ-P1-001`｜`AMBIGUOUS`

### 已知

- local Wall reuse 存在；
- Build/Attack/Absorb 的 local refs 可以 join；
- 各产品 event shape 和生命周期并不相同。

### 未知

- run-scoped canonical Wall ref；
- typed product refs；
- “某产品缺失而另一个存在”究竟是业务 optionality、export filtering 还是 missingness；
- hidden coupling。

因此 local reuse 得到限域确认，但 canonical reuse + independent lifecycle/optionality 的整体命题仍 `AMBIGUOUS`。

## 5.7 `E-BIZ-P1-002`｜`AMBIGUOUS`

Build 有：

```text
43,035 Start
45,149 Milestone
43,035 Stop
```

每个 supplied `build_id` 有一个 Start 与一个 Stop。这支持 lifecycle shape。

但以下缺失：

- milestone level / threshold identity；
- complete Stop reason；
- actual/confirm contract；
- frozen parameters；
- typed refs / run identity。

因此不能从行数或样式判断 milestone 业务身份，也不能判断 Stop 是否符合完整合同。整体主判断为 `AMBIGUOUS`。

## 5.8 `E-BIZ-P1-003`｜`MISSING`

Attack 17,856 行：

```text
10,115 行 stored business_end_ts 绑定 start_uti
10,110 个偏差 = -0.5s
5 个 i session-boundary 偏差 = -21,600.5s
closed_at = absent
```

这是可复现的 `ARTIFACT_CONFORMANCE` defect。没有 corrected authoritative export、frozen receipt、`closed_at` 和 TimeBasisContract，因此无法比较 complete occurrence 的 business effect。

本项为 `MISSING`，不是 `COUNTERS`：当前 artifact 不能承担 frozen contract 的业务判断。

## 5.9 `E-BIZ-P1-004`｜`AMBIGUOUS`

Absorb：

```text
106,429 rows
31,281 Started
38,333 Milestone
36,815 Resolved
25,821 same-track/same-UTI multi-milestone rows
5,534 resolve-only tracks
63 wall_local_no=0 rows / 30 tracks
```

局部定位：

```text
tick_000023 / i / track_id=454496 / UTI=78266204
```

同 UTI 多行可以由多个 threshold levels 解释，也可以由 export multiplicity 解释；current core 提供前一种机制，但未与 frozen run 绑定。resolve-only 也可能是 quote-track termination，而不是已观察 Start 的 interaction。

缺 milestone level、typed interaction/wall refs 和 receipt，故 `AMBIGUOUS`。正式使用中不得：

- 按等价 payload 多票计数；
- 假设 resolve-only 一定有 Started；
- 把 zero-Wall 行作为正式 bound interaction。

## 5.10 `E-BIZ-P1-005`｜`MISSING`

Frozen source 没有：

- `AttackFormationEvidence` direct stream；
- `WallRelationBarrier` direct stream；
- source occurrence refs；
- Barrier kind/order-unresolved contract。

Graph adjacency、display gap、migration glyph、color 和 table order 都不能替代正式 occurrence。Current producer/typed-port 只能解释设计边界，不能证明 frozen behavior。

因此正式产品行为为 `MISSING`。

## 5.11 `E-BIZ-P1-006`｜`MISSING`

- direct F3 artifact 缺失；
- current F3 是 transient-only，`dense_active_flow_artifact=false`；
- frozen F4 是两条 source lane，不是 canonical sparse product；
- availability 只出现 code 1。

无法比较 dense measurement、valid-no-activity、missing、sparse qualification 与 FRP occurrence 边界。本项为 `MISSING`。

## 5.12 `E-BIZ-P1-007`｜`MISSING`

### overlap 的正式材料事实

```text
tactical   127,713
structural  37,846
overlap     37,846
grade differs on overlap 25,116
```

同 key 的 amount、directional hit volume proxy、timestamp 一致，grade 经常不同。因此：

```text
naive concat 会 double count
只留 max grade 会丢信息
```

这支持冻结命题中的 anti-double-counting 要求。

### 为什么主判断仍是 `MISSING`

没有 canonical producer occurrence、occurrence_ref/source_run_ref、lane_mask+双 grade output、receipt 和 availability。Attack-local merge 与 review-only union 都没有 producer authority。

对“正确产品应该如何”的一部分要求有支持，但对“frozen product 实际是否符合”的产品判断不可作，故整体主判断为 `MISSING`。

## 5.13 `E-BIZ-P1-008`｜`MISSING`

缺失：

- `P1RunManifest`；
- `source_run_ref`；
- typed product/occurrence refs；
- revision ledger；
- source correction state；
- replay fixture / correction policy。

ZIP SHA 是 package identity，不是 producer-run identity。因此 deterministic replay、atomic replacement、cross-run mixing 都不能评价。

---

# 6. 14 场景 ScenarioEffectTable

| Scenario | 状态 | 当前可回答 | 当前不可回答 |
|---|---|---|---|
| `S-WALL-001` | `SUPPORTS` | `wall_id=57427` 在 Start→Dormant→End 中保持同一 local identity | global typed identity、完整 reason/time |
| `S-DECOUPLE-002` | `AMBIGUOUS` | nonzero local refs 可 join，产品形态不同 | run-scoped canonical identity、optionality、hidden coupling |
| `S-SWITCH-003` | `AMBIGUOUS` | wall 57428 End、57429 在同 UTI Start，local identity 分开 | formal switch/Barrier occurrence |
| `S-DIRECTION-004` | `MISSING` | 可确认没有 direct Barrier/canonical F4 | Barrier kind/source/order 与 direction-switch behavior |
| `S-DORMANT-005` | `AMBIGUOUS` | Dormant 保持同一 local Wall 到 End | Dormant 时是否产生 formal Barrier |
| `S-ATTACK-006` | `MISSING` | frozen artifact mixed endpoint、无 closed_at | business_end 与 closed_at 的正式效果 |
| `S-F4-007` | `MISSING` | overlap 证明 concat double-count、双 grade 需保留 | canonical producer occurrence 是否存在/合格 |
| `S-F3F4-008` | `MISSING` | direct F3、canonical F4 均不可得 | dense availability 与 sparse qualification |
| `S-MISSING-009` | `MISSING` | 只观察到 availability_code=1 | valid-empty/missing/stale/history/Pending 区分 |
| `S-GRAPH-010` | `SUPPORTS` | 图能定位场景但不能创造产品 authority | graph alone 不回答业务效果 |
| `S-SCOPE-011` | `SUPPORTS` | 精确对象/窗口边界已知 | 选择依据和代表性未知 |
| `S-REPLAY-012` | `MISSING` | run/replay/correction 材料不存在 | deterministic replay、atomic replace、mixing |
| `S-ABSORB-013` | `AMBIGUOUS` | 同 UTI multiplicity 真实，current core 提供一种可能机制 | frozen threshold level 与 export multiplicity 的区分 |
| `S-TIME-014` | `MISSING` | Attack mixed endpoint 与 session-gap 放大已定位 | authoritative TimeBasisContract 与效果比较 |

## 6.1 三个 `SUPPORTS` 场景的边界

### `S-WALL-001`

是业务 lifecycle 的限域支持。

### `S-GRAPH-010`

是材料方法支持：

```text
graph locates evidence
but graph ≠ product contract
```

### `S-SCOPE-011`

是 applicability support：

```text
结论必须限制在 rb/hc/i 和给定窗口
```

它并不支持这些窗口具有代表性。

---

# 7. EvidenceInducedCandidates

冻结 v1 不变。保留 D002 三项候选：

## `EIC-D002-001`

Attack export 应显式定义 inclusive/exclusive endpoint、session-boundary TimeBasis；`business_end` 与 `closed_at` 不得被一个 graph timestamp 重新绑定。

## `EIC-D002-002`

应区分：

```text
QuoteTrackResolvedWithoutInteraction
AbsorbInteractionResolved
```

## `EIC-D002-003`

若下游需要一个同时携带两条 lane label 的 public F4 occurrence，必须有明确 producer authority；Attack-local merge 或 review-only union 不够。

以上均：

```text
status = CANDIDATE_ONLY
not part of frozen v1
not used as tested expectations in D003
```

---

# 8. DiscrepancyQueue

```text
status = EMPTY
items  = []
```

## 8.1 为什么不进入 R3

- 没有合格 `COUNTERS`；
- Attack mixed timing 是 artifact-conformance defect；
- F4/Formation/Barrier/F3 是正式产品证据缺口；
- Build/Absorb 的未决点依赖缺失 identity/semantics，尚不是 diagnosis-ready business deviation；
- Wall 的合格限域证据支持而非反驳 frozen expectations；
- 对不存在的产品继续做根因诊断只会把 input gap 偷换成 business deviation。

因此，专业建议是：若 manager 接受本包并通过 `G-COMPARISON` 的 WorkQuality/完整性审查，可考虑 R2→R5；本 E1 不替 manager 作该路由决定。

---

# 9. 问题边界总结

## 9.1 已回答

1. 在 supplied package 内，Wall 是持续 local lifecycle object，而不是 per-tick/glyph object；
2. Dormant 是同一 local Wall 在 End 前的中间状态；
3. Build 有 Start/Milestone*/Stop artifact shape；
4. all nonzero same-symbol dependent Wall refs 可 local resolve；
5. graph/window/display artifacts 不能替代 product contracts；
6. Attack timing、F4 overlap、Absorb multiplicity、direct-product availability 缺口已经精确建立；
7. 全部结论限于 rb/hc/i 与给定选择窗口。

## 9.2 只能限域回答

1. canonical Wall reuse：只能证明 same-symbol/package local reuse；
2. Build/Absorb lifecycle：只能证明 shape 和真实 multiplicity；
3. switch/Dormant：只能回答 Wall local identity，不能回答 formal Barrier；
4. F4：只能回答 lane material 的 overlap 与 anti-double-counting，不回答 canonical product behavior。

## 9.3 仍未回答，因为正式证据 `MISSING`

1. frozen producer→FRP boundary；
2. complete Attack business_end/closed_at；
3. canonical F4 product；
4. FormationEvidence、WallRelationBarrier、F3 产品行为；
5. complete availability/missingness；
6. replay、revision、correction、cross-run identity。

## 9.4 未发现

```text
formal business COUNTERS = false
```

---

# 10. Worker、工具与写面

本 D 零 W 完成：

```text
Worker Orders       0
Worker Returns      0
accepted worker refs 0
Linux writes        0
upstream reruns     0
source changes      0
new producer outputs 0
```

原因：固定 Project Source、D001/D002 已接受事实和 GitHub 原件均可直接读取；D003 不要求、也不允许为已证明不存在的产品补造 W 或一次性 producer output。

---

# 11. D003 完成条件逐项核对

| 完成条件 | 结果 |
|---|---|
| 12 条冻结预期全部有 evidence package | 完成 |
| 14 场景全部有 effect/status | 完成 |
| 八产品全部进入 summary | 完成 |
| 三层 InputAssessment | 完成 |
| 每个 `COUNTERS` 排除输入/实现解释 | 无 `COUNTERS`，不适用 |
| 每个 `MISSING/AMBIGUOUS` 有缺项/来源/解除条件 | 完成，详见 YAML |
| 同源证据不重复计票 | 完成 |
| EIC 与 frozen v1 分开 | 完成 |
| DiscrepancyQueue 只含值得诊断项 | 完成，空队列 |
| 已回答/限域/未决边界 | 完成 |
| 专业报告和机器包 | 完成 |
| V2 Return | 在本报告提交后单独发布 |

D003 专业范围可记为：

```text
REPORTED_COMPLETE
```

这只表示原委派的限域 R06 已完整执行；不表示 `G-COMPARISON` 已通过，不表示 H3、R3、R4、R5 或父任务完成。

---

# 12. 原 manager 的合法后继边界

D003 回交后，原 manager 可：

1. 验收 D003 WorkQuality 和 V2 机器合同；
2. 判断 `G-COMPARISON`；
3. 核对 12/14/8 全景及三层边界；
4. 因 DiscrepancyQueue 为空，决定是否直接进入 R5；
5. 将 EIC 保留为未来候选，不无痕修改 frozen v1；
6. 对未来若要生产新 receipt-bound 产品，另行形成新任务/授权。

本 E1 不宣布这些 Gate 或后继已经发生。

---

# 13. 专业边界声明

本报告：

- 不把缺证写成反证；
- 不把 artifact defect 写成业务错误；
- 不把图层/审计派生物写成 producer product；
- 不把 current implementation 写成 frozen producer；
- 不修改 frozen v1；
- 不作 R3/R4；
- 不宣布任何产品全局合理或不合理；
- 不宣布 `G-COMPARISON`、H3 或父任务完成。

D003 原专业范围内的限域正式证据对照已完成，并正式回原 manager。
