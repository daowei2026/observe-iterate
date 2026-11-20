# 长程任务通用协作协议 · V2（首版）

> 本协议只规范跨角色**运行机制**。`observe-iterate` 中已采用的 Workflow 与具体专业 Skill 定义业务工作，长程协议不取代其专业方法或完成条件。当前 V2 是可做离线机械核验的候选合同，未经真实主控通道/状态/权限联调，不可宣称已具备自主长期运行能力。

## 1. 角色与责任不可混淆

- **Owner**：提供当前业务目标、对象和**已经明确的**范围/约束（统一归入 `BusinessTaskInput`）、真实 GO 和具体操作权限。分析深度/完成边界有未知项时允许在授权范围内先做有界调查；但未经合法确定不得扩范围、开展超授权动作或宣布整项完成。真正业务取舍与新授权仍返回 Owner。
- **主控 Codex**：持有**可信** Run 事实账本和物理聊天/线程映射；送达、监控、回交、去重/对账、按规则调用确定性检查；不决定专业业务正确性、不根据结果措辞擅自扩展任务。
- **多层 Workflow 运行协调 Chat（V2 `manager`）**：维护整个任务的当前状态与版本依赖，按已采用 Workflow 调用、等待、接续或回流 Skill 工作，按需安排多个执行 Chat。不增加业务预期、专业方法、执行约束、Worker 结果处理规则或额外专业 Gate。见 [运行协调 Chat 指南](../professional/PRO_MANAGER_GUIDE.md)。
- **Skill executor（V2 `executor`）**：不预设固定专业职位或唯一产品；按正式 D 所指 Skill 原件完成专业工作与内部流程。A～D 默认 ChatGPT、E 默认 Codex 独立线程；实际以 Owner GO、采用版本和 RUN_BINDING 为准。Codex 直接 E 在授权范围内连续运行并专业回交，通常零 W。见 [Skill 执行 Chat 指南](../professional/PRO_EXECUTOR_GUIDE.md)。
- **Worker Codex**：按 W 中明确的已授权操作和现场执行，交付事实、未完成项和证据；不替代 Skill 执行 Chat 的专业判断。

本版保留需要 Worker 时的 `manager→executor→worker` 路径，增加 E 的 `manager→Codex executor（零 W）→manager` 路径，不新增代理层级。每 Run 可按需绑定多个 `executor`，但各自的任务、版本、Worker 结果和实际聊天身份不能混淆；Worker 回原签发 `executor`，不能绕过对应 Skill 执行 Chat。

## 2. 身份：不能用业务阶段代替运行实体

`work_id` 是跨 Run 目标，`run_id` 是一次真实 GO 的执行，`call_id`（C0001…）是该 Run 实际发送的一次专业模型调用（可发送给 ChatGPT 或 Codex executor）；`delegation_id`（D001…）是 manager 签发的专业子任务；`work_order_id`（W001…）是 executor 签发的 Worker 操作工单。`call_id` 不给“准备的提示词”、未真实送达的消息占号。

`parent_task_id / question_id / stage_view / control_nodes / work_item_id / material_requirement_id / analysis_round_id / expectation_version` 属于业务控制面独立身份，不与 C/D/W 编号互换。一个 C 可以覆盖多个业务节点；一个 D 可无 W 或有多张 W。所有 D/W 有独立身份和原发行调用关联。

`RUN_BINDING.json` 需保存稳定逻辑身份（本 Run 唯一 manager、列出 executor；无 Worker 的 Run 允许 workers=[]），不可把逻辑名当物理 ChatGPT 聊天或 Codex thread。真正聊天 ID、当前运行工作区、操作分支和实际权限只能由主控从授权配置/真实设施核实并独立保存。

## 3. 只承认正式 GO、合法委派和真实 Return

完整先后关系：

```text
Owner GO → RUN_BINDING
→ C(manager): INVOCATION → （可选多张 D 先发布）→ MANAGER_RETURN 引用 D
→ 主控核发送与实际 manager receipt → 派发 D 给 executor（新 C）
→ C(executor): INVOCATION → 直接专业结果，或（先发布 W）EXECUTOR_RETURN 引用 W
→ 有 Worker 时：核实际 executor receipt、派 W、回收 Worker Return、回原 executor 消费
→ Codex 直接 E 时：首个 C 发送前核 Owner/D 操作授权、该 Run 专属线程、实际工作区和资源单写者；Codex 连续执行 E1～E6、通常零 W
→ executor 发布 EXECUTOR_RETURN（有 W 可接续，零 W 可直接提交本 D）
→ 主控将 D 完成/部分/阻断的专业回交交原 manager（新 C）
→ manager 消费后决定后继 / 请求 Owner / 申请任务收束
```

Skill 执行 Chat **零 W**时可直接提交 D 结果；有多 W 时按对应 Skill 与 V2 回执关系接续。不能把“某 Worker 工单完成”当作 D 已专业接受，也不能把“某 D 完成”当作 L0 父任务已完成。

**Git 版本引用无循环约束**：先发布 D，再发布引用 D 的 manager return；先发布 W，再发布引用 W 的 executor return；D/W 只记录 `issuer_call_id`，不倒向引用尚不存在的 return commit。GitHub 正式跨端来源统一用 `owner/repo@40位commit:path`；不得依赖 moving branch、文件标题或 chat 摘要代替原件。

## 4. V2 正式对象

```text
longrun/runs/<run_id>/
  OWNER_START.md
  RUN_BINDING.json
  calls/C0001/INVOCATION.json
  calls/C0001/FULL_ASSIGNMENT.md       # 仅确需存副本，或者引用精确远端原文
  calls/C0001/PRO_RETURN.json
  delegations/D001/DELEGATION.md
  delegations/D001/DELEGATION.json
  work_orders/W001/ORDER.md
  work_orders/W001/ORDER.json
  worker_results/W001/WORKER_RETURN.json
  ... 已发生的真实材料/事实
```

所有材料按实际执行逐步产生；测试 fixture 不写入 `runs/`。`pro_return` 同时适用于 manager/executor，但 `role`、`sender`、`delegation_ref`、`return_to`、`issued_delegation_refs`、`issued_order_refs` 明确不同。`WORKER_RETURN` 必须回到签发 W 的 executor。专业报告与受机器校验的 Return 分离；某段报告中的自然语言不能代替正式身份引用和发送回执。

## 5. GO、授权、现场与审计

Owner 的 `grants` 必须精确包含 `operation`、`execution_context`、`allowed_writes` 和从 Owner 真正授权原文逐字取得的 `authority_quote`；D/W 机读权限必须属于真实授权范围，不能扩权。Worker W 的操作、现场和写面须通过 Owner grant 与 D/W 的既有机械授权校验。**这是主控的运行权限验证，不是运行协调 Chat 自拟的专业执行约束。**读者应核对现场实际路径/仓库/分支，而不是把字符串相等当成操作沙箱。

**Codex executor 直接操作前检**：没有 W 时不得绕过 Worker 原有的执行安全边界。在正式向 Codex executor 发送 C 前，主控必须核原 manager 所签 D、Owner grants 与 D 允许操作/写面、该 Run 的真实 Linux cwd/realpath、专属 threadId、模型/强度和共享资源单写者，并用 `validate-executor-execution` 对当前直接操作范围做有界验证。此门禁是来源/权限核验，不是专业运行成功证明；程序不发送、不取得真实锁，不能相信任意模型自己提交的 `true` 值。

主控须在派 W 前独立验证实际工作区单写者；校验脚本返回 `PASS` 不等于自动获得锁、真正发出消息、实际 Run 成功或 Git 仓库写权限。

跨角色消息发送用主控可信行动身份及唯一 `call_id / invocation_token`；物理收件人和消息内容哈希由真实发送端回执核验。`RETURN` 自己的声明不构成送达证明；重复收到相同已确认回交是幂等消费，版本冲突或未知来源应阻断/核实。

敏感凭据、手机通信日志、私有数据不应因方便追溯写入公开仓库。可发布的是允许公开的精确引用、摘要和受限业务文本。

## 6. 可持久的动作事实与恢复

动作按 `run_id/C0001`、`run_id/D001`、`run_id/W001` 独立建账（不同类型 ID 不能交叉复用）；建议由主控按时间保持：

```text
NOT_SENT → IN_FLIGHT → COMPLETED
           ↘ UNKNOWN（先查物理回执与原结果）
NOT_SENT / IN_FLIGHT / UNKNOWN → BLOCKED（需要明确恢复条件）
BLOCKED → COMPLETED（只在原动作证据已查清时）
允许显式 SUPERSEDED，但需保留原动作及授权来源
```

`NOT_SENT` 必须有新动作已登记的可信证据，不得从没有记录推断。任何 `UNKNOWN` 先核对物理通道、原消息、运行现场和远端产物，禁止猜测重派。一次机器校验退出 0 不能代替“发送前原子占位 + 实际发送 + 真实回执 + 持久化”的协调机制。

主控恢复需重建：Owner GO 有效性、采用的 Binding、物理端映射、每次调用和 D/W 的已验证状态、工作区占用、剩余专业责任、等待事项和触发/恢复条件。不能从 GitHub 文件是否存在推导实际消息已成功送达。

## 7. 结果消费、局部阻断及最终收束

- **Worker Return**：`EXECUTED / PARTIAL / STOP / FAILED` 是操作端的既有机器状态；真实结果必须返回原 `executor`，其**专业消费完全按被执行的 Skill**。本协议不增设 Worker 返回后的专业处理步骤。
- **Executor Return**：Codex 直接 E 可零 W 使用同一 `longrun-professional-return/v2`，设置 `role=executor`、`sender=codex:<run_id>:executor:<id>`、`issued_order_refs=[]`、`accepted_worker_refs=[]`；按对应 Skill 的原生输出表达本 D 实际专业结果，并通过 V2 回交引用；`REPORTED_COMPLETE` 是 D 的机器回交状态，不直接等同于 Skill 专业完成或父任务完成。
- **Manager Return**：登记已核实的 Skill 工作回交、当前 Workflow 状态、下一项 D/续作或具名 Owner 问题；依据**原 Skill 的专业结果、既定 Workflow 和 Owner 明确的任务边界**判断是否还有后继。运行协调 Chat 不代替 Skill 提供独立业务验收，也不能单凭 Return 标记宣布父任务完成。
- 某 D/W 因确切缺前置而受阻，只阻断依赖它的工作；已满足独立前置的其他委派可继续。确认没有合法后继时可有据停止，但“停止”不等于“成功完成”。

## 8. 与控制面、Skill 和确定性程序的接口

实际采用的 Workflow 与 Skill 规定业务节点、条件及专业结果。运行协调 Chat 只根据**已采用**的阶段输入输出和真实返回安排后继，不新增另一套专业 Gate；专业状态（如 `DATA_READY`、`COUNTERS`、`PROVEN_UNAVAILABLE`）不翻译成机械 `PASS/FAIL`。合理性分析仍以其后续实际采用的版本为准。

确定性程序只能在**明确、可追溯的行动选择规则或专业决定**允许后调用；脚本维护事实并回交输出，不决定专业争议。何时启动某种专业分析、是否需标定和能否有界收束，不属于主控自由判断。

## 9. 多层 Workflow 运行协调与整体状态

本版只采用**多层 Workflow 运行协调 Chat + 按需多个 Skill 执行 Chat**的职责分工：

- 协调 Chat 持有 Owner 已明确的任务输入、已采用的 Workflow、Skill 及其真实成果引用；沿既定依赖调用下一 Skill、接续原工作或按已规定的返回路径处理，不自行补充专业任务内容。
- Skill executor（ChatGPT 或 Codex）负责其 Skill 的专业分析、内部流程、原生输出、完成判断及该 Skill 规定的 Worker 使用与结果处理；专业工作允许多次 C 接续同一 D。
- 协调 Chat 不承担默认独立专业 Gate，只核对任务/输入版本、真实工作状态及既定后继使用资格；必要的专业判断仍由 Skill 执行 Chat 完成，未定义的 Owner 业务取舍须明确提出。
- 运行协调 Chat 依 [TASK_PROGRESS](../templates/TASK_PROGRESS.md) 持续维护整体任务及工作项、执行 Chat、版本/依赖、在途与恢复状态。它由真实工作产物和可信消息/工单事实派生，不是另一份独立权威账本。
- 运行记录中使用现有 `business_control/TASK_PROGRESS.md` 与必要的具名接续引用；普通推进不要求额外创建 `MANAGEMENT_DECISION`、Gate 决定或新的机器字段。主控负责保存、回读与真实权限核验；它不能代替任何 Chat 编写专业结论。
- Owner 的操作授权与工作区、模型、身份、消息送达和 W 工单校验继续依本协议与真实 GO 执行，不因取消独立专业 Gate 而放宽。

## 10. V2 机械程序的真实能力

`longrun/tools/longrun_gate.py` 是只读校验/路由建议程序；它**不是**远端消息通道、GitHub 仓库读取器、持久动作账本、锁管理器、自动控制面和完整专业任务引擎。使用时需把真实 GO 文本、合法 Binding、D、W、Pro/Worker Return 和独立验实回执作为可信快照输入。模型自述的 `true` 或假造的 snapshot 不能当可信外部事实。实际发送、状态写入、强制独占和跨仓 Skill 更新仍需在后续联调完成。

## 11. 多 Run 采用接口（在本 Run 已有 V2 语义之上增量扩展）

当主控同时管理多个 Run 时，采用 [MULTI_RUN_CONTROLLER](MULTI_RUN_CONTROLLER.md)。C/D/W 仍独立按各自 run_id 的 V2 合同验证；同名 C0001/D001/W001 在不同 Run 可同时存在。主控在发送/回收前必须先选定正确的单 Run Binding 与真实物理回执，不将其他 Run 的完成、Gate、Owner grants 或资源资格借用到当前 Run。

首版每个 run_id 的 Linux 工作区由 Owner 在准备真实 GO 时先行准备并给出绝对路径；不同 Run 必须不同工作区，须实际核 realpath 以及路径不重叠。不得让主控临时建立工作区或用旧 BASE 默认路径替代。共享 Git 分支/数据库等写面仍按现有授权和实际单写者要求核实，必要时仅阻断对应动作。Run 采用的业务/专业来源版本独立锁定，不随其他 Run 或公共 Skill 修改自动改变。

本仓的多 Run 文件/只读检查程序尚未接线到仍在使用的 cgpterm 主控 Skill；文档发布不等于主控已支持并行物理派发。
