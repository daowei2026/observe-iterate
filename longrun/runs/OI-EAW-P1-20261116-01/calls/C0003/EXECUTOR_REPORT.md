# C0003｜D001 专业执行报告

> **run_id**：`OI-EAW-P1-20261116-01`  
> **call_id**：`C0003`  
> **invocation token**：`9a2574ceaaf2792e1373b387fb825d24`  
> **delegation_id**：`D001`  
> **executor**：`chatgpt:OI-EAW-P1-20261116-01:executor:E1`  
> **return_to**：`chatgpt:OI-EAW-P1-20261116-01:manager`  
> **原 D001**：`daowei2026/observe-iterate@e03fdd881209a1d4ae3e45c7a1e777e9d6a9b880:longrun/runs/OI-EAW-P1-20261116-01/delegations/D001/DELEGATION.json`  
> **专业范围**：M 步骤 1～7 + R0/R1；不做正式 R2 `SUPPORTS/COUNTERS`，不替 manager 宣布 H1、G-EXPECTATION-FREEZE 或父任务 Gate。

---

# 0. 回交摘要

## 0.1 专业完成状态

D001 规定的专业工作已完成到可回交状态：

- M 步骤 1～7：已形成处理骨架、材料取舍、观察方法、复用路径、真实材料取得、质量检查和交接；
- R0/R1：已形成 `BusinessIntentStatement`、`ExpectationRegister`、三层 `InputSuitabilityAssessment`、`ScenarioExpectationSet`、`OpenQuestions` 与候选冻结建议；
- 真实 Project Source 原件由本 E1 独立读取并复核字节数、SHA-256、ZIP CRC、manifest、timespans、日历、对象、字段、记录数量、身份/时间异常与局部探索场景；
- 本轮未签 Worker Order；不存在 Worker 结果被绕过或直送 manager 的情况；
- 未执行正式 R2；文中出现的样本定位均标为探索，不构成 `SUPPORTS/COUNTERS`。

本 D 的专业报告范围可记为 `REPORTED_COMPLETE`；但材料交接的真实状态只能是：

```text
PARTIAL_WITH_LIMITS
```

这不表示 H1 已通过，不表示预期已冻结，也不表示 P1 产品合理或不合理。

## 0.2 一句话结论

当前 CAEGraph 包不是“一套已经满足八类 P1 正式合同的产品输出”。它是一套真实、可读、范围明确的**派生产品表 + 图窗裁剪快照 + 绘图绑定材料**：

- 能直接支持 Wall / Build / AttackSegment / Absorb / F4 lane 的字段、生命周期形态和局部场景探索；
- 不能以图层或表名证明完整产品合同；
- FormationEvidence、formal Barrier、F3 没有独立正式产品表；
- F4 仍是 tactical/structural 两条 source lane，不是 canonical union；
- Attack 时间绑定存在系统性歧义；
- 缺少 `P1RunManifest`、`source_run_ref`、typed refs、完整 missingness/availability 和生产版本，因此不具备八类产品一体化正式 R2 资格。

## 0.3 本次正式成果

同目录成果：

1. `EXECUTOR_REPORT.md`：本报告；
2. `D001_DATA_AUDIT.json`：机器可读原数据与产品覆盖审计；
3. `D001_EXPECTATION_REGISTER.yaml`：WORKING 预期、场景、冻结建议、正式 R2 最小输入和补证请求；
4. `PRO_RETURN.json`：在上述成果先发布后另行提交的 V2 executor Return。

---

# 1. 实际读取与执行清单

## 1.1 正式任务、身份与方法

本 E1 亲自读取并采用：

- C0003 `FULL_ASSIGNMENT.md`：
  `daowei2026/observe-iterate@df89542e658773701d78e366f403111f2a462530:longrun/runs/OI-EAW-P1-20261116-01/calls/C0003/FULL_ASSIGNMENT.md`
- C0003 `INVOCATION.json`：
  `daowei2026/observe-iterate@ce02f15439c7a0685fb777ee2dc79d3ee59f2778:longrun/runs/OI-EAW-P1-20261116-01/calls/C0003/INVOCATION.json`
- D001 原件；
- H0 决定 `MD-0001.md`；
- `OWNER_START.md`、`RUN_BINDING.json`、`RUN_RESOURCE_BINDING.json`；
- 固定方法提交 `7e240b650b6ba6274b0263e34f5b0616a9a8ff1c` 下的：
  - `longrun/professional/PRO_EXECUTOR_GUIDE.md`
  - `control/02_L1_观察材料准备流程.md`
  - `control/04_L2_节点输入输出登记表.md`
  - `control/05_三级Gate及后继路由.md`
  - `skills/reasonableness-analysis/README.md`
  - `business-expectation-derivation/SKILL.md`
  - `business-evidence-comparison/SKILL.md`

步骤 0 的完整重复资产盘点按 Owner 特例跳过，记录为“跳过”，不是完成。

## 1.2 Owner 原始业务设计与 P1 候选合同

已亲自读取：

- Owner 原设计 §1.1.1、§1.1.2：
  `daowei2026/feature-refinement-implementation-agent-evolution@8d58ddd3392a3e67ef5ba44adf2c4cd0c9077f9f:candidate_gold_cases/eaw/preL0_source_materials_20261102/原文快照/mquant/ssot/eaw/01.04.01 EAW叙事一个小范围完整的部分-preL0细节.md`
- P1 候选任务包 `TASKPACK.md`、`P1_PRODUCT_AND_OCCURRENCE_MATRIX.csv`、`AUTHORITY_BY_SUBTREE.yaml`、`SOURCE_BASIS_AND_LIMITS.md`；
- Wall / Build / Attack / Absorb / Formation / Barrier / F3 / F4 的定向合同；
- output authority、identity/replay、Numba parameter surface、acceptance scenarios/anti-golds。

权威边界已保留：

```text
candidate taskpack status = replacement_requirement_candidate_for_owner_review
included_does_not_mean_owner_accepted = true
```

因此本报告不会把 V0.6 候选包冒充 Owner 已逐项接受的永久需求。

## 1.3 Project Source 原数据的 E1 独立核验

实际读取：`/mnt/data/caegraph-data-30tick.zip`

```text
实际字节数：16,654,307
预期字节数：16,654,307
实际 SHA-256：73e7c5f289d7b25f08f11cffda7315ad2dad3f8c323715425afdd485e15c4233
预期 SHA-256：73e7c5f289d7b25f08f11cffda7315ad2dad3f8c323715425afdd485e15c4233
ZIP 成员：446
CRC：全部通过
manifest assets：442
manifest evidence features：12
```

这是真实 E1 现场读取，不沿用 manager 的读取结果充当本 E1 证据。

## 1.4 脚本读取与运行边界

固定脚本原件：

```text
caegraph-scripts.zip
31,319 bytes
SHA-256 5eaf500616316ef7764cd30eb7467f2db3a6c85e45aa3b4f958becbc7818e8eb
4 members
```

已从展开副本提交 `036f24f4a4b7ca898280d8ed58cbf9c0b3634744` 直接读取：

- `caegraph_definitions.py`
- `snapshot_data.py`
- `run.py`
- `README.md`

定向确认：

- `run.py` 从独立 data 目录读 manifest/timespans，可列出 overview、multiscale、tick 图窗；
- `--check` 逐页构造并检查图数量，不生成 HTML；
- `snapshot_data.py` 不访问原 Aidata run、不重算上游，只读随包 CSV/NPZ；
- `caegraph_definitions.py` 的通用 `EvidencePlotter` 把 feature view 按 point/line/segment binding 变成图元；
- 图窗优先读取 `window_snapshot`，否则经 `read_evidence_frame` 和页面级 cache 读取/裁剪；
- UTI point/interval slicing 与自然索引绘图属于构图层，不改变源产品形成权。

当前会话依赖探测：

```text
bokeh：可用
pandas/numpy：可用
mquant：缺失
m3tt：缺失
```

所以未声称 `run.py --check` 已通过；完整 Bokeh 构造未运行。数据层核定不依赖这一步，故未签 W，也未把依赖缺失解释为业务反证。

---

# 2. M 步骤 1｜ProcessingSkeleton

## 2.1 业务输入与受限数据前提

Owner 固定的 Wall 前提：

- 半秒级 tick 聚合；
- L1 买一/卖一价格与挂单量；
- 成交；
- 看不到五档盘口、独立撤单 feed 或完整 L2/L3 深度。

因此 Wall 是在受限观察下随时间形成、更新、结束的流动性认知对象，不是单 tick 大挂单或一条绘图线。

本包对象与时间基础：

```text
symbols：rb / hc / i
block：blk@steel
calendar：night_end_at_2300
half-second slots：103,316,400
compressed calendar segments：10,219
calendar first：2013-01-04 09:00:00.500
calendar last：2024-02-29 15:00:00
```

图窗范围：

```text
overview/daily：1
big/30m：6
mid/1m：18
small/5s：54
tick raw windows：30
all tick locators in timespans：148
```

只有前 30 个 Tick 窗随包行情；其余 118 个只保留定位时间窗。

## 2.2 产品生产权与共用/解耦关系

按 Owner 原设计与候选合同，正确的专业骨架是：

```text
受限 L1 + 成交
  ├─ canonical Wall producer
  │    └─ Wall lifecycle sparse occurrences
  ├─ Build producer ─────────────┐
  ├─ AttackSegment producer ─────┼─ each references canonical Wall
  └─ Absorb producer ────────────┘

Attack/F4 source evidence
  ├─ AttackFormationEvidence producer
  ├─ tactical lane
  ├─ structural lane
  └─ canonical F4 union

Wall End / switch / direction relation
  └─ formal WallRelationBarrier producer

per-symbol/per-UTI directional measurements
  └─ F3 dense measurement + availability

P1 typed ports
  └─ FRP/Haskell consumes formal products; does not rebuild them
```

关键边界：

- Wall 定义不依赖 Attack/dense；
- Build、Attack、Absorb 共用 canonical Wall，但各有独立身份与生命周期；
- 一堵 Wall 上允许某些产品发生、另一些不发生；
- Formation gap 不自动是 Barrier；
- F3 是 dense measurement，F4 是 sparse occurrence；
- tactical/structural 双 lane 命中必须 canonical union，而不是两表 concat；
- 图层和显示线段不是产品形成权。

## 2.3 时间与身份

正式合同至少应区分：

```text
actual/business time
business_end
closed/confirm time
source_run_ref
product/occurrence typed ref
wall_ref / build_ref / segment_ref / interaction_ref
revision/replay scope
```

当前材料主要使用 symbol 内 local numeric IDs 和 UTI，没有 `source_run_ref`，不能承担跨 symbol、跨 run 的稳定身份。

## 2.4 当前材料的数据阶段

本包同时含：

1. K 线/Tick 基础图数据；
2. 已落盘的派生 evidence 表；
3. `window_evidence` 裁剪快照；
4. `wall_segments` 等显示区间；
5. 通用 plot binding / hover / style 信息。

不能把 2～5 统一称为“源业务产品”。尤其：

```text
source occurrence ≠ clipped window view ≠ display segment ≠ Bokeh glyph
```

---

# 3. M 步骤 2｜产品—证据—场景覆盖矩阵

| P1 产品 | 权威/成熟度 | 业务主语与 occurrence | 时间/身份合同 | 当前 asset/字段证据 | 当前证据状态 | 对本轮影响 |
|---|---|---|---|---|---|---|
| Wall | Owner 高层意图 + 候选详细合同 | 一堵 canonical Wall 的 Start/State/Band/End | wall_ref；actual/confirm/end；source_run | 45,698 lifecycle rows；7,428 display segments；local wall_id | `PARTIAL_DIRECT` | 可做生命周期/字段/局部场景探索；不可证明完整生产合同 |
| Build | V0.6 candidate | Start→Milestone*→Stop 的独立加固过程 | build_ref + wall_ref；milestone identity；stop reason | 131,219 rows；Start 43,035 / Milestone 45,149 / Stop 43,035 | `PARTIAL_DIRECT` | 可看形态与 local join；缺阈值身份、run ref、完整 reason |
| AttackSegment | V0.6 candidate | 一条完整进攻段 occurrence | segment_ref；business_end；closed_at；completeness | 17,856 rows；有 local wall ref、start/end UTI 和部分聚合 | `PARTIAL_DIRECT_TIME_AMBIGUOUS` | 精确时间正式对照被阻断 |
| Absorb | V0.6 candidate | Started→Milestone*→Resolved interaction | interaction_ref；wall_ref；milestone level；resolve reason | 106,429 rows；local track/wall IDs | `PARTIAL_DIRECT_IDENTITY_AMBIGUOUS` | 可探索；里程碑计数与 resolve-only 需补证 |
| FormationEvidence | V0.6 candidate | QualifiedWallAttackOccurrence / method-local gap / capability | source occurrence ref；qualification; availability | 无独立表 | `MISSING_DIRECT_PRODUCT` | 如纳入正式 R2，需补产品导出 |
| Barrier | V0.6 candidate | formal wall/direction/switch barrier | barrier_ref/type；source ref；old/new identities；order unresolved | 无独立表 | `MISSING_DIRECT_PRODUCT` | 图上的迁移/空档不能替代正式 Barrier |
| F3 | V0.6 candidate | per-symbol/per-UTI dense directional measurement | measurement identity；availability；run params | 有旧 Thick/Dense/Fight 图证据，无直接 F3 合同表 | `MISSING_DIRECT_PRODUCT` | 不可把旧 Thick 改名充当 F3 |
| F4 | V0.6 candidate | canonical sparse DirectedBigDeal occurrence | occurrence_ref；source_run；lane_mask；双 grade；availability | tactical 127,713 + structural 37,846 lane rows | `SOURCE_LANES_ONLY` | 可看 lane 源证据；不可作为 canonical F4 输出 |

候选任务包的详细字段不能因当前表名相似而自动宣布已满足。

---

# 4. M 步骤 2｜MaterialRequirementSet

| ID | 材料要求 | 级别 | 为什么需要 | 当前满足度 | 最小补法 |
|---|---|---|---|---|---|
| MR-01 | 原数据身份、manifest、对象/日历/图窗 | 必需 | 确定 DataBinding 与可用范围 | 已满足（缺 producer provenance） | 增加 P1RunManifest |
| MR-02 | Wall source lifecycle + identity/reason/time | 必需 | 冻结 Wall 高层预期、选择探索场景 | 部分满足 | typed ref + source_run +完整 reason/time |
| MR-03 | Build source lifecycle + milestone identity | 纳入 Build 时必需 | 区分加固过程与图元重复 | 部分满足 | milestone threshold/level + stop reason |
| MR-04 | Complete AttackSegment export | 纳入 Attack 时必需 | 区分 business_end 与 closed_at；避免错时判断 | 不满足正式对照 | corrected export + TimeBasisContract |
| MR-05 | Absorb interaction/milestone identity | 纳入 Absorb 时必需 | 区分多阈值里程碑与重复行 | 部分/歧义 | threshold/level identity + resolve-only explanation |
| MR-06 | FormationEvidence direct stream | 纳入时必需 | 区分 qualified hit、local gap、availability/technical close | 缺失 | 导出正式产品 |
| MR-07 | Formal Barrier direct stream | 纳入时必需 | 区分 switch/direction/end 与 Dormant/图形空档 | 缺失 | 导出正式产品及 source refs |
| MR-08 | F3 dense measurement + availability | 纳入 F3 时必需 | 验证 dense/sparse 边界和 missingness | 缺失 | per symbol/UTI export + availability/capability |
| MR-09 | Canonical F4 union | 纳入 F4 时必需 | 去重双 lane 并保留双 grade | 缺失 | union output + refs/lane_mask/audit |
| MR-10 | 完整 missing/empty/history/Pending 状态 | 正式 R2 必需 | 防止无行=业务反证 | 缺失 | P1RunManifest + availability table |
| MR-11 | 30 Tick/6 big window 选择依据 | 建议 | 判断场景代表性边界 | 缺失 | selection policy/manifest note |
| MR-12 | dependency-complete `run.py --check` | 可选 | 只验证当前环境可构造图 | 未做 | 合法 Worker 环境下只读运行；不重算上游 |

本轮不为了“覆盖八个名字”强制生成无消费者的新图，也不因已有图可看而把正式 occurrence 原值降为可选。

---

# 5. M 步骤 3｜观察数据处理与观察方法

## 5.1 原值与显示值分开

正式观察应优先保留：

```text
source product row
→ optional normalized/derived view
→ graph binding
→ glyph/display
```

产品判断使用 source row + contract；图只用于定位和并列观察。

## 5.2 生命周期类方法

Wall / Build / Absorb：

- 以产品身份排序 occurrence；
- 检查开始、重要中间事件、结束；
- 单独检查同 UTI、多阈值、Dormant、BandUpdate、reason；
- 不把一条 display segment 当作完整生命周期；
- 不把 row count 当 occurrence count，先核 identity。

## 5.3 Attack 方法

- 同时保留 start、business_end、closed_at、plot time；
- 无 closed_at 时不得假装完整；
- UTI→ts 的 session-boundary 转换必须检查；
- tactical/structural、count/volume/amount 与 wall relation 应来自同一 complete occurrence；
- 当前数据只可作字段/场景探索，不做精确时间正式对照。

## 5.4 F3/F4 方法

- F3 按 dense measurement 观察，不以无 F4 event 判 F3 无值；
- F4 先 canonical union，再统计/画图；
- 双 lane 重合处保留 lane_mask 与双 grade；
- 不 concat，不只留 max grade，不在 FRP 再做第二套 threshold。

## 5.5 缺失语义方法

至少区分：

```text
observed occurrence
valid no activity
no occurrence
source missing
stale
session invalid
calculation unavailable
insufficient history
pending
```

当前表只出现 `availability_code=1`，因此任何“无行”解释都需后续 manifest。

---

# 6. M 步骤 4｜既有能力复用与最小落地

本轮采用现成资产：

- raw Project Source ZIP；
- manifest/timespans/included_tick_nodes/calendar；
- CSV.GZ/NPZ 原值；
- 固定脚本展开副本；
- 已有图定义与 snapshot reader。

没有：

- 重算上游；
- 修改业务源码；
- 新建 CAEGraph；
- 改图方案；
- 写 BASE_E6_2；
- 签不必要 Worker。

如后续只需验证图构造，最小动作是依赖完整环境下只读运行：

```text
python run.py --list
python run.py --check --report <run-local-path>
```

该动作不能补齐 P1 产品合同，也不能替代 source export。

---

# 7. M 步骤 5｜真实材料取得与定量核验

## 7.1 记录量

```text
Wall lifecycle：45,698
Wall display segments：7,428
Build：131,219
AttackSegment：17,856
Absorb：106,429
F4 tactical lane：127,713
F4 structural lane：37,846
总计（含 display segments 与双 lane）：474,189
```

主表完整行精确重复：0。

## 7.2 Wall 与 Build 生命周期

Wall 汇总：

```text
Start 18,182
End 18,182
StateChange 8,452
BandUpdate 882
```

每个供给的 wall_id 都有一个 Start 和一个 End。

Build 汇总：

```text
Start 43,035
Milestone 45,149
Stop 43,035
```

每个供给的 build_id 都有一个 Start 和一个 Stop。

这只证明当前表形态闭合；不证明 producer 规则合理，也不解决 run-level identity。

## 7.3 Absorb 身份歧义

```text
Started tracks：31,281
Milestone rows：38,333
Resolved rows：36,815
resolve but no start tracks：5,534
business-equivalent repeated milestone rows：25,821
```

分 symbol resolve-only：

```text
rb 1,855
hc 2,154
i  1,525
```

若排除 `occurrence_ordinal` 和绘图 style，重复业务 payload：

```text
rb 4,462 rows / 1,858 groups
hc 2,366 rows / 981 groups
i  18,993 rows / 8,343 groups
```

另有少量 `wall_local_no=0`：rb 20 行、hc 30 行、i 13 行。

探索例：`tick_000023 / i / track_id=454496 / UTI=78266204` 有三条相同业务 payload 的 milestone 行，ordinal 为 0/1/2，之后 resolution。未获 threshold identity 前，不能把三行计作三份独立业务证据。

## 7.4 Cross-product local refs

除 `wall_local_no=0` 外，Build / Attack / Absorb 的 local wall refs 都能在同 symbol 的 Wall 表命中。

这足以做局部 join；不足以证明：

- 跨 symbol/global identity；
- 跨 run replay；
- source correction；
- typed product reference。

## 7.5 Attack 时间异常

所有 Attack 行满足：

```text
uti == plot_uti == business_end_uti
```

但 `ts/business_end_ts` 的绑定在 start/end 间不一致：

```text
rb mismatch 1,938 / 3,915
hc mismatch 1,161 / 2,573
i  mismatch 7,016 / 11,368
合计 10,115 / 17,856
```

多数偏差为 -0.5 秒；`i` 另有 5 行在交易边界偏差 -21,600.5 秒（6 小时 + 0.5 秒）。表中没有独立 `closed_at`。

结论：

```text
Attack 可做字段/场景探索；不具备精确时间正式 R2 资格。
```

这属于材料质量问题，不是业务 `COUNTERS`。

## 7.6 F4 lane 重合

structural key 是 tactical key 的完整子集：

| symbol | tactical | structural | overlap | grade differs on overlap |
|---|---:|---:|---:|---:|
| rb | 47,558 | 14,049 | 14,049 | 9,234 |
| hc | 40,730 | 12,199 | 12,199 | 8,106 |
| i | 39,425 | 11,598 | 11,598 | 7,776 |

若直接 concat，会重复 37,846 个 occurrence key。重合处 amount、directional hit volume proxy、price、ts 一致，但 grade 经常不同。

因此当前两表是 source lanes，不是 canonical F4。

## 7.7 探索窗口

本轮只把小样本用于字段、身份和场景理解：

```text
window：tick_000023
parent：small_000009
UTI：78266099..78266819
时间：2021-08-18 21:02:30 .. 21:08:30
symbols：rb/hc/i
```

`i` 窗口计数：

```text
Wall 35
Build 103
Attack 17
Absorb 80
F4 tactical 30
F4 structural 14
```

探索定位：

- wall_id=57427：Start→Dormant→End，且可局部 join Build/Attack/Absorb；
- wall_id=57428 以“同侧迁移”结束，wall_id=57429 同 UTI 开始；
- track_id=454496：同 UTI 重复 milestone payload。

这些不是正式支持/反证。

---

# 8. M 步骤 6｜MaterialReview

## 8.1 来源、版本与真实性

| 检查项 | 结果 |
|---|---|
| 数据文件真实存在 | PASS |
| bytes/SHA 与固定身份一致 | PASS |
| ZIP CRC | PASS |
| manifest/asset 可读 | PASS |
| 对象/日历/粒度/范围 | PASS_WITH_SCOPE_LIMITS |
| 原值/快照/显示阶段可区分 | PASS_WITH_DOCUMENTED_LIMITS |
| producer code/config/parameter/version | MISSING |
| source_run_ref / typed refs | MISSING |
| complete availability/missingness | MISSING |
| Attack time basis | FAIL_FOR_FORMAL_TIME_COMPARISON |
| F4 canonical output | MISSING |
| Formation/Barrier/F3 direct products | MISSING |
| Bokeh full construction in current env | NOT_RUN |

## 8.2 可回答的问题

当前材料可回答：

- 包内到底有哪些对象、尺度、时间窗、表和字段；
- Wall/Build/Attack/Absorb/F4-lane 的当前数据形态；
- 局部 lifecycle 是否可定位；
- local wall refs 是否可 join；
- Attack 时间绑定是否一致；
- F4 双 lane 是否重合；
- 哪些图证据只是显示层；
- 哪些产品/状态实际缺失；
- 哪些最小业务预期可形成 WORKING 版本。

当前材料不能回答：

- 八类产品是否整体业务合理；
- producer 规则/参数是否正确；
- Attack business_end 与 closed_at 的正式效果；
- canonical F4 质量；
- F3 dense/F4 sparse 正式效果；
- formal Barrier/FormationEvidence 的合理性；
- missing/valid-empty/history/Pending 的条件化效果；
- replay/修订/跨 run 身份；
- 全市场、全时间或随机样本的泛化结论。

## 8.3 防止重复计证据

- 同一 source occurrence 的多个图元只算一份源证据；
- F4 tactical/structural overlap 不是两份独立 occurrence；
- Absorb 同 payload ordinal 行不能在 identity 未明时多票；
- wall_segments 不是 wall lifecycle event 的第二份独立证据；
- window snapshot 是源表的裁剪，不是新的 producer output。

## 8.4 MaterialReview 结论

```text
PARTIAL_WITH_LIMITS
```

建议 manager 可将本包作为：

- R0/R1 的真实事实输入；
- R03 小样本探索输入；
- Wall/Build/Attack/Absorb/F4-lane 的受限材料交接候选；

但不建议把它作为“八类产品正式 R2 已 DATA_READY”的一体化交付。

---

# 9. M 步骤 7｜材料交接与 H1 建议（非 Gate）

## 9.1 建议可交接范围

建议 manager 评估 H1 时区分：

### 可交接

- 原件身份/CRC/manifest/对象/日历/图窗；
- Wall / Build / Attack / Absorb / F4 lanes 的真实表与字段审计；
- Wall/Build lifecycle closure 统计；
- Attack time anomaly；
- F4 overlap；
- Absorb identity ambiguity；
- 探索位置和 anti-golds；
- WORKING 预期与场景。

### 限制交接

- Attack 仅字段/场景探索，不做精确时间正式比较；
- F4 仅 source lane 观察，不称 canonical output；
- Absorb milestone 计数前需补 identity；
- 图层只作定位，不替代 product contract。

### 尚不可交接为正式产品证据

- FormationEvidence；
- formal Barrier；
- F3；
- P1RunManifest/typed refs/replay；
- complete missingness/availability；
- canonical F4；
- corrected complete Attack occurrence。

## 9.2 H1 建议

建议状态：

```text
PARTIAL_WITH_LIMITS
```

由 manager 决定是否接受及接受哪些用途；E1 不宣布 H1。

---

# 10. R0｜AnalysisInputAssessment

## 10.1 已确认事实

- Owner 对 Wall 的高层意图有明确来源；
- V0.6 八类产品合同是 Owner review candidate，不是永久接受；
- 当前数据包真实、可读、身份匹配；
- 当前包是派生表/快照/绘图证据，不是八类 formal typed product 全集；
- Wall/Build/Attack/Absorb/F4 lanes 可局部探索；
- Formation/Barrier/F3 direct products 缺失；
- Attack time 不适合正式精确对照；
- F4 需 canonical union；
- 当前表不足以解释 absent rows 的业务含义。

## 10.2 当前可开展范围

- Owner Wall 高层预期的 R1 推导；
- 候选合同的条件化 R1 推导；
- 实现事实预期的记录；
- 场景设计与 anti-golds；
- R03 探索样本；
- manager 的冻结/H1/首批 R2 范围选择。

## 10.3 当前不可开展范围

- 正式 `SUPPORTS/COUNTERS`；
- 精确 Attack time 效果；
- 八产品全覆盖 R2；
- replay/revision/identity 对照；
- missing/empty/history/Pending 对照；
- 参数修复或业务根因诊断。

---

# 11. R1｜最小业务预期

完整机器可读内容见 `D001_EXPECTATION_REGISTER.yaml`。本节给出来源分离和冻结建议摘要。

## 11.1 `OWNER_EXPLICIT`

建议 manager 可先审查冻结的四条高层命题：

1. Wall 是受限 L1/成交视角下跨时间形成的认知对象，不是单 tick/单图元；
2. Wall 应有开始、重要中间变化、明确结束和持续身份；
3. pre-L0 输出少量关键 occurrence + FRP 必需 payload，FRP 不重建正式产品；
4. Wall 与 Attack/dense 定义解耦，Attack/F3/F4 不反向定义 Wall。

这四条直接来自 Owner 原文。当前数据用于理解字段和适用条件，但没有在本轮作正式效果判断。

## 11.2 `BUSINESS_INFERRED`

已形成八条 WORKING 候选：

- canonical Wall 复用、下游产品解耦；
- Build lifecycle/milestone identity；
- complete AttackSegment + business_end/closed_at；
- Absorb interaction/milestone identity；
- FormationEvidence / local gap / Barrier / technical gap 分离；
- F3 dense / F4 sparse boundary；
- F4 canonical union；
- identity/replay/correction。

这些不是 Owner 已确认需求。只有 manager 明确把 V0.6 作为本 Run 的比较合同后，才建议进入冻结。

## 11.3 `IMPLEMENTATION_DERIVED`

记录四类实现事实：

- 当前表/快照/显示数据阶段；
- run/snapshot/plot binding 的真实读取合同；
- 当前实际存在/缺失的产品资产；
- rb/hc/i、多尺度、30 Tick 的真实范围。

这些可冻结为 DataBinding 事实，但不能作为业务应然。

---

# 12. InputSuitabilityAssessment

## 12.1 输入有效性

```text
PARTIAL_WITH_LIMITS
```

原件身份、CRC、manifest、主要表可读；但 Attack time、Absorb identity、typed refs、provenance、availability 和部分产品导出不足。

## 12.2 输入业务合理性

```text
EXPLORABLE_NOT_FORMALLY_JUDGED
```

现有数据确实呈现产品候选的若干业务形态，可用于探索；但未验证 producer 规则和业务含义是否正确。

## 12.3 对当前目的的适用性

```text
R0/R1 + R03 EXPLORATION：适用
FORMAL INTEGRATED R2：不适用
```

“输入不适合当前正式 R2 目的”不等于“输入特征本身错误”。

---

# 13. ScenarioExpectationSet 摘要

已建立 14 个场景，完整定义见 YAML：

| ID | 区分问题 | 当前材料状态 |
|---|---|---|
| S-WALL-001 | 一堵 Wall 的 Start/变化/Dormant/End | 可探索 |
| S-DECOUPLE-002 | Build/Attack/Absorb 共 Wall 但生命周期解耦 | local IDs 下可探索 |
| S-SWITCH-003 | 同侧 Wall 迁移与 canonical switch | Wall 行可见；Barrier 缺失 |
| S-DIRECTION-004 | direction switch 与 formal Barrier | 缺 Barrier |
| S-DORMANT-005 | Dormant 非 Barrier | Wall 可见；Barrier 缺失 |
| S-ATTACK-006 | business_end 与 closed_at | 不能正式测 |
| S-F4-007 | tactical/structural 同 UTI union | 只有 lanes |
| S-F3F4-008 | F3 dense / F4 sparse | F3 缺失 |
| S-MISSING-009 | event/valid empty/missing/history/Pending | 未覆盖 |
| S-GRAPH-010 | 图证据存在但产品关键合同缺失 | 可直接作为 anti-gold |
| S-SCOPE-011 | rb/hc/i、多尺度、30 Tick 的适用范围 | 范围已知；选择依据缺失 |
| S-REPLAY-012 | 稳定 identity/replay/correction | 缺失 |
| S-ABSORB-013 | 同 UTI 多 milestone identity | 歧义 |
| S-TIME-014 | UTI/ts/time basis 一致性 | Attack 不一致 |

---

# 14. 冻结建议（非 Gate）

## 14.1 可由 manager 立即审查冻结

```text
E-OWN-WALL-001
E-OWN-WALL-002
E-OWN-WALL-003
E-OWN-WALL-004
```

理由：来源为 Owner 原文，命题高层、可证伪、适用/反例/证据已明确。

## 14.2 条件冻结

```text
E-BIZ-P1-001 .. E-BIZ-P1-008
```

前提：manager 明确采用 V0.6 candidate taskpack 作为**本 Run 当前正式比较合同**，同时保留“非永久 Owner 接受”的成熟度标签。

## 14.3 不作为业务预期冻结

```text
E-IMP-DATA-001 .. E-IMP-DATA-004
```

它们是实现/DataBinding 事实。

## 14.4 E1 未执行

- G-EXPECTATION-FREEZE；
- H1；
- G-COMPARISON；
- 任何合理/不合理结论。

---

# 15. 正式 R2 最小输入

正式 R2 开始前至少需要：

1. manager 接受的 `FrozenExpectationSet` 及版本；
2. 首批产品范围；
3. P1RunManifest 或等价完整 DataBinding；
4. `source_run_ref`、typed product/occurrence refs；
5. time basis、参数、代码/config/data 版本；
6. 选择范围和场景定位；
7. 完整 missingness/availability；
8. 若纳入 Attack：corrected complete occurrence + business_end + closed_at；
9. 若纳入 F4：canonical union；
10. 若纳入 Formation/Barrier/F3：对应 direct products；
11. evidence preflight，分开检查有效性、业务含义、目的适用性；
12. 同源证据依赖和不重复计票规则。

建议首轮不要机械一次纳入八类。可由 manager 在以下两种范围中选择：

- **Wall-first**：先验证 Owner 高层 Wall lifecycle 与 sparse FRP boundary；
- **受限五产品**：Wall / Build / Attack / Absorb / F4，但先补 Attack/F4/identity/provenance；
- 全八类只有在 Formation/Barrier/F3 direct exports 到位后再进入。

这只是专业后继建议，不是 manager 决定。

---

# 16. AdditionalEvidenceRequest

| Request | 最小补证 | 区分什么 | 阻断范围 |
|---|---|---|---|
| AER-P1-001 | P1RunManifest、code/config/parameter/source、source_run_ref、DataBinding | 可复现产品还是匿名图快照 | 全部正式 R2 |
| AER-P1-002 | corrected complete AttackSegment export，含 business_end/closed_at/completeness/reason | 业务结束与绘图/flush 时间 | Attack |
| AER-P1-003 | canonical F4 occurrence，含 occurrence_ref/lane_mask/双 grade/audit/availability | source lanes 与正式 F4 | F4 |
| AER-P1-004 | FormationEvidence、Barrier、F3 direct exports + capability/availability | 真缺产品还是字段潜伏 | 对应三类 |
| AER-P1-005 | Absorb milestone level/threshold identity、resolve-only 说明、wall_local_no=0 语义 | 多阈值 vs 重复行 | Absorb milestone counting |
| AER-P1-006 | 可选 `run.py --check` 报告 | 静态图合同 vs 当前环境可构图 | 只阻断 full-render claim |

补证应回原 `AR-P1-001` 事实/预期上下文；冻结前得到的补证不自动成为正式证据。

---

# 17. OpenQuestions

1. 本 Run 是否采用 V0.6 candidate taskpack 作为正式 R2 工作比较合同，还是只作为需求候选？
2. 首批正式 R2 产品范围是什么？
3. 当前数据由哪一个 code/config/parameter/source snapshot 生成？
4. Attack timestamp 为何在 start/end 间变化，且 i 存在 6 小时 session-boundary offset？
5. Absorb 同 UTI 等 payload 多行代表多个 threshold milestone 还是重复输出？
6. 6 个 30m 和前 30 个 Tick 窗的选择规则是什么？
7. `availability_code=1` 之外的 valid-empty/missing/stale/history/Pending 怎样导出？

这些问题按实际影响路由给 manager 或 material/producer provider，不要求 Owner 解决纯技术事实。

---

# 18. D001 合同逐项完成表

| 交付项 | 状态 | 位置 |
|---|---|---|
| 专业执行报告 | 完成 | 本文件 |
| ProcessingSkeleton | 完成 | §2 |
| 八产品覆盖矩阵 | 完成 | §3 |
| MaterialRequirementSet | 完成 | §4 |
| 方法与复用方案 | 完成 | §5～6 |
| 真实材料与量化审计 | 完成 | §7 + `D001_DATA_AUDIT.json` |
| MaterialReview | 完成 | §8 |
| 交接状态 | `PARTIAL_WITH_LIMITS` | §9 |
| BusinessIntentStatement | 完成 | §10～11 + YAML |
| ExpectationRegister | WORKING，完成 | YAML |
| InputSuitabilityAssessment | 完成 | §12 + YAML |
| ScenarioExpectationSet | 完成 | §13 + YAML |
| OpenQuestions | 完成 | §17 + YAML |
| 冻结建议 | 完成，非 Gate | §14 |
| 正式 R2 最小输入 | 完成 | §15 |
| AdditionalEvidenceRequest | 完成 | §16 |
| Worker orders / returns | 0 / 不适用 | §19 |
| V2 Return | 成果提交后单独提交 | `PRO_RETURN.json` |

---

# 19. Worker 与写面说明

本 D 零 W 完成：

- Project Source 原件在当前 E1 会话可读；
- GitHub 固定源可读；
- 数据审计可直接完成；
- 完整 Bokeh 构造不是本轮数据层核定的必要前提；
- 因此没有理由额外占用未绑定 Worker 或写 `/dwdhome/fy/BASE_E6_2`。

```text
issued Worker Orders：0
accepted Worker Returns：0
Linux writes：0
```

---

# 20. 准确后继与剩余依赖

## 20.1 建议 manager 的下一动作

1. 分别判断 H1 的受限交接范围；
2. 判断是否采用 V0.6 作为本 Run 的正式比较合同；
3. 对 `E-OWN-WALL-001..004` 作 G-EXPECTATION-FREEZE 审查；
4. 选择首批正式 R2 产品范围；
5. 对所选范围签发精确 AER，而不是要求泛化“补全全部 P1”；
6. 补证返回后进入 R05 EvidencePreflight，再决定是否可正式 R06 对照。

## 20.2 仍需外部满足的依赖

- AER-P1-001 至 AER-P1-005 中与所选 R2 范围相关的项目；
- 如要宣称图构造可运行，再做 AER-P1-006；
- manager Gate 决定。

## 20.3 不受缺口阻断的独立工作

- Wall 高层预期冻结审查；
- 当前数据包的 R03 探索；
- Wall/Build/Attack/Absorb/F4 lane 的字段与 anti-gold 准备；
- 产品范围选择；
- provenance 与 time basis 的精确补证请求。

---

# 21. 专业边界声明

本 E1：

- 不宣布 H1；
- 不宣布 G-EXPECTATION-FREEZE；
- 不宣布 G-COMPARISON；
- 不把任何图或字段当作产品语义已成立；
- 不把候选 taskpack 当成 Owner 永久接受；
- 不把实现行为当作业务应然；
- 不宣布任何 P1 产品合理/不合理；
- 不宣布父任务完成；
- 不替 manager 作业务 Gate。

D001 专业范围内的事实准备、材料核定与最小业务预期形成已完成；后续按上述真实限制和精确依赖继续。
