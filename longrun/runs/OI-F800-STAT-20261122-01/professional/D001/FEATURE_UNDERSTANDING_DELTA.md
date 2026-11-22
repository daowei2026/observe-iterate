# D001｜F800 最小当前理解与 delta

本项对应 `OI-F800-STAT-20261122-01 / C0002 / D001 / F800-U-001`，执行者为 `codex:OI-F800-STAT-20261122-01:executor:E1`，回原 manager，workers=[]。

原生 `completion_status=PARTIAL`：本轮要求的最小实现理解、构造、对象、时序、期限和读取合同已说明；准确实例尚无正式结果，当前运行的字段可用性及真实引擎加载仍待 X 验实。主要链足以继续 X；这里没有把缺失的运行证据写成已完成。伴随的 `FeatureUnderstandingPackage.json` 使用原 Skill 顶层结构。

## 采用与复用

- Skill、WORKFLOW、IO_SPEC、BUSINESS_OBJECT_QUALIFICATION_GUIDE 采用 observe-iterate `87b951bbd15078a2d6353bdd24afe0d8f19c845c`；执行深度按同版 L0 §2、F_BASE_RUN_INPUT §6。
- 复用同版 `ai_chat/根据统计找不合理点/F特征：统计线闭环.md` 的已纠正对象口径和时序解释；并读取本工作区旧 `results/f-business-objects-v2-20261121/F_业务对象与属性驱动逻辑_V2.md`。旧统计数字、默认 6 的窗口和旧实例完成事实均不转成本 Run 成果。
- 当前 FRP 为 `ac1927518ad6105f15ffbe37fea45e4be91ba574`；TIS 为 `2f460d663d821cf2ba25555eda13e78b697d0767`。本轮只核影响 800 的改动及其必要上下游，没有重写全部旧材料，没有做统计、诊断、选值或合理性裁决。
- `SOURCE_AUDIT.json` 核对 packet 的 25 个精确来源（含 INVOCATION）；可见 adopted 副本与 Git 原件逐字节一致。外部完整配置由 GitHub connector 按锁定 commit 取得，Git blob 为 `a7417e3fa30bda3176670ee5dcfebf688e181bae`。

## 当前实现和实例定位

主工作树的 TIS HEAD 是 `10010b89…`，FRP HEAD 是 `37c790c0…`，均不是本轮锁定版本。它们保留原有修改，本 D 没有切换或修改这两个工作树。

准确 FRP 克隆在 `.runtime/f-observation-multiple-github-20261122/frp`，HEAD 为 `ac192751…`、分支为 `codex/f-observation-multiple-20261122`，已跟踪文件无差异。可用 runtime 在 `.runtime/f-wide-observation-20261122/runtime`；核对的 10 份 FRP 和 6 份 TIS runtime 源文件与对应锁定 Git 对象逐字节相同，见 `INSTANCE_INSPECTION.json`。

亲自执行的是 `inspect_instance.py`，通过既有 `run_in_runtime.py` 绑定上述 runtime。`inspect.getfile(make_features)` 和实际 wrapper 模块均落到已校验的 TIS 文件；`inspect.getfile(type(f))` 落到平台 proxy，不能拿 proxy 文件冒充业务实现。程序只构造对象和序列化配置，`run_ups=False`，没有调用 Feature.run/rerun/to_df/to_dfs，没有启动 FRP 可执行程序。源码等价核对不等于已经验证编译程序实际运行版本。

基线经正常 `make_features(**PARAMS)` 构造，只取 f，继承相同 inputs/sources、domain、result_layout；profile 只增加 observation_multiple。构造入口依约也构造 Q/V 参数对象，但没有运行、读取或分析 Q/V。

| 项目 | 当前核对事实 |
|---|---|
| 完整参数差异 | 唯一新增 `/profile/observation_multiple = 800` |
| 基线 | 完整 F 参数与锁定 U2/U3 JSON 的 `feature_parameters.F.params` 相等 |
| 其他参数 | delta=600、unit=CalendarUTITick、method.revision=1；rb/hc/i、5m、night_end_at_2300、steel 均继承 |
| SOF 与日期 | TA_updto20240229_DBA；请求 2021-01-01 至 2023-12-31，full_period=None |
| 当前配置 SHA-256 | `b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3` |
| 基线配置 SHA-256 | `f6249aca6d2ea0d8c2f664d675617d151bfc13b1a309124c4db57fca9d2f2a5f` |
| 当前结果身份 | INSTANCE_INSPECTION.full_dir；与 baseline_full_dir 不同，当前 fields.json 不存在 |

保存并重新 JSON 解析的 `configuration.json` 和 `baseline-configuration.json` 是当前构造证据，不是原生运行产物。目录路径中的请求日历区间也不是实测行情首末时点。

历史 `results/f-wide-observation-20261122/configuration/configuration.json` 的 method.revision 是 `wide-observation-800-v2-20261122`，与本轮要求的 `1` 不同；历史运行脚本显式改了这一项。因此该旧结果不能直接绑定为本轮准确实例。此差异是结果身份事实，没有据此修改正式配置。

## 业务对象、关系和计数单位

保持旧材料纠正后的三类：原始价格转折、指定尺度贴近转折、共同价格转折候选组。前两者可能对应同一行情位置在不同资格下的解释；不能把每个处理步骤都算成新对象。

| 对象或概念 | 属性与处理 | 身份及计数单位 |
|---|---|---|
| 原始价格转折 | 实际峰谷、价格、方向、确认和当前 Zig 状态；供尺度选择 | 上游品种、源实例和原发生；F 不保存全量原始转折，不能用成员表当分母 |
| 指定尺度贴近转折 | 被 M 尺度选中位置，P/T/C、价格、actual/confirm/known、Clock、轮次 | 当前 KLine adapter 的 Turn exact 由上游结果根、value1/value2、几何 confirm 位置定位；内部 TurnKey=(object,Turn Life) |
| 共同候选组 | 具体成员、四项两两依据、整组依据、覆盖、观察及修订、重叠/被覆盖 | 内部 CandidateKey=(原 FormationQuestion,有序 TurnKey 集)；输出 Life 标识组，Revision 标识一次观点，均限准确实例/结果身份 |
| 两两相容、组间关系、资格和责任 | 按成员属性计算的关系或对象属性；可以被多个组引用 | 不自动成为新的独立行情对象；pair 数、成员行数、组 Life 数、组 revision occurrence 数分开 |
| 配置、Clock、Material、处理器、Event 包装 | 实现、参数、位置参照或中间处理载体 | 不列为行情业务对象 |

当前 KLine 路径为 `GroupKLineInput → ScaleTurnCalendar → GroupTurn → Material → PairView → CandidateOccurrence → 正式 publication`。`GroupCandidateSource.hs` 的保留窗口也已参数化，但它属于另一 NativeSource 路径；不能说当前 KLine 实例先生产独立 Source 产品。

G 后续应分别使用：每品种上游选中转折身份、参与过组的去重转折、包含某品种的去重组 Life、这些组的观点发生。跨品种组数不能直接相加；同一组多次 revision 的成员行也不能重复作为上游转折总数。本 D 没有计算这些数量。

## 800 的实际消费关系

令 `a` 为组内最早 actual Clock，`u` 为当前 Calendar 进展，`Δ=600 tick=5 个开盘交易分钟`，`W=KΔ`。

| 处理 | 当前实现规则 | K=800 的含义 |
|---|---|---|
| 材料首次准入 | 非撤回、Clock 在当前知识下可用，且 actualClock+W≥u | 有限 4000 交易分钟；不是从 confirm 重新计时 |
| 新候选问题 | u≤a+W；在有限域内枚举正面和正面+未决的极大 complete-link 组合，至少两不同对象 | 原问题为 (a,a+800Δ,a+806Δ) |
| 实际贴近 | `abs(clockA-clockB)≤2*formationDelta`，仍由未改的 assessPair 判断 | 1200 tick=10 交易分钟；800 不进入该式 |
| 四项关系 | 时间、方向矩阵、类型矩阵、各成员自身 P/T/C 弯折；任一 veto 否决，全支持才 positive | 不能用 AB、BC 支持替代 AC，不能跨品种相减价格 |
| 覆盖 | 每个固定域对象需覆盖 [u-W,u]；覆盖不足单列 | 观察完整性所需区间同步扩大；不直接改写局部 Supported/Incomplete/Contradicted |
| 未知 Clock 等待 | 从首次未知记录起最多 6Δ | 仍为 30 交易分钟，没有随 800 放大 |
| 当前期限修订 | deadline=min(旧deadline,当前a+W)，revisionEnd=min(旧r,deadline+6Δ) | 只收紧，不续期；修订尾仍 30 分钟 |
| 参与交接 | 初始 min(原r+18Δ,当前r+18Δ)；后续只收紧 | 无收紧时 a+824Δ=4120 交易分钟；不延长 F 自身责任 |

FRP 入口把 profile.observation_multiple 读为可选正有限数，并由 groupFormationMethod 消费；省略时仍默认 6。旧脚本原样运行不能形成当前 F800。800 是 Owner 锁定输入，不是本 D 选出的标定结论。

主要代码位置：ac192751… 的 `CommonPriceTurnGroupCandidates.hs:114,128,138,180,267`，`U2/GroupCandidateTypes.hs:19`，`GroupCandidateMaterial.hs:54`，`GroupCandidateEvolution.hs:45,125`，`GroupCandidateDecisions.hs:43`；2Δ 见同版 `GroupCandidatePairs.hs:26`。

## 时序、状态与真实 occurrence

| 概念 | 当前语义和字段 |
|---|---|
| actual | 市场位置 T；memberActual、memberT_pointActual；anchor 基于 actual Clock |
| confirm | 上游几何确认检查点 C；memberConfirmation、memberC_pointActual；不自动等于系统收到发生的时点 |
| selected | ScaleTurnCalendar.value1/value2 真正发生时才获得尺度选中事实；F 无独立 selected_time 字段。需上游事件轴，不能拿 T.pointKnownFrom 代替 |
| F 接收/可知 | memberKnownFrom 是 adapter 本拍已取得该选中事实的 known；T.pointKnownFrom 可能来自更早的原始 Zig 事实 |
| group create/admission | 首条该 Life 的 groupKnownFrom/原事件 timestamp，及冻结的 participationAdmissionKnown；没有独立 groupCreateTime 字段 |
| revision | 同 Life 正文或决定含义变化后发布新随机 Revision，groupPrevious 接准确前版；用知识时间和链排序，不按 UUID 排序 |
| publication | 原 Tick 的事件时间由存储读口映射为 timestamp；同刻 occurrence 序号保留，不把 actual 当发表时间 |

本轮没有验证旧材料中“收到确认晚一根5m”等实测延迟；不能把它写成所有运行的常数。

局部依据为 Supported/Incomplete/Contradicted，与 observation、groupClosed、participationDutyClosed 分开。观察基础优先级是 scope结束→EndedByScope；反证→Withdrawn；closed且支持→ClosedSupported；其他closed→ClosedInsufficient；其余Open。随后同当前问题下更大支持组合严格包含本组时，可变为 Subsumed。Withdrawn/Subsumed 本身不销毁 Life，也不单独结束修订责任。

到 deadline 或 revisionEnd 的同拍先接纳材料，再关观察/责任；u==r 仍可形成最后观点，处理后仅 u<r 且非 scopeEnded 的候选保留活跃。观察一旦关闭不回 Open。没有新发生不代表 Invalid 或已结束；正文/决定没变可以不重复发行。

## 公开字段与缺失语义

Feature 为 CommonPriceTurnGroupCandidatesFrp，布局为 `common_price_turn_groups.core.v2`。原生 Event 是 `Tick [GroupCandidatesRecord]`，其中 `groupDefinitions[]` 是配置中间结果，`groupOccurrences[]` 中每一项才是一条候选版本发生。原事件可以携带多条候选发生，公开主表行与原事件发生次数不是同一粒度。

`PUBLIC_TABLE_SCHEMA.json` 是从锁定 TIS 公共读取声明取得的 31 张表合同，包含列、dtype、存储路径和 enum，**没有读取本 Run 正式表**。结构合同 AVAILABLE，当前准确实例数据统一 UNCONFIRMED。

| 业务项 | 表/字段 | 连接与缺失含义 |
|---|---|---|
| 组及版本发生 | occurrences 的 groupReference、groupKnownFrom、groupOriginal*、当前三期限、状态/覆盖/closed | 主表物理键 timestamp+occurrence+record_id+child_id_2；业务键须加准确实例及解码 Life/Revision |
| 成员和时间 | occurrences_groupMembers：memberObject、memberTurn/source、Actual/Confirmation/KnownFrom、P/T/C、Round/Status/Retracted | 用完整组父坐标连接；memberStatus 是在当前组中的相容资格，不是上游确认状态 |
| 可选 P/Clock | memberP、memberClock、各 pointClock 子表 | 空列表表示该可选值缺失；不补零，不据其缺失判整个事件没有发生 |
| 两两依据 | occurrences_groupRequired 的左右 exact 与四套 requiredVerdict/Gap/Veto；pairDistance 子表 | 支持/未决/否决分开；-1 是无相应 gap/veto 分支，真实0保留 |
| 修订沿革及组间关系 | groupPrevious、groupOverlaps、groupCoveredBy、participationAlternatives/alternativeBridge | 按准确端点和完整父坐标解释，不按同品种名单或时间近自动连接 |
| 原参与、责任、反证更正 | groupFormationParticipation 及成员、supports、operands、points、Clock 子表 | admission 冻结，candidate/decisionKnown 可更新；supports 是反证及更正历史，不是所有正面 pair 的重复表 |
| 保留的期外通知 | participationOutsideNotifications 及子表 | 原 F 存储校验要求为空、inputConflict=0；有表声明不代表当前 F 发行此类业务事件 |
| K 参数身份 | configuration.json 的 profile.observation_multiple | 正式 definitions 没有该字段；不能只凭 definitions.method 或口头 F800 认定结果身份 |
| 材料准入/首个阻断/全上游分母 | 内部 materialEnumerable、eligible、waiting、原始/未选转折 | NOT_EXPOSED 于 F 31 张表；后续须取得准确上游发生和独立处理证据，不能从组成员反推全量 |

## 回交范围与剩余事实

本 D 已形成最小当前理解及可复核配置。PARTIAL 的具名缺口是：准确实例正式结果尚未建立、未执行编译程序的实际配置回读、未核当前运行31表和真实首末行情。它们属于既定 X；不为补齐 U 而越过 Skill 的“不运行特征、不做统计”边界。

X 还需按既定 Owner 输入核真实结果写面、授权和单写者：当前解析的 full_dir 在 `/m3varK`，路径引用本身不授权写该目录，D001 没有向其写入。历史输出的 method.revision 差异须保留，不得默默复用或改名冒充。当前源代码中的覆盖连续性精确浮点比较与历史报告所载疑点，只作为后续已知 finding 线索；本 D 没有重新诊断、确认关闭或形成修改建议。

由原 manager 消费本回交后安排 X，再按已采用依赖进入 G/D/Release。本 executor 没有签发后继 D/W、修改 TASK_PROGRESS、创建线程或发送跨线程消息。Feature 行为及参数输入均未更改。
