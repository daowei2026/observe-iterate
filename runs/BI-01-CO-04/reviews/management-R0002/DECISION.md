# BI-01-CO-04 R0002｜R0001 交付缺件定向补齐

work_id: BI-01
run_id: BI-01-CO-04
role: management
invocation_id: BI01-CO-04-R0002-MSTART-HANDOFF-518040c2
assignment_token: 41b4ae30ce79f3d6ca799bab62aa956fe27cc3efe846833b

- `dispatch_kind`: `DELIVERY_REPAIR`
- `decision`: `ISSUE_FORMAL_INDEPENDENT_WORKMAP_READER_AND_REPAIR_RETURN_LOCATORS`
- 原实质成果：`runs/BI-01-CO-04/reviews/management-R0001/DECISION.md`
- 原正式专业任务：`runs/BI-01-CO-04/01_当前任务.md`

<a id="decision-summary"></a>
## 1. 本轮决定

本轮只补 R0001 已承诺但未形成可实际派发实物的独立 Workmap Reader 委派，并在本轮两份 Return 中使用生成器可解析的 `#anchor` 定位。R0001 的业务目标、采用／撤销裁定、首项 `CASE_OBSERVATION` 专业任务、投入起点和全部资格限制保持原样；历史 R0001 报告与 Return 不倒改。

具体处置：

1. 签发具名只读 Reader 任务 `BI01-CO-04-WORKMAP-READER-01`，正式文件为 `runs/BI-01-CO-04/reviews/management-R0001/READER_TASK.md`，接收者为 `chatgpt:BI-01-CO-04:workmap-reader-01`，mode 为 `INDEPENDENT_REVIEW`；
2. Reader 只核固定输入集的完整性、内部一致性、任务可读性、来源／方法覆盖和派发前机械风险，不形成市场观察，不接收专业业务结果，也不自动通过；
3. 将 Reader 专属输出固定到 `runs/BI-01-CO-04/reviews/independent/workmap-01/`，并从 Reader 输入结果投影中排除该严格子目录，防止审查输出反向改变自身输入；
4. Workmap Intake 仍保持 `reader_check.status=PENDING`，直到真实独立 Reader 调用、完整回交和管理接收发生；
5. 本轮不宣称 Reader 已发送／执行、dispatch preflight 已通过、Professional 已发送，或首个业务 Case 已形成。

<a id="reader-pre-adoption"></a>
## 2. Reader 前置采用与冻结输入

本次 Reader 的正式输入基线冻结在：

- `input_commit`: `ed9a32badf4077c25534184da28b0ad41db396ec`
- `workmap_snapshot`: `5f24d63895be9d5f52182fd8e4fa94a901667e8bdfda0fc4529f9addcecf19b2`
- `reader_fingerprint`: `b5f0c9826e1b7f639e39f64276e31d26a834e8ffcbd855497c6be628a63fc06b`
- `scope`: `bi01`
- `binding`: `runtime/config/WORKMAP_BINDING.json`
- `reader_output_root`: `runs/BI-01-CO-04/reviews/independent/workmap-01`

Reader 必须在同一 exact commit 全文读取并核对：Run README、长程推进地图、当前正式任务、Workmap Binding；同时全文读取 Owner GO 以及 Binding 中全部真实 `rule_paths`。存在、blob 或摘要均不等于已读。

Reader 只回答以下具名问题：

> 固定输入是否把 Owner GO、完整业务目标、当前任务、专业方法入口、证据资格、未完与真实派发关系连成一个可由 Professional 继续的工作面；是否存在足以阻止当前专业派发的具体断裂、矛盾、遗漏或越权？

Reader 必须把“阻断派发的问题”和“不阻断但应记录的限制”分开；不得把尚未产生专业结果写成管理失败，也不得以结构完整性替代业务接收。

<a id="adoption"></a>
## 3. 正式 Reader 委派采用

管理正式采用并签发：

- `task_id`: `BI01-CO-04-WORKMAP-READER-01`
- `role`: `review`
- `professional_mode`: `INDEPENDENT_REVIEW`
- `recipient_ref`: `chatgpt:BI-01-CO-04:workmap-reader-01`
- `task_path`: `runs/BI-01-CO-04/reviews/management-R0001/READER_TASK.md`
- `output_path`: `runs/BI-01-CO-04/reviews/independent/workmap-01/REPORT.md`
- `return_to`: `chatgpt:BI-01-CO-04:management`

该采用只授权一次当前冻结输入的独立只读审查。主控须用 Reader 任务文件全文作为 `current_task_ref`，用同一文件中唯一 `#question-work-binding` 作为 `binding_ref`，用本节 `#adoption` 作为 `task_adoption_ref`，另建真实 Pro 新 R、保存原样载荷和 `NOT_SENT`，经 pre-dispatch 后实际发送。不得把本轮管理调用、主控本地检查、旧 Run Reader 或未提交本地报告当作该 Reader。

<a id="reader-budget"></a>
## 4. Reader 投入边界

- 当前预算：一次真实独立 Reader Pro 调用；
- 只有 Reader 回交指出可复现且影响派发的具体缺件时，才做一次定向 repair；
- Reader 调用不计入首项专业任务的 1—2 次有效 Professional 调用；
- 不因 Reader 增加全仓审计、历史 Run 复核、业务方法再设计或新治理层；
- 若输入在发送前发生承重变化，旧 Reader 资格不沿用，按新 fingerprint 重新准备，而不是修改历史报告。

<a id="reader-accept"></a>
## 5. Reader 回交与管理接收

真实 Reader 必须交：

1. 对冻结输入逐项实际读取的材料使用记录；
2. `PASS`、`REPAIR_REQUIRED` 或 `INSUFFICIENT_EVIDENCE` 之一，且给出具体证据；
3. 阻断项、非阻断限制、未审范围及不能推出的结论；
4. 完整报告、`ROLE_RETURN.json`、`QUESTION_WORK_RETURN.json`；
5. 准确的 input commit、reader fingerprint、invocation 和 assignment token。

回交先由管理接收。只有报告与冻结输入匹配、独立身份成立、Return 一致且结论可追溯，管理才可把 Intake 的 Reader 状态从 `PENDING` 改为 `RECORDED`。`RECORDED` 仍只是派发前证据，不是专业业务结果通过；随后还须运行适用的 dispatch preflight，并单独记录 Professional 的真实发送。

<a id="completed-scope"></a>
## 6. 本轮已完成

- 保留并确认 R0001 已成业务判断、当前专业任务和持续管理责任，不重做业务分析；
- 核实具体缺件是 Reader 正式委派／Binding／采用关系缺失，以及原 Q-Return selector 未带 `#`；
- 签发具名独立 Reader 的目标、冻结输入、读写边界、回交与接收关系；
- 给 Reader 专属输出建立自输入排除，保持业务 artifacts 与其他 independent review 仍受监看；
- 本轮 Return 改用真实 `#completed-scope`、`#remaining-scope`、`#material-use`、`#handoff` 等可解析定位；
- 未倒改 R0001 历史文件，未虚报 Reader、Professional 或业务结果已发生。

<a id="remaining-scope"></a>
## 7. 仍未完成

- Reader 尚未由主控建立真实 review R、完成 pre-dispatch、发送或回交；
- Workmap Intake 的 Reader 状态仍应保持 `PENDING`；
- 首项 `CASE_OBSERVATION` 专业任务尚未实际发送和执行；
- 本 Run 的正式特征／行情输入资格、首个 as-of 多品种判断、自然挑战、失败候选／无候选与方法反馈仍全部未形成；
- 后续独立专业审查、管理接收、Owner 反馈和完整阶段收拢仍按 R0001 原责任继续。

上述未完不因本轮 metadata 修复而升级为完成。完整 BI-01 工作仍为 ACTIVE；R0001 的 Professional 投入计数起点未启动，也不因本轮 Reader 补交清零或前移。

<a id="material-use"></a>
## 8. 材料使用记录

本轮实际读取并用于定向修复：

- R0002 `FULL_ASSIGNMENT.md`、`DISPATCH.json`、`INVOCATION.json` 与真实发送记录；
- R0001 `FULL_ASSIGNMENT.md`、`DECISION.md`、`ROLE_RETURN.json`、`QUESTION_WORK_RETURN.json`；
- `HANDOFF_CHECK.md` 的 Reader 缺件与 locator 检查；
- 当前 `01_当前任务.md` 的 `#task-route-decide` 和 `#question-work-binding`；
- `WORKMAP_BINDING.json`、`WORKMAP_INTAKE_CURRENT.json`、Run README 与长程地图；
- `tools/bi01_run_gate.py` 及其离线测试中首次 Reader 的准确接线约束；
- `overlay/tools/workmap_gate.py`、`management_prompt.py`、`question_work.schema.json`、`question_work_check.py`、`longrun_handoff.schema.json`；
- `runtime/config/COORDINATOR_DISPATCH.json` 与 `operations/V2_ROUND_RECORD_CONTRACT.md`。

`unread_required=[]`，`unavailable_required=[]`。本轮没有声称未来 Reader 已读取任何材料。

<a id="handoff"></a>
## 9. 准确接续

主控下一步仅按既有流程落实已签 Reader：

1. 取得 `READER_TASK.md` 的 exact commit；
2. 以该文件全文和其中唯一 Binding、新 R 身份、本决定 `#adoption`，准备 `chatgpt:BI-01-CO-04:workmap-reader-01` 的真实 review 调用；
3. 保存原样完整任务、短载荷、`NOT_SENT` 和 pre-dispatch 结果后实际发送；
4. 真实 Reader 回交后交本管理聊天按 `#reader-accept` 接收；在此之前 Intake 保持 `PENDING`；
5. Reader 被接收且 dispatch preflight 通过后，才向 `chatgpt:BI-01-CO-04:professional` 实际发送既有 `01_当前任务.md`；
6. R0001 的 RESULT／CHANGE／EFFORT 三类管理责任、专业投入起点和所有业务限制继续有效。

本轮结束于“正式 Reader 委派已可供主控执行”，不等于 Reader 已执行或 Professional 已派发。
