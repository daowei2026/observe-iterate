# TASK_PROGRESS｜统计驱动 Feature 闭环

> 仅在真实 GO 后复制到 `longrun/runs/<run_id>/business_control/TASK_PROGRESS.md`。本模板没有完成事实。

## A. 身份与来源

- `run_id`：
- `work_id / business_case_id`：
- Owner GO：
- 采用 control／Skill／实践补充：
- execution profile：
- manager / executor 物理绑定：
- Linux workspace / verified realpath：
- snapshot status：`current / stale / not_yet_verified`

## B. 当前任务

| 项目 | 当前有据状态 | 精确引用／恢复条件 |
|---|---|---|
| CurrentReviewTarget | | |
| 必须完成与明确非目标 | | |
| Feature 代码 | | |
| 参数实例 | | |
| 数据范围与日历 | | |
| 整体状态 | `incomplete / complete / stopped_with_unmet_requirements` | |
| 下一合法动作 | | |

## C. 闭环节点

| 节点 | 当前输入版本 | 状态 | 当前有效产物 | 未完成／失效条件 | 精确引用 |
|---|---|---|---|---|---|
| U 共享理解 | | | | | |
| X 实例运行 | | | | | |
| G 全量统计 | | | | | |
| D 偏差诊断 | | | | | |
| FI 工程修正（适用时） | | | | | |
| P 参数处理（适用时） | | | | | |
| Release | | | | | |

## D. Finding Register

| finding_id | observation | 当前状态 | 直接责任点／路由 | 最新证据 | 下一动作 |
|---|---|---|---|---|---|
| | | `CANDIDATE / DIAGNOSIS_IN_PROGRESS / CONFIRMED / FIX_IN_PROGRESS / FIXED_PENDING_RERUN / CLOSED_ON_LATEST_PROFILE / DEFERRED_BY_SCOPE / REJECTED_AS_NON_ISSUE / SUPERSEDED` | | | |

## E. 已知限制

| limitation_id | 初始 ReviewTarget 范围依据 | 业务／下游影响 | 为什么当前不阻断 | 返回条件 | 精确引用 |
|---|---|---|---|---|---|
| | | | | | |

## F. Release

- `FeatureReleaseGate`：`BLOCKED / OPEN_CONFIRMED_DEFECT / RERUN_REQUIRED / PASS_WITH_ACCEPTED_LIMITATIONS / PASS`
- 最新运行结果：
- 最新全量统计：
- `UpstreamReleasePackage`：
- 下游消费者：
- 使 Release 失效的变化：

## G. 本次更新

- 新事实：
- 受影响节点和历史成果：
- 保留／复用／重验：
- 下一 Skill D、原 D 续接或等待条件：
