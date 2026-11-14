# 长程任务通用协作协议 · V2（首版）

> 本协议只规范跨角色**运行机制**。`observe-iterate` 分支的 L0/L1/L2 控制面及两个专业 Skill 的业务判断仍保有自己的权威。当前 V2 是可做离线机械核验的候选合同，未经真实主控通道/状态/权限联调，不可宣称已具备自主长期运行能力。

## 1. 角色与责任不可混淆

- **Owner**：提供当前业务目标、对象和**已经明确的**范围/约束（统一归入 `BusinessTaskInput`）、真实 GO 和具体操作权限。分析深度/完成边界有未知项时允许在授权范围内先做有界调查；但未经合法确定不得扩范围、开展超授权动作或宣布整项完成。真正业务取舍与新授权仍返回 Owner。
- **主控 Codex**：持有**可信** Run 事实账本和物理聊天/线程映射；送达、监控、回交、去重/对账、按规则调用确定性检查；不决定专业业务正确性、不根据结果措辞擅自扩展任务。
- **专业负责人 Pro（manager）**：持续持有父业务任务专业责任；按当前问题/依赖安排具名专业 D，检查对应专业成果和被消费范围，形成继续、补证、限定交付、请求 Owner 等候选后继。专业操作见 [manager 候选指南](../professional/PRO_MANAGER_GUIDE.md)；正式业务 Gate/完成资格仍来自已获批准的控制规则，而非其自述。
- **专业执行人 Pro（executor）**：只在正式 D 授权范围内**依据仓库现有材料准备/合理性分析 Skill 实际开展专业工作**；可零 W 自行完成，也可按需要签 W 给 Worker；先专业审查 Worker 结果，再将原生业务成果、未决与适用范围交回原 manager。专业操作见 [executor 候选指南](../professional/PRO_EXECUTOR_GUIDE.md)。
- **Worker Codex**：按 W 中明确的已授权操作和现场执行，交付事实、未完成项和证据；不替代专业 Pro 判断。

本版**固定 manager→executor→worker** 两个委派层级，不支持通用任意深度代理树。多位 executor/worker 可绑定，主控不能为方便让一个 Worker 绕过原执行人直接“专业回交” manager。未来是否允许 manager 直接签 W 另行设计，不从旧版默认迁入。

## 2. 身份：不能用业务阶段代替运行实体

`work_id` 是跨 Run 目标，`run_id` 是一次真实 GO 的执行，`call_id`（C0001…）是该 Run 实际发送的一次专业模型调用；`delegation_id`（D001…）是 manager 签发的专业子任务；`work_order_id`（W001…）是 executor 签发的 Worker 操作工单。`call_id` 不给“准备的提示词”、未真实送达的消息占号。

`parent_task_id / question_id / stage_view / control_nodes / work_item_id / material_requirement_id / analysis_round_id / expectation_version` 属于业务控制面独立身份，不与 C/D/W 编号互换。一个 C 可以覆盖多个业务节点；一个 D 可无 W 或有多张 W。所有 D/W 有独立身份和原发行调用关联。

`RUN_BINDING.json` 需保存稳定逻辑身份（本 Run 唯一 manager、列出 executor/worker），不可把逻辑名当物理 ChatGPT 聊天或 Codex thread。真正聊天 ID、当前运行工作区、操作分支和实际权限只能由主控从授权配置/真实设施核实并独立保存。

## 3. 只承认正式 GO、合法委派和真实 Return

完整先后关系：

```text
Owner GO → RUN_BINDING
→ C(manager): INVOCATION → （可选多张 D 先发布）→ MANAGER_RETURN 引用 D
→ 主控核发送与实际 manager receipt → 派发 D 给 executor（新 C）
→ C(executor): INVOCATION → 直接专业结果，或（先发布 W）EXECUTOR_RETURN 引用 W
→ 主控核实际 executor receipt → 派 W 给 worker
→ W: Worker 执行 → WORKER_RETURN + 真实可复核产物
→ 主控核实际 Worker receipt → 回原 executor（新 C，触发源为该 Worker 结果）
→ executor 消费结果并发布 EXECUTOR_RETURN（可发新 W / 可最终提交本 D）
→ 主控将 D 完成/部分/阻断的专业回交交原 manager（新 C）
→ manager 消费后决定后继 / 请求 Owner / 申请任务收束
```

专业执行人**零 W**时可直接提交 D 结果；有多 W 时要按每张 W 的独立结果分别收束。不能把“某 Worker 工单完成”当作 D 已专业接受，也不能把“某 D 完成”当作 L0 父任务已完成。

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

Owner 的 `grants` 必须精确包含 `operation`、`execution_context`、`allowed_writes` 和从 Owner 真正授权原文逐字取得的 `authority_quote`；专业 D 可以再收窄 `permitted_operations`/`allowed_writes`，但不能扩权。Worker W 的操作、现场和写面须同时落在 Owner grant 和 D 限制内。读者应核对现场实际路径/仓库/分支，而不是把字符串相等当成操作沙箱。

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

- **Worker Return**：`EXECUTED / PARTIAL / STOP / FAILED` 只说明操作端结果；未交付项和真实证据必须列明；返回原 executor，由其决定专业接受。
- **Executor Return**：汇总当前 D 的专业结果/已验证 W、未解决问题、续作、请求上层；`REPORTED_COMPLETE` 只代表此 D 范围的专业报告完整，不代表父任务完成。
- **Manager Return**：汇总已接受的 D、自己完成的专业工作、后继 D/续作/Owner 请求，父任务完成资格由**本轮已经合法明确的完成范围与已确认 Gate**给出；禁止主控凭 Return 标志宣布。
- 某 D/W 因确切缺前置而受阻，只阻断依赖它的工作；已满足独立前置的其他委派可继续。确认没有合法后继时可有据停止，但“停止”不等于“成功完成”。

## 8. 与控制面、Skill 和确定性程序的接口

当前分支的 `control/` 与 `review/` 中 `H0/H1/H2/H3`、`G-*`、`Mxx/Rxx`、`AdditionalEvidenceRequest` 的规则由业务控制面维护。本协议不把 `DATA_READY`、`COUNTERS`、`PROVEN_UNAVAILABLE` 误译成机械“专业 PASS/FAIL”。

确定性程序只能在**明确、可追溯的行动选择规则或专业决定**允许后调用；脚本维护事实并回交输出，不决定专业争议。何时启动某种专业分析、是否需标定和能否有界收束，不属于主控自由判断。

## 9. V2 机械程序的真实能力

`longrun/tools/longrun_gate.py` 是只读校验/路由建议程序；它**不是**远端消息通道、GitHub 仓库读取器、持久动作账本、锁管理器、自动控制面和完整专业任务引擎。使用时需把真实 GO 文本、合法 Binding、D、W、Pro/Worker Return 和独立验实回执作为可信快照输入。模型自述的 `true` 或假造的 snapshot 不能当可信外部事实。实际发送、状态写入、强制独占和跨仓 Skill 更新仍需在后续联调完成。
