"""从本W真实证据整理事实；不访问行情payload。"""
import datetime
import json
from pathlib import Path
from support import BASE,OUT,lease,write_json,now

lease()
def load(name):return json.loads((OUT/name).read_text())
b=load('BINDING.json');r=load('READBACK.json');s=load('SOURCES_INITIAL.json');m=load('METADATA_ENRICHMENT.json');q=load('RECONCILIATION.json')
unknowns=[
 {'id':'U01','item':'所定位ts binary的构建commit、与当前FRP checkout的对应','value':None,'reason':'有路径/hash/ELF BuildID；既有593字节stack安装日志未提供该binary到commit的可核绑定。未执行或重建binary。'},
 {'id':'U02','item':'顶层既有三路产物的生成binary/commit/run','value':None,'reason':'顶层目录只有三路存储及fields；未见独立provenance/receipt。source receipt不是顶层生成版本证明。'},
 {'id':'U03','item':'dirty generated Python ADT的生成提交及命令','value':None,'reason':'实际schema可导入、可完整decode本次样例，文件已有dirty；仅保存本对象选段和diff，不重生成。'},
 {'id':'U04','item':'全窗diagnostic的ingress/state分类分布及所有错误内容','value':None,'reason':'仅按约定解码外层index 0/164/327；328来自pointer/anchor。三例全为ingress不证明全窗没有state error。'},
 {'id':'U05','item':'完整时区/交易日映射、窗口种子、未闭合life覆盖','value':None,'reason':'仅取已有receipt、header及三组UTI/时间/chunk对应；未重建日历或全窗生命周期。datetime64[ns]本身不带时区。'},
 {'id':'U06','item':'整个上游市场数据及所有依赖的生成版本','value':None,'reason':'source receipt两份producer文件hash匹配当前文件，但未覆盖tick_quote_context等全部依赖；未恢复全资产盘点。'},
]
facts=dict(schema='w001-local-facts/v1',run_id='OI-EAW-WALL-20261116-01',work_order_id='W001',
 dispatch_id='33b5c20252764bd799a599a9b6859bb4',object='EawP1WallLifecycleFrp',
 worker='codex:OI-EAW-WALL-20261116-01:worker:W1',return_to='chatgpt:OI-EAW-WALL-20261116-01:executor:E1',
 order_ref='daowei2026/observe-iterate@1f5e1eb977c66368cb9a065afe596b5c3f4e5a62:longrun/runs/OI-EAW-WALL-20261116-01/work_orders/W001/ORDER.json',
 workspace=dict(cwd=str(BASE),realpath=str(BASE.resolve()),output_dir=str(OUT)),
 configured_model_effort=dict(value='gpt-6.1-sol/max',evidence='ENVFIX1主控明示；本席未另查运行器私有配置'),
 actual_context=dict(requested=b['context'],successful_api=b['context_api'],
     sof_api_arguments=dict(sof_name=b['context']['sof_name'],startDay=b['context']['startDay'],endDay=b['context']['endDay'],stk_tlist='black',opt_blks=[],full_period=None),
     binding_succeeded=b['binding_succeeded'],expression=b['expression']),
 related_sources=dict(repositories=s['repositories'],files=s['files'],additional=m['additional_sources']),
 loaded_modules=b['loaded_modules'],binary_facts=dict(
     file=next(x for x in s['files'] if x.get('role')=='binary_candidate'),
     resolution_evidence='logs/binary-runtime-resolve.log + logs/schema-binary-entry.log + frame/lang/frp/base.py:150',
     build_id='ec75e5e1bd08043268391fa3fc072230c65d70ed',executed=False,build_commit=None),
 schema_facts=dict(files=r['schema_files'],per_stream={k:dict(root=v['schema'],nested=v['nested_schema']) for k,v in r['streams'].items()},
     current_dirty_file='mquant/worker/adt/dbaw.py',excerpts='SCHEMA_EXCERPTS.md',dirty_diff='diffs/worker-dbaw.Wall.local.diff',generation_commit=None),
 feature_source_binding=b['bindings'],artifact_checks={role:{place:{k:v for k,v in d.items() if k!='direct_entries'} for place,d in info.items()} for role,info in b['artifact_checks'].items()},
 receipt_checks=dict(location_matches=m['receipt_location_matches_current_source'],parameter_comparisons=m['parameter_comparisons'],
     receipt_code_version=m['receipt_code_version'],current_two_file_source_digest=m['current_two_file_producer_source_digest'],source_digest_matches_receipt=m['source_digest_matches_receipt']),
 read_mode=r['read_mode'],read_mode_proof='READ_MODE.md',feature_computation_executed=False,
 read_attempts=[dict(id=x['id'],exit_code=x['exit_code'],log=x['stdout_stderr'],elapsed_seconds=x['elapsed_seconds']) for x in map(json.loads,(OUT/'COMMANDS.jsonl').read_text().splitlines()) if x['id'].startswith(('binding','readonly-readback'))],
 stream_checks={k:{x:v for x,v in t.items() if x!='samples'} for k,t in r['streams'].items()},
 sample_locations={k:dict(file='samples/'+k+'.json',outer_indices=[x['original_outer_index'] for x in v['samples']],complete=[x['complete_decoded_batch'] for x in v['samples']]) for k,v in r['streams'].items()},
 source_sample_location='samples/source_wall_matches.json',source_matches=r['source_matches'],
 source_metadata=m['source_headers'],unknowns=unknowns,side_effect_checks=dict(evidence='RECONCILIATION.json',all_related_unchanged=q['all_unchanged'],readonly_opens=q['read_only_open_count'],final_readback_denials=q['denied_final_readback_actions']),
 formal_acceptance=False,proposed_return_outcome='PARTIAL',created_files=[])

rows='\n'.join('| %s | %s | %s | %s | %s |'%(name,v['outer_event_count'],v['inner_item_count_from_anchors'],', '.join(str(x['original_outer_index']) for x in v['samples']),' ～ '.join(v['timestamp_range'])) for name,v in r['streams'].items())
repos='\n'.join('| %s | `%s` |'%(name,info['rev_parse'][-1]) for name,info in s['repositories'].items())
bound='\n'.join('| %s | `%s` | %s |'%(name,v['ppid'],v['cal_type']) for name,v in b['bindings'].items())
headers='\n'.join('| %s | %s | %s |'%(key,cols['uti']['valid_count'],' ～ '.join(str(x) for x in cols['uti']['first_last_raw'])) for key,cols in m['source_headers'].items())
report=f'''# W001｜现役绑定、三路物理输出与已有记录事实报告

run_id=OI-EAW-WALL-20261116-01；work_order_id=W001；dispatch_id=33b5c20252764bd799a599a9b6859bb4。
Worker：codex:OI-EAW-WALL-20261116-01:worker:W1；原消费者：chatgpt:OI-EAW-WALL-20261116-01:executor:E1。

本次完成有界现场事实调查，三路各取三处真实完整批次；具名限制仍在，按 PARTIAL 回交 E1 专业消费。没有执行特征计算，没有形成材料充分性、步骤通过或市场合理性判定。D001、步骤1和父任务不因此完成。

准确 order_ref：`{facts['order_ref']}`。

## G01：现役运行链、相关源码、binary 与 schema

**实际操作。** 本机 pwd/realpath 为 `{BASE}`；本地 ORDER.md 全文已读，SHA256=`4b014add73c8beffeaf78aeb34228278b31ffded9aa6cf525e4c166463f4c6ae`。inbox manifest 所列原样文件逐一hash匹配。沿现有 launcher、import 和 FRP subprocess 源码定位，没有全仓/全磁盘盘点。

**事实。** Python 为 `/m3c3/Linux/apps/anaconda3/bin/python`，相关 TIS/frame/quant/pydim 模块实际来自 BASE；详见 [BINDING.json](BINDING.json) 的 loaded_modules。相关仓 HEAD 如下；仅查本对象有关文件的 status，未据此声称整个仓库干净。

| 仓 | 当前 HEAD |
|---|---|
{repos}

现役与 E1 历史 TIS `ef887396...` / FRP `cac6c912...` 的直接比较已记录 actual/hash/historical hash 及 diff：

- WallAssembler 与 wall_assembler_core 两个文件逐字节相同于 TIS 历史基线。EawBattleP.py 整体不同，但此次 Wall 三类包装段未落入历史 diff；差异主要在其余产品段。tick_quote_context 有交易日分块来源变化，不能据两份assembler相同就宣称整个上游相同。
- FRP P1.hs 的 Wall `propCalType` 由 Cal 变为 Cache，并增加 source receipt 驱动的加载入口；WallLifecycle.hs 现役保留跨批ledger，Ended项仍插入 wallViews，current updates按本批changed identities取出；与 E1 基线的逐批ledger清空、End删除及独立update map存在直接差异。这些是源码事实，不是本次重新执行的状态测试。
- Products/FaoIngress/Publication 等实际hash和差异见 [SOURCES_INITIAL.json](SOURCES_INITIAL.json)、diffs/。现役 writer 使用 PublicStorage 的基础字段存储表示；本次 Python 取得的是这一物理 ADT，不是已经重建的 canonical WallIdentity/WallLifecycleEvent。

Python ADT 实际定义在 `/dwdhome/fy/BASE_E6_2/mquant/worker/adt/dbaw.py`，SHA256=`e9af247a05be7a62485a9bb5f870ae93fc5d35ffb55e025e1d3ad4d947825869`。该文件在调查前已 dirty；未改动。保存了12个相关定义选段和具名局部diff：[SCHEMA_EXCERPTS.md](SCHEMA_EXCERPTS.md)、[schema dirty diff](diffs/worker-dbaw.Wall.local.diff)。其仓HEAD为 `da0475a9c7fa769c2db8c803a5376ff2cdf09e0d`，不能把HEAD当成该dirty文件的生成版本。

FRP运行入口源码会在 M3WORKS/edh-universe 下调用 `epm exec ts`；epm现役脚本从最近workspace的edh-universe/bin注入PATH。解析到的文件为 `{BASE}/edh-universe/bin/ts`，89,618,768字节，SHA256=`8606cc020e5a0bbcbe953f3874f02f6e1cf3a3f8dc0ff3b0350404cefff5c159`，ELF BuildID=`ec75e5e1bd08043268391fa3fc072230c65d70ed`。本次没有执行该binary。安装日志存在，但未给出binary与当前FRP HEAD的可核对应。

**证据位置。** SOURCES_INITIAL.json、METADATA_ENRICHMENT.json、environment.json、BINDING.json、diffs/、logs/binary-runtime-resolve.log、logs/build-and-namespace-metadata.log。

**未核项/限制。** binary构建commit、dirty schema生成provenance、既有顶层输出生成commit/binary均unknown，不能用HEAD或mtime代替。

## G02：默认实例、source 与已存artifact资格

**实际操作。** 使用同值上下文 `TA_updto20240229_DBA / rb / night_end_at_2300 / 2020-12-01～2021-02-22`。原示例脚本的 OptContext 构造在现役Ndict/PPShare处失败，关键字形式也有相同异常，均保留原traceback。未修源码。随后按现有公开 `m3sof.load_sof` API构造同值Sof，保留OptContext源码中的black/[]/None默认上下文参数，成功实例化原特征及两级source；此适配未改变业务特征参数。

| 层 | 实际 ppid | cal type |
|---|---|---|
{bound}

全部actual ppdict、ggjson、class_file和三个full_dir均在 BINDING.json / FACTS.json。三个gfull_dir均为null。顶层full_dir：

```text
{b['bindings']['feature']['full_dir']}
```

source full_dir：

```text
{b['bindings']['source']['full_dir']}
```

顶层三路key全部存在，fdtype分别为 `adt@MulWrap_P1WallOccurrenceStorage`、`adt@MulWrap_P1WallCurrentStorage`、`adt@MulWrap_P1DiagnosticStorage`；不是缺key，也不是空流。顶层未见独立receipt；这不是凭source合同发明的顶层要求。WallOccurrenceFao的独立物化目录不存在，source实际指向WallAssembler现有目录。

source fields实际含 `wall__stream`、`wall__stream__occ0001`、`wall__stream__occ0002`、`wall_assembler_sparse_events`、`wall_assembler_state_trace`。明确receipt `p1_receipts/wall_lifecycle.json` 存在：product_kind=wall_lifecycle，schema_version=wall_lifecycle-v1.6.1，status=success，artifact_location精确等于当前source full_dir。receipt保存actual_business_parameters和producer_private_parameters；与当前raw defaults可直接比较的非null项一致。当前默认值为null的派生参数只抄录receipt，不调用make_wall_params补算。

receipt code_version为 `{m['receipt_code_version']}`。按其现役fingerprint规则，仅核对两份producer完整源码得到相同source digest；receipt中的git提交与当前TIS HEAD不同。该匹配不覆盖全部上游依赖，也不证明顶层产物由当前binary生成。

**证据位置。** BINDING.json、BINDING.attempt1～4.json、logs/binding*.log、METADATA_ENRICHMENT.json。曾读旧 `.runtime/parameter-inspection` 报告仅取得精确路径线索；随后以本次实际实例化和重新读取独立核实，没有采用旧success flag、计数或样例。

**未核项/失败限制。** 原OptContext入口在当前环境仍有具名ValueError；其余实际实例化成功不能写成原脚本原样可运行。source receipt的success是旧材料的存储内容，不是本Run新计算回执。

## G03：只读路径、三路schema层次和真实批次

**实际操作。** 先读现役DAO与DbArray分支，事前形成 [READ_MODE.md](READ_MODE.md)，随后直接复用FrpDbaDao的读取层：NormalField → generated ADT → DbaStore及DbaUtil.read_field_ts。均为shape=None、rb、mmap.ACCESS_READ；缺文件不会回补。未调用run/rerun/F，也没有使用EawBattleP替代。读取尝试46.6秒结束，未超时，三路的arm和时间轴数量检查分别通过；不是凭命令exit=0判断成功。

外层为时间轴 + root_seq的MulWrap；mul字段指向SeqOf_P1...Storage变长列表，再到基础字段业务行。每路仅decode下表三个外层批次，均完整、未截断；所有批次原始index、时间、anchor及完整decoded内容在 samples/。

| 流 | 外层事件/包数 | 内层存储行数 | 取样原始index | 外层时间轴首末 |
|---|---:|---:|---|---|
{rows}

总计数来自外层pointer和list anchor元数据，未全量decode业务payload。current物理行只有local no和state；不能把15208行当完整状态快照或15809个occurrence。本次三组index中，occurrence与current的UTI/local no/时间可对应；未宣称全窗join已验证。现役Haskell加载器可借source receipt及同UTI occurrence恢复canonical current，此处没有执行该加载器。

diagnostics的物理外层是MulWrap，内部是P1DiagnosticStorage行，字段包含source、kind、text1～3、double1、int1～3；对应canonical P1ProductDiagnostics中的ingress/state错误分流。328是外层包数，328也是anchor给出的物理错误行数，不能套成occurrence事件数。所选index 0/164/327各一行，均为 ingress / InvalidNumericDomain，text1=wall_band，text2=`band_lo <= core_price <= band_hi is required`。只对这些样例记录错误内容，未将三例外推为全窗错误分布。

按三个occurrence样例的已存UTI/local no，对source三条物理流做二分定位，匹配到wall__stream的行index 0/7598/15185、ordinal均0；保存全部原始列，包含真实NaN reason的显式编码，没有构造匹配行。对应UTI/local no为72335299/1、72696172/2455、73256339/5013。见 [source_wall_matches.json](samples/source_wall_matches.json)。两条occ分流在这三个位置没有匹配，不等于它们全窗为空。

**证据位置。** READBACK.json、samples/四份文件、SCHEMA_EXCERPTS.md、READ_MODE.md、logs/readonly-readback.log。

**未核项/限制。** 只验证接口、局部来源和真实形态；没有整窗join、完整生命周期覆盖或错误根因裁决。未取得顶层输出的历史生成provenance。

## G04：现成时基元信息

**实际操作。** 仅读receipt及source必要DBA的24字节header、首尾标量；2,206,800行trace没有整体加载或哈希。配置范围、路径范围、receipt范围、真实流范围分开保留。

| 已存source key | header有效行数 | UTI首末 |
|---|---:|---|
{headers}

配置start/end为2020-12-01～2021-02-22；full_dir的日期键为2020-12-01 21:00:00～2021-02-22 20:00:00。source receipt声明time范围为2020-12-01T09:00:00.500000～2021-02-22T23:00:00。trace实际header首尾时间为2020-12-01 09:00:00.500000～2021-02-22 15:00:00，稀疏events/source主流从2021-01-14 09:04:10至2021-02-22 14:55:15；顶层真实轴范围见G03，不能把路径或receipt跨度写成已读三路范围。

现成样例中2021-01-26 21:26:26.500000的source chunk_id=40，chunk_end_ts=2021-01-27 15:00:00；其outer time与source ts一致。其余两例chunk_id为31/53，完整值在source样例。datetime64[ns]不带时区，本次未建立完整夜盘/交易日/种子对齐结论。

**证据位置。** METADATA_ENRICHMENT.json（保留原始纳秒值）、BINDING.json receipt、samples/source_wall_matches.json。

**未核项/限制。** 时区声明、全窗交易日映射、窗口seed及未闭合life充分性unknown；未计算补齐。

## 操作对账、失败记录与回交边界

原turn三次命令在bwrap启动前失败；ENVFIX1后恢复。本次首次写前及后续命令均核主控holder PID296712、start_ticks58333981、inode13765718，竞争flock拒绝；没有清锁、夺锁或操作release.flag。初次只读FD探测的EBADF不当作锁证明，随后以O_RDWR无截断打开完成准确竞争核验。

原run-python.sh会写W外.migration日志，未直接执行；W内副本只适配workspace定位及日志路径，原文差异见launcher.diff。最初保护层拦住dill的/dev/null类型探测和tempfile对W外临时目录探测；允许空设备并将本进程TMPDIR定向W内后继续。原依赖、schema、参数和环境配置均未修复或改写。调查脚本独立编写，没有复制原长窗脚本的运行/全payload计数逻辑。

一次文本探测误把ts ELF交给sed，产生本地63,540字节二进制混合日志，日志预览随后发生UnicodeDecodeError；该动作仅打开binary读取。原始日志保留本地，不上传；提供文字摘要。此错误没有触发binary运行或写入。其他路径探测中不存在的候选文件和相关exit码照实留在COMMANDS.jsonl及日志。

副作用检查：[RECONCILIATION.json](RECONCILIATION.json) 对指定源码/launcher/schema重新hash、对binary核既有hash及不变size/mtime、对fields/receipt重新hash、对86次正式文件只读打开核size/mtime/inode；指定范围均未变。最终payload读取没有W外写入拒绝或producer调用。未以此声称对所有工作区文件做过盘点。

交付：FACT_REPORT.md、FACTS.json、实际脚本、必要命令/异常日志、四份真实样例、相关hash/diff和SHA256SUMS.txt。清单覆盖冻结的交付证据，排除自身、inbox、运行状态/tmp、未来Return及发布回执，避免自哈希循环。运行状态是本W的技术跟踪，不是E1业务接受状态。

向E1显式回交U01～U06（详见FACTS.json.unknowns）。两阶段发布仅限本Run worker_results/W001；先证据、后引用真实报告commit的WORKER_RETURN。Return=PARTIAL不代表E1接受。主控在实际回交及命令对账后释放租约，本Worker不释放。没有子委派或新建聊天。
'''
(OUT/'FACT_REPORT.md').write_text(report)
# 保留原异常日志原文前缀，二进制字节仅留本地。
p=OUT/'logs/readonly-proof-5.log';raw=p.read_bytes();prefix=raw.split(b'\x7fELF',1)[0].decode(errors='replace')
(OUT/'logs/readonly-proof-5.text.log').write_text(prefix+'\n[后续ELF二进制字节仅留本地原log，不上传。child exit=2；日志预览因UnicodeDecodeError使wrapper exit=1。binary未执行，未写入。]\n')
facts['created_files']=sorted(str(p.relative_to(OUT)) for p in OUT.rglob('*') if p.is_file() and 'inbox' not in p.relative_to(OUT).parts and 'tmp' not in p.relative_to(OUT).parts)
facts['created_files']+=['FACTS.json'] if 'FACTS.json' not in facts['created_files'] else []
facts['created_files_scope']='截至报告形成；后续清单、Return和发布回执另见HANDOFF/PUBLICATION记录；tmp技术文件不作为业务材料'
write_json('FACTS.json',facts)
print(json.dumps(dict(report=str(OUT/'FACT_REPORT.md'),facts=str(OUT/'FACTS.json'),unknown_ids=[x['id'] for x in unknowns]),ensure_ascii=False,indent=2))
