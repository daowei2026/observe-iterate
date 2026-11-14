# W001 当前源码、包装和读取入口

所有路径以 `/dwdhome/fy/BASE_E6_2` 为前缀；下表 repo 的完整 HEAD、branch、dirty、remote、worktree 原件见 `WORKSPACE_BINDING.json`。本报告中的静态事实只适用于已读取的 working tree 文本，不把它们提升为物化生成版本。

| repo | 路径 | HEAD | branch | 初始未提交状态 |
|---|---|---|---|---|
| tis | `/dwdhome/fy/BASE_E6_2/mquant/tis` | `ef887396e0a06d6e75be47efee0f1985ad7988a3` | eaw/p123-integration-20260820 |  M frpExample/STCalendar.py |
| frp | `/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp` | `cac6c912dd65a14acbd591ca57e0afd8ddb4ef13` | eaw/p123-integration-20260820 |  M src/Frp/Instance/BussinessUtils.hs |
| frame | `/dwdhome/fy/BASE_E6_2/mquant/frame` | `4d0ff8f2640e07a8b9ff066c48114f451fca6cfe` | e6.2 | 无已记录修改 |
| worker | `/dwdhome/fy/BASE_E6_2/mquant/worker` | `da0475a9c7fa769c2db8c803a5376ff2cdf09e0d` | e6.2 |  M __init__.py<br> M params/__init__.py<br> M params/cae/__init__.py<br> M params/cae/nodes/ScaleTurnCAEGraph.py<br> M params/cae/nodes/__init__.py<br>?? params/cae/nodes/RecoveredStandardizedHFCAEGraph.py |
| frp-core | `/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp-core` | `d3153e085cd0d99d86876b73aeb1d05497638f80` | e6.2 | 无已记录修改 |
| hasdim | `/dwdhome/fy/BASE_E6_2/edh-universe/e-wrks/hasdim` | `43c11e34822a4877e83a8316fbd6051499805d3f` | master | 无已记录修改 |
| mpds | `/dwdhome/fy/BASE_E6_2/edh-universe/mpds` | `26245696c1cdcd7c1b0202e00c998ef7f55ee0b0` | 6.2 | 无已记录修改 |
| m3sof | `/dwdhome/fy/BASE_E6_2/m3sof` | `f2d5b316b2d323c6344778f22561d56d258d252b` | codex/aidata-csv-feature-smoke-20261019 |  M __init__.py<br> M core/__init__.py<br> M settings/app.py<br> M settings/env/default.py<br> M settings/env/dev.py<br> M settings/env/prod.py<br> M settings/env/test.py<br> M settings/sof/CTP.py<br>?? settings/.ipynb_checkpoints/<br>?? settings/env/.ipynb_checkpoints/<br>?? settings/sof/.ipynb_checkpoints/<br>?? settings/sof/GTQH_L1_20210104_20240208.py<br>?? settings/sof/GTQH_L1_20210104_20240229.py |
| m3 | `/dwdhome/fy/BASE_E6_2/m3` | `62dddc5f6ad9247eb4508867117a570b6573584d` | new_ver | ?? mts/rebuild-prod<br>?? perfp/rebuild-prod |
| pydim | `/dwdhome/fy/BASE_E6_2/pydim` | `0dbe020a29f0bb1f7a37fae2cfa0a64827350fc8` | master | ?? dim/rt.bak |

## 1. 实际注册、配置及层间 Cal 组合

1. TIS `/dwdhome/fy/BASE_E6_2/mquant/tis/frp/EawBattleP.py:34` 定义 `_OnlyReadTypedIngress`，37–38 返回 `CalType.OnlyRead`；54–55 的 `WallOccurrenceFao` 默认 source 为 `WallAssembler()`。41–51 的 `_CalculatedP1Product` 返回 `CalType.Cache`，其 `to_df()` 主动抛 TypeError。93–97 的 `EawP1WallLifecycleFrp` 仅有 `wallLifecycleInput`，`doFrpUpSource()` 显式返回 assembler。不能通过改用下游 EawBattleP 绕过本 W 的 Wall 材料要求。
2. FRP `/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance.hs:67` 注册 Wall 产品。`src/Frp/Instance/ISL/Eaw/P1.hs:71` 是 newtype 包装，97–99 FaoMeta 为 `CalendarTarType SymbolType / Cal`；121–129 为 ingress → lifecycle → diagnostics 合并；177–180 绑定 `dumpWallOutputs / doWallLifecycleFrp`。
3. FRP `P1/FaoIngress.hs:240` 的 source 是 PyAny；285–287 为 Calendar Symbol / OnlyRead；313–317 读取 kind `wall_lifecycle`，dump 会报 read-only。166–185 强制 source 同目录 `p1_receipts/wall_lifecycle.json`，并核 receipt artifact_location 与实际 fullDir。
4. `frp-core/src/Frp/Core/Fao/Class.hs:614`：按实例 propCalType 分派；632–640 的 OnlyRead 只 load，缺材料报错；642 的 Cal 走 doImpl；643–660 的 Cache 依全局 Cal/Gen 决定 load 或 doImplAndDump。这是不同层的静态声明。缺当前真实任务参数、二进制及生成回执，不能凭 Python Cache 和 Haskell Cal 两个值判断本机可安全生成或复用。
5. `mquant/frame/lang/frp/base.py:97` 的 `doFrpTaskParam(run_ups=True)` 默认可能执行上游；116–143 直接 `up.run()`。149–183 写 task linker 并 `epm exec ts --f=... --jp=...`；204–206 还会删除 task 文件。它是执行入口，不是本 W 可用的只读 probe。

## 2. 对象、日历、参数与范围的来源

- `mquant/tis/hf/prel0/wall_assembler.py:681` 是默认参数：`wall-default`、qt_freq=1d、qt_n=30、qt_quantile=0.997、w_depth_ref_ticks=1200、p_wall_ticks=1、t_wall_ticks=6；near/far/timeout 等若干默认 None，再由 `make_wall_params` 推导。该默认值不是现役执行参数。712–735 读取 `.P` 并加载 cc/qt；838–860 构造 receipt，actual/private 参数、source_scope、source fingerprint 和能力分别记录。
- `m3sof/settings/app.py:4` 当前文本 ENV=prod；`env/default.py:13,18,21` 为 `/m3varK`、fao、TB，42 为默认小时 21:00/20:00；`sof/default.py:13,21,28` 为默认 calendar=all、category=BaseData/futures、full_period=None。`sof/TA_updto20240229_DBA.py:9,12,22,33` 定义相应源名、m3varI 基础源及 calendar_dir。配置仓库有 dirty 改动；未导入设置，不声称这些层合并后的本次任务值。
- `/dwdhome/fy/BASE_E6_2/config.yml:3` 显式给出 `/m3varK/BaseData/futures/TA_updto20240229_DBA/fao/prod` 作为候选存储根。这是候选目录来源，不证明本次特征采用该配置。
- 现场旧 receipt 给出 rb / night_end_at_2300、具体 source cut、业务参数和 code_version；详见库存。它们与当前 TIS HEAD 的关系尚未核成完整 tuple。
- 没有本 Run 的当前计算任务/物化生成回执。目标/日历/范围的现役生效值为 UNKNOWN；旧 receipt 与代码默认分开列。

## 3. 路径构造与 reader

`frp-core/src/Frp/Core/Fao/Class.hs:437` 对 ggjson 求 sha1；441–445 将参数 hash 的前 8 个字符逐层展开。447–454 从 store_dirs 覆盖或 Sof store_dir 取根；456–489 拼接 category/sof/store_name/env/[日期范围]/class/hash/target；503–519 取 Sof 起止范围及多存储根。目标 Calendar 表示和实际日期字符串以现场路径为准。不得自行从 class 名合成一个运行 tuple。

`mquant/frame/lang/frp/base.py:75` 返回 FrpDbaDao。`mquant/frame/lang/internal/dao/frp/dba.py:25` 定位 fields.json；46–53 优先 gfull_dir 再 full_dir；55–97 的 loadWith 读取字段并用 DbaStore + DbaUtil.read_field_ts 组装。ADT 类型经 `core/store.py:500` 的 eval2 求值，后者 `core/base/json.py:79,147` 导入 `m3sof.settings.json`。因此未证明导入副作用前不实际调用这个路径。`.to_dfs()` 在 mixin 第86行仍会访问 `.F`，不能当安全旁路。

generated wrapper **确实存在**：`/dwdhome/fy/BASE_E6_2/mquant/worker/adt/dbaw.py`，113663 bytes，sha256 `d6a58f6cb6595461ead45bb08c002826856bcacaab9e50c0e62cd45d76e7e4f2`。AST 检查有 118 个类，未见任何 Wall/P1 类，旧三类 `MulWrap_P1WallOccurrenceStorage / MulWrap_P1WallCurrentStorage / MulWrap_P1DiagnosticStorage` 和当前三类也均缺。`mquant/worker/adt/__init__.py:63` 导入 dbaw；worker README 第47–60行说明生成入口。本 W 未重新生成 wrapper，未安装依赖，未调用任何生成器。未对其它环境中的动态注入作全局不存在断言。

安全实读使用本 W `bounded_dba_reader.py`，只依 stdlib 与已核物理 layout，读既有文件 rb；它不是新的生产 reader。当前原生 reader 运行态未验证，历史物理字段的有界解码已验证。

## 4. 当前三路 writer 与真实旧物化分开

`frp/src/Frp/Instance/ISL/Eaw/P1/Publication.hs:611`：WallOccurrenceBatch.wallOccurrences=[WallLifecycleOccurrence]；616：WallCurrentBatch.wallCurrentViews=[WallCurrentView]；621：WallDiagnostic.wallDiagnosticError=P1ProductDiagnostics WallLifecycleError。684–688 writer 名严格为 `wall_occurrences / wall_current_view / wall_diagnostics`。681–682 注释明确 current writer 是本次更新，不是全量快照。

`Products.hs:443` 的 WallIdentity 实际是仅含 `wallIdentityLocalNo :: Int64` 的 newtype；186–196 另有 FeatureRunIdentity 九字段结构，486–490 的 occurrence 保存 identity/ref/payload；576–580 的 current 保存 identity/state/occurrence。这些静态结构不能被自动拼成物化样本中的完整 run identity。是否满足业务身份合同由 E1 专业审查。

`WallLifecycle.hs:38` 区分 ledger、views 和 update batch；78–89 处理 current 更新及 End 删除 active map；103–107 分别暴露 occurrence event、完整 current Dynamic、current updates、diagnostics；115 起为事务处理。以上只说明源码，不证明现场该二进制执行过这些分支。

实际两个产品 leaf 的 fields.json 都是 `adt@MulWrap_P1WallOccurrenceStorage / P1WallCurrentStorage / P1DiagnosticStorage`，而非上述当前 Batch 物理类型。短窗旧 occurrence 物理字段包括 localNo、ref、occurredAt(Int)、side/change/presence、band/core、availability/reason；旧 current 仅 localNo/state；诊断为 source/kind/text/int/double。全字段、路径、数量与 hash 见库存。产品 code receipt 缺失；不能把这些旧列视为当前 canonical ADT。

## 5. WallAssembler receipt、sparse、trace

`wall_assembler.py:139–209` 构造 sparse/trace；397 定义 trace schema；749–837 按交易日 chunk 写 trace，保留 compact results 并生成 sparse、packed streams；838–860 暂存 receipt。`p1_product_receipt.py:125` 绑定 git 与源文件 fingerprint；`source_scope` 和 receipt 写入口均在该文件。`p1_dba_export.py:1–4` 明确薄适配依现有 DBA，551 以后在 dump 成功后写 receipt。

`FaoIngress.hs:109–151,202–238` 的 packed reader 每 result key 注册一条行事件，先读 metadata，再可能映射整列。不能因为是 packed 就绕过大数据成本检查。

现场找到了真正的 sparse/trace/receipt；样本精确对应键见 SAMPLE_CHAIN。上游 trace 是 A0 状态，未找到/未取得 FRP DSU 完整 active-map 物化。原始大文件均留在原路径。

## 6. 尚未解除的竞争解释及最小查证

旧物化可能由历史 schema 的二进制产生；也可能是同参数目录中分阶段写入/遗留内容。产品无生成版本回执，mtime 和目录名不足以区分。最小后继是先找准确生成 manifest/二进制记录或由 E1 决定隔离的当前 wall-only 材料动作；不能把当前 HEAD 贴到旧数据上，也不能运行默认多产品入口求证。本 W 到此只给 ActionPreflight。
