import os
"""真实公开chart/board；只写本单隔离观察run，不调用会注册DAO的页面factory。"""
from pathlib import Path
import contextlib,datetime,hashlib,json,subprocess,traceback,uuid
rt=Path(os.environ.get('BI01_W11_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker11-runtime'));repo=Path('/dwdhome/fy/observe-iterate-bi01-fo-01')
root=repo/'artifacts/bi01-worker11-runs';root.mkdir(parents=True,exist_ok=True)
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2,default=str)+'\n')
def git_bytes(ref,path):return subprocess.check_output(['git','-C',str(repo),'show',ref+':'+path])
def pin(ref,path,target):
 data=git_bytes(ref,path);target.parent.mkdir(parents=True,exist_ok=True)
 if target.exists() and target.read_bytes()!=data:raise ValueError('拒绝覆盖不同固定原件')
 target.write_bytes(data)
 return dict(path=str(target),sha256=hashlib.sha256(data).hexdigest(),source=dict(repo='daowei2026/observe-iterate',commit=ref,path=path))
result=dict(order_id='BI01-FO01-N-NORMAL-CONSUMER-11',normal_platform_registration=False,DAO_writes=False,production_read_or_compute=False)
try:
 with (rt/'build-normal.private.log').open('w') as log,contextlib.redirect_stdout(log),contextlib.redirect_stderr(log):
  import bootstrap,pandas as pd
  from mquant.quant import OptContext
  from mquant.aidata.api import build_chart_run,build_board_run
  from mquant.aidata.contracts import build_run_handle
  from mquant.aidata.normal_node_behavior import persist_selection,display_selection
  from mquant.aidata.normal_node_behavior_time import CONSUMER_VERSION
  from mquant.aidata.big_world_chart import AidataBigWorldReviewCAE,_chart_params_from_run_brief,_params_for_fao
  scene_spec=pin('e4ada20368ccb6ef5b16993b7954fcff957be5ef','runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-TIME-EXPRESSION-10/TIME_EXPRESSION_PLAN.json',root/'source-cache/TIME_EXPRESSION_PLAN_W10.json')
  scene=json.loads(Path(scene_spec['path']).read_text());cuts={};prices={}
  W02='runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-DISPLAY-INTEGRATION-02/'
  W03='runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-READABILITY-CROSSK-03/'
  for symbol,ref,prefix in [('rb',scene['source_refs']['W02'],W02+'data/selected_cuts/'),('i',scene['source_refs']['W03'],W03+'data/crossk/')]:
   cuts[symbol]={}
   for name,k in scene[symbol+'_cuts'].items():
    folder=prefix+name+'/'
    names=subprocess.check_output(['git','-C',str(repo),'ls-tree','--name-only',ref+':'+folder],text=True).splitlines()
    tables={name[:-4]:pin(ref,folder+name,root/'source-cache'/symbol/str(k)/name) for name in names if name.endswith('.csv')}
    from mquant.aidata.normal_node_behavior import read_frame
    from mquant.aidata.u2_normal_node_behavior_display import _occurrences
    rows=_occurrences({n:read_frame(s) for n,s in tables.items()},symbol);assert len(rows)==1
    cuts[symbol][k]=dict(as_of=k,expected_exact=str(rows.iloc[0].source_exact),tables=tables)
   price_path=W02+('data/same_bound_price/rb_5m_price_calendar.csv' if symbol=='rb' else 'data/i_missing_context/i_5m_price_calendar.csv')
   prices[symbol]=pin(scene['source_refs']['W02'],price_path,root/'source-cache'/symbol/'original_price_calendar.csv')
  catalog_path=rt/'CATALOG.json'
  if catalog_path.exists():catalog=json.loads(catalog_path.read_text())
  else:
   prefix='BI01-FO01-W11-'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:6]
   catalog=dict(prefix=prefix,cases=[])
   for symbol in ('rb','i'):
    for name,k in scene[symbol+'_cuts'].items():catalog['cases'].append(dict(case=symbol+'_query_'+name,symbol=symbol,purpose='as_known_query',Ks=[k],run_id=prefix+'-'+symbol+'-'+name))
    keys='primary_pair' if symbol=='rb' else 'comparison_cuts'
    ks=[scene[symbol+'_cuts'][n] for n in scene['time_expression'][symbol][keys]]
    catalog['cases'].append(dict(case=symbol+'_comparison',symbol=symbol,purpose='retrospective_listed_cuts',Ks=ks,run_id=prefix+'-'+symbol+'-comparison'))
   dump(catalog_path,catalog)
  context=OptContext(sof_name=scene['sof_name']);results=[]
  for item in catalog['cases']:
   symbol=item['symbol'];ks=item['Ks'];refs={}
   if symbol=='rb' and max(ks)>=scene['rb_cuts']['at_or_after_confirmation']:
    refs=dict(member_before=scene['rb_cuts']['before_confirmation'],member_after=scene['rb_cuts']['at_or_after_confirmation'])
    if ks==[scene['rb_cuts']['final']]:refs['earlier_same_life']=scene['rb_cuts']['at_or_after_confirmation']
   selection=dict(version=2,purpose=item['purpose'],symbol=symbol,color=scene['instrument_colors'][symbol],
      node_life=cuts[symbol][ks[0]]['expected_exact'].split('/')[-2],knowledge_ks=ks,
      cuts=[cuts[symbol][k] for k in sorted(set(ks)|set(refs.values()))],reference_roles=refs,
      price=prices[symbol],scene=scene_spec,configuration_version=CONSUMER_VERSION)
   run=build_run_handle(root/item['run_id']);(run.run_dir/'manifest').mkdir(parents=True,exist_ok=True)
   persist_selection(run,selection);desc=display_selection(run.run_dir)
   policy=scene['time_expression'][symbol];start=policy.get('primary_price_start',policy.get('price_start'))
   source_price=read_frame(prices[symbol],formal=False)
   start_ts=str(source_price.loc[source_price.open_uti.eq(start)].index[0])
   end_ts=str(source_price.loc[source_price.open_uti.eq(max(ks))].index[0])
   rbi=dict(output_root=str(root),run_id=run.run_id,context=context,blk=symbol,calendar_override=scene['calendar'],generation_depth='big',
      big_source=dict(mode='manual',timespans=[dict(start_uti=start,end_uti=max(ks),start_ts=start_ts,end_ts=end_ts,label=item['case'])]),
      evidence_features=[desc],run_note='同BI-01-FO-01 Worker11已认可时间用途的隔离正常观察组织；非平台发布/新业务Run')
   existed=run.timespan_index_path.exists();chart=build_chart_run(rbi,reuse_core=existed,dry_run=False)
   core_before=chart.timespan_index_path.read_bytes()
   board=build_board_run(rbi,reuse_core=True,dry_run=False)
   assert board.timespan_index_path.read_bytes()==core_before
   spans=pd.read_csv(board.timespan_index_path);assert len(spans)==1 and spans.iloc[0].level=='big'
   node=str(spans.iloc[0].node_id);params=_params_for_fao(AidataBigWorldReviewCAE,{**_chart_params_from_run_brief(board,rbi),'big_node_id':node})
   obj=AidataBigWorldReviewCAE(params);fason_path=rt/'serialized'/('W11_'+item['case']+'.fason.txt');fason_path.parent.mkdir(exist_ok=True);fason_path.write_text(obj.fason)
   stats=pd.read_csv(board.feature_slice_stats_path)
   result_item={**item,'run_dir':str(board.run_dir),'node_id':node,'descriptor':desc,'fason_private_path':str(fason_path),
      'fason_sha256':hashlib.sha256(obj.fason.encode()).hexdigest(),'ppid':obj.ppid,'parameter_keys':sorted(dict(obj.P)),
      'public_chart_called':True,'public_board_called':True,'dry_run':False,'core_reused_for_board':True,
      'member_symbols':json.loads(board.run_brief_path.read_text())['member_symbols'],
      'formal_slice_stats_rows':len(stats),'all_slice_success':bool(stats.slice_success.all()),
      'display_in_formal_slices':bool(stats.source_role.eq('display').any()),'run_brief':str(board.run_brief_path)}
   assert result_item['all_slice_success'] and not result_item['display_in_formal_slices'] and len(result_item['parameter_keys'])==16
   results.append(result_item);dump(rt/'BUILT_RUNS.json',{'cases':results});print('built',item['case'],flush=True)
  result['cases']=results;result['complete']=True
except Exception as exc:
 with (rt/'build-normal-error.private.log').open('w') as f:traceback.print_exc(file=f)
 result.update(error_type=type(exc).__name__,complete=False)
dump(rt/'NORMAL_API_RESULTS.json',result)
print(json.dumps({k:v for k,v in result.items() if k!='cases'},ensure_ascii=False));raise SystemExit(0 if result['complete'] else 1)
