# C0004 manager 报告｜消费 U PARTIAL，安排原 L0 X

## 有效回交消费

本 manager 已亲自读取 C0004 的准确 INVOCATION／FULL_ASSIGNMENT、有效 C0003 Return，以及原 E1 在 `758c77a566672a4514cbff6d3f26236769d17b59` 的执行报告、原生 FeatureUnderstandingPackage、阅读版和 REMAINING_SCOPE；按其原生状态和下游使用资格消费，不代替 executor 重做专业判断。

- 有效 Return：`daowei2026/observe-iterate@72f33ce96e78653cfd94ae9fba0579fe50548848:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0003/PRO_RETURN.json`
- 原生 U 包：`daowei2026/observe-iterate@758c77a566672a4514cbff6d3f26236769d17b59:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D001/FeatureUnderstandingPackage.json`
- 阅读版：`daowei2026/observe-iterate@758c77a566672a4514cbff6d3f26236769d17b59:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D001/FeatureUnderstandingPackage.md`
- 原报告：`daowei2026/observe-iterate@758c77a566672a4514cbff6d3f26236769d17b59:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0002/EXECUTOR_REPORT.md`
- 未完成范围：`daowei2026/observe-iterate@758c77a566672a4514cbff6d3f26236769d17b59:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/professional_results/D001/REMAINING_SCOPE.md`

U 的 `completion_status=PARTIAL` 保持原样。原报告、完成原因、UQ01 和 REMAINING_SCOPE 明确：主要实现链可供 X 继续，G 尚缺本 Run 当前有效的正式运行绑定。已消费的是具名范围的可用成果，没有把 U 改为 COMPLETE。

C0002 原 Return `daowei2026/observe-iterate@5289eab7a18b434d8316f7bc87e7685d81df3370:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0002/PRO_RETURN.json` 的 `REPORTED_COMPLETE` 与非空 remaining／continuation 冲突，仍保留为历史，不作为合法路由触发。C0003 是原 E1 对原 D001 的定向补正，`professional_state=IN_PROGRESS`；没有重做 U、改产品代码或执行 X/G。原报告末段关于旧机器状态的文字也按历史保留，以 C0003 有效 Return 为准。

真实 turn、sol/max、token／调用关系与原件的核实采用 controller 在准确 FULL_ASSIGNMENT 中给出的事实，不由 manager 构造物理 receipt。

## 原 Workflow 后继

采用专业控制 commit：`9877826236e0995e7255e6cbfedc2d1b89dea6da`。

- 原 L0：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:control/01_L0_统计驱动的单特征闭环.md`
- 原 U Skill／IO：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:skills/feature-understanding/SKILL.md`；`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:skills/feature-understanding/IO_SPEC.md`
- manager 指南：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:longrun/professional/PRO_MANAGER_GUIDE.md`
- 唯一输入：`daowei2026/observe-iterate@9877826236e0995e7255e6cbfedc2d1b89dea6da:task-inputs/eaw-p1-attack-stat-20261124/ATTACK_RUN_INPUT.md`
- 原 Owner／Binding：`daowei2026/observe-iterate@b912f85368fed916c45603c81aa8ef304bc146b6:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/OWNER_START.md`；`daowei2026/observe-iterate@723d65a2ca4fbcf691e9a82eb153a21faae18390:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/RUN_BINDING.json`

原 U IO 的 PARTIAL 允许具名下游在明确范围内继续。依据原产物的 X 使用资格和 L0 U→X→G，本 C 签发 [D002](../../delegations/D002/DELEGATION.json) 给本 Run 原 E1，工作为原 L0 的「X｜运行正式 Feature」，输出沿原定义为 FeatureRunResultBinding。X 是工程操作，不新增独立 Skill；本 C 未提前签发 G、未制定实现步骤、专业方法、统计项目或附加 Gate。

D001 原包、缺口、代码／构造证据继续有效于其已说明范围；exact Wall/F4/Attack receipts、source_scope／exact axis、运行有效参数和完整读回仍未核定。NOT_EXPOSED、分支可达性、参考合同差异和最早信息可得时间继续按原项保留，不自动消除，也不先升级成 finding。

## 双进度与实际范围

本次同步 [BUSINESS_PROGRESS](../../business_control/BUSINESS_PROGRESS.md) 和 [TASK_PROGRESS](../../business_control/TASK_PROGRESS.md)，记录有效 PARTIAL 成果、C0002 冲突／C0003 补正历史、现有缺口和 D002 具名后继。原生产物和历史 Return 均未改写。

本 manager 仅协调并发布本 Run 记录，没有运行 Feature、统计、诊断、生产探针或修改 TIS。当前没有本 Run 正式 X/G、finding 诊断或 Release，父 Run 保持 `IN_PROGRESS / incomplete`。Build 在其独立 391 版 Run 的 D002/X，不是 Attack 前置，未混用其成果。

## 来源和合同核对

前次已与精确远端核对的 15 个 `9877826236e0995e7255e6cbfedc2d1b89dea6da` 原件，当前本 Run 只读快照 blob 均保持一致；已复核 L0 的 X 定义、manager 边界和 U 原生 PARTIAL 使用资格。对 C0003 使用原 v2 Schema／状态关系核对通过，对 C0002 仍复现其状态冲突。这些核对不代替 controller 的物理回执、发送前授权和共享资源核验。

| 本次准确读取的原件 | Git blob SHA |
|---|---|
| `c4_invocation` | `b1a0b3f627ab375bee12faa2d8c65ac28f908ab0` |
| `c4_assignment` | `19000a193f409e520c8f920f4c28343c7d6a0cc1` |
| `c3_return` | `3199478b2376196dfec64c09a09d20160984c3f7` |
| `c2_report` | `773384f842857d7b723084dcf6a2a2e7d0e726ba` |
| `u_package` | `15817e627ef65befc9ce36547aa8ba4d7cff8b8a` |
| `u_readable` | `d2ec7070e2d0926ab4b4e331ab8a923245f3cae2` |
| `u_remaining` | `4c7744c05e5eaed77f5d48aca4752872d6075312` |
| `c2_bad_return` | `4b4c44bab9ccd21ba6ea859969e5a9102d619f36` |

## 回交与恢复

- 当前指令：`daowei2026/observe-iterate@5300135d8a18d803a6215b7c007f94d16eb2da4f:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0004/INVOCATION.json`；`daowei2026/observe-iterate@8125d58f976f7c4faa049f2777e835d7ffef4889:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/calls/C0004/FULL_ASSIGNMENT.md`
- 权限与资源：`daowei2026/observe-iterate@723d65a2ca4fbcf691e9a82eb153a21faae18390:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/RUN_BINDING.json`；`daowei2026/observe-iterate@723d65a2ca4fbcf691e9a82eb153a21faae18390:longrun/runs/OI-EAW-P1-ATTACK-STAT-20261124-01/RUN_RESOURCE_BINDING.json`
- 先发布 D002／本报告／双进度并准确回读，再发布本 C 原 v2 manager Return，`professional_state=IN_PROGRESS`，保留 remaining_scope 与具名后继；`owner_request_ref=null`。
- 下一动作由 `codex:OI-EAW-P1-ATTACK-STAT-20261124-01:controller` 核真实 C0004 Return、D002 和既有 Owner 范围，向本 Run 原 E1 派达 X；不新建 Worker。实际共享写面沿已存生产互斥，由 controller／E1 核验，本 manager 不操作锁。
- 当前未确认新的阻断；初始授权内工作不新增 Owner 节点。D002 发布不代表物理派达或运行成功，实际 X 结果回原 manager 后再沿原 L0 消费。
