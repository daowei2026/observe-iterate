# Skill 工作委派正文（V2 D，运行协调 Chat 签发）

本 D 仅绑定一次**具体 Skill 工作**与已存在输入，不重新规定专业方法或专业验收条件；机器身份和授权以本 Run 的 V2 记录为准。

- Run / 委派身份：`run_id / Dxxx`；实际签发调用：`issuer_call_id`
- 发出和接收身份：`issuer / recipient / return_to`
- 原任务及本项工作：`parent_task_id / question_id / work_item_id / stage_instance_id`（按实际适用填写）
- 本次 Skill：`owner/repo@40位commit:path`；其必要的 `WORKFLOW.md / IO_SPEC.md / references` 按 Skill 原文读取
- 外层任务已提供的事实：本次特征名称、代码版本、特征实例及其精确来源（仅适用时）
- 已有上游真实产物：精确引用、版本和当前已知缺口（不把未完成事项写成既定结果）
- 本项专业输出：**直接遵循上面 Skill 的原生输出及完成条件**，不另写最小证据、专业验收或 Worker 返回处理要求
- 同一工作继续时：原 D/工作项、已形成产物和当前续接引用
- 实际回交对象：原运行协调 Chat、原工作身份

Owner 的具体操作授权和 V2 `grants` / D/W 机读权限必须由主控**单独按正式来源校验**；此专业委派正文不为运行协调 Chat 增加自行撰写“执行约束”的权限。

对应的 `DELEGATION.json` 继续使用既有 V2 身份、来源、授权及返回字段，不新增机器 Schema。
