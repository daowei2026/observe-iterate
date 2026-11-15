# D004｜A001 方法切换后的 D003/W007 收束、直接 BASE 取材与 current 合理性分析

## 0. 运输身份

- `run_id`：`OI-EAW-WALL-20261114-01`
- `delegation_id`：`D004`
- `issuer_call_id`：`C0016`
- `issuer`：`chatgpt:OI-EAW-WALL-20261114-01:manager`
- `recipient`：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`
- `return_to`：`chatgpt:OI-EAW-WALL-20261114-01:manager`
- 管理决定：`daowei2026/observe-iterate@02f7a2139e193aae6d9257363a82d72cc2502f1a:longrun/runs/OI-EAW-WALL-20261114-01/business_control/decisions/MD-C0016-001.md`
- Owner 方法与授权变更：
  - `daowei2026/observe-iterate@33c7a222687186c1e1c8c685993a341513820d8d:longrun/runs/OI-EAW-WALL-20261114-01/authority_changes/A001/OWNER_CHANGE.md`
  - `daowei2026/observe-iterate@b8514dbc38e3589fc01c9a7667899ee2059e814f:longrun/runs/OI-EAW-WALL-20261114-01/authority_changes/A001/EFFECTIVE_AUTHORITY.json`

本 D 是同一 Run 在 A001 生效后的专业接续。它不重做 D001/D002，不恢复旧 W007，不把旧 D003 换名继续，也不是新 GO、测试或源码开发项目。

D004 同时包含三个相邻但边界清楚的工作面：

1. **Closeout lane**：由原 E1 专业收束旧 D003/W007 和 reservation lock；
2. **M lane**：按新版唯一方法直接使用 BASE 现有源码、数据、环境和工具实际取得观察材料；
3. **R lane**：在真实材料上开展 current 范围的合理性分析并形成可交付结果。

局部 closeout 或某项材料缺失不得冻结其他可独立继续的工作。

## 1. 原业务问题、工作身份和本轮深度

### 1.1 三个父问题

- `Q-WALL-IDENTITY-LIFECYCLE`：current run-local Wall identity、正常/异常/时间状态变化及其可解释性；
- `Q-WALL-PUBLICATION-STATE`：current O/C/D/A 与 upstream、writer、reader、transaction 的真实关系；
- `Q-WALL-BUSINESS-SUITABILITY`：上述 identity/state/publication 语义是否适合“在本次运行内维护上游认出的同一 Wall 生命周期”。

### 1.2 新工作实例

```text
WI-WALL-D003-CLOSEOUT-001
WI-WALL-DIRECT-MATERIAL-001
WI-WALL-CURRENT-ANALYSIS-001
```

导航视图：

```text
M：只采用 control/02 原 Skill 步骤 0～7
R：R0/R1/R2/R5 为当前主路径；R3 仅在正式 COUNTERS 值得诊断时进入
analysis_round_id：AR-WALL-003
current expectation seed：EV-WALL-CURRENT-WORKING-v0.1
```

M 不再有 S0～S5、独立 S2、M05 或强制独立 G-RUN 链。实际动作只核本动作的成本、影响、差异和可恢复性。

## 2. 必须采用的精确输入

### 2.1 新方法、角色和运输合同

- `daowei2026/observe-iterate@dc18a7251b8d433bd8c16ccd0f9cbdf230b1819c:control/01_L0_完整业务任务与双向衔接.md`
- `daowei2026/observe-iterate@dc18a7251b8d433bd8c16ccd0f9cbdf230b1819c:control/02_L1_观察材料准备流程.md`
- `daowei2026/observe-iterate@dc18a7251b8d433bd8c16ccd0f9cbdf230b1819c:control/03_L1_合理性分析流程.md`
- `daowei2026/observe-iterate@dc18a7251b8d433bd8c16ccd0f9cbdf230b1819c:control/06_业务完成全景与更新协议.md`
- `daowei2026/observe-iterate@dc18a7251b8d433bd8c16ccd0f9cbdf230b1819c:longrun/professional/PRO_EXECUTOR_GUIDE.md`
- `daowei2026/observe-iterate@dc18a7251b8d433bd8c16ccd0f9cbdf230b1819c:longrun/contracts/LONGRUN_PROTOCOL_V2.md`
- `daowei2026/observe-iterate@dc18a7251b8d433bd8c16ccd0f9cbdf230b1819c:skills/reasonableness-analysis/README.md`

### 2.2 已接受业务成果

- D001 总报告：`daowei2026/observe-iterate@b03a3b43497fce8c10f9dd539a4f623225dce237:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D001/results/D001_EXECUTOR_REPORT.md`
- D001 material manifest：`daowei2026/observe-iterate@2b4d60f868ef715d12ba14131871227ba95517ea:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D001/results/MATERIAL_MANIFEST.json`
- D002 总报告：`daowei2026/observe-iterate@602c53c5602840d14068110a92bd90e80af6a306:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/D002_EXECUTOR_REPORT.md`
- D002 formal comparison：`daowei2026/observe-iterate@d66906a58144a190257eef4c5e45d0a4fccdddcc:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/FORMAL_LEGACY_NORMAL_CHAIN_COMPARISON.md`
- D002 QCR：`daowei2026/observe-iterate@f3645545d3f12294918832e47c8cdd2d3f4f86e9:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D002/results/QUESTION_COMPLETION_RECORDS.md`
- D002 current action designs、eligibility matrix和engineering precondition继续可作线索，但其中旧工程前置不再是强制执行顺序。

### 2.3 D003/W007 收束事实

- C0015 E1 progress：`daowei2026/observe-iterate@c9a7509ea824f4f014ba82f8a01a2d54cf94760e:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/D003_EXECUTOR_PROGRESS_C0015.md`
- Controller audit：`daowei2026/observe-iterate@64c2c923503bd86883cb39731d235dc811b42843:longrun/runs/OI-EAW-WALL-20261114-01/authority_changes/A001/CONTROLLER_STATUS_AUDIT.json`
- W007 local stage report：`daowei2026/observe-iterate@db7cc8a0c7337641017aef1b9fc980a23959dbfd:longrun/runs/OI-EAW-WALL-20261114-01/authority_changes/A001/W007_LOCAL_STAGE_REPORT.md`
- W007 ORDER：`daowei2026/observe-iterate@e788e36c8e4c18e4888f1d8a225950f51c9a695c:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W007/ORDER.json`

这些是 status/evidence 输入，不把 local report冒充 formal Worker Return。

## 3. 必须保留、不得重做或外推的结果

### 3.1 保留

- historical exact-artifact Start→BandUpdate→End normal chain；
- `EV-WALL-LEGACY-NORMAL-v1.0` 的四项 `SUPPORTS` 和同源依赖；
- 三个 accepted scoped QCR；
- D001 current working-tree静态事实和 legacy/current/schema/reader缺口；
- C0015 对 W002～W006 的限域专业接受；
- W007 已发生的时间、命令、STOP、85文件和锁事实。

### 3.2 不得重做/冒充

- 不重复扫描同一 historical chain并计作新证据；
- 不恢复或重派 W007；
- 不继续修旧 Landlock/seccomp、procfs、`/dev/null`、offline closure、global zero-write、独立 clean build或四 PASS链；
- 不把 W007 local report写成 formal Worker Return；
- 不把 current source prediction写成runtime事实或bug；
- 不把D003工程STOP写成Wall业务失败；
- 不把现有 historical `SUPPORTS` 外推到current/full suitability。

## 4. Lane A｜D003/W007 专业收束

### 4.1 目标状态

最终形成：

```text
D003 = SUPERSEDED_STOPPED_WITH_RETAINED_EVIDENCE
W007 = PHYSICAL_STOP_NO_FORMAL_RETURN / DO_NOT_RESUME
old reservation lock = RELEASED_WITH_RECEIPT
```

### 4.2 必做专业工作

1. 核对 controller audit、local report、C0015和必要的本地 manifest/hash/receipt/trace；明确哪些事实由主控核、哪些由原W1产生、哪些仍未专业接受。
2. 输出 `D003_W007_CLOSEOUT_REVIEW.md`：
   - 旧路线为何被 A001 取消；
   - W002～W006哪些专业事实保留；
   - W007哪些执行事实可保留、哪些不能使用；
   - 八EP/closure/cap/scenario哪些未发生且不再要求补齐；
   - D003最终未完成原合同但因方法变更合法停止，而不是伪装 `REPORTED_COMPLETE`。
3. 输出 `W007_EVIDENCE_RETENTION_AND_LOCK_RELEASE.md`：
   - 至少保留 W007 binding/local report/publication manifest/hashes/freeze receipt、R0-A/R0-B关键命令与trace、85原件总量/核验信息；
   - 不要求把85个文件全部搬到GitHub；记录本地精确根、保留策略和最小可审计refs；
   - 在确认 Worker终态、queue空、无执行中写者后，安排释放 holder `251010/startticks48763578/inode14806399` 和 `.D003-writer.lock`；
   - 锁释放前保存pre-state，释放后保存post-state/receipt；不得删除W007 evidence root。
4. 如果必须借助Linux动作完成核验/锁释放，签**新的**W（当前首个候选W008），引用D004和A001；它只做closeout事实/资源动作，不继续W007工程测试。
5. manager不要求补造W007 formal Return；若技术上可以只读生成新的closeout transport artifact，也必须作为新W结果返回E1，不得伪装成W007当时的Return。

### 4.3 独立性

- E1可以在closeout期间并行完成无需写Linux的M/R专业工作；
- 新Linux写动作不得在旧锁未释放时竞争同一Run writer资源；
- closeout局部问题不得无限阻断直接BASE材料工作；真实锁/单写者冲突除外。

## 5. Lane B｜新版 M：直接 BASE 观察材料准备

必须贯通或按实际需要执行 `control/02` 的0～7步；不重建阶段名。

### Step 0｜入口与资产

- 直接调查 `/dwdhome/fy/BASE_E6_2` 中已有源码、数据、构建环境、test、trace、reader、Notebook/CAEGraph及历史结果；
- 优先复用D001/D002已定位的材料和代码；
- 明确“完整图/纯数据/混合页面/需新建”的真实入口；本任务不要求为AI强制画图。

### Step 1｜处理骨架与输出双向核对

更新current真实链：

```text
WallAssembler/upstream occurrence or trace
→ Fao ingress/decode
→ lifecycle state/ledger/active/current update
→ wall_occurrences / wall_current_view / wall_diagnostics
→ actual reader/consumer/analysis material
```

逐项区分业务输入、实质阶段、业务预期输出、实现真实输出/working-state/调试状态/根本缺失项。D001处理骨架可复用，只补current BASE事实，不重抄旧报告。

### Step 2｜材料取舍

对三个父问题分别标：

```text
必需
有条件需要
可选建议
暂不准备
```

最低重新评估：

- current code/params/calendar/object/time/data binding；
- upstream sparse events/receipt/trace；
- O occurrence；
- C current-update stream；
- D diagnostics及其可关联身份；
- A full active map或等价state trace；
- terminal/replay/conflict/transaction/UTI场景；
- End measurement转换。

不得预设A和全部9场景都是本轮开工前置。缺某项若只限制一个问题，不阻断其他问题。

### Step 3～4｜方法与最小落地

- 先用现有 reader/test/trace/runner/小函数；
- 只有现有资产不足且缺项阻止当前判断时，才新增最小脚本/导出或小范围本地修改；
- 修改前保存目标文件的git status/diff/hash/mtime，确认不覆盖他人未提交改动；输出patch和回退说明；
- 不做破坏性Git、不clean/reset、不覆盖现役产物、不push正式源码；
- 不因旧D002设计存在就强制实现dedicated target、wrapper或全套evidence schema。

### Step 5｜实际取得材料

优先获得一个或多个**能精确绑定current实现**的窄窗口/小样本材料，按实际可得性包括：

- 正常 identity/lifecycle chain；
- O/C/D 同时点与upstream对账；
- current A/state trace；
- 一个或少量高区分度terminal/replay/conflict/transaction/time场景；
- existing test/controlled input或真实历史样本。

可以直接使用现有test和短窗口运行；不要求先建独立源码副本或sandbox。每次执行记录exact command、cwd、代码/参数/数据/日历、输入输出路径、退出状态、耗时/数据量和可见副作用。

禁止：未核影响的大范围/全年重算、生产覆盖、无关修改或用截图代替真实数据。显著高成本、不可逆或效果未知时停止对应动作并回E1/manager；不停止其他可继续工作。

### Step 6～7｜质量检查与交接

至少核：identity、actual/confirm/known time、data stage、source/postprocessed/display、对象/参数、空值/无事件/缺数据/历史不足/未确认、原值与转换损失。

交付真实标签只能择实：

```text
DATA_READY
PARTIAL_WITH_LIMITS
BLOCKED
```

只有计划时可用 `PLAN_READY`，但D004不能用它替代实际取数。材料包必须列能回答和不能回答的具体父问题/场景。

## 6. Lane C｜新版 R：current合理性分析

### 6.1 预期和版本

建立：

```text
analysis_round_id = AR-WALL-003
expectation seed  = EV-WALL-CURRENT-WORKING-v0.1
```

严格分开：

- `OWNER_EXPLICIT`：Owner要求观察材料准备和业务合理性分析；
- `BUSINESS_INFERRED`：维护同一Wall生命周期对identity/state/publication的业务要求；
- `IMPLEMENTATION_DERIVED`：current源码/需求规定的terminal、duplicate、transaction、UTI等行为。

探索可使用WORKING版本。正式对照前，只冻结实际材料能覆盖且不因已看结果倒写的最小子集；记录已看证据和freeze cutoff。不得修改legacy frozen v1.0。

### 6.2 证据消费

- R03/R05分别检查探索或正式证据适用性；M的`DATA_READY`不自动意味着可正式比较任何预期；
- 对每个场景使用：`SUPPORTS / COUNTERS / MISSING / AMBIGUOUS / NOT_APPLICABLE / PENDING`；
- 区分natural data、controlled test、static source、synthetic engineering test和business observation；
- 同源O/C/A/D或共享同一trace不得计成多份独立共证；
- current数据缺失时保留legacy scoped结论，但不拿legacy替current。

### 6.3 判断深度和后继

本轮至少应尽可能回答：

1. current正常链能否在真实绑定下保持identity并形成可解释O/C/D/A关系；
2. terminal/replay/conflict/transaction/UTI中哪些已有current证据，哪些只是静态风险；
3. current material/read path/转换是否足以支撑业务使用；
4. 对三个父问题分别达到支持、反证、局部适用还是有界未决。

只有正式`COUNTERS`业务影响大、可重复且有区分路径时才进入R3诊断。无须为完成流程强制诊断、调参或修代码。

形成：

- `CURRENT_EXPECTATIONS_AND_SCENARIOS.md`；
- 条件具备时 `CURRENT_EVIDENCE_COMPARISON_PACKAGE.md`；
- `ANALYSIS_DELIVERY.md` 和逐问题/子问题 `QUESTION_COMPLETION_RECORDS.md`；
- 若证据不足，准确列 `MISSING/PROVEN_UNAVAILABLE/PARTIAL` 和最小后继，不重复旧隔离工程。

## 7. Worker与授权边界

E1可以零Worker完成文档复审；实际Linux核验、锁释放、取数、短窗口运行或小范围修改通常需要新W。

### 7.1 新W身份

- 下一未占用候选：`W008`；
- worker：`codex:OI-EAW-WALL-20261114-01:worker:W1`；
- return_to：原E1；
- delegation_ref：D004当前JSON；
- 不得复用W007 order/turn/root作为新工作身份。

### 7.2 Linux grant

逐字使用A001：

```text
operation=wall-observation-work
execution_context=linux:/dwdhome/fy/BASE_E6_2
allowed_writes=/dwdhome/fy/BASE_E6_2
```

正文必须收窄实际动作：

- 默认新增中间/导出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/`；
- W007 root只读保留，除合法锁释放receipt；
- 现有BASE文件修改仅在业务必要、先核差异且不覆盖未提交修改时允许；
- GitHub只发布本Run目录；
- 禁止破坏性Git、正式源码push、生产覆盖和无关写。

主控派发前核物理thread/model/effort/cwd/single-writer和A001机械有效授权。旧W007锁、thread或资格不延续。

### 7.3 Worker边界

Worker只交执行事实/实物，不决定：

- D003是否专业关闭；
- 材料必要性和UseEligibility；
- expectation freeze；
- formal comparison；
-诊断、父问题或H3。

Worker Return先回E1；E1专业消费后再回manager。

## 8. 原生交付物和准确路径

所有GitHub新成果只发布到：

```text
longrun/runs/OI-EAW-WALL-20261114-01/delegations/D004/results/
```

### 最低交付

1. `D004_EXECUTOR_REPORT.md`
2. `D003_W007_CLOSEOUT_REVIEW.md`
3. `W007_EVIDENCE_RETENTION_AND_LOCK_RELEASE.md`
4. `DIRECT_BASE_MATERIAL_PLAN_AND_EXECUTION.md`
5. `CURRENT_MATERIAL_REVIEW.md`
6. `CURRENT_MATERIAL_MANIFEST.json`
7. `CURRENT_EXPECTATIONS_AND_SCENARIOS.md`
8. `ANALYSIS_DELIVERY.md`
9. `QUESTION_COMPLETION_RECORDS.md`

### 条件交付

10. `CURRENT_EVIDENCE_COMPARISON_PACKAGE.md`——有冻结最小预期和合格current证据时；
11. `CURRENT_DIAGNOSIS_REPORT.md`——仅正式COUNTERS值得诊断且证据足够时；
12. `ADDITIONAL_EVIDENCE_REQUEST.md`——确需跨专业、独立材料工作且不能在本D低成本完成时；
13. `BASE_LOCAL_CHANGE_MANIFEST.json` 与 `BASE_LOCAL_PATCH.diff`——实际修改BASE现有文件时；
14. 新Worker正式Return及其E1专业接受引用——实际签W时。

材料无法完整取得时，最低交付仍需准确返回可用子集、真实尝试和限制；不得伪造空manifest或fake PASS。

## 9. 接收标准

### 9.1 Closeout

- 不恢复W007；
- 明确physical STOP、formal Return缺失和E1消费边界；
- 85原件/关键证据有可审计保留策略；
- holder/lock有pre/post receipt并安全释放，或给出阻断原因；
- D003不再显示IN_FLIGHT，且不伪装原合同完成。

### 9.2 M材料

- 实际取得数据而非只有设计；
- source/code/params/calendar/object/time/data stage可追溯；
- 必需/条件/可选/不准备有业务理由；
- 现有资产优先、最小增量、真实执行和限制清楚；
- current材料和legacy材料不混版本；
- `DATA_READY/PARTIAL_WITH_LIMITS/BLOCKED`与实物一致。

### 9.3 R分析

- Owner/business/implementation来源分开；
- 正式comparison使用冻结最小预期和合格证据；
- 六类证据状态逐项；
- 静态预测/controlled evidence/natural data不混；
- D001/D002 scoped结果保留且不重复计证；
- 三个父问题各自有完成评价、限制和后继；
- `COUNTERS`可成为合格结果；无证据不能假完成。

## 10. 硬停止与结果分流

### 硬停止

- 旧W007被恢复、重派或steer；
- 需要破坏性Git、覆盖未提交改动、覆盖现役成果或push正式源码；
- 需要未授权操作/写面；
- 动作明显高成本、不可逆或效果未知且无安全停止；
- 外部动作可能已发生但回执未知；
- 材料身份/版本无法区分，继续会制造伪证据。

### 结果分流

- **Closeout完成 + material/analysis有结果**：完整回交；manager判断材料消费、current QCR和后继。
- **Closeout完成 + 材料部分**：保留可分析问题，其他限域未决；不整包失败。
- **Closeout受阻但独立取材可继续**：继续不冲突工作并报告锁/资源阻断。
- **材料取得但不能正式comparison**：交付探索事实和WORKING预期，不伪造freeze。
- **正式COUNTERS**：保留业务发现并提出是否诊断；不自行改代码。
- **现有工具确实不可执行或目标需重大改变**：形成具名Owner请求；正常缺证/返修不问Owner。

最终`EXECUTOR_RETURN`必须引用当前D004、全部真实结果、已接受Worker（如有）、remaining scope和准确后继。`REPORTED_COMPLETE`只表示D004合同完整回交，不表示父任务或三个父问题自动完成。
