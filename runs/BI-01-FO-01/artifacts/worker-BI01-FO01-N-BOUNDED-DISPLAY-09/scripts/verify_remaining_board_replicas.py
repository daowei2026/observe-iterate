"""补核rb/hc同冻结core的正式/显示角色；只写自有隔离副本，不注册图。"""
from pathlib import Path
import contextlib,hashlib,json,shutil,traceback
import os
rt=Path(os.environ.get('BI01_W09_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker09-runtime'));rt.mkdir(parents=True,exist_ok=True)
results=[]
with (rt/'board-rb-hc.private.log').open('w') as log,contextlib.redirect_stdout(log),contextlib.redirect_stderr(log):
 import bootstrap,pandas as pd
 from mquant.aidata.api import build_chart_run,build_board_run
 from mquant.aidata.normal_node_behavior import display_selection
 from mquant.quant import OptContext
 for symbol in ('rb','hc'):
  result={'symbol':symbol,'qualification':'同原run/node隔离工程副本；非新业务Run/平台发布'}
  try:
   original=Path('/dwdhome/fy/observe-iterate-bi01-fo-01/artifacts/bi01-worker07-runs')/('BI01-FO01-W07-20261024T0028-'+symbol)
   replica=rt/'core-validation-replica'/original.name
   (replica/'manifest').mkdir(parents=True,exist_ok=True)
   before={n:hashlib.sha256((original/'manifest'/n).read_bytes()).hexdigest() for n in ('timespan_index.csv','chart_manifest.csv','normal_node_behavior.json')}
   for name in before:shutil.copy2(original/'manifest'/name,replica/'manifest'/name)
   spans=pd.read_csv(replica/'manifest/timespan_index.csv')
   rbi=dict(output_root=str(replica.parent),run_id=original.name,context=OptContext(sof_name='TA_updto20240229_DBA'),
       blk=symbol,calendar_override='night_end_at_2300',generation_depth='big',
       big_source={'mode':'manual','timespans':spans[['start_uti','end_uti','start_ts','end_ts','label']].to_dict('records')},
       evidence_features=[display_selection(original)],run_note='Worker09 same frozen core isolated verification replica')
   chart=build_chart_run(rbi,reuse_core=True,dry_run=False)
   board=build_board_run(rbi,reuse_core=True,dry_run=False)
   stats=pd.read_csv(board.feature_slice_stats_path)
   assert stats.slice_success.all() and stats.source_role.eq('formal').all() and stats.selection_ref.notna().all()
   nodes=[]
   for node in spans.node_id:
    index_path=replica/'formal_dependencies'/node/'INDEX.json';index=json.loads(index_path.read_text())
    for row in index['original_tables']:
     data=(index_path.parent/row['path']).read_bytes()
     assert hashlib.sha256(data).hexdigest()==row['sha256']
    nodes.append({'node_id':node,'original_tables':len(index['original_tables']),'index_sha256':hashlib.sha256(index_path.read_bytes()).hexdigest(),
        'source_tables':[{'table':x['table'],'sha256':x['sha256'],'rows':x['rows'],'stored_time_min':x.get('stored_time_min'),'source':x['source']} for x in index['original_tables']]})
   assert all(hashlib.sha256((original/'manifest'/n).read_bytes()).hexdigest()==value for n,value in before.items())
   result.update(run_id=original.name,core_sha256=before,core_unchanged=True,public_chart_called=True,public_board_called=True,
       all_formal_slices_success=True,display_in_formal_slices=False,formal_slice_rows=len(stats),nodes=nodes,
       delivery_manifest_sha256=hashlib.sha256(board.delivery_manifest_path.read_bytes()).hexdigest(),normal_platform_registration=False)
  except Exception as exc:
   traceback.print_exc();result.update(error_type=type(exc).__name__)
  results.append(result)
(rt/'RB_HC_BOARD_REPLICAS.json').write_text(json.dumps({'results':results},ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{k:v for k,v in r.items() if k not in ('nodes','core_sha256')} for r in results],ensure_ascii=False))
raise SystemExit(1 if any('error_type' in r for r in results) else 0)
