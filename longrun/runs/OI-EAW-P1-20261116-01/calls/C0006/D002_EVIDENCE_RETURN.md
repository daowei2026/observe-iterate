# C0006｜D002 五项具名补证与 EvidencePreflight 回交

> **run_id**：`OI-EAW-P1-20261116-01`  
> **call_id**：`C0006`  
> **invocation token**：`a06b1534c843bf7965c26d5861017c68`  
> **delegation_id**：`D002`  
> **executor**：`chatgpt:OI-EAW-P1-20261116-01:executor:E1`  
> **return_to**：`chatgpt:OI-EAW-P1-20261116-01:manager`  
> **origin round / frozen set**：`AR-P1-001 / FZ-EAW-P1-AR-P1-001`  
> **专业边界**：只完成 AER-P1-001～005 与 EvidencePreflight；不重做 D001，不做正式 `SUPPORTS/COUNTERS`，不替 manager 决定 H2、G-COMPARISON 或父任务完成。

---

## 0. 回交结论

D002 具名补证与 preflight 已完成。五项 AER 的整体状态均为 `PARTIAL`，其中若干正式产品子项被有据关闭为 `PROVEN_UNAVAILABLE`；没有权限型或物理访问型 `BLOCKED`。

| AER | 整体状态 | 本轮得到的关键事实 | 正式 R2 尚缺 |
|---|---|---|---|
| AER-P1-001 provenance / DataBinding / availability | `PARTIAL` | ZIP、对象、日历、UTI、图窗及机械选窗规则已核定 | frozen source run、receipt、code/config/params/input cut、typed run identity、完整 missingness |
| AER-P1-002 Attack complete occurrence / time | `PARTIAL` | 10,115 行混合端点绑定及 5 个 session-gap 放大值已准确定位 | authoritative corrected export、`closed_at`、TimeBasisContract |
| AER-P1-003 canonical F4 union | `PARTIAL` | 37,846 overlap、127,713 audit-only union、25,116 grade differences | canonical producer output、双 grade identity、receipt/availability |
| AER-P1-004 Formation / Barrier / F3 | `PARTIAL` | current Formation/Barrier producer+typed ports 存在；F3 为 transient-only | frozen direct products；F3 direct artifact 当前本身不存在 |
| AER-P1-005 Absorb milestone / identity | `PARTIAL` | 多阈值同 tick 机制、5,534 resolve-only、63 zero-wall rows 已定位 | frozen receipt、milestone `level`、正式 typed identity 与产品边界 |

机器成果：

- `D002_EVIDENCE_AUDIT.json`：
  `daowei2026/observe-iterate@242a60e2d2b0b3320a753f1db6f5c7c6282051d6:longrun/runs/OI-EAW-P1-20261116-01/calls/C0006/D002_EVIDENCE_AUDIT.json`
- `D002_R2_PREFLIGHT.yaml`：
  `daowei2026/observe-iterate@750084b1d4bf177d0bb71e743655ab95b3b81ee2:longrun/runs/OI-EAW-P1-20261116-01/calls/C0006/D002_R2_PREFLIGHT.yaml`
- review-only 审计原件：
  `daowei2026/observe-iterate@6bc4808db0fbb631f5a345dcfb55e6087f0013bf:longrun/runs/OI-EAW-P1-20261116-01/calls/C0006/D002_REVIEW_ONLY_AUDIT_BUNDLE.zip`

按冻结集合的正式 R2 输入资格，没有任何一个八类产品达到无条件 `ELIGIBLE`：

```text
Wall                 PARTIAL
Build                PARTIAL
AttackSegment        PROVEN_UNAVAILABLE
Absorb               PARTIAL
F4                    PROVEN_UNAVAILABLE
FormationEvidence     PROVEN_UNAVAILABLE
WallRelationBarrier   PROVEN_UNAVAILABLE
F3                    PROVEN_UNAVAILABLE
```

这是输入资格结论，不是产品业务合理性结论。`S-GRAPH-010` 仅以“图层不能替代产品合同”的材料方法 anti-gold 达到 `ELIGIBLE`；它不等于任何业务效果被支持或反证。

---

# 1. 实际调查范围与来源分层

## 1.1 冻结 Project Source

本 E1 只读使用：

```text
caegraph-data-30tick.zip
bytes   = 16,654,307
sha256  = 73e7c5f289d7b25f08f11cffda7315ad2dad3f8c323715425afdd485e15c4233
members = 446
CRC     = ALL_PASS
```

检查范围包括 manifest、calendar、timespans、included tick nodes，以及 Wall/Build/Attack/Absorb/F4 两 lane 的源帧。没有访问原 run，也没有重算上游。

## 1.2 Current implementation evidence（不等于 frozen provenance）

为回答 producer/export/typed-contract 是否真实存在，定向读取：

```text
TIS current integration:
10010b89f8fc79a91affd26f985b6d9bf2d33c6c

FRP current integration:
37c790c0f456fe3022bb00609219d3e92a5c2f9b
```

这些 commit 只能证明当前实现合同。冻结 ZIP 没有 thin receipt 或 run manifest 将自身绑定到这些 commit，因此本报告不把 current defaults、参数或 schema 冒充 frozen run 事实。

## 1.3 Review-only 审计原件

审计包：

`daowei2026/observe-iterate@6bc4808db0fbb631f5a345dcfb55e6087f0013bf:longrun/runs/OI-EAW-P1-20261116-01/calls/C0006/D002_REVIEW_ONLY_AUDIT_BUNDLE.zip`

```text
bundle sha256 = 22665104288415e597e6bbc652231a8fb3db922955cdd00edb016997726cad23
script sha256 = d110c9c48054bb1eb9401b0083ac1841d414dc4f7b8d1b943fc617590fe343af
derived json  = b2140e2ff91bcf392bd5bd6b6bf8e99389e1ce3ea52053ff650762b790ba39d6
```

复现命令：

```bash
python D002_REVIEW_ONLY_AUDIT.py \
  caegraph-data-30tick.zip \
  D002_REVIEW_ONLY_DERIVATIONS.json
```

该包明确标记 `NOT_CANONICAL_PRODUCT`。其中 F4 union 只形成审计 digest，不生成 producer product。

---

# 2. AER-P1-001｜provenance、DataBinding 和 availability

## 2.1 已取得

- 对象：`rb / hc / i`；板块：`blk@steel`；
- 日历名：`night_end_at_2300`；半秒 UTI 轴共 103,316,400 slots；
- 数据包日历首尾：`2013-01-04 09:00:00.500`～`2024-02-29 15:00:00`；
- 1 个 overview、6 个 30m、18 个 1m、54 个 5s、30 个带行情的 Tick 窗；
- 30 Tick 包装规则：`tick_000001..tick_000030`，前 24 个属于 `big_000001`、后 6 个属于 `big_000002`；
- 148 个 Tick locator 中只有前 30 个带行情；
- microstructure evidence 的 `source_key=9be111...` 是 feature identity hash，不是 producer run id。

## 2.2 有据不可得

冻结包中不存在：

- `P1RunManifest`、source run id 或 `source_run_ref`；
- thin receipt、commit marker、revision/source-correction 状态；
- producer commit/config/实际参数/input market cut；
- timezone、session policy version、same-timestamp ordering；
- run-level typed product/occurrence identity；
- 6 个 30m 窗及 30 Tick 的业务选择/代表性理由。

Current thin receipt 设计虽然能表达 target、calendar/session、time range、market cut、参数、upstream、schema/code version，但它明确不是 commit marker、revision ledger、dependency DAG 或 source-correction 状态；更重要的是 frozen ZIP 没有携带这些 receipt。

## 2.3 availability

当前 Wall/Build/Attack/Absorb 表只观察到 `availability_code=1`。冻结包没有独立表达：

```text
ValidEmpty
SourceMissing
Stale
SessionInvalid
CalculationUnavailable
InsufficientHistory
Pending
```

因此“没有行”仍不能被解释为业务 negative。

## 2.4 状态

```text
AER-P1-001 = PARTIAL
```

common provenance 缺口影响全部八类产品，以及 `S-MISSING-009 / S-REPLAY-012 / S-SCOPE-011 / S-TIME-014`。

---

# 3. AER-P1-002｜Attack complete occurrence 与时间合同

## 3.1 Frozen 表的准确形态

17,856 行均满足：

```text
plot_uti == uti == business_end_uti
```

但不存在：

```text
closed_at_uti
closed_at_ts
technical truncation / unavailable 的完整行级合同
```

## 3.2 10,115 行不一致的原因边界

| symbol | rows | timestamp mismatch |
|---|---:|---:|
| rb | 3,915 | 1,938 |
| hc | 2,573 | 1,161 |
| i | 11,368 | 7,016 |
| **total** | **17,856** | **10,115** |

所有行的 stored timestamp 要么等于 `calendar(start_uti)`，要么等于 `calendar(business_end_uti)`，没有第三种映射。10,115 行把 stored `business_end_ts` 绑定到 start UTI；这些行均为 `business_end_uti = start_uti + 1` 的 one-tick segment。

有据可确认：

> frozen 表混用了“start-bound timestamp”和“business_end_uti”两种端点约定，类似把半开区间的右端 UTI 与最后包含 tick 的时间放在同一行。

由于 frozen source 缺 producer receipt，不能进一步把该现象归因到某个具体 commit/config。

## 3.3 `i` 的五个 −21,600.5 秒

五个 segment：

```text
219484, 222860, 224434, 225743, 232513
```

这些行 start 在 15:00，`business_end_uti=start_uti+1` 落在下一交易段 21:00:00.5；stored timestamp 仍是 15:00，所以普通 −0.5 秒端点差在 session gap 上被放大为：

```text
-21,600.5 seconds
```

这不是五个独立随机异常，而是同一端点约定在 session boundary 的表现。

## 3.4 Current producer contract 与 frozen export 的差距

Current Attack core 已将：

```text
business_end = last atom time
closed_at    = close/confirmation tick
```

分开，并带 availability/technical truncation 与 close reason；current wrapper 还正式产生 Segment、Formation、Barrier 三类产品。

但 frozen export 没有 `closed_at`，且 main timestamp 被重绑定，因此本包不能当作 corrected complete Attack occurrence。

## 3.5 状态

```text
AER-P1-002 = PARTIAL
corrected complete export = PROVEN_UNAVAILABLE
```

受影响：`E-BIZ-P1-003`、`S-ATTACK-006`、`S-TIME-014`。

---

# 4. AER-P1-003｜canonical F4 union

## 4.1 Frozen 两条 lane 的真实关系

| symbol | tactical | structural | overlap | overlap grade differs |
|---|---:|---:|---:|---:|
| rb | 47,558 | 14,049 | 14,049 | 9,234 |
| hc | 40,730 | 12,199 | 12,199 | 8,106 |
| i | 39,425 | 11,598 | 11,598 | 7,776 |
| **total** | **127,713** | **37,846** | **37,846** | **25,116** |

- structural key 完全是 tactical key 的子集；
- overlap 的 amount、directional-hit-volume proxy、timestamp 全部一致；
- grade 经常不同，不能只保留 max grade；
- 直接 concat 会多计 37,846 个 occurrence key。

## 4.2 Producer authority

Current TIS 的 `DirectedBigDealTick` 仍按 qualification family 独立输出 public artifacts。Attack 在自身输入处执行 `union_keep_labels`，并明确保留独立公开 F4 artifacts。Current FRP per-family ingress 也把另一 family 标成 unavailable，而不是生成双 grade canonical occurrence。

因此：

```text
Attack-local union != public canonical F4 product
review-only union   != public canonical F4 product
```

## 4.3 Review-only union

按 `(symbol, uti, side_code)` 形成 127,713 个 audit key，digest：

```text
d3535a41cbea4cc34c28c50d0cc0a6183dba3f3da4aecac0673241d9bf2927ca
```

用途仅是证明 overlap、去重数量和双 grade 保留要求；它没有 occurrence_ref、source_run_ref、receipt、capability/availability 或 producer authority。

## 4.4 状态

```text
AER-P1-003 = PARTIAL
canonical producer output = PROVEN_UNAVAILABLE
```

受影响：`E-BIZ-P1-007`、`S-F4-007`、`S-F3F4-008`。

---

# 5. AER-P1-004｜FormationEvidence、Barrier、F3 direct products

## 5.1 AttackFormationEvidence

Current producer 与 typed port 存在；其 current contract 能表达 accepted material、ordinary gap、same-UTI unresolved、gap/availability interval 及 capability-unavailable material。

但 frozen ZIP 没有 direct table，也没有 receipt；Attack/F4 latent rows 不能改名替代。

```text
current implementation existence = OBTAINED
frozen-run direct product         = PROVEN_UNAVAILABLE
```

## 5.2 WallRelationBarrier

Current producer 与 typed port 存在。Current producer 只允许 `Wall.End` 形成正式 barrier；`wall_switch / side_switch` close reason 会公开为 unsupported formation material，不能升级为 formal Barrier。

Frozen ZIP 没有 barrier table/receipt，Wall 迁移图形不能替代。

```text
current implementation existence = OBTAINED
frozen-run direct product         = PROVEN_UNAVAILABLE
```

## 5.3 F3

Current Build 代码明确：

```text
在有界交易日 chunk 内形成并即时消费 active-flow/F3
不形成历史 artifact
dense_active_flow_artifact = false
```

F3 也不在 current receipt product kinds 中。Frozen ZIP 没有 direct F3 table。

```text
F3 direct product = PROVEN_UNAVAILABLE
```

旧 Thick/Dense/Fight 图证据不能替代。

## 5.4 状态

```text
AER-P1-004 = PARTIAL
```

这里的 `PROVEN_UNAVAILABLE` 是 frozen/current product availability 结论，不是 business error。

---

# 6. AER-P1-005｜Absorb milestone 与 identity

## 6.1 Frozen lifecycle

```text
rows       106,429
Started     31,281
Milestone   38,333
Resolved    36,815
```

## 6.2 同 UTI 多 milestone

25,821 milestone rows 处于同一 track、同一 UTI 的 2 行或 3 行组。Current core 的正式机制是逐个遍历 milestone levels；若一个 tick 同时越过多个未触发阈值，就分别发射多条 occurrence，并携带 `level` 与 `ratio`。

但 frozen graph package 丢失了 `level`。因此：

- 行数模式与 distinct threshold milestones 一致；
- current default 0.25/0.5/0.75 不能无 receipt 地冒充 frozen actual params；
- 不得把 25,821 行按等价 payload 多票计数；
- `occurrence_ordinal` 只是同刻物理流拆分序号，不是 threshold identity。

## 6.3 5,534 resolve-only tracks

```text
rb 1,855  = breakthrough 41 + blocked/timeout 1,814
hc 2,154  = breakthrough 27 + blocked/timeout 2,127
i  1,525  = breakthrough 3  + blocked/timeout 1,522
```

这些 tracks 没有 milestone rows。Current core 可以：

1. 先建立 quote track；
2. 只有首次 hit 时才发 `InteractionStarted`；
3. 未发生 hit 也可能因 breakthrough/timeout 结束并发 `Resolved`。

因此它们更接近“没有观察到 Absorb interaction start 的 quote-track termination”，不能自动解释为完整 `Started→Resolved` Absorb interaction。由于 frozen code 未绑定，正式产品仍需 receipt 或 scope/filter 规则确认。

## 6.4 `wall_local_no=0`

```text
63 rows / 30 symbol-local tracks
```

Current core 在 quote track 无法绑定 exact active Wall 时保留 `active_wall_id=0`，仍可能发事件；Current FRP typed ingress 则要求 dependent Wall identity 存在，zero/missing 会被拒绝。

所以 frozen zero-wall rows 不能进入正式 typed Absorb product。

## 6.5 状态

```text
AER-P1-005 = PARTIAL
```

受影响：`E-BIZ-P1-004`、`S-ABSORB-013`、`S-DECOUPLE-002`、`S-REPLAY-012`。

---

# 7. EvidencePreflight 汇总

完整逐 expectation / scenario 表见 `D002_R2_PREFLIGHT.yaml`。

## 7.1 三层输入检查

| 层次 | 状态 | 说明 |
|---|---|---|
| 数据/文件/字段有效性 | `PARTIAL` | ZIP 与主要表真实可读；Attack/Absorb/F4 有已量化合同缺口 |
| 业务含义清晰度 | `PARTIAL` | current contracts 可帮助解释，但 frozen run 未绑定；多处字段被丢失或只剩图层 |
| 对 integrated formal R2 的适用性 | `PROVEN_UNAVAILABLE` | common provenance、corrected Attack、canonical F4、direct products 和 missingness 不齐 |

## 7.2 Expectation 状态

```text
PARTIAL             E-OWN-WALL-001..004
PARTIAL             E-BIZ-P1-001, 002, 004
PROVEN_UNAVAILABLE  E-BIZ-P1-003, 005, 006, 007, 008
```

## 7.3 Scenario 状态

```text
ELIGIBLE             S-GRAPH-010  # 仅材料 anti-gold
PARTIAL              S-WALL-001, S-DECOUPLE-002, S-SWITCH-003,
                     S-DORMANT-005, S-SCOPE-011, S-ABSORB-013
PROVEN_UNAVAILABLE   S-DIRECTION-004, S-ATTACK-006, S-F4-007,
                     S-F3F4-008, S-MISSING-009, S-REPLAY-012, S-TIME-014
```

## 7.4 同源证据控制

- window snapshot 与 source frame 同 lineage；
- wall_segments 是 lifecycle 的显示派生；
- F4 tactical/structural overlap 是同一 half-second material；
- review-only union 是两 lane 的派生；
- current TIS/FRP 合同不独立证明 frozen run 生产事实。

以上均不得重复计票。

---

# 8. 新发现候选（不改写 frozen v1）

本轮仅登记三个 `EvidenceInducedCandidate`：

1. **EIC-D002-001**：Attack 需要显式 inclusive/exclusive endpoint 和 session-boundary TimeBasisContract，`business_end` 与 `closed_at` 不得被 graph timestamp 合并。
2. **EIC-D002-002**：应区分 `QuoteTrackResolvedWithoutInteraction` 与 `AbsorbInteractionResolved`。
3. **EIC-D002-003**：若下游要求一条双 lane public F4 occurrence，必须新增明确 producer authority，不能依赖 Attack-local merge 或 review-only union。

它们没有被加入 frozen v1，也没有用于本轮正式比较。

---

# 9. Worker、写面和非目标

本 D 零 W 完成：

```text
Worker Orders    0
Worker Returns   0
Linux writes     0
source changes   0
upstream reruns  0
```

Frozen Project Source 与固定 GitHub 源均可由 E1 直接读取；没有必要为已不存在的 producer artifact 签 Worker，也不允许通过一次性生成冒充正式产品。

本报告没有：

- 正式 `SUPPORTS/COUNTERS`；
- H2 或 G-COMPARISON 决定；
- FrozenExpectationSet 修改；
- 产品合理/不合理结论；
- CAEGraph 新设计或业务源码修改；
- 父任务完成宣告。

---

# 10. D002 合同完成表

| 交付 | 状态 |
|---|---|
| AER-P1-001 | 完成，`PARTIAL`，具名不可得项已关闭 |
| AER-P1-002 | 完成，`PARTIAL`，corrected export=`PROVEN_UNAVAILABLE` |
| AER-P1-003 | 完成，`PARTIAL`，canonical union=`PROVEN_UNAVAILABLE` |
| AER-P1-004 | 完成，`PARTIAL`，三类 frozen direct products=`PROVEN_UNAVAILABLE` |
| AER-P1-005 | 完成，`PARTIAL` |
| `D002_EVIDENCE_AUDIT.json` | 完成 |
| `D002_R2_PREFLIGHT.yaml` | 完成 |
| review-only audit bundle | 完成，`NOT_CANONICAL_PRODUCT` |
| Worker 原件/回交 | 不适用，0 W |
| executor V2 Return | 本专业包发布后单独提交 |

D002 的专业范围已经完整执行。其后由 manager 消费本结果、决定 H2 与是否/如何签发正式 R2；这些 manager 后继不是 E1 的剩余专业范围。
