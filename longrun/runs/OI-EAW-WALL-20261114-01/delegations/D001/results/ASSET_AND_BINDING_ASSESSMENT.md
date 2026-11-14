# D001｜Asset and Binding Assessment

> `run_id`：`OI-EAW-WALL-20261114-01`  
> `delegation_id`：`D001`  
> 更新调用：`C0004`  
> Worker：`W001`  
> 当前材料状态：**PARTIAL_WITH_LIMITS**  
> 当前 D 专业状态：**可回交；不等于父任务完成**

## 1. 专业结论

W001 的正式回交及其冻结证据包可以接受为**真实现场调查结果**，但只能在下列边界内使用：

1. 当前 BASE 中 TIS、FRP 的 checkout、HEAD、branch、dirty 和相关源码已经真实核定；
2. 当前相关源码文本与 D001 指定阅读基线在相关路径上相同；
3. 真实存在 WallAssembler receipt／sparse／state trace，以及两组历史三路 Wall 产品；
4. 其中短窗旧物化已经用有界物理 reader 解码，并取得三条可复核的 `Start → BandUpdate → End` 链；
5. 这些产品是 **legacy `P1Wall*Storage` 物化**，产品自身生成版本回执缺失，不能绑定为当前 canonical typed writer 的运行结果；
6. 当前 generated wrapper 不含旧三类或当前三类 Wall ADT，原生 reader 运行态未验证；
7. FRP DSU 完整 active map、Dormant／恢复、重复／冲突／非法／迟到和同 firing 混合事务证据仍缺失。

所以准确关系是：

```text
current source checkout verified
≠ current runtime tuple verified

legacy material exists and is physically decodable
≠ current canonical material

normal-chain sample reconciled
≠ lifecycle semantics fully validated

worker return accepted as evidence
≠ business suitability passed
```

## 2. W001 专业消费

### 2.1 正式回交

- Worker Return：`daowei2026/observe-iterate@4edf75c2df58227084a595d869bdbe24c83e6871:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W001/WORKER_RETURN.json`
- 执行报告：`daowei2026/observe-iterate@c0c44515e9722c239534ac72eed942536e2ff436:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W001/WORKER_EXECUTION_REPORT.md`
- 原件 manifest：`daowei2026/observe-iterate@c0c44515e9722c239534ac72eed942536e2ff436:longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W001/PUBLICATION_MANIFEST.json`

主控已独立核验原件出版、hash、V2 schema 和路由。E1 进一步阅读了工作区绑定、源码／reader 入口、资产库存、物理数据统计、样本链、预检和必要验证原件。

### 2.2 接受范围

| Worker 事实 | 专业处理 |
|---|---|
| 真实 cwd/thread/model/effort、单写者和权限边界 | 接受；只用于证明 W001 真实执行 |
| 当前 repo/worktree/HEAD/dirty | 接受；相关源码可作为当前 working-tree 静态事实 |
| 物化目录、文件数量、大小和字段布局 | 接受；限已核路径与扫描范围 |
| 旧短窗／全年产品的 firing、record 数 | 接受；全年只接受首尾及数量，不扩写为全局统计 |
| 三条真实局部链 | 接受为 legacy historical exploratory material |
| bounded physical reader 的解码结果 | 接受为物理布局解码；不当原生生产 reader 通过 |
| current tuple、产品生成版本、active map 等缺口 | 保留；不得用当前 HEAD 或目录名补齐 |

## 3. 当前工作区绑定

### 3.1 核心仓库

| 仓库 | 真实路径 | HEAD / branch | 初始 dirty | 与 D001 相关路径 |
|---|---|---|---|---|
| TIS | `/dwdhome/fy/BASE_E6_2/mquant/tis` | `ef887396e0a06d6e75be47efee0f1985ad7988a3` / `eaw/p123-integration-20260820` | `frpExample/STCalendar.py` 已有修改 | 指定旧阅读 SHA 与当前 HEAD 相同 |
| FRP | `/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp` | `cac6c912dd65a14acbd591ca57e0afd8ddb4ef13` / `eaw/p123-integration-20260820` | `src/Frp/Instance/BussinessUtils.hs` 已有修改 | P1 相关路径相对基线 diff 为空 |
| frp-core | `/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp-core` | `d3153e085cd0d99d86876b73aeb1d05497638f80` / `e6.2` | 无已记录修改 | Fao CalType／读写分派依据 |

其他 frame、worker、m3sof、m3、pydim 等绑定详见 W001 `WORKSPACE_BINDING.json`。它们的既有 dirty 未被修改，也不能被拼接成一次现役运行配置。

### 3.2 当前代码可确认的静态组合

- TIS `WallOccurrenceFao`：`OnlyRead`；
- TIS `_CalculatedP1Product`：`Cache`，直接 `to_df()` 主动拒绝；
- FRP `EawP1WallLifecycleFrp`：`Cal`；
- Fao core 对 `OnlyRead / Cal / Cache` 的分派逻辑已经定位；
- `doFrpTaskParam(run_ups=True)` 可能执行上游并写 task linker，不是安全只读入口；
- 当前正式 writer 名仍为 `wall_occurrences / wall_current_view / wall_diagnostics`；
- 当前源码明确把 current writer 定义为本 firing 的 update，而非全量快照。

这些是当前 working-tree 的实现事实，不是当前二进制实际运行证明。

## 4. 配置、包装与 reader

### 4.1 参数和范围

WallAssembler 源码默认值已经定位，包括 `qt_freq=1d`、`qt_n=30`、`qt_quantile=0.997`、`w_depth_ref_ticks=1200`、`p_wall_ticks=1`、`t_wall_ticks=6` 等；这些是源码默认，不是本次生效参数。

现有上游 receipt 给出：

```text
target: rb
calendar: night_end_at_2300
schema: wall_lifecycle-v1.6.1
code_version: git:61988a3723ebadc861b4e94284254275be843255
              + source-sha256:47c09eb4ac84034ab9140be79249c338e266fa2b922ce1c14c021a3857b771f6
```

当前产品生成 binary、参数、对象、日历、范围与当前代码形成的完整 tuple：**UNKNOWN**。

### 4.2 generated wrapper

`/dwdhome/fy/BASE_E6_2/mquant/worker/adt/dbaw.py` 存在，113,663 bytes，AST 共 118 类，但未见：

- legacy：`MulWrap_P1WallOccurrenceStorage`、`MulWrap_P1WallCurrentStorage`、`MulWrap_P1DiagnosticStorage`；
- current：`WallOccurrenceBatch`、`WallCurrentBatch`、`WallDiagnostic`。

所以：

```text
generic wrapper exists
but matching native Wall wrapper is missing in inspected file
```

W001 没有重生成 wrapper，也没有导入可能产生副作用的项目运行环境。原生 `FrpDbaDao` 路径只做到静态定位。

### 4.3 reader 资格

- 原生 reader 运行态：`NOT_VERIFIED`；
- W001 `bounded_dba_reader.py`：`VERIFIED_FOR_BOUNDED_PHYSICAL_LAYOUT_ONLY`；
- 当前 canonical typed ADT readback：`NOT_VERIFIED`。

## 5. 物化资产

### 5.1 已核范围

三个代码／配置指向的候选 prod 根经过一层清单和 588 个明确类路径存在性检查；进入已存在 Wall 相关目录后，共清点：

```text
155 directories
796 files
41,550,396,966 bytes metadata total
```

这不是全盘无界扫描，也没有全量读取 41.55GB。

### 5.2 两组历史三路产品

| 目录范围 | occurrence firing / records | current firing / records | diagnostic firing / records | 专业资格 |
|---|---:|---:|---:|---|
| `2020-12-01 21:00:00~2021-02-22 20:00:00` | 14,858 / 15,809 | 14,858 / 15,208 | 328 / 328 | legacy，短窗部分完整解码，可做局部探索 |
| `2021-01-01 21:00:00~2021-12-31 20:00:00` | 241,659 / 266,469 | 241,659 / 254,424 | 7,456 / 7,469 | legacy，仅 header、数量和首尾；不可扩写为全量业务统计 |

短窗三路 physical firing timestamp 全列范围：

- occurrences/current：`2021-01-14T09:04:10Z` ～ `2021-02-22T14:44:30Z`；
- diagnostics：`2021-01-14T09:31:19.5Z` ～ `2021-02-22T10:09:03.5Z`。

目录范围、上游 receipt source range 和实际有输出的 firing range 不得混同。

### 5.3 schema 断点

历史 fields 为：

```text
MulWrap_P1WallOccurrenceStorage
MulWrap_P1WallCurrentStorage
MulWrap_P1DiagnosticStorage
```

当前源码 writer 为：

```text
WallOccurrenceBatch
WallCurrentBatch
WallDiagnostic
```

产品 leaf 中没有找到生成版本 receipt／manifest。因此不能把历史产品贴上当前 TIS/FRP HEAD，也不能把旧字段当当前 canonical schema。

## 6. 真实局部链

已核 chain：同一上游 artifact、`wall_local_no=1`、`rb / night_end_at_2300`。

| writer firing | UTI | occurrence | current update | 上游 |
|---|---:|---|---|---|
| `2021-01-14T09:04:10Z` | 72335299 | Start / Present / band=core=4270 | Present | sparse、packed、state trace 对齐 |
| `2021-01-14T09:04:11.5Z` | 72335302 | BandUpdate / Present / low=4269, high=4270, core≈4269.8528 | Present | sparse、packed、state trace 对齐 |
| `2021-01-14T09:04:14.5Z` | 72335308 | End / `not_present` / stored band/core=0 | Ended | 上游 sparse/trace band/core=4269 |

专业解释：

- 该链证明旧物化内 occurrence、current update、上游 sparse/packed 和 producer trace 可在三个 firing 上物理对账；
- End 时旧 occurrence 的 band/core 归零且标为 `not_present`，而上游仍保留 4269。这是明确的**转换信息损失／语义压缩**，不是由 E1 直接认定为 bug；解释 End 前最后 band/core 必须回到上游材料；
- `FeatureRunIdentity` 没有从旧产品获得。该链只能用“精确上游 artifact + local no”定位，不能把裸 local no 提升为跨 artifact 身份；
- producer trace 不是 FRP active map；active deletion 没有被物理验证；
- 样本没有 Dormant／恢复，也不是同 firing 多变化样本。

## 7. diagnostics

短窗 diagnostics 非空，共 328 firing。前三条实读为：

```text
source = ingress
kind = InvalidNumericDomain
field = wall_band
message = band_lo <= core_price <= band_hi is required
```

三条正常链同 firing 的 diagnostic 数为 0。限制：legacy diagnostics 没有直接 Wall identity 字段，只能按 firing 对齐，不能据此完成 identity-specific 异常链；“样本同 firing 无诊断”也不证明异常分支正确。

## 8. 资产资格阶梯

| 层级 | 状态 | 说明 |
|---|---|---|
| `SOURCE_BASELINE_VERIFIED` | YES | current checkout 与指定相关源码基线相同 |
| `CURRENT_CHECKOUT_VERIFIED` | YES | repo/worktree/HEAD/dirty 已核 |
| `CURRENT_CONFIG_VERIFIED` | NO | current effective params/target/calendar/range/binary 未绑定 |
| `LEGACY_ASSET_EXISTS` | YES | receipt/sparse/trace/三路产品存在 |
| `LEGACY_ASSET_DECODABLE` | PARTIAL | 短窗 bounded physical decode；全年仅 header/首尾 |
| `LEGACY_IDENTITY_COMPLETE` | PARTIAL | artifact+local no 可用；canonical FeatureRunIdentity 缺失 |
| `CURRENT_CANONICAL_ASSET_EXISTS` | NOT VERIFIED | 未核 current typed materialization |
| `CURRENT_NATIVE_READER_READY` | NO | matching wrapper 缺失，runtime 未验证 |
| `MATERIAL_PURPOSE_SUITABLE` | PARTIAL | 仅正常 legacy chain 与局部 publication 关系 |
| `DATA_READY` | NO | 不满足正式全场景／当前版本对照 |

综合 readiness：**PARTIAL_WITH_LIMITS**。

## 9. 三个业务问题的可回答范围

| 问题 | 当前可回答 | 当前不能回答 |
|---|---|---|
| `Q-WALL-IDENTITY-LIFECYCLE` | artifact+localNo 下的 legacy Start→BandUpdate→End 正常链；当前源码的 transition 静态语义 | canonical run identity、Dormant/恢复、duplicate/conflict/late、End 后事件与 runtime 行为 |
| `Q-WALL-PUBLICATION-STATE` | legacy occurrence/current/diagnostic 的物理存在、计数、三 firing 对账、End update | FRP active-map 删除、同 firing 最后更新规则的真实多更新样本、事务回滚、current canonical schema |
| `Q-WALL-BUSINESS-SUITABILITY` | 可建立局部材料基线和高价值反例队列 | 不能对现役完整语义作 PASS/FAIL，不能冻结全量 expectation |

## 10. Action Eligibility

| 动作 | 资格 |
|---|---|
| 使用 legacy chain 做探索性材料审查 | ELIGIBLE |
| 将 W001 作为当前 runtime PASS | NOT ELIGIBLE |
| 对全套 expectation 作正式 SUPPORTS/COUNTERS | NOT ELIGIBLE |
| 直接运行现有 integration runner | NOT ELIGIBLE：会 build、跑多个上游/产品，写面和成本未闭合 |
| 全年/全品种重算 | NOT AUTHORIZED |
| 修改 TIS/FRP/schema/wrapper | NOT AUTHORIZED |
| 提交 manager 后续 G-PLAN／G-RUN 候选 | ELIGIBLE，见 `ACTION_PREFLIGHT.md` |

## 11. 当前处理决定

- **接受 W001 正式回交作为本 D 的事实证据包**；
- 不返修 W001：已完成的只读事实与缺口表达满足原 W 合同；
- 不签 W002：当前剩余关键缺口不是另一次同边界只读扫描即可闭合；新运行需要 manager 的 G-RUN 和更窄、可验证的动作；
- D001 可按 `PARTIAL_WITH_LIMITS` 回交；这表示专业基线工作已完成，不表示三个业务问题或父任务已经完成。
