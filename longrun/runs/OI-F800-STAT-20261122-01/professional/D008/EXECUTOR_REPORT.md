# D008｜39f完整正式F800 X与全量G回交

本D按manager D008和锁定Skill执行完成。当前正式代码FRP `39f02ec4548e68ba8dbd30061afc870546000994`、TIS `2f460d663d821cf2ba25555eda13e78b697d0767`；完整配置SHA-256 `b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3`。本D没有修改正式Feature代码或参数。原生GlobalProfileGate=`PASS_TO_SCENARIO_REVIEW`；本D不签FeatureReleaseGate或UpstreamReleasePackage，不运行/释放Q/V或改WALL。

## Owner要求的七项当前进度

1. D001最小理解已接收；复用D005结构理解与D007 delta，只核39f绑定及J4非有限close分类，没有重做完整U。
2. X已开始并完成：本次成功尝试 `2026-11-22T17:35:16.621559+00:00` 至 `2026-11-22T17:44:22.997366+00:00`。
3. 重新生产。D005 be57及D002 ac192只作历史对照，未复用为当前结果；本D新attempt/store中形成一个完整合格F实例。
4. 正式Feature曾实际运行，当前已退出0。成功包装PID `2050192`、原生ts PID `2050491`。实际/proc/exe哈希与新构建一致；真实kernel flock和独立排他探测退出73，结束后锁释放。首次尝试因新平台少store_dir.json退出，无F结果，原日志及修复在PRODUCTION_ATTEMPT01_FAILURE/attempts/attempt01；第二次成功。补齐的是正常平台空存储覆盖配置，业务配置未变。
5. 当前结果目录：`/dwdhome/fy/BASE_E6_2_copy/artifacts/OI-F800-STAT-20261122-01/D008/store/BaseData/futures/TA_updto20240229_DBA/fao/prod/2021-01-01 21:00:00~2023-12-31 20:00:00/CommonPriceTurnGroupCandidatesFrp/3/9/a/1/9/2/a/4bbf414e0814726d92d156f2fe9b1f968/func`；fields SHA-256 `58ff1166df0e4bbdb84f4309b72947ee16de4a075d8992681fd60f46ccfb887c`。
6. G已执行：`2026-11-22T17:45:18.617683+00:00` 至 `2026-11-22T17:46:08.015410+00:00`，G1—G8可支持全量/分层剖面、finding复验、问题/案例/适配与原生Gate均已形成。
7. 当前运行/统计阻断：无。原生G后继：原manager消费D008，以最新U/X/G、finding和已知限制按CurrentReviewTarget处理FeatureReleaseGate/UpstreamReleasePackage；需场景时按原Workflow进入观察材料M与Skill1/2。本D不自动启动Q/V。。新结构疑点 0 项，场景问题 4 项；后继释放由原manager依CurrentReviewTarget处理。

## 当前版本、范围和独立读回

正常make_features构造基线F后只增加observation_multiple=800；其余inputs/sources/domain/result_layout/schema及SOF/Calendar/steel不变。delta=600 CalendarUTITick，2Δ=1200UTI，800Δ=480000UTI=4000开放分钟；revision尾6Δ=30分钟，handoff尾18Δ=90分钟，method.revision仍1。PNV未修改。当前源码827文件、实际构建二进制、Python构造/模块及原生进程已绑定。

请求范围固定rb/hc/i、5m、2021-01-01—2023-12-31、night_end_at_2300、TA_updto20240229_DBA。实际首末KLine `2021-01-04 09:05:00`—`2023-12-29 15:00:00`；每品种 49683 个位置，三品种共 149049 行，共享Calendar轴不乘3。每品种69个原始非有限close仍保留。独立OnlyRead PID `2056978` 与生产PID不同，31表全部与生产后读表hash、行数和列相同；另12个准确上游实例15表只读导出。当前对be57和ac基线上游15表均逐字相同，代码/行为比较基于同一输入。原生落盘文件及完整公开CSV清单已保存。

## 业务链、计数与全量剖面

KLine/Calendar → Rct实际位置 → 两轮ScaleTurn资格/已知时间 → 材料与四项pair → 候选Life/Revision → 正式publication及exact形成参与。原始分母按Rct可识别实际位置去重，不等于所有市场潜在转折；ScaleTurn按symbol/round/confirm定位，含3个初始化锚点，非初始化另报。成员关系行和Required行是观点内关系，不能当作上游位置或候选组数；publication事件亦不等于Revision occurrence。

| symbol | raw_turn_positions | scale_turn_positions | used_scale_turn_positions | candidate_lives | candidate_revision_occurrences |
| --- | --- | --- | --- | --- | --- |
| rb | 2557 | 425 | 324 | 401 | 1274 |
| hc | 2584 | 430 | 315 | 375 | 1179 |
| i | 4932 | 1004 | 236 | 310 | 1003 |
| ALL_DISTINCT | 10073 | 1859 | 875 | 480 | 1538 |

品种层的候选包含关系会跨层重叠，ALL_DISTINCT为全局去重。本次 480 Life、1538 Revision occurrence、1217 publication事件；用了 875/1859 个不同尺度位置。actual/几何confirm/selected知识分别保留，延迟分位数见profile/latency_by_symbol.csv。

| year | scale_turn_positions | candidate_lives | candidate_revision_occurrences |
| --- | --- | --- | --- |
| 2021 | 929 | 244 | 775 |
| 2022 | 642 | 162 | 515 |
| 2023 | 288 | 74 | 248 |

| session | input_5m_positions | candidate_lives | revision_occurrences | revisions_per_1000_input_positions |
| --- | --- | --- | --- | --- |
| DAY_CLOCK_09_15 | 32715 | 301 | 1005 | 30.7198532783127 |
| NIGHT_CLOCK_21_23 | 16968 | 179 | 533 | 31.412069778406412 |

状态占用以相邻已发表观点在知识轴的持有区间计算，按5m真实Calendar位置拆分分层，非内部逐Tick Dynamic trace。相邻Revision转换数=Revision-Life；生命周期是有限形成/修订责任，右删失单列。本次峰值责任内Life 36，样本末右删失 1。具体状态/分支/reason/同拍顺序、引用和SYMBOL/YEAR/MONTH/SESSION/OPENING/DIRECTION分布均见GlobalBehaviorProfile及profile CSV。

独立近actual跨品种pair筛查 648 条，800期限内positive 624 条；合格非否决pair未进任一候选筛查 0 条。首次阻断按实际已参加与明确参考规则分桶，非native未暴露计数。469/480 Life首次准入晚于旧6Δ期限，这是同输入的期限参考，没有运行新的K6实例，不能单凭此证明800合理。

## 原finding与全量副作用复验

GF001=`CLOSED_ON_LATEST_PROFILE`：原22位置及8个冷启动控制在新完整实例上通过原生Life/AsOf复验，全量连续有效输入误标不完整为 0。

GF002=`CLOSED_ON_LATEST_PROFILE`：原8观点按自然Life/known逐一对齐并通过原生AsOf复验；每个观点的三品种801行窗均保留69个原始非有限close，新flag均为1。完整新Revision总体中缺价窗内误标完整为 0，所有当前缺价影响窗观点详见MISSING_INPUT_WINDOW_VALIDATION。根因与FrozenExpectation沿已发布D006，FI沿D007，本G不重新诊断或改写原预期。

两项finding共38个历史位置的独立原生读取均通过。27项全量结构检查中，新待处理非零检查 0 项；所有previous/candidate/admission/member/alternative/bridge/子表父键和2Δ检查保留全量计数与空反例文件。

对最近be57：旧/新Life 480/480，自然匹配 480，仅旧/仅新 0/0；旧/新Revision 1534/1538。共同自然对象中UUID改变 480，跨版相同原始Revision UUID 0；UUID无跨运行稳定相等合同。已比较全部31表、全部共同自然Life×两版publication UTI并集 1538 点，状态不同 8 点，字段分布 {"coverage_incomplete": 8}，发行次数不同的Life/UTI 4 点。完整发行/差异和各版原生引用链分别保留，未用随机UUID相等判断业务等同。另对最初ac基线的全量同口径比较见InitialVersionComparison/comparison_ac，保护GF001历史闭环。

## 限制与原Workflow后继

四项原场景问题继续开放：i低参与及同步含义、时期/Session密度差异、800长责任及重叠意义、初始化锚点/稀有分支。当前候选索引使用新结果身份和时间位置，只是候选材料，未替代正式图上选场景。公开结果未暴露内部全部试探、逐Tick材料计数器或native每Turn首次阻断，不将参考筛查冒充正式轨迹。零分支不自动判不可达；统计Gate不等于全面业务合理性或Feature释放。

Q共享正常KLine适配的影响及Q独立数值边界限制继续传递，未运行/验证/释放Q或V；WALL M001没有变更。原manager按原L1核释放条件与依赖；如需场景解释，沿原Workflow进入观察材料和Skill1/2；本D未签新委派或放行下游。

准确D008、MP002 Owner原文、63个输入exact对象与远端I/D/批准一致性见SOURCE_REF_AUDIT、REMOTE_DISPATCH_READBACK和METHOD_LOCK。专业结果先发布，后续原V2 PRO_RETURN仅表示D008当前X/G职责REPORTED_COMPLETE，不表示manager已消费或业务Run已释放。
