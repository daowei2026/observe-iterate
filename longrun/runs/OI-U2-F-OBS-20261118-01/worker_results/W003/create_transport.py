from pathlib import Path
import hashlib,json
run=Path(__file__).resolve().parent; run_id='OI-U2-F-OBS-20261118-01'; work='W003'
excluded={'MANIFEST.local.json','TRANSPORT_PAYLOAD.json','SHA256SUMS','WORKER_RETURN.json','WORKER_RETURN.validation.json'}
files=[path for path in sorted(run.iterdir()) if path.is_file() and path.name not in excluded]
files += [path for path in sorted((run/'logs').iterdir()) if path.is_file() and path.name!='task_status_cli.log']
for directory in ('inputs','diagnostics'):
 files += [path for path in sorted((run/directory).rglob('*')) if path.is_file()]
files.append(run/'output/u2_f_caegraph/definition_run_report.json')
sources=json.loads((run/'source_hashes.json').read_bytes()); source_lookup={value['path']:value for value in sources.values()}
files += [Path(value['path']) for value in sources.values()]
assert len(files)==len(set(files))
entries=[]; bodies=[]
for path in files:
 assert path.resolve().is_relative_to(run.resolve())
 raw=path.read_bytes(); body=raw.decode('utf8'); assert body.encode('utf8')==raw
 relative=str(path.relative_to(run)); original=source_lookup.get(str(path))
 item={'relative_path':relative,'local_path':str(path),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'existing_ref':original['ref'] if original else None,'suggested_publication_path':None if original else f'longrun/runs/{run_id}/worker_results/{work}/'+relative}
 entries.append(item); bodies.append({**item,'body_utf8':body})
manifest={'format':'local evidence manifest; publication refs not yet assigned','run_id':run_id,'work_order_id':work,'parent_delegation_id':'D005','worker':f'codex:{run_id}:worker:W1','return_to':f'chatgpt:{run_id}:executor:E1','factual_status':'BLOCKED','proposed_outcome_after_publication':'STOP','formal_worker_return_signed':False,'D_attempt_count':1,'D_exit_code':1,'entries':entries,'next_action':'主控按原字节发布并提供真实 refs；Worker 在同一 W003 下核哈希并签认正式 worker_return，不重跑 D。'}
manifest_raw=(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode('utf8')
with (run/'MANIFEST.local.json').open('xb') as stream:stream.write(manifest_raw)
bodies.append({'relative_path':'MANIFEST.local.json','local_path':str(run/'MANIFEST.local.json'),'bytes':len(manifest_raw),'sha256':hashlib.sha256(manifest_raw).hexdigest(),'existing_ref':None,'suggested_publication_path':f'longrun/runs/{run_id}/worker_results/{work}/MANIFEST.local.json','body_utf8':manifest_raw.decode('utf8')})
payload={'format':'UTF-8 exact-body transport package; not a formal Worker Return','run_id':run_id,'work_order_id':work,'parent_delegation_id':'D005','worker':f'codex:{run_id}:worker:W1','return_to':f'chatgpt:{run_id}:executor:E1','all_bodies_are_complete':True,'files':bodies}
payload_raw=(json.dumps(payload,ensure_ascii=False,indent=2)+'\n').encode('utf8')
with (run/'TRANSPORT_PAYLOAD.json').open('xb') as stream:stream.write(payload_raw)
readback=json.loads((run/'TRANSPORT_PAYLOAD.json').read_bytes())
for item in readback['files']:
 raw=item['body_utf8'].encode('utf8'); assert len(raw)==item['bytes']; assert hashlib.sha256(raw).hexdigest()==item['sha256']; assert Path(item['local_path']).read_bytes()==raw
checks=json.loads((run/'evidence_checks.json').read_bytes()); assert all(checks.values())
assert not (run/'WORKER_RETURN.json').exists()
lines=[item['sha256']+'  '+item['relative_path'] for item in bodies]
lines.append(hashlib.sha256(payload_raw).hexdigest()+'  TRANSPORT_PAYLOAD.json')
with (run/'SHA256SUMS').open('x') as stream:stream.write('\n'.join(lines)+'\n')
print('EVIDENCE_CHECKS_PASSED='+str(len(checks)))
print('COMPLETE_TEXT_BODIES='+str(len(bodies)))
print('NEW_EVIDENCE_BODIES='+str(sum(item['existing_ref'] is None for item in bodies)))
for name in ('FACT_REPORT.md','MANIFEST.local.json','TRANSPORT_PAYLOAD.json','SHA256SUMS'):
 raw=(run/name).read_bytes(); print(json.dumps({'path':str(run/name),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()},ensure_ascii=False))
