# D006｜GF-002条件覆盖诊断与独立修改提案

GF-002已确认是正常KLine适配的既存实现偏差。当前实际消费的PNV中，三品种各69个位置确实没有有效价格；当前固定域无不适用豁免。适配器却丢弃close有效性、仅按有效且相邻的UTI恒发行CoverageObserved，使8个已发布观点的`groupCoverageIncomplete=0`。这不是本次CSV临时补空、读回反转、800参数标定问题或be57新引入的回归。

本C完成D006原Skill诊断并提出 **F800-MP-002**；未实施、提交或采用Feature改变，未重跑有效X/G。原GF001关闭结论和D005全部原件保留。新正式行为改变须由原manager携本提案向Owner取得独立确认，MP001批准不外延。

## 准确输入与授权

- 委派：`daowei2026/observe-iterate@f076db5afb51cc6b02502007713d7f83be97b9ad:longrun/runs/OI-F800-STAT-20261122-01/delegations/D006/DELEGATION.json`，C0014，原E1，workers=[]。
- 方法：`daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/reasonableness-analysis/business-discrepancy-diagnosis/SKILL.md`；本次亲自读取，既有适用补充沿准确版本复用。FULL_ASSIGNMENT及Owner最新原文按原件读取，51项exact来源和远端I/D blob匹配见审计。
- 冻结预期`F800-INV-COVERAGE-GAP-002`原文见FrozenExpectation.json；先核前件而非预置NaN必然是缺陷。D005适配包`F800-DA-D005-complete_flag_with_input_price_gap`保持原文。
- 当前FRP `be57d6752c9d43d10f1d670e1d2993bb8153ea7c`、TIS `2f460d663d821cf2ba25555eda13e78b697d0767`，配置SHA-256 `b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3`；800、delta600、2Δ=1200和原SOF/Calendar/范围保持。
- 只在BASE本D006产物目录和Run记录分支写诊断/记录；没有新正式生产、源代码写入、源采用/推送、Q/V或WALL工作。

## 结论依据与边界

1. 直接读取SOF的三个实际Calendar PNV目录，与D005导出的49,683行逐一核同轴/close相同。每品种69行OHLC全NaN，close物理编码为`0x7ff8000000000000`，UTI仍按600相邻。自日历PNV在这些69时刻没有记录；缺口前后有限报价均存在且与Calendar文件相同。另用标准库mmap独立核12个边界点，排除自日历时间轴整体错位。证据：PNV_INPUT_PROBE、BINARY_BOUNDARY_PROBE、PNV_GAP_EXCERPT。
2. 真实读取链为PNV→native Bar→closeTs逐拍历史调度→close/closeUti同拍事件；此链未过滤NaN。当前配置为complete=true的rb/hc/i固定域、coverage=[]，实际正常KLine分支没有不适用豁免。Material既有合同要求缺价/失知/未观察间隙断开，不能以Calendar时格存在取消该合同。16个窄范围源码/消费点及当前库接口指纹见SOURCE_EVIDENCE。
3. 最小责任阶段是`GroupCandidateKLineInput.hs:buildKLineGroupSource.advance`：它将报价解构为`(_,known,_,u)`，丢弃价格，只以UTI调用恒Observed的`klineForwardCoverage`，并恒更新previous。Material有合法InputMissing/SourceFailure处理能力，但在收到frame前已失去该区别；观点/保存按收到的标记表达。
4. 使用同一be57已安装原生库的实际`klineForwardCoverage`、`advanceMaterial`（含真实累积函数），三模式各重放1,672拍×3对象。实际Observed模式复现8/8已发布flag=0；仅把缺价分类改为SourceFailure或提案的InputMissing并清邻接状态，两模式8/8均为不完整。恢复首个有效点为UTI93715799，满480000后UTI94195799才重新完整。8项控制验证冷启动、无Turn正常流、单对象失败/缺价/失知、真实间隙和明确不适用。
5. 已有旧base同自然对象/known比较8/8也是0，因此是本轮新识别的既存缺陷，未重新打开GF001。当前受影响8/1534 Revision（0.5215%）、5/480 Life（1.0417%）、6个known，完整标记1526中占0.5242%。未量化Q/V损失，不据此断言转折正文或所有业务判断错误。

纯函数重放仅验证覆盖子链，不运行Reflex生产图、不生成新候选/UUID，也不是修后完整正式结果。原正式运行未暴露逐拍frame轨迹；入口分类由准确源码证明，后果由原生子链重放验证。上游行情为何缺失仍未追溯至供应/生成端；该事实缺口不影响adapter把实际缺价错称成功观测的定位。

## 参数能力与后继

ParameterRepairability状态为`PROVEN_NOT_ADJUSTABLE`，仅针对当前已明确参数能力。800×600控制期限；2Δ控制pair贴近；freq/Calendar换算控制UTI步长；6Δ/18Δ控制等待/修订/交接；它们均不消费价格有效性。相同UTI/Clock、无Turn且仅价格有限/NaN不同的输入，会被当前适配投影成相同覆盖，对所有这些参数不可区分。拉长至所有窗口均不完整或改变域/Calendar/范围是掩盖或改变问题，不能修复当前合同；无需盲调或正式参数标定。

RequirementOrImplementationIssue主类为ImplementationMismatch；实际PNV缺价是并存数据质量事实，供应端原因未定位。没有尚待Owner选择的业务目标取舍，因此不造OwnerDecisionPacket；OwnerDecisionApplicability说明了这一点。新正式行为确认则按FULL_ASSIGNMENT/L0单独执行。

F800-MP-002附未应用的可审阅diff：正常适配保留close；有限价沿原精确UTI规则Observed，非有限价发CoverageInputMissing并清previous，Clock进展仍保留；恢复先成功点后相邻边。不按零量或无Turn判失败，不填价，不改800/600/2Δ、配置/域/范围或对外schema。验证方案要求真实适配分类回归、原GF001/覆盖边界回归、批准后提交采用新FRP并完整三年X、31表独立读回及原Skill全量G，实测Revision/发行/UUID链变化。

共享正常适配可能影响Q；Q另一路数值边界限制继续保留。本Run不运行或释放Q/V。无新FeatureReleaseGate/ReleasePackage；原D005 GlobalProfileGate=DIAGNOSIS_REQUIRED保持原件，由manager消费诊断和批准后的后继成果按原L1处理。

## 原Owner要求的进度

| 项目 | 当前准确状态 |
|---|---|
| D001 | 已接受；未重做完整Feature Understanding |
| X是否开始 | D005新be57完整正式X已完成且有效，本C不重复 |
| 复用/新生产 | 复用D005合法结果及独立31表读回，不把存在目录当可复用证明 |
| 正式进程 | D005真实进程已退出0并释放生产锁；本C未启动Feature |
| 当前结果目录 | `/dwdhome/fy/BASE_E6_2_copy/artifacts/OI-F800-STAT-20261122-01/D005/store/BaseData/futures/TA_updto20240229_DBA/fao/prod/2021-01-01 21:00:00~2023-12-31 20:00:00/CommonPriceTurnGroupCandidatesFrp/3/9/a/1/9/2/a/4bbf414e0814726d92d156f2fe9b1f968/func` |
| G全量统计 | D005 G1—G8已完成有效，26项结构检查0冲突，GF002本候选8点已在本C诊断；未重统计 |
| 当前阻断/后继 | D006诊断无事实阻断，工作已完成；正式修正待新MP002明确批准和新委派，当前不释放Feature |

## 原生交付与验证

DiagnosisReport、MinimalDiscriminatingExperiment、RequirementOrImplementationIssue、ParameterRepairability、ModificationProposal、ContractAndDependencyImpact，以及8个精确Case和输入/原生重放证据均在本目录。WORKFLOW_COMPLETION逐项对应原Skill步骤；VALIDATION记录实际检查。原V2 Return须先发布本专业结果并远端回读，再引用已有exact提交单独发布，回原manager。完整CLI与Codex manager身份的既有不兼容边界会如实记入Return校验；不改锁定gate、不伪造controller receipt。
