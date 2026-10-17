# Worker 真实技术回交

工单：BI01V2-R0004-AIDATA-FIXED-01；run：BI-01-V2-01。

状态：**本工单技术图数交付完成，交原执行 Pro 消费 S3；未签专业／管理／独立审查 Gate，未宣称全 BI01 完成。**

## 当前成果与版本

- 实际 aidata run：`BI01V2_R0004_fixed_20261018_033648`。当前全部图数以 `CURRENT_VIEW_VERSION_INDEX.csv` 为准：320 个真实图节点、320 个同图数据包、33944 个 CSV 图层导出。
- 47 项请求完整保留，展开为 51 个请求 As-Of 视图；全部 304 raw 候选入口、205 个潜在组外、99 个空组外、11 个未覆盖 C0 窗口；750 条未覆盖谓词原行独立保留，不称机会簇。
- 每页有三品种独立原报价轴／共同原时间轴，known 与 retrospective 两页；当前 N Working 原方向通过明确原引用连接展示。无 U2/U3 重算、无正式 Feature 替换、无新指标／归一化。
- `CURRENT_MAIN_ASOF_1_VERSION.json` 与 `FIRST_DELIVERY.md` 提供图5781当前146CSV的不可变副本、完整新hash、窗口／AsOf、代码版本。主控发布b7c8780f的144CSV快照SHA=26bc0ef801e4c7da673b9fdc4805f06c632c173007c583a030b0ed8a01f38e61不覆盖新增原方向层；中间146CSV版本ce68bae86a128a046aa9e33b7b1cb87954792f0ade5fad3c8ea160c36ac660f5也属于历史，未修复small Zig的UTI显示连接。两者保留原件，不能配当前图冒称已覆盖全部当前坐标。详见PUBLICATION_AND_VERSION_BOUNDARY.json、INTEGER_LOOKUP_DISPLAY_CORRECTION.json及当前索引。

## 实际核验

- 本地真实aidata consumer对全部320视图逐层核对象、显式范围／AsOf、原物理行选择、全部源列原值，并将每个实际绘图坐标与原字段及显式连接独立比对；三品种独立Y轴／共同X轴、未来隔离、原价不归一化、空值不补零／插值均通过；全部页面实际HTTP 200。
- 对47项请求展开的51个AsOf，额外实际拉取Bokeh会话，并对会话反序列化后的真实对象和源行再次核查。其余269个全候选视图使用实际本地消费者的批量结构化断言及HTTP检查；不冒称全部320均单独打开Bokeh会话，不声称AI看过图像像素。
- 全部320包实际hash／ZIP CRC／CSV数量／VIEW参数指纹一致；对应验证原件在`validation/`。
- `LAYER_DISPLAY_SCOPE_INDEX.csv`逐层绑定当前包／CSV、原成员、原列、窗口／AsOf、可见性、显示转换和合法空层原因。`UNMAPPED_EXACT_LOOKUP_ORIGINAL_KEYS.csv`列出0处原键在固定KLine中没有精确匹配的坐标（含重复scope／窗口），保留缺失且不插值；这不是读取失败或已补出的坐标。
- 五个主Case当前图：5781、5782、5783、5784、5785。`MAIN_FOCAL_CHECKS.json`／平铺同图CSV保留R02物理2–16、N/01 15行、N/02 120行、R03 15行及N当前起点方向。5月11日10:00原字段：hc WorkingSoFar 38 bar、rb Completed 33、i Completed 1；hc完整终点在当时图保持未完成可知。actual/confirm/occurrence三时钟及N另一个Working Episode均已具名核查，没有暗接成同一Current。
- 43项回归全部通过。NaN列表Bokeh JSON传输故障及浮点字面UTI对整数KLine键的显示连接缺口均已修通；显式整数键用Decimal精确连接，不截断非整数，原字段不改。旧检查只核源行、漏了该坐标缺口的事实保留；当前revision 2已对全部绘图坐标实际比对，不用旧检查冒称通过。label修正同样有记录，未改窗口／AsOf／源结果。

## 代码与输入

- aidata独立分支`codex/bi01v2-r0004-fixed-input`，当前commit `e59fd90de5237b8a6756de00e54bdf841832fad4`，包含初始428c70f与后续整数显示键修复，tracked状态干净；受保护main仍是`9ff7ce4929b36945f63b1c9875e59f68141f997a`。当前图实际回用同一提交内容；两份patch随本回交提供。没有在observe/cgpterm另建绘图引擎，未对observe共享工作树commit/push。
- 工单及5份输入／规范的6个本地原件逐字节匹配指定Git blob。两包40个成员（38 CSV+2元数据）SHA／行数全部匹配；实际数据从指定资金管理目录只读取得。详见`ORDER_SOURCE_VERSION_BINDING.json`和`FIXED_INPUT_BINDING.json`。

## 全部未完与业务待决

- **本工单技术未完：0**，`PENDING_TECHNICAL_ITEMS.csv`为有表头的合法空表。
- **来源资格待原Pro／管理判断**：实际B ZIP外层SHA为历史ff3215，与Pro消费4fd1af不同，但所有成员匹配；原因保留未知，不换源、不展开重验算。
- **既有N/02单位限制**：六条空business_duration/normalized_amplitude仍保留原per_symbol_raw_quote元数据；只显示限制，不赋时长价格单位，不填值。
- R03 CalibrationPending／WITHHELD、NO_FORMAL_H1、LCC未提供及其他未输出维度均原样保留；专业S3、来源资格、管理接收不属于Worker代签范围。详见`BUSINESS_QUESTIONS.md`和`OBSERVATION_SCOPE_AND_LIMITS.md`。

## 合法回用与接续

Trier现于`http://192.168.11.40:6244`承载，Bokeh端口5006也须可达；主控将本目录可公开图数／文档发布到本run artifacts。私有日志、设备或凭据不进入发布包。

使用指定aidata分支／提交和当前run目录，人的图／AI数据按当前索引配套读取。已发布144CSV历史包不配当前新增层使用；若后续再调整源层／代码，必须新记图数版本和hash。

真实有限脚本在aidata gitignored `test_runs/bi01-v2-r0004/`，状态CLI任务`bi01v2-r0004-aidata-fixed-01`，state-dir位于BASE的`.runtime/bi01-v2-r0004/task-status`。未启动后台轮询／守护，不接旧Goal；不操作手机、不发送Pro消息。当前环境未暴露send_message_to_thread，主控从本目录及本聊天读取回交，按原角色机制原样交执行Pro。后续业务判断请由原Pro签发，不在此自造业务延续。
