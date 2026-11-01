from pathlib import Path
from datetime import datetime
from urllib.parse import urlsplit
import json,hashlib,csv
import pandas as pd
from mquant.aidata.api import build_chart_run,build_board_run,make_point_anchor
from mquant.aidata.csv_feature import ReadOnlyCsvFeature
from mquant.aidata.profiles import ensure_profile_runtime
from mquant.frame import TestCAE1,GMap,GMapX,KLine,eval2
from mquant.quant import OptContext
from mquant.quant.models.graph import CaeNodeDao
from mquant.uplot import PlotSet,SpecEntitiesMainFig,KPriceLine,DefaultFigTheme,MulFieldsGlyphs
ensure_profile_runtime()
root=Path(__file__).resolve().parent;stage=root/'turn_staging';ready=json.loads((stage/'all_validated.json').read_text());assert ready['status']=='nine_original_E_results_validated'
plot_root=root/'three_turn_plot';plot_root.mkdir(exist_ok=True)
roles={'small':{'marker':'circle','size':8,'label':'small（S）'},'mid':{'marker':'diamond','size':12,'label':'mid（M）'},'big':{'marker':'triangle','size':17,'label':'big（L，large）'}}
features={};exports={}
for role,style in roles.items():
 frames=[]
 for sym in ['rb','hc','i']:
  report=next(x for x in ready['reports'] if x['role']==role and x['symbol']==sym)
  p=Path(report['validated_csv']);assert hashlib.sha256(p.read_bytes()).hexdigest()==report['csv_sha256']
  df=pd.read_csv(p,dtype={'x':'int64','xConfirm':'int64'});df['symbol']=sym;df['source_feature_ppid']=report['feature_ppid'];df['source_engine_sha256']=report['engine_binary_sha256'];df['source_native_parameter_path']=report['native_parameter_path'];frames.append(df)
 df=pd.concat(frames,ignore_index=True).sort_values(['symbol','x','event_ts'],kind='stable');p=plot_root/(role+'_original_E.csv');df.to_csv(p,index=False);digest=hashlib.sha256(p.read_bytes()).hexdigest()
 feature=ReadOnlyCsvFeature({'alias':'GTQH_30m_original_E_'+role,'path':str(p),'sha256':digest,'symbol_field':'symbol','index_field':'event_ts','integer_columns':{'_csv_x':'x','_csv_xConfirm':'xConfirm'},'numeric_columns':{'_csv_y':'y','_csv_yConfirm':'yConfirm'}})
 features[role]=feature;exports[role]={'path':str(p),'sha256':digest,'rows':len(df),'source_feature_ppids':list(df.source_feature_ppid.unique())}
context=OptContext({'sof_name':'GTQH_L1_20210104_20240208','stk_tlist':'gtqh_four','startDay':None,'endDay':None})
evidence=[make_point_anchor(KLine(freq='30m'),uti_fields='closeUti',label='GTQH 30m正式行情',feature_key='gtqh_kline_30m',slice_levels=['big'],evidence_role='market_context_sidecar',is_raw_market_data=True)]
for role,feature in features.items():
 s=roles[role]
 evidence.append(make_point_anchor(feature,uti_fields='_csv_x',label=s['label']+' 原E暂存验证结果',feature_key='gtqh_E_'+role,slice_levels=['big'],plot_binding={'kind':'point','x_field':'_csv_x','y_field':'_csv_y','label':s['label'],'surfaces':['big'],'style':{'marker':s['marker'],'size':s['size']}}))
brief={'output_root':str(plot_root),'run_id':'GTQH_C001_three_turns_'+datetime.now().strftime('%Y%m%d_%H%M%S'),'run_note':'GTQH自身日历，原E small/mid/large暂存结果；large标为big；只生成一个30m图','context':context,'blk':'blk@steel','calendar_override':'@','extract_time_syms':'blk@steel','generation_depth':'big','big_source':{'mode':'manual','timespans':[('2021-08-15','2021-09-30','TEST-C001')]},'evidence_features':evidence}
run=build_chart_run(brief,dry_run=False)
plots=[KPriceLine(feat=KLine(freq='30m'),std_method='ratio')]
for role,feature in features.items():
 s=roles[role]
 plots.append(MulFieldsGlyphs({'feats':GMap({role:feature}),'dfkeys':[None],'legend_labels':[s['label']],'glyphs':s['marker'],'xfields':['_csv_x'],'yfields':['_csv_y'],'timefieldtype':'uti','size':s['size'],'alphas':0.85,'dynstd_method':True}))
# rb仅确定背景轴；绘制标的显式指定steel中的rb/hc/i，各自仍从@读取。
config={'Context':context,'plotsets':GMap({'TEST_C001':PlotSet({'calendar_name':'@','blk':['rb'],'timespans':[('2021-08-15','2021-09-30','TEST-C001')],'figs':GMapX.from_list([SpecEntitiesMainFig(entity_plots=GMap({'syms!blk@steel':GMapX.from_list(plots)}),title='!GTQH 30m TEST-C001 · small / mid / big（large）')])})}),'theme':DefaultFigTheme(),'x_label_freq':'1d','extra_time':0,'fig_width':2400,'fig_height1':700,'fig_height':150,'manual_upd':True,'plot_name':run.run_id}
wrapper=TestCAE1({'name':config});restored=eval2(wrapper.fason);assert len(restored.doShowCAEGraph().P.plotsets.P)==1
(plot_root/'single_three_turns.fason.txt').write_text(wrapper.fason)
old=str(CaeNodeDao.xqueryById(node_id=6141).get('params'));created=CaeNodeDao.createUniqueWithFao(tar=wrapper)
board=build_board_run({**brief,'run_id':run.run_id},reuse_core=True,dry_run=False)
stats=pd.read_csv(board.feature_slice_stats_path);assert stats.slice_success.all(),stats[['target_id','feature_key','error_message']].to_dict('records')
assert str(CaeNodeDao.xqueryById(node_id=6141).get('params'))==old
node=str(created['node']['id']);host=urlsplit(created['report_url']).hostname
result={'run_id':run.run_id,'node_id':node,'url':f'http://{host}:5006/cae?node_id={node}','source':'GTQH_L1_20210104_20240208','calendar':'@，背景轴rb；三品种自身数据','window':['2021-08-15','2021-09-30'],'members':['rb','hc','i'],'roles':roles,'exports':exports,'stats_path':str(board.feature_slice_stats_path),'delivery_manifest':str(board.delivery_manifest_path),'old_6141_preserved':True,'formal_F_source_modified':False,'result_storage':'本工作区test_runs暂存原E输出及只读CSV传输；未发布到F盘正式特征目录'}
(plot_root/'three_turn_page.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False,indent=2),flush=True)
