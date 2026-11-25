# 统计驱动的单 Feature 闭环｜当前 Control

本目录只有一份现行 Workflow 正文：[01_L0_统计驱动的单特征闭环.md](01_L0_统计驱动的单特征闭环.md)。

## 1. 当前任务如何运行

```text
首轮：U 理解 Feature → X 正式运行 → G 全量统计和高置信问题发现
                                   ↓ 有待处理 finding
                             D 逐项诊断、必要修正
                                   ↓ 正式行为／绑定发生变化
后续轮次：根据影响更新有效成果，取得当前正式运行及全量统计
                                   ↓ 当前目标已完成
                    完成判断 → FeatureReleaseGate → 下游
```

finding 是否待处理属于流程判断，**不是独立的 Q 工作节点**；修正代码／参数、修正绑定以及完成释放也不需要为每类动作另建专业 Skill。轮次不等于 Chat 调用次数或 finding 数，AI 不需要按每个问题重跑一次全量实例。

## 2. 工作与原 Skill

| 工作 | 专业方法与产出 |
|---|---|
| U Feature 理解 | `skills/feature-understanding/SKILL.md` 与业务对象判别补充；形成 `FeatureUnderstandingPackage` |
| X 正式运行 | 实际工程操作；形成当前实例的 `FeatureRunResultBinding` |
| G 全量统计／发现 | `feature-global-behavior-profiling` 和 `STATISTICS_DRIVEN_PRACTICE.md`；形成统计、发现与专业 Gate |
| D 偏差诊断（按需） | `business-discrepancy-diagnosis`；形成诊断及责任逻辑定位 |
| 参数标定（仅明确需要时） | `feature-instance-calibration` |

**Control 只组织工作，不重写 Skill 的内部步骤和专业完成条件。** 具体 Feature 的品种、版本、参数、范围与依赖来自 `task-inputs/` 及初始 GO。

## 3. 完成与运行记录

当前目标的完成、可释放状态、精确上游 `UpstreamReleasePackage`、下游版本失效及边界，统一见 L0 第 4～5 节。多 Run 并行与联合依赖按 `longrun/` 和具体任务输入，不另建专业上级。

运行期间，由 manager 按本专业 Workflow 采用的 [统计闭环业务进展模板](../longrun/templates/BUSINESS_PROGRESS_STATISTICS_CLOSURE.md) 与 [统计闭环恢复模板](../longrun/templates/TASK_PROGRESS_STATISTICS_CLOSURE.md) 维护：

- `longrun/runs/<run_id>/business_control/BUSINESS_PROGRESS.md`：业务进展、问题处理及有效成果；
- `longrun/runs/<run_id>/business_control/TASK_PROGRESS.md`：机器状态、版本、依赖、在途和恢复。

初始 GO 一次性明确自主迭代权限；运行中不设置 Owner 审批节点。授权之外的操作只阻断受影响部分，不擅自扩大范围。

## 4. 历史与非目标

原 V0.2 的观察材料、CAEGraph、真实场景及对照流程保留在 Git 历史；**不作为本 Control 的自动后继**。历史 Run 仍以各自已采用的精确 commit 为准，新分支不追认或改写旧结果。原 `control-v0.3/` 路径属于历史版本；当前从 `control/` 读取。
