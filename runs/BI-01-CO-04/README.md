# BI-01-CO-04｜基于既有特征的业务用例探索

<a id="common"></a>
## Common

- `run_id`: `BI-01-CO-04`
- `work_id`: `BI-01`
- Owner GO：`runs/BI-01-CO-04/OWNER_START.md`
- 管理者：`chatgpt:BI-01-CO-04:management`
- 当前阶段：R0009 已完成第 2 次有效 Professional 调用并形成固定 query snapshot 下的合格 `NO_CANDIDATE`；R0010 已消费 `ACTIVE_WORK_EFFORT_REVIEW`。该结果尚未完成 held-out outcome／自然挑战，因此首个完整 loop 仍未接收。一次纯行情尾部运输工单已签发，当前 Case 进入有硬停止的最后闭合段。
- 动态正本：
  - [长程推进地图](00_长程推进地图.md)
  - [当前正式任务](01_当前任务.md)
  - [R0010 管理决定](reviews/management-R0010/DECISION.md)
  - [R0010 frozen-tail Worker 工单](reviews/management-R0010/WORKER_ORDER.md)
  - [Workmap Intake](reviews/WORKMAP_INTAKE_CURRENT.json)

本 Run 独立于旧 CO 运行。历史图、旧任务、旧 Gate、旧聊天、旧预算和旧结论不自动取得本 Run 的采用或在途资格。专业背景在 `professional/exploration/`，它提供目标、能力、当前设想、工具与 Owner 过程，不替代本 Run 当前任务。

<a id="bi01"></a>
## BI01

完整目标是利用既有大／中／小尺度贴近点及其关系，逐步形成可验证的前瞻选择认识：在当时可知的信息下识别哪些品种更值得继续观察、目标是哪种后续市场过程，并允许诚实结论为“没有可靠候选”。

当前正式任务仍为 `BI-01-CO-04-CASE-INITIAL-ASOF`，mode 为 `CASE_OBSERVATION`。`QUERY_COMPLETION_ASOF_V1` 仍只适用于当前 Case：截至固定 cutoff 的物理前缀经冻结 batch 查询完成后，返回的 big／mid snapshot 是决策信息；它不声称旧生产系统逐事件发布。

R0009 已在 future tail 读取前冻结：rb／hc 是唯一共同 big high-proxy pair；二者 latest mid 同号且差异很浅；i 的 big proxy 不同。因此 `NO_CANDIDATE` 被 R0010 接收为 snapshot 业务结论。它不能被推广为 mid 无效，也尚未得到 outcome 支持或反证。

当前直接后继是 `BI01CO04-FROZEN-TAIL-TRANSPORT-01`：只从已核同源 GTQH 30m 输入运输 cutoff anchor 与 `(2021-09-30 15:00, 2021-10-15 15:00]` 的 rb／hc／i close tail，交 receipt 和冻结公式的机械指标；不重算特征、不改变 T、规则或候选。管理接收 tail 后，原 Professional 只做一次 tail-only closure；若 tail 不可恢复，当前 Case 以 `SNAPSHOT_DECISION_VALID__OUTCOME_UNVERIFIED` 停止，不再追加技术链。

R0008 中过宽的“不得再派 Worker”已撤销；保留的现行要求是不得再派 native visibility／first-seen／feature replay／旧来源搜索 Worker。本次 tail transport 完成或阻断后，其技术职责立即退出。
