# D004｜已批准 F800-MP-001 的 FI 工程修正

issuer_call_id=C0009；manager=`codex:OI-F800-STAT-20261122-01:manager`；recipient=`codex:OI-F800-STAT-20261122-01:executor:E1`；return_to=`codex:OI-F800-STAT-20261122-01:manager`。复用本Run原E1，CODEX_NATIVE_DIRECT，workers=[]。本文件与DELEGATION.json共同限定本次委派；实际派发及物理线程前检由controller完成。

节点采用 `daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:control-v0.3/03_L2_节点输入输出与完成状态.md` 的FI工程修正行，并沿 `daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:control-v0.3/01_L0_统计驱动的单特征闭环.md` §7、§9执行已确认修改。FI是既有工程动作；本D绑定该节点，不新建Skill。原生实现回交合同位于 `daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:control/03_L1_合理性分析流程.md` §8.1，消费和后继见同版control/04的XI行及control/05外部实现返回Gate。

本次真实批准为 `daowei2026/observe-iterate@8a4139b9250ed78c602f4c54b36a08380b196057:longrun/runs/OI-F800-STAT-20261122-01/owner-decisions/F800-MP-001/OWNER_APPROVAL.original.txt`；采用Binding为 `daowei2026/observe-iterate@bff656a28bafbd10919e05a01d799c20d0d25fad:longrun/runs/OI-F800-STAT-20261122-01/RUN_BINDING.json`；具体提案为 `daowei2026/observe-iterate@a99ab37cdcf43759b7f203a1233fe69a7fa733db:longrun/runs/OI-F800-STAT-20261122-01/professional/D003/ModificationProposal.json`。Owner答复“批准 F800-MP-001，实施修复并完整复验”。原诊断 `daowei2026/observe-iterate@a99ab37cdcf43759b7f203a1233fe69a7fa733db:longrun/runs/OI-F800-STAT-20261122-01/professional/D003/DiagnosisReport.json`、问题 `daowei2026/observe-iterate@a99ab37cdcf43759b7f203a1233fe69a7fa733db:longrun/runs/OI-F800-STAT-20261122-01/professional/D003/RequirementOrImplementationIssue.json`、反例和冻结预期适配包均以JSON所列exact输入传递，承载既有实现接口的专业事实；专业方法和验证计划沿原提案与既有Workflow，不另写预期或验收条件。D003为已完成诊断的历史输入，本D提供新的施工委派及真实批准绑定。

具体修改、回归、提交/推送/采用权限限F800-MP-001及新Binding相应grants；Owner批准的参数、TIS、用例和正式范围保持。旧BusinessTaskInput的FRP ac192751版本为修复前基线，新版本必须由真实ImplementationFixReturn绑定。WALL M001仍未批准，本Run不扩为Q/V正式生产。

按原生ImplementationFixReturn回交真实commit、文件、行为、测试、新版本及可重跑状态。当前D004仅委派实施节点；manager消费实施回交后自动按结构合同变化转受影响U或直接X，再完整X、31表独立读回、G、finding及释放后继，无需再次确认已批准范围。完整比较与正式复验在原Workflow中衔接，局部回归不等于释放。具体实施由原E1亲自完成，manager不代施工。

操作/写面以DELEGATION.json所列新Binding子集为准。后继重型正式生产仍按本C FULL_ASSIGNMENT所指既有HEAVY_RESOURCE_POLICY.json取得实际flock并核真实单写者；文件存在不构成持锁证据。新attempt/store保留原D002/D003。超出原提案的新行为修改或真实阻断按原Workflow如实回交。
