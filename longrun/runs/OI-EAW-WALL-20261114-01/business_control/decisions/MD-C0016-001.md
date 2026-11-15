# 管理决定｜MD-C0016-001｜A001 方法变更复审、D003/W007 合法收束与直接 BASE 接续

- `run_id / call_id / decision_id`：`OI-EAW-WALL-20261114-01 / C0016 / MD-C0016-001`
- manager：`chatgpt:OI-EAW-WALL-20261114-01:manager`
- invocation token：`oiwall-C0016-46ba9be6ddf5f86f77ad344d`
- 决定性质：同一 Run 的方法与授权增量生效后的管理复审；不是新 GO、不是新 Run、不是测试，不追溯改写历史已派 D/W 和已接受成果。
- 父任务结论：继续，仍为 `incomplete`；三个父问题继续 `OPEN`；H3 不具备条件。

## 1. 本次实际消费的权威来源

### 1.1 Owner 变更和有效授权

- Owner 逐字指令：`daowei2026/observe-iterate@33c7a222687186c1e1c8c685993a341513820d8d:longrun/runs/OI-EAW-WALL-20261114-01/authority_changes/A001/OWNER_CHANGE.md`
- 有效授权增量：`daowei2026/observe-iterate@b8514dbc38e3589fc01c9a7667899ee2059e814f:longrun/runs/OI-EAW-WALL-20261114-01/authority_changes/A001/EFFECTIVE_AUTHORITY.json`
- C0016 完整任务：`daowei2026/observe-iterate@096ee45c5c41a6afee5bed99ce634ee52ed3761a:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0016/FULL_ASSIGNMENT.md`
- C0016 Invocation：`daowei2026/observe-iterate@673896390068648fe25706c5d17207ed08d5ac51:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0016/INVOCATION.json`

后续新专业工作采用：

```text
business/control/skills = daowei2026/observe-iterate@dc18a7251b8d433bd8c16ccd0f9cbdf230b1819c
controller skill        = daowei2026/cgpterm@becfbcbc7eec3e4fc6a44cd0b0a7a934ec666ff8
```

观察材料准备唯一专业方法为新 `control/02_L1_观察材料准备流程.md` 中原 Skill 0～7。旧 S0～S5 独立执行链、S2/M05 工程前置和独立 G-RUN 执行链不再是现行方法。

A001 新增 Linux 授权原文：

```text
operation=wall-observation-work execution_context=linux:/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2
```

它允许本 Run 必要的 BASE 本地观察工作、按需新增脚本/数据/结果和先核差异后的必要小范围修改；仍禁止破坏性 Git、覆盖他人未提交修改、覆盖现役成果、无关写入或正式源码 push。

### 1.2 真实状态和旧执行事实

- 主控状态审计：`daowei2026/observe-iterate@64c2c923503bd86883cb39731d235dc811b42843:longrun/runs/OI-EAW-WALL-20261114-01/authority_changes/A001/CONTROLLER_STATUS_AUDIT.json`
- W007 本地事实报告：`daowei2026/observe-iterate@db7cc8a0c7337641017aef1b9fc980a23959dbfd:longrun/runs/OI-EAW-WALL-20261114-01/authority_changes/A001/W007_LOCAL_STAGE_REPORT.md`
- C0015 E1 Return：`daowei2026/observe-iterate@946fa7931bf25b88c04c11b3a58cbcb3590841c5:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0015/PRO_RETURN.json`
- C0015 专业进度报告：`daowei2026/observe-iterate@c9a7509ea824f4f014ba82f8a01a2d54cf94760e:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/D003_EXECUTOR_PROGRESS_C0015.md`
- 旧 D003：`daowei2026/observe-iterate@b7200816f86395cd1475ea3a482fc2e63086b967:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/DELEGATION.json`
- 旧 W007：`daowei2026/observe-iterate@e788e36c8e4c18e4888f1d8a225950f51c9a695c:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W007/ORDER.json`

确认：W007 已在 `2026-11-15T02:42:45.760143Z` 唯一物理派发，`2026-11-15T03:17:08.140Z` 本地 STOP；不是“未发送”。当前 Worker turn 已完成、thread `notLoaded`、Goal 为空、queue 为空，本次没有 resume/start/steer。

W007 的 85 份本地原件共 2,075,599 bytes，主控已独立核对具名 hash。没有 W007 formal Worker Return；本地报告不是 Worker Return，也不是专业接受。

## 2. 保留的 D001/D002 专业成果

### 2.1 D001

D001 `PARTIAL_WITH_LIMITS` 继续有效：

- current TIS/FRP working-tree 静态事实；
- historical O/C/D 资产、bounded reader 和 exact normal chain；
- current tuple、native reader、A、异常/时间场景等真实缺口；
- `EV-WALL-WORKING-v0.2` 继续为 WORKING，不冻结。

原件：`daowei2026/observe-iterate@b03a3b43497fce8c10f9dd539a4f623225dce237:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D001/results/D001_EXECUTOR_REPORT.md`。

### 2.2 D002

D002 的以下结果继续正式有效：

- `G-COMPARISON / EC-WALL-LEGACY-NORMAL-001 = PASS_WITH_SCOPE`；
- `EV-WALL-LEGACY-NORMAL-v1.0` 四命题均 `SUPPORTS`，共享同一 exact historical chain；
- `QCR-LEGACY-IDENTITY-NORMAL-001 = COMPLETE_FOR_SCOPE`；
- `QCR-LEGACY-OC-PUBLICATION-NORMAL-001 = COMPLETE_FOR_SCOPE`；
- `QCR-LEGACY-TO-CURRENT-NONEXTRAPOLATION-001 = COMPLETE_AS_BOUNDARY`；
- current terminal/replay/conflict/transaction/UTI 等静态风险候选继续作为后继问题线索，不是已确认 bug。

原管理消费：`daowei2026/observe-iterate@97fda81d932cb55eefb2674aa2d3e67a4425fa84:longrun/runs/OI-EAW-WALL-20261114-01/calls/C0007/MANAGER_REPORT.md`。

A001 不重开、降级或改写这些结果。后继不得重复抽取同一 historical chain来制造新增证据。

## 3. D003/W002～W007 的专业复审

### 3.1 WorkQuality 与事实资格

C0015 已专业接受 W002～W006 的限域 STOP 事实；这些历史专业接受继续有效。它们证明旧工程路线实际调查到哪里、哪些动作未发生，但不再构成新材料工作的前置资格。

W007 本地报告可作为**状态与执行事实来源**保留：

- fresh/carry-forward evaluator、FIOCLEX 与组合锁证明、唯一 R0-A1 当前实测为 PASS；
- R0-B 的首个 Git 命令因旧 sandbox policy 拒绝 `openat("/dev/null", O_RDWR)` 而 STOP；
- 两套 closure 均未实际评估；R0-C、八 EP、staged source、patch、fixture、compile/serialization 和所有 scenario/current evidence 均未进入；
- 85 文件和仍在的 reservation lock 是已发生副作用，需合法收束。

但 manager 不直接把 W007 当成 accepted Worker Return。W007 的专业消费、旧 D003 的最终关闭、证据取舍和锁释放仍由原 E1完成。

### 3.2 哪些旧工程工作不再是真正业务依赖

A001 后以下内容不再是取得 Wall 观察材料的必要前置，也不得换名重派：

- 独立源码副本或 staged source 作为先决条件；
- Landlock/seccomp 组合隔离；
- 全局零外写证明；
- independent clean/offline build closure；
- 为满足旧 S2/M05/G-RUN 而建立的四 PASS 链；
- 在业务取数前完成八 EP 全套工程建设；
- 为旧 cap/monitor 合同继续修 `/dev/null`、procfs 或 sandbox policy。

因此 W007 的 STOP 是旧工程动作的真实终态，不是业务材料准备失败，也不产生继续修旧隔离的后继。

### 3.3 哪些内容仍可能有业务价值

以下不因 D003 路线停止而删除，但只在新方法证明当前问题确实需要时最小复用：

- current state/active-map 可观察入口；
- structured evidence/identity/time schema；
- exact error/transaction trace；
- existing test-contract conflict ledger；
- targeted fixture/provenance。

它们不再作为整包前置。若现有 BASE 数据、源码、test、trace 或小脚本已经足够，就直接使用；只有缺少某项会阻止当前判断时，才做那一项最小增量。

## 4. 四类管理判断

### 4.1 WorkQuality

- C0015 历史专业报告：`ACCEPTED_AS_HISTORICAL_PROGRESS`；
- W007 local report：`FACTUAL_STATUS_EVIDENCE_ONLY`，等待 E1 closeout review；
- 旧 D003：不要求继续完成原八 EP 或旧 Phase-0，转入收束。

### 4.2 UseEligibility

可继续使用：D001/D002 业务成果、C0015 对 W002～W006 的限域专业接受、W007 已发生的时间/命令/STOP/文件/锁事实。

不得使用为：current business evidence、current runtime PASS、八 EP 完成、旧工程路线必要性、scenario action执行、父问题完成。

### 4.3 ActionEligibility

- 旧 W007：`PHYSICALLY_STOPPED / DO_NOT_RESUME / DO_NOT_REDISPATCH`；
- 旧 D003 的前瞻执行资格：`WITHDRAWN_BY_A001_METHOD_CHANGE`；
- 旧 D003 当前管理状态：`STOPPED_FOR_PROSPECTIVE_WORK / PENDING_E1_PROFESSIONAL_CLOSEOUT`；
- 新 D004：可按 A001 在 BASE 直接开展必要本地观察工作；
- 新方法不设独立 G-RUN 链。E1 对每个实际动作只需按当前动作检查真实成本、副作用、差异和可恢复性；显著高成本、不可逆或目标外动作才停止并回 manager。

### 4.4 TaskCompletion

三个父问题和父任务继续 OPEN/incomplete。historical normal-chain scoped records保持完成；current runtime、current identity/A/D/transaction/time、current suitability 仍未达到原完成深度。

## 5. Gate 与历史状态处理

| 对象 | C0016 决定 | 说明 |
|---|---|---|
| legacy `G-COMPARISON` | 保持 `PASS_WITH_SCOPE` | D002正式结果不变 |
| historical scoped QCR | 保持完成 | 不外推 current |
| full `EV-WALL-WORKING-v0.2` | `WORKING / NOT FROZEN` | 后继可派生新 current 版本，不无痕覆盖 |
| `G-DIAGNOSIS` | `NOT TRIGGERED` | 尚无 current frozen comparison 的正式 COUNTERS |
| old D003 prerequisite route | `SUPERSEDED_BY_A001` | 保留历史事实，不再执行八 EP 整包 |
| old scenario/normal `G-RUN` 记录 | 历史保留、对新 M 不构成门禁 | 两 action未执行；新方法按真实材料需要重判 |
| current M 方法 | `control/02` Step 0～7 | 不再使用 S 链、S2/M05或独立 G-RUN |
| H3 | `NOT ELIGIBLE` | parent仍 incomplete |

## 6. W007 证据、锁与旧单收束合同

原 E1 在新 D004 内必须先完成以下收束，不恢复旧 W007：

1. 引用 controller audit、W007 local report和必要的具名本地原件，形成 `D003_W007_CLOSEOUT_REVIEW.md`；
2. 明确 W007 为 `PHYSICAL_STOP_NO_FORMAL_RETURN`，不得伪造或补写成当时已存在的 Worker Return；
3. 保留至少 W007 binding、local stage report、publication manifest、hash/freeze receipt、R0-A/R0-B关键命令/trace和85原件总清单/核验结果；不要求为完成旧工程把85项全部搬运到GitHub；
4. 在确认原 Worker终态、无队列、无执行中写者且证据已固定后，通过**新的**合法 Worker action（如实际需要）释放 holder `251010/startticks48763578/inode14806399` 与旧 `.D003-writer.lock`；该动作是资源收束，不是 W007 resume；
5. 锁释放前不让新的写动作竞争旧 D003 资源；锁释放后记录 receipt。不得删除 W007 证据根；
6. 最终将 D003 标为 `SUPERSEDED_STOPPED_WITH_RETAINED_EVIDENCE`，清楚列出历史可用事实、未完成事项和“不再需要”的理由。

manager不直接签 W，也不把主控状态审计当成跳级 Worker专业接受。

## 7. 新的业务执行路线

签发 D004 给原 E1，覆盖三个相邻但分开的工作面：

### A. 旧 D003/W007 收束

按第6节完成专业 closeout和锁释放；不得继续旧隔离、closure、八 EP或cap链。

### B. 新 M｜直接 BASE 观察材料准备

按 `control/02` 原 Skill 0～7：

1. 复用 D001/D002 资产、材料计划、normal-chain和 current风险候选；
2. 在 `/dwdhome/fy/BASE_E6_2` 调查并直接使用现有源码、数据、构建环境、test、trace、reader、Notebook/工具；
3. 对三个父问题重新标注本轮**必需/有条件需要/可选/暂不准备**材料，不继承“九场景全部先做”的旧假设；
4. 优先实际取得 current 或可精确绑定当前实现的数据：source/params/calendar/time/object、upstream events、O/C/D；A/transaction/exact error只在当前判断确需且现有资产可低成本取得时补；
5. 可以使用现有test、短窗口运行、可控小脚本和先核差异后的必要小范围本地修改；不得覆盖他人未提交修改、破坏性Git、覆盖现役产物或push正式源码；
6. 每项动作记录命令、实际输入/输出、代码/参数/数据绑定、运行影响和真实失败；不要求独立副本、Landlock/seccomp、全局零外写或clean closure；
7. 形成 `DATA_READY / PARTIAL_WITH_LIMITS / BLOCKED` 的真实材料包。只完成计划不能冒充取数。

### C. 新 R｜按可用材料开展 current 合理性分析

- `analysis_round_id = AR-WALL-003`；
- 从 Owner目的、业务推导和实现来源建立 `EV-WALL-CURRENT-WORKING-v0.1`；
- 探索可先使用 WORKING版本；正式 comparison 前只冻结足以与已取得证据绑定的最小子集，记录证据截止，不因已看结果反写预期；
- 对 current identity/lifecycle、O/C/D/A publication/state和业务适用性逐场景给 `SUPPORTS/COUNTERS/MISSING/AMBIGUOUS/NOT_APPLICABLE/PENDING`；
- 只在正式 COUNTERS 值得解释且有区分路径时进入诊断；不因静态风险自动判 bug，不强制调参；
- 对能完成的 current 子问题形成新的 QuestionCompletionRecord，对其余准确保留限制和下一证据需求。

局部材料缺失不阻断其他独立问题；能在同一专业工作内低成本核实的事实直接核实，不为每个字段创建跨 Workflow 请求。

## 8. 准确后继与恢复条件

- 新 delegation：`D004`，recipient为原 E1，return_to为原 manager；
- manager不签 W；E1根据实际需要签下一未占用新 W（当前候选 W008），引用 A001 真实授权，不复用 W007；
- 新 W 的 Linux grant按A001使用 `/dwdhome/fy/BASE_E6_2`，GitHub只发布本Run目录；具体写入、保护现有差异和停止点由D004/W正文精确收窄；
- D004可先返回 D003 closeout，再继续材料/分析，或在同一正式回交中一起返回；但不能让旧收束无限阻断实际材料工作；
- manager恢复条件：D004完整/部分回交、具名材料阻断、确认的高成本/不可逆动作、或运输/权限/外部效果异常。

Owner无需逐项确认；只有现有工具确实无法执行或目标发生重大变化时再形成具名请求。
