# BI-01-CO-04 操作主控运行事实

更新时间：2026-11-01T22:43:47.680625+00:00（北京时间 2026-11-02T06:43:47.680625+08:00）。本文件是运行事实的滚动投影；正式业务目标、工作安排和接收结论取 Run README、推进地图、当前任务及有权 Pro 决定。

## 身份与来源

- work_id：BI-01；run_id：BI-01-CO-04。
- Owner GO 原始消息时点：2026-11-01T14:33:16.505Z；原文位于 ../OWNER_START.md，已与原消息逐字核验。
- 操作 controller：cgpterm@86dec991abb27a927c1b5c22af1e51b3f39b918b。
- 专业及运行规则：observe-iterate@b6ccf766dac055a793e75f76b77a73f4cfc74064；动态采用取当前 Run 实际 Git 记录。
- 截至本记录，从 Owner GO 起总经过 29431 秒（约 490 分钟），包含准备、外部等待、操作、收取与恢复；模型队列和实际思考耗时未单独取得。

## 真实 Pro 调用

| R | 角色/责任 | 真实提交 UTC | 已观察完成 UTC | 当前实际结果 |
|---|---|---|---|---|
| R0001 | Management M-START | 14:57:57.942 | 15:25:06.578 | 地图、当前任务、管理决定与回交已取得；历史前缀兼容问题保留原件 |
| R0002 | 原管理的窄补交 | 16:03:23.124 | 16:15:26.561 | 正式 Reader 任务/Binding/采用与准确定位已补齐，after-return 校验通过 |
| R0003 | 独立 Workmap Reader | 16:27:53.201 | 16:39:52.152 | Reader 报告及两份 Return 已收取；R0004已真实接收 |
| R0004 | 原管理接收 Reader | 17:06:51.556 | 17:18:38.290 | 实际接收 Reader、Intake RECORDED，并放行原已签 Professional |
| R0005 | 首次 Professional | 17:35:03.558 | 17:46:54.827 | 输入不合格批完整提交；未形成合法 T、品种排序或 as-of 业务循环 |
| R0006 | 原管理接收首专业批 | 18:33:02.847 | 19:00:56.707 | 限域接收输入资格否定，签发最小恢复工单；不接收市场业务循环 |
| R0007 | 原管理接收第一技术包 | 19:53:18.717 | 20:05:36.173 | 接收诊断基线、消费输入路线变化，保持Professional阻断，签发一次可知性重放 |

| R0008 | 原管理接收重放与业务取舍 | 21:53:21.971 | 22:04:01.932 | 实际接收B出口、关闭native visibility路线，当前Case采用QUERY_COMPLETION_ASOF_V1，放行原专业续作 |
| R0009 | 第二次Professional同任务续作 | 22:22:10.619（首次正面提交实证） | 手机完整待核；远端已完整 | 固定snapshot无候选已先冻结；bounded-tail字节未交付，评价未执行，EFFORT到期 |

这些时点均为 2026-11-01 UTC（后段已进入北京时间11月2日）。提交到观察完成的区间包含监督等待，不能据此分解实际思考耗时。

## 当前资格与后继

- 两个有限Worker单均已真实结束并由原Management接收关闭。第一包dfdf843b47c03c0121fd7151b72f24adb5d986c0为诊断基线；第二包e25e585779152aa670d54c87efecba984af4b7e3为BLOCKED_NO_LOOKAHEAD_PROOF，448项receipt/449项封口hash已由主控独立核验。
- R0008真实接收B出口并关闭同类native event-level visibility技术搜索；未将旧first-seen资格改PASS。仅本Case采用QUERY_COMPLETION_ASOF_V1：固定2021-09-30 15:00前缀，六组query完成后状态可用；方向仅固定几何proxy，先冻结判断再读至2021-10-15的评价tail。
- R0008明确授权主控登记新快照并机械接合字段，93436588999d6af0724348b828a5d899134bb3d3的snapshot及适用check/dispatch实际PASS，复用旧Reader有真实管理理由；R7旧HOLD已被R8合法替代，不再作为当前阻断。
- R0009已向原BI04专业一次实际提交，IME1/Send1/全文exact/Pro最高/控制释放。955UTF8/627UTF16的准确发送凭证a4d46cb32457d778233ce11d0a58a47a36476de8；服务端精确提交事件时刻未暴露，以首次正面实证22:22:10.619Z作监督起点。
- 实际R0009结果2970cd94f74594f9c1f034706ec1332daef0d5da：固定snapshot下NO_CANDIDATE已提交冻结，后续评价因原source一致的bounded-tail行未运输而未执行。不能声称无候选已获市场支持/反证或首完整as-of循环完成。完整原报告及两Return/身份/schema/实物refs通过，原报告逐字归档607423622b584188a814d0f269c9d363b27e16c4。
- Professional有效回交2、实际派发2，完整as-of市场循环仍0。R0009正式EFFORT=SATISFIED，原Management的decide复看责任到期；当前生成R0010精确管理请求，未有R0010手机Sender/IME/Send，不把专业的运输建议当已签Worker工单。
- R0009手机最新22:35:13.354Z仍思考；远端完成后的有界phone grace仍待新鲜完成证据。fresh network6已按22:42:44.795Z到期准入执行NO_SEND，主控不phone/不并行抢锁，不因已收GitHub结果假称手机长答已捕获。
- 当前真实业务后继由原Management按完整目标、已成冻结业务判断、输入缺口与EFFORT作取舍，主控不代签恢复单、不自选业务路线。Owner首版、必要独立业务审查、相邻Case及整体阶段收拢仍未完成。

## 保留的运行限制

- R0001 实际已发送的 invocation/marker/PROMPT 与 Return 保持原字节；旧前缀与 gate 规范化前缀的差异如实保留。R0002及后继使用规范化身份和实际校验。
- Reader 首答后的命名操作持有控制共12分23.7秒，超过原12分钟边界；回交如实记录，没有重复输入或业务 Send。
- 共享网络16:46:18.937Z到期检查延后，已记录 SLO 违约及实际操作/准备/回交成本。16:59:33.070Z重新完成正式准入后才开始 R0004 发送。
- R0005远端完成使观察期限提前，首次动作在原普通期限+120秒内，但超过提前期限+120秒约22秒；两个期限与实际时点均保留。
- R0006发送前主控误记远端基线并过早登记attempt；在任何业务输入前，凭真实零输入终态按既有resume/base-revision修复，原载荷、marker、ready时钟与延误成本均保留。最终新执行器独立核目标/空输入/全文后IME1、Send1；没有重复业务发送。
- Worker备用建立时，两个未提交空白上下文在首次消息前被释放，未产生持久聊天或工程派发；最终持久聊天仅有一次正式工单turn。实际模型证据晚于start回执，待真实turn_context和原生Goal验证后才记已采用。
- R0007观察首动作比原产品时钟SLO晚14.147秒，两套时钟和实际成本均保留。
- R0007接收快照的失效是管理有意保持的专业阻断，主控没有用机械指纹计算替代实际管理采纳。字段格式修复详情见同轮RECEIPT_FORMAT_RECONCILIATION.md。
- 已收取各轮的原始完整报告与两份 Return 保留在 GitHub；手机完整答复、远端报告、Reader结论、管理接收与业务结果分别记录。

## 正本定位

- [Run 入口](../README.md)
- [R0002 管理决定](../reviews/management-R0002/DECISION.md)
- [独立 Reader 原报告](../reviews/independent/workmap-01/REPORT.md)
- [R0004 管理决定](../reviews/management-R0004/DECISION.md)
- [R0005 专业原报告](../artifacts/R0005/REPORT.md)
- [R0005 实际发送记录](turns/R0005/SEND_RECEIPT.json)

- [R0006 管理决定](../reviews/management-R0006/DECISION.md)
- [已签 Worker 工单](../reviews/management-R0006/WORKER_ORDER.md)
- [真实 Worker 派发凭证](worker-BI01CO04-INPUT-RECOVERY-01/DISPATCH_RECEIPT.json)

- [R0007 管理决定](../reviews/management-R0007/DECISION.md)
- [重放签单](../reviews/management-R0007/WORKER_ORDER.md)
- [重放实际派发凭证](worker-BI01CO04-ASOF-VISIBILITY-REPLAY-01/DISPATCH_RECEIPT.json)

- R0008发送ready至首实际phone超过120秒33.962930秒，R0009到期观察首实际phone较原due+120秒分别按server/local迟59.398/63.177秒；原deadline和独立时钟均保留，不通过新观察期限掩盖。
