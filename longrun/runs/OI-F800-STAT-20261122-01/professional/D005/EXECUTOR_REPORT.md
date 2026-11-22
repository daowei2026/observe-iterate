# D005｜be57 完整正式 F X、独立31表读回与全量G复验

本D已完成授权范围内的新版本正式X和原Skill G1–G8。`GlobalProfileGate=DIAGNOSIS_REQUIRED`；原 `F800-GF-001` 当前状态为 `CLOSED_ON_LATEST_PROFILE`。本次完整实测为 480 个候选Life、1534 次Revision occurrence、1216 个发行事件。原22个错误flag位置与8个cold对照已由独立进程通过原生Life/AsOf读口复验，30/30符合各自预期。

本轮另识别 `F800-GF-002`：8个Revision、5个Life、6个发行时刻标记完整覆盖，但观察窗内三品种各有69行OHLC缺值/零成交量。8/8在修复前同对象同知识位置也已存在；这是一项新识别的结构疑点，不宣称be57新引入回归，也未判定数据或实现根因。故最终Gate为DIAGNOSIS_REQUIRED，须由原Skill3先核缺值、Calendar豁免与覆盖承诺。原GF-001的关闭与此项未决状态分别登记。

原manager=`codex:OI-F800-STAT-20261122-01:manager`；原E1=`codex:OI-F800-STAT-20261122-01:executor:E1`；当前C0012/D005，CODEX_NATIVE_DIRECT、workers=[]。未创建线程、Worker或新委派。D005只完成本次X/G专业职责；executor完成不等于manager已消费，也不替父Run出FeatureReleaseGate或启动Q/V。

## Owner七项进度

| 项目 | 本次事实 |
|---|---|
| D001是否完成 | 已接收，未重做完整U；复用原理解并沿D004合同不变结论更新be57最小适用绑定，见CurrentFeatureUnderstandingPackage.json |
| X是否开始 | 已开始并完成完整rb/hc/i、5m、2021—2023正式F |
| 复用还是生产 | NEW_FORMAL_PRODUCTION；D002的ac结果仅历史比较，独立新store保留所有旧产物 |
| 正式Feature是否实际运行 | 是，Feature Python PID 1884046，原生ts PID 1884302；实际包装进程退出0，监督进程退出0 |
| 当前结果目录 | `/dwdhome/fy/BASE_E6_2_copy/artifacts/OI-F800-STAT-20261122-01/D005/store/BaseData/futures/TA_updto20240229_DBA/fao/prod/2021-01-01 21:00:00~2023-12-31 20:00:00/CommonPriceTurnGroupCandidatesFrp/3/9/a/1/9/2/a/4bbf414e0814726d92d156f2fe9b1f968/func` |
| G是否开始 | 是，合格新X独立读回后完整执行G1–G8；可支持对象/事件/状态/责任/分层/引用及原finding全部复验 |
| 当前阻断 | 无未解决执行阻断；专业后继按原生GlobalProfileGate与下列限制处理 |

## 当前版本、实例和完整范围

- FRP `be57d6752c9d43d10f1d670e1d2993bb8153ea7c`，TIS `2f460d663d821cf2ba25555eda13e78b697d0767`。
- 完整配置SHA-256 `b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3`。`observation_multiple=800`、`delta=600 CalendarUTITick`、实际贴近`2Δ=1200UTI`、`method.revision=1`；inputs/sources/domain/result_layout与已批准配置一致。
- F-only；rb/hc/i、5m、2021-01-01—2023-12-31、night_end_at_2300、TA_updto20240229_DBA、steel。实际首末KLine为2021-01-04 09:05:00—2023-12-29 15:00:00，没有将节假日边界缩写为较短正式请求。
- 每品种49,683个Calendar位置，三对象149,049行；各69个非有限close保留在日历分母，连续有效覆盖对照在缺价处断开。上游15张导出表与旧版逐字节一致，见VersionComparison和UPSTREAM_EXTRACTION；不存在用输入变化解释修复效果的问题。

实际EPM入口为 `/dwdhome/fy/BASE_E6_2_copy/.runtime/f800-exact-uti-20261122/runtime/edh-universe/bin/ts`，SHA-256 `f1d312b92744e68e4a617c98c04b07fa9361ab744be79b92963a39024d7060ea`；本次实际原生进程加载已记录。FRP当前源文件逐文件匹配锁定Git对象，TIS关键入口/读口/Calendar六文件复核一致，原D004构建与版本采用链保留。D005未改动正式Feature代码或参数，未重跑已完成的64项局部回归。

共享flock在2026-11-22T13:47:09.829277+00:00取得，独立抢锁进程退出73，内核锁及实际持锁PID可核；正式过程于2026-11-22T13:56:15.652428+00:00退出0，锁已释放。生产前无新store写者且未见其他同UID引擎。实际进程的PID/executable/命令变化持续记录，保留同PID exec证据；没有复用旧监控故障或用文件存在代替持锁。

31张表已由独立Python PID 1890775以OnlyRead读取，表名、行数、列及CSV SHA-256与生产后的原生读取逐表一致，主`to_df`与`to_dfs()['occurrences']`相同。fields.json SHA-256 `58ff1166df0e4bbdb84f4309b72947ee16de4a075d8992681fd60f46ccfb887c`；其身份同时绑定新代码/引擎/配置/范围，并非单靠fields或目录名证明代码。

## 业务单位与全量剖面

计数沿最小业务链：同参数KLine→Rct原始实际位置→两轮ScaleTurn资格→材料/四坐标关系→候选Life/Revision→正式发行与exact/形成参与。原始位置、尺度位置、Life、Revision发生、成员关系和发行事件分别计数；同Life同刻保留occurrence及完整父子坐标，按previous引用核序，不按随机UUID排序。每项单位、分母、去重、同刻规则和来源见18项StatisticDefinition。

| 品种/去重全局 | 原始实际位置 | 尺度位置 | 参加F位置 | 候选Life | Revision发生 |
| --- | --- | --- | --- | --- | --- |
| rb | 2557 | 425 | 324 | 401 | 1270 |
| hc | 2584 | 430 | 315 | 375 | 1176 |
| i | 4932 | 1004 | 236 | 310 | 1001 |
| ALL_DISTINCT | 10073 | 1859 | 875 | 480 | 1534 |

品种层的组数是包含关系，会跨品种重叠；ALL_DISTINCT单独全局去重。Rct分母包含每品种初始化锚点，不能称为全部潜在市场转折。F成员行反映多次Revision中的关系，不能当作尺度分母。

| 知识年 | 尺度位置 | 新Life | Revision发生 |
| --- | --- | --- | --- |
| 2021 | 929 | 244 | 775 |
| 2022 | 642 | 162 | 515 |
| 2023 | 288 | 74 | 244 |

知识年、actual年、月、品种、方向、钟点日夜与开盘窗口均已分层；上游按selected知识轴、组按首次publication、观点按当次publication，actual另列。每层密度、责任跨度、状态/理由、观点持有和结构疑点率见profile/cross_strata_*。无可靠牛熊标签，未凭名称造环境分类。

状态占用采用已发表观点知识区间持有，并按真实5m位置分层取样；不是内部逐Tick Dynamic trace。生命周期统计的是有限观察/修订/交接责任，样本末右删失 1 个Life另列。独立上游近actual候选筛查 648 条，合格非否决边未在任何候选出现的筛查数 0；这不是应输出真值或已确认漏报。

## 修复复验与完整版本影响

原22个误报位置按自然Life（排序上游symbol/round/confirm成员及原anchor/deadline/revisionEnd）对齐，用新原生稀疏观点的知识持有值复验；随后独立进程通过未修改的TIS GroupCandidateReadSession Life/AsOf读口按previous链重新选择观点，逐项与CSV比较结果一致。原错误位置 22/22 为0，cold对照 8/8 保持1；新三年全量覆盖冲突为 0。证据在comparison/coverage_retest.csv、NATIVE_RETEST_API.json和27项全量结构检查。

当前结构检查：complete_flag_with_input_price_gap=8。检查包含成员准确上游、Required四项和actual 2Δ、固定原问题、责任不扩张、关闭不重开/责任后不更新、状态轴自洽、全部previous即时前版链、candidate/admission/成员exact及alternative桥、全部非空group子表父键。未暴露的内部变量不计作实测。原GF-001由FIXED_PENDING_RERUN转为CLOSED_ON_LATEST_PROFILE的依据是本次完整X/G，不是22flag隔离方程或64项局部回归。

共同自然Life 480；旧独有 0、新独有 0；共同对象中 480 个Life的UUID改变。Revision原始UUID交集 0。UUID无跨运行稳定相等合同，各版exact/previous/admission/alternative链按本版实际ID完整验实，不强行把随机ID相等当验收。

共同Life×两版publication UTI并集共 1546 个公开观点持有比较点，差异 22 点，变化字段计数为 `{"coverage_incomplete": 22}`。这里是按原生已发表观点进行的跨版对照，不是新造事件或内部逐Tick trace。发行次数不同的Life/UTI点 12；完整差异逐项保留在comparison/native_asof_state_differences.csv和publication_changes.csv。

| 量及单位（见定义） | 旧 | 新 | 新−旧 |
| --- | --- | --- | --- |
| candidate_lives | 480 | 480 | 0 |
| candidate_revision_occurrences | 1546 | 1534 | -12 |
| publication_events | 1218 | 1216 | -2 |
| definition_only_publication_events | 1 | 1 | 0 |
| upstream_raw_positions | 10073 | 10073 | 0 |
| upstream_scale_positions | 1859 | 1859 | 0 |
| initial_scale_anchors | 3 | 3 | 0 |
| used_distinct_scale_positions | 875 | 875 | 0 |
| input_5m_positions | 49683 | 49683 | 0 |
| input_symbol_rows | 149049 | 149049 | 0 |
| revision_events_per_1000_input_positions | 31.117283577883782 | 30.87575226938792 | -0.2415313084958619 |
| peak_responsibility_active_lives | 36 | 36 | 0 |
| right_censored_lives | 1 | 1 | 0 |
| coverage_incomplete_occurrences | 30 | 8 | -22 |
| coverage_incomplete_lives | 19 | 7 | -12 |
| coverage_conflict_occurrences | 22 | 0 | -22 |
| coverage_conflict_lives | 12 | 0 | -12 |
| potential_eligible_pairs_unseen | 0 | 0 | 0 |
| near_actual_pair_screen_count | 648 | 648 | 0 |
| positive_near_pair_screen_count | 624 | 624 | 0 |
| positive_near_joint_eligible_800 | 624 | 624 | 0 |
| positive_near_joint_eligible_6 | 16 | 16 | 0 |
| candidate_births_after_legacy_6 | 469 | 469 | 0 |

全31表原生行数影响如下；完整字节hash另见comparison/all_31_tables.csv。UUID变化会使载荷hash不同，表行减少也不自动证明业务改善。

| 公开表 | ac旧版行 | be57新版行 | 差值 |
| --- | --- | --- | --- |
| definitions | 1 | 1 | 0 |
| definitions_definitionObjects | 3 | 3 | 0 |
| definitions_definitionDirections | 4 | 4 | 0 |
| definitions_definitionTypes | 4 | 4 | 0 |
| occurrences | 1546 | 1534 | -12 |
| occurrences_groupPrevious | 1066 | 1054 | -12 |
| occurrences_groupMembers | 3472 | 3447 | -25 |
| occurrences_groupMembers_memberClock | 3472 | 3447 | -25 |
| occurrences_groupMembers_memberP | 3463 | 3438 | -25 |
| occurrences_groupMembers_memberP_pointClock | 3463 | 3438 | -25 |
| occurrences_groupMembers_memberT_pointClock | 3472 | 3447 | -25 |
| occurrences_groupMembers_memberC_pointClock | 3472 | 3447 | -25 |
| occurrences_groupRequired | 2306 | 2292 | -14 |
| occurrences_groupRequired_pairDistance | 2306 | 2292 | -14 |
| occurrences_groupOverlaps | 215 | 215 | 0 |
| occurrences_groupCoveredBy | 241 | 241 | 0 |
| occurrences_groupFormationParticipation | 1546 | 1534 | -12 |
| occurrences_groupFormationParticipation_participationMembers | 3472 | 3447 | -25 |
| occurrences_groupFormationParticipation_participationSupports | 0 | 0 | 0 |
| occurrences_groupFormationParticipation_participationSupports_supportPreviousFact | 0 | 0 | 0 |
| occurrences_groupFormationParticipation_participationSupports_supportOperands | 0 | 0 | 0 |
| occurrences_groupFormationParticipation_participationSupports_supportOperands_formationOperandNumber | 0 | 0 | 0 |
| occurrences_groupFormationParticipation_participationSupports_supportOperands_formationOperandCategory | 0 | 0 | 0 |
| occurrences_groupFormationParticipation_participationSupports_supportOperands_formationOperandPoints | 0 | 0 | 0 |
| occurrences_groupFormationParticipation_participationSupports_supportOperands_formationOperandPoints_formationPointClock | 0 | 0 | 0 |
| occurrences_groupFormationParticipation_participationSupports_supportOperands_formationOperandPoints_formationPointClockKnown | 0 | 0 | 0 |
| occurrences_groupFormationParticipation_participationAlternatives | 241 | 241 | 0 |
| occurrences_groupFormationParticipation_participationAlternatives_alternativeBridge | 482 | 482 | 0 |
| occurrences_groupFormationParticipation_participationOutsideNotifications | 0 | 0 | 0 |
| occurrences_groupFormationParticipation_participationOutsideNotifications_outsideNumber | 0 | 0 | 0 |
| occurrences_groupFormationParticipation_participationOutsideNotifications_outsideTurn | 0 | 0 | 0 |

## 原生Gate、场景队列与界限

`GlobalProfileGate=DIAGNOSIS_REQUIRED`。理由和后继原文见GlobalProfileGate.json；新结构finding 1 项，诊断适配包 1 项。已关闭旧finding保留FindingDisposition，新GF-002具名适配包已形成，不在G提前诊断。

原四项ScenarioQuestion逐项基于新结果更新：i参与率及潜在覆盖、知识年/Session密度、800的迟到/长责任及覆盖关系、初始化与低频分支。10个最小对照候选位置包含上游未参加F位置、跨年、迟到/覆盖及cold位置；理由与所需证据见CandidateCaseIndex。它们仍是场景问题，不当作新业务判错或已冻结正式场景，也不因旧finding关闭而消失。

限制保留：内部逐Tick材料/所有枚举与native首次阻断未暴露；参考K6只用于同输入期限筛查，未生产另一个正式实例，不能证明800已标定合理；缺少patch、scopeEnded、未知Clock分支适用输入不证明分支不可达。F/Q共享适配器及Q另有归一化数值边界沿D004 ContractAndDependencyImpact传递；本D未运行Q/V，不能据F通过推定下游通过。

后继由原manager按采用的control-v0.3与CurrentReviewTarget消费最新U/X/G、finding及限制，形成FeatureReleaseGate/UpstreamReleasePackage；需要真实场景解释时进入既定M/Skill1/2。没有新增正式行为变化；若后续提出新的正式修改，仍按原流程形成提案并取得Owner确认。D005不替manager签后继，不将本次G通过扩大为Feature在所有市场场景中已合理。

本报告与原生专业文件先发布，C0012 PRO_RETURN随后引用已发布exact提交。验证见VALIDATION.json、WORKFLOW_COMPLETION.json、SOURCE_REF_AUDIT.json和BASELINE_INPUT_READBACK.json。
