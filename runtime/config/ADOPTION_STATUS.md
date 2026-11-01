# 方法探索项目采用状态

当前状态：**BI-01-CO-04 首项 `CASE_OBSERVATION` 已完成第一次有效 Professional 调用。R0007 管理接收首个 Worker 包为 `PARTIAL_BLOCKED_FOR_ASOF` 技术基线：字节、参数、行情、大／中对象、图面与 receipt 已恢复，但 old run 的首次可知性、方向、生命周期和时间合同不合格。原业务问题继续 ACTIVE；新 visibility replay 工单已签发，实际发送、重放资格和首个 as-of 业务循环尚未被证明。**

- 专业及运行仓：`daowei2026/observe-iterate`
- 有权分支：`fy/feature-based-case-observation`
- `work_id`: `BI-01`
- `run_id`: `BI-01-CO-04`
- 首次管理采用：`runs/BI-01-CO-04/reviews/management-R0001/DECISION.md`
- Reader 接收：`runs/BI-01-CO-04/reviews/management-R0004/DECISION.md`
- 首轮 Professional：`runs/BI-01-CO-04/artifacts/R0005/REPORT.md`
- 首轮专业接收：`runs/BI-01-CO-04/reviews/management-R0006/DECISION.md`
- 首个 Worker 包：`runs/BI-01-CO-04/artifacts/worker-BI01CO04-INPUT-RECOVERY-01/`
- Worker 技术接收：`runs/BI-01-CO-04/reviews/management-R0007/DECISION.md`
- 新重放工单：`runs/BI-01-CO-04/reviews/management-R0007/WORKER_ORDER.md`
- Run 入口：`runs/BI-01-CO-04/README.md`
- 长程地图：`runs/BI-01-CO-04/00_长程推进地图.md`
- 当前任务：`runs/BI-01-CO-04/01_当前任务.md`
- 当前 mode：`CASE_OBSERVATION`
- Workmap Binding：`runtime/config/WORKMAP_BINDING.json`
- 当前 Intake：`runs/BI-01-CO-04/reviews/WORKMAP_INTAKE_CURRENT.json`

## 已采用与已接收

R0001 建立的完整业务目标和当前专业任务仍是唯一业务工作面。R0005 的 `INPUT_UNQUALIFIED_FOR_ASOF_COMPARISON` 仍是准确专业边界。

R0007 只接收首个 Worker 包的技术范围：旧 run 身份、实际参数消费、rb／hc／i 30m 行情、大／中对象、静态图、逐文件 receipt 和 blocker 可追溯；`byte_gate=PASS`。同时接收 `asof_semantic_gate=BLOCKED`：时间轴冲突、known-time 无证明、方向／生命周期缺失和历史 build 不完整，使旧 run 不能直接承担 T 时已知输入。

`MATERIAL_INPUT_OR_METHOD_CHANGE` 已在输入路线层面满足并由 R0007 消费。旧 `GTQH_C001_three_turns_20261101_162005` 降级为 `DIAGNOSTIC_BASELINE_NOT_ASOF_INPUT`；这不等于特征方法失败或市场无候选。

## 当前直接动作

主控对 `BI01CO04-ASOF-VISIBILITY-REPLAY-01` 运行 Worker-order preflight，通过后向 actual Worker thread `01a19881-cebf-73f3-a4d3-76c57bce0fe4` 实际发送并核 workspace `/dwdhome/fy/cgpterm`。新工单只做三品种、30m、同窗口的新命名顺序重放，冻结真实源码／参数，记录 first-seen 生命周期，并执行 prefix invariance、未来尾部扰动、instrumentation neutrality 和失败注入。

结果先回管理。只有管理接收 `QUALIFIED_FOR_PROFESSIONAL_ASOF`，原 Professional 才以 same-work continuation 执行第二次有效调用；不增加第二 Reader、不重复 R0005 已成输入边界。

## 未被本状态证明

本状态不证明：

- 新 Worker 工单已实际发送、执行或 replay 已形成；
- 旧正式 slice、`event_ts`、`xConfirm`、calendar time 或 bar time 已取得 operational known-time 资格；
- 已选合法 T、已有候选／排序／市场无候选；
- 中尺度具有或不具有独立选择增量；
- 首个业务循环、后续独立专业审查、管理业务 Gate 或 Owner 接收已经通过。

这些事实分别在 Worker 派发／回交、Professional continuation、业务实物和后续管理决定中记录，不用技术包、validator 或重放工单签发代替。

## 连续性与投入边界

旧 CO Run、U2／U3、I2—I6、历史图、旧聊天、旧预算和旧 Gate 仅按准确来源定向使用，不取得本 Run 当前权力。当前 `known_pro_turns=1`；Worker 不计入 Professional 调用预算。`FIRST_USABLE_ASOF_LOOP=NOT_YET`、`MATERIAL_INPUT_OR_METHOD_CHANGE=SATISFIED`、`ACTIVE_WORK_EFFORT_REVIEW=NOT_YET`。新重放只允许一次有限执行；若出口为 `BLOCKED_NO_LOOKAHEAD_PROOF`，不再重复同类来源搜索。
