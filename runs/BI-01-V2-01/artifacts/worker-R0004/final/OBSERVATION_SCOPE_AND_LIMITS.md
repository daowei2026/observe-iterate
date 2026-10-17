# 本轮图数的观察范围与边界

- 固定输入原件不改；不运行正式Feature替换，不重算U2/U3。人工窗口按工单与S1清单，不依默认big/mid/small重新选Case。
- 47是请求窗口数，完整Case展开5个AsOf；32个初始候选、3个后验挑战、11个未覆盖C0，加完整Case，共47项请求，映射51个AsOf视图。全部304 raw候选入口另外保留，不被47项替代。
- 初始32个候选按工单指定实际存在分层与边界取样；用户预先提供主Case数值且已预览少数C1行，不宣称盲测。C1物理29/33/34三个挑战明确为后验定向，不能倒写成初始盲选。
- 205个两成员候选显示Universe第三品种；仅待比较，不授予正式可比资格或负例。99个三成员候选组外为空；广域S的NOT_EVALUATED未变为Separated。
- 11个C0请求保持原行；hc 2024不补第12项。750条有方向且actual_uti未被C1覆盖的原C0行只是谓词结果，不称750个机会簇、不重分组。
- 主Case refonly-ad8824a52552d7bffa91 与 raw refonly-d7ea0ed7945a722aaa 仅按三个turn refs观察关联，不声明同一正式Cluster Life。
- 三品种原OHLC/close，独立原报价轴、共同原时间轴。12条空OHLC占位/品种不插值、不填0。mid读本包原ScaleTurnCalendar结果，value1/value2及actual/confirm/occurrence分开。
- 当时已知与事后完整上下文独立标签页。历史原行含未来完成可知时间时保留字段；当时图不提前绘成已知完成端点。原知时钟缺失不补历史provider证明。
- R02旧Episode与N同AsOf的Working不同对象并列。N起点原方向通过N working_episode_ref→C0E start_turn_id→C0T expected_direction的明确原引用连接显示，不新算方向。
- R02价量字段按原报价；efficiency/retained_fraction按原无量纲值；bar_elapsed为本包bar间隔，不是Calendar duration；count/runs是数量。return_to_origin_progress不改成归一化程度。
- R03三个Axis CalibrationPending、quality WITHHELD、NO_FORMAL_H1及LCC未提供均保留。turn density、dwell/recovery时间、跨尺度、U3 recentChange、流动性/容量/成本等未输出，不补算。
- N/02六条已知单位元数据问题保留原文和空值；不将未输出时长标为价格，不填值。B外层身份差异具名留给执行Pro/管理，不擅自解释或改源。
- AI只读取结构化对象/同图CSV，没有观看图像像素，没有调用视觉模型。图数技术核验不代签专业S3、独立审查Gate或全BI01完成。
