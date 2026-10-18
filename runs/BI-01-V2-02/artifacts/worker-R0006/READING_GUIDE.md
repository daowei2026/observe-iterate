# 六场景图与同源数据读取

以 CURRENT_NODE_INDEX.csv 的逐项状态、参数指纹及包 SHA 为当前事实。图对应的 CSV 来自本次 aidata 实际 ColumnDataSource，保持 shared_view、非 primary evidence 的合同；固定 ZIP 原件仍是来源。S1_SCENE_SYMBOL_PATH_FACTS 只作 Pro 选窗／核对输入，没有替代 S2 同图导出。

页面上方可以选择本 run 的17个节点。每个场景有 BASE、EVIDENCE；SCN-01另有五个独立 As-Of 子节点。BASE 用于看原始 KLine、small Zig、mid 两轮实际／确认／known 点和原方向。EVIDENCE并列固定包中已有的 C0/N、C1 raw/reference 或 SCN-01参考链；节点名称不是正式 Cluster 身份。

初始标签页“当时已知／原结果快照”使用原可知字段限制图层，时间轴右边界截到 As-Of；“事后完整上下文”另页显示后续。位置是 retrospective selection，不能把后续图形当成当时已知。每个节点的正式观察窗口按工单 chart_start/chart_end，额外 visual context 为0秒；它不是新建 Outcome Horizon。VIEW.json记录确切范围、As-Of及选择来源。

三品种有独立的原报价轴和共同原时间轴。要缩放，先点对应图右侧 **Wheel Zoom** 工具，再用滚轮；拖动使用 **Pan**。图层原字段下拉框可选择原 KLine、mid/Zig、C0 原 turn 的 expected_direction、N及其他已提供的源表。选择“所选实际转折/原expected_direction”可查看选中锚点的原方向和三种时间；known marker的Y只是原确认价，不是该时刻报价。

SCN-01 EVIDENCE 包含五个 As-Of 的原历史表；五个独立子节点各自绑定原cut。R02 anchored member episode和N current single-node working episode必须分开读。例如5月7日i的R02仍保留原Completed段，而N已进入不同Working段。SCN01_R02_VS_N_IDENTITY_ALIGNMENT.csv提供原ref、原progress和物理行。C1 raw `refonly-d7ea0ed7945a722aaa`与完整参考Case `refonly-ad8824a52552d7bffa91`按原turn refs关联，不声明相同正式Cluster Life。

SCN-04/06的i保留原价格路径和第三对象身份，不自动取得成员、可比对象、负例或Separated资格。SCN-05保留i 22:00、rb 22:30、hc 23:00的原转折先后及NOT_IN_EXACT_UTI_C1_RAW标识，没有伪C1/U2层。

每个包内有 VIEW.json、SOURCE_BINDING.json、plot_view_data目录和其manifest。CSV保留全部原列、源成员SHA、含表头的一基物理行 `_aidata_source_row`、node/As-Of/visibility；`_aidata_plot_*`只含明确数值／时间转换和UTI精确显示连接。原 `source_csv_row` 是另一字段，不能直接当物理行。不要将多个scope/图层重复的同一原行当成多个独立事件。

LAYER_SCOPE_AND_SOURCE_INDEX.csv逐层对应源成员、CSV、窗口／As-Of、known字段、坐标连接和合法空层。原件中存在事后完成时间字段不表示当时已知；原字段表保留原件，几何完成端点按原可知边界限制。空OHLC不补零／插值。

R02原报价量、ratio、bar位置数和生命周期分别读。Pro检查CSV的末位浮点写出差异只作1e-14容差核对，S2原字段仍逐字保留固定CSV。没有将其探索归一化列转成正式U3输出。N不是U3。WITHHELD、CalibrationPending、NO_FORMAL_H1、LCC缺失和其他未输出维度没有补算。

本次AI读取结构化数据，不看图像像素。逐页浏览器报告证明实际Canvas绘制、glyph重绘和原生交互，不代表专业S3或G4已完成。B外层ZIP来源差异及N/02已知单位限制见WORKER_RETURN，仍由原Pro／管理判断。公开发布和专业消费由主控负责，Worker只准备本机实物。
