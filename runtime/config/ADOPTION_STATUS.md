# 方法探索项目采用状态

当前状态：**BI-01-CO-04 已完成 2 次有效 Professional 调用。R0010 接收 R0009 的固定 query snapshot `NO_CANDIDATE` 为合格负向业务判断，但 held-out tail 尚未运输，因此首个完整 as-of loop 未完成。`ACTIVE_WORK_EFFORT_REVIEW` 已满足并由 R0010 消费；一次 pure frozen-tail transport 已签发，当前 Case 随后只允许一次 tail-only Professional closure 并硬停止。**

- 专业及运行仓：`daowei2026/observe-iterate`
- 有权分支：`fy/feature-based-case-observation`
- `work_id`: `BI-01`
- `run_id`: `BI-01-CO-04`
- 首次管理采用：`runs/BI-01-CO-04/reviews/management-R0001/DECISION.md`
- Reader 接收：`runs/BI-01-CO-04/reviews/management-R0004/DECISION.md`
- 第一次 Professional：`runs/BI-01-CO-04/artifacts/R0005/REPORT.md`
- 第二次 Professional：`runs/BI-01-CO-04/artifacts/R0009/REPORT.md`
- R0009 snapshot：`runs/BI-01-CO-04/artifacts/R0009/QUERY_SNAPSHOT_STATE_TABLE.csv`
- R0009 冻结决定：`runs/BI-01-CO-04/artifacts/R0009/DECISION_FREEZE.json`
- R0010 投入复看：`runs/BI-01-CO-04/reviews/management-R0010/DECISION.md`
- Frozen-tail 工单：`runs/BI-01-CO-04/reviews/management-R0010/WORKER_ORDER.md`
- Run 入口：`runs/BI-01-CO-04/README.md`
- 长程地图：`runs/BI-01-CO-04/00_长程推进地图.md`
- 当前任务：`runs/BI-01-CO-04/01_当前任务.md`
- 当前 mode：`CASE_OBSERVATION`
- Workmap Binding：`runtime/config/WORKMAP_BINDING.json`
- 当前 Intake：`runs/BI-01-CO-04/reviews/WORKMAP_INTAKE_CURRENT.json`

## 当前采用与已接收范围

R0001 的完整业务目标和当前任务继续有效。R0005 的输入资格否定、R0007 对旧 run 的降级、R0008 对 native event-level visibility 的阻断及 `QUERY_COMPLETION_ASOF_V1` 当前 Case 合同均保留。

R0010 接收 R0009 的 snapshot 业务认识：

- rb 与 hc 是唯一共同 big `HIGH_CONFIRMED_PROXY` pair；
- i 的 big proxy 不同，不进入同背景比较；
- rb／hc latest returned mid occurrence 同号且差异很浅；
- 在不发明新规则、不偷看未来的条件下，没有合法候选或排序；
- `NO_CANDIDATE` 是 snapshot 业务输出，不是输入失败。

R0010 不接收 outcome 支持／反证、最近自然挑战、mid 一般有效／无效、任何未来方向或首个完整 loop。原因是固定 `(2021-09-30 15:00, 2021-10-15 15:00]` 三品种 30m tail 尚未进入封口交付。

## 当前直接动作

主控对 `BI01CO04-FROZEN-TAIL-TRANSPORT-01` 运行 Worker-order preflight，通过后向既有 actual Worker thread `01a19881-cebf-73f3-a4d3-76c57bce0fe4` 发送并核 workspace `/dwdhome/fy/cgpterm`。

工单只允许从已核同一 GTQH source input 提取 cutoff anchor 与固定 held-out tail，交 timestamp／close、source identity、receipt、validator 和冻结公式的机械指标。禁止 feature 重算、换源、改 T、改阈值、改品种或作业务解释。

出口仅为 `TAIL_PACKAGE_READY` 或 `TAIL_SOURCE_INACCESSIBLE`。管理接受 A 后签一次 tail-only Professional continuation；出口 B 则当前 Case 以 `SNAPSHOT_DECISION_VALID__OUTCOME_UNVERIFIED` 停止，不签第二个 tail Worker。

## 旧要求撤销与保留

撤销 R0008 中过宽的 “No Worker may be inserted” 及地图中的“不得再派第三个 Worker”。该表述错误地把直接 held-out 数据运输与已关闭的技术研究混为一谈。

继续有效：

- `NO_FURTHER_NATIVE_VISIBILITY_WORKER`；
- 不再做 first-seen／publish／revision、feature replay、旧文件搜索、全市场重算或参数寻优；
- 本次 tail transport 完成或阻断后，其技术职责退出；
- 当前 cutoff、snapshot、`NO_CANDIDATE`、目标过程、指标和 5pp Case-only challenge line 不得改写。

## 未被本状态证明

本状态不证明：

- frozen-tail Worker 已实际发送、执行或交付；
- R0009 `NO_CANDIDATE` 得到后续市场支持或被反证；
- 中尺度具有或不具有一般选择增量；
- 首个完整 loop、独立专业审查、Owner 接收或方法稳定性已通过；
- query-completion 结论可外推为实时流式部署能力。

## 连续性与投入边界

当前 `known_pro_turns=2`，原起点累计 `8.1462` 小时。`FIRST_USABLE_ASOF_LOOP=NOT_YET`、`MATERIAL_INPUT_OR_METHOD_CHANGE=NOT_YET`、`ACTIVE_WORK_EFFORT_REVIEW=SATISFIED_AND_CONSUMED_BY_R0010`。

允许新增投入仅为 1 次 pure tail transport 和 1 次 tail-only Professional closure；closure 后当前 Case 硬停止，不建立新的两调用等待周期。后续相邻 Case 必须在派发 Professional 前把 snapshot input 与 held-out tail 成套封口，禁止重复数据可得性循环。
