# Owner修改确认项｜F800-MP-002（待独立批准）

## 具体请求与可审阅原件

是否批准 F800-MP-002：按已发布未应用 diff 修复正常 KLine 的缺价覆盖分类（非有限 close 发 InputMissing、清 previous，Clock 继续推进），保持现有参数、PNV 与正式范围，实施真实适配回归、提交／推送并采用新 FRP，再完整运行 F 的 rb/hc/i、5m、2021—2023，完成 31 表独立读回与全量 G？

请基于[原提案](https://github.com/daowei2026/observe-iterate/blob/46de903caa04be60a5600ef9f416445f5a6366cd/longrun/runs/OI-F800-STAT-20261122-01/professional/D006/ModificationProposal.json)、[未应用的具体diff](https://github.com/daowei2026/observe-iterate/blob/46de903caa04be60a5600ef9f416445f5a6366cd/longrun/runs/OI-F800-STAT-20261122-01/professional/D006/F800-MP-002.proposed.diff)和[依赖影响](https://github.com/daowei2026/observe-iterate/blob/46de903caa04be60a5600ef9f416445f5a6366cd/longrun/runs/OI-F800-STAT-20261122-01/professional/D006/ContractAndDependencyImpact.json)批准、给出具体范围调整、明确暂缓或拒绝。原MP-001批准只覆盖数值相邻修复及复验，不包括本次价格有效性分类。发布本包不代表批准。

提案exact：`daowei2026/observe-iterate@46de903caa04be60a5600ef9f416445f5a6366cd:longrun/runs/OI-F800-STAT-20261122-01/professional/D006/ModificationProposal.json`；diff exact：`daowei2026/observe-iterate@46de903caa04be60a5600ef9f416445f5a6366cd:longrun/runs/OI-F800-STAT-20261122-01/professional/D006/F800-MP-002.proposed.diff`。diff为1630字节，SHA-256=`95d05a657e16537da28aaeea89d5d00c1302fc6c6427e801388c4985ac314d9e`。原status=PROPOSED_NOT_AUTHORIZED_NOT_APPLIED，diff_applied=false、diff_compiled_or_integration_tested=false；本包未改写、应用或编译候选。

## 已确认问题与基线

[原生诊断](https://github.com/daowei2026/observe-iterate/blob/46de903caa04be60a5600ef9f416445f5a6366cd/longrun/runs/OI-F800-STAT-20261122-01/professional/D006/DiagnosisReport.json)确认ImplementationMismatch：实际PNV三品种各有69个缺价位置，当前固定域没有不适用豁免；正常KLine适配丢弃close有效性，只按相邻UTI发Observed并恒更新previous，8个已发布Revision/5个Life/6个时刻因而标完整。影响8/1534 Revision（0.5215%）、5/480 Life（1.0417%）；完整标记1526中的占比另为0.5242%。旧版同位置8/8亦存在，是既存缺陷；原GF-001已由D005完整复验关闭，不重新打开。

当前FRP=`daowei2026/frp@be57d6752c9d43d10f1d670e1d2993bb8153ea7c`，TIS=`daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767`，完整配置SHA-256=`b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3`。D005完整正式X/独立31表读回/G仍为当前未修复版本的有效结果，没有MP-002新版本或修后正式结果。

## 原提案修改范围

具体diff只涉及`src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateKLineInput.hs`正常advance的价格覆盖分类和previous成功邻接状态：保留同拍close，有限close沿原Observed/精确UTI相邻规则；非有限close（NaN/±Infinity）发`CoverageInputMissing Nothing Nothing`并清previous，恢复首个有效价先记成功点，之后真实相邻边才累计。

缺价拍仍推进有效UTI/Clock，原Turn/失知/exactUTI处理保持；不按零成交量或无Turn判失败，不填价、不重建PNV、不删除Calendar时格、不重新定义coverage。按原提案增加必要真实adapter分类回归；正式参数、硬编码常量、domain/sources/result_layout、保存schema、用例和范围不改。

保持observation_multiple=800、delta=600、CalendarUTITick、实际2Δ=1200UTI、method.revision=1；F-only rb/hc/i、5m、2021—2023、night_end_at_2300、TA_updto20240229_DBA、steel。请求在原工作区`/dwdhome/fy/BASE_E6_2_copy`和原FRP分支`codex/f-observation-multiple-20261122`实施、回归、提交/推送并采用真实新commit；实际新版本/二进制/配置和结果身份由后续回交绑定，不预填未来commit。

## 证据与尚不能承诺的影响

[最小实验](https://github.com/daowei2026/observe-iterate/blob/46de903caa04be60a5600ef9f416445f5a6366cd/longrun/runs/OI-F800-STAT-20261122-01/professional/D006/MinimalDiscriminatingExperiment.json)和[原生结果](https://github.com/daowei2026/observe-iterate/blob/46de903caa04be60a5600ef9f416445f5a6366cd/longrun/runs/OI-F800-STAT-20261122-01/professional/D006/ExperimentEvaluation.json)包括实际PNV/12个边界对照、三个模式各1672拍×3对象与8项原生控制；Observed模式复现8/8已发布flag=0，改缺价分类并清previous的两种干预均使8/8不完整，重新积满800Δ后恢复。原参数能力证明为[PROVEN_NOT_ADJUSTABLE](https://github.com/daowei2026/observe-iterate/blob/46de903caa04be60a5600ef9f416445f5a6366cd/longrun/runs/OI-F800-STAT-20261122-01/professional/D006/ParameterRepairability.json)，限当前明确能力；调800/600、2Δ、频率或期限不能恢复丢弃的有限价/NaN区别。

这些是纯覆盖子链重放，未执行正常adapter完整Reflex生产图、未生成修后F候选/UUID。具体diff尚未编译或集成测试，真实adapter回归及完整新X/G须批准后执行。不能据8个样本承诺只改8个观点或保持Life/Revision/发行次数/UUID不变。

覆盖标记参与候选正文与稀疏发行，Revision时点/数量及UUID/exact链可能改变。共享正常适配可能影响Q，Q另一路数值边界限制继续传递，V有依赖影响；本请求只运行F，不运行或释放Q/V，不批准WALL M001。输入缺失供应/生成端原因尚未定位，本提案不修该上游数据，只使实际缺价不被标为成功完整观测。

原提案另列替代：只修历史PNV不能让adapter识别未来缺价，且本次未定位供应端原因；调800/600或改域/Calendar不能表达有限价与缺价区别；把coverage重定义为仅代表时格须另立业务目的与预期。这些均不包含在本次局部修正许可中，不能因批准MP-002而采用。

## 原验证计划与批准后的既定回交

完整要求以原ModificationProposal.validation_plan六项为准，本包仅整理范围：

1. 真实KLine→frame分类回归：有限价、NaN/±Infinity、warm后单/连续缺价、单成员失败、有限价零量/无Turn；不能只手造SourceFailure替代分类位置验证。
2. 回归GF-001精确UTI/真实间隙/冷启动/2Δ，以及失败、失知、明确不适用、恢复满800Δ边界和revision/引用职责。
3. 批准后由原E1实施并提交/推送、采用新FRP，绑定真实code/binary/config/dependency；测试失败不得采用。
4. 核实际加载/完整配置/范围/Calendar/结果身份和真实单写者，持重型资源实际flock；新attempt/store保留D005及所有历史，完整三年正式F X、独立31表OnlyRead及fields/config身份回读。
5. 原Skill全量G复验8位置自然对象及GF-001的22+8控制，检查缺价窗冲突和exact链，实测当前480 Life/1534 Revision/1216发行的变化，保留场景问题和Q限制。
6. manager消费真实新X/G与finding处置后依原L1形成FeatureReleaseGate/适用ReleasePackage；批准、子链重放或局部回归不等于释放。

若批准，controller将真实答复纳入采用授权后，原manager签新的既有FI工作给原E1，再沿原Workflow补受影响理解绑定/完整X/独立读回/G；不重做完整Feature Understanding。调整、暂缓或拒绝按真实决定续接，不预置Owner接受限制。

## 独立确认的明确依据

本C派工 `daowei2026/observe-iterate@5c6ff5eb7fb039704c0185af6bcfa77cb0cae7c9:longrun/runs/OI-F800-STAT-20261122-01/calls/C0015/FULL_ASSIGNMENT.md` 明确：“MP002尚未获得Owner批准，候选diff未应用；MP001批准不得扩大到MP002。”原L0 §7.2 `daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:control-v0.3/01_L0_统计驱动的单特征闭环.md`将“正式 Feature 代码、业务规则和输出合同”及候选提交/推送/采用列为Owner确认范围。

`daowei2026/observe-iterate@46de903caa04be60a5600ef9f416445f5a6366cd:longrun/runs/OI-F800-STAT-20261122-01/professional/D006/OwnerDecisionApplicability.json`明确本案无待Owner选择的业务目标取舍，故不造OwnerDecisionPacket；新增正式行为修改仍须独立确认。当前WAITING_OWNER仅针对本MP-002许可；未签施工D、未改Feature或重复有效X/G。
