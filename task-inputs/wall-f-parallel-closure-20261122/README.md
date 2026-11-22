# WALL / F 并行统计闭环｜任务输入

> 状态：`PREPARED_NOT_GO`。WALL 远端修复代码、两条线的正式用例／品种／时间／尺度／工作区已经锁定；F 新参数实例、真实 Run 身份、必要版本绑定和正式授权仍待补齐。未满足真实 GO 条件前不得注册对应 Run。

## 1. 目标

并行安排两条基础 Feature 线：

```text
WALL 最新修正版
→ 按 EAW P1、rb/m、2021 全年正式范围运行／严格验证复用
→ 重新统计
→ 继续找明显不合理点
→ 新修改先回 Owner 确认
→ 当前深度闭环

F 新参数实例
→ 按 U2/U3 F 用例、rb/hc/i、5m、2021—2023 正式范围运行
→ 重新统计
→ 继续找明显不合理点
→ 新修改先回 Owner 确认
→ 当前深度闭环
```

两条基础线均形成可释放版本后，再启动各自下游。

## 2. 文件

| 文件 | 用途 |
|---|---|
| [OWNER_PROMPT_EXTRACT.md](OWNER_PROMPT_EXTRACT.md) | 从原 Chat、工作群和当前对话提炼的 Owner 原始意图、锁定范围、纠偏和确认边界 |
| [OWNER_INTENT_AND_RUN_PLAN.md](OWNER_INTENT_AND_RUN_PLAN.md) | 两线并行、当前深度和修改确认路由 |
| [WALL_BASE_RUN_INPUT.md](WALL_BASE_RUN_INPUT.md) | WALL 基础 Run 输入；已锁定远端修复提交、用例、范围和工作区 |
| [F_BASE_RUN_INPUT.md](F_BASE_RUN_INPUT.md) | F 基础 Run 输入；已锁定用例、范围和工作区，等待新参数实例 |
| [KNOWN_FINDINGS.md](KNOWN_FINDINGS.md) | 当前已知问题及新 Run 中的状态要求 |
| [DOWNSTREAM_DEPENDENCIES.md](DOWNSTREAM_DEPENDENCIES.md) | 联合 Barrier、WALL 下游、F→Q→V |
| [VERSION_WORKSPACE_LOCKS.md](VERSION_WORKSPACE_LOCKS.md) | 版本、参数、工作区和授权锁 |

## 3. Owner 已锁定的正式运行范围

| 线 | 用例 | 品种 | 正式时间／尺度 | 工作区 |
|---|---|---|---|---|
| WALL | EAW P1 integrated / WALL | `rb, m` | `2021-01-01..2021-12-31`，当前正式 tick 输入，bid/ask | `/dwdhome/fy/BASE_E6_2` |
| F | U2/U3 F-Q-V 用例中的 F | `rb, hc, i` | `2021-01-01..2023-12-31`，5m | `/dwdhome/fy/BASE_E6_2_copy` |

AI 不得自行改变正式用例、品种、时间、尺度或工作区。允许在锁定范围内做局部诊断，但局部结果不能替代正式运行结果。若正式范围不可运行，报告阻断和方案，等待 Owner 决定。

## 4. 专业来源

采用：

- `control-v0.3/`；
- `skills/feature-understanding/` 及业务对象判别补充；
- `feature-global-behavior-profiling`；
- `business-discrepancy-diagnosis`；
- 只有本轮确实需要正式标定时才采用 `feature-instance-calibration`；
- `STATISTICS_DRIVEN_PRACTICE.md`。

历史 Chat 是 Owner prompt、思考过程和已知问题来源；当前代码、参数和运行结果仍须精确绑定：

- `ai_chat/根据统计找不合理点/WALL 特征：统计线闭环.md`；
- `ai_chat/根据统计找不合理点/F特征：统计线闭环.md`；
- `ai_chat/根据统计找不合理点/wall特征，修frp代码.md`。

## 5. 已锁定的 WALL 代码版本

```text
branch: codex/wall-output-consistency-20261121
commit: 6618d4d147d6ebbe634e61facddf2c9a0b996982
```

该提交包含 D1、D2、D4 的修复链。新 Run 仍须核对实例、参数、数据和最终统计；远端提交存在不等于本特征已经通过释放 Gate。

## 6. 修改确认边界

Codex 可以直接运行、统计、分析、形成复现和修改方案。任何新的正式代码、参数、配置、业务规则、数据处理或范围修改，必须先形成 `ModificationProposal` 并经 Owner 确认；确认后才实施和采用。

此前已经由 Owner 确认并提交的 WALL D1、D2、D4，以及 Owner 后续提供并锁定的 F 新参数实例，属于当前输入，不重复确认。

## 7. Feature 理解复用

Owner 不需要先整理上一次运行的理解材料。执行 AI 从已有 WALL FeatureUnderstandingPackage、归档 Chat、旧运行产物和当前源码出发，只补本轮变化相关的最小差异；不得把“完整重做一遍理解包”设成启动前提。

## 8. 运行 profile

两个基础 Run 均采用：

```yaml
execution_profile: CODEX_NATIVE_DIRECT
manager: Codex new thread per run
executor: Codex new thread per run
workers: []
```

WALL、F 使用上表中不同且不重叠的 Linux 工作区。主控按现有多 Run 控制器交错推进。

## 9. 当前仍需补齐

- 两个真实 `run_id` 与正式 GO；
- WALL 的精确构造／执行入口、参数实例绑定和是否复用已有最终结果包（由锁定 EAW 用例和当前代码解析，不要求 Owner重新整理业务理解）；
- F 新参数实例的字段、值、配置文件、代码版本和 SHA；
- WALL 完整下游 Feature 图；
- 允许提交／推送／写缓存的真实 grants。
