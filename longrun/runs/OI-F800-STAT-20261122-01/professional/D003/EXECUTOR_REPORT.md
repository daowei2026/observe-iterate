# D003｜F800-GF-001 偏差诊断报告

已按锁定 Skill 完成单 finding 诊断。结论为 **ImplementationMismatch**：`GroupCandidateKLineInput.hs:109–112` 用两个已归一化浮点商的差严格等于1来判断相邻，真实600UTI边跨浮点量级边界时被误判为断点。不是当前数据缺口、冷启动、错绑或reader反读。本D未修改正式Feature、参数或输入处理。

## 准确输入与范围

原D003：`daowei2026/observe-iterate@a7fc7d76e4950978c04edf2777a049fd28f1b0c6:longrun/runs/OI-F800-STAT-20261122-01/delegations/D003/DELEGATION.json`，C0007/E1，workers=[]，回原manager。37项准确来源逐字节与Git对象核对，最新Owner原文逐字核对，见 [SOURCE_AUDIT.json](SOURCE_AUDIT.json)。

原 F800-DA-001 的冻结预期 `F800-INV-COVERAGE-001` / `FRP@ac1927518ad6105f15ffbe37fea45e4be91ba574` 保持不变：正常KLine固定rb/hc/i域、无未知Clock且三对象在[u-800Δ,u]有成功连续观测时，不应标记当前观察域不完整。。输入直接消费已接收D001与D002，不重做有效U/X/G。正式版本仍为FRP ac1927518ad6105f15ffbe37fea45e4be91ba574、TIS 2f460d663d821cf2ba25555eda13e78b697d0767；配置SHA `b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3`；rb/hc/i、5m、2021—2023、night_end_at_2300、TA_updto20240229_DBA/steel。正式目录与fields身份继续取原D002 FeatureRunResultBinding，未新生产。

## 可复现直接证据

2021-08-31 21:40到21:45，原UTI **78643199→78643799，差600**。代码step=5×120=600，而两个Double商为131071.99833333334与131072.99833333332，差 **0.9999999999854481**，所以 `position-p==1` 为False。三品种同拍各发生一次此假断点，跨过归一化2^17附近的表示精度边界。

源适配器因此声明`[78643799,78643799]`点，丢弃真实`[78643199,78643799]`相邻边。严格累计器正确地把它当不相接新片段，累计起点由72004199重启为78643799。之后直到u=79123799（2021-09-16 11:25）才再次积满480000UTI，即4000开放分钟。断点、相接累计、覆盖判定、候选发行、序列化/reader的逐阶段输入、规则、状态、时间和版本见 [ProcessingChain.json](ProcessingChain.json)。

独立Haskell Double小值实验结果：

| 对照 | 原商差guard | 原始UTI诊断判据 |
| --- | --- | --- |
| 断点前正常600UTI边 | True | True |
| 真实发生的600UTI数值边界 | False | True |
| 断点后正常600UTI边 | True | True |
| 跳过一根、相距1200UTI真实缺口 | False | False |

[HASKELL_DOUBLE_GUARD_PROBE.csv](HASKELL_DOUBLE_GUARD_PROBE.csv) 为当前真实执行结果。直接runghc先因缺libtinfo退出127；随后使用既有Stack环境运行同一独立脚本成功，没有安装系统库、编译或更改正式Feature。详见 [HASKELL_PROBE_VALIDATION.json](HASKELL_PROBE_VALIDATION.json)。

只读已有三品种UTI并重放锁定覆盖方程，在全部1546个已发表观点上，覆盖标志 **1546/1546一致、0差异**。仅在隔离方程中替换连续性guard，恰好改变原finding的22个观点、12个Life、18个时刻；8个冷启动标志保留，没有把所有flag强制清零。见 [EXPERIMENT_RESULTS.json](EXPERIMENT_RESULTS.json)、[PUBLISHED_FLAG_RECONCILIATION.csv](PUBLISHED_FLAG_RECONCILIATION.csv)、[DIAGNOSTIC_COUNTERFACTUAL_AT_PUBLISHED_LOCATIONS.csv](DIAGNOSTIC_COUNTERFACTUAL_AT_PUBLISHED_LOCATIONS.csv)。

这些是 **DIAGNOSTIC_ONLY派生重放**，不是未暴露的native内部trace；没有运行完整候选演化，不能据此宣布未来正式组数、观点数或UUID链。读取的输入文件SHA、6个FRP相关文件与加载runtime原件均核对，见 [CODE_AUDIT.json](CODE_AUDIT.json)。D002对22个窗口的三对象有效价格/801行连续UTI核验仍有效；本D未用缺价数据作反例。

## 竞争解释与责任

真实输入断点/夜盘跳跃与全轴600UTI步长不符；冷启动解释只适用于保留的8个对照，不适用于远离起点的22个位置；正常KLine每个Turn都携带Just Clock、patch为空，不是未知Clock等待；绑定、serializer和reader均与同一数据/方程相符。浮点guard假断点则同时预测了发生拍、累计起点、800Δ恢复边界及全部正式flag。逐项预测、检查、排除理由在 [DiagnosisReport.json](DiagnosisReport.json) 中。

ImplementationConformance与BusinessReasonableness分别报告：当前程序确实执行了写出的浮点guard，输出忠实反映其状态；但这个数值判据没有可靠实现已声明的相邻观测关系，因此属于实现不符。冻结覆盖预期在这些输入上仍适用，不因舍入而修改旧预期，也不产生新的业务取舍。未发现未决竞争解释；正式修复的通用实现与副作用验证仍是后继责任。

业务影响是22/1546=1.423%的正式观点把成功连续观测误报为缺覆盖，涉及12/480=2.5%的Life。该字段参与candidate affected/body比较，可能造成额外复评和修订；当前不估计完整修复后的总观点数、随机ID链或交易收益影响。按正式载荷正确性列为MEDIUM，释放前应修复验证或由Owner明确暂缓，不能因下游可能不读该字段而宣布无问题。

## 参数可修复性与具体修改提案

原生可修复性为 **PROVEN_NOT_ADJUSTABLE（限当前锁定输入及现有暴露参数）**。800与delta不进入source连续性guard；假断点让first=u后，无法覆盖此前真实正窗口。缩短K只缩短错误持续时间，不能恢复已丢失边；用极小W让浮点减法吞掉窗口、改变频率/单位或抑制候选，也不满足原预期。6Δ修订/等待、18Δ交接均在责任点之后。没有把“现有参数无解”扩大成“实现完全不可修复”；详见 [ParameterRepairability.json](ParameterRepairability.json)。本问题不应直接转盲目标定。

[ModificationProposal.json](ModificationProposal.json) 已准备为可审阅提案：在P2正常KLine适配器以源UTI及频率/Calendar的准确预期步长表达相邻，保留真实缺口/失知/冷启动边界；不改800、delta600、2Δ、正式范围或基线method.revision。其他频率/非整数步长须明确合同后实现，不能盲目round。当前没有准备、提交或推送正式候选patch，也未把诊断方程登记为正式版本。

提案列出保持现状、缩短K、浮点容差等替代及副作用；明确修复会影响稀疏Revision与exact引用。批准实施后先做数值边界/真实缺口/冷启动/Clock及原合同回归，再锁新版本完整X、31表独立回读和G，复验原22位置及全三年结构。局部算术通过不等于Feature释放。

正式行为改变须由Owner确认，依据 [原L0 §7](https://github.com/daowei2026/observe-iterate/blob/87b951bbd15078a2d6353bdd24afe0d8f19c845c/control-v0.3/01_L0_统计驱动的单特征闭环.md)：其§7.2将“正式 Feature 代码、业务规则和输出合同”及“把候选 patch／候选参数提交、推送或登记为本 Run 当前版本”列为确认后才能采用的改变。当前只回交分析、问题与提案，下一步由原manager提交Owner；本executor不代签批准。

没有需要Owner作价值取舍的第三类不确定性，故不生成OwnerDecisionPacket；这与正式修改仍需Owner确认是两回事。见 [OWNER_DECISION_APPLICABILITY.json](OWNER_DECISION_APPLICABILITY.json)。原G的4项场景问题不在本D范围，没有顺带裁决800是否合理。

## 当前交付与下一步

[DiagnosisReport.json](DiagnosisReport.json)、[MinimalDiscriminatingExperiment.json](MinimalDiscriminatingExperiment.json)、[RequirementOrImplementationIssue.json](RequirementOrImplementationIssue.json) 及提案均已完成；[FindingDisposition.json](FindingDisposition.json) 状态为DIAGNOSED_IMPLEMENTATION_MISMATCH_NOT_FIXED。原D002输出与GlobalProfileGate不改写。D003诊断职责完成，后继为manager消费→Owner修改确认→新D实施回归→X/G；不是已修复或FeatureRelease。

Owner七项进度：D001已接收；X已完成；准确结果来自D002一次新生产；原正式ts已运行结束、本C未启动Feature；目录仍为D002/store绑定实例；G1–G8已完成且未重复；本D无事实阻断，正式修复尚未授权。无Worker、无新委派、无跨线程发送，仅写授权工作区和本Run记录。专业结果先发布，再以已有exact提交形成C0007 PRO_RETURN，待原manager消费。
