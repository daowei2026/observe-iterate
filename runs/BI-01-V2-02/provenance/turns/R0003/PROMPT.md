[BI01-V2-02-R0003-20261018T135502Z-2de24e8b]
work_id: BI-01
invocation_id: BI01-V2-02-R0003-20261018T135502Z-2de24e8b
assignment_token: BI01-V2-02-READER-ddb4a7843ab8425b8e2ea795ef11ef77
role: review
recipient: chatgpt:细节叙事生成_金标:BI01-V202-地图只读接收-01
当前阶段：专业任务 BI01
当前职责：专业任务 BI01 独立只读审查
对应专业工作：具名独立只读审查（专业方法未齐，不自动通过）

本角色仅在存在真实独立审查委派与可取得exact被审对象时使用。按照[V2 交接方法](../../professional/v2/03_EXECUTION_HANDOFF.md)及本次真实被审业务目标和专业方法实际核对专业主张、反例、证据适用范围及影响；不信作者自评，不代写候选后自签。当前专业审查方法仍为PARTIAL时，如需超出现有合同的正式独立审查，明确MISSING并请求有权补充，不因通用role/review模板存在就报告PASS。管理Gate、执行自查、Worker技术验收、Owner决定彼此不能替代。
本轮独立审查若 GitHub 提交不可用，同样可以依 [V2 轮次 ZIP 合同](../../runtime/operations/V2_ROUND_RECORD_CONTRACT.md) 将原审查结果 ZIP 写入 MCP server 可写的 `H:\fy\observe-iterate-share`，由操作 Codex 在 `/dwdhome/fy/observe-iterate-share` 检查并合法发布；必须保留真实评审权限和完整 Return，不能因 ZIP 出现而自称审查/管理已接收。

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

# BI-01-V2-02 首次 Workmap 独立只读接收任务

task_id: BI01-V2-02-WORKMAP-READER-01
work_id: BI-01
run_id: BI-01-V2-02
professional_mode: INDEPENDENT_REVIEW
recipient_role: review
recipient_ref: chatgpt:细节叙事生成_金标:BI01-V202-地图只读接收-01
signed_by: BI01-V2-02-R0001-20261018T130131Z-7f26abeb

本任务由 R0001 管理在既有 review 职责中签发，是一次性、只读、独立的首次 Workmap 接收。新上下文尚未创建、尚未发送、尚未返回。它不新增常驻角色，不授 U2/U3 业务独立审查 PASS，也不允许参与候选形成的人仅通过换聊天获得独立性。

<a id="scope"></a>
## 1. 受托范围

独立阅读下列 exact 管理输入，从 Owner 完整目的而不是文件作者的状态名称，确认一个未参与编写的执行者能否准确恢复：

1. 本轮究竟要检验什么市场业务问题；
2. 固定数据怎样进入 S1/S2/S3、每层证据有什么资格；
3. 为什么必须先从基础行情自主找场景，再核 U2、U3、后续和基线；
4. 广域 raw 与单 Case 完整链分别能回答什么、不能回答什么；
5. 执行 Pro、Worker、管理与 Owner 的生产/消费关系；
6. 哪些旧 V2-01 要求已撤销，哪些正确业务、时间、状态、方法和消费者仍完整保留；
7. 完整任务、局部阻塞、完成条件、触发和真实后继是否一致且可执行。

只判地图/任务/Binding 的可理解性、完整性和前后一致性。不得改写候选，不替管理签预算/采用，不重新选择场景，不核 U2/U3 算法正确性，不审固定计算质量，不签 S1/S2/S3 或 Owner 业务 PASS。发现问题时给出 exact 位置、原文、会造成的具体执行误解和受影响范围；没有问题不凑 finding。

<a id="target"></a>
## 2. 冻结输入

候选输入锁定 `daowei2026/observe-iterate@5e8e4c1bb184a97bfe47bc40493c667bb7b8185d`：

- `runs/BI-01-V2-02/README.md::full`，overview anchors `common/bi01`；
- `runs/BI-01-V2-02/00_长程推进地图.md::full`，anchors `goal/stage/evidence/progress/remaining/management/next`，blob `368681d65d2196b3cc52180da1a1d74b889db85f`；
- `runs/BI-01-V2-02/01_当前任务.md::full`，含 `#question-work-binding`，task_id `BI01-V2-02-S123-SCENE-OBSERVATION-01`，blob `8f90121bd9d1657992313b6c9a78d44fcd3a546f`；
- `runs/BI-01-V2-02/reviews/management-R0001/DECISION.md::full`，blob `6335c8964f545a74e24d9bf68008dbad4eecc90a`；
- `runtime/config/WORKMAP_BINDING.json::full`，当前必须仍为 `NOT_CONFIGURED`；
- `runs/BI-01-V2-02/OWNER_START.md::full`；
- `professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md::full`、`07_BUSINESS_SCENE_OBSERVATION_METHOD.md::full`，以及地图/任务列出的适用 01—06、DR14、Overlay13、Workmap 工具合同。

管理候选之后的 reader task、provenance、Return 或进度提交不重新定义业务输入。实际发送前，操作端必须核上述业务输入没有实质漂移；如 map/task/decision/Owner/rules 改变，以新有权输入重新绑定，不能拿旧报告冒充新报告。

<a id="focus"></a>
## 3. 必须恢复和挑战的承重点

以下是容易误读的承重关系，不是只检查这些关键词：

- 业务链是“U2/U3 原问题 → 基础行情自主选位置 → U2 位置/成员 → U3 四束当时差异 → 后续支持/反证 → 基线增量 → 行动”。
- 广域基础行情、C0/N/C1 raw 与单一完整参考 Case × 五 As-Of 是互补证据面；raw 不是正式 Cluster，五 As-Of 不是五个 Case。
- 两成员 raw 才能在固定三品种 Universe 内观察第三对象；三成员 raw 和完整 Case 都不能制造非空组外优势。
- U3 四方面是四个 Movement Evidence Bundles，不是四类 Allocation Evidence；R02 只是客观路径事实，R03 全部 Withheld。
- `WorkingSoFar/Completed`、实际 bar 数、raw price 单位、actual/confirm/known/As-Of 必须进入可比性，不允许单数值直接排名赢家。
- `OBSERVATION_SCOPE` 是首发 mode，不缩掉 S2/S3；首个场景可尽快进入 S2/S3，但不成为主动停点。
- 执行 Pro 可在具名场景后签 Worker 工单；Worker 只做图、同源数据及普通工程修通，不签业务判断。
- 不重算/替换固定包，不预设场景类别/阈值/配额，不先清仓库，不建设视觉链，不修改 aidata 现有分支，不在观察仓另造图工具。
- 旧 V2-01 的任务、Workmap、Reader、Gate、R10、选样与完成状态全部退出；原 I1— I3 业务 Source 和经核版本的技术图/数据并没有被删除。
- `WORKMAP_BINDING.json=NOT_CONFIGURED` 是当前正确状态，Reader PASS 也不自动等于 ADOPTED；仍需真实 snapshot/Intake/check/dispatch。

需要核是否存在“管理正文宣称撤销，而任务/Binding 又继续要求”的相反正文；也要核是否因强调新方法而误删了 Owner 要求的正确业务字段、状态、时间、方法或消费者。

<a id="coverage"></a>
## 4. 输出与 verdict

将完整只读报告交到：

`runs/BI-01-V2-02/reviews/independent/WORKMAP_READER_R0001_INPUT.md`

报告至少记录：

- 本次真实 invocation/recipient；
- 实际读取 commit、task blob、map/decision/config 身份；
- 是否未参与候选形成；
- 你恢复出的完整业务关系与真实后继；
- 每个实质歧义的 exact 位置、误解方式和影响；
- 未读、不可得、超出本次资格的部分；
- verdict。

verdict：

- `PASS`：在当前狭义 Workmap 可理解性范围内，没有会改变执行方向或责任边界的实质歧义；
- `REPAIR_REQUIRED`：存在会使执行者做错业务问题、证据范围、职责、停点或后继的实质歧义；
- `INSUFFICIENT_EVIDENCE`：输入不全、发生漂移、独立性不足或无法取得必要正文。

`PASS` 只覆盖这次地图/任务可理解性，不覆盖固定数据正确性、场景选择、U2/U3 业务结论、S3 完成、管理 Gate、Owner 接收或生产资格。

<a id="completion"></a>
## 5. 完成、预算与非循环性

预计一次有效独立 review 回交完成本受托范围，不强制 PASS。真正缺输入或实质判断未完则如实接续，不以补字段冒充完成；不扩成全仓审计或算法验收。

本受托事项不另设 RESULT/CHANGE/EFFORT 循环。主业务的持续复看由专业任务 Binding 和管理责任承担。纯 Return 缺件可有限补交；相同交付错误一次补交仍失败，回管理接管。

<a id="same-work"></a>
## 6. 只读续作

只继续相同 exact 输入上尚未实际阅读/判断的部分，保留已成；不得修改候选、切换为专业执行、重新选择场景或重做已完成的独立判断。输入若实质改变，不再沿用本任务的旧 verdict。

<a id="accept"></a>
## 7. PASS 后的合法消费

完整回交运输回原操作端/管理路由。只有在：

- 实际 Reader 报告可取得；
- exact reader-input 未变；
- verdict 为狭义 `PASS`；
- 独立性、ROLE_RETURN、QUESTION_WORK_RETURN 完整；
- 既有 `workmap_gate.py snapshot/check/dispatch` 真实通过；

操作端才可按 R0001 管理 `DECISION.md#reader-decision` 机械形成 `runs/BI-01-V2-02/reviews/WORKMAP_INTAKE_CURRENT.json`，将 config 从 `NOT_CONFIGURED` 转为 `ADOPTED`，再准备专业首发。不得由操作端把 finding 改判为 PASS，不得把 Reader PASS 写成专业业务 PASS，也不得以 Reader 任务存在声称 Intake 已发生。

<a id="decide"></a>
## 8. 歧义、漂移或权限问题

路由到 `chatgpt:细节叙事生成_金标:BI01-V202-管理`，M-REASSESS。带 exact 输入、具体歧义/漂移、影响的工作和消费者、已读范围与未完。管理负责定向修 map/task/Binding 和重新采用；Reader 不代写候选，不把局部问题扩大成全历史审计。

<a id="parent"></a>
## 9. 父关系

本任务是新 `BI-01-V2-02` 首张 Workmap 的首次独立只读接收，`parent.status=NOT_APPLICABLE_NEW_CASE`。旧 V2-01 Reader 资格不继承。本任务不取消 BI-01 完整管理与专业责任。

<a id="question-work-binding"></a>
## 10. QUESTION_WORK_BINDING

以下 Binding 由 `BI01-V2-02-R0002-20261018T133550Z-3e483710` 在不改变 R0001 人读任务正文和业务输入的前提下补齐。`source_reads.reuse_evidence=null` 表示独立 Reader 必须实际取得正文；它不能借管理者已读状态或旧 Reader 资格。

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
    "commit": "ae5826028a8441a6ee018ebfac48eb0568a7be72",
    "path": "runs/BI-01-V2-02/reviews/management-R0002/DECISION.md",
    "selector": "#reader-pre-adoption"
  },
  "full_scope_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "ae5826028a8441a6ee018ebfac48eb0568a7be72",
    "path": "runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md",
    "selector": "full"
  },
  "batch_result": "独立读取冻结的 BI-01-V2-02 Workmap、专业任务、管理决定、Owner 目标和适用方法，判断未参与编写的执行者能否准确恢复完整业务链、证据资格、撤销/保留边界、完成条件与真实后继；只交可理解性 verdict，不修改候选或签 U2/U3 业务 PASS。",
  "question_ids": [
    "WORKMAP-READABILITY"
  ],
  "professional_mode": "INDEPENDENT_REVIEW",
  "focus_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "ae5826028a8441a6ee018ebfac48eb0568a7be72",
    "path": "runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md",
    "selector": "#focus"
  },
  "coverage_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "ae5826028a8441a6ee018ebfac48eb0568a7be72",
    "path": "runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md",
    "selector": "#coverage"
  },
  "source_reads": [
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "5e8e4c1bb184a97bfe47bc40493c667bb7b8185d",
        "path": "runs/BI-01-V2-02/README.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "恢复本 run overview、旧运行暂停边界和当前真实状态",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "5e8e4c1bb184a97bfe47bc40493c667bb7b8185d",
        "path": "runs/BI-01-V2-02/00_长程推进地图.md",
        "selector": "full"
      },
      "requirement": "MODE_FULL",
      "purpose": "恢复业务问题—证据—认识—Owner/后继的完整管理地图",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "5e8e4c1bb184a97bfe47bc40493c667bb7b8185d",
        "path": "runs/BI-01-V2-02/01_当前任务.md",
        "selector": "full"
      },
      "requirement": "MODE_FULL",
      "purpose": "检查连续 S1/S2/S3 专业任务、专业 Binding、完成条件和路线",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "5e8e4c1bb184a97bfe47bc40493c667bb7b8185d",
        "path": "runtime/config/WORKMAP_BINDING.json",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "核当前 Workmap 结构已具备但 status 仍准确为 NOT_CONFIGURED",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "04fea2ae48eb6bb50144e2b8b2e3fccca17ec7ea",
        "path": "runs/BI-01-V2-02/OWNER_START.md",
        "selector": "full"
      },
      "requirement": "MODE_FULL",
      "purpose": "取得新 run 的真实 Owner GO、旧 V2-01 暂停和不继承边界",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "177e81a32203665cb86ea04e8155dd030782c697",
        "path": "runs/BI-01-V2-02/reviews/management-R0001/DECISION.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "核实管理采用、撤销、预算、Reader 决定和专业后继没有被摘要改写",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
        "path": "professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md",
        "selector": "full"
      },
      "requirement": "MODE_FULL",
      "purpose": "对照 Owner 完整业务目标、三步工作和完成条件",
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
      "purpose": "核 S2 图、同源数据、实际渲染和 aidata 工具边界",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
        "path": "professional/v2/02_OBSERVATION_IDEAS_AND_VALIDATION.md",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "核 S3 事实、设计承诺、反证、基线和行动的完成要求",
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
      "purpose": "核管理、执行 Pro、Worker 和 Owner 的生产/消费职责",
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
      "purpose": "核 I1—I3 是业务 Source 而不是旧 run 状态继承",
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
      "purpose": "核两份固定 ZIP、广域 raw、单 Case 五 As-Of 和身份限制",
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
      "purpose": "核 U2/U3 承重原文、四束与固定结果映射",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
        "path": "professional/v2/07_BUSINESS_SCENE_OBSERVATION_METHOD.md",
        "selector": "full"
      },
      "requirement": "MODE_FULL",
      "purpose": "核场景先行、基础行情自主选位置和 U2/U3/后续/基线链",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
        "path": "runtime/dual_route_execution/DR14_QUESTION_WORK_CONTRACT.md",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "核 Binding、路线、完成、未完和 Return 合同",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
        "path": "runtime/operations/ADOPTION_HANDOFF_CHECKLIST.md",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "核首次 Reader、真实 Intake、ADOPTED 与专业首发的合法顺序",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
        "path": "runtime/overlay/12_管理接收与地图校验.md",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "核 snapshot/check/dispatch、Reader 证据和新消息取源边界",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "30d6cd28ca4cc52eb201f0aa474f9f4c93b74080",
        "path": "runtime/overlay/13_角色回交与主控接续协议.md",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "核 review 回交、独立性、完整 Goal 与主控接续",
      "reuse_evidence": null
    }
  ],
  "deliverables_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "ae5826028a8441a6ee018ebfac48eb0568a7be72",
    "path": "runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md",
    "selector": "#coverage"
  },
  "completion_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "ae5826028a8441a6ee018ebfac48eb0568a7be72",
    "path": "runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md",
    "selector": "#completion"
  },
  "budget_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "ae5826028a8441a6ee018ebfac48eb0568a7be72",
    "path": "runs/BI-01-V2-02/reviews/management-R0002/DECISION.md",
    "selector": "#reader-pre-adoption"
  },
  "routes": {
    "same_work": {
      "recipient_role": "review",
      "recipient_ref": "chatgpt:细节叙事生成_金标:BI01-V202-地图只读接收-01",
      "instructions_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "ae5826028a8441a6ee018ebfac48eb0568a7be72",
        "path": "runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md",
        "selector": "#same-work"
      }
    },
    "accept": {
      "recipient_role": "management",
      "recipient_ref": "chatgpt:细节叙事生成_金标:BI01-V202-管理",
      "instructions_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "ae5826028a8441a6ee018ebfac48eb0568a7be72",
        "path": "runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md",
        "selector": "#accept"
      }
    },
    "decide": {
      "recipient_role": "management",
      "recipient_ref": "chatgpt:细节叙事生成_金标:BI01-V202-管理",
      "instructions_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "ae5826028a8441a6ee018ebfac48eb0568a7be72",
        "path": "runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md",
        "selector": "#decide"
      }
    },
    "return_repair": {
      "recipient_role": "review",
      "recipient_ref": "chatgpt:细节叙事生成_金标:BI01-V202-地图只读接收-01",
      "instructions_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "ae5826028a8441a6ee018ebfac48eb0568a7be72",
        "path": "runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md",
        "selector": "#completion"
      }
    }
  },
  "triggers": [],
  "explicit_no_trigger_reason_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "ae5826028a8441a6ee018ebfac48eb0568a7be72",
    "path": "runs/BI-01-V2-02/reviews/management-R0002/DECISION.md",
    "selector": "#reader-pre-adoption"
  },
  "parent": {
    "status": "NOT_APPLICABLE_NEW_CASE",
    "ref": null,
    "reason_ref": {
      "repo": "daowei2026/observe-iterate",
      "commit": "ae5826028a8441a6ee018ebfac48eb0568a7be72",
      "path": "runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md",
      "selector": "#parent"
    }
  },
  "question_definitions": []
}
```

来源：daowei2026/observe-iterate@e3d65aa5131be591416b861343afa9953eaf6661:runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md::full

## 本轮原文与位置

本次原始要求：`daowei2026/observe-iterate@ae5826028a8441a6ee018ebfac48eb0568a7be72:runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md::#same-work`
当前生效任务：`daowei2026/observe-iterate@e3d65aa5131be591416b861343afa9953eaf6661:runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md::full`
当前任务采用依据：`daowei2026/observe-iterate@ae5826028a8441a6ee018ebfac48eb0568a7be72:runs/BI-01-V2-02/reviews/management-R0002/DECISION.md::#adoption`
上一轮实际采用的任务绑定：`daowei2026/observe-iterate@e3d65aa5131be591416b861343afa9953eaf6661:runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md::L127-L444`
接收完整范围：`daowei2026/observe-iterate@ae5826028a8441a6ee018ebfac48eb0568a7be72:runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md::full`
本次接收重点：`daowei2026/observe-iterate@ae5826028a8441a6ee018ebfac48eb0568a7be72:runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md::#focus`
接收交付：`daowei2026/observe-iterate@ae5826028a8441a6ee018ebfac48eb0568a7be72:runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md::#coverage`
接收完成条件：`daowei2026/observe-iterate@ae5826028a8441a6ee018ebfac48eb0568a7be72:runs/BI-01-V2-02/reviews/management-R0001/READER_TASK.md::#completion`

## 本次直接读取的上下文

- FOCUS_FULL：`daowei2026/observe-iterate@5e8e4c1bb184a97bfe47bc40493c667bb7b8185d:runs/BI-01-V2-02/README.md::full`
  用途与边界：恢复本 run overview、旧运行暂停边界和当前真实状态
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@5e8e4c1bb184a97bfe47bc40493c667bb7b8185d:runs/BI-01-V2-02/00_长程推进地图.md::full`
  用途与边界：恢复业务问题—证据—认识—Owner/后继的完整管理地图
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@5e8e4c1bb184a97bfe47bc40493c667bb7b8185d:runs/BI-01-V2-02/01_当前任务.md::full`
  用途与边界：检查连续 S1/S2/S3 专业任务、专业 Binding、完成条件和路线
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@5e8e4c1bb184a97bfe47bc40493c667bb7b8185d:runtime/config/WORKMAP_BINDING.json::full`
  用途与边界：核当前 Workmap 结构已具备但 status 仍准确为 NOT_CONFIGURED
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@04fea2ae48eb6bb50144e2b8b2e3fccca17ec7ea:runs/BI-01-V2-02/OWNER_START.md::full`
  用途与边界：取得新 run 的真实 Owner GO、旧 V2-01 暂停和不继承边界
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@177e81a32203665cb86ea04e8155dd030782c697:runs/BI-01-V2-02/reviews/management-R0001/DECISION.md::full`
  用途与边界：核实管理采用、撤销、预算、Reader 决定和专业后继没有被摘要改写
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md::full`
  用途与边界：对照 Owner 完整业务目标、三步工作和完成条件
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:professional/v2/01_AIDATA_CHART_AND_DATA.md::full`
  用途与边界：核 S2 图、同源数据、实际渲染和 aidata 工具边界
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:professional/v2/02_OBSERVATION_IDEAS_AND_VALIDATION.md::full`
  用途与边界：核 S3 事实、设计承诺、反证、基线和行动的完成要求
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:professional/v2/03_EXECUTION_HANDOFF.md::full`
  用途与边界：核管理、执行 Pro、Worker 和 Owner 的生产/消费职责
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:professional/v2/04_BI01_BUSINESS_BASELINE.md::full`
  用途与边界：核 I1—I3 是业务 Source 而不是旧 run 状态继承
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:professional/v2/05_BI01_FIXED_INPUT_DATA.md::full`
  用途与边界：核两份固定 ZIP、广域 raw、单 Case 五 As-Of 和身份限制
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md::full`
  用途与边界：核 U2/U3 承重原文、四束与固定结果映射
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:professional/v2/07_BUSINESS_SCENE_OBSERVATION_METHOD.md::full`
  用途与边界：核场景先行、基础行情自主选位置和 U2/U3/后续/基线链
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:runtime/dual_route_execution/DR14_QUESTION_WORK_CONTRACT.md::full`
  用途与边界：核 Binding、路线、完成、未完和 Return 合同
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:runtime/operations/ADOPTION_HANDOFF_CHECKLIST.md::full`
  用途与边界：核首次 Reader、真实 Intake、ADOPTED 与专业首发的合法顺序
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:runtime/overlay/12_管理接收与地图校验.md::full`
  用途与边界：核 snapshot/check/dispatch、Reader 证据和新消息取源边界
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@30d6cd28ca4cc52eb201f0aa474f9f4c93b74080:runtime/overlay/13_角色回交与主控接续协议.md::full`
  用途与边界：核 review 回交、独立性、完整 Goal 与主控接续
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

读取Owner完整要求、生效完整任务和输入输出地图，不能用最新remaining替全部责任。按source_reads取得准确正文用于判断，已读未变且可恢复者复用；不递归扫无关历史，不用索引/hash/旧回执代正文。

旧包中已被Owner否定的多余任务，必须由原有权责任者从当前正文、任务、前置、接收和后继删除；只为其存在的辅助代码与检查交原实现者删除。禁止继续完善、改名或列为暂缓/未来优化。不能只在顶部写新原则却继续采用相反正文。真实业务方法、时间、身份、状态、正式输出与消费者保留，技术机制替换回正常平台。正确正文禁止任何压缩或摘要替换。历史提交和实际记录不倒改；历史可追溯不授后续派发。通用材料维护不自动取得用例任务写权。

当前执行材料由管理和有权任务责任者明确采用。推进者取得实际需要的正确正文，不能用管理概述替代业务细节；也不要求每轮重读全部历史和已撤完整任务。

发现新的实质冲突时，给出准确位置与受影响结论，按原责任处理。来源不足只限制真正依赖的判断，不用旧快照补造事实，也不冻结无关工作。

方法版本、业务合同版本、源码版本和运行数据分别保持准确，不随一次方法更新全部追 latest。

运行事实（来自现有记录）：
观察时间：2026-10-18T13:55:02.204968+00:00

按既有协议交完整实质回答及ROLE_RETURN/QUESTION_WORK_RETURN，来源、未执行和资格如实保留，不新增控制表，不重抄协调者已存提示。完整任务未完成就保留完整责任及连续后继，局部交付不自设停点。要求GitHub提交时普通快进并fresh回读，最后commit message带turn complete及本轮invocation_id，无invocation时简要标明执行身份；不造空提交。

专业者回交实际实物、必要自检／执行结果、具体限制及完整未完，不代写管理接收、全局预算或主控派发。管理回交已完成的判断、实际处置和可执行后继，不以问题目录代替决定。

没有完整完成时，说明真实停止原因及已经明确的下一步；不得以自设局部目标完成作为结束解释。
