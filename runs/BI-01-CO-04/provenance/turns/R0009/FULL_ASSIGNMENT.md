[BI01-CO-04-R0009-PROFESSIONAL-QUERY-ASOF-8d6fcf14]
work_id: BI-01
invocation_id: BI01-CO-04-R0009-PROFESSIONAL-QUERY-ASOF-8d6fcf14
assignment_token: 625dea7ad3106c7bb13e2d923ed4e67f2d3713fcbf25f5a4
role: professional
recipient: chatgpt:BI-01-CO-04:professional
当前阶段：专业任务 BI01
当前职责：基于既有特征的业务用例探索（由管理按轮次安排具体工作）

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

# 业务目标与当前探索边界

基于既有特征表达的对象、衍生对象、属性及多对象关系，发现市场运动中的现象与候选规律，并利用它们在后续尚未知时判断哪些品种可能走势更好、机会更大、风险更小；也允许当前没有足够好的候选。当前从偏单边品种选择开始。

初始用例主要以大、中、小尺度贴近转折点、由其形成的线段及这些对象实际提供的属性和关系表达。行情用于理解与核对特征所表达的过程，不以自由价格故事取代特征对象。不得把尚未交付或尚未实现的信息当成现有能力。

当前不是建立稳定专业方法或专用Agent的阶段，而是通过多轮实践摸索怎样形成有业务价值的初始用例。Management Pro理解Owner整体意图、已有材料和实践结果，安排下一项专业工作；Professional Pro执行并反馈；Management Pro更新认识并安排下一轮。

业务价值优先于工具、图形工程、复杂网络结构或叙事形式。初版不要求复杂、穷尽反例或证明普遍有效，但不能只有事后描述，必须尝试把当时可知信息与尚未知的后续判断连接起来。只有多轮实践证明稳定有效后，才考虑固化规范或专用Agent。

来源：daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/00_BUSINESS_OBJECTIVE.md::full

## 本轮当前工作

task_id: BI-01-CO-04-CASE-INITIAL-ASOF
status: ISSUED
work_id: BI-01
run_id: BI-01-CO-04
professional_mode: CASE_OBSERVATION
issued_by: chatgpt:BI-01-CO-04:management
issued_from_invocation: BI-01-CO-04-R0001-MSTART-d4227cb476

# BI-01-CO-04 当前正式专业任务：首个可消费的 as-of 多品种判断循环

<a id="task-goal"></a>
## 1. 完整业务目标

不是为了证明某个既有图、参数或“二层观察”正确，而是利用已经存在的大／中／小尺度贴近点和相关对象，逐步发现能够支持前瞻选择判断的市场现象、关系、候选模式与失败条件。每次判断必须回答：**在当时真实可知的信息下，哪些品种更值得继续观察，目标是哪一种后续市场过程；若没有可靠候选，应明确给出无候选。**

本任务是新 Run 的第一项专业实践。它要取得一个可以由管理真正消费的完整循环，并为后续多轮探索提供可修正的认识；不是把当前设想升级为固定专业方法，也不是完成一个 Case 就宣告整个探索项目结束。

<a id="task-plan"></a>
## 2. 当前计划与顺序

1. **先核真实承重输入。** 取得本 Run 实际可读取的正式特征交付、manifest／board 数据、行情窗口、run 身份、参数与时间字段。2026-11-01 的 rb／hc／i 30m 图面实践只是一项低成本入口候选；只有其当前字节、run、对象语义和截至 T 的可知性均可核，才可作为本任务输入。
2. **再选一个有业务价值的比较窗口。** 优先寻找至少两个品种处于可比较的大尺度同方向背景、而中尺度状态存在可解释差异的位置。若真实数据不支持，不得为了凑例而硬选。
3. **严格按 as-of T 重建。** 只使用在 T 时已经确认或实际可知的对象；分别记录实际转折时间、确认／发布可知时间、方向、尺度、来源和状态。最终历史图不得倒填判断时点。
4. **形成明确前瞻判断。** 对给定后续过程给出候选、排序或无候选，并说明大尺度背景、中尺度差异、小尺度局部信息各自承担什么证据角色。
5. **沿同一材料继续到最近的自然挑战。** 检查后续确认点、反向对象、失败候选或同逻辑不成立的相邻区间；区分支持、反证、等待和不可判定，不只挑成功例。
6. **把观察反馈回下一轮。** 说明本次是否形成独立业务认识，哪些只是提高可追溯性，当前设想哪些保留、修改或暂不使用，以及下一项最有价值的专业问题。

<a id="task-full-scope"></a>
## 3. 本段完整范围

本段覆盖首个**完整专业探索批**，而非一张图或一个局部节点：

- 正式输入、来源身份、参数、对象语义和时间资格；
- 一个主 as-of 多品种比较路径；
- 同材料中最近的自然挑战、失败候选或合法无候选区间；
- 明确的前瞻目标、支持／反证、替代解释和限制；
- 对当前工作设想的实际反馈；
- 真实实物、材料使用记录、自查、全部未完、触发观察及一致的 `ROLE_RETURN`／`QUESTION_WORK_RETURN`。

容量不足时可以分次提交实物，但同一工作继续承担上述完整范围。当前重点只决定顺序，不允许以单 Case、单图、单参数解释或工具修通作为停止点。

<a id="task-focus"></a>
## 4. 当前集中重点

当前集中消除的高后果不确定性是：**既有特征能否在不使用未来信息的前提下，支持一次诚实的多品种前瞻比较；中尺度差异是否提供了超出“大方向一致”的独立选择信息。**

首选低成本入口是已完成的 rb／hc／i 30m 三尺度图面实践，但它尚未取得本 Run 的数据资格。若核验后不适合，专业执行者应选择最近、最小且真正适配的正式输入，不得为了延续旧图而牺牲业务问题。

<a id="task-question-definition"></a>
## 5. 具名专业问题

`CASE-FIRST-ASOF-CROSS-SYMBOL-SELECTION`：

> 在本 Run 可核的正式输入中，是否存在一个截至 T 至少两个品种具有可比较大尺度背景、而中尺度已确认状态存在差异的窗口？只用 T 时可知证据，能否对明确的后续市场过程形成候选／排序／无候选判断；后来的确认点、反向对象或失败区间如何支持、否定或限制该判断？本次结果对“用大尺度找背景、用中尺度找差异”的当前设想提出什么保留、修订或反例？

结束条件不是“有图”，而是该问题得到可追溯、可挑战、可继续使用的回答；若输入不成立，也要精确交付缺口、受影响结论和最小恢复条件。

<a id="task-coverage"></a>
## 6. 义务覆盖与相邻关系

| 义务 | 本任务中的形成物 | 消费关系 |
|---|---|---|
| 业务价值与问题 | 具名前瞻比较问题、目标过程、候选或无候选 | 管理判断是否值得继续与如何改下一轮 |
| Source／Method／As-Of 资格 | 输入身份表、字段语义、参数、实际时间与确认时间 | 只放行达到具体观察所需资格的范围 |
| 真实结果 | 图／表／节点状态、必要复算、可读证据链 | 专业观察与独立复核，不以文件存在代替 |
| 业务观察与挑战 | 主判断、自然挑战、失败候选、替代解释 | 管理接收 G4 范围及下一问题 |
| Owner 可读材料 | 关键图、简洁过程说明、争议和限制 | 达到有用首版后进入 Owner 反馈；本轮不冒称 Owner 已批准 |
| 下一轮安排输入 | 保留／修订／停止的工作设想及最有价值后续 | 管理 Pro 决定，不由执行者改全局地图 |

正式字段、可靠上游映射、图上视觉线索和未知状态必须分开；贴近点不自动等于有方向 zig 点。特征尺度、K 线频率和平台图节点层级不得混为一谈。

<a id="task-input-qualification"></a>
## 7. 输入资格与失败处理

最低需要记录：

- 品种、行情来源、时间范围、K 线频率；
- 特征交付或 manifest 的准确身份、run／配置／参数；
- 大／中／小对象的真实字段与方向语义；
- 实际转折时间、确认／发布可知时间及 as-of T 截断规则；
- 缺失、计算故障和真实市场“无信号／无候选”的区别。

若直接输入缺失，专业执行者先说明究竟缺哪一项、阻断哪个判断。确需补取数据、制图或有限核验时，执行 Pro 可依据 Owner 已授权分工签发具名 Worker 技术工单，使用现有 Worker 线程 `01a17dd7-5033-7e63-b7a2-edd90b691c33`；工单必须限定技术目标、输入、写面、返回位置和 `return_to`，并按现行 `worker-order` 合同提交。未确认需要前不预签 Worker，也不得让 Worker 代判业务或管理 Gate。无关且可继续的专业工作不因局部输入缺口全线冻结。

<a id="task-deliverables"></a>
## 8. 必交付实物

专业执行者在本 Run 的 `artifacts/` 工作面交付：

1. 一份完整业务报告，含问题、输入资格、as-of 重建、主判断、自然挑战、替代解释、限制、方法反馈和下一专业问题；
2. 可追溯输入／证据清单，准确定位实际数据、manifest、配置、图或表；
3. 必要图面和节点读数；图不可访问时提供真实静态证据或精确平台位置，不凭文字声称已看；
4. 若签发 Worker，交真实工单及 Worker 回交的消费说明；没有需要则不造工单；
5. 材料使用记录、完整未完和触发观察；
6. 符合当前 schema、身份和本 Binding 的 `ROLE_RETURN.json` 与 `QUESTION_WORK_RETURN.json`。

报告必须明确哪些结论是正式证据支持、哪些仅视觉线索、哪些未知；不得把组织和可追溯性改进冒充独立投资知识增量。

<a id="task-completion"></a>
## 9. 语义完成条件

本专业批只有同时满足以下条件才可提交管理接收：

- 本 Run 实际输入身份、方法、参数和时间语义足以支持所交判断；
- 至少形成一个截至 T 的明确前瞻比较循环，或有充分证据裁定本批只能给出无候选／输入不合格；
- 检查最近的自然挑战、失败候选或反例，未用最终历史结果倒填；
- 说明大／中／小尺度各自的证据作用和不能推出的内容；
- 交支持、反证、替代解释、限制、实际新增认识或无增量判断；
- 交真实实物、自查、全部未完和一致回交。

工具能运行、图可读、字段齐全、单一成功例或结构校验通过，均不单独构成完成。完整探索项目仍需后续多轮实践、必要独立审查、管理接收及 Owner 反馈。

<a id="task-budget"></a>
## 10. 条件性投入与复看

Owner 没有给固定轮数。当前预测：

- 首个专业批优先在 **1—2 次有效 Professional 调用**内取得输入资格和一个可消费的主循环；
- 只有出现真实技术缺口时才增加 **0—1 个定向 Worker 工单**；
- 若两次有效调用仍只有工具／来源循环、没有业务观察，触发管理复看并改变实际安排；
- 若首个循环提前形成，立即回管理消费，不为了用满预算继续加厚；
- 完整探索预计仍需若干独立迭代，具体轮数由真实结果、反例和 Owner 反馈决定，不在当前无证据预排。

有效调用从本任务第一次真实 Professional 执行起累计；重复回执、无回答或纯运输补交不计。`WHILE_WORK_ACTIVE` 的两次调用间隔持续生效，累计投入不因换轮清零。

<a id="task-trigger-result"></a>
## 11. RESULT 触发

当“输入资格 + 一个 as-of 前瞻比较循环 + 最近自然挑战／合法无候选 + 方法反馈”均有真实实物时，报告 `FIRST_USABLE_ASOF_LOOP=SATISFIED`，回管理执行 M-REASSESS。该触发不禁止专业者在原范围内整理已授权收尾，但任何依赖管理接收的新路线不得先行。

<a id="task-trigger-change"></a>
## 12. CHANGE 触发

若发现承重输入身份不成立、方向／确认时间语义与材料冲突、候选问题根本不适配现有对象，或 Owner／方法发生实质变化，报告 `MATERIAL_INPUT_OR_METHOD_CHANGE=SATISFIED` 并准确说明受影响结论与可继续范围。只暂停依赖该变化的动作；无关合法工作继续。

<a id="task-trigger-effort"></a>
## 13. EFFORT 触发

每累计两次有效 Professional 调用且完整工作仍 ACTIVE，报告 `ACTIVE_WORK_EFFORT_REVIEW=SATISFIED`，回管理复看投入收益、主体推进和下一段安排。该触发不强制通过、停止或缩小完整范围。

<a id="task-route-same-work"></a>
## 14. same_work 路线

在输入和授权仍成立时，继续本任务全部范围；采用最新合法 `continuation_ref`，不重做已证实内容，不以单 Case 或局部修复停下。交真实业务增量、全部未完、触发观察和两份一致回交。

<a id="task-route-accept"></a>
## 15. accept 路线

将完整专业报告、实物、两份 Return 和准确 Binding 交 `chatgpt:BI-01-CO-04:management`。管理复核业务问题、输入资格、真实结果、反例与增量，明确可消费范围、限制和下一责任；技术 PASS 不自动放行。

<a id="task-route-decide"></a>
## 16. decide 路线

只把具名的重要变化、依赖冲突、超出本任务授权的专业取舍或到期投入复看交 `chatgpt:BI-01-CO-04:management`。已明确的普通专业判断和获授权技术补齐由原执行者完成，不把 Owner 变成逐步按钮。

<a id="task-route-return-repair"></a>
## 17. return_repair 路线

仅补确切缺失的 Return 字段、引用或交付一致性；保留原实质和资格。若缺的是业务分析或承诺实物，继续原专业工作，不用 metadata 修成完成。

<a id="task-parent"></a>
## 18. Parent 裁定

这是 Owner GO 后本 Run 首次由管理签发的专业任务，当前没有已接受的 parent professional binding；状态为 `NOT_APPLICABLE_NEW_CASE`。旧 CO 运行、历史 U2／U3、旧 I2—I6、历史图和旧 Gate 仅可作准确来源事实，不取得本任务的 parent 权力。

<a id="task-handoff"></a>
## 19. 实际派发与接续

本文件表示管理已签发任务，不表示手机已发送或 Professional 已开始。主控须先按现行 Workmap Intake 完成独立 Reader 与 dispatch preflight，随后使用本文件全文作为 `current_task_ref`、管理 R0001 决定作为 `task_adoption_ref`，按 GitHub 完整派发／手机短指引流程实际发送。发送、执行、专业提交、独立审查和管理接收分别记录。

<a id="question-work-binding"></a>
## 20. QUESTION_WORK_BINDING

```json
{
  "schema": "question-work/v2",
  "kind": "BINDING",
  "work_id": "BI-01",
  "goal_ref": {
    "repo": "daowei2026/observe-iterate",
    "commit": "b6ccf766dac055a793e75f76b77a73f4cfc74064",
    "path": "professional/exploration/00_BUSINESS_OBJECTIVE.md",
    "selector": "full"
  },
  "plan_ref": {"answer_ref": "#task-plan"},
  "full_scope_ref": {"answer_ref": "#task-full-scope"},
  "batch_result": "形成本Run首个可消费的前瞻多品种比较循环：先核真实输入与截至T可知状态，再给出明确候选/无候选判断、后续支持或反证、合法替代解释和对下一轮方法的具体反馈；同一材料允许并要求继续到最近的自然挑战或失败候选，而不是交一张图即停。",
  "question_ids": ["CASE-FIRST-ASOF-CROSS-SYMBOL-SELECTION"],
  "professional_mode": "CASE_OBSERVATION",
  "focus_ref": {"answer_ref": "#task-focus"},
  "coverage_ref": {"answer_ref": "#task-coverage"},
  "source_reads": [
    {"source":{"repo":"daowei2026/observe-iterate","commit":"b6ccf766dac055a793e75f76b77a73f4cfc74064","path":"professional/README.md","selector":"full"},"requirement":"BOUNDARY","purpose":"确认探索项目不是定型规范，动态任务只由本Run正式工作面授权。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"b6ccf766dac055a793e75f76b77a73f4cfc74064","path":"professional/exploration/00_BUSINESS_OBJECTIVE.md","selector":"full"},"requirement":"MODE_FULL","purpose":"恢复完整业务目标、阶段定位及允许没有好候选的结果。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"b6ccf766dac055a793e75f76b77a73f4cfc74064","path":"professional/exploration/01_EXISTING_FEATURES_AND_CAPABILITIES.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"取得大中小贴近点、方向/确认状态和既有特征能力的准确边界。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"b6ccf766dac055a793e75f76b77a73f4cfc74064","path":"professional/exploration/02_CURRENT_WORKING_IDEAS.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"取得待实践修正的候选观察设想；不得把它当固定流程。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"b6ccf766dac055a793e75f76b77a73f4cfc74064","path":"professional/exploration/03_TOOLING_AND_DATA_USAGE.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"取得正式交付、aidata、图面、时间语义、数据与平台边界。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"b6ccf766dac055a793e75f76b77a73f4cfc74064","path":"professional/exploration/04_EXISTING_BUSINESS_REFERENCES.md","selector":"full"},"requirement":"BOUNDARY","purpose":"只在本轮问题确需时定向使用历史实物；不继承旧Gate或旧结论。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"b6ccf766dac055a793e75f76b77a73f4cfc74064","path":"professional/exploration/05_OWNER_PROCESS_EXPLANATION.md","selector":"full"},"requirement":"MODE_FULL","purpose":"完整理解Owner的实际观察过程、两层候选思路、复杂情况和反馈方式。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"b6ccf766dac055a793e75f76b77a73f4cfc74064","path":"professional/exploration/tooling_examples/2026-11-01_30m_multi_symbol_turn_chart.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"作为可核验的低成本起点候选；其品种、频率、参数和run身份不自动成为本Run正式输入。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"b6ccf766dac055a793e75f76b77a73f4cfc74064","path":"runtime/operations/CASE_OBSERVATION_RUN_GUIDE.md","selector":"full"},"requirement":"BOUNDARY","purpose":"遵守新Run、真实任务、Worker签发和动态工作面边界。","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"e28be2f92522064c146ffe28166350b39a7ae7ca","path":"runs/BI-01-CO-04/OWNER_START.md","selector":"full"},"requirement":"BOUNDARY","purpose":"取得本Run Owner GO、分工、工作面和现有Worker线程授权边界。","reuse_evidence":null}
  ],
  "deliverables_ref": {"answer_ref": "#task-deliverables"},
  "completion_ref": {"answer_ref": "#task-completion"},
  "budget_ref": {"answer_ref": "#task-budget"},
  "routes": {
    "same_work": {"recipient_role":"professional","recipient_ref":"chatgpt:BI-01-CO-04:professional","instructions_ref":{"answer_ref":"#task-route-same-work"}},
    "accept": {"recipient_role":"management","recipient_ref":"chatgpt:BI-01-CO-04:management","instructions_ref":{"answer_ref":"#task-route-accept"}},
    "decide": {"recipient_role":"management","recipient_ref":"chatgpt:BI-01-CO-04:management","instructions_ref":{"answer_ref":"#task-route-decide"}},
    "return_repair": {"recipient_role":"professional","recipient_ref":"chatgpt:BI-01-CO-04:professional","instructions_ref":{"answer_ref":"#task-route-return-repair"}}
  },
  "triggers": [
    {"trigger_id":"FIRST_USABLE_ASOF_LOOP","kind":"RESULT","condition_ref":{"answer_ref":"#task-trigger-result"},"signal_key":"first_usable_asof_loop","route":{"recipient_role":"management","recipient_ref":"chatgpt:BI-01-CO-04:management","instructions_ref":{"answer_ref":"#task-route-accept"}},"blocking":false,"effort_limit":null,"obligation_id":"initial-professional-result-review","cycle_id":"initial-1","rearm_ref":null,"repeat":"ONCE"},
    {"trigger_id":"MATERIAL_INPUT_OR_METHOD_CHANGE","kind":"CHANGE","condition_ref":{"answer_ref":"#task-trigger-change"},"signal_key":"material_input_or_method_change","route":{"recipient_role":"management","recipient_ref":"chatgpt:BI-01-CO-04:management","instructions_ref":{"answer_ref":"#task-route-decide"}},"blocking":false,"effort_limit":null,"obligation_id":"material-change-decision","cycle_id":"initial-1","rearm_ref":null,"repeat":"ONCE"},
    {"trigger_id":"ACTIVE_WORK_EFFORT_REVIEW","kind":"EFFORT","condition_ref":{"answer_ref":"#task-trigger-effort"},"signal_key":"active_work_effort_review","route":{"recipient_role":"management","recipient_ref":"chatgpt:BI-01-CO-04:management","instructions_ref":{"answer_ref":"#task-route-decide"}},"blocking":false,"effort_limit":{"unit":"EFFECTIVE_CALLS","limit":2,"count_from_ref":{"answer_ref":"#task-budget"}},"obligation_id":"active-professional-effort-review","cycle_id":"segment-1","rearm_ref":null,"repeat":"WHILE_WORK_ACTIVE"}
  ],
  "explicit_no_trigger_reason_ref": null,
  "parent": {"status":"NOT_APPLICABLE_NEW_CASE","ref":null,"reason_ref":{"answer_ref":"#task-parent"}},
  "question_definitions": [
    {"question_id":"CASE-FIRST-ASOF-CROSS-SYMBOL-SELECTION","definition_ref":{"answer_ref":"#task-question-definition"},"authority_ref":{"repo":"daowei2026/observe-iterate","commit":"e28be2f92522064c146ffe28166350b39a7ae7ca","path":"runs/BI-01-CO-04/OWNER_START.md","selector":"full"},"parent_question_id":null}
  ]
}
```

来源：daowei2026/observe-iterate@d5758f119c82b07236b1d0041c5febcbb1b12273:runs/BI-01-CO-04/01_当前任务.md::full

## 本轮原文与位置

本次原始要求：`daowei2026/observe-iterate@d5758f119c82b07236b1d0041c5febcbb1b12273:runs/BI-01-CO-04/01_当前任务.md::#task-route-same-work`
当前生效任务：`daowei2026/observe-iterate@d5758f119c82b07236b1d0041c5febcbb1b12273:runs/BI-01-CO-04/01_当前任务.md::full`
当前任务采用依据：`daowei2026/observe-iterate@c286238462c07f15d9ebfe3cac06edc6a2da29d4:runs/BI-01-CO-04/reviews/management-R0008/DECISION.md::#professional-release`
上一轮实际采用的任务绑定：`daowei2026/observe-iterate@d5758f119c82b07236b1d0041c5febcbb1b12273:runs/BI-01-CO-04/01_当前任务.md::#question-work-binding`
完整工作范围：`daowei2026/observe-iterate@d5758f119c82b07236b1d0041c5febcbb1b12273:runs/BI-01-CO-04/01_当前任务.md::#task-full-scope`
最新完整回答：`daowei2026/observe-iterate@28a915f9b6a7bb8f69651a7954028b02c3244684:runs/BI-01-CO-04/artifacts/R0005/REPORT.md::full`
最新结构化问题回交：`daowei2026/observe-iterate@d5d0cbf9dfcc49a0711b76f9190e36f576c43fb1:runs/BI-01-CO-04/provenance/turns/R0005/QUESTION_WORK_RETURN.json::full`
最新角色回交：`daowei2026/observe-iterate@b2b31f4bb1d99d18178bfa49890e28cf57c54890:runs/BI-01-CO-04/provenance/turns/R0005/ROLE_RETURN.json::full`
被当前任务替代的旧续作（仅历史）：`daowei2026/observe-iterate@28a915f9b6a7bb8f69651a7954028b02c3244684:runs/BI-01-CO-04/artifacts/R0005/REPORT.md::#continuation`
本次实际证据：`daowei2026/observe-iterate@216a83a9594e8ce65681f51c48ca10a607d5aa84:runs/BI-01-CO-04/reviews/management-R0008/PROFESSIONAL_CONTINUATION.md::full`
本次实际证据：`daowei2026/observe-iterate@c286238462c07f15d9ebfe3cac06edc6a2da29d4:runs/BI-01-CO-04/reviews/management-R0008/DECISION.md::#operational-contract`
本次实际证据：`daowei2026/observe-iterate@93436588999d6af0724348b828a5d899134bb3d3:runs/BI-01-CO-04/reviews/WORKMAP_INTAKE_CURRENT.json::full`
本次实际证据：`daowei2026/observe-iterate@e25e585779152aa670d54c87efecba984af4b7e3:runs/BI-01-CO-04/artifacts/worker-BI01CO04-ASOF-VISIBILITY-REPLAY-01/FULL_RESPONSE.md::full`
本次实际证据：`daowei2026/observe-iterate@e25e585779152aa670d54c87efecba984af4b7e3:runs/BI-01-CO-04/artifacts/worker-BI01CO04-ASOF-VISIBILITY-REPLAY-01/REPLAY_MANIFEST.json::full`
本次实际证据：`daowei2026/observe-iterate@e25e585779152aa670d54c87efecba984af4b7e3:runs/BI-01-CO-04/artifacts/worker-BI01CO04-ASOF-VISIBILITY-REPLAY-01/RECOMPUTED_OBJECT_ROWS.csv::full`
本次实际证据：`daowei2026/observe-iterate@e25e585779152aa670d54c87efecba984af4b7e3:runs/BI-01-CO-04/artifacts/worker-BI01CO04-ASOF-VISIBILITY-REPLAY-01/BATCH_INPUT_BOUNDARY_AUDIT.json::full`
本次实际证据：`daowei2026/observe-iterate@e25e585779152aa670d54c87efecba984af4b7e3:runs/BI-01-CO-04/artifacts/worker-BI01CO04-ASOF-VISIBILITY-REPLAY-01/PACKAGE_RECEIPT.json::full`
本次实际证据：`daowei2026/observe-iterate@e25e585779152aa670d54c87efecba984af4b7e3:runs/BI-01-CO-04/artifacts/worker-BI01CO04-ASOF-VISIBILITY-REPLAY-01/TIME_CONTRACT.md::full`

## 本次直接读取的上下文

- BOUNDARY：`daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/README.md::full`
  用途与边界：确认探索项目不是定型规范，动态任务只由本Run正式工作面授权。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/00_BUSINESS_OBJECTIVE.md::full`
  用途与边界：恢复完整业务目标、阶段定位及允许没有好候选的结果。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/01_EXISTING_FEATURES_AND_CAPABILITIES.md::full`
  用途与边界：取得大中小贴近点、方向/确认状态和既有特征能力的准确边界。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/02_CURRENT_WORKING_IDEAS.md::full`
  用途与边界：取得待实践修正的候选观察设想；不得把它当固定流程。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/03_TOOLING_AND_DATA_USAGE.md::full`
  用途与边界：取得正式交付、aidata、图面、时间语义、数据与平台边界。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/04_EXISTING_BUSINESS_REFERENCES.md::full`
  用途与边界：只在本轮问题确需时定向使用历史实物；不继承旧Gate或旧结论。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- MODE_FULL：`daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/05_OWNER_PROCESS_EXPLANATION.md::full`
  用途与边界：完整理解Owner的实际观察过程、两层候选思路、复杂情况和反馈方式。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- FOCUS_FULL：`daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:professional/exploration/tooling_examples/2026-11-01_30m_multi_symbol_turn_chart.md::full`
  用途与边界：作为可核验的低成本起点候选；其品种、频率、参数和run身份不自动成为本Run正式输入。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064:runtime/operations/CASE_OBSERVATION_RUN_GUIDE.md::full`
  用途与边界：遵守新Run、真实任务、Worker签发和动态工作面边界。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

- BOUNDARY：`daowei2026/observe-iterate@e28be2f92522064c146ffe28166350b39a7ae7ca:runs/BI-01-CO-04/OWNER_START.md::full`
  用途与边界：取得本Run Owner GO、分工、工作面和现有Worker线程授权边界。
  本checkout已核位置；正文仍须接收者实际读取。 本次不主张已读复用。

读取Owner完整要求、生效完整任务和输入输出地图，不能用最新remaining替全部责任。按source_reads取得准确正文用于判断，已读未变且可恢复者复用；不递归扫无关历史，不用索引/hash/旧回执代正文。

旧包中已被Owner否定的多余任务，必须由原有权责任者从当前正文、任务、前置、接收和后继删除；只为其存在的辅助代码与检查交原实现者删除。禁止继续完善、改名或列为暂缓/未来优化。不能只在顶部写新原则却继续采用相反正文。真实业务方法、时间、身份、状态、正式输出与消费者保留，技术机制替换回正常平台。正确正文禁止任何压缩或摘要替换。历史提交和实际记录不倒改；历史可追溯不授后续派发。通用材料维护不自动取得用例任务写权。

当前执行材料由管理和有权任务责任者明确采用。推进者取得实际需要的正确正文，不能用管理概述替代业务细节；也不要求每轮重读全部历史和已撤完整任务。

发现新的实质冲突时，给出准确位置与受影响结论，按原责任处理。来源不足只限制真正依赖的判断，不用旧快照补造事实，也不冻结无关工作。

方法版本、业务合同版本、源码版本和运行数据分别保持准确，不随一次方法更新全部追 latest。

按既有协议把完整实质报告及符合Schema的ROLE_RETURN/QUESTION_WORK_RETURN交付GitHub，来源、未执行和资格如实保留；GitHub提交与远端校验成功后手机只回准确定位，不贴长报告或两份JSON。无法交付时按原备用渠道提供真实完整回交，不新增控制表，不重抄协调者已存提示。完整任务未完成就保留完整责任及连续后继，局部交付不自设停点。要求GitHub提交时普通快进并fresh回读，最后commit message带turn complete及本轮invocation_id，无invocation时简要标明执行身份；不造空提交。

专业者回交实际实物、必要自检／执行结果、具体限制及完整未完，不代写管理接收、全局预算或主控派发。管理回交已完成的判断、实际处置和可执行后继，不以问题目录代替决定。

没有完整完成时，说明真实停止原因及已经明确的下一步；不得以自设局部目标完成作为结束解释。
