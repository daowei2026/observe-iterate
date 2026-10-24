from pathlib import Path
import contextlib,hashlib,json,traceback
import os
rt=Path(os.environ.get('BI01_W09_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker09-runtime'));rt.mkdir(parents=True,exist_ok=True)
result={}
with (rt/'cold-library.private.log').open('w') as log,contextlib.redirect_stdout(log),contextlib.redirect_stderr(log):
 try:
    import bootstrap
    from mquant.aidata.big_world_chart import AidataBigWorldReviewCAE
    from mquant.quant.models.graph import CaeNodeDao
    from mquant.aidata.u2_normal_node_behavior_display import write_html
    from mquant.aidata.api import render_review_nodes
    from mquant.aidata.contracts import build_run_handle
    from mquant.aidata.normal_node_behavior import display_selection
    from mquant.quant import OptContext
    from bokeh.models import GlyphRenderer
    payload=(rt/'PERSISTED_OPTIN.fason.private.txt').read_text()
    obj=CaeNodeDao.node2fao({'params':payload,'cls_name':'AidataBigWorldReviewCAE'})
    layout=obj.layout()
    write_html(layout,rt/'cold_rb_local.html',title='Worker09 cold normal CAE')
    result={'source':'separate cold process, actual persisted Fao input from previous producer',
        'serialized_sha256':hashlib.sha256(payload.encode()).hexdigest(),
        'fason_equal':obj.fason==payload,'keys':sorted(dict(obj.P)),
        'root_name':layout.name,'root_tags':layout.tags,'glyphs':len(list(layout.select({'type':GlyphRenderer}))),
        'dao_writes':False,'shared_service_adoption':False}
    run=build_run_handle(Path('/dwdhome/fy/observe-iterate-bi01-fo-01/artifacts/bi01-worker07-runs/BI01-FO01-W07-20261024T0028-i'))
    rbi=dict(context=OptContext(sof_name='TA_updto20240229_DBA'),blk='i',calendar_override='night_end_at_2300',
        generation_depth='big',evidence_features=[display_selection(run.run_dir)])
    rendered=render_review_nodes(run,node_ids=['big_000001'],run_brief_input=rbi,export_plot_view_data=False)
    write_html(rendered.rendered_objects[0],rt/'bridge_i_recovery.html',title='Worker09 actual render_review_nodes')
    result['bridge']={'actual_called':True,'plans':rendered.render_plans,
        'root_name':rendered.rendered_objects[0].name,'root_tags':rendered.rendered_objects[0].tags}
 except Exception as exc:
    traceback.print_exc();result['error_type']=type(exc).__name__;result['error']=str(exc)[:400]
(rt/'COLD_RESTORE_AND_BRIDGE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,default=lambda v:v.item() if hasattr(v,'item') else str(v))+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['root_tags','bridge']},ensure_ascii=False))
raise SystemExit(1 if 'error_type' in result else 0)
