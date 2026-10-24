"""同K/同价窗不同optional panels的实际组合；隔离技术回归，不扩平台认可。"""
from pathlib import Path
import contextlib,json
import os
rt=Path(os.environ.get('BI01_W09_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker09-runtime'));rt.mkdir(parents=True,exist_ok=True)
result={}
with (rt/'optional-identity.private.log').open('w') as log,contextlib.redirect_stdout(log),contextlib.redirect_stderr(log):
 import bootstrap
 from mquant.aidata.normal_node_behavior import read_frame,display_selection,resolve_selection_evidence
 from mquant.aidata.u2_normal_node_behavior_display import build_selected_cut_bundle,build_uplot_layout,U2NormalNodeBehaviorDisplayFeature
 from mquant.quant import OptContext
 run=Path('/dwdhome/fy/observe-iterate-bi01-fo-01/artifacts/bi01-worker07-runs/BI01-FO01-W07-20261024T0028-i')
 selection=json.loads((run/'manifest/normal_node_behavior.json').read_text())
 frames={name:read_frame(spec) for name,spec in selection['tables'].items()}
 price=read_frame(selection['price'],formal=False);rows=[]
 for panels in [(),('duration',),('duration','rhythm','waiting_time')]:
  b=build_selected_cut_bundle(frames,price,symbol='i',color=selection['color'],as_of=selection['as_of'],
      display_range=(35339400,35361000),optional_panels=panels)
  root=build_uplot_layout(b,context=OptContext(sof_name='TA_updto20240229_DBA'),calendar_name='night_end_at_2300')
  rows.append({'optional_panels':list(panels),'K':b.meta['selected_k'],'exact':b.meta['source_exact'],
      'ppid':U2NormalNodeBehaviorDisplayFeature(b).ppid,'root_tags':root.tags,
      'actual_panels':sorted(f.title.text for f in root.references() if hasattr(f,'x_range') and hasattr(f,'renderers')),
      'progress':b.views['working_progress_points'].y.tolist()})
 assert len({r['ppid'] for r in rows})==3
 assert len({r['K'] for r in rows})==1 and len({r['exact'] for r in rows})==1
 assert all(r['progress']==[12] for r in rows)
 failures=[]
 for key,value in [('configuration_version','not-adopted'),('selection_sha256','0'*64)]:
  descriptor=display_selection(run);descriptor['prepared_display'][key]=value
  try:resolve_selection_evidence(descriptor)
  except ValueError as exc:failures.append({'field':key,'error_type':type(exc).__name__,'message':str(exc)})
  else:raise AssertionError('invalid descriptor accepted')
 result={'qualification':'相同真实源/K/价窗的隔离可选面板技术验证，非新增平台用途或业务图接收',
     'results':rows,'identities_distinct':True,'actual_invalid_descriptor_rejections':failures,'dao_writes':False}
(rt/'OPTIONAL_IDENTITY_CHECK.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'identities_distinct':True,'cases':len(rows),'invalid_descriptors_rejected':len(failures)}))
