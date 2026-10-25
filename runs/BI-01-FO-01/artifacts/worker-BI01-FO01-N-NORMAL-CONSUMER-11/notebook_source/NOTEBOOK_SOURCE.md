# Worker11 实际执行Notebook：精确有序源码

主文件 N_normal_consumer_Worker11.ipynb；7600640 bytes；SHA256 53e1947a18b2b556aef66e0eef3924eb26c599a736278157eabb2795178a085c。

此副本不是完整Notebook：每个cell的source全文逐字保留，大段内嵌JS/widget/图形保存输出不展开，仅列MIME/位置/错误/hash；完整输出仍在主ipynb。

## 0. r0011-00 / markdown / execution_count=None

metadata: {}

````markdown
# Worker11：已认可时间用途的正常消费者验证

同BI-01-FO-01的有界工作3隔离接入，非新业务Run/共享平台发布。所有图从正常保存Fao恢复并调用普通AidataBigWorldReviewCAE.layout；不调用旧render_time，不在Notebook保留轴/标签后处理。逐K正式交付在同选择正常board/依赖。无共享服务、DAO或工作4动作。
````

输出索引：[]

## 1. r0011-01 / code / execution_count=1

metadata: {}

````python
import logging
logging.disable(logging.CRITICAL)
from pathlib import Path
import sys, os, json, importlib.util, datetime, uuid
ARTIFACT_DIR = Path(os.environ.get("BI01_W11_ARTIFACT_DIR", ".")).resolve()
AIDATA_WORKTREE = Path(os.environ.get("BI01_W11_AIDATA", "/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-normal-consumer-r0041"))
# 沿已有只读运行overlay采用修后TIS/worker；aidata覆盖为本单独立分支。
sys.path.insert(0, "/tmp/bi01-fo01-w03-runtime-20261022")
import mquant
import tempfile
IMPORT_OVERLAY = Path(tempfile.mkdtemp(prefix="bi01-w11-import-"))
(IMPORT_OVERLAY / "aidata").symlink_to(AIDATA_WORKTREE, target_is_directory=True)
mquant.__path__.insert(0, str(IMPORT_OVERLAY))
missing = [name for name in ("mquant", "ipywidgets") if importlib.util.find_spec(name) is None]
if missing:
    raise RuntimeError("现场依赖缺：" + str(missing))
EXECUTION_ID = "W11-" + datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
print("本次新kernel执行", EXECUTION_ID, sys.executable)
````

输出索引：[{"position": 0, "output_type": "stream", "mime_types": [], "ename": null, "bytes_json": 148, "sha256_json": "745e9ec4b438db97d415525cc8b3823b090e6c908df9ab01d6008805f05591ca"}]

## 2. r0011-02 / markdown / execution_count=None

metadata: {}

````markdown
## 正常持久输入与本次实际版本
从已建立的正常观察run和保存Fao恢复；旧W10只是上游画法，不是本单新执行。
````

输出索引：[]

## 3. r0011-03 / code / execution_count=2

metadata: {}

````python

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
````

输出索引：[{"position": 0, "output_type": "display_data", "mime_types": ["application/javascript", "application/vnd.bokehjs_load.v0+json"], "ename": null, "bytes_json": 7574259, "sha256_json": "b7d74e48621e4d9f41e21d6226e8836df28c4bc9fac1a94e41acdb486c22e6b6"}, {"position": 1, "output_type": "stream", "mime_types": [], "ename": null, "bytes_json": 155, "sha256_json": "6dec439fe078c8c7dd398119b5b5a6e658ca00dae6f2de71d1b1bc3d94f4ae95"}]

## 4. r0011-04 / markdown / execution_count=None

metadata: {}

````markdown
## 图与正式资料来自同一正常选择
一幅图可含多个原K，但不是新正式多K产品。每K正式主结果与合法早期参照分别保留，原价/显示域/知识范围分开。
````

输出索引：[]

## 5. r0011-05 / code / execution_count=3

metadata: {}

````python

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
````

输出索引：[]

## 6. r0011-06 / code / execution_count=4

metadata: {}

````python

rb_K=widgets.Dropdown(options=list(PLAN['rb_cuts']),value='before_confirmation',description='rb知识K')
rb_mode=widgets.Dropdown(options=[('所选K当时可知','query'),('事后确认两切点对照','comparison')],value='query',description='阅读模式')
rb_out=widgets.Output()
def display_rb(change=None):
 with rb_out:
  clear_output(wait=True);render_normal('rb',rb_K.value,rb_mode.value)
rb_K.observe(display_rb,names='value');rb_mode.observe(display_rb,names='value')
display(widgets.HBox([rb_mode,rb_K]),rb_out);display_rb()
````

输出索引：[{"position": 0, "output_type": "display_data", "mime_types": ["application/vnd.jupyter.widget-view+json", "text/plain"], "ename": null, "bytes_json": 362, "sha256_json": "9a31bd1b3508fabc46f3d2c0579b6e6d0e437d61d4700f01512c891cffe1ec4a"}, {"position": 1, "output_type": "display_data", "mime_types": ["application/vnd.jupyter.widget-view+json", "text/plain"], "ename": null, "bytes_json": 219, "sha256_json": "6d963bb77536ca888744d4a6cb94161fc6660a85ae15a635ed4b710e9f126f20"}]

## 7. r0011-07 / markdown / execution_count=None

metadata: {}

````markdown
## i：正常消费者里的缺/0/600及同一working
模式与K选择映射到具名正常观察run/node，并从其保存Fao恢复；不是NB内存bundle。
````

输出索引：[]

## 8. r0011-08 / code / execution_count=5

metadata: {}

````python

i_K=widgets.Dropdown(options=list(PLAN['i_cuts']),value='i_before_missing_recovery',description='i知识K')
i_mode=widgets.Dropdown(options=[('所选K当时可知','query'),('事后三切点对照','comparison')],value='query',description='阅读模式')
i_out=widgets.Output()
def display_i(change=None):
 with i_out:
  clear_output(wait=True);render_normal('i',i_K.value,i_mode.value)
i_K.observe(display_i,names='value');i_mode.observe(display_i,names='value')
display(widgets.HBox([i_mode,i_K]),i_out);display_i()
````

输出索引：[{"position": 0, "output_type": "display_data", "mime_types": ["application/vnd.jupyter.widget-view+json", "text/plain"], "ename": null, "bytes_json": 358, "sha256_json": "8601a7ef834a79f12f9c89d6f6bcaee0dd09da9269dbd029fd7445a6231952a9"}, {"position": 1, "output_type": "display_data", "mime_types": ["application/vnd.jupyter.widget-view+json", "text/plain"], "ename": null, "bytes_json": 219, "sha256_json": "e3e8fa49ce4bca12e7c1ce927c614f8b3a4da4d522e914e2867e146bfc3e6870"}]

## 9. r0011-09 / markdown / execution_count=None

metadata: {}

````markdown
## 当前资格与保护面
这是隔离环境实际普通CAE/bridge/同node正式资料核验，不是共享Trier/Bokeh采用或正常平台URL。原25a路线保持；未操作注册/DAO/旧6128—6131或正式工作4。
````

输出索引：[]

## 10. r0011-10 / code / execution_count=6

metadata: {}

````python
(EVIDENCE/'KERNEL_COMPLETION.json').write_text(json.dumps(dict(execution_id=EXECUTION_ID,cases=list(LAYOUTS),actual_normal_CAE=True,platform_registration=False),ensure_ascii=False,indent=2))
print('本次新kernel默认普通CAE图完成；实际导航/回看/像素证据另记。')
````

输出索引：[{"position": 0, "output_type": "stream", "mime_types": [], "ename": null, "bytes_json": 142, "sha256_json": "fd50f3c288bd75463b5de79d6e36f45b6498e88e730eeeac4e3e4b8687bba3f9"}]
