# 既定 Workflow / Skill 与长程 V2 的接入关系

此文件只说明**专业工作如何进入 V2 的 C/D/W 和整体状态**；不重新定义观察方法、合理性分析方法、专业完成标准或额外 Gate。

## 1. 来源及职责

- **整体 Workflow**：由本 Run 实际采用的业务仓流程提供。当前观察材料准备见 [control/02](../control/02_L1_观察材料准备流程.md)：A → (B、C) → D → E，E 按对应 Skill 的真实结论返回受影响阶段。
- **专业 Skill**：当前 M 的五个 Skill 见 [观察材料准备总入口](../skills/observation-material-preparation/SKILL.md)，各自的 `SKILL.md / WORKFLOW.md / IO_SPEC.md` 和 Reference 是专业执行依据。合理性分析按本 Run 实际采用的版本处理，不在这里固定 R0～R5。
- **多层 Workflow 运行协调 Chat（V2 `manager`）**：依据已有输入、真实 Skill 回交、阶段依赖及其版本推进、等待、回流，并维护 [当前完成全景](templates/TASK_PROGRESS.md)。
- **Skill 执行 Chat（V2 `executor`）**：执行本次指定 Skill；专业输出、完成条件、何时需要 Worker、如何消费 Worker 返回均依据该 Skill。
- **主控 Codex**：处理真实身份/授权、发送、回执、去重、消息回流、GitHub 保存和运行事实核验，不自行形成专业结论。

## 2. C/D/W 与专业工作的关系

- `C` 是一次真实模型调用；`D` 是具名 Skill 工作委派；`W` 是 Skill 执行 Chat 在该 Skill 确有需要且获 Owner 权限覆盖时派出的真实操作工单。三种身份不是 A/B/C/D/E 业务阶段，也不是 Skill 内部步骤。
- 一项 D **默认对应一个 Skill 工作**，可以通过多个 C 继续，直到其 Skill 原生流程实际完成或有据报告无法继续。无需为每个内部步骤单独创建 D。
- D 的正文按 [Skill 工作委派模板](templates/PRO_DELEGATION.md) 传递工作身份、Skill 版本、已接受上游输入/成果、返回对象；**不自行增加执行约束、专业方法、业务预期、Worker 返回处理说明或另一套完成条件**。Owner 的真实操作权限由 V2 机器授权机制独立核验。
- 同一个执行 Chat 可以在不同工作中运行不同 Skill，也可以按实际依赖增加多个执行 Chat。A 完成后 B/C 可以并行，D 只能消费当前有效的 A/B/C 结果；并行工作须具有独立身份与可核对的产物版本。
- 某 Skill 的内部步骤、循环和 Worker 处理由该 Skill 自己负责。E 当前的实际运行/取数仍按 [E Skill](../skills/observation-material-preparation/caegraph-execution/SKILL.md) 与其 Worker 合同进行，V2 只保证 W 返回原签发的 executor，不另设专业处理法。

## 3. 结果回流和整体状态

```text
Skill 执行 Chat 依 Skill 产生专业结果
  → V2 验证真实回交并送原 Workflow 运行协调 Chat
  → 运行协调 Chat 依据既定依赖和实际有效版本确定续作／后继／回流
  → 更新 TASK_PROGRESS 当前任务全景
  → 主控核验并保存真实来源和下一 C/D/W
```

运行协调 Chat不需要为正常的 Skill 推进再签独立专业 Gate 或专业管理决定。Skill 的专业完成由对应 Skill 执行 Chat 按原生合同判断；协调 Chat 负责准确记录有哪些工作与结果、哪些依赖已满足、哪些仍需继续或等待。

状态视图维护工作项、阶段/Workflow、业务问题、父任务之间的当前关系，并标记版本失效、未完成、在途、阻断和原工作接续入口。**全景只引用已核实的真实成果/回执，不新增状态系统或机器字段**。某项 W 完成不等于专业 Skill 完成；某项 D 完成不等于父任务完成。

## 4. 机械安全与采用边界

Owner GO 与 V2 原有 `grants`、物理聊天绑定、Worker 实际工作区/单写者校验、动作回执、`UNKNOWN` 对账及版本锁继续有效；不得将“运行协调 Chat 不制定执行约束”误解为可以绕过真正的权限校验。业务仓的新提交不自动升级已经采用固定版本的 Run。
