import os
"""从W10准确实物派生，清旧输出；新的读图路径只走正常持久Fao/普通CAE。"""
from pathlib import Path
import hashlib,json,subprocess
repo=Path('/dwdhome/fy/observe-iterate-bi01-fo-01');rt=Path(os.environ.get('BI01_W11_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker11-runtime'))
out=repo/'runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-NORMAL-CONSUMER-11';out.mkdir(parents=True,exist_ok=True)
ref='e4ada20368ccb6ef5b16993b7954fcff957be5ef';prefix='runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-TIME-EXPRESSION-10/'
raw=subprocess.check_output(['git','-C',str(repo),'show',ref+':'+prefix+'N_time_expression_Worker10.ipynb'])
assert subprocess.check_output(['git','hash-object','--stdin'],input=raw,text=False).decode().strip()=='3858c701904c7ef0c05d52f4fc12da76d5ddaffe'
nb=json.loads(raw);cells={c['id']:c for c in nb['cells']}
def source(id,text):cells[id]['source']=text.splitlines(keepends=True)
source('r0011-00','# Worker11：已认可时间用途的正常消费者验证\n\n同BI-01-FO-01的有界工作3隔离接入，非新业务Run/共享平台发布。所有图从正常保存Fao恢复并调用普通AidataBigWorldReviewCAE.layout；不调用旧render_time，不在Notebook保留轴/标签后处理。逐K正式交付在同选择正常board/依赖。无共享服务、DAO或工作4动作。\n')
first=''.join(cells['r0011-01']['source']).replace('W10','W11').replace('bi01-w10','bi01-w11').replace('aidata-bi01-fo01-n-time-expression-r0038','aidata-bi01-fo01-n-normal-consumer-r0041')
source('r0011-01',first)
source('r0011-02','## 正常持久输入与本次实际版本\n从已建立的正常观察run和保存Fao恢复；旧W10只是上游画法，不是本单新执行。\n')
source('r0011-03','''
import inspect,subprocess,hashlib,io
import pandas as pd,numpy as np
from bokeh.io import output_notebook,show
from bokeh.resources import INLINE
from bokeh.models import GlyphRenderer
from IPython.display import display,clear_output
import ipywidgets as widgets
from mquant.quant.models.graph import CaeNodeDao
from mquant.aidata.contracts import build_run_handle
from mquant.aidata.evidence_composition import prepare_node_evidence
import mquant.aidata.evidence_composition as ec
import mquant.aidata.normal_node_behavior as nn
import mquant.aidata.normal_node_behavior_time as nc
import mquant.aidata.u2_normal_node_behavior_display as nd
import mquant.aidata.u2_normal_node_behavior_time as nt
import mquant.aidata.big_world_chart as bw
RT=Path(os.environ.get('BI01_W11_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker11-runtime'))
CASES=json.loads((RT/'BUILT_RUNS.json').read_text())['cases'];BY_CASE={c['case']:c for c in CASES}
EVIDENCE=ARTIFACT_DIR/'evidence';EVIDENCE.mkdir(exist_ok=True)
PLAN=json.loads(Path(json.loads((Path(CASES[0]['run_dir'])/'manifest/normal_node_behavior.json').read_text())['scene']['path']).read_text())
output_notebook(resources=INLINE,hide_banner=True)
def clean(v):
 if isinstance(v,dict):return {str(k):clean(x) for k,x in v.items()}
 if isinstance(v,(list,tuple,pd.Series,pd.Index,np.ndarray)):return [clean(x) for x in v]
 if isinstance(v,np.generic):return clean(v.item())
 if v is pd.NA or v is pd.NaT:return None
 if isinstance(v,float) and not np.isfinite(v):return None
 if isinstance(v,(pd.Timestamp,datetime.datetime,Path)):return str(v)
 return v
RUNTIME=dict(execution_id=EXECUTION_ID,order_id='BI01-FO01-N-NORMAL-CONSUMER-11',python=sys.version,executable=sys.executable,kernel='python3',
 actual_aidata_head=subprocess.check_output(['git','-C',str(AIDATA_WORKTREE),'rev-parse','HEAD'],text=True).strip(),
 scene_version=PLAN['version'],normal_consumer_version=nc.CONSUMER_VERSION,modules={})
for mod in (nn,nc,nt,nd,ec,bw):
 p=Path(inspect.getfile(mod)).resolve();RUNTIME['modules'][mod.__name__]=dict(file=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
(EVIDENCE/'EXECUTION_RUNTIME.json').write_text(json.dumps(RUNTIME,ensure_ascii=False,indent=2))
LAYOUTS={};AUDITS={}
print('本次新kernel/普通CAE',EXECUTION_ID,RUNTIME['actual_aidata_head'])
''')
source('r0011-04','## 图与正式资料来自同一正常选择\n一幅图可含多个原K，但不是新正式多K产品。每K正式主结果与合法早期参照分别保留，原价/显示域/知识范围分开。\n')
source('r0011-05','''
EXPECTATIONS={}
for case in CASES:
 s=nn._descriptor_selection(case['descriptor'])
 for cut in s['cuts']:
  key=s['symbol']+'_'+next(n for n,k in PLAN[s['symbol']+'_cuts'].items() if k==cut['as_of'])
  frames={name:nn.read_frame(spec) for name,spec in cut['tables'].items()}
  root=nd._occurrences(frames,s['symbol']).iloc[0]
  raw={table:clean(frames[table].reset_index().iloc[0].to_dict()) for table in ('working_progress','working_efficiency','working_counter','working_duration','working_waiting','working_waiting_ratio')}
  EXPECTATIONS[key]=dict(K=cut['as_of'],exact=cut['expected_exact'],raw_formal_values=raw,working_life=str(root.working_life))
(EVIDENCE/'FORMAL_CUT_EXPECTATIONS.json').write_text(json.dumps(EXPECTATIONS,ensure_ascii=False,indent=2))
def render_normal(symbol,name,mode):
 case_name=symbol+'_comparison' if mode=='comparison' else symbol+'_query_'+name
 c=BY_CASE[case_name];payload=Path(c['fason_private_path']).read_text()
 assert hashlib.sha256(payload.encode()).hexdigest()==c['fason_sha256']
 obj=CaeNodeDao.node2fao({'params':payload,'cls_name':'AidataBigWorldReviewCAE'})
 assert obj.fason==payload and obj.ppid==c['ppid']
 # 唯一实际构图入口：正常持久恢复后的普通CAE；没有旧Notebook后处理。
 layout=obj.layout();layout.name='worker11:'+case_name
 layout.tags=[*layout.tags,'worker11','case:'+case_name,'execution:'+EXECUTION_ID,'normal_run:'+c['run_id'],'normal_node:'+c['node_id']]
 # 独立从同一选择再取投影作核图，不用该准备器代替上面的真实CAE构图。
 prepared=prepare_node_evidence([c['descriptor']],run_dir=c['run_dir'],node_id=c['node_id'])
 b=prepared.feature.bundle;folder=ARTIFACT_DIR/'plot_view_data'/case_name;nd.export_plot_view_data(b,folder)
 selection=nn._descriptor_selection(c['descriptor'])
 binding=dict(run_id=c['run_id'],node_id=c['node_id'],purpose=selection['purpose'],knowledge_ks=selection['knowledge_ks'],
  primary_and_reference=[nc._cut_role(selection,cut['as_of']) for cut in selection['cuts']],spec=prepared.spec,
  reading_policy=prepared.reading_policy,identity=prepared.identity,descriptor=c['descriptor'],
  qualification='实际普通CAE另构图；此处同源图用投影/绑定只用于核显示，非正式多K产品')
 (folder/'ACTUAL_NORMAL_SELECTION.json').write_text(json.dumps(clean(binding),ensure_ascii=False,indent=2))
 renderers=[dict(tags=r.tags,glyph=type(r.glyph).__name__,data=clean(r.data_source.data)) for r in layout.select({'type':GlyphRenderer}) if any(str(t).startswith('anchor:n_display/') for t in r.tags)]
 AUDITS[case_name]=dict(execution_id=EXECUTION_ID,normal_run=c['run_id'],node=c['node_id'],ppid=obj.ppid,fason_sha256=c['fason_sha256'],binding=binding,renderers=renderers)
 (EVIDENCE/'KERNEL_RENDERER_AUDIT.json').write_text(json.dumps(clean(AUDITS),ensure_ascii=False,indent=2))
 LAYOUTS[case_name]=layout;show(layout);return layout
''')
source('r0011-06',''.join(cells['r0011-06']['source']).replace("render_time('rb'","render_normal('rb'"))
source('r0011-07','## i：正常消费者里的缺/0/600及同一working\n模式与K选择映射到具名正常观察run/node，并从其保存Fao恢复；不是NB内存bundle。\n')
source('r0011-08',''.join(cells['r0011-08']['source']).replace("render_time('i'","render_normal('i'"))
source('r0011-09','## 当前资格与保护面\n这是隔离环境实际普通CAE/bridge/同node正式资料核验，不是共享Trier/Bokeh采用或正常平台URL。原25a路线保持；未操作注册/DAO/旧6128—6131或正式工作4。\n')
source('r0011-10',"(EVIDENCE/'KERNEL_COMPLETION.json').write_text(json.dumps(dict(execution_id=EXECUTION_ID,cases=list(LAYOUTS),actual_normal_CAE=True,platform_registration=False),ensure_ascii=False,indent=2))\nprint('本次新kernel默认普通CAE图完成；实际导航/回看/像素证据另记。')\n")
for c in nb['cells']:
 c['metadata']={}
 if c['cell_type']=='code':c['execution_count']=None;c['outputs']=[]
nb['metadata']={'kernelspec':{'display_name':'Python 3 (ipykernel)','language':'python','name':'python3'},
 'worker_order':dict(order_id='BI01-FO01-N-NORMAL-CONSUMER-11',issuer_invocation_id='BI01-FO-01-R0041-20261025T010254Z-8cf5489e',
 source_notebook_commit=ref,source_notebook_blob='3858c701904c7ef0c05d52f4fc12da76d5ddaffe',source_sha256=hashlib.sha256(raw).hexdigest(),
 qualification='W10准确谱系，新普通消费者执行；旧输出清空，不保留finish_comparison_axes或query标签后处理')}
(out/'N_normal_consumer_Worker11.ipynb').write_text(json.dumps(nb,ensure_ascii=False,indent=1)+'\n')
(out/'scripts').mkdir(exist_ok=True);(out/'evidence').mkdir(exist_ok=True)
print('prepared new W11 normal-consumer notebook; not yet executed')
