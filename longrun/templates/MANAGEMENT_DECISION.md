# 管理 Pro 控制决定（运行期模板；不是实际 Gate 结果）

> 真实 GO 后按需作为 `longrun/runs/<run_id>/business_control/decisions/<decision_id>.md` 归档。管理 Pro 生产专业判断；有权写 GitHub 时自己提交，否则主控原样发布。不为每个一般工作步骤增加额外 Gate。

- `run_id / decision_id`：
- `question_id / stage_instance_id / work_item_id / analysis_round_id`（适用部分）：
- 控制点：`H0/H1/H2/H3 / G-* / 其他具名异常或路由`：
- 输入和所检 Gate/完成条件的准确来源：
- 已核实事实（精确结果/回执/版本引用）：
- 业务判断与理由（包括未通过或部分可用的原因）：
- **本次试运行决定**：`ACCEPT / ACCEPT_FOR_SCOPE / REPAIR / ADD_EVIDENCE / CONTINUE / WAIT / BLOCK / COMPLETE / STOP / REQUEST_OWNER`（用最贴合实际的一个；不改写专业结果状态）：
- `accepted_scope / limitations`：
- `retained_results`（必须保留的已有有效成果）：
- `affected_work_items / affected_stage_instances / affected_questions`：
- `new_or_repaired_work`（输入、期望输出、消费者与最小范围）：
- `exact_next_action_or_resume_condition`：
- `owner_intervention_reason`（仅真实工具权限缺失、明确禁止事项冲突、真正改变已确认目的等情况；无则写“无”，不因正常 Gate 失败反复申请）：
- 对 `TASK_PROGRESS.md` 的更新摘要：

**边界**：试运行 manager 的业务决定是本轮有据的管理后继依据，不意味着后台生产级受保护 Gate 程序已经存在。主控负责核验真实引用、顺序、身份和实际工具权限，不能自行改写业务结论。