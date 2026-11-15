# BI-01-RESTART-01 R0002 管理交付窄修复决定

- invocation：`BI01-RESTART-01-R0002-c19efdc130c1995d4660ca4907747429`
- assignment token：`dc5df7008bbcb41665e37aea084c100e`
- authority：`OWNER_AUTHORIZED_MANUAL_REPAIR`
- Overlay12：`NOT_RUN_NOT_PASS`
- 原管理会话：`BI01-R01-管理`
- 业务范围：不变；不重新执行 M-START；不派发专业任务；不签 G4；不宣称 Workmap `ADOPTED`

## 六项决定

1. **task_id**：选择 `BI01-RESTART-01-I4-EXECUTION-01`。修正版 `01_当前任务.md` 只新增这一身份行；后续 intake 的 `dispatch.task_id` 必须完全一致。
2. **R0001 ROLE_RETURN**：保留 exact-commit 原件，新增修复旁路件，并将相同修正版物化到当前规范路径供 `after-return` 读取。唯一新增字段是指向原 R0001 `QUESTION_WORK_RETURN.json` 的非空 `question_work_ref`。
3. **professional_mode**：选择 `OBSERVATION_I4`。当前主体是 I4 真实结果观察与反证挑战；定向 I3 是 I4 任务内的证据资格核查，不另造 mode。
4. **Binding carrier**：删除 Binding 中全部 `answer_ref`。规范载体分别为 R0001 exact commit 中的 `00_长程推进地图.md`、`01_当前任务.md` 与 `FULL_RESPONSE.md`；每个引用均带 exact commit/path/selector。
5. **route**：全部 management route 改为 `chatgpt-project:细节叙事生成_金标/chat:BI01-R01-管理`。未来 professional same-work/return-repair route 继续保留 `chatgpt-project:细节叙事生成_金标/chat:new:BI01-RESTART-01-I4-EXECUTION`；这不表示聊天已创建或任务已发送。
6. **同步文件**：修正 run README、地图的当前操作位置与 Workmap Binding Candidate 说明；原 `MANAGEMENT_START_R0001.md` 和业务正文不重写。

## 原件与修复件

- R0001 原始历史：`daowei2026/observe-iterate@46119a8e0030b4c3597634735cbe5d22ad3a0ac7:runs/BI-01-RESTART-01/provenance/turns/R0001/::tree`
- R0001 原 ROLE_RETURN：`daowei2026/observe-iterate@46119a8e0030b4c3597634735cbe5d22ad3a0ac7:runs/BI-01-RESTART-01/provenance/turns/R0001/ROLE_RETURN.json::full`
- R0001 原 QUESTION_WORK_RETURN：`daowei2026/observe-iterate@46119a8e0030b4c3597634735cbe5d22ad3a0ac7:runs/BI-01-RESTART-01/provenance/turns/R0001/QUESTION_WORK_RETURN.json::full`
- R0002 修复件不会改变上述 Git 对象；新提交只形成当前采用修正版和旁路审计件。

## 仍未满足

- 尚未由本回答写入或推送 GitHub；
- 尚未 remote readback；
- 尚未 fresh snapshot/reader/intake；
- 尚未运行修复后的 Candidate/binding/dispatch Gates；
- Workmap 尚未 `ADOPTED`；
- 专业任务尚未派发；
- Overlay12 仍为 `NOT_RUN_NOT_PASS`。
