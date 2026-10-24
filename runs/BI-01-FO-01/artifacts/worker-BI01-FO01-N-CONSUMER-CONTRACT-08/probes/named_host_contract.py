"""已有BaseCAEFao独立宿主的隔离构造探针；不运行layout、不注册DAO。"""
from pathlib import Path
import argparse,contextlib,hashlib,json,logging,os,sys

parser=argparse.ArgumentParser();parser.add_argument('--prewarm-json',action='store_true')
args=parser.parse_args()

rt=Path(os.environ['BI01_W08_RUNTIME'])
logging.disable(logging.CRITICAL)
result={'scope':'isolated constructor/serialization only; no platform registration, layout or new drawing',
        'source_capability':'mquant.frame.BaseCAEFao + CAEFaoMixIn.doShowCAEGraph + normal CaeNodeDao.node2fao'}
with (rt/'named-host-library.private.log').open('a') as log,contextlib.redirect_stdout(log),contextlib.redirect_stderr(log):
 try:
  os.environ.setdefault('M3ROOT','/m3c3');os.environ.setdefault('M3WORKS','/dwdhome/fy/BASE_E6_2')
  sys.path[:0]=['/tmp/bi01-fo01-w03-runtime-20261022','/dwdhome/fy/BASE_E6_2']
  import mquant
  overlay=rt/'import-cbd';overlay.mkdir(exist_ok=True)
  link=overlay/'aidata'
  if not link.exists():link.symlink_to('/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-platform-board-r0022',target_is_directory=True)
  mquant.__path__.insert(0,str(overlay))
  from mquant.frame import BaseCAEFao,StraApp,EvalCtx
  from mquant.quant import OptContext
  from mquant.quant.models.graph import CaeNodeDao
  result['json_initialized_before_class']=EvalCtx._json_ctx is not None
  if args.prewarm_json:
   namespace=EvalCtx.json_ctx
  result['prewarm_requested']=args.prewarm_json

  class Worker08NamedNHostProbe(BaseCAEFao):
   """仅为验证正常宿主构造合同；不是本次获准上线的类。"""
   params=lambda:{'run_dir':'','run_id':'','big_node_id':'','context':None,'calendar_name':''}
   def hold_on_bokeh_server(self):return True
   def layout(self,*args,**kwargs):
    from mquant.aidata.normal_node_behavior import render_node
    return render_node(self)

  run=Path('/dwdhome/fy/observe-iterate-bi01-fo-01/artifacts/bi01-worker07-runs/BI01-FO01-W07-20261024T0028-rb')
  n=Worker08NamedNHostProbe(dict(run_dir=str(run),run_id=run.name,big_node_id='big_000002',
      context=OptContext(sof_name='TA_updto20240229_DBA'),calendar_name='night_end_at_2300'))
  result.update(memory_keys=sorted(dict(n.P)),bokeh_server=n.prop_on_bokeh_server,serialized_representation=n.fason,
    manifest_exists=(run/'manifest/normal_node_behavior.json').is_file(),
    class_known_in_this_process=StraApp.get_class('Worker08NamedNHostProbe') is not None,
    qualification='类只存在本探针进程；未加载到正常Trier/Bokeh、未创建节点，未调用本layout')
  result['class_in_actual_eval_namespace']=hasattr(EvalCtx.json_ctx,'Worker08NamedNHostProbe')
  try:
   recovered=CaeNodeDao.node2fao({'params':n.fason,'cls_name':'Worker08NamedNHostProbe'})
   result['normal_restore']={'status':'accepted','keys':sorted(dict(recovered.P))}
  except Exception as exc:
   result['normal_restore']={'status':'rejected','type':type(exc).__name__,
       'unknown_name':'Worker08NamedNHostProbe' if 'Worker08NamedNHostProbe' in str(exc) else None}
  # 证明独立宿主无需往共享普通类增加字段；不声称cbd分支自身已移除该字段。
  result['shared_class_source_changed']=False
 except Exception as exc:
  result['fatal_error']={'type':type(exc).__name__}
  import traceback;traceback.print_exc()
(rt/('NAMED_HOST_PREWARMED.json' if args.prewarm_json else 'NAMED_HOST_CONSTRUCTOR.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='serialized_representation'},ensure_ascii=False))
