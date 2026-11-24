# TASK_PROGRESS｜AttackSegment 机器状态与恢复

## A. Run、采用来源与角色

- run_id：`OI-EAW-P1-ATTACK-STAT-20261124-01`；work_id：`OI-EAW-P1-ATTACK-STAT`；business_case_id：`EAW-P1-ATTACKSEGMENT`
- 专业控制统一 commit：`9877826236e0995e7255e6cbfedc2d1b89dea6da`
- L0：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:control/01_L0_统计驱动的单特征闭环.md`；manager 指南：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:longrun/professional/PRO_MANAGER_GUIDE.md`
- 协议／profile：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:longrun/contracts/LONGRUN_PROTOCOL_V2.md`；`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:longrun/CODEX_NATIVE_EXECUTION_PROFILE.md`
- 唯一业务输入／ReviewTarget：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:task-inputs/eaw-p1-attack-stat-20261124/ATTACK_RUN_INPUT.md`
- Owner：`daowei2026/observe-iterate@b912f85368fed916c45603c81aa8ef304bc146b6:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/OWNER_START.md`；Binding：`daowei2026/observe-iterate@723d65a2ca4fbcf691e9a82eb153a21faae18390:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/RUN_BINDING.json`；Resource：`daowei2026/observe-iterate@723d65a2ca4fbcf691e9a82eb153a21faae18390:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/RUN_RESOURCE_BINDING.json`
- execution_profile：`CODEX_NATIVE_DIRECT`；post_start_owner_policy：`AUTONOMOUS`；`workers=[]`
- controller 版本仍为 `815c505c1cc3d965aaafa831d23c4c88368cb70a`。
- 原 manager：`codex:OI-EAW-P1-ATTACK-STAT-20261124-01:manager`；原 E1：`codex:OI-EAW-P1-ATTACK-STAT-20261124-01:executor:E1`；继续复用，物理映射由 controller 持有。
- workspace：`/dwdhome/fy/BASE_E6_2_copy`；TIS：`/dwdhome/fy/BASE_E6_2_copy/mquant/tis`。
- 当前 INVOCATION：`daowei2026/observe-iterate@6c0e83031bf4bab75db33599858ed3dd959782f2:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0008/INVOCATION.json`；FULL_ASSIGNMENT：`daowei2026/observe-iterate@22290b9ea6332fd9e3cac357898a39a2e580fe62:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0008/FULL_ASSIGNMENT.md`。
- controller 已独立核 C0007 的原 user payload、invocation/token、实际 sol/max、原 D002 回交关系、协议与 Git 原件，依据为上述准确 FULL_ASSIGNMENT；本 manager 不合成物理 receipt。
- 当前 snapshot：C0008 协调投影 current；X 部分有效、m 剩余工程资源等待。业务入口：[BUSINESS_PROGRESS.md](BUSINESS_PROGRESS.md)。

## B. 当前正式实例与有效 X 范围

| 项目 | 当前事实 | 准确来源 |
|---|---|---|
| 代码／分支 | TIS `179016111ed0394f92025313e46bd13534932a74`；`codex/oi-eaw-p1-attack-fix-20261124-01`；tracked 产品代码未改 | 当前任务和原生绑定 |
| constructor／参数 | `mquant.tis.hf.prel0.attack_flow_assembler.AttackFlowAssembler()`／`attack-default`；业务参数未改 | 实际 ppdict/ppid、code fingerprints、receipts 逐对象保存在当前绑定；不以 U 构造身份代替实际运行绑定 |
| 正式范围 | `TA_updto20240229_DBA`；`rb,m`；`2021-01-01..2021-12-31`；`night_end_at_2300`，未缩小目标 | 唯一输入／当前绑定 |
| 当前原生绑定 | `INCOMPLETE_WAITING_SHARED_LOCK`；`formal_complete=false`、`eligible_for_G=false` | `daowei2026/observe-iterate@0837509a7200dcffcfced4113cab22ec575bdcce:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D002/C0007/FeatureRunResultBinding.json` |
| 原生 U | PARTIAL，未重做／未自动关闭具名未知 | `daowei2026/observe-iterate@758c77a566672a4514cbff6d3f26236769d17b59:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D001/FeatureUnderstandingPackage.json`；`daowei2026/observe-iterate@758c77a566672a4514cbff6d3f26236769d17b59:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D001/REMAINING_SCOPE.md` |
| rb Wall／tactical／structural | 本 Run 当前版本均已生产并完整读回验证 | 当前绑定 per_feature_results／receipts |
| rb Attack 三产品 | 已生产，R01 只读完整重算及按列名全量读回 35 表有效，artifact manifest 与 receipt／metadata 不变 | 当前绑定 rb attack 及 readback_reconciliation |
| m Wall | 当前版本 receipt 与 5 表读回已有；补正运行上下文后的只读复核在 A04 未执行 | 当前绑定 m wall、A04 和原报告 |
| m tactical／structural／Attack | `NOT_RUN_AFTER_TRADE_SCOPE_CORRECTION_WAITING_SHARED_LOCK`；补正后仍未执行，新目标不存在 | 当前绑定与原恢复原件 |
| 父 Run | `incomplete / IN_PROGRESS` | rb 局部有效不等于完整 rb/m X；当前无 G／诊断／Release |

当前绑定的累计 `feature_execution_started=true`、`attack_feature_execution_started=true` 对应此前已发生的生产；A04 单项仍为 `feature_execution_started=false`。两者作用域分别保留。

C0007 原报告：`daowei2026/observe-iterate@0837509a7200dcffcfced4113cab22ec575bdcce:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0007/EXECUTOR_REPORT.md`；有效 Return：`daowei2026/observe-iterate@ab0ce5541a579ebaf2ae63bec698752576c50ae0:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0007/PRO_RETURN.json`。

## C. 原 D002 与真实 C／尝试历史

原 D002：`daowei2026/observe-iterate@c9742986ed6fbb7bc2d55bd87cab54de42c7539f:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/delegations/D002/DELEGATION.json`，`issuer_call_id=C0004`；签发 Return：`daowei2026/observe-iterate@74a46582f44b16b1f7f0890c30314684d211ef3f:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0004/PRO_RETURN.json`。C0006／C0007 是同一未完成工作的续接，本 C 不更换签发者，不签 D003。

| 调用／记录 | 已发生事实与效力 | 保留来源 |
|---|---|---|
| C0001／D001 | 原 manager 签发 U，父 Run 未完成 | `daowei2026/observe-iterate@e20128bff682c58bc2a66a6c5ed176f78634c476:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/delegations/D001/DELEGATION.json` |
| C0002／C0003 | U 产物 PARTIAL；C0002 Return 状态冲突保留，C0003 同 E1 定向补正有效回交，不重做 U | 旧 Return：`daowei2026/observe-iterate@5289eab7a18b434d8316f7bc87e7685d81df3370:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0002/PRO_RETURN.json`；补正：`daowei2026/observe-iterate@72f33ce96e78653cfd94ae9fba0579fe50548848:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0003/PRO_RETURN.json` |
| C0004／D002 | manager 消费有效 U，签发原 L0 X 工程工作 | 上述原 D002 及签发 Return |
| C0005／A01 | 未得锁，未执行 Feature／创建正式 store；原件逐字节保留 | `daowei2026/observe-iterate@647871627d9f5f591a23d54c4a2a842b39f05346:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D002/FeatureRunResultBinding.json` |
| C0006 | manager 消费 A01 资源等待，沿原 D002／E1 续接，无新 D | Return：`daowei2026/observe-iterate@0d2137442b76f872f2b38eb4e3cf3d16d98303f2:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0006/PRO_RETURN.json`；当时双进度：`daowei2026/observe-iterate@7cc81c24b94a1adc021e5ac6fc4e92e3e6ab091f:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/business_control/TASK_PROGRESS.md` |
| C0007／A02 | 取得并释放原锁，任何 Feature 前由运行器配置断言终止，无 store；框架类名匹配作工程纠正，旧脚本／错误保留 | 当前完整绑定 attempt_history 与原报告 |
| C0007／A03 | 实际取得并释放原锁；部分生产成功；rb 读回列顺序断言和 m F4 交易集异常原样保留 | 当前绑定 original_production_feature_results／recorded_errors |
| C0007／R01 | 取得并释放原锁，只读完整重算与按列名核对 rb 35 表；禁止 dump／数据库／缓存写入，既有 artifact／receipt 元数据不变 | 当前绑定 readback_reconciliation |
| C0007／A04 | 600 秒窗口未获原锁，runner 已结束，未持锁／未执行补正后的 m 工程 | 当前绑定 continuation_execution／post_execution_check |
| C0008 | 原 manager 消费 C0007 的有效部分 X 与真实剩余，保留原 D002／E1 | [本 C 报告](../calls/C0008/MANAGER_REPORT.md)，报告及双进度先发布回读，再签发原 v2 IN_PROGRESS Return |

A01/A02/A03/R01/A04 的原记录、错误、journal、结果和参数实例均保留；本 C 不改写原产物。完整历史恢复入口仍可追溯上述前次进度快照。本 C 消费 executor Return，`accepted_worker_refs=[]`，无 W 或 Worker Return。

## D. 工程纠正与原未决范围

m 的 A03 两组 F4 异常，原 E1 在 X 工程内只读核实为 runner 沿用 `OptContext` 默认 `black` 交易集，实际不含正式输入已有的 m。原生 `m.csv` 仅映射 m，索引及交易单位可读，补正上下文与 fresh 写面前检已完成。Feature 业务参数、市场数据、正式品种／时间／SOF／日历和产品源码均未变。运行上下文补正不是专业 Diagnosis、业务 finding 或上游代码修改许可。

A04 未获锁，未执行计划中的 m Wall 只读复核或补正后的 F4／Attack；前检成功不能写作这些工程已完成。m Wall 的已有读回事实与其补正上下文后的待复核分别保留。

原 U 的 UQ01–UQ07 与 NOT_EXPOSED 按 `daowei2026/observe-iterate@758c77a566672a4514cbff6d3f26236769d17b59:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D001/FeatureUnderstandingPackage.json`、`daowei2026/observe-iterate@758c77a566672a4514cbff6d3f26236769d17b59:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D001/REMAINING_SCOPE.md` 保留：部分运行事实由 C0007 绑定补充，原 U 状态未自动改为 COMPLETE。分支可达性、末尾状态、参考合同／职责差异、信息最早可得时间等没有由本 C 新作判断。

| 节点 | 当前状态 | 原合同后继资格 |
|---|---|---|
| U／D001 | PARTIAL，已消费，原未知保留 | 依原 Skill 和有效运行事实处理相关更新 |
| X／D002 | rb 部分有效，m 剩余工程等待 | 使用 C0007 最新 continuation 续接原 D002 |
| G | 未执行，`eligible_for_G=false` | 原 L0 要求当前完整正式结果，rb 局部成果不能替代 |
| finding／诊断／修正 | 尚无正式 finding、DiagnosisReport 或产品修复 | U 来源差异和运行器纠正未升级为业务结论 |
| Release | 未形成 FeatureReleaseGate／UpstreamReleasePackage | 沿原 L0 完成条件，无新增 Gate |

## E. 当前资源事实与具名恢复路径

仍为同一生产锁 `/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/FORMAL_PRODUCTION.lock`，原记录 inode=`15061041`。A03 与 R01 实际持锁后释放；A04 的 `lock_acquired=false / lock_released=false` 表示其从未持锁。全部本 Run runner 已结束，没有本 Run 遗留占锁。controller 最近核同锁由另一获准生产者持有，依据为 C0008 FULL_ASSIGNMENT；本 manager 不自行操作或复测生产锁。C0006 当时的 Build 持锁状态保留为历史，不当作本次持有者身份。

当前 continuation：`daowei2026/observe-iterate@0837509a7200dcffcfced4113cab22ec575bdcce:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D002/C0007/REMAINING_SCOPE.md`，替代当前路由中旧的 C0005 恢复指针，旧原件仍保留。

下一合法动作由 `codex:OI-EAW-P1-ATTACK-STAT-20261124-01:controller` 核原锁自然释放、A04 终态／未持锁／未执行 m 和新目标状态后，以新的真实 C 在原 E1／copy 工作区续接原 D002 剩余 m 工程；原 E1 使用新 attempt，不能重写 A04，不预占后继编号。完全同一性已核的本 Run 成果保留复用，原恢复范围只针对未完成工程。探测不是预约；持锁条件未变时不重复强启动新的 600 秒生产尝试。

锁、源工作区、物理权限和实际派达由 controller 独立核实；不强停持有者、不改锁或另造锁、不覆盖旧 Run／旧尝试。当前只影响具体生产写面，独立工作继续。Build 的专业版本、业务结果、角色和完成状态均不混用。

Owner／Binding 和禁止面持续有效：manager 仅协调及发布本 Run 记录，不运行 X/G 或改工程代码；E1 仍受原 D002／Owner 的操作写面约束，不越权改 Wall、F4、其它上游、公共模块或市场数据。不新增 Owner、专业 Skill、Q/Gate、Worker 或其它 Feature Run。

## F. 本 C 发布和双视图同步

BUSINESS_PROGRESS 已同步 rb 有效结果、m Wall 读回、运行上下文遗漏与纠正前检、A04 未执行以及完整 X/G 未满足。当前父 Run IN_PROGRESS。

本 C 报告和双进度先发布并准确回读，再发布 `calls/C0008/PRO_RETURN.json`。原 v2 Return 保持 `role=manager / professional_state=IN_PROGRESS`、`return_to=null`，`issued_delegation_refs=[]`、`issued_order_refs=[]`、`accepted_worker_refs=[]`、`owner_request_ref=null`。remaining_scope 引用已发布进度，continuation 使用上述已存在 C0007 原恢复原件；实际发行引用在回读后补记，避免循环。

快照日期：2026-11-24，C0008；记录分支仅 `codex/oi-eaw-p1-attack-stat-20261124-01`；已核 Personal 连接。
