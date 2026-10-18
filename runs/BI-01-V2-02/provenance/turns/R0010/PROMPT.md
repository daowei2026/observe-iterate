[BI01-V2-02-R0010-20261018T175239Z-75847f6b]
work_id: BI-01
invocation_id: BI01-V2-02-R0010-20261018T175239Z-75847f6b
assignment_token: BI01-V2-02-PRO-CONSUME-5754a4a7d26045d689b1e008a016a987
role: professional
recipient: chatgpt:细节叙事生成_金标:BI01-V202-执行
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

依新 run 实际有权 Binding 的专业 mode/source_reads，必须先读 [00 业务目的](../../professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md)、[07 场景方法](../../professional/v2/07_BUSINESS_SCENE_OBSERVATION_METHOD.md)、[06 U2/U3 Narrative/Use Case 原文导航](../../professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md)、[04 原业务背景](../../professional/v2/04_BI01_BUSINESS_BASELINE.md)和[05 固定包](../../professional/v2/05_BI01_FIXED_INPUT_DATA.md)。由专业者**从真实基础 K线/贴近转折行情自主选择值得研究的共同方向机会和成员强弱场景**（不预分类），有权 Worker 在 `/dwdhome/fy/BASE_E6_2` 先形成必要基础图/同图数据，专业者对 `/dwdhome/fy/资金管理` 的冻结源与 U2/U3 相关字段作对照，重点检验四束**当时能否辨别后续成员质量**及原 C0/N 已有信息；回顾性选例、合法 Outcome 与缺少正式 U3 分开。旧图可核来源与渲染后复用，不默认重画320图；不能以字段审计/小 Case 收工，不修改 aidata 原分支或擅自补算正式质量。

## Owner完整目的

# 专业 Agent V2：业务目标与叙事场景先行的三步观察迭代

## 1. 总意图：要从市场数据获得什么业务认识

**以已经形成的 U2/U3 特征细节设计和本轮事先验算、冻结的 rb/i/hc 真实数据为依据，检查现有业务设计是否准确描述了真实市场过程、是否实现了它原本声称的业务价值，发现不合理或无增量的地方，说明具体发生了什么、为什么不合理、影响什么判断，并为下一轮设计修订或进一步观察形成有证据的方向。**

**本次必要的方法修正：先读 U2/U3 Owner Decision、Narrative 和 Use Case，明确叙事想在真实市场行情中解决什么业务场景的什么问题；先用基础 K 线、Zig、贴近转折发现值得研究的共同方向运动位置，再核 U2 的位置和成员、U3 四方面的当时质量辨别及后续实际运动。** 不能从某几个指标、raw 候选、字段异常或技术易取性直接倒推场景与选例，也不预设场景分类、样本配额、强弱阈值或赢家。详见 [07 业务场景观察方法](07_BUSINESS_SCENE_OBSERVATION_METHOD.md)。这次应从真实市场行情中理解成员强弱，随后实际运动是否支持必须检验。

在本轮更具体地回答两组问题：

1. **对于基础行情中有业务意义的共同方向场景，U2 找共同机会簇的位置和边界是否合理？** 图上的实际转折、簇形成位置、成员/组外对象、当时可知情况、后续运动是否能支持这一组织？是否错组、漏组、过早确认、只是静态板块重述，或者完全没有增加有用的信息？
2. **这些场景中，U3 四方面能否在合法 As-Of 区分成员后续运动质量？** 对照成员和组外品种的真实运动、摩擦、保持、约束及可观察性，判断各方面究竟贡献了什么、哪些信息重复、哪些尚无输出或不足以支持判断。四方面的最终字段映射必须以 U3 有效设计与本次固定数据核实，不能把四个 Movement Bundle 与四种 Allocation Evidence 混为一谈。

U2 负责组织共同机会身份及成员边界，并不负责只寻找或只确认后验赢家；U3 才评价成员运动质量，比较还应考虑整组都弱或当时无法判断的情况。U3 的 Progress、Friction、Retention、ObservabilityAndConstraint 必须与已有单品种 C0/N、原 K 线和简单共同事件关联对照，说明真正的增量。

**要得到的最实质成果**是：一系列可定位到真实行情与特征图的数据事实、合理或不合理的具体业务判断、原因和反证、已有设计带来的新增或没有新增的认识，以及哪些地方值得修改、保留、继续验证或停止。Owner 应能先看图中实际过程，再理解每项判断；AI 在本版本读取图所对应的数据，不要求看图像像素。

这是一项投资业务设计的观察和价值检验，不以 AI/Owner 谁做、运行了多少小时、完成几个 Case、画几张图或是否搭建新工具为成功标准。任务由谁执行、谁接收由现有长程运行合同处理，不占用总意图篇幅。

## 2. 本轮固定的对象、数据与原业务底稿

- 本轮对象固定为 **rb、i、hc**，使用已经提前验算并提供的两份 ZIP：上游 30m K 线/Zig/mid 贴近转折和下游 U2/U3 单尺度参考结果。**本轮不安排重算这批参考结果，也不因“应优先使用正式 Feature”而替换数据源**。
- 已积累的 OP-01/Q-01、I1/I2/I3 的选择理由、方法分层、证据边界需要作为本次业务起点认真读取；详见 [04 上一版业务底稿](04_BI01_BUSINESS_BASELINE.md)。这属于复用已有业务知识，不继承旧 run 的 Pro 回答、Gate、任务和执行状态。
- 两份输入的确切位置、包内容、身份差异和使用规则见 [05 固定数据与取用位置](05_BI01_FIXED_INPUT_DATA.md)。下游完整参考链目前只有**同一个 hc/i/rb Case 的 5 个 As-Of**，不是五个独立机会簇；较广范围的 C0/N/C1 raw 与少量 C2/U3 参考记录必须分别解释。新运行重新开展观察，不把上次 I4/I5/I6 的任何发现预设为应得结论。
- U3 原用例同时含四个 Movement Evidence Bundles 和四类 Allocation Evidence，不能只凭“四方面”三字猜出同一套字段。先根据 Owner 本轮意图、原设计和固定 CSV 逐项对应；**没有计算出来的方面必须如实标注，不得重算补齐或把 Withheld 写成 Quality**。

## 3. 业务工作三步（S1—S3）

### S1：确定具体观察对象及问题

在上述 **固定品种、固定已验算数据、固定业务方向** 内，先实际阅读叙事和业务详细设计，明确共同方向机会、U2 机会组织及 U3 质量辨别的原始目的；优先用基础 K 线、Zig、贴近转折和对应数据寻找有研究价值的具体位置，再调查 U2 在这些位置是否找到合理的机会及成员。结合前期 OP-01/Q-01 和 Source/Method 背景确定比较窗口、对象、期待观察的现象和主要反例。具体观察类型由真实行情和专业判断决定，**不预设场景分类**；选择研究哪些局部不等于重选或扩大整个数据集。

**产物**：叙事原本想处理的业务场景及问题、从基础行情选中位置的理由、可执行的观察问题、已知设计期望、需要怎样在图上检查的内容、当前固定数据实际提供/未提供的字段。不得从一个方便的 Case 自动缩小整个目标。

### S2：决定画什么图并生成对应图与数据

a. **先提供基础行情图**：从 K 线、Zig 和贴近转折看真实共同方向机会及成员差异，按实际选择的场景再决定哪些时间点叠加 U2 位置/成员/边界、U3 结果和组内外对照；明确价格轴、尺度、As-Of 与图中实际显示的对象。  
b. **直接使用已固定的两份预先验算数据**，通过 [aidata](01_AIDATA_CHART_AND_DATA.md) 生成 Owner 可查看的图及同范围数据。一般不补计算、不重新生产 U2/U3 结果。发现输入错误或来源不一致时向管理/Owner 反馈并标明影响，未经决定不擅自修补或替换固定数据。

**产物**：可实际打开的图、对应的 CSV/图层数据与版本、图上关键事实的位置及读图说明。图和数据应来自同一观察口径，而不是分别完成两套互不相干的工作。

旧 `BI-01-V2-01` 的图和同源数据可核实版本、输入、场景相关性及浏览器实际渲染后按需复用，不因此继承旧选样或业务接收资格；不为新 run 无意义重画已有图。

### S3：根据对应数据给出观察想法

AI 当前只读取图所对应的**真实数据、必要图层导出与时间/标记信息**，不要求看 Bokeh 图片或经过视觉模型识图。围绕 S1 目的检验原业务设计：指出合理性、不合理性、成因、支持与反证、对原目标的贡献或没有贡献；将重要判断对到 S2 中 Owner 可查看的图。仍需深入时提出明确理由返回 S2，而不是凭旧结论直接跳到“设计错误”。

**产物**：以实际市场事实与图定位为依据的分析和观察想法，提出可检验的后续研究/设计修订方向，区分事实、案例发现、假设与仍未知。

在具名场景中先记录 U3 Progress/Friction/Retention/ObservabilityAndConstraint **当时合法可知**的成员差异或无法判断，再将后续实际运动与合法 Outcome/End/Horizon（若没有则明确为探索性显示范围）对照，说明支持、反证、证据不足以及比 C0/N 多出什么。回顾性发现赢家绝不产生“提前识别”资格。

## 4. 本轮不做的事情

- 不以“先重新验算 U2/U3”作为启动条件，也不默认重跑算法、生成新的正式特征、扩大品种或替换本轮两份数据。
- **不要求 AI 视觉看图**；aidata 当前没有提供这条视觉模型调用链，未来真正有需要时另议，不列为当前依赖或欠账。
- 不在本轮改动 aidata 既有分支；实际发现通用工具确需修改/新增时，必须先审查已有能力和 TODO，再在 **aidata 独立新分支** 处理，不得写入 aidata 当前分支，也不得在 observe-iterate 另做第二套画图工具。
- 不将当前参考计算直接升格为正式 U2 OpportunityCluster Commit/H1、U3 Quality、可交易性结论或资金/仓位决策。

## 5. 观察纪律与完成条件

实际转折、确认/可知时间、As-Of、Working/Completed、Reference/Shadow 与正式资格必须分开；图为人提供观察过程，数据给 AI 供分析，双方所依范围需一致，但“同图数据”不等于“AI 真的看到了图”。

用于发现典型场景的后续价格不能回填历史 Current；若当前 ZIP 缺完整正式 U3 或 Outcome，只能报告哪些局部证据已观察、哪些四方面充分性问题尚不能判定，不擅自补算或把 N 当成正式 U3。

业务认识必须说明它与单品种/静态品种分组等已有信息相比究竟多了什么，保留数据缺失、方法限制、反例和替代解释。上游数据身份疑问允许报告及针对性核对，但不得以此把整个新业务流程重新变成 I2/I3 的大规模验算工作。

本轮可以在 S2/S3 之间循环。整体结束应对 U2 位置与 U3 四方面的约定问题交出可由 Owner 定位图和数据核查的实质认识，或者精确指出受固定数据限制无法判断的部分及原因；有下一步真实行动或合法待决。图多、CSV 多、Pro 回复和脚本成功都不构成业务完成。

来源：daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md::full

## 本轮当前工作

# BI-01-V2-02 当前专业任务：场景先行的 U2/U3 连续业务观察

task_id: BI01-V2-02-S123-SCENE-OBSERVATION-01
work_id: BI-01
run_id: BI-01-V2-02
professional_mode: OBSERVATION_SCOPE
recipient_role: professional
recipient_ref: chatgpt:细节叙事生成_金标:BI01-V202-执行
signed_by: BI01-V2-02-R0001-20261018T130131Z-7f26abeb

本任务在 Workmap 首次采用并实际投递前只是**已签发、未发送**。`OBSERVATION_SCOPE` 表示首发当前顺序，不把责任缩成 S1；同一执行 Pro 连续承担 S1、S2、S3，S2/S3 可以循环。第一张图、一个 Case、一个局部修复或一次 Return 都不是主动停点。

<a id="scope"></a>
## 1. 完整目标与边界

从固定 rb/i/hc 的真实基础行情和已验算 U2/U3 结果，检验：

1. 基础行情中哪些共同方向运动位置真正有业务研究价值，成员之间出现了什么强弱、摩擦、保持或无法判断的差异；
2. U2 是否在恰当位置组织出同一轮机会身份，成员和第三对象/组外边界是否合理、及时且可知；
3. U3 的 Progress、Friction、Retention、ObservabilityAndConstraint 四束在当时合法 As-Of 是否增加了对成员后续运动质量的辨别，后续事实支持、削弱、反证还是仍未知；
4. 相对原 KLine、C0/N 单品种画像、静态三品种和简单共同事件关联，U2/U3 真正增加了什么，或没有增加什么；
5. 哪些设计应保留、修改、继续验证或停止。

本任务不输出正式资金、仓位、交易动作、因果 Driver/SelfSustain、数学分岔或永久品种好坏。

<a id="focus"></a>
## 2. 当前顺序与首批重点

### 2.1 先从基础行情自主找位置

在不先查看 U2/U3 候选结果的前提下，直接从三品种 2021-01-01 至 2024-02-29 的 30m KLine、small Zig、mid 贴近转折及其结构化数据中发现值得研究的位置。当前重点是：

- 多个品种出现同方向运动，但成员推进、路径、保持或后续转向有差异；
- 或看起来共同启动，实际整组都弱、成员边界不清、当时无法区分；
- 或基础行情明确显示应比较某个第三对象、时间先后或共同转折边界。

场景类别、阈值、赢家、数量和配额不预设。可以回顾性发现位置，但必须标明后验选择，不能据此声称提前识别。

### 2.2 首个有价值位置立即进入 S2/S3，同时继续 S1

不要求先清完整个时间范围才画第一张图；也不允许第一张图完成后停止场景发现。记录实际搜索覆盖和未覆盖范围，使 Owner 能区分“已看过、未发现”和“尚未看”。

### 2.3 两个证据面并行但不混同

- 广域基础行情 + C0/N/C1 raw：检验位置、成员、第三对象和简单基线；raw 不是正式 Cluster。
- 单一完整参考 Case `refonly-ad8824a52552d7bffa91` × 五个 As-Of：检验 Current 演进、Working/Completed、R02 客观路径与四束可判范围；它不是五个 Case，R03 仍 Withheld。

<a id="coverage"></a>
## 3. 全部观察义务

| 义务 | 必须回答 | 资格/限制 |
|---|---|---|
| 场景选择 | 基础行情发生什么、为什么值得研究、选择是否依赖后验、主要反例是什么 | 不由 raw 候选、字段异常或旧 run 选样反推 |
| U2 位置 | 实际转折、方向、actual/confirm/known、共同运动起点与可知时间是否匹配 | C1 raw/Reference/Shadow/official 分开 |
| U2 成员边界 | 成员是否同一轮机会；第三品种应入、应出、错时或无法判断 | 两成员 raw 可观察第三对象；三成员在固定 Universe 内无组外 |
| U3 Progress | 当时合法净推进、持续、极值更新/方向连贯能否区分成员 | raw price 单位不可直接跨品种排名 |
| U3 Friction | path efficiency、counter move、turn/retrace/reversal 是否提供差异 | 同源路径字段不逐项多票；带 lifecycle 和观察长度 |
| U3 Retention | 驻留、峰值保持、回到原点、恢复/承接是否有合法输出 | 固定 R02 只覆盖部分代理；缺项明确 |
| U3 Observability/Constraint | 样本、确认延迟、数据质量、流动性/容量/成本是否足以解释 | 没有的约束不得想象补齐 |
| 后续检验 | 合法 Outcome/End/Horizon 或探索性显示范围如何支持/反证 | 未来信息不得回填历史 Current |
| 增量 | 与 KLine、C0/N、静态组、简单共同事件相比判断哪里改变 | 组织/可追溯性改进与独立投资知识分开 |
| 设计行动 | 保留、修订、继续验证、停止及推翻条件 | 固定数据不足不自动等于设计失败 |

<a id="s1"></a>
## 4. S1：确定观察对象和可执行问题

### 4.1 必做

1. 完整读取 U2/U3 Owner Decision、Narrative 和 Use Case 承重原文，写出“原叙事想解决的市场场景—U2 责任—U3 责任—增量门槛”。
2. 核两份固定 ZIP 实际成员与身份，不重算；记录实际消费的文件、SHA、时间范围和缺失。
3. 设计低成本、可复核的基础行情搜索过程。它可以利用价格方向、Zig/贴近转折位置和共同时间，但不能先用 U2/U3 输出选答案。
4. 对每个进入 S2 的位置记录：
   - 场景 ID、窗口、品种、方向；
   - 基础行情事实与选择理由；
   - 回顾性/当时可知边界；
   - 想检验的 U2/U3 问题；
   - 主要反例、第三对象或“整组都弱”的可能；
   - 当前固定数据能提供/不能提供什么。
5. 搜索到的“无明显价值”区域也可作为范围覆盖证据，但不要求为每个空窗画图。

### 4.2 禁止

- 预先把场景分成固定类型并凑配额；
- 先看 C1/U3 数值再回头挑漂亮 K线；
- 把 304 个 exact-UTI raw 候选当作全部共同机会；
- 把一个完整 Case 当成本轮全部 S1；
- 因广域没有正式 U3 而停止基础场景观察。

<a id="s2"></a>
## 5. S2：先基础图，再定向 U2/U3 图层和同源数据

执行 Pro 在场景与窗口明确后签发具体 Worker 工单。每张进入业务结论的图至少满足：

1. 固定源：`/dwdhome/fy/资金管理` 两份 ZIP；aidata 工作区 `/dwdhome/fy/BASE_E6_2`。
2. 基础图先显示 KLine、Zig、mid 贴近转折、价格轴、时间和实际选择窗口。
3. 之后按该场景问题叠加必要的：
   - U2 actual/confirm 点、C1 候选/Reference 状态、成员和第三对象；
   - N 单品种画像；
   - 单 Case 合法 As-Of 的 R02 路径事实与明确缺项。
4. 人图与 AI 数据使用同一 `run_id/node_id/timespan` 和同一固定源；视觉上下文 `extra_time` 不替换证据窗口。
5. 实际打开浏览器核 K线和图层可见；HTTP 200、文件存在或图链接生成不算渲染通过。
6. 输出同源 CSV/图层视图、关键标记时间、读图说明和真实版本。
7. AI 只读取结构化数据，不自称看过像素图。

优先使用 aidata 已有能力。固定 CSV 接入先查现有 adapter/API/TODO；确有通用缺口且阻断本场景时，Worker 可在 **aidata 新独立分支** 连续修通普通工程依赖、兼容和真实测试。不得改当前 aidata 分支、不得在 observe-iterate/cgpterm 另做图工具、不得重算固定 Feature。

旧 V2-01 图仅可在输入、版本、窗口和浏览器渲染均重新核实后技术复用；旧选样与专业结论不复用。

<a id="s3"></a>
## 6. S3：按场景给出可证伪业务认识

每项重要观察使用以下链条：

1. **市场事实**：品种、时间、窗口、实际路径、转折和后续运动。
2. **设计承诺**：U2 或 U3 原本要解决什么，具体来源和当前输出资格。
3. **当时判断**：合法 As-Of 下位置/成员及四束差异或无法判断。
4. **后续检验**：合法 Outcome 或明确标注的探索性后续范围。
5. **基线比较**：KLine、C0/N、静态组、简单共同事件、U2、U2+U3。
6. **结论**：合理、可疑、不合理、无增量、反证、未知；说明原因和替代解释。
7. **行动**：保留、修改、补固定范围图、反馈预计算疑问、继续验证或有据停止。

事实、案例发现、假设、数据/方法问题分别标记。一个字段可观察不等于一束已校准；四束字段共享同一路径时不算四份独立证据。

### 6.1 当前参考 Case 的可比性纪律

同一 As-Of 的成员可能处于不同 `WorkingSoFar/Completed` 和不同观察 bar 数；raw progress 是各自价格单位。必须先比较可见区间、状态、单位与确认时效，再解释 path efficiency、counter move、retained fraction 等。禁止按 raw progress 或单个效率数直接给“最好品种”排名。

### 6.2 广域场景的 U3 边界

固定包对广域场景没有完整正式 U3。可观察基础路径、C0/N 和 C1 raw，并说明若要验证 U3 还缺哪份预计算输出；不得自行补算、把 N 改名 U3 或把缺失写成 Negative。

<a id="sources"></a>
## 7. 必须实际取得的 Source

### 7.1 observe-iterate `@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080`

- `professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md::full`
- `professional/v2/07_BUSINESS_SCENE_OBSERVATION_METHOD.md::full`
- `professional/v2/04_BI01_BUSINESS_BASELINE.md::full`
- `professional/v2/05_BI01_FIXED_INPUT_DATA.md::full`
- `professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md::full`
- `professional/v2/01_AIDATA_CHART_AND_DATA.md::full`
- `professional/v2/02_OBSERVATION_IDEAS_AND_VALIDATION.md::full`
- `professional/v2/03_EXECUTION_HANDOFF.md::full`
- `runtime/dual_route_execution/DR12_PROFESSIONAL_QUESTION_CATALOG.md::full`

### 7.2 complex-systems-vocabulary `@48f55f53e25d04e5b4b59fae1e652dd4b679c9d3`

- `OD_U2_U3_CAPITAL_VALUE_AND_ITERATION_DECISIONS_V0.1.0.md::full`
- `U2_OPPORTUNITY_CLUSTER_SCALE_TURN_NARRATIVE_SPEC_V0.3.0.md::full`
- `U2_OPPORTUNITY_CLUSTER_SCALE_TURN_USE_CASE_CARD_V0.4.0.md::full`
- `U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_NARRATIVE_SPEC_V0.3.0.md::full`
- `U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_USE_CASE_CARD_V0.4.0.md::full`

涉及具体公式、方法漂移或字段来源时，再按 06 的 exact 指针读取 Source/Metric/Step Witness 和候选 Local Contract；候选 `ownerAccepted=false`/`NOT_APPLIED` 不因目录名变正式。

<a id="deliverables"></a>
## 8. 必须交付的实物

在 `runs/BI-01-V2-02/artifacts/` 下形成真实业务成果，不新建平行控制系统。至少包括：

1. S1 场景搜索与选择记录：实际覆盖、具名位置、理由、后验边界、问题和反例。
2. S2 图与同源数据索引：固定源身份、aidata 版本、run/node/timespan、真实可打开链接/路径、图层、同源数据与读图定位。
3. S3 业务观察正文：逐场景的 U2/U3/后续/基线证据链，支持、反证、无增量、未知和设计行动。
4. 四束“设计字段—固定数据字段—状态/单位/窗口—已提供/缺失—可判范围”对应关系。
5. Worker 工单与技术结果的准确索引；尚未被执行 Pro 消费的技术产物必须标明。
6. 完整 `ROLE_RETURN`、`QUESTION_WORK_RETURN`、材料使用、全部未完和最新 continuation。

文件组织可随真实观察合理调整，但不得用字段清单、图目录或摘要替代业务认识。

<a id="worker"></a>
## 9. Worker 技术授权

只有执行 Pro 签发的具体工单才授权 Worker。工单须列：

- 场景/窗口/As-Of、品种、方向和业务问题；
- 两份固定 ZIP 全名、原件目录和状态边界；
- 基础图层、U2/N/U3 图层、同源数据和 Owner 读图要求；
- aidata 锁定版本、现有入口优先、浏览器核验；
- 允许连续处理的普通依赖、输入表示、调用与回归；
- 不得做的重算、替换、第二工具和业务裁定。

Worker 不签 U2/U3 业务结论或 G4；技术结果由执行 Pro解释、挑战和消费。

<a id="completion"></a>
## 10. 完整完成与合法停止

完成需同时满足：

- 已从基础行情形成有据的场景选择及实际覆盖说明；
- U2 位置、成员/第三对象、时效和正式资格得到实质检验；
- U3 四束在可用范围逐束给出差异/无法判断，并和后续事实对应；
- 基线增量或无增量明确；
- Owner 能打开图并按时间/品种定位每项重要判断；
- 固定数据已提供、未提供和方法限制分账；
- 有可执行设计行动、合法待决或有据停止。

如果固定数据不足，只有在准确说明具体文件/字段/窗口、受影响问题和为何不能从其他合法输出回答后，才算该局部“不可判断”；它不自动关闭其他主体。

<a id="budget"></a>
## 11. 投入预测

预计 6—10 个有效专业回交完成本完整任务，首个闭环应尽早出现；这是预测而非配额。每四个有效回交做非阻塞管理复看。工具、Worker、Git commit 和手机 episode 不计为业务 Pro 回交。新聊天不清零。

<a id="result-trigger"></a>
## 12. RESULT 触发

首次形成“真实基础行情位置 + 可打开图/同源数据 + U2 位置/成员判断 + U3 差异或精确限制 + 后续/基线增量结论”的闭环，触发一次非阻塞 M-REASSESS。脚本成功、单图或仅列字段不满足。

<a id="change-trigger"></a>
## 13. CHANGE 触发

以下任一情况触发 M-REASSESS：

- 固定包身份、字段、时间、方法或原业务合同出现会改变判断的具体冲突；
- 需要改变本任务已定业务前提、数据范围、工具边界或完成条件；
- 连续两次实质回交仍只处理来源、格式、环境或工具准备，真实场景/反例/迭代行动没有推进；
- Owner 新纠正。

只暂停受冲突影响的输出；不受影响的场景、数据阅读和业务主体继续。

<a id="effort-trigger"></a>
## 14. EFFORT 触发

完整工作 ACTIVE 期间，从 R0001 起每累计四个有效专业及必要管理/接收结果触发一次非阻塞投入复看，`WHILE_WORK_ACTIVE`。普通提交不触发，已消费一轮后完整任务仍未完则继续下一周期。

<a id="same-work"></a>
## 15. 同工作连续续作

继续本任务和当前正式 Binding，采用上一份完整 `QUESTION_WORK_RETURN.continuation_ref` 的具体重点；完整范围、固定源、权限、完成条件和触发不变。当前重点只决定顺序，不能以单 Case、单图、局部 finding 或 Worker 修通为停点。保留已成，不重做无新依据的部分；继续 S1/S2/S3、必要 Worker 工单、技术结果业务消费和两份一致 Return。

<a id="accept"></a>
## 16. 完整结果接收

完整条件满足或出现需要阶段性接受的实质结果时，路由到 `chatgpt:细节叙事生成_金标:BI01-V202-管理`，M-CLOSE 或管理明确的接收模式。提交 exact 成果、图/数据索引、来源、支持反证、未完、触发状态和 continuation；执行 Pro 不自行宣布管理/Owner 接收。

<a id="decide"></a>
## 17. 前提、方向与重要变化决定

重要前提冲突、首个闭环、投入触发或需要改变完整任务时，路由同一管理聊天 M-REASSESS。带准确问题位置、受影响结论/消费者、已完成和未完；不把“请全面检查一切”交回管理，也不让操作端临场裁业务。

<a id="return-repair"></a>
## 18. 有限回交修复

纯 Return 字段、关联或运输缺件回本专业角色有限补交，保留原业务结果，不重做分析。实质业务缺件按同工作继续；管理判断缺件回管理。相同纯交付错误一次补交后仍失败，交管理接管，不无限重发。

<a id="parent"></a>
## 19. 父关系

本任务来自 Owner 明确 GO 的新 `BI-01-V2-02` 首次 M-START。`parent.status=NOT_APPLICABLE_NEW_CASE`。原 I1— I3 是 Source；旧 `BI-01-V2-01` 是暂停历史，均不是活动 parent。


<a id="question-work-binding"></a>
## 20. QUESTION_WORK_BINDING

以下 Binding 锁定本次首次管理已提交的完整业务正文。`source_reads.reuse_evidence=null` 表示执行上下文仍须真正取得原文，不继承管理者已读状态。运行端以实际发布 commit 冻结本文件；完整 scope 不随最近 remaining 缩小。

```json
{
  "schema": "question-work/v2",
  "kind": "BINDING",
  "work_id": "BI-01",
  "goal_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
    "path": "professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md",
    "selector": "full"
  },
  "plan_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "a8ba3dba1da54d3715cecddfeb30bfdf78dd8358",
    "path": "runs/BI-01-V2-02/reviews/management-R0001/DECISION.md",
    "selector": "#plan"
  },
  "full_scope_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "a8ba3dba1da54d3715cecddfeb30bfdf78dd8358",
    "path": "runs/BI-01-V2-02/01_当前任务.md",
    "selector": "full"
  },
  "batch_result": "在固定 rb/i/hc 基础行情中自主发现有业务意义的共同方向场景，形成可打开的基础图与同源数据，再检验 U2 位置/成员边界、U3 四个 Movement Bundle 当时辨别力、后续支持/反证及相对 KLine/C0/N/静态组/简单共同事件的增量或无增量；完整责任不以首图、单 Case 或局部修复结束。",
  "question_ids": [
    "S1",
    "S2",
    "S3"
  ],
  "professional_mode": "OBSERVATION_SCOPE",
  "focus_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "a8ba3dba1da54d3715cecddfeb30bfdf78dd8358",
    "path": "runs/BI-01-V2-02/01_当前任务.md",
    "selector": "#focus"
  },
  "coverage_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "a8ba3dba1da54d3715cecddfeb30bfdf78dd8358",
    "path": "runs/BI-01-V2-02/01_当前任务.md",
    "selector": "#coverage"
  },
  "source_reads": [
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
        "path": "professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md",
        "selector": "full"
      },
      "requirement": "MODE_FULL",
      "purpose": "恢复 Owner 完整业务目标、固定范围、S1—S3 和完成条件",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
        "path": "professional/v2/07_BUSINESS_SCENE_OBSERVATION_METHOD.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "执行场景先行、基础行情自主选位置、U2/U3/后续/基线证据链",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
        "path": "professional/v2/04_BI01_BUSINESS_BASELINE.md",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "复用 I1—I3 业务知识并保持 raw/reference/formal、时间和基线边界",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
        "path": "professional/v2/05_BI01_FIXED_INPUT_DATA.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "锁定两份 ZIP、成员、哈希、状态和当前工作路径",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
        "path": "professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "取得原 U2/U3 承重原文、字段/状态与本次固定数据映射",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
        "path": "professional/v2/01_AIDATA_CHART_AND_DATA.md",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "按 S2 先基础图、同源数据、真实渲染和 aidata 保护面施工",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
        "path": "professional/v2/02_OBSERVATION_IDEAS_AND_VALIDATION.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "按 S3 形成市场事实、设计承诺、判断、反例、基线和行动",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
        "path": "professional/v2/03_EXECUTION_HANDOFF.md",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "保持管理/执行 Pro/Worker/Owner 的既有分工与成果消费关系",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
        "path": "runtime/dual_route_execution/DR12_PROFESSIONAL_QUESTION_CATALOG.md",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "取得当前 S1/S2/S3 专业问题、mode 与新 run 隔离边界",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/complex-systems-vocabulary",
        "commit": "48f55f53e25d04e5b4b59fae1e652dd4b679c9d3",
        "path": "docs/network-dynamic-ceps-factory/OD_U2_U3_CAPITAL_VALUE_AND_ITERATION_DECISIONS_V0.1.0.md",
        "selector": "full"
      },
      "requirement": "MODE_FULL",
      "purpose": "恢复 U2/U3 资金管理价值、责任分层、基线与禁止推论",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/complex-systems-vocabulary",
        "commit": "48f55f53e25d04e5b4b59fae1e652dd4b679c9d3",
        "path": "docs/network-dynamic-ceps-factory/U2_OPPORTUNITY_CLUSTER_SCALE_TURN_NARRATIVE_SPEC_V0.3.0.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "恢复 U2 从实际转折到同一机会身份、成员和重复暴露的原叙事",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/complex-systems-vocabulary",
        "commit": "48f55f53e25d04e5b4b59fae1e652dd4b679c9d3",
        "path": "docs/network-dynamic-ceps-factory/U2_OPPORTUNITY_CLUSTER_SCALE_TURN_USE_CASE_CARD_V0.4.0.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "核 U2 Formation/Validity/Separation、Identity、时间和非质量边界",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/complex-systems-vocabulary",
        "commit": "48f55f53e25d04e5b4b59fae1e652dd4b679c9d3",
        "path": "docs/network-dynamic-ceps-factory/U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_NARRATIVE_SPEC_V0.3.0.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "恢复 U3 Current/Outcome、四个 Movement Bundle、证据依赖与质量责任",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/complex-systems-vocabulary",
        "commit": "48f55f53e25d04e5b4b59fae1e652dd4b679c9d3",
        "path": "docs/network-dynamic-ceps-factory/U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_USE_CASE_CARD_V0.4.0.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "核 U3 字段、状态、可比性、四类资金接口分离、Case 和 Kill Criteria",
      "reuse_evidence": null
    },
    {
      "source": {
        "source_kind": "ATTACHMENT",
        "attachment_id": "file_0000000035c481fdbbfb82af5e57a96c",
        "filename": "steel_U2_U3_执行结果_20261010.zip",
        "selector": "full",
        "sha256": "7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c"
      },
      "requirement": "PROVENANCE_TRIGGER",
      "purpose": "锁定下游固定预计算包身份；真实读取使用 /dwdhome/fy/资金管理 原件",
      "reuse_evidence": null
    },
    {
      "source": {
        "source_kind": "ATTACHMENT",
        "attachment_id": "file_000000008c7481fd8604a79973ec5951",
        "filename": "rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip",
        "selector": "full",
        "sha256": "4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987"
      },
      "requirement": "PROVENANCE_TRIGGER",
      "purpose": "锁定上游基础行情包身份；保留历史外层哈希差异并使用当前原件",
      "reuse_evidence": null
    }
  ],
  "deliverables_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "a8ba3dba1da54d3715cecddfeb30bfdf78dd8358",
    "path": "runs/BI-01-V2-02/01_当前任务.md",
    "selector": "#deliverables"
  },
  "completion_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "a8ba3dba1da54d3715cecddfeb30bfdf78dd8358",
    "path": "runs/BI-01-V2-02/01_当前任务.md",
    "selector": "#completion"
  },
  "budget_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "a8ba3dba1da54d3715cecddfeb30bfdf78dd8358",
    "path": "runs/BI-01-V2-02/reviews/management-R0001/DECISION.md",
    "selector": "#budget"
  },
  "routes": {
    "same_work": {
      "recipient_role": "professional",
      "recipient_ref": "chatgpt:细节叙事生成_金标:BI01-V202-执行",
      "instructions_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "a8ba3dba1da54d3715cecddfeb30bfdf78dd8358",
        "path": "runs/BI-01-V2-02/01_当前任务.md",
        "selector": "#same-work"
      }
    },
    "accept": {
      "recipient_role": "management",
      "recipient_ref": "chatgpt:细节叙事生成_金标:BI01-V202-管理",
      "instructions_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "a8ba3dba1da54d3715cecddfeb30bfdf78dd8358",
        "path": "runs/BI-01-V2-02/01_当前任务.md",
        "selector": "#accept"
      }
    },
    "decide": {
      "recipient_role": "management",
      "recipient_ref": "chatgpt:细节叙事生成_金标:BI01-V202-管理",
      "instructions_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "a8ba3dba1da54d3715cecddfeb30bfdf78dd8358",
        "path": "runs/BI-01-V2-02/01_当前任务.md",
        "selector": "#decide"
      }
    },
    "return_repair": {
      "recipient_role": "professional",
      "recipient_ref": "chatgpt:细节叙事生成_金标:BI01-V202-执行",
      "instructions_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "a8ba3dba1da54d3715cecddfeb30bfdf78dd8358",
        "path": "runs/BI-01-V2-02/01_当前任务.md",
        "selector": "#return-repair"
      }
    }
  },
  "triggers": [
    {
      "trigger_id": "BI01V202-FIRST-GROUNDED-CYCLE",
      "kind": "RESULT",
      "condition_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "a8ba3dba1da54d3715cecddfeb30bfdf78dd8358",
        "path": "runs/BI-01-V2-02/01_当前任务.md",
        "selector": "#result-trigger"
      },
      "signal_key": "BI01V202_FIRST_GROUNDED_CYCLE",
      "route": {
        "recipient_role": "management",
        "recipient_ref": "chatgpt:细节叙事生成_金标:BI01-V202-管理",
        "instructions_ref": {
          "repo": "daowei2026/observe-iterate",
          "commit": "a8ba3dba1da54d3715cecddfeb30bfdf78dd8358",
          "path": "runs/BI-01-V2-02/01_当前任务.md",
          "selector": "#decide"
        }
      },
      "blocking": false,
      "effort_limit": null,
      "obligation_id": "BI01V202_FIRST_RESULT_REASSESSMENT",
      "cycle_id": "initial",
      "rearm_ref": null,
      "repeat": "ONCE"
    },
    {
      "trigger_id": "BI01V202-SUBSTANTIVE-CHANGE",
      "kind": "CHANGE",
      "condition_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "a8ba3dba1da54d3715cecddfeb30bfdf78dd8358",
        "path": "runs/BI-01-V2-02/01_当前任务.md",
        "selector": "#change-trigger"
      },
      "signal_key": "BI01V202_SUBSTANTIVE_CHANGE",
      "route": {
        "recipient_role": "management",
        "recipient_ref": "chatgpt:细节叙事生成_金标:BI01-V202-管理",
        "instructions_ref": {
          "repo": "daowei2026/observe-iterate",
          "commit": "a8ba3dba1da54d3715cecddfeb30bfdf78dd8358",
          "path": "runs/BI-01-V2-02/01_当前任务.md",
          "selector": "#decide"
        }
      },
      "blocking": false,
      "effort_limit": null,
      "obligation_id": "BI01V202_CHANGE_REASSESSMENT",
      "cycle_id": "initial",
      "rearm_ref": null,
      "repeat": "ONCE"
    },
    {
      "trigger_id": "BI01V202-EFFORT-4",
      "kind": "EFFORT",
      "condition_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "a8ba3dba1da54d3715cecddfeb30bfdf78dd8358",
        "path": "runs/BI-01-V2-02/01_当前任务.md",
        "selector": "#effort-trigger"
      },
      "signal_key": "BI01V202_EFFECTIVE_PRO_RESULTS",
      "route": {
        "recipient_role": "management",
        "recipient_ref": "chatgpt:细节叙事生成_金标:BI01-V202-管理",
        "instructions_ref": {
          "repo": "daowei2026/observe-iterate",
          "commit": "a8ba3dba1da54d3715cecddfeb30bfdf78dd8358",
          "path": "runs/BI-01-V2-02/01_当前任务.md",
          "selector": "#decide"
        }
      },
      "blocking": false,
      "effort_limit": {
        "unit": "EFFECTIVE_CALLS",
        "limit": 4,
        "count_from_ref": {
          "repo": "daowei2026/observe-iterate",
          "commit": "05aacb186e3538a0af6b5971d85f4429077a7095",
          "path": "runs/BI-01-V2-02/provenance/turns/R0001/INVOCATION.json",
          "selector": "full"
        }
      },
      "obligation_id": "BI01V202_CONTINUOUS_EFFORT_REVIEW",
      "cycle_id": "initial",
      "rearm_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "a8ba3dba1da54d3715cecddfeb30bfdf78dd8358",
        "path": "runs/BI-01-V2-02/01_当前任务.md",
        "selector": "#effort-trigger"
      },
      "repeat": "WHILE_WORK_ACTIVE"
    }
  ],
  "explicit_no_trigger_reason_ref": null,
  "parent": {
    "status": "NOT_APPLICABLE_NEW_CASE",
    "ref": null,
    "reason_ref": {
      "repo": "daowei2026/observe-iterate",
      "commit": "a8ba3dba1da54d3715cecddfeb30bfdf78dd8358",
      "path": "runs/BI-01-V2-02/01_当前任务.md",
      "selector": "#parent"
    }
  },
  "question_definitions": []
}
```

来源：daowei2026/observe-iterate@a3984f16415a5f1ac521a68c3a98d0364fed9546:runs/BI-01-V2-02/01_当前任务.md::full

## 本轮原文与位置

本次原始要求：`daowei2026/observe-iterate@a8ba3dba1da54d3715cecddfeb30bfdf78dd8358:runs/BI-01-V2-02/01_当前任务.md::#same-work`
当前生效任务：`daowei2026/observe-iterate@a3984f16415a5f1ac521a68c3a98d0364fed9546:runs/BI-01-V2-02/01_当前任务.md::full`
当前任务采用依据：`daowei2026/observe-iterate@5448c367072519bbce3542e4fb35b22ff0af79eb:runs/BI-01-V2-02/reviews/management-R0008/DECISION.md::#adoption`
上一轮实际采用的任务绑定：`daowei2026/observe-iterate@a3984f16415a5f1ac521a68c3a98d0364fed9546:runs/BI-01-V2-02/01_当前任务.md::L259-L649`
完整工作范围：`daowei2026/observe-iterate@a8ba3dba1da54d3715cecddfeb30bfdf78dd8358:runs/BI-01-V2-02/01_当前任务.md::full`
本次实际证据：`daowei2026/observe-iterate@5448c367072519bbce3542e4fb35b22ff0af79eb:runs/BI-01-V2-02/reviews/management-R0008/DECISION.md::full`
本次实际证据：`daowei2026/observe-iterate@cee668750af0a3ed8f4ae2a95b453bdb881d18ef:runs/BI-01-V2-02/provenance/turns/R0008/FULL_RESPONSE.md::full`
本次实际证据：`daowei2026/observe-iterate@cee668750af0a3ed8f4ae2a95b453bdb881d18ef:runs/BI-01-V2-02/provenance/turns/R0008/QUESTION_WORK_RETURN.json::full`
本次实际证据：`daowei2026/observe-iterate@acb3aa5abb06472f25e07a51ad07a25620593280:runs/BI-01-V2-02/artifacts/professional-R0006/FULL_RETURN.md::full`
本次实际证据：`daowei2026/observe-iterate@acb3aa5abb06472f25e07a51ad07a25620593280:runs/BI-01-V2-02/artifacts/professional-R0006/QUESTION_WORK_RETURN.json::full`
本次实际证据：`daowei2026/observe-iterate@19ef56db70addb71b2d29647bf93b56675f30370:runs/BI-01-V2-02/artifacts/worker-R0006/WORKER_RETURN.md::full`
本次实际证据：`daowei2026/observe-iterate@19ef56db70addb71b2d29647bf93b56675f30370:runs/BI-01-V2-02/artifacts/worker-R0006/ROLE_RETURN.json::full`
本次实际证据：`daowei2026/observe-iterate@19ef56db70addb71b2d29647bf93b56675f30370:runs/BI-01-V2-02/artifacts/worker-R0006/CURRENT_NODE_INDEX.csv::full`
本次实际证据：`daowei2026/observe-iterate@19ef56db70addb71b2d29647bf93b56675f30370:runs/BI-01-V2-02/artifacts/worker-R0006/FIXED_INPUT_BINDING.json::full`
本次实际证据：`daowei2026/observe-iterate@19ef56db70addb71b2d29647bf93b56675f30370:runs/BI-01-V2-02/artifacts/worker-R0006/TECHNICAL_VALIDATION_SUMMARY.json::full`
本次实际证据：`daowei2026/observe-iterate@19ef56db70addb71b2d29647bf93b56675f30370:runs/BI-01-V2-02/artifacts/worker-R0006/PUBLICATION_MANIFEST.json::full`
本次实际证据：`daowei2026/observe-iterate@5e2ff089b5c5edf0a0e99cabf5c5016c3475b858:runs/BI-01-V2-02/reviews/WORKMAP_INTAKE_CURRENT.json::full`
本次实际证据：`daowei2026/observe-iterate@e3bdc0c251729cf65c3f77d8d1bdc5dded4a830a:runs/BI-01-V2-02/reviews/management-R0009/CONTROLLER_RECEPTION.md::full`
本次实际证据：`daowei2026/observe-iterate@e3bdc0c251729cf65c3f77d8d1bdc5dded4a830a:runs/BI-01-V2-02/reviews/management-R0009/WORKMAP_CHECK.json::full`
本次实际证据：`daowei2026/observe-iterate@e3bdc0c251729cf65c3f77d8d1bdc5dded4a830a:runs/BI-01-V2-02/reviews/management-R0009/SUCCESSOR_DISPATCH_CHECK.json::full`
本次实际证据：`daowei2026/observe-iterate@5e2ff089b5c5edf0a0e99cabf5c5016c3475b858:runs/BI-01-V2-02/provenance/turns/R0009/FULL_RESPONSE.md::full`

## 本次直接读取的上下文

- MODE_FULL：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md::full`
  用途与边界：恢复 Owner 完整业务目标、固定范围、S1—S3 和完成条件
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:professional/v2/07_BUSINESS_SCENE_OBSERVATION_METHOD.md::full`
  用途与边界：执行场景先行、基础行情自主选位置、U2/U3/后续/基线证据链
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:professional/v2/04_BI01_BUSINESS_BASELINE.md::full`
  用途与边界：复用 I1—I3 业务知识并保持 raw/reference/formal、时间和基线边界
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:professional/v2/05_BI01_FIXED_INPUT_DATA.md::full`
  用途与边界：锁定两份 ZIP、成员、哈希、状态和当前工作路径
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md::full`
  用途与边界：取得原 U2/U3 承重原文、字段/状态与本次固定数据映射
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:professional/v2/01_AIDATA_CHART_AND_DATA.md::full`
  用途与边界：按 S2 先基础图、同源数据、真实渲染和 aidata 保护面施工
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:professional/v2/02_OBSERVATION_IDEAS_AND_VALIDATION.md::full`
  用途与边界：按 S3 形成市场事实、设计承诺、判断、反例、基线和行动
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:professional/v2/03_EXECUTION_HANDOFF.md::full`
  用途与边界：保持管理/执行 Pro/Worker/Owner 的既有分工与成果消费关系
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:runtime/dual_route_execution/DR12_PROFESSIONAL_QUESTION_CATALOG.md::full`
  用途与边界：取得当前 S1/S2/S3 专业问题、mode 与新 run 隔离边界
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/complex-systems-vocabulary@48f55f53e25d04e5b4b59fae1e652dd4b679c9d3:docs/network-dynamic-ceps-factory/OD_U2_U3_CAPITAL_VALUE_AND_ITERATION_DECISIONS_V0.1.0.md::full`
  用途与边界：恢复 U2/U3 资金管理价值、责任分层、基线与禁止推论
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/complex-systems-vocabulary@48f55f53e25d04e5b4b59fae1e652dd4b679c9d3:docs/network-dynamic-ceps-factory/U2_OPPORTUNITY_CLUSTER_SCALE_TURN_NARRATIVE_SPEC_V0.3.0.md::full`
  用途与边界：恢复 U2 从实际转折到同一机会身份、成员和重复暴露的原叙事
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/complex-systems-vocabulary@48f55f53e25d04e5b4b59fae1e652dd4b679c9d3:docs/network-dynamic-ceps-factory/U2_OPPORTUNITY_CLUSTER_SCALE_TURN_USE_CASE_CARD_V0.4.0.md::full`
  用途与边界：核 U2 Formation/Validity/Separation、Identity、时间和非质量边界
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/complex-systems-vocabulary@48f55f53e25d04e5b4b59fae1e652dd4b679c9d3:docs/network-dynamic-ceps-factory/U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_NARRATIVE_SPEC_V0.3.0.md::full`
  用途与边界：恢复 U3 Current/Outcome、四个 Movement Bundle、证据依赖与质量责任
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/complex-systems-vocabulary@48f55f53e25d04e5b4b59fae1e652dd4b679c9d3:docs/network-dynamic-ceps-factory/U3_MOVEMENT_QUALITY_ACTIVITY_CONVERSION_ALLOCATION_USE_CASE_CARD_V0.4.0.md::full`
  用途与边界：核 U3 字段、状态、可比性、四类资金接口分离、Case 和 Kill Criteria
  外仓准确定位；本checkout未读取，接收者按原工具取得正文。 本次不主张已读复用。

- PROVENANCE_TRIGGER；用途与边界：锁定下游固定预计算包身份；真实读取使用 /dwdhome/fy/资金管理 原件
  原始来源：`{"attachment_id": "file_0000000035c481fdbbfb82af5e57a96c", "filename": "steel_U2_U3_执行结果_20261010.zip", "selector": "full", "sha256": "7bebbee3fd7d425eb85116f33c5d0e01ae2163e6849818515fe3824a82b9a46c", "source_kind": "ATTACHMENT"}`
  原件由接收者实际取得；本工具未读取或验证原件。

- PROVENANCE_TRIGGER；用途与边界：锁定上游基础行情包身份；保留历史外层哈希差异并使用当前原件
  原始来源：`{"attachment_id": "file_000000008c7481fd8604a79973ec5951", "filename": "rb_hc_i_mid贴近转折_zig_small_K线_20210101_20240229.zip", "selector": "full", "sha256": "4fd1af4e7b34af6fc099e6289ffdd5d83125412fc16d2a9902af4fd9741b3987", "source_kind": "ATTACHMENT"}`
  原件由接收者实际取得；本工具未读取或验证原件。

读取Owner完整要求、生效完整任务和输入输出地图，不能用最新remaining替全部责任。按source_reads取得准确正文用于判断，已读未变且可恢复者复用；不递归扫无关历史，不用索引/hash/旧回执代正文。

旧包中已被Owner否定的多余任务，必须由原有权责任者从当前正文、任务、前置、接收和后继删除；只为其存在的辅助代码与检查交原实现者删除。禁止继续完善、改名或列为暂缓/未来优化。不能只在顶部写新原则却继续采用相反正文。真实业务方法、时间、身份、状态、正式输出与消费者保留，技术机制替换回正常平台。正确正文禁止任何压缩或摘要替换。历史提交和实际记录不倒改；历史可追溯不授后续派发。通用材料维护不自动取得用例任务写权。

当前执行材料由管理和有权任务责任者明确采用。推进者取得实际需要的正确正文，不能用管理概述替代业务细节；也不要求每轮重读全部历史和已撤完整任务。

发现新的实质冲突时，给出准确位置与受影响结论，按原责任处理。来源不足只限制真正依赖的判断，不用旧快照补造事实，也不冻结无关工作。

方法版本、业务合同版本、源码版本和运行数据分别保持准确，不随一次方法更新全部追 latest。

运行事实（来自现有记录）：
观察时间：2026-10-18T18:06:33.666873+00:00
有效回交数：6

按既有协议交完整实质回答及ROLE_RETURN/QUESTION_WORK_RETURN，来源、未执行和资格如实保留，不新增控制表，不重抄协调者已存提示。完整任务未完成就保留完整责任及连续后继，局部交付不自设停点。要求GitHub提交时普通快进并fresh回读，最后commit message带turn complete及本轮invocation_id，无invocation时简要标明执行身份；不造空提交。

专业者回交实际实物、必要自检／执行结果、具体限制及完整未完，不代写管理接收、全局预算或主控派发。管理回交已完成的判断、实际处置和可执行后继，不以问题目录代替决定。

没有完整完成时，说明真实停止原因及已经明确的下一步；不得以自设局部目标完成作为结束解释。
