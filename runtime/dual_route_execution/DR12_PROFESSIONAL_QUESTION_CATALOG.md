# 市场过程特征：固定专业问题与完整原文入口

修订：2026-09-18-question-work-v2。任务组织候选；题面、输入输出合同和结构检查已定义，实际长程效果须另行试跑。适用于本领域的不同用例，不预装 EAW、U2/U3 的对象、分包、阈值、路线配额或轮数。

## 0. 使用规则

本文件把已有 A/B/C 和 DR 的专业要求组织成可投递的问题。题面供明确委派，完整 reference 决定细节；不得只看本页就声明专业方法已读。管理者先按 [DR13](DR13_WORK_ARRANGEMENT_AND_CONTEXT.md) 绑定真实工作，再按 [DR14](DR14_QUESTION_WORK_CONTRACT.md) 交清结构化定位和接续。题号不授予模式、写权、阶段资格；一题可跨轮，数题可在同一合法模式中联动。没有某种业务复杂度就不创造对应实体；不适用须有具体业务依据，暂未处理仍保留为义务。

每次实际任务引用本文件相应锚点、下列原文的 repo/path/heading 以及实际采用的 exact commit。表中章节为重点回读位置；profile 中其他适用的完整必读内容仍需取得。首次读完整方法，同题续作按 DR13 §6 复用有效阅读。不能因缩上下文丢掉相邻合同，也不能把索引或阅读回执当成使用证明。

### 源文件定位规则

下列 S 编号只在本文件定位，不是新材料权力。路径相对于 `agent_evolution/agent_candidates/`，点击即可到正文；实际交接必须展开为完整仓库根路径并绑定同一方法版本。一个引用包含：完整路径、确切章节标题或范围、为何用于本题；不得只写“读 A/B 材料”。本版从 `742d0c5c58d214fa280153de5286ac476d8594c8` 对账，后续修订只对受影响引用重核。

|源|完整正文位置（相对于 agent_candidates）|重点定位|
|---|---|---|
|S01|[A/TASK_ROUTER](../market_process_modeling_contract_pro_candidate_v0_2/TASK_ROUTER.md)|§§1–9及 V0.2 router additions：对象、mode、写权、横切与结构回图|
|S02|[A/WORK_MAP_PROFILE](../market_process_modeling_contract_pro_candidate_v0_2/profiles/WORK_MAP_PROFILE.md)|§§2–8；V0.2 mandatory analysis、完成门|
|S03|[A/建图完整方法](../market_process_modeling_contract_pro_candidate_v0_2/references/work_map/WORK_MAP_CONSTRUCTION_METHOD_FULL_REFERENCE.md)|Scope Lock、过程分类、候选边界、四项组合性挑战、多视图、覆盖地图及 V0.2 Feature Narrative/Source→Fact→Feature|
|S04|[A/LOCAL_CONTRACT_PROFILE](../market_process_modeling_contract_pro_candidate_v0_2/profiles/LOCAL_CONTRACT_PROFILE.md)|§§2–9及 V0.2 mandatory outputs、当前方法五态、完成门|
|S05|[A/局部合同完整方法](../market_process_modeling_contract_pro_candidate_v0_2/references/local_contract/LOCAL_BUSINESS_CONTRACT_REFINEMENT_METHOD_FULL_REFERENCE.md)|§2入口/完成，§3三种循环，§4动作拆分/停止，§5典型动作，§6 D0–D6，§7 S1–S3，§§8–12运行/历史/knownness/产品，§16回图；末尾 V0.2 Feature形成/回看/最低充分表达/Case/探针补充|
|S06|[A/方法与参数完整参考](../market_process_modeling_contract_pro_candidate_v0_2/references/local_contract/METHOD_AND_PARAMETER_SURFACE_REFERENCE.md)|§1七类元素、§2方法位置、§3稳定输入输出/不变量/当前选择/替代与失败、§4首版、后续 RulePack/控制器及外围过程|
|S07|[A/Owner与工程自由](../market_process_modeling_contract_pro_candidate_v0_2/references/local_contract/OWNER_GATE_AND_ENGINEERING_FREEDOM_REFERENCE.md)|Owner Gate、可逆首版、业务等价工程自由；沉默不批准|
|S08|[A/探针与横切重扫](../market_process_modeling_contract_pro_candidate_v0_2/operations/IMPLEMENTER_PROBE_FINDING_DISPOSITION_AND_CROSS_CUT_RESCAN.md)|§§2–9：输入、完整生命走读、finding分类、Pro处置、受影响面、re-probe、审查区别、完成限制|
|S09|[A/MAP_REVISION_PROFILE](../market_process_modeling_contract_pro_candidate_v0_2/profiles/MAP_REVISION_PROFILE.md)|完整入口、受影响多视图、回图候选、原写权与正式应用边界|
|S10|[A/独立审查入口](../market_process_modeling_contract_pro_candidate_v0_2/profiles/INDEPENDENT_AUDIT_PROFILE.md)；[A/Harness](../market_process_modeling_contract_pro_candidate_v0_2/references/local_contract/CONTRACT_REFINEMENT_HARNESS_CANDIDATES.md)|按实际声明选检查，复做承重判断和 anti-gold；不得 Builder 自签|
|S11|[A/旧成果影响](../market_process_modeling_contract_pro_candidate_v0_2/operations/EXISTING_ARTIFACT_EFFECT_AND_RETROFIT_DECLARATION.md)|§§1–5：FUTURE_ONLY/REAUDIT/RETROFIT/下游重基，局部处置与禁止|
|S12|[A/正常材料读取](../market_process_modeling_contract_pro_candidate_v0_2/references/material/NORMAL_RUNTIME_SOURCE_PROFILE.md)；[A/材料与repo合同](../market_process_modeling_contract_pro_candidate_v0_2/references/material/MATERIAL_PLACEMENT_AND_REPO_READ_CONTRACT.md)|默认稳定内容、任务packet、完整方法激活、raw/repo触发、source-use；读取周期按 DR13 §6|
|S13|[B/选择器](../repo-aware-engineering-agent-candidate-v0.2/00_front_door/02_PROFILE_SELECTOR_AND_READ_ORDER.md)|Need/Select/Required hot reads/Stop；v0.2 Compiler读取顺序|
|S14|[B/RepoFact完整方法](../repo-aware-engineering-agent-candidate-v0.2/10_methods/02_REPOFACT_INVESTIGATION_FULL_REFERENCE.md)|当前事实调查、direct/inference/candidate/gap、冻结 S0|
|S15|[B/工程编译完整方法](../repo-aware-engineering-agent-candidate-v0.2/10_methods/03_ENGINEERING_COMPILATION_AND_REALIZATION_FULL_REFERENCE.md)|Current canonical method contract；B-R3编译循环、目标工程、工程自由、任务生成与返回|
|S16|[B/Feature realization](../repo-aware-engineering-agent-candidate-v0.2/10_methods/11_FEATURE_STATE_METHOD_REALIZATION_COMPILATION_V0_2.md)|§§1–3输入/事实；§§4–9业务到宿主/最低充分表达/状态/方法/物化/正式链；§10任务；§11 Owner工程图；§12完成/返回|
|S17|[B/VCC与Owner审查](../repo-aware-engineering-agent-candidate-v0.2/10_methods/04_VCC_EXECUTION_COMPILATION_AND_OWNER_REVIEW.md)；[父包连续性](../repo-aware-engineering-agent-candidate-v0.2/10_methods/05_ACCEPTED_PARENT_CONTINUITY_FULL_REFERENCE.md)；[消费回压](../repo-aware-engineering-agent-candidate-v0.2/10_methods/07_CONSUMER_BACKPRESSURE_MATERIALIZATION_FULL_REFERENCE.md)|完整工程→可执行任务；accepted parent原位；反馈分类与正文消费|
|S18|[B/事实Harness](../repo-aware-engineering-agent-candidate-v0.2/40_harness/10_REPOFACT_HARNESS.md)；[B/工程Harness](../repo-aware-engineering-agent-candidate-v0.2/40_harness/20_ENGINEERING_COMPILATION_HARNESS.md)；[B/连续性回压](../repo-aware-engineering-agent-candidate-v0.2/40_harness/30_CONTINUITY_BOUNDARY_BACKPRESSURE_HARNESS.md)；[B/材料读取](../repo-aware-engineering-agent-candidate-v0.2/40_harness/40_MATERIAL_REPO_READ_CONTEXT_HARNESS.md)|按当前题、claim和finding选中检查，不每轮全载|
|S19|[C/当前执行](../mission-c-host-implementation-system-candidate-v0.2/CURRENT_EXECUTION.md)；[C/模式路由](../mission-c-host-implementation-system-candidate-v0.2/runtime_profiles/host_builder/MODE_ROUTER.yaml)|normal/defect/recovery互斥、实际写权、平台锁和主体职责|
|S20|[C/实施判断完整方法](../mission-c-host-implementation-system-candidate-v0.2/canonical_methods/host/IMPLEMENTATION_JUDGMENT_AND_REASSESSMENT_FULL_REFERENCE.md)|§2四前沿；§§3–5正常主体循环；§§6–9表达/状态/方法/正式链；§10再判断及后续回压|
|S21|[DR01](DR01_A_COMPLEXITY.md)；[DR02](DR02_AB_SUBSTANTIVE_DEPTH.md)|DR01四种粒度、递归、普通Reflex与CEPS；DR02 §§1–8方法内部/控制器/事件/状态/产品/接收/完成，§§9–10管理与原义务|
|S22|[DR03](DR03_DELEGATION.md)；[DR04](DR04_B_ENGINEERING_PACKS.md)；[DR07](DR07_FEATURE_PRODUCTION_ADAPTER.md)|连贯委派、完整设计、两种任务、接收模式、首批代表性只读反馈和定向回修|
|S23|[DR05](DR05_COMPOSITION_IMPLEMENTATION.md)；[DR10](DR10_PRO_IMPLEMENTATION_AND_CODEX_ORDERS.md)；[DR11](DR11_CODEX_TWO_ROUTE_EXECUTION_AND_FEEDBACK.md)|组合接线、Pro关键主体/Codex明确指令、真实运行/诊断/复验|
|S24|[DR06](DR06_SUBSTANTIVE_MANAGEMENT.md)；[DR08](DR08_START_CONTINUE_AND_RETURN.md)；[管理Harness](MANAGEMENT_METHOD_HARNESS.md)|完整目标独立判断、取舍、条件性投入、地图、实际接续与责任完整性|
|S25|[来源、授权与人类参与](../runtime_overlay_candidates/agent_owned_long_horizon_overlay_v0_3/02_Source版本任务授权与人类参与_v0.3.md)|§§3–6：专业放权、Owner校准/决定、分支及材料连续性；管理题直接使用|

## 1. 每题共同输入与交付

正式专业任务须取得Owner完整目标及权限直接来源、实际工作对象及总体位置、已做/已审/未完、本题完整方法及相邻依赖、实际交付与回路。原合同/accepted parent只在真实存在或原任务要求时必读：全新用例明确无parent，已有成果缺原件则具名REQUIRED_MISSING，不得借新建例外规避连续性。首次管理尚无计划/覆盖/预算时按DR14 §1.0的BOOTSTRAP开始，由管理者实际形成这些输出；主控及Owner不预填专业答案。已形成计划的专业派发采用DR14 §1.2完整BINDING。

管理提供已确定的当前采用、已撤旧要求、整体位置和已知问题处置；专业者据此取得必要正确正文，交实质答案、实际成果和合法续作，不代做管理的全局裁定。A 的递归方法、时间、状态和消费者仍须完整，不把已否技术工程职责重新包装成业务对象；B 对照真实生产者与正常调用，不以无人生产的理想输入结算；C 检查正常入口和直接消费者确实迁移，不以新增内部函数结算。管理与审查题按 DR06／DR13 的实际职责执行，不按题号新增聊天、模式或必须产物。

专业正文使用已有 artifact 结构和人可读解释。下列题目的“交付”是必须真实存在的内容，可放在同一正文不同锚点；无需逐项新增文件。每轮用 DR14 定位本轮重点和本段剩余，不要求填满全部题目。局部完成、candidate、handoff-ready、Owner accepted、运行已证各自保持原权力。

<a id="a-1"></a>
## A-1｜完整市场过程、特征用途与持续责任怎样组织？

**原文与模式：**S01–S03、S12、S21；新建走 WORK_MAP，已有结构受影响按 MAP_REVISION委派。两者不可因题号相同混用写权。

**直接题面：**从 Owner 要识别、描述或解释的完整市场过程出发，恢复参与对象、作用关系、材料累积、转折、结束/失败及正式结果的用途。先说明每项关键 Feature 的正面含义、向上作用和 NonClaim，再判断 Source/measurement、客观事实、Feature、evidence、knownness、method intermediate、record和receipt。现有Book、类型和代码不决定业务边界。

对有独立业务生命的内容给出 identity、开始/持续/结束、材料推动、state owner与写权、正式结果及消费者；对复合内容继续展开内部真正独立的责任和普通处理。独立Book/Life必须资格化；不强制所有值成为DSU或公共产品。不把阶段或当前角色名字当边界。

形成过程、身份/状态、事件/时间、方法位置、正式产品/消费者相互对应的视图。说明中立事实和关系解释、复用产品和专用投影、内部计算的区别。候选比较仅限真实有差异的方案，不凑方案数。四个组合性挑战必须保持原义：同一事实换解释、同一产品换消费者、等价生成方法替换、合理新搭档；输入置换测试不能充当这些判断。

先覆盖完整 claim，再定当前可细化片段。跨多个片段的重要共用规则具名并安排责任，不预建通用运行底座。本题不将全部局部算法提前展开。已有用例要独立核目标变化，保留经过判断仍有效的结果，明确遗漏/不成立边界及最早受影响位置。

**实质交付：**业务叙事和形成层次；多视图边界及选用理由；覆盖地图中每项具体未清义务；WORK_SLICE_HANDOFF；结构修订返回关系。业务工作图、长程进度图、横切问题面保持不同用途。

**本段结束：**按原profile完成条件交候选；边界仍让Refiner猜则继续本题或具名Owner/source问题。没有所有叶子算法不妨碍结构候选；缺核心正面含义/产品责任不能候选完成。

**管理引用：**M-START消费全图及未决，检查Owner主体和共享前提；M-REASSESS仅深读影响安排的边界，不重复所有方法。

<a id="a-2"></a>
## A-2｜判断怎样真实形成，函数参数中的程序是什么，当前支撑到哪里？

**原文与模式：**S04–S07、S21（DR02 §§1–3）、S12；LOCAL_CONTRACT，结构修订内的受影响方法按原MAP_REVISION授权。

**直接题面：**对完整工作片段先识别承重Action树，再按D0–D6深入高后果动作。合法材料、候选形成、过滤、分组/分段、比较、排序/并列、投影、判断、commit和publish分别有真实责任。写出步骤与分支，不能用“按连续性合理分组”“取最优”“综合判断”结束。

每个可改变结果的步骤交清：当时有资格的材料及scope、输入身份与时间、候选是否可多选、排除理由、比较范围、并列/不可比/歧义、缺证可作多强结论、结果被谁消费。callback/列表/字典顺序不得取得业务选择权。材料合法性、时间和消费者契约必须随方法保持可见，不先按任意完备输入设计再以后补约束。

区分固定业务程序、可替换业务程序、运行输入、业务值、数值/枚举配置和工程自由。可替换方法展开当前程序、内部有实质可换的子步骤、稳定输入输出、不可弱化不变量、失败可见性和版本后果。换法改变scope、identity、状态生命、输出时点或消费者承诺时回合同，不作普通参数替换。具名函数不自动公开为参数或独立Feature。

按方法子树判断S1/S2/S3。充分支撑部分直接展开；部分支撑保留完整问题、骨架、已知分支、获授权简单首版、未知叶子和升级条件；真缺材料不编候选或阈值。区分当前程序完整、参数有合法来源、真实效果已校准。程序缺失不能称仅待校准；支持不足不能一律交Codex猜。停止依据为业务叶子、方法叶子、真实支撑边界或工程等价自由；支撑边界不自动带来主体完成资格。

涉及模糊判断时，从完整业务谓词判断连续程度、重叠原型、灰区和多因素，不从Bool/Double倒推。展开数值输入含义、单位、方向、universe与归一化；输出程度/多输出/分类依据；支持与反证、不可补偿因素、混合/不确定、当前规则程序、MF语义和配置来源。scope、knownness、身份、生命周期、错误及提交权由相应外围过程负责，不全塞进FIS。

分开一次推理多输出、同次级联、跨事件反馈和慢时钟方法切换；说明共同判断、采样时点、程度信息保留、反馈拥有者、防自证与旧状态处置。精确且实际可读的完整规则资产可引用，只有RulePack名称不够。复杂方法可按DR13作具名重点，必须回同一合同。

**实质交付：**完整Action树；当前程序及方法参数面；支撑/成熟度与合法首版；关键分支和市场Case；对时间、状态、正式结果与消费者的要求；具体残留业务选择。使用原方法五态，不造新的业务成熟度枚举。

**本段结束：**方法程序和边界清楚即可把重点转向A-3/A-4；实现者仍需选scope、candidate、group、rank、tie或fallback时继续。缺来源/Owner决定具名处理，保留其整体义务；不能编一个typed gap后宣布全量完成。

**管理引用：**M-REASSESS深读该方法的支撑与结果后果，判断继续研究收益、有限首版、真实材料需求和其他主体优先级；不要求固定多方案。

<a id="a-3"></a>
## A-3｜材料到达、确认与修订如何形成发生项、当前观点和历史？

**原文与模式：**S04–S05（§§8–12及V0.2回看/状态）、S06、S21（DR02 §§4–6）；与A-2写同一合同，不新建mode。

**直接题面：**从A-2当前方法出发，说明业务触发、当时可知材料、读取更新前/后何种状态、输入是同次发生还是历史值、结果何时仅为proposal、谁有commit/emit权。把事件类型和occurrence、业务发生/确认/发布时间、固定环境依赖与Dynamic持续业务状态分开。

同一firing多材料到达时给明确依赖与共同状态截面、冲突和顺序未知处理；没有正式先后依据不能借callback、遍历、技术延后或等待未来同刻回调制造业务次序。没有输入时是否有业务触发须有合同依据。

明确观察开始/停止/重新进入、订阅边界、scope变化、进行中/已结束材料资格及预热不足。每个持续判断明确回看所回答的问题、起止锚、可留材料、最小充分状态、结束/清退与重建，以及结束后仍允许的纠正。A给业务含义；实际容器/缓存/索引和组合器由B设计。

分别定义current、追加发生、正式历史、finality、revision与correction。说明duplicate/replay/late evidence、同身份修订、新生命、拆分合并影响哪些产物与消费者。增量状态对照明确参考语义，replay不重复正式发生；不能覆盖旧历史冒充新观点。

missing、pending、zero、blocked、unsupported、业务反证、正确业务空和程序错误分别表达。已有充分局部依据的合法结论不能被无关缺证整体压掉；未知不能升级成肯定。正式值说明成员含义、sum分支、集合基数、顺序/无序、关联身份、可空及消费者用途，不用“状态及证据等”包住实质。

时序/状态/消费者新义务触发对A-2的定向回扫，保留未影响方法。结构边界变化按S01/S09返回，不在局部静默改图。

**实质交付：**同一合同的完整时间与状态演化；current/occurrence/history/修订产品；knownness和合法有限结论；业务回看及充分状态；受影响方法修订、消费者及正例/near-miss/pending-conflict/correction Case。

**本段结束：**仍有同一事实的不同业务时间/状态结果就继续；已清楚而只欠物理承载则交B。整套历史未来证明不作为所有当前工作的前置，但已有正式历史义务不得缩掉。

**管理引用：**M-REASSESS判断哪些时序/历史缺口必须现在定清，哪些仅需后续忠实实现；检查是否为无依据未来场景扩建机制而当前结果仍未交齐。

<a id="a-4"></a>
## A-4｜局部结果能否组成完整业务合同，表达理由与下游使用是否成立？

**原文与模式：**S08–S11、S03组合性、S05 §16和V0.2完整形成/表达/Case/探针、S21；整合遵守当前mode，正式结构应用和独立审查另按原权力。

**直接题面：**将A-1边界、A-2程序、A-3时间状态和产品回装同一完整parent→child正文。正向追材料形成结果，反向追消费者需要的结果及真实生产责任；本任务内欠的上游形成或下游用途不得藏成空输入/将来集成。局部working稿不成为第二真源，后来的权威一句话不替代修掉冲突旧正文。

依据方法内部、事件状态拓扑和持续责任，判断既有滤波器/普通Reflex能否充分表达，复杂表达具体增加什么必要能力。普通Reflex可有事件、采样和状态；排除一个大纯函数/单reducer不构成CEPS必要性证明。不预设DSU数、CEPS层数、两路比例或Book数量。

四项组合性挑战保持原义。以实现者仅看正式合同走一条完整业务生命，检查是否还要自选材料、候选、分组、排序/并列、方法、时间、state owner、产品和消费者。探针仅返回残留，无权替上游给业务答案或最终PASS。

Pro按S08逐finding处置：接受/部分接受/拒绝越权/回地图/回局部/需RepoFact/需Owner。写回正文、只重扫实际影响面；达到规定条件时re-probe修订后的完整合同。独立Auditor仍须fresh上下文、复做承重判断与适用anti-gold；可消费真实探针事实但不继承Builder自评资格。

**实质交付：**连贯完整合同/版本连续性；复杂度理由；残留反馈、Pro处置、实际修订及必要再次消费；局部/整包审查对象及未审范围；进入B的有效输入和真正未决。

**本段结束：**按原专业完成门交候选及接收。局部handoff-ready不代表完整A，A完整也不代表B/C完成。重大原件缺失仍由具名责任者取得或请求有权处置，不能无限重复登记。

**管理引用：**M-CLOSE从完整A目标分类剩余：真实业务选择、明确整合、来源/权限、接收/审查；给条件性预算和下一工作，不能只增加待办。

<a id="b-1"></a>
## B-1｜真实平台、生产调用与消费事实能否支撑这段工程？

**原文与模式：**S13–S14、S16 §§1–3、S18事实/读取检查、S22 DR04 §1；RepoFact只读事实，Compiler不得反改冻结S0。

**直接题面：**围绕即将决定的工程问题定向调查：真实输入入口和caller、可复用typed业务值、状态owner和生命、实现或接近Action的symbol、method asset加载/参数/消费、正式product/writer/readback/consumer、平台能力及不能从repo唯一得出的事实。每项调查对应具体设计决定，不全仓漫游。

按任务命中读取共享 `agent_evolution/platform_engineering_references/feature-platform-engineering-reference-pack-candidate-v0.1.0/00_REFERENCE_ROUTER.md` 及完整成员。Python/Numba、跨语言和Haskell/FRP分别核实际基础计算、包装、Fao/Frame/DBA及caller；文档不代替现行代码，代码不裁业务。类型、PoC、历史失败实现、未调用资产与真正生产者分开；planned upstream不冒充外部已有。

先取得任务代码锁，再查live drift，选exact tuple取得承重文件，区分direct fact/inference/candidate/gap；报告真实不可取得项及影响，不偷换到旧索引。平台变化先证明宿主内无法解决，不新造backend或总adapter。

**实质交付：**可供当前设计使用的冻结S0、当前链/符号/真实限制、影响具体选择的未知、必要平台reference锁。S0元数据准备不算业务里程碑。

**本段结束：**足够支持当前设计则交Compiler；设计中发现新未知定向回本题，不每个子任务重扫全仓。业务合同本身缺失精确回A。

**管理引用：**M-REASSESS仅深读影响宿主/方法/状态/产品的事实，判断调查何时足够，防把本方欠设计/欠上游生产叫外部阻断。

<a id="b-2"></a>
## B-2｜方法、事件、状态及正式产品在实际宿主中怎样完整运行？

**原文与模式：**S13 Compiler、S15、S16 §§4–9/11–12、S18工程检查、S21 DR02、S22 DR04 §§1–6、S23 DR05；消费有效A及冻结S0。

**直接题面：**先给当前与目标运行设计，明确保留/修改/新增/退出。沿真实输入、基础计算/正式特征、消费过程、方法、状态、正式结果、writer/存储、readback/消费者，形成可施工的整条设计。每项承重Action落到宿主、实际caller、symbol、typed输入输出和状态读写。

按业务判断ordinary计算、简单Event变换、单owner更新、CEPS processor、局部递归子图和跨owner协作；普通Reflex充分时直接采用。不得按重要程度、文件数或有无状态选路；也不能将独立Action压入WholeState只包一层Event。root负责构造/连接，不吸收隐藏业务判断。

把方法构造/取得、配置来源、材料/状态/参数、caller、返回值、外围更新/发布和消费者一起设计。区分建立时选择与运行中切换，说明状态、历史、版本和replay后果。实际CFIS/RulePack按平台复用，保留程度/多输出，不crisp后伪造membership，不把方法成功当commit资格。

由业务回看给出活跃状态、充分摘要、持久历史、结束清退、重建和允许增长维度；最新版/固定最近N不自动等价业务回看。保留所有合法sum分支与产品含义，实际ADT/存储转换无损。区分同宿主调用、订阅独立特征、消费物化结果并选定真实连接；内部量可观察不等于新公共产品或Book。

定清主要工程选择、真实代码写面和回交。配置/类型/容器等允许自由不得掩盖中大型架构欠账。缺来源回B-1，缺业务回A，B自己未设计就继续做；平台窄回压按原权限，不能让C临场造新平台。

**实质交付：**Owner可读目标工程；Action→symbol/caller映射；有效方法链；状态物理计划；正式产品与整个消费连接；主要选择及工程自由；实际实施工作及返回成果。模型/fixture只能证明相应问题，不能代替工程正文或真实接通。

**本段结束：**当前范围主要工程已定即可形成B-3代表性任务；完整B仍须全范围和接收/组合收拢。局部模型越来越多但重要设计仍未定，按M-REASSESS判断投入。

<a id="b-3"></a>
## B-3｜完整设计如何交给正确实施者，两路怎样实际汇合？

**原文与模式：**S17、S16 §§10–12、S22全部、S23 DR05、S18连续性/回压；Compiler形成任务，接收角色只读/实施模式和权限分别确认。

**直接题面：**按可交回的连贯业务结果形成任务，不按文件/字段/聊天轮切。明确完整普通Feature、复杂过程以及父任务内普通方法；不为配额把helper升Feature或整个用例包总Fao。两类任务的业务深度相同；没有适用单元不凑双路。

区分表达方法、实际Pro/Codex执行者、方法仓、代码仓和组合责任。采用同事原版、明确接入版、方法借用分别满足真实输入/模式条件，不伪造对方需求Agent跑过或接受。

接收材料完整包含外部边界、责任块及事件关系、内部业务逻辑、语言无关类型、方法树/可换子步骤/当前程序、参数及响应式表达。工程身份放implementation_binding、真实链观察放verification_observation；两者不能吞掉B设计，接收者不读的附录不算保留。模块级函数集合包含真正具名业务子函数，不滥升普通helper。

首批代表性完整任务形成后即用授权的只读接收方式检查，不等全部任务写完。接收者仅凭正式输入恢复结果与实施方式，定位还需首次裁的业务/主要工程、格式缺失及运行限制。Pro独立处置反馈：A欠业务返回A、B欠设计自己补、适配缺口修实际入口、环境限制具名；修订输入再次被接收，不以已发反馈结束。

沿唯一父设计明确每个共享输入/产品谁生产、谁消费、接口/版本、共享注册和writer/readback由谁负责。组合接线是明确工程工作，不能把新业务判断留给“最后集成”。同一主正文按exact版本投影，生成视图不手工演化第二真源。

**实质交付：**实际需要的两类完整任务、适用平台锁、接收模式和反馈处置、父组合及最终交付责任、允许代码/运行面和真正未决。ARCHIVED/metadata通过不表示专业接受；有限只读、实现、真实运行和完整验收分账。

**本段结束：**按原B完成门/独立审查交接；工程完善只到B的任务不得因为题库有C而启动实现。未来来源/机器缺失不删除当前设计义务；不影响的独立工程继续。

**管理引用：**M-CLOSE引用目标工程、真实接收反馈和父组合，分类剩余设计/适配/验证，给实际任务和预算，不能把完整接收永远留在尾部。

<a id="c-1"></a>
## C-1｜已指派的全部业务主体是否真实进入代码并可以继续构建与实跑？

**原文与模式：**S19–S20、S23 DR05/10/11；按原profile取得完整业务、CEPS、平台与权限。正常主线从C实施判断§3—§4进入，五段不新增题号／机器模式。

**直接题面：**维护完整scope、实施、实证和预计形态四前沿。按相连业务结果组织施工批，Pro尽量完成全部相关方法、类型、必要分支、事件／状态／修订、caller、注册、手写包装与正式输出，不只交代表性内核、接口/no-op或外部已判答案。

忠实使用B的最低充分表达：普通函数／Reflex保持直接，真正复杂CEPS有typed端口、方法数据、子过程和拓扑，root只组装。方法id／版本／参数实际进入正确cut，外层消费并掌握commit资格；状态、摘要、持久历史按原回看／结束／纠正实现，不能为性能删历史、缩范围或降频。

涉及已有特征，读清业务含义、相关输入输出、参数及实际采用方式，核原值／缓存／投影是否提供本次所需信息。按已有工程接正式生产者和消费者，配置／import存在不证明已接入，不能让消费者重算上游或补猜来源。

一批源码可构建就交Codex，正常构建单预授可确定的编译小修范围，工程师按同根原因检查并集中修通后复编。重要事件状态／接口／结构／业务问题回Pro集中处理，其他确需Codex编码有具体理由。主控不编业务工作，现场执行不压给无环境Pro，纯执行不制造源码提交。

当前业务和真实接通优先，不提前大量扩写场景测试、fixture、proof或工业化设施。必要标准构建、日志、内存保护、正式写读保留。上游本任务未写继续内部施工，不妨碍合同清楚的独立工作，fixture不冒称上游。

**实质交付：**exact源码与完整已写／未写、实际方法／状态／连接、构建和运行证据分级、Codex明确连续工作单、当前工作说明和后继、必要窄回压。源码提交和局部编译成功不关完整Goal。

**接续：**主体继续；构建通过且正式路径／运行安排具备，进入C-2；未具备返回具体缺失主体。不等全用例写完才跑，也不因首次小路径跑通停止其余责任。normal／defect／recovery按实际场景，无新证据不重做。



<a id="c-2"></a>
## C-2｜真实市场结果怎样解释，必要修正和复验是否完成？

**原文与模式：**S20 §3—§4、§8—§10及适用回压，S23 DR10/11，S19当前模式。真实数据、源码和运行权限依当前任务，不从题号取得。

**直接题面：**对确切源码／配置／数据执行必要构建与正式实跑，沿输入→生产入口→实际方法／过程→正式输出→保存／读回→消费者取证。具备诚实路径即跑，其他主体继续；不全面环境研究或先做全测试。必要中间值来自真链，不另算旁路。

核对象／频率／时间／单位／预热、调用、方法参数激活、写读和消费者。无输出分别检查输入未到、预热不足、未调用、未激活、正在形成、读回失败与合法空。开跑前内存保护、进度和主要开销实际记录，异常先保护再定位；可信小范围结果先分析，目标规模问题继续，不无限先做性能优化。

Pro结合真实输入解释主要对象／过程／关系为何形成和怎样演化，关键参数作用及必要对照是否符合含义；持续对象按合同检查生命周期，其他特征不强加统一状态。结果全空／非空／字段齐全仅支持有限结论；核心对象未实际形成不签生命周期验证，观察窗末仍存活与漏结束区分。

对照保留基线，在授权的方法范围内按实际疑点安排，不固定三档或全矩阵。实现偏差修代码，主要工程失效回B，业务含义变化回A／必要Owner；静默改阈值追非空、删历史、降频或放宽正式预期禁止。

Pro主要写修订，工程师执行调查／对照和修后复验，独立审查复核重要解释及影响。技术故障修好后继续原业务问题，不能只保存反馈。后续综合图审／成熟化保留具体结果和问题，当前能查清的语义不留给Owner。

**实质交付：**真实命令、版本／数据／配置、正式可读结果与相关输入、业务解释和必要参数差异、问题性质／依据、实质修订及复验、完整未完与正常后继。当前工作说明进入现有continuation；不以fixture／计划／exit code代替结果。

**管理引用：**M-REASSESS决定缺主体、接线、输入、方法或证据怎样高效处理，M-CLOSE另核全范围已写／已跑／已解释／已审。局部工作单接收不关全Goal，不把未来最终调优变当前前置，也不漏当前最低正确性。

## 2. 题目自己的检查

向后：本题必须保留原文正向业务、细度、例外、禁止、写权和新补充；不能只抽Owner口号而丢Pro已展开细节。向前：结果应能进入下一专业题/接收，主控无需猜重点，实际完整目标未被局部取代。schema、标题和引用存在不能证明这两项。

任务本身不适当时审查可以否定前提；改变真正Owner决定仍需原授权。后续经验修题库要明确旧成果影响，不能让一次方法发布自动升级运行资格或批量重做旧用例。
