"""独立读固定Git原CSV→实际浏览器CDS→交付图用CSV；不重算N、不作专业接收。"""
from pathlib import Path
import csv,datetime,hashlib,io,json,math,os,subprocess
OUT=Path(os.environ.get('BI01_W10_DELIVERY',Path(__file__).resolve().parents[1]))
REPO=Path(os.environ.get('OBSERVE_REPO','/dwdhome/fy/observe-iterate-bi01-fo-01'))
def load(p):return json.loads(p.read_text())
def rows(p):return list(csv.DictReader(io.StringIO(p)))
def equal(a,b):
 if a in ('',None):return b in ('',None)
 try:return math.isclose(float(a),float(b),rel_tol=1e-12,abs_tol=1e-12)
 except (TypeError,ValueError):
  try:return datetime.datetime.fromisoformat(a)==datetime.datetime.fromisoformat(b)
  except (TypeError,ValueError):return a==b
runtime=load(OUT/'evidence/EXECUTION_RUNTIME.json');execution=runtime['execution_id']
nb=load(OUT/'N_time_expression_Worker10.ipynb');code=[c for c in nb['cells'] if c['cell_type']=='code']
assert [c['execution_count'] for c in code]==list(range(1,7))
assert not [o for c in code for o in c.get('outputs',[]) if o['output_type']=='error']
assert load(OUT/'evidence/KERNEL_COMPLETION.json')['execution_id']==execution
events=load(OUT/'evidence/FRONTEND_EVENTS.json')
needed=['restart_kernel_clicked','run_all_cells_explicit_clicked','run_all_finished',
 'rb_before_confirmation_before_actual_control_pass','rb_comparison_query_axis_isolation_and_final_reference_pass',
 'i_before_recovery_after_before_actual_control_pass','actual_hover_full_life_exact_state_pass','frontend_interactions_finished']
assert all(any(e['action']==name for e in events) for name in needed)
expected=load(OUT/'evidence/FORMAL_CUT_EXPECTATIONS.json');sources=load(OUT/'evidence/SOURCE_READS.json')
# Notebook读取hash与固定Git对象独立逐字核对；不是再读生产或重生成特征。
for source,sha in sources.items():
 raw=subprocess.check_output(['git','-C',str(REPO),'show',source]);assert hashlib.sha256(raw).hexdigest()==sha,source
raw_checks=[]
tables={'working_progress':'working_progress_points','working_counter':'working_counter_points',
 'working_duration':'working_duration_points','working_waiting':'working_waiting_points',
 'working_efficiency':'working_efficiency_points','working_waiting_ratio':'waiting_ratio_points'}
for name,e in expected.items():
 symbol,cut=name.split('_',1)
 for table,view in tables.items():
  matching=[source for source in sources if '/'+cut+'/'+table+'.csv' in source]
  assert len(matching)==1,(cut,table)
  raw=subprocess.check_output(['git','-C',str(REPO),'show',matching[0]])
  original=rows(raw.decode());assert len(original)==1
  for c in original[0]:assert equal(original[0][c],e['raw_formal_values'][table][c]),(cut,table,c,original[0][c],e['raw_formal_values'][table][c])
 raw_checks.append({'selection':name,'K':e['K'],'exact':e['exact'],'raw_formal_csvs_equal':True})
def view(snapshot,key):return [r['data'] for p in snapshot['plots'] for r in p['renderers'] if 'anchor:n_display/'+key in r['tags']]
def text(s):return '\n'.join([b['text'] for b in s['badges']]+[a['text'] for p in s['plots'] for a in p['annotations']])
checks=[]
for path in sorted((OUT/'evidence').glob('BROWSER_*.json')):
 s=load(path);case=s['case'];assert 'execution:'+execution in s['tags']
 bindings=load(OUT/'plot_view_data'/case/'ACTUAL_DISPLAY_BINDINGS.json')
 contexts=bindings['time_contexts'];Ks=[c['K'] for c in contexts];comparison=case.endswith('_comparison')
 assert all(c['resolved_origin_as_of']<=c['K'] for c in contexts)
 matched=[]
 for p in s['plots']:
  assert p['x'][0]<p['x'][1] and p['y'][0]<p['y'][1]
  for r in p['renderers']:
   names=[t.split('anchor:n_display/',1)[1] for t in r['tags'] if t.startswith('anchor:n_display/')]
   if not names:continue
   key=names[0];csvpath=OUT/'plot_view_data'/case/('n_display__'+key+'.csv')
   csvrows=rows(csvpath.read_text());data=r['data']
   columns=[c for c in ('x','y','x0','x1','y0','y1','source_exact','as_of_uti','state_text','working_life','working_start','formal_working_age') if c in data and (not csvrows or c in csvrows[0])]
   for c in columns:
    assert len(csvrows)==len(data[c]),(path.name,key,c)
    assert all(equal(row[c],actual) for row,actual in zip(csvrows,data[c])),(path.name,key,c)
   matched.append({'view':key,'rows':len(csvrows),'columns':columns,'renderer_id':r['id'],'csv_sha256':hashlib.sha256(csvpath.read_bytes()).hexdigest()})
  if '行情与过程' not in p['title']:
   if comparison:
    assert p['x'][0]<min(Ks)<max(Ks)<p['x'][1]
    assert all(r['glyph'] not in ('Line','Segment') for r in p['renderers'])
   else:assert p['x']==[Ks[0]-1,Ks[0]+1]
 assert max(view(s,'close_path')[0]['x'])<=max(Ks)
 for table,key in tables.items():
  actual=view(s,key);pairs=[]
  for c in contexts:
   e=next(e for e in expected.values() if e['K']==c['K'] and e['exact']==c['source_exact'])
   v=e['raw_formal_values'][table]
   if int(v['present'])==1:pairs.append((c['K'],v['value']))
  assert (not actual and not pairs) or list(zip(actual[0]['x'],actual[0]['y']))==pairs,(path.name,key)
 if not comparison and Ks==[103150800]:assert '新增recent' not in text(s) and 'ef2f74f6' not in text(s)
 if not comparison and Ks==[35360400]:assert '局部计时：waiting=' not in text(s)
 if not comparison and Ks==[35361600]:assert 'waiting=600' in text(s) and 'last_update仍缺' in text(s)
 if case.startswith('i_'):
  close=rows((OUT/'plot_view_data'/case/'n_display__close_path.csv').read_text())
  assert sum(row['y']=='' for row in close)==24
 checks.append({'snapshot':path.name,'case':case,'root':s['root'],'Ks':Ks,'current_browser_CDS_to_plot_csv':matched,
  'raw_formal_point_values_equal':True,'future_record_leak':False,'scalar_interpolation':False})
life=load(OUT/'evidence/FRONTEND_EPISODE_LIFECYCLE.json')
assert life['frontend_exit_code']==0 and life['owned_server_exited'] and life['remaining_owned_kernels']==0
result={'order_id':'BI01-FO01-N-TIME-EXPRESSION-10','execution_id':execution,'actual_aidata_head':runtime['actual_aidata_head'],
 'qualification':'仅本单工作1/2真实技术一致性；非生产算法认证、Pro判断、管理接收或平台用途放行',
 'source_git_hashes_equal':True,'raw_formal_checks':raw_checks,'current_browser_checks':checks,
 'required_real_frontend_actions':needed,'notebook_counts':[c['execution_count'] for c in code],
 'owned_services_closed':True,'new_production_read_or_calculation':False,'platform_or_DAO_write':False,'all_actual_checks_passed':True}
(OUT/'CHECK_RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'execution_id':execution,'browser_snapshots':len(checks),'raw_selections':len(raw_checks),'consistent':True}))
