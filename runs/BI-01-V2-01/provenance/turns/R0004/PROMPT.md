[BI01-V2-01-R0004-23dee3405bd9e50d20b28f00]
work_id: BI-01
invocation_id: BI01-V2-01-R0004-23dee3405bd9e50d20b28f00
assignment_token: 41acd7cfe4480f624bb09a27e9365f58
role: professional
recipient: chatgpt-project:细节叙事生成_金标/chat:BI01-V2-执行
当前阶段：专业任务 BI01
当前职责：V2 S1 确定观察对象及业务问题

**每次实质业务推进，都以完整完成 Owner 确定的本用例当前阶段全部约定工作为目标。禁止自行将本轮目标缩成单个 Case、一组局部 Case、一个文件、一个接口或最近几项修复。当前重点只决定顺序，不能成为主动收工点。**

**本轮 S1/S2/S3 必须围绕固定两份预计算数据开展。S1 读取已有 I1–I3 的业务问题及设计前提，S2 通过 aidata 给 Owner 生成真实图、给 AI 对应 CSV/图层标记，S3 由 AI 基于这些结构化数据分析业务合理性、增量和反证。AI 现在不视觉看图，也不以重新验算或替换数据启动；遇到数据问题具名反馈。详见[专业 V2 当前入口](../../professional/v2/README.md)。**

业务事实、CaseFinding、待证假设、设计/方法问题、证据缺失与计算错误分别表达，不因单 Case 推成普遍规律。本轮固定数据若存在具名疑问，可在具体文件/行/As-Of 范围内核对并反馈；不得因为“缺正式 Feature”就默认重跑预计算 U2/U3 或把技术失败当作市场事实。

本轮确有获授权技术任务时，已有实现可用于核对方法、数据与实际调用，不能以列出读过的文件代替核验，也不照搬未完成的方法。代码示例只用于理解适用做法，不要求所有 BI-01 观察问题使用统一Header、生命周期或固定数量模块；没有该技术任务时不把这些工程事项列为专业观察前置。

发现实际结果、方法或已授权工程有可证实错误时，按当前有权处置处理直接受影响的位置；新任务不默认开展清理、全仓审计或恢复工程。当前重点只决定推进顺序，不成为完成局部即停止的理由。

从完整目标、当前 S1–S3 的真实业务工作和未决问题出发，连续完成已经明确的全部剩余。围绕本轮业务问题组织实际证据、Case/Source/Method/As-Of、必要挑战、所得认识和下游使用资格；确需技术补证时再连同输入、计算、输出及直接消费者一起处理。已授权的相关修改可以跨多个文件；不按文件数判断完成，也不为了显得完整修改无关文件。

**管理已经完成的材料采用、旧要求撤销、已知问题裁定和全局安排直接使用。推进者不再每轮重判全部历史、维护公共工作量、编写独立接收结论或设计主控派发。**但仍须理解实际业务、读取必要完整专业正文、查真实数据/结果/方法和直接依赖；涉及代码时核实实际实现，不能以管理未点名某个文件为由漏掉真正的使用位置。

BI-01 的专业观察问题、可信结果范围、阶段成果与必要工单来源仍是相应专业产物；减负不取消实质义务。Worker回交真实技术变化，执行Pro消费后向管理交业务结果，管理维护完整推进位置。地图不能代替正确专业方法和事实正文。

**本轮确有授权工程修改时，新增内部函数、Direct 入口、适配器或类型，不等于真实业务结果已经改变。实际使用的公共入口、生产者和消费者必须改接；旧错误路径仍在使用时，不得宣称相关职责已经退出。**

本轮确需 Worker 技术执行时，在有权任务、固定数据和现有工具具备后，优先直接用 aidata 形成图与同源数据并检验真实展示；只有具体预计算结果疑问才做受影响的有界核对。aidata 原则不改；确需通用修改必须先在 aidata 新建工作分支，不能直接改原分支，也不能在观察仓做第二套工具。未执行如实说明缺件。

方法未实现不能改称待校准；输入与调用未实现不能改称等数据；工程缺件不能改称市场正常 Pending。真实零、合法空、未成熟、输入缺失、未调用和读取失败分别说明。

受到实际容量、工具、真实权限或未定业务问题限制时，交出真实实物、具体限制及完整未完，并明确已知后继；不能以自设小目标达成作为停止理由。完整目标不授予跨仓、抢写或更改受保护业务的权限。

正确专业正文和本轮确有授权的工程细节禁止压缩、概述替换或只留历史链接。已否机制按现行处置连同专属使用位置删除，不换名称、换容器或移入 helper 保留。
**本轮备用回交通道：**优先按原权限把本次实质成果提交 GitHub。如果 Pro 的 GitHub 提交确实不可用，可通过实际可用的 MCP server 文件写入能力，将本轮对应文件、完整回交和必要 Return 打包成唯一 ZIP，写入 MCP server 一侧 `H:\fy\observe-iterate-share`，报告准确 ZIP 路径、关联 invocation 和打包内容；操作 Codex 从对应的 `/dwdhome/fy/observe-iterate-share` 校验收取，再依 [V2 轮次 ZIP 合同](../../runtime/operations/V2_ROUND_RECORD_CONTRACT.md) 核远端是否已有同轮成果、恢复并合法发布。ZIP 只用于**成果运输**，不自动意味着已提交、已接收或通过 Gate；写入/读取不具备时如实报告具体阻断，不虚称成功。

依实际 Binding 的专业 mode/source_reads，读 V2 业务目标、[04 原 I1–I3 业务依据](../../professional/v2/04_BI01_BUSINESS_BASELINE.md)、[05 固定 ZIP 和当前数据目录](../../professional/v2/05_BI01_FIXED_INPUT_DATA.md)、[06 U2/U3 叙事与细节设计 Source 导航](../../professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md)以及必要的原文正文。S2 由有权 Worker 在 `/dwdhome/fy/BASE_E6_2` 使用 aidata 处理 `/dwdhome/fy/资金管理` 的既定数据，S3 的专业 Pro 读图同源数据并给出合理/不合理、原因、反证、限制及后续观察。无需 AI 视觉看图/重算 U2/U3，也不得擅改 aidata 当前分支；图数/单 Case 不能作为全目标停点。

## Owner完整目的

# 专业 Agent V2：业务目标与三步观察迭代

## 1. 总意图：要从市场数据获得什么业务认识

**以已经形成的 U2/U3 特征细节设计和本轮事先验算、冻结的 rb/i/hc 真实数据为依据，检查现有业务设计是否准确描述了真实市场过程、是否实现了它原本声称的业务价值，发现不合理或无增量的地方，说明具体发生了什么、为什么不合理、影响什么判断，并为下一轮设计修订或进一步观察形成有证据的方向。**

在本轮更具体地回答两组问题：

1. **U2 找共同机会簇的位置和边界是否合理？** 图上的实际转折、簇形成位置、成员/组外对象、当时可知情况、后续运动是否能支持这一组织？是否错组、漏组、过早确认、只是静态板块重述，或者完全没有增加有用的信息？
2. **这些位置上的 U3 四方面能否辨别品种好不好做？** 对照成员和组外品种的真实运动、摩擦、保持、约束及可观察性，判断各方面究竟贡献了什么、哪些信息重复、哪些尚无输出或不足以支持判断。四方面的最终字段映射必须以 U3 有效设计与本次固定数据核实，不能把四个 Movement Bundle 与四种 Allocation Evidence 混为一谈。

**要得到的最实质成果**是：一系列可定位到真实行情与特征图的数据事实、合理或不合理的具体业务判断、原因和反证、已有设计带来的新增或没有新增的认识，以及哪些地方值得修改、保留、继续验证或停止。Owner 应能先看图中实际过程，再理解每项判断；AI 在本版本读取图所对应的数据，不要求看图像像素。

这是一项投资业务设计的观察和价值检验，不以 AI/Owner 谁做、运行了多少小时、完成几个 Case、画几张图或是否搭建新工具为成功标准。任务由谁执行、谁接收由现有长程运行合同处理，不占用总意图篇幅。

## 2. 本轮固定的对象、数据与原业务底稿

- 本轮对象固定为 **rb、i、hc**，使用已经提前验算并提供的两份 ZIP：上游 30m K 线/Zig/mid 贴近转折和下游 U2/U3 单尺度参考结果。**本轮不安排重算这批参考结果，也不因“应优先使用正式 Feature”而替换数据源**。
- 已积累的 OP-01/Q-01、I1/I2/I3 的选择理由、方法分层、证据边界需要作为本次业务起点认真读取；详见 [04 上一版业务底稿](04_BI01_BUSINESS_BASELINE.md)。这属于复用已有业务知识，不继承旧 run 的 Pro 回答、Gate、任务和执行状态。
- 两份输入的确切位置、包内容、身份差异和使用规则见 [05 固定数据与取用位置](05_BI01_FIXED_INPUT_DATA.md)。下游完整参考链目前只有**同一个 hc/i/rb Case 的 5 个 As-Of**，不是五个独立机会簇；较广范围的 C0/N/C1 raw 与少量 C2/U3 参考记录必须分别解释。新运行重新开展观察，不把上次 I4/I5/I6 的任何发现预设为应得结论。
- U3 原用例同时含四个 Movement Evidence Bundles 和四类 Allocation Evidence，不能只凭“四方面”三字猜出同一套字段。先根据 Owner 本轮意图、原设计和固定 CSV 逐项对应；**没有计算出来的方面必须如实标注，不得重算补齐或把 Withheld 写成 Quality**。

## 3. 业务工作三步（S1—S3）

### S1：确定具体观察对象及问题

在上述 **固定品种、固定已验算数据、固定业务方向** 内，梳理 U2 共同机会簇的具体发生位置和 U3 要检验的四方面；使用前期 OP-01/Q-01 和 Source/Method 背景，确定比较窗口、对象、期待观察的现象和主要反例。选择研究哪些局部不等于重选或扩大整个数据集。

**产物**：可执行的观察问题、已知设计期望、需要怎样在图上检查的内容、当前固定数据实际提供/未提供的字段。不得从一个方便的 Case 自动缩小整个目标。

### S2：决定画什么图并生成对应图与数据

a. 先按业务目的设计图：在哪些行情时间点展示 U2 的位置/成员/边界、U3 结果和组内外对照；明确价格轴、尺度、As-Of 与图中实际显示的对象。  
b. **直接使用已固定的两份预先验算数据**，通过 [aidata](01_AIDATA_CHART_AND_DATA.md) 生成 Owner 可查看的图及同范围数据。一般不补计算、不重新生产 U2/U3 结果。发现输入错误或来源不一致时向管理/Owner 反馈并标明影响，未经决定不擅自修补或替换固定数据。

**产物**：可实际打开的图、对应的 CSV/图层数据与版本、图上关键事实的位置及读图说明。图和数据应来自同一观察口径，而不是分别完成两套互不相干的工作。

### S3：根据对应数据给出观察想法

AI 当前只读取图所对应的**真实数据、必要图层导出与时间/标记信息**，不要求看 Bokeh 图片或经过视觉模型识图。围绕 S1 目的检验原业务设计：指出合理性、不合理性、成因、支持与反证、对原目标的贡献或没有贡献；将重要判断对到 S2 中 Owner 可查看的图。仍需深入时提出明确理由返回 S2，而不是凭旧结论直接跳到“设计错误”。

**产物**：以实际市场事实与图定位为依据的分析和观察想法，提出可检验的后续研究/设计修订方向，区分事实、案例发现、假设与仍未知。

## 4. 本轮不做的事情

- 不以“先重新验算 U2/U3”作为启动条件，也不默认重跑算法、生成新的正式特征、扩大品种或替换本轮两份数据。
- **不要求 AI 视觉看图**；aidata 当前没有提供这条视觉模型调用链，未来真正有需要时另议，不列为当前依赖或欠账。
- 不在本轮改动 aidata 既有分支；实际发现通用工具确需修改/新增时，必须先审查已有能力和 TODO，再在 **aidata 独立新分支** 处理，不得写入 aidata 当前分支，也不得在 observe-iterate 另做第二套画图工具。
- 不将当前参考计算直接升格为正式 U2 OpportunityCluster Commit/H1、U3 Quality、可交易性结论或资金/仓位决策。

## 5. 观察纪律与完成条件

实际转折、确认/可知时间、As-Of、Working/Completed、Reference/Shadow 与正式资格必须分开；图为人提供观察过程，数据给 AI 供分析，双方所依范围需一致，但“同图数据”不等于“AI 真的看到了图”。

业务认识必须说明它与单品种/静态品种分组等已有信息相比究竟多了什么，保留数据缺失、方法限制、反例和替代解释。上游数据身份疑问允许报告及针对性核对，但不得以此把整个新业务流程重新变成 I2/I3 的大规模验算工作。

本轮可以在 S2/S3 之间循环。整体结束应对 U2 位置与 U3 四方面的约定问题交出可由 Owner 定位图和数据核查的实质认识，或者精确指出受固定数据限制无法判断的部分及原因；有下一步真实行动或合法待决。图多、CSV 多、Pro 回复和脚本成功都不构成业务完成。

来源：daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md::full

## 本轮当前工作

# BI-01 V2：固定数据上的 U2 位置边界与 U3 四方面连续观察

task_id: BI01-V2-S123-OBSERVATION-01
work_id: BI-01
run_id: BI-01-V2-01
professional_mode: OBSERVATION_SCOPE
recipient_ref: chatgpt-project:细节叙事生成_金标/chat:BI01-V2-执行

此接收者为本次管理指定的首次专业聊天名称，尚未声称实际创建或投递。签发来自 R0001 管理；必须先完成原 Workmap 首次采用与实际发送核验。本任务整段承担 S1/S2/S3，不把 OBSERVATION_SCOPE 的首发标题解释成“只做 S1 后停”。三步由同一 professional 角色依完整方法连续完成，S2 可签实际 Worker 工单；不发生越权的角色转换。需要改变机器 mode 时由管理另签 Binding；普通 S2/S3 深入仍在本完整任务内继续，不为标签变化等待重批。

<a id="scope"></a>
## 1. 完整目标和采用依据

完整 Owner 目标为 `daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md::full`，必须读取原文，不能用本任务代替它。

从固定 rb/i/hc 行情及既有 U2/U3 细节设计判断：U2 共同机会的位置、成员/组外和可知边界合理与否；U3 Progress/Friction/Retention/ObservabilityAndConstraint 四束能否增加对品种好不好做的认识；交具体事实、原因、反证、替代解释、相对单品种/静态分组的增量或无增量，以及可检验的修订/继续/停止方向。原 I1—I3 的 OP-01/Q-01、输入和参考方法是业务起点，旧 run 的 Pro 回答、Gate、任务和预算不继承。

管理已经决定：本轮四方面是 Movement Bundles，而不是四个 Allocation Evidence 接口；完整参考 Case 没有非空组外，不得写组外优势；C2/H1 非正式、R03 Withheld 保持原资格；不重算固定数据。详情见 `reviews/management-R0001/DECISION.md`。推进者采用这些决定，不重做整套历史裁定；新冲突准确回管理。

<a id="focus"></a>
## 2. 当前顺序与全部观察对象

同时保留两层证据：

- 全范围 C0/N/C1 raw：304 个同实际 UTI 参考候选的覆盖，其中 205 个两成员候选可对照固定 Universe 内第三品种，99 个三成员候选不能在该 Universe 内制造组外。查看实际转折/可知时间、方向/类型、后续分化和候选未覆盖现象；这些 raw 行不是正式 Formation/OpportunityCluster，也不穷尽所有时间临近组。
- 完整单尺度参考 Case `refonly-ad8824a52552d7bffa91`：2021-04-30 15:00 的共同实际转折及 05-06、05-07、05-11、05-14、05-18 10:00 五个 As-Of。检查 C1/S/C2 的参考资格如何与实际行情、成员及 U3 路径对应。

先记录可复核的观察选择条件、预期和主要反例，不看完 Outcome 后只留下成功形态。没有必要为 304 条都建一套深图；不能因为完整链只一个 Case 就放弃广域位置/成员检查，也不能把没有完整链的范围伪装成已检验全 U3。

首个图数过程重点画清：actual 转折、knowledge/confirm、各 As-Of，Working 可见前缀与 Completed 实际终点/可知终点，以及在同一时钟下各品种的实际路径。05-11 截面 hc 38 bar、rb 33 bar、i 1 bar 的原记录只是需要解释的范围差异，不预设谁最好或算法有错。首个局部修通后立即推进已经明确的广域对照、四束和增量问题。

<a id="coverage"></a>
## 3. 适用义务及成果覆盖

| 义务 | 具体要回答什么 | 当前证据与完成限制 |
|---|---|---|
| S1/U2 位置、边界、及时性 | 当时可知的共同转折能否支持同轮方向组织？是否混组、漏出值得观察的第三品种、过晚或过早解释？ | 全范围 C0/N/C1 raw 与单 Case C1/S/C2 分层；无正式 Cluster 时只判断参考组织，不声称召回率/正确率 |
| S1/U3 四束 | 各束原设计字段、真实 CSV、单位、区间、状态和未输出项是什么？ | 按管理映射继续核实际方法；计数不冒充时长/密度，缺流动性容量成本不作交易承载判断 |
| S2 | 图上实际显示哪些对象、范围、标记？AI 得到的数据是否与 Owner 所看相同？ | 必须真实 aidata 页面与结构化视图，不能只交链接或 CSV 名字 |
| S3/对照与反证 | 相对 N、单品种行情和静态三品种分类，哪些身份/重复暴露/不确定性或成员辨别真正改变？ | 原观测字段共享路径时不算独立多票；Working/Completed、确认延迟和后验信息列替代解释 |
| S3/迭代收拢 | 保留、改什么、为何改、什么反例会推翻、还有何种固定数据内观察值得做？ | 没有数据的设计环节明确不可判断，不等于设计失败；完整下一行动或合法待决 |

<a id="sources"></a>
## 4. 源、数据和时间口径

首先完整读取 V2 00/04/05/06、01 aidata、02 观察想法、03 交接，锁 `11626f64bc64ae21e52108b2e47fafbbc1023615`。按 06 进入 `complex-systems-vocabulary@48f55f53e25d04e5b4b59fae1e652dd4b679c9d3` 的 Owner Decision、U2/U3 Narrative、Use Case 和承重 Witness；涉及公式/状态时读取其列出的 EAW exact Local Contract/MethodProfile。候选 ownerAccepted=false/NOT_APPLIED 不能因目录含 effective 就变正式。

两份固定输入完整文件名：`steel_U2_U3_执行结果_20261010.zip`、`rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip`。实际 Worker 目录 `/dwdhome/fy/资金管理`，aidata 工作区 `/dwdhome/fy/BASE_E6_2`。按 05 记录第一次真实消费的包/成员身份；B 外层历史 SHA 差异保留未知，不插值空 KLine、不改 value1/value2、actual/confirm/known，不用另一正式 Feature 替换。

图优先分品种自己的价格轴和共同时间定位。既有无量纲量仍须说明测量区间和生命周期。可以选择、过滤、连接现有行并作显示所需类型转换，但不得重跑特征、重分组、补新的质量/归一化指标或把显示变换写回预计算结果。若新的诊断运算实质变成另一批 U2/U3 结果，先回管理。

<a id="deliverables"></a>
## 5. 必须交付的实物与专业认识

在本 run `artifacts/` 保存真实专业正文与实际产物索引，不新增平行调度/管理系统。须有可执行观察问题和已记录选择理由；四束的原设计—实际字段—缺项—可判范围；Owner 可实际打开的 aidata 图、同 run/node/timespan 的对应数据、原件/代码版本/时间口径、真实打开与图层验证；每个重要判断能定位到图、时间、品种和 CSV 原行，含支持、反证、替代解释、与 N/静态组的增量及具体下一行动。

图数量和 Case 数没有预设完成配额。某方面确因固定结果未提供而不能判断，须给准确文件/字段/时间/设计责任和影响；不能仅写“数据不足”或补零。每次回交保留全部未完和最新合法续作，技术产物尚未被专业消费也应明说。

<a id="worker"></a>
## 6. 技术授权边界

执行 Pro 在实际 S1 窗口/图层明确后签 Worker 技术工单，Worker 才获具体施工任务。工单须说明固定源、窗口/As-Of、U2/U3 显示对象、预期图与同源数据和原状态；不能用预设空包或运行时默认节点重新选择 Case。

Worker 优先读 aidata 的 README、OWNER_INTENT_AND_RATIONALE、TODO、Development Guide、Run Brief/API 和相关现有代码，使用现成能力。固定 CSV 的合法接入是否存在由首次真实使用核实，不为此先做全库审计或重测 Owner 已检查的环境。正常配置、依赖补齐、输入表示和实际调用/核验在工单内可连续处理；不用封闭文件白名单、逐错误批准或“重要工程全回 Pro”阻断既有权限。确有必要通用能力缺口时，在 aidata 新独立分支修通并作真实回归和回用说明；不改其原分支，不在 observe-iterate/cgpterm 建第二套图或特征切片工具。改固定结果、未定业务语义或保护面仍交原责任。

AI 不视觉看图；Owner 看真实页面，执行 Pro 读对应结构化数据。没有视觉模型不触发新建设。无法取得同源数据才是具体输入缺件；只阻断其依赖判断，其他工作继续。

<a id="completion"></a>
## 7. 完整提交条件

对 U2 位置/边界与 U3 四束全部约定问题，已经形成 Owner 能按图和数据核查的实质认识，或者准确证明固定输入使哪些具体问题不可判断；有支持、反证、单品种/静态基线比较、已提供与缺失设计环节的分账，以及可执行后继/合法待决。第一张图、一个 Case、工具成功或某条 finding 修复不满足完整条件。执行自查不等于独立专业审查，管理与 Owner 接收分别发生，不自行关闭完整 Goal。

<a id="budget"></a>
## 8. 投入与管理触发

条件性预测和起点见管理决定 §8。每 4 个有效 Pro 回交从 R0001 INVOCATION 累计触发持续 EFFORT 复看；未达到里程碑也要回看，旧 run 不计入、新聊天不清零。主控用实际记录计数，不以自估时间或工具数代替。

<a id="result-trigger"></a>
### RESULT 条件

第一次形成可打开的真实行情/特征图、同源数据及关于 U2 边界/U3 差异的支持/反证/增量判断，触发非阻塞 M-REASSESS。完整任务达到 §7 时经 accept 交 M-CLOSE。单图或脚本成功不触发实质接收。

<a id="change-trigger"></a>
### CHANGE 条件

发现具体固定输入/时间/方法矛盾、Owner 新纠正或需要改变已定业务前提；或者连续两次实质回交仍只在来源、工具、格式/准备中循环，真实观察未推进。说明只影响哪些图、结论、消费者，触发 M-REASSESS；暂停受冲突影响的输出，不冻结无关主体。

<a id="effort-trigger"></a>
### EFFORT 条件

完整工作 ACTIVE 期间，以真实收到的有效专业及必要管理/接收结果累计每 4 次复看一次，采用 WHILE_WORK_ACTIVE，原起点 R0001；按 DR14 保持稳定责任、重复段和在途去重。非阻塞，不强制局部结案。已消费本段仍未完成完整工作时保留后继复看。

<a id="same-work"></a>
## 9. 同工作续作正文

继续本任务和当前实际 Binding。完整范围、权限、固定源与完成条件仍按本任务，集中重点采用上一份完整 QUESTION_WORK_RETURN.continuation_ref 的准确正文。当前重点只决定顺序，不能以单 Case/单图/局部修复为停点；不重做无新依据的已成工作。继续 S1/S2/S3、必要的真实 Worker 工单与技术结果专业消费，交实物、材料使用、全部未完、触发观察和一致的两份 Return。

<a id="accept"></a>
## 10. 管理接收正文

回 `chatgpt-project:细节叙事生成_金标/chat:BI01-V2-管理`。按 M-CLOSE 对完整 Owner 目标、本任务全部义务、真实图与同源数据、业务发现/反证/增量和所有未完作接收。区分技术完成、专业自查、独立审查、管理接受、Owner 取舍；不能因文件齐全通过全部业务。未达终点给明确连续后继，保留原投入起点和持续管理。

<a id="decide"></a>
## 11. 重要变化/投入管理正文

回同一管理聊天执行 M-REASSESS，带完整目标和当前任务、触发条件、具体原结果/证据及直接消费者。管理独立决定保留、停止深化、改真实安排、定向返修或请求具体 Owner 取舍；不让最近报错/remaining 默认取得全局最高优先。正常不受影响工作继续，完整剩余与预算不清零。

<a id="return-repair"></a>
## 12. 专业回交有限修复正文

回本任务实际专业聊天，仅补原回答确切缺失的字段、引用或续作一致性，保留原实物与资格，不为补字段造业务完成；确欠实质则继续原工作。一次同根因机械补交仍失败，交 §11 的管理接管。管理自己的缺件须回管理，不误派专业者代签。

<a id="parent"></a>
## 13. 新工作父关系

这是 Owner 明确 GO 的全新 BI-01-V2-01；没有本 run 已接受的旧专业 parent。原 I1—I3 是业务 Source，不是活动父任务；不继承旧 I4/I5/I6/Gate。首次 Binding 的 parent 为 NOT_APPLICABLE_NEW_CASE。

<a id="question-work-binding"></a>
## 14. QUESTION_WORK_BINDING

以下绑定引用已提交的 `444179c49ae2f926c287d3bf75b43e1eea44fcfc` 中完整且未被本次附加改变的业务正文。当前生效 task_payload 为包含本节的整份当前任务；运行端按真实发布 commit 冻结，不预填未来 SHA。首发及同工作续作均使用这份完整任务，不按最新 remaining 缩范围。source_reads 的 reuse_evidence=null 表示目标专业上下文仍需真正取得，不继承管理已读状态。

```json
{
  "schema": "question-work/v2",
  "kind": "BINDING",
  "work_id": "BI-01",
  "goal_ref": {"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md","selector":"full"},
  "plan_ref": {"repo":"daowei2026/observe-iterate","commit":"444179c49ae2f926c287d3bf75b43e1eea44fcfc","path":"runs/BI-01-V2-01/reviews/management-R0001/DECISION.md","selector":"#plan"},
  "full_scope_ref": {"repo":"daowei2026/observe-iterate","commit":"444179c49ae2f926c287d3bf75b43e1eea44fcfc","path":"runs/BI-01-V2-01/01_当前任务.md","selector":"full"},
  "batch_result": "在固定 rb/i/hc 的广域 C0/N/C1 raw 和唯一完整参考 Case 两个证据层中，形成实际 aidata 图与同源数据、U2 位置/成员边界及 U3 四个 Movement Bundle 的有据观察、反例、增量或无增量和可执行后继；完整责任不以局部 Case 或首图结束。",
  "question_ids": ["S1","S2","S3"],
  "question_definitions": [],
  "professional_mode": "OBSERVATION_SCOPE",
  "focus_ref": {"repo":"daowei2026/observe-iterate","commit":"444179c49ae2f926c287d3bf75b43e1eea44fcfc","path":"runs/BI-01-V2-01/01_当前任务.md","selector":"#focus"},
  "coverage_ref": {"repo":"daowei2026/observe-iterate","commit":"444179c49ae2f926c287d3bf75b43e1eea44fcfc","path":"runs/BI-01-V2-01/01_当前任务.md","selector":"#coverage"},
  "source_reads": [
    {"source":{"repo":"daowei2026/observe-iterate","commit":"e07034fbab080df85af57da4362d5a24119a8bbe","path":"runs/BI-01-V2-01/OWNER_START.md","selector":"full"},"requirement":"BOUNDARY","purpose":"实际新 run GO、固定输入和原有权限；旧 run 不继承","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md","selector":"full"},"requirement":"MODE_FULL","purpose":"Owner 完整目标、S1-S3 和禁止缩为单 Case","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"professional/v2/04_BI01_BUSINESS_BASELINE.md","selector":"full"},"requirement":"MODE_FULL","purpose":"OP-01/Q-01 与 I1-I3 业务起点，不继承旧 Gate 或 Pro 发现","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"professional/v2/05_BI01_FIXED_INPUT_DATA.md","selector":"full"},"requirement":"MODE_FULL","purpose":"固定两包、成员、哈希差异和实际取用路径","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md","selector":"full"},"requirement":"MODE_FULL","purpose":"人读叙事、用例、Witness 和具体 Local Contract/Method 的承重来源","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"professional/v2/01_AIDATA_CHART_AND_DATA.md","selector":"full"},"requirement":"MODE_FULL","purpose":"只读 aidata、图数同源、无像素要求和新分支保护","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"professional/v2/02_OBSERVATION_IDEAS_AND_VALIDATION.md","selector":"full"},"requirement":"MODE_FULL","purpose":"S3 市场事实、原因、反证、增量和下一行动","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"professional/v2/03_EXECUTION_HANDOFF.md","selector":"full"},"requirement":"MODE_FULL","purpose":"专业/Worker/管理/操作角色，真实技术工单与消费","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"444179c49ae2f926c287d3bf75b43e1eea44fcfc","path":"runs/BI-01-V2-01/reviews/management-R0001/DECISION.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"采用管理已经完成的来源/四束/空组外/非正式资格/优先级决定；不重判整套历史","reuse_evidence":null},
    {"source":{"repo":"daowei2026/complex-systems-vocabulary","commit":"48f55f53e25d04e5b4b59fae1e652dd4b679c9d3","path":"docs/network-dynamic-ceps-factory/OD_U2_U3_CAPITAL_VALUE_AND_ITERATION_DECISIONS_V0.1.0.md","selector":"full"},"requirement":"BOUNDARY","purpose":"U2 机会边界而非质量、U3 四资金接口与增量标准；历史实现任务不在本轮激活","reuse_evidence":null},
    {"source":{"repo":"daowei2026/complex-systems-vocabulary","commit":"48f55f53e25d04e5b4b59fae1e652dd4b679c9d3","path":"docs/network-dynamic-ceps-factory/U2_OPPORTUNITY_CLUSTER_SCALE_TURN_NARRATIVE_SPEC_V0.3.0.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"共同转折、可知时间、线段组织和机会边界的人读业务过程；保留非目标","reuse_evidence":null},
    {"source":{"repo":"daowei2026/complex-systems-vocabulary","commit":"48f55f53e25d04e5b4b59fae1e652dd4b679c9d3","path":"docs/network-dynamic-ceps-factory/U2_OPPORTUNITY_CLUSTER_SCALE_TURN_USE_CASE_CARD_V0.4.0.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"U2 详细字段、Formation/Validity/Separation 与反例；TypedDesign 不等于当前实跑算法","reuse_evidence":null},
    {"source":{"repo":"daowei2026/complex-systems-vocabulary","commit":"48f55f53e25d04e5b4b59fae1e652dd4b679c9d3","path":"docs/network-dynamic-ceps-factory/U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_NARRATIVE_SPEC_V0.3.0.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"U3 人读质量与 Current/Outcome 过程，不采用历史实施排程","reuse_evidence":null},
    {"source":{"repo":"daowei2026/complex-systems-vocabulary","commit":"48f55f53e25d04e5b4b59fae1e652dd4b679c9d3","path":"docs/network-dynamic-ceps-factory/U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_USE_CASE_CARD_V0.4.0.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"四个 Movement Bundle、四资金接口、时间和证据依赖的准确区别","reuse_evidence":null},
    {"source":{"repo":"daowei2026/feature-refinement-implementation-agent-evolution","commit":"ed62cd716cd603f0bcc566368c62caec7cdba554","path":"agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/material_catchup/current_inputs/source_to_behavior/U2_SOURCE_OCCURRENCE_EPISODE_NODE_BEHAVIOR_LOCAL_CONTRACT_RETROFIT_0.1.0-candidate.1.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"本次 C0/N 的实际/可知、Episode、单品种画像解释；不是令其全部生产实施","reuse_evidence":null},
    {"source":{"repo":"daowei2026/feature-refinement-implementation-agent-evolution","commit":"ed62cd716cd603f0bcc566368c62caec7cdba554","path":"agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/material_catchup/current_inputs/relation_to_cluster/U2_RELATION_FORMATION_QUALIFICATION_PHYSICALIZATION_LOCAL_CONTRACT_RETROFIT_0.1.0-candidate.1.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"解释 C1/S/C2 的 Formation/Qualification/Validity/Separation 正确职责与边界，不能用 raw 代 formal","reuse_evidence":null},
    {"source":{"repo":"daowei2026/feature-refinement-implementation-agent-evolution","commit":"ed62cd716cd603f0bcc566368c62caec7cdba554","path":"agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u3-retrofit-20260907/artifacts/material_catchup/effective_mission_a/04_movement_current/02_U3_MA_LOCAL_CONTRACT_MOVEMENT_01.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"核实际使用的 R02/R03 字段、时间和成熟度；不把候选阈值冒充冻结数据实际算法","reuse_evidence":null},
    {"source":{"repo":"daowei2026/feature-refinement-implementation-agent-evolution","commit":"ea126840aa68701135491572a453bf88e96ca58d","path":"agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/mission_a_r28_role_domain_20260917/UPSTREAM_FIRST_EDITION_PROFILE.md","selector":"full"},"requirement":"PROVENANCE_TRIGGER","purpose":"仅在所用参考方法阈值解释命中时区分原 Δ 合同和临时 Shadow 参数；不是当前生产采用或补算要求","reuse_evidence":null},
    {"source":{"source_kind":"ATTACHMENT","attachment_id":"file_0000000035c481fdbbfb82af5e57a96c","filename":"steel_U2_U3_执行结果_20261010.zip","selector":"baseline_U2_C0_N_C1/ 与 single_scale_U2_C1_S_C2_U3/ 的原 CSV；按实际观察字段/窗口读取","sha256":"7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c"},"requirement":"FOCUS_FULL","purpose":"实际预计算参考结果，不能用本任务的统计摘要代原件","reuse_evidence":null},
    {"source":{"source_kind":"ATTACHMENT","attachment_id":"file_000000008c7481fd8604a79973ec5951","filename":"rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip","selector":"manifest.json、数据说明.md 与相应 rb/hc/i KLine/Zig/mid CSV 的本次观察范围","sha256":"4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987"},"requirement":"FOCUS_FULL","purpose":"真实路径和原转折来源；外层历史哈希差异保留，不自动换源","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"runtime/dual_route_execution/DR14_QUESTION_WORK_CONTRACT.md","selector":"full"},"requirement":"BOUNDARY","purpose":"完整工作、最新 continuation、Return 和持续管理触发","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"runtime/overlay/13_角色回交与主控接续协议.md","selector":"full"},"requirement":"BOUNDARY","purpose":"真实身份、实物、资格与两份回交及运输失败处理","reuse_evidence":null}
  ],
  "deliverables_ref": {"repo":"daowei2026/observe-iterate","commit":"444179c49ae2f926c287d3bf75b43e1eea44fcfc","path":"runs/BI-01-V2-01/01_当前任务.md","selector":"#deliverables"},
  "completion_ref": {"repo":"daowei2026/observe-iterate","commit":"444179c49ae2f926c287d3bf75b43e1eea44fcfc","path":"runs/BI-01-V2-01/01_当前任务.md","selector":"#completion"},
  "budget_ref": {"repo":"daowei2026/observe-iterate","commit":"444179c49ae2f926c287d3bf75b43e1eea44fcfc","path":"runs/BI-01-V2-01/reviews/management-R0001/DECISION.md","selector":"#budget"},
  "parent": {"status":"NOT_APPLICABLE_NEW_CASE","ref":null,"reason_ref":{"repo":"daowei2026/observe-iterate","commit":"444179c49ae2f926c287d3bf75b43e1eea44fcfc","path":"runs/BI-01-V2-01/01_当前任务.md","selector":"#parent"}},
  "routes": {
    "same_work":{"recipient_role":"professional","recipient_ref":"chatgpt-project:细节叙事生成_金标/chat:BI01-V2-执行","instructions_ref":{"repo":"daowei2026/observe-iterate","commit":"444179c49ae2f926c287d3bf75b43e1eea44fcfc","path":"runs/BI-01-V2-01/01_当前任务.md","selector":"#same-work"}},
    "accept":{"recipient_role":"management","recipient_ref":"chatgpt-project:细节叙事生成_金标/chat:BI01-V2-管理","instructions_ref":{"repo":"daowei2026/observe-iterate","commit":"444179c49ae2f926c287d3bf75b43e1eea44fcfc","path":"runs/BI-01-V2-01/01_当前任务.md","selector":"#accept"}},
    "decide":{"recipient_role":"management","recipient_ref":"chatgpt-project:细节叙事生成_金标/chat:BI01-V2-管理","instructions_ref":{"repo":"daowei2026/observe-iterate","commit":"444179c49ae2f926c287d3bf75b43e1eea44fcfc","path":"runs/BI-01-V2-01/01_当前任务.md","selector":"#decide"}},
    "return_repair":{"recipient_role":"professional","recipient_ref":"chatgpt-project:细节叙事生成_金标/chat:BI01-V2-执行","instructions_ref":{"repo":"daowei2026/observe-iterate","commit":"444179c49ae2f926c287d3bf75b43e1eea44fcfc","path":"runs/BI-01-V2-01/01_当前任务.md","selector":"#return-repair"}}
  },
  "triggers": [
    {"trigger_id":"BI01V2-FIRST-GROUNDED-OBSERVATION","kind":"RESULT","condition_ref":{"repo":"daowei2026/observe-iterate","commit":"444179c49ae2f926c287d3bf75b43e1eea44fcfc","path":"runs/BI-01-V2-01/01_当前任务.md","selector":"#result-trigger"},"signal_key":"BI01V2_FIRST_GROUNDED_OBSERVATION","route":{"recipient_role":"management","recipient_ref":"chatgpt-project:细节叙事生成_金标/chat:BI01-V2-管理","instructions_ref":{"repo":"daowei2026/observe-iterate","commit":"444179c49ae2f926c287d3bf75b43e1eea44fcfc","path":"runs/BI-01-V2-01/01_当前任务.md","selector":"#decide"}},"blocking":false,"effort_limit":null,"obligation_id":"BI01V2_FIRST_RESULT_REASSESSMENT","cycle_id":"initial","rearm_ref":null,"repeat":"ONCE"},
    {"trigger_id":"BI01V2-SUBSTANTIVE-CHANGE","kind":"CHANGE","condition_ref":{"repo":"daowei2026/observe-iterate","commit":"444179c49ae2f926c287d3bf75b43e1eea44fcfc","path":"runs/BI-01-V2-01/01_当前任务.md","selector":"#change-trigger"},"signal_key":"BI01V2_SUBSTANTIVE_CHANGE","route":{"recipient_role":"management","recipient_ref":"chatgpt-project:细节叙事生成_金标/chat:BI01-V2-管理","instructions_ref":{"repo":"daowei2026/observe-iterate","commit":"444179c49ae2f926c287d3bf75b43e1eea44fcfc","path":"runs/BI-01-V2-01/01_当前任务.md","selector":"#decide"}},"blocking":false,"effort_limit":null,"obligation_id":"BI01V2_CHANGE_REASSESSMENT","cycle_id":"initial","rearm_ref":null,"repeat":"ONCE"},
    {"trigger_id":"BI01V2-EFFORT-4","kind":"EFFORT","condition_ref":{"repo":"daowei2026/observe-iterate","commit":"444179c49ae2f926c287d3bf75b43e1eea44fcfc","path":"runs/BI-01-V2-01/01_当前任务.md","selector":"#effort-trigger"},"signal_key":"BI01V2_EFFECTIVE_PRO_RESULTS","route":{"recipient_role":"management","recipient_ref":"chatgpt-project:细节叙事生成_金标/chat:BI01-V2-管理","instructions_ref":{"repo":"daowei2026/observe-iterate","commit":"444179c49ae2f926c287d3bf75b43e1eea44fcfc","path":"runs/BI-01-V2-01/01_当前任务.md","selector":"#decide"}},"blocking":false,"effort_limit":{"unit":"EFFECTIVE_CALLS","limit":4,"count_from_ref":{"repo":"daowei2026/observe-iterate","commit":"c792c8616b445060e738d981ea272c0d170ff5f8","path":"runs/BI-01-V2-01/provenance/turns/R0001/INVOCATION.json","selector":"full"}},"obligation_id":"BI01V2_CONTINUOUS_EFFORT_REVIEW","cycle_id":"initial","rearm_ref":null,"repeat":"WHILE_WORK_ACTIVE"}
  ],
  "explicit_no_trigger_reason_ref": null
}
```

来源：daowei2026/observe-iterate@81533abbced55b3af14a428dec9cbf8353fc8286:runs/BI-01-V2-01/01_当前任务.md::full

## 本轮原文与位置

本次原始要求：`daowei2026/observe-iterate@444179c49ae2f926c287d3bf75b43e1eea44fcfc:runs/BI-01-V2-01/01_当前任务.md::#same-work`
当前生效任务：`daowei2026/observe-iterate@81533abbced55b3af14a428dec9cbf8353fc8286:runs/BI-01-V2-01/01_当前任务.md::full`
当前任务采用依据：`daowei2026/observe-iterate@f87a9a64f4f0fa3ead13b9ee7c108f87847a581a:runs/BI-01-V2-01/reviews/management-R0002/DECISION.md::#adoption`
上一轮实际采用的任务绑定：`daowei2026/observe-iterate@81533abbced55b3af14a428dec9cbf8353fc8286:runs/BI-01-V2-01/01_当前任务.md::L124-L177`
完整工作范围：`daowei2026/observe-iterate@444179c49ae2f926c287d3bf75b43e1eea44fcfc:runs/BI-01-V2-01/01_当前任务.md::full`
本次实际证据：`daowei2026/observe-iterate@81533abbced55b3af14a428dec9cbf8353fc8286:runs/BI-01-V2-01/reviews/WORKMAP_INTAKE_CURRENT.json::full`
本次实际证据：`daowei2026/observe-iterate@ccc3f74c38549759a17d8a48ddf63b4994c18cc8:runs/BI-01-V2-01/reviews/independent/WORKMAP_READER_INITIAL.md::full`

## 本次直接读取的上下文

- BOUNDARY：`daowei2026/observe-iterate@e07034fbab080df85af57da4362d5a24119a8bbe:runs/BI-01-V2-01/OWNER_START.md::full`
  用途与边界：实际新 run GO、固定输入和原有权限；旧 run 不继承
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md::full`
  用途与边界：Owner 完整目标、S1-S3 和禁止缩为单 Case
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:professional/v2/04_BI01_BUSINESS_BASELINE.md::full`
  用途与边界：OP-01/Q-01 与 I1-I3 业务起点，不继承旧 Gate 或 Pro 发现
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:professional/v2/05_BI01_FIXED_INPUT_DATA.md::full`
  用途与边界：固定两包、成员、哈希差异和实际取用路径
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md::full`
  用途与边界：人读叙事、用例、Witness 和具体 Local Contract/Method 的承重来源
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:professional/v2/01_AIDATA_CHART_AND_DATA.md::full`
  用途与边界：只读 aidata、图数同源、无像素要求和新分支保护
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:professional/v2/02_OBSERVATION_IDEAS_AND_VALIDATION.md::full`
  用途与边界：S3 市场事实、原因、反证、增量和下一行动
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:professional/v2/03_EXECUTION_HANDOFF.md::full`
  用途与边界：专业/Worker/管理/操作角色，真实技术工单与消费
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@444179c49ae2f926c287d3bf75b43e1eea44fcfc:runs/BI-01-V2-01/reviews/management-R0001/DECISION.md::full`
  用途与边界：采用管理已经完成的来源/四束/空组外/非正式资格/优先级决定；不重判整套历史
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/complex-systems-vocabulary@48f55f53e25d04e5b4b59fae1e652dd4b679c9d3:docs/network-dynamic-ceps-factory/OD_U2_U3_CAPITAL_VALUE_AND_ITERATION_DECISIONS_V0.1.0.md::full`
  用途与边界：U2 机会边界而非质量、U3 四资金接口与增量标准；历史实现任务不在本轮激活
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/complex-systems-vocabulary@48f55f53e25d04e5b4b59fae1e652dd4b679c9d3:docs/network-dynamic-ceps-factory/U2_OPPORTUNITY_CLUSTER_SCALE_TURN_NARRATIVE_SPEC_V0.3.0.md::full`
  用途与边界：共同转折、可知时间、线段组织和机会边界的人读业务过程；保留非目标
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/complex-systems-vocabulary@48f55f53e25d04e5b4b59fae1e652dd4b679c9d3:docs/network-dynamic-ceps-factory/U2_OPPORTUNITY_CLUSTER_SCALE_TURN_USE_CASE_CARD_V0.4.0.md::full`
  用途与边界：U2 详细字段、Formation/Validity/Separation 与反例；TypedDesign 不等于当前实跑算法
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/complex-systems-vocabulary@48f55f53e25d04e5b4b59fae1e652dd4b679c9d3:docs/network-dynamic-ceps-factory/U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_NARRATIVE_SPEC_V0.3.0.md::full`
  用途与边界：U3 人读质量与 Current/Outcome 过程，不采用历史实施排程
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/complex-systems-vocabulary@48f55f53e25d04e5b4b59fae1e652dd4b679c9d3:docs/network-dynamic-ceps-factory/U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_USE_CASE_CARD_V0.4.0.md::full`
  用途与边界：四个 Movement Bundle、四资金接口、时间和证据依赖的准确区别
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/feature-refinement-implementation-agent-evolution@ed62cd716cd603f0bcc566368c62caec7cdba554:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/material_catchup/current_inputs/source_to_behavior/U2_SOURCE_OCCURRENCE_EPISODE_NODE_BEHAVIOR_LOCAL_CONTRACT_RETROFIT_0.1.0-candidate.1.md::full`
  用途与边界：本次 C0/N 的实际/可知、Episode、单品种画像解释；不是令其全部生产实施
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/feature-refinement-implementation-agent-evolution@ed62cd716cd603f0bcc566368c62caec7cdba554:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/material_catchup/current_inputs/relation_to_cluster/U2_RELATION_FORMATION_QUALIFICATION_PHYSICALIZATION_LOCAL_CONTRACT_RETROFIT_0.1.0-candidate.1.md::full`
  用途与边界：解释 C1/S/C2 的 Formation/Qualification/Validity/Separation 正确职责与边界，不能用 raw 代 formal
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/feature-refinement-implementation-agent-evolution@ed62cd716cd603f0bcc566368c62caec7cdba554:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u3-retrofit-20260907/artifacts/material_catchup/effective_mission_a/04_movement_current/02_U3_MA_LOCAL_CONTRACT_MOVEMENT_01.md::full`
  用途与边界：核实际使用的 R02/R03 字段、时间和成熟度；不把候选阈值冒充冻结数据实际算法
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 本次不主张已读复用。

- PROVENANCE_TRIGGER：`daowei2026/feature-refinement-implementation-agent-evolution@ea126840aa68701135491572a453bf88e96ca58d:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/runs/u2-retrofit-20260907/artifacts/mission_a_r28_role_domain_20260917/UPSTREAM_FIRST_EDITION_PROFILE.md::full`
  用途与边界：仅在所用参考方法阈值解释命中时区分原 Δ 合同和临时 Shadow 参数；不是当前生产采用或补算要求
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 本次不主张已读复用。

- FOCUS_FULL；用途与边界：实际预计算参考结果，不能用本任务的统计摘要代原件
  原始来源：`{"attachment_id": "file_0000000035c481fdbbfb82af5e57a96c", "filename": "steel_U2_U3_执行结果_20261010.zip", "selector": "baseline_U2_C0_N_C1/ 与 single_scale_U2_C1_S_C2_U3/ 的原 CSV；按实际观察字段/窗口读取", "sha256": "7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c", "source_kind": "ATTACHMENT"}`
  原件由接收者实际取得；本工具未读取或验证原件。

- FOCUS_FULL；用途与边界：真实路径和原转折来源；外层历史哈希差异保留，不自动换源
  原始来源：`{"attachment_id": "file_000000008c7481fd8604a79973ec5951", "filename": "rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip", "selector": "manifest.json、数据说明.md 与相应 rb/hc/i KLine/Zig/mid CSV 的本次观察范围", "sha256": "4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987", "source_kind": "ATTACHMENT"}`
  原件由接收者实际取得；本工具未读取或验证原件。

- BOUNDARY：`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:runtime/dual_route_execution/DR14_QUESTION_WORK_CONTRACT.md::full`
  用途与边界：完整工作、最新 continuation、Return 和持续管理触发
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:runtime/overlay/13_角色回交与主控接续协议.md::full`
  用途与边界：真实身份、实物、资格与两份回交及运输失败处理
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

读取Owner完整要求、生效完整任务和输入输出地图，不能用最新remaining替全部责任。按source_reads取得准确正文用于判断，已读未变且可恢复者复用；不递归扫无关历史，不用索引/hash/旧回执代正文。

旧包中已被Owner否定的多余任务，必须由原有权责任者从当前正文、任务、前置、接收和后继删除；只为其存在的辅助代码与检查交原实现者删除。禁止继续完善、改名或列为暂缓/未来优化。不能只在顶部写新原则却继续采用相反正文。真实业务方法、时间、身份、状态、正式输出与消费者保留，技术机制替换回正常平台。正确正文禁止任何压缩或摘要替换。历史提交和实际记录不倒改；历史可追溯不授后续派发。通用材料维护不自动取得用例任务写权。

当前执行材料由管理和有权任务责任者明确采用。推进者取得实际需要的正确正文，不能用管理概述替代业务细节；也不要求每轮重读全部历史和已撤完整任务。

发现新的实质冲突时，给出准确位置与受影响结论，按原责任处理。来源不足只限制真正依赖的判断，不用旧快照补造事实，也不冻结无关工作。

方法版本、业务合同版本、源码版本和运行数据分别保持准确，不随一次方法更新全部追 latest。

运行事实（来自现有记录）：
观察时间：2026-10-17T18:00:33.988454+00:00
有效回交数：3

按既有协议交完整实质回答及ROLE_RETURN/QUESTION_WORK_RETURN，来源、未执行和资格如实保留，不新增控制表，不重抄协调者已存提示。完整任务未完成就保留完整责任及连续后继，局部交付不自设停点。要求GitHub提交时普通快进并fresh回读，最后commit message带turn complete及本轮invocation_id，无invocation时简要标明执行身份；不造空提交。

专业者回交实际实物、必要自检／执行结果、具体限制及完整未完，不代写管理接收、全局预算或主控派发。管理回交已完成的判断、实际处置和可执行后继，不以问题目录代替决定。

没有完整完成时，说明真实停止原因及已经明确的下一步；不得以自设局部目标完成作为结束解释。
