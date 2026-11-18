# U2 F/Q/V 观察数据准备与 CAEGraph 讨论

归档日期：2026-11-17（北京时间）。来源为 Owner 按上传顺序提供的同一新聊天的三份粘贴文本，每份各含一轮问答，共第 1～3 轮。标题按内容拟定，原聊天链接未提供。

第 1 轮按原文时间行另列 24 小时制时间，源文未注明时区。第 2、3 轮未提供对话时间。可见的思考耗时、代码片段、原有排版和附件名照录。整理时统一换行，去掉问答边界的空白行及第一份文本末尾的孤立短横线。

第 2 轮提到的 `fqv_caegraph_definition.py` 仅提供了附件名与回复中的代码片段，“完整代码”后未附可用链接；本次归档保留这些可见内容。完整 Python 附件未随粘贴文本提供。

本文件保存 discussion provenance。正文中的 AI 判断、资料状态、执行回交及后续建议按原对话记录，正式采用以 Owner 明确决定和对应正式文档／实现为准。

## 第 1 轮

### 问：

2026-11-17 14:32，by: 樊月（源文署名：fy；时区未注明）。

- November 17th 202602:32 PM; by : fy  继续执行第4步

### 回答：

思考了 7m 49s




第 4 步执行结果：落地设计
一、结论
本轮已经完成“优先既有图和代码，再按最小增量扩展”的调查与设计。

最终决定是：
不改 F/Q/V 正式输出合同，不重新生产全期特征，不先建设新的 CAEGraph。先复用现有正式读口、已有 F 真实叠图结构和已导出的 F/Q/V 全表，增加一层临时的“候选中心取材与联图适配”。

原因是：
1. 仓库里已有一张真实 F 候选叠图和对应取材代码；
2. 当前 TIS 已分别提供 F、Q、V 的公开观察适配入口；
3. 当前已有完整 F/Q/V 正式表和精确引用映射；
4. 但没有找到一张已经可直接修改参数就能得到的 新版 F/Q/V 完整联图；
5. 当前 实例运行脚本.py 只读取少量常用表，不能直接承担步骤 3 规划的全部观察材料。
因此，第 4 步不是“把某个现成 Notebook 的参数换一下”，而是需要一个最小临时数据适配和展示层。
二、已有资产调查与采用决定
2.1 已有真实 F 叠图：可以复用展示骨架，不能原样复跑
仓库里已有一份 F 的真实结果观察代码：

ENGINEER_FIRST_FEATURE_R05/evidence/reasonableness.py

它已经完成过：
- 调用公开 candidate_overlay()；
- 读取三品种原行情；
- 三个品种使用独立价格轴；
- 标出 selected P/T/C；
- 标出 Source confirmation；
- 标出候选 knowledge；
- 生成 REAL_CANDIDATE_OVERLAY.png。
对应说明明确写着，这张图使用三个独立价格轴，并将 P、T、C、Source 确认和候选知识位置分别标出。
可以复用的部分
- 三品种上下排列、时间轴对齐；
- 各品种独立价格轴；
- Turn 的 P/T/C 标点；
- actual 与 confirmation/knowledge 分开；
- 候选成员高亮；
- 图形背后保留准确 F 记录引用。
不能原样复用的部分
旧代码使用的是：
U2MainlineKLineInput
+ MapKLineOpenData
+ open_uti

而当前新版 F/Q/V 使用的是：
正常 KLine
+ close
+ closeUti
+ 当前 ScaleTurnCalendar 接线

所以旧脚本只能复用图的结构、字段对应思想和局部展示方式，不能继续沿用旧输入入口或 open_uti 横轴。

这是第 4 步最重要的实现边界之一。
2.2 F、Q、V 已经有可复用的公开观察入口
当前 TIS 已提供三个薄观察接口：
特征	已有入口	实际返回
F	candidate_overlay()	F 主发生和候选成员
Q	directional_organization_overlay()	Q 主发生和逐成员方向组织
V	validity_overlay()	V 主发生、逐成员判断和原因


F 的现有代码实际调用 candidate_overlay() 并核对主表与成员表。

Q 的公开入口返回 occurrences 与 occurrences_organizationMembers。

V 的公开入口包含主结果、成员和原因；现有接收材料也明确记录 validity_overlay 已接通。
采用结论
这些入口适合用作第一层主表取材，但不能只使用它们，因为它们没有一次性返回：
- F 的 Pair Required、距离、overlap、previous；
- Q 的六量、端点、后继、previous、DutyEnd；
- V 的 previous、DutyEnd、负向或零推进值、实际后继；
- F→Q→V 精确引用映射；
- 原始 KLine 和同窗口全部 Turn。
所以落地时：
overlay() 负责主表和主要成员
to_dfs([...]) 负责必要子表
EXACT_REFERENCE_MAP.json 负责跨特征精确连接
KLine / ScaleTurn 读口负责行情和未入组转折

2.3 已有正式结果包：优先复用，不先重跑
当前已有结果包中保存：
- F：97 条主发生；
- Q：286 条主发生；
- V：318 条主发生；
- F、Q、V 的全部公开薄表；
- Q→F 286 项精确映射；
- V→F、V→Q 各 318 项精确映射。
现有读取指南还明确：
- 不能用相同 occurrence 作为不同特征之间的连接键；
- 必须沿实际 Life/Revision 引用连接；
- 当前导出没有新增完整原行情价样；
- 需要具体价样时要另取真实来源。
采用结论
第一轮观察优先使用这批已导出的正式结果，不先调用：
f.rerun(2)q.rerun(2)v.rerun(2)


只有以下情形才讨论重新运行：
- 当前正式物理根确实不可读；
- 现有导出缺少某项必须字段；
- 需要的真实 Case 不在现有导出范围；
- 已确认源码或配置已经改变，原结果不再对应当前分析对象。
2.4 现有完整 CAEGraph 情况
本轮在以下仓库的默认分支，以 F/Q/V 类名、overlay 方法、FQV、候选组等关键词进行了搜索：
- viewer
- uplot
- observe-iterate
- feature-refinement-implementation-agent-evolution
- tis
目前找到的是：
- 旧版 F 的静态真实叠图；
- F/Q/V 的 Python 数据读取适配；
- F/Q/V 正式 CSV 导出；
- 没有找到已完成的新版 F/Q/V 完整 CAEGraph 或 Notebook。
因此不能走“只改现有图参数”的路径。
三、确定的落地形态
3.1 总体结构
现有正式 F/Q/V 结果
+ EXACT_REFERENCE_MAP
+ 同窗口真实 5m KLine
+ 同窗口全部 ScaleTurn
        │
        ▼
候选中心临时取材器
        │
        ├─ 统一身份
        ├─ 精确 F→Q→V 连接
        ├─ actual / confirm / known / publication 分离
        ├─ 原值与显示值分离
        └─ 局部 Case 窗口裁剪
        │
        ├──────────────┐
        ▼              ▼
纯数据包          联图视图
CSV / JSON       HTML / 静态预览

它不是新 Feature，也不参与正式产品保存。
3.2 临时工作目录建议
第 5 步执行时使用本地临时目录，不提交仓库：
.runtime/u2-fqv-observation/
├── prepare_fqv_case.py
├── render_fqv_case.py
├── cases/
│   ├── case-01/
│   │   ├── manifest.json
│   │   ├── kline.csv
│   │   ├── turns.csv
│   │   ├── f_occurrences.csv
│   │   ├── f_members.csv
│   │   ├── f_required.csv
│   │   ├── f_relations.csv
│   │   ├── q_occurrences.csv
│   │   ├── q_members.csv
│   │   ├── q_quantities.csv
│   │   ├── q_endpoints.csv
│   │   ├── v_occurrences.csv
│   │   ├── v_members.csv
│   │   ├── v_reasons.csv
│   │   ├── reference_index.json
│   │   ├── overview.html
│   │   └── overview.png
│   └── case-02/
└── run_report.json

这里的脚本只做特征之后的观察取材，不重写 F/Q/V 算法。
四、数据适配的具体设计
4.1 F 层
直接复用
f.candidate_overlay()


用于取得：
- occurrences
- occurrences_groupMembers
追加读取
f.to_dfs([    "occurrences_groupMembers_memberP",    "occurrences_groupMembers_memberClock",    "occurrences_groupMembers_memberP_pointClock",    "occurrences_groupMembers_memberT_pointClock",    "occurrences_groupMembers_memberC_pointClock",    "occurrences_groupRequired",    "occurrences_groupRequired_pairDistance",    "occurrences_groupOverlaps",    "occurrences_groupPrevious",])


现有正式包已经证明这些主要表存在，例如：
- F 成员 221 行；
- Pair Required 151 行；
- overlap 13 行；
- previous 62 行。
取材结果
形成一份候选级表：
字段组	作用
F Life/Revision	候选身份
member object + Turn Life/Revision	候选成员身份
actual / confirmation / known	多时间角色
P/T/C actual、price、Clock	局部转折几何
Pair 的四项 Required	为什么成组或未决
pairDistance	实际时间距离
overlap / previous	候选间关系与演化


4.2 Q 层
直接复用
q.directional_organization_overlay()


用于取得：
- Q 主发生；
- 逐成员 verdict、completion、used Turn。
追加读取
q.to_dfs([    "occurrences_organizationMembers_organizationQuantities",    "occurrences_organizationMembers_organizationQuantities_motionNumber",    "occurrences_organizationMembers_organizationEndpoint",    "occurrences_organizationMembers_organizationEndpoint_endpointPrice",    "occurrences_organizationMembers_organizationEndpoint_endpointClock",    "occurrences_organizationMembers_organizationSuccessor",    "occurrences_organizationMembers_organizationSuccessor_motionClock",    "occurrences_organizationMembers_organizationAskedTurn_motionClock",    "occurrences_organizationMembers_organizationUsedTurn_motionClock",    "occurrences_organizationPrevious",    "duty_ends",])


现有正式包中，Q 已有：
- 656 条成员；
- 3936 条六量可用性记录；
- 103 条真实后继；
- 251 条 previous；
- 35 条 DutyEnd。
取材结果
逐成员形成：
asked Turn
used Turn
endpoint
actual successor
P / A / D / L / E / C
availability
verdict
working / completed
observedThrough
knownFrom

Q 六量保持原值，不重新计算成另一个“观察版运动质量”。
4.3 V 层
直接复用
v.validity_overlay()


用于取得：
- V 主状态；
- 成员判断；
- reason。
追加读取
v.to_dfs([    "occurrences_validityRecordPrevious",    "occurrences_validityDutyEnd",    "occurrences_validityMembers_validityActualSuccessor",    "occurrences_validityMembers_validityActualSuccessor_motionClock",    "occurrences_validityMembers_validityNegativeOrZero",])


现有正式包中，V 已有：
- 731 条成员；
- 501 条原因；
- 283 条 previous；
- 35 条 DutyEnd。
取材结果
V 不再新算一套值，只恢复：
V Life / Revision
准确 F exact
准确 Q exact
result
formation basis / observation
qualification
member verdict
reason
previous
duty end

4.4 跨特征连接
唯一允许的主连接是：
Q.organizationCandidate → F exact
V.validityFormation     → F exact
V.validityOrganization  → Q exact

实现中优先直接读取：
EXACT_REFERENCE_MAP.json

不得使用：
timestamp 相同
occurrence 编号相同
成员集合相同

作为替代连接。

这些引用映射在当前结果包中已经完整提供。
五、原行情与 Turn 的落地设计
5.1 KLine
现有 F/Q/V 导出包不包含完整价格路径，因此步骤 5 必须另取：
rb 5m KLine
hc 5m KLine
i  5m KLine

采用当前正常配置：
SOF       = TA_updto20240229_DBA
calendar  = night_end_at_2300
freq      = 5m
symbols   = rb, hc, i

重要决定
- 使用当前 KLine(close, closeUti)；
- 不复用旧图代码的 MapKLineOpenData/open_uti；
- 不从 Q 的 P/A/D/L/E/C 反推完整价格路径；
- 每个品种保留独立原价轴。
当前准确 KLine 读取调用在第 5 步运行环境中定向核实；第 4 步不凭旧代码猜一个新入口。
5.2 同窗口全部 Turn
F 成员表只能提供已经进入候选的 Turn。

为了回答：
为什么某个 Turn 没进入现有候选，而是形成另一个候选或没有候选？

还需要在同一窗口内取得：
- rb 全部 ScaleTurn；
- hc 全部 ScaleTurn；
- i 全部 ScaleTurn；
- 包括未进入当前 F 候选的 Turn。
采用方式
优先读取当前 F 的正常 ScaleTurn 上游输出；不修改 F 正式保存合同，不要求 F 新增“所有未入组 Turn”字段。

如果正式上游难以独立读取，则本轮最低替代是：
- 先完成 F/Q/V 已有成员的观察；
- 把“未入组 Turn 原因”标为证据不足；
- 不从候选成员表反推不存在其他 Turn。
六、联图设计
6.1 主页面
面板 1：rb 原价 KLine
面板 2：hc 原价 KLine
面板 3：i  原价 KLine
面板 4：F Candidate
面板 5：Q Member Organization
面板 6：V Validity
面板 7：精确记录和原因明细

6.2 KLine 和 Turn 图层
每个品种：
- 原价 KLine；
- 全部附近 Turn 浅色标记；
- 当前 F 成员 Turn 高亮；
- P/T/C 使用不同符号；
- actual 画在实际位置；
- confirmation/known 使用另一标记或连线；
- 不将 actual 和 known 合成一个时间。
这里复用已有 F 叠图的三独立价格轴结构。旧图已经证明这一结构可表达 P/T/C、confirmation 和 group knowledge。
6.3 F 图层
每个 F Life 一条轨道，显示：
- 成员集合；
- Supported / Incomplete / Contradicted；
- Open / ClosedSupported / ...；
- Pair 的时间、方向、类型、弯折四项；
- overlap、covered-by、previous；
- candidate publication。
F 的四项 Required 采用并列显示，不做雷达图，不合成总分。
6.4 Q 图层
每个成员一条轨道，显示：
- verdict；
- working/completed；
- used Turn；
- endpoint；
- successor；
- P/A/D/L/E/C；
- quantity availability；
- Q publication 和 DutyEnd。
默认只在选中成员时展开六量，避免把 3936 条数量记录全部铺在主图。
6.5 V 图层
采用离散状态点：
Pending
Invalid
AcceptedWorking
AcceptedCompleted
ValidityConflict
SubjectNotApplicable

点击某次 V 变化时，显示：
- 准确 F exact；
- 准确 Q exact；
- formation basis；
- qualification；
- reason；
- member verdict；
- previous；
- duty end。
状态带边界
主证据仍是离散发生点。

若为了阅读生成“保持到下一状态”的状态带，该状态带必须标记为：
derived display state

并满足：
- 同一 V Life；
- previous 链连续；
- 到 DutyEnd 停止；
- 空白不能自动填成 Invalid。
七、可选局部相对价格视图
为了比较三个品种转折后是否同向，可以附加：
relative_price = price / used_turn_price - 1


但只作为辅助图：
- 每个品种使用自己的 used Turn；
- 不跨候选复用基准；
- 不替代原价；
- 不替代 Q 的 ProgressP；
- 不替代 PathLengthL 或 EfficiencyE；
- 基准对应准确 Turn Revision。
这属于 S4 的有条件使用，不进入首轮主证据。
八、首批 Case 的实际落地顺序
Case 1：同一候选多状态变化
优先使用已经明确的：
2016-03-08
hc / rb
DirectionUp
Pending
→ Invalid
→ AcceptedWorking
→ Invalid

这一个 Case 可以同时观察：
- F 候选为何形成；
- Q 某成员为何从支持变反向再恢复；
- V 为什么等待 F 收口；
- Working 与 Completed 的差别；
- DutyEnd 后为什么不能继续延展状态。
Case 2：重叠候选
按确定性规则选择：
F 时间顺序中第一条 overlap 非空、成员及 Pair Required 完整、原 KLine 可读的候选。

用于观察：
- complete-link 分组；
- AB、BC、ABC 等重叠结构；
- 较大候选与较小候选的关系；
- “重叠备选”是否在行情中具有可理解意义。
不按未来涨得好不好选择 Case。
九、最小代码增量决定
不修改
- FRP F/Q/V；
- TIS 正式输出字段；
- F/Q/V writer；
- 正式存储布局；
- 当前 fqv_kline_example.py；
- 现有完整参数；
- 现有 实例运行脚本.py 的通用职责。
临时新增
第 5 步在本地临时目录新增：
prepare_fqv_case.py
职责：
- 读取既存正式表；
- 读取精确引用映射；
- 选择 Case；
- 读取局部 KLine/Turn；
- 建立统一 Case 数据包；
- 记录来源和缺失。
render_fqv_case.py
职责：
- 读取 Case 数据包；
- 生成联图；
- 提供记录明细回指；
- 生成静态预览；
- 不重新计算 F/Q/V。
这样比把所有逻辑塞进 实例运行脚本.py 更清楚，也避免把观察专用逻辑变成正式运行入口。
十、第 4 步完成状态
已完成
- 已调查现有完整图和相关代码；
- 已确认旧 F 真实叠图可以复用展示结构；
- 已确认 F/Q/V 公开观察入口；
- 已确认现有正式结果包和精确引用映射；
- 已确定 KLine、Turn、F、Q、V 的数据拼接方式；
- 已确定联图面板、身份、时间和显示规则；
- 已确定首批两个 Case；
- 已确定最小临时代码边界；
- 已明确不修改正式 Feature 和不重跑全期。
尚未执行
- 没有实际读取本地正式物理根；
- 没有取得局部 KLine；
- 没有取得同窗口全部 Turn；
- 没有生成 Case 数据包；
- 没有生成 HTML 或 PNG；
- 没有执行步骤 5 的运行和取数；
- 没有提交任何文件。
当前总体状态
仍为：
PLAN_READY

第 4 步已经完成，但只有第 5 步实际取得并核对材料之后，才能升级为 DATA_READY 或 PARTIAL_WITH_LIMITS。

## 第 2 轮

### 问：

by: 樊月；原对话时间未提供。

好的，继续给出一份CAEGraph图的定义

### 回答：

已给出一份具体的 CAEGraph 定义
这次不再只是“图应该长什么样”的概念说明，而是已经写成了具体 Python 定义，包括：

CAEGraph
PlotSet
PerSymFigs
SubFig
KPriceLine
F、Q、V 三个专用 BasePlotter
graph.layout(..., all_figs=..., plot_roots=...)
F→Q→V 精确引用与源记录回跳字段
第一步实际观察案例的默认时间范围
完整代码：

该文件已通过 Python 语法编译检查，但尚未在你们实际的 mquant、SOF 和正式结果目录中运行，因此当前属于可执行定义已完成、运行证据尚未取得。

一、最终定义的图是什么
U2 F/Q/V candidate-centred observation
│
├── rb：5m close + F 成员转折 + P/T/C + actual→confirmation
├── hc：5m close + F 成员转折 + P/T/C + actual→confirmation
├── i ：5m close + F 成员转折 + P/T/C + actual→confirmation
│
├── F：候选形成窗口、正式发表点、basis、observation、closed
├── Q：各成员的转折后运动段、verdict、completion、六量、组级资格
└── V：离散发表的 Pending / Invalid / AcceptedWorking / ...
这里使用 PerSymFigs 为 rb、hc、i 分别生成价格面板，避免不同品种使用同一绝对价格轴。其后使用三个共享时间轴的 SubFig 表达 F、Q、V。

CAEGraph 当前源码本身支持 Context、`plotsets`、主题、图宽高、开关等参数；`layout()` 也明确接受 all_figs 和 plot_roots，可在步骤 5 取得构图阶段的数据树和 Bokeh 图对象。

PlotSet 当前接口支持：

calendar_name
blk
timespans
timespans_fao
figs
并按时间范围建立同一个 PlotCtx，让后续面板共享时间轴。

PerSymFigs、`SubFig`、`MainFig` 等布局类都由当前 uplot 正式导出。

二、核心 CAEGraph 构造
完整文件中的主定义是：

def make_fqv_caegraph(
    bundle_dir: str | Path,
    *,
    start: str = "2016-03-08 09:00:00",
    end: str = "2016-03-08 15:00:00",
) -> CAEGraph:
    bundle = FQVCaseBundle.from_dir(bundle_dir)
    bundle.validate()

    price_panels = PerSymFigs(
        title="!{sym} - 5m close / F member turns",
        fig_height=260,
        plots=GMapX.from_list([
            KPriceLine(
                feat=KLine(freq="5m"),
                std_method=None,
                add_hover=True,
                label="5m close",
            ),
            FQVTurnOverlay(bundle=bundle),
        ]),
    )

    graph = CAEGraph({
        "Context": OptContext({
            "sof_name": "TA_updto20240229_DBA",
            "stk_tlist": "steel",
            "startDay": start[:10],
            "endDay": end[:10],
        }),
        "plotsets": GMap({
            "FQV candidate-centred observation": PlotSet({
                "calendar_name": "night_end_at_2300",
                "timespans": [(start, end, "FQV case")],
                "blk": ["rb", "hc", "i"],
                "figs": GMapX.from_list([

执行布局：

graph = make_fqv_caegraph(".runtime/u2-fqv-observation/cases/case-01")

all_figs = []
plot_roots = []

layout = graph.layout(
    ncols=1,
    all_figs=all_figs,
    plot_roots=plot_roots,
)

show(layout)

这与 CAEGraph 手册中 CAEGraph → PlotSet → 布局类 → 绘图类 的构造方式一致。手册现有示例也是在 PlotSet.figs 中组合多品种主图和每品种附图，然后通过 graph.layout() 显示。

三、四个具体绘图器
1. FQVTurnOverlay
叠加在每个品种的 KPriceLine 上。

它画：

P
T
C
正式 Turn
actual 到 confirmation 的虚线
Turn exact
F candidate exact
source row key
因此一个 Turn 虽然有 actual、confirmation 和 known 多个时间角色，仍然只保持一个业务身份。

这部分复用了旧版 F 真实叠图已经验证过的结构：三品种独立价格轴，P/T/C、Source confirmation、candidate knowledge 分开显示。

但不复用旧图的 MapKLineOpenData/open_uti 输入，而是改成当前正式配置的：

KPriceLine(
    feat=KLine(freq="5m"),
    std_method=None,
)

当前 KPriceLine 正式接口支持 feat=KLine()、`std_method`、`extra_bars`、hover、颜色和标签等参数。

2. FCandidatePlot
F 面板画两种对象。

候选问题窗口
groupAnchor ───────── groupDeadline
它只是形成观察窗口，不是候选已经持续成立的区间。

F 正式发表点
发表点位于 groupKnownFrom，hover 中保留：

Candidate Life/Revision
Supported / Incomplete / Contradicted
Open / ClosedSupported / ...
closed
原 CSV 行键
原文件 URL
F 的 Pair Required 和 overlap 等详细信息目前不全部铺到主图，而是进入 Case 数据包和 hover/明细入口。当前正式结果中已经存在成员、Pair Required、pair distance、overlap 和 previous 等表。

3. QOrganizationPlot
Q 面板的 y 轴固定为：

rb
hc
i
group
每个成员用一条线段表示：

used Turn actual ───── endpoint / successor actual
线段颜色表示成员 verdict，hover 中显示：

SupportsAskedDirection
ContradictsAskedDirection
WorkingNotMature
WorkingPathUnavailable
working/completed
P/A/D/L/E/C 六量
Q exact
F exact
源记录键
组级 Q 发表点单独画在 group 轨道。

当前正式 Q 结果确实已经公开成员、六量、endpoint、successor、previous 和 DutyEnd 等数据。

六量不会被重新压成一个观察版总分。

4. VValidityPlot
V 面板只画离散正式发表点，y 轴固定为：

Pending
Invalid
AcceptedWorking
AcceptedCompleted
ValidityConflict
SubjectNotApplicable
每个点保存：

V exact
实际使用的 F exact
实际使用的 Q exact
formation basis
Q qualification
reason
源记录键
原文件 URL
这里没有先画“状态保持带”。

这是有意的：V 是稀疏发表结果，没有新发表不能自动理解为状态持续，更不能把 DutyEnd 后的空白填成 Invalid。

当前正式 V 结果已经公开：

318 条主发生
731 条成员
501 条原因
283 条 previous
35 条 DutyEnd。
四、图所需要的 Case Bundle
CAEGraph 定义不直接重算 F/Q/V，而是消费步骤 5 形成的六份临时观察表：

turn_points.csv
f_windows.csv
f_events.csv
q_member_segments.csv
q_group_events.csv
v_events.csv
turn_points.csv
字段	含义
symbol	rb / hc / i
role	P / T / C / TURN
actual_uti	实际位置
price	原价
confirmation_uti	确认位置
known_uti	当时可知位置
turn_exact	Turn Life/Revision
candidate_exact	F Candidate exact
source_key	原 CSV 索引
source_url	原文件入口
f_events.csv
核心字段：

known_uti
lane
candidate_label
local_basis
observation
closed
exact
source_key
source_url
color
q_member_segments.csv
核心字段：

symbol
start_uti
end_uti
lane
verdict
completion
p a d l e c
q_exact
f_exact
source_key
source_url
color
v_events.csv
核心字段：

known_uti
state_y
result
formation_basis
qualification
reason
v_exact
f_exact
q_exact
source_key
source_url
color
这些都是观察适配表，不成为新的业务 Feature，也不修改正式 F/Q/V 输出。

五、精确引用与“点回原数据”
图中的每个 F、Q、V glyph 都带：

source_key
source_url
F exact
Q exact
V exact
代码为相应 glyph 增加 TapTool + OpenURL：

TapTool(
    renderers=[renderer],
    callback=OpenURL(url="@source_url"),
)

因此点击正式点或线段，可以打开对应源文件；hover 中同时显示准确记录键。

跨特征仍严格依赖：

Q.organizationCandidate → F exact
V.validityFormation     → F exact
V.validityOrganization  → Q exact
不使用 timestamp 或 occurrence 编号猜关联。现有结果包已经提供 Q→F 286 项、V→F 和 V→Q 各 318 项精确映射。

六、当前完成边界
已完成
已确定具体 CAEGraph、PlotSet 和布局类；
已确定每个 panel 的类和参数；
已确定 F/Q/V 的字段映射；
已定义四个实际绘图器；
已定义 Case Bundle 文件和字段合同；
已定义点击回源；
已定义 all_figs、`plot_roots` 的取得方式；
完整 Python 文件已通过 py_compile。
尚未完成
尚未生成 Case Bundle；
尚未在 FY/CYF 的正式 mquant 环境导入；
尚未验证 KLine 和正式结果物理根可读；
尚未生成 Bokeh 页面；
尚未核对实际 ColumnDataSource；
尚未执行步骤 5。
因此，这份内容现在可以称为：

CAEGraph 可执行定义已完成
运行和真实取数尚未执行
总体仍为 PLAN_READY
下一步就是直接进入步骤 5：先生成 2016-03-08 的 Case Bundle，再运行这份定义并检查 plot_roots、`all_figs` 和每一层真实数据。


fqv_caegraph_definition.py
代码

## 第 3 轮

### 问：

by: 樊月；原对话时间未提供。

嗯，上面的表达还不够具体，我需要知道，就是比如说有几个输出事件，然后事件的 occurrence 是什么，这个 occurrence 包含哪些信息？包括输入也是同样的道理。要精确到这个程度，才有做这个观察数据准备事情的基础

### 回答：

F/Q/V 的输入事件与输出事件：按实际数据合同展开
这次要从 Event → Occurrence → 字段 → 子对象 → 正式保存表 五个层次讲清楚。这样后面准备观察数据时，才能确定究竟需要取得哪些事件、哪些字段，而不是仅凭“F 是候选、Q 是方向、V 是成立”去画图。

依据当前实际 FRP 实现版本：

daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c

一、先回答：三个特征分别有几个输入、输出事件？
这里要区分：

事件流（Event Stream）：随着时间发生的一条 FRP 事件通道。

Occurrence：这条事件流某一次发生所携带的一项业务记录。

一个 Occurrence 里的状态值：例如 AcceptedWorking 或 Invalid，并不是两种独立事件。

特征

实际处理器的输入

内部业务输出

正式保存的输出

F

1 条合并后的 FormationFrame 流，来自多个品种的行情、转折及来源变化

1 类 CandidateOccurrence

1 类候选 Occurrence，另有首次保存的 Definition

Q

1 条合并后的 DirectionalFrame 流，内部含来源帧、行情样本和 F 候选三类材料

DirectionalOccurrence、DirectionalDutyEnd 两类

1 类方向观点 Occurrence + 1 类独立责任结束记录，另有 Definition

V

1 条合并后的 ValidityInput 流，包含 F 更新、Q 更新、Q 责任结束三类变化

ValidityOccurrence，另有 ValidityInputError 诊断

1 类成立判断 Occurrence，另有 Definition；输入错误不作为正式市场判断保存

也就是说，不能说 F 有 Supported、Incomplete、Contradicted 三个输出事件；也不能说 V 有六个输出事件。它们是同一种 Occurrence 里的不同状态。

正式物理输出类型分别是：

-- F
FrpEvent (Tick [GroupCandidatesRecord])

-- Q
FrpEvent (Tick [DirectionalOrganizationRecord])

-- V
FrpEvent (Tick [GroupValidityRecord])

一个 Tick 可以承载一个包含多条 Occurrence 的记录包；也可能只承载首次 Definition，或者 Q 的结束信息。因此 Tick 数、Occurrence 行数、不同 Life 数不是一回事。

当前 2026-11-16 新版真实批次的正式主表包含：

特征

主表 Occurrence 行数

其他重要记录

F

97

成员 221 行，Pair Required 151 行

Q

286

成员 656 行，数量状态 3936 行，DutyEnd 35 行

V

318

成员 731 行，原因 501 行

这些数字是该批次实际保存/读回的数据行数，不是事件类型数，也不是唯一候选数量。

来源：当前真实 F/Q/V 结果读取指南。

二、F：共同价格转折候选组
2.1 F 输入的事件究竟是什么？
F 正常实例在每个品种上接入四类上游事件/材料：

来源

真实事件类型

一个发生携带什么

KLine

5m KLine 的价格/时间字段事件

close、closeUti，转换后形成价格、实际 UTI、采样位置和 Calendar Clock

ScaleTurn 第一轮

CompleteScaleTurn

actual、confirm、processInfo

ScaleTurn 第二轮

CompleteScaleTurn

同样三个字段，但属于第二轮选择结果

RctZigWithStatus

ZigWithStatusOcc

最新状态点与最近确认 Zig 的价格、带方向价格和 UTI

这里的 ScaleTurn 第一轮和第二轮确实是两条不同的上游事件流，正式读取键分别为 value1、value2。

一个 CompleteScaleTurn 的实际结构是：

CompleteScaleTurn {
    actual      :: Point 2 Double,
    confirm     :: Point 2 Double,
    processInfo :: [MapEntry Text Double]
}

actual 和 confirm 各自包含一个位置与价格。

ZigWithStatusOcc 的六个字段是：

price0, pivot0, posUTI0
price1, pivot1, posUTI1
其中 0 是最新状态点，1 是最近确认 Zig。

F 使用这些信息构造方向、转折类型、P/T/C 几何及其可知时间。

来源：ScaleTurn 类型、ScaleTurnCalendar、ZigN。

2.2 F 内部真正接收的一条输入事件
上述上游事件合成 FormationFrame：

FormationFrame {
    frameProgress :: Double,
    frameKnown    :: Int64,
    frameTurns    :: [GroupTurn],
    framePatches  :: [FormationPatch],
    frameEnded    :: Bool,
    frameCoverage :: [ObjectCoverage]
}

字段的准确含义：

字段

含义

frameProgress

当前已处理到的交易 Calendar 进展

frameKnown

当前业务材料的知识时点

frameTurns

本次带来的转折记录，可以为空或包含多个

framePatches

已合法接受的来源修订，例如价格、Clock、覆盖或转折来源修订

frameEnded

输入范围结束标记

frameCoverage

各对象当前输入覆盖的情况

**本批正常 KLine 接线还有一项具体边界：**其 buildKLineGroupSource 当前构造的 FormationFrame 将 framePatches=[]、frameEnded=False，并随价格样本提供 CoverageObserved。通用 FormationFrame 类型支持更丰富的修订事件，不代表这批 KLine 运行实际产生了所有这些类型。

frameTurns 中的一条 GroupTurn
这才是 F 用来比较不同品种转折的基本业务对象：

GroupTurn
├── groupTurnRef            准确 Turn 引用
├── groupTurnSource         原来源引用
├── groupTurnObject         品种 rb / hc / i
├── groupTurnActual         实际转折 UTI
├── groupTurnPrice          转折原价
├── groupTurnConfirmation   确认 UTI
├── groupTurnKnown          知识 UTI
├── groupTurnDirection      DirectionUp / DirectionDown / 未知
├── groupTurnType           SourcePeakTurn / SourceTroughTurn / 未知
├── groupTurnRound          FirstRound / SecondRound
├── groupTurnGeometry       selected P/T/C 几何及知识信息
├── groupTurnClock          Clock 数值及其已知时点，可缺失
├── groupTurnRetracted      是否撤回
└── groupTurnOriginOrder    来源实际提供的顺序，可缺失
frameCoverage 中每项 ObjectCoverage 包含：

coverageObject
coverageCondition
coverageFrom
coverageThrough
coverageCondition 可以是 CoverageColdStart、CoverageObserved、CoverageInputMissing、CoverageClockUnknown、CoverageSourceFailure 或 CoverageInapplicable。

因此，F 的输入不是仅仅“一个转折发生了”，而是一批带身份、时点、来源、几何及覆盖状态的转折材料。

来源：F 输入构造、FormationFrame 定义。

2.3 F 有几个正式输出 Occurrence 类型？
一个：CandidateOccurrence。

它每次发表一个候选的新版本，而不是分别发“形成事件”“确认事件”“关闭事件”。

内部业务对象是：

CandidateOccurrence {
    candidateReference,
    candidatePrevious,
    candidateQuestion,
    candidateKnown,
    candidateBody,
    candidateParticipation
}

正式保存时对应 GroupOccurrenceRecord，完整字段结构可以分为六组。

A. 候选身份与历史
正式字段

含义

groupReference

当前 F Candidate 的 Life + Revision

groupPrevious

上一个正式 Revision，首版可以为空

groupKnownFrom

本次候选观点何时可知

一个 Candidate Life 可以有多个 Revision。

B. 形成观察期限
groupOriginalAnchor
groupOriginalDeadline
groupOriginalRevisionEnd

groupAnchor
groupDeadline
groupRevisionEnd
前三个是原问题期限，后三个是当前合法期限。

这些是 Calendar 观察/修订边界，不是 KLine 价格，也不能直接当作候选实际转折 UTI。

C. 候选当前判断
groupLocalBasis
groupAlternative
groupObservation
groupCoverageIncomplete
groupClosed
对应枚举：

字段

可能值

groupLocalBasis

Supported / Incomplete / Contradicted

groupAlternative

Unambiguous / UnresolvedOverlap

groupObservation

Open / ClosedSupported / ClosedInsufficient / Withdrawn / Subsumed / EndedByScope

groupCoverageIncomplete

布尔值

groupClosed

布尔值

D. 候选成员：groupMembers[]
每个成员完整包含：

memberObject
memberTurn
memberSource

memberActual
memberPrice
memberConfirmation
memberKnownFrom

memberDirection
memberType
memberRound
memberClock

memberP           可选 P 点
memberT           T 点
memberC           C 点

memberStatus
memberRetracted
其中每个 P/T/C 点保存：

pointActual
pointPrice
pointKnownFrom
pointClock[] {
    clockCoordinate
    clockKnownFrom
}
memberStatus 分为 ConfirmedMember 和 CandidateMember。

这里需要特别注意，F 的成员信息是在候选 Occurrence 中保存的子对象，而不是独立的 F 成员事件流。

E. 成员之间的 Pair 依据：groupRequired[]
每一对 Turn 包含：

pairLeft
pairRight
pairDistance[]

pairTime {
    requiredVerdict
    requiredGap
    requiredVeto
}
pairDirection { 同上 }
pairType      { 同上 }
pairBend      { 同上 }
每项 Required 的判定是：

CoordinateSupports
CoordinateUnresolved + RequiredGap
CoordinateVeto       + RequiredVeto
这四项是并列的必要判断，不能压成四个可以互相抵消的分数。

F. 候选之间的关系与参与事实
groupOverlaps[]
groupCoveredBy[]
groupFormationParticipation[]
其中 groupFormationParticipation 是正式保存的结构化子对象，主要包含：

participationAdmission
participationAdmissionKnown
participationCandidate
participationMembers[]

participationQuestionAnchor
participationQuestionDeadline
participationQuestionRevisionEnd
participationDeadline
participationRevisionEnd
participationHandoffEnd

participationDecisionMethod
participationDecisionScope
participationSubject
participationHistoryComplete
participationDutyClosed

participationSupports[]
participationAlternatives[]
participationOutsideNotifications[]
participationInputConflict
participationDecisionKnown
participationSupports[] 还能继续下钻到支撑/反证所针对的两个成员、坐标、状态、原因、操作数及可知时间。

这属于正式输出合同，不是单纯的调试字段。不过当前 2026-11-16 批次的 participationSupports 公开表为 0 行，不能因此假设所有 F 运行都没有这个结构，也不能凭空补值。

F 正式输出的外层包装
GroupCandidatesRecord
├── groupDefinitions[]     本次首次固定定义
└── groupOccurrences[]     0～多条 Candidate Occurrence
groupDefinitions[] 包含方法、上下文、尺度、Calendar、Universe、Domain、对象列表、Δ、时间单位以及方向/转折类型相容矩阵。

Definition 是实例配置声明，不是市场中的候选 Occurrence。

来源：F 业务类型、F 正式存储结构。

三、Q：转折后方向组织
3.1 Q 的输入事件究竟有几类？
Q 的内部处理器只接收 1 条 DirectionalFrame 事件流，但这条流合并了三类输入：

DirectionalFrame {
    directionalSourceFrame :: FormationFrame,
    directionalSamples     :: [(Text, MotionSample)],
    directionalCandidates  :: [CandidateOccurrence]
}

内部输入

实际来源

一个输入项包含什么

directionalSourceFrame

各品种 ScaleTurn/KLine 形成的来源材料

frameProgress、frameKnown、frameTurns[]、framePatches[]、frameEnded、frameCoverage[]

directionalSamples

新 KLine 报价样本

品种及 MotionSample

directionalCandidates

已经保存的 F 候选观点，经读入后还原为内部候选事件

F 的 Candidate 身份、成员、形成依据、期限及修订信息

所以从业务输入类别上看是 3 类，从 Q 的 CEPS 正式输入类型上看是 1 条合并事件流。

Q 的一条价格输入 MotionSample
MotionSample {
    sampleActual   :: Int64,
    sampleKnown    :: Int64,
    samplePrice    :: Maybe Double,
    sampleClock    :: Maybe FormationClock,
    samplePosition :: Maybe Double
}

具体含义：

字段

用途

sampleActual

此报价实际发生的 UTI

sampleKnown

此报价当时合法可知的 UTI

samplePrice

真实价格，可以缺失；缺价不是价格等于零

sampleClock

Calendar Clock 及其知识时间

samplePosition

采样格位置，用于判断路径是否连续

这是 Q 与 F 最明显的输入差异。

F 主要研究转折之间的关系；Q 则需要逐根读取候选成员转折以后的真实价格样本。

它也会接收真正后继 Turn，用于确定一段运动是否完成。

directionalCandidates 中的一项是什么？
它就是 F 已经发表的 CandidateOccurrence，不是重新构造的“候选名称”。

其必要内容包括：

candidateReference
candidatePrevious
candidateKnown
candidateBody.candidateMembers[]
candidateBody.candidateBasis
candidateBody.candidateObservation
candidateBody.candidateClosed
candidateBody.candidateAnchor
candidateBody.candidateDeadline
candidateBody.candidateRevisionEnd
Q 的订阅逻辑使用准确候选身份和原成员，不会根据后续行情重新选择一个更好的成员组合。

源码：Q 输入合并。

3.2 Q 产生几类输出？
从业务处理器的角度，Q 产生两类：

第一类：DirectionalOccurrence，即方向组织观点。

第二类：DirectionalDutyEnd，即方向观察问题的责任结束。

内部处理后，它们一起放在：

DirectionalBatch {
    batchInput       :: DirectionalFrame,
    batchOccurrences :: [DirectionalOccurrence],
    batchEnds        :: [DirectionalDutyEnd]
}

batchInput 是传给同图消费者的本拍材料，不作为 Q 正式产品的行情原文保存。

正式存储包装是：

DirectionalOrganizationRecord
├── organizationDefinitions[]
├── organizationOccurrences[]
└── organizationDutyEnds[]
这意味着即使某个时点 organizationOccurrences=[]，只要有真正的 DutyEnd，Q 仍可保存该次结束发生。

3.3 一条 DirectionalOccurrence 包含什么？
内部类型是：

DirectionalOccurrence {
    directionalReference,
    directionalPrevious,
    directionalKnown,
    directionalOccurrenceView
}

保存为 DirectionalOccurrenceRecord 之后，字段如下。

A. Q 观点身份与 F 引用
organizationReference
organizationPrevious
organizationCandidate
organizationKnownFrom
其中：

organizationReference：Q 自己的 Life/Revision；

organizationPrevious：Q 前一个 Revision；

organizationCandidate：这条 Q 观点使用的准确 F 候选引用；

organizationKnownFrom：当前 Q 观点可知时间。

注意，organizationCandidate 不能只当成 F 的 Life。它包含准确 Revision，能够说明 Q 当时采用的是哪一个 F 版本。

B. Q 原始和当前观察期限
organizationOriginalAnchor
organizationOriginalDeadline
organizationOriginalRevisionEnd

organizationAnchor
organizationDeadline
organizationRevisionEnd
同样，原期限和当前合法收紧后的期限都保留。

它们属于 Q 的方向观察责任边界，不是成员真实运动的起止点。

C. Q 组级业务状态
organizationObservation
organizationApplicability
organizationQualification
三个字段的含义不同：

字段

枚举值

organizationObservation

MotionObserving / HorizonReached / MotionScopeEnded

organizationApplicability

SubjectApplicable / SubjectWithdrawn

organizationQualification

QualificationRejected / QualificationConflict / QualificationPending / QualifiedCompleted / QualifiedWorking

例如：

HorizonReached 是观察期限相关的状态，不等于所有成员运动 MotionCompleted。

而 QualifiedWorking 是 Q 的组级结论，不是独立事件类型。

D. Q 全部成员：organizationMembers[]
这是 Q 最值得认真取材的正文。

每一条成员记录包含：

organizationObject

organizationAskedTurn
organizationUsedTurn
organizationSuccessor[]

organizationEndpoint[]

organizationCompletion
organizationQuantities[]
organizationVerdict
organizationBasis

organizationPathComplete
organizationThrough
organizationMaterialKnownFrom
organizationMissingRange[]
其中：

字段

业务含义

organizationObject

品种对象

organizationAskedTurn

F 候选原来要求观察的 Turn

organizationUsedTurn

当前实际合法采用的 Turn 版本

organizationSuccessor

真正紧邻的后继 Turn，可以为空

organizationEndpoint

当前实际量测端点

organizationCompletion

MotionWorking 或 MotionCompleted

organizationQuantities

P/A/D/L/E/C 六个量及可用性

organizationVerdict

当前成员的方向判断

organizationBasis

原候选成员依据或成员依据修订

organizationPathComplete

路径材料是否完整

organizationThrough

实际观察到的 Calendar 边界

organizationMaterialKnownFrom

本次量测实际使用材料的知识时点

organizationMissingRange

当前路径缺失区间，可以为空

E. Asked / Used / Successor Turn 的结构
这三个位置使用相同的 DirectionalTurnRecord：

motionTurn
motionSource

motionActual
motionPrice
motionConfirmation
motionKnownFrom

motionClock[]
motionOrder[]
motionRetracted
这里没有在 Q 的这个窄 Turn 子结构中再次保存完整的 F selected P/T/C 几何。

需要查看 P/T/C，应该回到准确 F 和原 ScaleTurn，而不是从 Q 的字段名称猜测。

F. 当前运动端点：organizationEndpoint[]
endpointActual
endpointKnownFrom
endpointPrice[]
endpointClock[]
注意：这个端点才是 Q 当前实际量测停在哪里的重要依据。

仅有 organizationThrough 还不能还原端点的实际价格位置。

G. 六个运动量：organizationQuantities[]
每一个量的结构是：

motionQuantity
motionNumber[]
motionAvailability
六个 motionQuantity 值分别是：

Quantity

含义

ProgressP

所问方向上的净推进

AmplitudeA

端点绝对价格差

DurationD

真实 Calendar 持续时间

PathLengthL

路径累计绝对变化

EfficiencyE

幅度与路径长度之比

CounterC

最大反向回落

motionAvailability 的值：

QuantityKnown
EndpointUnavailable
ClockUnavailable
PathUnavailable
ZeroPathNotApplicable
一个 Quantity 不是一个 Q Occurrence。 它是该成员 Occurrence 正文里的一个数量子项。

例如一条成员记录通常带六个 Quantity 子项。当前实际数据中 656 条 Q 成员对应 3936 条 Quantity 记录，正好是每成员六项。

H. 成员方向判断：organizationVerdict
全部枚举为：

SupportsAskedDirection
ContradictsAskedDirection
RequiredMotionConflict
UndeterminedZeroProgress
UndeterminedEndpoint
WorkingNotMature
WorkingPathUnavailable
MemberAnchorWithdrawn
这些状态尤其不应该被画图时简单压缩成“支持/不支持”两类。

例如 UndeterminedZeroProgress、WorkingNotMature、WorkingPathUnavailable 的业务含义完全不同。

3.4 第二类 Q 输出：DirectionalDutyEnd
这类结果需要单独理解，因为它不是一条新的方向观点。

正式字段是：

organizationEndLast
organizationEndReason
organizationEndKnown
organizationEndProgress
字段

含义

organizationEndLast

最后一条成功的 Q 观点，完整的 DirectionalOccurrenceRecord

organizationEndReason

DirectionalRevisionDutyEnded 或 DirectionalScopeEnded

organizationEndKnown

责任结束的知识时间

organizationEndProgress

结束时 Calendar 进展

因此，Q 的观察材料必须至少区分：

Q 发表了新的方向观点；

Q 当前没有新观点，但确实结束了责任。

它们不能合成一个普通的状态变化。

来源：Q 业务类型、Q 正式存储结构。

四、V：共同转折组局部成立判断
4.1 V 的输入事件有几类？
V 的实际 CEPS 输入是：

ValidityInput {
    validityFormationUpdates    :: [ValidityFormation],
    validityOrganizationUpdates :: [ValidityOrganization],
    validityDutyEnds            :: [ValidityDutyEnd]
}

所以它有 3 类输入变化。

与 Q 不同，V 当前版本不再读取真实 KLine、ScaleTurn 或价格样本。

输入 A：ValidityFormation
这是从 F 的正式 Candidate Occurrence 中投影出来、供 V 判断所需的字段。

validityFReference
validityFPrevious
validityFKnown

validityFMembers[]
validityFPairs[]

validityFBasis
validityFClosed
validityFObservation
validityFOverlap
validityFDomainIncomplete
validityFSubsumedBy[]
其成员 ValidityTurn 包含：

validityTurnReference
validityTurnSource
validityTurnObject

validityTurnActual
validityTurnPrice
validityTurnConfirmation
validityTurnKnown

validityTurnDirection
validityTurnType
validityTurnClock
validityTurnOrder
validityTurnRetracted
validityFPairs[] 包含：

validityPairLeft
validityPairRight
validityPairCoordinates[]
这里的 Pair 已经是 F 判断完成的四项 Required，V 不重新比较 P/T/C。

输入 B：ValidityOrganization
这是从 Q 正式方向观点中投影出来的 V 所需信息。

validityQReference
validityQPrevious
validityQKnown
validityQFormation

validityQMembers[]

validityQQualification
validityQObservation
validityQApplicability

validityQOriginalBounds
validityQBounds
其中一条 ValidityMember 包含：

validityObject
validityAsked
validityUsed
validitySuccessor

validityVerdict
validityCompletion

validityUnavailable[]
validityThrough
validityMissingRange
validityProgress
这里有一个特别重要的差别：

V 没有完整复制 Q 的 P/A/D/L/E/C 六量。

它只保留自己成立判断需要的成员类别、必要量缺失情况，以及反向/零推进时的小解释数值。

所以如果后面需要分析“Q 的某个成员为什么支持或反对”，仍应读取准确 Q Occurrence，而不能只读取 V。

输入 C：ValidityDutyEnd
validityEndQuestion
validityEndLastQ
validityEndCause
validityEndKnown
这来自 Q 的正式责任结束记录。

V 需要知道：这个方向观察问题的责任确实结束了，以及最后一条成功 Q 观点是哪一条。

它不能根据当前时间到了，就自行假造一个结束事件。

来源：V 的输入投影类型、V 从 F/Q 正式记录构造输入。

4.2 V 输出有几类？
V 的正式业务 Occurrence 只有一种：

ValidityOccurrence

其内部类型是：

ValidityOccurrence {
    validityReference,
    validityPrevious,
    validityQuestion,
    validityDirection,
    validityQ,
    validityKnown,
    validityStatement
}

正式保存时展开为 ValidityOccurrenceRecordV2。

A. V 观点身份和实际消费的 F/Q
validityRecordReference
validityRecordPrevious

validityFormation
validityOrganization
validityRecordDirection
validityKnownFrom
字段

作用

validityRecordReference

V 自己的 Life/Revision

validityRecordPrevious

上一条 V 正式观点

validityFormation

实际采用的 F Candidate exact

validityOrganization

实际采用的 Q Organization exact

validityRecordDirection

所问方向

validityKnownFrom

当前 V 声明可知时间

最重要的是 validityFormation 与 validityOrganization。

它们告诉我们 V 究竟依据哪一次 F、Q 观点形成判断，而不是让我们到相同时间找一条“最新 F/Q”来代替。

B. V 的当前业务结果
validityResult
六种可能值：

AcceptedWorking
AcceptedCompleted
Invalid
Pending
ValidityConflict
SubjectNotApplicable
这六种是一个字段的六种枚举值，不是六种输出 Occurrence。

C. V 保存的 F 形成信息
validityFormationBasis
validityFormationClosed
validityFormationObservation

validityOverlap
validityDomainIncomplete
validityContainments[]
例如：

validityFormationBasis = Supported

validityFormationClosed = True

这两项分别表明形成依据已经得到支持、形成观察已经关闭，不是同一个条件。

validityOverlap 和 validityDomainIncomplete 也是实际限制信息，不能直接理解成 V 必须不成立。

D. V 保存的 Q 方向信息
validityQualification
validityObservation
validityApplicability
分别对应：

Q 组级方向资格；

Q 观察是否仍在进行、达到期限或结束范围；

Q 的观察主语是否仍适用。

E. V 责任边界
validityOriginalAnchor
validityOriginalDeadline
validityOriginalRevisionEnd

validityAnchor
validityDeadline
validityRevisionEnd
它们沿用实际方向观察问题的原始和当前界限。

F. V 成员：validityMembers[]
每一条正式成员记录包含：

validityMemberObject

validityAskedTurn
validityUsedTurn

validityAskedDirection
validityAskedType
validityUsedDirection
validityUsedType

validityActualSuccessor[]

validityMemberVerdict
validityMemberCompletion

validityMemberUnavailable[]
validityObservedThrough
validityMemberMissingRange[]
validityNegativeOrZero[]
其中 Asked/Used/Successor Turn 都包含：

motionTurn
motionSource
motionActual
motionPrice
motionConfirmation
motionKnownFrom
motionClock[]
motionOrder[]
motionRetracted
validityMemberUnavailable[] 保存数量类型及不可用原因；validityNegativeOrZero[] 只承载相应负向或零推进解释值。

这再次说明：V 的成员结构是为解释成立判断而保留的窄投影，并不是 Q 成员完整量测的副本。

G. V 的原因：validityReasons[]
这是观察 V 合理性时不能遗漏的一组信息。

正式 ValidityReasonRecordV2 包含：

validityReasonKind
validityReasonObject
validityReasonLeft[]
validityReasonRight[]
validityReasonDetail
validityReasonKind 当前对应：

原因类别

业务含义

FormationMissing

F 某一 Pair 的形成必要信息缺失

FormationVeto

F 某一 Pair 存在明确形成反证

MemberCondition

Q 某个成员当前不满足所问方向

FormationObservationOpen

F 形成观察仍未关闭

RequiredFormationMissing

F 形成必要条件尚不完整

CandidateWithdrawn

候选主语撤回或不适用

如果原因来自 Pair，validityReasonLeft、validityReasonRight 会定位相关转折；如果来自成员，validityReasonObject 指向对应品种，validityReasonDetail 编码具体成员判断。

因此，一次 V Invalid 不是只输出一个 Invalid 标签，它还可以明确指出是形成反证还是某个成员反向。

H. V 责任结束：validityDutyEnd[]
其内部记录含：

validityEndReason
V 的责任结束信息被保存在 V Occurrence 的正文里。

与 Q 不同，V 没有另设一条独立保存的 V DutyEnd Occurrence 流。

V 正式包装
GroupValidityRecordV2
├── validityDefinitions[]
└── validityOccurrences[]
validityDefinitions[] 保存 V 方法定义和 Q 上游定义，只在固定定义时写入。

另外 V 内部还可能产生 ValidityInputError：

validityErrorQuestion
validityErrorMessage
它是诊断结果，不是市场业务结论，不能转写成 Pending 或 Invalid。

来源：V 正式存储合同、V 判断与声明变化规则。

五、这些 Occurrence 在 Python 中怎样取出来？
前面说的是原始业务对象结构；Python 正式读取时，嵌套数组会展开成主表和子表。

业务对象

Python 主表

需要配套读取的子表

F CandidateOccurrence

F/occurrences.csv

occurrences_groupMembers、occurrences_groupRequired、occurrences_groupRequired_pairDistance、occurrences_groupOverlaps、occurrences_groupPrevious 等

Q DirectionalOccurrence

Q/occurrences.csv

occurrences_organizationMembers、occurrences_organizationMembers_organizationQuantities、对应 motionNumber、端点、后继等

Q DirectionalDutyEnd

Q/duty_ends.csv

最后成功 Q 引用及结束原因、时间

V ValidityOccurrence

V/occurrences.csv

occurrences_validityMembers、occurrences_validityReasons、occurrences_validityRecordPrevious、occurrences_validityDutyEnd 等

这里尤其需要区分两个“occurrence”：

业务 Occurrence： 一次带独立 Life/Revision 的 F、Q 或 V 业务观点。

CSV 的 occurrence 索引： Python 展开正式 ADT 时使用的物理行索引。

当前数据包的主表索引是：

timestamp
occurrence
record_id
child_id_2
子表还会继续增加 child_id_3 等索引。

不能仅凭同名 occurrence 字段，把 F、Q、V 不同产品的行连接起来。必须使用各自明确保存的 Life/Revision exact，以及现成的 EXACT_REFERENCE_MAP.json。

查看真实表级字段与条数 FACTS.json

六、对当前观察材料准备的直接影响
按上面这份事件合同，我认为接下来不能把三个特征各自的 occurrences 主表拿来就开始画图。

至少要分别保留以下信息：

观察部分

必须保留的原始关系

丢失后会导致什么问题

F 输入

KLine → 第一轮/第二轮 ScaleTurn → GroupTurn；包括全部附近转折

无法判断 F 为什么把某些 Turn 放在一起、其他 Turn 没加入

F 输出

Candidate exact → 成员 Turn exact → Pair Required → basis/observation → previous

只能看到候选组成员，无法解释形成依据和演化

Q 输入

准确 F Candidate → 后续每个 MotionSample → 真实后继 Turn

无法独立核对成员运动过程

Q 输出

Q exact → F exact → 成员 verdict/六量/端点/后继 → DutyEnd

无法判断一个成员为什么支持、反向、未成熟或真正完成

V 输入

当前实际接收到的 F 更新、Q 更新、Q DutyEnd

无法知道 V 为什么在这个时间才改变结论

V 输出

V exact → F exact/Q exact → result → members → reasons → previous/end

只能看 Accepted/Invalid，无法分析组合判断是否合理

还有一个必须保持的时间关系：

市场实际发生时间 actual
       ≠
上游确认时间 confirmation
       ≠
业务信息可知时间 known
       ≠
正式记录的事件发生时间 timestamp（需逐条核对）
这些时点不能默认相等，也不能只取一个画到同一位置后，丢掉其他时间角色。

目前最关键的认识
现在可以准确地说：

F 对外只有一类 Candidate Occurrence，但它的正文已经包含形成、成员、Pair 依据、候选关系和演化信息。

Q 有方向观点 Occurrence 和独立的 DutyEnd，它的核心信息在完整成员量测，而不只是组级 Qualification。

V 只有一类正式 Validity Occurrence，它不重新计算行情，而是保存准确 F/Q 组合之后的成立判断及其原因。

因此，后续 CAEGraph 最需要做的不是新增很多“输出事件”，而是把这三种业务 Occurrence 内部的关键子对象和关系正确展开，同时保留输入事件及其原始时间信息。

这份合同已经可以作为进一步精确制定 F/Q/V 取数清单的基础。但就实际取数而言，仍需要把上游全部 ScaleTurn、逐根 KLine 与现有 F/Q/V 正式多表关联起来；目前并没有因为梳理完成合同，就等于这些输入材料已经全部取得。


## 第 4 轮

### 问：

by: 樊月；原对话时间未提供。

```
CandidateBody里面的这么多字段，都是属于最终的结果，没有就哪些是中间数据，哪些是最终结果吗。你现在你没有一次性给一下这些东西的中文注释，我也看不太明白哪个是哪个。
```

### 回答：

思考了 32s

`CandidateBody`**&#x20;里的字段性质确实不同。它们虽然都被保存为正式输出，但不代表每个字段都是 F 最终想给出的业务判断。**

我前面混淆了两个概念：

- **是否属于正式输出**：`CandidateBody` 的 12 个字段全部属于正式 `CandidateOccurrence` 的正文。
- **在业务处理过程中承担什么角色**：有的是候选形成的结果，有的是中间计算的判断依据，有的是输入事实，还有的是观察范围及状态。

第二个区别才是你现在真正需要的。

下面严格按照源码原来的 12 个字段、原来的顺序，一次性补齐中文注释。

## **一、CandidateBody 原始结构及全部中文注释**
```lua
data CandidateBody = CandidateBody
  {
    -- 1. 候选成员
    -- 当前候选组由哪些转折组成。
    -- 每个成员包含具体 Turn 及其成员状态。
    -- 既有最终选择的成员，也保留成员的原始转折事实。
    candidateMembers :: [(GroupTurn, MemberStatus)]

    -- 2. 成员之间的两两判断依据
    -- 保存每一对成员的时间、方向、类型、弯折判断。
    -- 这是形成候选时产生的中间判断结果，
    -- 但被保留下来，作为正式输出的解释依据。
  , candidatePairs :: [PairBasis]

    -- 3. 候选形成依据的综合结论
    -- Supported：形成依据得到支持
    -- Incomplete：必要依据不完整
    -- Contradicted：存在明确反证
    -- 这是根据成员与Pair判断得到的核心业务结果。
  , candidateBasis :: LocalBasis

    -- 4. 候选的备选关系状态
    -- Unambiguous：当前没有未解决的重叠备选关系
    -- UnresolvedOverlap：存在未解决的重叠关系
    -- 这是比较多个候选后形成的关系判断结果。
  , candidateAlternatives :: AlternativeResolution

    -- 5. 候选当前的形成观察状态
    -- Open：尚未关闭
    -- ClosedSupported：关闭且形成依据得到支持
    -- ClosedInsufficient：关闭但依据不足
    -- Withdrawn：撤回
    -- Subsumed：被更大候选包含
    -- EndedByScope：观察范围结束
    -- 这是当前候选生命周期的业务状态。
  , candidateObservation :: ObservationState

    -- 6. 形成所需的观察域是否不完整
    -- 来自输入对象的覆盖完整性判断。
    -- 用于说明当前候选判断的前提条件。
    -- 不是候选本身是否成立的最终结论。
  , candidateDomainIncomplete :: Bool

    -- 7. 当前形成观察锚点
    -- 根据合法成员Clock确定的当前观察起点。
    -- 属于观察时间边界，不是候选发表时间。
  , candidateAnchor :: Double

    -- 8. 当前形成观察截止位置
    -- 依据锚点和方法期限计算，并受原有期限约束。
    -- 属于观察时间边界。
  , candidateDeadline :: Double

    -- 9. 当前允许修订的截止位置
    -- 限制候选最晚可以修订到哪里。
    -- 属于修订责任边界。
  , candidateRevisionEnd :: Double

    -- 10. 形成观察是否已经关闭
    -- 根据观察进展及已有关闭状态确定。
    -- 是生命周期状态，不等于形成依据已得到支持。
  , candidateClosed :: Bool

    -- 11. 与当前候选存在重叠关系的其他候选
    -- 保存其他候选的Life标识。
    -- 是候选之间的关系判断结果。
  , candidateOverlaps :: [Text]

    -- 12. 包含当前候选的其他候选
    -- 保存满足包含条件的更大候选的Life标识。
    -- 是候选之间的关系判断结果。
  , candidateCoveredBy :: [Text]
  }
```

这份结构保持了源码原来的全部字段和顺序，没有重新组织。

源码：[GroupCandidateTypes.hs](https://github.com/daowei2026/frp/blob/67711c492da909ed0f044f357beb278abf7fc71c/src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateTypes.hs?utm_source=chatgpt.com)

## **二、逐个字段区分：中间数据还是业务结果？**

这里的“性质”是根据实际计算和使用方式做出的分析，不是源码另有一套正式分类。

|   |
| - |

字段

|   |
| - |

业务性质

|   |
| - |

是否属于核心业务结果

|   |
| - |

`candidateMembers` 候选成员

|   |
| - |

**候选组成结果**，同时保存原 Turn 事实及成员状态

|   |
| - |

是

|   |
| - |

`candidatePairs` 两两判断依据

|   |
| - |

**中间判断结果的正式保留**，用于解释为什么形成候选

|   |
| - |

不是最终综合结论

|   |
| - |

`candidateBasis` 形成依据结论

|   |
| - |

**核心判断结果**，由 Pair 等依据综合得到

|   |
| - |

是

|   |
| - |

`candidateAlternatives` 备选关系状态

|   |
| - |

**候选间关系判断结果**

|   |
| - |

是，属于关系层面的结果

|   |
| - |

`candidateObservation` 形成观察状态

|   |
| - |

**当前业务生命周期结果**

|   |
| - |

是

|   |
| - |

`candidateDomainIncomplete` 观察域不完整

|   |
| - |

**输入覆盖条件的汇总信息**

|   |
| - |

不是

|   |
| - |

`candidateAnchor` 观察锚点

|   |
| - |

**计算得到的业务时间边界**

|   |
| - |

不是判断结论

|   |
| - |

`candidateDeadline` 观察截止

|   |
| - |

**计算得到的业务时间边界**

|   |
| - |

不是判断结论

|   |
| - |

`candidateRevisionEnd` 修订截止

|   |
| - |

**计算得到的修订责任边界**

|   |
| - |

不是判断结论

|   |
| - |

`candidateClosed` 是否关闭

|   |
| - |

**当前生命周期状态**

|   |
| - |

是状态结果，但不是形成依据结论

|   |
| - |

`candidateOverlaps` 重叠候选

|   |
| - |

**候选之间的关系判断结果**

|   |
| - |

是

|   |
| - |

`candidateCoveredBy` 包含关系

|   |
| - |

**候选之间的关系判断结果**

|   |
| - |

是

这里有两个特别容易混淆的地方。

### **1.&#x20;**`candidatePairs`**&#x20;是中间计算结果，但已经正式输出**

F 内部的处理关系是：
```
各品种输入转折
       ↓
FormationMaterial
当前可参与判断的转折材料
       ↓
PairView
转折之间的两两相容判断
       ↓
CandidateState
候选组成、形成结论、当前状态
       ↓
CandidateOccurrence
正式发表的候选观点
```

其中 `PairView` 是内部处理对象，**并没有把整个&#x20;**`PairView`**&#x20;原样输出**。

但它里面与当前候选相关的 Pair 判断，被提取进了：

`candidateBody.candidatePairs`

所以它既是计算过程中的中间判断，又是正式输出中保留的解释依据。

这两个说法不矛盾。

### **2.&#x20;**`candidateMembers`**&#x20;不只是原始输入数据**

每个成员的 `GroupTurn` 确实包含从上游来的转折事实，但**哪些 Turn 被组合成当前候选**，本身就是 F 的业务处理结果。

因此不能简单地说 `candidateMembers` 是输入数据副本。

它实际上同时包含：

- 被选入当前候选的成员组合——业务结果；
- 每个成员的具体 Turn 事实——结果所依赖的材料；
- 每个成员当前的 `MemberStatus`——根据 Pair 关系得出的成员判断。

## **三、F 到底最终要表达什么？**

从这个业务特征的目的来看，核心是回答三个问题：

**第一，哪些转折形成了一个候选？**

对应 `candidateMembers`。

**第二，这个候选的形成依据是什么结论？**

对应 `candidateBasis`，由 `candidatePairs` 等提供依据。

**第三，这个候选目前处于什么状态，与其他候选是什么关系？**

对应 `candidateObservation`、`candidateClosed`、`candidateAlternatives`、`candidateOverlaps`、`candidateCoveredBy`。

其他字段主要帮助限定判断成立的条件、期限和可修订范围。

这里的“最终”是指**本次已经正式发表的业务观点**，并不是说它以后不能再有 Revision。

## **四、这对观察数据准备的影响**

最需要注意的是，不能只观察 `candidateBasis`，然后把其他字段都当成不重要的中间信息。

例如，假设某个候选的输出是：
```ini
candidateMembers      = [rb-A, hc-B]
candidateBasis        = Supported
candidateObservation  = Open
candidateClosed       = False
candidateOverlaps     = [另一个候选的Life]
```

这里真正需要观察的不是一个简单的 `Supported`。

我们还需要理解：

- 为什么 rb-A、hc-B 组成候选？需要回看 `candidatePairs`；
- 为什么已经 Supported，却仍然 Open？需要看观察期限和事件发生时间；
- 为什么还有另一个重叠候选？需要看两个候选的成员和关系判断。

**因此，我现在认为，准备 F 的观察材料时，应该以&#x20;**`CandidateOccurrence`**&#x20;作为观察对象，同时区分“业务结果”“结果依据”“输入事实”“时间及状态约束”。不需要把每个字段画成独立事件，但也不能因为某个字段来自中间计算，就从观察材料中删掉它。**

这才是沿着实际结构理解 F 的输出，而不是重新发明一套字段结构。
