"""封存本 W 本地交付；不发布、不生成正式 Return、不读业务源数据。"""
import os, sys, pathlib, json, hashlib, datetime, shlex

W=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(W))
import runner
RUN='OI-EAW-WALL-20261114-01'
PREFIX='longrun/runs/'+RUN+'/worker_results/W001/'
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,obj):
    with p.open('x') as f:json.dump(obj,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def strict(p):return json.loads(p.read_text(),parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))

runner.guard()
started=utc()
assert not (W/'HASHES.sha256').exists() and not (W/'PUBLICATION_MANIFEST.json').exists()
assert not (W/'WORKER_RETURN.json').exists()
with (W/'COMMAND_LOG.txt').open('a') as f:
    f.write('\nFINAL_SEAL_COMMAND '+shlex.join([sys.executable,'-B',str(pathlib.Path(__file__).resolve())])+
            '\nSTART_UTC '+started+'\nCWD '+str(pathlib.Path.cwd())+'\n')
required=['WORKER_EXECUTION_REPORT.md','WORKSPACE_BINDING.json','CODE_AND_READER_ENTRYPOINTS.md',
          'ASSET_INVENTORY.json','COMMAND_LOG.txt','SAMPLE_CHAIN.jsonl','SAMPLE_CHAIN_README.md',
          'ACTION_PREFLIGHT_FACTS.md','WORKER_RETURN_PREPARATION.json','VALIDATION_REPORT.json']
for name in required:assert (W/name).is_file() and (W/name).stat().st_size>0
prep=strict(W/'WORKER_RETURN_PREPARATION.json')
assert prep['return_to']=='chatgpt:'+RUN+':executor:E1' and prep['result_ref'] is None and prep['outcome']=='PARTIAL'
assert len([json.loads(x) for x in (W/'SAMPLE_CHAIN.jsonl').open()])==3
assert strict(W/'WORKSPACE_BINDING.json')['final_readonly_audit']['all_relevant_heads_and_statuses_unchanged']
assert strict(W/'evidence/CHAIN_RECONCILIATION_VALIDATION.json')['checks']
for p in W.rglob('*'):assert not p.is_symlink() and p.resolve().is_relative_to(W)
assert not list(W.rglob('__pycache__'))
runner.guard()
terminal=strict(W/'artifacts/task-status/tasks/w001-local/snapshot.json')
assert terminal['status']=='completed' and terminal['progress']['completed_steps']==3
ended=utc()
# This receipt measures the sealer validation interval. The final tool result is
# the independent observer of the actual shell exit, after index hashing below.
receipt={'command':[sys.executable,'-B',str(pathlib.Path(__file__).resolve())],
         'cwd':str(pathlib.Path.cwd()),'started_at_utc':started,
         'validation_finished_at_utc':ended,'shell_exit_code':None,
         'shell_exit_code_reason':'Self-logger cannot observe its own process exit; actual exit code is independently returned by the exec tool after sealing.',
         'validation_passed':True,'final_index_check':'All HASHES entries will be recomputed and checked in memory before returning 0.'}
put(W/'evidence/FINAL_SEAL_COMMAND.json',receipt)
with (W/'COMMAND_LOG.txt').open('a') as f:
    f.write('VALIDATION_END_UTC '+ended+'\nVALIDATION_EXIT_CODE 0\n'+
            'SHELL_EXIT_CODE independent exec tool result (not fabricated by self-logger)\n'+
            'OUTPUT_SUMMARY core artifacts/strict JSON/physical reconciliation/local ledger passed; '+
            'PUBLICATION_MANIFEST.json and HASHES.sha256 are the final sealing outputs; sha256 values and index verification returned by the tool.\n')
files=sorted(p for p in W.rglob('*') if p.is_file() and p.name not in ('PUBLICATION_MANIFEST.json','HASHES.sha256'))
entries=[]
for p in files:
    rel=p.relative_to(W).as_posix()
    entries.append({'relative_path':rel,'absolute_local_path':str(p),'bytes':p.stat().st_size,'sha256':digest(p),
                    'publication_target':PREFIX+rel,'ref':None,
                    'ref_reason':'Actual publication commit does not exist in this local phase; controller supplies real pinned ref after byte-preserving publication.'})
mapping={}
for title,names in {
 'execution_report':['WORKER_EXECUTION_REPORT.md'],
 'workspace_binding':['WORKSPACE_BINDING.json'],
 'code_and_reader_entrypoints':['CODE_AND_READER_ENTRYPOINTS.md'],
 'asset_inventory':['ASSET_INVENTORY.json'],
 'command_log':['COMMAND_LOG.txt'],
 'real_sample_chain':['SAMPLE_CHAIN.jsonl','SAMPLE_CHAIN_README.md'],
 'action_preflight':['ACTION_PREFLIGHT_FACTS.md'],
 'return_preparation':['WORKER_RETURN_PREPARATION.json'],
 'validation':['VALIDATION_REPORT.json','evidence/CHAIN_RECONCILIATION_VALIDATION.json']}.items():
    mapping[title]=[{k:v for k,v in next(e for e in entries if e['relative_path']==name).items()} for name in names]
manifest={'schema':'w001-local-publication-manifest/v1','run_id':RUN,'work_order_id':'W001',
          'phase':'LOCAL_ARTIFACT_HANDOFF_ONLY','outcome':'PARTIAL',
          'return_to':'chatgpt:'+RUN+':executor:E1','github_write_performed':False,
          'repository':'daowei2026/observe-iterate','approved_branch':'runs/'+RUN,
          'publication_prefix':PREFIX,'publication_commit':None,
          'publication_commit_reason':'Controller publishes first; exact commit is not fabricated.',
          'result_ref':None,'result_ref_reason':'Pending actual publication commit for WORKER_EXECUTION_REPORT.md',
          'deliverable_mapping':mapping,'files':entries,
          'integrity_index':{'absolute_local_path':str(W/'HASHES.sha256'),'publication_target':PREFIX+'HASHES.sha256',
             'sha256':None,'sha256_reason':'Self-referential integrity index is created after this manifest; its actual digest is returned by the final sealing tool and final handoff.',
             'coverage':'HASHES.sha256 covers every regular file in W001 except HASHES.sha256 itself, including this manifest.'},
          'manifest_self':{'absolute_local_path':str(W/'PUBLICATION_MANIFEST.json'),'publication_target':PREFIX+'PUBLICATION_MANIFEST.json',
             'sha256':None,'sha256_reason':'Self hash omitted to avoid circularity; actual digest appears in HASHES.sha256 and final handoff.'},
          'formal_worker_return':{'absolute_local_path':str(W/'WORKER_RETURN.json'),'exists':False,
             'reason':'Original W1 generates only after controller sends real refs/sha256 for published evidence; not part of the local stage.'},
          'raw_large_market_assets_copied':False,
          'transport_instruction':'Copy each files[] exact byte body to publication_target preserving relative paths; also publish PUBLICATION_MANIFEST.json and HASHES.sha256 at their explicit targets. Recompute local sha256 and compare HASHES. Return actual 40-hex commit, exact refs and sha256 to original W1. No editing, fabricated refs or manager return.',
          'completion_limit':'Only local originals delivered. W001/D001/parent business completion and professional acceptance are not claimed.'}
put(W/'PUBLICATION_MANIFEST.json',manifest)
allfiles=sorted(p for p in W.rglob('*') if p.is_file() and p.name!='HASHES.sha256')
hashlines=[digest(p)+'  '+p.relative_to(W).as_posix() for p in allfiles]
with (W/'HASHES.sha256').open('x') as f:f.write('\n'.join(hashlines)+'\n')
for p,line in zip(allfiles,hashlines):assert digest(p)==line[:64]
for e in entries:assert digest(pathlib.Path(e['absolute_local_path']))==e['sha256']
for p in W.rglob('*.json'):strict(p)
report={'local_stage_complete':True,'outcome':'PARTIAL','github_publication_performed':False,
        'formal_worker_return_generated':False,'file_count_including_integrity_index':len(allfiles)+1,
        'hashed_files':len(hashlines),'hash_verification':'ALL_PASS',
        'local_root':str(W),'publication_target':'daowei2026/observe-iterate:runs/'+RUN+':'+PREFIX,
        'PUBLICATION_MANIFEST.json':{'absolute_path':str(W/'PUBLICATION_MANIFEST.json'),'sha256':digest(W/'PUBLICATION_MANIFEST.json')},
        'HASHES.sha256':{'absolute_path':str(W/'HASHES.sha256'),'sha256':digest(W/'HASHES.sha256')},
        'core_deliverables':{name:{'absolute_path':str(W/name),'sha256':digest(W/name)} for name in required},
        'seal_finished_utc':utc(),
        'next_step':'Controller byte-preserving publication, then original W1 generates final longrun-worker-return/v2 back to E1 using actual refs.'}
print(json.dumps(report,ensure_ascii=False,indent=2))
