# D009｜当前39f实例的M-B观察位置准备

本D完成原B Skill的“任务明确指定”位置用法，阶段状态为**完整**，未完成位置为空。产物为ObservationPositionPreparationResult.json及OrdinaryPositions.json；可供后续M-D直接绑定原SOF、品种集和起止日期。本D只做B，没有生成新的Feature、统计、图或正式图数据，没有形成ObservationMaterialPackage，也未选择正式合理性案例或冻结预期。

## 原输入与方法

唯一专业Skill为`daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/observation-material-preparation/observation-position-preparation/SKILL.md`，按同版WORKFLOW/IO_SPEC及原M-B外层入口执行。原方法规定任务明确给出品种和时间时直接采用；本任务已有rb/hc/i和2021—2023，因此采用原明确输入，不使用未指定位置时的2021—2022默认范围覆盖它。没有另造典型案例算法或多尺度节点链。

准确D009与C0021、适用Owner原文及63个输入exact对象已核同，远端I/D/批准与本地字节一致。Owner既有批准和最新Binding允许本D分析/Run记录写面；无新Owner等待，也没有扩大到正式Feature运行、实现采用、Q/V或WALL。当前U/X/G继续使用已接收D008，不重做完整理解、生产或全量统计。

## 原生位置定义

| 项目 | 当前明确位置 |
| --- | --- |
| 位置编号 | F800-MB-D009-P001 |
| 位置用法 | 任务明确指定，按普通位置字段承接 |
| SOF | TA_updto20240229_DBA，沿特征实例绑定 |
| 品种集 | rb、hc、i；steel |
| 开始日期 | 2021-01-01 |
| 结束日期 | 2023-12-31 |
| 采样与日历 | 5m；night_end_at_2300 |
| 位置来源 | 原F_BASE_RUN_INPUT §4、D009、D008 FeatureRunResultBinding.data_scope |
| 未完成位置 | 无 |
| 阶段状态 | 完整 |

开始/结束保留原任务日期粒度，结束边界解释由后续D的日历/PlotSet绑定确定；B未重新决定SOF或替换请求范围。D008实际输入首末为2021-01-04 09:05至2023-12-29 15:00，这只是沿原日历的实际可用记录，不把正式三年请求改短。

当前实例为CommonPriceTurnGroupCandidatesFrp，FRP39f02ec4548e68ba8dbd30061afc870546000994、TIS2f460d663d821cf2ba25555eda13e78b697d0767，参数SHA-256 `b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3`，仍800/600/CalendarUTITick/2Δ1200及method.revision1。实例/SOF引用为`daowei2026/observe-iterate@d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca:longrun/runs/OI-F800-STAT-20261122-01/professional/D008/FeatureRunResultBinding.json#data_scope`，共享理解引用为`daowei2026/observe-iterate@d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca:longrun/runs/OI-F800-STAT-20261122-01/professional/D008/CurrentFeatureUnderstandingPackage.json`。当前Package的feature_ref/current_applicability与实例一致，PARTIAL限制原样传递；B未另查Feature语义形成第二份理解。

## 既有候选来源与位置对齐

原四项场景问题及七个候选全部保留原来源。SQ001、SQ003保持HIGH，SQ002、SQ004保持MEDIUM；本B不改变其专业性质、优先级或开放状态，也不声明Owner已接受暂缓。七个候选位于明确位置内：六个F观点与当前公开表的原父坐标、Life/Revision和known对应；一个上游尺度位置与原actual/known来源对应。该核对只用于范围和来源对齐，没有重新做业务对照或挑选正反例。

| 原候选来源 | 品种 | 原开始位置 | 原结束位置 |
| --- | --- | --- | --- |
| F800-SQ-001-C1 | i | 2021-01-04 21:15:00 | 2021-01-05 09:40:00 |
| F800-SQ-001-C2 | hc,i,rb | 2021-01-07 13:35:00 | 2021-01-07 13:35:00 |
| F800-SQ-002-C1 | hc,rb | 2021-01-06 11:05:00 | 2021-01-06 11:05:00 |
| F800-SQ-002-C2 | hc,rb | 2023-01-03 09:15:00 | 2023-01-03 09:15:00 |
| F800-SQ-003-C1 | i,rb | 2023-07-07 09:05:00 | 2023-07-07 09:05:00 |
| F800-SQ-003-C2 | hc,rb | 2021-01-07 13:35:00 | 2021-01-07 13:35:00 |
| F800-SQ-004-C1 | hc,i,rb | 2021-01-04 10:05:00 | 2021-01-04 10:05:00 |

来源为`daowei2026/observe-iterate@d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca:longrun/runs/OI-F800-STAT-20261122-01/professional/D008/ScenarioQuestionQueue.json`与`daowei2026/observe-iterate@d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca:longrun/runs/OI-F800-STAT-20261122-01/professional/D008/CandidateCaseIndex.json`，完整原exact、父坐标及核对来源保留在PositionSourceAlignment.json。同刻不同对象/观点未合并，actual/confirm/known和原事件位置沿共享理解与原数据字段保留。表内候选点/段仍只是原索引来源，不是B另选的正式观察窗口或CaseReviewSet；实际图和图数据形成后，由原S1选择案例并冻结预期。

## 限制、后继和完成边界

本B明确位置没有缺口。共享理解未暴露的内部逐Tick全部轨迹、800的业务场景解释及Q共享适配/独立数值边界限制继续传递，不把参考筛查当作native轨迹或业务真值。D009没有重新生产、重统计、改代码/参数/PNV/范围或申请重型生产锁，也不声称本次持锁；D008已完成的真实生产/锁/读回证据继续引用原件。

原manager消费B后按既有依赖衔接M-C展示准备、M-D集成、M-E真实执行/核图/正式取数与适用S1/S2。本D不冒充这些后继已经委派或完成。B已完成不等于B—D PLAN_READY、ObservationMaterialPackage DATA_READY、FeatureReleaseGate或业务Run完成；本D不签释放包、不运行或释放Q/V、不改WALL。

## Owner要求的七项当前进度

1. D001最小理解已接收，本C未重做完整U。
2. X已由D008完成有效；本C没有新X。
3. D008为新版本真实重新生产，本B只沿用其已接收原件作为输入，没有新的生产或复用验收。
4. D008成功Feature进程2050192/native2050491已退出0并释放锁；本C未启动Feature进程。
5. 当前有效结果目录：`/dwdhome/fy/BASE_E6_2_copy/artifacts/OI-F800-STAT-20261122-01/D008/store/BaseData/futures/TA_updto20240229_DBA/fao/prod/2021-01-01 21:00:00~2023-12-31 20:00:00/CommonPriceTurnGroupCandidatesFrp/3/9/a/1/9/2/a/4bbf414e0814726d92d156f2fe9b1f968/func`，fields SHA-256 `58ff1166df0e4bbdb84f4309b72947ee16de4a075d8992681fd60f46ccfb887c`。
6. G已由D008完成并被原manager接收，PASS_TO_SCENARIO_REVIEW；本C未重统计。
7. 本B当前没有阻断；四项场景问题继续开放，后继材料/分析和释放由原manager依既有Workflow处理。

原生校验见VALIDATION.json，覆盖原IO字段、当前实例/对象/时间一致性、明确输入优先级、候选来源保留及未越界事实。专业结果先发布并远端读回，再引用已有exact提交回C0021原V2 Return。REPORTED_COMPLETE仅表示D009的B职责完成，不表示manager已消费本C或父Run已经释放。
