# BI-01-CO-01 首轮地图与完整任务独立只读审查

task_id: BI01-CO-01-WORKMAP-READER-01
work_id: BI-01
run_id: BI-01-CO-01
role: review
professional_mode: INDEPENDENT_REVIEW
recipient_ref: chatgpt:BI-01-CO-01:review

<a id="scope"></a>
## 本次确切委派与独立性

这是本次新 run 的启动候选审查，当前来源是 R0003 管理的[首轮预采用授权](https://github.com/daowei2026/observe-iterate/blob/2edace84ff6129dca8f39370cde57bc3b880f5d8/runs/BI-01-CO-01/reviews/management-R0003/DECISION.md#reader-pre-adoption)，不是继承旧运行的 Reader 特例或 PASS。R0001 签发后尚未完成真实阅读；R0002 的 W01 修复已由 R0003 实质接收。本次在原文件、原 task_id 下更新输入与授权，不另开 Run 或第二项审查。

在真实未参与本次候选编写的上下文中，独立恢复 Owner 目标和本批完整专业方法，检查下列准确版本的地图、任务及 Binding 是否忠实、完整、可执行。只读受审材料，不替管理编计划、不替执行 Pro 选 Case、不做不存在的市场成果验收，不进行全仓审计。

逻辑接收者由主控关联到实际独立聊天，真实标题/定位/发送由主控记录；这个名字不是已核实的 UI 聊天 ID。独立性来自真实参与关系与实际检查，不来自新建名字。

<a id="input"></a>
## 冻结的受审输入

四项受审实物统一在提交 **`d4ba5e043367fa4678eca339ba32b53044baaad9`**：

| 文件 | 检查用途 |
| --- | --- |
| `runs/BI-01-CO-01/README.md` | 人读全景与当前下一步是否真实 |
| `runs/BI-01-CO-01/00_长程推进地图.md` | 完整业务问题、输入/生产者、产出/消费者、范围和全部未完 |
| `runs/BI-01-CO-01/01_当前任务.md` | 已签全批专业任务、权限、方法、回交及持续复看 |
| `runtime/config/WORKMAP_BINDING.json` | 当前 run 路径、保护面、读者窄输出、尚未采用状态 |

另外读取 exact Owner START、00–04 与 README 原专业方法、R0001 完整回答及保留的业务决定、R0003 当前接收/授权决定。来源版本由下面 Binding 固定，不追 moving branch，不借别的 run 任务/资格。

主控按既有 `workmap_gate.py snapshot --binding runtime/config/WORKMAP_BINDING.json --scope bi01` 对冻结输入取得真实 snapshot/reader_fingerprint，并在发送前与当前输入核对；不得手填指纹或把有摘要当成已读。检查同时保留受监控结果树与 scoped Binding 的变化，不只比较文档 reader_fingerprint。读者实际收到什么、真正读到什么分别说明。若受审输入变化，回原管理说明具体变化和影响，不能对未读新版本签通过。

W01 的技术接收与工具实现采用已经由原签发管理者完成，范围见 R0003 决定。本次不是工程重审，不要求读者重跑测试或阅读全部运行源码；发现影响业务候选可执行性的具体新矛盾仍如实指出。技术通过、独立阅读与管理 Intake 不互相替代。

<a id="question-definition"></a>
## CASE-CO-WORKMAP-READ：专业问题与全部覆盖

本次问题是：这套启动候选能否在不缩小、不改义 Owner 完整目标的前提下，指导专业者取得本批真实数据、完成 3–5 个多品种差异用例与自由回看研究、交统一平台页和可读认识，同时保持必要来源、权限、时间资格及持续管理？

直接对照原文检查以下相互关联的责任，不能只确认文件齐全或文句顺畅：

- 两项产出是否真正指向市场对照和解释，而不是旧特征四项验收、先定赢家、只看最终收益、标签映射或新增分类/评分工程；3–5 例是否仍为全批责任，内部步骤是否被错误改成逐例/逐接口 Gate。
- 2021 共同起点、首版请求结束边界与真实覆盖是否分开；aidata 是不是唯一正式取数入口；方式一全范围日线与方式二局部切片是否混淆；30m、big、mid、图上留量与正式数据范围是否清楚。
- 回看是否可以由实际问题向更早历史或必要尺度扩展；支持、反证、竞争解释和未知是否有实质要求；实际转折位置与后来确认、历史解释与当时辨别是否被混同；没有确认字段是否只限制相应断言。
- 一个真实同页平台交付是否保留；历史单页成功更正有没有被改回必须重写 aidata；页面暂缺是否错误冻结已有可靠数据上的研究；旧测试日期/行数/URL/ZIP 是否被冒用为本批事实。
- 角色、写面、Worker 回原签发 Pro、工具仓/共享服务边界、普通研究自主权是否清楚；已明确旧要求不适用的裁定是否真正落入任务，而非让执行者重新审历史。
- 当前工作、全部未完、条件性投入、RESULT/CHANGE/持续 EFFORT、实际接收者和下一步是否可按原文执行；技术、专业、独立审查、管理接收、Owner 认可是否区分；尚无 Reader/Intake 的事实有没有被伪装成 ADOPTED。

这些是同一次启动审查的完整相关范围，不是新的业务分类表，不要求逐项新开 R。发现明确冲突给出准确原文、受影响结论/消费者和需要原管理裁定的内容；一般表达偏好不得替代 Owner 业务要求。

<a id="deliverables"></a>
## 交付与写面

提交 `runs/BI-01-CO-01/reviews/independent/workmap-01/REVIEW.md`，说明真实输入提交、真实独立上下文依据、实际读到的来源、关键检查及结论、具体 finding/影响、未审范围与限制。结论按真实情况为 PASS、REPAIR_REQUIRED 或 INSUFFICIENT_EVIDENCE；PASS 只限本次启动候选，不是市场研究、工具可用、管理 Intake 或 Owner 认可。

只写上述独立输出窄目录和主控为本次真实 Reader 调用建立的 `provenance/turns/Rnnnn/` 完整回答及 Return。不改受审 README/地图/任务、当前 Workmap 配置、管理决定、共享规范、Intake 或源码。自己的回交绑定自己的实际 invocation/token，不能复用 R0001/R0003 管理身份或归档未发 Reader 身份。未实际打开图不声称看过，本次也不存在须先验收的业务图。

沿原 ROLE_RETURN 与 QUESTION_WORK_RETURN 合同交完整报告和有效回交，准确定位同一份实质报告。现已采用的接收实现支持完整正文及两份独立 JSON；正文不必再内嵌重复 JSON，旧合法内嵌形式的兼容不是本次新增义务。主控实际检查失败则如实回原责任者定位，不自行改工具、伪造通过或把此 Reader 偷换成普通专业派发。

<a id="completion"></a>
## 完成与资格边界

对准确候选与原始依据完成必要独立核查，交清实质判断、影响、限制和两份有效回交后，提交原管理。发现不足不需要你代改候选才能提交；没有必要材料时说明具体缺口及影响，不靠作者自评签通过。未完成实质检查则继续本次限定范围，不能以填回执结算。

你不签正式管理采用，不决定扩大业务范围，不把当前一批研究无限延伸。管理真实消费你对准确版本的意见后，才决定修订或采用和专业发送。

<a id="same-work"></a>
## 同一审查续作

开始或继续本次 exact 输入的首轮独立只读审查，恢复仍可使用的已读原文与已核结果，完成全部相关检查。只补真实未完，不改候选；有新版本或权限冲突交原管理明确受影响范围。交真实独立结论、具体限制和一致回交，不把局部检查扩成整批研究 PASS。本次尚无真实旧 Reader 结果，管理回交不能被当作你的既有审查。

<a id="accept"></a>
## 返回原管理的完整接收要求

由 `chatgpt:BI-01-CO-01:management` 接收本次真实 Reader 报告与两份回交，结合 Owner 完整目标、冻结输入、R0001 保留的业务决定、R0003 当前决定及全部重要未完，核实 finding 的实际影响和范围。准确候选可采用则明确采用、实际 Intake 和专业后继；有实质问题则由管理定向修改自己的地图/任务并限定重读受影响部分。Reader PASS 不自动替代管理决定；主控不代判。当前尚不存在研究成果，不把启动审查当作本批业务接收。

<a id="decide"></a>
## 缺口或变化返回原管理

把本次实际缺失来源、受审版本变化、独立性不足或相反任务正文定位交原管理裁定，说明影响哪些判断和发送动作。保留已核实部分，不用旧运行材料补造资格，不全面冻结与问题无关的已授权工作。主控只投递原文及真实事实，不替管理编计划或选择旧模式绕过。

<a id="return-repair"></a>
## 读者回交定向补件

只补原 Reader 调用的确切缺字段/定位/回交不一致，保留原结论和范围；缺的是实质审查则保持未完继续检查，不用格式补齐冒充完成。不得替管理补缺失决定。一次机械补交仍失败，回原管理按实际缺口窄处理。

<a id="budget"></a>
## 本次投入与返回

本任务是一次限定的启动候选独立核查，不是长期开着的新研究线。完整检查中复用仍有效原文，不全仓搜索、不读取旧 run。没有实际运行计时和结果前不编投入数；主控保留真实 Reader 调用和发送记录，下一次管理消费时连同本次启动累计投入一起判断。缺重型方法判断给出准确问题返回管理，不将只读审查改成代写候选。

<a id="no-triggers"></a>
## 本次不另设批次触发的理由

这是一项具名、限定范围的初始只读接收工作；实际完整结果（包括返修或证据不足）直接按 accept/decide 回原管理，不在这里形成第二条长期专业线，也不新增逐 Case Gate。未完审查按 same_work 连续承担，主控正常收取和既有异常处理不取消；管理收到结果后立即承担采用或修订，不以空 triggers 让责任沉默。完整批次的持续管理已在专业任务 Binding 单独签发，尚未专业发送前不编造其计时起点。

<a id="question-work-binding"></a>
## QUESTION_WORK_BINDING

```json
{
  "schema": "question-work/v2",
  "kind": "BINDING",
  "work_id": "BI-01",
  "goal_ref": {"repo":"daowei2026/observe-iterate","commit":"f7f2bffe9bcddd951d5bf218d56449e8f42999ae","path":"professional/case_observation/00_PURPOSE_AND_OUTPUTS.md","selector":"full"},
  "plan_ref": {"repo":"daowei2026/observe-iterate","commit":"2edace84ff6129dca8f39370cde57bc3b880f5d8","path":"runs/BI-01-CO-01/reviews/management-R0003/DECISION.md","selector":"#reader-pre-adoption"},
  "full_scope_ref": {"answer_ref":"#scope"},
  "batch_result": "对准确冻结的本run启动地图、完整专业任务和Binding进行真实独立只读核查，交有具体检查依据、finding/影响/限制的报告及有效回交，返回原管理作采用或修订；不冒称业务研究已完成。",
  "parent": {"status":"NOT_APPLICABLE_NEW_CASE","ref":null,"reason_ref":{"repo":"daowei2026/observe-iterate","commit":"0c00de3312d8428ff94b76352a6a24f8a190b843","path":"runs/BI-01-CO-01/OWNER_START.md","selector":"full"}},
  "question_ids": ["CASE-CO-WORKMAP-READ"],
  "question_definitions": [{"question_id":"CASE-CO-WORKMAP-READ","definition_ref":{"answer_ref":"#question-definition"},"authority_ref":{"repo":"daowei2026/observe-iterate","commit":"2edace84ff6129dca8f39370cde57bc3b880f5d8","path":"runs/BI-01-CO-01/reviews/management-R0003/DECISION.md","selector":"#reader-pre-adoption"},"parent_question_id":null}],
  "professional_mode": "INDEPENDENT_REVIEW",
  "focus_ref": {"answer_ref":"#question-definition"},
  "coverage_ref": {"answer_ref":"#question-definition"},
  "source_reads": [
    {"source":{"repo":"daowei2026/observe-iterate","commit":"d4ba5e043367fa4678eca339ba32b53044baaad9","path":"runs/BI-01-CO-01/README.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"冻结的人读全景和当前状态","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"d4ba5e043367fa4678eca339ba32b53044baaad9","path":"runs/BI-01-CO-01/00_长程推进地图.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"冻结的完整业务地图和剩余","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"d4ba5e043367fa4678eca339ba32b53044baaad9","path":"runs/BI-01-CO-01/01_当前任务.md","selector":"full"},"requirement":"FOCUS_FULL","purpose":"冻结的完整专业任务、方法引用与Binding；业务正文未因W01改变","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"d4ba5e043367fa4678eca339ba32b53044baaad9","path":"runtime/config/WORKMAP_BINDING.json","selector":"full"},"requirement":"FOCUS_FULL","purpose":"同一输入提交的保护面、run路径和未采用状态","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"0c00de3312d8428ff94b76352a6a24f8a190b843","path":"runs/BI-01-CO-01/OWNER_START.md","selector":"full"},"requirement":"BOUNDARY","purpose":"真实Owner GO、运行身份和权限","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"f7f2bffe9bcddd951d5bf218d56449e8f42999ae","path":"professional/case_observation/README.md","selector":"full"},"requirement":"MODE_FULL","purpose":"恢复当前两项产出及方法替换关系","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"f7f2bffe9bcddd951d5bf218d56449e8f42999ae","path":"professional/case_observation/00_PURPOSE_AND_OUTPUTS.md","selector":"full"},"requirement":"MODE_FULL","purpose":"恢复完整业务目标、批次和非目标","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"f7f2bffe9bcddd951d5bf218d56449e8f42999ae","path":"professional/case_observation/01_RESEARCH_METHOD.md","selector":"full"},"requirement":"MODE_FULL","purpose":"核真实选例、自由回看、解释与挑战","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"f7f2bffe9bcddd951d5bf218d56449e8f42999ae","path":"professional/case_observation/02_OWNER_DELIVERY.md","selector":"full"},"requirement":"MODE_FULL","purpose":"核Owner入口、统一页面及完整图数交付","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"f7f2bffe9bcddd951d5bf218d56449e8f42999ae","path":"professional/case_observation/03_AIDATA_USE.md","selector":"full"},"requirement":"MODE_FULL","purpose":"核必经数据入口、两种用法、2021/mid和时间范围","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"f7f2bffe9bcddd951d5bf218d56449e8f42999ae","path":"professional/case_observation/04_SOURCES_AND_REUSE.md","selector":"full"},"requirement":"MODE_FULL","purpose":"核旧任务退出、知识复用和测试证据层次","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"215bc3ae1c4817fdbc3be4494fb1b6b674103da4","path":"runs/BI-01-CO-01/provenance/turns/R0001/FULL_RESPONSE.md","selector":"full"},"requirement":"BOUNDARY","purpose":"核初始管理业务判断、已知冲突处置和投入依据；当前状态以R0003及冻结输入为准，不信自评替独立检查","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"989e732fc6a017669184184e8e132947cb1685c3","path":"runs/BI-01-CO-01/reviews/management-R0001/DECISION.md","selector":"full"},"requirement":"BOUNDARY","purpose":"保留的完整业务安排和旧要求退出；即时Reader授权已由R0003更新","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"2edace84ff6129dca8f39370cde57bc3b880f5d8","path":"runs/BI-01-CO-01/reviews/management-R0003/DECISION.md","selector":"full"},"requirement":"BOUNDARY","purpose":"当前W01接收、工具采用、更新后的首次阅读授权及未放行边界；不要求重做工程验收","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"f7f2bffe9bcddd951d5bf218d56449e8f42999ae","path":"runtime/operations/ADOPTION_HANDOFF_CHECKLIST.md","selector":"full"},"requirement":"BOUNDARY","purpose":"首轮独立阅读与管理实际采用不能混同","reuse_evidence":null},
    {"source":{"repo":"daowei2026/observe-iterate","commit":"f7f2bffe9bcddd951d5bf218d56449e8f42999ae","path":"runtime/overlay/13_角色回交与主控接续协议.md","selector":"full"},"requirement":"BOUNDARY","purpose":"真实读者回交、独立性、原接收和有限补件","reuse_evidence":null}
  ],
  "deliverables_ref": {"answer_ref":"#deliverables"},
  "completion_ref": {"answer_ref":"#completion"},
  "budget_ref": {"answer_ref":"#budget"},
  "routes": {
    "same_work":{"recipient_role":"review","recipient_ref":"chatgpt:BI-01-CO-01:review","instructions_ref":{"answer_ref":"#same-work"}},
    "accept":{"recipient_role":"management","recipient_ref":"chatgpt:BI-01-CO-01:management","instructions_ref":{"answer_ref":"#accept"}},
    "decide":{"recipient_role":"management","recipient_ref":"chatgpt:BI-01-CO-01:management","instructions_ref":{"answer_ref":"#decide"}},
    "return_repair":{"recipient_role":"review","recipient_ref":"chatgpt:BI-01-CO-01:review","instructions_ref":{"answer_ref":"#return-repair"}}
  },
  "triggers": [],
  "explicit_no_trigger_reason_ref": {"answer_ref":"#no-triggers"}
}
```
