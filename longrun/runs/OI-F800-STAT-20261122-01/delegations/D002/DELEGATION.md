# D002｜F800 正式 X → G

- run_id：`OI-F800-STAT-20261122-01`；work_id / parent_task_id：`OI-F800-STAT-20261122`；work_item_id：`F800-XG-001`；stage：已采用 L0 的 X→G；issuer_call_id：`C0004`。
- issuer / return_to：`codex:OI-F800-STAT-20261122-01:manager`；recipient：`codex:OI-F800-STAT-20261122-01:executor:E1`。
- `CODEX_NATIVE_DIRECT`；workers=[]。接收者为本 Run 已存在的原 E1，由 controller 复用；本 manager 不新建线程或直接发送。本 D 签发时尚未派发。

## 任务与唯一专业 Skill

Owner 最新继续指令逐字原件位于 `daowei2026/observe-iterate@81505c8f0d0216be94b68c4a3ae7c10a61c97da0:longrun/runs/OI-F800-STAT-20261122-01/calls/C0004/FULL_ASSIGNMENT.md`。按该原文第2、4项及 `daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:control-v0.3/01_L0_统计驱动的单特征闭环.md` 的 §3→§4，直接完成锁定正式 X：查验可合法复用的准确结果，不满足则运行锁定全范围；取得合格 FeatureRunResultBinding 后紧随进入 G，不再以重复完整理解作为前置。

X 是原 Workflow 的实际执行动作，不新增 Skill。本 D 唯一专业 Skill 为 `daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/reasonableness-analysis/feature-global-behavior-profiling/SKILL.md`，适用补充 `daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/reasonableness-analysis/STATISTICS_DRIVEN_PRACTICE.md`；必要 WORKFLOW/IO_SPEC 依其原文（准确引用列于 input_refs）。G 的原生输入和完成条件保持原合同，签发本 D 不表示 X 结果已存在或 G 已开始。

本 D 只绑定上述已发布方法与任务、当前输入、回交和 Owner 授权；各阶段方法、产物与完成状态依已采用原件，不另写专业方法或 Gate。

## 当前有效输入

- BusinessTaskInput：`daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:task-inputs/wall-f-parallel-closure-20261122/F_BASE_RUN_INPUT.md`；初始 Owner GO：`daowei2026/observe-iterate@43a13e14129984d6f3a142c6eb64397a43c3ca79:longrun/runs/OI-F800-STAT-20261122-01/OWNER_START.md`；最新继续指令：上引 C0004 FULL_ASSIGNMENT 中的 Owner 原文。
- 已消费回交：`daowei2026/observe-iterate@c81c64d64aaa7d22a6d95459e15345ee3e028ced:longrun/runs/OI-F800-STAT-20261122-01/calls/C0003/PRO_RETURN.json`，对应原 D001 的最小核对委派已交付；专业报告：`daowei2026/observe-iterate@78b684ba6956f4c33a03b9167e846e3b741316a5:longrun/runs/OI-F800-STAT-20261122-01/calls/C0002/EXECUTOR_REPORT.md`。
- 原生理解：`daowei2026/observe-iterate@78b684ba6956f4c33a03b9167e846e3b741316a5:longrun/runs/OI-F800-STAT-20261122-01/professional/D001/FeatureUnderstandingPackage.json`，`completion_status=PARTIAL`；本轮最小当前理解已足以进入 X，六项具名缺口仍按该包交 X/G，不升级为整项完成或重做全部 U。
- 完整实例：`daowei2026/observe-iterate@78b684ba6956f4c33a03b9167e846e3b741316a5:longrun/runs/OI-F800-STAT-20261122-01/professional/D001/configuration.json`；构造与候选结果身份：`daowei2026/observe-iterate@78b684ba6956f4c33a03b9167e846e3b741316a5:longrun/runs/OI-F800-STAT-20261122-01/professional/D001/INSTANCE_INSPECTION.json`；其余 delta、baseline 和公开表合同列于 input_refs。

Feature=`CommonPriceTurnGroupCandidatesFrp`，只取 make_features 返回的 f。FRP=`ac1927518ad6105f15ffbe37fea45e4be91ba574`；TIS=`2f460d663d821cf2ba25555eda13e78b697d0767`；正式参数沿用已发布完整配置，唯一已批准 override 为 observation_multiple=800，delta=600、CalendarUTITick，method.revision=1 保持基线。配置 SHA-256=`b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3`。

正式范围仍为 rb/hc/i、5m、2021-01-01 至 2023-12-31、night_end_at_2300、TA_updto20240229_DBA、steel；工作区 `/dwdhome/fy/BASE_E6_2_copy`，不运行 Q/V 专业任务。最新 Owner 第4项及 BusinessTaskInput §3—5 给出的配置回读、实际加载、2Δ、复用与正式运行条件均沿用原文。

D001 只形成构造/源码证据，未运行引擎、未独立读回正式表。当前准确配置的 fields.json 在 D001 核对时不存在；已查历史 F800 另改 method.revision，不能直接作本配置结果。实际是否另有合格复用结果及正式结果绑定由既定 X 形成，本 D 不预填未来结果引用。

## Owner 权限与回交

Binding=`daowei2026/observe-iterate@2665f0cbabff0439fe8d361c2ad545bf922e1792:longrun/runs/OI-F800-STAT-20261122-01/RUN_BINDING.json`；资源绑定=`daowei2026/observe-iterate@2665f0cbabff0439fe8d361c2ad545bf922e1792:longrun/runs/OI-F800-STAT-20261122-01/RUN_RESOURCE_BINDING.json`。permitted_operations 与 allowed_writes 仅取原 Binding grants：正式 Feature 运行、运行结果/统计/分析写入及本 Run 记录写入；执行工作继续受原 profile/V2 的实际写面授权和单写者核验约束。INSTANCE_INSPECTION 中候选 full_dir 是定位事实，未被本 D 追加为新 grant。

本次采用已批准的锁定代码与800实例；新的正式 Feature 行为变化继续按原 Owner 的 ModificationProposal→确认链处理。

按 X 原 Workflow 与 G 原生合同回交真实结果、实际范围、未完成项和专业状态；V2 executor PRO_RETURN 回 `codex:OI-F800-STAT-20261122-01:manager`，绑定本 D 发布后的 exact ref。无 Worker，issued_order_refs=[]、accepted_worker_refs=[]。最新 Owner 第6项要求的七项进度依真实证据分别报告；本 D 不把派发、进程启动或发现目录当作 X/G 完成。
