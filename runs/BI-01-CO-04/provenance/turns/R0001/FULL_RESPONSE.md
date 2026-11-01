# BI-01-CO-04 R0001｜首次实质管理决定

- `work_id`: `BI-01`
- `run_id`: `BI-01-CO-04`
- `invocation_id`: `BI-01-CO-04-R0001-MSTART-d4227cb476`
- `assignment_token`: `5481bd398ce7f2ab306cdf7467d4b0d4f2d6975996fe92c4`
- `role`: `management`
- `recipient`: `chatgpt:BI-01-CO-04:management`
- `decision`: `ADOPT_RUN_AND_ISSUE_INITIAL_CASE_OBSERVATION`
- `professional_task`: `BI-01-CO-04-CASE-INITIAL-ASOF`
- `professional_mode`: `CASE_OBSERVATION`

<a id="decision-summary"></a>
## 1. 决定摘要

本 Run 具备真实 Owner GO，且此前没有可继承的本 Run 专业结果、Accepted Parent、当前任务或管理 Intake。本轮完成首次实质管理采用，并签发首项专业任务：

> 在严格 as-of T、不得使用未来确认的条件下，核验既有特征能否支持一次诚实的多品种前瞻比较；重点检验中尺度已确认差异是否提供超出“大尺度同方向背景”的独立选择信息。除主路径外，沿同一材料继续到最近的自然挑战、失败候选或合法无候选，并把结果反馈给下一轮方法选择。

采用路径为 `runs/BI-01-CO-04/01_当前任务.md`。该任务属于 `CASE_OBSERVATION`，不是方法发布、单图试跑、全仓审计或历史结果复述。

本轮**没有**预签 Worker 工单，没有宣称独立 Reader 已完成、任务已发送、Professional 已执行或任何业务 Gate 已通过。任务已由管理签发；主控须先按现行 Workmap 机制完成真实 Reader／dispatch preflight，再实际发送。

<a id="normal-business-system"></a>
## 2. 正常业务系统与前后关系

### 2.1 业务问题

Owner 要解决的不是“某个转折点算得对不对”，而是：利用已经存在的大／中／小尺度贴近点及其关系，逐步发现有前瞻价值的市场现象和候选模式，使人能够在当时可知的信息下判断哪些品种更值得继续观察、目标是哪一种后续市场过程；可靠答案也可以是“没有候选”。

### 2.2 正常证据链

| 位置 | 生产／输入 | 必须先解决的资格 | 合法输出 | 下游消费者 |
|---|---|---|---|---|
| 正式特征与行情 | 特征交付、manifest、board／节点数据、行情窗口、配置与参数 | 输入身份、字段语义、run、时间范围、频率、缺失／计算状态 | 可追溯的对象与行情事实 | Professional Pro |
| 时间状态重建 | 大／中／小贴近对象、方向、确认状态 | 实际转折时间与确认／发布可知时间分离；截至 T 截断 | T 时真实可知状态 | 前瞻比较 |
| 背景与差异 | 多品种大尺度背景、中尺度状态、小尺度局部线索 | 特征尺度、K 线频率、图节点层级分开；贴近点不自动等于 zig | 候选／排序／无候选的证据基础 | 业务判断 |
| 前瞻判断 | 明确后续市场过程及候选 | 禁止最终历史图倒填；说明不能推出什么 | 可证伪判断 | 后续确认与挑战 |
| 支持／反证 | 后续确认点、反向对象、失败候选、相邻区间 | 支持、反证、等待、数据缺口和真实无信号分开 | 更新后的认识与替代解释 | 管理接收 |
| 方法反馈 | 主路径、反例、组织增量与业务增量 | 不以“图好看／字段齐全”冒充投资知识 | 保留／修改／停止的工作设想 | 下一专业任务与 Owner |

### 2.3 证据等级

1. **正式证据：**当前 Case 的正式字段、manifest、配置、时间与可知性均可核；
2. **可靠映射：**有明确上游语义和版本映射，但仍需说明适用范围；
3. **视觉线索：**图上可见、尚无正式字段或时间资格，只能用于提出问题；
4. **未知／不可用：**来源、语义、时间或状态不能成立，不得补猜。

<a id="adoption-and-withdrawal"></a>
## 3. 当前采用、保全与不采用

### 3.1 采用

- 采用 Owner 的完整业务目标和原过程说明，当前摘要只作导航；
- 采用“大尺度看背景、中尺度找差异、小尺度作局部补充”作为**待实践检验的工作假设**；
- 采用 as-of T、实际转折时间／确认可知时间分离、支持与反例并看；
- 采用历史 30m rb／hc／i 图面实践作为低成本输入候选，但须重新核本 Run 数据资格；
- 采用现有 Run 工作面、Question Work v2、Workmap Intake、角色回交与主控接续机制；
- 采用 `CASE_OBSERVATION` 为正式专业 mode。

### 3.2 保全

- 正确的特征语义、工具知识、Owner 原过程和历史实物定位保留；
- 旧结果只按其准确版本和范围用作来源事实；
- 未受具体输入缺口影响的专业工作可继续；
- 执行 Pro 可在真实需要出现后签限定 Worker 技术工单，Worker 结果仍回原签发 Pro 消费。

### 3.3 不采用／撤销为当前前置

以下内容不取得本 Run 当前行动权：

- 旧 CO Run 的任务、Gate、聊天、预算、在途、等待或“已通过”状态；
- 把 U2／U3、旧 I2—I6 或历史图直接视为本 Run 专业结果；
- 先做全仓审计、全历史 taxonomy、通用 Agent 固化或另建治理平台；
- 把“一层筛背景、二层看中尺度”固化成两个串行 Gate；
- 把 1d 总览、rb／hc／i、30m、固定参数或某一图节点规定为每轮默认配置；
- 以工具可运行、图可读、字段存在、schema PASS 或单一成功例代替业务完成；
- 让 Worker、主控或本轮管理者代替 Professional Pro 形成业务观察，或代替独立 Reviewer 自签资格。

<a id="completed-and-open"></a>
## 4. 已完成、当前空白与资格限制

### 4.1 已完成

- Owner GO、本 Run 身份、管理角色、写面和 Worker 线程边界已明确；
- 探索目标、既有能力、当前设想、工具／数据使用、历史参考、Owner 完整过程及管理／回交合同已全文读取；
- 已形成完整业务关系、当前优先顺序、条件性投入和管理触发；
- 已建立本 Run README、推进地图、当前任务、正式 Binding 与 Intake；
- 已签发首项完整专业任务。

### 4.2 尚未完成

- 本 Run 正式特征／行情输入的准确身份、字段、参数和时间资格；
- 首个 as-of 多品种判断、自然挑战、失败候选或无候选结果；
- 对当前工作假设的真实支持、反证或无增量结论；
- 任何 Professional 回交、独立专业审查、管理接收或 Owner 反馈；
- 独立 Reader 记录、dispatch preflight 和实际发送。

### 4.3 不能升级的资格

历史图面实践只证明特定输入下曾完成绘图；它不证明本 Run 已取得同一数据，也不证明图中所有点有方向、可在 T 时知道或具有前瞻价值。当前管理结论只签发问题和工作，不签业务结果。

<a id="full-gap-and-priority"></a>
## 5. 全范围差距与优先顺序

1. **P0｜派发资格与真实输入：**完成独立 Reader／dispatch preflight；Professional 核 manifest、字段、参数、时间语义和实际可读实物。
2. **P0｜首个完整业务循环：**主 as-of 比较 + 最近自然挑战／失败候选／合法无候选 + 替代解释 + 方法反馈。
3. **P1｜管理接收：**明确哪些范围可信、哪些需补方法／数据／技术核查，是否形成独立业务增量；据此签发下一专业工作。
4. **P1｜必要独立专业审查：**有 exact 候选后，复做承重判断和反例；不在候选尚不存在时造审查结论。
5. **P1｜多轮扩展：**围绕真实发现增加相邻成功／失败场景，检验适用边界，避免参数或品种偏置。
6. **P1｜Owner 消费：**形成关键图、过程、争议、限制与行动选项，取得真实反馈并转成下一轮工作。
7. **终点收拢：**当前可用认识、完整实物、证据资格、反例、方法边界、未完、投入偏差和直接后继。

<a id="issued-work"></a>
## 6. 已签发工作

**正式任务：**`runs/BI-01-CO-04/01_当前任务.md`

- `task_id`: `BI-01-CO-04-CASE-INITIAL-ASOF`
- `professional_mode`: `CASE_OBSERVATION`
- `recipient_ref`: `chatgpt:BI-01-CO-04:professional`
- `full_scope`: 首个完整专业探索批，而非单图／单 Case 停点；
- `batch_result`: 输入资格、主 as-of 判断、自然挑战／失败候选／合法无候选、替代解释、方法反馈和完整实物；
- `Worker`: 当前不签；真实技术缺口出现后由 Professional Pro 定向签发；
- `accept`: 回本管理聊天执行 M-REASSESS；
- `independent_review`: exact 专业候选形成后由管理按实际影响签发，不预填 PASS。

<a id="budget"></a>
## 7. 投入预测与复看

Owner 未规定轮数，历史投入不继承。本 Run 当前已知投入为一次 M-START 管理调用。

- 首个专业批：预计 1—2 次有效 Professional 调用；
- 技术补齐：0—1 个定向 Worker 工单，仅在真实缺口出现时；
- 首次管理复看：首个可消费循环形成时立即触发，或累计两次有效 Professional 调用仍无业务主体时触发；
- 持续管理：完整工作 ACTIVE 时，每两次有效调用复看一次，累计起点不清零；
- 完整终点：预计需要多个相邻 Case、支持／反例、必要审查和 Owner 反馈；当前不能诚实给出固定总轮数。后续必须随真实结果更新，而不是用“不确定”取消预测责任。

若首个循环提前形成，不为用满预算继续加厚；若两轮仍停留在工具／来源循环，管理必须改变真实安排。

<a id="owner-items"></a>
## 8. Owner 事项

当前没有需要 Owner 先回答的普通细节；现有授权足以开始专业工作。只有出现以下情况才回 Owner：

- 正式输入不可取得且替代输入会改变业务问题；
- 需要超出现有仓库／线程／写面的新授权；
- 两种业务目标存在真实冲突，管理无法在既有目的内裁定；
- 已形成有用首版，需要 Owner 对过程、图面或下一业务方向给实质反馈。

<a id="material-use"></a>
## 9. 材料使用记录

本轮已全文读取并实际使用：

| 来源 | 用途 |
|---|---|
| `FULL_ASSIGNMENT.md`、`OWNER_START.md`、`M_START_INPUT.md`、`QUESTION_WORK_BOOTSTRAP.json` | 当前授权、完整任务、身份、回交与新 Run 边界 |
| `professional/README.md`、`exploration/README.md` | 确认探索性质、动态工作面与背景权力 |
| `00_BUSINESS_OBJECTIVE.md` | 完整业务目标与阶段定位 |
| `01_EXISTING_FEATURES_AND_CAPABILITIES.md` | 特征对象与能力边界 |
| `02_CURRENT_WORKING_IDEAS.md` | 当前候选设想，不固定化 |
| `03_TOOLING_AND_DATA_USAGE.md` | 正式交付、aidata、图、时间和权限边界 |
| `04_EXISTING_BUSINESS_REFERENCES.md` | 历史来源的定向使用与不继承 |
| `05_OWNER_PROCESS_EXPLANATION.md` | Owner 完整观察过程、复杂情况与反馈方式 |
| `2026-11-01_30m_multi_symbol_turn_chart.md` | 已完成工具实践和当前低成本入口候选 |
| `CASE_OBSERVATION_RUN_GUIDE.md`、`WORKMAP_BINDING.json`、`ADOPTION_STATUS.md` | 新 Run 工作面、采用与校验边界 |
| `DR06`、`DR08`、`DR13`、`DR14`、`MANAGEMENT_METHOD_HARNESS` | 管理职责、任务组合、Binding、触发和阶段资格 |
| Overlay 08／12／13、两份 schema、Workmap 工具与测试 | 派发、Intake、回交和结构要求 |
| cgpterm controller Skill | GitHub交付、手机短指引、主控／Pro／Worker边界 |

`unread_required=[]`，`unavailable_required=[]`。本轮没有把“主控取得文件”冒充其他角色已经阅读；首项 Professional Binding 的 `reuse_evidence` 均为 `null`，目标角色须按新上下文实际读取。

<a id="completed-scope"></a>
## 10. 本次 M-START 已完成范围

- 独立核了完整目标、旧成果适用性、正常业务关系、主要证据资格和全部重要剩余；
- 完成当前采用／不采用／保全裁定；
- 建立本 Run 的 README、地图、任务、Binding 和 Intake；
- 签发首项专业工作及 RESULT／CHANGE／EFFORT 触发；
- 给出 Owner 事项、投入预测、持续管理责任和准确后继；
- 未虚报 Reader、发送、Professional 执行、专业结果、独立审查或管理 Gate。

<a id="remaining-management"></a>
## 11. 持续管理责任

本次 M-START 调用已完整提交，但 BI-01 全目标仍 ACTIVE。后续管理责任由正式 Binding 承接：

- 首个可消费循环形成时执行 M-REASSESS；
- 承重输入／方法发生重大变化时裁定受影响范围；
- 每两次有效 Professional 调用进行持续投入复看；
- exact 专业候选形成后决定管理接收、必要独立审查、下一专业任务和 Owner Pack；
- 完整阶段成熟时执行 M-CLOSE。

<a id="handoff"></a>
## 12. 准确接续

主控下一步：

1. 以本决定、Run README、推进地图、当前任务、Workmap Binding 和 Intake 为同一采用集；
2. 不把管理签发写成已发送；
3. 先完成 Workmap 独立 Reader 记录并运行 dispatch preflight；Reader 必须独立于本轮地图／任务构建者；
4. preflight 通过后，以 `01_当前任务.md` 全文为 `current_task_ref`、本决定为 `task_adoption_ref`，按现行 GitHub 完整派发／手机短指引流程向 `chatgpt:BI-01-CO-04:professional` 实际发送；
5. 保留首个 RESULT、重大 CHANGE 和持续 EFFORT 三类管理责任；不因专业 CONTINUE 丢失管理复看；
6. 若 Reader／preflight 发现机械缺件，只定向修复；不得重做已成管理判断或由主控改写业务任务。
