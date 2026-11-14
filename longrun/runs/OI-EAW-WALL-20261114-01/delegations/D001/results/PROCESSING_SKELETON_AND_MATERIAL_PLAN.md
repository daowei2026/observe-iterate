# D001｜Processing Skeleton 与 Material Plan

> `run_id`：`OI-EAW-WALL-20261114-01`  
> `delegation_id`：`D001`  
> `analysis_round_id`：`AR-WALL-001`  
> 更新调用：`C0004`  
> 当前材料状态：**PARTIAL_WITH_LIMITS**  
> expectation：`EV-WALL-WORKING-v0.2 / WORKING / NOT FROZEN`

## 1. 目的和边界

本文把 current working-tree 静态实现、真实 historical legacy material、缺失证据和后续最小动作放入同一处理骨架。它服务：

- `Q-WALL-IDENTITY-LIFECYCLE`；
- `Q-WALL-PUBLICATION-STATE`；
- `Q-WALL-BUSINESS-SUITABILITY`。

本轮没有执行新计算、没有 current canonical product、没有 FRP active-map trace。因此本文给出的是**可接续基线**，不是现役业务合理性 PASS。

## 2. 当前绑定总览

### 2.1 current working-tree

```text
TIS  /dwdhome/fy/BASE_E6_2/mquant/tis
     HEAD ef887396e0a06d6e75be47efee0f1985ad7988a3

FRP  /dwdhome/fy/BASE_E6_2/edh-universe/frp/frp
     HEAD cac6c912dd65a14acbd591ca57e0afd8ddb4ef13
```

D001 指定的 P1 相关源码与当前 checkout 对齐；相关路径 diff 为空。未相关的 `STCalendar.py`、`BussinessUtils.hs` 等既有 dirty 不被本 D 消除，也未被 W001 修改。

### 2.2 historical material binding

```text
target: rb
calendar: night_end_at_2300
upstream receipt schema: wall_lifecycle-v1.6.1
upstream receipt code:
  git:61988a3723ebadc861b4e94284254275be843255
  + source-sha256:47c09eb4ac84034ab9140be79249c338e266fa2b922ce1c14c021a3857b771f6
product physical schema:
  MulWrap P1WallOccurrenceStorage
  MulWrap P1WallCurrentStorage
  MulWrap P1DiagnosticStorage
product generation code receipt: MISSING
```

因此 current source 与 historical material 必须并列，不得拼成一个 tuple。

## 3. 处理骨架与当前证据状态

```text
S0 WallAssembler
  receipt / fields / sparse events / packed streams / producer state trace
        ↓
S1 WallOccurrenceFao ingress
  receipt+artifact 校验 / packed decode / ingress diagnostics
        ↓
S2 WallLifecycleP transaction
  occurrence ledger / transition / active map / current-update map / diagnostics
        ↓
S3 publication
  wall_occurrences / wall_current_view / wall_diagnostics
        ↓
S4 readback and analysis
  exact identity + firing/order + O/C/A/D + business context
```

### 3.1 分阶段合同

| 阶段 | 业务输入／身份 | 处理状态 | 输出角色 | 时间 | W001 后状态 |
|---|---|---|---|---|---|
| S0 WallAssembler | source run、参数、target、calendar、producer `wall_id` | 同 run 内维护 Wall slot；生成 sparse/packed/trace | receipt、sparse event、state trace | `uti`、`ts`、chunk | historical receipt/sparse/trace 存在并局部可读；current effective tuple 未绑定 |
| S1 typed ingress | committed artifact + receipt + fields/result key | 解码、数值/enum/identity 校验；错误进入 ingress diagnostic | typed occurrence batch 或 diagnostic | firing trigger + payload UTI | current source可读；legacy product不证明 current ingress runtime；diagnostic 实物存在 |
| S2 lifecycle | 同 firing typed occurrences | ledger、transition、active map、last current update、transaction commit/rollback | accepted occurrence、full active map、update batch、state diagnostics | 输入顺序；旧源码未独立核 UTI 单调 | current source语义已核；FRP active map/runtime trace 缺失 |
| S3 publication | lifecycle outputs | typed ADT → DBA | O=`wall_occurrences`；C=`wall_current_view` update；D=`wall_diagnostics` | writer firing time | legacy 三路实物可解码；current canonical schema未核 |
| S4 analysis | receipt + O/C/D + A 或可验证 replay +背景 | identity/time/version 对账、场景比较 | material review | actual/confirm/known 按事实保留 | 正常 legacy 链可做探索；完整正式比较不具备资格 |

## 4. current source 可确认的实现语义

以下由当前 checkout 的相关源码直接支持，但仍不等于当前 runtime 已执行：

1. `WallOccurrenceFao` 是 `OnlyRead`，FRP product 是 `Cal`，TIS product wrapper 是 `Cache`；三者属于不同层；
2. current writer 名为 `wall_occurrences / wall_current_view / wall_diagnostics`；
3. lifecycle working state 分开保存 occurrence ledger、active map 与本 firing update map；
4. current public writer 发布 update stream，不是完整 active-map snapshot；
5. End 会形成 Ended current update，并从 active map 删除 identity；
6. ingress 任一 decode error 会拒绝该 firing typed batch；lifecycle 任一 state error 会使该 firing state transaction 不提交；
7. occurrence ledger 在旧／当前相关源码中按 firing 新建，其直接去重／冲突范围不是自动的 run-wide；
8. End 后 active map 不再保存 terminal identity，未见独立 ended-id ledger，End 后同号 Start／update 的真实边界仍是高价值反例候选；
9. transition 按输入顺序处理，未见独立 payload UTI 单调检查。

第 6～9 项必须通过当前运行材料或受控 fixture 判断实际可达性和业务影响，不能只凭代码判最终不合理。

## 5. historical material 的实际处理链

### 5.1 正常链

已取得：

```text
upstream sparse / packed / producer trace
  localNo=1
  UTI 72335299 Start
  UTI 72335302 BandUpdate
  UTI 72335308 End
        ↓
legacy wall_occurrences
        ↓ same physical firing
legacy wall_current_view updates
        ↓
legacy diagnostics count at same firing = 0
```

三条 writer trigger：

```text
2021-01-14T09:04:10.0Z
2021-01-14T09:04:11.5Z
2021-01-14T09:04:14.5Z
```

### 5.2 身份语义

可用身份：

```text
exact upstream artifact path
+ target rb
+ calendar night_end_at_2300
+ wall_local_no 1
+ occurrence ref
+ UTI
```

缺失：

```text
current canonical FeatureRunIdentity
product generation code version
current binary/config tuple
```

所以该链只允许在 exact artifact namespace 内解释。

### 5.3 End 转换损失

End 上游仍保存 `band_lo=band_hi=core=4269`；legacy occurrence 写出：

```text
measurement = not_present
band/core = 0
```

这说明旧公开 occurrence 不保留 End 时 producer band/core。需要 End 前最后几何背景时，必须联合上游 sparse/trace；不能把 0 当真实价格，也不能擅自填回 occurrence。

### 5.4 current 与 active map

三条样本分别有 `Present / Present / Ended` current update。它们只证明 update 行存在；没有 FRP active map，所以：

- 能观察 Ended update；
- 不能直接观察 End 后 active map 删除；
- 不能用 current 缺行补造完整状态；
- 不能验证同 firing 多变化时“只保留最后 update”的真实效果。

### 5.5 diagnostics

短窗共 328 diagnostic firing，前三条为 ingress `InvalidNumericDomain / wall_band`。legacy diagnostic 无 Wall identity 字段；只能按 firing 判断是否同刻有 diagnostic，不能重建 identity-specific 异常 transition。

## 6. Material Requirement Set：W001 后状态

| ID | 级别 | 材料 | 回答 Q | 当前状态 | 专业处理 |
|---|---|---|---|---|---|
| MR-01 | 必需 | receipt/source scope/参数/schema/code/artifact | 三个 Q | **PARTIAL** | upstream receipt 有；product generation/current tuple 缺 |
| MR-02 | 必需 | current checkout/source/wrapper | 三个 Q | **PARTIAL** | source checkout 已核；matching wrapper/current reader 缺 |
| MR-03 | 必需 | producer sparse/packed events | identity/lifecycle/publication | **AVAILABLE_LEGACY** | 三条真实链可对账；完整场景未抽取 |
| MR-04 | 必需 | `wall_occurrences` | identity/lifecycle/publication | **AVAILABLE_LEGACY** | 短窗可解码；current schema 未核 |
| MR-05 | 必需 | `wall_current_view` update | publication/state | **AVAILABLE_LEGACY** | 三 firing 对账；不是 active map |
| MR-06 | 必需 | `wall_diagnostics` | publication/suitability | **AVAILABLE_LEGACY_PARTIAL** | 非空、字段可读；无 Wall identity，异常覆盖不足 |
| MR-07 | 必需 | FRP full active map 或等价 replay | publication/state | **MISSING** | producer trace 不能替代 |
| MR-08 | 必需 | firing boundary/order/list anchors | txn/duplicate/late | **PARTIAL** | legacy root list pointers 与三链顺序已核；current runtime 分组未知 |
| MR-09 | 条件需要 | producer state trace/price/band/core | 解释变化/End | **AVAILABLE_LEGACY** | 已用于三链；GB级范围不全读 |
| MR-10 | 条件需要 | duplicate/conflict/invalid/late 场景 | lifecycle/suitability | **MISSING** | 自然样本未取得；需 fixture 或更定向材料 |
| MR-11 | 条件需要 | 原始 L1/tick/QT | producer 偏差诊断 | **NOT_PREPARED** | 当前 Q 不先展开 |
| MR-12 | 可选 | CAEGraph/Notebook | 人工局部观察 | **NOT_ELIGIBLE_AS_PRIMARY_EVIDENCE** | 旧 EawBattleP 图不冒充 WallLifecycle |
| MR-13 | 暂不准备 | Build/Attack/Absorb 独立产品 | 非本 D | **EXCLUDED** | 只在 identity 接缝必要时引用 |
| MR-14 | 暂不准备 | 全年/全品种重算 | 非基线必要 | **PROHIBITED** | W001 只对全年 header/首尾做有限读取 |

## 7. 材料 readiness

```text
Source baseline:                 VERIFIED_CURRENT_CHECKOUT
Current effective tuple:         UNBOUND
Legacy upstream material:        AVAILABLE
Legacy three-writer material:    AVAILABLE
Legacy bounded decodability:     PARTIAL_VERIFIED
Current canonical material:      NOT VERIFIED
FRP active-map evidence:         MISSING
Real normal-chain sample:        OBTAINED
Full scenario coverage:          MISSING
Overall:                         PARTIAL_WITH_LIMITS
```

## 8. Material Plan 决定

### 8.1 现在直接复用

复用 W001 三条 historical chain，限定用于：

- exact artifact namespace 内的正常身份连续性；
- Start、非平凡 BandUpdate、End 的 producer→occurrence 映射；
- occurrence 与 current update 同 firing 的探索性对账；
- End measurement 信息损失；
- diagnostics channel 非空这一事实。

详见 `MATERIAL_REVIEW.md` 和 `MATERIAL_MANIFEST.json`。

### 8.2 现在不做正式比较

不启动：

- current canonical schema 全场景正式对照；
- active-map 删除验证；
- duplicate/conflict/late/co-fired transaction 判断；
- Dormant/恢复覆盖；
- 参数或实现修改。

原因：expectation 未冻结、current tuple 未绑定、材料缺关键中间状态。

### 8.3 不签 W002

另一轮同边界只读扫描不能可靠产生：

- 缺失的 product generation receipt；
- matching generated wrapper；
- FRP active-map trace；
- current canonical scenario outputs。

若 manager 决定进入 current schema 材料生产，应先通过 G-RUN 选择一个隔离、wall-only、成本可预检的动作；不得把现有 multi-product integration runner 原样启动。详见 `ACTION_PREFLIGHT.md`。

## 9. Gate 建议

| Gate | E1 建议 | 原因 |
|---|---|---|
| G-PLAN：legacy material reuse | **可进入候选** | 范围、身份和限制已经可审计 |
| G-EXPECTATION-FREEZE：全量 set | **暂不通过** | current tuple、A、异常场景和时间角色缺失 |
| G-RUN：现有 runner 原样执行 | **不通过** | 自动 build、多上游/多产品、写面和成本不闭合 |
| G-RUN：未来 wall-only isolated action | **可由 manager 评审候选** | 需先绑定 fixture、参数、预热、binary、store/cache/log、stop points |
| Formal Evidence Comparison | **不启动** | 只有 WORKING expectations；当前只做 exploratory review |

## 10. D001 当前收束

D001 已完成合同要求的：

- current checkout 与资产事实核验；
- processing skeleton；
- material requirement 与 plan；
- WORKING expectation/scenario 更新；
- historical exploratory material review；
- accurate preflight。

其专业交付结果为 `PARTIAL_WITH_LIMITS`。后续 current run、冻结、正式对照和父任务完成均由 manager 的下一层 Gate 决定。
