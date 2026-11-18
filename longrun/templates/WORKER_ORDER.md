# W 操作工单正文（由运行本次 Skill 的执行 Chat 签发）

- `run_id / work_order_id / parent_delegation_id`：
- `issuer`（签单 executor）及 `issuer_call_id`：
- `worker / return_to`（return_to 必须为上述 executor）：
- 本次实际要做的操作、输入/数据与具体位置：
- 为什么属于原 D、要交回什么实物/日志/证据：
- 操作目标仓库、分支、工作区、命令或正式工具入口：
- 精确操作权限：`operation / execution_context / allowed_writes / authority_quote`
- 预期交付物清单（名称/类型/路径/验证方法）：
- 失败、部分交付、无数据、重复、工作区冲突时的停止与回报：
- 幂等/重跑条件、当前在途动作身份：
- 工单与 Owner、D 的对应引用（精确 GitHub commit）：

本模板只提供 V2 W 的通用操作身份与授权字段；**何时发 W、要求何种专业事实、如何消费 Worker 返回，完全由本次 Skill 决定**。Worker 按实际工单执行并事实回报；`ORDER.md` 不替代已发布的 `ORDER.json`。
