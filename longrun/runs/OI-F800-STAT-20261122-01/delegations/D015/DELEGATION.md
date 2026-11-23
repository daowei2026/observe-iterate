# D015｜原G补充：当前F800结果上的高置信发现pass

Run `OI-F800-STAT-20261122-01`，issuer_call=C0033；原manager `codex:OI-F800-STAT-20261122-01:manager` → 本Run原独立executor `codex:OI-F800-STAT-20261122-01:executor:E1` → 回原manager。一份D只对应原feature-global-behavior-profiling一项Skill，不拆内部工单，CODEX_NATIVE_DIRECT、workers=[]，无W/Worker。

**当前完整专业控制commit：`b8c2b513f0b08be6a1fa6782b71bf74a07faff0d`。** 采用起点C0033，旧专业控制`87b951bbd15078a2d6353bdd24afe0d8f19c845c`和旧D/报告保留历史；原线程不重建。物理controller Skill仍为cgpterm@fc966bcf5441701182339c992865504692f3a466，与专业控制分开。准确采用记录 `daowei2026/observe-iterate@4bf46f3fbe402915e3272e49a71dc94eac787c15:longrun/runs/OI-F800-STAT-20261122-01/PROFESSIONAL_CONTROL_ADOPTION.json`。

执行前须亲读该commit的Control L0/L1/L2、`daowei2026/observe-iterate@b8c2b513f0b08be6a1fa6782b71bf74a07faff0d:skills/reasonableness-analysis/feature-global-behavior-profiling/SKILL.md` 及同版WORKFLOW/IO_SPEC、STATISTICS_DRIVEN_PRACTICE、本次 `daowei2026/observe-iterate@b8c2b513f0b08be6a1fa6782b71bf74a07faff0d:task-inputs/wall-f-parallel-closure-20261122/F_CURRENT_RUN_CONTINUATION.md` 与KNOWN_FINDINGS；profile/manager指南/协议和上述原件均列于JSON准确输入。专业方法、内部G1—G8与完成条件直接依原文，不附加manager自写方法、阈值、根因、上限或验收表。

## 当前任务与有效输入

最新Owner原文 `daowei2026/observe-iterate@4bf46f3fbe402915e3272e49a71dc94eac787c15:longrun/runs/OI-F800-STAT-20261122-01/owner-decisions/CONTINUE-20261123/OWNER_CONTINUE.original.txt` 不接受F800-REL-001，要求原Run/原manager/原E1继续。本D只在当前D008结果上补做“覆盖面与高置信度并重”的finding discovery pass，不重做有效U、三年X、31表独立读回或既有D008 G，也不重复S1/S2或原GF001/002诊断（除非新证据直接推翻其闭环）。

准确当前输入为D008 CurrentFeatureUnderstandingPackage、FeatureRunResultBinding、GlobalBehaviorProfile、StatisticDefinitions、StratificationPlan、StatisticsInputReadiness、31表读回/字段及结果清单；均以JSON whole-file exact refs传递。FRP `39f02ec4548e68ba8dbd30061afc870546000994`、TIS `2f460d663d821cf2ba25555eda13e78b697d0767`，配置SHA-256 `b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3`；rb/hc/i、5m、2021—2023、night_end_at_2300/TA_updto20240229_DBA/steel、800/600/CalendarUTITick/2Delta1200及原PNV保持。当前结果不是旧ac/be57或默认F6。

本次ReviewTarget由Owner接续原文及接续输入§2—4直接给定：在当前正式结果上完成适用业务面的高置信发现，记录未升级观察和未覆盖边界，先形成结果绑定队列快照再逐个D；不在首个候选处停止，也不机械穷尽。执行者可提出参考类别以外候选，不把数量/极值直接当最终判错；每个升级候选说明为何不是普通波动、与什么语义/合同/数量关系冲突、证据支持边界及D仍需确认什么。

Owner候选已登记于本C同批OWNER_CANDIDATE_REGISTRATION：`F-LIFE-PEAK-CONCURRENCY`，`candidate_origin=OWNER_RAISED`、`status=CANDIDATE`、`must_assess_before_release=true`、current_confidence=OWNER_CONCERN。原报告峰值责任内Life=36是Owner关注，不预设责任内=active、历史残留/800根因、36为确认缺陷或三品种的固定数量上限。其准确权威来源为 `daowei2026/observe-iterate@4bf46f3fbe402915e3272e49a71dc94eac787c15:longrun/runs/OI-F800-STAT-20261122-01/owner-decisions/CONTINUE-20261123/OWNER_CONTINUE.original.txt` 和接续输入§4—5；G形成队列后该候选按原D先LogicLocalization，Owner列明的D要求由原D执行，不在本G提前代做或省略。

## 权限、回交与范围

只传最新 `daowei2026/observe-iterate@3dc11a9dbf39e181b3c6a3051419a90e46b92aac:longrun/runs/OI-F800-STAT-20261122-01/RUN_BINDING.json` 的run_result_statistics_analysis_write与run_record_write；工作区 `/dwdhome/fy/BASE_E6_2_copy`，分析写本Run独立D015产物，正式记录写本Run授权根。历史MP001/MP002批准链不新增权限；没有formal_feature_run、正式行为/参数/常量/期限/数据处理/输出合同改变或代码采用授权。后续若确需正式改变，先定位/Proposal/影响/验证回Owner确认；绑定/口径问题按Owner和新Workflow走B，不机械重跑三年F。

当前G输出由原Skill/IO和Owner接续输入给定：FindingDiscoverySummary、当前结果绑定CandidateFindingQueue快照、ObservationsNotPromoted以及必要原生剖面/适配包/Gate。快照不禁止后来新增证据/候选。原E1的原生报告必须明确实际采用完整commit `b8c2b513f0b08be6a1fa6782b71bf74a07faff0d` 及准确来源读取；V2 Return字段不增改，通过result_ref指向该报告。manager消费真实回交后才按Q逐个签D，先LogicLocalization，不预签后继或Release。

最新Campaign原文 `daowei2026/observe-iterate@4bf46f3fbe402915e3272e49a71dc94eac787c15:longrun/runs/OI-F800-STAT-20261122-01/owner-decisions/CONTINUE-20261123/CAMPAIGN_ROUTE.original.txt` 明确F独立继续、不再等待WALL/F联合Barrier，覆盖接续输入末尾保留的旧Barrier文字；不推断WALL已通过合理性，也不在本F Run管理Absorb/WALL执行。F→Q→V顺序不变，当前不签F Gate/Package或启动Q/V；未来Q必须消费最终准确F800 ReleasePackage，不能旧make_features重得F6冒充。

controller核原E1真实线程/sol/max/cwd、权限/单写者及状态后物理派达，D发布不是送达/开工回执。manager不代统计、诊断或改Feature，不新建线程、不向其他聊天发消息、不设timer。
