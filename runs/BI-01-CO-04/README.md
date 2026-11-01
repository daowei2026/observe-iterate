# BI-01-CO-04｜基于既有特征的业务用例探索

<a id="common"></a>
## Common

- `run_id`: `BI-01-CO-04`
- `work_id`: `BI-01`
- Owner GO：`runs/BI-01-CO-04/OWNER_START.md`
- 管理者：`chatgpt:BI-01-CO-04:management`
- 当前阶段：首项 Professional 已完成一次有效调用；R0007 已接收首个 Worker 包为 `PARTIAL_BLOCKED_FOR_ASOF` 技术基线，并确认旧 run 不能直接承担严格 as-of 输入。原业务问题继续 ACTIVE；可知性顺序重放工单已签发，尚未把签发写成实际发送或重放完成。
- 动态正本：
  - [长程推进地图](00_长程推进地图.md)
  - [当前正式任务](01_当前任务.md)
  - [R0007 管理决定](reviews/management-R0007/DECISION.md)
  - [R0007 可知性重放工单](reviews/management-R0007/WORKER_ORDER.md)
  - [Workmap Intake](reviews/WORKMAP_INTAKE_CURRENT.json)

本 Run 独立于旧 CO 运行。历史图、旧任务、旧 Gate、旧聊天、旧预算和旧结论不自动取得本 Run 的采用或在途资格。专业背景在 `professional/exploration/`，它提供目标、能力、当前设想、工具与 Owner 过程，不替代本 Run 当前任务。

<a id="bi01"></a>
## BI01

完整目标是利用既有大／中／小尺度贴近点及其关系，逐步形成可验证的前瞻选择认识：在当时可知的信息下识别哪些品种更值得继续观察、目标是哪种后续市场过程，并允许诚实结论为“没有可靠候选”。

当前正式任务仍为 `BI-01-CO-04-CASE-INITIAL-ASOF`，mode 为 `CASE_OBSERVATION`。R0005 的输入资格否定仍成立。R0007 进一步确认：旧 run 的行情、参数、大／中对象和 receipt 均已真实恢复，但 known-time、方向、对象生命周期与唯一时间合同仍不成立；因此没有合法 T、候选排序或市场无候选。

当前直接后继是执行 `BI01CO04-ASOF-VISIBILITY-REPLAY-01`：只在 rb／hc／i、30m、同一窗口内建立新命名、源码／参数冻结、逐事件 first-seen 与生命周期可审计的顺序重放包，并通过 prefix invariance、未来尾部扰动和失败注入。只有管理接收 `QUALIFIED_FOR_PROFESSIONAL_ASOF` 后，原 Professional 才继续同一问题；不增加第二 Reader、不重做 R0005 已成分析、不把旧图或字节 PASS 冒充业务结论。
