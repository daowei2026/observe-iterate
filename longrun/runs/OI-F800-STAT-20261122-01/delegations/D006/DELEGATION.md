# D006｜单 finding F800-GF-002 偏差诊断

issuer_call_id=C0013；issuer=`codex:OI-F800-STAT-20261122-01:manager`；recipient=`codex:OI-F800-STAT-20261122-01:executor:E1`；return_to=`codex:OI-F800-STAT-20261122-01:manager`。CODEX_NATIVE_DIRECT，复用本Run原E1，workers=[]；实际派发和原线程前检由controller完成。

唯一专业Skill为 `daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/reasonableness-analysis/business-discrepancy-diagnosis/SKILL.md`，适用补充及Workflow均按DELEGATION.json所列锁定版本。当前输入是D005已完成且有效的新版本X/G；原生Gate `daowei2026/observe-iterate@38e2af72be826a1e98fd7f5d4522c50d218750f3:longrun/runs/OI-F800-STAT-20261122-01/professional/D005/GlobalProfileGate.json` 为DIAGNOSIS_REQUIRED并要求此诊断。委派只绑定该既有方法、准确输入、原生输出及原授权，不重写专业方法或另设Gate。

单finding=`F800-GF-002`；准确候选 `daowei2026/observe-iterate@38e2af72be826a1e98fd7f5d4522c50d218750f3:longrun/runs/OI-F800-STAT-20261122-01/professional/D005/GlobalFindingCandidates.json`；原生适配包 `daowei2026/observe-iterate@38e2af72be826a1e98fd7f5d4522c50d218750f3:longrun/runs/OI-F800-STAT-20261122-01/professional/D005/DiagnosisInputAdapters.json` 中adapter_id=`F800-DA-D005-complete_flag_with_input_price_gap`，冻结预期ID=`F800-INV-COVERAGE-GAP-002`。V2机读引用采用whole-file exact对象，包内原生定位与条件保持原文。该预期明确以实际非豁免缺价/SourceFailure/失知或未观察间隙为前件，公开OHLC空值是否满足此前件尚待诊断；不把统计观察直接登记为业务冲突、真实SourceFailure或实现根因。

当前FRP `be57d6752c9d43d10f1d670e1d2993bb8153ea7c`，TIS `2f460d663d821cf2ba25555eda13e78b697d0767`，配置SHA-256 `b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3`；正式结果/范围依 `daowei2026/observe-iterate@38e2af72be826a1e98fd7f5d4522c50d218750f3:longrun/runs/OI-F800-STAT-20261122-01/professional/D005/FeatureRunResultBinding.json`，当前最小理解依 `daowei2026/observe-iterate@38e2af72be826a1e98fd7f5d4522c50d218750f3:longrun/runs/OI-F800-STAT-20261122-01/professional/D005/CurrentFeatureUnderstandingPackage.json`，统计证据、反例窗口、历史同事实与原生条件均由准确输入传递。原GF-001已在该最新profile关闭，不合并重诊或重复有效完整X/G、完整U。GF-002是新识别的既存候选，原包记录8/8旧版同位置亦存在，不预写为be57新引入回归。

输出按原Skill的DiagnosisReport、MinimalDiscriminatingExperiment、RequirementOrImplementationIssue及适用时OwnerDecisionPacket/原L0提案链，回原manager。事实缺口与可由证据解决的不确定性依原Skill继续分析；正式改变沿原Owner确认流程，不把缺少事实直接提交Owner取舍。

权限限本D JSON的分析/记录写面子集。`daowei2026/observe-iterate@8a4139b9250ed78c602f4c54b36a08380b196057:longrun/runs/OI-F800-STAT-20261122-01/owner-decisions/F800-MP-001/OWNER_APPROVAL.original.txt` 与 `daowei2026/observe-iterate@bff656a28bafbd10919e05a01d799c20d0d25fad:longrun/runs/OI-F800-STAT-20261122-01/RUN_BINDING.json` 只使已批准F800-MP-001修复/复验有效，未授权本新finding的正式行为或输入处理改变；本D不含新正式生产、Feature正式修改/提交推送采用、Q/V或WALL M001权限。正常诊断与隔离分析沿既有Workflow/资源约束进行；后继由真实专业结果决定。
