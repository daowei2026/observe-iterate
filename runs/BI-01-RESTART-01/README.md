# BI-01 / RESTART-01 — 管理窄修复已落库，正式派发现场核对暂停

**MANAGEMENT_R0001_RECEIVED / R0002_MANUAL_REPAIR_COMPLETE / WORKMAP_ADOPTED / PROFESSIONAL_NOT_SENT / NEEDS_HUMAN_PAUSED**。

R0001 已完成首次实质管理并形成地图、当前任务和 Question Work Binding；其原始回答、Return、提示、receipt 与管理包继续由 exact commit `46119a8e0030b4c3597634735cbe5d22ad3a0ac7` 保留。R0002 只修复 Owner 授权的机器接线缺项，不重新执行 M-START，不产生专业结果，不签 G4，也不表示 Overlay12 prepare/verify 已通过。

<a id="common"></a>
## 运行身份与历史隔离

- 唯一新运行空间为本目录；业务协调器固定 `work_id=BI-01`，但 `run_id=BI-01-RESTART-01`、新 invocation/token/marker、管理/执行 chat/thread 和 local long-task 身份均与旧试跑隔离。
- 旧业务仓 `complex-systems-vocabulary/.../observation-iteration-runs/BI-01-IT-01/` 仍是已停止试跑的历史，不继承为本 run 的业务成果、当前任务、Gate 或在途。
- R0001 原管理业务判断继续有效；R0002 只修接线。原物理管理会话是 `BI01-R01-管理`。
- 当前没有任何专业执行消息发送证据；不得从地图、任务、Binding、commit 或 intake 准备状态推出专业任务已发送。

<a id="bi01"></a>
## 当前生效管理面与实际恢复顺序

已形成并保留：

- `00_长程推进地图.md`：R0001 的完整业务关系、阶段与后继；R0002 仅同步当前操作位置。
- `01_当前任务.md`：I4 真实业务观察（含定向 I3 核查）；当前 `task_id` 为 `BI01-RESTART-01-I4-EXECUTION-01`。
- `bindings/QUESTION_WORK_BINDING_I4.json`：模式采用 `OBSERVATION_I4`；全部业务引用为 exact Git locator；管理路线回到 `BI01-R01-管理`。
- `reviews/MANAGEMENT_START_R0001.md`：原管理业务决定，不改写。
- `reviews/MANAGEMENT_DELIVERY_REPAIR_R0002.md`：本次窄修复决定和原件／修复件关系。
- `provenance/turns/R0001/`：原始 R0001 历史与明确修复旁路件。
- `provenance/turns/R0002/`：本次管理修复回交；不是专业轮次。

实际恢复位置与后续顺序：

1. R0002 修复包下载、验哈、按路径落库、提交、推送和远端读回已完成；
2. 修正版 task/binding/map/README 的 snapshot、fresh reader 与 intake 已完成，`dispatch.task_id` 严格等于 `BI01-RESTART-01-I4-EXECUTION-01`；
3. Candidate intake、reader、binding、dispatch 与真实发送现场 `NOT_SENT` 检查已在 exact input commit `e4ece3a9b31152a04c4fbf901be0d6e74ecb42b8` 全部通过；
4. Candidate 已按原管理角色给出的条件原样物化为 `ADOPTED` 的正式 `runtime/config/WORKMAP_BINDING.json`；
5. 正式 Binding 的 fresh reader 为 `READABLE`、mechanical intake 为 `PASS`；但 exact-commit 发送现场状态只能保持 `UNKNOWN`，正式 dispatch Gate 真实失败为 `DELIVERY_NOT_SENDABLE:UNKNOWN`；
6. 当前停在 `needs_human / paused`。恢复条件是先让 ChatGPT 的 Project/内部搜索路径回到可安全重复观察的状态，再对新的 exact commit 重做 snapshot、fresh reader/intake 和 protocol-clean `NOT_SENT` 核对；此前不得创建专业轮次或发送专业消息。

准确流程：[BI-01 真实运行合同](../../runtime/operations/BI01_REAL_RUN_V1.md)；[轮次合同](../../runtime/operations/ROUND_RECORD_CONTRACT.md)。
