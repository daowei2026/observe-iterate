from pathlib import Path
import os,sys,json,hashlib,datetime,fcntl,errno,re,importlib.metadata
from jsonschema import Draft202012Validator
ROOT=Path('/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W002');DEST=ROOT/'final-return'
A=Path('/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01');LOCK=ROOT.parents[1]/'.D003-writer.lock'
RUN='OI-EAW-WALL-20261114-01';COMMIT='2af8a364b4157958b59d68ab4fc24eb6a95f5593';PUBLISH_ROOT='longrun/runs/'+RUN+'/delegations/D003/results/W002/'
HOME_BEFORE=os.environ.get('HOME');CODEX_BEFORE=os.environ.get('CODEX_HOME');BEGIN=datetime.datetime.now(datetime.timezone.utc).isoformat()
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def digest(b):return hashlib.sha256(b).hexdigest()
def guard():
 assert Path.cwd()==Path('/dwdhome/fy/BASE_E6_2')
 assert DEST.resolve()==DEST and not any(p.is_symlink() for p in [DEST,*DEST.parents])
 assert os.environ.get('HOME')==HOME_BEFORE and os.environ.get('CODEX_HOME')==CODEX_BEFORE
 assert os.environ.get('PYTHONDONTWRITEBYTECODE')=='1'
 t=Path('/proc/237355/stat').read_text();assert t[t.rfind(')')+2:].split()[19]=='45798445'
 st=LOCK.lstat();assert st.st_ino==14806399 and not LOCK.is_symlink()
 holder=Path('/proc/237355/fdinfo/3').read_text();assert 'FLOCK' in holder and 'WRITE 237355' in holder and '14806399' in holder
 fd=os.open(LOCK,os.O_RDWR|os.O_NOFOLLOW)
 try:
  assert os.fstat(fd).st_ino==14806399
  try:fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
  except BlockingIOError as e:assert e.errno in (errno.EACCES,errno.EAGAIN)
  else:raise RuntimeError('STOP: lock unexpectedly acquired')
 finally:os.close(fd)
 return {'utc':utc(),'holder_pid':237355,'holder_startticks':'45798445','inode':14806399,'holder_fdinfo':holder,'same_inode_competition_failed':True,'holder_lock_acquired_replaced_released':False}
def save(name,obj):
 guard();p=DEST/name;assert p.parent==DEST and not p.exists();b=(json.dumps(obj,ensure_ascii=False,indent=2)+'\n').encode();p.write_bytes(b);return {'local_path':str(p),'bytes':len(b),'sha256':digest(b)}
def load(p):return json.loads(p.read_bytes())
def snap(p):
 st=p.lstat();b=p.read_bytes();assert p.is_file() and not p.is_symlink() and p.resolve()==p and p.is_relative_to(ROOT) and not p.is_relative_to(DEST)
 return {'path':str(p),'bytes':len(b),'sha256':digest(b),'git_blob_sha':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'mtime_ns':st.st_mtime_ns,'ctime_ns':st.st_ctime_ns,'mode':st.st_mode,'dev':st.st_dev,'inode':st.st_ino}
def inventory_digest(items):return digest(json.dumps(items,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
def verify():
 lock_before=guard();task=A/'W002-FORMAL-RETURN-TASK.txt';tb=task.read_bytes();assert len(tb)==4058 and digest(tb)=='356ef2bf142ab375d624e3e0af9676d434e0f43f7a65faae2214b3d0685fa269'
 publication=load(A/'W002-published-refs.json');local=load(A/'W002-local-archive-verification.json');candidate=load(A/'W002-archive-commit-candidate.json');attempt=load(A/'W002-archive-publish-attempt.json')
 assert publication['state']=='PUBLISHED_REMOTE_BYTE_VERIFIED' and publication['commit']==COMMIT and publication['outcome']=='STOP'
 assert publication['repository']=='daowei2026/observe-iterate' and publication['branch']=='runs/'+RUN
 assert publication['all_299_byte_equal'] is True and publication['only_allowed_new_paths'] is True
 assert attempt['commit']==COMMIT and attempt['all_299_byte_equal'] is True and attempt['only_allowed_new_paths'] is True
 assert candidate['commit']==COMMIT and candidate['base']==publication['parent']==attempt['parent']
 rows=publication['files'];assert len(rows)==299 and local['file_count']==299 and local['exact_file_set'] is True
 assert len({x['ref'] for x in rows})==len({x['local_path'] for x in rows})==len({x['path'] for x in rows})==299
 local_by_path={x['local_path']:x for x in local['files']};assert len(local_by_path)==299
 old=[];by_local={};by_key={}
 for row in rows:
  p=Path(row['local_path']);s=snap(p);assert row['path'].startswith(PUBLISH_ROOT) and '..' not in Path(row['path']).parts
  assert row['ref']=='daowei2026/observe-iterate@'+COMMIT+':'+row['path']
  assert s['bytes']==row['bytes'] and s['sha256']==row['sha256'] and s['git_blob_sha']==row['git_blob_sha']==row['remote_blob_sha'] and row['byte_equal'] is True
  l=local_by_path[str(p)];assert l['sha256']==row['sha256'] and l['bytes']==row['bytes'] and l['publish_target']==row['path'] and l['git_blob_sha']==row['git_blob_sha']
  key=row['path'][len(PUBLISH_ROOT):];assert key and not row['path'].endswith('/WORKER_RETURN.json')
  old.append(s);by_local[str(p)]=row;by_key[key]=row
 old.sort(key=lambda x:x['path']);assert sum(x['bytes'] for x in old)==local['total_bytes']==3476977
 frozen_paths={str(p) for p in ROOT.rglob('*') if p.is_file() and not p.is_relative_to(DEST)};assert frozen_paths==set(by_local)
 order=load(ROOT/'input/C0009-remote-work_orders--W002--ORDER.json');handoff=load(ROOT/'artifacts/LOCAL_STAGE_HANDOFF.json');schema=load(ROOT/'input/longrun_schema_v2.json');assert order['work_order_id']=='W002' and order['run_id']==RUN
 assert digest((ROOT/'input/C0009-remote-work_orders--W002--ORDER.json').read_bytes())=='1752e212d056d73a7868a168612e8e609a3d16247db4071b6f67aa03755ae249'
 assert digest((ROOT/'input/longrun_schema_v2.json').read_bytes())=='32c1e2409ff4936a87d688848736bb9af71fe0415d338ba66dd031e3149243d3'
 assert order['worker']=='codex:'+RUN+':worker:W1' and order['return_to']==order['issuer']=='chatgpt:'+RUN+':executor:E1'
 assert handoff['outcome']=='STOP' and handoff['preflight_decision']=='PREFLIGHT_STOP'
 assert handoff['order_ref']=='daowei2026/observe-iterate@8bc47de4fe83742049853a6538d1db0bad9468e4:longrun/runs/'+RUN+'/work_orders/W002/ORDER.json'
 report=by_key['WORKER_EXECUTION_REPORT.md'];assert report['sha256']=='2ab3240b7c9306d61a67e60e7a27f478d6322f07dcc11f6b46df0932ccecd0ac'
 session=Path('/home/dw/.codex/sessions/2026/11/14/rollout-2026-11-14T21-53-08-01a1da55-5881-7590-94a1-0661f0236977.jsonl');turn=None
 for line in session.open():
  try:r=json.loads(line)
  except json.JSONDecodeError:continue
  if r.get('type')=='turn_context':turn=r
 actual={k:turn['payload'].get(k) for k in ['cwd','model','effort']};assert actual=={'cwd':'/dwdhome/fy/BASE_E6_2','model':'gpt-6.1-sol','effort':'max'}
 manifest={key:{'ref':v['ref'],'sha256':v['sha256']} for key,v in by_key.items()}
 alias_targets={0:'WORKER_EXECUTION_REPORT.md',1:'D003_BINDING.json',2:'DRY_DEPENDENCY_PREFLIGHT.json',3:'PUBLICATION_MANIFEST.json',4:'PUBLICATION_MANIFEST.json',6:'EP_ACCEPTANCE_MATRIX.md',7:'FIXTURE_SCHEMA_AND_PROVENANCE.md',8:'KNOWN_CONTRACT_CONFLICTS.md',9:'PUBLICATION_MANIFEST.json',10:'ENGINEERING_STOP_REPORT.md'}
 coverage=[]
 for i,description in enumerate(order['deliverables']):
  h=handoff['deliverable_manifest'][description];direct=[by_local[p]['ref'] for p in h['local_files']]
  if i in alias_targets:
   x=by_key[alias_targets[i]];manifest[description]={'ref':x['ref'],'sha256':x['sha256']}
  coverage.append({'order_deliverable':description,'manifest_alias_present':i in alias_targets,'alias_evidence':alias_targets.get(i),'direct_published_evidence_refs':direct,'original_local_stage_status':h['status'],'remaining_engineering_gaps':h['gaps'] if i!=11 else [],'current_interpretation':'本正式Return已本地生成，等待主控出版；禁止自引用，所以没有已出版manifest alias' if i==11 else ('真实patch未产生，保留缺失且不虚构ref' if i==5 else 'alias仅定位真实已出版证据；不将报告/状态文档等同于缺失的patch/fixture/build结果')})
 engineering=list(handoff['engineering_missing']);assert len(engineering)==9
 missing=engineering+[
  order['deliverables'][5]+'：Phase0 STOP后未构造该patch；manifest未为缺失文件虚构ref。',
  order['deliverables'][7]+'：仅已出版状态/来源说明文档；完整fixture/schema及9/18/22静态验证仍缺失。',
  order['deliverables'][11]+'：本正式Return已在本地生成；仍待主控逐字发布至longrun/runs/'+RUN+'/worker_results/W002/WORKER_RETURN.json，当前没有该Return真实出版ref，禁止self/future ref。299份原件出版缺口已由commit '+COMMIT+'解决；冻结handoff/report的pending仅为先前本地阶段历史。'
 ]
 result={'schema':'longrun-worker-return/v2','run_id':RUN,'work_order_id':'W002','order_ref':handoff['order_ref'],'worker':order['worker'],'return_to':order['issuer'],'outcome':'STOP','result_ref':report['ref'],'missing':missing,'manifest':manifest}
 checked_schema={'$schema':schema['$schema'],'$defs':schema['$defs'],'$ref':'#/$defs/worker_return'};Draft202012Validator.check_schema(checked_schema);v=Draft202012Validator(checked_schema);errors=list(v.iter_errors(result));assert not errors,[e.message for e in errors]
 assert len(manifest)==309 and all(set(x)=={'ref','sha256'} for x in manifest.values())
 trusted={x['ref']:x['sha256'] for x in rows};assert all(trusted[x['ref']]==x['sha256'] for x in manifest.values())
 omitted=set(order['deliverables'])-set(manifest);assert omitted=={order['deliverables'][5],order['deliverables'][11]} and result['outcome']!='EXECUTED' and result['missing']
 assert all(any(ep in x for x in missing) for ep in ['EP-WALL-SHARED-01','EP-WALL-SHARED-02','EP-WALL-SHARED-03','EP-SCENARIO-01','EP-SCENARIO-02','EP-SCENARIO-03','EP-SCENARIO-04','EP-SCENARIO-05'])
 rf=save('WORKER_RETURN.json',result);loaded=load(DEST/'WORKER_RETURN.json');assert loaded==result and not list(v.iter_errors(loaded))
 new=[]
 for row in rows:new.append(snap(Path(row['local_path'])))
 new.sort(key=lambda x:x['path']);assert old==new
 assert {str(p) for p in ROOT.rglob('*') if p.is_file() and not p.is_relative_to(DEST)}==frozen_paths
 receipts={}
 for name in ['W002-FORMAL-RETURN-TASK.txt','W002-published-refs.json','W002-local-archive-verification.json','W002-archive-commit-candidate.json','W002-archive-publish-attempt.json']:
  p=A/name;b=p.read_bytes();receipts[name]={'path':str(p),'bytes':len(b),'sha256':digest(b)}
 lock_after=guard();validation={'record_type':'W002_FORMAL_WORKER_RETURN_LOCAL_VALIDATION','started_at':BEGIN,'completed_at':utc(),'result':'PASS_FOR_LOCAL_FORMAL_RETURN_ONLY','outcome':'STOP','work_order_id':'W002','worker_return':rf,'schema':{'path':str(ROOT/'input/longrun_schema_v2.json'),'sha256':digest((ROOT/'input/longrun_schema_v2.json').read_bytes()),'validator':'jsonschema.Draft202012Validator','version':importlib.metadata.version('jsonschema'),'worker_return_definition_checked':True,'errors':[],'remote_schema_resolution':False},'actual_configuration':actual,'thread_id':'01a1da55-5881-7590-94a1-0661f0236977','lock_before':lock_before,'lock_after':lock_after,'HOME_preserved':HOME_BEFORE,'CODEX_HOME_preserved':CODEX_BEFORE,'unique_new_file_root':str(DEST),'controller_receipts':receipts,'publication':{'repository':publication['repository'],'branch':publication['branch'],'commit':COMMIT,'controller_state':publication['state'],'controller_remote_byte_equal_assertions_checked':299,'worker_direct_remote_access_performed':False,'scope':'主控真实运输回执为远端出版依据；Worker仅直接读取本地299原件，核sha256/bytes/Git blob hash及映射一致性，不把主控远端回读冒称Worker直接远端访问。'},'frozen_originals':{'count':299,'total_bytes':sum(x['bytes'] for x in old),'sha256_bytes_blob_sha_all_match_published_index':True,'path_set_unchanged':True,'byte_hash_size_mtime_ctime_inode_dev_mode_unchanged':True,'before_inventory_sha256':inventory_digest(old),'after_inventory_sha256':inventory_digest(new),'read_atime_not_used_for_freeze_comparison':True},'manifest':{'published_file_entries':299,'exact_order_deliverable_aliases':10,'total_entries':309,'each_value_only_ref_and_sha256':True,'all_values_found_in_actual_publication_index':True,'return_itself_or_future_refs_in_manifest':False,'missing_order_keys':sorted(omitted),'non_EXECUTED_with_nonempty_missing_allows_missing_keys':True,'full_controller_validate_worker_return_or_route_return_executed':False},'deliverable_coverage':coverage,'missing_reconciliation':{'engineering_missing_carried_verbatim':engineering,'resolved_evidence_publication_gap':True,'resolved_local_formal_return_generation_gap':True,'formal_return_publication_remaining':True,'historical_frozen_pending_notes':'299原件中的LOCAL_STAGE_HANDOFF.json、WORKER_EXECUTION_REPORT.md记载的是先前阶段；现299已真实出版，本正式Return已本地生成。没有修改历史原件。','no_patch_fixture_compile_serialization_or_semantic_acceptance_fabricated':True},'new_file_publish_targets':{n:'longrun/runs/'+RUN+'/worker_results/W002/'+n for n in ['WORKER_RETURN.json','WORKER_RETURN_VALIDATION.json','COMMAND_LOG.jsonl','generate_worker_return.py']},'required_next_step':{'operator':'原主控','publish_exact_local_return_to':'longrun/runs/'+RUN+'/worker_results/W002/WORKER_RETURN.json','then':'主控validate-worker-return/route-return后交原E1消费；Worker不直接联系E1或manager'},'limits':['本次只核验原件完整性、schema、身份、真实索引与missing；不重新调查、probe、stage/build/test/scenario或直接访问远端','原工程零外写unknown及全部工程缺口维持；未作EP/专业接受、D003/G-RUN或父任务完成判断','正式Return本身当前未出版，其ref/hash没有放入已出版证据manifest','完整controller receipt/route验证需要主控真实Return出版ref和独立receipt，未在本地伪造'],'command_records':str(DEST/'COMMAND_LOG.jsonl')}
 vf=save('WORKER_RETURN_VALIDATION.json',validation)
 print(json.dumps({'result':'PASS','outcome':'STOP','originals_verified_unchanged':299,'manifest_entries':309,'order_deliverable_aliases':10,'missing_count':len(missing),'formal_return':rf,'validation':vf,'GitHub_write_performed':False},ensure_ascii=False))
if __name__=='__main__':verify()
