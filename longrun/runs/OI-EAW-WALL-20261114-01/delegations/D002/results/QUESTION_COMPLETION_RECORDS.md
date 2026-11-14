# D002｜Question Completion Records

> `run_id`：`OI-EAW-WALL-20261114-01`  
> `delegation_id`：`D002`  
> 来源 comparison：`EC-WALL-LEGACY-NORMAL-001`  
> 冻结版本：`EV-WALL-LEGACY-NORMAL-v1.0`  
> 性质：**限域子问题完成候选；不关闭三个原业务问题或父任务**

## 1. 记录规则

本文件使用以下状态：

```text
COMPLETE_FOR_SCOPE
COMPLETE_AS_BOUNDARY
PARTIAL
OPEN
```

`COMPLETE_FOR_SCOPE` 只表示：冻结的对象、材料、命题和判断深度已穷尽，且已有正式 comparison 结果。它不自动传播到父 question。

`COMPLETE_AS_BOUNDARY` 表示：已经能够稳定说明“现有材料不能回答什么、为什么不能以及下一层需要何种不同证据”，但没有给出被排除范围内的正面业务结论。

正式 Gate 与 QuestionCompletion 决定仍由原 manager 作出。

# 2. QCR-LEGACY-IDENTITY-NORMAL-001

| 字段 | 内容 |
|---|---|
| `record_id` | `QCR-LEGACY-IDENTITY-NORMAL-001` |
| parent question | `Q-WALL-IDENTITY-LIFECYCLE` |
| scoped question | historical exact-artifact normal identity continuity |
| scope | exact upstream artifact + exact legacy product leaf；`rb/night_end_at_2300`；localNo=1；UTI `72335299/302/308` |
| frozen expectation | `FN-IDENTITY-01` |
| formal status | `SUPPORTS` |
| completion candidate | **`COMPLETE_FOR_SCOPE`** |

## 2.1 Completion criteria

- exact source/product scope 被绑定；
- local no、occurrence ref、UTI 和 event type 可连续对账；
- Start→BandUpdate→End 的 source/O 身份没有冲突；
- 跨 artifact 外推被明确禁止；
- evidence dependency 和版本缺口被保留。

上述条件均已满足。

## 2.2 Evidence basis

同一 upstream artifact 内：

```text
wall_id/localNo = 1
UTI              = 72335299 → 72335302 → 72335308
event code       = 4 → 5 → 7
change           = Start → BandUpdate → End
```

occurrence ref 同时包含 exact artifact path、stream、UTI、localNo 和 event code。正式比较没有发现链断裂或相同标识指向不同 Wall。

## 2.3 What is closed

可以限域结案：

> 在该 exact historical artifact 中，这三条 normal occurrences 能作为 producer 已认出的同一 Wall 的连续生命周期链使用；裸 localNo 不具备跨 artifact 身份资格。

## 2.4 What remains open

- current canonical FeatureRunIdentity；
- localNo 全 run 不复用不变量；
- Dormant／恢复；
- same/cross-firing duplicate/conflict；
- End 后同号事件；
- late/out-of-order；
- current runtime。

因此 parent `Q-WALL-IDENTITY-LIFECYCLE`：**OPEN**。

## 2.5 Reopen condition

只有发现该 exact chain 的 anchor／identity 证据错误、物化损坏或更高修订 source evidence 时，才重开本 scoped record。current 新证据属于新的 scope，不重开这一历史记录。

# 3. QCR-LEGACY-OC-PUBLICATION-NORMAL-001

| 字段 | 内容 |
|---|---|
| `record_id` | `QCR-LEGACY-OC-PUBLICATION-NORMAL-001` |
| parent question | `Q-WALL-PUBLICATION-STATE` |
| scoped question | historical Start/BandUpdate/End normal O/C publication |
| scope | 同一 exact historical chain 的三个独立 writer firing |
| frozen expectations | `FN-START-01 / FN-BAND-01 / FN-END-01` |
| formal status | `SUPPORTS / SUPPORTS / SUPPORTS` |
| completion candidate | **`COMPLETE_FOR_SCOPE`** |

## 3.1 Completion criteria

- Start O 与 Present C same-firing；
- nontrivial BandUpdate 保持 identity/presence、更新 band/core，并与 Present C same-firing；
- End O 与 Ended C same-firing；
- C 只按 update/delta 解读；
- 没有用缺行补造 snapshot；
- A、D 和异常语义不混入本子问题。

上述条件均已满足。

## 3.2 Evidence basis

| event | O | C | same firing |
|---|---|---|---|
| Start UTI 72335299 | `started / alive / band=core=4270` | `present` | yes |
| BandUpdate UTI 72335302 | `band_updated / alive / low=4269/high=4270/core≈4269.8528` | `present` | yes |
| End UTI 72335308 | `ended / not_present` | `ended` | yes |

三条 row 均与 upstream sparse／packed 和 producer trace 的对应 UTI、timestamp、identity 对账。

## 3.3 What is closed

可以限域结案：

> 该 historical normal chain 的 Start、非平凡 BandUpdate 和 End 均存在可追溯 legacy occurrence，并在同一 writer firing 形成冻结命题要求的 current update。

## 3.4 What remains open

- full active-map add/update/delete；
- same-firing 多次合法更新只保留最后 C；
- ingress/state transaction rollback；
- current canonical O/C/D schema；
- native reader；
- identity-specific diagnostics；
- End 后状态；
- actual／confirm／known time roles。

因此 parent `Q-WALL-PUBLICATION-STATE`：**OPEN**。

## 3.5 End measurement note

legacy End O 的 `0 + not_present` 与 upstream 4269 不同。它作为 `EIC-END-MEASUREMENT-LEGACY-01` 保留，不推翻本子问题 O End + C Ended 的完成；也不在本记录中定性为缺陷。

# 4. QCR-LEGACY-TO-CURRENT-NONEXTRAPOLATION-001

| 字段 | 内容 |
|---|---|
| `record_id` | `QCR-LEGACY-TO-CURRENT-NONEXTRAPOLATION-001` |
| parent question | `Q-WALL-BUSINESS-SUITABILITY` |
| scoped question | legacy normal-chain 对 current full suitability 的不可外推边界 |
| completion candidate | **`COMPLETE_AS_BOUNDARY`** |

## 4.1 Boundary criteria

要完成该边界记录，需要明确：

1. historical material 能回答什么；
2. current runtime 仍缺什么；
3. 为什么相同正常链不能替代缺失证据；
4. 下一层证据必须改变哪一项材料性质，而不是重复读取同一链。

上述四项均已形成稳定答案。

## 4.2 Accepted local use

legacy normal chain 适用于：

- exact artifact identity continuity；
- Start/BandUpdate/End 的正常 O/C publication；
- current update 必须按 delta 解读这一材料读取规则；
- End measurement information-loss candidate 的识别。

## 4.3 Non-extrapolation basis

以下断点均为直接事实：

```text
legacy product generation version       = MISSING
legacy physical schema                  ≠ current typed writer schema
matching generated Wall wrapper         = MISSING in inspected dbaw.py
native reader runtime                   = NOT VERIFIED
current canonical product material      = NOT OBTAINED
FRP full active map                      = MISSING
Dormant/duplicate/conflict/transaction  = MISSING
End-after/late/out-of-order             = MISSING
actual/confirm/known time contract       = MISSING
```

current source checkout 只能说明 static implementation，不把这些断点补齐。

## 4.4 What is closed

可以限域结案：

> 无论四条 normal-chain 命题在 historical material 上是否获得支持，该结果都不具备外推为 current canonical runtime 或完整业务 suitability PASS/FAIL 的资格；重复读取相同三行链不会解除这一边界。

## 4.5 What remains open

`Q-WALL-BUSINESS-SUITABILITY` 的正面判断仍需：

- current generation tuple；
- current schema/native read；
- O/C/A/D；
- terminal／replay／atomicity／late 等高价值场景；
- 必要时冻结新的 expectation version 后正式 comparison。

因此 parent `Q-WALL-BUSINESS-SUITABILITY`：**OPEN**。

# 5. Parent Question Status

| parent question | scoped records completed | remaining decisive scope | parent close candidate |
|---|---|---|---|
| `Q-WALL-IDENTITY-LIFECYCLE` | exact historical normal continuity | current identity、Dormant、replay、terminal、late | **NO** |
| `Q-WALL-PUBLICATION-STATE` | historical normal O/C publication | A、same-firing last update、transactions、current reader/schema/D | **NO** |
| `Q-WALL-BUSINESS-SUITABILITY` | non-extrapolation boundary | current high-value evidence + frozen comparison | **NO** |

# 6. Completion Recommendation

E1 建议 manager：

```text
ACCEPT QCR-LEGACY-IDENTITY-NORMAL-001
ACCEPT QCR-LEGACY-OC-PUBLICATION-NORMAL-001
ACCEPT QCR-LEGACY-TO-CURRENT-NONEXTRAPOLATION-001
KEEP all three parent questions OPEN
KEEP parent task INCOMPLETE
```

本文件没有创建新的 Owner 请求，也没有把 manager Gate 预先判定为通过。
