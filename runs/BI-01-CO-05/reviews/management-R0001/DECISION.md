# BI-01-CO-05 R0001 M-START 管理决定

work_id: `BI-01`  
run_id: `BI-01-CO-05`  
invocation_id: `BI01-CO-05-R0001-ba918c19cb62`  
role: `management`  
decision_status: `M_START_COMPLETE__PROFESSIONAL_TASK_ISSUED_NOT_SENT`

<a id="decision-summary"></a>
## 一、决定摘要

本轮完成新 Run 的首次实质管理：恢复完整 Owner 目标与初版过程，建立业务问题—真实输入—证据资格—专业认识—Owner/下一行动的关系图，裁定旧 Run 与当前来源的权力，签发一个能真实实践 Owner 完整过程的专业任务，并建立 Workmap Binding 与 Intake。

当前可以进入专业派发准备；**不能声称任务已经实际发送、Professional 已执行、任何市场规律成立或本阶段完成。**

<a id="source-adoption"></a>
## 二、来源采用与旧要求处置

### 当前现行

- `professional/exploration/00_BUSINESS_OBJECTIVE.md`：最终投资业务目的；
- `professional/exploration/06_EXPLORATION_STAGE_GOAL.md`：当前探索任务直接目标和职责；
- `professional/exploration/05_OWNER_PROCESS_EXPLANATION.md`：当前优先实践的 Owner 完整初版过程；
- `01_EXISTING_FEATURES_AND_CAPABILITIES.md` 与 `03_TOOLING_AND_DATA_USAGE.md`：特征语义、正式数据/图与权限边界；
- `runs/BI-01-CO-05/OWNER_START.md`：本 Run 的真实 GO、分支、Worker 线程与首次实践要求；
- 当前运行/回交合同：DR13、DR14、Overlay 08/12/13 和 V2 round contract。

### 摘要或参考，不能替代现行来源

- `02_CURRENT_WORKING_IDEAS.md` 只是 05 的摘要；
- `04_EXISTING_BUSINESS_REFERENCES.md` 只提供定向历史入口；
- `tooling_examples/2026-11-01_30m_multi_symbol_turn_chart.md` 只证明特定输入与参数下的一次工具实践，不能成为本 Run 默认数据、频率、品种、窗口或业务证据。

### 不继承/撤销作为当前要求

CO-01—CO-04 的地图、任务、Reader、预算、在途、固定 Case、as-of 合同、业务结论和触发状态全部留在历史。没有将 CO-04 的固定 query snapshot、固定 T、rb/hc/i、30m 或其投入边界迁入本 Run。历史准确工具知识可按当前任务定向复用，但必须重新取得本 Run 的输入资格。

<a id="business-system"></a>
## 三、完整业务系统判断

当前正常系统必须是：

1. Professional 取得本 Run 真实 aidata/特征输入及同身份图和正式切片；
2. 区分正式字段、上游可靠映射、图面线索与未知，核 actual/confirm/as-of 和方向语义；
3. 沿信息到达顺序观察多品种大尺度背景的形成、变化和失效，并判断中尺度结构是否足够；
4. 在具体背景内形成、挑战和更新候选规律/前瞻判断，或交合法无候选/不适配；
5. 将业务新增认识和 Owner 过程实践反馈一起交管理；
6. Management 决定同工作续作、下一具名问题、独立业务审查、Owner 校准或停止。

数据可得、图可读、工具 PASS、单 Case 或一个正式文件都不是业务接收。证据资格只限制依赖它的主张，不把一个字段/来源/Reader/Worker 缺口升级为全局冻结。

<a id="current-task-decision"></a>
## 四、正式专业任务

签发：

- task_id: `BI-01-CO-05-OWNER-PROCESS-PRACTICE-01`
- path: `runs/BI-01-CO-05/01_当前任务.md`
- professional_mode: `CASE_OBSERVATION`
- question_id: `CASE-OWNER-PROCESS-PRACTICE-01`
- recipient route: `chatgpt:BI-01-CO-05:professional`

任务不预选品种、时间、频率或参数；Professional 从真实可用输入中选择最低成本且适配的范围并记录理由。任务必须走过完整 Owner 过程，首个可消费实践包只是管理复看点，不是主动停点。

<a id="reader-decision"></a>
## 五、Reader、Reviewer 与 Worker

### Workmap Reader

`reader_check.status=NOT_REQUIRED`。

授权来源：`professional/exploration/06_EXPLORATION_STAGE_GOAL.md`，并由本 Run Owner GO 明确采用“首次 Workmap Reader 按需而非固定前置”。理由：本轮由有权 Management 首次建立新 Run 的真实地图、任务、来源和 Intake；当前没有 Owner 指定独立 Workmap Reader，也没有需独立裁定的严重意图冲突。该决定不等于 Reader PASS，机械 Workmap/dispatch 检查仍全部保留。

### 业务 Reviewer

当前不派。尚无具体市场主张或候选规律可供独立复做。首个专业实践包到达后，管理按主张重要性、证据争议与投入收益决定是否签具名独立审查。

### Worker

当前不预签。只有 Professional 发现直接阻断业务观察的具体数据/制图/计算/核验缺口，才可按现行合同签 0—1 个窄工单；实际线程为 `01a17dd7-5033-7e63-b7a2-edd90b691c33`，workspace 为 `/dwdhome/fy/cgpterm`。Worker 不代行业务或管理判断。

<a id="effort-decision"></a>
## 六、投入与触发

- 第一有效 Professional 调用：取得真实输入与初步时间轨迹，或在唯一现场技术阻断时签窄 Worker；
- 第二有效调用：应消费技术结果并推进到真实业务观察、候选/无候选和过程反馈；
- 每两次有效 Professional 调用且工作仍 ACTIVE，触发 `ACTIVE_PROCESS_PRACTICE_EFFORT_REVIEW`；
- 首个完整过程实践包触发 `FIRST_PROCESS_PRACTICE_PACKAGE`；
- 承重输入/字段语义冲突、问题不适配或主要过程替换建议触发 `CORE_INPUT_OR_PROCESS_CHANGE`；
- 若连续回交仍主要停留在来源、工具、格式或运行准备，下一管理轮必须改变真实安排，而非只重申完整范围。

当前段最多 0—1 个窄 Worker；新增技术路线先回管理。没有给完整探索预设固定总轮数。

<a id="owner-items"></a>
## 七、Owner 事项

### 当前无阻塞 Owner 决定

普通输入选择、可逆图面安排、局部缩放、正式切片和对象定位由 Professional 在现有授权内决定。无需 Owner 逐项批准。

### 到时必须显式呈现 Owner

- Professional 或 Management 建议实质替换当前研究问题、主要做事过程或业务方向；
- 形成重要新增候选规律、投资用途解释或当前过程“不适配”的结论；
- 需要把探索做法固定为规范/Agent，或转入全市场分类、评分器、重型回放工程。

Owner 沉默不算批准。

<a id="dispatch-decision"></a>
## 八、派发与机械状态

- Workmap Binding：更新为 `workmap-binding/v2`、`status=ADOPTED`；
- 当前任务：`ISSUED`；
- dispatch decision：`ISSUED`；
- actual delivery：尚未由协调者在 exact commit 上观察，当前事实为 `NOT_SENT`；
- 本管理上下文只通过 GitHub connector 建立和回读实物，未运行本地 `workmap_gate.py` CLI；协调者必须在实际发送前用最终 exact commit、真实 delivery JSON 和当前 Binding 运行机械 Intake/dispatch preflight；
- CLI 未运行不授权手写绕过；失败只修受影响的地图/Intake/发送记录，不重做业务或继承旧 Reader。

<a id="management-remaining"></a>
## 九、持续管理责任

1. 收取首个专业结果时核真实业务内容、证据资格、Owner 过程实践得失和全部未完；
2. 消费 RESULT/CHANGE/EFFORT，避免工具循环；
3. 决定 same-work、下一具名问题、Reviewer、Owner 校准或停止；
4. 重要新增分析明确交 Owner；
5. 地图、任务、Owner 来源或 watch roots 实质变化时更新 Intake；
6. 不把机械 PASS、Worker 结果或 Professional 自评冒充管理接收。

<a id="handoff"></a>
## 十、当前后继

协调者取得本轮完整管理回交后：

1. fresh read 当前分支的 Binding、README、地图、任务、决定和 Intake；
2. 在同一 exact commit 运行 Workmap `check` 与带真实 `NOT_SENT` delivery 的 `dispatch`；
3. 通过后按 Overlay 08 生成 Professional 完整派发原文、提交 GitHub、回读，并向 `chatgpt:BI-01-CO-05:professional` 发送经核验的手机短指引；
4. 保存真实发送记录；未发送、失败或状态未知不得改写成已发送；
5. 不新增 Reader、Worker 或业务范围。
