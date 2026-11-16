# D001｜核实 Wall 生命周期实际处理骨架与输出，形成观察材料取舍依据

## 1. 委派身份与原结果消费者

- run_id：`OI-EAW-WALL-20261116-01`
- delegation_id：`D001`
- issuer_call_id：`C0002`
- issuer / return_to：`chatgpt:OI-EAW-WALL-20261116-01:manager`
- recipient：`chatgpt:OI-EAW-WALL-20261116-01:executor:E1`
- 发行调用 token 关联：`42f36c785f9fe8c352c0897d54c2ebee`。这是 manager C0002 的 token，不代替主控为执行人实际调用生成的身份。
- parent_task_id：`OI-EAW-WALL-20261116-01-BT01`
- question_id：`Q-WALL-01`
- work_item_id：`WI-WALL-SKELETON-001`
- Workflow：M 观察材料准备。
- 当前正式工作：`M-step-1`；stage_instance_id=`M-step-1-WALL-B001`。
- 可随本 D 提交：步骤 2 的材料取舍候选，不冒充已被 manager 接受的步骤 2 成果。
- analysis_round_id：尚未建立；expectation_version=`not_frozen`。

管理决定原件：
`daowei2026/observe-iterate@7e994a6718748dd956781b34244298c507e2de79:longrun/runs/OI-EAW-WALL-20261116-01/business_control/decisions/MD001.md`

原专业消费者是本 Run manager：先消费 ProcessingSkeleton 和输出核对结果，决定步骤 1 的接受范围及材料取舍；随后由步骤 2～4 的工作消费这些已接受事实。**本 D 不直接把未经接受的取舍交给步骤 5 整批执行，更不直接向 R 交付正式合理性结论。**

## 2. 本 D 要解决的业务问题

唯一分析对象是 **EawP1WallLifecycleFrp**。父问题关注真实市场数据经实际业务处理链后，输出能否可信表达墙的身份、生命周期变化和当前状态。

本 D 先回答：

> 对这个对象，实际输入是什么，哪些实质处理会改变墙身份、事件资格、状态或发布结果；业务要求提供的信息，与实际内存输出、正式落盘结果和 Python 可读结果分别是什么关系？要开展后续真实市场观察，哪些材料确有必要，哪些信息当前缺失？

不能只复述输入文档或按函数数量列源码。必须把“输入→判断/更新→输出→下游怎样使用”讲清，并把业务预期、历史指定实现、现场现役事实和未核实内容分开。

SubContinuousContract、VolQuant、WallAssembler、WallOccurrenceFao 仅在说明本对象输入、处理链和证据所必需的范围内查证，不扩成各自的独立合理性分析任务。不得顺便调查 EawBattleP 其他产品或重建全平台资产目录。

## 3. 精确输入与采用方法

### 3.1 授权、首次接管与绑定

- `daowei2026/observe-iterate@55303ab99aeb349ddf9ffde7a375ca241b29d0f6:longrun/runs/OI-EAW-WALL-20261116-01/OWNER_START.md`
- `daowei2026/observe-iterate@675c66a14a123f60409403030ef1a19540813430:longrun/runs/OI-EAW-WALL-20261116-01/RUN_BINDING.json`
- `daowei2026/observe-iterate@0c98f09538dbb8c21ba6595bbfe4dc9e1a2f8d0a:longrun/runs/OI-EAW-WALL-20261116-01/calls/C0002/FULL_ASSIGNMENT.md`
- `daowei2026/observe-iterate@000b5bd6731c3bc51dc2274f127b880045391b7e:longrun/runs/OI-EAW-WALL-20261116-01/controller/OWNER_EARLIER_RESUME.md`

本 Run 从 C0002 首次实际接管开始。旧 C0001 的 UNKNOWN 运输历史保留但已显式替代；不接受它或旧 Run 的未核完成状态。

### 3.2 三份特征输入

- `daowei2026/observe-iterate@56008df45473231c25d4ccae7f0a8c7ec599a18c:task-inputs/eaw-p1-wall-lifecycle/无二义性需求和实现文件.md`
- `daowei2026/observe-iterate@56008df45473231c25d4ccae7f0a8c7ec599a18c:task-inputs/eaw-p1-wall-lifecycle/设计文件.md`
- `daowei2026/observe-iterate@56008df45473231c25d4ccae7f0a8c7ec599a18c:task-inputs/eaw-p1-wall-lifecycle/实例运行脚本.py`

以上已被接受为**调查入口**，不是现役组合已可运行或本 Run 市场材料已准备好的证明。禁止使用已删除的 FEATURE_CONTEXT.md。

### 3.3 必须实际采用的专业来源

- `daowei2026/observe-iterate@56008df45473231c25d4ccae7f0a8c7ec599a18c:longrun/professional/PRO_EXECUTOR_GUIDE.md`
- `daowei2026/observe-iterate@56008df45473231c25d4ccae7f0a8c7ec599a18c:control/02_L1_观察材料准备流程.md`
- `daowei2026/observe-iterate@56008df45473231c25d4ccae7f0a8c7ec599a18c:control/04_L2_节点输入输出登记表.md`
- `daowei2026/observe-iterate@56008df45473231c25d4ccae7f0a8c7ec599a18c:control/05_三级Gate及后继路由.md`
- `daowei2026/observe-iterate@56008df45473231c25d4ccae7f0a8c7ec599a18c:longrun/contracts/LONGRUN_PROTOCOL_V2.md`
- `daowei2026/observe-iterate@56008df45473231c25d4ccae7f0a8c7ec599a18c:longrun/contracts/longrun_schema_v2.json`

材料准备唯一专业正文是 control/02。步骤 0 为 Owner 指定跳过，**不执行、不补验、不记完成**；直接做步骤 1。缺某项真实入口只定向核实该项，不借此恢复全面资产盘点。旧 S0～S5/M05/G-RUN 不构成另一条专业执行链。

本 D 不激活 R 的正式预期、证据对照、诊断或标定 Skill；不要为了填全节点而先给合理/不合理结论。必要的业务需求来源核对仍属于步骤 1 的双向核对，不等于完成 R1。

## 4. 专业执行内容

### 4.1 核对真实职责和有效需求，而非默认整理文档全部正确

从三份输入定向跟读影响本对象的需求和实现原件。优先核对有效需求纠正、Wall 生命周期 DSU、正式输出合同以及实际执行入口；遇到冲突保留冲突双方的精确来源及影响，不自行把历史归档升级为新需求。

输入提供的历史基线为 TIS `ef887396e0a06d6e75be47efee0f1985ad7988a3`、FRP `cac6c912dd65a14acbd591ca57e0afd8ddb4ef13`、需求仓 `8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f`。它们只说明可读历史依据，**不预设与 BASE 的现役 checkout、codegen、二进制和已有物化数据一致**。

聚焦如下实质链条，若源码证明不一致就按实际修正：

`行情/阈值参照 → WallAssembler 形成变化 → receipt/物理 occurrence 流 → WallOccurrenceFao 解码与诊断 → maintainWallLifecycle 状态维护 → occurrence/current update/diagnostics 正式发布 → Python 读取`。

### 4.2 建立可被后续材料选择消费的 ProcessingSkeleton

每个实质阶段至少列出：输入业务对象与字段/时间、关键判断或状态变化、输出角色、身份连续性、错误/空值语义、下游消费者、准确源码/需求依据、为何值得观察及缺它会阻碍什么。

需要特别查清而不能由名字猜测的边界：

| 边界 | 本 D 所需核对 | 对后续观察的影响 |
|---|---|---|
| producer 与 lifecycle | 谁形成 Start/BandUpdate/StateChange/End，谁只恢复类型和维护状态 | 避免把认墙阈值的效果错误归到 FRP 新算法 |
| 输入资格与批次 | receipt/字段错误、逐行解码、同 firing 成败、状态事务的真实边界 | 无正常输出究竟是无事件、输入拒绝还是状态拒绝 |
| 身份与时间 | source/run namespace、wall local no、occurrence ref、同 UTI 多变化、行序与业务序 | 防止跨运行同号混用、同拍丢事件或虚构先后 |
| 状态转换与终态 | Present/Dormant/Ended、更新合法性、End 删除、跨批重复/迟到的保护范围 | 区分已实现保证、依赖 producer 的前提与未覆盖情况 |
| 输出角色 | 内存 active map、完整 occurrence、批内每墙最后 update、诊断以及 writer 表 | 不把增量表读成全量快照，不把压缩后的 update 数当事件数 |
| Python 回程 | 默认包装、generated ADT schema、实际 .run()/.F 读取路径 | 不把历史 to_df 抛错或 Cal/Cache 差异直接判为本轮运行失败 |

这些是问题清单，不是要求逐项造异常输入或开发新测试平台。U-01～U-10 亦仅作缺口线索；应说明哪些影响当前材料选择，哪些只能留给后续有据诊断。

### 4.3 必要时定向核实 BASE 的现役事实

仅为回答上述链条与读取入口的具体未知，核实相关仓库实际提交/工作树差异、加载模块位置、既有 wrapper/schema、对应实例 ppid/参数、source receipt 和 fields 等。已有真实记录可作少量字段/时间/输出角色核对，不要求为这一事实核查重新跑完整市场链。

现成脚本的候选上下文是 `TA_updto20240229_DBA / rb / night_end_at_2300 / 2020-12-01～2021-02-22 / 默认实例`；在现场核实前只记为候选运行绑定。必须保留脚本“未命中已有 fields.json 即停止长窗自动补算”的约束。脚本捕获异常，不能凭退出码判成功；历史成功说明不作本 Run 回执。

本 D 不要求调用该长窗口脚本。只有对本次未明事实确有帮助、已核实不会触发长窗口补算或覆盖现役成果时，才可在 W 中使用既有读取路径。复用脚本须使用本 Run 独立输出位置，避免覆盖旧报告，保留来源及任何路径性改动；不得以修改守卫来强迫运行。三路计数及少量样例只证明其明确核实范围，**不能交成完整观察数据包**。

源码/metadata 已足够的部分可以先交，不得因为某个现场事实需要 Worker 而把全部专业工作搁置；现场未知必须如实留给后继。

### 4.4 可附带材料取舍候选，但不自行启动其下游

在已经核实的骨架上，提出 `MaterialRequirementSet` 候选：逐项说明要回答的问题、必需/有条件需要/可选建议/暂不准备、可用源、缺口影响及条件材料触发点。优先把同一次真实运行可满足的需求放在一起，不按函数/图元/材料数量机械拆 W。

候选应具体讨论生命周期三路正式输出、用于解释墙状态的必要市场参照、输入 occurrence 与诊断的对应；上游细粒度 trace 只在确实影响当前判断或特定异常解释时纳入。是否需要 CAEGraph、纯数据或特定视窗值由用途决定，不强制造图，也不能凭静态定义声称已有图。

本 D 的步骤 2 候选须回 manager 接受。未被接受前不开展步骤 3～5 的整批规划执行，不把候选中的“可选”用来取消父任务必需证据。

## 5. 原生交付与验收

可把以下内容组织在一份完整专业报告及必要附表中，不要求机械生成同样数量的文件。

1. **ProcessingSkeleton**：业务输入、实质阶段、真实输出/状态及消费关系；每项有精确依据，历史与现役证据分开。
2. **输出双向核对表**：业务预期信息 vs 内存/落盘/Python 实际信息；一致、额外中间结果、需要但未提供、语义/时间不一致及其影响。来源不充分处保留未决，不能由实现反证或证明需求本身。
3. **已核事实与缺口**：读了哪些底层原件，现场核实了什么；对象/时间/参数/代码/数据绑定；未核实项和最小后继。未取得的数据版本、二进制来源、历史产物版本不得补造。
4. **材料取舍候选（有充分依据时附带）**：为何准备、具体用途、候选来源与最小缺口；明确候选状态。
5. **专业消费记录**：有 W 时逐项对应工单、实际回执/产物、接受或限制范围、剩余/在途 W；零 W 时明确无需 Worker 的理由和仍未核现场范围。
6. **准确回交**：按 M-step-1 及候选步骤 2 分开报告，不以“D 做过”代替成果验收；说明 manager 可接受什么、仍需查什么、下一项具体输入依赖。

D 完成报告的条件：已对实际取得的来源完成本问题的专业分析，给出足以供 manager 判断材料需求的骨架和差异，或对关键不可得给出准确失败/已尝试/影响及恢复条件；所有已派 W 均有清楚消费或在途说明。关键事实不足时应报告 PARTIAL/未完成范围，不能用笼统“已理解”宣称全部完成。

即使本 D 可以 `REPORTED_COMPLETE`，也只表示此委派范围的专业报告完成，不表示 M、R、父任务或真实市场运行已完成。没有真实材料时不报 DATA_READY；步骤 2～4 尚未完成也不要把整个材料计划报 PLAN_READY。

## 6. Worker 边界与操作授权

可进一步下放的操作类别限于 Binding 原有 `wall-observation-work` 和 `run-record-publish`，分别对应下列 Owner 原文；本 D 的专业内容限制继续适用：

```text
operation=wall-observation-work execution_context=linux:/dwdhome/fy/BASE_E6_2 allowed_writes=/dwdhome/fy/BASE_E6_2
operation=run-record-publish execution_context=github:daowei2026/observe-iterate:runs/OI-EAW-WALL-20261116-01 allowed_writes=longrun/runs/OI-EAW-WALL-20261116-01
```

- 优先读取 BASE 既有源码、数据和环境；本 D 所需新增调查脚本、报告和导出只放 Run 专属非正式产物目录，如 `.runtime/observe-iterate/OI-EAW-WALL-20261116-01/D001/`。这只是避免覆盖的产物目录，不是另建隔离工程。确需其他普通运行辅助写入时，W 须明确实际位置及必要性并仍落在 grant 内。
- GitHub 仅发布本 D 的专业结果、执行人实际调用回交及其合法 W/Worker 结果到本 Run 前缀；不修改 Owner、Binding、controller 事实、manager 决定、TASK_PROGRESS 或别的委派原件。
- 不授权改业务需求/算法/参数实例、覆盖既有正式产物、破坏性 Git、长窗口自动补算、参数搜索、新建复杂隔离构建或其他无关工作。
- 不以人工构造输入替代真实市场链。本 D 主要是事实核对，不安排合成用例作为首轮观察成果。
- 真正高成本或不可逆动作先停止该动作，返回必要性、成本/影响及精确后继给 manager；无需为普通低风险读取新建独立 Gate 或向 Owner 逐项申请。

只有 E1 可以给已绑定 W1 签 W。主控在首次 W 前独立核实 Linux 工作区实际路径、单写者、物理线程和 `GPT-6.1 Sol Max` 配置；Pro 环境采用 Project `细节叙事生成_金标`、档位 `Pro`。这些是待主控实际核验的要求，不是本 D 自述已经核实的事实。

## 7. 各结果的回路与禁止事项

- 充分：回原 manager 验收步骤 1，并决定材料取舍及步骤 3～4/实际取材后继。
- 部分：保留已核骨架，只列影响后继的具名缺口，不要求从步骤 0 重来。
- 来源不可读/环境缺失：报告精确仓库、commit、path 或现场路径、失败信息、已尝试及所需原文；不凭摘要假称读过。一次读取失败不等于永久不可得。
- 动作结果未知：先请主控核实原动作与回执，不重复派相同动作。
- 新业务冲突：提交事实和选项给 manager；普通取舍仍由 manager 在 GO 内决定，不把所有未知扔给 Owner。
- Worker 结果必须先回 E1 专业消费，再由 E1 回 manager；不得直接让主控把 Worker EXECUTED 当成步骤验收。

使用正式 `longrun-professional-return/v2`，role=executor，delegation_ref 指向本 D 随后发布的**实际 JSON 精确引用**，return_to 为本 manager。需要 W 时先发布 W 原件再在后续 commit 引用；剩余工作和合法续作必须明确。主控为实际执行人调用提供新的 INVOCATION，不能沿用本 manager 的 C0002 当执行人 call_id。

本正文仅记录 issuer_call_id，不引用未来 manager Return 或自己的未来 commit。D001 的 GitHub 发布不等于物理送达；派发与回执由主控核实。
