"""独立核对固定正式原表、实际图用CSV和实际Notebook浏览器CDS。"""
from pathlib import Path
from functools import lru_cache
import hashlib,io,json,math,subprocess
from uuid import UUID
import pandas as pd

OUT=Path(__file__).resolve().parents[1]
REPO=OUT.parents[3]
PLAN=json.loads((OUT/'DISPLAY_PLAN.json').read_text())
EXECUTION=json.loads((OUT/'evidence/EXECUTION_RUNTIME.json').read_text())['execution_id']
W02='runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-DISPLAY-INTEGRATION-02/'
W03='runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-READABILITY-CROSSK-03/'
checks=[]
def check(name,condition,actual=None):
    checks.append({'check':name,'pass':bool(condition),'actual':actual})
def near(a,b):
    if isinstance(a,float) and not math.isfinite(a):a=None
    if isinstance(b,float) and not math.isfinite(b):b=None
    return a==b if a is None or b is None else math.isclose(float(a),float(b),rel_tol=1e-10,abs_tol=1e-10)
@lru_cache(None)
def raw(ref,path):return subprocess.check_output(['git','-C',str(REPO),'show',f'{ref}:{path}'])
def table(ref,folder,name):return pd.read_csv(io.BytesIO(raw(ref,folder+name+'.csv')),dtype='string')
def root_rows(frame,root):
    answer=frame
    for k in ('timestamp','occurrence','record_id'):
        answer=answer[answer[k].eq(root[k])]
    return answer
def one(frame,label):
    assert len(frame)==1,(label,len(frame))
    return frame.iloc[0]
def expected(ref,folder,K):
    origin=one(table(ref,folder,'origins').query('as_of == @k',local_dict={'k':str(K)}),'origin')
    row=one(root_rows(table(ref,folder,'rows'),origin),'row')
    window=one(table(ref,folder,'windows').query('address == @w',local_dict={'w':row['window']}),'window')
    binding=one(table(ref,folder,'bindings').query('address == @b',local_dict={'b':window['binding']}),'binding')
    spec=one(root_rows(table(ref,folder,'specs'),binding).query('definition_life == "PathEfficiency"'),'PathEfficiency spec')
    metric=one(root_rows(table(ref,folder,'metrics'),window).query('kind == @kind',local_dict={'kind':spec['kind']}),'metric')
    revision=one(root_rows(table(ref,folder,'revisions'),origin),'revision')
    exact='NodeBehaviorBook/NodeScaleTurnBehaviorRevision/'+binding['node_life']+'/'+str(UUID(int=(int(revision['high'])<<64)|int(revision['low'])))
    values={'completed_recent_updates':float(metric['current']) if metric['present']=='1' else None,
            'completed_previous_updates':float(metric['previous']) if metric['present']=='1' else None}
    for field,view in [('working_progress','working_progress_points'),('working_counter','working_counter_points'),
                       ('working_efficiency','working_efficiency_points'),('working_duration','working_duration_points'),
                       ('working_waiting','working_waiting_points'),('working_waiting_ratio','waiting_ratio_points')]:
        value=one(root_rows(table(ref,folder,field),origin),field)
        values[view]=float(value['value']) if value['present']=='1' else None
    base=one(table(ref,folder,'working_bases').query('address == @a',local_dict={'a':row['working']}),'working base')
    rhythm=one(root_rows(table(ref,folder,'rhythm'),base),'rhythm')
    values['interval_median_points']=float(rhythm['current_median_value']) if rhythm['current_median_present']=='1' else None
    return values,exact

cases={}
for name,K in PLAN['rb_cuts'].items():cases['rb_'+name+'_full']=(PLAN['source_refs']['W02'],W02+'data/selected_cuts/'+name+'/',K)
cases['rb_final_local']=cases['rb_final_full']
for name,K in PLAN['i_cuts'].items():cases[name]=(PLAN['source_refs']['W03'],W03+'data/crossk/'+name+'/',K)
cases['hc_close_waiting_final']=(PLAN['source_refs']['W03'],W03+'data/crossk/hc_final/',103315800)

for case,(ref,folder,K) in cases.items():
    browser=json.loads((OUT/'evidence'/('BROWSER_'+case+'.json')).read_text())
    check(case+':current_execution','execution:'+EXECUTION in browser['tags'])
    manifest=json.loads((OUT/'plot_view_data'/case/'plot_view_data_manifest.json').read_text())
    values,exact=expected(ref,folder,K)
    check(case+':resolved_exact',manifest['meta']['source_exact']==exact,exact)
    renderers=[r for p in browser['plots'] for r in p['renderers']]
    # KPriceLine displays the CENTER of each already supplied original bar.
    # It is not a knowledge-time point.  Verify actual bars and their complete
    # OHLC against the pinned original input instead of declaring its midpoint
    # a future market record (utlv2.py KPriceLine._plot_fig).
    price_path=(W02+'data/same_bound_price/rb_5m_price_calendar.csv' if case.startswith('rb_') else
                W02+'data/i_missing_context/i_5m_price_calendar.csv' if case.startswith('i_') else
                W03+'data/crossk/hc_final/hc_5m_price_calendar.csv')
    price_ref=PLAN['source_refs']['W02'] if not case.startswith('hc_') else PLAN['source_refs']['W03']
    original=pd.read_csv(io.BytesIO(raw(price_ref,price_path)))
    assert not original['open_uti'].duplicated().any()
    original=original.set_index('open_uti')
    projected=pd.read_csv(OUT/'plot_view_data'/case/'same_bound_5m_ohlc.csv')
    projected['label']=pd.to_datetime(projected['bar_time']).dt.strftime('%Y-%m-%d %H:%M')
    assert not projected['label'].duplicated().any()
    check(case+':input_origin_cut',int(projected['open_uti'].max())<=K,{'first':int(projected['open_uti'].min()),'last':int(projected['open_uti'].max()),'K':K})
    for field in ('open','high','low','close'):
        check(case+':price_projection_vs_original:'+field,
              all(near(None if pd.isna(row[field]) else row[field],None if pd.isna(original.loc[row['open_uti'],field]) else original.loc[row['open_uti'],field]) for _,row in projected.iterrows()))
    by_label=projected.set_index('label')
    for view,value in values.items():
        if view=='working_duration_points' and case.startswith('rb_'):continue
        if view=='working_duration_points' and case.startswith('hc_'):continue
        rs=[r for r in renderers if 'anchor:n_display/'+view in r['tags']]
        ys=[y for r in rs for y in r['data'].get('y',[])]
        check(case+':CDS:'+view,(ys==[] if value is None else len(ys)==1 and near(ys[0],value)),{'formal':value,'browser':ys})
        csv=OUT/'plot_view_data'/case/('n_display__'+view+'.csv')
        ys_csv=pd.read_csv(csv)['y'].tolist()
        check(case+':CSV:'+view,(ys_csv==[] if value is None else len(ys_csv)==1 and near(ys_csv[0],value)))
        for r in rs:
            check(case+':x_at_K:'+view,r['data']['x']==[K])
            check(case+':exact:'+view,r['data']['source_exact']==[exact])
    for renderer in renderers:
        data=renderer['data']
        if not renderer['tags'] and {'ts','open','high','low','close'}.issubset(data):
            selected=by_label.loc[data['ts']]
            utis=selected['open_uti'].tolist()
            centers=[u+(utis[n+1]-u)/2 if n+1<len(utis) else u+(u-utis[n-1])/2 for n,u in enumerate(utis)]
            check(case+':background_origins_not_future:'+renderer['id'],max(utis)<=K,{'last_original_uti':max(utis),'last_display_midpoint':max(data['x'])})
            check(case+':background_normal_bar_midpoint:'+renderer['id'],len(centers)==len(data['x']) and all(near(x,y) for x,y in zip(centers,data['x'])))
            for field in ('open','high','low','close'):
                expected_values=[None if pd.isna(v) else v for v in selected[field]]
                check(case+':background_actual_original_'+field+':'+renderer['id'],len(expected_values)==len(data[field]) and all(near(x,y) for x,y in zip(expected_values,data[field])))
            if case.startswith('i_'):
                check(case+':24_original_missing_close_bars:'+renderer['id'],sum(v is None or isinstance(v,float) and not math.isfinite(v) for v in data['close'])==24)
            continue
        for field in ('x','x0','x1','uti'):
            xs=renderer['data'].get(field,[])
            if xs and all(isinstance(x,(float,int)) or x is None for x in xs):
                check(case+':no_future:'+renderer['id']+':'+field,all(x is None or not math.isfinite(x) or x<=K for x in xs))
    check(case+':nondegenerate_ranges',all(p['y'][0]<p['y'][1] for p in browser['plots']))

full=json.loads((OUT/'evidence/BROWSER_rb_final_full.json').read_text())
local=json.loads((OUT/'evidence/BROWSER_rb_final_local.json').read_text())
check('same_final_exact_different_range_actual_documents',full['root']!=local['root'] and full['plots'][0]['x']!=local['plots'][0]['x'])
hc=json.loads((OUT/'evidence/BROWSER_hc_close_waiting_final.json').read_text())
refs={tag:[y for p in hc['plots'] for r in p['renderers'] if 'anchor:n_display/'+tag in r['tags'] for y in r['data']['y']]
      for tag in ('close_reference_points','high_reference_points')}
check('hc_original_close_and_wick',refs=={'close_reference_points':[3952.0,3946.0,3904.0],'high_reference_points':[3959.0]},refs)
i=json.loads((OUT/'evidence/BROWSER_i_recovery.json').read_text())
labels=[a['text'] for p in i['plots'] for a in p['annotations']]
check('i_visible_local_restart_and_missing_state',any('last_update缺' in s and 'local_start=35361000' in s for s in labels) and any('路径效率缺' in s for s in labels) and any('等待倍数缺' in s for s in labels),labels)
for name in ('rb_sparse_knowledge_cuts','i_sparse_recovery'):
    manifest=json.loads((OUT/'plot_view_data'/name/'plot_view_data_manifest.json').read_text())
    check(name+':no_sparse_hold_interpolation',all(item['rows']==0 for view,item in manifest['files'].items() if view.endswith(('_hold','_steps'))))
source_reads=json.loads((OUT/'evidence/SOURCE_READS.json').read_text())
for key,digest in source_reads.items():
    ref,path=key.split(':',1)
    check('source_hash:'+path,hashlib.sha256(raw(ref,path)).hexdigest()==digest)
nb=json.loads((OUT/'N_observation_Worker05.ipynb').read_text())
code=[c for c in nb['cells'] if c['cell_type']=='code']
check('six_code_cells_executed_no_error',all(c.get('execution_count') and not any(o.get('output_type')=='error' for o in c['outputs']) for c in code))
check('current_notebook_metadata',nb['metadata']['bi01']['order_id']==PLAN['order_id'] and 'R0014' in nb['metadata']['bi01']['invocation_id'])
check('no_platform_acceptance_in_current_configuration','platform_acceptance' not in PLAN)
result={'status':'PASS' if all(c['pass'] for c in checks) else 'FAIL','checks':checks,'qualified_scope':'Worker05 work2技术一致性；不代签专业判断/管理认可'}
(OUT/'evidence/TECHNICAL_VERIFICATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(result['status'],len(checks),'checks;',sum(not c['pass'] for c in checks),'failed')
raise SystemExit(0 if result['status']=='PASS' else 1)
