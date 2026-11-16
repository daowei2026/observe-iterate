# C0005｜C0003 专业审查与材料取舍 v1

## 1. 本报告的身份与边界

- run_id：`OI-EAW-WALL-20261116-01`；call_id：`C0005`。
- manager：`chatgpt:OI-EAW-WALL-20261116-01:manager`。
- invocation token：`0234cfb5e9eb572c2c886596ad26067e`。
- business_task_id：`OI-EAW-WALL-20261116-01-BT01`；question_id：`Q-WALL-01`。
- 审查工作：`WI-WALL-SKELETON-001 / M-step-1-WALL-B001 / D001`。
- 本轮独立完成的取舍工作：`WI-WALL-MATERIAL-SCOPE-001 / M-step-2-WALL-B001`；不是新 D/W。
- 唯一分析对象：`EawP1WallLifecycleFrp`。上游仅为必要输入和处理链证据。
- analysis_round_id：尚未建立；expectation_version：`not_frozen`。

本报告接收的是原 E1 的 C0003 专业成果，不是绕过 E1 接收 W001。本调用没有读取 W001 的 FACT_REPORT、FACTS、READ_MODE 或 WORKER_RETURN 内容，没有替 E1 判断现场结果；读取 C0004 INVOCATION 仅用于核对既有原消费者和接续引用。现场事实继续等待 E1 消费。

步骤 0 始终为 Owner 指定跳过，不执行、不补验、不记完成。人工构造输入不能替代真实市场经过实际业务链的观察材料。不导入旧 Run 或 C0001 的未核完成状态。

## 2. 本轮实际采用和读取的来源

### 2.1 调用、原专业成果及当前管理投影

以下均已全文读取；长报告按原文件范围补读至结尾。

| ID | 精确来源 | 本次用途 |
|---|---|---|
| C5A | `daowei2026/observe-iterate@1f3e6eec2549d581c49272a459331d74eb3aa830:longrun/runs/OI-EAW-WALL-20261116-01/calls/C0005/FULL_ASSIGNMENT.md` | 本次完整任务；主控报告的 W001 PARTIAL、C0004 未发送和局部通信状态 |
| C5I | `daowei2026/observe-iterate@d3ab0a31f78f3623600331acdbb64d87c4424699:longrun/runs/OI-EAW-WALL-20261116-01/calls/C0005/INVOCATION.json` | recipient、call、token、assignment、origin 核对一致 |
| ERET | `daowei2026/observe-iterate@de3efaf88fc84c3a15032a3314f0aefecdae3ed6:longrun/runs/OI-EAW-WALL-20261116-01/calls/C0003/PRO_RETURN.json` | E1→本 manager；D001；IN_PROGRESS；accepted_worker_refs=[] |
| ERPT | `daowei2026/observe-iterate@54754891345bcb4f66b298cfbe2145c317e80b94:longrun/runs/OI-EAW-WALL-20261116-01/calls/C0003/PRO_REPORT.md` | ProcessingSkeleton A–G、B01–B14、MR01–MR08、G01–G06 |
| ESRC | `daowei2026/observe-iterate@298b35a68b32db01c136820bee63d82d0e630d99:longrun/runs/OI-EAW-WALL-20261116-01/calls/C0003/SOURCE_REGISTER.md` | E1 实际阅读范围、版本和未核范围 |
| EREM | `daowei2026/observe-iterate@eae3b3f64236f6661ffbc683b569c191d78652da:longrun/runs/OI-EAW-WALL-20261116-01/calls/C0003/REMAINING_SCOPE_AND_CONTINUATION.md` | 原 D 的剩余专业责任、W 原件和原消费者 |
| BIND | `daowei2026/observe-iterate@675c66a14a123f60409403030ef1a19540813430:longrun/runs/OI-EAW-WALL-20261116-01/RUN_BINDING.json` | 唯一已绑定 E1、W1；原 grants 未变 |
| ORIG | `daowei2026/observe-iterate@0c98f09538dbb8c21ba6595bbfe4dc9e1a2f8d0a:longrun/runs/OI-EAW-WALL-20261116-01/calls/C0002/FULL_ASSIGNMENT.md` | 沿用的完整接管任务与授权边界 |
| PREV | `daowei2026/observe-iterate@d3ab0a31f78f3623600331acdbb64d87c4424699:longrun/runs/OI-EAW-WALL-20261116-01/business_control/TASK_PROGRESS.md` | 发布前最新分支仍是 C0002 初始快照，尚未纳入 C0003 |
| C4I | `daowei2026/observe-iterate@d3ab0a31f78f3623600331acdbb64d87c4424699:longrun/runs/OI-EAW-WALL-20261116-01/calls/C0004/INVOCATION.json` | 已准备接续的 recipient=原 E1，origin=已有 W001 Return；文件存在不证明发送 |

C5A 是本次采用的运输状态来源，不宣称本 manager 重新核验了手机、线程、命名或网络。C0004 的准备/未发送状态是主控报告的事实，不记作一次已实际执行的专业调用。

前轮已采用的 MD001 和正式 D001 保持有效：
- `daowei2026/observe-iterate@7e994a6718748dd956781b34244298c507e2de79:longrun/runs/OI-EAW-WALL-20261116-01/business_control/decisions/MD001.md`
- `daowei2026/observe-iterate@40310127d8b700141f2ab1a17a1b114cbd1ff95b:longrun/runs/OI-EAW-WALL-20261116-01/delegations/D001/DELEGATION.json`
- `daowei2026/observe-iterate@4b918010f9ec48c48482acca066cea8e97fb5183:longrun/runs/OI-EAW-WALL-20261116-01/delegations/D001/DELEGATION.md`

### 2.2 本轮全文重读的控制与方法

以下路径均位于 `daowei2026/observe-iterate@56008df45473231c25d4ccae7f0a8c7ec599a18c`：

- `longrun/professional/PRO_MANAGER_GUIDE.md`。
- `longrun/contracts/LONGRUN_PROTOCOL_V2.md`、`longrun/contracts/longrun_schema_v2.json`。
- `control/01_L0_完整业务任务与双向衔接.md`。
- `control/02_L1_观察材料准备流程.md`。
- `control/03_L1_合理性分析流程.md`。
- `control/04_L2_节点输入输出登记表.md`。
- `control/05_三级Gate及后继路由.md`。
- `control/06_业务完成全景与更新协议.md`。

材料准备仍以 control/02 为唯一专业正文。未启动 R 专业工作，不声称本轮执行了四个 R 子 Skill。前轮其他已采用来源未被替代，也不将其表述为本轮重新全文阅读。

### 2.3 manager 针对影响后继的结论直接复核的底层原件

| ID | 精确来源 | 本轮实际阅读范围 |
|---|---|---|
| V1 | `daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13:src/Frp/Instance/ISL/Eaw/P1/WallLifecycle.hs` | 全文；批事务、终态删除、批内 ledger、occurrence/current 输出 |
| V2 | `daowei2026/frp@cac6c912dd65a14acbd591ca57e0afd8ddb4ef13:src/Frp/Instance/ISL/Eaw/P1/Publication.hs` | 原文件 625–720；实际 Wall writer 与 current 更新表注释 |
| V3 | `daowei2026/tis@ef887396e0a06d6e75be47efee0f1985ad7988a3:hf/prel0/wall_assembler_core.py` | 原文件 1090–1235；support 更新、band 发出阈值、Dormant 与 End 条件段 |
| V4 | `daowei2026/tis@ef887396e0a06d6e75be47efee0f1985ad7988a3:hf/prel0/wall_assembler.py` | 原文件 275–385；trading_day 分块调用、carry 输入输出、trace 输出 |
| V5 | `daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/01_EFFECTIVE_SCOPE_AND_REQUIREMENT_CORRECTIONS.md` | 全文；有效纠正与保留 chunk invariance 等边界 |
| V6 | `daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/dsu/P1-DSU-01_Wall_生命周期_DSU.md` | 全文；身份、转换与 producer/FRP 职责 |
| V7 | `daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/preL0_source_materials_20261102/README.md` | 全文；原文归档不新增业务要求 |
| V8 | `daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/preL0_source_materials_20261102/原文快照/mquant/ssot/eaw/03_assemblers_Wall_Build_Absorb_Attack_Exhaustion.md` | 原文件 1–105；硬边界含义、A0 输入/输出与 Dormant preset |

其余细节依赖 E1 已署名专业成果和 ESRC 的准确来源登记接收；不谎称 manager 全量重读全部底层源码，更不把两位 Pro 的同源阅读计成两份独立市场证据。以上都是固定历史版本，不是 BASE 现役、二进制或产物生成版本的核实。

## 3. 对步骤 1 的逐项审查

| 成果 | WorkQuality 与保留内容 | 可消费用途 | 不接受的扩大解释 / 剩余责任 |
|---|---|---|---|
| A–G ProcessingSkeleton | 有实质输入→形成变化→发布→typed ingress→事务→正式回读链；职责与来源清楚，来源级成果合格 | 步骤 2 判断材料种类、需保留的信息及语义损失；定向形成后继事实问题 | 不升级为 BASE 现役链已贯通。G01–G03 未由 E1 消费闭环，步骤 1 整体仍为部分完成 |
| 输出角色表与 B01/B10/B12 | V1–V3 直接支持 occurrence、current update、active map 和 producer state 的区分 | MR02/03/05/06 的需求口径；避免错误重建或对照 | 不接受 current 更新表等于全量快照、producer dense 等于 FRP current，或更新数少就是丢事件 |
| B02/B03 身份与转换 | V6 明确 run 身份加 local no、保持同 life 与不重认墙；V1 支持状态转换范围 | namespace、原 occurrence、前序状态与显示边界必须保留 | 具体 producer artifact/ppid 未经现役核验，不得跨实例按 local no 合并 |
| B04/B05 终态与去重 | V1 明确 End 删除 active entry、ledger 每批重置；E1 的保护范围描述有据 | 保留为实现能力边界与真实材料中待核的检查点 | 不接受“已发生终态重用/跨批冲突”的市场结论；也不因存在错误构造器就认定永久终态防护 |
| B06/B07 同拍引用 | E1 明确引用不含 ordinal 与潜在同拍碰撞，且没有声称实际发生 | 保留 physical key、batch/row、原列表顺序、UTI/ref 的要求 | 不把潜在路径写成必现缺陷；不得预先按 ref 去重或以排序修复覆盖原输入 |
| B08/B09/B11 拒绝、原因和缺失 | V1 支持全批回滚，其他 ingress/payload 细节以 E1 已读来源为依据 | 同时取得输入、三路输出和加载/失败说明；不能仅看空表或诊断计数 | 不接受无诊断即无失败、没有 key 即 valid empty、reason_code 未核即补原因名字 |
| B13 与 G05 | 接受为具名来源/语义待核，不接收为已裁定需求违规 | 只限制依赖争议条款的预期/解释，不阻断其余材料需求 | 见 §4；不要求 Worker 裁决业务权威，不因该项停掉全部工作 |
| B14 与脚本边界 | E1 已区分 Cal/Cache、.run/.F 与 to_df；flags/计数/少量样例不足以验收正式包 | 后继只核真实读取模式和缺项，不凭退出码确认成功 | W001 的实际读取可用性尚待 E1；输入脚本历史成功不作本 Run 回执 |

**合并结论：**C0003 的来源级骨架、角色、双向核对及已限定的风险线索可以限域接收，足以完成材料类别与必要信息的取舍；D001 的现场闭环与 Worker 消费尚未完成，不能认定 D001 或整个步骤 1 已通过。此结论不依赖 W001 的未消费内容。

## 4. manager 对 G05 的进一步专业判断

V8 的默认 reset 针对“硬边界”，理由是跨长停市延续微观对象的风险；V5 同时要求保留 chunk invariance；V4 明确存在按 trading_day 分块且传递 carry 的实现。

因此必须分清：

1. 纯技术 chunk 切分；
2. 交易日、Session 或长停市这种业务边界；
3. 当前采用合同到底把哪类边界定义为必须结束/reset。

**仅凭“有 carry”不能推导任意技术分块都应 reset，也不能证明实际长停市边界一定被错误延续。**另一方面，现有读取也没有找到足以宣告所有业务硬边界都获准 carry 的逐条权威裁决。`allow_brick_join_dormant` 的归档 False 与 E1 报告所读实现 True 差异仍保留，不从实现自行推出业务已批准。

G05 在本轮的处理：不提升归档为新要求，不立即修码，不要求全量追溯；在后续确需使用对应边界/休眠续接场景作判断时，定向确定有效条款、真实边界和行为。取得明确证据前，该争议只限制相关预期/结论，不作为整个步骤 2、所有观察材料或 D001 专业报告可提交性的总阻断。

## 5. MaterialRequirementSet｜MRSET-WALL-v1

### 5.1 用途及证据等级

本节由 E1 MR01–MR08 候选和上面已可消费的源码级骨架形成，是本 manager 本轮实际完成的材料取舍成果。正式接受范围由后续 MD002 指定；本报告不引用未来决定作为来源。

要回答的是 Q-WALL-01：真实市场经实际链后，该生命周期输出能否在明确条件下可信表达墙身份、变化和当前状态。以下要求定义“需要什么、为何需要”，**不证明文件已经取得或可运行路径已存在**。具体对象/参数/观察窗口仍以真实绑定和后续方法/落地选择为准，不把 I03 的整段日期自动规定为必须全量取数。

| 材料 | v1 取舍与理由 | 最小内容与核对重点 | 来源入口 / 当前未满足事项 |
|---|---|---|---|
| MR01 来源与实例 manifest | **必需**；没有它无法知道同名墙属于哪次实际处理 | 顶层及 source 的实例/参数、ppid/artifact/receipt、已知生成版本与实际加载版本分别记录、相关工作树差异、schema/binary 证据等级、品种/日历/数据源及时间覆盖 | ERPT/ESRC 的历史入口；现役 G01/G02 待 E1。只保留本对象实际路径，未知 provenance 记 unknown，不为填字段建 clean-build 工程 |
| MR02 正式三路输出 | **必需**；直接判断 lifecycle 的接纳、状态更新与拒绝 | 所选范围 wall_occurrences、wall_current_view、wall_diagnostics；原 ADT 字段、外层时间/批边界、列表行序与实际基数；加载失败或未形成输出须另记 | V1/V2 与 E1 的 wrapper 线索；实际 schema/路径/内容待 E1。已核实“无诊断事件”可按事实交付，不要求伪造非空诊断；缺 key/读失败不能当零错误 |
| MR03 同源 producer 稀疏输入 | **必需**；分清 producer 发布、ingress 拒绝及 DSU 接纳 | 同 source 的物理 rows、keys/ordinal、local no、ref、UTI/时间、事件码、状态、价带及实际保留原因；保留 source 到正式输出映射 | ERPT B01/B02/B06–B09；G02/G03 待消费。禁止先去重、静默改时间或取另一个 producer 的结果冒充同一输入 |
| MR04 市场与时基最小参照 | **必需最小参照**；生命周期不能脱离真实市场与输入有效期解释 | 同品种/日历的 last、bid/ask、tick_size、原时间到 UTI 的可解释关系、必要量和可用性；所选范围的夜盘/交易日与缺口说明 | ERPT A/T05；实际绑定待核。认墙、支撑、休眠或 End 成因判断若依赖 QT/量/门槛，相关实际值与生效时点立即成为该判断必需项，不以“条件材料”免除 |
| MR05 窗口起点与 life 边界 | **必需**；防止截窗伪出生、伪结束、空状态初始化 | 完整 life，或可信起点状态及其后更新，或可覆盖起点的前序历史；运行边界/显示边界/业务 End 分开；未闭合墙单列 | V1/V6 与 ERPT B10；G04 尚未关闭。上述是可替代满足方式，不要求同时建设三套。无 seed 时限定可解释墙/时段，不假设空 map |
| MR06 dense/判定中间量 | **有条件需要**；只在解释具体差异时取最小区分证据 | 当 sparse/current 与市场或 dense 差异影响判断、或需定位认墙/休眠/End 成因，复用同源 trace、局部支撑/薄触/距离等 | V3/V4 与 ERPT MR06；不默认全历史 dense，不自动加 debug/重算。触发后为该问题必需，取不到要保留未决和影响 |
| MR07 图或 CAEGraph | **可选建议**；用于定位与联看而非替代数据 | 如实际需要图，分别标注 producer、FRP、事件、诊断图层及原值/显示值；需要视窗最终值时另核回调与范围 | 目前没有已验图。纯数据能满足用途时不强制画图；一旦采用依赖图的观察方法，必要图层/视窗核验不能再按可选略过 |
| MR08 本轮不准备 | **暂不准备/明确排除**；避免扩大对象与替代证据 | 不准备合成市场替代品、其他 P1 产品独立全链、全资产盘点、通用 revision 平台、盲调参数或无用途全量新算 | Owner/ORIG、V5/V6；普通有界真实取数并未被排除，后续只按实际动作、成本和授权组织 |

### 5.2 不能从这份取舍推出什么

- MR01–MR05 的必要性已可判断，但它们在现场是否存在、当前样例能回答多少、是否需补材料仍未知。
- 不把 MRSET-WALL-v1 标为完整 MaterialPlan 的 PLAN_READY；步骤 3 的字段/时间/转换方案和步骤 4 的实际入口尚未完成。
- 不把“文件有”“脚本退出 0”“Worker PARTIAL”“少量记录可读”换算成 DATA_READY 或 PARTIAL_WITH_LIMITS 的正式市场材料交接。
- 不要求所有源码潜在边界都在市场样本中必然发生；真实未出现应如实记未覆盖，不能用合成测试填成已观察。
- 生成版本 unknown 不自动意味着全部数据不可用，也不自动放行。E1 要说明可建立的源/产物关联与仍受限制的具体判断，manager 再按用途决定。

## 6. 实际依赖与独立工作判断

| 工作 | 是否依赖 W001 尚待消费结论 | 本轮处理 / 下游条件 |
|---|---|---|
| 源码级步骤 1 的接受范围 | 否 | 本报告已实质审查；由 MD002 限域决定 |
| 材料类别、必要信息、条件材料触发 | 否 | 已完成 MRSET-WALL-v1；manager 在本轮接受，不另派一个重复整理 D |
| G05 权威与边界解释 | 否（本次已做的来源澄清部分） | 已作 §4 限定；未假装有效业务边界/现场行为已确定 |
| 完整现役 ProcessingSkeleton | 是 | 原 E1 消费 W001 的 G01–G03 后给出现役/不同/未核对照 |
| 步骤 3 的具体字段/时间方法、步骤 4 的可执行入口 | 部分依赖 | 语义约束已明确；实际 schema、路径、顺序/时基及加载副作用待原 E1。不能把历史字段直接当现役已验入口 |
| R01/R02 仅依赖文档的事实整理/最小预期 | 业务上不必等待 W001 或 M 全部结束 | 在原目标内具有独立输入潜力，但本轮未执行对应 Skill/未产出 R 原生结果，不计已启动。当前只绑定且可承接执行任务的是通信受阻 E1；给同一 E1 增发 D 不消除通道阻碍，暂不重复排队 |
| R03/正式 R05–R06 | 是，且另缺合格材料/预期 | 无实际材料使用资格，无冻结预期，不启动 |

不新增 D 的理由是：本轮能独立完成的取舍审查已完成；原 D001 的现场结果仍有唯一原消费者；并不存在一个已绑定、已确认可收件的第二执行人供本轮新 D 立即独立推进。不是认定全部业务工作都依赖 W001，也不是要求 Owner 重新批准普通工作。若后续真实新增/恢复可用收件能力，可以依据上述独立输入另作安排。

## 7. 给原 E1 的剩余专业输入要求

仍在原 D001 范围内，不新签 W：消费既有 W001 及原证据，逐项记录接受/限域/拒绝；区分生成版本、现役加载版本和历史文档版本；逐项更新 G01–G04 的实际答案，不能凭 PARTIAL 二字判为全部无效或全部完成。

E1 应交回：影响骨架的具体差异；三路真实 key/schema 与读取能力；source/实例/时间与 seed 的已知和未知；每项缺失是未查、读失败、确实不可得还是仅限观察范围；MRSET-WALL-v1 哪些仍适用、哪些须调整及原因；是否需要新动作以及其准确最小 I/O。没有新事实不重派 W001、不改造成另一个 ID 重做同件事。

G01–G03 的调查允许得出准确的不可得结果；这可结束相应调查，不等于所需材料已满足。若 E1 已消费后仍缺关键输入，应提交具名限定结果而不是无限等到所有字段齐全。manager 再决定步骤 1 的进一步接受、步骤 3/4 的合法工作及真实材料路径。

## 8. 本次未声称的完成

没有 W001 专业接受、D001 完成、M 正式材料取得/交接、R 预期冻结或正式对照、H1/H2/H3 通过。父任务保持 incomplete。下一项实际专业接续仍是主控恢复原 E1 通信后，将既有 W001 结果送回原 E1 消费；局部恢复不改变目标、授权、方法版本或原消费者。