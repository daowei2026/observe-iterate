# D010 / C0023｜CAEGraph 展示方式准备回交

本项原 C 阶段完成，原生阶段状态为“完整”。C1 信息清单、C2A 直接阅读及能力核实、首版与当前可打开 HTML、真实复杂点迭代、C3 具体可注入代码和合同齐备。当前唯一预期为 `C2_CURRENT_EXPECTATION.json` / `html/current.html`（F800-C2-v4）。这只是展示准备；D 正式实例/位置/字段绑定、E 最终图与正式数据及适用 S1/S2 留原 manager 依既有流程签发。

准确派工为 `daowei2026/observe-iterate@a33dc91d08a4e888d08af71b6a1769a0db06ae8a:longrun/runs/OI-F800-STAT-20261122-01/delegations/D010/DELEGATION.json`，C0023 INVOCATION 为 `ef32a9bed08ad7396b8b91cf0a71330b22ee9103` 原件。49 个精确来源本地 Git 对象及字节核准；D/I/原 CAEGraph 手册再经 GitHub 原件核同，见 SOURCE_REF_AUDIT、REMOTE_DISPATCH_READBACK。按原 C Skill/WORKFLOW/IO_SPEC `87b951bbd15078a2d6353bdd24afe0d8f19c845c` 及适用 Owner MP002 原文/最新 Binding 执行；workers=[]，没有新线程或其他聊天消息。

当前输入复用 D008 的 FRP `39f02ec4548e68ba8dbd30061afc870546000994`、TIS `2f460d663d821cf2ba25555eda13e78b697d0767`、配置 SHA-256 `b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3`。已接受的 U/X/G 和 D009 B 不重做，U 的 PARTIAL 不升级。四项场景问题、七个 candidate-only 来源和原 B 的 rb/hc/i 5m、2021—2023 三年位置保持，C 没有挑正式场景或冻结业务预期。INPUT_BINDING、SOURCE_RETENTION 记录这些边界。

C1 的 12 项信息按业务主输出和形成关系选择，不按 31 张公开表机械铺图。保留原价、已暴露 Rct、ScaleTurn 实际/几何确认/上游被选已知、每个 exact 候选修订、成员/引用、Required 及独立依据/观察/覆盖/形成关闭/责任关闭。逐 tick 材料准入、失败组合、first blocker 和原生 coverage 区间仍 NOT_EXPOSED，不补造曲线、原生字段或完整分母。详见 C1_INFORMATION_LIST。

亲自阅读锁定 `daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:CAEGraph使用手册.md` 的说明、术语、CAEGraph/PlotSet、布局/绘图快速选择、候选类、相近示例及类关系，并查同版 utlv2/utkv2/pfw/pdt。手册 60101 字节，SHA-256 `f7dd1061a2b170ec4cfb0a508afd737e195e7ec16db269e5655b63dc06591c19`。本机原 uplot 是其他版本且有原有未提交修改，所以使用隔离、逐文件核哈希的精确源码快照；未改原 uplot、未新增 uplot API。C2A_MANUAL_READING、UPLOT_SOURCE_SNAPSHOT 给出证据。

首版 `html/first.html` 已实际打开并看图：输出数据源 3 条可见修订因同刻同依据叠成 2 个分离点；编码纵轴难辨身份；6 条合成样例的后 3 条位于首版视区外。C2C_FIRST_REVIEW 与 BROWSER_v1、截图保留原状。随后真实迭代到逐品种原价/T/C、上游已知附图、跨品种稀疏修订/携带窗口以及 exact 原值明细。每轮同步代码与 HTML 后再看图。v2 的图例带首品种前缀；v3 去前缀时裸字符串被 Bokeh 当字段，产生 3 条 Invalid field 错误。该版没有被接受；v4 按 Bokeh 原实现使用文字值包装并同步选择控件，问题关闭。round1/round2 HTML、各轮浏览器记录与截图保留；独立 v3 源快照没有保留，未声称其存在。

当前实际浏览器 Bokeh 3.6.0 中，5 个图共享同一 x_range；6 条合成修订分别成行。同刻 A-r2/B-r1 保留独立坐标。真实下拉选择第 3 行后，图点、明细和控件均为 SYN-Life-B / SYN-B-r1。浏览器 console 为空，外部请求为 0。见 BROWSER_v4、screenshots/current-selected.png。价格不标准化，显示行/round 偏移及区间裁剪均明示；窗口段仅是当次修订携带的 a/d/r，不是逐 tick 状态或覆盖轨迹。精确关系采用完整明细，未承诺全图关系拓扑或自动跨来源高亮。

C2 使用全合成业务值和 SYN 身份，日历只读借用 SOF；没有读取真实 K 线/转折/候选作预览，也没有把 B 全范围正式绑定。PREVIEW_BINDING_v4 记录样例范围 2022-06-15—2022-07-07、每品种 1148 条合成价格行和 6 条合成修订。该样例只验证显示表达，不能作为 F 可执行输出、市场合理性或正式案例预期。

C3 为 `display_code/caegraph_display.py`，SHA-256 `e5d6a235cd23f7e90ebbd8f020768f7e91b81ffd1782fc824362543c0f696ec0`，与生成当前 HTML 的 v4 实现字节一致。`current_impl.py` 重导出同一实现，没有另生成第二份预期 HTML。代码实际调用 CAEGraph、PlotSet、PerSymFigs、AllSymsFig、KPriceLine、MulFieldsGlyphs、MulSegPlot，并通过原生 CDS 和既有 Bokeh hover/table/div 组合精确明细；只读 DataFrame 入口的 rerun 不进入真实 Feature/生产。

`build_display(*, instance, reader, context, position, fields, caption)` 的实例、数据入口、SOF/context、品种/时间/日历及字段映射均由 D 注入。C3 无真实外层实例、结果目录、运行状态或 B 最终位置硬编码。多位置/尺度由 D 对每个批准位置调用同一入口。INJECTION_CONTRACT 和 FIELD_MAP_TEMPLATE 说明真实绑定时的父键、原生字段/枚举、UUID 表示、round 显示编码及空值处理。模板是形状说明，不是 D 已完成的正式绑定。

CODE_VALIDATION 的 15 项检查通过：必要接口与无最终绑定字面值、uint64 UUID 无损及浮点 ID 拒绝、当前公开 Schema/首行身份形状、单品种/整型 UTI/字段全面改名后的原生内存模型、同刻父组不合并、全部成员子坐标、NaN 保留、显示裁剪原值保留、空输出和重复父键拒绝、浏览器及 C2/C3 字节一致。C3 检查只建内存模型，不产生新 HTML，不代 E 取正式数据。

当前无未解决的工具能力缺口；原 U/数据不可暴露限制照常传递，见 CAEGRAPH_CAPABILITY_GAPS。未运行正式 Feature、未重跑 G、未修改/采用 F 源码行为，未运行或释放 Q/V、未改 WALL M001。此 D 仅分析及 Run 记录写入，不申请或声称持有重型生产 flock。

专业结果先提交并远端核验，随后独立发布 C0023 原 V2 PRO_RETURN。原 manager 消费前，不声称对方已验收或父 Run 完成；不签 D 完整定义、E 最终图、ObservationMaterialPackage DATA_READY、正式场景预期或 FeatureReleaseGate/ReleasePackage。原 gate/schema 不改，已知完整 CLI 对 Codex manager 的兼容边界在 VALIDATION.md 与 Return 校验记录如实保留。
