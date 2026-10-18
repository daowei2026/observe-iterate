[BI01-V2-01-R0010-9c54d7a73e2bd619ee5d9f47]
work_id: BI-01
invocation_id: BI01-V2-01-R0010-9c54d7a73e2bd619ee5d9f47
assignment_token: 99ff37c6ea307fb90ba24f046e
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

<a id="continuation"></a>
## 八、交原操作端及专业者的完整接续

原操作端`codex-thread:01a14a59-7f26-7921-b549-3e7cd9be5119`先收本R9全文及两份Return，核身份、远端同轮实物和原R9派发Binding。按本轮#adoption办理真实增量Intake；R8无Return状态保留，不对它运行伪造after-return，也不把当前R9当成R8的补交。

核旧结果和真实在途状态后，沿原same_work向`chatgpt-project:细节叙事生成_金标/chat:BI01-V2-执行`准备**采用本轮新安排的正常专业接续**。使用原完整task/Binding与本R9实际提交的#adoption、#plan及本节，不重新搬R8原稿只换marker。保持原样载荷、真实接收者/当前标记、NOT_SENT与去重检查；下一R/token由实际主控生成，本文不预记发送成功。

专业接续正文如下：

> 继续BI01-V2-S123-OBSERVATION-01完整S1—S3。R8两次承诺发送后没有可取得原答，不能继承其未证实进展；已成业务起点仍为R6真实实物及R7已接收F01—F07和时间/证据限制。不要重做S1、首次reader、定位修补、原图数生产或51包运输。
>
> 直接从`b9ecbfa4b27f40365ed72f35448116420fb085a6:runs/BI-01-V2-01/artifacts/worker-R0004/readable_views/REQUESTED_51_CURRENT/READING_GUIDE.md`及其原VIEW/SOURCE_BINDING/CSV进入；原最终图数索引锁1917f868d61f8de7110b7165ee9125e5b156c4d2。读取实际所需同图数据，文件截断按行范围续取，不能用索引或管理概述代正文。
>
> 本次按业务问题形成并及时保存实证正文，不先机械读完全5430CSV再写认识。原专业artifacts中使用自身调用成果位置，第一份新增内容就要有真实数据、图数定位、支持/反证与限制；成熟的实质增量正常提交后继续后继。不要造空框架/空提交，不为每次中间保存新开Pro或请求管理。完整任务未完时不因一个Case、一组窗口或一份文件完成而停止；最终回交资格仍按原合同。
>
> 持续完成原已选C1广域/第三品种/可知时效、11个未覆盖turn、主Case五As-Of剩余层，以及Progress/Friction/Retention/ObservabilityAndConstraint的增量分账。用支持例和反例检验F05，区分原成员与当前N、段内与跨段、当时知识与事后辅助字段；不预定谁最好、不重算指标。原35个C1及相关剩余必须有业务处置，51/320不是完成配额。
>
> 以事实和反例说明哪些设计应保留、具体哪里应改、什么观察会推翻、哪些无增量或无法判断；比较Node-only、静态分组和简单共同事件关联，不能只宣布组织变清楚。现成但未读数据与固定包真正没有输出的设计环节分别记录。正确业务原文、方法、字段、状态与已知限制完整保留，已读未变者按实际记录复用。
>
> 不承担UI根因诊断、全仓审计或管理/主控职责。GitHub交付优先；确实不可用才按实际可用的原MCP共享通道交唯一ZIP，不能把本地sandbox冒充H盘。若旧R8实物迟到，保留原身份和版本，不覆盖当前任务；新冲突只限制其依赖判断。交真实实物、材料使用、全部未完、合法后继及一致的ROLE_RETURN/QUESTION_WORK_RETURN。

普通工程和未来确有必要的Worker签发权仍按原完整任务，不因本轮没有新技术工单而取消。达到完整提交条件才交原accept/M-CLOSE；实际新实质冲突才回decide。没有本轮必须Owner新答才能继续的问题。


来源：daowei2026/observe-iterate@c67bbfa80cac9bfcb55cce20e44697333a292030:runs/BI-01-V2-01/provenance/turns/R0009/FULL_RESPONSE.md::#continuation

## 本轮原文与位置

本次原始要求：`daowei2026/observe-iterate@444179c49ae2f926c287d3bf75b43e1eea44fcfc:runs/BI-01-V2-01/01_当前任务.md::#same-work`
当前生效任务：`daowei2026/observe-iterate@81533abbced55b3af14a428dec9cbf8353fc8286:runs/BI-01-V2-01/01_当前任务.md::full`
当前任务采用依据：`daowei2026/observe-iterate@c67bbfa80cac9bfcb55cce20e44697333a292030:runs/BI-01-V2-01/provenance/turns/R0009/FULL_RESPONSE.md::#adoption`
上一轮实际采用的任务绑定：`daowei2026/observe-iterate@81533abbced55b3af14a428dec9cbf8353fc8286:runs/BI-01-V2-01/01_当前任务.md::L124-L177`
完整工作范围：`daowei2026/observe-iterate@444179c49ae2f926c287d3bf75b43e1eea44fcfc:runs/BI-01-V2-01/01_当前任务.md::full`
最新完整回答：`daowei2026/observe-iterate@c67bbfa80cac9bfcb55cce20e44697333a292030:runs/BI-01-V2-01/provenance/turns/R0009/FULL_RESPONSE.md::full`
原任务内最新接续：`daowei2026/observe-iterate@c67bbfa80cac9bfcb55cce20e44697333a292030:runs/BI-01-V2-01/provenance/turns/R0009/FULL_RESPONSE.md::#continuation`
本次实际证据：`daowei2026/observe-iterate@c67bbfa80cac9bfcb55cce20e44697333a292030:runs/BI-01-V2-01/provenance/turns/R0009/FULL_RESPONSE.md::#plan`
本次实际证据：`daowei2026/observe-iterate@c67bbfa80cac9bfcb55cce20e44697333a292030:runs/BI-01-V2-01/provenance/turns/R0009/FULL_RESPONSE.md::#late-return`
本次实际证据：`daowei2026/observe-iterate@c67bbfa80cac9bfcb55cce20e44697333a292030:runs/BI-01-V2-01/provenance/turns/R0009/FULL_RESPONSE.md::#effort`
本次实际证据：`daowei2026/observe-iterate@87d6e85a79168016607f761e762b7e12eabfef74:runs/BI-01-V2-01/reviews/WORKMAP_INTAKE_CURRENT.json::full`
本次实际证据：`daowei2026/observe-iterate@b3ef5f67f48525086950ddf0123a6d779be14d61:runs/BI-01-V2-01/provenance/turns/R0007/FULL_RESPONSE.md::#time-boundary`
本次实际证据：`daowei2026/observe-iterate@750adeb4007c2fe0f7d44abeb9ab14a9bbe867e7:runs/BI-01-V2-01/provenance/turns/R0006/FULL_RESPONSE.md::#findings`
本次实际证据：`daowei2026/observe-iterate@b9ecbfa4b27f40365ed72f35448116420fb085a6:runs/BI-01-V2-01/artifacts/worker-R0004/readable_views/REQUESTED_51_CURRENT/READING_GUIDE.md::full`
本次实际证据：`daowei2026/observe-iterate@1917f868d61f8de7110b7165ee9125e5b156c4d2:runs/BI-01-V2-01/artifacts/worker-R0004/final/READING_GUIDE.md::full`

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
观察时间：2026-10-18T02:19:05.698385+00:00
有效回交数：8

按既有协议交完整实质回答及ROLE_RETURN/QUESTION_WORK_RETURN，来源、未执行和资格如实保留，不新增控制表，不重抄协调者已存提示。完整任务未完成就保留完整责任及连续后继，局部交付不自设停点。要求GitHub提交时普通快进并fresh回读，最后commit message带turn complete及本轮invocation_id，无invocation时简要标明执行身份；不造空提交。

专业者回交实际实物、必要自检／执行结果、具体限制及完整未完，不代写管理接收、全局预算或主控派发。管理回交已完成的判断、实际处置和可执行后继，不以问题目录代替决定。

没有完整完成时，说明真实停止原因及已经明确的下一步；不得以自设局部目标完成作为结束解释。
