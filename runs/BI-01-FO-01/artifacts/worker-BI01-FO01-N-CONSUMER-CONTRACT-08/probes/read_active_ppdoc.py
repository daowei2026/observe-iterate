"""调用现有正常只读参数文档接口；地址取实际既有回执，不输出私网基址。"""
from pathlib import Path
import hashlib,json,urllib.request,urllib.parse,datetime
rt=Path(__file__).parent
prior=Path('/dwdhome/fy/cgpterm/artifacts/bi01-worker07-runtime/rb-pages.private.json')
actual=json.loads(prior.read_text())[0]['report_url']
parts=urllib.parse.urlsplit(actual)
assert not parts.username and not parts.password
route='/api/fao/AidataBigWorldReviewCAE/ppdoc'
url=urllib.parse.urlunsplit((parts.scheme,parts.netloc,route,'',''))
result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'source':'actual running Trier normal GET parameter-document API',
 'route':route,'endpoint_origin_source':'W07 actual DAO URL in ignored evidence',
 'side_effect_scope':'existing API constructs default CAE for ppdoc only; no run/layout/DAO write'}
try:
 # 与既有平台浏览器相同直达已授权的正常内网端点，不采用进程外HTTP代理。
 with urllib.request.build_opener(urllib.request.ProxyHandler({})).open(url,timeout=30) as response:
  payload=response.read();result['status']=response.status
 (rt/'TRIER_PPDOC_RESPONSE.private.json').write_bytes(payload)
 result.update(response_sha256=hashlib.sha256(payload).hexdigest(),response_bytes=len(payload))
 decoded=json.loads(payload)
 result['response_top_keys']=list(decoded) if isinstance(decoded,dict) else None
 text=json.dumps(decoded,ensure_ascii=False)
 result['key_occurrence']={key:key in text for key in ['run_dir','big_node_id','fixed_input_manifest','fig_width_big','normal_node_behavior_manifest']}
except Exception as exc:
 result['error_type']=type(exc).__name__
 if isinstance(exc,urllib.error.HTTPError):
  result['status']=exc.code
  (rt/'TRIER_PPDOC_ERROR.private.txt').write_bytes(exc.read())
(rt/'TRIER_PPDOC_OBSERVATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
