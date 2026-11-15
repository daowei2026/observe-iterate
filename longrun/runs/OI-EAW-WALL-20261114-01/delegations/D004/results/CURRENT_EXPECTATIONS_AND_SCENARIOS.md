# D004｜Current Expectations and Scenarios

## 0. 版本与状态

```text
analysis_round_id   = AR-WALL-003
expectation_version = EV-WALL-CURRENT-WORKING-v0.1
status              = WORKING / NOT FROZEN
formal comparison   = NOT STARTED
```

本版本只用于指导 W008 的 current 材料探索。它不得用于正式 `SUPPORTS/COUNTERS`，不得无痕吸收后见证据。正式对照前只冻结实际材料能够覆盖的最小子集，并记录 freeze cutoff 与已看材料。

## 1. 来源分层

### 1.1 `OWNER_EXPLICIT`

`OE-WALL-01`

> 对 `EawP1WallLifecycleFrp` 准备真实观察材料，并开展业务合理性分析。

Owner没有直接给出 terminal/replay/transaction/UTI 的预期结论，也没有要求必须完成旧九场景或八EP。

### 1.2 `BUSINESS_INFERRED`

#### `BI-IDENTITY-01`｜同一运行绑定内身份连续

在同一 current run/data binding 和同一上游 Wall 身份范围内，Start、合法更新和 End 应能被解释为同一 Wall 生命周期；不同 artifact/run 的裸 local number 不应无条件合并。

可能反证：同一 current binding内 identity无故漂移、复用或无法关联；不同binding被静默并为同一Wall。

#### `BI-STATE-01`｜状态变化可解释

正常 Start→update→End 的状态应可解释；异常、terminal、duplicate、late等至少应有明确、可追溯的处理结果，而不是把缺失、有效空、拒绝和未确认混为一类。

可能反证：输入被部分提交、state与publication无可解释关系、terminal identity无业务边界。

#### `BI-PUBLICATION-01`｜O/C/D/A角色分明

Occurrence、current-update、diagnostic和active state应各自保持清楚角色；C不应被误读为全量A，D应尽可能关联到触发firing/identity，End后A变化应能被等价state证据说明。

可能反证：消费者无法区分update与snapshot；D无法回到触发对象；O/C与state互相矛盾。

#### `BI-MEASUREMENT-01`｜End测量损失显式

若 End publication对最后band/core做语义转换或丢失，current material和consumer contract应显式说明，不能把占位0当真实价格。

可能反证：显示/reader把占位值误作业务测量，无法回源。

#### `BI-USABILITY-01`｜材料可供业务使用

current material/read path至少保留判断identity、state、publication、time和转换损失所需信息；controlled evidence的结论范围应与natural data明确区分。

可能反证：只有源码预测或截图，无真实可追溯数据；reader不能运行或丢失关键身份/时间。

### 1.3 `IMPLEMENTATION_DERIVED`

以下来自 current source/static findings，只是待current证据核的实现候选，不自动等于业务应该如此。

#### `ID-START-01`

Start应建立Present state并发布对应O/C；A add需真实state证据。

#### `ID-BAND-01`

合法BandUpdate在保持identity的同时更新state并发布O/C；同firing多更新的C可能只反映last update，需实证。

#### `ID-END-01`

End应发布End occurrence和Ended current update，并从active map删除identity；End测量形状需current material核验。

#### `ID-LEDGER-01`

occurrence ledger为firing-local，因此same-firing exact duplicate与cross-firing duplicate可能不同；已有旧test与current static prediction存在冲突候选。

#### `ID-TERMINAL-01`

End后未见独立terminal ledger，静态预测End→update/End可能表现为before-start，而End→Start同local no可能重新建立；只作current controlled场景候选。

#### `ID-TRANSACTION-01`

一个firing含legal+invalid input时，decode层或state层可能整批拒绝；需要pre/post state和publication实证。

#### `ID-UTI-01`

transition按到达顺序处理，未见独立UTI monotonic guard；out-of-order行为待current证据。

## 2. 场景集合与优先级

| ID | 场景 | 当前优先级 | 需要的最低证据 | C0017状态 |
|---|---|---:|---|---|
| `CS01` | current Start→BandUpdate→End normal chain | 必需 | exact binding、upstream、O/C、D、A/等价state、reader | `PENDING` |
| `CS02` | End measurement conversion | 必需 | upstream最后值、current O/C、reader/display值 | `PENDING` |
| `CS03` | current O/C/D/A同firing关系 | 必需到可回答深度 | firing/order/identity/pre-post | `PENDING` |
| `CS04` | current reader/consumer path | 必需 | exact command/schema/output/转换损失 | `PENDING` |
| `CS05` | cross-firing exact duplicate Start | 条件高优先 | existing targeted test、exact constructor/publication/state | `PENDING` |
| `CS06` | after-End update/End/Start | 条件高优先 | existing targeted test、exact error/state | `PENDING` |
| `CS07` | same-firing exact duplicate | 条件 | order、O/C/D、ledger evidence | `PENDING` |
| `CS08` | same-ref different-payload conflict | 条件 | exact input/error/transaction | `PENDING` |
| `CS09` | one legal + one state-invalid same firing | 条件 | pre/post state、O/C/D | `PENDING` |
| `CS10` | one legal + one decode-invalid same firing | 条件 | decode rejection、pre/post | `PENDING` |
| `CS11` | out-of-order UTI | 条件 | input order/payload UTI/state/publication | `PENDING` |
| `CS12` | natural current sample | 可选建议 | current data binding、raw/current material | `PENDING` |
| `CS13` | missingness distinctions | 必需于材料层 | no occurrence/valid empty/data unavailable/history/pending | `PENDING` |

本轮不把 Dormant/restore 作为强制场景；producer natural reachability尚未建立。

## 3. 证据类别与计数规则

```text
static source
controlled existing test
synthetic engineering test
natural current data
business observation
```

规则：

- 同一trace的O/C/A/D是同源证据，不按四票计算；
- legacy `EV-WALL-LEGACY-NORMAL-v1.0`四项SUPPORTS继续保留，但不替current；
- source prediction只能形成`IMPLEMENTATION_DERIVED`候选或静态风险；
- controlled test可判断特定typed behavior，不证明自然频率或production runtime；
- 没有current material时保持`MISSING/PENDING`，不能用legacy填空。

## 4. 正式冻结资格

最小子集只有同时满足以下条件才可 `FROZEN_FOR_COMPARISON`：

1. expectation statement及来源明确；
2. object/calendar/time/data/code/parameter binding可追溯；
3. 实际材料覆盖对应场景；
4. 已看证据和freeze cutoff记录；
5. support/counter/falsifier可区分；
6. current与legacy不混版本。

W008 返回后，E1只冻结已真正覆盖的子集。未覆盖场景继续WORKING或MISSING，不为完成流程强制冻结。

## 5. 六类结果状态

正式或探索对照统一使用：

```text
SUPPORTS
COUNTERS
MISSING
AMBIGUOUS
NOT_APPLICABLE
PENDING
```

在当前 C0017 时点，current runtime场景均未取得真实材料，故不产生正式 `SUPPORTS/COUNTERS`。

## 6. 进入诊断的条件

只有满足以下全部时才考虑R3：

- 属于正式 frozen subset；
- `COUNTERS`具有明显业务影响；
- 可重复或至少有稳定复现入口；
- 存在能区分竞争解释的最小路径；
- 诊断不要求擅自改变Owner目标或生产实现。

静态风险、缺证或单次工具失败不自动进入诊断。

## 7. 当前可交给 W008 的问题

1. current exact binding和真实可执行入口是什么；
2. 是否存在低成本 normal chain material；
3. O/C/D和A/等价state能取得到什么深度；
4. reader/consumer是否真实可用，损失在哪里；
5. existing test能否低成本覆盖 cross-firing duplicate或after-End中的一项；
6. current material能否支持冻结CS01～CS04中的最小子集；
7. 不能取得的项是不存在、不可执行、成本过高、数据缺失还是仅本轮未尝试。
