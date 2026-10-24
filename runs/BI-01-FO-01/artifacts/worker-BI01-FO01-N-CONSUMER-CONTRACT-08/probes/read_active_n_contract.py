"""一次已有6129的纯参数恢复对照；不请求report、不运行layout、不改节点。"""
from pathlib import Path
import datetime,hashlib,json,os,re,urllib.parse,urllib.request
rt=Path(os.environ['BI01_W08_RUNTIME'])
prior=json.loads(Path('/dwdhome/fy/cgpterm/artifacts/bi01-worker07-runtime/rb-pages.private.json').read_text())[0]['report_url']
parts=urllib.parse.urlsplit(prior);assert not parts.username and not parts.password
route='/api/graph/fao/6129/doc'
url=urllib.parse.urlunsplit((parts.scheme,parts.netloc,route,'',''))
result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'node_id':6129,'route':route,
 'source':'current active Trier existing read-only node2fao/fason API',
 'scope':'single parameter-recovery contrast to shared-class6126; no report/layout/Bokeh/node write'}
try:
 with urllib.request.build_opener(urllib.request.ProxyHandler({})).open(url,timeout=30) as response:
  raw=response.read();result['http_status']=response.status
 (rt/'ACTIVE_N_DOC_RESPONSE.private.json').write_bytes(raw)
 decoded=json.loads(raw);result['application_code']=decoded.get('code')
 message=str(decoded.get('msg',''))
 match=re.search(r"(\w+) have no param key '([\w_]+)'",message)
 result.update(unknown_parameter=match.group(2) if match else None,
               restoring_class=match.group(1) if match else None,
               response_sha256=hashlib.sha256(raw).hexdigest())
except Exception as exc:result['error_type']=type(exc).__name__
(rt/'ACTIVE_TRIER_N_RECOVERY.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
