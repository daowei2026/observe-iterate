【Owner 指令｜停止继续 WALL 合理性，释放工作区并启动 Absorb 统计闭环】

一、收束当前 WALL Run

当前 Run：

run_id = OI-WALL-STAT-20261122-01
workspace = /dwdhome/fy/BASE_E6_2

Owner 现调整本轮 EAW 业务范围：

- WALL 不再继续做 m 品种的正式 X/G 和后续合理性发现；
- 不继续追求 WALL FeatureReleaseGate；
- 改为选择 WALL 的直接下游 Absorb 作为下一项合理性分析目标。

请将当前 WALL Run 收束为：

OWNER_TERMINATED / CANCELLED_BY_OWNER

准确含义：

- 这是 Owner 主动停止当前合理性范围；
- 不代表 WALL 业务任务已完成；
- 不代表 WALL 已通过合理性验收；
- 不得签 WALL FeatureReleaseGate；
- 不得形成虚假的 WALL UpstreamReleasePackage；
- 不得把 rb 部分结果扩大成 rb/m 完成；
- 所有既有 D、C、专业报告、rb 结果、m 失败现场、M001 和资源记录全部保留。

同时记录外部代码事实：

daowei2026/tis
branch = codex/wall-output-consistency-20261121
latest_commit = 179016111ed0394f92025313e46bd13534932a74

该提交已经处理 m 的开盘全空半秒占位输入问题，但当前 WALL Run 不再继续用它完成 WALL 合理性闭环。因此：

- 记录该修复事实；
- 不把它写成当前 WALL Run 已完成正式 m 重跑和统计；
- 不恢复 M001 后继；
- 不再签新的 WALL 专业 D。

对账并停止当前 WALL manager、executor、任何残留进程和写副作用。历史线程和记录保留，不复用于新 Run。

确认没有继续写入后，正式释放：

/dwdhome/fy/BASE_E6_2

二、当前 Campaign 路由变更

Owner 本次明确选择：

WALL 的直接下游 Absorb

作为 EAW 线下一项合理性目标。

EAW 正式架构中 Wall 同时直接供给 Build、AttackSegment 和 Absorb；本次选择 Absorb 不表示 Build 或 Attack 已完成，也不要求先运行 Build 或 Attack。

本次 Owner 指令覆盖此前“必须等 WALL FeatureReleaseGate 才能启动 EAW 下游”的安排。

新的实际关系是：

- WALL 合理性 Run 停止；
- Absorb 可以使用精确的 WALL 代码和 exact Wall artifact 作为技术上游；
- WALL 未完成全面合理性验收这一事实必须在 Absorb 的来源和限制中保留；
- 不得因此宣称 WALL 已释放；
- F 线独立继续；
- F → Q → V 的顺序不变；
- 本次不再要求 Absorb 等待 WALL/F 联合 Barrier。

三、注册新的 Absorb Run

请注册全新的独立 Run：

run_id = OI-ABSORB-STAT-20261123-01
work_id = OI-ABSORB-STAT-20261123
business_case_id = EAW-P1-ABSORB-STATISTICS-CLOSURE

工作区：

/dwdhome/fy/BASE_E6_2

物理执行方式：

execution_profile = CODEX_NATIVE_DIRECT
controller_skill =
daowei2026/cgpterm@fc966bcf5441701182339c992865504692f3a466:
.agents/skills/observe-iterate-longrun-v2-codex-native-controller/SKILL.md

角色：

- fresh Codex manager thread；
- fresh Codex executor:E1 thread；
- manager 与 executor 必须是不同线程；
- 不复用 WALL Run 的 threadId；
- workers = []；
- model = gpt-6.1-sol；
- reasoning effort = max。

三类角色统一采用专业控制版本：

daowei2026/observe-iterate@b8c2b513f0b08be6a1fa6782b71bf74a07faff0d

即：

1. controller／主控；
2. Absorb manager；
3. Absorb executor:E1。

manager 把该 commit 写入 TASK_PROGRESS 和各 D；executor Return 记录实际采用的专业控制 commit。

四、目标 Feature 与精确代码

目标 Feature：

AbsorbAssembler

业务名称：

EAW P1 Absorb 交互／吸收交互

精确代码：

repository = daowei2026/tis
branch = codex/wall-output-consistency-20261121
commit = 179016111ed0394f92025313e46bd13534932a74

Feature 入口：

mquant.tis.hf.prel0.absorb_assembler.AbsorbAssembler

源码位置：

hf/prel0/absorb_assembler.py
hf/prel0/absorb_assembler_core.py

本 Run 只以 Absorb 为目标 Feature，不自动把 Build、AttackSegment、Exhaustion 或其它 P1 Feature 扩入本轮专业范围。

五、正式业务来源

执行者必须亲自读取以下精确来源：

1. P1 六 Feature 与依赖：

daowei2026/feature-refinement-implementation-agent-evolution@
8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:
candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/
EAW_P1_PREL0_BASE_PRODUCTS_ENGINEERING_DESIGN_AND_VCC_V1_6_1_20260818/
02_FINAL_P1_ARCHITECTURE.md

2. Absorb DSU：

同一 commit：
.../dsu/P1-DSU-04_Absorb_交互_DSU.md

3. Wall / Build / Absorb 生命周期 occurrence 合同：

同一 commit：
candidate_gold_cases/eaw/taskpacks_and_checkpoints/p1/
EAW_P1_EXISTING_PREL0_BASE_PRODUCTS_AND_SPARSE_OCCURRENCE_V0_6_20260813/
03_WALL_BUILD_ABSORB_LIFECYCLE_CONTRACTS.md

4. 组装器业务规格：

同一 commit：
candidate_gold_cases/eaw/preL0_source_materials_20261102/原文快照/mquant/ssot/eaw/
03_assemblers_Wall_Build_Absorb_Attack_Exhaustion.md

5. 当前实际实现：

daowei2026/tis@179016111ed0394f92025313e46bd13534932a74:
hf/prel0/absorb_assembler.py
hf/prel0/absorb_assembler_core.py

历史材料可以作为来源索引，但不得用旧文档覆盖当前实际代码，也不得把当前代码行为自动当成业务预期。

六、正式实例范围

沿用当前 EAW P1 WALL 线的正式实例范围：

sof_name = TA_updto20240229_DBA
symbols = [rb, m]
requested_start_time = 2021-01-01
requested_end_time = 2021-12-31
calendar = night_end_at_2300
workspace = /dwdhome/fy/BASE_E6_2

不得自行缩短年份、换品种、换 Calendar 或换工作区。局部窗口只能标为 DIAGNOSTIC_ONLY，不能替代正式范围。

Absorb 使用当前代码中的默认正式参数。运行前保存并回读完整 ppdict。

关键默认项至少核对：

parameter_set_id = absorb-default
price_shift_ratio_thres = 0.01
t_track_max_ticks = 6
milestone_levels = [0.25, 0.5, 0.75]
same_track_tol_ticks = 0
visible_samepx_tol_ticks = 0
visible_guard_mode = off
large_quote_ratio_min = 1.0
allow_zero_qt_fallback = false
qt_freq = 1d
qt_n = 30
qt_quantile = 0.997

不得自行标定或改变参数。

七、exact Wall 上游要求

Absorb 必须消费与本次实例完全一致的 exact Wall artifact。

Wall 上游必须满足：

- TIS commit = 179016111ed0394f92025313e46bd13534932a74；
- WallAssembler 默认参数；
- 相同 SOF；
- 相同 symbols = rb/m；
- 相同 2021 全年范围；
- 相同 Calendar；
- 有可核验 wall_lifecycle product receipt；
- Wall artifact、receipt、state trace 和 Absorb 读取范围一致。

旧 WALL Run 中基于 6618d4d... 形成的 rb 部分结果不能冒充本 Run 的 exact upstream，因为代码版本和 m 覆盖均不一致。

若当前平台需要在 Absorb Run 中先物化 exact Wall artifact，可以把它作为 Absorb 的准确技术依赖进行生产或读取；但：

- 这不是恢复 WALL 合理性 Run；
- 不形成 WALL 合理性结论；
- 不把上游生产算作当前目标 Feature 的专业完成；
- 不自动扩展到 Build 或 Attack。

八、最小理解核对

U 只需形成足以支持本轮 X/G/D 的 Absorb 当前理解，不重做整个 EAW P1。

至少核对：

- 业务对象：一次绑定 exact Wall 的 Absorb interaction；
- identity：FeatureRunIdentity + interaction_local_no；
- 状态：AbsorbInProgress / AbsorbResolved；
- 正式事件：
  - Absorb.InteractionStarted；
  - Absorb.ConsumptionMilestone；
  - Absorb.Resolved；
- Resolved 类型及当前实现：
  - Breakthrough；
  - Aborted；
  - Blocked；
- Wall ref、side、tracked price、actual time、hit volume proxy、milestone、consumed ratio；
- Resolved 是局部交战结束，不自动等于 Fate；
- 当前／历史 interaction、track state、occurrence 与 publication 的区别；
- exact Wall 上游合同；
- chunk / trading-day 边界的状态和结束语义。

不要求先做 CAEGraph，不自动进入场景观察线。

九、正式运行与高置信发现

流程：

U 最小理解核对
→ X 正式运行或严格验证合法复用
→ G 全量行为统计及高置信不合理现象发现
→ Q
→ D 逐个诊断
→ 必要时 B / M
→ Release

G 阶段必须“覆盖面与高置信度并重”：

- 不因发现第一个候选就停止其余适用业务面；
- 不为追求找全而把所有边角现象升级成 finding；
- 参考类别不是穷尽清单、固定阈值或自动判错规则；
- executor 根据 Absorb 的业务对象、生命周期、Wall 绑定、事件顺序、数量关系、全量结果和业务常识自主判断高置信候选。

至少检查以下业务面，但该清单不是限制：

1. TrackStartCandidate → InteractionStarted → Milestone → Resolved 的数量与转化；
2. 按 rb/m、bid/ask、年份／时期和 Resolved type 的分层；
3. interaction identity 连续性和重复创建；
4. Wall ref 完整性、同一 interaction 内是否稳定绑定 exact Wall；
5. Started / Milestone / Resolved 的合法顺序；
6. Resolved 后是否继续出现 milestone 或更新；
7. milestone 是否单调、是否重复或跳级；
8. 未 Resolved interaction、样本末右删失和数据结束的区分；
9. active interaction 并发量、峰值、峰值持续时间和业务合理性；
10. 生命周期长度、零时长／极短／异常长 interaction；
11. Breakthrough / Aborted / Blocked 的数量、条件和相互关系；
12. 当前 active interaction 与历史 interaction 是否混用；
13. chunk / trading-day 边界是否错误终止、丢失或延续 track；
14. Wall 状态、Wall 生命周期与 Absorb interaction 是否出现不可能关系；
15. 正式事件、state/current view、summary/checkpoint 之间是否自洽。

输出：

- GlobalBehaviorProfile；
- FindingDiscoverySummary；
- CandidateFindingQueue；
- ObservationsNotPromoted；
- GlobalProfileGate。

十、D 责任逻辑定位

每个进入 D 的 finding 必须先：

1. 固定不合理表现；
2. 沿输入、Wall ref、track 状态、判断、事件输出回溯；
3. 定位最早使该表现产生的责任逻辑；
4. 解释该逻辑当前实际做什么；
5. 再判断业务上哪里不合理；
6. 再决定走 B、M 或关闭。

未形成 LogicLocalization，不进入正式修改讨论。

若问题来自 exact Wall artifact 或上游绑定：

- 不得为了让 Absorb 通过而错误修改 Absorb；
- 准确登记 upstream dependency finding；
- 区分上游输入问题、Absorb 绑定问题和 Absorb 自身行为问题。

十一、修改边界

本 Run 可以自主：

- 运行；
- 统计；
- 查源码和需求；
- 形成诊断；
- 写诊断脚本；
- 准备候选 patch 和新旧比较。

若要正式改变：

- Absorb 代码；
- Wall/Absorb 接线；
- 正式参数；
- 生命周期规则；
- Resolved 类型或输出合同；
- 数据处理；
- 正式范围；

必须先形成修改方案、责任逻辑定位、影响范围和验证方案，并回 Owner 确认。确认后才正式采用。

行为改变后必须完整回 X/G。

十二、Release

Absorb ReleasePackage 必须明确：

- 目标 Feature 只是 Absorb；
- exact Wall 上游的 commit、参数、范围、receipt 和 artifact 身份；
- WALL 合理性 Run 已由 Owner 停止，未形成 WALL 全面合理性 Release；
- Absorb 当前代码、参数、结果和统计；
- 所有高置信 finding 的状态；
- 已知限制和下游影响；
- 什么变化会使 Release 失效。

没有完成当前高置信发现和 finding 闭环前，不签 Absorb FeatureReleaseGate。