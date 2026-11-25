# Owner GO｜Codex 原生直执行

本模板未填写不构成授权；采用 [通用 Owner GO](OWNER_GO.md) 的任务、实例、来源、权限和保存目标。本文件仅补充物理配置，不引入专业要求。任务书/启动消息可直接提供所需信息，不必复制模板。

```yaml
execution_profile: CODEX_NATIVE_DIRECT
manager:
  product: Codex
  create_new_thread: true
executors:
  product: Codex
  create_new_thread_per_run: true
  direct_workspace_access: true
workers: []
post_start_owner_policy: AUTONOMOUS
```

- run_id / work_id / business_case_id：
- 专业任务依据及适用章节/精确引用：
- 实例输入、目标、范围、产出及结束条件：
- manager / executor 各自模型及推理强度：
- owner_declared_linux_workspace（Owner 已准备独立绝对路径）：
- 结果保存、Git 目标和授权（按通用 GO 的精确 grants）：
- 实际采用的运行协议、专业来源、cgpterm 实现版本：

新 Run 创建本 Run 专属 manager/executor Codex session；同 Run 接续先核原绑定，不要求 Owner 提供新 threadId。manager 只组织运行协调和记录；executor 直接完成授权内专业动作。没有 Worker。不能从工作区路径推断写权；只读研究无需生产修改、重跑或发布权限。运行中不增加 Owner 审批。
