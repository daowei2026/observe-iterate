# TASK_PROGRESS｜统计驱动 Feature 闭环（机器状态与恢复）

> 仅在真实 GO 后复制至 `longrun/runs/<run_id>/business_control/TASK_PROGRESS.md`，不表示已有完成事实。
> **此文件主要服务运行协调、精确版本与合法恢复；人类业务阅读入口是 [BUSINESS_PROGRESS.md](BUSINESS_PROGRESS.md)。**
> 两文件均由 manager 投影真实成果，不另立专业事实库或重复专业结论。

## A. Run 身份、版本和绑定

- `run_id / work_id / business_case_id`：
- Owner 初始 GO / `CurrentReviewTarget`：
- 当前采用 control / Skill / 补充的 exact commit：
- execution profile：
- manager / executor 逻辑身份与物理绑定：
- Linux workspace / verified realpath：
- snapshot status：`current / stale / not_yet_verified`
- 业务阅读文件：`business_control/BUSINESS_PROGRESS.md`

## B. 当前正式实例和流程状态

| 项目 | 机器状态／当前版本 | 精确引用／必要的恢复条件 |
|---|---|---|
| Feature 代码／constructor／参数 | | |
| 数据范围／日历／结果身份 | | |
| 首轮或后续轮次 | | |
| 父 Run 整体状态 | `incomplete / complete / stopped_with_unmet_requirements` | |
| 当前在途 C／D／角色 | | |
| 下一合法动作 | | |

## C. 当前有效节点结果及失效

| 节点 | 有效输入版本 | 状态 | 原生结果准确引用 | 待办、失效或继续条件 |
|---|---|---|---|---|
| U Feature 理解 | | | | |
| X 正式运行／读回 | | | | |
| G 全量统计与发现 | | | | |
| D 偏差诊断 | | | | |
| 实际修正与回归（适用时） | | | | |
| Release | | | | |

> 节点名称不要求对每次命令、内部检查另建工作项。条件分支不是独立 Skill。

## D. Finding 索引（不重复业务分析正文）

| finding_id | 状态 | 责任逻辑／原生产物引用 | 最新回归版本 | 下一合法动作 |
|---|---|---|---|---|
| | `CANDIDATE / DIAGNOSIS_IN_PROGRESS / CONFIRMED / FIX_IN_PROGRESS / FIXED_PENDING_RERUN / CLOSED_ON_LATEST_PROFILE / DEFERRED_BY_SCOPE / REJECTED_AS_NON_ISSUE / SUPERSEDED` | | | |

> 完整的「为什么不合理、如何解决、实际业务效果」放在 BUSINESS_PROGRESS，技术原始依据保留在对应 Skill 产物中。
>
> `FIXED_PENDING_RERUN` 不能算关闭，必须在修改后的当前正式实例及完整统计验证后，才可进入 `CLOSED_ON_LATEST_PROFILE`。`DEFERRED_BY_SCOPE` 只允许初始 `CurrentReviewTarget` 明确为非阻断范围外问题时使用，不是执行者自行降低完成条件的方式。`OWNER_RAISED` 表示初始任务输入提出的候选来源，不产生运行中的 Owner 审批。

## E. Release / 依赖 / 已知限制

- `FeatureReleaseGate`：`BLOCKED / OPEN_CONFIRMED_DEFECT / RERUN_REQUIRED / PASS_WITH_ACCEPTED_LIMITATIONS / PASS` 或未形成
- 当前 `UpstreamReleasePackage`：
- 下游依赖／需失效的消费版本：
- 已知限制原件及是否为初始 ReviewTarget 明确允许的范围外项：
- 最新有效结果与统计 refs：

## F. 本次恢复快照与业务视图同步

- 新取得并验证的回交与动作事实：
- 保留／复用／重验的旧产物：
- 阻断、UNKNOWN、写面冲突或缺证据的具体范围：
- 下一 D / 原 D 续接 / 等待条件：
- BUSINESS_PROGRESS 同步到的业务依据与版本：
- 本次更新时间：

> 同一业务事实变更应更新两个文件相应视图；业务视图生成或 Git 提交失败时记录待同步，不得据此伪造专业完成，不必停下已授权的独立业务工作。
