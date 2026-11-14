# D001｜Material Review

> `review_id`：`MR-WALL-001`  
> `run_id`：`OI-EAW-WALL-20261114-01`  
> `delegation_id`：`D001`  
> expectation：`EV-WALL-WORKING-v0.2 / WORKING / NOT FROZEN`  
> review mode：**EXPLORATORY**  
> readiness：**PARTIAL_WITH_LIMITS**

## 1. 审查对象

本审查消费：

- `daowei2026/observe-iterate@4edf75c2df58227084a595d869bdbe24c83e6871:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W001/WORKER_RETURN.json`
- `daowei2026/observe-iterate@c0c44515e9722c239534ac72eed942536e2ff436:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W001/WORKER_EXECUTION_REPORT.md`
- 同 commit 的 `WORKSPACE_BINDING.json`、`CODE_AND_READER_ENTRYPOINTS.md`、`ASSET_INVENTORY.json`、`SAMPLE_CHAIN.jsonl`、`SAMPLE_CHAIN_README.md`、`ACTION_PREFLIGHT_FACTS.md`、`VALIDATION_REPORT.json` 及必要 evidence 原件。

使用的专业方法：

- Observation Material Preparation；
- Business Expectation Derivation；
- Business Evidence Comparison 的探索性模式。

因为 expectation 未冻结，本审查不使用正式 `SUPPORTS/COUNTERS`，只给：

```text
EXPLORATORY_CONSISTENT
EXPLORATORY_TENSION
MISSING
AMBIGUOUS
NOT_OBSERVED
NOT_APPLICABLE
```

## 2. Evidence Preflight

### 2.1 Data binding

| 项 | 已核值 | 限制 |
|---|---|---|
| business object | Wall lifecycle | 只核 rb historical artifact |
| target | `rb` | 不是 current 新运行选择 |
| calendar | `night_end_at_2300` | 不是 current 生效配置证明 |
| product short-window path | `.../2020-12-01 21:00:00~2021-02-22 20:00:00/EawP1WallLifecycleFrp/.../rb.night_end_at_2300` | legacy physical product |
| upstream path | 同范围 `WallAssembler/.../rb.night_end_at_2300` | exact source artifact 可核 |
| receipt schema | `wall_lifecycle-v1.6.1` | upstream receipt，不是 product receipt |
| receipt code version | `git:61988a... + source-sha256:47c09e...` | 与 current TIS HEAD 不同；不能拼接 |
| product schema | `MulWrap P1Wall*Storage` | 与 current typed writer 不同 |
| product generation version | `null` | leaf 无 receipt/manifest |
| current TIS/FRP source | HEAD 与 D001 指定 baseline 相同 | 静态源码，不是物化生成版本 |
| canonical FeatureRunIdentity | `null` | legacy product 未携带完整 identity |

### 2.2 Time basis

已保留两个时间轴：

- writer firing epoch ns，并提供数值 ISO-Z；
- occurrence `p1WallLifecycleOccurredAt`，三样本与 upstream UTI 一致。

没有取得：

- 独立 actualTime；
- confirmTime；
- knownTime；
- writer epoch 的交易所当地时区合同。

因此只能写“物理 firing time”和“producer UTI”，不能自行命名为完整 actual/confirm/known。

### 2.3 Read chain

```text
legacy DBA files
→ bounded_dba_reader.py（stdlib, rb-only）
→ header/list anchor/field rows
→ upstream sparse/packed/state-trace join
→ SAMPLE_CHAIN.jsonl
```

这条链已做 size/mtime 前后不变、header、anchor、row count、exact UTI 和 source path 核验。它不是原生 FrpDbaDao runtime，也不证明 generated wrapper 可用。

### 2.4 Data quality

可接受：

- 三路 root list pointer 与 firing row 顺序已核；
- 短窗时间列单调非降；
- localNo、record counts、fields 可读；
- 原始 NaN 被显式记录为 JSON null，没有插补；
- 三样本的 source、ref、UTI 和 trigger 精确对齐。

限制：

- product generation version 缺失；
- legacy/current schema 不同；
- End band/core 表示发生信息损失；
- diagnostics 无直接 Wall identity；
- active map 不存在；
- 只有三条正常事件。

## 3. Material Eligibility

| 材料 | 输入有效性 | 业务含义 | 本次目的适用性 | 结论 |
|---|---|---|---|---|
| current TIS/FRP source | 高 | current working-tree 静态行为 | 可用于 implementation-derived expectations | `ELIGIBLE_STATIC_ONLY` |
| upstream receipt | 中高 | source scope、schema、code、artifact | 可绑定 legacy source；不能绑定 product binary | `ELIGIBLE_WITH_SCOPE` |
| sparse/packed events | 高（样本范围） | producer occurrence | 正常链 O 对账 | `ELIGIBLE_EXPLORATORY` |
| producer state trace | 高（样本点） | producer A0 state | 解释 band/core；不能替代 FRP A | `ELIGIBLE_UPSTREAM_ONLY` |
| legacy occurrences | 高（物理层） | historical accepted occurrence | 正常 chain；非 current canonical | `ELIGIBLE_LEGACY` |
| legacy current update | 高（物理层） | historical update row | 观察 Present/Ended update；非 snapshot | `ELIGIBLE_LEGACY_DELTA` |
| legacy diagnostics | 中 | historical diagnostic channel | 证明非空/字段；identity-specific 场景不足 | `ELIGIBLE_LIMITED` |
| matching native wrapper | 不存在于已核文件 | — | 不能验证 native readback | `MISSING` |
| FRP active map | 不存在 | — | 不能核删除、transaction、完整状态 | `MISSING` |
| current canonical product | 未核得 | — | 不能核 current runtime | `MISSING` |

## 4. 真实 chain

### 4.1 Chain identity

```text
upstream artifact:
  /m3varK/.../2020-12-01 21:00:00~2021-02-22 20:00:00/
  WallAssembler/.../rb.night_end_at_2300

legacy product:
  /m3varK/.../2020-12-01 21:00:00~2021-02-22 20:00:00/
  EawP1WallLifecycleFrp/.../rb.night_end_at_2300

wall_local_no: 1
```

裸 `1` 不具有跨 artifact 解释资格。

### 4.2 Chain rows

| 行 | firing | UTI | producer event | legacy occurrence | legacy current | D same firing |
|---:|---|---:|---|---|---|---:|
| 0 | 09:04:10.0Z | 72335299 | event 4 / Start / alive / 4270 | started / alive / measured / 4270 | present | 0 |
| 1 | 09:04:11.5Z | 72335302 | event 5 / BandUpdate / alive / 4269–4270 | band_updated / alive / measured / core≈4269.8528 | present | 0 |
| 2 | 09:04:14.5Z | 72335308 | event 7 / End / reason 2 / band=core=4269 | ended / not_present / band=core=0 | ended | 0 |

### 4.3 可作出的探索性观察

- Start 和非平凡 BandUpdate 在 producer、O、C 中可对账；
- End occurrence 和 Ended current update 同 firing 存在；
- End occurrence 丢弃 producer 最后 band/core，需通过 ref/UTI 回源；
- 样本内没有 diagnostic；整份短窗 D 非空；
- 没有 A，不能观察 End 后 membership；
- 三事件分别处于不同 firing，不能检验 same-firing last-update 或 transaction。

## 5. Expectation-to-Evidence Mapping

| expectation / scenario | 直接字段 | 状态 | 观察 | 不能推出 |
|---|---|---|---|---|
| Identity scoped by artifact+localNo | source path、localNo、ref、UTI | `EXPLORATORY_CONSISTENT` | 三行在同 artifact/localNo 下连续 | current FeatureRunIdentity、跨 run identity |
| S01 Start Present | change/presence/current + upstream | `EXPLORATORY_CONSISTENT` | started→present | Start Dormant 拒绝 |
| S03 BandUpdate preserves presence | change/presence/band/current | `EXPLORATORY_CONSISTENT` | presence 保持，band/core 变化 | 非法 presence change 处理 |
| S07 End publication | End occurrence/current | `EXPLORATORY_CONSISTENT` for O/C | Ended update 实际存在 | A 删除、End 后事件 |
| End measurement contract | upstream vs occurrence | `EXPLORATORY_TENSION` | 4269 被压为 0/not_present | 当前 schema 是否仍如此、是否错误 |
| current update is delta | O/C counts + source | `EXPLORATORY_CONSISTENT` | record 数不一、源码明示 update | current 表全部行为、A snapshot |
| diagnostic channel | D fields/counts | `EXPLORATORY_CONSISTENT` for existence | 328 firing；前三条 ingress invalid band | state diagnostic、identity-specific mapping |
| Dormant/restore | — | `MISSING` | 无自然样本 | transition合理性 |
| duplicate/conflict | — | `MISSING` | 无输入/输出链 | same/cross firing 幂等 |
| mixed valid+invalid firing | — | `MISSING` | 无 pre/post A | transaction 原子性 |
| late/out-of-order | trigger + UTI仅正常顺序 | `NOT_OBSERVED` | 样本顺序正常 | late policy |
| five missingness states | receipt/read结果 | `AMBIGUOUS` | 材料层能区分存在/不可读 | runtime五类领域状态 |

## 6. 三层 Input Assessment

### 6.1 输入有效性

结论：`VALID_FOR_BOUNDED_LEGACY_EXPLORATION`。

理由：物理结构、anchor、row count、时间、ref 和 upstream join 均有直接证据。产品生成版本缺失阻止其进入 current canonical comparison。

### 6.2 输入业务合理性

结论：`LOCALLY_REASONABLE`。

正常链足以表达 producer 认出的同一 Wall 的 Start、属性更新和 End；但旧 End occurrence 的 measurement 压缩、diagnostic 无身份、A 缺失，使其不能完整表达终止后的当前状态和异常链。

### 6.3 对当前目的的适用性

结论：`PARTIAL`。

- 对 Q1 正常生命周期：局部适用；
- 对 Q2 O/C 正常 publication：局部适用；
- 对 Q2 A/D/transaction：不适用；
- 对 Q3 current full suitability：不适用；
- 对下一轮场景选择：适用。

## 7. Evidence-induced candidates

### EIC-01｜End measurement semantics

候选问题：End occurrence 是否应保留最后 band/core，还是明确 `not_present` 并要求 join upstream？

区分材料：current canonical schema + End sample + 下游消费合同。

### EIC-02｜Diagnostic correlation key

候选问题：diagnostic 是否应携带 identity/ref/batch，或能经 firing 无歧义映射到 rejected input？

区分材料：current `WallDiagnostic` 物化和混合错误 fixture。

### EIC-03｜Terminal identity memory

候选问题：若 producer 同 run local no 绝不复用且 End 后不再发事件，源码当前删除 terminal state 可能足够；否则需要 terminal ledger 或明确 violation mapping。

区分材料：producer invariant + End 后同号 fixture。

### EIC-04｜Cross-firing idempotence

候选问题：ledger 的 firing-local scope 是否符合 replay contract？

区分材料：upstream ref uniqueness policy + cross-firing duplicate/conflict fixture。

## 8. Discrepancy Queue

| ID | 问题 | 业务影响 | 当前替代解释 | 推荐区分动作 |
|---|---|---|---|---|
| DQ-01 | End 后同号 Start 可能重新接受 | identity 完整性高风险 | producer 保证永不发生 | current fixture + producer contract |
| DQ-02 | current source 与 legacy product schema/version不绑定 | 无法判断现役行为 | historical artifact 正常遗留 | 取得生成 manifest或隔离 current run |
| DQ-03 | End band/core 上游与 occurrence表示不同 | 终止背景解释损失 | `not_present` 为有意合同 | current schema + consumer review |
| DQ-04 | D 无 identity | 异常链不可审计 | firing 本身可能足够原子 | mixed batch sample + current D schema |
| DQ-05 | 同 firing 一错全退 | 可能丢合法 Wall 变化 | firing 可能是不可分 transaction | firing formation contract + pre/post A |

不进入诊断：没有证据的 Dormant 行为本身；它先保持 `MISSING`。

## 9. Review Decision

```text
Material package accepted: YES, with professional scope limits
Legacy normal-chain reuse: YES
Current runtime acceptance: NO
Formal evidence comparison: NO
Full expectation freeze: NO
Need W001 rework: NO
Need immediate W002: NO
```

W001 已充分完成只读事实调查；关键剩余需要 manager 决定是否进入更窄 G-RUN／独立证据生产，而不是重复扫描。
