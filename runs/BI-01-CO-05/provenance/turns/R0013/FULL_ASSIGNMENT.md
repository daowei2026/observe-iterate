[BI01-CO-05-R0013-7bb3a890a1de]
work_id: BI-01
invocation_id: BI01-CO-05-R0013-7bb3a890a1de
assignment_token: 07197e6da03f444694e43e2088c5
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

<a id="continuation"></a>
## 9. 唯一接续

`same_work_after_worker_result_returns_to_issuer`

```text
controller worker-order preflight
→ 实际派发新 order
→ 同身份精确读探针
→ [失败：停止且额度耗尽，回 Management]
   或
   [通过：原 R0008 全段脚本单次执行]
→ Worker 回交 / worker-result
→ 原 Professional 消费
→ 技术成功则立即开始 as-of 第一层业务观察
```


来源：daowei2026/observe-iterate@ed0da9d0ff8974ac34ebbb290c859627bfdd6137:runs/BI-01-CO-05/artifacts/professional-R0011/REPORT.md::#continuation

## 本轮原文与位置

本次原始要求：`daowei2026/observe-iterate@a6a8acf7fa65665218d0f2163598d434fb921b24:runs/BI-01-CO-05/01_当前任务.md::#task-route-same-work`
当前生效任务：`daowei2026/observe-iterate@a6a8acf7fa65665218d0f2163598d434fb921b24:runs/BI-01-CO-05/01_当前任务.md::full`
当前任务采用依据：`daowei2026/observe-iterate@0776c5645be4bf1d38c7151baa8662def243e26b:runs/BI-01-CO-05/reviews/management-R0010/DECISION.md::#continuation`
上一轮实际采用的任务绑定：`daowei2026/observe-iterate@a6a8acf7fa65665218d0f2163598d434fb921b24:runs/BI-01-CO-05/01_当前任务.md::#question-work-binding`
完整工作范围：`daowei2026/observe-iterate@a6a8acf7fa65665218d0f2163598d434fb921b24:runs/BI-01-CO-05/01_当前任务.md::#task-full-scope`
最新完整回答：`daowei2026/observe-iterate@ed0da9d0ff8974ac34ebbb290c859627bfdd6137:runs/BI-01-CO-05/provenance/turns/R0011/FULL_RESPONSE.md::full`
最新结构化问题回交：`daowei2026/observe-iterate@00f204b40d9d0477412389eb7ba847fbd8b74ce2:runs/BI-01-CO-05/provenance/turns/R0011/QUESTION_WORK_RETURN.json::full`
最新角色回交：`daowei2026/observe-iterate@b2b0883e54c0e8118f55357b82e3c79765a5c05e:runs/BI-01-CO-05/provenance/turns/R0012/ROLE_RETURN.json::full`
原任务内最新接续：`daowei2026/observe-iterate@ed0da9d0ff8974ac34ebbb290c859627bfdd6137:runs/BI-01-CO-05/artifacts/professional-R0011/REPORT.md::#continuation`
本次实际证据：`daowei2026/observe-iterate@45e9f33474d8d36f4f9fa07a3f72824c710c0d46:runs/BI-01-CO-05/artifacts/worker-BI01CO05-FULLRANGE-CONDITIONAL-REENTRY-01/FULL_RESPONSE.md::full`
本次实际证据：`daowei2026/observe-iterate@45e9f33474d8d36f4f9fa07a3f72824c710c0d46:runs/BI-01-CO-05/artifacts/worker-BI01CO05-FULLRANGE-CONDITIONAL-REENTRY-01/REENTRY_OUTCOME.json::full`
本次实际证据：`daowei2026/observe-iterate@45e9f33474d8d36f4f9fa07a3f72824c710c0d46:runs/BI-01-CO-05/artifacts/worker-BI01CO05-FULLRANGE-CONDITIONAL-REENTRY-01/PROBE_RECEIPT.json::full`
本次实际证据：`daowei2026/observe-iterate@45e9f33474d8d36f4f9fa07a3f72824c710c0d46:runs/BI-01-CO-05/artifacts/worker-BI01CO05-FULLRANGE-CONDITIONAL-REENTRY-01/EXECUTION_RECEIPT.json::full`
本次实际证据：`daowei2026/observe-iterate@45e9f33474d8d36f4f9fa07a3f72824c710c0d46:runs/BI-01-CO-05/artifacts/worker-BI01CO05-FULLRANGE-CONDITIONAL-REENTRY-01/MOUNT_AND_IDENTITY.json::full`
本次实际证据：`daowei2026/observe-iterate@45e9f33474d8d36f4f9fa07a3f72824c710c0d46:runs/BI-01-CO-05/artifacts/worker-BI01CO05-FULLRANGE-CONDITIONAL-REENTRY-01/BLOCKER_EVIDENCE.json::full`
本次实际证据：`daowei2026/observe-iterate@45e9f33474d8d36f4f9fa07a3f72824c710c0d46:runs/BI-01-CO-05/artifacts/worker-BI01CO05-FULLRANGE-CONDITIONAL-REENTRY-01/SHA256SUMS::full`
本次实际证据：`daowei2026/observe-iterate@2e34c004458e30d4bb02863def47514beb3a7ed7:runs/BI-01-CO-05/provenance/turns/R0013/WORKER_RESULT_TRANSPORT_CHECK.json::full`
本次实际证据：`daowei2026/observe-iterate@ed0da9d0ff8974ac34ebbb290c859627bfdd6137:runs/BI-01-CO-05/artifacts/professional-R0011/WORKER_ORDER.md::full`
本次实际证据：`daowei2026/observe-iterate@0776c5645be4bf1d38c7151baa8662def243e26b:runs/BI-01-CO-05/reviews/management-R0010/DECISION.md::full`
本次实际证据：`daowei2026/observe-iterate@e03e184b06fb058c36fe18c28bc0dc52701b803f:runs/BI-01-CO-05/OWNER_CHANGE_20261102_R0005_TIME_COVERAGE.md::full`

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
观察时间：2026-11-02T19:44:16.847537+00:00
有效回交数：5

按既有协议把完整实质报告及符合Schema的ROLE_RETURN/QUESTION_WORK_RETURN交付GitHub，来源、未执行和资格如实保留；GitHub提交与远端校验成功后手机只回准确定位，不贴长报告或两份JSON。无法交付时按原备用渠道提供真实完整回交，不新增控制表，不重抄协调者已存提示。完整任务未完成就保留完整责任及连续后继，局部交付不自设停点。要求GitHub提交时普通快进并fresh回读，最后commit message带turn complete及本轮invocation_id，无invocation时简要标明执行身份；不造空提交。

专业者回交实际实物、必要自检／执行结果、具体限制及完整未完，不代写管理接收、全局预算或主控派发。管理回交已完成的判断、实际处置和可执行后继，不以问题目录代替决定。

没有完整完成时，说明真实停止原因及已经明确的下一步；不得以自设局部目标完成作为结束解释。
