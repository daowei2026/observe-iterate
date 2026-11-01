# BI-01-CO-04｜基于既有特征的业务用例探索

<a id="common"></a>
## Common

- `run_id`: `BI-01-CO-04`
- `work_id`: `BI-01`
- Owner GO：`runs/BI-01-CO-04/OWNER_START.md`
- 管理者：`chatgpt:BI-01-CO-04:management`
- 当前阶段：首项 Professional 已完成一次有效调用；R0008 已接收 visibility replay 的真实出口 `BLOCKED_NO_LOOKAHEAD_PROOF`，关闭 native event-level known-time 技术路线，并采用 `QUERY_COMPLETION_ASOF_V1`。原业务问题继续 ACTIVE；same-work Professional continuation 已签发，尚未把签发写成实际发送或业务结果。
- 动态正本：
  - [长程推进地图](00_长程推进地图.md)
  - [当前正式任务](01_当前任务.md)
  - [R0008 管理决定](reviews/management-R0008/DECISION.md)
  - [R0008 Professional continuation](reviews/management-R0008/PROFESSIONAL_CONTINUATION.md)
  - [Workmap Intake](reviews/WORKMAP_INTAKE_CURRENT.json)

本 Run 独立于旧 CO 运行。历史图、旧任务、旧 Gate、旧聊天、旧预算和旧结论不自动取得本 Run 的采用或在途资格。专业背景在 `professional/exploration/`，它提供目标、能力、当前设想、工具与 Owner 过程，不替代本 Run 当前任务。

<a id="bi01"></a>
## BI01

完整目标是利用既有大／中／小尺度贴近点及其关系，逐步形成可验证的前瞻选择认识：在当时可知的信息下识别哪些品种更值得继续观察、目标是哪种后续市场过程，并允许诚实结论为“没有可靠候选”。

当前正式任务仍为 `BI-01-CO-04-CASE-INITIAL-ASOF`，mode 为 `CASE_OBSERVATION`。R0005 的输入资格否定、R0007 对旧 run 的降级和 R0008 对 native event-level visibility 的阻断均被保留。Replay 已证明冻结至 `2021-09-30 15:00 Asia/Shanghai` 的三品种 30m 物理前缀可独立执行且不读取前缀外行情，但不能证明对象在 prefix 内的原生 first-seen／publish／revision 生命周期。

管理现采用范围受限的 `QUERY_COMPLETION_ASOF_V1`：只把截至固定 T 的物理前缀送入冻结 batch 引擎，查询完成后返回的 big／mid snapshot 是本次决策可用状态；它不声称旧生产系统曾逐事件实时发布。唯一 cutoff、几何代理公式、future tail 和禁止挑选规则已在 R0008 预先锁定。

当前直接后继是主控记录当前 Workmap snapshot、运行 pre-dispatch，并向原 Professional 发送 `PROFESSIONAL_CONTINUATION.md`。Professional 必须直接形成固定 snapshot 下的候选／排序／无候选、未来评价、自然挑战和方法反馈；不得再开启 Worker、Reader 或 native known-time 来源循环。
