import sys,json,os,hashlib,datetime
from pathlib import Path
from runtime import B,R,save,desc,now,guard
A=R/'artifacts';guard()
T=json.loads((A/'SELECTED_GHC_TOOLCHAIN.json').read_text())
pre=json.loads((A/'CURRENT_COMPILE_PREFLIGHT.json').read_text())
closure=json.loads((A/'CURRENT_SOURCE_CLOSURE.json').read_text())
readers=json.loads((A/'CURRENT_READER_SOURCE_BASELINE.json').read_text())
inputs=json.loads((A/'READONLY_INPUTS_BASELINE.json').read_text())
old=json.loads((A/'W007_EVIDENCE_RETENTION_MANIFEST.json').read_text())
checks=[]
for group,rows in [('current_source',closure['files']),('reader_source',readers['files']),('package_db_metadata',pre['package_DB_metadata']),('W007_frozen85',old['files']),('readonly_contract_inputs',inputs['inputs'])]:
 for x in rows:
  y=desc(x['path']);same=all(y[k]==x[k] for k in ['bytes','sha256','mtime_ns','inode','dev']);assert same,(group,x['path'])
  checks.append({'group':group,'before':x,'after':y,'same_bytes_hash_mtime_inode_dev':same})
repo_check=[];repos={}
for name,path in [('frp',B/'edh-universe/frp/frp'),('frp_core',B/'edh-universe/frp/frp-core'),('tis',B/'mquant/tis')]:
 comparisons=[]
 for suffix in ['head','branch','status','diff','cached-diff']:
  p=R/'logs'/f'base-pre-{name}-{suffix}.stdout';q=R/'logs'/f'base-post-{name}-{suffix}.stdout';same=p.read_bytes()==q.read_bytes();assert same
  comparisons.append({'kind':suffix,'pre':desc(p),'post':desc(q),'bytes_equal':same})
 repos[name]={'path':str(path),'head':(R/'logs'/f'base-post-{name}-head.stdout').read_text().strip(),'branch':(R/'logs'/f'base-post-{name}-branch.stdout').read_text().strip(),'status_porcelain_tracked':(R/'logs'/f'base-post-{name}-status.stdout').read_text(),'before_after_same':True}
 repo_check.append({'repo':name,'comparisons':comparisons})
for name,path in [('frame',B/'mquant/frame'),('worker',B/'mquant/worker')]:
 repos[name]={'path':str(path),'head':(R/'logs'/f'reader-current-{name}-head.stdout').read_text().strip(),'branch':(R/'logs'/f'reader-current-{name}-branch.stdout').read_text().strip(),'status_porcelain_tracked':(R/'logs'/f'reader-current-{name}-status.stdout').read_text(),'reader_paths_diff_bytes':(R/'logs'/f'reader-current-{name}-reader-diff.stdout').stat().st_size,'note':'只读reader源码绑定；未进行该repo运行构建，不作未记录pre/post全repo断言'}
extra=[B/'stack.yaml',B/'stack.yaml.lock',B/'edh-universe/frp/frp/frp.cabal',B/'edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1.hs',B/'edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/FaoIngress.hs',B/'edh-universe/frp/frp/test/Frp/Instance/ISL/Eaw/P1/P1EndToEndSpec.hs',B/'m3sof/settings/json.py',B/'mquant/worker/adt/__init__.py']
source_files={x['path']:x for x in closure['files']+readers['files']}
for p in extra:source_files[str(p)]=desc(p)
snapshots=[]
for p in map(Path,source_files):snapshots.append({**desc(p),'text_utf8':p.read_text()})
save(A/'CURRENT_SOURCE_TEXT_SNAPSHOTS.json',{'at':now(),'role':'只读证据文本归档；不是独立源码树或build输入；实际编译直接读取liveBASE','files':snapshots})
save(A/'BASE_ASSET_INVENTORY.json',{'at':now(),'repos':repos,'current_sources':list(source_files.values()),'toolchain':T,'compile_preflight':str(A/'CURRENT_COMPILE_PREFLIGHT.json'),'existing_test_target':'frp:eaw-p1-v1-6-1-light-integration exists in current frp.cabal; no prebuilt target found in scoped dist filename query; whole smoke main not executed','available_live_interfaces':['applyWallOccurrenceBatch','existing derived Show of WallLifecycleState','Publication ToBSON/FromBSON WallLifecycleOccurrence','FrpDbaDao source path'],'current_normal_material':str(R/'materials/CURRENT_NORMAL_CHAIN.jsonl'),'current_BSON_material':str(R/'materials/CURRENT_BSON_READER.jsonl'),'existing_scenarios':[str(R/'materials/EXISTING_CROSS_FIRING_DUPLICATE.jsonl'),str(R/'materials/EXISTING_AFTER_END_UPDATE.jsonl')],'native_DBA_wrapper_scope':'specified existing dbaw.py AST118classes, zero Wall/P1 classes; no global environment absence claim','graph_notebook_scope':'pure data selected by C0017; no wholeBASE notebook/CAEGraph search, none executed','historical_material':'D001/D002 accepted normal chain preserved; no legacy material re-read as current','broad_search_boundary':'snapshot root361children exceeded declared200 cap; no child probes, exact2pkgdbpaths from existing setup-config used','new_existing_source_edits':0})
fs=[p for p in R.rglob('*') if p.is_file()];buildfs=[p for p in (R/'build').rglob('*') if p.is_file()]
save(A/'BASE_SIDE_EFFECTS_AND_DIFF_REPORT.json',{'at':now(),'observation_scope':'具名合同输入、85旧W7、10current source/具名reader、3repos status/diff与精确packageDBmetadata；未做全盘副作用追踪，不宣称全BASE/HOME全局零写','worker_shell_cwd':str(B),'HOME':os.environ['HOME'],'CODEX_HOME':os.environ['CODEX_HOME'],'source_and_inputs_checks':checks,'repo_checks':repo_check,'expected_new_write_paths':[str(R/'build'),str(R/'tmp'),str(R/'materials'),str(R/'logs'),str(R/'receipts'),str(R/'artifacts'),str(R/'input'),str(R/'tools'),str(R/'cache')],'shared_BASE_build_cache_writes_planned':[],'selected_packageDB_metadata_unchanged':True,'build_competition_pre':str(A/'BASE_BUILD_COMPETITION_PRE.json'),'compile_competition_pre':pre['competing_selected_build_processes'],'build_file_count_at_check':len(buildfs),'build_bytes_at_check':sum(p.stat().st_size for p in buildfs),'W008_file_count_at_check':len(fs),'W008_bytes_at_check':sum(p.stat().st_size for p in fs),'scope_counts_note':'最终文件数/bytes以FREEZE为准，以上为本检查时点；无把新增量虚报为零','old_W007_commands_rerun':0,'W007_evidence_preserved':True,'production_writer_invocations':0,'WallAssembler_market_compute_invocations':0,'new_scenario_count':2,'new_Cabal_target_count':0,'dependency_install_count':0,'GitHub_write_count':0,'other_chat_message_count':0,'new_lock_final_check':guard(),'old_lock_released_by_worker':False,'new_lock_released_or_replaced_by_worker':False})
(A/'CURRENT_PROCESSING_SKELETON.md').write_text('''# 当前处理骨架与实际观察层

静态生产链：WallAssembler occurrence/receipt/packed numeric rows → TIS WallOccurrenceFao OnlyRead → current FaoIngress decode/partition → applyWallOccurrenceBatch + FRP maintainWallLifecycle → dumpWallOutputs → wall_occurrences(O)/wall_current_view(C updates)/wall_diagnostics(D) → FrpDbaDao + generated wrapper/consumer。完整A是内部active map/FRP Dynamic，不是C append-update表。

本W实际执行的层：existing test形状typed input → live BASE current applyWallOccurrenceBatch → 实际returned occurrence和WallLifecycleState既有Show；独立执行current Publication occurrence ToBSON/FromBSON。未运行WallAssembler/packed ingress、FaoModel事件引擎或dumpWallOutputs，未物化DBA产品。9个current生产模块从live BASE直接编译，依赖现成installed package DB，Frp.Instance.BussinessUtils仍来自缓存ABI；不声称全checkout重新构建或依赖二进制生成版本已完整追回。

| 对象 | 真实取得 | 不能混同 |
|---|---|---|
| upstream/input | 4条人工typed normal input，两个已有test表达式输入 | 自然WallAssembler输出或产品生成receipt |
| O | reducer实际returned列表，normal各1/2/1，共4 | production event writer执行 |
| C | 实际state Show中的wallCurrentUpdateBatch，N2仅最后update，N3 Ended | full active snapshot、物化C或FRP Event |
| A | 实际state Show中的wallViews，End后fromList [] | producer A0 trace、FRP Dynamic实际提交 |
| D | scenario实际Left constructor和identity | wall_diagnostics通道实际发布或有效空 |
| consumer | current occurrence-level BSON adapter四条读回相等 | physical DBA reader/完整Batch/D roundtrip |

End当前typed change和BSON为WallEnded(reason)，没有band/core字段；不存在本W物化的价格0。最后合法更新band[101,103]/core102只在前一更新上下文，不能补进End原值。源值、Show、JSON记录、BSON文档层次分别保存；JSON是观察容器，不是新canonical product schema。

版本、HEAD/branch/status/diff及source metadata见BASE_ASSET_INVENTORY/BASE_SIDE_EFFECTS报告；相关源码逐字文本单独作为JSON证据归档，未复制为可构建源码树，现有源码无改动。
''')
rawfiles=sorted(p for p in (R/'materials').iterdir() if p.is_file())
for p in rawfiles:assert p.stat().st_size>0
bindings={'source_repos':repos,'compiled_current_modules':'5 initial Wall modules +4 Publication dependency modules, exact paths/hashes in preflight/source closure','compiler':T,'data_origin':'synthetic controlled typed input using existing light-test fixture shape; not natural data','symbol':'rb','side':'BidWall','localNo':999,'calendar':'SHFE-night existing test label only; no loaded calendar','UTI':[10,11,12,14],'writer_firing':'NOT_EXECUTED; N1/N2/N3 are call ordinal only','actual_time':None,'confirm_time':None,'known_time':None,'production_FeatureRunIdentity':None,'effective_production_parameters':None,'natural_current_data_loaded':False,'FeatureRunIdentity_note':'not constructed/loaded by direct reducer; actualW008 scope explicit in binding; do not fabricate run receipt from fixture'}
missing=[
 {'id':'M-PRODUCTION-RUNTIME','reason':'已运行current纯reducer与occurrence BSON adapter；未执行FaoModel/maintainWallLifecycle事件引擎、dumpWallOutputs、物理O/C/D或FRP Dynamic提交，不能称production runtime PASS。'},
 {'id':'M-NATIVE-DBA-READER','reason':'当前DBA产品未物化；指定dbaw.py的118类中无Wall/P1 wrapper。只核现成reader源码/命名空间，未导入完整production设置或运行FrpDbaDao.loadWith；四条ToBSON/FromBSON内存读回不等于native physical reader或Batch/D roundtrip。'},
 {'id':'M-PRODUCTION-TUPLE-TIME','reason':'人工typed输入rb/BidWall/local999/UTI10,11,12,14；SHFE-night仅existing test label，未加载日历，无生产参数/receipt/canonical FeatureRunIdentity/market epoch/actual-confirm-known时间。'},
 {'id':'M-D-EVENT-CORRELATION','reason':'取得exact reducer Left+identity；未运行D事件通道、ingress decode与诊断合并，不能把无Left等同D有效空，也无实际D时序identity对账。'},
 {'id':'M-CACHED-DEPENDENCY-PROVENANCE','reason':'9个相关production模块从liveBASE编译，既有frp-core/其他依赖与BussinessUtils缓存ABI只读复用；未证明这些缓存全部由当前dirty checkout生成。'},
 {'id':'M-COVERAGE','reason':'normal3call/4input加最多2既有表达式；after-End setup省略Dormant/restore，原after-End update UTI低于End，未单独隔离late policy；未执行整套existing smoke assertion，也未验证其他terminal/transaction/UTI/自然频率。'},
 {'id':'M-PROFESSIONAL-QUALIFICATION','reason':'预期WORKING/未冻结。专业材料接受、必要性/正式comparison、父Q/H3/G-RUN和D003最终关闭均仍由E1/manager决定，不以本W事实自动完成。'},
 {'id':'M-EVIDENCE-PUBLICATION','reason':'本地文件已准备；尚无本W真实GitHub出版commit/ref，所有ref保留null，主控须先逐字运输并回读bytes/SHA。'},
 {'id':'M-FORMAL-RETURN','reason':'仅在主控提供真实已出版证据refs后，由原W1同W008生成v2 WORKER_RETURN.json只回原E1；当前不造future/self ref或Return。'}]
save(A/'CURRENT_MATERIAL_MANIFEST.json',{'schema':'w008-current-material-manifest/v1','at':now(),'work_order_id':'W008','delegation_id':'D004','outcome':'PARTIAL','material_status':'PARTIAL_WITH_LIMITS','bindings':bindings,'raw_and_derived_materials':[{**desc(p),'class':'controlled synthetic current source reducer' if 'BSON' not in p.name else 'controlled existing current occurrence BSON codec','ref':None} for p in rawfiles],'normal_calls':3,'normal_input_count':4,'normal_O_count':4,'existing_scenario_expression_count':2,'BSON_occurrence_roundtrip_equal_count':4,'all_materials_same_origin_not_independent_votes':True,'professional_comparison_status':'NOT_FROZEN_NOT_STARTED','missing':missing})
(A/'CURRENT_MATERIAL_REVIEW.md').write_text('''# W008真实材料核查

标签：**PARTIAL_WITH_LIMITS**；本地outcome **PARTIAL**。这是材料事实标签，不作业务合理性或专业接受决定。

normal实跑3个纯reducer调用：N1 Start UTI10，N2两条合法BandUpdate UTI11/12，N3 End UTI14。全部Right，O条数1/2/1；完整人工typed input、O和pre/post原始Show在CURRENT_NORMAL_CHAIN.jsonl。N2实际A与C仅ref wall-occurrence-2b（band[101,103]/core102）；N3 A为空，C仍含WallEndedState。A/C来自既有derived Show的精确字段抽取，CURRENT_NORMAL_RECONCILIATION保留原Show来源，不推断FRP提交。

当前Publication occurrence-level ToBSON/FromBSON实跑4条全部读回相等，compact-local-v2 schema及完整BSON文档Show保留。End只有reason，没有band/core字段，不按legacy zero表示重构当前数据。该读回是内存canonical occurrence adapter，未测试DBA物理批次/诊断schema或generated wrapper。

两个已存在场景表达式：cross-firing相同Start实际Left WallStartedTwice(local999)；已有test预期requireRight/空发布，二者的实现合同张力保留。after-End update实际Left WallUpdateBeforeStart(local999)，原test只要求任意Left；setup本W缩为Start/BandUpdate/End，省去Dormant/restore；update UTI11低于End14，不能另称已隔离late policy。harness exit0表示观察记录成功，不是整套smoke assertion通过；没有运行旧九场景整包或额外第三scenario。这里不作正式SUPPORTS/COUNTERS。

身份仅限本W人工数据scope/localNo999/ref；没加载生产FeatureRunIdentity或上游receipt。rb、BidWall和UTI值真实记录于typed input；SHFE-night只是现成testlabel，无实际日历/自然时间映射。command wallclock是执行时间，不是业务actual/confirm/known。现成依赖缓存只绑定packageDB metadata/ABI，不伪造全部生成来源。

缺失区分：N3 reducer A fromList []为实际有效空；normal中没有Left是本层成功，不等于D事件有效空；未物化current DBA、无真实生产参数tuple是DataUnavailable/NotObtained；自然无事件、InsufficientHistory、Pending runtime状态均未由该人工fixture验证，不能混成0。

可交原E1消费的事实：当前reducer正常身份/变化、同次两更新last C、reducer A删除、两个exact state error constructor、current End measurement shape、occurrence BSON adapter四条往返。不能回答：production engine/DBA writer/native reader完整链、实际诊断事件对账、自然频率、完整terminal/transaction/time policy或业务适用性最终判断。

首次PATH GHC缺libtinfo.so.5 exit127；现成tinfo6同9.4.8替代查询成功，无依赖安装。第一次脚本编译因Worker本W列表类型歧义exit1，5个production模块编译成功；仅新增脚本NoOverloadedLists后同范围编译成功，失败脚本及完整日志保留。现有snapshot361目录超过自定小搜索200边界，未逐项搜索，转用setup-config已给两个精确pkgdb。三项局部问题未冻结其他合法取材。

逐份bytes/SHA/真实missing见CURRENT_MATERIAL_MANIFEST；完整命令、exit、elapsed、输出和副作用见EXECUTION报告/COMMAND_LOG/receipts。旧W007的85原件只读保存，未作为本轮current material。
''')
execs=[json.loads(l) for l in (R/'logs/COMMAND_EXECUTIONS.jsonl').read_text().splitlines()]
lines=['# W008当前材料执行记录','', 'worker shell实际cwd=/dwdhome/fy/BASE_E6_2；单个工具子进程真实cwd逐项记录。HOME/CODEX_HOME保持。所有命令先写.pre receipt声明输入范围、写面、timeout与process-group TERM/KILL停止法；最大600秒，输出阈值5GiB。未执行不计为已执行。','', '| command | exit | seconds | stdout bytes | stderr bytes |','|---|---:|---:|---:|---:|']
for e in execs:lines.append(f"| {e['label']} | {e['exit_code']} | {e['elapsed_seconds']:.6f} | {e['stdout']['bytes']} | {e['stderr']['bytes']} |")
lines+=['','每项完整argv/cwd、输入/输出绝对路径、bytes/SHA、开始结束时间、env override、预计写面和实际exit在同名receipt以及logs/COMMAND_EXECUTIONS.jsonl。其余只读资格核验/文件生成命令及上述命令的外层shell也逐字保存在COMMAND_LOG.jsonl。原生封存调用进行中状态如实记null；其真实终态由最终工具回执交主控，不能预填exit0。','']
for e in execs:
 lines += [f"## {e['label']}",'',f"cwd: `{e['cwd']}`",f"argv: `{json.dumps(e['argv'],ensure_ascii=False)}`",f"输入边界：{e['input_scope']}",f"输出：`{e['stdout']['path']}` / `{e['stderr']['path']}`；receipt=`{R/'receipts'/(e['label']+'.json')}`",f"exit={e['exit_code']}；elapsed={e['elapsed_seconds']:.9f}s；预期写面={json.dumps(e['expected_writes'],ensure_ascii=False)}；stop={e['stop_reason']}。",'']
lines+=['## 副作用与版本限制','', '本W直接编译live BASE的相关9模块，原有源码没有写入。BASE共享build/cache/packageDB只读复用，编译输出在W008/build、临时文件在W008/tmp；具名source/input/packageDB metadata与3repo tracked status/diff前后相等。未追踪全盘每次系统调用，不作全BASE/HOME零写证明；旧零外写工程前置已取消。所有实际文件最终体量及nonUTF8类型在FREEZE/PUBLICATION_MANIFEST。现有dirty STCalendar.py/BussinessUtils.hs保留，不覆盖。','', '当前源码HEAD只是源码绑定；9模块确实由本W编译，外部已装依赖缓存另列ABI metadata，未声称生产二进制全checkout来源完备。未安装依赖、未调用stack重建共享库、未clean/fetch/pull/checkout/reset/rebase/merge/push，未执行生产或自然行情计算。']
(A/'CURRENT_MATERIAL_EXECUTION_REPORT.md').write_text('\n'.join(lines)+'\n')
(A/'WORKER_EXECUTION_REPORT.md').write_text('''# W008/D004本地执行原件交付

身份：原W1 / 原E1 C0017签新W008，原物理thread01a1da55-5881-7590-94a1-0661f0236977，实际gpt-6.1-sol/max，worker cwd BASE。Owner A001及D004根grant生效；原HOME/CODEX_HOME保持，现有源码只读。

**outcome=PARTIAL；material_status=PARTIAL_WITH_LIMITS。** 本地有限Goal只覆盖本W实际取材及归档，不能作为W/D/父任务完成或专业接受。

Lane A：只读逐份核W007冻结85原件、2,075,599bytes SHA一致，原PID251010已不存在，旧kernel锁无匹配。主控PRE/POST逐字留存；主控实际pidfd SIGTERM释放，精确unlock时刻/keeper exitcode未知。本W没有释放旧锁、恢复旧工程、补造W007 Return。新D004真实holder255320/startticks49586940/inode14866078保持，本W同inode独立竞争EAGAIN；未替换/释放。

Lane B：按新版control/02步骤0～7直接使用BASE。实际取得current最小normal：Start→同次两条合法BandUpdate→End，3个纯reducer调用/4条typed输入，O返回1/2/1。实际state Show显示N2只保留最后C，N3 A空、C为Ended。两个existing低成本表达式分别实际返回WallStartedTwice与WallUpdateBeforeStart。current occurrence BSON adapter四条内存读回全部相等，compact-local-v2及End无band/core字段的原始文档保留。现有源码、生产结果无修改，未建设隔离/副本/旧closure或九场景整包。

材料是人工controlled current-source reducer与occurrence BSON adapter，不是自然行情、FRP engine提交、production DBA writer或原生physical reader PASS。SHFE-night只是existing test label；UTI人工、无actual/confirm/known/market epoch或生产FeatureRunIdentity tuple。harness exit0不表示whole existing smoke test通过；cross-firing重放与既有test合同张力如实保留，未作正式COUNTERS。

局部问题已保留：PATH GHC libtinfo.so.5缺失；现成同9.4.8 tinfo6可用。Worker脚本初次类型歧义失败后只在本W修正，不改现有源码，生产5模块初次已编过。snapshot目录361超过声明小搜索边界，停止展开，使用既有setup-config两个精确pkgdb。无依赖安装、无生产覆盖、无源码push或GitHub写、无其他聊天消息。所有命令/原件/bytes/SHA/副作用和12项ORDER映射附本包。

缺口完整列于CURRENT_MATERIAL_MANIFEST及LOCAL_STAGE_HANDOFF：FRP/物理产品/native reader、生产tuple/time、D事件、缓存完整生成来源、覆盖限制、专业资格、证据出版及后续正式Return。conditional BASE_CHANGE_CANDIDATE未触发：normal已取得，native链也不是单一小源码变更可保证解除，本W不实施源码改动。

主控运输目标：longrun/runs/OI-EAW-WALL-20261114-01/delegations/D004/results/W008/。逐文件精确目标见PUBLICATION_MANIFEST；artifacts内文件映射到该目录根，其他目录保持相对路径。非UTF8编译产物保留真实bytes/hash/mime，不冒充UTF8。

当前没有本W真实出版commit/ref，未生成正式WORKER_RETURN.json。主控先逐字出版证据并回读校验，再回原W1同W008生成V2正式Return，目标worker_results/W008/WORKER_RETURN.json，return_to只原E1。未来Return不能作为当前manifest证据或自hash。旧W007禁止补Return。专业材料接受、预期冻结、comparison/父Q/H3/G-RUN与最终D003关闭由原E1/manager负责。
''')
order=json.loads((R/'input/C0017-pin-ORDER.json').read_text())
mapfiles=[['WORKER_EXECUTION_REPORT.md'],['W008_BINDING.json'],['W007_CLOSEOUT_EXECUTION_FACTS.md','W007_EVIDENCE_RETENTION_MANIFEST.json'],['../input/W007_LOCK_RELEASE_PRE.json','../input/W007_LOCK_RELEASE_POST.json','../input/D004_W008_LOCK_BINDING.json'],['BASE_ASSET_INVENTORY.json','CURRENT_PROCESSING_SKELETON.md'],['MATERIAL_REQUIREMENTS_AND_SELECTION.md'],['CURRENT_MATERIAL_EXECUTION_REPORT.md','../logs/COMMAND_EXECUTIONS.jsonl'],['CURRENT_MATERIAL_REVIEW.md','CURRENT_MATERIAL_MANIFEST.json'],['../materials/CURRENT_NORMAL_CHAIN.jsonl','../materials/CURRENT_NORMAL_RECONCILIATION.json','../materials/CURRENT_BSON_READER.jsonl','../materials/EXISTING_CROSS_FIRING_DUPLICATE.jsonl','../materials/EXISTING_AFTER_END_UPDATE.jsonl'],['BASE_SIDE_EFFECTS_AND_DIFF_REPORT.json','COMMAND_LOG.jsonl','PUBLICATION_MANIFEST.json','HASHES.sha256'],[],[]]
mapping=[]
for i,(literal,names) in enumerate(zip(order['deliverables'],mapfiles)):
 mapping.append({'deliverable_index_0based':i,'order_literal':literal,'local_files':[str((A/n).resolve()) for n in names],'status':'PRESENT' if i<10 else ('NOT_TRIGGERED_NO_EXISTING_SOURCE_EDITS' if i==10 else 'DEFERRED_PENDING_REAL_PUBLISHED_REFS'),'notes':('current事实原件，production/reader等具体限制见missing' if i==8 else '所有ref在真实出版前保持null')})
save(A/'LOCAL_STAGE_HANDOFF.json',{'schema':'w008-local-stage-handoff/v1','at':now(),'run_id':'OI-EAW-WALL-20261114-01','work_order_id':'W008','delegation_id':'D004','issuer_call_id':'C0017','worker':order['worker'],'return_to':order['return_to'],'order_ref':'daowei2026/observe-iterate@a61efeed234064599011ebc897e4da61928c2403:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W008/ORDER.json','outcome':'PARTIAL','material_status':'PARTIAL_WITH_LIMITS','result_local_path':str(A/'WORKER_EXECUTION_REPORT.md'),'result_ref':None,'formal_return_created':False,'deliverable_mapping':mapping,'missing':missing,'publication_repository':'daowei2026/observe-iterate','authorized_publication_prefix':'longrun/runs/OI-EAW-WALL-20261114-01/delegations/D004/results/W008/','publication_layout':'strip local artifacts/ prefix; retain input/tools/logs/receipts/materials/build relative paths','formal_return_publication_target':'longrun/runs/OI-EAW-WALL-20261114-01/worker_results/W008/WORKER_RETURN.json','formal_return_to':order['return_to'],'self_or_future_refs_invented':False,'next_steps':['Root逐字运输真实证据，回读bytes/SHA并给原W1 exact refs','原W1同W008只生成正式v2 Return及validation，只回E1；不重跑调查','Root逐字出版正式Return并执行机械Gate；原E1专业消费，manager按权责决定后继'],'goal_scope':'仅本W本地原件交付；不是W/D/父任务完成','lock_kept_for_formal_same_W008':True})
print(json.dumps({'report':desc(A/'WORKER_EXECUTION_REPORT.md'),'material_manifest':desc(A/'CURRENT_MATERIAL_MANIFEST.json'),'handoff':desc(A/'LOCAL_STAGE_HANDOFF.json'),'qualified_readonly_comparisons':len(checks),'command_receipts':len(execs),'outcome':'PARTIAL','material_status':'PARTIAL_WITH_LIMITS'},ensure_ascii=False))
