# 看图与同图数据读取指引

以 `CURRENT_VIEW_VERSION_INDEX.csv`、`TECHNICAL_VALIDATION_SUMMARY.json` 为当前工程事实；完整技术状态见 `WORKER_RETURN.md`。图数存在不等于专业 S3 或管理接收。

## 主 Case 五个 As-Of

| As-Of | 当前真实图 |
| --- | --- |
| 2021-05-06 10:00 | http://192.168.11.40:6244/graph/cae/5781/report |
| 2021-05-07 10:00 | http://192.168.11.40:6244/graph/cae/5782/report |
| 2021-05-11 10:00 | http://192.168.11.40:6244/graph/cae/5783/report |
| 2021-05-14 10:00 | http://192.168.11.40:6244/graph/cae/5784/report |
| 2021-05-18 10:00 | http://192.168.11.40:6244/graph/cae/5785/report |

三品种各用原报价轴，共用原时间轴。页面初始为“当时已知／原结果快照”；“事后完整上下文”另页展示完整后续过程，不能当作当时已知。上方入口选择器保留全部320个视图，索引中可按请求名、C1物理行或时间定位。

每个时间视图的“图层原字段”选择器可打开：R02、N1、N2、N_WORKING_ORIGIN、R03、CASE_C1/CASE_C2/CASE_S/BRIDGE，以及价格、small Zig、mid两轮、C0原行。广域候选默认显示C1原行，另有PAIR/REL/MEM/GATE/OUTSIDE，不赋正式簇身份。

主比较点为图5783。`MAIN_FOCAL_CHECKS.json` 逐项保存原字段检查：hc WorkingSoFar 38 bar、rb Completed 33、i Completed 1；hc/rb事后实际终点虽相同，完成可知代理不同。N当前Working的原Episode及方向另通过N_WORKING_ORIGIN与原引用连接展示，不把R02旧Episode接成N Current。

## 数据与版本

`CURRENT_VIEW_VERSION_INDEX.csv` 每行给出相同run/node、窗口、As-Of、视图参数SHA、当前包SHA和核验方法。每个包中的 `VIEW.json` 为该图确切参数，`SOURCE_BINDING.json` 为原包/成员身份；`plot_view_data_manifest.json` 把每个真实CDS对应到CSV。

`LAYER_DISPLAY_SCOPE_INDEX.csv` 逐层给出当前包/CSV、原成员SHA、窗口/As-Of、known/retrospective显示范围、原可知字段、显式坐标连接和合法空层原因；它与包内VIEW和manifest共同解释该CSV的显示范围。`UNMAPPED_EXACT_LOOKUP_ORIGINAL_KEYS.csv`具名列出固定KLine中无精确匹配的原键，保留缺失，不补时间。

CSV保留全部原列，并附 `_aidata_source_row`（含表头的物理行）、源成员/SHA、视图/As-Of/可见性。`_aidata_plot_*` 只作数值/时间转换或明示的精确显示连接。空值不能按0读；同一源行可能在actual、confirm、known等多个图层重复出现，不能按CSV行数当独立事件数。

原件中的 `source_csv_row` 是另一原字段，不能直接等同上述物理行。主Case的B mid锚点已按rb/hc物理43、i物理83核查；不改写原source_csv_row。

R02表保留源原行中的事后完成可知代理等字段。字段出现在表中不意味着当时已知完成；当时图按原As-Of和可知时钟限制几何端点，原stage_at_cut仍保留。原始自然时间及UTI均未重新解释为另一个Calendar。

`MAIN_R02_15_SAME_CHART_ROWS.csv`、`MAIN_N1_15_SAME_CHART_ROWS.csv`、`MAIN_N2_120_SAME_CHART_ROWS.csv`、`MAIN_R03_15_SAME_CHART_ROWS.csv` 为五cut真实同图源的便捷平铺；`MAIN_R02_AND_N_CURRENT_EPISODE_SOURCE_ALIGNMENT.csv` 保留N起点原引用与方向，方便原Pro对照。

## 历史首项与当前新增层

主控发布在 b7c8780f699bb158593d702d4cd1644831190213 的 MAIN_ASOF_1 是144CSV历史快照，SHA为26bc0ef801e4c7da673b9fdc4805f06c632c173007c583a030b0ed8a01f38e61。之后新增N_WORKING_ORIGIN两个scope形成中间146CSV包（ce68bae86a128a046aa9e33b7b1cb87954792f0ade5fad3c8ea160c36ac660f5）。上述两版均有small Zig status/confirmed的浮点字面UTI未接上整数KLine键的显示缺口；旧检查只核源行，不能作为坐标通过。

当前V3以aidata `e59fd90de5237b8a6756de00e54bdf841832fad4`显式精确整数键连接，源字符串和固定输入不变。当前146CSV包SHA为 `8dd8824509375c57a1f47756d30403bc0fca92a0d6ab38c1ce839b174467f86c`；不可变副本、验证时间和参数指纹见 `CURRENT_MAIN_ASOF_1_VERSION.json`。当前revision 2逐一核对实际绘图坐标。旧两版继续保留为历史快照，不能配当前图冒称覆盖新增层及修正坐标。

## 覆盖与限制

47是请求窗口，展开51个As-Of视图，不是47张图配额或47个机会。全部304 raw候选入口仍保留；205个两成员候选的第三品种只是潜在比较对象，99个三成员候选组外为空，不自动形成分离结论。11个未覆盖C0请求和750条原谓词记录不重分组为机会簇。三个后验挑战明确标识，不倒写为初始盲选。

外层B ZIP来源差异、N/02六条单位元数据限制、R03 Withheld、无正式H1及其他未输出字段，按 `BUSINESS_QUESTIONS.md` 和 `OBSERVATION_SCOPE_AND_LIMITS.md` 保留。Worker只交技术图数与核验事实，由原执行Pro继续S3。
