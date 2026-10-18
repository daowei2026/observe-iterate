# V2 S2：先基础行情图，再有目的展示 U2/U3 与同范围数据

## 1. 本次先看什么、已有什么

本轮 **rb/i/hc 的两份固定 ZIP 是既定输入**，不是未来“若被采用”的候选；数据身份、来源路径、23 个下游 CSV 和 15 个上游 CSV 见 [05 固定数据](05_BI01_FIXED_INPUT_DATA.md)，原 I1–I3 业务背景见 [04](04_BI01_BUSINESS_BASELINE.md)。

S2 先根据 [00 业务问题](00_PURPOSE_AND_THREE_STEP_FLOW.md) 和 [07 业务场景方法](07_BUSINESS_SCENE_OBSERVATION_METHOD.md)，**先用上游 K 线、Zig 和 mid 贴近转折等基础行情图/同源数据**辅助专业 Agent 发现有研究价值的位置；再为这些场景展示 U2 识别位置、成员/组外如何对应当时走势与转折，以及 U3 四方面在合法 As-Of 的真实可用字段、后续结果与未产出情况。不要由 U2 raw 候选或 aidata 默认 big/mid/small 搜索反向决定全部业务 Case，不预先划分场景类别。

**正常处理：直接读取固定数据并画图。** 不是先找有没有正式 Feature，不是要求 Worker 重新计算 U2/U3，也不把“缺完整 Runner”当作必须从头验算的理由。若某项预先验算本身疑似错误，标出准确字段/窗口和影响，向有权角色反馈；未经决定不改数据原件。

## 2. 统一工具及现有接口

`daowei2026/aidata` 是统一图、图层数据、观察窗口与切片工具。**当前希望尽量不修改 aidata**，不在 observe-iterate/cgpterm 中另外做一套 matplotlib/Bokeh 绘图、CSV 特征切片或专用图工作台。

实际使用前按当前锁定的 aidata 版本核其：
- `README.md`、`OWNER_INTENT_AND_RATIONALE.md`、`TODO.md`；
- `docs/DEVELOPMENT_GUIDE.md`、`docs/RUN_BRIEF_INPUT_CONTRACT.md` 及真实使用 API；
- 已知 `build_chart_run`、`build_big_world_chart_pages`、`build_board_run(...,reuse_core=True)`、`build_chart_review_requests`、`render_review_nodes`、`export_plot_view_data` 等接口的真实支持范围。

同一 `run_id/node_id/timespan`、合法 As-Of 用于人的图和给 AI 的对应数据；图上额外 `extra_time` 只作视觉上下文，不能在证据上默许替换正式窗口。回顾性选择位置与当时已知 Current/后来 Outcome 分开，不能借未来显示信息声称提前辨别。主证据与 `plot_view_data` 展示层区分，图链接和实际可打开状态须核对。

目前已知 aidata 正常主证据路径主要消费 `Feature.rerun().to_df()/to_dfs()`，**不能由此推断它能直接读任意 ZIP/CSV**，更不能为了让 API 工作而改成对业务 Feature 现场重算。本轮先寻找现成的只读固定结果接入方式。

## 2.1 执行 Codex 的 aidata 工作区

执行 Codex 当前可使用的工作区是 `/dwdhome/fy/BASE_E6_2`。两份固定 ZIP 的**当前数据目录**是 `/dwdhome/fy/资金管理`（不同于工作区）。Owner 已确认 aidata 的基础运行检查完成，**无需重新设置一套环境预检流程**。S2 直接从固定数据目录取本轮原件，按已锁定版本的 aidata 和已确认的工作环境执行，正常记录真实命令、配置及图数据产物。不要把原数据复制后的副本或临时渲染目录当成新的正式数据源。

旧 `BI-01-V2-01` 已产生的约 320 张图/包及同源数据可在逐项核实输入、版本、窗口和实际浏览器可见后用于本轮技术观察，**不继承旧 S1 选样或专业结论**，也不因此重新批量出图。旧图曾遇 BokehJS `DataTable` 注册错误；Trier 独立修复分支 `codex/bi01-v2-chart-render-fix-20261018` 的 `adea9b46ce4016045eee714121f7a322924e14a3` 曾现场修复并核四张代表图，不能由此声称全部图页或未来服务重启后都通过。需要使用的图必须实际核浏览器 K 线/图层可见，不能以 HTTP 200 代替。

## 3. 本轮 AI 不视觉看图

**本轮不让 AI 看渲染图片；没有视觉模型调用要求。** aidata 尚不支持这里想要的“向专业模型发送渲染图像”的完整链，本轮不因此建设、测试或改造视觉能力。

- 人/Owner：用 aidata 页面直接查看真实行情与特征图。
- AI/执行 Pro：读取与该图同源、同窗口的实际 CSV、图层可见数据、必要图注/标记时间，并用数据核验推理。
- 数据确实被 AI 取得才能声称“基于图的对应数据完成观察”；**不能说“AI 看过图”**。无法证明输入被读取时如实标记该观察尚缺输入。
- 未来需要真正的模型视觉看图时，另作为新需求评估，不属于此 V2 当前启动阻断、必做事项或 aidata 欠账。

## 4. 使用中的修复优先级与改动保护

1. **优先只读使用 aidata**：合理配置 `run_brief`、人工观察窗口、既有 Feature 展示能力及必要 Export；先核实际效果再判断是否真有工具缺口。
2. 有 CSV/Feature 接口问题时先准确确认它是否已经被 `TODO.md` 记载、是否存在低成本的 **现成** 接入途径，避免为本任务提前大改工具。
3. **如果确实需要修改/新增 aidata 通用能力：必须在 `daowei2026/aidata` 另建独立工作分支后施工、测试与提审；绝不能直接提交到 aidata 当前 `main` 或 CYF 现有使用分支。也就是说，确有必要时只能在 aidata 的全新独立分支修改。** 新分支基于当时实际锁定 commit；说明改动缘由、影响、真实回归测试与回用方式，避免未经验证合并进他人工作。
4. 相关变化仍属于 aidata 工具代码，不落在 observe-iterate 形成第二套制图实现。专业任务不因临时工具改动丢失 U2/U3 业务目标；确实无法获得合法可视化时准确提交阻断与恢复条件。

## 5. 一次实际 S2 输出要看得见

按真实观察问题，交：固定两份 ZIP 的读取/绑定和已知差异、aidata 精确版本及 run/node/timespan、实际可打开的图、同源数据与字段来源、U2/U3 图层是否真实显示、Owner 读图定位指引、AI 实际读取了哪些数据、未解决的具体问题。

先交可识别市场过程的基础图、选中位置理由，再交该位置 U2/U3 的有目的叠加；实际浏览器效果与业务分析是否完成分别核验。

不以“图已创建链接”冒充 Bokeh 图层真实渲染，也不以“导出了 CSV”冒充业务设计结论。工作可选择首张有业务价值的图尽快试用，但不得缩成只完成一个局部 Case。
