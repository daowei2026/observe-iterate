# aidata 的必经数据入口与两种本批用法

本页保存可复用的接口用法、当前输入选择和影响研究的工具边界。依据是 Owner 提供的两项真实测试报告及代码；原件、版本和材料覆盖范围见 [测试来源说明](references/aidata_20261027/README.md)。测试结果不是本批业务成果，也不另设一项专业工作或运行 Gate。

## 1. 位置与责任

本批所有正式行情、定位特征和分析输入必须由 aidata 接口及其正式交付提供。允许 AI 在取得的数据上程序筛选、计算辅助量和回看，不允许在 observe-iterate/cgpterm 中另建直接 KLine、数据库或旧 ZIP 的平行取数路径。构造 `KLine(...)` 等 Feature 对象交给 aidata 是正常配置，不是绕过 aidata 取数。

已知实际工作区为 `/dwdhome/fy/BASE_E6_2`。它不是 Git 仓库身份，也不授予其中所有仓库写权。沿用现场已有环境，记录真实 checkout 和必要本地差异，不因整理本页重新安装依赖或重做全部基础预检。本页本身不授予 aidata、uplot、tis/frp 或共享服务写权；具体修复以真实 Owner 授权及相应技术工单的明确范围为准。

接口历史出处仍是 [04_AIDATA_USE.md 第3节](https://github.com/daowei2026/observe-iterate/blob/9badfa6f30caebbe3156c5e4ee4deb43d22cacb5/professional/feature_observation/04_AIDATA_USE.md#3-%E5%AE%9E%E9%99%85%E4%BD%BF%E7%94%A8%E6%97%B6%E6%80%8E%E6%A0%B7%E8%80%83%E8%99%91)。只复用接口关系，不继承旧四项工作的验收顺序。使用版本变化时定向核 README、API 和输入合同，不把报告中的工作分支名或缩写 SHA 当作新的实际版本证明。

## 2. 仍从这三个接口理解

| 接口 | 负责什么 | 不代表什么 |
| --- | --- | --- |
| `build_chart_run(run_brief_input, dry_run=False)` | 建立 run，确定图与数据共用的节点/时间范围 core | 尚未证明生成平台图或正式 feature_slices |
| `build_big_world_chart_pages(run, run_brief_input=..., save=True)` | 消费 core，生成平台图并返回图定位；测试版本内部先建 overview，再逐 big 建页 | 返回多个页面不等于已经组合为一个页面 |
| `build_board_run({...run_brief_input, "run_id": run.run_id}, reuse_core=True, dry_run=False)` | 复用同一 core，形成正式切片、来源索引和数据交付 | 不追加冻结节点，不替代专业分析或平台打开核验 |

仅画概览时实际调用 `build_run_overview_chart_page`，它是图生成层的独立入口，不是假称调用了第二接口。单页组合是现有平台的页面组织动作，不是第四种行情获取接口；实际采用的组合代码、调用顺序与 URL 另记。

## 3. 当前这组三品种的输入选择

以下是本批 rb/hc/i 的具体设置，不是所有未来板块的永久默认值。

| 输入 | 本批采用方式 |
| --- | --- |
| 对象 | `blk=extract_time_syms="blk@steel"`；报告中的实际成员为 rb、hc、i，实际运行仍保留成员展开结果 |
| Context 数据集 | 沿用已测试的 `sof_name="TA_updto20240229_DBA"`、`stk_tlist="tick_test_all57_takeout_lcNsiNcy"` |
| 共同观察起点 | `2021-01-01`。Owner 明确这三个品种从此时起交易日历相同，之前时间对不齐；概览不再从 2013 年开始 |
| Context 起点 | 两种方式均把 `OptContext` 的 `startDay` 设为 `2021-01-01`，不能只修改 manual 用例窗口或前端缩放而保留 2013 年概览 |
| 结束边界 | 按实际选定范围传入 `endDay`；报告使用 `2024-02-29`，但有效日线止于 2024-02-28 收盘，不能写成包含结束日全天 |
| 日历 | `calendar_override="night_end_at_2300"`；本批共同范围不等于以后任何品种都可强行套同一日历 |
| 节点 | `generation_depth="big"`、`big_source.mode="manual"`；不生成 mid/small/tick 子节点 |
| 正式行情证据 | `make_point_anchor(KLine(freq="1d"/"30m"), uti_fields="closeUti", slice_levels=["big"], evidence_role="market_context_sidecar", is_raw_market_data=True, ...)` |
| 30m 图上的贴近转折 | `ScaleTurnCalendar("mid")`，时间字段 `x`、图点 `x/y`，`slice_levels=["big"]`、`plot_binding.surfaces=["big"]` |
| 运行与输出 | 本次唯一 run_id、实际 output_root；不复用测试 run_id 或把测试目录当正式批次目录 |

**30m 是 K 线频率，big 是节点/展示层级，mid 是贴近转折参数，三者独立。** 换成 mid 不需要改 `generation_depth`、`slice_levels` 或 `surfaces`，也不表示增加 1m 中尺度页面。特征对象、feature_key、图例和正式数据引用都应一致改成 mid；不能只把 large 的图例改名，或继续读取 large 的旧 CSV。

本批初始全范围扫描与概览采用上述共同范围；回看仍不预设固定 T 或固定长度。若具体研究确需更早信息或计算预热，分别说明实际计算范围、可比范围和展示范围，不能把 2021 年之前未对齐的信息无说明并入三品种共同对照。

已整理 [当前入参示例](examples/aidata_inputs.py)：只构造 brief 和 Feature 描述，没有取数、保存图或自动执行；保留现有 aidata API。结束边界、输出位置、run_id 和真实用例窗口由调用方填写。该示例已按 Owner 要求改为 2021 起点和 mid，不能冒称其全部组合已在现场重跑通过。原测试的 `ensure_profile_runtime()` 只是注册配置；自定义 brief 的 `profile_id="" / profile_version=0` 不能称为标准 Profile v4。

## 4. 两种用法及各自真正得到的数据

### 方式一：只有 1d 的图和正式数据——用于全范围寻找位置

用 `make_overview_brief` 构造本次 brief：Context 从 2021-01-01 开始，唯一 manual 窗口为 `(2021-01-01, 实际结束边界, full_history)`，证据只有 1d KLine。`slice_levels=["big"]` 只表示在该全范围节点切日线，不会因此自动创建 30m 页面。

```python
# brief 是当前有效完整输入；在已有 mquant 环境中调用以下现有 API。
run = build_chart_run(brief, dry_run=False)
page = build_run_overview_chart_page(run, run_brief_input=brief, save=True)
board = build_board_run(
    {**brief, "run_id": run.run_id}, reuse_core=True, dry_run=False
)
```

实际顺序为第一个接口 → 独立 overview 入口 → 第三个接口；不调用 `build_big_world_chart_pages`。从正式交付取得这段共同历史的 rb/hc/i 日线，供 AI 扫描并自行选择用例。报告已验证 `closeUti` 绑定和这条图数链，不必再次从零调查日线是否能导出；新起点下的实际覆盖仍由本次输出说明。

### 方式二：1d 概览 + 用例 30m 大尺度图 + mid 贴近转折及正式数据

用 `make_case_brief` 构造本次 brief：Context 仍覆盖 2021 起的共同历史，manual 窗口由 AI 实际选出的 3–5 个用例及适当前后范围给出；证据包括 1d KLine、30m KLine 和 mid 贴近转折。

```python
run = build_chart_run(brief, dry_run=False)
pages = build_big_world_chart_pages(run, run_brief_input=brief, save=True)
board = build_board_run(
    {**brief, "run_id": run.run_id}, reuse_core=True, dry_run=False
)
# 这三次调用不冒称已得到单页综合 URL；页面组合见下一小节。
```

第二接口内部已经创建 overview，不为相同用途再重复调用独立 overview 入口。大尺度先画行情与 mid 贴近转折，不扩展成 N 特征专页或全 U2/U3 图层。菱形大小 20 是原测试样式，不是业务阈值；显示细节可按可读性调整，颜色仍主要区分品种。

**方式二的正式 1d 切片只覆盖各个 manual big 窗口，不覆盖概览显示的全部历史。** 报告的任务 2 只有 282 行日线切片，不能据一张全历史概览图声称已取得全历史正式数据。继续使用方式一的正式日线交付，或通过 aidata 另取所需完整范围，并记录对应 run；不从 Bokeh 图层反向提取数据冒充正式切片。

### 同一平台页面怎样处理

首轮正文和原 probe 的四个 URL，是“一个 overview + 三个独立 big 页面”的历史结果。报告开头随后更正：**已用现有 CAEGraph 的四个 PlotSet 组合成单页，并改为 mid，无需改源码。** 因此不再把首轮末尾提出的 aidata 源码改造方案当作当前待办。

本次附件没有包含更正所引用的 `mid_combined_revision/补充测试报告.md` 和组合代码。采用方向是复用已经报告成功的现有平台组合，不重新设计服务；执行者从 [测试来源说明](references/aidata_20261027/README.md) 指定的现场位置取得补充代码和实际页面身份，用于本批页面。不得虚构一个新的公开接口、组合选项或补充测试 URL。

正式交付仍须一个页面内包含本批概览和全部用例 30m 图；3 个测试用例的四个 PlotSet 不是永久固定数量。追加/刷新页面按实际支持方式操作，不把“曾组合成功”扩写为“同一 URL 无限追加已经验证”。新窗口需要重新建立适用 core/run 或使用真实支持的更新方式，`reuse_core=True` 不是追加节点接口。保留旧冻结证据；页面组合不改变各图与其数据源的对应。

### 概览上的大尺度节点范围阴影

单页组合须保留概览的节点范围阴影。行情可以复用全范围日线交付，但要标出的范围须来自本批实际 Case 对应的冻结 big 节点，不能沿用只有全历史节点的旧 overview 范围。各阴影须能对应 Case/节点，边界按同一 Context、日历及图坐标口径落到正确位置；核心差异区间、manual 节点范围和显示边距仍分开。

已有代码中，`AidataRunOverviewCAE.layout()` 是在生成概览布局后调用 `_mark_review_scope` 添加范围标记和显隐控件；只抽取 `_register_run_overview_graph` 的 PlotSet 不会自动带走这些后置标记。另有 manual 节点的 `start_uti/end_uti` 实际保存日期字符串的情况，直接用 `_number_or_none` 转数值会跳过该窗口。须按真实字段形态复用已有 Context/日历转换能力，不能按字段名假定是数值、当Unix时间解释，或静默漏画。

这两项已知定位分别可核 [W03组合代码](https://github.com/daowei2026/observe-iterate/blob/1fa38c7a3a084a5a364437b21b6a3041b9ca0738/runs/BI-01-CO-01/artifacts/batch-01/aidata/w03/build_native_combined.py)、[W03冻结节点索引](https://github.com/daowei2026/observe-iterate/blob/1fa38c7a3a084a5a364437b21b6a3041b9ca0738/runs/BI-01-CO-01/artifacts/batch-01/aidata/delivery/bi01_co01_w03_cases_20261028_5e4fa62eaf/manifest/timespan_index.csv)及[对应aidata实现](https://github.com/daowei2026/aidata/blob/f58ea95c358b9ac31659c92b7bc20fe9bf7f8264/big_world_chart.py)。它们是修复依据，不是修复成功证明；实际修复方式按现场能力及工单权限选择，不预设必须新增接口或改造平台。

阴影通过情况按 02 单独实核：交付页面上实际可见、边界和Case对应正确，重新打开及相关缩放/显隐操作后仍正确。修复页面不默认要求重取原行情或改写冻结节点、CSV；所做代码/配置变化和实际验收结果沿原交付记录保存。

## 5. 影响研究的范围与时间含义

| 已知情况 | 实际使用时怎样处理 |
| --- | --- |
| 日期字符串映射为日历边界，报告各窗口未包含结束日的日盘收盘 | 同时记录请求范围与实际首末时间；需要覆盖某日收盘时，在 aidata 支持的边界表达下取数并检查，不能未经核对一律加一天或声称全天已含 |
| 30m 图配置 `extra_time="10h"`，图上有窗口外点 | 区分核心差异区间、manual 冻结/切片窗口、实际显示范围和研究所需范围；需要分析额外点时经 aidata 补正式数据，不能拿显示行数当正式切片行数 |
| 转折的 `x/y` 是实际位置 | 用于历史定位；不能据 x 推断该时点已确认/可知。声称当时能够辨别时，另核确认信息；本次材料未给出可直接照用的确认时间字段 |
| 原始 OHLC 存在空值 | 保留并区分无效行情和有效行情，不填零或拼接不同时刻制造共同走势；2021 起点不自动证明每行无缺失 |
| 图层有展示投影/归一化 | 图数核对比较同源原始值和时间；展示坐标不冒充正式价格或独立证据 |
| `context_ref.start_day/end_day` 在原报告中为 null | 保留实际 OptContext 的 camelCase 输入、窗口索引和实际数据覆盖；不能只靠这两个空字段判无范围，也不为此先改通用序列化层 |

正式数据从 `board.delivery_manifest_path`、`board.feature_slice_stats_path` 和 run 的 `manifest/timespan_index.csv` 定位。原路径形状为 `feature_slices/<node>/symbol/<sym>/<feature_key>/__default__.csv`；实际文件以本次 manifest 为准，不能机械写死测试前缀、节点编号、默认参数组名或行数。

## 6. 已有验证怎样复用，哪些仍须看本次实物

已有报告可支持正式图数链、字段绑定、big-only 和原范围图数一致性的复用，不要求每个用例重新证明全部基础设施。报告和代码原件不自动变成本批通过证据；aidata 精确提交、依赖本地差异及实际环境的适用性仍需对应。

本次发生变化的关键处是 2021 起点、mid 特征和单页组合。随本次正常交付核实际范围/成员、mid 实物与图例、正式切片、同页全部图及概览节点范围阴影；不继承旧 8,031 行、47 个 large 转折或旧 URL 的通过结论。单页补充代码暂未取得只影响相关页面交付，不冻结已经取得可靠日线上的选例和回看研究。

每次结果按 [02](02_OWNER_DELIVERY.md) 给 Owner 看到实际输入、接口调用及页面组合顺序、图内名称、正式数据路径和未解决缺口。程序创建成功、页面真实打开、专业研究成立和 Owner 认可分别说明；测试窗口不是业务发现。

## 7. 结果消费与写权

原签发 Pro 接收 Worker 的数据/图/调用实物，判断是否足够支撑具体研究；管理接收范围仍依真实任务。技术 PASS 不等于专业认可，未实际看图不声称本人看过。

遇到共享服务、认证、注册或部署权限缺口时只限制真正依赖的动作，保留已取得可靠数据上的研究。确有工具缺口才按授权在工具所属仓处理，不能绕过权限、修改全局服务或在观察仓另造数据/绘图平台。
