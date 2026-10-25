import os
"""独立进程正常Fao冷恢复/普通CAE及公开bridge；无DAO/服务写入。"""
from pathlib import Path
import contextlib,hashlib,json,traceback
rt=Path(os.environ.get('BI01_W11_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker11-runtime'));result={'DAO_writes':False,'normal_platform_registration':False}
def clean(v):
 import numpy as np,pandas as pd
 if isinstance(v,dict):return {str(k):clean(x) for k,x in v.items()}
 if isinstance(v,(list,tuple,pd.Series,pd.Index,np.ndarray)):return [clean(x) for x in v]
 if isinstance(v,np.generic):return clean(v.item())
 if v is pd.NA or v is pd.NaT:return None
 if isinstance(v,float) and not np.isfinite(v):return None
 if isinstance(v,(Path,pd.Timestamp)):return str(v)
 return v
try:
 with (rt/'cold-consumers.private.log').open('w') as f,contextlib.redirect_stdout(f),contextlib.redirect_stderr(f):
  import bootstrap
  from mquant.quant.models.graph import CaeNodeDao
  from mquant.aidata.big_world_chart import AidataBigWorldReviewCAE
  from mquant.aidata.normal_node_behavior import display_selection
  from mquant.aidata.contracts import build_run_handle
  from mquant.aidata.api import render_review_nodes
  from mquant.quant import OptContext
  from bokeh.models import GlyphRenderer
  built=json.loads((rt/'BUILT_RUNS.json').read_text())['cases'];rows=[]
  for case in built:
   payload=Path(case['fason_private_path']).read_text()
   obj=CaeNodeDao.node2fao({'params':payload,'cls_name':'AidataBigWorldReviewCAE'})
   assert obj.fason==payload and obj.ppid==case['ppid']
   layout=obj.layout()
   row=dict(case=case['case'],run_id=case['run_id'],node_id=case['node_id'],Ks=case['Ks'],
     cold_fason_equal=True,cold_ppid_equal=True,parameter_keys=sorted(dict(obj.P)),root_name=layout.name,
     glyphs=len(list(layout.select({'type':GlyphRenderer}))),
     scalar_ranges=[{'title':p.title.text,'x':[p.x_range.start,p.x_range.end],'y':[p.y_range.start,p.y_range.end]}
       for p in layout.references() if 'aidata_bounded_panel' in getattr(p,'tags',[]) and 'panel:price' not in p.tags],
     identity=layout.tags)
   rows.append(row);(rt/'COLD_CONSUMER_PARTIAL.json').write_text(json.dumps(clean(rows),ensure_ascii=False,indent=2)+'\n')
  # 另核公开bridge确实经过同一个普通CAE，不调用平台注册factory。
  bridges=[]
  for name in ('rb_comparison','i_query_i_after_recovery'):
   case=next(c for c in built if c['case']==name);run=build_run_handle(Path(case['run_dir']))
   rbi=dict(context=OptContext(sof_name='TA_updto20240229_DBA'),blk=case['symbol'],calendar_override='night_end_at_2300',
     generation_depth='big',evidence_features=[display_selection(run.run_dir)])
   rendered=render_review_nodes(run,node_ids=[case['node_id']],run_brief_input=rbi,export_plot_view_data=False)
   bridges.append(dict(case=name,actual_public_bridge_called=True,plans=rendered.render_plans,
     root_name=rendered.rendered_objects[0].name,root_tags=rendered.rendered_objects[0].tags))
  result.update(cases=rows,bridges=bridges,complete=True)
except Exception as exc:
 with (rt/'cold-error.private.log').open('w') as f:traceback.print_exc(file=f)
 result.update(error_type=type(exc).__name__,complete=False)
(rt/'COLD_CONSUMERS.json').write_text(json.dumps(clean(result),ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('cases','bridges')},ensure_ascii=False));raise SystemExit(0 if result['complete'] else 1)
