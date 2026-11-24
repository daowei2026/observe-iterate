# TASK_PROGRESS｜AttackSegment 机器状态与恢复

## A. Run、来源和角色

- run_id：`OI-EAW-P1-ATTACK-STAT-20261124-01`；work_id：`OI-EAW-P1-ATTACK-STAT`；business_case_id：`EAW-P1-ATTACKSEGMENT`
- 专业控制统一 commit：`9877826236e0995e7255e6cbfedc2d1b89dea6da`；controller 版本：`815c505c1cc3d965aaafa831d23c4c88368cb70a`
- 原 L0：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:control/01_L0_统计驱动的单特征闭环.md`；manager 指南：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:longrun/professional/PRO_MANAGER_GUIDE.md`
- 当前现有 Skill：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:skills/reasonableness-analysis/business-discrepancy-diagnosis/SKILL.md`；适用补充：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:skills/reasonableness-analysis/STATISTICS_DRIVEN_PRACTICE.md`
- 唯一业务输入／ReviewTarget：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:task-inputs/eaw-p1-attack-stat-20261124/ATTACK_RUN_INPUT.md`；正式目标仍为完整 rb/m。
- Owner：`daowei2026/observe-iterate@b912f85368fed916c45603c81aa8ef304bc146b6:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/OWNER_START.md`；Binding：`daowei2026/observe-iterate@723d65a2ca4fbcf691e9a82eb153a21faae18390:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/RUN_BINDING.json`；Resource：`daowei2026/observe-iterate@723d65a2ca4fbcf691e9a82eb153a21faae18390:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/RUN_RESOURCE_BINDING.json`
- profile：`CODEX_NATIVE_DIRECT`；post_start_owner_policy：`AUTONOMOUS`；`workers=[]`
- manager：`codex:OI-EAW-P1-ATTACK-STAT-20261124-01:manager`；复用原 E1：`codex:OI-EAW-P1-ATTACK-STAT-20261124-01:executor:E1`，物理映射和新 C 派达由 controller 负责。
- workspace：`/dwdhome/fy/BASE_E6_2_copy`；TIS：`/dwdhome/fy/BASE_E6_2_copy/mquant/tis`。
- 当前 INVOCATION：`daowei2026/observe-iterate@954d75f884b043cbc163963ef2fea978effbd148:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0010/INVOCATION.json`；FULL_ASSIGNMENT：`daowei2026/observe-iterate@beb0dded73ea5df390a874bdfd3b0af80737dab5:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0010/FULL_ASSIGNMENT.md`。
- controller 已核 C0009 原 payload/token、实际 sol/max、D002 issuer/return_to 与 executor_return；依据为准确 FULL_ASSIGNMENT，本 manager 不构造物理 receipt。
- snapshot：C0010 current；原 D002 未完，X 工程缺口待专业诊断。业务入口：[BUSINESS_PROGRESS.md](BUSINESS_PROGRESS.md)。

## B. 当前代码、实例与有效结果

| 项目 | 当前事实 | 来源 |
|---|---|---|
| TIS／分支 | `179016111ed0394f92025313e46bd13534932a74`；`codex/oi-eaw-p1-attack-fix-20261124-01`；tracked 产品源码无改 | C0009 完整绑定和当前任务 |
| Feature／参数 | AttackFlowAssembler()／`attack-default`，Wall／两组 F4 默认业务参数不变 | 逐对象 ppdict/ppid、源码指纹和 receipts 保存在原生绑定 |
| 正式范围 | `TA_updto20240229_DBA`；`rb,m`；`2021-01-01..2021-12-31`；`night_end_at_2300` | 唯一业务输入，未缩减范围 |
| 当前绑定 | `INCOMPLETE_WITH_RECORDED_ENGINEERING_GAP`；`formal_complete=false`、`eligible_for_G=false` | `daowei2026/observe-iterate@d3e05b73fd2a6fcc3b3b5d248bdd61f11e8f7a34:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D002/C0009/FeatureRunResultBinding.json` |
| U | PARTIAL，原具名未知和 NOT_EXPOSED 保留 | `daowei2026/observe-iterate@758c77a566672a4514cbff6d3f26236769d17b59:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D001/FeatureUnderstandingPackage.json`；`daowei2026/observe-iterate@758c77a566672a4514cbff6d3f26236769d17b59:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D001/REMAINING_SCOPE.md` |
| rb 三产品 | 35 表严格读回资格沿 C0007 保留；其 Wall/tactical/structural 也保留有效资格 | 当前绑定及原 C0007 |
| m 实际上下文 | `stk_tlist=m`，`symbols=['m']`、`symbol_index=0`、`trading_unit=10`，A05 已实测 | current_call_execution |
| m Wall | `REUSED_CURRENT_RUN_AND_FULL_READBACK_VERIFIED`；5 表、receipt、PPID、同版本指纹、当前原生轴及 source_scope 全量只读核验通过 | 当前绑定 m wall，未重产 Wall |
| m 两 F4 | `EXECUTION_OR_READBACK_FAILED`，已真实 Gen，未取得完整有效结果/成功 receipt/严格读回 | 当前绑定异常链及原报告 |
| m Attack | `BLOCKED_MISSING_CURRENT_UPSTREAM`；本 C0009 未启动，目录不存在 | `current_call_attack_execution_started=false` 及原 effects |
| 父 Run | `incomplete / IN_PROGRESS` | 完整 X/G、诊断结果及 Release 未形成 |

当前绑定累计 `attack_feature_execution_started=true` 只对应历史 rb；C0009 的 m Attack 未启动，作用域分别保留。C0009 原报告：`daowei2026/observe-iterate@d3e05b73fd2a6fcc3b3b5d248bdd61f11e8f7a34:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0009/EXECUTOR_REPORT.md`；有效 Return：`daowei2026/observe-iterate@ebbf7b69a092459f8011cf90a37383ec5fdd5696:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0009/PRO_RETURN.json`。

## C. 原工作与本次既有 Skill 委派

- 原 D002：`daowei2026/observe-iterate@c9742986ed6fbb7bc2d55bd87cab54de42c7539f:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/delegations/D002/DELEGATION.json`，`issuer_call_id=C0004`；签发 Return：`daowei2026/observe-iterate@74a46582f44b16b1f7f0890c30314684d211ef3f:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0004/PRO_RETURN.json`。本次不改写原 D002，不把其 X 变更为诊断完成。
- C0009 原恢复：`daowei2026/observe-iterate@d3e05b73fd2a6fcc3b3b5d248bdd61f11e8f7a34:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D002/C0009/REMAINING_SCOPE.md`，原文明确本 D002 不含诊断或产品修复，需 manager 按原 Workflow 协调校验失败后继。
- 本 C 已签发 D003：`issuer_call_id=C0010`，recipient 为原 E1，回原 manager；机读件：`daowei2026/observe-iterate@ff042e7c90cf73019616f4a9a5710364a0a4bffe:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/delegations/D003/DELEGATION.json`，正文同 commit，均已发布并逐字回读。
- D003 使用原 `business-discrepancy-diagnosis` Skill 对已记录 X 工程异常作专业来源／责任核查。其原文第 1 节适用于多种竞争解释和改动前判断问题层，第 3／4 节规定事实缺口由执行者补查；输出／完成条件直接沿 Skill。
- 诊断输入只引用原正式目标、U 处理链、C0009 实际比较／绑定、失败 effects 和原权限；没有伪造 G profile、候选队列或业务 finding。完整 G 仍未开展，不新增专业 Gate。
- D003 发布不表示已物理派达或诊断完成；controller 核本 C 真实 Return／D003 后，复用原 E1 发新 C。当前没有 DiagnosisReport、LogicLocalization 或 UpstreamFinding。

## D. 真实历史与失败 effects

| 调用／尝试 | 已发生事实 | 原件／保留入口 |
|---|---|---|
| C0001／D001 | 首轮 U 签发，之后原生 U PARTIAL | `daowei2026/observe-iterate@e20128bff682c58bc2a66a6c5ed176f78634c476:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/delegations/D001/DELEGATION.json` |
| C0002／C0003 | U 报告和旧机器状态冲突保留；同 E1 C0003 定向补正，不重做 U | `daowei2026/observe-iterate@72f33ce96e78653cfd94ae9fba0579fe50548848:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0003/PRO_RETURN.json`；完整历史见前次进度快照 |
| C0004／D002 | 签发原 L0 X | 上述原 D002 与 C0004 Return |
| C0005／A01、C0006 | A01 未获锁、未执行 Feature；manager 资源等待协调，无新 D | `daowei2026/observe-iterate@0d2137442b76f872f2b38eb4e3cf3d16d98303f2:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0006/PRO_RETURN.json` |
| C0007／A02/A03/R01/A04、C0008 | A02 运行器断言保留；A03 部分生产、R01 rb 35 表有效；A04 未获锁；C0008 沿原 D002 剩余 m 续接 | `daowei2026/observe-iterate@e38beb147f5238eeebebb1a9203676c6843573b4:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0008/PRO_RETURN.json`；当时双进度：`daowei2026/observe-iterate@e71c51aca17a3349bab09bcfed4c3b2c6595eaf8:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/business_control/TASK_PROGRESS.md` |
| C0009／A05 | 已采用原生 m 上下文，取得原锁后复核 Wall 并真实运行两 F4；两者校验失败，m Attack 未启动 | 当前完整绑定／报告／失败清单 |
| C0010／D003 | 原 manager 已消费真实未完 X，签发既有诊断 Skill，未作专业归因 | 报告：`daowei2026/observe-iterate@ff042e7c90cf73019616f4a9a5710364a0a4bffe:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0010/MANAGER_REPORT.md`；实际 Return：`daowei2026/observe-iterate@290fabcdb5d6070ed1dbab49f0485dd8079a3250:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0010/PRO_RETURN.json`；待 controller 核回收与物理派达 |

A05 原始失败为：`交易日区间在 2021-03-12 00:00:00 前不连续: 1792800 != 1792801`。调用栈经过 pressure_big_deal.py 至 tick_quote_context.py。堆栈是执行证据，未证明责任归属；manager 不依据文件名、栈位置或其它 Run 预定原因／修法。

失败 effects：`daowei2026/observe-iterate@d3e05b73fd2a6fcc3b3b5d248bdd61f11e8f7a34:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D002/C0009/evidence/failed_F4_effect_manifest.json`。共 12 个 DBA／677,239,968 字节；每个文件的路径、大小、mtime、SHA256 和 `INCOMPLETE_UNVERIFIED_FAILED_F4_EFFECT_DO_NOT_CONSUME_OR_OVERWRITE` 资格均保留。完整读回和成功 F4 receipt 未建立，不作为有效结果或 G 输入，不原路径覆盖重试。

原 640 个既存产物文件和历史 JSON／发布原件及 U 未变，原 A01/A02/A03/R01/A04/A05、原错误和 journal 均保留。本 C 未重新读取市场结果或修改失败路径。

## E. 当前未完成范围、权限与恢复

| 范围 | 当前状态 | 合法后继／恢复来源 |
|---|---|---|
| U | PARTIAL | 按原 Skill 和新的有效事实处理相关更新，未知不自动关闭 |
| X／D002 | m 无有效 F4，Attack 未启动；完整 rb/m X 未完成 | 原 C0009 剩余及诊断专业回交；未确认合法有效执行条件前，不重复相同失败 Gen |
| 诊断／D003 | 已签发，待原 E1 专业执行 | 原 Skill 的 DiagnosisReport 及相关原生记录，不预定责任结论 |
| G | 未执行，`eligible_for_G=false` | 须有当前完整正式结果，不用局部 rb 或失败半成品替代 |
| UpstreamFinding | 尚未形成 | 若专业证据指向上游，依原输入／Skill 如实记录原因、影响和恢复条件 |
| 修正／Release | 未发生／未形成 | 原 GO 禁止面和原 L0 完成条件持续有效 |

Owner 代码修改授权仅 Attack 自身两文件、直接测试及其专属参数／业务常量；F4、Wall、其它上游、公共模块、市场数据禁止修改。D003 当前仅诊断，机读写面为 copy 工作区与本 Run 记录分支，不扩大为上游修复许可。manager 只协调发布，不跑 X/G、诊断实验或修改工程代码。

正式 rb/m、2021 全年、SOF 与日历不变。不得通过缩窗、换品种、绕过检查、改数据或覆盖半成品取得成功表象；局部诊断证据不能替代正式 X/G。若实际证据指向越权修改，只保留受影响工作的局部阻断和恢复条件，不新增 Owner 业务审批。

A05 实际获取并释放原锁：`/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/FORMAL_PRODUCTION.lock`，device=83、inode=15061041。runner／观察器已结束，后检探测获取释放不是预约；没有本 Run 遗留占锁。未来共享写入仍需实际取得同一原锁，由 controller／E1 核现场，不改锁、另造锁或强停他人。当前生产阻断记录为已发生工程校验失败，未继续登记为旧的“未获锁未执行”状态。

独立工作继续；Build 的控制版本、业务结果、修复与诊断结论均不迁用。

## F. 当前具名下一动作与发行

controller 核 C0010 真实 Return、D003 与原权限／现场绑定后，在原 E1 派达现有偏差诊断 Skill；专业原生回交原 manager，再按原 Workflow、原 D002 剩余和真实权限协调。当前没有重复生产、G 或 Feature 验收任务。

BUSINESS_PROGRESS 已同步有效 rb/m Wall、上下文纠正后真实 F4 失败、12 个无效半成品、责任未诊断和本次既有 Skill 后继。报告、D003 和双进度先发布并准确回读，再发布本 C 原 v2 Return。

C0010 实际发行事实：

- D003：`daowei2026/observe-iterate@ff042e7c90cf73019616f4a9a5710364a0a4bffe:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/delegations/D003/DELEGATION.json`；正文、报告和双进度先前快照同 `ff042e7c90cf73019616f4a9a5710364a0a4bffe` 提交，五个文件均已发布并逐字回读。
- 报告：`daowei2026/observe-iterate@ff042e7c90cf73019616f4a9a5710364a0a4bffe:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0010/MANAGER_REPORT.md`。
- Return：`daowei2026/observe-iterate@290fabcdb5d6070ed1dbab49f0485dd8079a3250:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0010/PRO_RETURN.json`，以先前提交为 parent，普通条件发布并逐字回读。
- Return 使用原 `longrun-professional-return/v2`，保持 `role=manager / IN_PROGRESS`、`return_to=null`，issued_delegation_refs 与 continuation 均引用上述既存 D003；remaining_scope 引用先前已存在进度。`issued_order_refs=[]`、`accepted_worker_refs=[]`、`owner_request_ref=null`。
- 本次只补记真实发行事实，不制造引用循环；原 D002 签发仍为 C0004，C0009/A05 及失败 effects、既有成果原件未改写。发布不表示 controller 已核回收、E1 已物理接收、诊断已执行或 X 已恢复。

快照：2026-11-24，当前 C0010；父 Run IN_PROGRESS；记录分支仅 `codex/oi-eaw-p1-attack-stat-20261124-01`，已核 Personal 连接。
