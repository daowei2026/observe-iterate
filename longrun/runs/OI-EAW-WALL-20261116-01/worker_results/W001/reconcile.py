"""定向副作用对账与实际dirty schema片段。"""
import ast
import difflib
import hashlib
import json
import pathlib
import subprocess
from support import BASE,OUT,lease,write_json,sha,now

proof=lease()
initial=json.loads((OUT/'SOURCES_INITIAL.json').read_text())
extra=json.loads((OUT/'METADATA_ENRICHMENT.json').read_text())
b=json.loads((OUT/'BINDING.json').read_text())
r=json.loads((OUT/'READBACK.json').read_text())
checks=[]
for item in initial['files']+extra['additional_sources']:
    if not item.get('sha256'):continue
    p=pathlib.Path(item['path']);s=p.stat()
    same_meta=(s.st_size,s.st_mtime_ns)==(item['size'],item['mtime_ns'])
    actual=sha(p) if item.get('role')!='binary_candidate' or not same_meta else item['sha256']
    checks.append(dict(path=str(p),metadata_unchanged=same_meta,sha256_before=item['sha256'],sha256_after=actual,
        unchanged=actual==item['sha256'],hash_basis='initial hash plus unchanged size/mtime' if item.get('role')=='binary_candidate' and same_meta else 'rehashed specified source file'))
for role,entry in b['artifact_checks'].items():
    for location,artifact in entry.items():
        for name in ('fields.json','p1_receipts/wall_lifecycle.json'):
            item=artifact[name];p=pathlib.Path(item['path'])
            checks.append(dict(path=str(p),role=role,existed_before=item['exists'],exists_after=p.exists(),
                unchanged=(sha(p)==item['sha256']) if item.get('sha256') else p.exists()==item['exists']))
for row in r['audit']:
    if row.get('decision')=='READ_ONLY' and 'mtime_ns_before' in row:
        p=pathlib.Path(row['path']);s=p.stat()
        checks.append(dict(path=str(p),unchanged=(s.st_size,s.st_mtime_ns,s.st_ino)==(row['size_before'],row['mtime_ns_before'],row['inode_before']),verification='size/mtime/inode; no full DBA hash'))

p=BASE/'mquant/worker/adt/dbaw.py';current=p.read_text()
old=subprocess.run(['git','-C',str(BASE/'mquant/worker'),'show','HEAD:adt/dbaw.py'],capture_output=True,text=True,check=True).stdout
names={x+suffix for x in ('P1WallOccurrenceStorage','P1WallCurrentStorage','P1DiagnosticStorage') for suffix in ('',)}
names|={prefix+x for x in tuple(names) for prefix in ('SeqOf_','MulWrap_','SeqOf_MulWrap_')}
def sections(text):
    lines=text.splitlines(True);out=[]
    for node in ast.parse(text).body:
        targets=[node.name] if isinstance(node,(ast.ClassDef,ast.FunctionDef)) else [x.id for x in getattr(node,'targets',[]) if isinstance(x,ast.Name)]
        if names.intersection(targets):
            out.append((node.lineno,node.end_lineno,''.join(lines[node.lineno-1:node.end_lineno])))
    return out
new_sections=sections(current);old_sections=sections(old)
excerpt='# 实际schema的本对象相关定义\n\n实际路径：`'+str(p)+'`；此为选段，不是整个schema文件。\n\n'
for first,last,text in new_sections:excerpt+='原文件行 %s–%s：\n\n```python\n%s\n```\n\n'%(first,last,text)
(OUT/'SCHEMA_EXCERPTS.md').write_text(excerpt)
diff=''.join(difflib.unified_diff(''.join(x[2] for x in old_sections).splitlines(True),
    ''.join(x[2] for x in new_sections).splitlines(True),fromfile='HEAD:adt/dbaw.py (selected Wall classes)',tofile='actual adt/dbaw.py (selected Wall classes)'))
(OUT/'diffs/worker-dbaw.Wall.local.diff').write_text(diff)
result=dict(checked_at_utc=now(),lease=proof,checks=checks,all_unchanged=all(x['unchanged'] for x in checks),
    read_only_open_count=sum(x.get('decision')=='READ_ONLY' for x in r['audit']),
    denied_final_readback_actions=[x for x in r['audit'] if 'DENIED' in x.get('decision','')],
    schema=dict(path=str(p),dirty_preexisting=True,selected_classes=len(new_sections),
        selected_diff='diffs/worker-dbaw.Wall.local.diff',selected_diff_nonempty=bool(diff),
        mtime_before_w001=p.stat().st_mtime_ns<1794805200000000000),
    in_flight_commands=[],lock_release_performed=False)
write_json('RECONCILIATION.json',result)
print(json.dumps({k:v for k,v in result.items() if k!='checks'},ensure_ascii=False,indent=2))
