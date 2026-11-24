# D001｜首轮 U：理解 BuildAssembler

本 D 对应一项原 Skill 工作；专业方法、内部流程、原生产物、完成条件和专业边界均以锁定 Skill 及其引用为准。

- run_id：`OI-EAW-P1-BUILD-STAT-20261124-01`
- work_id：`OI-EAW-P1-BUILD-STAT`；business_case_id：`EAW-P1-BUILD`
- work_item_id：`EAW-P1-BUILD-U-R01`；stage_instance_id：`U-R01`
- delegation_id：`D001`；issuer_call_id：`C0001`
- issuer / return_to：`codex:OI-EAW-P1-BUILD-STAT-20261124-01:manager`
- recipient：`codex:OI-EAW-P1-BUILD-STAT-20261124-01:executor:E1`
- 当前专业控制 commit：`391adcd18bd2da82c13c01710980f41e01c7de25`；执行 profile：`CODEX_NATIVE_DIRECT`；`workers=[]`
- 当前正式业务输入／CurrentReviewTarget：`daowei2026/observe-iterate@391adcd18bd2da82c13c01710980f41e01c7de25:task-inputs/eaw-p1-build-stat-20261124/BUILD_RUN_INPUT.md`
- 本次 Skill：`daowei2026/observe-iterate@391adcd18bd2da82c13c01710980f41e01c7de25:skills/feature-understanding/SKILL.md`
- 适用补充：`daowei2026/observe-iterate@391adcd18bd2da82c13c01710980f41e01c7de25:skills/feature-understanding/BUSINESS_OBJECT_QUALIFICATION_GUIDE.md`
- Skill 所引用的 WORKFLOW.md、IO_SPEC.md 及必要来源按同一锁定版本读取；准确引用也列于 DELEGATION.json。

本项工作是既定 L0 首轮 U。当前目标 Feature、源码基线、constructor、build-default 实例、正式数据范围和原始业务来源均沿用正式输入；完整参数和实际实现事实由本 Skill 据实核定。本 D 不包含后续 X、G、偏差诊断或实现修改工作。机读操作名来自原 GO，实际使用限于本项 Skill 工作与授权写面；未列 TIS 修改分支为本 D 写面。

已有 U 包、正式 X/G、finding 或 Release：尚无。本 Run 的旧 Absorb 资源释放、工作区核验和注册事实见 DELEGATION.json 的准确输入引用；不继承旧 Run 的专业完成事实。当前 exact Wall artifact/receipt/state trace 与 Build 上游引用尚未核验，STCalendar 预存修改及其加载影响仍为未确认事实，见原派达与工作区核验原件。

原生产物为 `FeatureUnderstandingPackage`，状态及未完成范围依原 Skill 的 IO_SPEC；不在本 D 增设专业验收。原 Owner GO 与 RUN_BINDING 已列入准确输入，工程权限与物理执行前检由 controller 按原协议核验。

交回上述原 manager，保持本 D／工作项身份。使用原 `longrun-professional-return/v2` 并引用实际发布的原生产物；后续物理 C 及 E1 创建、模型和工作区核验由 controller 完成。
