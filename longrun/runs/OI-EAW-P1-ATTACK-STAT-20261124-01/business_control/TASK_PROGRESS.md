# TASK_PROGRESS｜AttackSegment 机器状态与恢复

## A. Run、来源与角色

- run_id：`OI-EAW-P1-ATTACK-STAT-20261124-01`；work_id：`OI-EAW-P1-ATTACK-STAT`；business_case_id：`EAW-P1-ATTACKSEGMENT`
- Owner GO：`daowei2026/observe-iterate@b912f85368fed916c45603c81aa8ef304bc146b6:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/OWNER_START.md`
- 唯一业务输入／CurrentReviewTarget：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:task-inputs/eaw-p1-attack-stat-20261124/ATTACK_RUN_INPUT.md`
- 专业控制统一 commit：`9877826236e0995e7255e6cbfedc2d1b89dea6da`
- Workflow：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:control/01_L0_统计驱动的单特征闭环.md`；manager 指南：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:longrun/professional/PRO_MANAGER_GUIDE.md`
- U Skill／补充：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:skills/feature-understanding/SKILL.md`；`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:skills/feature-understanding/BUSINESS_OBJECT_QUALIFICATION_GUIDE.md`
- U IO：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:skills/feature-understanding/IO_SPEC.md`，原生 PARTIAL 允许具名下游在明确范围内继续。
- 当前后继：原 D002 的 X 资源等待；原锁自然释放且原 C0005 效果核实后，由原 E1 续接同一未完成工作。
- Binding：`daowei2026/observe-iterate@723d65a2ca4fbcf691e9a82eb153a21faae18390:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/RUN_BINDING.json`；Resource Binding：`daowei2026/observe-iterate@723d65a2ca4fbcf691e9a82eb153a21faae18390:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/RUN_RESOURCE_BINDING.json`
- execution_profile：`CODEX_NATIVE_DIRECT`；post_start_owner_policy：`AUTONOMOUS`；`workers=[]`
- controller 版本：`815c505c1cc3d965aaafa831d23c4c88368cb70a`
- manager：`codex:OI-EAW-P1-ATTACK-STAT-20261124-01:manager`，原线程 `01a20c65-8d30-7ee3-ad1c-8086eac5f31a`
- executor：本 Run 原 `codex:OI-EAW-P1-ATTACK-STAT-20261124-01:executor:E1`，后继复用；物理映射由 controller 持有，不新建 Worker。
- 工作区：`/dwdhome/fy/BASE_E6_2_copy`；TIS：`/dwdhome/fy/BASE_E6_2_copy/mquant/tis`
- 当前 C0006 原件：`daowei2026/observe-iterate@a980fee7b4a97d6df2ea47165fbdf53674ee0ada:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0006/INVOCATION.json`；`daowei2026/observe-iterate@0b09d264d42d64e643d970c45cee40c7b5280317:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0006/FULL_ASSIGNMENT.md`
- snapshot：本 C 协调投影 current；D002 处于资源等待，当前未建立有效正式结果。业务入口：[BUSINESS_PROGRESS.md](BUSINESS_PROGRESS.md)。

## B. 当前正式实例与有效成果

| 项目 | 当前真实状态／版本 | 依据 |
|---|---|---|
| 代码／分支 | TIS `179016111ed0394f92025313e46bd13534932a74`；`codex/oi-eaw-p1-attack-fix-20261124-01` | 原 U 报告和当前完整任务；本 C 未操作 TIS |
| constructor／参数 | `mquant.tis.hf.prel0.attack_flow_assembler.AttackFlowAssembler()`；`attack-default` | 原 U 实际构造证据 |
| 构造 ppid | `AttackFlowAssembler_700681a3da4b7aedeb84a6066b6ca4af733d4b14` | 已核构造身份；不等于正式运行有效参数／receipt |
| 数据／日历 | `TA_updto20240229_DBA`；`rb,m`；`2021-01-01..2021-12-31`；`night_end_at_2300` | 唯一业务输入；实际 source_scope/exact axis 待 X |
| 正式产品 | `attack_segment / attack_formation_evidence / wall_relation_barrier` | 当前三产品布局已由 U 说明，未取得完整正式结果 |
| U 原生包 | PARTIAL，已通过有效 C0003 回交在 C0004 消费 | `daowei2026/observe-iterate@758c77a566672a4514cbff6d3f26236769d17b59:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D001/FeatureUnderstandingPackage.json` |
| U 阅读版／未完成范围 | 仍保留 UQ01–UQ07 与结果字段缺口 | `daowei2026/observe-iterate@758c77a566672a4514cbff6d3f26236769d17b59:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D001/FeatureUnderstandingPackage.md`；`daowei2026/observe-iterate@758c77a566672a4514cbff6d3f26236769d17b59:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D001/REMAINING_SCOPE.md` |
| X A01 记录 | `NOT_ESTABLISHED_WAITING_SHARED_LOCK`；`formal_complete=false`、`eligible_for_G=false` | `daowei2026/observe-iterate@647871627d9f5f591a23d54c4a2a842b39f05346:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D002/FeatureRunResultBinding.json`，binding_id=`OI-EAW-P1-ATTACK-STAT-20261124-01-D002-X-R01-A01` |
| 实际执行／结果 | `feature_execution_started=false`，实际 receipts／per_feature_results 均为空，正式 store 不存在 | 此为未运行事实，不代表业务数量为零 |
| X 原恢复入口 | 原 D002／原 E1 保留 | `daowei2026/observe-iterate@647871627d9f5f591a23d54c4a2a842b39f05346:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D002/REMAINING_SCOPE.md` |
| 父 Run | `incomplete / IN_PROGRESS`，X 资源等待 | 无有效完整 X，不具备 G 资格；无诊断或 Release |

## C. 真实 C／D／Return 历史与消费

| 调用／委派 | 已发生的事实 | 准确原件与当前效力 |
|---|---|---|
| C0001／D001 | manager 签发首轮 U | D001：`daowei2026/observe-iterate@e20128bff682c58bc2a66a6c5ed176f78634c476:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/delegations/D001/DELEGATION.json`；manager Return：`daowei2026/observe-iterate@9b32c8e9dbc4bd2b1ff87a9b78bd44fb8a9e5211:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0001/PRO_RETURN.json` |
| C0002／D001 | 原 E1 实际执行 U，形成 PARTIAL 产物，未执行 Feature/X/G、未修改产品代码 | 报告：`daowei2026/observe-iterate@758c77a566672a4514cbff6d3f26236769d17b59:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0002/EXECUTOR_REPORT.md`；产物 commit `758c77a566672a4514cbff6d3f26236769d17b59` |
| C0002 旧 Return | `REPORTED_COMPLETE` 与非空 remaining／continuation 冲突；controller 未将其消费为合法后继，保留原件 | `daowei2026/observe-iterate@5289eab7a18b434d8316f7bc87e7685d81df3370:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0002/PRO_RETURN.json`；原报告末段的旧机器状态说明不作为当前有效路由依据 |
| C0003／原 D001 | 同 E1 定向补正 Return，非重做 U；有效状态为 IN_PROGRESS，原生 U 仍 PARTIAL | `daowei2026/observe-iterate@72f33ce96e78653cfd94ae9fba0579fe50548848:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0003/PRO_RETURN.json` |
| C0003 物理核验 | controller 已核真实 turn `01a20c88-531a-7821-b4e4-5cc7200b35d8`、token／调用关系及实际 sol/max | 依据 C0004 FULL_ASSIGNMENT；本 manager 不合成独立物理 receipt |
| C0004／D002 | 原 manager 已消费上述有效回交，签发 X 后继，issuer_call_id=C0004 | `daowei2026/observe-iterate@c9742986ed6fbb7bc2d55bd87cab54de42c7539f:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/delegations/D002/DELEGATION.json`；正文同 commit；原 E1 已在 C0005 对同一 D002 作有限 X 工程尝试 |
| C0004 Return | D002／报告／双进度先发布回读，后以其为 parent 发布 IN_PROGRESS manager Return 并逐字回读 | `daowei2026/observe-iterate@74a46582f44b16b1f7f0890c30314684d211ef3f:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0004/PRO_RETURN.json`；报告：`daowei2026/observe-iterate@c9742986ed6fbb7bc2d55bd87cab54de42c7539f:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0004/MANAGER_REPORT.md` |
| C0005／D002／A01 | 原 E1 已作有限 X 工程尝试；600 秒窗口未获指定锁，runner 结束，Feature／正式 store 未开始 | Return：`daowei2026/observe-iterate@6610e2df899bb4f68666eacb8a8d33dfb242077c:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0005/PRO_RETURN.json`；报告：`daowei2026/observe-iterate@647871627d9f5f591a23d54c4a2a842b39f05346:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0005/EXECUTOR_REPORT.md`；A01：`daowei2026/observe-iterate@647871627d9f5f591a23d54c4a2a842b39f05346:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D002/FeatureRunResultBinding.json` |
| C0005 物理核验 | controller 已独立核真实 turn `01a20c98-d46b-7cc2-9969-0aae2dd689c8`、原 payload/token/调用关系、实际 sol/max、协议和 Git 原件 | 依据当前 C0006 FULL_ASSIGNMENT；本 manager 不合成物理 receipt |
| C0006 | 原 manager 消费有效资源等待回交，保留原工作后继；本 C 不签新 D/W | [本 C 报告](../calls/C0006/MANAGER_REPORT.md)，报告和双进度先发布回读，随后签发原 v2 IN_PROGRESS Return |

本 C 消费的是 executor Return，未借 `accepted_worker_refs` 登记；`workers=[]`，无 W 和 Worker Return。C0005 真实回交不赋予 X/G 完成资格；U 保持 PARTIAL。

## D. 原生有效范围、缺口与后继

| 节点／范围 | 当前状态 | 下一合法动作或保留条件 |
|---|---|---|
| U／D001 | PARTIAL，核心链可供 X 使用 | 原包／REMAINING_SCOPE 明确允许 X；取得真实 X 后依原件更新相关缺口，不重做本次 U、不自动改 COMPLETE |
| X／D002 | `NOT_ESTABLISHED_WAITING_SHARED_LOCK`，原工作未完成 | controller 核原锁自然释放及 A01 效果后，以新 C 在原 E1／copy 工作区续接原 D002；锁条件未变时不重复派生产，不预占 C 号 |
| G | 未开始，当前无有效正式结果输入 | 按原 L0，须有与当前实例绑定的完整正式结果；本 C 不提前签 G |
| finding／诊断 | 尚无正式 finding 或 DiagnosisReport | U 的源码／合同差异不是已确认业务缺陷，沿原 Workflow 后续处理 |
| 修正／回归 | 未发生 | 按原 Skill 与 Owner 初始范围；本 C 不制定路线 |
| Release | 未形成 FeatureReleaseGate／UpstreamReleasePackage | 原 L0 完成条件，不新增 Gate |

未确认项沿原生包保留：

| 原项 | 影响与恢复来源 |
|---|---|
| UQ01–UQ03 | 当前代码下 Wall、两组 F4、三 Attack 产品的 receipts、实际 source_scope／exact axis、有效参数和完整表读回待 X；旧候选均未采纳。有界路径查询不等于穷尽缓存。 |
| UQ04 | 分支可达性、末尾在建状态和过程证据待真实结果；不能从正式空行推造结论。 |
| UQ05–UQ06 | 指定 FRP 参考与当前 TIS 的版本／字段／职责差异作为来源事实保留；不启动 FRP/P2，不改上游或公共合同，不先升级为 finding。 |
| UQ07／NOT_EXPOSED | 信息最早可得时间及未正式暴露的 atom/carry/checkpoint/attempt 等仍未知或未暴露；receipt 不自动消除这些缺口。 |

## E. 权限、共享资源与恢复

D002 仅传 Owner／Binding 已有操作和 copy 工作区、本 Run 记录分支写面，当前工作范围为原 L0 X；controller 的 Chat 归档、Registry 维护不在 D 中。本 manager 无 Feature 执行或代码修改授权，只在本 Run 记录分支发布协调材料；未操作生产、未查看锁占用或启动计算。

共享生产互斥仍为 `/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/FORMAL_PRODUCTION.lock`。A01 原件记录 `acquired=false / released=false`，表示原尝试从未持锁；runner 已结束。A01 记录的锁身份为 device=83、inode=15061041；本 C 未操作锁或自行复测其状态。

依据准确 C0006 FULL_ASSIGNMENT，Build 独立 Run 当前仍在原 E1 中持同一实际锁计算 m 技术输入。D002 的具体生产因此等待；锁条件未变时不重复派同一生产尝试，不强停持有者、不另造锁或覆盖其成果。

恢复严格沿原 `daowei2026/observe-iterate@647871627d9f5f591a23d54c4a2a842b39f05346:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D002/REMAINING_SCOPE.md`：controller 核原锁自然释放、原 C0005 无未知副作用，核实没有实际 Feature 执行及正式结果目录后，在原 E1／copy 工作区续接原 D002。Owner 初始业务授权、原 D002 权限及实际系统审批边界不变；本 C 不改专业方法或建立 Owner 节点。

Build 独立采用其 391 版控制并在自身 D002/X；不得混用其专业版本、成果、线程或完成状态。只有具体冲突写入沿已有互斥管理，其余独立工作继续。

当前明确等待范围为 D002 的共享生产写入；独立、无冲突工作继续。没有新增 Owner 请求。发送或副作用状态如为 UNKNOWN，由 controller 先核原通道和动作事实；不能把旧的无结果记录当作新一次尝试已安全执行。

## F. 视图同步与具名后继

BUSINESS_PROGRESS 已同步到 C0005/A01 资源等待、有效成果与恢复条件；原 U 及未决全景保留。历史 C0001 进度快照在 `daowei2026/observe-iterate@0d5ae479b92e55b19e5a88bf1ebc8c4393b6d8f8:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/business_control/TASK_PROGRESS.md` 保留。

具名下一动作：`codex:OI-EAW-P1-ATTACK-STAT-20261124-01:controller` 保持上述资源等待，确认自然锁释放及原 C0005 效果后，向本 Run 原 E1 续接原 D002。具体生产恢复前不重派；实际 X 结果回原 manager 后，再按原 L0 判断后继资格，当前不能转 G。

C0004 既存发行历史：

- D002：`daowei2026/observe-iterate@c9742986ed6fbb7bc2d55bd87cab54de42c7539f:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/delegations/D002/DELEGATION.json`
- 报告：`daowei2026/observe-iterate@c9742986ed6fbb7bc2d55bd87cab54de42c7539f:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0004/MANAGER_REPORT.md`
- Return：`daowei2026/observe-iterate@74a46582f44b16b1f7f0890c30314684d211ef3f:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0004/PRO_RETURN.json`，`longrun-professional-return/v2 / role=manager / IN_PROGRESS`。
- Return 的 remaining_scope／continuation 均指向已存在的准确原件；`return_to=null`、`issued_order_refs=[]`、`accepted_worker_refs=[]`、`owner_request_ref=null`。
- C0004 Return 引用 `c9742986ed6fbb7bc2d55bd87cab54de42c7539f` 的先前进度快照；其后的 C0005 实际回交事实见上表。

C0006 报告与双进度先发布并准确回读，再发布本 C `longrun-professional-return/v2`。本 C 保持 `IN_PROGRESS`，`issued_delegation_refs=[]`、`issued_order_refs=[]`、`accepted_worker_refs=[]`、`owner_request_ref=null`；continuation 指向已存在的原 X 未完成范围，不签 D003，不改 D002 或 A01 原件。实际 Return 发行引用在回读后补记。

前次 C0004 双进度快照：`daowei2026/observe-iterate@69ece4ac48016cbfb656297388696a92195a96be:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/business_control/TASK_PROGRESS.md`。

快照日期：2026-11-24，当前协调调用 C0006；记录分支仅 `codex/oi-eaw-p1-attack-stat-20261124-01`；已核 Personal 连接。
