# BI-01-RESTART-01 R0002 Owner 一次性管理交付修复授权

- 授权类型：`OWNER_AUTHORIZED_MANUAL_REPAIR`
- 授权作用域：仅限 `runs/BI-01-RESTART-01/reviews/MANAGEMENT_DELIVERY_REPAIR_REQUIRED_R0001.md` 已列缺项
- 恢复基线：`46119a8e0030b4c3597634735cbe5d22ad3a0ac7`
- 目标物理管理会话：`BI01-R01-管理`
- 明确边界：不修改通用 Overlay12/runtime；不把本次记为 Overlay12 prepare/verify PASS；不重发 R0001；不在 Gates 通过前派发专业任务或声明 `ADOPTED`
- 来源：当前 Codex Owner 消息，`2026-10-16`（Asia/Shanghai）

## Owner 授权原文

<!-- OWNER_MESSAGE_BEGIN -->
请从 observe-iterate 提交
46119a8e0030b4c3597634735cbe5d22ad3a0ac7
继续 BI-01-RESTART-01。

作为 Owner，我批准 BI-01-RESTART-01 的一次性管理交付修复例外。

本次先不修改 observe-iterate 的通用 Overlay12/runtime 机制。该例外仅用于解决当前机制无法准备 BOOTSTRAP-origin 管理补交消息的问题，不代表现有 Overlay12 已通过或已支持这种补交流程。

修复范围严格限定为：
runs/BI-01-RESTART-01/reviews/
MANAGEMENT_DELIVERY_REPAIR_REQUIRED_R0001.md
已经列出的缺项。

执行要求：

1. 保留 R0001 的原始历史，不重发 M-START，不覆盖、伪造或改写原始管理交付记录。

2. 先把以下内容作为可审计记录提交并推送到 observe-iterate：
   - 本次 Owner 授权原文；
   - 准备发送给管理角色的完整补交提示词；
   - 实际接收方：原物理管理会话 `BI01-R01-管理`；
   - 提示词 SHA-256；
   - 本次调用的轮次/调用标识。

3. 本次必须如实标记为：
   `OWNER_AUTHORIZED_MANUAL_REPAIR`
   不得记录成 Overlay12 prepare/verify PASS。

4. 把窄范围修复请求发送给同一个原管理角色会话
   `BI01-R01-管理`。
   不得新建替代管理会话，不得让操作 Codex 自己填写管理判断。

5. 要求原管理角色检查并重新交付修正后的管理包，范围只包括：
   - 为当前任务补充合法 `task_id:`；
   - 为 R0001 `ROLE_RETURN` 补充可追溯的
     `question_work_ref`；
   - 从当前锁定配置允许的模式中选择合法
     `professional_mode`；
   - 提供能够被解析、定位和校验的 `answer_ref`
     carrier/locator；
   - 把管理 route 修正为实际存在的
     `BI01-R01-管理`，不再指向 `chat:new:*`；
   - 如这些修复要求管理地图、当前任务或相关签发物同步更新，
     由原管理角色明确给出修正版及其关系。

6. 上述字段及业务判断必须由原管理角色决定和交付。
   操作 Codex 只负责：
   - 准备和传递已获授权的修复请求；
   - 捕获原管理角色的完整回复；
   - 保存 invocation、receipt、原始回复、hash 和相关证据；
   - 按管理角色交付内容落库；
   - 重新运行 Candidate intake、reader、binding、dispatch 等 Gates。

7. 本次修复调用属于新的管理 invocation/管理轮次，不是专业任务轮次。
   如按顺序编号，可将其作为 R0002 管理修复轮；
   首个专业任务随后顺延，不能把修复轮伪装成专业轮。

8. 所有相关 Gates 真正通过以前：
   - 不得派发专业任务；
   - 不得创建后续业务轮；
   - 不得声明 `ADOPTED`；
   - 不得自行选择或补写管理角色尚未明确给出的业务字段。

9. 如果无法安全定位同一个 `BI01-R01-管理` 会话、无法保存发送前证据，
   或管理角色返回内容仍不满足修复要求，应立即停在
   `needs_human / paused`，如实报告剩余缺项，不得继续绕过。

修复通过后，请汇报：
- Owner 授权记录和提交链接；
- 修复 invocation/receipt；
- 原管理角色修正版交付物；
- 各 Gate 的真实结果；
- 当前恢复提交；
- 是否已经具备专业派发条件。

现在按上述范围继续，不要重新执行 R0001。
<!-- OWNER_MESSAGE_END -->
