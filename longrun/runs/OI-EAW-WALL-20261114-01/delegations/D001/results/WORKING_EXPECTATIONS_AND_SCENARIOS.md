# D001｜WORKING Expectations、Input Suitability 与 Scenario Set

> `run_id`：`OI-EAW-WALL-20261114-01`  
> `delegation_id`：`D001`  
> `analysis_round_id`：`AR-WALL-001`  
> `expectation_version`：`EV-WALL-WORKING-v0.2`  
> `previous_version`：`EV-WALL-WORKING-v0.1`  
> `status`：**WORKING / NOT FROZEN**  
> 更新来源：W001 current checkout + historical legacy material  
> 本文件不得作为正式 `SUPPORTS/COUNTERS` 对照基准。

## 1. 版本变化

v0.2 不改变 Owner 目标，也不把样本观察回写成已冻结业务规则。它做三件事：

1. 把“旧指定 SHA 的静态事实”升级为“当前 BASE checkout 的静态事实”，因为 W001 已核 current HEAD 与相关路径；
2. 把三条 historical legacy chain 作为探索性观察，更新每个场景的材料状态；
3. 增加 End measurement loss、diagnostic identity、current tuple／active-map 缺口等 evidence-induced candidate。

## 2. 来源层级

### 2.1 `OWNER_EXPLICIT`

Owner 原文：

> 对 `EawP1WallLifecycleFrp` 开展观察材料准备和业务合理性分析。

Owner 没有预先批准某个 transition、transaction、duplicate、publication 或参数结论。

### 2.2 `BUSINESS_INFERRED`

候选业务目的：

> 在一个 exact Wall feature run 内，持续维护 producer 已认出的同一 Wall 的可解释生命周期；下游能够区分身份、状态变化、终止、异常、缺失和当前状态。

### 2.3 `IMPLEMENTATION_DERIVED_CURRENT_SOURCE`

W001 已核：

- TIS current HEAD=`ef887396...`；
- FRP current HEAD=`cac6c912...`；
- P1 相关路径与 D001 指定基线无差异。

因此下面的源码行为可以称为 current working-tree 静态行为；但 historical product generation version 缺失，仍不能称 current runtime behavior。

### 2.4 `HISTORICAL_EXPLORATORY_EVIDENCE`

真实物化链来自 legacy `P1Wall*Storage`，对象／日历为 `rb / night_end_at_2300`。它可帮助理解数据形状和正常链，不构成冻结后的正式证据比较。

## 3. Expectation Register

### `EV-WALL-001`｜任务与判断边界

- **origin**：`OWNER_EXPLICIT`
- **statement**：本 Run 应准备可追溯材料并形成业务合理性基线；不得把源码、旧数据或计划单独当最终合理性结论。
- **applicable**：本 D 全部三个 Q。
- **falsifier**：无 current/legacy 区分却宣布 PASS；擅改实现或启动大运行。
- **evidence needed**：版本、数据绑定、材料审查、限制。
- **status**：WORKING，高置信。

### `EV-WALL-IDENTITY-001`｜身份作用域

- **origin**：`BUSINESS_INFERRED`
- **statement**：Wall identity 至少需要 exact artifact/run namespace + local no；裸 local no、裸 ref 不得跨 artifact 连接。
- **applicable**：同一 producer source run。
- **non-applicable**：跨 run matching；当前不做。
- **falsifier**：正式产品存在经批准、可核的跨 run stable identity。
- **W001 observation**：legacy chain 只能恢复 exact upstream artifact + localNo=1；current canonical `FeatureRunIdentity` 缺失。
- **status**：WORKING；探索性材料与该预期一致，但不是正式支持。

### `EV-WALL-IDENTITY-002`｜生命周期不重新认墙

- **origin**：`BUSINESS_INFERRED`
- **statement**：Start 后的 BandUpdate、PresenceChange、End 沿用同一 identity；FRP 不按价格接近重新认墙。
- **falsifier**：FRP 自行重分配 identity；producer 同号实际代表不同对象。
- **W001 observation**：三条 chain 的 upstream wall_id、legacy localNo、ref、UTI 连续为同一 Wall。
- **status**：WORKING；只覆盖 Start→BandUpdate→End。

### `EV-WALL-START-001`｜合法起点

- **origin**：`BUSINESS_INFERRED`
- **statement**：新 Wall 应由可用的 Start Present 建立；Start Dormant 需要显式业务例外，不能静默建立。
- **falsifier**：producer 合同存在“首次出现即 Dormant”的合法语义。
- **W001 observation**：真实链 Start 为 `alive/present`。
- **status**：WORKING；Start Dormant 仍 MISSING。

### `EV-WALL-BAND-001`｜BandUpdate 保持 presence

- **origin**：`BUSINESS_INFERRED`
- **statement**：BandUpdate 更新 band/core，不承担 Present↔Dormant；presence 变化应有具名事件。
- **falsifier**：producer 合同明确允许 BandUpdate 同时改变 presence。
- **W001 observation**：真实 BandUpdate 保持 `alive/present`，low/high/core 非平凡变化。
- **status**：WORKING；探索性正常例一致，非法变更场景缺失。

### `EV-WALL-PRESENCE-001`｜Presence 转移

- **origin**：`BUSINESS_INFERRED`
- **statement**：合法转移候选为 `Present→Dormant`、`Dormant→Present`；同态重申需显式合同。
- **evidence needed**：pre/post state、input change、diagnostic。
- **W001 observation**：无 Dormant／恢复。
- **status**：WORKING / MISSING。

### `EV-WALL-END-001`｜终止和终止证据

- **origin**：`BUSINESS_INFERRED`
- **statement**：End 后 identity 不在 active map；历史 occurrence 和终止 update 可追溯；同 run 同号不能无规则复活。
- **falsifier**：业务明确允许同 local identity 重用并有无歧义合同。
- **W001 observation**：真实 legacy End occurrence + Ended current update 存在；FRP active map 缺失；current source仍未见独立 ended-id ledger。
- **status**：WORKING；终止输出有探索性材料，active deletion／End 后事件仍未决。

### `EV-WALL-END-002`｜End measurement 可解释性

- **origin**：`EVIDENCE_INDUCED_CANDIDATE`
- **statement**：若 End occurrence 不保留最后 band/core，产品必须明确 `not_present` 并允许通过 exact identity/ref 回到 producer evidence；不得把占位 0 当真实 band/price。
- **source**：W001 chain End 上游 band/core=4269，legacy occurrence=0 + `not_present`。
- **alternative**：当前 canonical schema 可能已采用不同 ADT。
- **status**：WORKING candidate；需 current schema 与下游消费合同。

### `EV-WALL-PUBLICATION-001`｜O/C/A/D 可对账

- **origin**：`BUSINESS_INFERRED`
- **statement**：occurrence、current update、diagnostic 与 active map 必须按 run、firing、identity、time 形成无歧义解释；current update 不得被读成完整快照。
- **falsifier**：reader 无法取得必要 identity/order，导致 End、缺行或多更新不可解释。
- **W001 observation**：三 firing O/C 对齐；短窗 O=15,809 records、C=15,208 records、相同 14,858 firing；A 缺失；D 无 Wall identity。
- **status**：WORKING；O/C 局部可解释，A 与 identity-specific D 缺失。

### `EV-WALL-DIAGNOSTIC-001`｜异常可关联性

- **origin**：`EVIDENCE_INDUCED_CANDIDATE`
- **statement**：diagnostic 应至少能通过 batch/firing/ref/identity 中一种稳定方式关联到被拒绝输入和未提交状态；仅有文本错误而无法定位 Wall 会限制异常合理性分析。
- **W001 observation**：legacy D 有 source/kind/field/message，但无直接 Wall identity；前三条为 ingress InvalidNumericDomain。
- **status**：WORKING candidate；current `WallDiagnostic` 需另核。

### `EV-WALL-TXN-001`｜异常不得静默污染，原子边界待证

- **origin**：`BUSINESS_INFERRED`
- **statement**：非法 occurrence 不得静默污染 current state；“同 firing 一错全退”是否合适取决于 firing 是否不可分 transaction。
- **current source**：ingress 与 lifecycle 各有整批拒绝。
- **W001 observation**：没有合法+非法同 firing 样本，也没有 pre/post active map。
- **status**：前半高置信；原子策略 PENDING。

### `EV-WALL-DUP-001`｜重复与冲突

- **origin**：`BUSINESS_INFERRED`
- **statement**：exact duplicate 不制造第二次业务变化；same-ref different-payload 显式冲突；作用域必须与 run/firing identity contract 一致。
- **current source**：ledger 每 firing 新建，直接覆盖同 firing；未证明 run-wide。
- **W001 observation**：无 duplicate/conflict 场景。
- **status**：WORKING / MISSING。

### `EV-WALL-TIME-001`｜发生顺序与迟到

- **origin**：`BUSINESS_INFERRED`
- **statement**：transition 应基于明确业务顺序；writer trigger、producer UTI/ts、actual/confirm/known 若不同应分开；晚到不能偶然兼容而无痕接受。
- **W001 observation**：样本保留 writer epoch 和 UTI；二者可对齐，但独立 actual/confirm/known 缺失；交易所时区解释未核。
- **status**：WORKING / PARTIAL。

### `EV-WALL-OBS-001`｜缺失语义分离

- **origin**：`BUSINESS_INFERRED`
- **statement**：`NoOccurrence / ValidEmpty / DataUnavailable / InsufficientHistory / Pending` 必须结合 receipt、read success、范围和 history 区分。
- **W001 observation**：资产存在、部分可解码、current schema 不可得被明确分开；未构造五类业务场景。
- **status**：WORKING；材料轨道支持分层，不是运行场景证明。

## 4. Current-source implementation findings

以下是 current checkout 静态事实，origin=`IMPLEMENTATION_DERIVED_CURRENT_SOURCE`：

| ID | 静态行为 | 证据状态 | 业务影响状态 |
|---|---|---|---|
| `IMPL-01` | Start 只允许 `Nothing + Alive`；BandUpdate 保持 presence；Presence 只允许 Present↔Dormant；End 得到 Ended | current source verified | runtime 未证 |
| `IMPL-02` | 任一 ingress decode error 拒绝同 firing typed batch | current source verified | firing 原子性未证 |
| `IMPL-03` | 任一 lifecycle state error 使同 firing transaction 不提交 | current source verified | firing 原子性未证 |
| `IMPL-04` | current update 对每 identity 保留本 firing 最后 update，full active map另存 | current source verified | 无多更新真实样本／A |
| `IMPL-05` | End 发布 Ended update并删除 active map | current source verified | legacy End update有；A删除缺失 |
| `IMPL-06` | occurrence ledger 每 firing 重置 | current source verified | cross-firing replay 未证 |
| `IMPL-07` | End 后未见独立 ended ledger；normal Ended state不留在 active lookup | current source verified | End 后同号场景未证，高价值风险候选 |
| `IMPL-08` | transition 按 input order；未见 UTI 单调 guard | current source verified | late/out-of-order 未证 |

## 5. Input Suitability Assessment

### 5.1 输入有效性

| 层 | 判断 |
|---|---|
| current source | `VALID_FOR_STATIC_READING`：HEAD、相关文件 hash、diff 已核 |
| upstream legacy receipt/sparse/trace | `VALID_WITH_SCOPE`：artifact、schema、code version、target/calendar 可核 |
| legacy three-writer product | `PHYSICALLY_VALID_WITH_VERSION_GAP`：header、anchor、字段和局部数据可核；product generation version 缺失 |
| current canonical product | `UNAVAILABLE` |
| native reader | `UNVERIFIED`；matching wrapper 缺失 |

### 5.2 输入业务合理性

legacy chain 能表达：

- exact artifact 内同一 local Wall；
- Start、BandUpdate、End；
- current update；
- producer band/core 背景。

限制：

- End occurrence 本身丢失 band/core；
- diagnostic 无 identity；
- active map 缺失；
- actual/confirm/known 缺失。

判断：`LOCALLY_REASONABLE_FOR_NORMAL_CHAIN_EXPLORATION`。

### 5.3 对当前目的的适用性

| 目的 | 适用性 |
|---|---|
| 理解 legacy 正常链和 O/C 物理关系 | SUITABLE |
| 验证 current canonical runtime | NOT SUITABLE |
| 验证 active-map 与 transaction | NOT SUITABLE |
| 冻结完整业务预期 | NOT SUITABLE |
| 形成后续高价值场景清单 | SUITABLE |

## 6. Scenario Expectation Set v0.2

记号：O=`wall_occurrences`；C=`wall_current_view` update；A=full active map；D=`wall_diagnostics`。

| ID | 场景 | WORKING 预期 | current-source行为 | W001 material | 当前状态 |
|---|---|---|---|---|---|
| S01 | 无→Start Present | O Start；C Present；A add；D none | 符合 | 真链 row0，有 O/C/producer trace，无 A | `EXPLORATORY_CONSISTENT / A_MISSING` |
| S02 | 无→Start Dormant | 默认拒绝或显式例外 | `WallMustStartPresent` | 无 | `MISSING` |
| S03 | Present→BandUpdate Alive | identity/presence不变，更新 band/core | 符合 | 真链 row1，O/C/producer trace | `EXPLORATORY_CONSISTENT` |
| S04 | Present→Dormant | O/C/A 转 Dormant | 符合 | 无 | `MISSING` |
| S05 | Dormant→BandUpdate Dormant | 保持 Dormant，更新 band/core | 符合 | 无 | `MISSING` |
| S06 | Dormant→Present | O/C/A 恢复 Present | 符合 | 无 | `MISSING` |
| S07 | Present→End | O End；C Ended；A delete | 源码符合 | 真链 row2 O/C；A 缺；End band/core发生转换损失 | `PARTIAL / A_MISSING` |
| S08 | Dormant→End | 同 S07 | 源码符合 | 无 | `MISSING` |
| S09 | 同 firing exact duplicate | 一次变化，不重复发布 | ledger suppress | 无 | `MISSING` |
| S10 | 跨 firing exact duplicate | 需明确 run-wide/upstream policy | ledger不跨 firing | 无 | `PENDING_HIGH_VALUE` |
| S11 | 同 firing same-ref不同 payload | conflict，transaction不静默部分提交 | 源码 conflict+rollback | 无 | `MISSING` |
| S12 | 跨 firing same-ref不同 payload | 需上游或持久规则 | 源码不保证 ref conflict | 无 | `PENDING_HIGH_VALUE` |
| S13 | update/end before start | diagnostic，无伪 state | before-start errors | 无 | `MISSING` |
| S14 | active Wall 再 Start | diagnostic，无重认 | StartedTwice | 无 | `MISSING` |
| S15 | End 后 update/end/Start | terminal policy明确，不无痕复活 | update/end可能归 before-start；Start可能重建 | 无 | `PENDING_HIGHEST_PRIORITY` |
| S16 | BandUpdate 改 presence | diagnostic，不提交 | ChangedPresence | 无 | `MISSING` |
| S17 | 同态 PresenceChange | 默认 diagnostic或明确例外 | InvalidPresenceTransition | 无 | `MISSING` |
| S18 | 合法+state-invalid 同 firing | 非法不污染；是否整批回滚需业务原子性 | 整批 rollback | 无 | `PENDING_ATOMICITY` |
| S19 | 同 identity 多条合法变化同 firing | O保留顺序；C最后一条；A最终态 | 源码如此 | 三样本是不同 firing | `NOT_OBSERVED` |
| S20 | 合法+decode-invalid 同 firing | D ingress；整批策略需业务解释 | ingress整批拒绝 | 仅单独 InvalidNumericDomain D | `PENDING_ATOMICITY` |
| S21 | payload UTI乱序／迟到 | 明确 sort/late policy | 未见单调 guard | 样本顺序正常，不能区分 | `MISSING` |
| S22 | 无输出／空／不可读／历史不足／Pending | 五类分开 | 不由单一 ADT全表达 | W001只证明材料层可分 | `PARTIAL_MATERIAL_ONLY` |

## 7. Exploratory findings

这些不是正式 `SUPPORTS/COUNTERS`：

1. exact artifact + localNo 能把三条正常 legacy occurrence 串成一条链；
2. nontrivial BandUpdate 能在上游、O、C 三层对账；
3. Ended current update 真实存在；
4. active deletion 没有可见材料；
5. End occurrence 对 band/core 的表示有明显信息损失；
6. diagnostics channel 真实非空，但 legacy shape 不足以做 identity-specific error analysis；
7. current source与legacy product不能形成同版 tuple。

## 8. Evidence-induced candidates

### EIC-01｜Terminal identity policy

若 producer 不保证同 run local no 永不复用／End 后无事件，则 DSU 需要 terminal ledger 或等价机制；否则 current source 的 End 后语义可能不准确。先查 producer invariant 与受控场景。

### EIC-02｜End measurement contract

正式输出应明确：End 的 band/core 是“不适用并通过 ref 回源”，还是“保留最后 measurement”。不得用数值 0 同时承担缺失与真实价格。

### EIC-03｜Diagnostic correlation

异常材料至少要能定位 firing/batch/ref/identity 和 rejected payload；否则难以验证 transaction 与 state safety。

### EIC-04｜Cross-firing replay scope

同 firing ledger 不等于 run-wide idempotence。需要上游唯一性合同、持久 dedup 或明确“不支持 replay”的边界。

## 9. Freeze assessment

```text
Expectation version: EV-WALL-WORKING-v0.2
Full-set freeze:     NOT READY
Formal comparison:   NOT STARTED
Exploratory review:  COMPLETED WITH LIMITS
```

冻结前最低仍需：

- current product generation tuple；
- matching reader/schema；
- A 或等价 state replay；
- Dormant/恢复或明确不可达合同；
- duplicate/conflict/co-fired/End-after/late 场景；
- actual/confirm/known time contract。

manager 可据此决定是否冻结一个更窄的正常链子集；E1 本轮不擅自冻结。
