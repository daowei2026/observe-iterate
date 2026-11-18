# A｜CommonPriceTurnGroupCandidatesFrp 事件级 occurrence 理解

## 0. 产物身份与结论

| 项目 | 值 |
|---|---|
| run_id | `OI-U2-F-OBS-20261118-01` |
| work_item_id | `OI-U2-F-OBS-20261118-01-WI-A` |
| stage_instance_id | `OI-U2-F-OBS-20261118-01-M-A` |
| delegation_id | `D001` |
| 执行调用 | `C0003` |
| 特征 | `CommonPriceTurnGroupCandidatesFrp`（F｜共同价格转折候选组） |
| FRP 版本 | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c` |
| TIS 版本 | `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767` |
| 实例 | `TA_updto20240229_DBA / steel / night_end_at_2300 / 5m / rb,hc,i`；只取 `make_features(...)` 的第一项 `f` |
| A 阶段状态 | **完整** |

本产物只完成 A Skill：识别 F 真实消费、形成和公开的事件级 occurrence，区分业务主输出与中间处理结果，说明各类事件自己的发生位置、携带位置和处理关系。没有运行特征、没有选择 B 的观察位置、没有设计 C/D 的 CAEGraph，也没有处理 Q/V。

**核心结论：**

1. F 的业务主输出不是某一张成员表、Pair 表或 DataFrame，而是**某个候选 Life 的一次新 revision**；同一 Life 的正文或正式决定含义发生变化时，才形成新 revision。
2. 对外 FRP 载体是 `FrpEvent (Tick [GroupCandidatesRecord])`。一次外层 Event occurrence 是一个 publication 批次，里面可带多个候选 revision；首次批次还可只带定义而没有候选。
3. 候选 occurrence 自己的业务发表／可知位置是 `candidateKnown`，存储后为 `groupKnownFrom`。候选本身没有唯一“实际转折点”；它携带多个成员各自的 actual、confirmation、known，以及候选问题的 Calendar clock 窗口。
4. `occurrences_groupMembers`、`occurrences_groupRequired`、overlap、covered-by、previous 等是同一候选 revision 的嵌套正文或形成证据，不是各自独立的业务事件。
5. 当前正常 `from_kline` 实例链为：5m KLine 与 ScaleTurn/Zig occurrence → `FormationFrame` → `FormationMaterial` → `PairView` → `CandidateOccurrence` → F publication。

---

## 1. A1｜当前实现来源记录

| 编号 | 精确来源 | 类型／函数／入口 | 职责 | 状态 |
|---|---|---|---|---|
| SRC-01 | `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py` | `make_features(...)` | 正常实例构造；建立 KLine、ScaleTurnCalendar、domain/profile/market，并返回 `f,q,v` | 已核实 |
| SRC-02 | `daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json` | `feature_parameters.F` | 本批完整展开实例、SOF、Calendar、对象、参数和绑定 | 已核实 |
| SRC-03 | `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/CommonPriceTurnGroupCandidates.hs` | `CommonPriceTurnGroupCandidatesFrp`、`doImpl`、`buildStoredGroupFormation`、`commonTurnFormationCurrent`、`groupCandidatePublication` | Fao 主入口、形成链与 publication 边界 | 已核实 |
| SRC-04 | 同一 FRP 提交：`src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateKLineInput.hs` | `groupKLineEvents`、`buildKLineGroupSource` | 当前正常 KLine/ScaleTurn/Zig 输入如何变成逐对象 `FormationFrame` | 已核实 |
| SRC-05 | 同一 FRP 提交：`src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateTypes.hs` | `GroupTurn`、`PairBasis`、`CandidateBody`、`CandidateOccurrence`、`FormationMaterial`、`PairView` | 事件正文、身份、状态与位置类型 | 已核实 |
| SRC-06 | 同一 FRP 提交：`src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateMaterial.hs` | `FormationFrame`、`advanceMaterial` | 有限材料状态及 `FormationMaterial` 事件 | 已核实 |
| SRC-07 | 同一 FRP 提交：`src/Frp/Instance/ISL/Opportunity/U2/GroupCandidatePairs.hs` | `assessPair`、`advancePairView` | 四项 Required 判断及 `PairView` | 已核实 |
| SRC-08 | 同一 FRP 提交：`src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateEvolution.hs` | `formationQuestions`、`advanceCandidates` | complete-link 候选枚举、Life/revision、更新、关闭与稀疏发行 | 已核实 |
| SRC-09 | 同一 FRP 提交：`src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateDecisions.hs` | `resolveFormationDecisionCorrections`、`attachFormationAlternatives` | 候选正式参与决定、反证修订和候选间关系 | 已核实 |
| SRC-10 | 同一 FRP 提交：`src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateStorage.hs` | `GroupCandidatesRecord`、`GroupOccurrenceRecord`、`storeGroupOccurrence` | F 的公开存储正文及字段合法性 | 已核实 |
| SRC-11 | `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonPriceTurnGroupCandidates.py` | `CommonPriceTurnGroupCandidatesFrp`、`GroupCandidateReadSession` | Python 正常构造、主表／明细表和 exact/as-of 读取 | 已核实 |
| SRC-12 | 同一 TIS 提交：`frp/_U2GroupCandidateFields.py` | `GROUP_TABLES`、`GROUP_DTYPES` | 当前公开表字段映射 | 已核实 |
| SRC-13 | 同一 FRP 提交：`src/Frp/Instance/ISL/Geometry/ScaleTurn/ScaleTurn.hs`、`.../STCalendar.hs` | `CompleteScaleTurn`、`ScaleTurnCalendar` | 上游贴近转折 actual/confirm 语义与两轮 Event | 已核实 |

### 1.1 本实例的静态配置（不是输入 occurrence）

- SOF：`TA_updto20240229_DBA`；对象域：`steel`；对象：`rb / hc / i`。
- Calendar：`night_end_at_2300`；KLine 尺度：`5m`。
- `formationDelta=600`，单位是 `CalendarUTITick`；不能写成 600 秒或 600 分钟。配置同时给出 `units_per_open_minute=120`。
- 价格比较为 `ExactNumericPrice`，无跨对象归一化。
- 方向和 TurnType 相容性由实例矩阵决定；当前矩阵中同码相容、异码 veto，不应仅用口头“同方向”替代配置。
- domain/profile/market、FIS、Zig/ScaleTurn 参数属于处理规则和配置，不因位于 Fao 输入结构中就成为事件 occurrence。

---

## 2. A2｜输入事件级 occurrence 记录

### IN-01｜逐品种 5m KLine 收盘 occurrence

| 字段 | 说明 |
|---|---|
| 事件方向 | 输入事件；当前正常 KLine 路径的直接市场 occurrence |
| 事件载体 | 上游 `KLine` 的 `close`、`closeUti` Event；在 `groupKLineEvents` 中按同一发生合并为 `FrpEvent (Tick (Double,Int64,Double,Double))` |
| 一次 occurrence 的业务含义 | 某品种一根 5m KLine 的收盘价格及其原始 UTI／Calendar 位置到达 |
| 自身发生位置 | 外层 `Tick.ts` 是平台事件轴；F 的显式业务可知位置取 payload 中的 `closeUti`，代码将其 round 后作为 `known` |
| 携带位置 | `closeUti` 原值、round 后 UTI、折算的连续 KLine 位置、Calendar clock 值 |
| 主体范围 | `rb`、`hc`、`i` 各自独立，之后合并 |
| payload | `(closePrice, round closeUti, closeUti/step, unitsPerCalendarTick*closeUti)` |
| 产生位置 | `KLine(freq='5m') % ('closeUti as uti','close as value')`；FRP `groupKLineEvents` |
| 消费位置 | `buildKLineGroupSource`；给逐对象 Turn/覆盖投影提供当前 price、known、progress/clock |

`close` 与 `closeUti` 是同一个 KLine 收盘 occurrence 的两个字段；代码为了等到两字段同拍到齐而合并，不能把它们解释成两个业务事件。

### IN-02｜第一轮贴近转折 occurrence

| 字段 | 说明 |
|---|---|
| 事件方向 | 子处理器输出后被 F 消费的输入事件 |
| 事件载体 | `ScaleTurnCalendar` 第一项 `FrpEvent CompleteScaleTurn`，经 `wrapTickEvent` 进入 `buildKLineGroupSource` |
| 一次 occurrence 的业务含义 | 第一轮首次识别出的一个贴近转折 |
| 自身发生位置 | 上游识别／确认 occurrence；F 在当前 KLine known 到达时把它投影为成员材料 |
| 携带位置 | `actual` 点、`confirm` 点；`CompleteScaleTurn` 还含 `processInfo`，但当前 F 投影不保存该字段 |
| 主体范围 | 单品种；投影时标记 `FirstRound` |
| 身份 | `ScaleTurnCalendar/Turn/<full_dir>/value1/<confirmed>`；Life/Revision 来自该 exact 引用，不由坐标重新造身份 |
| 消费位置 | `buildKLineGroupSource.selected` → `GroupTurn` |

### IN-03｜第二轮贴近转折 occurrence

与 IN-02 的载体和位置语义相同，但来自 `ScaleTurnCalendar` 第二项 Event，投影时标记 `SecondRound`，引用路径使用 `value2`。第二轮不能与第一轮合并成无 round 区别的单一输入。

### IN-04｜`falter` Zig 状态 occurrence

| 字段 | 说明 |
|---|---|
| 事件方向 | 子处理器输出后被 F 的 KLine adapter 消费的辅助输入事件 |
| 事件载体 | `FrpEvent ZigWithStatusOcc`，经 `wrapTickEvent` 合入逐对象输入 |
| 一次 occurrence 的业务含义 | 当前 Zig 状态点更新；给实际 UTI 提供峰／谷极性 |
| 自身发生位置 | Zig Event 自己的 Tick 位置；业务 actual key 使用 `posUTI1` |
| 携带信息 | `posUTI1`、`price1`、`pivot1` 等；F 当前只据 `pivot1*price1` 的符号生成 direction/type 映射 |
| 消费位置 | `buildKLineGroupSource.advance`；为 ScaleTurn actual 位置补 `DirectionUp/Down` 与 `SourcePeak/TroughTurn` |

### 不列为 F 直接输入 occurrence 的内容

- `fcheck` Zig Event 是 `ScaleTurnCalendar` 内部检查点输入，不是 F 主处理器直接消费的独立业务输入；F 消费其已经形成的 `CompleteScaleTurn`。
- 当前 domain、profile、Calendar、相容矩阵、FIS、价格比较方法是静态处理配置。
- `Behavior` 中的 candidate dependencies、Dynamic 当前值不是新的输入 occurrence。
- 旧 `NativeSourcePlan` 路径仍保留兼容代码，但本次 `from_kline` 实例走 `GroupKLineConfiguration`，不能把旧 Source 产品列成本实例必需前置事件。

---

## 3. A3/A4｜输出事件与中间处理结果

### MID-01｜逐对象／合并的 `FormationFrame` occurrence

| 字段 | 说明 |
|---|---|
| 业务角色 | 中间处理事件 |
| 载体 | 单对象 `FrpEvent (Tick FormationFrame)`；三对象合并后为 `FrpEvent (Tick [FormationFrame])` |
| 一次 occurrence 含义 | 当前输入拍使某对象的转折、进展和覆盖材料发生；合并批次可同时含多个对象 frame |
| 自身发生位置 | 保留输入事件的外层 `Tick.ts`；payload 的 `frameKnown` 是业务可知位置，`frameProgress` 是当前 Calendar 进展 |
| payload | `frameTurns`、`framePatches`、`frameEnded`、`frameCoverage` |
| 当前实例事实 | `from_kline` 路径产生 `framePatches=[]`、`frameEnded=False`；成员 `retracted=False`，覆盖为 `CoverageObserved` |
| 下游 | `formationMaterialProcess` |

### MID-02｜`FormationMaterial` occurrence

| 字段 | 说明 |
|---|---|
| 业务角色 | 中间处理事件／有限材料当前值的更新发表 |
| 载体 | `FrpEvent (Tick FormationMaterial)` |
| 一次 occurrence 含义 | 当前 frame 已安装到形成材料 owner；给出当前有限 Turn、可枚举 Turn、进展、知识、变化端点、覆盖是否不完整 |
| 自身发生位置 | 外层 Tick 沿用 MID-01；业务 known 为 `materialKnown`，progress 为 `materialProgress` |
| 关键条件 | 有合法 Clock、未撤回且在当前 `6×Δ` 新枚举域内才进入 enumerable；被既有候选引用的端点可继续保留用于修订 |
| 下游 | `formationPairProcess` |

### MID-03｜`PairView` occurrence

| 字段 | 说明 |
|---|---|
| 业务角色 | 中间处理事件／当前 pair Required 结果 |
| 载体 | `FrpEvent (Tick PairView)` |
| 一次 occurrence 含义 | 对当前需要的跨对象 Turn pair 形成四项 Required：时间、方向、TurnType、selected bend |
| 自身发生位置 | 沿用材料 Event 的外层 Tick；判断只可使用不晚于 `materialKnown` 的知识 |
| payload | `pairMaterial`、`Map PairKey PairBasis` |
| 判断 | 任一坐标 veto → `PairVeto`；四项全 support → `PairPositive`；否则 `PairUnresolved` |
| 下游 | `formationCandidateProcess` / `advanceCandidates` |

四项 Required 的位置与语义：

1. **时间**：两个成员各自的 Calendar clock；距离 `<=2×formationDelta` 才 support；缺 Clock 明确 unresolved。
2. **方向**：两成员 direction 依配置矩阵比较。
3. **TurnType**：Peak/Trough 依配置矩阵比较。
4. **bend**：各成员 selected P/T/C 所形成的局部弯折；缺 P、Clock、知识、共线或非法 leg 保留对应 gap。

### MID-04｜候选变化批次 `Tick [CandidateOccurrence]`

| 字段 | 说明 |
|---|---|
| 业务角色 | **业务主输出的未存储逻辑 occurrence 批次**；外层批次仍是内部 publication 输入 |
| 载体 | `FrpEvent (Tick [CandidateOccurrence])` |
| 一次 occurrence 含义 | 当前 PairView 使零个、一个或多个候选形成了新 Life 或新 revision；列表每一项都是一个候选业务 occurrence |
| 自身发生位置 | 外层 Tick 沿用 PairView；每个候选自己的业务可知位置是 `candidateKnown=materialKnown` |
| 身份 | `candidateReference=(Book,Kind,Life,Revision)`；Life 对应稳定 `CandidateKey=(FormationQuestion,[TurnKey])`，TurnKey 是 `(object, turn Life)`；正文改变时新建 Revision，`candidatePrevious` 指向前一 exact |
| 下游 | `groupCandidatePublication`、存储转换 `storeGroupOccurrence` |

候选枚举和演化不是简单“把时间相近的点聚类”：

- 在 anchor 到 `anchor+6Δ` 的有限 Clock 域内，以完整连接寻找极大候选集合；成员至少两个且对象不同。
- 正面图只允许 `PairPositive`；可能图允许 `PairPositive` 或 `PairUnresolved`，所以 Supported 和 Incomplete 候选都可存在。
- 一个候选所有成员两两 positive 才是 `Supported`；任何 veto/retracted 为 `Contradicted`；其余为 `Incomplete`。
- 候选可由 `Open` 更新为 `ClosedSupported`、`ClosedInsufficient`、`Withdrawn`、`Subsumed` 或 `EndedByScope`。这些是同一候选 revision 正文中的状态，不是六条独立 FRP Event。
- 没有正文或正式决定含义变化时不发行新候选 revision；空列表不表示“候选失败”。

### OUT-01｜F 正式 publication Event

| 字段 | 说明 |
|---|---|
| 事件方向 | 输出事件 |
| 输出业务角色 | 业务主输出的正式公开载体 |
| 事件载体 | `FrpEvent (Tick [GroupCandidatesRecord])` |
| 一次外层 occurrence 含义 | 当前拍公开一份 F publication；其列表当前由一个 `GroupCandidatesRecord` 组成，该 record 可含配置定义和多个候选 revision |
| 自身发生位置 | 外层 `Tick.ts` 沿用 MID-04；每个候选正文的业务发表／可知位置是 `groupKnownFrom` |
| 公开读取 | Python `to_df()` 默认读 `occurrences`；`to_dfs()` 读主表和嵌套明细；支持 exact 与 Life/AsOf 读取 |
| 产生位置 | `groupCandidatePublication` → `publishGroupOccurrences` → `storeGroupOccurrence` |

#### OUT-01A｜候选 revision（业务主输出）

这是 OUT-01 中 `groupOccurrences` 的每一条逻辑 occurrence，字段包括：

- **身份与修订**：`groupReference` 的 Life/Revision；`groupPrevious`。
- **自身业务发生位置**：`groupKnownFrom`。
- **原问题窗口**：`groupOriginalAnchor / Deadline / RevisionEnd`。
- **当前收紧窗口**：`groupAnchor / Deadline / RevisionEnd`；代码只允许收紧，不允许把原问题续期。
- **候选当前状态**：`groupLocalBasis`（Supported/Incomplete/Contradicted）、`groupAlternative`、`groupObservation`、`groupCoverageIncomplete`、`groupClosed`。
- **成员正文**：对象、Turn exact/source、actual、price、confirmation、known、direction、type、round、Clock、selected P/T/C、Confirmed/Candidate member、retracted。
- **完整 pair Required**：每一对成员的 distance，以及 time/direction/type/bend 各自 Support/Unresolved/Veto 与明确 gap/veto 原因。
- **候选间关系**：overlap、covered-by。
- **正式形成参与决定**：Haskell 存储结构含 `groupFormationParticipation`，记录 admission、决定范围、反证修订和 candidate alternative 等。

#### OUT-01B｜定义记录（公开元数据，不是候选业务主输出）

首次 publication 会携带最多一条 `GroupDefinitionRecord`，保存 method/context/scale/calendar/universe/domain/objects/Δ/unit 和方向／类型相容矩阵。它用于解释候选正文和固定配置，不是一个“共同转折候选发生”。

实现上，第一次 MID-04 即使候选列表为空，也会发布 definition-only OUT-01；之后若没有定义且没有候选 revision，`publishGroupOccurrences` 返回 `Nothing`，正式 F Event 不发生。

### 公开明细不等于独立 occurrence

当前 Python `GROUP_TABLES` 将同一个 `GroupOccurrenceRecord` 展开为：

- `occurrences`；
- `occurrences_groupPrevious`；
- `occurrences_groupMembers` 及成员 Clock/P/T/C 子表；
- `occurrences_groupRequired` 及 pair distance；
- `occurrences_groupOverlaps`；
- `occurrences_groupCoveredBy`；
- definitions 及其对象／矩阵子表。

这些表只是同一 publication 中嵌套 ADT 的关系化读取视图。成员的一行、Pair 的一行、previous 的一行都不是新 FRP Event，也没有独立 Life。

---

## 4. A5｜事件位置总表

| 编号 | 事件／结果 | occurrence 自身发生位置 | occurrence 携带的其他位置 |
|---|---|---|---|
| IN-01 | KLine close | 平台 Tick；显式业务 known 为 `closeUti` | bar position、Calendar clock |
| IN-02/03 | 第一／二轮 CompleteScaleTurn | 上游识别／确认 occurrence；F 投影 known 取当前 KLine known | actual 点、confirm 点；P/T/C 中 T=actual、C=confirm |
| IN-04 | ZigWithStatus | Zig Tick，actual key=`posUTI1` | price/pivot 和前一状态位置 |
| MID-01 | FormationFrame | 输入 Tick；`frameKnown` | frameProgress、每个 Turn actual/confirmation/known/Clock、覆盖范围 |
| MID-02 | FormationMaterial | 沿用 frame Tick；`materialKnown` | materialProgress、有限 Turn 的各自位置、覆盖 |
| MID-03 | PairView | 沿用 material Tick | 两端 Turn 的各自 actual/known/Clock/P/T/C；pair distance |
| MID-04 | CandidateOccurrence batch | 外层 Tick；每个候选 `candidateKnown` | 候选问题 anchor/deadline/revisionEnd；所有成员 actual/confirmation/known；pair 依据 |
| OUT-01A | 存储后的候选 revision | `groupKnownFrom` 是正式业务可知／发表位置 | 原／当前 Calendar clock 窗口；成员 actual/confirmation/known/selected 点；pair 距离 |
| OUT-01B | definition-only publication | 首次 candidate-process Event 的外层 Tick | 无候选 actual 点；仅配置语境 |

### 位置解释硬边界

1. **成员 actual 不是候选 occurrence 自己的发生位置。** 一个候选包含多个成员 actual，候选发生是系统形成／修订该候选观点的 `knownFrom`。
2. **anchor/deadline/revisionEnd 不是 KLine UTI。** 它们是当前方法在 `CalendarUTITick` 空间里的形成问题窗口。
3. **confirmation 与 known 分开。** 成员保存上游 `confirm`，F 投影还保存当前 KLine `known`；不能假设二者恒等。
4. **outer `Tick.ts` 与业务字段分开。** 源码沿处理链传递 `atTickTs`，但没有在本特征合同中声明它与 `groupKnownFrom` 完全同义；后继展示和回放应以显式业务字段为准。
5. **图可以按成员 actual 叠加，但回放到 `groupKnownFrom` 之前不能显示该候选 revision 已知。**

---

## 5. A6｜处理关系记录

| 关系编号 | 上游 | 下游 | 类型 | 条件／身份和位置映射 |
|---|---|---|---|---|
| REL-01 | KLine `close` + `closeUti` | IN-01 joined quote | 形成 | 同拍两字段均到齐；price 与 closeUti 保持同一 KLine occurrence |
| REL-02 | `falter`/`fcheck` Zig | IN-02/IN-03 CompleteScaleTurn | 形成（上游子处理器） | `ScaleTurnCalendar` 两轮选择 actual/confirm；F 不重算该算法 |
| REL-03 | IN-02/03 + IN-04 + IN-01 | `GroupTurn` / MID-01 | 形成／引用 | ScaleTurn actual 绑定 object+Turn Life；Zig 在相同 actual 提供 direction/type；当前 KLine 提供 known、Calendar clock 和覆盖 |
| REL-04 | 三对象 MID-01 | 合并 `Tick [FormationFrame]` | 合并 | 同拍 frame 列表合并；对象身份保留，不把多对象值压成一条匿名 Turn |
| REL-05 | MID-01 + 当前依赖 Behavior | MID-02 | 更新 | 安装 Turn/patch/coverage；有限枚举域与既有候选依赖分别保留 |
| REL-06 | MID-02 + 当前依赖 Behavior | MID-03 | 形成／更新 | 只重算真实端点变化影响的 pair；同一个 `PairKey` 保持端点 Turn Life |
| REL-07 | MID-03 | CandidateState | 形成／更新／结束 | complete-link 候选；按固定 CandidateKey 保持 Life；正文或决定变化才创建 Revision |
| REL-08 | 旧 CandidateOccurrence | 新 CandidateOccurrence | 修订／替代 | 同 Life 新 Revision；`candidatePrevious`／`groupPrevious` 精确指前一 revision |
| REL-09 | 候选 Required 与成员状态 | local basis / member status / observation | 确认／反证／关闭 | all-positive 才 Supported；veto 形成 Contradicted；期限和 scope 决定关闭状态；严格超集支持可使子候选 Subsumed |
| REL-10 | 候选集合之间共享成员／严格覆盖 | overlap / covered-by / alternatives | 引用 | 使用候选 Life 建立直接关系；不改变两候选各自身份 |
| REL-11 | MID-04 | OUT-01 | 公开／存储 | 每个 CandidateOccurrence 转为 GroupOccurrenceRecord；批次原 Tick 保留；首次同时放定义 |
| REL-12 | 空变化批次 | 无 OUT-01 | 抑制发表 | 非首次且 rows 为空时不产生 F Event；“无 Event”不能解释成失败、撤回或结束 |

### 5.1 业务主输出向上追溯

```text
OUT-01A 候选 revision
  ← CandidateOccurrence 的 Life/Revision/previous/body/participation
  ← CandidateState 对 PairView 的 complete-link 枚举与演化
  ← PairView 中所有成员两两 time/direction/type/bend Required
  ← FormationMaterial 的有限合法 Turn、coverage、known/progress
  ← 各对象 FormationFrame
  ← 5m KLine close/closeUti + 两轮 CompleteScaleTurn + falter Zig 状态
```

### 5.2 各输入事件的可能去向

- 一个 KLine occurrence 可能只推进 known/coverage，而不形成新 Turn、Pair 或 Candidate revision。
- 一个 ScaleTurn occurrence 先形成／更新一个 `GroupTurn`；若不在有限枚举域或缺 Clock，可暂不成为 candidate member。
- 一个 Zig occurrence 只更新 actual→方向/类型的辅助映射；若没有对应 ScaleTurn，自己不形成候选。
- 新 Turn 可能使 pair positive、unresolved 或 veto；只有候选正文／决定实际变化才向下形成 CandidateOccurrence。
- 一个候选可在后续材料到达时更新、关闭、撤回或被覆盖；它仍保持原 Life，并以 revision 链表达变化。

---

## 6. A7｜交叉核对

### 6.1 从主输出向上追溯

已从 `GroupOccurrenceRecord` 的每个核心字段追到 `CandidateOccurrence/CandidateBody`，再追到 Pair、Material、FormationFrame 和正常 KLine/ScaleTurn/Zig 输入。成员 actual/confirmation/known、候选 known/window、Pair Required 均有明确代码来源。

### 6.2 从输入向下追踪

KLine、两轮 ScaleTurn 和 Zig occurrence 均可说明其可能只更新中间状态、形成候选 revision 或不形成输出的条件；没有把每次上游发生机械等同于 F 输出。

### 6.3 业务角色核对

- `CandidateOccurrence`／`GroupOccurrenceRecord` 是业务主输出。
- `FormationFrame`、`FormationMaterial`、`PairView`、当前 CandidateState 是中间处理结果。
- definitions、members、Required、overlap/covered-by、previous、formation participation 是主输出的配置或嵌套形成证据；公开保存不改变其角色。
- Python DataFrame 是读取视图，不是运行时事件定义。

### 6.4 当前实例与通用兼容路径核对

当前实例明确走 `GroupKLineConfiguration/from_kline`：

- 不要求独立 `NativeSourcePlan` 产品；
- 正常路径 `framePatches=[]`、`frameEnded=False`，不发行 `GroupCoverageCorrection`；
- 当前输入投影将 `memberRetracted=False`。

源码还保留 stored-source、有限修订、coverage correction 和 scope-end 能力，但这些不能无依据写成本实例已经发生的输入／输出。

---

## 7. 当前公开读取接口与字段可用性

### 可直接读取

- `f.to_df()`：`occurrences` 主表。
- `f.to_dfs()`：当前 `GROUP_TABLES` 中的 definitions、occurrences、previous、members、member P/T/C/Clock、Required、distance、overlaps、covered-by。
- `read_exact(reference)`：按候选 exact 读取。
- `read_at_knowledge(life, as_of)`：按 Life/AsOf 选择当时唯一可见 revision；没有唯一 tip 时明确报错。
- `candidate_overlay()`：返回 occurrences 和 members，供按成员 actual 叠加；它不改变 known-time 限制。

### 当前接口缺口

Haskell `GroupOccurrenceRecord` 已存 `groupFormationParticipation`，但当前 TIS `_U2GroupCandidateFields.py` 的 `GROUP_TABLES` 未列出该嵌套字段。因此：

- A 能从源码确认它属于候选 revision 的形成决定证据；
- B/C/D 不能仅凭当前 `to_dfs()` 假定可直接取得该表；
- 若后续展示确实要求 admission/support correction/alternative 的完整细节，应把它记为读取接口缺口，而不是用其他字段猜测或另造事件。

---

## 8. 未确认项与影响

| 编号 | 未确认项 | 当前可采用结论 | 对后继影响 |
|---|---|---|---|
| UNC-01 | 外层 `Tick.ts` 与 `groupKnownFrom` 在所有平台运行中的精确等价关系，当前 F 合同未明文声明 | 业务 occurrence 位置使用显式 `groupKnownFrom`；成员使用各自 actual/confirmation/known | 不阻断 B/C/D；禁止用外层时间替代业务字段 |
| UNC-02 | `groupFormationParticipation` 的当前 Python 公开表映射缺失 | Haskell 存储语义已确认；当前正常 `to_dfs()` 不可假定能读 | 不阻断核心候选展示；若 C 要完整形成决定细节，需显式记录接口缺口 |

没有发现阻断 A 核心输入、业务主输出或位置关系的缺口。

---

## 9. 给后继 Skill 的准确输入边界

1. B/C/D 应把**候选 revision**作为 F 的主 occurrence，而不是把成员行或 Pair 行当成多条 F 主事件。
2. 展示时至少同时保留：
   - 候选 `groupKnownFrom`；
   - 各成员 actual / confirmation / known；
   - Candidate Life/Revision/Previous；
   - local basis、observation、closed、coverage incomplete；
   - member status；
   - Pair Required 的四项 verdict 和具体 gap/veto；
   - overlap/covered-by。
3. 若在成员 actual 位置画标记，必须表达“这是候选成员的实际转折位置”，不能说成候选在该点已经发生；候选最早在 `groupKnownFrom` 才可知。
4. definition-only publication 不应被画成一个共同转折候选。
5. 非首次无输出只表示候选正文没有新 revision，不代表失败或结束。
6. Q/V 不属于本 Run 当前 A 产物；不得用 Q 后续运动或 V 成立结果反向改写 F 成员选择和 F occurrence 定义。

## 10. 完成判定

按 A Skill/IO 的状态合同，本阶段为 **完整**：输入事件、业务主输出和中间结果已经区分；每类 occurrence 自身发生位置与携带位置已经说明；主输出形成、更新、关闭和修订关系可追溯到锁定代码；公开明细没有被误判为独立业务主输出。UNC-01/02 是明确的非阻塞边界，不要求 Worker，也不要求运行特征才能完成本项代码事实分析。
