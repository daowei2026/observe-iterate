# C0003｜EawP1WallLifecycleFrp 处理骨架、双向核对与材料取舍候选

## 0. 身份、范围和当前结论

| 项目 | 值 |
|---|---|
| run_id / call_id | OI-EAW-WALL-20261116-01 / C0003 |
| invocation token | f30dbae896605726339bf8c9c393a6e6 |
| 执行人 | chatgpt:OI-EAW-WALL-20261116-01:executor:E1 |
| 原消费者 | chatgpt:OI-EAW-WALL-20261116-01:manager |
| delegation / work item | D001 / WI-WALL-SKELETON-001 |
| business task / question | OI-EAW-WALL-20261116-01-BT01 / Q-WALL-01 |
| stage_instance_id | M-step-1-WALL-B001 |
| analysis_round / expectation | 尚未建立 / not_frozen |
| 本报告状态 | **来源级专业结果已形成；现场绑定未闭环；D001 未完成** |

正式委派：`daowei2026/observe-iterate@40310127d8b700141f2ab1a17a1b114cbd1ff95b:longrun/runs/OI-EAW-WALL-20261116-01/delegations/D001/DELEGATION.json`。

本报告的来源 ID、准确提交/路径及实际阅读范围统一在：
`daowei2026/observe-iterate@298b35a68b32db01c136820bee63d82d0e630d99:longrun/runs/OI-EAW-WALL-20261116-01/calls/C0003/SOURCE_REGISTER.md`。
下文的 [F02]、[R03] 等均指该登记中的精确原件，不指搜索摘要。

**已经完成的实质工作：**亲自读 D001、专业步骤和三份输入；跟读影响骨架及取材判断的底层需求/源码；还原输入、业务变化形成、稀疏发布、typed ingress、状态事务和正式回读之间的边界；形成需求→输出和输出→用途的双向核对；指出输入整理文档之外需要保留的证据差异，并给出步骤 2 的材料取舍候选。

**尚未完成：**BASE 现役源码、加载模块、generated schema、二进制与既有市场产物的绑定；本 Run 的真实取数/回读；Worker 结果专业消费；manager 对步骤 1 及步骤 2 候选的接受。下文所有“代码事实”只适用于登记的历史 SHA。

步骤 0 按 Owner 跳过：不执行、不补验、不记完成。没有用本报告建立独立 S2/M05/G-RUN 阶段。没有取得 DATA_READY，没有启动正式合理性分析，没有修改业务源码、需求、参数或现役正式成果。

## 1. 采用专业方法及需求权威

按 control/02 原步骤 1，先问“判断当前特征是否可信需要知道哪些输入、实质处理和输出”，再沿真实调用核对，最后反查每个真实输出能够回答什么。没有按函数数目拆层，也没有要求所有内部函数都产出独立材料。[P01–P04]

有效需求阅读采用三层：

1. v0.6 的共同与 Wall 生命周期合同提供同一 life、Dormant、End、payload 和原因的业务基础；v1.6.1 的有效范围纠正覆盖旧条款。[R01、R04]
2. v1.6.1 的最终架构、Wall DSU、转换表、同 UTI 接线和 Python 投影给出实现与交接合同。[R02、R03、R05–R08]
3. A0 归档用于理解认墙与状态形成，但归档 README 明确“没有新增业务要求”。其中 hard-boundary reset、allow_brick_join_dormant=False 与所读实现不同；本报告保留差异，不把归档自动当作必须照改的现行规则。[R09、R10、T02、T03]

R01 已排除历史 source correction、因新证据 rerun、retraction/split/merge 和算法/参数换版流程。不能把它们重新塞成本 D 的前置工程；对同输入 deterministic replay、身份和正常新 tick 的边界仍需保留。[R01]

## 2. ProcessingSkeleton：实质业务链，而非新控制流程

```text
选定品种/日历/数据源与参数实例
  → 上游行情表 + QT 阈值表
  → WallAssembler 的大挂单/厚度/候选与 Wall 状态形成
  → 稀疏 Wall 变化、物理分流、receipt；另有 producer dense trace
  → wallOccurrenceIngress 元数据/行解码与输入资格
  → maintainWallLifecycle 生命周期事务
  → 正式 occurrence / current-update / diagnostics writer
  → 实际 generated ADT + Python .F 读取
```

下表 A～G 只是本次步骤 1 中的链内环节，不是新增管理阶段或独立分析对象。

| 环节 | 输入及实质处理 | 真实输出/状态与消费者 | 为什么需要观察；当前证明边界 |
|---|---|---|---|
| A. 形成可解释的输入上下文 | 当前品种、calendar、Sof 范围；加载 SubContinuousContract 和 VolQuant；QT 各侧按自然日零点找严格更早一条；session_ok 接线为全 1 | WallAssembler 所用行情、QT 和时间数组；不是 FRP lifecycle 的直接盘口输入 | 判定 Start/End 与行情是否在同一时基、是否存在阈值/暖启动缺口。加载接线已核；原始数组完整性及更深层上游算法未独立验收。[T05、I01] |
| B. producer 形成 Wall 变化 | 大挂单、相对厚度和墙砖候选作为内部计算；每侧有界 Wall 状态；候选兼容、支撑、变薄、远离、休眠/恢复、结束 | Start/BandUpdate/StateChange/End 的稀疏记录；每 tick 最后状态的 dense trace；carry 与 next_wall_id | 业务“认墙”发生在这里。FRP 不应重新认墙；内部度量不自动是独立 Feature 输出。两侧、生命周期和价格/时间门槛必须解释清楚。[T02、T03、R02] |
| C. 发布 source artifact | 实际 _impl 产生 P1ChunkedArtifactPlan；执行器按块追加 trace，最终选择 sparse_events，补 availability=1，形成 packed wall 流并暂存 receipt | wall_assembler_sparse_events、wall__stream 及同拍分流；wall_assembler_state_trace；wall_lifecycle receipt。runner 临时 summary/checkpoint 并不因此全成为独立正式 key | 核对 what-produced 与 what-loaded，不能从 docstring/临时返回推断所有材料均已落盘。已经核对 _impl 的选择，未执行写盘、未核整个 mixin。[T02、T04] |
| D. typed ingress | source 参数→receipt 与 artifact_location 校验→wall__ 前缀物理行→Wall 字段解码→当前 firing 批次成败 | 正常 FrpEvent [WallLifecycleOccurrence] 与 ingress diagnostics；部分 metadata/DBA 错误直接异常中止 | receipt/字段缺失不一定出现在诊断流。每物理行装箱及同拍多行必须无损；一行解码失败可压掉同批其他正常行。[F05] |
| E. 生命周期维护 | 接纳 typed list；当前 firing 引用/fingerprint 检查；逐条转换；全批成功才提交 | accepted occurrences；active-map Dynamic；每墙本批最后 current update；状态错误 diagnostics | 判断身份连续、状态转换、拒绝影响及当前状态语义；这里不计算新墙/阈值。历史静态路径已核，市场发生情况未知。[F02、F03] |
| F. 正式发布 | outer Fao 合并 ingress/state diagnostics；按 typed ADT 写出 | wall_occurrences、wall_current_view、wall_diagnostics 三路；并非每拍 full current map | 必须分开 occurrence、更新记录、诊断。逻辑事务一致不能自动推出多文件写入的故障原子性。[F01、F06] |
| G. Python 回读与观察入口 | 既有 wrapper、schema、FrpDbaDao/ADT；I03 使用 .run()/.F/root_seq | 三路真实返回对象、时间、schema/业务行；是否存在及怎样加载尚待现场 | TIS 包装 Cache/to_df 抛错与 FRP Cal 是不同层事实；不能凭类名推定可回读或运行新链。generated schema/binary/缓存必须定向核实。[T01、I03] |

### 2.1 必须保留的处理责任

`doWallLifecycleFrp` 直接调用 `wallOccurrenceIngress (wallLifecycleInput feature)`，再调用 `maintainWallLifecycle`，并合并诊断。不是先运行内层 Fao 的 generic load 返回值，再不加区分地交给外层。[F01、F05]

上游 SubContinuousContract、VolQuant、WallAssembler 和 WallOccurrenceFao 仅为本对象的必要输入/处理证据。此次没有对 Build、AttackSegment、Absorb 或整个 P1 发起独立分析。wrapper 的同名 Python 类不另算一个新的业务处理层。[R02、T01]

### 2.2 producer 的时间与参数不是一个模糊的“ticks”

T03 的参数派生把价格尺度 p 与时间尺度 t 分开：near/connect/band-shift 默认 p，far/dormant-far/end-far 默认 2p；gap/thin-window/no-presence/end-far-hold/break-no-presence 默认 max(1,t//2)，support 默认 t，dead-timeout 默认 2t。默认 p=1、t=6 来自 T02，而非本次现场 ppdict。

kernel 的 far_run_len、no_presence_run_len 按输入行递增；birth/gap 等又使用 UTI 差。不能一律换算成自然秒，也不能将 dormant_far_ticks 误作持续时间。T05 的 QT 对齐按自然日 anchor，不是仅凭变量名就可当成交易日/夜盘完全一致。实际输入间隔、日历和阈值可用时刻仍未核实。[T02、T03、T05]

## 3. 输出到底能表达什么

| 输出/状态 | 已核语义 | 不能直接推出 |
|---|---|---|
| producer sparse Wall rows | producer 明确发布的业务变化，保留原物理行与时间 | 每 tick 所有 band/core 微小变化均已发出；每行已经被 FRP 接纳 |
| producer state_trace | 每个输入 tick 结束后的 bid/ask 状态轨迹 | 所有中间 occurrence 后的瞬时状态；等于 FRP 稀疏持有状态 |
| wallLifecycleOccurrences / wall_occurrences | 当前成功批次内接纳并发布的 occurrence 列表；保留合法的多次变化 | 被拒绝输入也在其中；一条外层 Event 等于一个 Wall 变化 |
| wallLifecycleCurrent | 内存中的完整 active map；End 后从 active map 删除 | Python writer 每拍保存该完整 map；包含所有终态墙 |
| wallLifecycleCurrentUpdates / wall_current_view | 本批有变化的每堵墙最后状态；可含 Ended 更新 | 完整历史过程；任意截窗都能从空 map 正确恢复当时状态 |
| wall_diagnostics | ingress 与 DSU 状态错误的 typed envelope | 所有加载异常均在其中；没有诊断就证明行情无缺失 |
| I03 run-result | 执行与回读标志、实际返回 key/schema/计数及少量样例 | 完整材料包、业务合理性、完整链新算成功、版本匹配或覆盖完整 |

以上对应 [T02、T03、F01–F06、I03]。

### 3.1 一条对后续观察非常重要的新区分

producer 的 band/core 可在支撑更新中改变，只有达到 band_update_min_shift_ticks 才发 BandUpdate；FRP 的 current view 保存最近被接纳 occurrence，而不直接读取每 tick trace。[T03、F02、F04]

因此后继不能预设：

```text
producer dense state == FRP current == 图上逐 tick 墙状态
```

首先应分别检验“producer 发布了什么”“FRP 接纳并维护了什么”“消费者把这种稀疏持有状态解释成什么”。未发事件的小变化不能被观察脚本静默补成 FRP 正式输出；反过来，两条轨迹不同也不能不看发布口径就认定 lifecycle 维护失败。这是取材语义，不是已经完成的 R 对照结论。

### 3.2 current 的恢复必须带边界条件

对更新表恢复 active map 时，Present/Dormant 更新对应插入/替换，Ended 对应移除；但还须有正确 namespace、顺序、开始前历史/可信 seed，以及对拒绝批次的说明。仅把窗口第一条记录当作墙出生，或只取窗口内最后一行当完整 current，均不具备该解释资格。[F02、F04、F06]

这只是说明所需材料，不在本 D 新造正式状态恢复器或写入替代产物。若任意时点恢复所需 seed 不可得，要明确限制可回答的窗口/墙，不能假设空状态。

## 4. 双向核对：需求需要什么，实际保留/丢失什么

以下“差异/风险”是源码与合同的对照，不是已在真实市场中观察到异常，也不是正式 R 的 SUPPORTS/COUNTERS。

| 编号 | 需求/观察需要 | 亲自核实的历史实现事实 | 专业判断与材料影响 |
|---|---|---|---|
| B01 认墙责任 | producer 形成变化，FRP 维护状态，不重认墙。[R02、R03] | outer Fao 只接 ingress→maintainer，识别参数在 WallAssembler。[F01、T02] | 责任骨架有据；不能用 FRP 状态内部一致证明认墙业务合理。需要 source rows 及必要市场参照。 |
| B02 身份域 | Wall FeatureRunIdentity + local no；同 life 保持，End 后新 life 新引用。[R03、R04] | WallIdentity/WallRef 只含 local no；实际 source 在流/receipt 上下文；typed row 不自行携带完整 run namespace。[F04、F05] | 观察/导出必须附 exact producer artifact/namespace，不能跨实例按相同 wall_id 合并。现场绑定是核心缺口。 |
| B03 状态转换 | Present↔Dormant 保持身份；Band 不应改变 presence；错误不是 End。[R03–R05] | Start 必须 Alive；Band 只许同 presence；PresenceChange 必须切换；状态错误保留原 state，输出 diagnostic。[F02] | 可将转换作为后继最小预期来源，但未冻结、未实证；诊断和无变化要分开。 |
| B04 End 终态 | End 后普通更新禁止；新 life 用新引用。[R03、R04、R08] | End 输出 Ended update 后删除 active-map 条目；无独立终态身份集合。后续同号新 Start 在缺失状态下可接纳；普通更新走 before-start 错误。[F02] | 不能因存在 WallUpdateAfterEnd 构造器就宣称完整终态保护。需区分 producer 不重用前提与 DSU 自身防护；未证明市场中曾重用。 |
| B05 幂等范围 | all/exact duplicate 不重复输出，conflict 不推进状态。[R08] | 当前 firing 内 SHA1(show occurrence) 判重；每批 ledger 清空。[F02、F03] | 已核范围是当前批，不是永久历史。跨批 exact/conflict 的效果需原始序列及实际输入资格支持，不能由类名推出。 |
| B06 同 UTI 无损与身份 | 同时发生的多 occurrence 不丢、不改时间；ordinal 不是业务身份。[R04、R06] | 物理 __occNNNN 分流保留行；decoder ref=wall:local:uti:eventCode，不含 ordinal；DSU 按输入 list fold。[T04、F05、F02] | 保留 physical key、ordinal、batch/row、业务 UTI/事件码和引用。不能先按 ref 去重、按时间排序就称业务顺序已定。 |
| B07 同类型同拍可能性 | 多变化是否可无损表达，需要实际 producer 语义与引用能配合 | kernel 的候选支撑和普通支撑有两个 BandUpdate 发出点；decoder 引用不区分两个同墙同 UTI 同码记录。[T03、F05] | 形成明确的潜在碰撞检查点，不宣称两分支在真实样本已同时触发，更不构造输入代替观察。后续应在获准真实材料中查重及对照。 |
| B08 拒绝范围 | 一次合法 occurrence 的状态/history/publication 一致。[R05] | ingress 任一行错误拒绝当前批正常流；DSU 任一转换错误回滚整批，其他墙合法变化也不发布。[F05、F02] | 实现保证的是批事务，影响范围大于单条。要保存批边界及被拒 source，判断 current 保持不变是因无变化还是拒绝停留；是否合业务要求留给后续有据对照。 |
| B09 payload 与原因 | 变化后的 band/core/state、来源、交易日、可解释原因；不可得明确标记。[R04] | decoder 为 End 只读取 reason_code，产生 producer-reason-code-N；Start/PresenceChange 无 reason 参数；typed payload 没有独立交易日/source_run 字段。[F04、F05、F06] | 不把 producer 全列当 typed 已保留。End 位置需前序状态/source 行；原因名称需准确编码来源，未知码不得猜。缺失不算业务 End。 |
| B10 current 的语义 | 消费者能读取每墙当前状态。[R07] | writer 保存 currentUpdates，不存完整 map；同批同墙多变化只保留最后 current。[F02、F06] | current 行数少于 occurrence 行数可以是预期压缩；完整过程需 occurrence，任意时点状态需 seed/历史，不能互相替代。 |
| B11 空与失败 | 无 occurrence、缺数据、不可用、拒绝及加载失败需要区分 | availability 非 1 被拒；receipt/fields/列长/无匹配 key 可能直接异常；producer 空 packed frame 返回无 packed streams。[F05、T04] | 有效空的实际物理表示需查，不能自动把缺 wall__ key 当 valid empty，也不能只查 diagnostics。需加载结果、metadata、原始行及缺失说明。 |
| B12 current 与市场细节 | 输出要能按声明口径解释，而非图形看起来一致 | producer dense 更新与稀疏发出有阈值边界；FRP 只接纳稀疏流。[T03、F02] | 先核 sparse→typed→current 关系，必要时再看 dense 与行情；不得静默插值重写正式含义。 |
| B13 chunk 与 Dormant 权威 | 必须清楚何时同 life、何时终止 | 归档 A0 建议 reset、Dormant 不接砖；代码跨块 carry，强制 allow_brick_join_dormant=True，False 报错。[R10、T02、T03] | 有明确差异但未找到本次已读原件中的逐条裁决；保留两方依据。不能照旧规强制 reset，也不能从实现反推业务已批准。 |
| B14 回读与可运行性 | 正式三路输出通过既有链读取。[R07] | Fao 为 Cal；TIS 包装 Cache、to_df 主动抛错；I03 以 .run/.F/ADT 读取，先查 fields。[F01、T01、I03] | 静态上有正式 writer；运行组合仍需实际 loaded path/schema/binary/artifact 证据。失败不自动改用 EawBattleP 扩大对象。 |

## 5. 对已有运行脚本的专业消费

I03 已固定 `TA_updto20240229_DBA / rb / night_end_at_2300 / 2020-12-01～2021-02-22` 和默认实例，读取前要求已有 fields.json，180 秒 alarm，并分别记录 run_succeeded 与 readback_succeeded。脚本捕获异常，故进程退出 0 不能单独判成功。以上是亲自读到的脚本逻辑；脚本说明中的历史成功不是本 Run 回执。[I03]

还需补充四个解释边界：

- fields.json 存在只是一项命中检查，不证明相关 DBA 文件、receipt、schema 全部匹配，也不证明当前框架 .run 分支一定不会触发计算。
- 循环遍历的是实际 result.F.items()，没有显式断言预期三个 key 都出现；不能只凭两个 success flag 验收三路完整。
- event_count 是外层时间轴数量；business_rows 的含义依赖真实 root_seq schema。尤其 diagnostic envelope、内部 error list 和业务 occurrence 数不能混作一个口径。
- 最多三处非空样例用于证明接口形态，不足以覆盖完整 life、同拍变化、拒绝批次、窗口种子或真正场景；不构成步骤 5～7 的材料包。

本 D 不直接执行这段长窗口入口。现场核查优先读已有 metadata 和明确的只读 DAO；只有不触发重算的既有材料读取才落在本次事实动作边界。任何必须计算、生成 schema、重建 binary 或改正式文件的需要都原样回报，不在 Worker 自行扩大动作。

## 6. MaterialRequirementSet 候选：供 manager 接受，不是已生效输入

材料 ID 只是本报告内的候选索引。所有范围均指后续由 manager 接受的观察范围，不预先把 I03 全窗口定为正式必需范围。没有在本次取得这些材料。

| 候选 | 取舍 | 要回答的问题与最小内容 | 不可替代/条件 |
|---|---|---|---|
| MR01 来源与实例 manifest | 必须准备 | 顶层与 Wall source 的 ppdict/ppid、artifact/receipt、代码及相关 dirty 状态、实际加载模块/schema/binary 来源、数据源/品种/calendar/时间口径、真实加载范围与参数有效值 | HEAD 不能替代产物生成版本；local wall_no 不能替代 namespace；未知版本明确 unknown |
| MR02 正式三路材料 | 必须准备 | 选定范围的 wall_occurrences、wall_current_view、wall_diagnostics；保留 typed 字段、原批次边界、时间与实际基数；配套加载错误/未产生输出记录 | current 不能替代 occurrence；少量样例不能替代正式选定范围；诊断缺 key 不等于零错误 |
| MR03 对应 producer 输入流 | 必须准备 | 同一 source 的稀疏 Wall 物理行、result-key/ordinal/业务 identity、UTI/时间、事件码/状态/价带/原因及 receipt；能与正式输出对应 | 不预去重、不改时间；应可解释接纳/拒绝/未加载；不是重跑另一个 producer |
| MR04 市场与时基参照 | 必须准备最小参照；深入成因字段按条件增补 | 同品种/同日历的 last/bid/ask 价格与必要量、tick_size、原 ts/linear time/UTI 关系、交易日/夜盘及输入可用性；解释 Start/认墙门槛时还需实际 QT 与其生效时点 | 只取本问题所需市场窗口和上下文，不全市场盘点，不独立评价全部上游特征；不能用示意输入填缺 |
| MR05 观察起点与生命周期边界 | 必须准备 | 对要解释 current 的窗口，有前序 occurrence/可信起点状态或完整 life；区分运行边界、显示边界、业务 End；记录未闭合墙 | 缺 seed 时限定可解释范围，不能当空 map；末尾无 End 不自动判漏发 |
| MR06 producer dense 与判定中间量 | 条件准备 | 当稀疏持有状态与市场/producer trace 的差别影响结论，或需区分 start/dormant/end 成因时，取同版本已有 trace、支撑/厚度/薄触/远离信息 | 先复用已有局部证据；没有现成中间量不自动授权重算/加 debug；不要求全部历史 dense 表 |
| MR07 对齐观察图/CAEGraph | 可选，依实际观察需要决定 | 为 MR02–06 提供定位和联看；图层需声明 producer 状态、FRP 状态、变化点与诊断各是什么 | 图不能替代源数据；当前没有核实已有可用图，也不把画完图设成本 D 完成条件 |
| MR08 不准备项 | 本轮不准备 | 人工受控市场替代品、其他 P1 产品全链、全资产盘点、全量新算、盲调参数、通用 revision 平台、旧 Run 完成状态 | 若真正新增业务范围，回 manager 明确理由；不得偷偷扩入 |

MR06 没有被降为不重要：当具体问题离不开成因字段时，它就成为该问题的必需材料。它的条件性是避免在尚无问题时无差别导出所有内部数组，不是用缺证降低父目标。

## 7. 已证事实、现场缺口和当前合法动作

### 7.1 可保留的结果

可保留为“指定历史版本已核”的内容：第 2 节处理责任和数据形状、第 3 节输出角色、第 4 节具体源码/合同差异，以及第 5 节脚本能力边界。即使 BASE 当前版本不同，这些准确历史事实也不清零；只对受版本变化影响的行补核。

可作为后续材料设计候选的判断：必须保持 namespace、batch/row 与双时间、完整 occurrence 和 current-update 区分；读取空结果需要诊断及加载上下文；稀疏持有状态与 dense state 分开。它们尚未被 manager 接受为步骤 3 输入。

### 7.2 缺口登记

| gap_id | 现在不知道什么 | 影响范围 | 最小解除办法 / 责任 |
|---|---|---|---|
| G01 | BASE 相关实际 checkout/dirty、import 实际文件、所用 binary/schema，是否对应所读历史版本 | 骨架能否称现役事实 | Worker 定向读相关文件/元数据/加载路径；E1 判断差异影响，不做全资产盘点 |
| G02 | 默认实例与其 Wall source 的真实 ppid/full_dir、receipt、三路字段/schema，产物生成版本和时间覆盖 | 数据源选择与读取资格 | Worker 在既有环境检查实际绑定；不触发 .run/.rerun 计算；缺失准确列出 |
| G03 | 现有只读回读入口是否能得到三路真实 ADT，实际样例/基数与批次怎样对应 | 输出形态和后继最小落地 | 安全只读路径可用时取少量已有真实记录；不可用则保留具体原因；E1 专业消费，不当正式材料验收 |
| G04 | source UTI 与外层事件时间、日历/交易日/夜盘、窗口种子和未闭合 life 的实际对应 | 时间对齐及任意时点解释 | 当前只查现有 metadata/少量记录；正式范围与充分性随步骤 2 接受后确定 |
| G05 | 归档 A0 的 reset/Dormant 条款与当前采用方法之间的完整权威关系 | 把哪项差异写成“应当” | E1 已保留准确双方来源；manager 后继决定必要定向澄清，不让 Worker 发明业务裁决 |
| G06 | 潜在同拍引用冲突、跨批重复、终态重用、整批拒绝是否在真实材料中发生及影响 | 后续场景选择与正式对照 | 在获准的真实材料中核对；当前不以静态路径或合成测试宣称市场问题成立 |

G01–G03 是本 D 现场闭环的核心，适合一张有界事实 W。G04 只取现成局部信息。G05/G06 不在该 W 变成全量业务分析或测试工程。

### 7.3 为什么此时需要 W，而不是把全部分析交给 Worker

本席已完成需求/源码双向核对，已明确缺什么事实及其用途。只有实际 import、二进制/生成 schema、现役字段与市场 artifact 不能从 GitHub 历史源码推得，因此为这些事实签发 W001。W 的唯一业务接收者仍为本 E1；Worker 不判断步骤 1/2 是否合格、不冻结预期、不形成合理性结论、不直接交 manager 绕过本席。

Worker 的物理线程、BASE 单写者和实际配置由主控在首 W 前核实，本席没有替其声明完成。W 原件发布及正式 Return 的引用不构成实际送达/执行证据。

## 8. 回交与完成边界

| 层次 | 本调用的真实状态 |
|---|---|
| C0003 本次专业产出 | 已形成来源登记、ProcessingSkeleton、双向表、事实/缺口和步骤 2 候选；为后续现场核查提供明确依据 |
| D001 范围报告 | **部分完成**；须取得或有据收束 G01–G03，先由 E1 消费 Worker 结果，再交 manager |
| 步骤 1 验收 | 尚未由 manager 接受；本报告不代作 Gate |
| 步骤 2 | 仅候选；未经 manager 接受不能成为后继正式输入 |
| M 步骤 5～7 / H1 | 未取得并验收本 Run 正式市场材料；未交接 |
| R / 父任务 | 未启动本轮正式 R；父任务未完成 |
| Worker 消费 | 当前无 Worker Return，accepted_worker_refs=[]；不填虚假通过 |

后继：主控按正式 Return 引用的 W 原件，完成真实通道/单写者核验后派 W1；结果先以新调用回 E1。E1 核对现役差异、真实读取边界及缺项，保留/修订本报告，再向 manager 提交 D001 的完整或具名限定结果。没有必要向 Owner 请求普通节点审批；若现场存在明确权限或范围冲突，报告具体动作/失败/所缺条件，不以泛泛“等待确认”替代工作。

本报告及其来源没有引用尚未存在的 W/Return commit；后续正式 Return 以已发布原件的准确提交单向引用。本次不改写 TASK_PROGRESS、MD001、Owner/Binding 或主控运输记录。
