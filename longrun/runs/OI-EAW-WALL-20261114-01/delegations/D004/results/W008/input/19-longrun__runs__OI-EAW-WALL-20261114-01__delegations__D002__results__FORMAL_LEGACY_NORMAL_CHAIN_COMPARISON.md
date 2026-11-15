# D002｜Formal Legacy Normal-Chain Comparison

> `run_id`：`OI-EAW-WALL-20261114-01`  
> `delegation_id`：`D002`  
> `stage_instance_id`：`R-NORMAL-COMP-001`  
> `work_item_id`：`WI-WALL-LEGACY-NORMAL-COMP-001`  
> `analysis_round_id`：`AR-WALL-002`  
> `comparison_id`：`EC-WALL-LEGACY-NORMAL-001`  
> `expectation_version`：`EV-WALL-LEGACY-NORMAL-v1.0`  
> expectation 状态：`FROZEN_FOR_COMPARISON`  
> comparison 状态：**COMPLETE_FOR_FROZEN_SCOPE**

## 1. 比较边界

本次只比较 manager 在下列决定中冻结的四条命题：

`daowei2026/observe-iterate@9ce476e26079b10a5806a9a20fb63db1abe5d02d:longrun/runs/OI-EAW-WALL-20261114-01/business_control/decisions/MD-C0005-001.md`

冻结命题：

```text
FN-IDENTITY-01
FN-START-01
FN-BAND-01
FN-END-01
```

只适用于：

```text
historical legacy material
object/calendar = rb / night_end_at_2300
exact upstream artifact + exact legacy product leaf
wall_local_no = 1
UTI = 72335299, 72335302, 72335308
three separate writer firings
```

固定解释：

- `C` 是本次 update/delta row，不是 full active-map snapshot；
- 缺失 row 不补造成“状态未变”；
- legacy product generation version 仍缺；
- End occurrence 的 `0 + not_present` 不解释为真实价格 0；
- current source只作静态解释上下文，不绑定为 legacy product 的生成版本；
- 四条命题独立判断，不形成总体分数。

本比较不涉及 current canonical runtime、FRP active-map、Dormant／恢复、diagnostic identity、duplicate／conflict、same-firing transaction、End 后同号事件、late／out-of-order 或完整业务适用性。

## 2. Frozen expectation 与证据输入

### 2.1 Frozen expectation

- 版本：`EV-WALL-LEGACY-NORMAL-v1.0`
- 来源：manager 从 D001 的 BUSINESS_INFERRED 正常链命题中限域冻结；未把 evidence-induced candidates 冻结为结论。
- 冻结前已见样本：是。因此本轮只按预先写明的命题、反驳条件和适用边界判断，不把观察反向改写为命题。

### 2.2 正式材料

- D001 material manifest：  
  `daowei2026/observe-iterate@2b4d60f868ef715d12ba14131871227ba95517ea:longrun/runs/OI-EAW-WALL-20261114-01/delegations/D001/results/MATERIAL_MANIFEST.json`
- 三行真实链：  
  `daowei2026/observe-iterate@c0c44515e9722c239534ac72eed942536e2ff436:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W001/SAMPLE_CHAIN.jsonl`
- 样本方法与限制：  
  `daowei2026/observe-iterate@c0c44515e9722c239534ac72eed942536e2ff436:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W001/SAMPLE_CHAIN_README.md`
- root-list／chain reconciliation：  
  `daowei2026/observe-iterate@c0c44515e9722c239534ac72eed942536e2ff436:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W001/evidence/CHAIN_RECONCILIATION_VALIDATION.json`
- 有界物理统计与 probe：  
  `daowei2026/observe-iterate@c0c44515e9722c239534ac72eed942536e2ff436:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W001/evidence/PHYSICAL_DATA_STATS.json`  
  `daowei2026/observe-iterate@c0c44515e9722c239534ac72eed942536e2ff436:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W001/evidence/SHORT_WINDOW_PHYSICAL_PROBE.json`

未重新读取相同三行链，也未产生新的数据材料。

# 3. EvidencePreflight

## 3.1 Business intent 与 Judgment target

本次判断对象不是“整个 WallLifecycle 实现是否合理”，而是：

> 在已冻结的 exact historical artifact normal chain 中，producer 已识别的同一 Wall 是否保持 artifact-scoped identity，并在 Start、非平凡 BandUpdate、End 三个正常事件上形成可追溯的 legacy occurrence/current update publication。

## 3.2 DataBinding

### upstream artifact

```text
/m3varK/BaseData/futures/TA_updto20240229_DBA/fao/prod/
2020-12-01 21:00:00~2021-02-22 20:00:00/
WallAssembler/8/8/5/1/d/6/1/b25bd29dd0d30a972dfabd41edcdf0518/
rb.night_end_at_2300
```

### legacy product leaf

```text
/m3varK/BaseData/futures/TA_updto20240229_DBA/fao/prod/
2020-12-01 21:00:00~2021-02-22 20:00:00/
EawP1WallLifecycleFrp/1/c/b/0/c/1/4/44aea11813b85d33becc06242f43621b6/
rb.night_end_at_2300
```

### object/scope

```text
target          = rb
calendar        = night_end_at_2300
wall_local_no   = 1
```

目录范围、upstream receipt source range 与实际 writer firing range不被混同。

## 3.3 Identity

可直接使用：

```text
exact upstream artifact path
target/calendar
wall_local_no
occurrence_ref
UTI
writer firing
```

不可直接使用：

```text
current canonical FeatureRunIdentity
legacy product generation binary identity
naked localNo outside exact artifact namespace
```

三条 occurrence ref 均显式包含同一 upstream artifact、`wall__stream`、各自 UTI、localNo=1 与 event code：

```text
...:wall__stream:72335299:1:4
...:wall__stream:72335302:1:5
...:wall__stream:72335308:1:7
```

## 3.4 Time basis

已取得：

| role | value |
|---|---|
| writer firing 1 | `2021-01-14T09:04:10.000000000Z` |
| writer firing 2 | `2021-01-14T09:04:11.500000000Z` |
| writer firing 3 | `2021-01-14T09:04:14.500000000Z` |
| producer UTI | `72335299 / 72335302 / 72335308` |
| upstream `ts` | 与对应 writer firing 的数值时间一致 |

未取得且不推断：

```text
actualTime
observedTime
confirmTime
knownTime
```

本轮“同一 writer firing”只由 physical firing anchor／epoch equality 判定，不把它改名为业务 confirm time。

## 3.5 Version 与 schema

### upstream

```text
schema = wall_lifecycle-v1.6.1
code   = git:61988a3723ebadc861b4e94284254275be843255
         + source-sha256:47c09eb4ac84034ab9140be79249c338e266fa2b922ce1c14c021a3857b771f6
```

### legacy product physical schema

```text
MulWrap_P1WallOccurrenceStorage
MulWrap_P1WallCurrentStorage
MulWrap_P1DiagnosticStorage
```

### unresolved gap

```text
legacy product generation code/binary version = MISSING
```

current working-tree TIS／FRP HEAD 只用于理解字段角色和 delta／active-map 区别，不被贴到历史产品。

## 3.6 Read chain

```text
legacy DBA physical files
→ W001 bounded physical reader
→ root list pointer / value-row anchor
→ writer firing equality
→ upstream sparse / packed / producer state-trace exact UTI join
→ SAMPLE_CHAIN.jsonl
```

该链通过文件大小／mtime保持、header、anchor、row count、exact UTI 和 source path 核验。它不是 native `FrpDbaDao` runtime，也不证明 generated wrapper 可用。

## 3.7 Data validity

| 检查 | 结果 |
|---|---|
| exact product/source path | VERIFIED |
| 三条 O rows 可物理解码 | VERIFIED |
| 三条 C rows 与 O same-firing | VERIFIED |
| upstream sparse/packed exact UTI join | VERIFIED |
| producer state trace exact UTI join | VERIFIED |
| localNo continuity | VERIFIED in exact artifact |
| row/firing order | VERIFIED for three rows |
| duplicate/conflict | NOT TESTED |
| actual/confirm/known role | MISSING |
| product generation version | MISSING |
| FRP active map | MISSING |
| diagnostics identity | MISSING |

非有限 `reason_code` 在前两行按原存储事实记录为 JSON `null`，没有插补；它不参与四条冻结命题。

## 3.8 Evidence dependency

四条判断共享：

- 同一 exact upstream artifact；
- 同一 legacy product leaf；
- 同一三行 physical chain；
- 同一 upstream join 方法；
- 同一 bounded reader／reconciliation evidence。

因此：

```text
four proposition judgments
≠ four independent evidence sources
```

它们是对同一条链不同位置的形式判断，不作“4票通过”式汇总。

## 3.9 InputAssessment

### 输入有效性

`VALID_FOR_FROZEN_EXACT_CHAIN`。

### 输入业务合理性

能够表达 exact artifact 内 producer-recognized Wall 的 Start、非平凡 band update、End，以及 legacy O/C publication；不能表达 full active state 或异常语义。

### 对当前目的适用性

`SUITABLE_FOR_FROZEN_NORMAL_CHAIN_COMPARISON_ONLY`。

不适合 current runtime、完整 lifecycle、active map、transaction/replay 或 full suitability。

# 4. 三行证据表

| position | writer firing | UTI | upstream | legacy O | legacy C | D same firing |
|---|---|---:|---|---|---|---:|
| P1 | `09:04:10.0Z` | 72335299 | event 4；wall_id=1；alive；band/core=4270 | Start；localNo=1；Present/alive；measured；band/core=4270 | localNo=1；Present | 0 |
| P2 | `09:04:11.5Z` | 72335302 | event 5；wall_id=1；alive；low=4269；high=4270；core≈4269.8528 | BandUpdate；localNo=1；alive；同 band/core | localNo=1；Present | 0 |
| P3 | `09:04:14.5Z` | 72335308 | event 7；wall_id=1；status=3；reason=2；band/core=4269 | End；localNo=1；`not_present`；stored band/core=0 | localNo=1；Ended | 0 |

D 同 firing 为 0 只表示这三个正常 firing 未观察到 diagnostic；不证明异常路径正确。

# 5. 逐命题正式对照

## 5.1 `FN-IDENTITY-01`｜artifact-scoped identity continuity

### Frozen statement

在同一 exact feature artifact/run namespace 内，连续 occurrence 的 local number、ref 和 UTI 应能无歧义指向 producer 已认出的同一 Wall；不得把裸 local number 跨 artifact 连接。

### Judgment

**`SUPPORTS`**

### 直接证据

- 三条 upstream sparse／packed rows 均来自同一 exact artifact；
- `wall_id=1` 保持不变；
- UTI 严格为 `72335299 → 72335302 → 72335308`；
- legacy O 的 `p1WallOccurrenceLocalNo=1`；
- occurrence ref 同时保留 exact upstream artifact、stream、UTI、local no 和 event code；
- event code `4→5→7` 与 Start→BandUpdate→End 对应。

### 反证

在冻结范围内未观察到相同标识指向不同 Wall，亦未观察到链断裂。

### 缺失／歧义

- current canonical FeatureRunIdentity 不在 legacy shape 中；
- product generation version 缺失；
- 没有跨 artifact 对照，也不需要跨 artifact 才能判断本命题。

### 替代解释

三条 row 可能属于历史 schema 生成物；这影响向 current schema 的迁移，不改变 exact artifact 内 ref/localNo/UTI 的物理连续性。

### 适用范围

仅该 exact artifact、localNo=1、三条事件。

### 不能推出

- 裸 localNo 在其他 artifact 中仍是同一 Wall；
- current canonical identity 完整；
- producer 永不复用 localNo；
- End 后同号事件合同正确。

### Confidence

`HIGH_WITHIN_FROZEN_SCOPE`。

---

## 5.2 `FN-START-01`｜normal Start publication

### Frozen statement

正常生命周期由 `Start Present` 建立；被接受的 Start 应在同一 writer firing 中具有可追溯 occurrence Start 和 current Present update。

### Judgment

**`SUPPORTS`**

### 直接证据

在 `2021-01-14T09:04:10Z`：

- upstream event code 4，status alive，wall_id=1；
- legacy O 为 `started / alive / measured`，localNo=1，band/core=4270；
- legacy C 同一 physical writer firing 有 localNo=1、state=`present`；
- upstream sparse、packed、state trace、O、C 的 UTI／timestamp／identity一致。

### 反证

冻结位置没有缺 O、缺 C 或状态／身份不一致。

### 缺失／歧义

FRP A 未持久化，因此不能用本位置物理观察 active-map add；该内容不属于本冻结命题。

### 替代解释

C 是 update row 而不是 full snapshot；本命题只要求 Start 的同 firing Present update，正好由该 row 直接表达。

### 适用范围

该 Start normal event。

### 不能推出

- Start Dormant 的处理；
- duplicate Start；
- transaction rollback；
- current canonical writer 行为。

### Confidence

`HIGH_WITHIN_FROZEN_SCOPE`。

---

## 5.3 `FN-BAND-01`｜nontrivial BandUpdate continuity

### Frozen statement

同一 Wall 的非平凡 BandUpdate 应保持 identity 和 presence，同时更新 band/core；被接受的更新应在同一 writer firing 中具有可追溯 occurrence BandUpdate 和 current Present update。

### Judgment

**`SUPPORTS`**

### 直接证据

P1→P2：

- localNo／wall_id 保持 1；
- presence/status 保持 `alive / present`；
- band 从 `[4270,4270]` 变为 `[4269,4270]`；
- core 从 4270 变为约 4269.8527778236985；
- upstream event code 5 与 legacy O `band_updated` 一致；
- legacy O 与 C Present 位于 `2021-01-14T09:04:11.5Z` 同一 writer firing；
- occurrence ref 保留 UTI=72335302、localNo=1、event code 5。

### 反证

没有 identity／presence 无合同改变，也没有 O/C 失配。

### 缺失／歧义

没有 A；不能物理观察完整 current map replacement。该内容不属于冻结命题。

### 替代解释

数值变化不是浮点噪声式“无变化”：band low 明确下降一个单位，且 upstream／O 同值。

### 适用范围

该单一非平凡 BandUpdate。

### 不能推出

- Dormant 状态下 BandUpdate；
- BandUpdate 改 presence 的拒绝；
- 多条 update 同 firing 的 last-update 语义；
- late UTI policy。

### Confidence

`HIGH_WITHIN_FROZEN_SCOPE`。

---

## 5.4 `FN-END-01`｜normal End publication

### Frozen statement

正常 End 应在同一 writer firing 中具有可追溯 occurrence End 和 current Ended update。

### Judgment

**`SUPPORTS`**

### 直接证据

在 `2021-01-14T09:04:14.5Z`：

- upstream event code 7、status 3、reason 2、wall_id=1；
- legacy O 为 `ended`，localNo=1，ref UTI=72335308/event code 7；
- legacy C 同一 physical writer firing 为 localNo=1、state=`ended`；
- O／C／upstream timestamp 和 identity 可对账。

### 反证

冻结位置没有接受 End 后缺 O／C、identity/time 失配或 C 非 Ended。

### 缺失／歧义

- FRP A 缺失；不能观察 End 后 active-map deletion；
- End 后同号事件没有样本；
- actual／confirm／known time 未独立保存。

### 替代解释与信息损失

upstream End row 保留 band/core=4269，而 legacy O 写为 `not_present` 且 band/core=0。按冻结解释规则，0 是“不提供 measurement”的物理表示，不是真实价格 0。该差异是 evidence-induced candidate，不反驳本命题要求的 O End + C Ended publication。

### 适用范围

该单一 normal End。

### 不能推出

- A 删除已验证；
- End 后 update/end/Start 被正确分类；
- End measurement contract 对 current schema 合适；
- terminal identity memory 完整。

### Confidence

`HIGH_WITHIN_FROZEN_SCOPE`。

# 6. Comparison Summary

| expectation | status | direct distinction achieved | principal limit |
|---|---|---|---|
| `FN-IDENTITY-01` | `SUPPORTS` | exact artifact 内 localNo/ref/UTI 连续 | 不支持跨 artifact／current identity |
| `FN-START-01` | `SUPPORTS` | Start O + Present C same firing | 无 A，不覆盖异常 Start |
| `FN-BAND-01` | `SUPPORTS` | nontrivial band/core update + Present C same firing | 单一 update，无 same-firing multi-update |
| `FN-END-01` | `SUPPORTS` | End O + Ended C same firing | 无 A 删除；End measurement 有信息损失 |

本表不是总体 PASS 分数。四项依赖同一条 physical chain，不能计为四份独立共证。

# 7. Formal findings 与发现路由

## 7.1 正式 COUNTERS

`NONE`。

因此本轮不触发 `G-DIAGNOSIS` 候选。

## 7.2 Evidence-induced candidate

### `EIC-END-MEASUREMENT-LEGACY-01`

观察：producer End 仍有 band/core=4269，legacy O 使用 `0 + not_present`。

当前解释：可能是有意的“不适用”编码，也可能对需要最后几何背景的 consumer 造成信息损失。

路由：保持 candidate；未来由 current canonical schema、consumer contract 与 current End material 区分。不得回写或修改 frozen v1.0。

## 7.3 Version-gap finding

legacy product generation version 仍缺。它不阻止 exact physical chain 的局部比较，但阻止把本结果归因于 current source binary或外推为 current runtime。

# 8. 专业结论与 manager Gate 建议

本轮已完成 `EV-WALL-LEGACY-NORMAL-v1.0` 的正式逐命题 comparison。

E1 建议 manager 对 narrow `G-COMPARISON` 判定：

```text
PASS_WITH_SCOPE
```

准确含义：

- 四条冻结 normal-chain 命题在 exact historical chain 上均获得 `SUPPORTS`；
- 没有正式 `COUNTERS`；
- 结果只闭合 frozen scope；
- 不解锁 current runtime、active map、异常场景、full expectation freeze、full suitability 或父任务完成。

最终 Gate 仍由 manager 决定。
