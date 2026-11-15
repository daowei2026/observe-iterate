"""W005正式Return生成与形式/运输一致性验证；不执行任何原工程步骤。"""
from pathlib import Path
import datetime, errno, fcntl, hashlib, inspect, json, os, re, sys
import jsonschema
from jsonschema import Draft202012Validator

BASE=Path('/dwdhome/fy/BASE_E6_2')
ROOT=BASE/'.oi-runs/OI-EAW-WALL-20261114-01/D003/W005'
FINAL=ROOT/'final-return'
ART=ROOT/'artifacts'
AUTH=Path('/dwdhome/fy/cgpterm/artifacts/oi-eaw-wall/OI-EAW-WALL-20261114-01')
LOCK=ROOT.parents[1]/'.D003-writer.lock'
SESSION=Path('/home/dw/.codex/sessions/2026/11/14/rollout-2026-11-14T21-53-08-01a1da55-5881-7590-94a1-0661f0236977.jsonl')
TURN='01a1dc8a-bc4d-7882-9e12-56fb0382968f'
RUN='OI-EAW-WALL-20261114-01'
ORDER_REF='daowei2026/observe-iterate@bf5a28e7afe8ef87280d3c37fd40b81c5f5ea804:longrun/runs/OI-EAW-WALL-20261114-01/work_orders/W005/ORDER.json'
COMMIT='10e9433477db333ed5d7bf7ac4a1feee508dce44'
PREFIX='longrun/runs/'+RUN+'/delegations/D003/results/W005/'
REF_PREFIX='daowei2026/observe-iterate@'+COMMIT+':'
RETURN_TO='chatgpt:'+RUN+':executor:E1'
WORKER='codex:'+RUN+':worker:W1'
STOP='STOP_SECCOMP_STATIC_PREPARATION_ASSERTION'

def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def fact(p):
    p=Path(p);b=p.read_bytes();s=p.lstat()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'mtime_ns':s.st_mtime_ns,'mtime_ns_exact':str(s.st_mtime_ns),'inode':s.st_ino,'dev':s.st_dev}
def save(name,obj):
    p=FINAL/name;assert p.parent==FINAL and p.resolve().is_relative_to(FINAL)
    with p.open('x') as f:f.write(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def guard():
    assert Path.cwd()==BASE and FINAL.resolve()==FINAL and not any(p.is_symlink() for p in [FINAL,*FINAL.parents])
    assert os.environ['HOME']=='/home/dw' and os.environ['CODEX_HOME']=='/home/dw/.codex'
    assert sys.flags.isolated and sys.dont_write_bytecode
    assert os.environ['PYTHONDONTWRITEBYTECODE']=='1' and Path(os.environ['TMPDIR'])==FINAL
    t=Path('/proc/246047/stat').read_text();assert t[t.rfind(')')+2:].split()[19]=='47679582'
    info=Path('/proc/246047/fdinfo/3').read_text();assert 'FLOCK' in info and 'WRITE 246047' in info and LOCK.lstat().st_ino==14806399
    fd=os.open(LOCK,os.O_RDWR|os.O_NOFOLLOW)
    try:
        assert os.fstat(fd).st_ino==14806399
        try:fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError as e:competition_errno=e.errno;assert e.errno in (11,13)
        else:raise RuntimeError('STOP unexpected lock acquisition')
    finally:os.close(fd)
    return {'at':utc(),'holder_pid':246047,'startticks':'47679582','session':45594,'inode':14806399,'fdinfo':info,'independent_same_inode_competition_errno':competition_errno,'only_own_contender_closed':True,'holder_lock_not_changed_or_released':True}
def safe_ref(ref):
    m=re.fullmatch(r'([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)@([a-f0-9]{40}):([^\s:#]+)',ref)
    assert m and '\\' not in m[3] and all(x not in ('','.','..','.git') for x in m[3].split('/'))
    return m.groups()

lock_before=guard()
pref=json.loads((FINAL/'FINALIZE_PREFLIGHT.json').read_bytes())
for original in pref['contract_inputs']:assert fact(original['path'])==original
pub=json.loads((AUTH/'W005-published-refs.json').read_bytes())
assert pub['commit']==COMMIT and pub['file_count']==67 and len(pub['files'])==67 and pub['bytes']==1226532
assert pub['all_remote_exact_bytes_gitblob_sha256_verified'] and pub['only_67_allowed_added_paths'] and pub['branch_head_verified']
published_by_path={e['path']:e for e in pub['files']}
assert len(published_by_path)==67
original_before={r['file']['path']:r['file'] for r in pref['original67_before']}
assert set(original_before)==set(published_by_path)
for p,f in original_before.items():assert fact(p)==f
order=json.loads((AUTH/'C0013-remote-work_orders--W005--ORDER.json').read_bytes())
signed=json.loads((AUTH/'C0013-remote-calls--C0013--PRO_RETURN.json').read_bytes())
assert order['work_order_id']=='W005' and order['run_id']==RUN and order['issuer_call_id']==signed['call_id']=='C0013'
assert order['issuer']==order['return_to']==RETURN_TO and order['worker']==WORKER and ORDER_REF in signed['issued_order_refs']
handoff=json.loads((ART/'LOCAL_STAGE_HANDOFF.json').read_bytes())
verdict=json.loads((ART/'PHASE0_RECOVERY_VERDICT.json').read_bytes())
constant=json.loads((ART/'FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json').read_bytes())
static=json.loads((ART/'SECCOMP_FILTER_STATIC_EVALUATION.json').read_bytes())
delta=json.loads((ART/'SECCOMP_IOCTL_FILTER_DELTA.json').read_bytes())
failure=json.loads((ROOT/'receipts/STATIC_PREPARATION_FAILURE.json').read_bytes())
assert verdict['outcome']=='STOP' and verdict['stop_code']==STOP and verdict['new_preparer_attempts']==1
assert verdict['R0_A1_attempts']==verdict['R0_B_attempts']==verdict['R0_C_attempts']==0 and not verdict['automatic_retry']
assert not any(verdict[x] for x in ['WRITE_CONFINEMENT_PASS','OFFLINE_CLOSURE_PASS','FOUR_BUDGETS_KNOWN_WITHIN_CAP','CONTINUOUS_MONITORS_PASS','BPF_static_acceptance_PASS','conditional_EP_entered'])
assert constant['integer_decimal']==21585 and constant['integer_hex']=='0x5451' and constant['local_definitions_agree']
assert static['evaluator_attempts']==0 and static['preparer_attempts']==1 and not static['static_PASS']
assert not delta['candidate_BPF_generated'] and not delta['new_launcher_exists'] and not delta['new_runtime_exists']
assert failure['native_command_record']['item']['exit_code']==1 and failure['BPF_evaluator_entered'] is False
assert failure['R0_A1_attempts']==0 and 'AssertionError' in failure['stderr']
assert not (ROOT/'tools/runtime.py').exists() and not (ROOT/'tools/landlock_launcher.py').exists()

manifest={}
for e in pub['files']:
    assert e['ref']==REF_PREFIX+e['repo_path'] and e['repo_path']==PREFIX+e['relative']
    safe_ref(e['ref']);assert e['relative'] not in manifest
    manifest[e['relative']]={'ref':e['ref'],'sha256':e['sha256']}
label_records=[]
assert len(order['deliverables'])==len(handoff['deliverable_mapping'])==13
for index,(literal,mapping) in enumerate(zip(order['deliverables'],handoff['deliverable_mapping'])):
    assert literal==mapping['deliverable_literal']
    candidates=[published_by_path[p] for p in mapping['local_files']]
    if candidates:
        assert literal not in manifest
        main=candidates[0]
        manifest[literal]={'ref':main['ref'],'sha256':main['sha256']}
        label_records.append({'deliverable_literal':literal,'manifest_alias_added':True,'primary_ref':main['ref'],'all_associated_published_files':[{'path':e['path'],'ref':e['ref'],'sha256':e['sha256']} for e in candidates],'status':'实际STOP报告与原件索引；证明式标签不代表实质要求已PASS。'})
    else:
        assert index in (10,12)
        label_records.append({'deliverable_literal':literal,'manifest_alias_added':False,'status':'NOT_ATTEMPTED_FOUR_PASS_NOT_MET' if index==10 else 'LOCAL_RETURN_CREATED_BUT_SELF_PUBLICATION_PENDING_NO_FUTURE_REF','reason':'四PASS未成立；不造空条件产物。' if index==10 else '当前Return尚无真实出版ref，不能把自身或未来validation/generator/log塞入manifest。'})
assert len(manifest)==78 and len({x['ref'] for x in manifest.values()})==67

# Preserve substantive gaps. The frozen publication-pending statements remain history.
assert len(handoff['missing'])==14
missing=list(handoff['missing'][:11])
missing[0]=STOP+'：'+missing[0]+' 本机termios/header已一致核实FIOCLEX=0x5451；此次不是静态case运行失败、新kernel/ioctl实测失败或kernel不支持。'
missing.append('67份证据已经真实出版至commit '+COMMIT+'且逐字/Gitblob/hash核验完成，证据出版缺口已解决；正式Return本阶段已本地生成，但主控仍需逐字出版至longrun/runs/'+RUN+'/worker_results/W005/WORKER_RETURN.json，取得真实Return ref及独立Worker receipt后执行完整Gate。ORDER逐字标签“V2 WORKER_RETURN.json returning only to executor E1”尚无可列的自身出版ref；不造future/self ref。')
missing.append(handoff['missing'][13])
assert len(missing)==len(set(missing))==13
w={'schema':'longrun-worker-return/v2','run_id':RUN,'work_order_id':'W005','order_ref':ORDER_REF,'worker':WORKER,'return_to':RETURN_TO,'outcome':'STOP','result_ref':pub['result_ref'],'missing':missing,'manifest':manifest}
assert w['result_ref']==published_by_path[str(ART/'WORKER_EXECUTION_REPORT.md')]['ref']
schema_path=AUTH/'observe-iterate/longrun/contracts/longrun_schema_v2.json'
schema=json.loads(schema_path.read_bytes())
worker_schema={'$defs':schema['$defs'],'$ref':'#/$defs/worker_return'}
Draft202012Validator.check_schema(worker_schema)
Draft202012Validator(worker_schema).validate(w)
Draft202012Validator({'$defs':schema['$defs'],'$ref':'#/$defs/order'}).validate(order)
assert safe_ref(w['order_ref'])[2]=='longrun/runs/'+RUN+'/work_orders/W005/ORDER.json'
assert w['worker']==order['worker'] and w['return_to']==order['issuer'] and w['return_to'].endswith(':executor:E1')
verified={e['ref']:e for e in pub['files']}
manifest_checks=[]
for key,item in manifest.items():
    assert set(item)=={'ref','sha256'} and item['ref'] in verified
    e=verified[item['ref']];f=fact(e['path']);b=Path(e['path']).read_bytes()
    assert f['sha256']==item['sha256']==e['sha256'] and f['bytes']==e['bytes']
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob']==e['remote_git_blob']
    safe_ref(item['ref']);assert item['ref'].startswith(REF_PREFIX+PREFIX)
    assert not item['ref'].endswith('/worker_results/W005/WORKER_RETURN.json')
    manifest_checks.append({'key':key,'ref':item['ref'],'sha256':item['sha256'],'path':e['path'],'verified_against_actual_published_receipt_and_local_bytes':True})
uncovered=sorted(set(order['deliverables'])-set(manifest))
assert set(uncovered)=={order['deliverables'][10],order['deliverables'][12]} and w['outcome']!='EXECUTED' and w['missing']

save('WORKER_RETURN.json',w)
assert json.loads((FINAL/'WORKER_RETURN.json').read_bytes())==w
Draft202012Validator(worker_schema).validate(json.loads((FINAL/'WORKER_RETURN.json').read_bytes()))

# Full native commands and file changes for this formal-return turn only; no reasoning/session copy.
assert SESSION.stat().st_size<25000000
completed={};changes={};context=None
for lineno,line in enumerate(SESSION.open(),1):
    j=json.loads(line);p=j.get('payload',{})
    if j.get('type')=='turn_context' and p.get('turn_id')==TURN:context={k:p.get(k) for k in ['turn_id','cwd','model','effort']}
    if j.get('type')!='event_msg' or not isinstance(p,dict) or p.get('turn_id')!=TURN or p.get('type')!='item_completed':continue
    item=p['item'];r={'native_session_source':str(SESSION),'native_session_line':lineno,'timestamp':j.get('timestamp'),'turn_id':TURN,'item':item}
    if item.get('type')=='CommandExecution':completed[item['id']]=r
    if item.get('type')=='FileChange':changes[item['id']]=r
assert context==pref['current_context']
current_command='PYTHONDONTWRITEBYTECODE=1 TMPDIR='+str(FINAL)+' /usr/bin/python3.12 -I -B '+str(FINAL/'generate_worker_return.py')
with (FINAL/'COMMAND_LOG.jsonl').open('x') as out:
    for r in completed.values():out.write(json.dumps({'record_type':'NATIVE_COMPLETED_COMMAND',**r},ensure_ascii=False)+'\n')
    for r in changes.values():out.write(json.dumps({'record_type':'NATIVE_FILE_CHANGE',**r},ensure_ascii=False)+'\n')
    out.write(json.dumps({'record_type':'FINAL_GENERATION_CURRENT_COMMAND','at':utc(),'pid':os.getpid(),'cwd':str(BASE),'shell_command':current_command,'sys_argv':sys.argv,'status':'RUNNING_AT_LOG_FREEZE','exit_code':None,'note':'完整本阶段命令与聚合输出截至此边界。本命令真实完成由执行器terminal result及平台原生completed事件证明；不虚构未发生终态。','HOME':os.environ['HOME'],'CODEX_HOME':os.environ['CODEX_HOME'],'TMPDIR':os.environ['TMPDIR'],'PYTHONDONTWRITEBYTECODE':os.environ['PYTHONDONTWRITEBYTECODE']},ensure_ascii=False)+'\n')
for line in (FINAL/'COMMAND_LOG.jsonl').open():json.loads(line)

original_after=[]
for path,before in original_before.items():
    after=fact(path);assert before==after
    original_after.append({'before':before,'after':after,'bytes_hash_mtime_inode_dev_unchanged':True})
old_files=[]
for parent,dirs,names in os.walk(ROOT,followlinks=False):
    if Path(parent)==ROOT:dirs[:]=[n for n in dirs if n!='final-return']
    for n in dirs:assert not (Path(parent)/n).is_symlink()
    for n in names:old_files.append(str(Path(parent)/n));assert len(old_files)<2000
assert set(old_files)==set(original_before)
lock_after=guard()
expected={'FINALIZE_PREFLIGHT.json','generate_worker_return.py','WORKER_RETURN.json','WORKER_RETURN_VALIDATION.json','COMMAND_LOG.jsonl'}
assert {p.name for p in FINAL.iterdir()}==expected-{'WORKER_RETURN_VALIDATION.json'}
validation={'schema':'local-worker-return-validation/v1','at':utc(),'status':'PASS_LOCAL_SCHEMA_IDENTITY_AND_TRANSPORT_CONSISTENCY_ONLY','full_gate_status':'NOT_RUN_AWAITING_TRUE_RETURN_PUBLICATION_AND_INDEPENDENT_RECEIPT','professional_acceptance_claimed':False,'business_or_parent_completion_claimed':False,'current_context':context,'write_root':str(FINAL),'HOME':os.environ['HOME'],'CODEX_HOME':os.environ['CODEX_HOME'],'HOME_CODEX_reset':False,'root_lock_before':lock_before,'root_lock_after':lock_after,'formal_worker_return':fact(FINAL/'WORKER_RETURN.json'),'official_schema':fact(schema_path),'official_schema_selection':'与Gate.validated相同：$defs原样 + $ref #/$defs/worker_return；未改schema文件。','official_gate_source_readonly':fact(AUTH/'observe-iterate/longrun/tools/longrun_gate.py'),'validator_module':fact(jsonschema.__file__),'validator_implementation':fact(inspect.getfile(Draft202012Validator)),'python_binary':fact('/usr/bin/python3.12'),'preflight':fact(FINAL/'FINALIZE_PREFLIGHT.json'),'generator_source':fact(__file__),'phase_command_log':fact(FINAL/'COMMAND_LOG.jsonl'),'command_log_closure':'当前生成命令完整输入已记录，exit/null为封存时真实状态；其后真实exit由执行器回执提供。不回写旧67原件。','native_completed_commands_exported':len(completed),'native_file_changes_exported':len(changes),'nonzero_readonly_commands_preserved':[{'id':r['item']['id'],'exit_code':r['item']['exit_code'],'note':'只读回执枚举曾假定外层FREEZE也有可选publication_target，KeyError保留于原生日志；随后明确核读该行并使用repo_path校验，无原件写入或工程重跑。'} for r in completed.values() if r['item']['exit_code']!=0],'checks':{'V2_schema':True,'original_W1_W005_C0013_order_and_E1_route':True,'outcome_STOP':True,'result_ref_is_published_report':True,'manifest_value_keys_only_ref_sha256':True,'all_manifest_refs_real_and_evidence_hashes_verified':True,'no_future_or_self_Return_ref':True,'substantive_missing_preserved':True,'resolved_67_publication_gap_updated':True,'formal_generation_gap_updated_to_pending_publication':True,'old67_frozen_bytes_hash_mtime_inode_dev_unchanged':True,'nanosecond_metadata_exact_python_comparison':True,'old67_only_read_no_new_network':True,'no_preparer_evaluator_R0_or_engineering_run':True},'published_commit':COMMIT,'published_receipt':fact(AUTH/'W005-published-refs.json'),'metadata_precision_correction':pub['metadata_precision_correction'],'original_unique_files':67,'original_total_bytes':1226532,'manifest_entries':len(manifest),'manifest_unique_real_refs':67,'manifest_literal_label_aliases':11,'manifest_item_checks':manifest_checks,'ORDER_literal_deliverable_mapping':label_records,'ORDER_literals_without_published_ref':uncovered,'missing_count':len(missing),'missing':missing,'substantive_fact_binding':{'stop_code':STOP,'local_FIOCLEX':'0x5451','local_constant_definitions_agree':True,'preparer_attempts':1,'preparer_exit':1,'failure':'Worker preparation assertion over both pre-policy success and post-policy EPERM historical W004 FIOCLEX lines','evaluator_attempts':0,'R0_A1_attempts':0,'W005_current_kernel_measurement':False,'kernel_unsupported_claim':False,'confinement_PASS_claim':False,'R0_B_C_entered':False,'eight_EP_constructed':False,'new_EP_SATISFIED':0,'old_SCENARIO04':'PARTIAL','SHARED03':'UNSATISFIED','other_six':'NOT_ATTEMPTED','scenario_normal_build_compile_serialization_current_material':0,'original_input_immutability_scope':'37具名输入；不外推全BASE/HOME或global zero writes。'},'original67_before_after':original_after,'new_files_for_controller_publication':[{'local_path':str(FINAL/n),'repo_path':'longrun/runs/'+RUN+'/worker_results/W005/'+n,'ref':None} for n in sorted(expected)],'remaining_steps':['主控逐字出版本阶段五个正式文件到worker_results/W005/，远端回读bytes/hash。','主控取得真实WORKER_RETURN ref及独立receipt后运行完整validate-worker-return/route-return，不能以本地schema一致性冒充完整Gate。','正式Return仅送原E1消费；E1/manager负责专业接受、G-RUN/H3与父任务决定。']}
save('WORKER_RETURN_VALIDATION.json',validation)
assert {p.name for p in FINAL.iterdir()}==expected
json.loads((FINAL/'WORKER_RETURN_VALIDATION.json').read_bytes())
for path,before in original_before.items():assert fact(path)==before
guard()
print(json.dumps({'outcome':'STOP','return_to':RETURN_TO,'manifest_entries':len(manifest),'unique_published_refs':67,'literal_label_aliases':11,'missing_count':len(missing),'local_schema_identity_transport_validation':'PASS','full_gate':'PENDING_CONTROLLER_TRUE_RETURN_REF_AND_INDEPENDENT_RECEIPT','old67_bytes_hash_mtime_inode_dev_unchanged':True,'all_new_files':[fact(FINAL/n) for n in sorted(expected)]},ensure_ascii=False,indent=2))
