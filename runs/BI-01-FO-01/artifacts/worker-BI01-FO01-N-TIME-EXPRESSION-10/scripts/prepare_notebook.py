"""从W09确切主Notebook派生本单：保留读取谱系，清输出，新时间场景实际接线。"""
from pathlib import Path
import hashlib,json,subprocess
OUT=Path(__file__).resolve().parents[1];REPO=OUT.parents[3]
W09='runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-BOUNDED-DISPLAY-09/'
REF='35e1836f6a0ef8a123d0441070d3e8e4e760a816'
raw=subprocess.check_output(['git','-C',str(REPO),'show',REF+':'+W09+'N_observation_Worker09.ipynb'])
assert subprocess.check_output(['git','hash-object','--stdin'],input=raw).decode().strip()=='b271fe3541166a1e04d216bd845d59e8f7b25123'
nb=json.loads(raw);cells={c['id']:c for c in nb['cells']}
original_plan=subprocess.check_output(['git','-C',str(REPO),'show','91887f0dfff9c4d5d6182bde49124ba0e832323f:runs/BI-01-FO-01/artifacts/professional-R0038/TIME_EXPRESSION_PLAN.json'])
(OUT/'inputs').mkdir(parents=True,exist_ok=True);(OUT/'evidence').mkdir(exist_ok=True)
(OUT/'inputs/TIME_EXPRESSION_PLAN_R0038.json').write_bytes(original_plan)
plan=json.loads(original_plan);plan.update(version='0.5.1-worker10',source_scene_version=plan['version'],
 status='WORKER_SCENE_IMPLEMENTED_REQUIRES_THIS_EXECUTION_NOT_MANAGER_ACCEPTED',
 order_id='BI01-FO01-N-TIME-EXPRESSION-10')
(OUT/'TIME_EXPRESSION_PLAN.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
def setcell(id,source):cells[id]['source']=source.splitlines(keepends=True)
setcell('r0011-00','''# Worker10｜已知切点的时间解释与真实回看

BI01-FO01-N-TIME-EXPRESSION-10；原Pro R0038签发。本次只做工作1/2的新时间表达，不修改M37已认可四视域或进入工作4。
从W09确切主Notebook派生并清旧输出；源为W02/W03锁定正常原表，不是旧图用CSV，不重算N。
“所选K当时可知”和“事后并列所列切点”明确分开。仅六个已供准确K，不提供任意K全历史；没有连续保持线或插值。
下面的实际图由既有Uplot/共用组合构建；新时间准备器只返回有限视图/注记，不返回任意layout。新用途待原Pro与管理判断。
''')
first=''.join(cells['r0011-01']['source']).replace('W09-','W10-').replace('BI01_W09','BI01_W10').replace('bi01-w09','bi01-w10').replace('aidata-bi01-fo01-n-bounded-display-r0035','aidata-bi01-fo01-n-time-expression-r0038')
setcell('r0011-01',first)
setcell('r0011-02','## 准确源与本次执行身份\n原有读取/UInt64/空值处理复用；当前kernel、模块有效字节和源hash另记，不把W09执行冒成本次。\n')
helpers=''.join(cells['r0011-03']['source']).split('context = OptContext')[0]
helpers=helpers.replace('"DISPLAY_PLAN.json"','"TIME_EXPRESSION_PLAN.json"')
helpers=helpers[:helpers.index('def merge_real_cuts')]
helpers+='''
import mquant.aidata.u2_normal_node_behavior_time as nt
from copy import deepcopy
from bokeh.models import GlyphRenderer,LabelSet,Range1d,FixedTicker
context=OptContext(sof_name=PLAN['sof_name'])
output_notebook(resources=INLINE,hide_banner=True)
EVIDENCE=ARTIFACT_DIR/'evidence';EVIDENCE.mkdir(exist_ok=True)
RUNTIME={'execution_id':EXECUTION_ID,'python':sys.version,'executable':sys.executable,'kernel':'python3',
 'order_id':'BI01-FO01-N-TIME-EXPRESSION-10','plan_path':str(ARTIFACT_DIR/'TIME_EXPRESSION_PLAN.json'),'plan_version':PLAN['version'],
 'actual_aidata_head':subprocess.check_output(['git','-C',str(AIDATA_WORKTREE),'rev-parse','HEAD']).decode().strip(),'modules':{}}
for mod in (uplot,nd,ec,nt):
 p=Path(inspect.getfile(mod)).resolve();RUNTIME['modules'][mod.__name__]={'file':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
(EVIDENCE/'EXECUTION_RUNTIME.json').write_text(json.dumps(RUNTIME,ensure_ascii=False,indent=2))
LAYOUTS,BUNDLES,AUDITS={},{},{}
def clean(value):
 import numpy as np
 if isinstance(value,dict):return {str(k):clean(v) for k,v in value.items()}
 if isinstance(value,(tuple,list)):return [clean(v) for v in value]
 if isinstance(value,(pd.Series,pd.Index,np.ndarray)):return clean(value.tolist())
 if isinstance(value,np.generic):return clean(value.item())
 if value is pd.NA or value is pd.NaT:return None
 if isinstance(value,float) and not np.isfinite(value):return None
 if isinstance(value,(pd.Timestamp,datetime.datetime,datetime.date,Path)):return str(value)
 return value
print('本次真实新kernel',EXECUTION_ID,RUNTIME['actual_aidata_head'])
'''
setcell('r0011-03',helpers)
setcell('r0011-04','## 原切点、查询准备与明确的点式对照\n不调用sparse_evolution/build_evolution_bundle。不用当前末值或后来成员回填较早K。\n')
setcell('r0011-05','''
rb_price=frame_at(PLAN['source_refs']['W02'],W02+'data/same_bound_price/rb_5m_price_calendar.csv',False)
i_price=frame_at(PLAN['source_refs']['W02'],W02+'data/i_missing_context/i_5m_price_calendar.csv',False)
rb_cuts={name:cut_tables(PLAN['source_refs']['W02'],W02+'data/selected_cuts/'+name+'/') for name in PLAN['rb_cuts']}
i_cuts={name:cut_tables(PLAN['source_refs']['W03'],W03+'data/crossk/'+name+'/') for name in PLAN['i_cuts']}
MEMBER_ROLES=nt.member_role_changes(rb_cuts['before_confirmation'],rb_cuts['at_or_after_confirmation'],symbol='rb')
(EVIDENCE/'RB_MEMBER_ROLE_CHANGES.json').write_text(json.dumps(clean(MEMBER_ROLES),ensure_ascii=False,indent=2))
QUERY_BUNDLES={};EXPECTATIONS={}
for symbol,cuts,price in [('rb',rb_cuts,rb_price),('i',i_cuts,i_price)]:
 for name,tables in cuts.items():
  K=PLAN[symbol+'_cuts'][name];start=PLAN['time_expression'][symbol].get('primary_price_start',PLAN['time_expression'][symbol].get('price_start'))
  b=nd.build_selected_cut_bundle(tables,price,symbol=symbol,color=PLAN['instrument_colors'][symbol],as_of=K,
      optional_panels=tuple(PLAN['time_expression'][symbol]['optional_panels']),display_range=(start,K))
  b.meta['formal_entry']='Pinned normal OnlyRead export reuse; not a fresh product computation'
  QUERY_BUNDLES[(symbol,name)]=b
  raw_values={}
  for table in ('working_progress','working_efficiency','working_counter','working_duration','working_waiting','working_waiting_ratio'):
   rows=tables[table].reset_index();assert len(rows)==1
   raw_values[table]=clean(rows.iloc[0].to_dict())
  EXPECTATIONS[symbol+'_'+name]={'K':K,'exact':b.meta['source_exact'],'raw_formal_values':raw_values,'meta':clean(b.meta)}
(EVIDENCE/'FORMAL_CUT_EXPECTATIONS.json').write_text(json.dumps(clean(EXPECTATIONS),ensure_ascii=False,indent=2))

def finish_comparison_axes(layout,prepared,contexts):
 # 本场景显式使用原K坐标；不使用样本序号，不让事后范围进入查询。
 Ks=[c['K'] for c in contexts];gap=min(b-a for a,b in zip(Ks,Ks[1:]));margin=.7*gap
 labels={c['K']:c['natural_time'][5:16]+' / K'+str(c['K']) for c in contexts}
 for fig in layout.references():
  if not hasattr(fig,'x_range') or 'aidata_bounded_panel' not in getattr(fig,'tags',[]):continue
  if 'panel:price' in fig.tags:continue
  fig.x_range=Range1d(min(Ks)-margin,max(Ks)+margin)
  for axis in fig.xaxis:axis.ticker=FixedTicker(ticks=Ks);axis.major_label_overrides=labels;axis.major_label_text_font_size='8pt'
  for label in fig.select({'type':LabelSet}):
   if 'aidata_value_label' not in label.tags:continue
   values=label.source.data.get('y',[]);lo,hi=fig.y_range.start,fig.y_range.end
   # 仅文字屏幕偏移；真实值/坐标不改，零值和最高点都留在框内。
   label.source.data={**label.source.data,'time_label_dy':[-18 if y>hi-.22*(hi-lo) else 8 for y in values]}
   label.y_offset={'field':'time_label_dy'}
   if 'CalendarUTITick' in fig.title.text:
    label.source.data={**label.source.data,'display_value':[f'{y:.6g}' for y in values]}
    # 数值旁短标，量纲仍明确写在本面板标题；不改变任何值或坐标。

def render_time(symbol,name,mode):
 if mode=='query':
  b=deepcopy(QUERY_BUNDLES[(symbol,name)])
  reference=nt.time_context(QUERY_BUNDLES[('rb','at_or_after_confirmation')]) if symbol=='rb' and name=='final' else None
  prepared=nt.prepare_time_query(b,scene_version=PLAN['version'],roles=MEMBER_ROLES['changes'] if symbol=='rb' else (),previous_same_life=reference)
  contexts=[b.meta['time_context']];case=symbol+'_query_'+name
 else:
  names=PLAN['time_expression'][symbol].get('primary_pair',PLAN['time_expression'][symbol].get('comparison_cuts'))
  prepared,b,contexts=nt.prepare_cut_comparison([deepcopy(QUERY_BUNDLES[(symbol,n)]) for n in names],
       scene_version=PLAN['version'],roles=MEMBER_ROLES['changes'] if symbol=='rb' else ())
  case=symbol+'_comparison'
 layout=ec.compose_prepared_display(prepared,context=context,calendar_name=PLAN['calendar'])
 if mode=='comparison':finish_comparison_axes(layout,prepared,contexts)
 if mode=='query':
  # 单K时仅把正式年龄的文字放在点左侧，避免与相近完成时长标签重叠。
  for label in layout.select({'type':LabelSet}):
   if 'view:working_duration_points' in label.tags:
    label.x_offset=-12;label.text_align='right';label.y_offset=-36
 layout.name='worker10:'+case;layout.tags=[*layout.tags,'worker10','case:'+case,'execution:'+EXECUTION_ID]
 folder=ARTIFACT_DIR/'plot_view_data'/case;nd.export_plot_view_data(b,folder)
 (folder/'ACTUAL_DISPLAY_BINDINGS.json').write_text(json.dumps(clean({'spec':prepared.spec,
   'anchors':[{k:v for k,v in a.items() if k!='feature'} for a in prepared.anchors],
   'identity':prepared.identity,'time_contexts':contexts,'qualification':'实际场景绑定；继承N视图配置另在原manifest，不把新增scene键说成通用API'}),ensure_ascii=False,indent=2))
 renderers=[{'tags':r.tags,'glyph':type(r.glyph).__name__,'data':clean(r.data_source.data)} for r in layout.select({'type':GlyphRenderer}) if any(str(t).startswith('anchor:n_display/') for t in r.tags)]
 AUDITS[case]={'execution_id':EXECUTION_ID,'meta':clean(b.meta),'contexts':clean(contexts),'identity':prepared.identity,'renderers':renderers}
 (EVIDENCE/'KERNEL_RENDERER_AUDIT.json').write_text(json.dumps(clean(AUDITS),ensure_ascii=False,indent=2))
 LAYOUTS[case]=layout;BUNDLES[case]=b;show(layout);return layout
''')
setcell('r0011-06','''
rb_K=widgets.Dropdown(options=list(PLAN['rb_cuts']),value='before_confirmation',description='rb知识K')
rb_mode=widgets.Dropdown(options=[('所选K当时可知','query'),('事后确认两切点对照','comparison')],value='query',description='阅读模式')
rb_out=widgets.Output()
def display_rb(change=None):
 with rb_out:
  clear_output(wait=True);render_time('rb',rb_K.value,rb_mode.value)
rb_K.observe(display_rb,names='value');rb_mode.observe(display_rb,names='value')
display(widgets.HBox([rb_mode,rb_K]),rb_out);display_rb()
''')
setcell('r0011-07','## i：整体年龄、局部时钟与部分恢复\n从缺价末拍回看到恢复和后一拍；真实零、缺值、未覆盖起点分别保留。\n')
setcell('r0011-08','''
i_K=widgets.Dropdown(options=list(PLAN['i_cuts']),value='i_before_missing_recovery',description='i知识K')
i_mode=widgets.Dropdown(options=[('所选K当时可知','query'),('事后三切点对照','comparison')],value='query',description='阅读模式')
i_out=widgets.Output()
def display_i(change=None):
 with i_out:
  clear_output(wait=True);render_time('i',i_K.value,i_mode.value)
i_K.observe(display_i,names='value');i_mode.observe(display_i,names='value')
display(widgets.HBox([i_mode,i_K]),i_out);display_i()
''')
setcell('r0011-09','## 本次新用途的资格与完整未完\n事后图不是完整发生历史，不把revision UUID变化标为历史纠错。原M37四视域不变；本单新用途待原Pro/管理接收。无共享服务、DAO或平台操作，无工作4。\n')
setcell('r0011-10','''
(EVIDENCE/'SOURCE_READS.json').write_text(json.dumps(SOURCE_READS,ensure_ascii=False,indent=2))
(EVIDENCE/'KERNEL_COMPLETION.json').write_text(json.dumps({'execution_id':EXECUTION_ID,'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'cases':list(LAYOUTS),'qualification':'新kernel默认图完成；后续真实控件/比较/像素证据另记，不预签'},ensure_ascii=False,indent=2))
print('本次新kernel已执行默认查询图；实际控件回看/事后对照和像素由当前活会话核验，未采用共享平台。')
''')
for c in nb['cells']:
 c['metadata']={}
 if c['cell_type']=='code':c['execution_count']=None;c['outputs']=[]
nb['metadata']={'kernelspec':{'display_name':'Python 3 (ipykernel)','language':'python','name':'python3'},
 'worker_order':{'order_id':'BI01-FO01-N-TIME-EXPRESSION-10','issuer_invocation_id':'BI01-FO-01-R0038-20261024T222007Z-a5dc9677',
 'source_notebook_commit':REF,'source_notebook_blob':'b271fe3541166a1e04d216bd845d59e8f7b25123','source_sha256':hashlib.sha256(raw).hexdigest(),
 'qualification':'旧输出清空；本单须新kernel真实执行，不复用W09执行或像素'}}
(OUT/'N_time_expression_Worker10.ipynb').write_text(json.dumps(nb,ensure_ascii=False,indent=1)+'\n')
(OUT/'evidence/REVISION_PROVENANCE.json').write_text(json.dumps(nb['metadata']['worker_order'],ensure_ascii=False,indent=2)+'\n')
print('W10 Notebook prepared from exact W09, outputs cleared; not executed')
