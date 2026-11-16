# aidata 四层选位与 CAEGraph 落地对照

> **用途**：为 [高频特征的分层观察与位置选择 Skill](../SKILL.md) 提供可直接照用的 aidata 初版选位配置与绘图实现映射，**不**另发明观察领域术语或样本价值排序方法。
>
> **核查源码基线**：\`daowei2026/aidata@9ff7ce4929b36945f63b1c9875e59f68141f997a\`，\`standard_multiscale\` Profile v4。这里的参数是 aidata 当前标准 Profile 的已有实现，**不是为 EAW Wall 重新证明合理的参数**。
>
> **边界**：阅读本页已足以知道怎样按当前既有方案定位及组织图；只有实际接口不匹配、需要执行代码或核验历史事实时，才针对表中准确文件/函数查源码，不应把“重新设计 aidata 选位方法”交给执行 Agent。

## 一、先区分三件事

1. **位置定位**：\`timespan_builder.py\` 从定位特征的真实位置提取 \`big → mid → small → tick\` 节点时间窗，写入 \`manifest/timespan_index.csv\`。
2. **图形组织**：\`big_world_chart.py\` 根据已有节点时间窗定义 CAEGraph 和 Bokeh 页面。四层**不是**四张 CAEGraph。
3. **证据数据**：\`feature_slicer.py\` 从观察特征真实接口取得按节点切片的数据；\`delivery.py\` 打包。图的 \`plot_view_data\` 不替代这些切片。

\`big/mid/small/tick\` 是 aidata 的**时间窗节点名**；绘图中 \`1d/30m/1m/5s/半秒盘口\` 是**展示所用行情频率**。不能把这两套名称机械当成一一对应的“图层总数”。

## 二、四层默认定位：特征、字段、生成顺序

| 时间窗 | 在什么范围内继续定位 | 定位特征及当前默认参数 | 从特征读取的实际位置 | 对应细看行情 |
|---|---|---|---|---|
| \`big\` | overview 全局有效范围，或 focused 指定范围 | \`ZigConfirm\` 包裹 \`ZigZag\`；\`KLine(freq="30m")\` 的收盘价；\`retracePct=10\` | \`zigUTI\` | 30m |
| \`mid\` | 一个 big 时间窗内 | \`ScaleTurnCalendar("large")\`，即 30m 的 L 尺度贴近转折 | \`x\` | 1m |
| \`small\` | 一个 mid 时间窗内 | \`ScaleTurnCalendar("mid_1m")\`，即 1m 的 M 尺度贴近转折 | \`x\` | 5s |
| \`tick\` | 一个 small 时间窗内 | \`ZigConfirm\` 包裹 \`ZigZag\`；\`KLine(freq="1m")\` 的收盘价；\`retracePct=0.4\` | \`zigUTI\` | half-second L1 盘口 |

**代码位置**：
- [profiles.py 的 \`_big_anchor\`、\`_large_turn_anchor\`、\`_mid_turn_anchor\`、\`_tick_anchor\`](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/profiles.py#L381-L453)
- [timespan_builder.py 的 \`extract_feature_anchored_big_spans\`、\`_extract_mid_small_with_actual_position_fields\`、\`extract_timespans_by_actual_position_fields\`](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/timespan_builder.py#L189-L600)

\`mid\` 的 L、\`small\` 的 M 是**定位特征使用的尺度名称**，不等于绘图层级的命名；在 \`mid\` 节点上显示的是 1m 行情，在 \`small\` 节点上显示的是 5s 行情。tick 的定位依据是 1m Zig，但细看的是半秒盘口。

\`ScaleTurnCalendar\` 的 DataFrame index 可能对应确认时间，定位必须用 \`x\`；不要将 \`xConfirm\` 或其他确认位置字段当成实际转折位置。Zig 读取 \`zigUTI\` 而非 index/确认时点。

## 三、现有分段参数（照原值使用，不重新调参）

\`n_inter\`、\`n_margin\`、\`n_max\` 都以 **UTI 数量**传入，以下保留 aidata 原始表达以免日历／交易时段换算失真。

| 节点 | \`n_inter\` | \`n_margin\` | \`n_max\` | 代码来源 |
|---|---|---|---|---|
| big | \`7200 * 24 * 3\` | \`7200 * 24 * 2\` | \`7200 * 24 * 10\` | \`profiles.build_overview_run_brief\` 与 \`build_focused_run_brief\` 的 \`big_source.params\` |
| mid | \`7200 * 10\` | \`7200 * 5\` | \`7200 * 30\` | \`profiles.build_focused_run_brief().timespan_extraction.mid\` |
| small | \`60 * 120\` | \`15 * 120\` | \`120 * 120\` | \`timespan_extraction.small\` |
| tick | \`5 * 60 * 2\` | \`150 * 2\` | \`12 * 60 * 2\` | \`timespan_extraction.tick\` |

**这些参数的实际作用**：
- \`n_inter\` 是同段候选发生位置允许的跨度限制，**不是两个任意相邻 occurrence 的最大独立间隔**。
- \`n_margin\` 用在生成时间窗时增加前后范围。
- \`n_max\` 限制时间窗长度；源码的分段条件同时考虑 \`n_inter\` 和 \`n_margin/n_max\`。
- 实现先从定位字段选出所需范围内的 UTI，去重排序；调用 \`mquant.uplot.core.identify_uti_segments\`（导入失败时有兼容实现），按上述参数输出窗口。不要自行改成按自然日期等宽切分。
- 生成 tick 窗口后会先裁到父 small 窗口、再合并相互重叠的 tick 段。

**数量上限**：
- overview：\`overview_max_big_nodes = 10000\`；\`generation_depth="big"\`，不会因此产生 mid/small/tick。
- focused：\`max_big_nodes=60\`、每个 big 的 \`max_mid_nodes=60\`、每个 mid 的 \`max_small_nodes=60\`、每个 small 的 \`max_tick_nodes=60\`。
- 源实现对超过上限的列表按生成顺序截取并记录原始、保留、丢弃数量；**不是评分排序后取最典型的 60 个**。

**来源**：
- [profiles.py 参数与 Profile v4](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/profiles.py#L25-L245)
- [timespan_builder.py：四层提取与窗口裁合](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/timespan_builder.py#L330-L698)

## 四、overview 与 focused：两种已存在的运行方式

**仅有历史大范围时**（现有标准平台操作）：

\`\`\`text
overview：数据有效的全局范围
  → 只运行 big 定位特征
  → timespan_index 的 big 位置
  → 1d 全局 CAE 图（标出搜索范围和 big 时间框）
  → 由使用者明确 focused 的开始/结束日期
focused_search：在所选日期范围重新提取 big/mid/small/tick
  → 新 run 的 timespan_index/chart_manifest/source_occurrences
  → 大—中—小及中—小—tick 页面
\`\`\`

**已有具体时间范围时**：公开 API 的 \`run_brief_input\` 可直接给 \`big_source.search_timespans\`，以 \`generation_depth="tick"\` 生成该范围的四层时间窗，省去全局 overview 的使用者操作。具体例子见 [examples/microstructure_review.py](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/examples/microstructure_review.py)。注意该例为适应当时实际缓存情况，把 tick 的定位换成了另一种 ScaleTurn；**这不是 Profile v4 的默认 tick 定位，不可无声明照抄成标准选位规则**。

现有标准平台采用的 Profile 具名配置为 \`standard_multiscale\` v4，默认全局历史 \`2013-02-19 ～ 2024-02-29\`、板块输入 \`blk@...\`。这一 Sof、时间和对象范围是**该 Profile 的实例约束**，不是此方法适用于其他特征时必须使用的输入。目标 Wall 若使用不同品种/时间/数据，须绑定其真实运行上下文，保留四层定位方法，但不能假装标准 Profile 已直接支持该 Wall。

**重要限制**：overview → focused 目前由使用者选定日期；没有已验证的自动选“典型历史位置”算法。focused 会重新搜索 big，只记录 \`source_chart_run_id\`，不直接继承旧 big identity，必须以 \`run_id + 时间窗\` 核对。

**来源**：
- [aidata README：怎样使用与跨图编号限制](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/README.md)
- [USER_OPERATION_V1.md：Overview / Focused / Build Evidence / Refresh](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/docs/USER_OPERATION_V1.md)
- [RUN_BRIEF_INPUT_CONTRACT.md：run_brief 的字段](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/docs/RUN_BRIEF_INPUT_CONTRACT.md)

## 五、四层实际如何形成多张 CAEGraph 与 Bokeh 图

### 5.1 一张图对应哪种页面

| 页面类及生成数量 | 内部调用的绘图构造 | 时间窗来源 | 显示 |
|---|---|---|---|
| \`AidataRunOverviewCAE\`（每个 run 一个总览页） | \`_register_run_overview_graph\` 注册一个 \`CAEGraph\`，\`CAEGraph(...).layout()\` | 整个 overview 有效范围；上层标注 big 节点和搜索范围 | 1d 主图、搜索范围、big 时间框 |
| \`AidataBigWorldReviewCAE\`（每个 big 一个页面） | \`_register_big_graph\` + \`_register_mid_graph\` + \`_register_small_graph\`，对应三种 **CAEGraph 定义**；big 使用 \`.layout()\`，mid/small 分别对父子窗口 \`.produce_widgets()\` | big 当前节点及其子 mid/small 的 explicit timespan | 一个 30m big 图、多个 1m mid 图及其多个 5s small 图 |
| \`AidataMidTickWorldReviewCAE\`（每个 mid 一个页面） | \`_register_mid_graph\` + \`_register_small_graph\` 对应两种 **CAEGraph 定义**；tick 由 \`_tick_l1_figure\` / \`_build_tick_l1_figure\` **Bokeh 绘图**，没有 tick CAEGraph | mid 当前节点、子 small、子 tick | 1m 大图、5s 子图、各小窗口对应的半秒盘口及附图 |

因此，“四层”不能化约为“一个包含四个 PlotSet 的 CAEGraph”；单个页面也可能组合多个 CAEGraph 和直接 Bokeh 图元。一个图定义可以对多个不同的 \`timespans\` 复用，不能把每个 node 都当成一份全新图定义。

### 5.2 具体图定义从哪里照搬

- [big_world_chart.py：三个 \`BaseCAEFao\` 页面类、内部组合](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/big_world_chart.py#L38-L357)。
- [big_world_chart.py：\`_register_run_overview_graph\`](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/big_world_chart.py#L1826-L1874)：\`PlotSet(main)\` + \`SpecEntitiesMainFig\` + \`KPriceLine(KLine('1d'), std_method='ratio')\`；\`extra_time=0\`。
- [big_world_chart.py：\`_register_big_graph\`](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/big_world_chart.py#L1875-L1924)：30m \`KPriceLine\`，\`PlotSet(main)\`，\`extra_time='10h'\`。
- [big_world_chart.py：\`_register_mid_graph\` 与 \`_register_small_graph\`](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/big_world_chart.py#L1925-L2040)：1m、5s \`KPriceLine\`，对应 \`plotsets.main.timespans\`、\`plotsets.smallscale.timespans\`；5s 图配置 \`extra_time='10m'\`；1m 另外有开盘辅助附图。
- [big_world_chart.py：tick 盘口绘制](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/big_world_chart.py#L592-L801)：\`tick_provider.read_symbol_window(symbol, start, end)\` 读取 half-second L1；\`_build_tick_l1_figure\` 绘 Bokeh 盘口价格、买卖价量、交易量/持仓变化等附图；读取失败时显示未读取提示而不是假数据。
- [big_world_chart.py：基于 Bokeh 的窗口辅助与页面滚动布局](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/big_world_chart.py#L2080-L2260)：父图标注子节点时间框、实际点竖线，\`CurrWidgets\` 与 \`ScrollBox\` 组织多图。

**观察特征的接入**：[evidence_plot.py](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/evidence_plot.py#L65-L226) 使用 \`EvidencePlotter\` / \`evidence_plotters\`，依目标特征自身已核实 \`plot_binding\` 在相应 \`surfaces\` 绘制；tick 使用 \`add_tick_evidence\` 单独叠加。这是已有的显示合同，**不能凭 Wall 特征名称猜想可用字段**。需要核对其实际 \`to_df()/to_dfs()\`、源值、时间绑定和是否已具备此画法。

### 5.3 怎样实际生成页面，不只是定义图

\`\`\`python
from mquant.aidata.api import (
    build_chart_run, build_run_overview_chart_page,
    build_big_world_chart_pages, build_board_run
)

# run_brief_input 必须已经按本轮真实代码、数据、日历、对象配置；
# 这里不填假造的 context/blk/feature。
run = build_chart_run(run_brief_input, dry_run=False)

# 仅需长期 overview 时：
overview = build_run_overview_chart_page(
    run, run_brief_input=run_brief_input, save=True
)

# 需要完整 big→mid→small→tick 详情时：
# run_brief_input 必须 generation_depth="tick" 且有真实定位特征。
pages = build_big_world_chart_pages(
    run, run_brief_input=run_brief_input, save=True
)

# 需要真实主证据切片时复用当前同一批节点：
full = build_board_run(run_brief_input, reuse_core=True, dry_run=False)
\`\`\`

**上述代码为接口调用顺序示意，不是可脱离真实 \`context\`／\`blk\`／Sof／特征运行的完整脚本。** 针对一项任务应选择 overview 或 focused 相应的输入，而不是把 overview 与 focused 误用为同一个 run／同一套 \`run_brief_input\`。新页面类还要求平台反序列化支持，见 [DEVELOPMENT_GUIDE.md](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/docs/DEVELOPMENT_GUIDE.md)。

## 六、时间窗、图和数据的唯一对应关系

源实现里用于统一对应的是：

\`\`\`text
build_chart_run(...)
  run_brief / context / calendar
  manifest/timespan_index.csv    ← big/mid/small/tick、parent_node_id、start/end
  source_occurrences/            ← 具体定位特征的原始 occurrence
  manifest/chart_manifest.csv    ← 每个 node 的 explicit timespan
             ↓
  AidataRunOverviewCAE / AidataBigWorldReviewCAE /
  AidataMidTickWorldReviewCAE 及 Bokeh tick 图
             ↓ （有证据需要时）
build_board_run(..., reuse_core=True)
  feature_slices/                 ← 源观察特征真实切片
  delivery/                       ← 对应节点数据包
\`\`\`

- \`timespan_index\` 的 \`node_id\`、\`parent_node_id\`、\`start_uti/end_uti\` 是画图与取数的核心关联；不要在渲染时重新跑 \`ExtractTimespans\`。
- \`n_margin\` 改的是**节点时间窗本身**，\`extra_time\` 只是图上可见的前后行情，不应扩大数据切片。
- \`build_chart_run\` 产生定位及构图元数据，**不**自动导出目标特征切片，也**不**物化半秒盘口 CSV。
- \`build_big_world_chart_pages\` 创建页面 URL，**不**表示页面已经成功打开或 tick 已经被读取。tick 图依用户打开页面等实际操作而按需读取；半秒盘口 CSV 另走 \`materialize_big_small_tick_slice\`。
- \`feature_slices\` 是主证据；\`plot_view_data\` 只是共享显示视图，不应凭后者逆推原始数据。
- 同一时间位置从 overview 进入 focused 可能因重新搜索而重新编号，必须用 \`source_chart_run_id\` 和实际时间范围追溯。

**来源**：
- [boardrun.py：\`build_chart_run\` / \`build_board_run(reuse_core=True)\`](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/boardrun.py)
- [chart_review.py：frozen explicit timespan](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/chart_review.py)
- [render_bridge.py：按 node_id 渲染，不重新选位](https://github.com/daowei2026/aidata/blob/9ff7ce4929b36945f63b1c9875e59f68141f997a/render_bridge.py)

## 七、对 EAW Wall 复用时不能假装已经完成的部分

这份初版 Skill 只固定**四层选位及多图组织**。EAW Wall 真正接入时仍须依据已有第 1～3 步的材料调查核对：Wall 实例的品种、历史范围和日历；其可用输出、状态/变化时间及是否有可读真实数据；拟显示的字段与位置、输出来源/处理角色、对应图层的可用 \`plot_binding\`；正确重放的历史依赖以及性能限制。不能假装 \`standard_multiscale\` 的默认历史数据和已登记 Feature 已经涵盖 Wall。

特别是：\`WallAssembler\` 可以消费 tick/半秒行情、产出稀疏 Wall 变化与状态 trace；\`EawP1WallLifecycleFrp\` 当前文档约束下直接接收 typed Wall occurrence 而不是直接消费原始 tick。**定位用行情转折窗口，不应误写为根据 Wall occurrence 自己就能生成与 aidata 一样的四层**。窗口裁剪仅限定观察范围，不自动保证从该处独立重算时已具有正确的历史阈值或 Wall 生命周期状态。

如果某项输出／绘图接口未具备，只报告对应缺口；不因目标特征名是 Wall 而虚构 \`to_df\` 字段、CAE 图已生成、完整观察完成或正式业务判断。

## 八、执行完成时应交出什么

在已经实际运行的情况下，至少指向本次 \`run_id\`、\`run_brief\`（除内存运行时对象）、\`timespan_index.csv\`、\`source_occurrences\`、\`chart_manifest\`、图 URL 与其页面类、实际已取得的数据切片、截断/失败记录、已核对的原值/显示值范围。

未运行成功或只完成图定义时，按原观察准备流程明确标明实际完成范围；不得将本页这份源码对照文档或 CAEGraph 类的存在本身当作实际数据交付。
