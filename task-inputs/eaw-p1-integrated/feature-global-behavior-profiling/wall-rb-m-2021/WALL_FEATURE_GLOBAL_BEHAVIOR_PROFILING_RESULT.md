# EAW P1 Wall｜特征全量行为统计与结构疑点发现

> **Result ID**：`FGB-WALL-RB-M-2021-20261121-01`  
> **执行 Skill**：`feature-global-behavior-profiling v0.1.0`  
> **Feature Understanding**：`WALL_FEATURE_UNDERSTANDING_PACKAGE_V0.2.0_20261120.md`  
> **运行结果**：`wall-rb-m-2021.zip`  
> **Gate**：`DIAGNOSIS_REQUIRED`

## 0. 执行边界

- 本次使用 ZIP 内完整 producer occurrence、dense state trace、receipt、coverage 与 validation 表；没有依赖图或画图脚本。
- 不运行或重算 Feature，不解释结构疑点根因，不调参数。
- `F0/F1/F2/F6/F7/F8/F9`、support/thin rings 和内部 counters 未暴露，因此未伪造候选命中率。
- ZIP 未包含物化的 FRP `wall_occurrences/current/diagnostics`；涉及 typed identity 的结论是 producer 结果对当前 FRP 合同的兼容性疑点，不声称实际 FRP 已经输出 diagnostic。

## 1. StatisticsInputReadiness

| 项 | 结论 |
|---|---|
| 代码版本 | `MATCH`：Feature Understanding 锁定 TIS `10010b89…`；交付源快照与该基线一致。m 另有已声明的输入占位过滤修复，Wall core 与参数未变 |
| 参数版本 | `MATCH`：rb/m 均为 `WallAssembler:wall-default`，`p=1`、`t=6`、QT=`1d/30/0.997` |
| 数据范围 | `CONFIRMED`：243 交易日，实际 Tick `2021-01-04 09:00:00.500000` 至 `2021-12-31 15:00:00` |
| QT 有效起点 | `2021-02-22 00:00:00`；首 Wall 事件均在 `2021-02-23`，预热期不进事件密度分母 |
| 完整性 | ZIP SHA-256 与内部 `SHA256SUMS.txt` 全部通过；原生表逐行精确对比通过 |
| 对象键 | `symbol + feature_instance + wall_id` |
| 时间键 | `UTI + timestamp`；同拍物理分流保留 `occurrence_ordinal` |
| Readiness | **READY** |

- Archive SHA-256：`52f9032c8808828b54a575c04f5a1f21adb833d7c857d7ee27980023014f9648`
- Feature Understanding SHA-256：`a7d64112a34fe7424ada0908abd213621d926ba485aa964458c1e563e083f097`

## 2. 全局概览

| 指标 | rb | m |
|---|---:|---:|
| post-QT Tick 行 | 8,746,200.000 | 8,746,187.000 |
| Wall 对象 | 71,686.000 | 27,920.000 |
| 生命周期事件 | 278,800.000 | 79,734.000 |
| 事件/百万 post-QT Tick | 31,876.701 | 9,116.430 |
| Start/百万 post-QT Tick | 8,196.245 | 3,192.248 |
| 每对象事件数均值 | 3.889 | 2.856 |
| 生命周期中位数（秒） | 5.000 | 13.000 |
| 生命周期 P95（秒） | 20.500 | 88.500 |
| 生命周期最大值（秒） | 11,377.000 | 575.500 |

rb 的 Start 密度是 m 的 **2.57 倍**，事件密度是 **3.50 倍**；但 m 的 Wall 生命周期更长、逐 Tick 至少一侧活跃覆盖更高。这里只形成跨品种场景问题，不直接判错。

## 3. 对象、事件与生命周期剖面

### 3.1 对象与生命周期完整性

- rb `wall_id=1..71,686`、m `wall_id=1..27,920`，均连续；每个 ID 只属于一侧。
- 每个对象恰好一个 Start 和一个 End；首事件均为 Start，末事件均为 End。
- 未发现 Start 前更新、End 后更新、重复 Start/End 或声明外状态转换。
- relocation End 全部在同一 UTI 配有后续新 identity 的 Start：rb 3,964 次、m 64 次；顺序全部正确。

### 3.2 事件类型

| 事件 | rb | m |
|---|---:|---:|
| `Wall.Start.ByBigQuote` | 71,686 | 27,920 |
| `Wall.BandUpdate` | 113,813 | 20,056 |
| `Wall.StateChange` | 21,615 | 3,838 |
| `Wall.End` | 71,686 | 27,920 |

### 3.3 生命周期长度

| 指标 | rb | m |
|---|---:|---:|
| q00 秒 | 0.50 | 1.00 |
| q25 秒 | 3.00 | 5.00 |
| q50 秒 | 5.00 | 13.00 |
| q75 秒 | 9.50 | 30.50 |
| q95 秒 | 20.50 | 88.50 |
| q99 秒 | 33.50 | 158.00 |
| q100 秒 | 11,377.00 | 575.50 |
| mean 秒 | 7.51 | 24.54 |
| ≤6 Tick 对象 | 21,949 (30.62%) | 4,616 (16.53%) |

极短与极长对象均进入场景问题队列；统计本身不判断它们是否合理。

## 4. 状态占用与 Dormant

### 4.1 post-QT side-tick 状态

| 品种/侧 | Empty | Alive | Dormant | Ended |
|---|---:|---:|---:|---:|
| rb/bid | 56,656 | 547,110 | 4,823 | 8,137,611 |
| rb/ask | 56,771 | 521,149 | 4,172 | 8,164,108 |
| m/bid | 61,116 | 671,972 | 82 | 8,013,017 |
| m/ask | 59,433 | 698,471 | 62 | 7,988,221 |

`Ended` 是 producer slot 在终结后的持续占位，不是业务对象仍然活跃。因此活跃覆盖使用 Alive+Dormant，并与事件重建的生命周期交叉核对。rb 精确一致；m 仅差 2 个 side-tick。

| 指标 | rb | m |
|---|---:|---:|
| Active side-tick 占全部 side-tick | 6.16% | 7.84% |
| 至少一侧 active 的 Tick | 11.44% | 14.62% |

### 4.2 Dormant episode

| 指标 | rb | m |
|---|---:|---:|
| Dormant entries | 20,593 | 3,816 |
| 零时长 Dormant | 14,915 (72.43%) | 3,727 (97.67%) |
| Revival | 1,022 | 22 |

Dormant→End 同 UTI 在当前实现顺序中合法，因此这里进入高优先级场景解释问题，而不是直接宣布非法转换。

## 5. End reason 与分支可达性

| reason | rb 数量 | rb 比例 | m 数量 | m 比例 |
|---|---:|---:|---:|---:|
| `thin_contact` | 52,509 | 73.25% | 26,700 | 95.63% |
| `far_price` | 12,201 | 17.02% | 1,008 | 3.61% |
| `same_side_relocation` | 3,964 | 5.53% | 64 | 0.23% |
| `timeout` | 3,012 | 4.20% | 148 | 0.53% |
| `breakthrough` | 0 | 0.00% | 0 | 0.00% |

`breakthrough=0` 不形成结构异常：默认 wrapper 把 absorb 输入绑定为全零，此分支在当前输入合同下为 `NOT_APPLICABLE_UNDER_BOUND_INPUT`。

## 6. 同刻事件与顺序

| 指标 | rb | m |
|---|---:|---:|
| 多事件 timestamp | 28,078 | 5,142 |
| 同刻最大事件数 | 4 | 4 |
| 跨侧同刻 timestamp | 9,300 | 1,341 |
| 跨侧顺序错误 | 0 | 0 |
| relocation End | 3,964 | 64 |
| relocation 配对/顺序缺失 | 0 | 0 |

同对象同 UTI 的主要组合：

| 组合（Start|BandUpdate|StateChange|End） | rb | m |
|---|---:|---:|
| `0|0|1|1` | 14,941 | 3,727 |
| `0|1|0|1` | 548 | 69 |
| `0|1|1|0` | 517 | 15 |
| `0|1|1|1` | 142 | 5 |
| `0|2|0|0` | 131 | 1 |

## 7. GlobalFindingCandidates

### GF-001｜同一业务 OccurrenceRef 对应不同 BandUpdate payload

- 重复业务 ref 组：**132**（rb 131、m 1）。
- 受影响对象：**125/99,606 = 0.13%**。
- 多余物理行：**132/358,534 = 0.04%**。
- 全部是同一 `wall_id + UTI + event_type_code=5` 的两条 BandUpdate，`occurrence_ordinal` 不同且 band/core payload 不同。
- 当前 typed ref 合同为 `wall:<wall_id>:<uti>:<eventCode>`，不含 ordinal；同 ref 不同 payload 对当前 occurrence ledger 构成冲突候选。
- producer 物理打包本身完整且 ordinal 连续；疑点位于“物理多 occurrence”到“业务 occurrence identity”的边界。
- 代表位置：rb wall 3527 @ `2021-03-24 14:30:18.000`；m wall 9878 @ `2021-06-23 14:18:40.500`。
- 置信度：**HIGH**；下一路由：`BUSINESS_DISCREPANCY_DIAGNOSIS`。

完整 132 组见 `DUPLICATE_BUSINESS_OCCURRENCE_REFS.csv`。

## 8. ScenarioQuestionQueue

| ID | 统计模式 | 优先级 | 为什么统计不能决定 |
|---|---|---|---|
| SQ-001 | Dormant episodes are predominantly zero-duration: rb 14,915/20,593 (72.43%); m 3,727/3,816 (97.67%). Revival counts are rb 1,022 and m 22. | HIGH | The implementation explicitly allows StateChange(Dormant) followed by End in the same UTI; positive Dormant duration is not a frozen invariant. A real process window is needed to decide whether Dormant is informative or mostly an intermediate label. |
| SQ-002 | rb has 2.57x the Start density and 3.50x the event density of m; rb median life is 5s versus m 13s, while m has higher at-least-one-active tick coverage. | HIGH | Cross-symbol price tick size, quote structure and market microstructure can legitimately alter object density and life duration; statistics alone cannot declare either distribution wrong. |
| SQ-003 | thin_contact dominates m (95.63%) and rb (73.25%); rb has more far_price/relocation/timeout. breakthrough is zero in both. | MEDIUM | breakthrough is not applicable under the bound default wrapper because absorb input is all zero; low or high frequency of other reasons needs scene-level physical interpretation. |
| SQ-004 | rb post-QT event density peaks in Sep/Oct; m peaks in Jun/Sep/Dec. PM is highest-density session for both; session and month spreads are material. | MEDIUM | Market activity and price regimes vary by period/session; no reliable activity-regime field is exposed in this artifact, so density variation cannot be classified as defect from counts alone. |
| SQ-005 | rb maximum life is 11,377s (wall 11872, 09:35:24.5 to 21:00:01.5); second is 3,315s across the midday break. m maximum is 575.5s. | HIGH | UTI time and trading-session gaps may intentionally carry identity across physical breaks, but whether these lives retain business continuity requires scene review. |
| SQ-006 | rb: 21,949/71,686 lives <=6 ticks (30.62%); m: 4,616/27,920 (16.53%). rb has 61 one-tick lives, all observed minimum examples end by relocation; m minimum is 2 ticks and far_price. | MEDIUM | Short life may be a legitimate reaction to immediate relocation/far/thin evidence or may indicate over-fragmentation; the count alone does not decide. |

## 9. 分层剖面

### 9.1 Session event density（每百万 post-QT Tick）

| Session | rb | m |
|---|---:|---:|
| NIGHT_2100_2300 | 32,249.9 | 8,099.3 |
| DAY_AM1_0900_1015 | 30,294.2 | 9,258.2 |
| DAY_AM2_1030_1130 | 28,467.7 | 8,560.9 |
| DAY_PM_1330_1500 | 34,982.2 | 10,692.9 |

### 9.2 Monthly event density（每百万 post-QT Tick）

| 月份 | rb | m |
|---|---:|---:|
| 2021-02 | 5,787.4 | 6,111.1 |
| 2021-03 | 17,790.4 | 7,661.2 |
| 2021-04 | 28,388.3 | 8,057.3 |
| 2021-05 | 20,265.5 | 7,249.6 |
| 2021-06 | 27,880.7 | 13,954.4 |
| 2021-07 | 26,070.5 | 8,147.8 |
| 2021-08 | 33,625.4 | 8,892.2 |
| 2021-09 | 49,158.1 | 15,483.1 |
| 2021-10 | 50,384.3 | 6,390.4 |
| 2021-11 | 40,753.2 | 4,496.1 |
| 2021-12 | 35,296.2 | 11,240.3 |

完整事件、对象、reason 分层字段见 `STRATIFIED_EVENT_PROFILE.csv`。

## 10. CandidateCaseIndex

| Case | 来源 | 品种 | 范围 | 对象 | 选择原因 |
|---|---|---|---|---|---|
| CASE-GF001-RB-3527 | GF-001 | rb | 2021-03-24 14:30:15.000 → 2021-03-24 14:30:21.000 | 3527 | 首个 rb 业务 occurrence ref 冲突代表位置 |
| CASE-GF001-M-9878 | GF-001 | m | 2021-06-23 14:18:37.000 → 2021-06-23 14:18:44.000 | 9878 | 唯一 m 业务 occurrence ref 冲突代表位置 |
| CASE-SQ001-RB-2 | SQ-001 | rb | 2021-02-23 09:07:18.000 → 2021-02-23 09:07:24.000 | 2 | rb 零时长 Dormant 代表位置 |
| CASE-SQ001-M-2 | SQ-001 | m | 2021-02-23 10:06:10.000 → 2021-02-23 10:06:16.000 | 2 | m 零时长 Dormant 代表位置 |
| CASE-SQ005-RB-11872 | SQ-005 | rb | 2021-05-10 09:35:24.500 → 2021-05-10 21:00:01.500 | 11872 | 全年最长生命周期，跨午间/收盘到夜盘边界 |
| CASE-SQ005-RB-12648 | SQ-005 | rb | 2021-05-14 11:27:38.000 → 2021-05-14 14:22:53.000 | 12648 | 第二长生命周期，跨午休 |
| CASE-SQ004-RB-20210818 | SQ-004 | rb | 2021-08-18 00:00:00 → 2021-08-18 23:59:59.999 | — | rb 全年单日事件数最高 |
| CASE-SQ004-M-20210813 | SQ-004 | m | 2021-08-13 00:00:00 → 2021-08-13 23:59:59.999 | — | m 全年单日事件数最高 |
| CASE-SQ006-RB-11434 | SQ-006 | rb | 2021-05-06 09:05:05.000 → 2021-05-06 09:05:08.000 | 11434 | rb 最短生命周期代表位置 |
| CASE-SQ006-M-530 | SQ-006 | m | 2021-03-01 22:36:10.000 → 2021-03-01 22:36:14.000 | 530 | m 最短生命周期代表位置 |

该索引只是后续场景选择候选，不替代正式场景冻结。

## 11. DiagnosisInputAdapter

`DIA-GF-001` 已生成，包含：

- frozen expectation：同一业务 OccurrenceRef 不应标识两个不同 payload；
- 132 组完整证据及代表位置；
- `WallAssembler → wall__stream* → WallOccurrenceFao → WallLifecycle ledger` 处理链；
- 数据范围、参数版本、时间基础；
- 不提前写根因。

结构化字段见 `FEATURE_GLOBAL_BEHAVIOR_PROFILING_RESULT.yaml`。

## 12. GlobalProfileGate

```yaml
status: DIAGNOSIS_REQUIRED
reasons:
  - GF-001: 132 组相同业务 occurrence ref 对应不同 BandUpdate payload
valid_profile_ref: GBP-WALL-RB-M-2021-01
next_action: >-
  先执行 business-discrepancy-diagnosis。若处理改变 producer 或 identity 行为，
  必须重跑 Feature 与本统计；若未改变行为，也需正式关闭该疑点后才能进入场景观察。
```

这个 Gate 不表示 Wall 已被判断为不合理；它只表示全量结构检查发现了必须先诊断的身份兼容性疑点。

## 13. 附件清单

- `FEATURE_GLOBAL_BEHAVIOR_PROFILING_RESULT.yaml`：完整 Skill 输出。
- `PROFILE_SUMMARY.csv`：核心统计汇总。
- `STATISTIC_DEFINITIONS.csv`：计数单位、分母、去重和同刻规则。
- `STRATIFIED_EVENT_PROFILE.csv`：月度与 Session 分层。
- `DUPLICATE_BUSINESS_OCCURRENCE_REFS.csv`：GF-001 全部 132 组。
- `CANDIDATE_CASE_INDEX.csv`：后续场景候选索引。
