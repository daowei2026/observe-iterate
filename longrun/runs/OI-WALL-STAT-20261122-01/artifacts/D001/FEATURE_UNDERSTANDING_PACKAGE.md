# WALL 当前版本理解包：既有理解复用与差异核对

`FeatureUnderstandingPackage`；`package_id=FUP-WALL-STAT-20261122-D001`；`completion_status=PARTIAL`。

本包属于 `OI-WALL-STAT-20261122-01 / C0002 / D001 / WALL-U-CURRENT / WALL-U-01`，由 `codex:OI-WALL-STAT-20261122-01:executor:E1` 回交原 manager。执行的是指定 Skill 的 U1—U10；当前可用范围为固定提交的 producer 实现理解，当前实例加载与物化字段尚待补证。

## 1. 来源、复用规则和当前目标

- 委派：`daowei2026/observe-iterate@39cf79944683d2a458d042effbecacea37ebae66:longrun/runs/OI-WALL-STAT-20261122-01/delegations/D001/DELEGATION.json`，及同提交同目录 `DELEGATION.md`。
- Skill、WORKFLOW、IO_SPEC、对象资格补充：`daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:skills/feature-understanding/SKILL.md` 及该提交同目录对应原件。
- 业务输入：`daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:task-inputs/wall-f-parallel-closure-20261122/WALL_BASE_RUN_INPUT.md`，采用其第 5 节复用政策和 control-v0.3 的 U 节点。
- 复用基包（下文 BASE）：`daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:task-inputs/eaw-p1-integrated/feature-understanding-result/WALL_FEATURE_UNDERSTANDING_PACKAGE.md`，包 ID `FUP-EAW-WALL-20261120-01`。

本包由 BASE 中未受影响的 producer 事实与下列覆盖项组成；冲突时采用本包针对当前目标的记录。BASE 的 TIS `ef887396…`、FRP `cac6c912…`、`rb / 2020-12-01..2021-02-22` 集成实例及 FRP 主输出分类属于历史上下文。它们不成为本 Run 的实际版本、范围或结果绑定；FRP typed ingress、DSU 与三路 writer 也不扩展成本次 producer 任务的验收面。

| 绑定项 | 当前采用值 | 证据层级 |
|---|---|---|
| Feature / 构造 | `mquant.tis.hf.prel0.wall_assembler.WallAssembler`；固定提交的 `WallAssembler()` 默认实例引用 | Owner 锁定，可由代码解析；未实际构造 |
| TIS | `daowei2026/tis@6618d4d147d6ebbe634e61facddf2c9a0b996982` | 固定 Git 对象已读取 |
| 范围 | `TA_updto20240229_DBA`、`[rb,m]`、2021-01-01 至 2021-12-31、bid/ask、`night_end_at_2300` | Owner 硬输入，尚无本 C 运行结果 |
| 工作区 | `/dwdhome/fy/BASE_E6_2`；TIS 位于其 `mquant/tis` | realpath 已读 |
| 现场一致性 | TIS HEAD 等于锁定提交；工作树 `hf/prel0/wall_assembler.py`、`frpExample/STCalendar.py` 已有修改 | 本 C 读取前即存在；原样保留 |

`wall_assembler.py` 的现有修改加入全空日历占位排除函数及 `_load_cc_df` 覆盖，影响实际输入路径。因此 HEAD 一致不足以证明实际加载与锁定实现一致。本 C 没有导入、构造或运行 Feature，没有采用该输入处理，也没有确定本轮 m 的占位行数量。固定源码、工作树哈希和原有 diff 见本调用 `checks/LOCKED_SOURCE_OBSERVATION.json`、`WORKSPACE_PREEXISTING_DIFF.patch`。

### ImplementationSourceRecord

下表 TIS 引用均为完整固定版本 `daowei2026/tis@6618d4d147d6ebbe634e61facddf2c9a0b996982:<文件>`；行号属于该 Git 对象。

| 编号 | 文件／位置 | 职责与核实状态 |
|---|---|---|
| IS-C1 | `hf/prel0/wall_assembler.py:232–388,681–861` | 默认参数、F1/F2/F6 接线、跨 chunk carry、公开结果与 receipt；固定源码已核 |
| IS-C2 | `hf/prel0/wall_assembler_core.py:119–167,902–1341,1377–1685` | 对象身份、状态、D1/D2/D4、事件与 trace；固定源码已核 |
| IS-C3 | `hf/prel0/tick_quote_context.py:160–246` | `SubContinuousContract().rerun().F.value`、`VolQuant(...).rerun().F.qt`、严格前值 QT、`trading_days()` 分块；固定源码已核 |
| IS-C4 | `hf/prel0/tick_quote_context_core.py`、`hf/prel0/track_wall_candidates_core.py` | F0/F1/F2/F6；与 BASE 对应文件字节相同，复用其 ID-03..06 |
| IS-C5 | `hf/prel0/p1_dba_export.py:256–305,460–467,522–584` | 同拍物理分流、最终 frame 选择、chunk DBA 写入及 Dao 读回路径；固定源码已核 |
| IS-C6 | `hf/prel0/p1_product_receipt.py:115–199` | commit 加源文件哈希的实现指纹、实际 input scope；固定源码已核 |
| IS-C7 | `hf/qt.py`、`t0/gen/cc.py`、`hf/mc.py` | 上游数据与交易日来源；职责沿 BASE 复用，版本差异仅补影响当前定位的事实 |

BASE 到当前版本的最小补充：当前交易日计划来自 `trading_days()` 的区间，以左右 `searchsorted` 选行并检查无缝全覆盖；不能沿用旧 calendar-period helper 的具体实现描述。当前 `hf/qt.py` 从 Sof 的 `tlist/main_contract/{sym}.csv` 读取主力区间。`p1_dba_export.py` 整文件有 AttackSegment 部分差异，当前 Wall 的 packing 与导出路径按上述固定符号核对。没有据此开展其他 Feature 分析。

## 2. 业务对象、属性和计数单位

### BusinessObjectModel

| 编号 | 对象、业务含义与身份 | 生命周期、关系和状态载体 |
|---|---|---|
| BO-C1 | 单侧盘口上由候选砖及后续支撑形成和维护的 Wall life。`wall_id>0` 是单次 producer source 执行中的本地身份；对象键为结果/source namespace、symbol、wall_id，side 是应保持一致的属性与统计分层 | Start 创建；BandUpdate 和 StateChange 更新；End 终止。每侧一个当前 slot，bid/ask 独立但共享 next_wall_id。core/band、support 成员材料与状态均描述同一 Wall。状态由 slot 和完整 carry 维持；跨物理 chunk 延续，重跑不保证编号可比。证据 IS-C1:265–371、IS-C2:916–1012,1510–1685 |

BASE BO-01 的持续对象语义可复用。BASE BO-02 是同一 Wall 的投影，不增加第二种独立 Wall 计数；本次 producer trace 也按此解释。对象没有独立的 confirm_time；事件 uti/ts 即代码记录的发生位置，不能另外生成确认延迟。

| 候选项 | 当前归类 | 计数解释 |
|---|---|---|
| 某时刻某侧的一档价格／挂量 | 输入业务观测单位 | 一条双侧行情行可提供两个侧别观测，须保留 symbol、时间和 side |
| LargeQuote、Wall brick candidate | 同一观测获得的资格／中间材料 | 可以分别计资格命中；不能因过了两个门就把同一观测算成两个持续实体 |
| Wall life | 业务对象 BO-C1 | 按 source namespace 与本地身份去重 |
| band/core、Alive/Dormant/Ended | 对象属性／状态 | 状态样本与状态转换分别计数 |
| support、thin touch、far/no-presence 计数 | 关系判断／内部状态 | 不自动升级为独立 life 或 occurrence |
| QT、深度 mid/hi、阈值、发布位置基准 | 参照量／参数／工程状态 | 不作为行情中新增业务对象 |
| Feature、Calendar、chunk、结果表、receipt | 实现和运行绑定 | 不作为 Wall 业务对象 |

| 单位编号 | 可用于后继的单位和分母边界 |
|---|---|
| CU-1 | 输入行数与有效侧别观测数分开；有效性及占位处理以 X 确认的正式输入为准 |
| CU-2 | F1 资格命中侧拍数；分母为同侧有效输入观测，不能用 sparse event 行数代替 |
| CU-3 | F6 候选侧拍数；可对 F1 命中或同侧观测分别求转化，但必须标明分母 |
| CU-4 | 新 Wall identity 数；兼容候选并入／恢复旧身份不创建新 life，relocation 才结束旧身份并创建新身份 |
| CU-5 | Start/BandUpdate/StateChange/End occurrence 数；每条离散输出各计一次，同拍多条应保留 |
| CU-6 | Alive/Dormant/Ended trace 样本数及连续状态段数；Ended 可持续占据 slot 多拍，行数不等于 End 次数 |
| CU-7 | 完整生命周期与范围尾仍活跃对象分开；寿命优先用同身份 Start/End 的 UTI 差，未结束对象须标截尾 |

这里只定义单位，没有计算数量、比例、持续时间或任何分层统计。

## 3. StateModel 与 occurrence

| 状态编号 | 状态及初始／终止性质 | 已实现进入与退出 |
|---|---|---|
| ST-C0 | Empty=0，slot 初始空态 | 无 candidate 维持空态；candidate 建新身份 Alive；不是已有 Wall 的业务状态 |
| ST-C1 | Alive=1，Wall 初始活态 | Start 或 Dormant 恢复进入；兼容材料更新仍保留身份；End 条件成立则 Ended；无 End 且无支撑计数和距离门同时成立才进入 Dormant |
| ST-C2 | Dormant=2，同一 life 的可恢复状态 | 兼容 candidate 或有效 support 可恢复 Alive；满足 End 条件则终止。进入 Dormant 本身不新建身份 |
| ST-C3 | Ended=3，终态 | End occurrence 进入；后续无 candidate 可保留原终态 trace，新 candidate 分配新编号；不能按终态 trace 行重复推断 End |

证据 IS-C2:916–1075、1125–1271、1336–1341；状态持续在每侧 slot 和 carry 中。no-presence/far/thin 计数按被处理拍更新；`uti-birth_uti` 是 UTI 差。价格距离的 tick、处理拍计数、UTI 差和自然时间应分别解释，不能把所有 `_ticks` 无条件换成同一墙钟时长。

### OccurrenceRecord

| 编号 | 名称／码、方向和业务角色 | 单次含义、位置、对象和产生／消费 |
|---|---|---|
| OC-C1 | `Wall.Start.ByBigQuote / 4`；producer 输出，当前目标的主业务 occurrence | 新 Wall life 在当前侧建立；`wall_id`、Alive、band/core。产生于空／终态候选或 relocation 新建；当前拍 uti/ts；由数值 frame、packing 和 producer 消费方使用 |
| OC-C2 | `Wall.BandUpdate / 5`；同上 | 同身份位置更新达到发布门；来自 candidate/support 更新或 D1 无事件补发；当前拍 uti/ts，携带事件当时 status 和该拍末几何位置 |
| OC-C3 | `Wall.StateChange / 6`；同上 | Alive↔Dormant 转换；仍是原身份；当前拍 uti/ts，status 记录该次转换的目标状态 |
| OC-C4 | `Wall.End / 7`；同上 | 结束原 Wall life，status=Ended，含 reason；relocation End 与新身份 Start 可同拍，旧 End 保留旧对象位置 |

输入行情和 QT 是按轴消费的观测／参照表，F1/F2/F6 的当前数组值和 trace 样本不据此变成额外 Event。对于本次 `WallAssembler`，四类 sparse lifecycle occurrence 是主输出语义，`wall__stream*` 是同一批 occurrence 的物理表示；两份表示不能相加计数。BASE 对集成 FRP 目标的“producer 只是上游材料”分类不覆盖本目标。

| payload 字段 | 类型、可缺失性和语义 |
|---|---|
| `wall_id,uti` | 整数；事件有有效本地身份，uti 为发生位置；source/run/symbol 在绑定上下文补足 |
| `ts`／DataFrame index | 自然时间位置；与 uti 的当前运行换算尚未读回验证；chunk_end_ts 是物理分块边界，不是事件确认时间 |
| `event_type_code,side_code,status_code` | 数值码；side 为 1=bid/2=ask；status 为 1/2/3；D1 保留各 occurrence 的状态与顺序 |
| `band_lo,band_hi,core_price` | 浮点价格；D1 对该拍末仍占 slot 的同身份事件同步最终几何位置；不能据此说所有中间状态都等于 trace 末态 |
| `reason_code` | End reason 映射为 1=far_price、2=thin_contact、3=breakthrough、4=timeout、5=same_side_relocation；无 reason 的事件不会主动写 reason_code，混合 frame 可为空值，不能把所有非 End 都强写为 0 |
| `availability_code` | wrapper 为已形成 sparse 行加入 1；不能单凭该码证明输入完整或运行正确 |
| `chunk_id,chunk_end_ts` | producer 组帧追踪信息，不是业务身份或生命周期边界 |
| `occurrence_ordinal` | 同 timestamp 有重复时按原行顺序 cumcount 物理分流；无重复时可不出现；不是跨运行事件身份 |

证据 IS-C1:96–102,175–185,814–825；IS-C2:1604–1658；IS-C5:256–269。事件排序为 `(tick_index,side_rank,event_index)`；bid-before-ask 只说明实现顺序。`wall_id+uti+event_type_code` 未被 producer 声明为唯一事件键，不得用它盲目去重同拍输出。

## 4. 关键中间判断与 D1/D2/D4 delta

| 编号 | 输入、规则和输出 | 消费、结果暴露与证据 |
|---|---|---|
| ID-C1 | QT 严格自然日前值、F0 mid/hi、F1 LargeQuote、F2 thick/thin、F6 candidate 沿 BASE ID-01..06 复用；当前 QT 入口及 chunk 见 IS-C3 | F6 形成 Wall 材料；本 WALL 最终结果不持久化逐拍这些数组，`NOT_EXPOSED` |
| ID-C2 | candidate 到 core 的距离在门内并入；不兼容则旧 End(reason=5)+新身份 Start；brick gap 只清 support cluster | 身份创建、更新、恢复；事件可见，兼容/gap 判断值不暴露；IS-C2:953–1090 |
| ID-C3 | support ring 按 UTI 窗口过期重建；band=min/max，core 为强度加权价，复用 BASE ID-09 | 位置、距离及 BandUpdate；band/core 暴露，ring `NOT_EXPOSED` |
| ID-C4 | F7 距离以价差/tick_size 的 round 计算；near 是 best 或 last 至 band 任一距离≤near 门，far 标记看 last | F8/F9、Dormant、far End；逐拍距离未暴露；IS-C2:351–371,1100–1124 |
| ID-C5 | F8 有效 support=near 且非 thin；强度为 max(thickness_ratio,0)+max(large_ratio-1,0) | 加入材料、恢复 Alive、清 no-presence 与 far streak；support_flag 本身未暴露；IS-C2:473–489,1125–1185,1208–1215 |
| ID-C6 | thin contact 按近 band 命中和 thin 命中更新固定环形计数；最低 hits 与 thin/contact 比例共同参与 End | End(reason=2)；逐拍 ring/counter 未暴露；IS-C2:1190–1206,1222–1226 |
| ID-C7 | End 优先级为 far→thin/contact→breakthrough→timeout；relocation 在更早 candidate 分支独立处理 | End reason；IS-C2:1217–1252，reason 可见；无数量或合理性结论 |
| ID-C8 | 默认 wrapper 不传 recent_absorb_event_type，replay 将 None 转全零 | breakthrough pending 的 core 路径存在但默认实例没有真实 Absorb 接线；IS-C1:318–363、IS-C2:1420,1453–1454 |
| ID-D1 | 同拍已有事件时，只把属于最终 slot 身份的事件 core/band 同步到拍末几何；无事件但活墙位置相对发布基准／拍前的移动达到门，则补 BandUpdate | `_published_wall_id/_published_position` 跨完整 carry 传递，属于发布基准，不参与认墙；各 occurrence status 和顺序保留。relocation 旧 End 不改成新墙几何；IS-C2:198–203,1273–1322,1519–1530 |
| ID-D2 | 先判 End，只有无 End 才判 Alive→Dormant | 同拍符合 End 与进入 Dormant 时只走 End 分支；不等于禁止较早的 Dormant→Alive 恢复与 End 同拍，也不禁止 BandUpdate+End；IS-C2:1217–1271 |
| ID-D4 | `support_flag!=0` 先令 far_run_len=0；否则 last 距离≥end_far_ticks 时加一，未达距离时归零 | far End 的连续计数；不是任意候选或非零挂量都触发 reset；IS-C2:1208–1221 |

三项修复已由 Owner 采用，本 C 仅核其代码事实。未运行回归、未重算 D3 发生比例、未宣布任何 finding 在本 Run 关闭。D3 继续按 Owner 口径暂缓且不阻断后继。

## 5. ProcessingRelationMap

| 编号 | 上下游、条件及关系 | 身份／位置映射和信息变化 |
|---|---|---|
| PR-C1 | 一档行情、QT→对齐 tape→F1/F2/F6 | 观测获得资格，侧别保留；旧输入被阈值和 thin 门过滤，不创造额外持续身份 |
| PR-C2 | candidate→创建／并入／relocation | 空／终态分新号；兼容保留旧号；迁移为旧 End+新 Start，同 UTI 不代表同一对象 |
| PR-C3 | candidate/support→support ring→band/core | 过期、压缩和加权；同一 life，多拍材料可压缩成一个位置 |
| PR-C4 | support/距离/thin/age→状态与 End 仲裁 | D4 reset 和 D2 优先级按 §4；处理拍计数不等同于全部时间差 |
| PR-C5 | 内部几何→D1 发布同步／补发→四类 occurrence | 几何同步到当前身份拍末状态，但保留事件状态和顺序；此前亚门限位置变化不保证逐拍发事件 |
| PR-C6 | occurrence→sparse frame→packed streams | 文本码变数值，增 availability=1；同刻只分 result-key，不改业务时间；两路表示同一 occurrence |
| PR-C7 | 每拍 slot→state trace | 每侧每拍一个末态投影；同拍 relocation 的旧身份、较早状态可能不在末态 trace，须联读事件 |
| PR-C8 | 完整 carry→后续交易日 chunk | 两侧 slot、计数与发布基准延续，next_wall_id 传递；不能在 chunk 边界人为结束或新建 Wall |

证据分别为 IS-C1 的接线/导出与 IS-C2 的维护位置；BASE PR-01..09 的对应 producer 关系按本包 delta 更新，PR-10..15 的 FRP 关系保留为历史集成说明。

## 6. ParameterMap

28 个声明默认值已逐个由固定 `WallAssembler.params` 的 AST 字面量提取，完整清单在本调用 `checks/DECLARED_DEFAULT_PARAMETERS.json`；它是代码默认值快照，不是现场 `feature.ppdict`。BASE PA-01..28 的默认值和派生值在当前 producer 中保持该表所列值，定义位置更新为 IS-C1:681–710 与 IS-C2:119–167；BASE PA-29..31 仍为私有 eps、session policy 与未接线输入，均不增加公开参数。

| 参数组 | 当前声明／派生值与消费 |
|---|---|
| 实例身份 | `parameter_set_id=wall-default`，用于参数/receipt 身份 |
| QT/F0/F1/F2/F6 | `qt_freq=1d,qt_n=30,qt_quantile=.997,w_depth_ref_ticks=1200,large_quote_ratio_min=1,allow_zero_qt_fallback=false,thick_vs_hi_ratio=1,thin_vs_mid_ratio=.7,allow_thin_brick=false`；消费位置 IS-C1:287–317,737–748 |
| 基础尺度 | `p_wall_ticks=1,t_wall_ticks=6`；派生门见下行，消费位置 IS-C1:717–736 和 replay |
| 价格距离门，声明为 None | `near_band_ticks=1,far_band_ticks=2,connect_max_core_dist_ticks=1,band_update_min_shift_ticks=1,dormant_far_ticks=2,end_far_ticks=2`；默认由 p 或 2p 派生，消费 F7、连接、发布、Dormant、End |
| 处理/UTI 窗口门，声明为 None | `connect_gap_max_ticks=3,support_buffer_keep_ticks=6,thin_eval_window_ticks=3,dormant_no_presence_ticks=3,end_far_hold_ticks=3,break_after_no_presence_ticks=3,wall_dead_timeout_ticks=12`；分别来自 max(1,t//2)、t 或 2t，消费语义按 §3/§4 |
| 固定 policy 和 thin 门 | `allow_brick_join_dormant=true`，传 false 会报错；`thin_contact_min_hits=3,thin_contact_frac_end=.6` |
| 私有事实 | `eps_vol=1e-12`；当前 tape 的 session_ok 全 1；Absorb 可选输入默认全 0。参照 BASE 与当前接线，不把它们伪装成新公开参数 |

参数没有调节或替代；X 仍需回读完整实际参数，不能把上述静态表作为 ppdict 已验证的证据。

## 7. RunResultFieldMap

`PARTIAL` 表示代码侧可产生／保存的合同已定位，但本 Run 实际物化字段和独立读回尚未验证。`NOT_EXPOSED` 表示本锁定 wrapper 的最终输出没有选择该中间量。两者都不能当作当前结果中已经存在该列。

| 编号 | 结果载体、字段和读取路径 | 可用状态、键、同刻与缺失规则 |
|---|---|---|
| RR-C1 | `wall_assembler_sparse_events`；id/uti/ts、event/side/status、band/core、可选 reason、chunk 元信息、availability | `PARTIAL`；source+symbol+id 分组，side 校验并分层，ts/uti 定位；同拍多行保留。非 End reason 可能空或不存在；空范围下 result-key 是否存在须读回。IS-C1:175–198,811–826 |
| RR-C2 | `wall__stream`、`wall__stream__occNNNN`；与 sparse 同一批数值行，重复同刻时带 ordinal | `PARTIAL`；合并所有匹配 streams 才覆盖 occurrence，ordinal 恢复同刻顺序；不能再叠加 sparse。零行时 packing 返回空字典。IS-C5:256–305 |
| RR-C3 | `wall_assembler_state_trace`；uti/ts/chunk_id 及每侧 `wall_id,wall_side_code,wall_status_code,wall_band_lo,wall_band_hi,wall_core_price` 后缀列 | `PARTIAL`；ts/uti+side 为采样位置，身份仍带 source；0/Empty 是空槽，Ended 可重复。schema 与 append 路径已核；物理 dtype/fields 待读回。IS-C1:209–229,397–414,787–793,828–837 |
| RR-C4 | `<feature full_dir>/p1_receipts/wall_lifecycle.json`；actual/private parameters、source scope、code version、artifact location、状态等 | `UNCONFIRMED` 于本 Run；代码路径已定位。receipt 提供来源上下文，不是 Wall 对象；指纹含 HEAD 和 wrapper/core 实际源字节，dirty wrapper 不能被同 HEAD 掩盖。IS-C1:838–860、IS-C6 |
| RR-C5 | F0/F1/F2/F6 逐拍量：QT 对齐、mid/hi、large/thickness ratio、candidate 等 | `NOT_EXPOSED` 于本 WALL 最终结果；各自产生于计算接线，无最终 frame。X/G 若需转化分母，须先确认合法的上游读取／诊断证据，不能用 event 表倒算 |
| RR-C6 | far_run_len、no_presence_run_len、support_flag/strength、thin/contact counter、距离、完整 carry、发布位置基准 | `NOT_EXPOSED` 于本 WALL 最终结果；事件 checkpoint/内部数组可能存在这些值，但最终普通结果只选 sparse+packing，trace 只含 RR-C3 列。D4 连续计数回归不能宣称已有逐拍 far 列 |
| RR-C7 | chunk_meta/summary/end_state/carry_out/checkpoints/optional audit 等 runner frames | `NOT_EXPOSED` 于最终普通 keys；生成局部 frame 不等于持久化。trace 是单独追加的例外；IS-C1:194–207,822–837 |
| RR-C8 | 本 Run 正式 `full_dir`、fields/config 哈希、读回样例及实际 keys | `UNCONFIRMED`；本 C 没有运行或复用判定，不能引用旧目录冒充当前结果 |

公开执行/读取入口沿现有 Feature 框架为 `WallAssembler().run()` 及结果 `.F`；当前 chunk 导出真正执行的路径是 `P1DbaExportMixin.dump`→writer.finalize→`self.Dao.loadWith(full_dir)`。本 C 只读取该实现，没有调用它，也未确认实际 `.F` 属性展开。源中 `_impl` 返回计划对象并不意味着结果只含一个计划字段。

本目标的 `business_main_outputs=[OC-C1,OC-C2,OC-C3,OC-C4]`。中间/支持结果为输入与资格流、support/thin/distance 判断、slot trace、carry、receipt 和 packing。BASE 的 `wall_occurrences/wall_current_view/wall_diagnostics` 是 FRP 集成目标的输出名，不要求本次 producer 物化同名三路表。

## 8. 未确认项与完成状态

| 编号 | 具名缺口与已有边界 | 最小后续证据和可继续范围 |
|---|---|---|
| U-C1 | 工作树 wrapper 与锁定提交不同；实际 inspect.getfile、完整 ppdict 未取 | manager 安排 X 前按原输入核加载与参数，并对输入处理采用来源作对账；本 C 不恢复或采用现有修改。静态 U 仍可使用 |
| U-C2 | 本轮正式结果身份、Calendar、输入占位处理、单写者、哈希与独立读回未验证 | 由合法 X 取得 FeatureRunResultBinding；旧结果目录和“曾删 17 行”只作线索。本包不证明生产预检通过 |
| U-C3 | RR-C1..4/8 的现场 keys、字段、类型、空值和同刻顺序未读回 | 同一正式实例的 fields、receipt、配置及公开读取样例；到齐后补 U9/U10。X 可按固定目标继续准备，当前不能把代码字段当已物化字段 |
| U-C4 | 资格转换与 D4 计数所需逐拍中间量在 WALL 最终结果未暴露 | 后继确认合法可读的上游／诊断材料及其身份；未取得前明确统计覆盖缺口，不自行修改正式输出合同 |
| U-C5 | 当前代码事实还不是 D1/D2/D4 在本次全量结果上的回归证据；D3 仍暂缓 | 依既定 X/G/D 后继补证；本 C 不判合理性、不提出调整、不登记 finding 关闭 |

原 Skill 的七项完成条件已逐项自检：固定实现已定位；对象/身份/状态/occurrence 已区分；当前 producer 主输出与中间结果已分类；形成/更新/恢复/结束/引用可追溯；默认参数及消费关系已记录；字段、键和缺失含义已映射且未暴露量已具名；未知项没有写成确定事实。由于当前加载绑定与实际结果字段仍有 U-C1..3，本包按原生状态 **PARTIAL** 回交。它足以供 manager 安排固定范围的 X 和后续统计准备，不构成当前物化结果已验证或 Feature 已释放。

本 C 完成了原 D 要求的既有理解复用、受影响 delta 及最小统计事实核对。尚未满足的 U9/U10 现场字段核对明确保留；专业协议状态为 `IN_PROGRESS`。建议 manager 消费本包后按已采用 L0 安排 X，取得结果绑定后再补本包必要字段。没有签发或执行后继。

## 9. 规范化 FeatureUnderstandingPackage

以下记录编号均指向上文同名表，BASE 引用是 §1 的固定原件；不是待补占位。

```yaml
package_id: FUP-WALL-STAT-20261122-D001
feature_ref:
  feature_name: mquant.tis.hf.prel0.wall_assembler.WallAssembler
  code_version: daowei2026/tis@6618d4d147d6ebbe634e61facddf2c9a0b996982
  instance_ref:
    expression: WallAssembler(defaults-at-locked-commit)
    sof_name: TA_updto20240229_DBA
    symbols: [rb, m]
    start_date: 2021-01-01
    end_date: 2021-12-31
    calendar: night_end_at_2300
    binding_status: OWNER_LOCKED_REFERENCE_RUNTIME_UNVERIFIED
implementation_sources: [IS-C1, IS-C2, IS-C3, IS-C4, IS-C5, IS-C6, IS-C7]
business_objects: [BO-C1]
states: [ST-C0, ST-C1, ST-C2, ST-C3]
occurrences: [OC-C1, OC-C2, OC-C3, OC-C4]
intermediate_decisions: [ID-C1, ID-C2, ID-C3, ID-C4, ID-C5, ID-C6, ID-C7, ID-C8, ID-D1, ID-D2, ID-D4]
processing_relations: [PR-C1, PR-C2, PR-C3, PR-C4, PR-C5, PR-C6, PR-C7, PR-C8]
parameters:
  - BASE::PA-01..PA-28-as-verified-in-section-6
  - BASE::PA-29..PA-31-private-facts-as-qualified-in-section-6
run_result_field_map: [RR-C1, RR-C2, RR-C3, RR-C4, RR-C5, RR-C6, RR-C7, RR-C8]
business_main_outputs: [OC-C1, OC-C2, OC-C3, OC-C4]
intermediate_processing_results:
  - input-and-qualification-materials-in-section-2
  - judgments-and-support-rings-in-section-4
  - state-trace-and-transport-representations-in-section-7
unconfirmed_items: [U-C1, U-C2, U-C3, U-C4, U-C5]
completion_status: PARTIAL
```
