# Owner GO｜Codex 原生直执行

> 本模板未填写、未发布或未核实，不构成授权。适用 profile：`CODEX_NATIVE_DIRECT`。

## 1. 任务

- `work_id`：
- `business_case_id`：
- `run_id`（全新，不复用历史）：
- `BusinessTaskInput` 精确引用：
- `CurrentReviewTarget`：
- 本轮必须完成：
- 明确非目标：
- 停止／完成条件：
- 采用的 Workflow／Control／Skill／实践补充精确引用：

## 2. 版本和数据

- Feature 代码完整 commit：
- 构造入口：
- 参数实例引用和 SHA：
- 数据／品种／时间／日历：
- 允许复用的既有结果及校验条件（没有则写无）：

## 3. 物理角色

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
```

- 主控逻辑身份和物理绑定：
- manager 逻辑身份：
- executor 逻辑身份范围：
- 同一 Run 恢复时复用规则：

## 4. Linux 工作区

- `owner_declared_linux_workspace`：
- Owner 已准备：是／否
- 目标主机／环境：
- 对应仓库、分支和输出位置：
- 与其他活跃 Run 的关系：

主控必须核目录存在、realpath、实际 cwd、权限和外部写面冲突。路径声明本身不是写权限。

## 5. 一次性工程授权

每类实际操作填写：

```text
operation=<准确动作>
execution_context=<准确仓库/分支/工作区>
allowed_writes=<允许写入的路径或分支>
authority_quote=<Owner 原文，包含以上值>
```

按需覆盖：运行 Feature、写任务产物、修改代码、提交／推送分支、运行测试、读取缓存或写结果。未被任何 grant 覆盖的动作只阻断该动作。

## 6. 多 Run 和下游

- 本 Run 所属并行任务：
- 独立上游：
- 联合 Barrier（如有）：
- 下游依赖：
- 上游版本变化后的失效规则引用：

## 7. 发布

- Owner 实际 GO 原件／消息：
- `observe-iterate` 采用 commit：
- 授权生效时间：
- 取消或修改条件：

所有 `PENDING_OWNER` 均被替换、工作区和 grants 核实后，主控才能注册 Run 和创建物理线程。
