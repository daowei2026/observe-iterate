import pathlib, json, datetime, hashlib

W=pathlib.Path(__file__).resolve().parent
B=pathlib.Path('/dwdhome/fy/BASE_E6_2')
RUN='OI-EAW-WALL-20261114-01'
E1='chatgpt:'+RUN+':executor:E1'
ORDER_REF='daowei2026/observe-iterate@ad20770c69bc431d2e9188dcecd89883bce20cfa:longrun/runs/'+RUN+'/work_orders/W001/ORDER.json'
DEST='longrun/runs/'+RUN+'/worker_results/W001/'
binding=json.loads((W/'WORKSPACE_BINDING.json').read_text())
meta=json.loads((W/'evidence/WALL_ASSET_METADATA.json').read_text())
stats=json.loads((W/'evidence/PHYSICAL_DATA_STATS.json').read_text())
wrapper=json.loads((W/'evidence/GENERATED_WRAPPER_BINDING.json').read_text())
sample=[json.loads(x) for x in (W/'SAMPLE_CHAIN.jsonl').read_text().splitlines()]
short=next(x for x in stats['assets'] if '2020-12-01' in x['source_leaf'])
year=next(x for x in stats['assets'] if '2021-12-31' in x['source_leaf'])
up=sample[0]['identity']['upstream_artifact_location']
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def write(name,text):
    with (W/name).open('x') as f:f.write(text.strip()+'\n')
def dump(name,value):write(name,json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False))
repo_by_name={x['name']:x for x in binding['repos']}
repo_rows=[]
for name in ('tis','frp','frame','worker','frp-core','hasdim','mpds','m3sof','m3','pydim'):
    x=repo_by_name[name];cmd=x['commands'];status=cmd['status']['stdout'].strip().splitlines()
    repo_rows.append('| '+name+' | `'+x['path']+'` | `'+cmd['head']['stdout'].strip()+'` | '+cmd['branch']['stdout'].strip()+' | '+('<br>'.join(status[1:]) if len(status)>1 else '无已记录修改')+' |')
repos_table='\n'.join(repo_rows)

# Inventory retains every observed asset path and metadata fact; no market-data copy.
assets=[]
for a in meta['assets']:
    item={k:v for k,v in a.items() if k not in ('files','directories')}
    item['directory_metadata']=a['directories']
    item['files']=a['files']
    item['file_count_is_complete_within_class_root']=not a['stopped']
    item['sha256_null_reason']='大文件仅元数据；不为 hash 强读大文件。小文件已按原始 bytes 核 sha256。'
    item['leaves']=[]
    for leaf in a['leaf_parents']:
        fs=[f for f in a['files'] if f['path'].startswith(leaf+'/')]
        fields=next((f for f in fs if f['path']==leaf+'/fields.json'),None)
        receipts=[f for f in fs if '/p1_receipts/' in f['path'] and 'json' in f]
        ps=next((s for s in stats['assets'] if s['source_leaf']==leaf),None)
        d={'absolute_path':leaf,'files':len(fs),'total_bytes':sum(f['bytes'] for f in fs),
           'fields_exists':fields is not None,'fields_sha256':fields['sha256'] if fields else None,
           'fields_reason':None if fields else '未观察到 fields.json',
           'schema':fields.get('json') if fields else None,
           'receipt_files':[{'path':r['path'],'sha256':r['sha256'],'receipt':r['json']} for r in receipts],
           'object_calendar_path_hint':pathlib.Path(leaf).name,
           'target':receipts[0]['json'].get('source_scope',{}).get('target') if receipts else None,
           'target_reason':None if receipts else '仅目录对象/日历提示，缺该产品 receipt，不提升为生成配置事实',
           'calendar':receipts[0]['json'].get('source_scope',{}).get('calendar_or_session') if receipts else None,
           'calendar_reason':None if receipts else '产品 receipt 缺失；目录提示 rb.night_end_at_2300',
           'source_scope':receipts[0]['json'].get('source_scope') if receipts else None,
           'source_scope_reason':None if receipts else '未找到该产品的 source-scope receipt/manifest',
           'product_generation_code_version':receipts[0]['json'].get('code_version') if receipts else None,
           'product_generation_code_version_reason':None if receipts else '旧产品未附 code-version receipt；不得以当前 HEAD 填入',
           'same_version_as_current_checkout':None,
           'same_version_as_current_checkout_reason':'未把 producer receipt、产品生成代码、二进制和现 checkout 绑定；旧产品 schema 与当前 writer 有差异',
           'physical_data_stats':ps,
           'physical_data_stats_reason':None if ps else '只做 metadata；未对这个 leaf 载入数据列',
           'data_decoded':bool(ps and '2020-12-01' in leaf),
           'data_decoded_reason':'短窗三路 scalar/部分完整数值列已解码；全年只读头及首尾，其他 leaf 仅 metadata',
           'native_reader_runtime_verified':False,
           'native_reader_runtime_verified_reason':'现存 dbaw 缺 P1 Wall 类型；未导入项目，未调用 .F/.run/to_df',
           'sensitivity':'市场业务材料；原始大数据只引用，不复制。样本仅 3 条局部链及必要参照，无凭据。',
           'professional_suitability':None,
           'professional_suitability_reason':'交 E1 专业判断；Worker 不决定用途接受、预期冻结或业务合理性'}
        item['leaves'].append(d)
    assets.append(item)
inventory={'schema':'w001-asset-inventory/local-v1','run_id':RUN,'work_order_id':'W001','observed_at_utc':now,
 'scope':'由当前代码/配置指向的三个 fao/prod 根目录；只精确测试 WallAssembler/EawP1WallLifecycleFrp/WallOccurrenceFao/EawBattleP 类名，再进入已存在的 Wall/Wall 产品根。',
 'search_roots_file':str(W/'evidence/STORE_ROOTS.json'),'class_probes_file':str(W/'evidence/CLASS_CANDIDATES.json'),
 'limits':meta['limits'],'observed_directories':meta['directories_visited'],'observed_files':meta['files_observed'],
 'total_observed_bytes':sum(a['total_file_bytes'] for a in meta['assets']),
 'metadata_scan_stops':meta['stops'],'metadata_scan_elapsed_seconds':meta['elapsed_seconds'],
 'small_file_hash_bytes':meta['small_bytes_hashed'],'source_code_readable':True,'generated_wrapper':wrapper,
 'distinctions':{'source_readable':True,'generic_generated_wrapper_present':True,'matching_P1_Wall_wrapper_present_in_inspected_file':False,
 'receipt_and_fields_exist_for_upstream':True,'three_writer_legacy_materialization_exists':True,
 'legacy_short_window_partially_decoded':True,'current_canonical_writer_materialization_verified':False,
 'current_complete_run_tuple':None,'current_complete_run_tuple_reason':'缺当前产品回执、生成版本与匹配 reader/binary 绑定',
 'suitability_accepted':None,'suitability_accepted_reason':'Worker 无专业接受权限'},
 'assets':assets,'physical_stats_file':str(W/'evidence/PHYSICAL_DATA_STATS.json'),
 'sample_chain_file':str(W/'SAMPLE_CHAIN.jsonl'),
 'historical_or_downstream_candidates':[
  {'path':c['path'],'feature':c['feature'],'exists':True,'reuse_status':'CANDIDATE_ONLY','wall_lifecycle_material':False,'reason':'EawBattleP 为下游候选；只查目录存在，不替代三路 Wall 材料；未解码其数据'}
  for c in json.loads((W/'evidence/CLASS_CANDIDATES.json').read_text()) if c['exists'] and c['feature']=='EawBattleP'],
 'cost_stop':{'command':'340-headers-only','status':'STOPPED_FOR_COST','timeout_seconds':35,
 'reason':'796 文件头探测超时；无可靠逐项完成记录，未声称全部完成。后改为 95 个明确产品/短窗 sparse 文件头，0.221 秒、全部结构有效。'},
 'large_unperformed_searches':['未递归整个 BASE、HOME、磁盘或所有 fao hash 分支','未扩搜无关 uplot 父仓库','未搜索其它机器、远程数据目录或数据库'],
 'notes':['receipt 的 success 是文件声明；不等于 Worker 重新验证本次执行成功。','mtime 为现场文件系统事实，不作为生成时间或版本证明。','物理触发时间、目录范围、receipt source range 分开保存。']}
for p in (B/'cae/CAEGraph.ipynb',B/'cae/CAE-PoC.ipynb'):
    s=p.stat();inventory['historical_or_downstream_candidates'].append({'path':str(p),'exists':True,'bytes':s.st_size,'mtime_utc':datetime.datetime.fromtimestamp(s.st_mtime,datetime.timezone.utc).isoformat(),'sha256':None,'reason':'仅登记低成本目录候选，不读 Notebook 大内容求 hash','reuse_status':'UNKNOWN','wall_lifecycle_material':None,'wall_lifecycle_material_reason':'未作内容或 tuple 验证，不作为 Wall 成果'})
dump('ASSET_INVENTORY.json',inventory)

write('SAMPLE_CHAIN_README.md',f'''
# W001 真实局部链说明

本文件说明 `{W}/SAMPLE_CHAIN.jsonl`。它有 **3 条真实物理数据记录**，不是新测试 Run，也不是当前源码的通过证明。

- 产品原件：`{short['source_leaf']}`。
- 同身份上游：`{up}`；receipt schema `wall_lifecycle-v1.6.1`，receipt code version 原样保存在每条 sample 的 `version` 中。
- 对象/日历：上游 receipt 为 `rb / night_end_at_2300`。Wall 局部号为 1；当前 canonical `FeatureRunIdentity` 没有从旧产品中取得，显式 null 并给 reason。
- 旧产品物理类型：`MulWrap P1WallOccurrenceStorage`、`MulWrap P1WallCurrentStorage`、`MulWrap P1DiagnosticStorage`。产品自身生成 code version 没有回执，不用当前 HEAD 补齐。

| 原物理行 | writer 触发 epoch 的 ISO Z 数值表示 | stored change | stored current | stored UTI |
|---:|---|---|---|---:|
| 0 | {sample[0]['writer_trigger_epoch_iso_z']} | started | present | 72335299 |
| 1 | {sample[1]['writer_trigger_epoch_iso_z']} | band_updated | present | 72335302 |
| 2 | {sample[2]['writer_trigger_epoch_iso_z']} | ended | ended | 72335308 |

第一条 band/core 为 4270；第二条 band low 为 4269、core 约 4269.8527778236985，属于确有数据变化的 BandUpdate。第三条的零数值和 `not_present` 原样保留；不把零自动当作缺失。该链未出现 Dormant/恢复；未寻找或合成全场景链。

抽取使用 `bounded_dba_reader.py`（仅 Python 标准库、所有数据 open 为 rb）。DBA header 按 `pydim/dim/rt.py:69` 的 24-byte `<iiiiq` 验证 offset、item size、有效长度与容量；Text 使用 `pydim/dim/dbas.py:14` 的 anchor/payload UTF-8 规则。按 list anchor 把 value row 对到 firing row；每条保留 occurrence ref 和 payload、同 firing 的 current update、全部 diagnostics 时间列上的同 firing 计数、同 Wall/UTI 的 sparse 与 packed row。upstream trace 通过有界二分 seek 后再核 exact UTI；只声明找到的真实点，不由未命中推断不存在。

抽取读取 {json.loads((W/'evidence/SAMPLE_CHAIN_EXTRACTION.json').read_text())['read_budget']['bytes_read']} bytes；有 4 MiB、18 秒、90 文件上限。被读文件的 size/mtime 在探针前后均一致。trace 是 WallAssembler 上游状态，**不是 FRP DSU 完整 active map**；后者明确缺失。没有从 current update 缺行补状态。

三条链的同 firing diagnostics 均为 0；这是精确时间对齐范围内未观察到诊断，不表示整份 diagnostics 为空。短窗整体另有 328 个 diagnostic firing，前三条实测为 ingress / InvalidNumericDomain / wall_band，要求 `band_lo <= core_price <= band_hi`。这些样本不证明错误分支正确。

初次严格 JSON 写出遇到原始 IEEE NaN 而失败，留下的空文件保存在 `evidence/460-SAMPLE_CHAIN.empty.failed`。修正只做 JSON 表示：原始 NaN 写为 null，每项在 `nonfinite_stored_values` 保留 JSON 路径、`nan` 原值表示及原因，未插补数值。重读后生成本文件所述样本。失败和修正命令均在日志内。

时间说明：ISO Z 由文件中 epoch ns 做数值转换；未核交易所当地时区解释。`p1WallLifecycleOccurredAt` 的 Int 在这 3 条记录与上游 UTI 精确一致，不称其为 epoch actual time。独立 actual/confirm/known 字段未取得，均为 null 加 reason。

这只是可复核的历史物化局部样本。E1 决定能否复用、还需哪些材料；Worker 不判断业务合理性、冻结资格或正式接受。
''')

write('CODE_AND_READER_ENTRYPOINTS.md',f'''
# W001 当前源码、包装和读取入口

所有路径以 `{B}` 为前缀；下表 repo 的完整 HEAD、branch、dirty、remote、worktree 原件见 `WORKSPACE_BINDING.json`。本报告中的静态事实只适用于已读取的 working tree 文本，不把它们提升为物化生成版本。

| repo | 路径 | HEAD | branch | 初始未提交状态 |
|---|---|---|---|---|
{repos_table}

## 1. 实际注册、配置及层间 Cal 组合

1. TIS `{B}/mquant/tis/frp/EawBattleP.py:34` 定义 `_OnlyReadTypedIngress`，37–38 返回 `CalType.OnlyRead`；54–55 的 `WallOccurrenceFao` 默认 source 为 `WallAssembler()`。41–51 的 `_CalculatedP1Product` 返回 `CalType.Cache`，其 `to_df()` 主动抛 TypeError。93–97 的 `EawP1WallLifecycleFrp` 仅有 `wallLifecycleInput`，`doFrpUpSource()` 显式返回 assembler。不能通过改用下游 EawBattleP 绕过本 W 的 Wall 材料要求。
2. FRP `{B}/edh-universe/frp/frp/src/Frp/Instance.hs:67` 注册 Wall 产品。`src/Frp/Instance/ISL/Eaw/P1.hs:71` 是 newtype 包装，97–99 FaoMeta 为 `CalendarTarType SymbolType / Cal`；121–129 为 ingress → lifecycle → diagnostics 合并；177–180 绑定 `dumpWallOutputs / doWallLifecycleFrp`。
3. FRP `P1/FaoIngress.hs:240` 的 source 是 PyAny；285–287 为 Calendar Symbol / OnlyRead；313–317 读取 kind `wall_lifecycle`，dump 会报 read-only。166–185 强制 source 同目录 `p1_receipts/wall_lifecycle.json`，并核 receipt artifact_location 与实际 fullDir。
4. `frp-core/src/Frp/Core/Fao/Class.hs:614`：按实例 propCalType 分派；632–640 的 OnlyRead 只 load，缺材料报错；642 的 Cal 走 doImpl；643–660 的 Cache 依全局 Cal/Gen 决定 load 或 doImplAndDump。这是不同层的静态声明。缺当前真实任务参数、二进制及生成回执，不能凭 Python Cache 和 Haskell Cal 两个值判断本机可安全生成或复用。
5. `mquant/frame/lang/frp/base.py:97` 的 `doFrpTaskParam(run_ups=True)` 默认可能执行上游；116–143 直接 `up.run()`。149–183 写 task linker 并 `epm exec ts --f=... --jp=...`；204–206 还会删除 task 文件。它是执行入口，不是本 W 可用的只读 probe。

## 2. 对象、日历、参数与范围的来源

- `mquant/tis/hf/prel0/wall_assembler.py:681` 是默认参数：`wall-default`、qt_freq=1d、qt_n=30、qt_quantile=0.997、w_depth_ref_ticks=1200、p_wall_ticks=1、t_wall_ticks=6；near/far/timeout 等若干默认 None，再由 `make_wall_params` 推导。该默认值不是现役执行参数。712–735 读取 `.P` 并加载 cc/qt；838–860 构造 receipt，actual/private 参数、source_scope、source fingerprint 和能力分别记录。
- `m3sof/settings/app.py:4` 当前文本 ENV=prod；`env/default.py:13,18,21` 为 `/m3varK`、fao、TB，42 为默认小时 21:00/20:00；`sof/default.py:13,21,28` 为默认 calendar=all、category=BaseData/futures、full_period=None。`sof/TA_updto20240229_DBA.py:9,12,22,33` 定义相应源名、m3varI 基础源及 calendar_dir。配置仓库有 dirty 改动；未导入设置，不声称这些层合并后的本次任务值。
- `{B}/config.yml:3` 显式给出 `/m3varK/BaseData/futures/TA_updto20240229_DBA/fao/prod` 作为候选存储根。这是候选目录来源，不证明本次特征采用该配置。
- 现场旧 receipt 给出 rb / night_end_at_2300、具体 source cut、业务参数和 code_version；详见库存。它们与当前 TIS HEAD 的关系尚未核成完整 tuple。
- 没有本 Run 的当前计算任务/物化生成回执。目标/日历/范围的现役生效值为 UNKNOWN；旧 receipt 与代码默认分开列。

## 3. 路径构造与 reader

`frp-core/src/Frp/Core/Fao/Class.hs:437` 对 ggjson 求 sha1；441–445 将参数 hash 的前 8 个字符逐层展开。447–454 从 store_dirs 覆盖或 Sof store_dir 取根；456–489 拼接 category/sof/store_name/env/[日期范围]/class/hash/target；503–519 取 Sof 起止范围及多存储根。目标 Calendar 表示和实际日期字符串以现场路径为准。不得自行从 class 名合成一个运行 tuple。

`mquant/frame/lang/frp/base.py:75` 返回 FrpDbaDao。`mquant/frame/lang/internal/dao/frp/dba.py:25` 定位 fields.json；46–53 优先 gfull_dir 再 full_dir；55–97 的 loadWith 读取字段并用 DbaStore + DbaUtil.read_field_ts 组装。ADT 类型经 `core/store.py:500` 的 eval2 求值，后者 `core/base/json.py:79,147` 导入 `m3sof.settings.json`。因此未证明导入副作用前不实际调用这个路径。`.to_dfs()` 在 mixin 第86行仍会访问 `.F`，不能当安全旁路。

generated wrapper **确实存在**：`{wrapper['path']}`，{wrapper['bytes']} bytes，sha256 `{wrapper['sha256']}`。AST 检查有 {wrapper['class_count']} 个类，未见任何 Wall/P1 类，旧三类 `MulWrap_P1WallOccurrenceStorage / MulWrap_P1WallCurrentStorage / MulWrap_P1DiagnosticStorage` 和当前三类也均缺。`mquant/worker/adt/__init__.py:63` 导入 dbaw；worker README 第47–60行说明生成入口。本 W 未重新生成 wrapper，未安装依赖，未调用任何生成器。未对其它环境中的动态注入作全局不存在断言。

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
''')

write('ACTION_PREFLIGHT_FACTS.md',f'''
# W001 ActionPreflight 现场事实（未运行）

## 触发原因与可先复用范围

有真实旧物化和有界可解码样本；**没有已核同版的当前 canonical 产品材料**。本文件为补齐当前绑定或必要后续运行准备事实。没有启动新 Run、样本重算、构建、依赖安装或测试。

最小已有材料读法已经执行：在 `{short['source_leaf']}` 取 value rows 0–2，按 anchor 对 firing，关联 `{up}` 的 localNo=1 / UTI 72335299、72335302、72335308。它区分旧物化“仅存在”与“部分可解码并能对账”；不能区分当前二进制行为或证明业务适合性。

## 已存在的执行入口与精确模板

源码入口为 `{B}/mquant/tis/test/integration/verify_eaw_p1_real_run.py:773–817`。CLI 原文要求 `--fixture`，执行选项为 `--execute-normal --evidence-dir --frp-stack-executable --frp-stack-yaml --frp-project-root --frp-source-worktree`。示例 fixture `{B}/mquant/tis/test/integration/fixtures/eaw_p1_real_run.example.json` 含 REPLACE 占位符，不是真实窗口凭据。

以下只是现有入口的准确命令形状；尖括号仍为未绑定值，**本 W 未执行，也不是获准命令**：

```bash
PYTHONDONTWRITEBYTECODE=1 \\
TMPDIR='{W}/tmp' \\
XDG_CACHE_HOME='{W}/cache' \\
MPLCONFIGDIR='{W}/cache/matplotlib' \\
<已核环境的Python绝对路径> -B \\
  '{B}/mquant/tis/test/integration/verify_eaw_p1_real_run.py' \\
  --fixture '<E1批准且已冻结的fixture绝对路径>' \\
  --execute-normal \\
  --evidence-dir '<获准且不存在或为空的独立证据目录>' \\
  --frp-stack-executable '<已核Stack绝对路径>' \\
  --frp-stack-yaml '<已核隔离overlay绝对路径>' \\
  --frp-project-root '<已核FRP工程根>' \\
  --frp-source-worktree '{B}/edh-universe/frp/frp'
```

这个 runner 的 AUTH_ENV 原文是 `EAW_P1_HEAVY_RUN_AUTHORIZED`；161–165 要求 Owner 明确授权后值为 YES。本 W 没有设置它。`--evidence-dir` 只限定回执位置，**不保证计算产物、Stack 缓存或项目日志在 W 写面内**。

该入口当前会先 Stack build `trade-poc:exe:ts`（427–460、809），按 EXECUTION_ORDER 生成 Wall、两组大单、Build、Attack、Absorb，再调四个 FRP 产品（28–46、680–703）。它不是 wall-only 有界探针。当前授权禁止构建/计算、禁止其它写面，故不能直接采用。未自行修改 runner 以缩窄流程。

native FRP worker 调用合同位于562–590行：`<ts绝对路径> --f=<worker one.edh绝对路径> --jp=<task绝对路径>`，cwd 为已核 project_root。Wall 单任务的 schema 来源为237–256、299–325行的 CalendarTarget/params/cal_type=Gen，但现存 runner 会构造四产品，未提供已经冻结的 wall-only task。是否另行签发最小动作由 E1/manager 决定，本 W 不生成假执行回执。

## 窗口、对象、成本的证据与未知

| 项目 | 已核事实 | 未核/停止条件 |
|---|---|---|
| 对象/日历候选 | 已有 receipt 是 rb / night_end_at_2300 | 不是本次新计算的选定值 |
| 局部窗口线索 | 旧样本 writer 触发数值时间为 2021-01-14 09:04:10–09:04:14.5，含非平凡更新和 End | 按日期截取会改变 source run/起始状态；不能保证短算重现同 Wall |
| 预热来源 | WallAssembler 默认 qt_n=30、qt_freq=1d、w_depth_ref_ticks=1200；`_impl` 先加载 cc/qt | 最小真实日历窗及预热需求未知；缩小 startDay 不保证缩小所有上游加载 |
| 已有短窗 | 46 文件、8,024,734 bytes；occurrence 15,809、current 15,208、diagnostic 328 记录 | 目录2020-12-01–2021-02-22，与触发数据真正范围分开 |
| 全年旧产品 | 43 文件、131,322,404 bytes；occurrence 266,469、current 254,424、diagnostic 7,469 记录 | 全年仅头与首尾；不全量解码 |
| 上游规模 | 本次仅 metadata 清点的各 class 合计 {inventory['total_observed_bytes']} bytes；部分 dense trace 为 GB 级 | 不加载这些整份大数据，不据旧报告推算当前峰值 |
| 只读实测成本 | 3条 probe 3,075 bytes；统计读取994,952 bytes；完整局部链抽取1,255,773 bytes，均低于显式上限 | 这是读取成本，不是重算内存/耗时预测；未测计算峰值 |
| 环境 | 当前源码/依赖 HEAD、dirty 已列；存在 ts/dbaw 路径候选，未运行 | Python ABI/依赖、二进制生成版本、Stack overlay、数据库权限尚未实际验证 |

不提供无证据的预计新行数、内存或秒数。这些均 UNKNOWN。已有源代码算法或旧 receipt 不能替代当前成本实测。

## 后继动作的前置条件与停止点

先由 E1 消费旧材料、判断是否足以回答局部问题；若要求当前 schema，需核准唯一对象/日历/预热范围、Wall 参数、生成版本、二进制和只写隔离区的存储/缓存/日志覆盖，并对依赖导入完成副作用检查。现有 root `run-python.sh:6–7` 会在 W 外写 migration 日志，不能直接复用。本 W 未 source m3rc，未调用该脚本。

可观察回执依源码为：源产品 thin receipt、三路 fields.json/data/trigger axes、明确生成版本和命令 exit code，必要 FRP active-map trace。到任一上游大加载、未知写入、同目录覆盖、自动构建、当前 schema 不匹配或成本超限，先停在 metadata/任务预览层。当前没有已批准的 wall-only 可运行材料动作；本 W 已在此停止计算路径。G-RUN/窗口采用及业务接受由 E1/manager 后继决定。
''')

checks=[
 ('A1','EXECUTED','真实 cwd/thread/model/effort、UTC、主机/用户、可用磁盘已核','evidence/PHYSICAL_BINDING.json'),
 ('A2','EXECUTED','PID227535/startticks44274656/inode14781898；竞争 EX flock EAGAIN；未替换/释放主控锁','evidence/PHYSICAL_BINDING.json'),
 ('A3','EXECUTED','真实 TIS/FRP/reader 依赖仓库 HEAD/branch/status/worktree/remote 与文件 hash 已记录','WORKSPACE_BINDING.json'),
 ('A4','EXECUTED','TIS 与 FRP 旧 SHA 在本地可比较，HEAD 匹配，相关路径 diff stat 为空；其他 dirty 不修改','WORKSPACE_BINDING.json'),
 ('A5','PARTIAL','BASE/tis 向上归到无关 uplot，发生一次意外父仓库 status 元数据枚举；已隔离记录且未扩搜','WORKSPACE_BINDING.json'),
 ('B1','EXECUTED','当前注册、FaoMeta、Cal/Cache/OnlyRead、源码参数和默认配置入口已定位','CODE_AND_READER_ENTRYPOINTS.md'),
 ('B2','UNKNOWN','当前真实执行的对象/日历/生效参数/范围/binary tuple 缺生成回执；不以静态默认补值','WORKSPACE_BINDING.json'),
 ('B3','EXECUTED','generic generated wrapper 存在；静态 AST 明确缺三组 P1 Wall 所需类型','evidence/GENERATED_WRAPPER_BINDING.json'),
 ('B4','PARTIAL','原生 FrpDbaDao/read接口已定位，未进行可能有副作用的项目导入；物理只读探针另行已实测','CODE_AND_READER_ENTRYPOINTS.md'),
 ('B5','EXECUTED','三路 writer 当前名称/typed schema/路径规则和上游 receipt/sparse/trace 保存入口已列','CODE_AND_READER_ENTRYPOINTS.md'),
 ('C1','EXECUTED','三个代码/配置指向的 prod 根，588 精确类路径检查；155 目录796 文件 metadata，未全盘递归','ASSET_INVENTORY.json'),
 ('C2','EXECUTED','已有三路旧物化、上游 receipt/fields/sparse/state trace 的存在性分开登记','ASSET_INVENTORY.json'),
 ('C3','NOT_FOUND','已核产品 leaf 未见产品自身生成版本 receipt/manifest；当前 canonical schema 的物化未核得','ASSET_INVENTORY.json'),
 ('C4','NOT_FOUND','未取得 FRP DSU 完整 active-map 物化；上游 trace 不替代它','SAMPLE_CHAIN.jsonl'),
 ('C5','PARTIAL','下游 EawBattleP 和 Notebook 仅候选登记，未作当前同版或 Wall 适合性确认','ASSET_INVENTORY.json'),
 ('D1','STOPPED_FOR_COST','全796文件 header 探测35秒超时；无完成清单，不声称成功；随后仅95明确文件头完成','evidence/340-headers-only.command.json'),
 ('D2','EXECUTED','95 文件头全部有效；两份产品数量和短窗数值/时间列已核；全年只读首尾','evidence/PHYSICAL_DATA_STATS.json'),
 ('D3','EXECUTED','3条真实 Start→非平凡BandUpdate→End，同 Wall/UTI 对应 sparse/packed/current/上游trace','SAMPLE_CHAIN.jsonl'),
 ('D4','PARTIAL','样本没有 Dormant/恢复；未覆盖全部生命周期/异常场景；不合成','SAMPLE_CHAIN_README.md'),
 ('D5','EXECUTED','短窗diagnostics非空328 firing；前三条 InvalidNumericDomain，样本同firing无诊断','evidence/SHORT_WINDOW_PHYSICAL_PROBE.json'),
 ('D6','PARTIAL','保留 epoch trigger 与 raw UTI；独立 actual/confirm/known 字段和生成 code binding 未取得','SAMPLE_CHAIN_README.md'),
 ('E1','EXECUTED','只静态列真实CLI、模板、窗口候选、重算/构建风险、成本未知、前置条件和停止点','ACTION_PREFLIGHT_FACTS.md'),
 ('E2','NOT_APPLICABLE','没有实际运行计算、测试Run、构建、安装、git变更或GitHub写入','COMMAND_LOG.txt'),
 ('F1','PARTIAL','本地原件交付；真实发布commit/ref缺失，正式 WORKER_RETURN.json 等主控回准确refs再同单生成','WORKER_RETURN_PREPARATION.json'),
 ('F2','NOT_APPLICABLE','业务预期、合理性、冻结、专业接受与父任务完成不属本Worker权限','WORKER_EXECUTION_REPORT.md')]
check_rows='\n'.join('| '+a+' | '+b+' | '+c+' | `'+str(W/d)+'` |' for a,b,c,d in checks)
missing=[
 'CURRENT_TUPLE_UNBOUND：未取得当前任务/二进制/生效参数/对象/日历/范围与当前代码和数据的完整绑定。',
 'LEGACY_SCHEMA_ONLY：已解码为真实旧 P1Wall*Storage 物化；与当前 typed writer 不能认定同版，产品自身生成版本回执缺失。',
 'MATCHING_NATIVE_WRAPPER_MISSING：现存 generated dbaw 缺旧三组及当前三组 P1 Wall 类型；未验证原生 reader 运行态。',
 'FRP_ACTIVE_MAP_NOT_MATERIALIZED：没有 FRP 完整 active-map trace；上游 WallAssembler trace 与之区分。',
 'LIMITED_SCENARIOS_AND_TIMES：3条链没有 Dormant/恢复；未覆盖全部异常分支；独立 actual/confirm/known 未取得。',
 'COST_LIMIT：796文件 header 尝试35秒超时；全年与GB级上游未全量加载，范围外未知。',
 'PUBLICATION_PENDING：未写GitHub；缺真实发布commit及每文件准确ref；正式Return尚待同W补签，仅回E1。']
dump('WORKER_RETURN_PREPARATION.json',{'state':'LOCAL_ARTIFACTS_READY_AWAITING_REAL_PUBLICATION_REFS','is_formal_worker_return':False,
 'schema_for_final_return':'longrun-worker-return/v2','run_id':RUN,'work_order_id':'W001','order_ref':ORDER_REF,
 'worker':'codex:'+RUN+':worker:W1','return_to':E1,'outcome':'PARTIAL',
 'result_ref':None,'result_ref_reason':'实际 GitHub commit 尚不存在；主控先逐字发布报告后回准确 commit/ref/sha256',
 'missing':missing,'manifest_source':str(W/'PUBLICATION_MANIFEST.json'),
 'required_final_fields':['schema','run_id','work_order_id','order_ref','worker','return_to','outcome','result_ref','missing','manifest'],
 'final_manifest_contract':'每项仅 ref 和 sha256；ref 必须真实 pinned commit，不使用 branch/placeholder 冒充；内容 sha256 须与本地原件核对',
 'publication_repository':'daowei2026/observe-iterate','publication_branch':'runs/'+RUN,'publication_prefix':DEST,
 'formal_WORKER_RETURN_json_exists':False,'formal_WORKER_RETURN_json_reason':'用户明确分两阶段：待主控真实证据 refs 回传后由原W1生成，当前不可伪造'} )

write('WORKER_EXECUTION_REPORT.md',f'''
# W001 本地执行报告

本地 outcome：**PARTIAL**。已实际完成有界现场核验并交付原件；当前同版运行 tuple 与正式出版/Return 仍有缺口。没有启动计算或新测试 Run，没有 GitHub 写入，没有作业务接受/完成决定。本地 Goal 完成只表示本地交付，不表示 W001、D001 或父任务完成。

## 身份、授权与交付

- Run：{RUN}；D001/W001；Worker：codex:{RUN}:worker:W1。
- 原 ORDER：`{ORDER_REF}`；签单 Return：`daowei2026/observe-iterate@b94b367692c252ed2ef41441ff6244d6d71e4b0c:longrun/runs/{RUN}/calls/C0003/PRO_RETURN.json`。
- return_to 只能是 **{E1}**。
- 唯一业务写面：`{W}/`；实际 cwd：`{B}`；实际 thread：{binding['thread_id']}；session metadata 核实 gpt-6.1-sol / max，非逻辑名替代。
- 首次绑定可用磁盘 {binding['disk_available_bytes']} bytes；UTC/主机/非敏感用户标识在绑定 JSON。
- 主控持有锁：PID227535 / startticks44274656 / inode14781898。开原 inode 的竞争 `LOCK_EX|LOCK_NB` 返回 EAGAIN；没有创建、截断、写锁文件，没有替换/释放/重取主控锁。只读描述符最初返回 EBADF，改为无写入的 O_RDWR 描述符完成竞争核验。每次 runner 前再次核验 holder 与保护。
- 本地输入原件在 `inputs/`；命令、stdout/stderr、每次 source 和失败记录在 `commands/`、`evidence/`、`COMMAND_LOG.txt`。执行器预览没有代替原件。

## 最重要的现场事实

真实 TIS 是 `{B}/mquant/tis`，HEAD `ef887396e0a06d6e75be47efee0f1985ad7988a3`；真实 FRP 是 `{B}/edh-universe/frp/frp`，HEAD `cac6c912dd65a14acbd591ca57e0afd8ddb4ef13`。两者与 ORDER 的旧源码阅读 SHA 相同，但分别有 STCalendar.py、BussinessUtils.hs 的既有 dirty 修改；m3sof、worker 等也有既有修改，未处理它们。完整路径/branch/worktree/remote/status/相关文件 sha256 和 blob 在绑定 JSON。D001 与 FEATURE_CONTEXT 本地镜像均已与其准确 Git object 核字节一致，无 fetch。

已找到真实 WallAssembler receipt、fields、sparse、state trace 和两个三路产品 leaf。三个候选 prod 根只做一层低成本清单，再对588个明确类路径作存在性检查；只进入已存在的 Wall/Wall产品，155目录、796文件的 metadata 清点共 {inventory['total_observed_bytes']} bytes，未载入这些数据。没有把目录名、mtime 或 success receipt 当本次运行证明。

旧产品与当前代码的关键差异：物化 fields 用 P1Wall*Storage；当前 writer 用 WallOccurrenceBatch/WallCurrentBatch/WallDiagnostic。产品生成版本回执缺失。现存 generated wrapper 有118类但没有 Wall/P1 类。因此“源码可读”“包装存在”“物化存在”“有界可解码”“当前同版”“用途适合”分别报告，不能逐级自动推导。

| 物化范围 | occurrence firing / records | current firing / records | diagnostic firing / records | 本W读取范围 |
|---|---:|---:|---:|---|
| 目录2020-12-01–2021-02-22 | 14,858 / 15,809 | 14,858 / 15,208 | 328 / 328 | header、短窗部分完整数值/时间列、真实3条链 |
| 目录2021-01-01–2021-12-31 | 241,659 / 266,469 | 241,659 / 254,424 | 7,456 / 7,469 | header和首尾，不声称全局min/max |

短窗物理 firing 时间列的全列范围是2021-01-14T09:04:10至2021-02-22T14:44:30（epoch数值转换为ISO Z，未核交易所时区解释），与目录范围及上游 receipt range 分开。短窗两路 localNo 均 min1/max5013/distinct5009，数值列 null/NaN/zero 等原始统计见 PHYSICAL_DATA_STATS；未把零值当缺失。独立 actual/confirm/known 时间字段未取得。

真实局部链为 localNo=1 的 Start→band_updated→End，writer trigger 相隔1.5秒和3秒；每条都对上 source artifact / UTI、sparse、packed row、current update 和上游 trace。未取得 FRP active map，不从 current 缺行补状态。短窗 diagnostics **非空**；前三条实读是 ingress InvalidNumericDomain / wall_band。样本同 firing 未见诊断仅限这个范围，不证明错误路径正确。

## 工单逐项状态与证据

| 项 | 状态 | 实际事实或限制 | 原件证据 |
|---|---|---|---|
{check_rows}

## 运行边界和失败原件

- 未执行任何 fetch/pull/checkout/reset/clean/rebase/merge、安装、构建、生产写入、数据库查询、全年/全品种重算或缓存清理。没有向其它聊天发消息或派生 Worker。
- 所有业务产物只在 W001；Python -B / PYTHONDONTWRITEBYTECODE=1，runner 的 TMPDIR、XDG_CACHE_HOME、PYTHONPYCACHEPREFIX、MPLCONFIGDIR 均指向 W001。没有 source m3rc，没有执行会在 W 外写 migration 日志的 run-python.sh，没有导入项目或触发 `.run/.F/to_df`。
- 796文件头尝试在35秒超时（exit124）；没有完整逐项回执，保留失败 stdout/stderr/命令，不补称已核。后续缩到95个明确文件头，结构全部有效，未重做大范围加载。
- 460样本JSON首次写出因真实NaN失败（exit1），空原件留存；470只修正JSON表示后重读。字段null均保留非有限值原因，无伪样本。
- 若干最初假设路径的 rg 返回exit2，真实错误全文保留；随后沿已定位路径查证。rg无匹配exit1按无匹配解释，不当运行成功证据。
- BASE/tis 的 Git 探测曾意外向上进入 `/dwdhome/fy` 的 uplot 父仓库并列未跟踪名称。没有读取那些文件内容、没有后续扩搜；此偏差明确登记。真实 TIS 另行准确核定。没有进行预计大搜索；进一步全盘、其它环境或更多数据库调查均未开展。

## 证据性质与专业未决

静态源码事实说明当前文本规定；现场绑定事实说明这台主机的 checkout、dirty、配置文本与文件存在；物化事实说明旧文件当前存在和具体 schema；可解码事实仅覆盖明确列和样本。没有当前同版生成回执/二进制绑定，不能将旧样本用作当前实现验收。当前 WallIdentity 结构本身仅含localNo，其与 run context 的业务含义交 E1，不用旧需求措辞替代源码事实。

E1 仍需判断旧材料可复用范围、当前身份/事务/End发布的业务适合性、完整 active map 或异常场景是否必要、是否签最小后继动作、是否具备冻结或专业接受资格。Worker 对这些项没有决定权。

## 主控逐字出版与原W1续签

请主控按 `PUBLICATION_MANIFEST.json` 的本地绝对路径与 sha256，逐字运输到 `daowei2026/observe-iterate` 获准分支 `runs/{RUN}` 下 `{DEST}`，保留相对目录。原始大数据仅引用不上传；本包没有复制原始大型市场文件。`HASHES.sha256` 覆盖自产原件，标准排除 hash索引自身；其自身摘要在本地封包命令及最终回报给出。

本地准备 `WORKER_RETURN_PREPARATION.json` 载明 outcome=PARTIAL、missing、准确 E1 及待填 result_ref，不是 V2 正式 Return。实际 commit 尚不存在，当前没有伪造精确ref。主控先出版证据，再回同W1：真实40位commit、各文件完整ref及sha256；W1核对后同单生成 `WORKER_RETURN.json`，按 V2 仅回原 E1，再由主控运输。不能改送manager，不能把本地Goal完成当作W或父任务完成。当前回合交件后自然结束，不轮询等ref。

采用的状态技能：[long-task-status](/home/dw/.agents/skills/long-task-status/SKILL.md)，只在W001内建 general/local ledger；没有对外发消息、通知或注册服务。本地阶段状态不代表专业接受。
''')

print(json.dumps({'written':['ASSET_INVENTORY.json','SAMPLE_CHAIN_README.md','CODE_AND_READER_ENTRYPOINTS.md','ACTION_PREFLIGHT_FACTS.md','WORKER_RETURN_PREPARATION.json','WORKER_EXECUTION_REPORT.md'],'outcome':'PARTIAL','sample_records':len(sample),'inventory_files':meta['files_observed'],'total_observed_asset_bytes':inventory['total_observed_bytes']},ensure_ascii=False))
