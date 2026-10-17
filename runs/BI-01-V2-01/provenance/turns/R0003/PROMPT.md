[BI01-V2-01-R0003-104e88d2b67a7431818598f2]
work_id: BI-01
invocation_id: BI01-V2-01-R0003-104e88d2b67a7431818598f2
assignment_token: 17de901f52e643eafe271fc279450dbb
role: review
recipient: chatgpt-project:细节叙事生成_金标/chat:new:BI01-V2-地图只读接收-01
当前阶段：专业任务 BI01
当前职责：专业任务 BI01 独立只读审查
对应专业工作：具名独立只读审查（专业方法未齐，不自动通过）

本角色仅在存在真实独立审查委派与可取得exact被审对象时使用。按照[V2 交接方法](../../professional/v2/03_EXECUTION_HANDOFF.md)及本次真实被审业务目标和专业方法实际核对专业主张、反例、证据适用范围及影响；不信作者自评，不代写候选后自签。当前专业审查方法仍为PARTIAL时，如需超出现有合同的正式独立审查，明确MISSING并请求有权补充，不因通用role/review模板存在就报告PASS。管理Gate、执行自查、Worker技术验收、Owner决定彼此不能替代。
本轮独立审查若 GitHub 提交不可用，同样可以依 [V2 轮次 ZIP 合同](../../runtime/operations/V2_ROUND_RECORD_CONTRACT.md) 将原审查结果 ZIP 写入 MCP server 可写的 `H:\fy\observe-iterate-share`，由操作 Codex 在 `/dwdhome/fy/observe-iterate-share` 检查并合法发布；必须保留真实评审权限和完整 Return，不能因 ZIP 出现而自称审查/管理已接收。

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

# BI-01 V2 首次地图独立只读接收任务

task_id: BI01-V2-WORKMAP-READER-01
work_id: BI-01
run_id: BI-01-V2-01
professional_mode: INDEPENDENT_REVIEW
recipient_role: review
recipient_ref: chatgpt-project:细节叙事生成_金标/chat:new:BI01-V2-地图只读接收-01

此为 R0001 管理在既有 review 职责中签发的同一一次性、只读工作；R0002 保留其完整正确范围，更新实际被审输入、前置适用性和接收依据。新上下文尚未创建、未发送、未返回。不新增常驻角色或审查系统，不授 U2/U3 全业务独立审查 PASS。真正曾参与这份候选形成的承办者不得作为独立读者，即使换聊天也不独立。

<a id="scope"></a>
## 1. 完整受托范围

按既有 Workmap 首次采用合同，独立阅读下列 exact 输入，从 Owner 完整目的而不是地图作者的状态名称，确认：一个没有参加编写的读者能否理解业务要检验什么、已有真实数据和其资格、当前完整任务、生产者/消费者、局部阻塞边界、未完和实际后继。

只判地图/任务可理解性及前后一致性。不得编制、改写或修补地图/任务，不替管理签预算/全局接受，不给 U2/U3 公式、图、数据或投资判断做未实际执行的专业验证。发现问题给具体位置、原文、导致何种执行误解和受影响范围；非问题不凑 finding。

必须区分首次地图阅读与 AI 视觉看行情：此处读的是管理/任务文字；本轮 Owner 看 aidata 图，业务执行 Pro 读图对应结构化数据，不要求像素进入模型。

<a id="target"></a>
## 2. 已冻结的实际输入

工作输入锁 `daowei2026/observe-iterate@f87a9a64f4f0fa3ead13b9ee7c108f87847a581a`：

- `runs/BI-01-V2-01/README.md::full`；
- `runs/BI-01-V2-01/00_长程推进地图.md::full`，七个业务锚点 goal/stage/evidence/progress/remaining/management/next；
- `runs/BI-01-V2-01/01_当前任务.md::full`，包含 `#question-work-binding`，task_id `BI01-V2-S123-OBSERVATION-01`，task blob `442c47cc30226796a16b6f7420af9748d0d1e00e`；
- `runs/BI-01-V2-01/reviews/management-R0001/DECISION.md::full`，保留正确业务判断，不把其旧运行状态当当前事实；
- `runs/BI-01-V2-01/reviews/management-R0002/DECISION.md::full`，当前前置裁定、实际后继和接收依据；
- `runtime/config/WORKMAP_BINDING.json::full`。

Owner 原文锁 `11626f64bc64ae21e52108b2e47fafbbc1023615:professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md::full`，真实启动 `e07034fbab080df85af57da4362d5a24119a8bbe:runs/BI-01-V2-01/OWNER_START.md::full`。同一 policy lock 的 V2 04/05/06/01/02/03、ADOPTION_HANDOFF_CHECKLIST、DR14、Overlay13 和原 Workmap 工具是适用方法；首次只读派发采用本次 R0002 的具名用途修正。读者不需要为地图可读性重做 EAW 全公式审计，也不能仅凭管理概述认为算法已被独立验过。

原 `ff84e7e9d22d4c6d6e2633c9701404afcca1b827` 输入及 `69d96209b16115ac1ce9ac9d65402be11f11c358ced9dd6d223b5b287343a8d7` 指纹仅保留为实际历史 snapshot。此前并无独立报告。本次地图更新运行事实和后继，须对上列新 commit 重新用既有工具取得 reader_fingerprint；不能复制旧指纹或说已读过本次新输入。

上述输入后的回交、读取任务及 provenance 提交不是重新定义业务。操作端在发送前确认 reader-input 仍一致；若 map/task/Owner/rules 发生实质变化，用实际有权的新 input 重新绑定，不能把旧 reader 报告冒充新输入报告。

<a id="focus"></a>
## 3. 需要实际恢复出来的业务关系

用自己的话完整说明这项业务如何从固定 rb/i/hc 数据，经过 S1 观察问题、S2 aidata 真实图/同源数据，到 S3 事实/反证/增量认识与管理/Owner 下一行动。以下是当前容易发生误读而需核查的承重点，不是让你只审几条而忽略完整范围：

304 条同实际 UTI raw 候选与一个 Case 五个 As-Of 是两个不同证据层；只有前者中的两成员候选可在三品种内看第三对象，完整 Case 组外数为零。四方面为 Movement Bundles，不是四资金接口。Working/Completed、actual/known/As-Of 和 Reference/Shadow/Withheld 不混同。初始 OBSERVATION_SCOPE 绑定 S1/S2/S3 完整职责，而不是 S1 做完就停，也不允许未经管理改机器 mode/角色。

同时恢复明确的排除项：不重算/替换固定数据，不等待正式 H1，不做 AI 像素看图，不重测已确认基础环境，不在观察仓建第二套图工具；必要 aidata 通用修改只在独立新分支。核是否存在“管理说排除、实际当前任务又要求”的相反正文。对正确业务字段、状态、时间、方法和消费者不能用删除来消歧。

新增的前置处置只限：本受托 reader 在尚未 adopted 时产生采用所需的阅读证据；它不取得 S1—S3 业务执行权。原 Codex 线程受派 Worker 修 gate 不等于编制或独立接收了本地图；你无需把本次阅读扩成该代码的独立验收。

<a id="coverage"></a>
## 4. 输出、完成与资格

交完整只读报告到 `runs/BI-01-V2-01/reviews/independent/WORKMAP_READER_INITIAL.md`，标明实际调用身份、实际输入 commit、task blob、真实阅读范围、是否真正未参与候选形成、恢复出的完整业务关系、确切歧义及其影响。没有实质歧义才可将本次狭义地图阅读 verdict 写 PASS；有歧义写 REPAIR_REQUIRED，资料或独立性不足写 INSUFFICIENT_EVIDENCE。PASS 只覆盖此次地图可理解性，不覆盖固定计算正确性、S3 完成、正式质量或 Owner 接收。

<a id="completion"></a>
完成指上述范围已真实阅读并报告结论，必要原文不足及未审部分如实披露，附原 ROLE_RETURN 的 review 输出和 QUESTION_WORK_RETURN；不能因 report 文件存在就称独立接收发生。不得修改候选；受本次委托可提交自己的独立报告及本轮回交。操作端按真实新 R 记录；R0002 是已发生的管理接续，不是读者，后续待派 R 尚不预记为已发生。

<a id="budget"></a>
## 5. 预算与不中断完整业务责任

当前预测一次有效只读调用即可完成本受托范围，不是强制一次 PASS。确欠输入/独立性或实质分析未完按真实限制接续，不能以补字段冒充完成；不把阅读扩成全仓审计或 U2/U3 算法验收。它计入原 BI-01 V2 的必要 Pro 实际投入，不新建总预算、不清零 R0001 起点。

<a id="no-extra-trigger"></a>
不为这项一次性地图接收另设 RESULT/CHANGE/EFFORT 循环：完整工作持续复看已由专业任务 Binding 的三个触发及本管理承担；本受托事项按一次完成/缺件/实质歧义路由返回，不能与主工作并行重复同一管理义务。

<a id="same-work"></a>
## 6. 只读续作/有限补交

继续相同 exact 输入的本地图只读受托范围，仅补尚未实际阅读/判断的部分，保留真实已成；不能修改地图或切换成业务执行。纯回交缺字段只补确切缺件，不重做已成判断。相同交付错误一次有限补交后仍失败，交当前管理接管，不无限回到读者重复同句。

<a id="accept"></a>
## 7. 实际收取与已签采用路径

完整回交运输回原操作端 `codex-thread:01a14a59-7f26-7921-b549-3e7cd9be5119`。该接收者在收取/投递时是既有操作 Codex，不是新业务裁定角色；其受派修 gate 的 Worker 容量限于 R0002 明确工单。当前合法业务依据为 `f87a9a64f4f0fa3ead13b9ee7c108f87847a581a:runs/BI-01-V2-01/reviews/management-R0002/DECISION.md#adoption`：独立读者能完整恢复任务且无实质歧义时，允许对同一 reader-input 按既有工具机械发布 Workmap Intake 与采用，无需 Owner 再批启动；实质歧义必须走下节管理决定，不由操作端看 finding 自行判业务通过。

本任务派发前由 R0002 已受派 Worker 修通采用前只读 gate，保留原样载荷、来源、角色和实际非重复发送检查，不提前填 ADOPTED/Intake/reader PASS，不使用采用后专业 Workmap dispatch 反向检查首次 reader。具体工程在 R0002 工单，读者不施工、不自签该代码正确。

操作端需要从真实 local Git 执行原 `runtime/overlay/tools/workmap_gate.py snapshot`，记录上列观察输入及新 fingerprint。提交真实 reader 报告后，以实际最新 Git 中相同 map/task/Owner/rules 的输入核 `reader_fingerprint`；reader-input 未变可复用该真实报告，不因它自己的报告加入 result tree 而重复开读者。Intake 的 manager decision_report 绑定实际 R0002 决定及 blob，reader 绑定真实 report/input_commit/input_snapshot；不得填假 reader、snapshot 或 validation_claim。

Intake 写在原配置的 `runs/BI-01-V2-01/reviews/WORKMAP_INTAKE_CURRENT.json`，专业新任务按首次签发而非 ROUTINE_RESULT 处理；原始 Owner GO、policy、专业 Binding 与完整 task_payload 原样保留。实物/前置校验满足后，再机械将 config 标 ADOPTED，并使用原 check/dispatch、真实发送端 NOT_SENT 和任务载荷身份核验。`provenance/turns` 不纳入业务 watch 根。这个过程不启动 U2/U3 重算，也不改变专业完整任务。

采用时的 base 为首次真实管理开始前的 `2e817e2e8408b714185be55aa8f443e389b92ddf`：当时已有模板 config，但 map/task/intake 尚不存在。读者不改工具；已受派 Worker 按 R0002 工单核查、修通同一首建合同的必要直接消费者，不再逐错误申请；实质新权限/业务冲突仍回管理。不随意拿 current 充当旧已接收 base，不关闭普通专业 gate。读取、记录、发布和 actual send 分别报告。

<a id="decide"></a>
## 8. 歧义、前提冲突或权限问题

交 `chatgpt-project:细节叙事生成_金标/chat:BI01-V2-管理`，M-REASSESS。带 exact input、具体歧义、对哪个工作/消费者的实际影响、你的真实阅读结论及未完。管理负责修 map/task/Binding 和重新采用，不让读者代写候选；不把局部问题升级成全部业务或全历史审计。没有实质问题就不发明新限制。

<a id="parent"></a>
本次是新 run 首张地图的首次独立只读接收，没有旧 run 可复用的 reader 资格；R0002 没有取代或完成读者。parent 为 NOT_APPLICABLE_NEW_CASE；这是受托事项关系，不取消 BI-01 完整管理和专业责任。

<a id="question-work-binding"></a>
## 9. QUESTION_WORK_BINDING

本绑定引用 `126a914eb07356fd333acffd98d5db7b9aff5cda` 的完整受托正文；被审地图输入锁 `f87a9a64f4f0fa3ead13b9ee7c108f87847a581a`。source_reads 必须由目标读者真实取得，不能继承管理者的已读状态。当前 task_payload 为包含本节的完整任务，操作端按其实际发布 commit 冻结并定位 JSON 的实际行范围，不沿用旧行号。

```json
{
  "schema":"question-work/v2",
  "kind":"BINDING",
  "work_id":"BI-01",
  "goal_ref":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md","selector":"full"},
  "plan_ref":{"repo":"daowei2026/observe-iterate","commit":"f87a9a64f4f0fa3ead13b9ee7c108f87847a581a","path":"runs/BI-01-V2-01/reviews/management-R0002/DECISION.md","selector":"#reader-pre-adoption"},
  "full_scope_ref":{"repo":"daowei2026/observe-iterate","commit":"126a914eb07356fd333acffd98d5db7b9aff5cda","path":"runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md","selector":"full"},
  "batch_result":"完成 exact-input 首次管理地图和完整任务的独立只读可理解性接收，交真实阅读报告和明确狭义资格；不编修候选、不审行情像素、不自签 U2/U3 全业务或派发代码通过。",
  "question_ids":["AUDIT"],
  "question_definitions":[],
  "professional_mode":"INDEPENDENT_REVIEW",
  "focus_ref":{"repo":"daowei2026/observe-iterate","commit":"126a914eb07356fd333acffd98d5db7b9aff5cda","path":"runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md","selector":"#focus"},
  "coverage_ref":{"repo":"daowei2026/observe-iterate","commit":"126a914eb07356fd333acffd98d5db7b9aff5cda","path":"runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md","selector":"#coverage"},
  "source_reads":[
    {"source":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md","selector":"full"},"requirement":"MODE_FULL","purpose":"从 Owner 原完整目标校验，而不是仅核作者概述自洽","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"e07034fbab080df85af57da4362d5a24119a8bbe","path":"runs/BI-01-V2-01/OWNER_START.md","selector":"full"},"requirement":"BOUNDARY","purpose":"真实新 run GO 和原权限，不继承旧 run","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"f87a9a64f4f0fa3ead13b9ee7c108f87847a581a","path":"runs/BI-01-V2-01/README.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"总体入口、当前状态与实际采用关系","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"f87a9a64f4f0fa3ead13b9ee7c108f87847a581a","path":"runs/BI-01-V2-01/00_长程推进地图.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"被审完整地图、重要未完和消费者，包含R0002真实运行处置","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"f87a9a64f4f0fa3ead13b9ee7c108f87847a581a","path":"runs/BI-01-V2-01/01_当前任务.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"被审完整 S1-S3 任务及专业 Binding，未因修gate缩小或重写","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"f87a9a64f4f0fa3ead13b9ee7c108f87847a581a","path":"runs/BI-01-V2-01/reviews/management-R0001/DECISION.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"保留采用/撤销、两证据层、四束、资格和预算决定；旧运行状态由R0002更新","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"f87a9a64f4f0fa3ead13b9ee7c108f87847a581a","path":"runs/BI-01-V2-01/reviews/management-R0002/DECISION.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"当前采用前只读权限、受派技术工作和实际连续后继；不要求读者独立验代码","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"f87a9a64f4f0fa3ead13b9ee7c108f87847a581a","path":"runtime/config/WORKMAP_BINDING.json","selector":"full"},"requirement":"FOCUS_FULL","purpose":"真实路径/锚点/输入与尚未 ADOPTED 的事实","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"professional/v2/04_BI01_BUSINESS_BASELINE.md","selector":"full"},"requirement":"BOUNDARY","purpose":"旧业务知识与旧运行状态不能混同","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"professional/v2/05_BI01_FIXED_INPUT_DATA.md","selector":"full"},"requirement":"BOUNDARY","purpose":"固定输入/身份差异/范围，不重复审算法","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md","selector":"full"},"requirement":"BOUNDARY","purpose":"业务原文与方法入口是否明确到可取正文","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"professional/v2/01_AIDATA_CHART_AND_DATA.md","selector":"full"},"requirement":"BOUNDARY","purpose":"图数同源、AI不看像素和必要工具修改新分支","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"professional/v2/02_OBSERVATION_IDEAS_AND_VALIDATION.md","selector":"full"},"requirement":"BOUNDARY","purpose":"S3 真实业务认识的完整终点而非首图停点","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"professional/v2/03_EXECUTION_HANDOFF.md","selector":"full"},"requirement":"BOUNDARY","purpose":"专业、Worker、管理和操作的正确分界","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"runtime/operations/ADOPTION_HANDOFF_CHECKLIST.md","selector":"full"},"requirement":"MODE_FULL","purpose":"首次独立地图读取与实际采用，不自签；前置适用性按R0002具名决定","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"runtime/dual_route_execution/DR14_QUESTION_WORK_CONTRACT.md","selector":"full"},"requirement":"BOUNDARY","purpose":"当前受托原文、Return 和合法续作","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"11626f64bc64ae21e52108b2e47fafbbc1023615","path":"runtime/overlay/13_角色回交与主控接续协议.md","selector":"full"},"requirement":"BOUNDARY","purpose":"真实独立身份、狭义 review 输出与回交","reuse_evidence":null}
  ],
  "deliverables_ref":{"repo":"daowei2026/observe-iterate","commit":"126a914eb07356fd333acffd98d5db7b9aff5cda","path":"runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md","selector":"#coverage"},
  "completion_ref":{"repo":"daowei2026/observe-iterate","commit":"126a914eb07356fd333acffd98d5db7b9aff5cda","path":"runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md","selector":"#completion"},
  "budget_ref":{"repo":"daowei2026/observe-iterate","commit":"126a914eb07356fd333acffd98d5db7b9aff5cda","path":"runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md","selector":"#budget"},
  "parent":{"status":"NOT_APPLICABLE_NEW_CASE","ref":null,"reason_ref":{"repo":"daowei2026/observe-iterate","commit":"126a914eb07356fd333acffd98d5db7b9aff5cda","path":"runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md","selector":"#parent"}},
  "routes":{
    "same_work":{"recipient_role":"review","recipient_ref":"chatgpt-project:细节叙事生成_金标/chat:new:BI01-V2-地图只读接收-01","instructions_ref":{"repo":"daowei2026/observe-iterate","commit":"126a914eb07356fd333acffd98d5db7b9aff5cda","path":"runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md","selector":"#same-work"}},
    "accept":{"recipient_role":"receiver","recipient_ref":"codex-thread:01a14a59-7f26-7921-b549-3e7cd9be5119","instructions_ref":{"repo":"daowei2026/observe-iterate","commit":"126a914eb07356fd333acffd98d5db7b9aff5cda","path":"runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md","selector":"#accept"}},
    "decide":{"recipient_role":"management","recipient_ref":"chatgpt-project:细节叙事生成_金标/chat:BI01-V2-管理","instructions_ref":{"repo":"daowei2026/observe-iterate","commit":"126a914eb07356fd333acffd98d5db7b9aff5cda","path":"runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md","selector":"#decide"}},
    "return_repair":{"recipient_role":"review","recipient_ref":"chatgpt-project:细节叙事生成_金标/chat:new:BI01-V2-地图只读接收-01","instructions_ref":{"repo":"daowei2026/observe-iterate","commit":"126a914eb07356fd333acffd98d5db7b9aff5cda","path":"runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md","selector":"#same-work"}}
  },
  "triggers":[],
  "explicit_no_trigger_reason_ref":{"repo":"daowei2026/observe-iterate","commit":"126a914eb07356fd333acffd98d5db7b9aff5cda","path":"runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md","selector":"#no-extra-trigger"}
}
```

来源：daowei2026/observe-iterate@df7bfd51a626be7a63ce97d58bdbc90e7a1583b8:runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md::full

## 本轮原文与位置

本次原始要求：`daowei2026/observe-iterate@126a914eb07356fd333acffd98d5db7b9aff5cda:runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md::#same-work`
当前生效任务：`daowei2026/observe-iterate@df7bfd51a626be7a63ce97d58bdbc90e7a1583b8:runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md::full`
当前任务采用依据：`daowei2026/observe-iterate@f87a9a64f4f0fa3ead13b9ee7c108f87847a581a:runs/BI-01-V2-01/reviews/management-R0002/DECISION.md::#adoption`
上一轮实际采用的任务绑定：`daowei2026/observe-iterate@df7bfd51a626be7a63ce97d58bdbc90e7a1583b8:runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md::L98-L142`
接收完整范围：`daowei2026/observe-iterate@126a914eb07356fd333acffd98d5db7b9aff5cda:runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md::full`
本次接收重点：`daowei2026/observe-iterate@126a914eb07356fd333acffd98d5db7b9aff5cda:runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md::#focus`
接收交付：`daowei2026/observe-iterate@126a914eb07356fd333acffd98d5db7b9aff5cda:runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md::#coverage`
接收完成条件：`daowei2026/observe-iterate@126a914eb07356fd333acffd98d5db7b9aff5cda:runs/BI-01-V2-01/reviews/management-R0001/READER_TASK.md::#completion`

## 本次直接读取的上下文

- MODE_FULL：`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:professional/v2/00_PURPOSE_AND_THREE_STEP_FLOW.md::full`
  用途与边界：从 Owner 原完整目标校验，而不是仅核作者概述自洽
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@e07034fbab080df85af57da4362d5a24119a8bbe:runs/BI-01-V2-01/OWNER_START.md::full`
  用途与边界：真实新 run GO 和原权限，不继承旧 run
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@f87a9a64f4f0fa3ead13b9ee7c108f87847a581a:runs/BI-01-V2-01/README.md::full`
  用途与边界：总体入口、当前状态与实际采用关系
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@f87a9a64f4f0fa3ead13b9ee7c108f87847a581a:runs/BI-01-V2-01/00_长程推进地图.md::full`
  用途与边界：被审完整地图、重要未完和消费者，包含R0002真实运行处置
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@f87a9a64f4f0fa3ead13b9ee7c108f87847a581a:runs/BI-01-V2-01/01_当前任务.md::full`
  用途与边界：被审完整 S1-S3 任务及专业 Binding，未因修gate缩小或重写
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@f87a9a64f4f0fa3ead13b9ee7c108f87847a581a:runs/BI-01-V2-01/reviews/management-R0001/DECISION.md::full`
  用途与边界：保留采用/撤销、两证据层、四束、资格和预算决定；旧运行状态由R0002更新
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@f87a9a64f4f0fa3ead13b9ee7c108f87847a581a:runs/BI-01-V2-01/reviews/management-R0002/DECISION.md::full`
  用途与边界：当前采用前只读权限、受派技术工作和实际连续后继；不要求读者独立验代码
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@f87a9a64f4f0fa3ead13b9ee7c108f87847a581a:runtime/config/WORKMAP_BINDING.json::full`
  用途与边界：真实路径/锚点/输入与尚未 ADOPTED 的事实
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:professional/v2/04_BI01_BUSINESS_BASELINE.md::full`
  用途与边界：旧业务知识与旧运行状态不能混同
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:professional/v2/05_BI01_FIXED_INPUT_DATA.md::full`
  用途与边界：固定输入/身份差异/范围，不重复审算法
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:professional/v2/06_U2_U3_DESIGN_SOURCE_MAP.md::full`
  用途与边界：业务原文与方法入口是否明确到可取正文
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:professional/v2/01_AIDATA_CHART_AND_DATA.md::full`
  用途与边界：图数同源、AI不看像素和必要工具修改新分支
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:professional/v2/02_OBSERVATION_IDEAS_AND_VALIDATION.md::full`
  用途与边界：S3 真实业务认识的完整终点而非首图停点
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:professional/v2/03_EXECUTION_HANDOFF.md::full`
  用途与边界：专业、Worker、管理和操作的正确分界
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:runtime/operations/ADOPTION_HANDOFF_CHECKLIST.md::full`
  用途与边界：首次独立地图读取与实际采用，不自签；前置适用性按R0002具名决定
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:runtime/dual_route_execution/DR14_QUESTION_WORK_CONTRACT.md::full`
  用途与边界：当前受托原文、Return 和合法续作
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@11626f64bc64ae21e52108b2e47fafbbc1023615:runtime/overlay/13_角色回交与主控接续协议.md::full`
  用途与边界：真实独立身份、狭义 review 输出与回交
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

读取Owner完整要求、生效完整任务和输入输出地图，不能用最新remaining替全部责任。按source_reads取得准确正文用于判断，已读未变且可恢复者复用；不递归扫无关历史，不用索引/hash/旧回执代正文。

旧包中已被Owner否定的多余任务，必须由原有权责任者从当前正文、任务、前置、接收和后继删除；只为其存在的辅助代码与检查交原实现者删除。禁止继续完善、改名或列为暂缓/未来优化。不能只在顶部写新原则却继续采用相反正文。真实业务方法、时间、身份、状态、正式输出与消费者保留，技术机制替换回正常平台。正确正文禁止任何压缩或摘要替换。历史提交和实际记录不倒改；历史可追溯不授后续派发。通用材料维护不自动取得用例任务写权。

当前执行材料由管理和有权任务责任者明确采用。推进者取得实际需要的正确正文，不能用管理概述替代业务细节；也不要求每轮重读全部历史和已撤完整任务。

发现新的实质冲突时，给出准确位置与受影响结论，按原责任处理。来源不足只限制真正依赖的判断，不用旧快照补造事实，也不冻结无关工作。

方法版本、业务合同版本、源码版本和运行数据分别保持准确，不随一次方法更新全部追 latest。

按既有协议交完整实质回答及ROLE_RETURN/QUESTION_WORK_RETURN，来源、未执行和资格如实保留，不新增控制表，不重抄协调者已存提示。完整任务未完成就保留完整责任及连续后继，局部交付不自设停点。要求GitHub提交时普通快进并fresh回读，最后commit message带turn complete及本轮invocation_id，无invocation时简要标明执行身份；不造空提交。

专业者回交实际实物、必要自检／执行结果、具体限制及完整未完，不代写管理接收、全局预算或主控派发。管理回交已完成的判断、实际处置和可执行后继，不以问题目录代替决定。

没有完整完成时，说明真实停止原因及已经明确的下一步；不得以自设局部目标完成作为结束解释。
