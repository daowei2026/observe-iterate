# Owner GO（V2 通用启动模板，未填写不构成授权）

Owner 可以用自然语言启动消息、任务书或已有任务输入提供下列事实；不要求重新制作本模板文件。主控把真实原文、适用来源及已核实运行配置保存到 OWNER_START.md。缺失必要权限或资源不猜测；可查的专业事实由 executor 核实。

## 目标、来源与边界

- work_id / business_case_id（无独立标识可用 work_id）/ 全新 run_id：
- 任务目标、范围、明确非目标、产出、完成/停止条件：
- 专业任务依据（任务书、Workflow、Skill 或混合；精确引用与适用章节）：
- 实例输入（数据、对象、代码/参数/版本、可复用结果及待查项，按适用）：
- 允许自主选择、研究、执行、修改或发布的范围：
- post_start_owner_policy: AUTONOMOUS（新 Run 必填）
- 可选：已有专业进度模板；没有则采用通用 TASK_PROGRESS 和 BUSINESS_PROGRESS。

## 执行配置与资源

- 采用运行协议、指南和 cgpterm 主控版本：
- 物理 profile：CODEX_NATIVE_DIRECT 或本 Run 明确的 Web/Codex 角色绑定：
- manager / executor / 可选 worker：逻辑角色、平台、项目（Web 时）、模型/强度、创建或恢复规则：
- owner_declared_linux_workspace：Owner 已准备且没有其他 Run 占用的绝对路径；已真实释放的常用工作区可复用。
- 工作区/主机、结果位置、Git 目标仓库和分支、共享写面：
- 多 Run 关系、依赖、优先级、适用的失效规则（如有）：

新 Run 按本次配置创建新会话，恢复核原绑定；不要求 Owner 预先提供新会话 ID。主控在实际主机验证目录、realpath、模型、权限及冲突，物理 ID 由真实设施回读。角色、平台和任务阶段独立。

## 一次性真实授权

每项适用操作以可核验的 Owner 原文明确（只读研究不要求生产写权）：

```text
operation=<明确动作>
execution_context=<精确运行仓库/分支/工作区>
allowed_writes=<明确允许写入的仓库/分支/路径；无写入可为空列表>
authority_quote=<实际 Owner 原文，包含上述授权值>
```

仅授权本任务实际所需操作及写面。路径不等于权限；模板、AI 总结、旧 Run GO 均不能构成真实授权。主控按原 V2 精确授权校验；未覆盖仅阻断相关操作，不设运行中 Owner 审批。需要主控 Chat 归档时另一次性明确指定分支和 longrun/controller/chats/ 的提交/推送授权，仅归档主控自身可见对话。

## 发布

真实 GO 原件/消息及精确保存引用：
采用来源版本（运行协议、专业任务定义、物理主控实现分开）：
授权生效/取消条件：
