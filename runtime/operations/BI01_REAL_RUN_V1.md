# BI-01 下一次真实长程：启动、轮次、地图、管理接收和恢复

**状态：PREPARED_NOT_STARTED / NO_SEND。** Owner 2026-10-15 已停止旧试跑，明确新任务要在运行机制验证符合预期后**重新真实开始**。本次工程提交不是开始授权。旧 I4 所有回交（含刚才试跑第四段）、G3 认定、旧管理聊天和 local long-task 状态均不继承；Git 保留其历史是审计，不是活动业务成果。

## 0. 唯一运行根、正本与职责

- 生效机制来源：daowei2026/observe-iterate 的**本次实际锁定完整 40 位 commit**，运行时检查本分支最新身份；不要复用过往 prompt 的 76f053... 或旧 CYF Release。
- 操作端：cgpterm 个人分支的 observation-iteration-longrun-controller + 通用 ChatGPT Terminal、long-task-status Skills，工具接口在现场动态核实；本地 detached HEAD 不能证明目标 Skill 已安装，须按锁定 Git 文件确实加载。主控不直接操作手机；手机语义 episode 均为新的零继承执行者。
- 新 run **唯一工作面**：`runs/BI-01-RESTART-01/`。不能再向旧 `complex-systems-vocabulary/.../observation-iteration-runs/BI-01-IT-01/` 写新的活动 CURRENT/PROGRESS/ROUTES/returns。
- 专业方法只取本仓 `professional/source/00—07` 和下一次有权任务。旧 I4 四段不得作为此次 I4 已成结果或观察证据；旧 I1–I3 的设计原文仍可按真实来源重新核，G1–G3 资格必须由新管理 Pro 按本次数据事实重新认定，不预填通过。

## 1. 首轮 M-START：可以先管理，不可以先造地图

1. 等 Owner 下一次明确授权开始；本仓协调器保持固定 `work_id=BI-01`，但必须为 `run_id=BI-01-RESTART-01` 另建**全新 task/root、invocation/token/marker/聊天身份及本地账本**，不 resume 旧 `bi01-i4-rerun-20261013-01`，也不继承其历史投入与已完成状态。项目里创建新的管理 Pro 角色聊天（此次 Owner 放弃旧聊天续跑），新建/命名及身份恢复按 cgpterm 通用 Skill。记录项目、唯一物理聊天身份、唯一标题、首轮 marker；无可靠 chat 定位不得发送，不能仅凭相似标题/预览定位。
2. 将下一次 Owner 的**真实启动原文**先作为本 run 的 OWNER_START.md 保存入 Git，记录真实消息来源与授权（本次准备消息不算开工）；首次管理 BOOTSTRAP 的 current_task_ref 和 task_adoption_ref 可以都指向这个真实 Owner 启动原文，而不是不存在的管理地图。随后从最新实际 Source 和 Owner 启动消息编制有据 `question-work/v2 BOOTSTRAP`，用 `Overlay08/12` 的 M-START 准备和核验**整条精确载荷**，传输状态为未发送才可投递。首次管理**不要求预先存在**地图/正式专业 Binding；也不得为了过 gate 由操作端捏造已批准地图。
3. 管理 Pro 先核 I1–I3 实际可用材料/参考与正式差异及 G3 范围，再判断本轮 I4 合法工作，形成真管理决策、完整目标/未完、条件性预算、复看和完整首份专业任务。**由管理 Pro**在新 run 写并签发 `00_长程推进地图.md`、`01_当前任务.md`、`reviews/management-Rnnnn/` 与 `QUESTION_WORK_BINDING`；有缺项时继续原管理责任，不自行填业务结论。
4. 只有上述事实提交到实际有权 Git 分支、完整 Return 已收到并验证、远端回读成立后，才能将 `runtime/config/WORKMAP_BINDING.json` 从 NOT_CONFIGURED 采用为此 run 的实际 map/task/管理接收正本，并用已有 `workmap_gate.py` 建立真实 intake 与检查。候选状态字段本身不给合法授权；无正式接收不得派首轮专业执行。
5. Worker 只有执行 Pro 实际签发有权技术工单后才激活，绝不从 CYF A/B/C 预建工程角色或继承其 Release。

## 2. 每个 Pro 角色调用都要在 GitHub 留下 R 轮

真实管理／执行／审查 Pro 调用依次记 `R0001/R0002/...`，不是手机 Episode、local long-task step、git commit 或专业阶段 I1–I6。旧四段不能倒灌为新轮。具体字段按 [轮次交付合同](ROUND_RECORD_CONTRACT.md)。

每轮：先由 Overlay12 `prepare` 生成真实最终载荷，它的**第一行就是 `[invocation_id]`**，也是 cgpterm 通用调度器唯一 `--round-marker`。把这份未经改写的 UTF-8 字节作为 `provenance/turns/Rnnnn/PROMPT.md`，保存对应 `INVOCATION.json`，先提交 Git 并从远端回读；**该预发送提交**应作为 scheduler 本轮 GitHub 远端完成检查的 `base SHA`。然后在这个已提交版本上运行 `runtime/tools/bi01_run_gate.py pre-dispatch` 和 Overlay12 `verify`，核完整载荷、首行、recipient、合法 role/Binding 与真实未发送状态；通过才允许手机发送。PASS 和提交均不等于已发送。发送结果、完整回复、真实 Return、附件实际收取、GitHub 结果分别记录，不合并成一个“已完成”。未拿到真实 Return 不得猜下一段；未知 Send 效果绝不能重发。

专业 Pro 只交实际业务结果、自查和最新合法同工作 continuation，不修改共享图或签 G4；管理 Pro 在已触发的管理轮接收实物、更新地图和 `01_当前任务`、预算/触发、合法下一阶段及 Gate。`PROGRESS.md` 仅是操作端对 Owner 的阅读投影，**不得替代**管理地图/任务/接收。没有新业务事实的心跳不生成“业务轮”，但重要阻断须有实际操作回执。

## 3. 管理/复看何时介入

沿 DR13/14 有权已签 RESULT、CHANGE、EFFORT 义务，在真正业务里程碑、G3/G4 申请、重大反证、原计划失效/投入复看时回原管理 Pro。正常已授权同工作短续作不每轮重签；但 CONTINUE 不取消已签独立审查、管理复看或已有非阻塞工作。

管理实际将决定写回地图/任务/预算/接收/后继后，才能消费并标记管理责任 CONSUMED。新提交不表示管理 Pro 已看，执行 Pro 自称完成不表示 Gate 通过，独立审查方法仍 PARTIAL 时不能冒称独立 PASS。管理不在场时不能由操作端填结果。工作未完须有明确的合法下一步/等待来源/复看条件，不能只写“继续”。

## 4. 真实运行接线与失败恢复

- 本地 `long-task-status`、手机 scheduler、GitHub Pro 轮次/地图是三种不同状态源，须用真实 run/round marker 对齐；GitHub 无新提交不证明模型还在运行。
- cgpterm 的固定聊天 rename/唯一标题、两列表预检、准确 Wi-Fi、完整视觉 Copy、未知提交去重和有界等待按**已安装的通用 Skill**执行；不要强制列未暴露的历史 MCP 工具，生成中的静止 UI 不等于完整回复。
- GitHub 写入和证据须 remote fresh readback。手机回交看见链接不等于取得附件，Pro 声称写了文件不等于远端存在，脚本结构通过不等于专业正确。
- 活动 `WORKMAP_BINDING` 的字段与结果不能从旧仓复制来凑；签发后每次新专业任务要证明绑定/当前任务/recipient 和 Send 未提交状态。已有 `workmap_gate.py` 和 `question_work_check.py` 提供机械验证，**不会创建管理决定或调用手机**；新 run gate 只补真轮次和地图准入。
- 真实权限/输入/原件/聊天不可核时，仅保持相应分支 NO_SEND、具名报告恢复条件；不伪造结果、不绕过旧保护、不为补字段重跑已完成的业务。
- 源 `runtime/release/` 仍是 CYF 锁定副本，Overlay03–06 与 DR 旧 A/B/C 专业文本不是 BI-01 的运行入口，不能被默认引用成完整方法；不强制读取全部历史。

## 5. 下次实跑的可验收目标

应在 GitHub 直接读到：真实管理形成的 00 地图、01 当前任务、每次真实 Rnnnn 的原提示/完整答复/Return/发送依据、管理 review/资格/复看、实际 Workmap Binding 和 Owner PROGRESS。**本次提交只是为这些成果接线；没有启动业务、没有填成果、没有让自动接续引擎变成已部署。**

**模式覆盖说明**：固定 Dispatch 的 `work_id=BI-01` 支持 M-START/M-REASSESS/M-CLOSE 及 I1—I6 对应模式，允许实际管理 Pro 为前段补证、I4、I5/I6 签出可装配任务；这些只是配置中的合法显示名称，`professional_mode`、专业原文、角色写权和 Gate 仍完全来自本次真实管理任务与 Binding。工具可组装，不自动形成专业 Router 或正式独立审查方法。
