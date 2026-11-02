[BI01-CO-05-R0002-a60d58cf183f]
work_id: BI-01
invocation_id: BI01-CO-05-R0002-a60d58cf183f
assignment_token: 1f902426303447e1a117ecaa1da002e6
role: professional
recipient: chatgpt:BI-01-CO-05:professional
当前阶段：专业任务 BI01
当前职责：依据 Owner 当前做事设想开展业务用例观察与方法反馈

**每次实质业务推进都以有权任务的完整目标及真实未完为范围；当前重点只决定顺序，不得未经授权把整项任务缩成单个 Case、文件或局部修复。工作可根据实际需要往返，不要求每次 R 走完全部内部步骤。** 本次任务明确要求管理接收的跨工作依赖须先取得适用交付与认可；无依赖的合法工作可并行，已签任务内部的普通步骤不另设Gate。原专业续作、Worker工单和技术PASS不能替代实际需要的管理放行。

**本轮专业主体、预期产出和具体方法以配置 goal_ref、实际完整任务和 source_reads 的准确正文为准。** 结果按本次产出要求组织，有价值的额外分析保留；不从历史任务继承未经采用的观察对象、固定数据、工程前置或阶段顺序。

业务事实、CaseFinding、待证假设、设计/方法问题、证据缺失与计算错误分别表达，不因单 Case 推成普遍规律。本次实际数据或方法存在具体疑问时，按来源、位置、字段/时间及影响定向核对并反馈；不把技术缺件解释为市场事实，也不未经授权重新定义观察对象。

本轮确有获授权技术任务时，已有实现可用于核对方法、数据与实际调用，不能以列出读过的文件代替核验，也不照搬未完成的方法。代码示例只用于理解适用做法，不要求所有 BI-01 观察问题使用统一Header、生命周期或固定数量模块；没有该技术任务时不把这些工程事项列为专业观察前置。

发现实际结果、方法或已授权工程有可证实错误时，按当前有权处置处理直接受影响的位置；新任务不默认开展清理、全仓审计或恢复工程。当前重点只决定推进顺序，不成为完成局部即停止的理由。

从完整目标、本次专业工作的真实进展和未决问题出发，连续完成已经明确的全部剩余。围绕本轮业务问题组织实际证据、Case/Source/Method/As-Of、必要挑战、所得认识和下游使用资格；确需技术补证时再连同输入、计算、输出及直接消费者一起处理。已授权的相关修改可以跨多个文件；不按文件数判断完成，也不为了显得完整修改无关文件。

**管理已经完成的材料采用、旧要求撤销、已知问题裁定和全局安排直接使用。推进者不再每轮重判全部历史、维护公共工作量、编写独立接收结论或设计主控派发。**但仍须理解实际业务、读取必要完整专业正文、查真实数据/结果/方法和直接依赖；涉及代码时核实实际实现，不能以管理未点名某个文件为由漏掉真正的使用位置。

BI-01 的专业观察问题、可信结果范围、阶段成果与必要工单来源仍是相应专业产物；减负不取消实质义务。Worker回交真实技术变化，执行Pro消费后向管理交业务结果，管理维护完整推进位置。地图不能代替正确专业方法和事实正文。

**本轮确有授权工程修改时，新增内部函数、Direct 入口、适配器或类型，不等于真实业务结果已经改变。实际使用的公共入口、生产者和消费者必须改接；旧错误路径仍在使用时，不得宣称相关职责已经退出。**

本轮确需 Worker 技术执行、须由本Pro签发工单时，先定向读取[12的Worker工单字段和规范位置](12_管理接收与地图校验.md#worker-order-contract)，按实际原签发身份填写并提交完整工单；其余轮次无须为此读取工具合同。工单派出前由主控运行同一工具的worker-order检查，结果回原签发Pro消费，不能由主控补造签发或据机械PASS认可业务；本次数据入口和真实执行仍须按有权工单及工具约定完成并检验。具体数据疑问按受影响范围核对；工具修改须在所属仓库、实际有权分支和写面内处理，不在观察仓另造平行平台，也不从旧任务继承跨仓权限或强制新建分支要求。未执行如实说明缺件。

方法未实现不能改称待校准；输入与调用未实现不能改称等数据；工程缺件不能改称市场正常 Pending。真实零、合法空、未成熟、输入缺失、未调用和读取失败分别说明。

受到实际容量、工具、真实权限或未定业务问题限制时，交出真实实物、具体限制及完整未完，并明确已知后继；不能以自设小目标达成作为停止理由。完整目标不授予跨仓、抢写或更改受保护业务的权限。

正确专业正文和本轮确有授权的工程细节禁止压缩、概述替换或只留历史链接。已否机制按现行处置连同专属使用位置删除，不换名称、换容器或移入 helper 保留。
**本轮备用回交通道：**优先按原权限把本次实质成果提交 GitHub。如果 Pro 的 GitHub 提交确实不可用，可通过实际可用的 MCP server 文件写入能力，将本轮对应文件、完整回交和必要 Return 打包成唯一 ZIP，写入 MCP server 一侧 `H:\fy\observe-iterate-share`，报告准确 ZIP 路径、关联 invocation 和打包内容；操作 Codex 从对应的 `/dwdhome/fy/observe-iterate-share` 校验收取，再依 [轮次与 ZIP 合同](../../runtime/operations/V2_ROUND_RECORD_CONTRACT.md) 核远端是否已有同轮成果、恢复并合法发布。ZIP 只用于**成果运输**，不自动意味着已提交、已接收或通过 Gate；写入/读取不具备时如实报告具体阻断，不虚称成功。

依本次真实有权 Binding 的专业 mode/source_reads，取得完整目标、产出要求和实际方法正文及其承重输入。专业者按真实问题决定内部研究顺序、必要迭代和所用信息，不让通用 stage 名称变成业务阶段，不让 Worker 自定业务目标。需要旧知识时按准确来源定向复用，不加载另一套任务要求。

## Owner完整目的

# 当前探索阶段的长程任务目标

## 一、当前直接目的

[00_BUSINESS_OBJECTIVE.md](00_BUSINESS_OBJECTIVE.md) 说明最终投资业务目的：利用既有特征对象、属性和多对象关系发现市场现象及候选规律，在后续尚未知时辅助判断哪些品种可能走势更好、机会更大、反向风险更小。

**本次长程任务的直接目的，是通过多轮真实专业实践，检验并迭代 Owner 已提出的初始业务用例形成方式。** 当前首先要看这套方式能否走通，实际能够发现哪些有投资业务意义的现象、候选规律和用例，在哪些地方困难，需要怎样修订；不是简单地从最终投资目的重新选择一项预测能力检验。

Owner 的 [05_OWNER_PROCESS_EXPLANATION.md](05_OWNER_PROCESS_EXPLANATION.md) 是当前优先实践的具体做事设想，包含初版特征、候选背景、沿当时可知信息向前观察、背景内中尺度结构、具体用例形成及反馈。02 只是摘要。05 **不是已验证的规律、固定专业规范或两道 Gate**，但不能因为它尚未验证就不加说明地用另一套研究路线代替。

## 二、期待从真实实践逐渐得到的认识

- **业务内容：**实际市场过程、可定位的贴近转折点/线段/属性/关系、值得研究的现象与初版用例及候选规律；必要时尝试前瞻判断，诚实记录后续支持、反证或无候选。
- **做事过程反馈：**Owner 设想中哪些内容已实际尝试、哪些能够开展、哪些不适用或难以取得有价值结果；区分市场难题、特征信息缺口、工具/数据缺口和业务方法问题。
- **下一轮依据：**根据实践所得的保留、局部调整、待证假说或改变研究方式的具体建议，支持继续实践和 Owner 检查。

这些是理解探索进展的角度，**不是必须串行完成的固定阶段、Gate、文件数量或案例计数**。初版不要求普遍验证或完整场景分类，但也不能长期停留于缺少投资用途的事后描述。一次固定时点的快照或选品种判断，即使合法，也不自动证明整套用例形成方式走通。

## 三、职责与新增业务分析

**Owner** 提供业务目的、初版做事设想和重要反馈/决定。已给出的过程应得到准确恢复和实际使用，不要求 Owner 代填普通工作地图或执行细节。

**Management Pro** 主要在 Owner 已有想法和真实工作全景的基础上，确定当前已成、重要剩余和依赖，组织可执行的专业实践、接收真实成果、判断实践反馈与成本收益，安排下一轮。授权内的执行组织、取数制图、普通可逆具体化可自主决定；不能仅从最终目的自行替换原来要实践的业务研究过程。

**Professional Pro** 按有效任务实际观察特征与市场过程，发现现象、形成和修订候选规律/初版用例，核对实际可知性、进行必要挑战，交真实业务成果与过程反馈。Management 不应在执行前代替 Professional 设计未经授权的新专业路线。

有新内容时，明确区分**Owner 已有认识、实际已核实事实、Professional 新发现/待证假说、Management 新增业务解释或建议、需要 Owner 校准/决定的变化**。重要新增业务分析须呈现给 Owner 检查；实质替换当前研究问题、主要做事过程或业务方向前应取得 Owner 确认。不受影响的合法工作可继续，Owner 不逐项审批普通细节，沉默不算批准。

## 四、边界

当前不是形成正式稳定专业规范、专用 Agent、完整全市场分类或选品种评分器的阶段。当前过程可以根据真实实践修订，不为了维持旧设想无限加厚技术工作；已经走通的数据、工具与图面知识优先复用，先补本次真正缺失的内容。

本文件只规定**当前长程任务的直接目的与职责边界**。最终投资目的仍以 00 为准，Owner 完整过程仍以 05 为准；专业方法、具体案例参数和合法运行/派发机制由当前有效来源和实际任务确定。动态任务与进度只写在当前 Run 正式工作面。

来源：daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/06_EXPLORATION_STAGE_GOAL.md::full

## 本轮当前工作

task_id: BI-01-CO-05-OWNER-PROCESS-PRACTICE-01
status: ISSUED
work_id: BI-01
run_id: BI-01-CO-05
professional_mode: CASE_OBSERVATION
issued_by: chatgpt://global/BI05管理
issued_from_invocation: BI01-CO-05-R0001-ba918c19cb62

# BI-01-CO-05 当前正式专业任务：真实实践 Owner 初版用例形成过程

<a id="task-goal"></a>
## 1. 完整业务目标

最终要利用既有特征对象、属性和多对象关系，在未来尚未知时判断哪些品种可能走势更好、机会更大、反向风险更小，也允许没有足够好候选。本任务的当前直接目的不是单独验证某个评分、固定时点或旧 Case，而是用真实市场材料实践 Owner 的完整初版形成方式，并据此取得两类结果：

1. **业务结果**：可定位的市场过程、现象、候选规律、截至当时的前瞻判断及其更新、反证或合法无候选；
2. **过程结果**：Owner 的“明确特征范围→沿当时可知信息找大尺度背景并检查中尺度结构→在具体背景内形成/修正用例”哪些实际可走、哪里困难、应怎样局部修订。

当前仍是探索阶段，不把本次做法升级为稳定专业规范、评分器或专用 Agent。

<a id="task-plan"></a>
## 2. 当前计划与顺序

1. **核本 Run 可用的真实输入，而非继承旧 Case。** 从当前 aidata 正式入口、已有可复用 run/core/图页/board 或最小新增调用中选择实际适配的品种、时间、K 线频率和大/中尺度参数；记录选择理由和实际身份。2026-11-01 的 rb/hc/i 30m 页面只是一项工具参考，不是默认输入。
2. **建立一张足以观察大尺度过程及其中中尺度结构的主视图。** 优先相对完整时间范围并叠加大、中尺度贴近转折；过密时保留全局定位，再做必要局部放大。不能默默改用 1d 概览或只画一个尺度。
3. **同步取得正式结构化数据。** 需要 AI 读取、比较或计算时，以同一 run/core 的 board/manifest/FILE_INDEX 为准；图与正式切片分别说明，不能互相冒充。
4. **先核证据语义。** 检查贴近转折方向覆盖、上游 zig 可否可靠对应、额外无方向贴近点、actual/confirm/event 及修订含义、正式覆盖和缺失。不能凭名称或最终图补造字段。
5. **沿信息到达顺序实践第一层。** 从必要前史开始，记录关键 T 上各品种已确认对象、当前发展部分和未知状态，观察共同大尺度背景何时才可辨、怎样改变或失效，以及其中是否已有足够中尺度结构。
6. **在值得研究的背景内实践第二层。** 定位具体中尺度对象及关系，提出一个或多个候选规律，对明确后续过程给出候选、排序或无候选，并随新确认和实际后续维持、削弱、撤销或改选。
7. **主动检查自然挑战。** 查看相邻失败片段、复杂错位、替代解释或最接近反例；不只保留最后成功者，不把后来结果倒填早期选择。
8. **把业务认识和过程反馈一起回交。** 明确哪些是 Owner 原设想、正式事实、Professional 新发现/待证假说、建议调整和需要 Owner/管理决定的变化。

两层可以往返，不是固定 Gate。当前重点只决定先后；完成一张图、一个 Case 或一个局部修通后，继续本任务已经明确的全部剩余。

<a id="task-full-scope"></a>
## 3. 本专业批完整范围

本批覆盖一个可由管理真实消费的**完整过程实践批**：

- 实际输入选择、来源/版本/参数、对象语义、正式覆盖和图/数据对应；
- 至少一段连续市场过程中的大尺度背景形成、可辨、变化或不成立；
- 背景内中尺度结构是否足够及其实际对象定位；
- 一个或多个具体用例/候选规律，或有证据的无候选/框架不适配裁定；
- 截至关键 T 的前瞻判断、后续更新、自然挑战和替代解释；
- 对 Owner 完整初版过程逐项实践反馈；
- 真实实物、材料使用记录、限制、完整未完、自查以及一致的两份 Return。

容量不足可分次提交，但同一工作持续承担完整范围。首个可消费实践包会触发管理复看，不等于整个探索阶段或本任务未完自动关闭。

<a id="task-focus"></a>
## 4. 当前集中重点

先消除这个承重不确定性：

> **在不使用未来信息、也不把最终历史图当当时状态的前提下，现有大/中尺度贴近转折对象能否支持沿时间找到一个当时可辨的多品种大尺度背景，并在其中形成有投资用途、可随新信息更新的中尺度用例？**

第一优先是取得真实业务观察，而不是继续循环来源、图形格式或回放工程。若某项历史可知性无法恢复，只限制依赖该语义的主张，并在可合法使用的范围继续；只有直接阻断当前观察的具体技术缺口才进入 Worker。

<a id="task-question-definition"></a>
## 5. 具名专业问题

`CASE-OWNER-PROCESS-PRACTICE-01`：

> 在本 Run 实际可核的特征输入中，沿当时可知信息向前推进时，多品种同向大尺度背景何时能够被辨认、怎样改变或失效？其中是否存在足够的中尺度对象和关系，能形成一个具体候选规律，对明确后续过程给出候选/排序/无候选并随新信息更新？最近的自然挑战和失败片段怎样支持、否定或限制该规律？这一真实实践对 Owner 初版用例形成方式应保留、局部修改还是提出经 Owner 确认的替代建议？

不得把完整历史中最终整齐的线段交集倒选为当时背景；不得以缺少一个完美 Case 为由长期停留在工具准备。

<a id="task-coverage"></a>
## 6. 义务覆盖与消费关系

| 义务 | 本任务形成物 | 消费者 |
|---|---|---|
| 最终投资用途 | 明确目标后续过程、候选/排序/无候选及风险含义 | Management、Owner |
| Owner 过程实践 | 特征范围、第一层、第二层、更新和反馈的真实轨迹 | Management |
| Source/Method/As-Of | 输入身份表、字段语义、关键 T 可知性、未覆盖边界 | Professional、Reviewer |
| 业务证据 | 图、正式切片、对象定位、状态表、必要计算 | Professional、Management |
| 候选规律与挑战 | 现象、待证规律、支持/反证、替代解释、不适用范围 | Management、后续 Professional |
| 方法反馈 | 保留/修改/替代建议及事实依据 | Management、Owner |
| 后继 | 完整未完、下一具名问题或 Owner 决定事项 | Management |

正式字段直接提供、上游可靠对应、图面视觉线索和当前无法核实四种证据状态必须分开。特征尺度、K 线频率、平台节点层级和显示范围必须分开。

<a id="task-input-qualification"></a>
## 7. 真实输入与证据资格

最低记录：

- 实际 workspace/checkout、aidata 与相关实现版本及必要本地差异；
- context、成员实际展开、日历、时间范围、K 线频率、节点/窗口、特征尺度与展开参数；
- run_id、output_root、调用顺序、图页、manifest、FILE_INDEX、正式切片首末有效时间和缺失；
- 贴近转折正式字段、方向覆盖、上游 zig 对应依据、额外无方向点；
- actual、confirm、event/发布/修订和观察时点 T 各自含义；
- 图是否由 Professional 实际打开核对，正式数据是否由程序读取；
- 正式事实、视觉线索、未知和技术故障的区分。

已有 run/core/图页/切片适用就复用，缺什么只补什么。不另建直连数据库的平行取数通道，不从截图或浏览器序列反造正式数据，不擅改共享服务源码、重启服务或全局配置。

<a id="task-process-practice"></a>
## 8. 对 Owner 过程的实际实践要求

### 第一层

从必要前史开始列关键 T：新确认到达了什么、回指何处、另一个品种当时已知状态是什么、共同背景何时才提出、何时变得不确定或结束。共同观察范围与各品种完整大尺度线段分开；阶段错位、短背景和复杂变化本身就是结果。

在提出具体用例前，检查中尺度结构是否足够、是否跨窗、是否只在未来才变得丰富。若反复不足或可知时已无后续空间，应把它识别为框架/尺度问题，而不是凑出第二层故事。

### 第二层

明确前一推进、回落、当前发展部分等实际对象；用截至 T 可知表现提出对指定后续过程的判断。推进和反向负担分别判断；过去表现好不自动继续好。新信息到来后记录维持、削弱、撤销或改选，并对照实际后续。

必要时才打开小尺度，用于解释中尺度内部的反复或反向负担；不得为图层齐全默认叠加。

### 反馈

逐项说明：实际尝试了什么、能否开展、得到什么业务认识；困难属于市场、特征信息、工具/数据还是方法；Owner 原设想应保留、局部修改、待证或实质替换。重要新分析和实质方向变化须显式交管理/Owner，不能在 Professional 内静默采用。

<a id="task-deliverables"></a>
## 9. 必交付实物

在 `runs/BI-01-CO-05/artifacts/professional-<Rxxxx>/` 交付：

1. `REPORT.md`：完整业务报告，含问题、真实输入、证据资格、第一层过程、第二层用例、关键 T 判断与更新、挑战、限制、方法反馈和完整未完；
2. `EVIDENCE_INDEX.md` 或等价机器可读清单：准确定位 run、manifest、数据、图、对象和版本；
3. 一份关键 T 状态表：每个 T 的新增确认、实际位置、已知对象、当前发展、背景认识、判断和不可知项；
4. 必要图面/静态证据或精确平台位置；未实际查看不得声称图面通过；
5. 候选规律/用例卡及自然挑战；若无候选，交证据化的无候选/不适配裁定；
6. 对 Owner 过程的实践反馈与下一专业问题；
7. 若签 Worker，交正式工单、技术结果和 Professional 消费说明；没有真实需要则不造；
8. 材料使用、自查、完整未完、触发观察、`ROLE_RETURN.json` 和 `QUESTION_WORK_RETURN.json`。

<a id="task-completion"></a>
## 10. 语义完成与停止边界

首个过程实践包只有同时满足以下条件才可提交管理接收：

- 实际输入身份、对象语义、参数、时间和覆盖足以支持所交主张；
- 第一层真实走过一个连续过程，说明背景何时可辨、怎样改变/失效，或有证据说明当前输入不能形成；
- 中尺度结构及实际对象被定位，没有把窗口截段冒充完整线段；
- 形成具体候选规律和截至 T 的前瞻判断/无候选，并随新信息更新；
- 检查自然挑战、失败片段或替代解释；
- 明确业务新增认识与 Owner 过程反馈；
- 交付真实实物、限制、自查和全部未完。

图已生成、接口已调用、字段齐全、单个漂亮 Case、结构校验 PASS 或 Worker 技术完成，均不单独构成语义完成。若实际证据表明当前过程无法走通，也可以提交高质量否定结果，但必须精确区分市场无候选、特征不足、工具故障和方法不适配，并给出对 Owner 过程的可操作反馈。

首个包触发管理复看，不自动关闭本任务或探索阶段。未经管理采用，不开始依赖该结果的新业务路线。

<a id="task-budget"></a>
## 11. 条件性投入

Owner 未给固定轮数。当前安排：

- 第一次有效 Professional 调用应取得真实输入与初步时间轨迹；若唯一直接阻断来自现场技术操作，可签 **0—1 个**具名窄 Worker 工单，同时继续不受影响的专业分析；
- 第二次有效 Professional 调用应消费已有技术结果并推进到真实业务观察、候选/无候选和过程反馈；
- 每累计两次有效 Professional 调用且工作仍 ACTIVE，触发管理复看；若仍主要停留在来源、工具、格式或运行准备，管理必须改变实际安排；
- 首个可消费实践包提前形成即立即回管理，不为用满投入继续加厚；
- 当前段不允许连续串联多个 Worker 去追求全面可见性；确需新增技术路线时先触发管理决定；
- 完整探索还需多少轮由真实结果、反例和 Owner 反馈决定，不在无证据时预排。

有效调用从本任务第一次实际 Professional 执行起算；纯运输补交、重复回执或无回答不计。

<a id="task-trigger-result"></a>
## 12. RESULT 触发

当“真实输入资格 + 第一层连续过程 + 中尺度结构判断 + 第二层具体用例/合法否定 + 自然挑战 + Owner 过程反馈”均有实物时，报告 `FIRST_PROCESS_PRACTICE_PACKAGE=SATISFIED` 并回管理接收。原范围内必要收尾可继续，但不得先行启动依赖管理采用的新路线。

<a id="task-trigger-change"></a>
## 13. CHANGE 触发

若承重输入身份或字段语义冲突、现有对象无法支持具名问题、Owner/方法发生实质变化，或 Professional 建议替换主要问题/做事过程/方向，报告 `CORE_INPUT_OR_PROCESS_CHANGE=SATISFIED`，列明受影响主张、仍可继续范围和具体建议，回管理决定。只暂停真正依赖该变化的部分。

<a id="task-trigger-effort"></a>
## 14. EFFORT 触发

每累计两次有效 Professional 调用且工作仍 ACTIVE，报告 `ACTIVE_PROCESS_PRACTICE_EFFORT_REVIEW=SATISFIED`，回管理复看投入收益、真实业务推进和下一段安排。该触发不自动停止 same-work 中不受影响的合法工作。

<a id="task-trigger-effort-rearm"></a>
### 重置条件

管理实际消费本次投入触发、更新继续/改派决定且工作保持 ACTIVE 后，从下一次有效 Professional 调用开始新的两调用段；换 SHA、补运输或重发不清零累计投入。

<a id="task-route-same-work"></a>
## 15. same_work

原具名问题和完整范围仍有效、没有触发需先决定的实质变化时，继续在 `chatgpt:BI-01-CO-05:professional` 完成本任务；不得把最新 remaining 替代完整范围。

<a id="task-route-accept"></a>
## 16. accept

首个可消费实践包提交到 `chatgpt://global/BI05管理`，由管理核业务价值、证据资格、Owner 过程反馈、全部未完和下一轮，不由 Professional 自签接收。

<a id="task-route-decide"></a>
## 17. decide

承重输入/过程实质变化或投入触发提交到 `chatgpt://global/BI05管理`。说明受影响范围和建议；无关合法工作继续，Owner 不逐项审批普通取数、画图和可逆具体化。

<a id="task-route-return-repair"></a>
## 18. return_repair

只有主体成果已交而回交字段/文件确切缺失时，回原 Professional 只补缺件；主体分析未完成则继续 same_work，不用 metadata 冒充完成。

<a id="task-parent"></a>
## 19. 父工作

这是新 Run 的首个专业 Case，`parent.status=NOT_APPLICABLE_NEW_CASE`。旧 CO-01—CO-04 是历史，不是本 Case 的父任务、基线结果或在途来源。

<a id="task-worker-boundary"></a>
## 20. Worker 边界

只有 Professional 确认存在直接阻断当前业务观察的具体技术任务时，才可签发符合现行合同的 `WORKER_ORDER.md`，实际投递到 Owner 指定线程 `01a17dd7-5033-7e63-b7a2-edd90b691c33` 并核 workspace `/dwdhome/fy/cgpterm`。Worker 只做获授权的数据取得、制图、计算或核验，结果回原签发 Professional 消费；不得代判候选规律、方法反馈、管理接收或 Owner 决定。本任务尚未预签任何 Worker。

<a id="question-work-binding"></a>
## 21. QUESTION_WORK_BINDING

```json
{
  "schema": "question-work/v2",
  "kind": "BINDING",
  "work_id": "BI-01",
  "goal_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "b6b344ef0dbd5bc5596c8ec726aad39474254fc4",
    "path": "professional/exploration/06_EXPLORATION_STAGE_GOAL.md",
    "selector": "full"
  },
  "plan_ref": {
    "answer_ref": "#task-plan"
  },
  "full_scope_ref": {
    "answer_ref": "#task-full-scope"
  },
  "batch_result": "完成本 Run 首个真实过程实践批：在一个连续市场过程中走通或诚实裁定不能走通 Owner 初版用例形成方式，形成可消费业务认识与过程反馈，并保留当前探索阶段的全部后续责任。",
  "question_ids": [
    "CASE-OWNER-PROCESS-PRACTICE-01"
  ],
  "professional_mode": "CASE_OBSERVATION",
  "focus_ref": {
    "answer_ref": "#task-focus"
  },
  "coverage_ref": {
    "answer_ref": "#task-coverage"
  },
  "source_reads": [
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "b6b344ef0dbd5bc5596c8ec726aad39474254fc4",
        "path": "professional/README.md",
        "selector": "full"
      },
      "requirement": "MODE_FULL",
      "purpose": "探索期角色、动态工作面和非固定规范边界。",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "b6b344ef0dbd5bc5596c8ec726aad39474254fc4",
        "path": "professional/exploration/06_EXPLORATION_STAGE_GOAL.md",
        "selector": "full"
      },
      "requirement": "MODE_FULL",
      "purpose": "当前探索任务的直接目的、职责与新增分析边界。",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "b6b344ef0dbd5bc5596c8ec726aad39474254fc4",
        "path": "professional/exploration/00_BUSINESS_OBJECTIVE.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "最终投资业务目的与现阶段允许无候选的边界。",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "b6b344ef0dbd5bc5596c8ec726aad39474254fc4",
        "path": "professional/exploration/01_EXISTING_FEATURES_AND_CAPABILITIES.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "既有特征对象、方向、尺度与 actual/confirm 能力边界。",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "b6b344ef0dbd5bc5596c8ec726aad39474254fc4",
        "path": "professional/exploration/02_CURRENT_WORKING_IDEAS.md",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "当前设想摘要；不得替代 05 或当成固定算法。",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "b6b344ef0dbd5bc5596c8ec726aad39474254fc4",
        "path": "professional/exploration/03_TOOLING_AND_DATA_USAGE.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "aidata 图与正式数据的取得、对应、消费和权限边界。",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "b6b344ef0dbd5bc5596c8ec726aad39474254fc4",
        "path": "professional/exploration/04_EXISTING_BUSINESS_REFERENCES.md",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "历史业务与 U2/U3 仅按当前问题定向使用，不继承旧任务。",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "b6b344ef0dbd5bc5596c8ec726aad39474254fc4",
        "path": "professional/exploration/05_OWNER_PROCESS_EXPLANATION.md",
        "selector": "full"
      },
      "requirement": "FOCUS_FULL",
      "purpose": "本轮必须真实实践并反馈的 Owner 完整初版用例形成过程。",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "b6b344ef0dbd5bc5596c8ec726aad39474254fc4",
        "path": "professional/exploration/tooling_examples/2026-11-01_30m_multi_symbol_turn_chart.md",
        "selector": "full"
      },
      "requirement": "PROVENANCE_TRIGGER",
      "purpose": "特定环境下已走通的绘图工具参考；仅在实际输入适配时低成本复用。",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "b6b344ef0dbd5bc5596c8ec726aad39474254fc4",
        "path": "runtime/operations/CASE_OBSERVATION_RUN_GUIDE.md",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "当前 Run 的管理/专业接线、可选 Reader 与不继承旧 Run 边界。",
      "reuse_evidence": null
    },
    {
      "source": {
        "repo": "daowei2026/observe-iterate",
        "commit": "85febea03631aef7757412c20533ff536dbf51d9",
        "path": "runs/BI-01-CO-05/OWNER_START.md",
        "selector": "full"
      },
      "requirement": "BOUNDARY",
      "purpose": "本 Run 的真实 Owner GO、分支、Worker 线程和首次观察要求。",
      "reuse_evidence": null
    }
  ],
  "deliverables_ref": {
    "answer_ref": "#task-deliverables"
  },
  "completion_ref": {
    "answer_ref": "#task-completion"
  },
  "budget_ref": {
    "answer_ref": "#task-budget"
  },
  "routes": {
    "same_work": {
      "recipient_role": "professional",
      "recipient_ref": "chatgpt:BI-01-CO-05:professional",
      "instructions_ref": {
        "answer_ref": "#task-route-same-work"
      }
    },
    "accept": {
      "recipient_role": "management",
      "recipient_ref": "chatgpt://global/BI05管理",
      "instructions_ref": {
        "answer_ref": "#task-route-accept"
      }
    },
    "decide": {
      "recipient_role": "management",
      "recipient_ref": "chatgpt://global/BI05管理",
      "instructions_ref": {
        "answer_ref": "#task-route-decide"
      }
    },
    "return_repair": {
      "recipient_role": "professional",
      "recipient_ref": "chatgpt:BI-01-CO-05:professional",
      "instructions_ref": {
        "answer_ref": "#task-route-return-repair"
      }
    }
  },
  "triggers": [
    {
      "trigger_id": "FIRST_PROCESS_PRACTICE_PACKAGE",
      "kind": "RESULT",
      "condition_ref": {
        "answer_ref": "#task-trigger-result"
      },
      "signal_key": "first_process_practice_package",
      "route": {
        "recipient_role": "management",
        "recipient_ref": "chatgpt://global/BI05管理",
        "instructions_ref": {
          "answer_ref": "#task-route-accept"
        }
      },
      "blocking": false,
      "effort_limit": null,
      "obligation_id": "initial-process-practice-management-review",
      "cycle_id": "practice-1",
      "rearm_ref": null,
      "repeat": "ONCE"
    },
    {
      "trigger_id": "CORE_INPUT_OR_PROCESS_CHANGE",
      "kind": "CHANGE",
      "condition_ref": {
        "answer_ref": "#task-trigger-change"
      },
      "signal_key": "core_input_or_process_change",
      "route": {
        "recipient_role": "management",
        "recipient_ref": "chatgpt://global/BI05管理",
        "instructions_ref": {
          "answer_ref": "#task-route-decide"
        }
      },
      "blocking": false,
      "effort_limit": null,
      "obligation_id": "core-input-or-process-management-decision",
      "cycle_id": "practice-1",
      "rearm_ref": null,
      "repeat": "ONCE"
    },
    {
      "trigger_id": "ACTIVE_PROCESS_PRACTICE_EFFORT_REVIEW",
      "kind": "EFFORT",
      "condition_ref": {
        "answer_ref": "#task-trigger-effort"
      },
      "signal_key": "active_process_practice_effort_review",
      "route": {
        "recipient_role": "management",
        "recipient_ref": "chatgpt://global/BI05管理",
        "instructions_ref": {
          "answer_ref": "#task-route-decide"
        }
      },
      "blocking": false,
      "effort_limit": {
        "unit": "EFFECTIVE_CALLS",
        "limit": 2,
        "count_from_ref": {
          "answer_ref": "#task-budget"
        }
      },
      "obligation_id": "active-process-practice-effort-review",
      "cycle_id": "practice-segment-1",
      "rearm_ref": {
        "answer_ref": "#task-trigger-effort-rearm"
      },
      "repeat": "WHILE_WORK_ACTIVE"
    }
  ],
  "explicit_no_trigger_reason_ref": null,
  "parent": {
    "status": "NOT_APPLICABLE_NEW_CASE",
    "ref": null,
    "reason_ref": {
      "answer_ref": "#task-parent"
    }
  },
  "question_definitions": [
    {
      "question_id": "CASE-OWNER-PROCESS-PRACTICE-01",
      "definition_ref": {
        "answer_ref": "#task-question-definition"
      },
      "authority_ref": {
        "repo": "daowei2026/observe-iterate",
        "commit": "85febea03631aef7757412c20533ff536dbf51d9",
        "path": "runs/BI-01-CO-05/OWNER_START.md",
        "selector": "full"
      },
      "parent_question_id": null
    }
  ]
}
```

来源：daowei2026/observe-iterate@a6a8acf7fa65665218d0f2163598d434fb921b24:runs/BI-01-CO-05/01_当前任务.md::full

## 本轮原文与位置

本次原始要求：`daowei2026/observe-iterate@a6a8acf7fa65665218d0f2163598d434fb921b24:runs/BI-01-CO-05/01_当前任务.md::#task-route-same-work`
当前生效任务：`daowei2026/observe-iterate@a6a8acf7fa65665218d0f2163598d434fb921b24:runs/BI-01-CO-05/01_当前任务.md::full`
当前任务采用依据：`daowei2026/observe-iterate@0a2347e93ef66fcc1165ed5ac31960b59813f6c8:runs/BI-01-CO-05/reviews/management-R0001/DECISION.md::#current-task-decision`
上一轮实际采用的任务绑定：`daowei2026/observe-iterate@a6a8acf7fa65665218d0f2163598d434fb921b24:runs/BI-01-CO-05/01_当前任务.md::#question-work-binding`
完整工作范围：`daowei2026/observe-iterate@a6a8acf7fa65665218d0f2163598d434fb921b24:runs/BI-01-CO-05/01_当前任务.md::#task-full-scope`
本次实际证据：`daowei2026/observe-iterate@204e81c2c3199341a70417eeb4894a0444a4d3e7:runs/BI-01-CO-05/README.md::full`
本次实际证据：`daowei2026/observe-iterate@204e81c2c3199341a70417eeb4894a0444a4d3e7:runs/BI-01-CO-05/00_长程推进地图.md::full`
本次实际证据：`daowei2026/observe-iterate@204e81c2c3199341a70417eeb4894a0444a4d3e7:runs/BI-01-CO-05/reviews/WORKMAP_INTAKE_CURRENT.json::full`

## 本次直接读取的上下文

- MODE_FULL：`daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/README.md::full`
  用途与边界：探索期角色、动态工作面和非固定规范边界。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/06_EXPLORATION_STAGE_GOAL.md::full`
  用途与边界：当前探索任务的直接目的、职责与新增分析边界。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/00_BUSINESS_OBJECTIVE.md::full`
  用途与边界：最终投资业务目的与现阶段允许无候选的边界。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/01_EXISTING_FEATURES_AND_CAPABILITIES.md::full`
  用途与边界：既有特征对象、方向、尺度与 actual/confirm 能力边界。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/02_CURRENT_WORKING_IDEAS.md::full`
  用途与边界：当前设想摘要；不得替代 05 或当成固定算法。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/03_TOOLING_AND_DATA_USAGE.md::full`
  用途与边界：aidata 图与正式数据的取得、对应、消费和权限边界。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/04_EXISTING_BUSINESS_REFERENCES.md::full`
  用途与边界：历史业务与 U2/U3 仅按当前问题定向使用，不继承旧任务。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/05_OWNER_PROCESS_EXPLANATION.md::full`
  用途与边界：本轮必须真实实践并反馈的 Owner 完整初版用例形成过程。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- PROVENANCE_TRIGGER：`daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:professional/exploration/tooling_examples/2026-11-01_30m_multi_symbol_turn_chart.md::full`
  用途与边界：特定环境下已走通的绘图工具参考；仅在实际输入适配时低成本复用。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@b6b344ef0dbd5bc5596c8ec726aad39474254fc4:runtime/operations/CASE_OBSERVATION_RUN_GUIDE.md::full`
  用途与边界：当前 Run 的管理/专业接线、可选 Reader 与不继承旧 Run 边界。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@85febea03631aef7757412c20533ff536dbf51d9:runs/BI-01-CO-05/OWNER_START.md::full`
  用途与边界：本 Run 的真实 Owner GO、分支、Worker 线程和首次观察要求。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

读取Owner完整要求、生效完整任务和输入输出地图，不能用最新remaining替全部责任。按source_reads取得准确正文用于判断，已读未变且可恢复者复用；不递归扫无关历史，不用索引/hash/旧回执代正文。

旧包中已被Owner否定的多余任务，必须由原有权责任者从当前正文、任务、前置、接收和后继删除；只为其存在的辅助代码与检查交原实现者删除。禁止继续完善、改名或列为暂缓/未来优化。不能只在顶部写新原则却继续采用相反正文。真实业务方法、时间、身份、状态、正式输出与消费者保留，技术机制替换回正常平台。正确正文禁止任何压缩或摘要替换。历史提交和实际记录不倒改；历史可追溯不授后续派发。通用材料维护不自动取得用例任务写权。

当前执行材料由管理和有权任务责任者明确采用。推进者取得实际需要的正确正文，不能用管理概述替代业务细节；也不要求每轮重读全部历史和已撤完整任务。

发现新的实质冲突时，给出准确位置与受影响结论，按原责任处理。来源不足只限制真正依赖的判断，不用旧快照补造事实，也不冻结无关工作。

方法版本、业务合同版本、源码版本和运行数据分别保持准确，不随一次方法更新全部追 latest。

运行事实（来自现有记录）：
观察时间：2026-11-02T05:13:16.057879+00:00
有效回交数：0

按既有协议把完整实质报告及符合Schema的ROLE_RETURN/QUESTION_WORK_RETURN交付GitHub，来源、未执行和资格如实保留；GitHub提交与远端校验成功后手机只回准确定位，不贴长报告或两份JSON。无法交付时按原备用渠道提供真实完整回交，不新增控制表，不重抄协调者已存提示。完整任务未完成就保留完整责任及连续后继，局部交付不自设停点。要求GitHub提交时普通快进并fresh回读，最后commit message带turn complete及本轮invocation_id，无invocation时简要标明执行身份；不造空提交。

专业者回交实际实物、必要自检／执行结果、具体限制及完整未完，不代写管理接收、全局预算或主控派发。管理回交已完成的判断、实际处置和可执行后继，不以问题目录代替决定。

没有完整完成时，说明真实停止原因及已经明确的下一步；不得以自设局部目标完成作为结束解释。
