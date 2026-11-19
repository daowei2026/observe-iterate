from pathlib import Path
import datetime,hashlib,json,os,subprocess
r=Path(__file__).resolve().parent
run_id='OI-U2-F-OBS-20261118-01';worker='codex:'+run_id+':worker:W1';return_to='chatgpt:'+run_id+':executor:E1'
order_ref='daowei2026/observe-iterate@1ce39d12f160c624916e7e370692915f3b4af6d3:longrun/runs/'+run_id+'/work_orders/W004/ORDER.json'
def load(name):return json.loads((r/name).read_text())
def save(name,value):(r/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def info(name):
 p=r/name;b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
report=load('output/u2_f_caegraph/definition_run_report.json');overlay=load('module_overlay_report.json');generated=load('tis_generated_inits.json');dispatch=load('logs/D_dispatch.json');final=load('source_final_verification.json')
assert overlay['ok'] and not overlay['preloaded'] and len(overlay['origins'])==7
assert all(v['expected']==v['actual'] and Path(v['actual']).is_relative_to(r/'source/mquant/tis') for v in overlay['origins'].values())
assert generated['seeder']['exit_code']==0 and generated['generated_count']==18 and generated['only_missing_empty_inits_created']
assert dispatch['attempt_count']==1 and int((r/'logs/w004_run.attempt_count').read_text())==1
code=int((r/'logs/w004_run.exit_code').read_text());assert code==1
assert report['completed'] is False and report['error_type']=='ModuleNotFoundError' and report['error']=="No module named 'mquant.tis.t1'"
assert all(not x['tracked_business_source_modified'] for x in final['repositories'].values())
assert not (r/'output/u2_f_caegraph/u2_f_caegraph.html').exists()
assert not (r/'output/u2_f_caegraph/prepared_tables').exists() and not (r/'output/u2_f_caegraph/plot_data').exists()
for entry in generated['generated']:
 p=Path(entry['path']);b=p.read_bytes();assert len(b)==entry['bytes']==0 and hashlib.sha256(b).hexdigest()==entry['sha256']
for entry in load('inputs/input_manifest.json'):
 p=Path(entry['path']);b=p.read_bytes();assert len(b)==entry['bytes'] and hashlib.sha256(b).hexdigest()==entry['sha256']
semaphores={}
for label in ['before','after']:
 rel='logs/dev_shm_sem.'+label+'.tsv';b=(r/rel).read_bytes();ec=int((r/('logs/dev_shm_sem.'+label+'.exit_code')).read_text())
 semaphores[label]={**info(rel),'snapshot_exit_code':ec,'object_count':len(b.splitlines()),'rows_tsv':b.decode()}
assert semaphores['before']['object_count']==semaphores['after']['object_count']==0
sem={'run_id':run_id,'work_order_id':'W004','method':'只读find /dev/shm -maxdepth 1 -name sem.*元数据并排序；与W003相同','snapshots':semaphores,'manual_semaphore_probe_count':0,'manual_creation_count':0,'manual_cleanup_count':0,'endpoint_residue_observed':False,'limitations':'两次端点快照为空不证明运行期间没有临时创建并正常删除sem.*；不是逐次IPC事件审计。没有删除无法归属或运行前对象。'}
save('semaphore_audit.json',sem)
blocker={'run_id':run_id,'work_order_id':'W004','state':'BLOCKED','error_type':report['error_type'],'error':report['error'],'traceback':report['traceback'],'occurrence':'D main line 679进入CurrSof时，平台SOF上下文加载uplot.multiscale，继而导入锁定TIS blk/gen.py line 5的from ..t1 import *','stage':'CurrSof construction before make_features call','constructor_import_succeeded':True,'make_features_called':False,'F_constructed':False,'fields_json_checked':False,'stop_rule':'首次明确阻断；不从旧runtime TIS拼装混合模块，不修改业务源码/平台，不作无界搜索或重试。','limited_static_check':str(r/'diagnostics/locked_tis_t1_path_check.json'),'repair_attempt_count_after_blocker':0,'additional_D_attempt_count':0}
save('first_blocker.json',blocker)
stages={name:load(name+'_source_stage_report.json') for name in ['observe_iterate','tis']}
save('source_stage_report.json',{'run_id':run_id,'work_order_id':'W004','status':'SUCCESS','repositories':{n:{'report':str(r/(n+'_source_stage_report.json')),'remote':d['remote_url'],'requested_commit':d['requested_commit'],'actual_head':d['actual_head'],'detached_head':d['detached_head'],'verification_passed':d['verification_passed'],'source_root':d['source_root']} for n,d in stages.items()}})
(r/'repair.diff').write_bytes(b'')
changes={'run_id':run_id,'work_order_id':'W004','business_source_modified':False,'D_modified':False,'C3_modified':False,'TIS_tracked_business_source_modified':False,'business_source_diff':str(r/'repair.diff'),'business_source_diff_bytes':0,'generated_empty_package_inits':generated['generated'],'generated_package_boundary_is_declared_build_product':True,'new_execution_wiring':[info(n) for n in ['w004_environment.sh','seed_tis.sh','materialize_tis.py','run_d_with_locked_tis.py','run_w004.sh','stage_sources.py']],'scope':'所有显式持久文件在W004；不修改平台包、生产数据、其他仓库工作树或W001-W003；原件源码未改，接线文件完整正文单独保留。'}
save('actual_changes.json',changes)
facts={'run_id':run_id,'work_order_id':'W004','parent_delegation_id':'D005','worker':worker,'return_to':return_to,'order_ref':order_ref,'fact_state':'BLOCKED','proposed_worker_return_outcome':'STOP','operation':'caegraph_run_and_repair','execution_context':'/dwdhome/fy/BASE_E6_2_copy','persistent_write_root':str(r),'source_staging':{'observe_iterate':{'commit':stages['observe_iterate']['actual_head'],'detached':True,'status':'SUCCESS'},'tis':{'commit':stages['tis']['actual_head'],'detached':True,'status':'SUCCESS','direct_SHA_fetch_accepted':True,'unlocked_fallback_used':False}},'tis_package_materialization':{'attempt_count':1,'exit_code':0,'generated_empty_init_count':18,'tracked_source_diff_bytes':0,'pretty_exports_executed':False},'module_overlay':{'ok':True,'preloaded_tis_modules':[],'origin_check_count':7,'origins_all_locked_checkout':True,'wrapper':info('run_d_with_locked_tis.py'),'report':str(r/'module_overlay_report.json'),'scope':'七个指定模块find_spec origin核验；不声称已经穷尽后续所有TIS依赖。'},'runtime':{'python_entry':(r/'logs/python_entry.txt').read_text().strip(),'python_version':(r/'logs/python_version.txt').read_text().strip(),'cwd':dispatch['cwd'],'environment_source':'W003已验证M3HOST/NO_PROXY/PYTHONPATH/TLS接线，W004 cache重定向','wrapper_attempt_count':1,'wrapper_exit_code':code,'D_attempt_count':1,'D_exit_code':code,'D_exit_code_basis':'D在同一Python进程中由runpy执行；未改D的main因completed=false返回1，SystemExit(1)经wrapper原样传播；shell保存该Python进程exit1。','wrapper_started_at':(r/'logs/w004_run.started_at').read_text().strip(),'D_dispatch_started_at':dispatch['started_at'],'finished_at':(r/'logs/w004_run.finished_at').read_text().strip(),'log':str(r/'logs/w004_run.log'),'environment_log':str(r/'logs/w004_environment.log'),'nif2_DNS_message':'environment日志保留；沿用W003 fallback后已成功进入overlay和D，不是本次最终阻断。','Landlock_used':False,'namespace_attempt_count':0,'mount_used':False,'sudo_used':False,'platform_patched':False,'independent_SemLock_probe_count':0},'source_final_verification':{'D_modified':False,'C3_modified':False,'TIS_business_source_modified':False,'repair_diff_bytes':0,'repositories':final['repositories'],'report':str(r/'source_final_verification.json')},'first_blocker':blocker,'products':{'candidate_html':None,'definition_run_report':str(r/'output/u2_f_caegraph/definition_run_report.json'),'definition_run_report_completed':False,'prepared_tables':None,'plot_data':None,'C2_preview_is_input_only':True,'make_features_called':False,'F_constructed':False,'exact_F_fields_json_checked':False,'exact_F_product_absence_inferred':False,'F_rerun_called':False,'full_history_producer_called':False,'Q_V_product_data_read':False,'E3_graph_acceptance':False,'E4_formal_export_admission':False,'formal_export_order':None,'DATA_READY':False,'D005_E_business_completed':False},'semaphore':sem,'history_preserved':['W001','W002','W003'],'source_checkout_pushed':False,'remote_records_written':False,'goal_created':False,'wakeup_created':False,'new_executor_created':False,'additional_live_audit':'无额外平台诊断执行；仅按首个缺失模块检查锁定checkout两个直接路径和Git树条目。'}
save('facts.json',facts)
receipt=load('execution_receipt.json');receipt.update({'phase':'EXECUTION_STOPPED_KNOWN_RESULT','fact_state':'BLOCKED','proposed_worker_return_outcome':'STOP','D_attempt_count':1,'D_exit_code':1,'wrapper_attempt_count':1,'wrapper_exit_code':1,'seed_inits_attempt_count':1,'seed_inits_exit_code':0,'ended_at':facts['runtime']['finished_at'],'first_blocker':report['error'],'candidate_html':None,'definition_run_report_completed':False,'not_business_completion':True});save('execution_receipt.json',receipt)
missing=["锁定TIS overlay在CurrSof上下文加载时无法导入mquant.tis.t1；本工单未混入旧runtime TIS或修改业务源码/平台", "make_features未调用，F未构造，精确fields.json存在性与真实F表未检查", "候选u2_f_caegraph.html未生成；definition_run_report.json已生成但completed=false", "prepared_tables与plot_data未生成", "E3核图接受与E4正式数据导出准入尚未发生；D005/E业务未完成"]
prep={'format':'local-worker-return-preparation/v2','is_formal_worker_return':False,'reason':'本轮新事实/日志/证据尚待主控原样发布并提供真实精确Git refs；本地路径不替代schema ref，不伪造未来commit。','target_schema_ref':'daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:longrun/contracts/longrun_schema_v2.json','fixed_fields':{'schema':'longrun-worker-return/v2','run_id':run_id,'work_order_id':'W004','order_ref':order_ref,'worker':worker,'return_to':return_to,'outcome':'STOP','missing':missing},'result_local_path':str(r/'FACT_REPORT.md'),'result_ref':None,'pending_manifest':'MANIFEST.local.json与TRANSPORT_PAYLOAD.json完整列出本地正文、bytes和SHA-256；正式manifest需以真实发布ref填充并按原worker_return schema仅保留ref/sha256。','facts':{'state':'BLOCKED','D_attempt_count':1,'D_exit_code':1,'seeder_exit_code':0,'origin_checks_passed':7,'candidate_html':None,'definition_report_completed':False,'business_completed':False},'return_signoff_next_action':'主控发布实际材料并给真实映射后，在同一W004下核验并生成WORKER_RETURN.json；此阶段不重跑D/producer/诊断。'}
save('RETURN_PREPARATION.json',prep)
text=f'''# W004 最小完整事实报告

- Run／工单／父委派：`{run_id} / W004 / D005`。
- Worker：`{worker}`；回交：`{return_to}`（原 issuer E1）。
- 活跃工单 JSON：`{order_ref}`。
- 工单正文：`daowei2026/observe-iterate@a243c56c9450c3a6964ce9b56701c921244821ad:longrun/runs/{run_id}/work_orders/W004/ORDER.md`。
- 事实状态：**BLOCKED**；正式 Return 待签认的 `outcome=STOP`。
- 这是实际执行后的已知停止结果。D005/E、WI-E、M-E 和父 Run 的业务完成均未发生。

## 1. 实际结果与首个真实阻断

原 D 已由工单指定的 run-local overlay wrapper 执行 **1 次，exit1**；wrapper 同为 1 次、exit1。D 在同一 Python 进程中经 `runpy.run_path(..., run_name="__main__")` 执行；未改 D 的 main 因 `completed=false` 返回1，`SystemExit(1)` 原样传播到 shell。seeder 是单独一次 **exit0**，不与 D 退出码混记。

```text
ModuleNotFoundError: No module named 'mquant.tis.t1'
```

阻断发生于 D main 第679行进入 `CurrSof` 时：SOF 上下文加载 `m3sof.settings.lib3` → `mquant.worker` → `mquant.uplot.multiscale` → 本轮锁定 TIS 的 `blk/gen.py` 第5行 `from ..t1 import *`。完整 traceback 原样保留在 `{r}/output/u2_f_caegraph/definition_run_report.json` 和 `{r}/first_blocker.json`。

原 `make_features` 构造模块已成功导入，但 `make_features(...)` 尚未调用；F 尚未构造，精确 `fields.json` 尚未检查。这不是 F 正式产品不存在的证据，也不是对 F、B、C 或 D 业务语义的否定。

对首个缺失模块只做了锁定 TIS checkout 的 `t1/`、`t1.py` 与 `git ls-tree HEAD t1` 有限静态核对：二个路径均不存在，Git 树查询为空。记录见 `{r}/diagnostics/locked_tis_t1_path_check.json`。没有进行全局搜索、额外平台 import 或诊断运行，未据此推断整个工作区或其他版本不存在该模块。按照首次明确阻断和禁止混用旧 runtime TIS 的条件停止；未接入旧 TIS、未修改业务模块或平台，未进行第二次 D。

## 2. 两个精确 source staging

- observe-iterate：`{r}/source/observe-iterate`；detached HEAD=`f4f0e4b276b1118b779473c1fbe462bc7a64b358`。报告：`{r}/observe_iterate_source_stage_report.json`。
- TIS：`{r}/source/mquant/tis`；detached HEAD=`2f460d663d821cf2ba25555eda13e78b697d0767`。direct SHA fetch 真实成功，没有使用未锁定分支或提交。报告：`{r}/tis_source_stage_report.json`。
- 二者 staging 与所需文件存在性检查均成功；初始和最终 `git status --short` 都为空。组合入口：`{r}/source_stage_report.json`。

## 3. Package boundary 与 overlay

锁定 TIS README 和 `seed_inits.py` 均按原件使用。seeder SHA-256：`{generated['seeder']['sha256']}`。

- `seed_inits.py` 一次 exit0，生成 **18 个原先缺失的空 `__init__.py`**；完整路径、字节数和 SHA-256：`{r}/tis_generated_inits.json`。
- 没有运行 `pretty-exports.py`，没有修改任何已跟踪 TIS 业务 `.py`；生成的空 init 是 README 声明的构建产物。它们被仓库忽略，空 `git status` 不代表没有这些构建产物。
- Wrapper：`{r}/run_d_with_locked_tis.py`，{info('run_d_with_locked_tis.py')['bytes']} 字节，SHA-256=`{info('run_d_with_locked_tis.py')['sha256']}`。
- Overlay 报告：`{r}/module_overlay_report.json`；`ok=true`、预加载 TIS 模块为空。构造模块、F/Q/V 类及 Wave/STCalendar/ScaleTurn 共七个 `find_spec` origin 均为本轮锁定 TIS checkout 的精确路径。
- 上述 origin 核验只覆盖工单列出的七个模块；本次随后出现的 `t1` 依赖阻断真实保留，未将七项通过扩大为所有依赖可用。
- Wrapper 只修改该进程内 `mquant.__path__`，未定义或替换 `make_features`，未复制构造参数，未修改平台 `mquant` 或 D/C3。

## 4. 运行包络与原始日志

- cwd：`{facts['runtime']['cwd']}`。
- Python：`{facts['runtime']['python_entry']}`，`{facts['runtime']['python_version']}`。
- 原入口 `source /dwdhome/fy/BASE_E6_2_copy/m3rc`，沿用 W003 已验证 M3HOST fallback、NO_PROXY、`.runtime/python-deps` 和 TLS preload；TMP/XDG/Numba/Matplotlib 均重定向本 W004 cache。
- Run 开始：`{facts['runtime']['wrapper_started_at']}`；结束：`{facts['runtime']['finished_at']}`。
- 完整运行日志：`{r}/logs/w004_run.log`；退出码：`{r}/logs/w004_run.exit_code`；D 派发原始记录：`{r}/logs/D_dispatch.json`；argv/cwd/Python/timestamps 同在 logs。
- 环境日志：`{r}/logs/w004_environment.log`；保留 `nif2` DNS 错误，fallback 后实际已进入 overlay 和 D，它不是本次首个最终阻断。
- Seeder stdout/stderr/环境日志和退出码均在 `{r}/logs/tis_seed_*`。
- 没有 Landlock、namespace、mount、sudo、平台 patch 或独立 SemLock probe；没有 producer 重跑和 Q/V 产品数据读取。原构造模块按锁定代码导入 F/Q/V 类，不等于读取 Q/V 结果。

## 5. 实际修改与最终源码

D/C3/TIS 已跟踪业务源均未修改：

- D：`{r}/source/observe-iterate/longrun/runs/{run_id}/artifacts/D/u2_f_caegraph_definition.py`，原提交 `f4f0e4b276b1118b779473c1fbe462bc7a64b358`，SHA-256 `92ab234df976469c6deb85052251b81633d79994440dccca199120672072433f`。
- C3：`{r}/source/observe-iterate/longrun/runs/{run_id}/artifacts/C/caegraph_display.py`，原件精确 ref 为 `daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/{run_id}/artifacts/C/caegraph_display.py`，SHA-256 `798042296f88ff5747a0248a81902953550fe39e4fa18337e8fdcfe9557877b7`。
- TIS 业务源目录与锁定提交见第2节；全部声明源文件路径／字节数／hash及未变核对：`{r}/source_final_verification.json`。
- `{r}/repair.diff`、`observe_iterate_final.diff`、`tis_final.diff` 均0字节。

本轮新增的是两个 run-local checkout、18空 init、namespace／环境／日志接线脚本和事实证据文件；完整接线正文独立保留，不能把“业务 diff 为零”写成“没有任何新文件”。接线清单见 `{r}/actual_changes.json`。没有修改或清理 W001–W003，没有推送 source checkout 或写远端记录。

## 6. 产物与未完成项

- 候选 HTML：**未生成**（C2 preview 仅为输入原件）。
- `definition_run_report.json`：**已生成**，路径 `{r}/output/u2_f_caegraph/definition_run_report.json`，`completed=false`。
- `prepared_tables/`、`plot_data/`：均未生成。
- make_features 未调用、F 未构造、fields.json 未检查、F 正式表未读。
- 未调用 `f.rerun()` 或全历史 producer；未读取 Q/V 产品数据。
- E3 未开始／未接受图；E4 正式取数未准入；无正式导出工单，`DATA_READY=false`。
- Worker 不作专业图接受判断，D005/E 业务未完成。结果继续回原 E1，由其消费此新阻断。

## 7. Semaphore 事实

前后均只读记录 `/dev/shm/sem.*` 的名称／属主／组／mode／size／mtime／inode：

- `{r}/logs/dev_shm_sem.before.tsv`：0字节，快照命令exit0。
- `{r}/logs/dev_shm_sem.after.tsv`：0字节，快照命令exit0。

没有手工创建测试 semaphore、没有删除运行前或无法归属对象，没有观察到端点残留。空快照不证明进程存续期间没有临时创建并正常删除 semaphore；这不是逐次IPC事件审计。机器说明：`{r}/semaphore_audit.json`。

## 8. 权限、运输与后继

授权与 Binding 逐字匹配证据：`{r}/authority_validation.json`；持久写面进一步限定 `{r}/**`，D 进程树临时 `sem.*` 继续使用原授权限制。不建立 Goal、计划休眠、后台唤醒或新执行器，不改本轮业务/图/位置语义。

本轮本地最小完整证据列表见 `{r}/MANIFEST.local.json`；正文、精确本地路径、字节数和SHA-256统一保存在 `{r}/TRANSPORT_PAYLOAD.json`，运输包与证据哈希索引见 `{r}/SHA256SUMS`。Git/cache和实时状态投影不作为报告原件混入运输正文；原始已锁定输入可沿用清单中真实存在的精确 refs。

`{r}/RETURN_PREPARATION.json` 是本地准备稿，**不是已发布或正式 Worker Return**。事实 `BLOCKED` 对应拟签认 `outcome=STOP`。待主控原样发布完整证据并返回真实 ref/hash 映射后，同一 W004 下核验并生成正式 `WORKER_RETURN.json`；不伪造未来提交，不重跑 D、producer 或诊断。主控负责运输，专业判断归原 E1。
'''
(r/'FACT_REPORT.md').write_text(text,encoding='utf-8')
checks={'run_id':run_id,'work_order_id':'W004','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'order_hashes_match':True,'grant_binding_exact_match':True,'both_detached_commits_match':True,'source_declared_files_unchanged':True,'generated_18_inits_empty_verified':True,'seven_origin_checks_passed':True,'D_attempt_count':1,'D_exit_code':1,'seeder_exit_code':0,'first_blocker_exact_match':True,'definition_report_completed':False,'no_candidate_html':True,'no_prepared_or_plot_data':True,'business_diff_zero':True,'sem_before_after_empty':True,'no_business_success_claimed':True,'formal_return_pending_real_publication_refs':True}
save('evidence_checks.json',checks)
env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1';env.pop('LONG_TASK_CONTROL_REGISTER_HELPER',None)
cli='/home/dw/.agents/skills/long-task-status/scripts/task_status.py';tid='oi-u2-f-obs-20261118-01-w004'
for a in [['step-complete','--root',str(r),'--task-id',tid,'--step-id','episode','--evidence',str(r/'facts.json'),'--evidence',str(r/'output/u2_f_caegraph/definition_run_report.json')],['step-start','--root',str(r),'--task-id',tid,'--step-id','transport','--action','D一次exit1，首阻断mquant.tis.t1；封存完整事实和运输材料，不重跑','--next-action','检查本地正文/hash后交主控原样发布']]:
 p=subprocess.run(['/usr/bin/python',cli]+a,env=env,cwd=r,capture_output=True,text=True)
 with (r/'logs/task_status_cli.log').open('a') as log:log.write(json.dumps(a,ensure_ascii=False)+'\n'+p.stdout+p.stderr)
 assert p.returncode==0,p.stderr
print(json.dumps({'state':'BLOCKED','outcome_pending':'STOP','D_attempts':1,'D_exit_code':1,'blocker':report['error'],'FACT_REPORT':info('FACT_REPORT.md')},ensure_ascii=False,indent=2))
