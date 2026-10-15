# BI-01 Workmap 采用：从管理结果真正接到下一轮

此页只规定运行接线，不代替真实管理判断；所有例子仅作流程，不能提前创建有效管理 Intake。

1. **首次 Owner GO**：下次 Owner 发出明确开始指令后，操作端保存真实 `runs/BI-01-RESTART-01/OWNER_START.md` 并取得 Owner 来源；`management_prompt.py` 的 `prepare_bootstrap` 还要求 `current_task_ref` 与 `task_adoption_ref`，这两项可以都是该次 Owner START 的 exact Git locator，不要求伪造不存在的 manager map/计划。BOOTSTRAP 的 `binding_ref` 指真实新 BOOTSTRAP。首次聊天必须有新的实际 recipient。
2. **M-START 管理实质交付**：管理 Pro 从真实数据/方法与本次目标出发，提交 `runs/.../00_长程推进地图.md`、`01_当前任务.md`、`reviews/management-Rnnnn/` 的 decision/plan 与签发 Binding，回答完整返回。真实 map 按模板的 goal/stage/evidence/progress/remaining/management/next 稳定 anchors 组织；任务带准确 `task_id:` 行，不能空模板。管理 Pro 是业务唯一写者，操作端可以机械发布已经授权的原文。
3. **采用真实 Workmap Binding**：从[模板](templates/WORKMAP_BINDING_TEMPLATE.json)生成新配置（`runtime/config/WORKMAP_BINDING.json`），将 status 从 TEMPLATE_DO_NOT_ADOPT 变为 ADOPTED **仅当实际路径/业务任务/角色和权限已形成**。结构要有 overview/shared anchors、streams.bi01 的 map/task/anchors、owner_sources、rule_paths、watch_roots 与 receipt_path。正式旧文件的 NOT_CONFIGURED 绝不能只改 status 蒙混。旧仓的 CURRENT 不许成为新地图。
4. **两次合法提交**：先提交新 manager map/task/真实 Binding/decision，得确切 commit A；在本地 Git 对 A 运行 `runtime/overlay/tools/workmap_gate.py snapshot --repo . --ref A --binding runtime/config/WORKMAP_BINDING.json --scope bi01`。基于真实管理审查、管理接收、适用的独立读图结果，提交 `runs/.../reviews/WORKMAP_INTAKE_CURRENT.json`，包含与 A 对应的 fingerprint、实际 manager 身份、决定全文路径及 blob、真实 task_id/path/blob、实际 method_paths、reader_check 与资格范围；得 commit B。由于管理 intake 不在 watch_roots，下次 snapshot 不会因自身提交而失效。对 B 运行已有 workmap_gate.py 的 check/dispatch，再核出具结果中的剩余要求。
5. **独立性**：新的重要地图/阶段若按已有 v2 规则需要独立 reader_check，必须有实际新上下文和明确对象、读图记录，不能仅将 reader_check 写为 RECORDED。该阅读只检可理解性，不自动成为 BI-01 独立专业审查 PASS；后者目前专业 Harness 仍 PARTIAL。真实例外由有权管理判断、具名用途，不能由操作端偷偷把首轮当 ROUTINE_RESULT 免门。
6. **首轮专业发送**：完成已采用的 current task、绑定、真实接收者、新 round INVOCATION/PROMPT 后，由 `runtime/tools/bi01_run_gate.py pre-dispatch` 与适用 workmap_gate 和 `Overlay12` 验证，再检查手机端身份/未发送事实。检查器不会发送或自动生成 Binding/receipts；出现无法取得 source、reader、live MCP 或 Gate 则给确切恢复点，不借用旧业务仓/旧管理聊天绕过。
7. **后续**：同工作短续作不必每轮管理重签，但 Rnnnn 始终更新。重要新增证据/结果与 Gate/预算复看按 DR13/14 找管理，更新地图/当前任务/正式 intake；不能仅更新 PROGRESS。当前权限和提交来源不同于 Git 包字节源时要分别标记，不把 map 变新 SHA 误认为管理已重新判断。
