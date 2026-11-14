# D001｜WORKING Expectations、Input Suitability 与 Scenario Set

> `run_id`：`OI-EAW-WALL-20261114-01`  
> `delegation_id`：`D001`  
> `analysis_round_id`：`AR-WALL-001`  
> `expectation_version`：`EV-WALL-WORKING-v0.1`  
> `status`：**WORKING**  
> 本文件未通过 `G-EXPECTATION-FREEZE`，不得作为正式 `SUPPORTS/COUNTERS` 对照基准。

## 1. Business Intent 与来源边界

### 1.1 `OWNER_EXPLICIT`

Owner 原文只有：

> 对 `EawP1WallLifecycleFrp` 开展观察材料准备和业务合理性分析。

来源：

`daowei2026/observe-iterate@9188847b057f1e39dd210a80862f6af358b617a9:longrun/runs/OI-EAW-WALL-20261114-01/OWNER_START.md`

Owner 没有在原文中预先批准任何具体 transition、duplicate、transaction 或 publication 结论。参数标定、代码修改、全年重算、跨运行 Wall matching、source correction、Build/Attack/Absorb 独立分析不在本 D 默认范围。

### 1.2 本轮 `BUSINESS_INFERRED` 目的

基于“Wall Lifecycle”与当前管理决定，本轮候选目的为：

> 在一个 exact Wall feature run 内，持续维护 producer 已认出的同一 Wall 的可解释生命周期；为下游提供不会混淆身份、状态、终止、更新与异常的正式材料。

这是业务推导，不是 Owner 原话。它需要真实材料支持、反驳或修订。

### 1.3 `IMPLEMENTATION_DERIVED` 基线

指定旧源码只说明 `tis@ef887...`、`frp@cac6...` 的文本行为；实际 Linux checkout、生成包装、物化 reader 和数据仍待 W001。实现行为不能循环证明业务预期。

## 2. Expectation Register

### `EV-WALL-001`｜任务边界

- **origin**：`OWNER_EXPLICIT`
- **statement**：本 Run 应为 `EawP1WallLifecycleFrp` 准备真实可追溯观察材料，并对业务合理性形成有来源的分析；不能把源码阅读或计划本身记为最终合理性结论。
- **applicable**：本 Run 全部三个 Q。
- **non-applicable**：参数标定、生产修复、跨运行重认墙等另行授权事项。
- **falsifier/counterevidence**：仅交代码摘要、无真实材料也宣布任务完成；或擅自改实现。
- **evidence needed**：当前 tuple、真实材料、冻结后对照。
- **known unknowns**：Linux 资产与 reader。
- **confidence**：高。
- **owner decision required**：否。

### `EV-WALL-IDENTITY-001`｜身份作用域

- **origin**：`BUSINESS_INFERRED`
- **statement**：`wall_local_no` 只能与 exact `FeatureRunIdentity`/receipt 一起解释；裸 local no、裸 occurrence ref 不应跨 artifact/run 比较为同一 Wall。
- **source/rationale**：P1 DSU 需求与 compact-local transport 共同支持这一候选。
- **applicable**：同一 receipt/source run 下的 Wall 链。
- **non-applicable**：跨运行 matching；当前明确不做。
- **falsifier**：真实公开产品自身带有经批准的跨运行 stable identity；或下游实际只靠裸 local no 且仍能无歧义证明。
- **evidence needed**：receipt、artifact path、source scope、schema/code、local no。
- **known unknowns**：现役投影是否自动附 receipt context。
- **confidence**：中高。

### `EV-WALL-IDENTITY-002`｜生命周期不重新认墙

- **origin**：`BUSINESS_INFERRED`
- **statement**：在同一 run identity 下，Start 后的 BandUpdate、Presence change 和 End 应沿用同一 Wall identity；FRP 不因 band/core/price 接近重新认墙。
- **applicable**：上游已经正确识别 Wall 的当前 P1 职责。
- **non-applicable**：producer 本身认出新 Wall、跨运行 matching。
- **falsifier**：同一链中 identity 被 FRP 按价格重分配；或者 producer 同号实际代表不同 Wall。
- **evidence needed**：上游 sparse event、typed occurrence、receipt、三路输出。
- **known unknowns**：producer local id 的实际不复用保证。
- **confidence**：中高。

### `EV-WALL-START-001`｜合法起点

- **origin**：`BUSINESS_INFERRED`
- **statement**：一个新 Wall 的正式生命周期应由可用的 `Start Present` 建立；Start Dormant 不能静默建立一个“从未出现过”的休眠 Wall。
- **applicable**：正常 producer semantics。
- **falsifier**：业务存在“首次可见即 Dormant”且下游需要保留的真实场景。
- **evidence needed**：Start sparse event、presence/status、producer语义、输出。
- **known unknowns**：自然数据是否出现 Start Dormant。
- **confidence**：中。

### `EV-WALL-BAND-001`｜BandUpdate 保持 presence

- **origin**：`BUSINESS_INFERRED`
- **statement**：BandUpdate 只更新 band/core 等 Wall 属性，不应隐式承担 Present↔Dormant 转移；presence 改变应由具名 PresenceChange 表达。
- **applicable**：事件类型已正确分类。
- **falsifier**：producer 明确定义 BandUpdate 同时包含合法 presence change，且下游依赖该合同。
- **evidence needed**：event code/status、前后 state、band/core。
- **known unknowns**：现役 producer 是否严格分型。
- **confidence**：中高。

### `EV-WALL-PRESENCE-001`｜合法 presence 转移

- **origin**：`BUSINESS_INFERRED`
- **statement**：合法 presence 变化为 `Present→Dormant` 或 `Dormant→Present`；同状态的 PresenceChange 应视为重复、上游分类问题或其他需解释情况，而非悄然改变状态。
- **applicable**：同一未结束 identity。
- **falsifier**：真实业务要求用 PresenceChange 重申当前状态且该重申有独立意义。
- **evidence needed**：前态、输入 change、后态、diagnostic。
- **known unknowns**：同状态重申在 producer 是否可能发生。
- **confidence**：中。

### `EV-WALL-END-001`｜终止与终止证据

- **origin**：`BUSINESS_INFERRED`
- **statement**：End 后该 identity 不再属于 active map；End occurrence 和终止 update 应仍可供历史/下游解释。对同一 identity 的后续普通变化或重新 Start 应有明确拒绝、revision 或新 identity 规则，不能无痕复活。
- **applicable**：当前无 source correction、无跨运行复活的平台。
- **falsifier**：业务明确允许同一 local identity 在同一 run End 后复用，且有无歧义语义。
- **evidence needed**：End 前后 active map、occurrence/current update、后续同号输入。
- **known unknowns**：producer 是否绝对保证 End 后无同号事件。
- **confidence**：高（目的层）；现役满足性未知。

### `EV-WALL-PUBLICATION-001`｜三路输出与 active map 可对账

- **origin**：`BUSINESS_INFERRED`
- **statement**：accepted occurrence、current update、diagnostic 与完整 active map 必须能按 run identity、firing、Wall identity 和时间形成无歧义解释；`wall_current_view` 作为 update stream 不应被读成全量快照。
- **applicable**：正式 materialized outputs/readback。
- **falsifier**：读取端无法获得 firing/identity/order，导致 End、缺行或多更新无法解释。
- **evidence needed**：三路 writer、active-map/state trace、receipt、writer timestamps。
- **known unknowns**：正式 reader 是否暴露足够的 firing/order 元数据。
- **confidence**：高。

### `EV-WALL-TXN-001`｜异常不得静默污染，原子边界待证

- **origin**：`BUSINESS_INFERRED`
- **statement**：非法 occurrence 应被诊断且不应静默污染正式 current state；但“同 firing 一条非法导致其他合法 occurrence 全部拒绝”是否业务上合适，必须结合 firing 的原子业务含义判断，当前不预设答案。
- **applicable**：多 occurrence 同 firing。
- **falsifier**：错误行仍改变 state 却无 diagnostic；或 firing 只是物理同拍集合但整批拒绝造成重要合法事件丢失。
- **evidence needed**：firing 形成方式、合法+非法混合样本、pre/post state。
- **known unknowns**：同 firing 是否代表不可分割 producer transaction。
- **confidence**：前半高；原子策略低/待证。
- **owner decision required**：仅当真实证据表明存在业务取舍时，由 manager 决定是否升级 Owner。

### `EV-WALL-DUP-001`｜重复/冲突边界

- **origin**：`BUSINESS_INFERRED`
- **statement**：exact duplicate 不应制造第二份业务变化；same-ref different-payload 必须显式冲突。幂等作用域至少应与 artifact/run/firing 的真实 identity contract 一致，不能靠裸 ref 猜测。
- **applicable**：同一正式输入流与重放。
- **falsifier**：duplicate 被重复发布/更新且下游无法区分；冲突被当正常变化接受。
- **evidence needed**：input ref/payload、firing、receipt、输出和 replay。
- **known unknowns**：上游是否已永久保证 ref 唯一；DSU 是否只需同 firing 去重。
- **confidence**：中高。

### `EV-WALL-TIME-001`｜发生顺序与迟到

- **origin**：`BUSINESS_INFERRED`
- **statement**：生命周期 transition 必须依据明确的业务顺序。transport time、producer `uti/ts`、观察/确认/已知时点若不同，应保留区别；晚到或乱序不能靠当前 state 偶然兼容而无痕接受。
- **applicable**：存在异步、重放、packed rows 或跨 partition 时。
- **falsifier**：真实平台严格保证单一顺序且所有时点完全相同，可简化但需证据。
- **evidence needed**：DBA timestamp、payload UTI/ts、排序/merge 规则、late sample。
- **known unknowns**：当前数据是否只有一个时间轴。
- **confidence**：中。

### `EV-WALL-OBS-001`｜可观测/缺失状态分离

- **origin**：`BUSINESS_INFERRED`
- **statement**：`NoOccurrence`、`ValidEmpty`、`DataUnavailable`、`InsufficientHistory`、`Pending` 必须由读取成功、source scope、history/availability 和业务状态证据区分；不能把“表里没行”统一解释成没有 Wall。
- **applicable**：材料准备和后续对照。
- **falsifier**：正式产品合同已经给出一种无歧义、可验证的统一空语义。
- **evidence needed**：receipt/status、fields、范围、availability、row count、history/warmup。
- **known unknowns**：哪些状态由 producer 显式编码、哪些只属于分析层。
- **confidence**：高。

### `EV-WALL-IMPL-001`｜旧 transition 矩阵

- **origin**：`IMPLEMENTATION_DERIVED`
- **statement**：在 `frp@cac6...` 中：Start 只允许 `Nothing + Alive`；BandUpdate 必须保持 presence；PresenceChange 只允许 Present↔Dormant；Present/Dormant + End 得到 Ended；其他情况产生具名状态错误。
- **source**：`P1/WallLifecycle.hs`。
- **applicable**：仅旧 SHA。
- **counterevidence**：实际 checkout 不同或运行结果不同。
- **evidence needed**：W001 current source hash、真实/fixture trace。
- **confidence**：对旧文本高；对现役未知。

### `EV-WALL-IMPL-002`｜旧双层整批拒绝

- **origin**：`IMPLEMENTATION_DERIVED`
- **statement**：旧 ingress 在同 firing 任一 decode error 时不提交任何 typed occurrence；旧 lifecycle 在任一 state error 时不提交该 firing 的任何 state/occurrence/current update。
- **source**：`P1/FaoIngress.hs`、`P1/WallLifecycle.hs`。
- **applicable**：仅旧 SHA 且同 firing 分组相同。
- **counterevidence**：当前代码或实际 event grouping 不同。
- **evidence needed**：current source + mixed batch trace。
- **confidence**：旧文本高。

### `EV-WALL-IMPL-003`｜旧 current update 语义

- **origin**：`IMPLEMENTATION_DERIVED`
- **statement**：旧 current writer 发布本 firing 每个 identity 的最后更新；完整 active map 不直接写入该表。End 从 active map 删除但仍发布 Ended update。
- **source**：`P1/WallLifecycle.hs`、`P1/Publication.hs`。
- **applicable**：旧 SHA。
- **counterevidence**：现役 writer/reader 另有快照层。
- **evidence needed**：同 Wall 多更新 firing、End sample、actual reader。
- **confidence**：旧文本高。

### `EV-WALL-IMPL-004`｜旧 duplicate ledger 只在 firing 内

- **origin**：`IMPLEMENTATION_DERIVED`
- **statement**：旧 `applyWallOccurrenceBatch` 每个 firing 重置 occurrence ledger；因此 exact duplicate suppression/ref conflict 直接覆盖的是同一 firing，不是全 run。
- **source**：`P1/Internal/OccurrenceLedger.hs`、`P1/WallLifecycle.hs`。
- **applicable**：旧 SHA。
- **counterevidence**：上游或外层存在另一个 run-wide dedup，或现役实现已改变。
- **evidence needed**：actual ingress contract、跨 firing replay。
- **confidence**：旧控制流高。

### `EV-WALL-IMPL-005`｜旧 End identity 记忆缺口候选

- **origin**：`IMPLEMENTATION_DERIVED`
- **statement**：旧代码在 End 后从 `wallViews` 删除 identity，未见独立 ended set；由本函数自身产生的 `WallEndedState` 不保留在查找 map。静态控制流显示后续 Start 可能按新 Wall 接受，后续 update/end 更可能报 before-start，`WallUpdateAfterEnd` guard 对正常产生的状态看起来不可达。
- **source**：`P1/WallLifecycle.hs`。
- **applicable**：仅旧 SHA 且 producer 真的可能发送 End 后同号事件。
- **counterevidence**：现役代码保留 terminal ledger；或 producer/receipt 有被实际验证的永不复用/永不后发不变量。
- **evidence needed**：current code、producer invariant、End 后同号 fixture/自然 trace。
- **known unknowns**：该分支是否现实可达。
- **confidence**：旧控制流中高；业务影响待证。

### `EV-WALL-IMPL-006`｜compact local identity 依赖 receipt

- **origin**：`IMPLEMENTATION_DERIVED`
- **statement**：旧 Wall ADT/OccurrenceRef 不在每条 occurrence 内复制完整 FeatureRunIdentity；公开解释依赖已校验 receipt/artifact namespace。
- **source**：`P1/Products.hs`、`P1/Publication.hs`、`P1/FaoIngress.hs`。
- **applicable**：compact-local-v2 物理合同。
- **counterevidence**：现役 writer 在外层显式附上完整 run identity。
- **evidence needed**：真实 BSON/DBA projection 与 reader。
- **confidence**：旧文本高。

## 3. Input Suitability Assessment

### 3.1 输入有效性

当前结论：`PENDING`。

必须核：

- receipt kind/status/schema/code/artifact path；
- target/calendar/time/source scope/parameter set；
- result key、fields/dtype、row count 与 DBA timestamp；
- local no > 0、availability、event/status codes、band `lo <= core <= hi`；
- firing grouping、行顺序、重复/冲突；
- actual checkout 与旧基线是否一致。

旧 decoder 存在明确字段校验，但目前没有真实材料证明当前输入通过。

### 3.2 输入业务合理性

当前结论：`WORKING / UNOBSERVED`。

候选判断：WallAssembler sparse events 若能准确区分 Start、BandUpdate、PresenceChange、End，并保留 exact local identity、band/core 和发生顺序，则具备表达 Wall 生命周期的基础信息。反例包括：BandUpdate 与 presence 混用、同号跨 Wall 复用、End 后继续事件、有效 Wall 变化被 packed transaction 丢弃。

### 3.3 对当前目的的适用性

当前结论：`CONDITIONALLY SUITABLE, NOT YET VERIFIED`。

满足以下条件才足够支撑本轮三个 Q：

```text
exact receipt/run identity
+ producer sparse events
+ firing/order
+ three public streams
+ full active-map or equivalent trace
+ minimal price/band/core context
```

只有 `wall_current_view` 一张表、只有下游图、只有源码或只有 diagnostics 空表，均不够。

### 3.4 可继续范围与隔离范围

可继续：旧需求/源码推导、材料计划、WORKING 场景。  
隔离：现役 tuple 事实、真实 data readiness、正式支持/反证、参数/实现修复。

## 4. Scenario Expectation Set

记号：

- `O`：`wall_occurrences`；
- `C`：`wall_current_view` update；
- `A`：完整 active map；
- `D`：`wall_diagnostics`。

“旧基线”均指 `frp@cac6...` 静态控制流，不表示现役结果。

| ID | 输入与前态 | WORKING 业务预期 | 旧基线 O/C/A/D 关系 | 主要可反驳材料 | 当前状态 |
|---|---|---|---|---|---|
| S01 | 无→Start Present | 建立同一 identity 的 Present Wall | `O=Start`；`C=Present`；`A=add Present`；`D=none` | receipt、input/output、active trace | 核心正常场景，待真实样本 |
| S02 | 无→Start Dormant | 默认不建立；需诊断或显式业务例外 | 状态 error `WallMustStartPresent`；无 O/C/A commit；D=state | producer 是否允许首次 Dormant | 反例场景，待样本/fixture |
| S03 | Present→BandUpdate Alive | identity/state 不变，band/core 更新 | `O=BandUpdate`；`C=Present latest`；`A=replace Present`；D=none | 前后 band/core、presence | 核心正常场景 |
| S04 | Present→Presence Dormant | identity 不变，进入 Dormant | `O=yes`；`C=Dormant`；`A=replace Dormant`；D=none | state trace | 核心正常场景 |
| S05 | Dormant→BandUpdate Dormant | 保持 Dormant，更新 band/core | `O=yes`；`C=Dormant latest`；`A=replace`；D=none | dormant band sample | 核心正常场景 |
| S06 | Dormant→Presence Present | identity 不变，恢复 Present | `O=yes`；`C=Present`；`A=replace`；D=none | restore sample | 核心正常场景 |
| S07 | Present→End | 终止；从 active set 删除，保留终止证据 | `O=End`；`C=Ended update`；`A=delete`；D=none | End 三路+active trace | 核心正常场景 |
| S08 | Dormant→End | 同 S07 | 同 S07 | Dormant End 样本 | 核心正常场景 |
| S09 | 同 firing exact duplicate | 一次业务变化；不得重复更新 | 旧 ledger 抑制 duplicate；O/C 各只体现一次，A=最终态，D=none | 输入两条 ref/payload、输出计数 | 待 fixture/自然样本 |
| S10 | 跨 firing exact duplicate | 应有明确 run-wide/upstream 幂等合同；不能假定同 S09 | ledger 已重置：重复 Start 在 active 时可报 StartedTwice；兼容 BandUpdate 可再次接受；End 后重复 End可报 EndBeforeStart | 跨 firing replay、upstream dedup | 高价值未决 |
| S11 | 同 firing same ref、不同 payload | 显式 conflict，整批不得静默部分提交 | `WallOccurrenceRefConflict`；该 state batch 无 O/C/A commit；D=state | mixed conflict batch | 待 fixture |
| S12 | 跨 firing same ref、不同 payload | 应由上游/run contract或持久幂等规则处理；当前不能假定检测 | 旧 ledger 不记忆，按当时 transition 处理，不一定报 ref conflict | 跨 firing conflict | 高价值未决 |
| S13 | update/end before start | 不建立伪生命周期；显式诊断 | update→`WallUpdateBeforeStart`；End→`WallEndBeforeStart`；无 commit | 自然/fixture | 待证 |
| S14 | active Wall 再 Start | 不重认同一 identity；显式诊断 | `WallStartedTwice`，整批无 commit | duplicate-start trace | 待证 |
| S15 | End 后 update/end/Start | 同一 identity 终止后不能无规则复活；错误应准确表达 terminal violation | 旧代码删除 A 条目：update 可能报 BeforeStart，End 报 EndBeforeStart，Start 可能重新接受；`UpdateAfterEnd` 看似不可达 | current code、producer invariant、End 后 fixture | 最高优先静态反例候选 |
| S16 | BandUpdate 改 presence | 应由 PresenceChange 表达，不静默转移 | `WallBandUpdateChangedPresence`；整批无 commit | 输入 type/status | 待证 |
| S17 | Present→Presence Present 或 Dormant→Dormant | 重申语义未批准；默认 diagnostic | `WallInvalidPresenceTransition`；无 commit | producer 是否产生同态重申 | 待证 |
| S18 | 一条合法 + 一条 state-invalid 同 firing | 非法不得污染；合法是否随整批回滚取决于 firing 原子业务意义 | 旧 lifecycle 整批 rollback：无 O/C/A update；D=state | firing formation + mixed batch | 原子策略 PENDING |
| S19 | 同 identity 多条合法变化同 firing | occurrence 链应保留；current update/active map只需最终当前态，但必须可解释 | O 保留全部 accepted 顺序；C 对 identity 只保留最后一条；A=最后态；D=none | Start+BandUpdate、Start+End sample | 核心 publication 场景 |
| S20 | 一条合法 + 一条 decode-invalid 同 firing | 非法应有 ingress diagnostic；是否整批拒绝需结合物理 transaction 语义 | 旧 ingress 整批不送 DSU；无 O/C/A，D=ingress | packed row grouping、mixed decode batch | 原子策略 PENDING |
| S21 | 业务 UTI 乱序/晚到但 transition 类型与当前态兼容 | 必须由输入排序合同或显式 late policy决定，不应偶然接受 | 旧 transition 无 UTI 单调检查，可能接受兼容 BandUpdate/PresenceChange | DBA ts vs payload UTI、merge ordering | 高价值未决 |
| S22 | 无输出/空表/不可读/历史不足/尚待发生 | 五类状态分开；不能从一张空表下结论 | 旧 WallLifecycle ADT 未统一编码这五类；部分 availability/receipt 只在 ingress/producer | receipt、reader result、scope、warmup、availability | 材料层必测 |

## 5. 形式化关系检查要点

真实样本到达后，对每个 firing 检查：

```text
accepted typed input count
→ accepted O count（考虑 same-firing exact duplicate）
→ C identity set（每 identity 最多一个、为本 firing 最后 update）
→ A before/after delta
→ D ingress/state classification
```

特别禁止：

- 把 `C` 缺行填成“状态不变”的伪全量快照；
- 按 O/C 行号直接 zip；
- 用空 D 证明异常处理合理；
- 用裸 `wall_local_no` 跨 receipt 连接；
- 把 fixture 当真实行情样本；
- 在 expectation 冻结前给正式 `SUPPORTS/COUNTERS`。

## 6. 本轮最小对照优先级

### P0：核心正常链

S01、S03、S04/S06、S07/S08、S19，加上 receipt、active map 与三路 writer 对账。

### P1：身份/事务边界

S09～S18、S20、S21。自然样本缺失可保持 `MISSING`；低成本 fixture 与真实行情证据分层。

### P2：材料语义

S22，以及实际 `Cal/Cache/OnlyRead`、generated wrapper、FrpDbaDao 读取组合。

## 7. 进入冻结候选的必要条件

本版本只能由 manager 后继决定是否冻结。最低条件：

1. W001 或等价事实核实真实 checkout、reader 和 materialized asset；
2. 至少一条真实正常生命周期/局部链能对账 receipt、输入、O/C/A/D；
3. 明确 current update、firing/order 和 End 语义；
4. 把旧实现静态反例候选与现役事实分开；
5. 对 co-fired atomicity、cross-firing dedup、End terminality 等未知项给出 `PENDING/MISSING`，不擅自补结论。

当前：

```text
Expectation status: WORKING
Freeze gate:         NOT PASSED
Formal comparison:   NOT STARTED
Owner decision:      NOT REQUIRED YET
```
