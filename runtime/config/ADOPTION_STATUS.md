# 方法探索项目采用状态

当前状态：**BI-01-CO-04 首项 `CASE_OBSERVATION` 已真实派发并完成第一次有效 Professional 调用。R0006 管理限域接收 `INPUT_UNQUALIFIED_FOR_ASOF_COMPARISON`；原业务问题继续 ACTIVE。最小正式输入恢复工单已签发，Worker 实际发送、数据恢复和首个 as-of 业务循环尚未被证明。**

- 专业及运行仓：`daowei2026/observe-iterate`
- 有权分支：`fy/feature-based-case-observation`
- `work_id`: `BI-01`
- `run_id`: `BI-01-CO-04`
- 首次管理采用：`runs/BI-01-CO-04/reviews/management-R0001/DECISION.md`
- Reader 接收：`runs/BI-01-CO-04/reviews/management-R0004/DECISION.md`
- 首轮 Professional：`runs/BI-01-CO-04/artifacts/R0005/REPORT.md`
- 首轮专业接收：`runs/BI-01-CO-04/reviews/management-R0006/DECISION.md`
- 最小恢复工单：`runs/BI-01-CO-04/reviews/management-R0006/WORKER_ORDER.md`
- Run 入口：`runs/BI-01-CO-04/README.md`
- 长程地图：`runs/BI-01-CO-04/00_长程推进地图.md`
- 当前任务：`runs/BI-01-CO-04/01_当前任务.md`
- 当前 mode：`CASE_OBSERVATION`
- Workmap Binding：`runtime/config/WORKMAP_BINDING.json`
- 当前 Intake：`runs/BI-01-CO-04/reviews/WORKMAP_INTAKE_CURRENT.json`

## 已采用与已接收

R0001 建立的完整业务目标和当前专业任务仍是唯一业务工作面。R0004 接收的 Reader `PASS` 只覆盖派发前工作面。R0005 已真实执行并准确报告：当前通道没有取得可构造 T 时已知集合的正式行情、特征对象、actual／confirm 时间和运行身份字节；因此不能形成候选、排序或市场无候选。

R0006 接收该输入资格否定及最小恢复条件，但不接收任何市场或方法结论。管理已签发 `BI01CO04-INPUT-RECOVERY-01`，只恢复 rb／hc／i、30m 历史候选窗口所需的 run 身份、实际参数、行情、大／中尺度对象、时间语义和不可变 receipt。结构化 P0 为承重；静态图只作辅助。

## 当前直接动作

主控对 exact `WORKER_ORDER.md` 运行 Worker-order preflight，通过后向 Owner 指定线程 `01a17dd7-5033-7e63-b7a2-edd90b691c33` 实际发送并核 workspace `/dwdhome/fy/cgpterm`。Worker 结果先回管理做技术接收；P0 包合格后，原 Professional 以 same-work／`EXISTING_AUTHORIZED_REPAIR` 继续现有问题，不增加第二 Reader、不重做 R0005 已成分析。

## 未被本状态证明

本状态不证明：

- Worker 工单已实际发送、执行或数据已恢复；
- 历史 run、图面、参数或页面已经成为本 Run 正式输入；
- 已选合法 T、已有候选／排序／市场无候选；
- 中尺度具有或不具有独立选择增量；
- 首个业务循环、后续独立专业审查、管理业务 Gate 或 Owner 接收已经通过。

这些事实分别在 Worker 派发／回交、Professional continuation、业务实物和后续管理决定中记录，不用“工单已签发”或“输入缺失”替代。

## 连续性与投入边界

旧 CO Run、U2／U3、I2—I6、历史图、旧聊天、旧预算和旧 Gate 仅按准确来源定向使用，不取得本 Run 当前权力。当前 `known_pro_turns=1`；Worker 不计入 Professional 调用预算。三个原管理触发均为 `NOT_YET`。包到位前不消耗第二次 Professional 调用；若第二次有效调用仍无业务主体，必须执行 EFFORT 复看并改变实际安排。
