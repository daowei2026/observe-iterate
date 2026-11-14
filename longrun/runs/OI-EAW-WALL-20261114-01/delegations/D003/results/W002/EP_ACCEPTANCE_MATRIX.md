# W002 八项EP工程事实矩阵

UTC：2026-11-14T18:50:57.319315+00:00。Worker仅列工程事实；最终专业接受由原E1负责。outcome STOP，不因静态台账子集而把Phase0硬停止改成EXECUTED。

| EP | 状态 | 直接证据 | 未满足部分 | 阻断影响 | 最小解除条件 |
|---|---|---|---|---|---|
| EP-WALL-SHARED-01 | NOT_ATTEMPTED | exact WallLifecycle.hs状态字段已核；SOURCE_BASELINE_REPORT | 没有snapshot accessor/patch/typecheck | 阻断依赖真实A的EP；不阻断本次STOP交付 | Phase0先合格，再按只读字段投影实现并有限验证 |
| EP-WALL-SHARED-02 | NOT_ATTEMPTED | D002工程合同逐字输入；WRITE_SURFACE_PLAN | 没有DTO/JSON schema/canonical roundtrip | 阻断structured evidence/serialization | Phase0先合格，建设one-record-per-firing schema并测canonical bytes |
| EP-WALL-SHARED-03 | UNSATISFIED | D003_BINDING、DRY_DEPENDENCY_PREFLIGHT、原始bwrap stderr/strace | offline closure和四项cap预测未知；零外写unknown | Phase0硬Gate阻断Phase1/2全部构造/验证 | 冻结兼容离线闭包、可信预算和实际可验证写入隔离/监测 |
| EP-SCENARIO-01 | NOT_ATTEMPTED | frp.cabal exact blob；现有component声明 | dedicated target/main未创建或编译 | 阻断后续actual scenario能力，不准在本W执行 | Phase0合格后在staged source建设、至多compile-only |
| EP-SCENARIO-02 | NOT_ATTEMPTED | KNOWN_CONTRACT_CONFLICTS；exact error源码 | 没有structured exact-error adapter/assertion测试 | 依赖01/SHARED-02 | 先合格并建设typed constructor/payload serialization；不跑场景 |
| EP-SCENARIO-03 | NOT_ATTEMPTED | exact applyWallOccurrenceBatch/stepWall/partitionIngressBatch静态路径 | 没有transaction DTO及synthetic serialization验证 | 依赖真实snapshot和structured schema | 先合格；formal rejected post=pre且O/C空，debug不得冒充提交 |
| EP-SCENARIO-04 | PARTIAL | KNOWN_CONTRACT_CONFLICTS.md；exact source/test与行号、有限rg输出 | 有静态台账；dedicated harness/manifest未构造，没有actual结果 | 不独立解除Phase0或其他EP | 保留冲突并在后续合格staged manifest显式引用，由E1处理专业争议 |
| EP-SCENARIO-05 | NOT_ATTEMPTED | FIXTURE_SCHEMA_AND_PROVENANCE.md；D002输入合同 | 完整fixture/schema/hash和9/18/22静态验证均未产生 | 阻断后续fixture准备，不阻断STOP归档 | Phase0先合格，再物化并仅静态验证完整controlled输入 |
