# 方法探索项目采用状态

当前状态：**BI-01-CO-04 首项 `CASE_OBSERVATION` 已完成第一次有效 Professional 调用。R0008 管理接收 visibility replay 的真实出口 `BLOCKED_NO_LOOKAHEAD_PROOF`：物理 prefix 与 batch 执行可审计，但 native event-level first-seen／publish／revision 不可证明。该技术路线已关闭；管理采用范围受限的 `QUERY_COMPLETION_ASOF_V1` 并签发原 Professional 的 same-work continuation。实际续发和首个业务循环尚未被证明。**

- 专业及运行仓：`daowei2026/observe-iterate`
- 有权分支：`fy/feature-based-case-observation`
- `work_id`: `BI-01`
- `run_id`: `BI-01-CO-04`
- 首次管理采用：`runs/BI-01-CO-04/reviews/management-R0001/DECISION.md`
- Reader 接收：`runs/BI-01-CO-04/reviews/management-R0004/DECISION.md`
- 首轮 Professional：`runs/BI-01-CO-04/artifacts/R0005/REPORT.md`
- 首轮专业接收：`runs/BI-01-CO-04/reviews/management-R0006/DECISION.md`
- 旧 run 恢复包：`runs/BI-01-CO-04/artifacts/worker-BI01CO04-INPUT-RECOVERY-01/`
- Visibility replay：`runs/BI-01-CO-04/artifacts/worker-BI01CO04-ASOF-VISIBILITY-REPLAY-01/`
- Replay 管理接收：`runs/BI-01-CO-04/reviews/management-R0008/DECISION.md`
- Professional continuation：`runs/BI-01-CO-04/reviews/management-R0008/PROFESSIONAL_CONTINUATION.md`
- Run 入口：`runs/BI-01-CO-04/README.md`
- 长程地图：`runs/BI-01-CO-04/00_长程推进地图.md`
- 当前任务：`runs/BI-01-CO-04/01_当前任务.md`
- 当前 mode：`CASE_OBSERVATION`
- Workmap Binding：`runtime/config/WORKMAP_BINDING.json`
- 当前 Intake：`runs/BI-01-CO-04/reviews/WORKMAP_INTAKE_CURRENT.json`

## 已采用与已接收

R0001 的完整业务目标和当前专业任务继续有效。R0005 的 `INPUT_UNQUALIFIED_FOR_ASOF_COMPARISON`、R0007 对旧 run 的 `DIAGNOSTIC_BASELINE_NOT_ASOF_INPUT` 降级，以及 R0008 对 event-level native visibility 的阻断均保留。

R0008 接受 replay package 的技术事实：冻结至 `2021-09-30 15:00 Asia/Shanghai` 的 rb／hc／i 30m 物理前缀、big／mid 六组 batch 执行、源码／参数／环境、边界审计、baseline、failure injection、receipt 和 validator 可核；没有证据支持逐事件 first-seen、撤回／重现或旧生产 publish time。`physical_prefix_bound_passed=true` 不等于 event-level no-lookahead proof。

管理不再派发同类 Worker。当前采用 `QUERY_COMPLETION_ASOF_V1`：决策者只用截至固定 cutoff 的物理前缀运行冻结 batch，query 完成后返回的 snapshot 是该次决策信息。它可以测试当前特征在 on-demand query workflow 中的选择价值，但不能证明旧生产系统历史实时发布。

## 当前直接动作

主控记录当前 Workmap snapshot，使用现有 `01_当前任务.md`、R0008 `#professional-release` 和 `PROFESSIONAL_CONTINUATION.md` 运行 pre-dispatch，通过后向原 Professional 实际发送。

唯一 cutoff 已锁定为 `2021-09-30 15:00 Asia/Shanghai`；三品种、30m、big／mid、参数、几何代理公式和 bounded future tail 均不可根据结果改变。Professional 必须先冻结候选／排序／无候选与未来过程，再读 T 后行情并交最近自然挑战和方法反馈。

## 未被本状态证明

本状态不证明：

- Professional continuation 已实际发送或第二次有效调用已发生；
- 已有候选、排序或市场无候选；
- 中尺度具有或不具有独立选择增量；
- 旧系统的 `event_ts`、`xConfirm` 或任何对象具有历史原生 publish／known-time；
- query-completion 结论可外推为实时流式部署能力；
- 首个业务循环、独立专业审查、管理业务 Gate 或 Owner 接收已经通过。

这些事实分别在 Professional 派发／回交、业务实物和后续管理决定中记录。

## 连续性与投入边界

旧 CO Run、U2／U3、I2—I6、历史图、旧聊天、旧预算和旧 Gate 只按准确来源定向使用。当前 `known_pro_turns=1`；Worker 不计入 Professional 调用预算。`FIRST_USABLE_ASOF_LOOP=NOT_YET`、`MATERIAL_INPUT_OR_METHOD_CHANGE=SATISFIED_AND_CONSUMED_BY_R0008`、`ACTIVE_WORK_EFFORT_REVIEW=NOT_YET`。R0008 continuation 是第二次有效调用；若仍无业务主体，必须执行 EFFORT 复看，不得回到技术来源循环。
