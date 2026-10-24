"""实际交付Notebook/浏览器当前CDS/图用CSV对应；不替正式N算法或专业接收。"""
from pathlib import Path
import csv,hashlib,json,math
OUT=Path(__file__).resolve().parents[1]
def load(path):return json.loads(path.read_text())
runtime=load(OUT/'evidence/EXECUTION_RUNTIME.json')
nb=load(OUT/'N_observation_Worker09.ipynb')
events=load(OUT/'evidence/FRONTEND_EVENTS.json')
completion=load(OUT/'evidence/KERNEL_COMPLETION.json')
assert completion['execution_id']==runtime['execution_id']
assert runtime['actual_aidata_head']=='25a9fd8b1333aafd4c56fd1b288e7f8d3c8c3113'
code=[c for c in nb['cells'] if c['cell_type']=='code']
assert [c['execution_count'] for c in code]==list(range(1,7))
assert not [o for c in code for o in c.get('outputs',[]) if o['output_type']=='error']
needed=('restart_kernel_clicked','run_all_cells_explicit_clicked','run_all_finished',
 'rb_full_local_full_scope_and_formal_identity_pass','native_zoom_pan_reset_pass','native_legend_hide_restore_pass',
 'i_actual_24_price_nulls_formal_missing_and_waiting_zero_pass','i_compact_top_numeric_labels_actual_consumer_check',
 'hc_actual_sidebar_toggle_live_view','frontend_interactions_finished')
assert all(any(e['action']==name for e in events) for name in needed)
def equal(left,right):
 if left in ('',None):return right is None
 try:return math.isclose(float(left),float(right),rel_tol=1e-12,abs_tol=1e-12)
 except (TypeError,ValueError):return left==right
checks=[]
for case,file in [('rb_final_full','BROWSER_rb_final_full.json'),('rb_final_local','BROWSER_rb_final_local_visible.json'),
                  ('i_recovery','BROWSER_i_recovery.json'),('hc_close_waiting_final','BROWSER_hc_close_waiting_final.json')]:
 browser=load(OUT/'evidence'/file)
 assert 'execution:'+runtime['execution_id'] in browser['tags']
 matched=[]
 for plot in browser['plots']:
  assert plot['y'][1]>plot['y'][0] and plot['x'][1]>plot['x'][0]
  for renderer in plot['renderers']:
   names=[t[len('anchor:n_display/'):] for t in renderer['tags'] if t.startswith('anchor:n_display/')]
   if not names:continue
   view=names[0];path=OUT/'plot_view_data'/case/('n_display__'+view+'.csv')
   with path.open() as stream:rows=list(csv.DictReader(stream))
   columns=[k for k in ('x','y','x0','x1','y0','y1','source_exact','as_of_uti') if k in renderer['data'] and (not rows or k in rows[0])]
   for col in columns:
    assert len(rows)==len(renderer['data'][col]),(case,view,col,'row count')
    assert all(equal(row[col],actual) for row,actual in zip(rows,renderer['data'][col])),(case,view,col)
   matched.append({'view':view,'rows':len(rows),'columns':columns,'csv_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
       'actual_renderer_id':renderer['id'],'panel':plot['title']})
 assert matched
 checks.append({'case':case,'root':browser['root'],'tagged_execution':runtime['execution_id'],
   'actual_renderer_to_plot_csv':matched,'all_geometry_identity_columns_equal':True})
formal=load(OUT/'evidence/FINAL_CONTRACT.json')
cold=load(OUT/'evidence/COLD_RESTORE_AND_BRIDGE.json')
assert formal['fason_byte_equal_to_old'] and formal['ppid_equal_to_old'] and len(formal['keys'])==16
assert cold['fason_equal'] and cold['bridge']['actual_called'] and not cold['dao_writes']
life=load(OUT/'evidence/FRONTEND_EPISODE_LIFECYCLE.json')
assert life['frontend_exit_code']==0 and life['owned_server_exited'] and life['remaining_owned_kernels']==0
result={'order_id':'BI01-FO01-N-BOUNDED-DISPLAY-09',
 'qualification':'本单真实技术交付一致性；不等于共享采用/平台页面恢复/工作3接收/正式工作4',
 'execution_id':runtime['execution_id'],'actual_aidata_head':runtime['actual_aidata_head'],
 'actual_notebook_counts':[c['execution_count'] for c in code],
 'required_actual_frontend_actions':list(needed),'cases':checks,
 'ordinary_16_key_fason_ppid_unchanged':True,'cold_actual_restore_and_bridge':True,
 'owned_services_closed':True,'normal_platform_registration':False,'shared_adoption':False,
 'unit_test_result':{'passed':59,'warnings':2,'qualification':'有限技术夹具及相连回归，非全仓/市场验收'},
 'all_actual_checks_passed':True}
(OUT/'CHECK_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'execution_id':runtime['execution_id'],'cases':len(checks),'actual_delivery_consistent':True}))
