# D003｜原偏差诊断 Skill 与授权范围内的 X 恢复

本 D 绑定一项现有偏差诊断 Skill。专业方法、输入核实、责任逻辑定位和原生产物均遵循准确 Skill 原文；诊断后的授权处理、必要回归与恢复 X 属于已采用 L0 的实际动作，不新建实现修改 Skill 或专业 Gate。

- run_id：`OI-EAW-P1-BUILD-STAT-20261124-01`；work_id：`OI-EAW-P1-BUILD-STAT`；business_case_id：`EAW-P1-BUILD`。
- work_item_id：`EAW-P1-BUILD-X-RECOVERY-R01`；stage_instance_id：`DIAG-X-R01`。
- delegation_id：`D003`；issuer_call_id：`C0005`。
- issuer / return_to：`codex:OI-EAW-P1-BUILD-STAT-20261124-01:manager`；recipient：`codex:OI-EAW-P1-BUILD-STAT-20261124-01:executor:E1`，继续复用本 Run 原 E1。
- 专业控制：`391adcd18bd2da82c13c01710980f41e01c7de25`；CODEX_NATIVE_DIRECT／AUTONOMOUS／workers=[]。
- 本次 Skill：`daowei2026/observe-iterate@391adcd18bd2da82c13c01710980f41e01c7de25:skills/reasonableness-analysis/business-discrepancy-diagnosis/SKILL.md`；适用补充：`daowei2026/observe-iterate@391adcd18bd2da82c13c01710980f41e01c7de25:skills/reasonableness-analysis/STATISTICS_DRIVEN_PRACTICE.md`。
- 原 L0：`daowei2026/observe-iterate@391adcd18bd2da82c13c01710980f41e01c7de25:control/01_L0_统计驱动的单特征闭环.md`；唯一业务输入：`daowei2026/observe-iterate@391adcd18bd2da82c13c01710980f41e01c7de25:task-inputs/eaw-p1-build-stat-20261124/BUILD_RUN_INPUT.md`。
- 真实 X 原件：`daowei2026/observe-iterate@150858c767c229951bf3fce587e6bb09752364ec:longrun/runs/OI-EAW-P1-BUILD-STAT-20261124-01/delegations/D002/results/X-R01/FeatureRunResultBinding.json`；准确 Return／报告／未完成范围／继续入口均列于 DELEGATION.json。
- 当前有效 U：`daowei2026/observe-iterate@6b8122773e04046e154ce1839efe66912bd5b526:longrun/runs/OI-EAW-P1-BUILD-STAT-20261124-01/delegations/D001/results/U1/FeatureUnderstandingPackage.json`。

当前工作来源为真实 X 运行偏差：rb 全年结果及六个公开流最终严格读回有效；m 的 Build 原生调用失败且无产物／receipt，完整 rb/m X 未完成。堆栈、输入轴差异和 17 个全空报价时点仅为已发布事实，当前没有责任逻辑定位或正式 G finding。现有 Skill 的「真实输入／输出与原预期不一致、存在多种解释、改动前需定位来源」适用范围见原件；本项不将局部 X 冒充完整 G 前提。

原 Skill 必需的 FrozenExpectation／BusinessIntent 来源为正式业务输入、初始 GO 与原 L0 X；可核对的实际比较证据及 DataBindingAndTimeBasis 来源为上述 X 绑定／报告；ProcessingChain 和 RelevantCodeOrRequirementRefs 来源为准确 U、X 堆栈及其原始实现／业务来源。其含义、可用性及事实缺口由 E1 按原 Skill 据实核定和补查，manager 不撰写新的业务预期或专业方法。

D002 的窄 X 范围保留为历史委派，不撤销初始 Owner GO 对本 Run 的工程授权。本 D 沿初始 GO 覆盖本项诊断后有据的 Build 自身必要处理、直接相关测试／回归、当前正式 X 恢复及指定分支普通 commit/push；实际处理和完成判断依原 Skill、L0 与原 GO。若问题来自上游或无法在原范围继续，依原正式输入／Skill形成有据 UpstreamFinding／ScopedBlocker及恢复条件。原生产物为 DiagnosisReport、责任逻辑定位及恢复过程中按原 L0 更新的 FeatureRunResultBinding；未完成部分据实回交，不强造成功。

权限引用为原 OWNER_START／RUN_BINDING／Resource／本 C FULL_ASSIGNMENT，准确 refs 均已列入 JSON。代码写面仅为原 GO 的 Build 自身文件、直接相关测试及 Build 参数／业务常量；TIS 基线 `179016111ed0394f92025313e46bd13534932a74`，允许目标 `codex/oi-eaw-p1-build-fix-20261124-01`，不修改原 Wall 分支。Wall、其它上游、公共处理模块、市场数据和无关 FRP 不属于授权修改范围；STCalendar 预存修改完整保留。本 D 不扩大初始范围，也不再次请求 Owner 审批。

当前 rb 与 rb/m Wall 原件、所有错误和读回调和证据保留；行为／绑定改变后的 U／X 有效性与后续重跑依 L0 实际影响规则处理，不能用旧结果证明新版本通过。完整请求范围的正式 X 仍未完成，G 尚未委派。

回交原 manager，保持本 D／原工作身份与原 longrun-professional-return/v2。controller 负责真实权限、工作区／共享生产互斥和物理派达；manager 不代跑 Feature，不代作专业责任定位，不创建 Worker 或 W，不迁用 Attack 的版本或成果。
