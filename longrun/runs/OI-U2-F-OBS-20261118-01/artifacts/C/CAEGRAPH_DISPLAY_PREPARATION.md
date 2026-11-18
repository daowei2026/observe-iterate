# C｜CommonPriceTurnGroupCandidatesFrp CAEGraph 展示方式准备

## 0. 产物身份与阶段结论

| 项目 | 值 |
|---|---|
| `run_id` | `OI-U2-F-OBS-20261118-01` |
| `work_item_id` | `OI-U2-F-OBS-20261118-01-WI-C` |
| `stage_instance_id` | `OI-U2-F-OBS-20261118-01-M-C` |
| `delegation_id` | `D003` |
| 执行调用 | `C0008` |
| 特征 | `CommonPriceTurnGroupCandidatesFrp`（F｜共同价格转折候选组） |
| C Skill 版本 | `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288` |
| CAEGraph 版本 | `daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad`（原 `e6.2` 标签的精确展开） |
| A 当前产物 | `daowei2026/observe-iterate@823b56a018c0f49e1632885db484ff2e1e64d6b8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.md` |
| B 当前产物 | `daowei2026/observe-iterate@6f1ee9eb4595254845d3b228a146ad68cabc64e0:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/B/OBSERVATION_POSITION_PREPARATION.md` |
| C 阶段状态 | **完整** |

本阶段只完成 C：列出待展示信息，形成并迭代展示预期与唯一当前预期 HTML，再把当前展示语义整理为位置、实例和字段可注入的 CAEGraph Python 代码。

本阶段没有把 B 的最终真实位置绑定进图，没有运行 D 的完整定义，也没有运行 E 的真实实例。两份预期 HTML 使用确定性的**合成样例数据**；`rb / hc / i` 只用于贴近外层实例的对象形状，并不构成 B 的正式位置绑定或真实历史结论。

### 当前被接受的展示主线

```text
每品种 5m 原价与输入转折证据
→ 候选成员 actual / confirmation / member-known 的位置链
→ 候选 revision 在 groupKnownFrom 的正式 occurrence
→ Required 四坐标的 pair 审计
```

候选 revision 是 F 的业务主 occurrence。成员行、Required 行、previous、overlap 和 covered-by 只是候选 revision 的正文或形成证据，不在图中冒充独立的 F 主 occurrence。

---

# 1. C1｜待展示信息清单

## 1.1 判断规则

- 业务主输出默认展示；
- 输入事件只有在能帮助理解候选形成时才展示；
- 中间处理结果只在能解释候选形成、修订、关闭或反证时进入；
- 不按公开 DataFrame 数量机械生成面板；
- 不从字段名自行发明 A 未确认的业务关系；
- `groupKnownFrom` 是候选 revision 自己的正式业务可知／发表位置；成员 `actual / confirmation / known` 是正文携带的位置，不能相互替代。

## 1.2 信息清单

| 编号 | A 来源 | 业务角色 | 纳入方式 | A 已确认的位置／身份 | 原值字段与展示关系 | 决定 |
|---|---|---|---|---|---|---|
| C1-01 | IN-01｜5m KLine close | 输入 | 常显 | 每品种 `closeUti`；对象身份 | KLine OHLC／close 原值；作为价格语境 | 每品种原价主图 |
| C1-02 | IN-02｜第一轮 CompleteScaleTurn | 输入 | 条件展示 | Turn Life/Revision；actual、confirm；FirstRound | 原始 ScaleTurn 视图由 D 注入时可叠加；候选成员正文始终保留 | 可选灰色输入点；成员点常显 |
| C1-03 | IN-03｜第二轮 CompleteScaleTurn | 输入 | 条件展示 | Turn Life/Revision；actual、confirm；SecondRound | 与第一轮分开；不同 marker | 可选灰色输入点；成员点常显 |
| C1-04 | IN-04｜`falter` Zig 状态 | 辅助输入 | 不单独成图 | Zig actual key；方向／Peak-Trough 类型 | 当前 F 只用它给 Turn 补 direction/type | 方向和类型进入成员 hover；不新增 Zig 面板 |
| C1-05 | MID-01｜FormationFrame | 中间 working event | 不单独成图 | frameKnown、frameProgress、对象 | 当前正常路径 `framePatches=[]`、`frameEnded=False` | 只通过下游成员及覆盖信息追溯 |
| C1-06 | MID-02｜FormationMaterial | 中间 working event | 不单独成图 | materialKnown、progress | 有限材料与覆盖状态 | 只通过候选成员、coverage 和 Required 追溯 |
| C1-07 | MID-03｜PairView | 中间形成证据 | 展示其已存正式证据 | PairKey；Time/Direction/TurnType/Bend | `occurrences_groupRequired` 和 pair distance | Required 审计附图 |
| C1-08 | MID-04｜CandidateOccurrence | 主输出逻辑 occurrence | 常显 | Candidate Life/Revision/Previous；candidateKnown | CandidateOccurrence 存储为 GroupOccurrenceRecord | 候选 revision 附图 |
| C1-09 | OUT-01A｜GroupOccurrenceRecord | **业务主输出** | 常显 | `groupKnownFrom`；Life/Revision；previous | basis、observation、alternative、coverage、closed、成员 | 候选 revision 点与 hover |
| C1-10 | OUT-01B｜definition record | 配置元数据 | 页首说明／hover，不画候选点 | definition identity | method/context/scale/calendar/universe/domain/objects/Δ/unit | definition-only publication 不画成候选 occurrence |
| C1-11 | `groupMembers` | 主输出正文 | 常显／hover | member Turn/Source exact；object | actual、price、confirmation、known、round、direction、type、status | 每品种价格主图成员证据 |
| C1-12 | `groupPrevious` | revision 引用 | 常显 | 同 Life 前一 exact | previous → current | 候选附图虚线连接 |
| C1-13 | `groupRequired` | 形成／反证证据 | 常显摘要，hover 明细 | pair Left/Right Turn exact | 四坐标 verdict/gap/veto、distance | 每候选每坐标最坏结果与计数；pair 明细 hover |
| C1-14 | `groupOverlaps` | 候选间引用 | hover | 目标 candidate Life | 当前公开表没有唯一目标 revision/time | 不画跨时线，避免伪造唯一目标 occurrence |
| C1-15 | `groupCoveredBy` | 候选间引用 | hover | 目标 candidate Life | 同上 | 不画跨时线，避免伪造唯一目标 occurrence |
| C1-16 | `groupFormationParticipation` | 正式决定证据 | 应展示但当前不可读 | Haskell 已存 | 锁定 TIS `GROUP_TABLES` 未公开 | 记录真实数据接口缺口，不猜测、不补造 |

## 1.3 未把中间结果机械扩成面板的理由

`FormationFrame`、`FormationMaterial` 和当前 CandidateState 是处理过程 working-state。它们对本轮最重要的可审计信息已经以候选成员、coverage、Required pair 和 revision 链进入正式输出。再各画一张“状态面板”会重复同一信息，并容易把 working-state 误认成业务主 occurrence。

---

# 2. C2A｜CAEGraph 阅读与能力核实记录

## 2.1 实际阅读范围

直接阅读锁定提交的：

- `CAEGraph使用手册.md`
  - 文档说明、名词定义；
  - `CAEGraph / PlotSet`；
  - 布局类快速选择指南；
  - `AllSymsMainFig / AllSymsFig / PerSymFigs / PerSymFigSet / MainFig / SubFig / OneFig`；
  - 绘图类快速选择指南；
  - `KPriceLine / TickPriceLine / VBarPlot / MulFieldsGlyphs / MulSegPlot / SegsPlot / TextPlot / MulPointPlot / OneToGroupPointPlot / SeqOfFieldsPlot`；
  - `ExtractTimespans / PerDPTimespans`；
  - `FigCtrls`；
  - 多品种大单和 Dense/Fight 示例。
- 锁定源码：
  - `uplot/utkv2.py`：布局、共享 `x_range`、legend hide、hover 与逐品种上下文；
  - `uplot/utlv2.py`：`CAEGraph`、`PlotSet`、`KPriceLine`、`MulFieldsGlyphs`、动态 glyph、segment、Text、变长字段等；
  - `uplot/pfw.py`：`PlotCtx.feat_data`、UTI→X／时间标签、hover、动态标准化、DataFrame 直接输入支持；
  - `uplot/__init__.py`：当前公开导出。

## 2.2 已确认能力

| 能力 | 采用依据 | 本次用法 |
|---|---|---|
| 顶层组合 | `CAEGraph → PlotSet → BaseFigSet → BasePlotter` | 单个 PlotSet 共享位置和时间轴 |
| 每品种独立原价图 | `PerSymFigs` | 避免 `rb/hc/i` 绝对价格量纲混在一条 Y 轴 |
| 全局附图 | `AllSymsFig` | 候选 revision 与 Required 审计只绘制一次 |
| 价格线 | `KPriceLine` | D 注入真实 5m KLine Feature |
| 离散点／动态 marker | Bokeh scatter；锁定源码已有 `MulFieldsGlyphs`、`DynamicGlyphPlot` | C3 使用小型 `BasePlotter` 子类支持逐行 marker/color |
| 位置链／revision 链 | Bokeh segment；锁定 `SegsPlot / MulSegPlot` 同类能力 | actual→confirmation、confirmation→known、previous→revision |
| 共享 X 轴 | `BaseFigSet._create_fig` 复用 `ctx.x_range` | 从价格输入横向核对候选与 Required |
| hover | `PlotCtx.add_hover` 和 Bokeh `HoverTool` | 保存 exact identity、原值和不宜常显的细节 |
| legend 显隐 | `click_policy="hide"` | 图层显隐，不需要复杂弹窗 |
| DataFrame 适配 | `PlotCtx.feat_data` 接受 DataFrame | C3 将正式读取表转换为只读 FrameFeature |
| 自定义布局／绘图器 | `BaseFigSet / BasePlotter` 公开基类 | 只补当前业务表达，不修改 uplot |

## 2.3 未采用或不作为核心依赖的能力

- `MulPointPlot / OneToGroupPointPlot / SeqOfFieldsPlot` 的手册没有当前可运行示例；本轮不把它们作为核心交付依赖。
- `ExtractTimespans / PerDPTimespans` 适合按特征自动找位置，但 B 已经负责位置，C 不重新选择位置。
- `FigCtrls` 主要服务参数交互，本轮核心是事件审计，不用控件替代主附图阅读。

---

# 3. 外层特征实例使用记录

| 字段 | 记录 |
|---|---|
| 是否读取外层实例 | 是，只读 |
| 实例来源 | `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py`、F Python 包装、完整配置 |
| 使用目的 | 核实构造、对象、5m KLine、公开读取接口和字段层次；确定 C3 注入形状 |
| 读取接口 | `to_df / to_dfs / read_exact / read_at_knowledge / candidate_overlay` 及 `GROUP_TABLES` |
| 是否运行真实实例 | 否 |
| C2 预览绑定 | 仅用 `rb / hc / i` 名称和合成时间／价格／occurrence，未读取真实历史结果 |
| 是否进入 C3 固化 | 否；仅通过 `DisplayBindings` 注入 |
| D 需替换 | candidate Feature、price Feature、SOF、日历、symbols、timespans、可选 raw turn view |

---

# 4. C2B｜第一版展示预期与第一版 HTML

## 4.1 第一版编号

```text
C2-V1
```

## 4.2 第一版结构

1. 所有品种比例标准化后放在同一价格概览；
2. 另一个附图只在 `groupKnownFrom` 放候选 revision 点；
3. hover 展示候选状态。

第一版 HTML：

`daowei2026/observe-iterate@4e69f0cc0e5373dc0cb6daa41ce6ac3e0cf63e40:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview_v1.html`

## 4.3 第一版结论

第一版**不接受**。它证明共享时间轴和候选 occurrence 面板可行，但丢失了 A 的关键业务语义，不能进入 C3。

---

# 5. C2C／C2D｜复杂展示点循环记录

| 编号 | 要保留的信息 | V1 具体问题 | 核实与判断 | 当前决定 | 状态 |
|---|---|---|---|---|---|
| CX-01 | 三品种真实价格语境 | 共同 Y 轴必须标准化；标准化值可能被误认成业务原值，成员 price 也难以直接贴回 | `PerSymFigs` 可给每品种独立图，仍共享 X 轴 | 改为每品种原价主图；不把 display ratio 当业务值 | 已解决 |
| CX-02 | 同一成员的 actual、confirmation、known | V1 只画候选 known，成员的三种位置不可见 | segment + point + hover 可表达多位置 | actual 为成员点；actual→confirmation、confirmation→known 分段；所有时间进入 hover | 已解决 |
| CX-03 | 候选自身位置不能与成员 actual 混同 | V1 容易让读者把价格上的成员点当候选 occurrence | 全局附图可独立以 `groupKnownFrom` 定位 | 候选只在 revision 附图以 `groupKnownFrom` 发生 | 已解决 |
| CX-04 | Candidate Life/Revision/Previous | V1 点之间没有 revision 链 | segment 支持 previous→current | 同 Life 前驱用虚线连接；hover 保留 exact | 已解决 |
| CX-05 | 一条候选包含多个成员与 pair | V1 无法追溯成员及 Pair Required | 每品种面板 + 全局 Required 附图 + hover 可组合 | 成员按对象落在各自价格图；Required 每候选每坐标聚合，pair 明细 hover | 已解决 |
| CX-06 | Required 的 verdict/gap/veto | 全部 pair 直接常显会拥挤；完全不画又失去反证来源 | CAEGraph 支持点、hover、共享时间轴；摘要可在 C3 预处理 | 显示派生 `worst + supports/unresolved/veto counts`；原 pair reason 在 hover | 已解决 |
| CX-07 | anchor/deadline/revisionEnd | 这些是 Calendar clock，不是 UTI，直接画到时间轴会制造假坐标 | 没有证据支持把它们转换为唯一 UTI | 只在候选 hover 展示原值 | 已解决，无语义损失 |
| CX-08 | overlap/covered-by | 当前公开表只给目标 Life，没有唯一目标 revision/time；画线会擅自选点 | 不是绘图能力问题，是目标定位语义不足 | hover 显示 Life；不画跨候选线 | 已解决，保留明确边界 |
| CX-09 | definition-only publication | 若按外层 Event 画点，会被误解为候选发生 | A 已确认它是元数据 | 页首说明，不画候选 point | 已解决 |
| CX-10 | `groupFormationParticipation` | 形成决定细节当前 Python 表不可读 | 已核 TIS 包装和 `GROUP_TABLES` | 不猜测；明确接口缺口 | **数据接口缺口** |
| CX-11 | 外层 `Tick.ts` 与 `groupKnownFrom` | 合同未证明完全同义 | A 已给边界 | 所有候选横坐标使用显式 `groupKnownFrom` | 已解决 |

## 5.1 当前版本编号

```text
C2-CURRENT-V2
```

## 5.2 当前唯一预期 HTML

`daowei2026/observe-iterate@56eef30b28c928255329f77798fb46b9adbbc71a:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview.html`

生成原型：

`daowei2026/observe-iterate@b753885342ed3a95258137efb6c62f4d6e181076:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/generate_caegraph_preview.py`

---

# 6. C2 当前展示预期

## 6.1 页面与阅读路径

```text
页首：实例与数据接口告警
  ↓
P1～P3：rb / hc / i 每品种 5m 原价与成员形成证据
  ↓
P4：Candidate revision occurrence 时间线
  ↓
P5：Required 四坐标审计
```

所有图共享水平时间位置。观察者可以在某个成员 actual 处看价格语境，再向右读到 confirmation、member-known 和候选 `groupKnownFrom`，最后在同一候选时点核查 Required pair 的支持／未决／否决。

## 6.2 面板定义

| 面板 | 布局 | 横轴 | 纵轴 | 承担信息 |
|---|---|---|---|---|
| P0 | 自定义说明区 | — | — | 实例标签、合成／真实状态、数据告警、缺口 |
| P1～P3 | `PerSymFigs` | 共享 UTI 时间轴 | 各品种原价 | 5m KLine、可选 raw ScaleTurn、候选成员 actual、actual→confirmation、confirmation→member-known |
| P4 | `AllSymsFig` | `groupKnownFrom` | `groupObservation` 类别 | Candidate Life/Revision、basis、observation、previous 链、members、coverage、closed、窗口原值、overlap/covered-by |
| P5 | `AllSymsFig` | `groupKnownFrom` | Time / Direction / TurnType / Bend | 每候选每坐标的最坏 verdict、计数和 pair 明细 |

## 6.3 图元定义

| 图元 | 来源 | X | Y | 视觉语义 | hover |
|---|---|---|---|---|---|
| G-PRICE | 5m KLine | KLine UTI | 原始价格 | 各品种自己的价格线 | OHLC／价格字段由 `KPriceLine` |
| G-RAW-TURN | D 可选 `raw_turn_view` | Turn actual | Turn price | 灰色、低透明度输入证据 | turn exact、round、direction、type、confirmation、known |
| G-MEMBER-ACTUAL | `groupMembers` | memberActual | memberPrice | color=basis；marker=round | candidate exact、Turn/Source exact、全部成员字段 |
| G-A2C | 同上 | actual→confirmation | memberPrice | 点线 | candidate exact、turn exact |
| G-C2K | 同上 | confirmation→memberKnown | memberPrice | 虚线 | candidate exact、turn exact |
| G-REVISION | occurrences | groupKnownFrom | observation category | color=basis；marker=observation | exact、previous、members、alternative、coverage、closed、clock window、overlap/covered-by |
| G-PREVIOUS | previous + occurrence lookup | previous known→current known | previous/current observation | 灰色虚线 | Life、前后 Revision |
| G-REQUIRED | Required display summary | groupKnownFrom | coordinate category | color/marker=worst verdict | supports/unresolved/veto counts、所有 pair 的 verdict/gap/veto/distance |

## 6.4 原值与显示派生

| 值 | 类型 | 是否可反推业务原值 |
|---|---|---|
| KLine price、memberPrice | 原值 | 是，直接来自数据 |
| groupKnownFrom、memberActual、memberConfirmation、memberKnownFrom | 原值位置 | 是 |
| basis、observation、verdict/gap/veto | 原枚举的公开名称 | 是 |
| observation Y=0～5、coordinate Y=0～3 | **显示编码** | 否；只表示类别位置 |
| basis color、observation marker、verdict color | **显示编码** | 否 |
| Required `worst` 和计数 | **显示派生摘要** | 不能替代 pair 原值；hover 保留原 pair 明细 |
| V1 price ratio | **被否决的显示派生** | 不进入当前 C3 |

## 6.5 当前允许变化与必须保持

D/E 可以改变：真实曲线、点数、坐标范围、symbols、timespans、SOF、日历、正式 Feature 对象、原始 Turn 是否可注入。

D/E 必须保持：

- 候选 occurrence 只以 `groupKnownFrom` 定位；
- 成员 actual/confirmation/known 分开；
- per-symbol 原价语境；
- candidate revision、previous 和 Required 审计；
- 原值与显示派生分开；
- definition-only 不画候选点；
- 无法读取的信息不伪装为已展示。

---

# 7. C3｜位置与实例可注入的 CAEGraph 代码

## 7.1 代码与测试引用

正式 C3 代码：

`daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`

纯表夹具：

`daowei2026/observe-iterate@891f77c194ed7ac607a38429d8f1ff2bfafef6cb:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/test_caegraph_display.py`

## 7.2 代码结构

```text
CandidateTableNames
    锁定公开表名，可由 D 替换

DisplayBindings
    D 的实例／位置注入合同

prepare_display_tables(...)
    将真实 occurrence、member、previous、Required、overlap、coveredBy
    组织成 C2 当前展示所需的只读表

FrameFeature / PerSymbolFrameFeature
    把准备表接入 PlotCtx.feat_data

build_caegraph(bindings)
    具体构造 CAEGraph / PlotSet / PerSymFigs / AllSymsFig / KPriceLine
    以及小型 BasePlotter 子类
```

C3 代码没有写死：

- `TA_updto20240229_DBA`；
- `rb / hc / i`；
- `2021-01-01 / 2022-12-31`；
- 外层 `f` 实例；
- 本地结果路径；
- 真实运行状态。

## 7.3 D 的注入合同

```python
from caegraph_display import DisplayBindings, build_caegraph

bindings = DisplayBindings(
    candidate_feature=f,          # 本 Run make_features(...) 的第一项
    price_feature=kline_5m,       # 与实例一致的 5m KLine Feature
    symbols=symbols,              # D 从 B-POS-001 注入
    sof_name=sof_name,            # D 从实例/B 注入
    calendar_name=calendar_name,  # D 从实例/B 注入
    timespans=timespans,          # D 解释 B 边界后注入
    raw_turn_view=raw_turn_view,  # 可选；见 7.4
    instance_label="D-bound F instance",
)

graph = build_caegraph(bindings)
```

## 7.4 可选 raw Turn 视图字段合同

`raw_turn_view` 是只读 DataFrame，必填字段：

```text
symbol
actual
price
round
direction
turn_type
turn_exact
```

可选字段：

```text
confirmation
known
```

若 D 无法从正常上游接口形成该视图，传 `None`；图仍保留候选成员证据，并在页首写明 raw overlay 未注入。C3 不要求为绘图重跑一条被 Owner 排除的全历史 producer 链。

## 7.5 字段注入与读取

默认使用锁定 TIS 的：

```text
occurrences
occurrences_groupPrevious
occurrences_groupMembers
occurrences_groupRequired
occurrences_groupRequired_pairDistance
occurrences_groupOverlaps
occurrences_groupCoveredBy
```

如 D 的实际平台列名发生版本差异，使用 `CandidateTableNames` 或在 D 的 adapter 层明确映射；不得在 C3 内猜字段。

## 7.6 C3 与 C2 核对

| 核对项 | 结果 |
|---|---|
| C1 每项有展示位置或明确不展示理由 | 通过 |
| 每品种原价主图 | 通过 |
| 成员 actual/confirmation/known 分离 | 通过 |
| 候选以 groupKnownFrom 定位 | 通过 |
| revision previous 链 | 通过 |
| Required 摘要与 pair hover | 通过 |
| overlap/coveredBy 不伪造唯一时间线 | 通过 |
| 外层实例可替换 | 通过 |
| B 最终位置未固化 | 通过 |
| `groupFormationParticipation` 缺口保留 | 通过 |
| 未另造与当前 HTML 不同的展示语义 | 通过 |

---

# 8. 验证记录

## 8.1 已执行检查

- `generate_caegraph_preview.py`：Python 语法检查通过；
- `caegraph_display.py`：Python 语法检查通过；
- 两份 HTML：HTML 结构解析通过；
- 两份 HTML 中的 JavaScript：`node --check` 通过；
- `test_caegraph_display.py`：纯表夹具通过：

```text
prepare_display_tables fixture: OK
revisions (2, 25)
members (5, 18)
required (8, 10)
```

夹具核对了：

- 两个 revision 与一条 previous 链；
- 五个成员和三品种映射；
- overlap／covered-by；
- 八条候选×坐标 Required 摘要；
- Veto 及 pair distance 进入 hover 明细；
- `groupFormationParticipation` 告警保留。

## 8.2 未冒充完成的检查

- 当前 executor 没有在 `/dwdhome/fy/BASE_E6_2_copy` 中运行真实 `m3 / mquant / uplot` CAEGraph 环境；
- 没有绑定 B 的 2021～2022 位置；
- 没有读取或重跑真实 F 全历史产物；
- 没有生成 E 的真实图或 E5 一致性结论；
- Chromium 在当前隔离环境中未完成截图渲染，因此不声称已有浏览器截图证据。独立 HTML 文件、HTML 结构和 JavaScript 语法已检查。

这些属于 D 的正式绑定和 E 的实际运行，而不是 C 的剩余专业工作。

---

# 9. CAEGraph／数据能力缺口

| 缺口 | 受影响信息 | 已核实能力 | 为什么不是普通用法问题 | 最低替代方案 | 语义损失／建议 |
|---|---|---|---|---|---|
| GAP-01 | `groupFormationParticipation` | Haskell 存储存在；锁定 TIS `GROUP_TABLES` 无对应公开表 | 绘图器不能读取不存在的公开数据 | 页首明确告警；不展示 admission/correction/alternative 决定细节 | 丢失正式参与决定的完整审计；建议后续补 TIS 表映射 |
| GAP-02 | overlap/covered-by 的唯一目标 occurrence | 当前表公开目标 Life，没有唯一 target revision/time policy | 不是 CAEGraph 画线能力不足，而是目标点不唯一 | hover 显示目标 Life | 不丢失关系存在性，但不表达某个唯一时间连线；若要画线需业务上先给 target exact policy |
| GAP-03 | 当前 executor 的真实平台运行 | C3 已使用锁定公开类；运行依赖工作区平台包与真实 Feature | C 阶段没有 D 的实例与位置绑定，也未被授权冒充 E | D 注入后在工作区执行 | 无 C 展示语义损失；属于既定后继 |

没有发现需要先扩展 CAEGraph 才能表达 C1 核心信息的工具级阻断。当前核心表达通过既有 `CAEGraph / PlotSet / PerSymFigs / AllSymsFig / KPriceLine / BasePlotter / PlotCtx / HoverTool` 可以实现。

---

# 10. 完成条件核对

| C Skill 完成条件 | 结果 |
|---|---|
| C1 明确输入、主输出和必要中间结果 | 已完成 |
| 直接阅读锁定 CAEGraph 手册并按需查源码 | 已完成 |
| 第一版展示预期与可打开 HTML | 已完成，C2-V1 已发布 |
| 识别复杂点并循环修订预期和 HTML | 已完成，形成 C2-CURRENT-V2 |
| 当前 HTML 表达接受的展示预期或真实缺口 | 已完成 |
| C3 整理为位置与实例可注入 CAEGraph 代码 | 已完成 |
| 预览绑定有记录且未固化为最终实例 | 已完成 |
| 未把 C HTML 冒充 D 定义或 E 结果 | 已遵守 |
| 无 Worker 未决结果 | 已满足；本 C 零 Worker |

**阶段最终状态：完整。**

D003 内没有尚未满足的 C 专业工作，不需要续接同一 D。后继 D 应消费 A、B 和本 C 当前产物，完成单一正式绑定；E 再运行真实实例并与 C2 当前展示预期核对。
