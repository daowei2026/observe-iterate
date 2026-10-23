"""只核W06已定位的范围语义、正式标量与真实前端；不重跑W05 693项。"""
from pathlib import Path
from uuid import UUID
import io,json,subprocess,math
import pandas as pd

OUT=Path(__file__).resolve().parents[1]
REPO=OUT.parents[3]
checks=[]
def check(name,condition,actual=None):checks.append({'check':name,'pass':bool(condition),'actual':actual})
def table(ref,folder,name):
    raw=subprocess.check_output(['git','-C',str(REPO),'show',ref+':'+folder+name+'.csv'])
    return pd.read_csv(io.BytesIO(raw),dtype='string')
def one(frame):
    assert len(frame)==1,len(frame)
    return frame.iloc[0]
def at_root(frame,root):
    for key in ('timestamp','occurrence','record_id'):frame=frame[frame[key].eq(root[key])]
    return frame
def expected(ref,folder,K):
    origins=table(ref,folder,'origins');origin=one(origins[origins['as_of'].eq(str(K))])
    row=one(at_root(table(ref,folder,'rows'),origin))
    windows=table(ref,folder,'windows');window=one(windows[windows['address'].eq(row['window'])])
    bindings=table(ref,folder,'bindings');binding=one(bindings[bindings['address'].eq(window['binding'])])
    specs=at_root(table(ref,folder,'specs'),binding);spec=one(specs[specs['definition_life'].eq('PathEfficiency')])
    metrics=at_root(table(ref,folder,'metrics'),window);metric=one(metrics[metrics['kind'].eq(spec['kind'])])
    revision=one(at_root(table(ref,folder,'revisions'),origin))
    exact='NodeBehaviorBook/NodeScaleTurnBehaviorRevision/'+binding['node_life']+'/'+str(UUID(int=int(revision['high'])*(1<<64)+int(revision['low'])))
    values={'completed_recent_updates':float(metric['current']),'completed_previous_updates':float(metric['previous'])}
    for field,view in (('working_progress','working_progress_points'),('working_counter','working_counter_points'),
                       ('working_efficiency','working_efficiency_points'),('working_waiting','working_waiting_points'),
                       ('working_waiting_ratio','waiting_ratio_points')):
        value=one(at_root(table(ref,folder,field),origin))
        values[view]=float(value['value']) if value['present']=='1' else None
    return exact,values,{'window':int(row['window']),'working':int(row['working']),'binding':int(window['binding'])}
def snapshot(name):return json.loads((OUT/'evidence'/('BROWSER_'+name+'.json')).read_text())
def renderers(s,view):return [r for p in s['plots'] for r in p['renderers'] if 'anchor:n_display/'+view in r['tags']]
def manifest(name):return json.loads((OUT/'plot_view_data'/name/'plot_view_data_manifest.json').read_text())

runtime=json.loads((OUT/'evidence/EXECUTION_RUNTIME.json').read_text())
plan=json.loads((OUT/'DISPLAY_PLAN.json').read_text())
names=['rb_final_full_before','rb_final_local','rb_final_full','rb_final_local_visible','i_recovery','hc_close_waiting_final']
for name in names:
    s=snapshot(name)
    check(name+':current_execution','execution:'+runtime['execution_id'] in s['tags'],s['root'])
for case,ref,folder,K in (
    ('rb_final_full',plan['source_refs']['W02'],'runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-DISPLAY-INTEGRATION-02/data/selected_cuts/final/',103315800),
    ('rb_final_local',plan['source_refs']['W02'],'runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-DISPLAY-INTEGRATION-02/data/selected_cuts/final/',103315800),
    ('i_recovery',plan['source_refs']['W03'],'runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-READABILITY-CROSSK-03/data/crossk/i_recovery/',35361000),
    ('hc_close_waiting_final',plan['source_refs']['W03'],'runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-READABILITY-CROSSK-03/data/crossk/hc_final/',103315800)):
    exact,values,identity=expected(ref,folder,K)
    m=manifest(case);s=snapshot(case)
    check(case+':exact_K_identity',m['meta']['source_exact']==exact and m['meta']['selected_k']==K and
          m['meta']['window_address']==identity['window'] and m['meta']['working_address']==identity['working'] and m['meta']['data_binding']==identity['binding'])
    for view,value in values.items():
        csv=pd.read_csv(OUT/'plot_view_data'/case/('n_display__'+view+'.csv'))
        rs=renderers(s,view)
        if value is None:
            check(case+':'+view+':true_missing',csv.empty and not rs)
        else:
            check(case+':'+view+':formal_CSV_CDS',len(csv)==1 and len(rs)==1 and float(csv.iloc[0]['x'])==K and
                  math.isclose(float(csv.iloc[0]['y']),value,rel_tol=1e-12) and rs[0]['data']['x']==[K] and
                  math.isclose(rs[0]['data']['y'][0],value,rel_tol=1e-12) and rs[0]['data']['source_exact']==[exact])
    price=pd.read_csv(OUT/'plot_view_data'/case/'same_bound_5m_ohlc.csv')
    check(case+':no_future_input',int(price['open_uti'].max())<=K)

full,local=manifest('rb_final_full'),manifest('rb_final_local')
check('rb:source_coverage_unchanged',full['meta']['source_price_range']==local['meta']['source_price_range']==[100443000,103315800] and full['meta']['source_price_rows']==local['meta']['source_price_rows']==4789)
check('rb:real_display_changed',full['meta']['price_rows']==4789 and local['meta']['price_rows']==294 and local['meta']['price_range']==[103140000,103315800])
check('rb:local_only_omissions',local['notices'] and all(n.get('category')=='display_omission' for n in local['notices']))
check('rb:consumed_configuration_scope_policy', 'local view displays only its selected range' in local['configuration']['readability_policy']['price_range'] and local['configuration']['readability_policy']['scalar_layout']['height']==220)
omitted=[g for n in local['notices'] for g in n.get('omitted_geometry',[])]
check('rb:original_member0_preserved_as_omitted',any(g.get('x0')==100460400 and g.get('x1')==100633800 and g.get('y0')==3953 and g.get('y1')==4034 for g in omitted))
check('rb:no_outside_boundary_geometry',all(all(v>=103140000 and v<=103315800 for k,v in r['data'].items() if k in ('x','x0','x1') for v in v) for p in snapshot('rb_final_local')['plots'] for r in p['renderers'] if any(t in str(r['tags']) for t in ('selected_previous_boundaries','selected_recent_boundaries','selected_working_boundary','selected_actual_endpoints','selected_confirmations'))))
irecovery=manifest('i_recovery')
check('i:real_missing_price_not_suppressed',irecovery['meta']['display_missing_close_rows']==24 and any(n.get('category')=='price_missing' for n in irecovery['notices']))
check('i:input_coverage_distinct',any(n.get('category')=='input_coverage' for n in irecovery['notices']))
check('i:formal_states_not_suppressed',any(n.get('category') is None and n.get('formal_state',{}).get('knownness')==4 for n in irecovery['notices']))
events=json.loads((OUT/'evidence/FRONTEND_EVENTS.json').read_text())
for action in ('rb_full_local_full_scope_and_formal_identity_pass','i_actual_24_price_nulls_formal_missing_and_waiting_zero_pass','hc_actual_sidebar_toggle_live_view','frontend_interactions_finished'):
    check('actual_frontend:'+action,any(e['action']==action for e in events))
result={'order_id':'BI01-FO01-N-W05-SCOPE-READABILITY-06','execution_id':runtime['execution_id'],
        'qualification':'W06定向技术核验；HC文字是否可读另见实际像素记录，不以模型值替代',
        'result':'PASS' if all(c['pass'] for c in checks) else 'FAIL','checks':checks,
        'passed':sum(c['pass'] for c in checks),'failed':sum(not c['pass'] for c in checks)}
(OUT/'evidence/SCOPE_VERIFICATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(result['result'],result['passed'],'checks;',result['failed'],'failed')
raise SystemExit(bool(result['failed']))
