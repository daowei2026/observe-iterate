"""补充已有header/小型receipt事实；不解码新的外层批次。"""
import hashlib
import json
import pathlib
import struct
import subprocess
from support import BASE,OUT,lease,write_json,sha,now

proof=lease()
b=json.loads((OUT/'BINDING.json').read_text())
r=json.loads((OUT/'READBACK.json').read_text())
for stream in r['streams'].values():
    for key in ('axis_matches_root','payload_read_succeeded'):
        if stream.get(key) in ('True','False'):stream[key]=stream[key]=='True'
write_json('READBACK.json',r)  # 只修正numpy bool的JSON表示；不重读样例payload。
source=pathlib.Path(b['bindings']['source']['full_dir'])
receipt=b['artifact_checks']['source']['full_dir']['p1_receipts/wall_lifecycle.json']['content']
params=b['bindings']['source']['ppdict']
comparisons=[]
for group in ('actual_business_parameters','producer_private_parameters'):
    for key,value in receipt[group].items():
        raw=params.get(key)
        comparisons.append(dict(key=key,receipt_group=group,receipt_value=value,current_raw_default=raw,
            comparison='equal' if key in params and raw is not None and raw==value else
            'different' if key in params and raw is not None else 'receipt-only resolved value; not recomputed'))
root=BASE/'mquant/tis';digest=hashlib.sha256()
for p in sorted((root/'hf/prel0/wall_assembler.py',root/'hf/prel0/wall_assembler_core.py')):
    digest.update(p.relative_to(root).as_posix().encode());digest.update(b'\0');digest.update(p.read_bytes());digest.update(b'\0')
result=dict(checked_at_utc=now(),lease=proof,receipt_location_matches_current_source=receipt['artifact_location']==str(source),
    parameter_comparisons=comparisons,current_two_file_producer_source_digest=digest.hexdigest(),
    source_digest_matches_receipt=receipt['code_version'].endswith('source-sha256:'+digest.hexdigest()),
    receipt_code_version=receipt['code_version'],source_headers={},additional_sources=[])

def header(p,dt):
    info=dict(path=str(p),exists=p.is_file())
    if not p.is_file():return info
    before=p.stat()
    with p.open('rb') as f:
        version,offset,item_size,align,count=struct.unpack('@iiiiq',f.read(24))
        info.update(layout_version=version,data_offset=offset,item_size=item_size,alignment=align,valid_count=count,size=before.st_size,mtime_ns=before.st_mtime_ns)
        if count and item_size==8:
            f.seek(offset);first=f.read(8);f.seek(offset+(count-1)*item_size);last=f.read(8)
            fmt='d' if dt in ('f8','float64') else 'q'
            info['first_last_raw']=[struct.unpack('@'+fmt,x)[0] for x in (first,last)]
            info['dtype']=dt
    after=p.stat();info['unchanged_after_read']=(before.st_size,before.st_mtime_ns,before.st_ino)==(after.st_size,after.st_mtime_ns,after.st_ino)
    return info
fields=b['artifact_checks']['source']['full_dir']['fields.json']['content']
for key,cols in fields.items():
    result['source_headers'][key]={col:header(source/(key+'.'+col+'.dba'),cols[col]) for col in ('ts','uti','chunk_id') if col in cols}

paths=[BASE/'edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/PublicStorage.hs',
       BASE/'mquant/frame/core/app/proxy.py',BASE/'mquant/frame/core/base/share.py',
       BASE/'mquant/frame/core/base/internal/dict.py',BASE/'m3sof/settings/sof/TA_updto20240229_DBA.py',
       BASE/'mquant/frame/core/base/json.py',pathlib.Path('/usr/local/bin/epm')]
paths.extend(pathlib.Path(p) for p in r['schema_files'])
for p in paths:
    s=p.stat();g=subprocess.run(['git','-C',str(p.parent),'rev-parse','--show-toplevel','HEAD'],capture_output=True,text=True)
    info=dict(path=str(p),realpath=str(p.resolve()),size=s.st_size,mtime_ns=s.st_mtime_ns,sha256=sha(p),
        repository_info=g.stdout.splitlines(),repository_error=g.stderr.strip() if g.returncode else None)
    if g.returncode==0:
        repo=g.stdout.splitlines()[0];rel=str(p.resolve().relative_to(repo))
        q=subprocess.run(['git','-C',repo,'status','--porcelain=v1','--untracked-files=no','--',rel],capture_output=True,text=True)
        info['related_status']=q.stdout
    result['additional_sources'].append(info)
write_json('METADATA_ENRICHMENT.json',result)
print(json.dumps(result,ensure_ascii=False,indent=2))
