# BI-01-CO-04 R0006｜首轮 Professional 接收与最小输入恢复安排

- `work_id`: `BI-01`
- `run_id`: `BI-01-CO-04`
- `invocation_id`: `BI01-CO-04-R0006-PROFESSIONAL-INTAKE-6fd91174`
- `assignment_token`: `43645083c9663b83a73077ab4c48cb4815b3221177edc89b`
- `role`: `management`
- `recipient`: `chatgpt:BI-01-CO-04:management`
- `decision`: `ACCEPT_LIMITED_INPUT_QUALIFICATION_AND_ISSUE_MINIMUM_TECHNICAL_RECOVERY`
- `professional_result`: `INPUT_UNQUALIFIED_FOR_ASOF_COMPARISON`
- `current_task`: `BI-01-CO-04-CASE-INITIAL-ASOF`
- `current_task_status`: `ACTIVE_SAME_QUESTION_PENDING_INPUT_RECOVERY`

<a id="decision-summary"></a>
## 1. 管理决定

管理接收 R0005 Professional 的首轮实质回交，但只接收其证据实际支持的范围：

> 当前执行通道没有取得能够重建截至 T 可知状态的正式行情、特征对象、实际／确认时间及运行身份字节，因此本批输入不具备进行 as-of 多品种比较的资格。

该结论是合格的**输入资格否定**，不是市场 `NO_CANDIDATE`，不是“中尺度没有选择增量”，也不是现有业务设想已经失败。R0005 正确地没有选取事后好看的 T、没有倒填未来确认、没有给 rb／hc／i 排名，并把历史定位事实、正式证据、视觉线索和未知分开。

当前业务问题和 `01_当前任务.md` 保持不变，不另签第二个业务问题，不要求 Professional 在没有输入时空转第二轮。管理据此签发一次窄范围技术取件工单 `BI01CO04-INPUT-RECOVERY-01`，只恢复原任务所需的最小不可变数据包；包到位并经技术接收后，原 Professional 继续同一问题。

本轮不签收首个 as-of 业务循环，不启动独立专业审查，不宣称任何候选、反例或方法有效性已经形成。

<a id="professional-evidence"></a>
## 2. R0005 回交真实性与一致性

管理核对：

- Professional invocation：`BI01-CO-04-R0005-PROFESSIONAL-678c6b83`
- assignment token：`0649d81fca1b11b13103f0a0202e943936b6edb65cd173ff`
- recipient：`chatgpt:BI-01-CO-04:professional`
- `SEND_RECEIPT.state`: `COMMITTED`
- 报告：`28a915f9b6a7bb8f69651a7954028b02c3244684:runs/BI-01-CO-04/artifacts/R0005/REPORT.md`
- 证据索引：`705d97e922c15eb28b0a28a7f8895df0eff449d4:runs/BI-01-CO-04/artifacts/R0005/EVIDENCE_INDEX.md`
- 输入资格：`705d97e922c15eb28b0a28a7f8895df0eff449d4:runs/BI-01-CO-04/artifacts/R0005/INPUT_QUALIFICATION.json`
- Question Work Return：`d5d0cbf9dfcc49a0711b76f9190e36f576c43fb1:runs/BI-01-CO-04/provenance/turns/R0005/QUESTION_WORK_RETURN.json`
- Role Return：`b2b31f4bb1d99d18178bfa49890e28cf57c54890:runs/BI-01-CO-04/provenance/turns/R0005/ROLE_RETURN.json`

报告、输入资格 JSON 与两份 Return 对以下事实一致：`asof_t=null`、`candidate_ranking=null`、`market_no_candidate_claim=false`、三个管理触发均 `NOT_YET`、完整任务仍 ACTIVE、R0005 为第一次有效 Professional 调用。当前分支只有上述输入资格实物，没有本 Case 正式行情／特征数据包；这只证明仓库当前未交付，不证明源环境不存在。

<a id="accepted-scope"></a>
## 3. 接收、保全与不接收

### 3.1 接收

1. 接收 `INPUT_UNQUALIFIED_FOR_ASOF_COMPARISON` 为本批准确专业结论；
2. 接收 `T=NOT_SELECTED`，因为无法构造 T 时真实可知集合；
3. 接收历史工具实践仅提供 run、品种、频率、窗口、页面、源目录和参数文件名等定位事实；
4. 接收正式运行身份、参数消费证明、K 线切片、特征对象切片、确认时间语义、日历／时区和不可变哈希为承重缺件；
5. 接收“缺输入”与“市场无信号／无候选”必须分账；
6. 接收同一业务问题在最小数据包到位后继续，而不是重做来源阅读或改成全市场普查。

### 3.2 保全

- “大尺度找背景、中尺度看差异、小尺度按需补充”继续保留为待实践假设；
- rb／hc／i、30m、2021-08-15 至 2021-09-30 和历史 run 只保留为低成本恢复入口，不升级为默认方法；
- R0001 的完整任务、证据等级、RESULT／CHANGE／EFFORT 触发和 1—2 次 Professional 调用预测继续有效；
- R0005 已完成的输入边界核验不在后续重复。

### 3.3 不接收

- 不接收市场 `NO_CANDIDATE`、任何品种排序或未来过程判断；
- 不接收中尺度有／无独立增量或当前工作设想成功／失败；
- 不接收页面、文件名或历史说明等同于本 Run 正式数据；
- 不接收图能打开、数据到位或 Worker 完成等同于业务循环完成；
- 不接收扩大到全市场重算、全仓审计、通用 Agent 建设或参数寻优。

<a id="business-diagnosis"></a>
## 4. 当前业务诊断

当前阻断发生在“来源定位”到“可执行 as-of 对象”之间，是一次具体的数据运输／实例资格缺口，而不是业务问题本身被推翻：

| 必要环节 | R0005 已有 | 当前缺口 | 对业务判断的影响 |
|---|---|---|---|
| 运行身份 | 历史 run 名、目录和页面定位 | manifest、文件索引、版本、真实消费配置、哈希 | 不能证明观察的是同一正式实例 |
| 行情 | 品种、30m 与窗口说明 | rb／hc／i 正式 K 线字节、时区／交易日历、覆盖与缺失状态 | 不能定义比较窗口和后续过程 |
| 特征对象 | 大／中／小尺度语义说明 | 大／中对象真实行、方向、对象身份、revision、状态 | 不能比较背景与差异 |
| as-of 时间 | actual／confirm 概念说明 | `x/y`、`xConfirm/yConfirm`、`event_ts` 实值和边界映射 | 不能构造 T 时可知集合 |
| 挑战与反例 | 任务要求明确 | T 后确认、反向对象或相邻失败区间的真实字节 | 不能检验主判断 |
| 图面 | 历史页面 locator | 与正式 run 对应的可读静态导出 | 不能视觉复核；但图不能替代结构化数据 |

因此下一步应恢复最小实例，而非让 Professional 继续文字分析。若源环境中的正式字节确实不存在，Worker 必须返回可复现的具体缺口；届时管理再决定是否做同配置窄范围重生或更换低成本入口。

<a id="recovery-arrangement"></a>
## 5. 已签发最小技术恢复

正式工单：`runs/BI-01-CO-04/reviews/management-R0006/WORKER_ORDER.md`

- `order_id`: `BI01CO04-INPUT-RECOVERY-01`
- `recipient_thread_id`: `01a17dd7-5033-7e63-b7a2-edd90b691c33`
- `workspace`: `/dwdhome/fy/cgpterm`
- `return_to`: `chatgpt:BI-01-CO-04:management`
- `scope`: 只读定位、最小切片复制／必要时同配置窄范围重生、不可变 receipt；不作业务判断。

### 5.1 P0 必须取得

1. 正式 run／board／文件索引或等价 manifest，含 run、core／build／版本、源根、品种、频率、窗口和每个文件 SHA-256；
2. 实际参数字节及该 run 的消费证明，不只文件名或文档默认值；
3. rb／hc／i 的 30m 正式 K 线切片，覆盖实际 warm-up、完整观察窗口及可检验最近挑战所需范围；
4. rb／hc／i 的大尺度和中尺度正式对象行；小尺度仅在恢复后 Professional 证明需要时补；
5. 每个对象至少含 scale、symbol、object id、direction、actual time／位置、confirm／known time、event timestamp、revision／status 和源键；
6. 字段词典、方向／zig 映射、确认与 revision 语义、交易日历、时区、UTI／event_ts 边界；
7. 行数、首末业务时间、缺失／计算失败／真实无信号状态及生成／复制来源；
8. `PACKAGE_RECEIPT.json`，逐文件记录 path、sha256、bytes、rows、first／last business time、generated_at、tool／version、copied／regenerated。

### 5.2 P1 辅助但不替代 P0

取得节点 6153 或同一 run 的静态 PNG／PDF／HTML 导出及对应证明，用于视觉核对和 Owner 阅读。若结构化 P0 完整而页面无法导出，不因此阻断 Professional 先做 as-of 重建；必须如实记录图面限制。

### 5.3 恢复边界

优先复制正式既有字节。若正式切片不存在但 exact 代码／配置／数据源均可核，可只对 rb／hc／i 和该窗口做一次同配置窄范围重生，并把 copied 与 regenerated 严格分开；不得调参数追结果、不得全市场重算、不得改业务算法。无法满足 exact 重生条件时，交 `BLOCKER_REPORT.md`，不静默制造替代数据。

<a id="trigger-assessment"></a>
## 6. 触发与投入裁定

| 触发 | 本轮状态 | 理由 |
|---|---|---|
| `FIRST_USABLE_ASOF_LOOP` | `NOT_YET` | 没有合格 T、候选／无候选、后续挑战及方法反馈闭环 |
| `MATERIAL_INPUT_OR_METHOD_CHANGE` | `NOT_YET` | 发现的是缺失实例字节；没有证据推翻输入语义或业务问题 |
| `ACTIVE_WORK_EFFORT_REVIEW` | `NOT_YET` | 当前累计 1 次有效 Professional 调用，阈值为 2 |

R0005 计入 `known_pro_turns=1`。Worker 调用不计入 Professional 调用预算。恢复包被管理技术接收后，再发原 Professional 的第二次同工作 continuation；若第二次有效调用仍无业务主体，必须触发 EFFORT 复看并改变实际安排，不能继续来源循环。

<a id="independent-review"></a>
## 7. 独立专业审查裁定

当前不签独立专业审查。没有市场候选、as-of 判断或方法增量可供复做；此时审查只能重复确认缺文件。待首个承重业务结论形成后，再按影响决定是否签具名独立审查。

<a id="completed-scope"></a>
## 8. 本轮完成范围

- 核 R0005 Professional 的真实身份、发送、报告、证据索引、输入资格 JSON 和两份 Return；
- 接收输入资格否定，拒绝把它升级为市场无候选或方法失败；
- 恢复完整业务链并定位唯一当前瓶颈为正式实例数据运输；
- 保持原业务问题和任务 ACTIVE，不另开业务路线；
- 签发一次管理 Worker 最小恢复工单，明确 P0／P1、不可变 receipt、窄范围重生和禁止事项；
- 记录 `known_pro_turns=1`，裁定三个触发均 `NOT_YET`；
- 决定包到位前不消耗第二次 Professional 调用，当前不做独立专业审查；
- 未虚报 Worker 已发送／执行、数据已恢复、Professional 已继续或业务循环已完成。

<a id="remaining-scope"></a>
## 9. 全部重要剩余

1. 主控尚需对已签 `WORKER_ORDER.md` 运行 Worker-order preflight，并向 Owner 指定线程实际发送；
2. Worker 尚需交 P0 数据包、receipt、完整技术报告或准确 blocker；
3. 管理尚需只按技术合同接收 Worker 结果，不作市场判断；
4. 原 Professional 尚需在合格数据包上继续同一问题，选首个合法 T，定义前瞻过程，给候选／排序／市场无候选及最近挑战；
5. 首个业务循环尚需管理接收，必要时签独立专业审查；
6. 后续相邻 Case、Owner 首版、真实反馈、方法边界和完整阶段收拢仍未完成。

完整 BI-01 工作保持 ACTIVE。当前不是等待 Owner 普通细节，而是执行已经明确的最小技术恢复。

<a id="material-use"></a>
## 10. 材料使用记录

本轮实际读取并用于裁定：

- R0006 `FULL_ASSIGNMENT.md`、`DISPATCH.json`、`INVOCATION.json`、实际 `SEND_RECEIPT.json`；
- R0005 `REPORT.md`、`EVIDENCE_INDEX.md`、`INPUT_QUALIFICATION.json`、两份 Return、`INVOCATION.json`、`SEND_RECEIPT.json`；
- 当前 `WORKMAP_INTAKE_CURRENT.json`、`ADOPTION_STATUS.md`、Run README、长程地图和 Workmap Binding；
- Owner GO 的 Worker thread／workspace 授权；
- `CASE_OBSERVATION_RUN_GUIDE.md` 的原签发者消费、真实输入与多轮接续边界；
- `DR10_PRO_IMPLEMENTATION_AND_CODEX_ORDERS.md` 的 Pro／Worker 分工；
- `workmap_gate.py` 的 Worker-order authority、路径、身份与 send receipt 校验规则；
- 当前分支树对本 Run artifacts 的独立核对。

`unread_required=[]`。`unavailable_required` 为 R0005 已列的本地正式数据包、内部页面和源目录；这些正是本轮 Worker 工单的目标，不被管理补猜。

<a id="handoff"></a>
## 11. 准确接续

主控下一步：

1. 读取本决定与 `reviews/management-R0006/WORKER_ORDER.md`；
2. 对该 exact 工单运行 Worker-order preflight；
3. 通过后向 `threadId=01a17dd7-5033-7e63-b7a2-edd90b691c33` 实际发送，核 workspace 为 `/dwdhome/fy/cgpterm`；若不符，按 Owner GO 只修真实派工通道；
4. Worker 结果回 `chatgpt:BI-01-CO-04:management`，不直接升级为业务接收；
5. 管理确认 P0 包和 receipt 后，按 `EXISTING_AUTHORIZED_REPAIR`／same-work 方式把原任务续发给 `chatgpt:BI-01-CO-04:professional`，不再做 Reader；
6. Professional 第二次有效调用形成首个可消费循环或触发 EFFORT／CHANGE 时，再回本管理聊天 M-REASSESS。

本轮结束于“R0005 已限域接收、恢复工单已签发”；Worker 实际发送、数据恢复和后续业务结果均须由独立真实记录证明。
