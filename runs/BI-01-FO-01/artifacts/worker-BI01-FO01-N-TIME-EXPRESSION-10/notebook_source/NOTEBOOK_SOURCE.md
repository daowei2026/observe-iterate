# Worker10 实际执行Notebook：精确有序源码

主文件 N_time_expression_Worker10.ipynb；7606013 bytes；SHA256 1f8abd97a83886e1daf4cf9c582040adcc5cac40f73e1753931f2452954025e0。

此副本不是完整Notebook：每个cell的source全文逐字保留，大段内嵌JS/widget/图形保存输出不展开，仅列MIME/位置/错误/hash；完整输出仍在主ipynb。

## 0. r0011-00 / markdown / execution_count=None

metadata: {}

````markdown
# Worker10｜已知切点的时间解释与真实回看

BI01-FO01-N-TIME-EXPRESSION-10；原Pro R0038签发。本次只做工作1/2的新时间表达，不修改M37已认可四视域或进入工作4。
从W09确切主Notebook派生并清旧输出；源为W02/W03锁定正常原表，不是旧图用CSV，不重算N。
“所选K当时可知”和“事后并列所列切点”明确分开。仅六个已供准确K，不提供任意K全历史；没有连续保持线或插值。
下面的实际图由既有Uplot/共用组合构建；新时间准备器只返回有限视图/注记，不返回任意layout。新用途待原Pro与管理判断。
````

输出索引：[]

## 1. r0011-01 / code / execution_count=1

metadata: {}

````python
import logging
logging.disable(logging.CRITICAL)
from pathlib import Path
import sys, os, json, importlib.util, datetime, uuid
ARTIFACT_DIR = Path(os.environ.get("BI01_W10_ARTIFACT_DIR", ".")).resolve()
AIDATA_WORKTREE = Path(os.environ.get("BI01_W10_AIDATA", "/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-time-expression-r0038"))
# 沿已有只读运行overlay采用修后TIS/worker；aidata覆盖为本单独立分支。
sys.path.insert(0, "/tmp/bi01-fo01-w03-runtime-20261022")
import mquant
import tempfile
IMPORT_OVERLAY = Path(tempfile.mkdtemp(prefix="bi01-w10-import-"))
(IMPORT_OVERLAY / "aidata").symlink_to(AIDATA_WORKTREE, target_is_directory=True)
mquant.__path__.insert(0, str(IMPORT_OVERLAY))
missing = [name for name in ("mquant", "ipywidgets") if importlib.util.find_spec(name) is None]
if missing:
    raise RuntimeError("现场依赖缺：" + str(missing))
EXECUTION_ID = "W10-" + datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
print("本次新kernel执行", EXECUTION_ID, sys.executable)
````

输出索引：[{"position": 0, "output_type": "stream", "mime_types": [], "ename": null, "bytes_json": 148, "sha256_json": "cc35ede00fd8990e85d5801a0e0c462226b75c866ba2e109c9f52f713eb73864"}]

## 2. r0011-02 / markdown / execution_count=None

metadata: {}

````markdown
## 准确源与本次执行身份
原有读取/UInt64/空值处理复用；当前kernel、模块有效字节和源hash另记，不把W09执行冒成本次。
````

输出索引：[]

## 3. r0011-03 / code / execution_count=2

metadata: {}

````python
from pathlib import Path
from functools import lru_cache
import io, os, subprocess, inspect, hashlib
import pandas as pd
import mquant.uplot as uplot
import mquant.aidata.u2_normal_node_behavior_display as nd
import mquant.aidata.evidence_composition as ec
from mquant.quant import OptContext
from bokeh.io import output_notebook, show
from bokeh.resources import INLINE
from IPython.display import display, clear_output
import ipywidgets as widgets

# ARTIFACT_DIR 已由本单首单元设置
PLAN = json.loads((ARTIFACT_DIR / "TIME_EXPRESSION_PLAN.json").read_text(encoding="utf-8"))
REPO = Path(os.environ.get("OBSERVE_REPO", "/dwdhome/fy/observe-iterate-bi01-fo-01")).resolve()
if not REPO.is_dir():
    raise FileNotFoundError(f"实际仓库不存在：{REPO}")
W02 = "runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-DISPLAY-INTEGRATION-02/"
W03 = "runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-READABILITY-CROSSK-03/"
SOURCE_READS = {}
@lru_cache(maxsize=160)
def source_bytes(ref, path):
    result = subprocess.run(["git", "-C", str(REPO), "show", f"{ref}:{path}"], capture_output=True, check=True)
    raw = result.stdout
    SOURCE_READS[f"{ref}:{path}"] = hashlib.sha256(raw).hexdigest()
    return raw

def frame_at(ref, path, formal=True):
    frame = pd.read_csv(io.BytesIO(source_bytes(ref, path)), dtype="string")
    time_col = "timestamp" if formal else frame.columns[0]
    frame[time_col] = pd.to_datetime(frame[time_col])
    for col in frame.columns:
        if col == time_col:
            continue
        if col == "text" or col.endswith("_text"):
            frame[col] = frame[col].fillna("")
        elif col.endswith("_high") or col.endswith("_low"):
            frame[col] = pd.array(frame[col], dtype="UInt64")
        else:
            try:
                frame[col] = pd.to_numeric(frame[col], errors="raise")
            except (ValueError, TypeError):
                pass
    if not formal:
        return frame.set_index(time_col)
    children = sorted([c for c in frame if c.startswith("child_id_")], key=lambda c: int(c.rsplit("_", 1)[1]))
    return frame.set_index(["timestamp", "occurrence", "record_id", *children])

def cut_tables(ref, folder):
    return {name: frame_at(ref, folder + name + ".csv") for name in nd.FORMAL_PRODUCTS}


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
````

输出索引：[{"position": 0, "output_type": "display_data", "mime_types": ["application/javascript", "application/vnd.bokehjs_load.v0+json"], "ename": null, "bytes_json": 7574259, "sha256_json": "b7d74e48621e4d9f41e21d6226e8836df28c4bc9fac1a94e41acdb486c22e6b6"}, {"position": 1, "output_type": "stream", "mime_types": [], "ename": null, "bytes_json": 151, "sha256_json": "0d8249a307b5214ad230aee10cb1ca5239f88643688a92bd398cffd02da4b012"}]

## 4. r0011-04 / markdown / execution_count=None

metadata: {}

````markdown
## 原切点、查询准备与明确的点式对照
不调用sparse_evolution/build_evolution_bundle。不用当前末值或后来成员回填较早K。
````

输出索引：[]

## 5. r0011-05 / code / execution_count=3

metadata: {}

````python

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
  clear_output(wait=True);render_time('rb',rb_K.value,rb_mode.value)
rb_K.observe(display_rb,names='value');rb_mode.observe(display_rb,names='value')
display(widgets.HBox([rb_mode,rb_K]),rb_out);display_rb()
````

输出索引：[{"position": 0, "output_type": "display_data", "mime_types": ["application/vnd.jupyter.widget-view+json", "text/plain"], "ename": null, "bytes_json": 362, "sha256_json": "a8117930d5af7111936dbd6fada94ac319deb1f01dcee20e6f90dbd22a65ea5d"}, {"position": 1, "output_type": "display_data", "mime_types": ["application/vnd.jupyter.widget-view+json", "text/plain"], "ename": null, "bytes_json": 219, "sha256_json": "7af404edd17f9ae35e23fb8b763f02a537b482d5a887c4a4d9cc9215f09164f5"}]

## 7. r0011-07 / markdown / execution_count=None

metadata: {}

````markdown
## i：整体年龄、局部时钟与部分恢复
从缺价末拍回看到恢复和后一拍；真实零、缺值、未覆盖起点分别保留。
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
  clear_output(wait=True);render_time('i',i_K.value,i_mode.value)
i_K.observe(display_i,names='value');i_mode.observe(display_i,names='value')
display(widgets.HBox([i_mode,i_K]),i_out);display_i()
````

输出索引：[{"position": 0, "output_type": "display_data", "mime_types": ["application/vnd.jupyter.widget-view+json", "text/plain"], "ename": null, "bytes_json": 358, "sha256_json": "ede61015e294e3abc4ce3027989bd8cf2b6b321ea07939b82bcec5a374a6c136"}, {"position": 1, "output_type": "display_data", "mime_types": ["application/vnd.jupyter.widget-view+json", "text/plain"], "ename": null, "bytes_json": 219, "sha256_json": "5f83b8cc4b9c6046ddc64e4eebb418e14f7d586ee0d4c72a1483bcd8a8b80282"}]

## 9. r0011-09 / markdown / execution_count=None

metadata: {}

````markdown
## 本次新用途的资格与完整未完
事后图不是完整发生历史，不把revision UUID变化标为历史纠错。原M37四视域不变；本单新用途待原Pro/管理接收。无共享服务、DAO或平台操作，无工作4。
````

输出索引：[]

## 10. r0011-10 / code / execution_count=6

metadata: {}

````python

(EVIDENCE/'SOURCE_READS.json').write_text(json.dumps(SOURCE_READS,ensure_ascii=False,indent=2))
(EVIDENCE/'KERNEL_COMPLETION.json').write_text(json.dumps({'execution_id':EXECUTION_ID,'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'cases':list(LAYOUTS),'qualification':'新kernel默认图完成；后续真实控件/比较/像素证据另记，不预签'},ensure_ascii=False,indent=2))
print('本次新kernel已执行默认查询图；实际控件回看/事后对照和像素由当前活会话核验，未采用共享平台。')
````

输出索引：[{"position": 0, "output_type": "stream", "mime_types": [], "ename": null, "bytes_json": 192, "sha256_json": "a9dab1884802918571fdb42077a418fe03e01224e1bb06f6000c29145406a3c0"}]
