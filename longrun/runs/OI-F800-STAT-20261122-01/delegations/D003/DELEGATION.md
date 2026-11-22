# D003｜F800-GF-001 偏差诊断

- run_id：`OI-F800-STAT-20261122-01`；work_id / parent_task_id：`OI-F800-STAT-20261122`；work_item_id：`F800-DIAG-GF001`；stage_instance_id：`F800-DIAG-001`（原 L0 偏差诊断节点）；issuer_call_id：`C0006`。
- issuer / return_to：`codex:OI-F800-STAT-20261122-01:manager`；recipient：`codex:OI-F800-STAT-20261122-01:executor:E1`，本 Run 原 E1；`CODEX_NATIVE_DIRECT`；workers=[]。
- 本 D 签发时尚未派发，后续由 controller 复用原 E1；manager 不创建线程或跨聊天发送。

## 准确 Skill 与既定任务

唯一 Skill：`daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/reasonableness-analysis/business-discrepancy-diagnosis/SKILL.md`；适用补充：`daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/reasonableness-analysis/STATISTICS_DRIVEN_PRACTICE.md`。专业方法、输出和完成条件直接依上述原件及已采用 control-v0.3 L0 §5—7。

本项仅处理 G 的单个 `F800-GF-001`（原生类型 `STRUCTURAL_FINDING_CANDIDATE`），输入适配包为 `F800-DA-001`。D002 原生 GlobalProfileGate=DIAGNOSIS_REQUIRED 已明确将该 finding 路由到本 Skill，本 D 不预置根因、责任层、修改方案或额外专业 Gate。

## 当前输入与已完成范围

最新合法 Return：`daowei2026/observe-iterate@2754c9595641983e3e2185d122c6dce93868eb47:longrun/runs/OI-F800-STAT-20261122-01/calls/C0005/PRO_RETURN.json`；专业报告：`daowei2026/observe-iterate@3169703e769340200b183dad7675a1d22ecc1850:longrun/runs/OI-F800-STAT-20261122-01/professional/D002/EXECUTOR_REPORT.md`；最新 Owner 原文：`daowei2026/observe-iterate@e25acf900cca64f24a54ab0d9721b35ddce382e6:longrun/runs/OI-F800-STAT-20261122-01/calls/C0006/FULL_ASSIGNMENT.md`。

当前正式 X 已新生产并完成独立只读读回，G1—G8 已完成。准确运行绑定：`daowei2026/observe-iterate@3169703e769340200b183dad7675a1d22ecc1850:longrun/runs/OI-F800-STAT-20261122-01/professional/D002/FeatureRunResultBinding.json`；完整剖面：`daowei2026/observe-iterate@3169703e769340200b183dad7675a1d22ecc1850:longrun/runs/OI-F800-STAT-20261122-01/professional/D002/FeatureGlobalBehaviorProfilingResult.json`；专业 Gate：`daowei2026/observe-iterate@3169703e769340200b183dad7675a1d22ecc1850:longrun/runs/OI-F800-STAT-20261122-01/professional/D002/GlobalProfileGate.json`。这些当前有效成果供本项直接消费，不重复有效生产/统计或完整 Feature Understanding。

本项输入为 `daowei2026/observe-iterate@3169703e769340200b183dad7675a1d22ecc1850:longrun/runs/OI-F800-STAT-20261122-01/professional/D002/GlobalFindingCandidates.json` 中的 F800-GF-001 及 `daowei2026/observe-iterate@3169703e769340200b183dad7675a1d22ecc1850:longrun/runs/OI-F800-STAT-20261122-01/professional/D002/DiagnosisInputAdapters.json` 中的 F800-DA-001。原 FrozenExpectation、EvidenceComparisonPackage、BusinessIntent、ProcessingChain、代码/需求和数据/时间绑定均按该已发布适配包读取，包内定位选择符保留原文，不由 manager 重写。

G 回交的观测范围为22个观点发生、12个Life、18个发行时刻；原生结论仍是待诊断候选。统计就绪性原生为PARTIAL，其具体可用性/内部轨迹限制按已发布 StatisticsInputReadiness 保留。相关证据、候选索引和既有理解均为 DELEGATION.json.input_refs 中的准确已发布原件。

Feature/参数/范围继续锁定：CommonPriceTurnGroupCandidatesFrp（只f）；FRP ac1927518ad6105f15ffbe37fea45e4be91ba574，TIS 2f460d663d821cf2ba25555eda13e78b697d0767；配置 SHA-256 `b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3`；observation_multiple=800、delta=600、CalendarUTITick、method.revision=1；rb/hc/i、5m、2021—2023、night_end_at_2300、TA_updto20240229_DBA、steel。正式结果路径和fields身份以所引FeatureRunResultBinding为准，工作区为 `/dwdhome/fy/BASE_E6_2_copy`。

## Owner 权限与回交

初始 Owner GO：`daowei2026/observe-iterate@43a13e14129984d6f3a142c6eb64397a43c3ca79:longrun/runs/OI-F800-STAT-20261122-01/OWNER_START.md`；最新继续指令：上引 C0006 FULL_ASSIGNMENT 中逐字 Owner 原文；Binding：`daowei2026/observe-iterate@2665f0cbabff0439fe8d361c2ad545bf922e1792:longrun/runs/OI-F800-STAT-20261122-01/RUN_BINDING.json`；资源绑定：`daowei2026/observe-iterate@2665f0cbabff0439fe8d361c2ad545bf922e1792:longrun/runs/OI-F800-STAT-20261122-01/RUN_RESOURCE_BINDING.json`。

本 D 机读权限仅取原 grants 的 run_result_statistics_analysis_write、run_record_write 及原工作区/本Run记录写面。实际诊断操作按原 Skill/profile/V2 和 Owner 范围执行；签发本 D 不追加正式 Feature 行为修改授权。若诊断建议正式改变，沿已采用 L0 的 ModificationProposal→Owner确认链；确认前不实施、提交、推送或采用新的正式行为。

原生输出依 Skill，包括 DiagnosisReport、适用的实验/问题/Owner决策材料以及真实下一路由。专业报告和 V2 executor PRO_RETURN 回 `codex:OI-F800-STAT-20261122-01:manager`，绑定本 D 发布后的 exact ref。issued_order_refs=[]、accepted_worker_refs=[]；不将候选 finding、D002交付或本次签发改写为已诊断、已修复或Feature释放。
