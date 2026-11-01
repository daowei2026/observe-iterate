"""封装逐文件receipt；不运行特征，不修改旧包。"""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,sys
ROOT=Path(__file__).resolve().parents[1]
EXCLUDE={'PACKAGE_RECEIPT.json','SHA256SUMS'}

def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
 return h.hexdigest()

def files():
 for p in sorted(ROOT.rglob('*')):
  rel=p.relative_to(ROOT)
  if '.runtime' in rel.parts:continue
  assert not p.is_symlink(),str(rel)
  if p.is_file():yield p

def metadata(p):
 result={'rows':None,'first_business_time':None,'last_business_time':None,'business_time_field':None}
 if p.suffix=='.csv':
  with p.open(newline='',encoding='utf-8-sig') as f:
   reader=csv.DictReader(f);cols=reader.fieldnames or [];rows=list(reader)
  result['rows']=len(rows);key=next((k for k in ['replay_event_ts','event_ts','closeTs','start_ts'] if k in cols),None)
  if key:
   times=[r[key] for r in rows if r.get(key)]
   result.update(business_time_field=key,first_business_time=min(times) if times else None,last_business_time=max(times) if times else None)
 return result

def main():
 now=datetime.now(timezone.utc).isoformat();m=json.loads((ROOT/'REPLAY_MANIFEST.json').read_text());rid=m['replay_run_id']
 source=json.loads((ROOT/'SOURCE_SNAPSHOT.json').read_text())
 mapped={r.get('path'):r['source_path'] for r in source['files'] if r.get('path')}
 for r in source.get('supporting_references',[]):mapped[r['path']]=r['source_path']
 reader=json.loads((ROOT/'READER_DEPENDENCY_SNAPSHOT.json').read_text())
 for r in reader['files']:
  if r.get('frozen_path'):mapped[r['frozen_path']]=r['source_path']
 versions={str(p.relative_to(ROOT)):sha(p) for p in (ROOT/'scripts').glob('*.py')}
 records=[]
 for p in files():
  rel=p.relative_to(ROOT).as_posix()
  if rel in EXCLUDE:continue
  kind='wrapper_only_instrumentation';origin='本工单真实调用、日志、只读整理或独立校验'
  source_run=rid
  if rel.startswith('copied/baseline/'):
   kind='copied';source_run='GTQH_C001_three_turns_20261101_162005'
   origin='daowei2026/observe-iterate@dfdf843b47c03c0121fd7151b72f24adb5d986c0:runs/BI-01-CO-04/artifacts/worker-BI01CO04-INPUT-RECOVERY-01/'+rel[len('copied/baseline/'):]
  elif rel.startswith('frozen/'):
   kind='copied' if rel in mapped else 'wrapper_only_instrumentation';origin=mapped.get(rel,'本工单wrapper或已记录原入口的wrapper副本')
  elif rel.startswith('execution/cache/') and '/KLine/' not in rel:
   kind='recomputed_feature_output';origin='原E成功调用：NATIVE_PREFIX_ROUTE_EXECUTION/OBSERVER_CAPABILITY_EXECUTION/MATRIX_EXECUTION_RECEIPTS'
  elif rel.startswith('recomputed/') or rel=='RECOMPUTED_OBJECT_ROWS.csv':
   kind='recomputed_feature_output';origin='execution/cache/ 原E真实结果；经冻结原Int/Double ADT reader读回'
  elif rel.startswith('execution/tmp/'):
   kind='wrapper_only_instrumentation';origin='原E根据未修改T1FisSystem参数生成的owned FIS临时配置'
  else:origin=mapped.get(rel,origin)
  record={'path':rel,'source_path':origin,'sha256':sha(p),'bytes':p.stat().st_size,**metadata(p),
   'generated_at':now,'generated_at_semantics':'本次封装时刻，实际原生调用时间见对应execution receipts',
   'tool':'seal_package.py / recorded native engine / ADT reader','version':versions,
   'classification':kind,'source_run_id':source_run,'replay_run_id':rid,
   'verification_status':'BYTES_SEALED_B_EXIT_STRUCTURE_VERIFIED_NOT_ASOF_QUALIFIED'}
  records.append(record)
 counts={k:sum(r['classification']==k for r in records) for k in ['copied','wrapper_only_instrumentation','recomputed_feature_output']}
 receipt={'schema':'bi01-asof-replay-receipt/v1','order_id':m['order_id'],'work_id':'BI-01','run_id':'BI-01-CO-04',
  'replay_run_id':rid,'exit':'BLOCKED_NO_LOOKAHEAD_PROOF','generated_at':now,'file_count':len(records),
  'total_bytes_excluding_envelope':sum(r['bytes'] for r in records),'classification_counts':counts,
  'native_process_invocations':9,'successful_native_computations':7,
  'self_reference_exclusion':{'paths':sorted(EXCLUDE),'reason':'receipt由SHA256SUMS固定；seal本身由Git blob/commit固定'},'files':records}
 (ROOT/'PACKAGE_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
 (ROOT/'SHA256SUMS').write_text('\n'.join(sha(p)+'  '+p.relative_to(ROOT).as_posix() for p in files() if p.relative_to(ROOT).as_posix()!='SHA256SUMS')+'\n')
 print(json.dumps({'sealed_files':len(records),'outer_entries':len(records)+1,'bytes':receipt['total_bytes_excluding_envelope'],'classification_counts':counts},ensure_ascii=False))

if __name__=='__main__':main()
