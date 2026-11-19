# W009要求的只读origin probe；不实现环境接线，不修改sys.path或package __path__。
from pathlib import Path
import datetime,importlib,json,os,sys,traceback
r=Path('/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W009')
base=Path('/dwdhome/fy/BASE_E6_2_copy');candidate=base/'.runtime/fqv-rb-hc-i-20261117';mquant_root=candidate/'runtime/mquant'
modules=['mquant','mquant.frame','mquant.tis','mquant.tis.frp','mquant.tis.frp.fqv_kline_example','mquant.tis.frp.CommonPriceTurnGroupCandidates','mquant.tis.frp.PostTurnGroupDirectionalOrganization','mquant.tis.frp.CommonTurnGroupValidity','mquant.tis.blk.gen','mquant.tis.t0','mquant.tis.t1','mquant.tis.t2','mquant.tis.t3']
report={'run_id':'OI-U2-F-OBS-20261118-01','work_order_id':'W009','candidate':str(candidate),'expected_mquant_root':str(mquant_root),'python_executable':sys.executable,'python_version':sys.version,'sys_path_before_probe':list(sys.path),'environment_summary':{k:os.environ.get(k) for k in ['M3WORKS','PYTHONPATH','PATH','LD_PRELOAD','PYTHONDONTWRITEBYTECODE','TMPDIR','XDG_CACHE_HOME','NUMBA_CACHE_DIR','MPLCONFIGDIR']},'requested_module_origins':{},'all_loaded_mquant_origins':{},'import_failure':None,'first_failure':None,'probe_explicitly_modified_import_paths':False,'business_functions_called':False,'make_features_called':False,'producer_called':False,'product_data_read':False,'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
def origin(module):
 spec=getattr(module,'__spec__',None)
 return {'file':getattr(module,'__file__',None),'path':list(getattr(module,'__path__',[])),'spec_origin':None if spec is None else spec.origin}
for name in modules:
 try:
  module=importlib.import_module(name);report['requested_module_origins'][name]={'import_succeeded':True,**origin(module)}
 except Exception as exc:
  report['requested_module_origins'][name]={'import_succeeded':False,'error_type':type(exc).__name__,'error':str(exc)}
  report['import_failure']={'module':name,'error_type':type(exc).__name__,'error':str(exc),'missing_module':getattr(exc,'name',None),'traceback':traceback.format_exc()};break
outside=[];unresolved=[]
for name,module in sorted(list(sys.modules.items())):
 if name=='mquant' or name.startswith('mquant.'):
  if module is None:report['all_loaded_mquant_origins'][name]={'unresolved':True};unresolved.append(name);continue
  item=origin(module);paths=([item['file']] if item['file'] else [])+item['path'];item['all_paths_within_candidate_mquant']=bool(paths) and all(Path(p).resolve().is_relative_to(mquant_root.resolve()) for p in paths);report['all_loaded_mquant_origins'][name]=item
  if not paths:unresolved.append(name)
  elif not item['all_paths_within_candidate_mquant']:outside.append({'module':name,**item})
report['sys_path_after_probe']=list(sys.path);report['probe_sys_path_unchanged']=report['sys_path_after_probe']==report['sys_path_before_probe']
report['outside_candidate_mquant_modules']=outside;report['unresolved_origin_modules']=unresolved
codex=base/'.codex'
codex_paths=[p for p in [sys.executable]+list(sys.path) if p and Path(p).resolve().is_relative_to(codex)]
report['codex_target_in_executable_or_sys_path']=codex_paths
if report['import_failure'] is not None:report['first_failure']={'classification':'DEDICATED_RUNTIME_IMPORT_FAILED','reason':report['import_failure']['error'],'module':report['import_failure']['module']}
elif codex_paths:report['first_failure']={'classification':'DEDICATED_RUNTIME_EXTERNAL_SOURCE_LEAK','reason':'现有入口的executable/sys.path实际来自.codex目标','paths':codex_paths}
elif outside:report['first_failure']={'classification':'DEDICATED_RUNTIME_MIXED_MQUANT_ORIGINS','reason':'至少一个实际加载mquant模块的来源不在同一候选mquant根','first_outside_module':outside[0]['module']}
elif unresolved or not report['probe_sys_path_unchanged']:report['first_failure']={'classification':'DEDICATED_RUNTIME_MIXED_MQUANT_ORIGINS','reason':'无法证明所有mquant来源或probe期间路径发生改变'}
report['status']='PASS' if report['first_failure'] is None else 'FAIL';report['loaded_mquant_module_count']=len(report['all_loaded_mquant_origins']);report['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (r/'dedicated_runtime_provenance.json').open('x',encoding='utf-8') as f:json.dump(report,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({'status':report['status'],'requested_modules_imported':len(report['requested_module_origins']),'loaded_mquant_module_count':report['loaded_mquant_module_count'],'outside_candidate_mquant_count':len(outside),'unresolved_origin_count':len(unresolved),'first_failure':report['first_failure'],'import_failure':report['import_failure']},ensure_ascii=False,indent=2))
raise SystemExit(0 if report['status']=='PASS' else 1)
