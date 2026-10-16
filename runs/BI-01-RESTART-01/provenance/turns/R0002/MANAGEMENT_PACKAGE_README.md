# BI01_RESTART_01_R0002_MANUAL_REPAIR_package

本包是 R0002 `OWNER_AUTHORIZED_MANUAL_REPAIR` 的窄修复交付，基于 `46119a8e0030b4c3597634735cbe5d22ad3a0ac7`。它不修改通用 Overlay12/runtime，不表示 Overlay12 prepare/verify PASS，不重发 R0001，不派发专业任务，不签 G4，不声明 Workmap `ADOPTED`。

## 核心选择

- task_id：`BI01-RESTART-01-I4-EXECUTION-01`
- professional_mode：`OBSERVATION_I4`
- 管理会话：`chatgpt-project:细节叙事生成_金标/chat:BI01-R01-管理`
- 专业会话：保持未来新聊天 `chatgpt-project:细节叙事生成_金标/chat:new:BI01-RESTART-01-I4-EXECUTION`，尚未创建或发送
- Binding carrier：R0001 exact commit 的地图、任务与 FULL_RESPONSE；无 `answer_ref`

## 落库规则

1. 先核本 ZIP 的 SHA-256 及 `MANIFEST.json`。
2. 按相对路径复制所有文件。
3. `R0001/ROLE_RETURN.json` 使用修正版当前内容；原内容仍由 exact commit `46119a8e0030b4c3597634735cbe5d22ad3a0ac7` 保留。
4. 同时保存 `ROLE_RETURN_REPAIR_R0002.json` 与采用说明。
5. 不更新通用 runtime；不把 Candidate 直接改为 ADOPTED。
6. 提交和远端读回后，重新运行 R0001 after-return、snapshot/reader/intake、binding/dispatch 与发送现场检查。
7. intake 的 `dispatch.task_id` 必须严格等于 `BI01-RESTART-01-I4-EXECUTION-01`。
8. 所有 Gate 通过前，不得派发专业任务。

## 完整回复载体

`runs/BI-01-RESTART-01/provenance/turns/R0002/FULL_RESPONSE.md` 包含本轮决定、全部修正版文件正文和两份 Return。
