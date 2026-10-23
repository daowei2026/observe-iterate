"""生成不含现场端口的公开证据副本，保留原字节于ignored运行目录。"""
from pathlib import Path
import hashlib,json
OUT=Path(__file__).resolve().parents[1]
RAW=Path('/dwdhome/fy/cgpterm/artifacts/bi01-worker05-runtime/raw-public-evidence')
RAW.mkdir(exist_ok=True)
changed=[]
for folder in ('evidence','iterations','failures'):
    for p in (OUT/folder).glob('*.json'):
        payload=json.loads(p.read_text())
        def redact(value):
            if isinstance(value,dict):
                return {k:('[现场Jupyter入口仅保存在本机ignored运行材料]' if k=='url' and isinstance(v,str) and v.startswith('http://127.0.0.1:') else redact(v)) for k,v in value.items()}
            if isinstance(value,list):return [redact(v) for v in value]
            return value
        sanitized=redact(payload)
        if sanitized!=payload:
            original=p.read_bytes()
            (RAW/(folder+'__'+p.name)).write_bytes(original)
            p.write_text(json.dumps(sanitized,ensure_ascii=False,indent=2)+'\n')
            changed.append({'path':str(p.relative_to(OUT)),'original_sha256':hashlib.sha256(original).hexdigest(),'change':'仅url字段的本机端口隐去，实际Notebook路径/动作/结果保留','raw_retention':'gitignored runtime/raw-public-evidence'})
if changed:
    (OUT/'evidence/RUNTIME_LOCATOR_REDACTIONS.json').write_text(json.dumps(changed,ensure_ascii=False,indent=2)+'\n')
print('runtime locator redactions:',len(changed))
