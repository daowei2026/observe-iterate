# WALL / F 并行统计闭环｜任务输入

> 状态：`PREPARED_NOT_GO`。WALL 远端修复代码版本已经锁定；F 新参数实例、两个独立工作区、WALL 运行入口／参数以及正式授权仍待 Owner 补齐。任何会影响对应 Run 的 `PENDING_OWNER` 未替换前，不得注册该真实 Run。

## 1. 目标

并行安排两条基础 Feature 线：

```text
WALL 最新修正版
→ 全量运行／验证复用
→ 重新统计
→ 继续找明显不合理点
→ 当前深度闭环

F 新参数实例
→ 全量运行
→ 重新统计
→ 继续找明显不合理点
→ 当前深度闭环
```

两条基础线均形成可释放版本后，再启动各自下游。

## 2. 文件

| 文件 | 用途 |
|---|---|
| [OWNER_INTENT_AND_RUN_PLAN.md](OWNER_INTENT_AND_RUN_PLAN.md) | Owner 意图、两线并行和停止深度 |
| [WALL_BASE_RUN_INPUT.md](WALL_BASE_RUN_INPUT.md) | WALL 基础 Run 输入；已锁定远端修复提交 |
| [F_BASE_RUN_INPUT.md](F_BASE_RUN_INPUT.md) | F 基础 Run 输入 |
| [KNOWN_FINDINGS.md](KNOWN_FINDINGS.md) | 当前已知问题及新 Run 中的状态要求 |
| [DOWNSTREAM_DEPENDENCIES.md](DOWNSTREAM_DEPENDENCIES.md) | 联合 Barrier、WALL 下游、F→Q→V |
| [VERSION_WORKSPACE_LOCKS.md](VERSION_WORKSPACE_LOCKS.md) | 版本、参数、工作区和授权锁 |

## 3. 专业来源

采用：

- `control-v0.3/`；
- `skills/feature-understanding/` 及业务对象判别补充；
- `feature-global-behavior-profiling`；
- `business-discrepancy-diagnosis`；
- 必要时 `feature-instance-calibration`；
- `STATISTICS_DRIVEN_PRACTICE.md`。

历史 Chat 是思考过程和已知问题来源，不替代当前代码、参数和运行结果：

- `ai_chat/根据统计找不合理点/WALL 特征：统计线闭环.md`；
- `ai_chat/根据统计找不合理点/F特征：统计线闭环.md`；
- `ai_chat/根据统计找不合理点/wall特征，修frp代码.md`。

## 4. 已锁定的 WALL 代码版本

```text
branch: codex/wall-output-consistency-20261121
commit: 6618d4d147d6ebbe634e61facddf2c9a0b996982
```

该提交包含 D1、D2、D4 的修复链。新 Run 仍须核对实例、参数、数据和最终统计；远端提交存在不等于本特征已经通过释放 Gate。

## 5. 运行 profile

两个基础 Run 均采用：

```yaml
execution_profile: CODEX_NATIVE_DIRECT
manager: Codex new thread per run
executor: Codex new thread per run
workers: []
```

WALL、F 使用不同且不重叠的 Linux 工作区。主控按现有多 Run 控制器交错推进。

## 6. 当前仍不能自动推定的内容

- WALL 的正式执行入口、参数实例和是否复用已有最终结果包；
- F 新参数的字段、值、配置文件和代码 commit；
- WALL 完整下游 Feature 图；
- 两个 Linux 工作区；
- 允许提交／推送／写缓存的真实 grants。

这些必须由 Owner 在 `VERSION_WORKSPACE_LOCKS.md` 和实际 GO 中补齐。
