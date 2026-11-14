from pathlib import Path
import sys,json,os,hashlib,datetime,re,time
import runner as w
R=w.ROOT;START=w.utc();MODE=sys.argv[1] if len(sys.argv)>1 else 'imported'
RUN='OI-EAW-WALL-20261114-01';PUB='longrun/runs/'+RUN+'/delegations/D003/results/W002/'
SESSION=Path('/home/dw/.codex/sessions/2026/11/14/rollout-2026-11-14T21-53-08-01a1da55-5881-7590-94a1-0661f0236977.jsonl')
CONTROL={'artifacts/HASHES.sha256','artifacts/PUBLICATION_MANIFEST.json','artifacts/HANDOFF_RECEIPT.json'}
def load(rel):return json.loads((R/rel).read_text())
def fact(rel):
 p=R/rel;assert p.exists() and p.is_file() and not p.is_symlink() and p.resolve().is_relative_to(R)
 b=p.read_bytes();return {'local_path':str(p),'relative_path':rel,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
def all_files():
 found=[]
 for p in R.rglob('*'):
  assert not p.is_symlink()
  if p.is_file():found.append(str(p.relative_to(R)))
  assert len(found)<=50000
 return sorted(found)
def target(rel):
 if rel.startswith('artifacts/task-status/'):return PUB+'audit/frozen-local-task-status/'+rel[len('artifacts/task-status/'):]
 if rel.startswith('artifacts/'):return PUB+rel[len('artifacts/'):]
 return PUB+rel
def capture_transport():
 rows=[]
 for line in SESSION.open():
  try:r=json.loads(line)
  except json.JSONDecodeError:continue
  if r.get('type')!='event_msg' or r.get('timestamp','')<'2026-11-14T18:29:00':continue
  p=r.get('payload',{});i=p.get('item',{})
  if p.get('type')=='item_completed' and i.get('type')=='CommandExecution':rows.append({'record_type':'tool_transport_command_completion','timestamp':r.get('timestamp'),'started_at_ms':p.get('started_at_ms'),'completed_at_ms':p.get('completed_at_ms'),'item':i})
 p=R/'logs/EXEC_COMMAND_TRANSPORT.jsonl';p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
 nested=[json.loads(x) for x in (R/'logs/COMMAND_LOG.jsonl').read_text().splitlines() if x.strip()]
 header={'record_type':'command_log_scope','utc':w.utc(),'scope':'completed tool exec transport since W002 dispatch plus all nested logged business subprocess commands; nested/transport spans overlap and must not be summed','raw_stdout_stderr':'per nested command path/hash; transport aggregated_output retained verbatim as received, including any transport truncation markers','closing_driver':{'argv':['/usr/bin/python3.12','-B',str(Path(__file__)),MODE],'source':fact('audit/finalize_delivery.py'),'started_at':START,'purpose':'local manifest/hash validation and sealing only','process_exit':'observed in the enclosing execution tool receipt after this file is sealed; not invented here'},'no_reasoning_or_conversation_events_copied':True}
 p=R/'artifacts/COMMAND_LOG.jsonl';p.write_text(json.dumps(header,ensure_ascii=False)+'\n'+''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows)+''.join(json.dumps({'record_type':'nested_subprocess_completion',**x},ensure_ascii=False)+'\n' for x in nested))
 return len(rows),len(nested)
def validation():
 w.guard();o=load('input/C0009-remote-work_orders--W002--ORDER.json');d=load('input/C0008-remote-delegations--D003--DELEGATION.json');b=load('input/RUN_BINDING.json');p=load('artifacts/DRY_DEPENDENCY_PREFLIGHT.json');a=load('artifacts/WRITE_SURFACE_AUDIT.json')
 assert o['grant'] in b['grants'] and set(o['grant']['allowed_writes'])<=set(d['allowed_writes'])
 assert o['return_to']=='chatgpt:'+RUN+':executor:E1' and o['worker']=='codex:'+RUN+':worker:W1'
 assert p['decision']=='PREFLIGHT_STOP' and p['outcome']=='STOP' and not p['phase_1_started'] and not p['phase_2_started']
 assert a['writes_outside_WORK_ROOT']=='unknown' and a['shared_checkout_changed_by_W002'] is False
 assert all(all(v[k] for k in ['head_equal','branch_equal','status_equal','all_selected_file_metadata_and_hashes_equal']) for v in a['shared_audit_results'].values())
 assert not (R/'WORKER_RETURN.json').exists()
 for name in ['source','fixture','build','tests','stack-root']:assert not any((R/name).iterdir())
 for name in ['PREREQUISITE_PATCHSET.diff','COMPILE_ONLY_REPORT.json','SERIALIZATION_TEST_REPORT.json','STAGED_LOCAL_COMMIT_REPORT.json']:assert not (R/'artifacts'/name).exists()
 expected={'input/W002-DISPATCH.txt':'97531ff1c33d02233bae75c8e7b0aa0685e3a040f3e3f3ff503a99e575b1bca5','input/C0009-remote-work_orders--W002--ORDER.md':'03aaf0dbbb3b29602635e2d5f6874722874a68bfef7ccb62e3797bad1c785331','input/C0009-remote-work_orders--W002--ORDER.json':'1752e212d056d73a7868a168612e8e609a3d16247db4071b6f67aa03755ae249'}
 for rel,h in expected.items():assert fact(rel)['sha256']==h
 for x in load('receipts/INPUT_MIRROR_MANIFEST.json').values():assert hashlib.sha256(Path(x['local_path']).read_bytes()).hexdigest()==x['sha256']
 for x in load('audit/EXACT_SOURCE_BLOBS.json').values():assert hashlib.sha256(Path(x['receipt_path']).read_bytes()).hexdigest()==x['sha256']
 matrix=(R/'artifacts/EP_ACCEPTANCE_MATRIX.md').read_text()
 for ep in ['EP-WALL-SHARED-01','EP-WALL-SHARED-02','EP-WALL-SHARED-03','EP-SCENARIO-01','EP-SCENARIO-02','EP-SCENARIO-03','EP-SCENARIO-04','EP-SCENARIO-05']:assert ep in matrix
 for rel in all_files():
  q=R/rel;q.read_bytes().decode('utf-8')
  if q.suffix=='.json':json.loads(q.read_text())
  if q.suffix=='.jsonl':
   for l in q.read_text().splitlines():
    if l.strip():json.loads(l)
 return {'utc':w.utc(),'validation_status':'PASS_FOR_LOCAL_STOP_HANDOFF_ONLY','input_hash_checks':True,'JSON_and_JSONL_parse':True,'binding_and_return_to_E1':True,'phase1_and_phase2_not_entered':True,'gated_patch_fixture_compile_reports_absent':True,'no_formal_return_without_refs':True,'shared_named_audit_unchanged':True,'global_zero_write_proof':False,'work_root_symlink_escape':False,'no_business_acceptance_inferred':True,'process_exit_of_closing_driver':'separate enclosing tool receipt; no fabricated future exit'}
def handoff():
 o=load('input/C0009-remote-work_orders--W002--ORDER.json');definitions=[('DELIVERED',['WORKER_EXECUTION_REPORT.md'],[]),('DELIVERED',['D003_BINDING.json'],[]),('DELIVERED_PREFLIGHT_STOP',['DRY_DEPENDENCY_PREFLIGHT.json'],['offline compatible closure and future build cost bounds are not established']),('DELIVERED_WITH_FAILED_PROOF',['WRITE_SURFACE_PLAN.json','WRITE_SURFACE_AUDIT.json'],['zero outside-root writes unknown; EP-WALL-SHARED-03 unsatisfied']),('DELIVERED_NO_STAGING',['SOURCE_BASELINE_REPORT.md','SOURCE_CHANGE_MANIFEST.json'],['no staged baseline/tree or source patch']),('MISSING_PHASE0_GATE',[],['PREREQUISITE_PATCHSET.diff not created; no fake/empty patch']),('DELIVERED_WITH_EP_GAPS',['PRECONDITION_REPORT.md','EP_ACCEPTANCE_MATRIX.md'],['eight EPs not professionally accepted; static ledger subset only']),('PARTIAL_DOCUMENT_ONLY',['FIXTURE_SCHEMA_AND_PROVENANCE.md'],['complete schema and 9/18/22 fixture absent, not statically validated or executed']),('DELIVERED_STATIC_ONLY',['KNOWN_CONTRACT_CONFLICTS.md'],['dedicated harness/manifest absent; no runtime fact']),('DELIVERED',['COMMAND_LOG.jsonl','HASHES.sha256'],[]),('DELIVERED_APPLICABLE_STOP_ONLY',['ENGINEERING_STOP_REPORT.md'],['compile/serialization/local-commit conditional reports not applicable because not performed']),('PENDING_REAL_PUBLISHED_REFS',[],['formal WORKER_RETURN.json will be generated by same W1 only after controller supplies actual published evidence refs/hashes'])]
 mapping={}
 for description,(status,names,gaps) in zip(o['deliverables'],definitions):
  mapping[description]={'status':status,'local_files':[str(R/'artifacts'/n) for n in names],'sha256_and_bytes_catalog':str(R/'artifacts/PUBLICATION_MANIFEST.json'),'gaps':gaps}
 engineering=['EP-WALL-SHARED-01 snapshot accessor/patch/typecheck not constructed after Phase0 stop','EP-WALL-SHARED-02 evidence DTO/schema/canonical serialization not constructed','EP-WALL-SHARED-03 compatible offline dependency closure, four resource predictions and auditable zero outside writes not proven; procfs follow-up write facts unknown','EP-SCENARIO-01 dedicated target/main not constructed or compiled','EP-SCENARIO-02 exact-error evidence adapters/assertions not constructed or validated','EP-SCENARIO-03 transaction DTO and direct synthetic serialization not constructed or validated','EP-SCENARIO-04 only exact-source static conflict ledger delivered; dedicated harness/manifest absent','EP-SCENARIO-05 complete FX-WALL-SCENARIO-001 schema/fixture/hash and static 9/18/22 count/order validation absent','no staged tree/prerequisite local commit/PREREQUISITE_PATCHSET.diff; no compile-only or serialization test result; none invented']
 h={'record_type':'W002_LOCAL_STAGE_HANDOFF_NOT_FORMAL_WORKER_RETURN','run_id':RUN,'work_order_id':'W002','order_ref':'daowei2026/observe-iterate@8bc47de4fe83742049853a6538d1db0bad9468e4:longrun/runs/'+RUN+'/work_orders/W002/ORDER.json','worker':o['worker'],'return_to':o['return_to'],'outcome':'STOP','preflight_decision':'PREFLIGHT_STOP','result_ref':None,'intended_result_publish_path':PUB+'WORKER_EXECUTION_REPORT.md','engineering_missing':engineering,'missing':engineering+['W002 evidence has not yet been transported with real published commit/refs by the controller; all result refs are pending','formal v2 WORKER_RETURN.json generation and publication remain subsequent steps; no self/future ref or self hash invented'],'deliverable_manifest':mapping,'absolute_root':str(R),'all_output_file_paths_hashes_bytes_and_targets_catalog':str(R/'artifacts/PUBLICATION_MANIFEST.json'),'publication':{'worker_GitHub_write_authorized':False,'evidence_publish_root':PUB,'published_commit':None,'published_refs':None,'return_publish_path':'longrun/runs/'+RUN+'/worker_results/W002/WORKER_RETURN.json','steps':['controller transports frozen local originals byte-for-byte to approved Run branch','controller returns actual exact commit/ref/sha256/bytes mapping to same original W1','W1 validates real evidence refs and creates formal longrun-worker-return/v2 for W002 only to original E1','controller publishes Return byte-for-byte; original E1 consumes and makes professional decisions'],'publication_gap_vs_return_gap':'evidence publication is pending now. Once real refs are supplied, remove only that resolved gap; formal Return publication is a separate final step. Engineering gaps remain.'},'limits':['local Goal/ledger completion means this local stop handoff only; W002/D003/business completion not declared','no polling/new chat/new Worker or Run; W001 originals not modified','named source hash/mtime/status checks unchanged; global outside-write proof remains unknown','authorized mirrors hashes verified; optional current local Git object verification incomplete, not a claim of absent remote refs'],'conditional_reports_not_created':['COMPILE_ONLY_REPORT.json','SERIALIZATION_TEST_REPORT.json','STAGED_LOCAL_COMMIT_REPORT.json'],'indexes':{'HASHES_scope':'all publishable local originals except HASHES itself, PUBLICATION_MANIFEST and outer HANDOFF_RECEIPT; outer receipt seals these non-cyclic indexes','PUBLICATION_MANIFEST_scope':'all files except itself and outer receipt; outer receipt holds its hash','outer_receipt_self_hash':'returned in actual tool/final response, not embedded as a false self hash'}}
 w.save('artifacts/LOCAL_STAGE_HANDOFF.json',h)
 return h
def seal():
 w.guard();transport,nested=capture_transport();v=validation();v.update({'tool_transport_completed_commands':transport,'nested_subprocess_commands':nested,'phase':'final' if MODE=='final' else 'prepare'})
 w.save('receipts/LOCAL_STAGE_VALIDATION.json',v);handoff()
 base=[x for x in all_files() if x not in CONTROL]
 checks=''.join(fact(rel)['sha256']+'  '+rel+'\n' for rel in base);(R/'artifacts/HASHES.sha256').write_text(checks)
 entries=[{**fact(rel),'publish_target':target(rel),'publication_ref':None,'frozen_archive':True} for rel in all_files() if rel not in {'artifacts/PUBLICATION_MANIFEST.json','artifacts/HANDOFF_RECEIPT.json'}]
 targets=[x['publish_target'] for x in entries];assert len(targets)==len(set(targets))
 manifest={'record_type':'W002_EXACT_LOCAL_PUBLICATION_MANIFEST','utc':w.utc(),'run_id':RUN,'work_order_id':'W002','outcome':'STOP','published_commit':None,'publish_root':PUB,'file_count':len(entries),'total_bytes':sum(x['bytes'] for x in entries),'files':entries,'self_and_outer_receipt_not_self_hashed':['PUBLICATION_MANIFEST.json','HANDOFF_RECEIPT.json'],'separate_outer_receipt':str(R/'artifacts/HANDOFF_RECEIPT.json'),'excluded_large_build_cache_source_payloads':'none exist; source/build/cache directories empty','frozen_local_task_ledger':'archived under audit/frozen-local-task-status in destination; not an executor/manager acceptance ledger'}
 w.save('artifacts/PUBLICATION_MANIFEST.json',manifest)
 for e in entries:assert fact(e['relative_path'])['sha256']==e['sha256'] and fact(e['relative_path'])['bytes']==e['bytes']
 for line in (R/'artifacts/HASHES.sha256').read_text().splitlines():h,rel=line.split('  ',1);assert fact(rel)['sha256']==h
 fs=all_files();assert sum((R/p).stat().st_blocks*512 for p in fs)<2147483648 and len(fs)<50000
 receipt={'utc':w.utc(),'mode':MODE,'local_stage_outcome':'STOP','preflight_decision':'PREFLIGHT_STOP','actual_work_root':str(R),'return_to':'chatgpt:'+RUN+':executor:E1','publication_manifest':fact('artifacts/PUBLICATION_MANIFEST.json'),'hashes':fact('artifacts/HASHES.sha256'),'handoff':fact('artifacts/LOCAL_STAGE_HANDOFF.json'),'report':fact('artifacts/WORKER_EXECUTION_REPORT.md'),'local_validation':fact('receipts/LOCAL_STAGE_VALIDATION.json'),'manifest_file_count':len(entries),'hashes_verified_file_count':len(base),'all_manifest_hashes_rechecked':True,'all_files_UTF8_no_binary_payload':True,'symlink_escape_detected':False,'outer_indexes_publish_targets':{'PUBLICATION_MANIFEST.json':PUB+'PUBLICATION_MANIFEST.json','HANDOFF_RECEIPT.json':PUB+'HANDOFF_RECEIPT.json'},'receipt_self_hash':'not embedded; actual sha256 printed after write','closing_script':fact('audit/finalize_delivery.py'),'formal_return_created':False,'ledger_state':load('artifacts/task-status/tasks/w002-local-stage/snapshot.json')['status'],'limits':['proof applies to integrity/local STOP handoff, not engineering prerequisite acceptance','outside-WORK_ROOT writes unknown; procfs writes not captured; no build/test/scenario performed','no GitHub write; real result refs are pending','tool transport capture is completed commands before sealing; closing driver source/argv and this validation are preserved, enclosing execution tool supplies its actual final process exit']}
 w.save('artifacts/HANDOFF_RECEIPT.json',receipt)
 expected=set(e['relative_path'] for e in entries)|{'artifacts/PUBLICATION_MANIFEST.json','artifacts/HANDOFF_RECEIPT.json'};assert set(all_files())==expected
 for e in entries:assert fact(e['relative_path'])['sha256']==e['sha256']
 w.guard()
 print(json.dumps({'mode':MODE,'outcome':'STOP','preflight':'PREFLIGHT_STOP','file_count_total':len(all_files()),'publish_manifest_files':len(entries),'hashes_verified':len(base),'allocated_bytes':sum((R/p).stat().st_blocks*512 for p in all_files()),'key_files':{n:fact('artifacts/'+n) for n in ['WORKER_EXECUTION_REPORT.md','DRY_DEPENDENCY_PREFLIGHT.json','WRITE_SURFACE_AUDIT.json','LOCAL_STAGE_HANDOFF.json','PUBLICATION_MANIFEST.json','HASHES.sha256','HANDOFF_RECEIPT.json']},'ledger_state':receipt['ledger_state']},ensure_ascii=False,indent=2))
if __name__=='__main__':seal()
