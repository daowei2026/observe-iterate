# EAW CAEGraph 观察准备 Skill 候选：专业方法、原图落地与复用边界（讨论稿）

> 日期：2026-11-12  
> 性质：基于 EAW 已有 CAEGraph 定义的候选专业方法专题整理，**不是已发布 Skill、已验收的跨用例通用实现、完整对话逐字归档或 EAW 业务合理性结论**。  
> 对照格式：[四个候选观察准备 Skill：标准化高频用例落地与复用边界](四个候选观察准备Skill_标准化高频用例落地与复用边界_20261112.md)。  
> 录音背景：[观察迭代讨论转写（第一段录音）](https://github.com/daowei2026/feature-refinement-implementation-agent-evolution/blob/fy/observation-iteration-agent-20261109/discuss-materials/observation-iteration-agent/observation-iteration-recording-transcript.txt)。其重点是：给 AI 的应该是针对观察意图准备的适当数据；人的选区、缩放、叠加及辨识重叠等动作包含潜在的数据处理方法，不应要求 AI 反向从图像读回已经可以由代码整理的数据。  
> **本轮范围限制：只把 CAEGraph 图及其定义的画法和直接数据变换作为 Skill 提取证据。** AI Data 的通用运行/导出工具、Binder 为 EAW 另写的取数、引用回连、盘口衍生量、tick Bokeh 画法、附图0、批量页面组织等另设任务讨论；本文只在必要时用于辨明图形边界，不把其处理能力计入 CAEGraph 候选。

## 0. 首要入口：EAW 原 CAEGraph 究竟在哪里

本用例不只有一张“EAW 图”，而有逐步演化的几种页面。必须区分**实际 CAEGraph 定义、可核的原 HTML、尚未运行的示例配置**。

| 来源与状态 | CAEGraph 的实际内容 | 本轮如何使用 |
| --- | --- | --- |
| [T014 看图调研样稿](https://github.com/daowei2026/binder/blob/c6f928a04adbbc08c50036e31d07cec028128eb1/input/O001/A1%20%26%20A2%20opened/A2_M029_%E4%BB%BB%E5%8A%A1%E5%8C%85%E6%8B%86%E5%88%86%E5%B7%A5%E7%A8%8B/60_%E6%94%B6%E5%8F%A3%E8%BF%87%E7%A8%8B/%E7%AB%96%E5%88%87_%E5%8D%87%E7%BA%A7%E7%89%88Opened_20261015/VS6_%E7%9C%8B%E5%9B%BE%E8%B0%83%E7%A0%94/%E8%B0%83%E7%A0%94_v0_1.md)，`② | 设想以 1m/5s K 线、BP-07 三支持度、BP-09 三支持度为四个面板，配置写出但**明确只写未跑** | 仅用于追溯最早的观察目的，不称已生成实例 |
| [T056 实际图定义 `configuration](https://github.com/daowei2026/binder/blob/c6f928a04adbbc08c50036e31d07cec028128eb1/input/O001/A1%20%26%20A2%20opened/A2_M029_%E4%BB%BB%E5%8A%A1%E5%8C%85%E6%8B%86%E5%88%86%E5%B7%A5%E7%A8%8B/60_%E6%94%B6%E5%8F%A3%E8%BF%87%E7%A8%8B/%E7%AB%96%E5%88%87_%E5%8D%87%E7%BA%A7%E7%89%88Opened_20261015/VS6_%E8%AF%95%E9%A1%B5_GTQH/tools/page/page.py)，[原 HTML](https://github.com/daowei2026/binder/blob/c6f928a04adbbc08c50036e31d07cec028128eb1/input/O001/A1%20%26%20A2%20opened/A2_M029_%E4%BB%BB%E5%8A%A1%E5%8C%85%E6%8B%86%E5%88%86%E5%B7%A5%E7%A8%8B/60_%E6%94%B6%E5%8F%A3%E8%BF%87%E7%A8%8B/%E7%AB%96%E5%88%87_%E5%8D%87%E7%BA%A7%E7%89%88Opened_20261015/VS6_%E8%AF%95%E9%A1%B5_GTQH/tools/page/page.py_HTML)、[交件说明](https://github.com/daowei2026/binder/blob/c6f928a04adbbc08c50036e31d07cec028128eb1/input/O001/A1%20%26%20A2%20opened/A2_M029_%E4%BB%BB%E5%8A%A1%E5%8C%85%E6%8B%86%E5%88%86%E5%B7%A5%E7%A8%8B/60_%E6%94%B6%E5%8F%A3%E8%BF%87%E7%A8%8B/%E7%AB%96%E5%88%87_%E5%8D%87%E7%BA%A7%E7%89%88Opened_20261015/VS6_%E8%AF%95%E9%A1%B5_GTQH/tools/page/page.py_REPORT) | `CAEGraph` + 一个 `PlotSet`，四个面板：`k1m`、`k5s`、`materiality`、`opening` | **本次最清楚的 EAW 原 CAEGraph 主证据**：有实际运行结果及 HTML 字段回读 |
| [T059 S01 改版](https://github.com/daowei2026/binder/blob/c6f928a04adbbc08c50036e31d07cec028128eb1/input/O001/A1%20%26%20A2%20opened/A2_M029_%E4%BB%BB%E5%8A%A1%E5%8C%85%E6%8B%86%E5%88%86%E5%B7%A5%E7%A8%8B/60_%E6%94%B6%E5%8F%A3%E8%BF%87%E7%A8%8B/%E7%AB%96%E5%88%87_%E5%8D%87%E7%BA%A7%E7%89%88Opened_20261015/VS6_%E8%AF%95%E9%A1%B5_GTQH%E6%94%B9%E7%89%88/tools/redraw/render.py)、[独审摘要](https://github.com/daowei2026/binder/blob/c6f928a04adbbc08c50036e31d07cec028128eb1/input/O001/A1%20%26%20A2%20opened/A2_M029_%E4%BB%BB%E5%8A%A1%E5%8C%85%E6%8B%86%E5%88%86%E5%B7%A5%E7%A8%8B/60_%E6%94%B6%E5%8F%A3%E8%BF%87%E7%A8%8B/%E7%AB%96%E5%88%87_%E5%8D%87%E7%BA%A7%E7%89%88Opened_20261015/VS6_%E8%AF%95%E9%A1%B5_GTQH%E6%94%B9%E7%89%88/tools/redraw/render.py_REVIEW) | CAEGraph 本身只提供两张 1m/5s K 线；原两张支持度附图被删除，其他逐笔/判定链用直接 Bokeh 实现 | 仅核对 CAEGraph 的延续与删改，不将混合 Bokeh 新内容算成 CAEGraph |
| [正式看板的 CAEGraph 注册函数](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/big_world_chart.py)，约 L1875–2070 | `_register_big_graph` 30m、`_register_mid_graph` 1m、`_register_small_graph` 5s；`PlotSet`/`SpecEntitiesMainFig`/`KPriceLine` 与可选证据图层 | 用于观察多时间粒度、比例标准化等；不得把其 **非 CAEGraph 的 tick 附图和 EAW 专属衍生图**混入 |

- T056 图实例：品种 `rb`、日历 `@`、S01 本地观察窗 `2021-03-10 09:38:51 ～ 09:48:51`。K 线由 `KlineMsbView` 读取 `rb.1m.msb`／`rb.5s.msb`，两层均 `KPriceLine(..., std_method=None)`。
- T056 实际四个面板是 **K 线背景**与**判断支持度独立面板**；从 HTML 读回了 `BP-09` 的业务锚、确认点、三支持度及余量等关键数值，与正式结果清单一致。并不等于已经通过业务侧“像不像开战”的过目。
- 正式看板的 30m、1m、5s 采用 `std_method="ratio"`，但 5s 图集另设 `static_dynstd=True`。这与 T056/T059 的 `std_method=None` 不同，不能混成一套默认处理口径。
- 正式看板有大尺度页与中小尺度/tick 页两个 HTML。这里研究的只是其中 CAEGraph 构成的 30m、1m、5s 图；tick 主图和附图不在本轮研究范围内（[大尺度页面](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/big_world_chart.pyPAGE)、[中小尺度页面](https://github.com/daowei2026/binder/blob/c6f928a04adbbc08c50036e31d07cec028128eb1/input/O001/A1%20%26%20A2%20opened/A2_M029_%E4%BB%BB%E5%8A%A1%E5%8C%85%E6%8B%86%E5%88%86%E5%B7%A5%E7%A8%8B/60_%E6%94%B6%E5%8F%A3%E8%BF%87%E7%A8%8B/%E7%AB%96%E5%88%87_%E5%8D%87%E7%BA%A7%E7%89%88Opened_20261015/VS6_%E6%AD%A3%E5%BC%8F%E7%9C%8B%E6%9D%BF%E8%AF%95%E8%B7%91/pages/2_%E4%B8%AD%E5%B0%8F%E5%B0%BA%E5%BA%A6%E4%B8%8Etick_1m-5s-tick.html)）。

## 1. 对象边界与共同落地层次

“候选观察准备 Skill”应先说明**稳定的观察问题和处理方法**，再列明原 EAW 如何落地；不是简单抽象一份画图参数，也不要求每一种方法单独有一段新代码。参照标准化高频稿，将本轮证据按三层表示：

1. **特征和数据来源：** EAW `EawBattleP` 的正式输出（主要 `BP-07` 和 `BP-09`）、K 线；字段及业务语义以原输出为准。
2. **正式数据之后、为了观察而发生的处理：** 选择时间窗、按字段分出不同观察视图、保留共同身份与不同时间角色、价格比例标准化；没有专用后处理器的部分如实标明“原字段直接投影”。
3. **CAEGraph 图的表达：** 图集、主/附面板、`KPriceLine`、`EvidencePlotter`、点的时间/数值/文本字段、比例基准及是否动态更新。

不将 `EawBattleP` 原本计算支持度的业务实现，误记为“为了画图新算了支持度”；也不能把单纯视觉颜色、点大小当成新的业务观测量。

本次整理的 Skill 候选是**可选、可组合的方法**，而非必须串联的四步流水线。原图已经存在，后续检验优先复用现有运行与取图链，不为验证候选而重新发明一套图。

## 2. 候选 Skill 总览：与标准化高频结果的对应

| EAW 候选／对应已有 Skill | 稳定观察问题或专业方法 | EAW CAEGraph 实际落地 | 候选复用边界与本轮判断 |
| --- | --- | --- | --- |
| **E1 同一判断的竞争支持度对照**（EAW 新候选） | 对一个判断同时观察多个候选语义的支持度、余量及共同身份；重合值不能视作缺项 | T056 `BP-07` 的 trace/usable/strong，`BP-09` 的 probe/forming/committed 与 margin 各取字段做独立点层 | 适用同类竞争判断，不等于高频 S1 多参数事件序列比较；**建议保留为新候选** |
| **E2 同一对象的多时间角色表达**（复用高频 **S3**） | 业务发生位置、正式确认位置可以不同；同一对象多标记不得重复统计 | T056 同一 `BP-09.committed_support` 分别在 `business_anchor_uti` 与 `confirmed_at_uti` 上投影 | 是高频 S3 的跨用例验证，**不另立同义 Skill** |
| **E3 事件与多分辨率行情共时对照**（暂列新候选） | 将判定点放回不同时间粒度的局部行情，保留区间 K 线与瞬时判定点的区别 | T056 同一 `PlotSet.timespans` 下 1m/5s K 线和 BP 判断；正式看板 30m/1m/5s 采用多个 CAEGraph | 窗口如何自动选、如何派生各级节点不在 CAEGraph 直接定义中；**有方法候选，但独立性待核** |
| **E4 局部基准下的多价格层一致变换**（复用高频 **S4**） | 说明价格基准、加载/可见范围、变换生效时机，避免原值/显示值混淆 | T056/T059 不比值化；正式看板 30m/1m/5s 使用 ratio，5s 的 `static_dynstd=True` 与动态处理不同 | 补充高频 S4 的复用边界，**暂不新增** |
| 高频 **S1** 多组事件序列同口径比较 | 多套参数/同类事件序列的位置、疏密和强弱对照 | EAW 这些 CAEGraph 没有画多套判法/多参数方案产生的同类事件序列 | **未形成有效复用证据** |
| 高频 **S2** 评价依据、判断产生与应用时段分离 | 明确历史评价区间、结果可知时刻、应用时段 | EAW 图出现业务锚/确认点，但未展示评价区间和应用区间的完整关系 | **不能等同 S2 已实现** |

## 3. E1：同一判断的竞争支持度对照（新候选）

**专业方法。** 当一个判断同时给出多个候选类别/语义的支持度时，在**同一判断身份、同一判定语义层、可比数值口径**下并列保留这些值，检查主要语义与竞争项及其差距；避免点位重叠导致漏看。它比较的是**一个判断对象上的竞争语义**，不是不同方案所生成的独立事件序列。

**EAW 的特征数据。**

- `BP-07` 分量判断：`judged_at_uti`、`trace_support`、`usable_support`、`strong_support`、`attack_segment_ref`（悬停可回到对应记录）；原图还可展示 judgement_ref。
- `BP-09` 开战判断：`business_anchor_uti`、`confirmed_at_uti`、`probe_support`、`forming_support`、`committed_support`、`commitment_margin`、`anchor_ref`。
- 注意 `commitment_margin` 是竞争支持度差额，不是第四种开战类别支持度；`BP-07` 与 `BP-09` 处于不同判断层，虽然数值都在 0～1 范围，也不能自动作同一业务量比较。

**特征后的观察处理。** T056 [`configuration()`](https://github.com/daowei2026/binder/blob/c6f928a04adbbc08c50036e31d07cec028128eb1/input/O001/A1%20%26%20A2%20opened/A2_M029_%E4%BB%BB%E5%8A%A1%E5%8C%85%E6%8B%86%E5%88%86%E5%B7%A5%E7%A8%8B/60_%E6%94%B6%E5%8F%A3%E8%BF%87%E7%A8%8B/%E7%AB%96%E5%88%87_%E5%8D%87%E7%BA%A7%E7%89%88Opened_20261015/VS6_%E8%AF%95%E9%A1%B5_GTQH/tools/page/page.py) 中的 `point(key,x,y,text,color,marker)` 将一个表的不同 `y` 字段直接投影为不同点视图，保留各自的 `df_key` 和 `view_id`。此处并没有观察后处理算法重新求出支持度，也没有对数值做 `clip_linear` 之类的强度截断。

- `BP-07`：三种视图都以 `judged_at_uti` 作 x，分别用 `trace_support`、`usable_support`、`strong_support` 作 y。
- `BP-09`：`probe`、`forming`、`opened_business` 分别以 `business_anchor_uti` 作 x，各自选其对应支持度作 y；`margin` 在相同业务锚上画差额；`opened_confirmed` 另以确认时刻画同一 `committed_support`，时间角色另见 E2。
- T056 交件记录指出，S01 左右分量的 trace 和 usable 值重合；开战的 probe、forming 也在同一业务时刻和值上重合（[交件 `新 S01 数值解释样张](https://github.com/daowei2026/binder/blob/c6f928a04adbbc08c50036e31d07cec028128eb1/input/O001/A1%20%26%20A2%20opened/A2_M029_%E4%BB%BB%E5%8A%A1%E5%8C%85%E6%8B%86%E5%88%86%E5%B7%A5%E7%A8%8B/60_%E6%94%B6%E5%8F%A3%E8%BF%87%E7%A8%8B/%E7%AB%96%E5%88%87_%E5%8D%87%E7%BA%A7%E7%89%88Opened_20261015/VS6_%E8%AF%95%E9%A1%B5_GTQH/tools/page/page.py_REPORT)）。图像可能看成一个点，但数据应保留两个含义。

**CAEGraph 定义。** 四面板中的 `materiality: AllSymsFig(...)` 使用 `evidence(['trace','usable','strong'])`，`opening: AllSymsFig(...)` 使用 `evidence(['probe','forming','opened_business','opened_confirmed','margin'])`。支持度面板与 K 线价格面板分开，避免不同量纲混成同一 y 轴。

**供 AI 的数据材料。** 至少有判断/occurrence 身份、判定阶段、时间字段及时间角色、类别名称、支持度原值、如已有的竞争差额、图层映射和重合情况。原始值不能被图中一个重合点替代；不把两个表的类别混成一个无阶段标签的数组。

**迁移候选／待核。** 可迁移到其他输出互相竞争的状态支持度/隶属度场景。但 EAW 原图尚不足以说明支持度为何产生、前件是否充分、后续应如何改判法。若需求变成比较多套参数下事件位置和密度，那更接近高频 S1，应另按方案身份组织。

## 4. E2：同一业务对象的多时间角色表达（高频 S3 的 EAW 复用实例）

**专业方法。** 对同一个业务 occurrence 可以分别观察“业务上回指的位置”和“程序正式作出判断的位置”，二者共享身份但不能混同。在较早位置画一条已经确认的结果，是**事后回指**，并不意味着该位置当时已经可知最终结论。

**EAW 特征来源。** 正式 `BP-09` 的 `business_anchor_uti`、`confirmed_at_uti`、`committed_support`、`anchor_ref`。T056 新数据上的 S01：业务锚 `2021-03-10 09:43:39.5`，确认 `09:43:51`，两者相距 11.5 秒（[交件原值](https://github.com/daowei2026/binder/blob/c6f928a04adbbc08c50036e31d07cec028128eb1/input/O001/A1%20%26%20A2%20opened/A2_M029_%E4%BB%BB%E5%8A%A1%E5%8C%85%E6%8B%86%E5%88%86%E5%B7%A5%E7%A8%8B/60_%E6%94%B6%E5%8F%A3%E8%BF%87%E7%A8%8B/%E7%AB%96%E5%88%87_%E5%8D%87%E7%BA%A7%E7%89%88Opened_20261015/VS6_%E8%AF%95%E9%A1%B5_GTQH/tools/page/page.py_REPORT)）。

**特征后处理。** 本例**没有必要的新多时间角色处理器**，只是将同一个 `BP-09.committed_support` 在两种 x 字段上直接投影：

- `opened_business`：`x=business_anchor_uti`，`y=committed_support`。
- `opened_confirmed`：`x=confirmed_at_uti`，`y=committed_support`，图形用菱形以示区分。

**CAEGraph 定义。** T056 的 `opening` 附图同时接入两层；两层源于同一个 `BP-09` 结果和 `anchor_ref`，不是两次开战记录。

**供 AI 的数据材料。** occurrence 身份、`time_role`、原时间、支持度及其正式公布/确认时点；如果做延迟分析，可用确认与业务锚的间隔，但不能据此推断原判断的全部评价区间、当时可用信息或后续有效期。

**与高频 S3 的关系／复用边界。** 高频例子是代表高频结束与合并组确认结束；EAW 是开战业务锚与确认位置。稳定共同骨架较清楚，适合作为 S3 的第二个真实实例。若无稳定 occurrence 身份，只能说明字段角色，不能凭相近时间推定同一对象。

## 5. E3：事件与多分辨率行情的共时观察准备（待核新候选）

**专业方法（候选）。** 为评价一个离散业务判断位置，将该位置置于明确的行情时间背景，并用较粗/较细的时间粒度同时呈现；确保不同频率 K 线代表**区间**，判断点代表**有具体业务含义的时刻**，避免把绘图位置当作原始发生时刻。

**EAW 的原始输入。** T056 的 1m、5s K 线读面具有 `open/high/low/close/volume/openUti/closeUti`；判断来自 `BP-07.judged_at_uti`、`BP-09.business_anchor_uti`／`confirmed_at_uti`。T056 `PlotSet.timespans` 固定为同一 S01 时间窗，且 `extra_time=0`；正式看板分出 30m、1m、5s CAEGraph。

**特征之后／成图时的处理。**

- T056 直接选择两个频率的 K 线并交给 `KPriceLine`，由图中的窗口切片取实际 K 线数据，而不是重算 K 线或改变价格值。
- [uplot `KPriceLine._plot_fig`](https://github.com/daowei2026/uplot/blob/e6.2/utlv2.py) 使用 `openUti` 和 `closeUti` 将 K 线画在两者中间的 x 位置，即 `x=(openUti+closeUti)/2`；BP 判断点仍在其自身业务 UTI 上。
- CAEGraph 将价格图与 0～1 支持度图放在不同面板，并通过 `PlotSet`/日历/`timespans` 组织同窗。它们共用时间语义，不要求共用数值量纲。
- 正式看板 30m/1m/5s 是多个 CAEGraph 图的组合，**不保证彼此完全同窗**。其更深层级时间窗/节点由 CAEGraph 之外的输入流程准备；本轮仅把“接收各自明确的 `timespans` 并绘图”认作直接证据。

**CAEGraph 定义。** T056：`AllSymsMainFig` 的 `k1m`／`k5s`，另有 `materiality`／`opening` 两个 `AllSymsFig`。正式看板：[`_register_big_graph`](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/big_world_chart.py) 使用 30m，[`_register_mid_graph`](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/big_world_chart.py) 使用 1m，[`_register_small_graph`](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/big_world_chart.py) 使用 5s，并由外层页面嵌入。

**供 AI 的数据材料。** 事件身份和时刻、各频率 K 线的开始/结束及 OHLC、每个视图真实时间窗、日历时区及坐标转换、判断点所属记录与判断值。不能只给 K 线中心 x 而丢掉 K 线时间区间，也不能只给截图推定原始发生时刻。

**迁移候选／待核。** 可用于转折、突破、头尾等局部事件，需要同时看局部行情和位置的场景。但“如何自动挑正确的观察跨度、层级及代表窗口”**尚不能从 CAEGraph 直接定义证明**；如果新方法只剩下给不同频率 K 线配置 `timespans`，可能应降格为共享绘图组织约定而非独立 Skill。它与高频 S4 的区别在于**时间粒度/区间与点的对应**，不是价格标准化。

## 6. E4：局部基准下的价格变换（高频 S4 的 EAW 复用实例）

**专业方法。** 观察局部价格运动时，明确原始价格、选择的时间窗口、比例基准、受此变换的价格层及更新时机。不要把“图表参数都写 ratio”直接解释成“所有图层都随浏览器拖动以同一规则重算”。

**EAW 原图差异。**

| 实例 | 配置 | 对数据含义的影响 |
| --- | --- | --- |
| T056 S01 | `KPriceLine(..., std_method=None)` | 不启用比例标准化 |
| T059 中 CAEGraph 两张 K 线 | `KPriceLine(..., std_method=None)` | 同样不启用比例标准化；其余 Bokeh 图另议 |
| 正式看板 30m、1m | `std_method="ratio"` | 价格显示相对基准变化；究竟采用何时的基准依运行时窗口和实现 |
| 正式看板 5s | `std_method="ratio"`、`static_dynstd=True` | 以构图阶段的静态处理实现；并非与其他图完全一样的 JS 逐次更新 |

**源码关系。** [uplot `utlv2.py / KPriceLine`](https://github.com/daowei2026/uplot/blob/e6.2/utlv2.py) 把 `open` 作为基准字段，`high/low/close` 作为附属价格字段登记到 `DynStd`；[`pfw.py / DynStd`](https://github.com/daowei2026/uplot/blob/e6.2/pfw.py) 保存 `__prestd_*` 原值并建立关联图层变换；[`dynstd.js`](https://github.com/daowei2026/uplot/blob/e6.2/dynstd.js) 按可见 x 范围动态处理；[`utkv2.py / BaseFigSet._finish_fig`](https://github.com/daowei2026/uplot/blob/e6.2/utkv2.py) 遇到 `static_dynstd=True` 则转为一次 Python 静态处理。

**供 AI 的数据材料。** 原价格、显示价格、基准、实际加载/可见范围、动态或静态路径、同一价格实体下适用的图层，以及已完成更新/尚未更新的状态。`ratio` 是原值除以基准，不自动等于涨跌百分比。

**迁移与待核。** 与高频 S4 的专业问题基本一致，本轮不新增 Skill。但**只看 EAW CAEGraph** 不能声称它已经验证了 EAW 的墙、攻击段等所有价格层与 K 线共同进行同基准变换；这些 EAW 专属层位于本轮排除的部分。若实际 HTML 的交互和生成阶段的数组不一致，应实测后确认，不能按想象补齐。

## 7. 为什么高频 S1、S2 不能直接算 EAW 的已验证复用

- **S1 多组事件序列同口径比较：** T056 画的是同一判断下的多个语义支持度，而非 20 组参数方案等**同类候选事件序列**。相同时间的两个支持度点不等同两个候选方案生成的不同事件。E1 因此作为不同专业问题保留。
- **S2 评价依据／判断产生／应用时段分离：** EAW CAEGraph 只有业务锚与确认点，**没有完整明确的评价历史段和生效时段图层**。二者能够支撑高频 S3 的时间角色区分，却不能自动推出“过去哪段历史用于评价”“何时可应用”。
- **与业务合理性分析的关系：** 支持度和位置画出来，不代表某次 EAW 开战“业务上像开战”；原交件 `business_completed=false`。本次不根据图上数字判断业务正确性。

## 8. 源码与已生成图的导航

| 类型 | 入口 | 读什么 |
| --- | --- | --- |
| 对照讨论稿 | [标准化高频四候选](四个候选观察准备Skill_标准化高频用例落地与复用边界_20261112.md) | S1～S4 的专业方法粒度、三层落地结构及复用限制 |
| T014 讨论样稿 | [VS6 看图调研 `②](https://github.com/daowei2026/binder/blob/c6f928a04adbbc08c50036e31d07cec028128eb1/input/O001/A1%20%26%20A2%20opened/A2_M029_%E4%BB%BB%E5%8A%A1%E5%8C%85%E6%8B%86%E5%88%86%E5%B7%A5%E7%A8%8B/60_%E6%94%B6%E5%8F%A3%E8%BF%87%E7%A8%8B/%E7%AB%96%E5%88%87_%E5%8D%87%E7%BA%A7%E7%89%88Opened_20261015/VS6_%E7%9C%8B%E5%9B%BE%E8%B0%83%E7%A0%94/%E8%B0%83%E7%A0%94_v0_1.md) | 最初四面板方案，**只写未跑** |
| **原始 CAEGraph** | [T056 `configuration()](https://github.com/daowei2026/binder/blob/c6f928a04adbbc08c50036e31d07cec028128eb1/input/O001/A1%20%26%20A2%20opened/A2_M029_%E4%BB%BB%E5%8A%A1%E5%8C%85%E6%8B%86%E5%88%86%E5%B7%A5%E7%A8%8B/60_%E6%94%B6%E5%8F%A3%E8%BF%87%E7%A8%8B/%E7%AB%96%E5%88%87_%E5%8D%87%E7%BA%A7%E7%89%88Opened_20261015/VS6_%E8%AF%95%E9%A1%B5_GTQH/tools/page/page.py) | 实际 CAEGraph、四面板、`point` 的字段映射，K 线 `std_method=None` |
| T056 实际图 | [S01.html](https://github.com/daowei2026/binder/blob/c6f928a04adbbc08c50036e31d07cec028128eb1/input/O001/A1%20%26%20A2%20opened/A2_M029_%E4%BB%BB%E5%8A%A1%E5%8C%85%E6%8B%86%E5%88%86%E5%B7%A5%E7%A8%8B/60_%E6%94%B6%E5%8F%A3%E8%BF%87%E7%A8%8B/%E7%AB%96%E5%88%87_%E5%8D%87%E7%BA%A7%E7%89%88Opened_20261015/VS6_%E8%AF%95%E9%A1%B5_GTQH/tools/page/page.py_HTML)、[试页及读回记录](https://github.com/daowei2026/binder/blob/c6f928a04adbbc08c50036e31d07cec028128eb1/input/O001/A1%20%26%20A2%20opened/A2_M029_%E4%BB%BB%E5%8A%A1%E5%8C%85%E6%8B%86%E5%88%86%E5%B7%A5%E7%A8%8B/60_%E6%94%B6%E5%8F%A3%E8%BF%87%E7%A8%8B/%E7%AB%96%E5%88%87_%E5%8D%87%E7%BA%A7%E7%89%88Opened_20261015/VS6_%E8%AF%95%E9%A1%B5_GTQH/tools/page/page.py_REPORT) | 实际输出已生成，六项 BP-09 关键数字实读对账，确认“图已出”而非业务验收 |
| T059 中的 CAEGraph | [`redraw/render.py`](https://github.com/daowei2026/binder/blob/c6f928a04adbbc08c50036e31d07cec028128eb1/input/O001/A1%20%26%20A2%20opened/A2_M029_%E4%BB%BB%E5%8A%A1%E5%8C%85%E6%8B%86%E5%88%86%E5%B7%A5%E7%A8%8B/60_%E6%94%B6%E5%8F%A3%E8%BF%87%E7%A8%8B/%E7%AB%96%E5%88%87_%E5%8D%87%E7%BA%A7%E7%89%88Opened_20261015/VS6_%E8%AF%95%E9%A1%B5_GTQH%E6%94%B9%E7%89%88/tools/redraw/render.py)、[独审摘要](https://github.com/daowei2026/binder/blob/c6f928a04adbbc08c50036e31d07cec028128eb1/input/O001/A1%20%26%20A2%20opened/A2_M029_%E4%BB%BB%E5%8A%A1%E5%8C%85%E6%8B%86%E5%88%86%E5%B7%A5%E7%A8%8B/60_%E6%94%B6%E5%8F%A3%E8%BF%87%E7%A8%8B/%E7%AB%96%E5%88%87_%E5%8D%87%E7%BA%A7%E7%89%88Opened_20261015/VS6_%E8%AF%95%E9%A1%B5_GTQH%E6%94%B9%E7%89%88/tools/redraw/render.py_REVIEW) | 只保留两张 K 线，支持度附图删除；其他直接 Bokeh 图不纳入本轮 |
| 正式看板 CAEGraph | [`aidata/big_world_chart.py`](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/big_world_chart.py) L1875–2070 | 30m/1m/5s 三种 `CAEGraph[graph_key]`、`PlotSet`、`KPriceLine` 的注册配置 |
| CAEGraph 基础画法 | [`uplot/utlv2.py`](https://github.com/daowei2026/uplot/blob/e6.2/utlv2.py)、[`utkv2.py`](https://github.com/daowei2026/uplot/blob/e6.2/utkv2.py) | K 线时间坐标、主附面板、静态标准化开关 |
| 价格标准化 | [`uplot/pfw.py`](https://github.com/daowei2026/uplot/blob/e6.2/pfw.py)、[`dynstd.js`](https://github.com/daowei2026/uplot/blob/e6.2/dynstd.js) | 原值、基准、视窗及关联显示变换 |
| 通用证据绘制的边界 | [`aidata/evidence_plot.py`](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/evidence_plot.py) | 说明 T056 的点层由现有画法消费；本轮不扩展为 AI Data 工具能力研究 |

版本说明：Binder 引用 `c6f928a04adbbc08c50036e31d07cec028128eb1`，AI Data 引用 `9ff7ce4929b36945f63b1c9875e59f68141f997a`，uplot 阅读基线为 `e6.2`。这些是源码追溯锚点，**不是已核实三仓在单次历史运行中的完整版本锁**。历史工作进程、页导出后 JS 状态与其他分支的差异尚需实际环境核实。

## 9. 当前状态与后续使用原则

- **候选结论：** EAW 初步新增 E1“同一判断的竞争支持度对照”、E3“事件与多分辨率行情共时对照”；E2 并入高频 S3 的复用验证；E4 并入高频 S4 的复用验证。E3 是否足以独立为 Skill 仍有不确定性。
- **没有新增的：** 高频 S1、S2 在此批 EAW CAEGraph 中缺乏充分同型证据；不为凑四项而硬套。
- **不应过早建设：** 不要求每个候选都有新 Python 处理器，不从视觉展示值倒推正式数据，也不为了统一形式重画 T056、T059 和正式看板。
- **后续需要验证：** 真实 HTML 的视窗及重合支持度读取、判断身份与时间角色关系、5s 静态标准化及跨尺度读数的一致性；跨另一个真实场景能否保持相同触发问题和处理骨架。
- **范围已留给另外任务：** AI Data／Binder 工具本身值得保留的通用能力、EAW 的墙失效遮蔽、上游引用回连、主动买卖代理价、盘口成交/撤单诊断、tick 图和多例页面组织等，不计入本次 CAEGraph 候选结论。这些内容可能比本轮更具有专业数据处理价值，但必须另以原代码、原图、观察意图为证据独立分析。

> 本文是可继续审查和修改的讨论材料，不代替完整聊天 provenance，也不把候选方法作为 Owner 已确认的 Skill 合同。
