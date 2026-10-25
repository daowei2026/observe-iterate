import os
"""逐K真实原表/自然切片/较早依赖/正常packet；不重算N。"""
from pathlib import Path
import csv,datetime,hashlib,io,json
import pandas as pd
import yaml
rt=Path(os.environ.get('BI01_W11_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker11-runtime'));built=json.loads((rt/'BUILT_RUNS.json').read_text())['cases'];records=[]
for c in built:
 run=Path(c['run_dir']);s=json.loads((run/'manifest/normal_node_behavior.json').read_text())
 folder=run/'formal_dependencies'/c['node_id'];index=json.loads((folder/'INDEX.json').read_text());ks=c['Ks']
 assert index['knowledge_ks']==ks and index['purpose']==c['purpose']
 primary=[k['knowledge_k'] for k in index['selections'] if k['role']=='primary'];assert primary==ks
 copies=[];shared={};paths=[];source_rows={}
 for cut in s['cuts']:
  k=cut['as_of'];entry=next(x for x in index['selections'] if x['knowledge_k']==k)
  assert entry['exact']==cut['expected_exact'] and entry['working_life']
  for table,source in cut['tables'].items():
   row=next(x for x in entry['original_tables'] if x['table']==table)
   payload=(folder/row['path']).read_bytes();assert payload==Path(source['path']).read_bytes()
   assert hashlib.sha256(payload).hexdigest()==row['sha256']==source['sha256']
   source_rows[source['sha256']]=list(csv.DictReader(io.StringIO(payload.decode())))
   paths.append(row['path']);shared.setdefault(source['sha256'],[]).append(dict(K=k,table=table))
   copies.append(dict(K=k,table=table,path=row['path'],sha256=row['sha256'],role=entry['role']))
 assert len(paths)==len(set(paths))
 brief=json.loads((run/'run_brief.json').read_text());formal=[a for a in brief['anchor_registry'] if a.get('source_role')=='formal']
 for k in index['selections']:
  refs=[a['knowledge_ref'] for a in formal if a.get('knowledge_ref',{}).get('knowledge_k')==k['knowledge_k']]
  assert refs and all(r['exact']==k['exact'] and r['working_life']==k['working_life'] and r['role']==k['role'] for r in refs)
 stats=pd.read_csv(run/'manifest/feature_slice_stats.csv');assert stats.slice_success.all() and stats.source_role.eq('formal').all()
 assert not stats.feature_key.str.contains('n_display').any() if 'feature_key' in stats else True
 qualified=pd.read_csv(folder/'qualified_price_calendar.csv');node_price=pd.read_csv(folder/'node_price_calendar.csv')
 assert int(qualified.open_uti.max())<=max(ks) and node_price.open_uti.between(*index['node_range']).all()
 if c['symbol']=='i':assert int(qualified.close.isna().sum())==24
 packet=run/'delivery/big_node_packets'/(c['node_id']+'_packet')
 packet_dep=packet/'10_NORMAL_N_FORMAL_DEPENDENCIES';assert (packet_dep/'INDEX.json').read_bytes()==(folder/'INDEX.json').read_bytes()
 for row in copies:assert (packet_dep/row['path']).read_bytes()==(folder/row['path']).read_bytes()
 fields=yaml.safe_load((packet/'06_FEATURE_CONFIGS_AND_FIELDS.yaml').read_text())
 slice_index=fields['slice_index'];assert slice_index
 refs=[json.loads(row['knowledge_ref']) for row in slice_index if isinstance(row.get('knowledge_ref'),str)]
 assert refs and all(r.get('role') in ('primary','reference','price_context') for r in refs)
 precise_ids=0
 for row in csv.DictReader((packet/'03_FEATURE_SLICES.csv').open()):
  raw=json.loads(row['raw_fields_json']);digest=raw.get('_csv_source_sha256')
  if digest not in source_rows:continue
  original=source_rows[digest][int(raw['_csv_source_row'])-2]
  for field,value in raw.items():
   if (field.endswith('_high') or field.endswith('_low')) and field in original and original[field]!='':
    assert not isinstance(value,float) and int(value)==int(original[field]),(c['case'],field,value,original[field])
    precise_ids+=1
 older=[]
 for k in index['selections']:
  for row in k['original_tables']:
   if row['stored_time_min'] and pd.Timestamp(row['stored_time_min'])<pd.Timestamp(index['node_natural_range'][0]):older.append(dict(K=k['knowledge_k'],table=row['table'],original_time=row['stored_time_min']))
 records.append(dict(case=c['case'],run_id=c['run_id'],node_id=c['node_id'],purpose=c['purpose'],knowledge_ks=ks,
   dependency_originals=copies,per_K_paths_unique=True,normal_packet_contains_originals=True,knowledge_ref_in_normal_slice_index=True,
   legal_empty_slices=int(stats.empty_slice_warning.sum()),older_dependencies_retained=older,
   exact_non_float_identity_fields_in_main_slices=precise_ids,
   byte_shared_bases=[dict(sha256=h,referenced_by=items) for h,items in shared.items() if len(items)>1],
   qualified_price_rows=len(qualified),node_price_rows=len(node_price),qualified_price_max=int(qualified.open_uti.max())))
result=dict(order_id='BI01-FO01-N-NORMAL-CONSUMER-11',actual_normal_cases=records,all_passed=True,
 qualification='正常隔离board/同node原件与逐K引用核验，不代表共享平台采用、工作3接收或正式工作4')
(rt/'FORMAL_DELIVERY_CHECK.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(cases=len(records),all_formal_originals_exact=True,normal_delivery_closed=True)))
