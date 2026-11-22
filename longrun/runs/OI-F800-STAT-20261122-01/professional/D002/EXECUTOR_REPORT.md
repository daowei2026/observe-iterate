# D002｜F800 正式 X 与全量 G 专业报告

本次已完成准确实例的新生产、独立只读回读与原 Skill G1–G8。产出 **480 个候选 Life、1546 次候选 Revision occurrence**。`GlobalProfileGate=DIAGNOSIS_REQUIRED`：覆盖完整标志存在一项结构疑点，22 次观点涉及 12 个 Life，需交原 manager 委派偏差诊断。本报告不将 D002 完成交付扩大为 FeatureRelease 或父 Run 完成。

## 1. 版本、授权与正式 X

本 D 来源：`daowei2026/observe-iterate@d22655642b4e4dd8f9b1371cfce743164c7dbf6d:longrun/runs/OI-F800-STAT-20261122-01/delegations/D002/DELEGATION.json`。接收者仍为 E1，workers=[]，回原 manager。D001 已接收，本次只复核其关键入口哈希与未决输入，不重做完整理解。准确来源审计见 [SOURCE_AUDIT.json](SOURCE_AUDIT.json)。

仅生产 `CommonPriceTurnGroupCandidatesFrp`（make_features 的 f）。FRP `ac1927518ad6105f15ffbe37fea45e4be91ba574`；TIS `2f460d663d821cf2ba25555eda13e78b697d0767`。完整配置 [configuration.json](configuration.json) SHA-256 `b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3`，与 D001 逐值、逐文件哈希一致。唯一业务 override 是 observation_multiple=800；delta=600、CalendarUTITick、method.revision=1；2Δ actual贴近仍为1200 UTI（10开放分钟）。

准确原候选目录无 fields.json；历史 F800 修改了 method.revision，不满足复用。故选择新生产，未拿历史目录冒充当前实例。平台用正常进程配置将 APP_DIR、store、日志和任务输出指向本工作区；SOF 原输入路径保持原配置，配置差异证据在 [PLATFORM_STORAGE_BINDING.json](PLATFORM_STORAGE_BINDING.json)。实际目录：

`/dwdhome/fy/BASE_E6_2_copy/artifacts/OI-F800-STAT-20261122-01/D002/store/BaseData/futures/TA_updto20240229_DBA/fao/prod/2021-01-01 21:00:00~2023-12-31 20:00:00/CommonPriceTurnGroupCandidatesFrp/3/9/a/1/9/2/a/4bbf414e0814726d92d156f2fe9b1f968/func`

实际 ts PID **1712794**，可执行文件 SHA-256 `668cee8c7939caae2a3b01bdb12fb7390a37a92ac7baf8c416ae9204f6e84e58`。778 个相关 FRP 源文件与锁定提交一致；关键 TIS 6 文件再次对照已接收哈希一致。正式 Feature Python PID1712546，UTC 2026-11-22T09:50:06.055079+00:00 至 2026-11-22T09:59:03.227008+00:00，引擎日志总耗时约508.6秒。实际共享 flock 由 supervisor1712483 持有，独立进程争锁退出73证实排他；结果均写本Run独立store。证据见 [FRP_SOURCE_BINDING.json](FRP_SOURCE_BINDING.json)、[TIS_SOURCE_RECHECK.json](TIS_SOURCE_RECHECK.json)、[NATIVE_PROCESS_OBSERVATION.json](NATIVE_PROCESS_OBSERVATION.json)。

监控脚本最初按PID只记录一次，漏记同PID shell exec为ts，导致生产结束后监控收尾断言退出1。Feature Python已退出0、正式生产和公开读取成功；先前新鲜独立/proc快照已记录真实ts。执行过的脚本原样保留，修正版未再启动生产；[PRODUCTION_RECONCILIATION.json](PRODUCTION_RECONCILIATION.json)明确区分真实生产成功与监控失败。未伪造监控原记录或精确锁释放时刻。

由另一 Python 进程1720502只读加载准确结果，31张公开表行数、列、CSV SHA-256全部与生产后导出相同；to_df与occurrences一致。fields SHA-256 `58ff1166df0e4bbdb84f4309b72947ee16de4a075d8992681fd60f46ccfb887c`。145个原生文件共13180182字节逐文件登记。所有1546个观点的原deadline-anchor均480000，原revisionEnd-deadline均3600：800已由原生引擎消费。见 [FeatureRunResultBinding.json](FeatureRunResultBinding.json)、[NATIVE_OUTPUT_MANIFEST.json](NATIVE_OUTPUT_MANIFEST.json)。

## 2. 范围与统计口径

请求 rb/hc/i、5m、2021-01-01至2023-12-31、night_end_at_2300、TA_updto20240229_DBA/steel。实际每品种49683行，首2021-01-04 09:05:00、末2023-12-29 15:00:00；三品种共149049输入行且时间轴相同。年分母16599/16530/16554；无重复或乱序，closeUti连续每步600。每品种69个非有限close仍计入日历位置，独立有效覆盖对照会断开。完整同参数KLine/Zig/Rct/ScaleTurn缓存均以OnlyRead取得，没有补算或运行Source、Q/V。见 [UPSTREAM_EXTRACTION.json](UPSTREAM_EXTRACTION.json)、[INPUT_SCOPE_VALIDATION.json](INPUT_SCOPE_VALIDATION.json)。

原生readiness为PARTIAL：核心版本、参数、范围、对象键可靠；未暴露逐Tick Dynamic、materialTotals及native首阻断轨迹。该限制不阻止完成已支持剖面。[StatisticDefinitions.json](StatisticDefinitions.json)登记17项口径，[StratificationPlan.json](StratificationPlan.json)声明品种、知识年/月、日夜盘和开盘窗口。Life数、Revision occurrence、发行事件、成员关系和上游位置分别计数；品种组数按包含关系，会重叠；全局Life去重。公共Calendar位置49683用于事件密度，149049输入行另列。原始位置含每品种一个初始化锚点；1859个尺度位置中非初始化1856，参加F的875个中非初始化872。

actual、几何confirm、selected原事件知识及F发表时间分别保留；成员T.pointKnownFrom是raw知识。UUID按uint64高低位精确解码，不转float；子表按完整父坐标归属，同刻保留occurrence/child坐标并以previous核序。无 occurrence 不当成失败。定义事件可单独发表。

## 3. 业务链分母、转化与潜在漏报筛查

| 品种/去重全局 | 原始实际位置 | 尺度位置 | 参加F的位置 | 候选Life | Revision occurrence |
| --- | --- | --- | --- | --- | --- |
| rb | 2557 | 425 | 324 | 401 | 1282 |
| hc | 2584 | 430 | 315 | 375 | 1187 |
| i | 4932 | 1004 | 236 | 310 | 1003 |
| ALL_DISTINCT | 10073 | 1859 | 875 | 480 | 1546 |

全局原始位置10073、尺度位置1859（含3个锚点），875个尺度位置曾参加候选，比例47.07%；非初始化872/1856=46.98%。3472个成员子表行是跨观点的关系数，不能作尺度总分母。三品种候选包含数401/375/310之和大于480，原因是共同组本来跨品种。

全量独立建立648个跨品种actual距离≤2Δ近边：624个四坐标正向、3个初始化Unresolved、21个否决。624个正边全满足800首次共同可知期限，K6参考仅16个；480个Life中469个首次准入在旧6Δ期限之后。1859个尺度位置均在自身800窗口内首次可知；K6参考91个。K6是同输入期限参考筛查，不是额外正式生产，也不是“800已标定成功”的结论。

按独立规则筛查，rb未参加101个均无跨品种2Δ邻点；hc为114个无邻点、1个近边否决；i为759个无邻点、9个近边否决。当前未发现“合格非否决近边完全未进入任何候选”的位置，但这仍不是全部市场真值，更不能宣称无业务漏报。见 [profile/first_block_reference_by_symbol.csv](profile/first_block_reference_by_symbol.csv)、[profile/near_actual_pair_screen.csv](profile/near_actual_pair_screen.csv)。

## 4. 对象、事件、状态与有限责任

1218个公开发行事件，其中1个只有definitions，1217个含候选；一事件可含多个观点。1546观点/49683位置=每千位置31.117观点；责任内同时Life峰值36，当前没有接近逐拍发行的证据。对象准确身份、成员与上游actual/价格/confirm/known、原问题固定、期限不扩张、关闭不重开、责任关闭后不再更新、previous/overlap/coveredBy、admission/candidate/alternative exact及bridge、四坐标和2Δ等23项检查未见违例。初始化无方向在公开表称Unavailable，与参考Unknown对应，未错误列作冲突。

观察状态观点数：Open498、ClosedSupported805、ClosedInsufficient2、Subsumed241、Withdrawn0、EndedByScope0；局部Supported1543、Incomplete3、Contradicted0。Required2306条的verdict/gap/veto分布及分层见 [profile/required_reasons.csv](profile/required_reasons.csv)、[profile/cross_strata_reasons.csv](profile/cross_strata_reasons.csv)。零分支缺少适用输入证明，只作为覆盖限制。Subsumed与责任退出分别表达，未合并。

同Life相邻观点1066条转换，含Open→ClosedSupported398、Open→Subsumed80、Open→ClosedInsufficient1，以及同状态正文/责任变化；没有同Life同拍多观点或previous悬空。状态占用只按已发表观点持有区间计算，末段截断于修订终点或样本末；分年/Session占用另按公开5m位置拆分，不冒充内部逐Tick trace。

480个原观察窗全部4000开放分钟；修订尾30、交接尾90。首次准入actual年龄中位280、最大1665分钟；观察剩余责任中位3720分钟；已发表观点跨度中位3750分钟。479个Life末观点责任已关，1个样本末右删失；不把这些期限称为真实市场运动寿命。非初始化actual→selected中位rb280、hc270、i110分钟，几何confirm→selected均5开放分钟。见 [profile/lifecycles.csv](profile/lifecycles.csv)、[profile/latency_by_symbol.csv](profile/latency_by_symbol.csv)。

## 5. 分层比较

| 知识年 | 尺度位置 | 参加位置 | 新建Life | 观点 |
| --- | --- | --- | --- | --- |
| 2021 | 929 | 446 | 244 | 787 |
| 2022 | 642 | 300 | 162 | 515 |
| 2023 | 288 | 129 | 74 | 244 |

| Session钟点 | 5m分母 | 新建Life | 观点 | 覆盖冲突观点 |
| --- | --- | --- | --- | --- |
| DAY_CLOCK_09_15 | 32715 | 301 | 1008 | 7 |
| NIGHT_CLOCK_21_23 | 16968 | 179 | 538 | 15 |

知识年Revision密度47.41→31.16→14.74/千输入位置，伴随上游尺度位置929→642→288。i参与比例低于rb/hc，未据此判错。日/夜密度30.81/31.71接近；开盘首15分钟钟点窗口为50.91/千位置，其他29.24；该窗口以真实Calendar行作分母，不臆测交易日归属。上/下方向分别227/252个Life，另1个初始化无方向Life。

各品种、年份、Session与开盘窗口的密度、出生责任跨度、右删失、状态/依据、Required reason、观点持有期、覆盖冲突率均另有全量对照，而非只报平均。参见 [profile/cross_strata_comparison.csv](profile/cross_strata_comparison.csv) 及同目录states/reasons/held_view_time；月度、actual年与知识年分别保留。没有可靠环境标签时未猜牛熊或波动市场阶段。

## 6. 结构疑点、场景问题与Gate

**F800-GF-001：覆盖完整标志冲突候选。** 三对象公开KLine在[u-480000,u]均有效且整数UTI连续、正常入口Clock可用时，groupCoverageIncomplete仍为1；22个Revision occurrence、12个Life、18个发行时刻。 范围2021-08-31 21:45至2021-09-15 21:25；占全部观点22/1546=1.423%、Life12/480=2.5%；在30个coverageIncomplete观点中占73.33%。分年全在2021；日盘7、夜盘15。另8个flag观点未满足完整历史条件，未列为冲突；没有把冷启动当异常。清楚代表Life `3657ca5e-f0c0-42fe-a30f-943fc97a9ecf`，Revision `22df3987-1df8-40d8-b736-02fceed8e239`，2021-08-31 21:45，u=78643799，需要从78163799覆盖，而三品种有效连续输入均从72004199开始。该组同Life此前flag=0，成员身份和原问题未变。

这里只冻结已有覆盖合同与观测事实，不写根因、补丁、参数建议或宣称历史finding关闭。最强竞争解释和可证伪条件均在 [GlobalFindingCandidates.json](GlobalFindingCandidates.json)、[DiagnosisInputAdapters.json](DiagnosisInputAdapters.json) 中；全部22个准确位置可复现。

4项场景解释问题另列 [ScenarioQuestionQueue.json](ScenarioQuestionQueue.json)：i低参与和潜在漏报边界、跨年/Session密度、800带来的长责任与并行候选、零分支及初始化。10项 [CandidateCaseIndex.json](CandidateCaseIndex.json) 是最小区分候选（清楚反例、同Life对照、冷启动、日夜、上游未出组、跨年及延迟边界），不是已画图或冻结的正式场景集。

原生完整输出 [FeatureGlobalBehaviorProfilingResult.json](FeatureGlobalBehaviorProfilingResult.json)，独立组件 [GlobalBehaviorProfile.json](GlobalBehaviorProfile.json) 与 [GlobalProfileGate.json](GlobalProfileGate.json)。Gate为 **DIAGNOSIS_REQUIRED**，应由原manager按Skill3处理F800-GF-001；若后续处理改变行为，再按X/G重验。当前D002职责已完成，无生产或统计阻断；尚有专业诊断门槛，不宣称800业务合理、Feature已释放或父Run结束。

## 7. Owner七项进度与验收边界

1. D001：已由manager接收，本次未重做完整U；六项缺口的处置见 [D001_GAP_RESOLUTION.json](D001_GAP_RESOLUTION.json)。
2. X：已开始且验收完成，准确结果绑定及独立只读已形成。
3. 复用/生产：准确旧结果不合格，执行一次新生产；未因监控脚本失败重复生产。
4. 正式进程：真实ts1712794已运行并结束，Python成功；监控异常如实保留并核销证据。
5. 结果目录：上列本工作区D002/store准确实例；原生dba与上游输入CSV保留本地，记录分支发布31张F公开表CSV、全量统计、合同、脚本、定位与SHA-256。
6. G：已完成原Skill G1–G8，24项结构筛查、全部可支持剖面与分层已完成。
7. 阻断：本D无未完成生产/统计阻断；后续Gate为DIAGNOSIS_REQUIRED。该专业下一步交manager，不把它伪装成本executor仍持有的未完原D。

本轮未修改正式Feature代码或业务参数，未运行额外专业任务、未创建Worker、未向其他线程发消息。只更新本Run记录分支与Owner工作区。合法PRO_RETURN待专业产物先真实发布后，以该提交exact ref另行回交，不写未来自引用。
