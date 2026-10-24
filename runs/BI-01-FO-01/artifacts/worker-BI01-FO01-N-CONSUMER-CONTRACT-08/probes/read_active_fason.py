"""取既有共享类实例的活动展开合同；没有新N键不等于非N业务对象。"""
from pathlib import Path
import ast,contextlib,datetime,hashlib,json,logging,os,sys,urllib.parse,urllib.request
rt=Path(__file__).parent
logging.disable(logging.CRITICAL)
result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'existing shared-class instance without the new N key; read-only query/doc, no run/layout/node write'}
with (rt/'active-fason-library.private.log').open('a') as log,contextlib.redirect_stdout(log),contextlib.redirect_stderr(log):
 try:
  os.environ.setdefault('M3ROOT','/m3c3');os.environ.setdefault('M3WORKS','/dwdhome/fy/BASE_E6_2')
  sys.path[:0]=['/tmp/bi01-fo01-w03-runtime-20261022','/dwdhome/fy/BASE_E6_2']
  from mquant.quant.db import provide_graph_repo
  from mquant.quant.models.graph import FaoLabelConfig
  @provide_graph_repo
  def select_one(repo):
   return repo.graph.run('MATCH (n:'+FaoLabelConfig.Cae+') WHERE n.cls_name=$name AND n.params STARTS WITH $prefix AND NOT n.params CONTAINS $nkey RETURN id(n) AS node_id ORDER BY id(n) DESC LIMIT 1',
       name='AidataBigWorldReviewCAE',prefix='AidataBigWorldReviewCAE(',nkey='normal_node_behavior_manifest').data()
  found=select_one()
  if not found:result['no_existing_ordinary_node']=True
  else:
   node_id=int(found[0]['node_id'])
   old=json.loads(Path('/dwdhome/fy/cgpterm/artifacts/bi01-worker07-runtime/rb-pages.private.json').read_text())[0]['report_url']
   parts=urllib.parse.urlsplit(old);assert not parts.username and not parts.password
   route=f'/api/graph/fao/{node_id}/doc'
   url=urllib.parse.urlunsplit((parts.scheme,parts.netloc,route,'',''))
   with urllib.request.build_opener(urllib.request.ProxyHandler({})).open(url,timeout=30) as response:
    raw=response.read();result['http_status']=response.status
   (rt/'ACTIVE_ORDINARY_DOC_RESPONSE.private.json').write_bytes(raw)
   decoded=json.loads(raw)
   result['application_code']=decoded.get('code') if isinstance(decoded,dict) else None
   def find(value):
    if isinstance(value,dict):
     if '_fason_' in value:return value['_fason_']
     for v in value.values():
      x=find(v)
      if x is not None:return x
    return None
   serial=find(decoded)
   result.update(node_id=node_id,route=route,response_sha256=hashlib.sha256(raw).hexdigest())
   if serial is None:result['fason_missing']=True
   else:
    parsed=ast.parse(serial,mode='eval').body
    keys=[k.value for k in parsed.args[0].keys if isinstance(k,ast.Constant) and isinstance(k.value,str)]
    result.update(active_fason_class=ast.unparse(parsed.func),effective_expanded_parameter_keys=keys,
       n_parameter_present='normal_node_behavior_manifest' in keys,
       fason_sha256=hashlib.sha256(serial.encode()).hexdigest(),
       qualifier='fason is produced by the active Trier process using its actual loaded class; module __file__/live bytecode not exposed')
 except Exception as exc:
  result['error_type']=type(exc).__name__
  import traceback;traceback.print_exc()
(rt/'ACTIVE_TRIER_FASON_OBSERVATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
