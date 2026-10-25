import os
"""最终候选下有据复用正确core，只更新正常board元信息/交付，不重定位。"""
from pathlib import Path
import contextlib,hashlib,json,subprocess,traceback
rt=Path(os.environ.get('BI01_W11_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker11-runtime'));result={'public_board_called':True,'reuse_core':True,'chart_relocated':False,'DAO_writes':False}
try:
 with (rt/'refresh-formal.private.log').open('w') as f,contextlib.redirect_stdout(f),contextlib.redirect_stderr(f):
  import bootstrap,pandas as pd
  from mquant.aidata.api import build_board_run
  from mquant.aidata.contracts import build_run_handle
  from mquant.aidata.normal_node_behavior import display_selection
  from mquant.quant import OptContext
  built=json.loads((rt/'BUILT_RUNS.json').read_text())['cases'];rows=[]
  for c in built:
   run=build_run_handle(Path(c['run_dir']));before=run.timespan_index_path.read_bytes();span=pd.read_csv(run.timespan_index_path).iloc[0]
   rbi=dict(output_root=str(run.output_root),run_id=run.run_id,context=OptContext(sof_name='TA_updto20240229_DBA'),blk=c['symbol'],
      calendar_override='night_end_at_2300',generation_depth='big',
      big_source=dict(mode='manual',timespans=[dict(start_uti=int(span.start_uti),end_uti=int(span.end_uti),start_ts=str(span.start_ts),end_ts=str(span.end_ts),label=str(span.label))]),
      evidence_features=[display_selection(run.run_dir)],run_note='Worker11最终隔离候选，复用正确冻结core补齐逐K正式来源元信息/交付，非平台发布')
   board=build_board_run(rbi,reuse_core=True,dry_run=False)
   assert board.timespan_index_path.read_bytes()==before
   stats=pd.read_csv(board.feature_slice_stats_path)
   index=json.loads((board.run_dir/'formal_dependencies'/c['node_id']/'INDEX.json').read_text())
   assert all('working_life' in k for k in index['selections'])
   rows.append(dict(case=c['case'],run_id=c['run_id'],node_id=c['node_id'],correct_frozen_core_sha256=hashlib.sha256(before).hexdigest(),
     core_byte_unchanged=True,formal_slice_stats_rows=len(stats),all_slice_success=bool(stats.slice_success.all()),
     knowledge_ref_in_all_stats=bool(stats.knowledge_ref.notna().all()),explicit_working_Life_in_dependency=True))
   (rt/'FORMAL_REFRESH_PARTIAL.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
  result.update(actual_aidata_head=subprocess.check_output(['git','-C',str(bootstrap.candidate),'rev-parse','HEAD'],text=True).strip(),cases=rows,complete=True)
except Exception as exc:
 with (rt/'refresh-formal-error.private.log').open('w') as f:traceback.print_exc(file=f)
 result.update(error_type=type(exc).__name__,complete=False)
(rt/'FORMAL_REFRESH.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='cases'},ensure_ascii=False));raise SystemExit(0 if result['complete'] else 1)
