# BI-01 Workmap 采用：从真实管理结果接到下一轮

本页只规定运行接线，不定义专业工作，也不代替真实管理判断。所有例子为结构示意，不能提前创建有效 Intake；当前准备见 [运行指南](CASE_OBSERVATION_RUN_GUIDE.md)。

1. **首次 Owner GO**：保存真实 `runs/<本次run_id>/OWNER_START.md` 和原始授权来源。`management_prompt.py` 的 `prepare_bootstrap` 要求 `current_task_ref` 与 `task_adoption_ref`，可以都引用该次真实 Owner START 的 exact Git locator，不伪造尚不存在的 manager map/计划。binding_ref 指真实新 BOOTSTRAP；接收聊天取本次实际定位。
2. **M-START 管理实质交付**：管理从本次配置 goal_ref、完整专业方法、真实材料和实际目标出发，提交 map/task、decision/plan 和签发 Binding。map 按 goal/stage/evidence/progress/remaining/management/next 稳定 anchors 组织；任务有真实 `task_id:` 行。管理 Pro 是业务写者，操作端只机械发布已经授权的原文。
3. **采用真实 Workmap Binding**：使用 [通用模板](templates/WORKMAP_BINDING_TEMPLATE.json)，填实际 owner_sources、rule_paths、overview/shared anchors、streams.bi01 的 map/task/anchors、watch_roots 和 receipt_path。当前默认位置为 `runtime/config/WORKMAP_BINDING.json`，也可在实际采用时明确 run 专属路径；相关工具必须一致使用同一路径。只有管理签发、地图/任务/接收与校验真实完成，才写 ADOPTED，不能只切换 status。
4. **两次合法提交**：先交真实 manager map/task/Binding/decision，取得 commit A；按 A 运行 workmap_gate.py snapshot，显式提供 `--binding` 与 `--scope bi01`。依据真实管理/适用审查形成 Intake，保留 fingerprint、manager、决定全文 path/blob、task_id/path/blob、method_paths、reader_check 及范围，再取得 B 并 check/dispatch。Intake 不在 watch_roots，自身提交不使快照失效。工具结果不替代业务认可。
5. **独立性**：实际合同要求独立 reader_check 时，使用真实新上下文和具名对象；不只写 RECORDED，不把阅读可理解性当独立专业 PASS。实际例外必须有权且限范围，不由操作端把首轮偷偷改成 ROUTINE_RESULT。
6. **首轮专业发送**：采用 current task、Binding、真实接收者和新 INVOCATION/PROMPT；运行 `bi01_run_gate.py pre-dispatch --run-id <本次真实run_id>`，必要时同时指定 `--binding <本次路径>`，与 workmap_gate 和 Overlay12 使用同一来源，再核手机身份/未发送事实。检查器不发送、不生成业务采用；具体缺件按实际依赖处理，不借旧聊天或旧绑定绕过。
7. **后续**：原任务同工作续作不要求每轮管理重签，真实 Pro 调用仍记录新 R。重要结果、CHANGE/EFFORT 和接收按 DR13/14 处理；Worker 技术结果先回原签发 Pro 消费，不能仅因 INTAKE_STALE 自动改投管理。需要管理判断时由原 Pro 依绑定提出，真实到期管理责任继续保留。
8. **业务接收**：依据本次完整目标与专业产出核实物、认识、范围和未完；不以文件、图数、格式或接口成功代替专业完成，不从旧运行继承接收条件。

`provenance/turns` 是运输记录，不列入 watch_roots，否则新 PROMPT 提交会使现行 Intake 无谓失效。watch 实质 artifacts 和必要审查材料；实际成果变化仍可能影响 Intake，应按上述真实责任处理，不能为连续发消息伪造通过或排除实质成果。
