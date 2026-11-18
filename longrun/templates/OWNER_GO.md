# Owner GO（V2 任务启动模板，未填写不构成授权）

## 目标与边界

- `work_id`：
- `business_case_id`（用例稳定标识；如无独立标识，可明确与 work_id 相同）：
- `run_id`（本次全新、不得复用历史 Run）：
- `BusinessTaskInput`：当前实际已知的业务目的、对象、问题、现有资料线索及精确来源；未知项如实列为待查：
- **已明确**的本轮范围/允许深度/预算/不可做事项/停止与完成条件（没有明确的写“待明确”，不是另设启动前必须填满的 TaskBoundary）：
- 仅列出 Owner **已明确禁止**的事项或不能改变的业务目标（如无则不为了预设审批点而虚构）：
- 采用的专业 Skill / 控制面来源（仓库、提交、路径）：
- 任务结果期望及 Owner 接收方式：

## 本 Run 的两类 Chat 工作方式

- **多层 Workflow 运行协调 Chat**（V2 身份 `manager`）：维护整个任务的当前状态及版本依赖；依据已采用 Workflow 调用、等待、接续和回流具体 Skill 工作；按需增加 Skill 执行 Chat。不自行添加执行约束、专业方法、业务预期、Worker 处理办法或专业验收条件，也不额外担任独立专业 Gate。
- **Skill 执行 Chat**（V2 身份 `executor`）：根据本次指定 Skill 的原始文件实际完成专业工作及其内部 Workflow；专业结果、完成条件及 Worker 使用与返回处理全部以该 Skill 为准。
- **状态与恢复**：继续以 `longrun/runs/<run_id>/business_control/TASK_PROGRESS.md` 记录当前整体任务及阶段工作、版本、在途和合法后继；主控据真实产物和回执保存、核实，不编造专业决定。不另设状态数据库。
- **派发单位**：默认一个 D 对应一项 Skill 工作；同一 Skill 可跨多个 C 接续。观察材料准备 A 后 B/C 可在有效输入和物理身份可用时按需并行，不强制每个 Skill 单独建 Chat。
- **运行限制**：Owner 授权和 V2 机器执行权限由主控单独校验，协调 Chat 不增设专业执行约束。没有真实 GO 与特征来源时，只可准备运行接线，不创建实际业务 Run。

## 运行角色

- 主控逻辑身份与物理端绑定方式：
- 多层 Workflow 运行协调 Chat（V2 manager）逻辑身份与物理聊天绑定方式：
- 允许参与的 Skill 执行 Chat（V2 executor）身份范围及按需增加方式：
- 允许参与的 Worker Codex 身份范围：

## 本项目执行目标（正式 GO 时确认适用配置）

以下是用户本次对**未来长程执行环境**的指定，写在模板里用于避免实际派发时猜 Project/Worker 工作区；**不是已经发布的 Run GO，也不是证明项目、聊天、Linux 目录或模型已经验收**。

- 多层 Workflow 运行协调 Chat、Skill 执行 Chat：均使用 ChatGPT Project **`细节叙事生成_金标`**；各自独立角色聊天，当前指定的目标模型为 **`GPT-5.6 Sol`**，推理档位为 **`Pro`**。是否已经实际选中，须由每次发送前的现有操作 Skill 验证；模板本身不证明设置成功。
- Worker：每个 `run_id` 的 Linux 工作区由 Owner 提前准备，并在本次真实 GO 中指定独立绝对路径；不从其他 Run 或示例路径推断。
- Worker 目标模型/推理配置：**`GPT-6.1 Sol Max`**；实际可用性与现场配置仍需在真实派发前核验。
- 若 Owner 后续重新指定项目、路径或档位，以新的真实指令为准；不同 Run 不自动继承。物理 Project/ChatGPT 聊天、Codex threadId、实际目录和配置在真实启动时记录到可信运行映射；不能因为模板包含上述信息就认定已创建。
- **工作区路径不是写权限**：真正执行 W 仍须受下列独立的 `operation / execution_context / allowed_writes / authority_quote` 授权及共享目标单写者检查约束。

## 本 Run Linux 工作区（多 Run 时必须由 Owner 明确给出）

- `owner_declared_linux_workspace`：<本 Run 已准备的绝对 Linux 路径，不填其他 Run 的工作区>。
- 当前工作区是否已由 Owner 准备：<是/否；未准备则不得派出依赖此路径的 Worker 动作>。
- 对应仓库、分支及实际输出/写入位置：<明确现行使用范围，真实权限仍以下面的 grants 为准>。
- 多 Run 关系：<新的 run_id，若与旧用例/旧 Run 有关联，给出准确引用；不要沿用旧 Run 运行状态>。

主控负责在真实目标 Linux 主机上核实目录存在、realpath 与其他活跃 Run 不重叠、权限和 Worker 实际 cwd，再写入 `runs/<run_id>/RUN_RESOURCE_BINDING.json`。这不是主控自动创建工作区的授权。

## 本 Run 一次性覆盖常规工程操作（V2 仍须可校验的 Owner 原文）

这部分仅用于**真实工具派发的机器权限校验**，不是由运行协调 Chat 自拟的专业执行约束。Owner 可在启动 GO 里**一次性覆盖本次业务通常需要的操作类别和写入位置**；主控据此为 V2 Binding 编制一个或多个可核对的 `grants`，随后各 D/W 在覆盖范围内自主执行，不再每条工单都向 Owner 要授权。

现有 V2 Schema 与 `longrun_gate.py` 对 `operation`、`execution_context`、`allowed_writes` 采取精确值匹配，所以**以下字段需要在启动 GO 中有真实、准确的 Owner 原文**。可以按操作类别共用一条授权，不是为每个具体文件/每次取数申请一次。不能把模板示例、任何 Chat 的解释或主控猜测当作实际 `authority_quote`：

对本 Run 需要覆盖的**操作类别**填写（不是每次动作重复）：

```text
operation=<明确动作>
execution_context=<精确运行仓库/分支/工作区>
allowed_writes=<明确允许写入仓库/分支/路径>
authority_quote=<包含以上三个值的 Owner 原文>
```

**使用原则**：既有工具实际允许、且属于 GO 一次性涵盖的操作，按 V2 直接派发而不再次请求人工批准。若单项真实动作不属于任何已登记的操作类别，先检查现有授权是否已经包含等价操作；不能因字段命名不同就无故中断，也不能通过伪造 `authority_quote` 绕过 V2 校验。确实缺少实际访问权限时只阻断该动作，具体说明缺什么；其他合法工作继续。

## 真实发布

- Owner 实际 GO 消息/原件：
- 采用提交：
- 授权生效与取消/修改条件：

主控收到真实 GO 后方可创建 `longrun/runs/<run_id>/`；未填写、未发布或未核实的不启动运行。
