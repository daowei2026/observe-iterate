"""只检查指定文件，不扫描仓库或数据资产。"""
import difflib
import hashlib
import json
import os
import pathlib
import subprocess
from support import BASE, OUT, lease, now, write_json

lease_proof=lease()
env=os.environ.copy();env['GIT_OPTIONAL_LOCKS']='0'
def git(root,*args):
    r=subprocess.run(['git','-c','core.fsmonitor=false','-C',str(root),*args],env=env,
        stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=15)
    return r
groups={
 'tis':(BASE/'mquant/tis','ef887396e0a06d6e75be47efee0f1985ad7988a3',[
    'frp/EawBattleP.py','hf/prel0/wall_assembler.py','hf/prel0/wall_assembler_core.py',
    'hf/prel0/tick_quote_context.py','hf/prel0/p1_dba_export.py','hf/prel0/p1_product_receipt.py']),
 'frp':(BASE/'edh-universe/frp/frp','cac6c912dd65a14acbd591ca57e0afd8ddb4ef13',[
    'src/Frp/Instance/ISL/Eaw/P1.hs','src/Frp/Instance/ISL/Eaw/P1/FaoIngress.hs',
    'src/Frp/Instance/ISL/Eaw/P1/WallLifecycle.hs','src/Frp/Instance/ISL/Eaw/P1/Products.hs',
    'src/Frp/Instance/ISL/Eaw/P1/Publication.hs','src/Frp/Instance/ISL/Eaw/P1/Internal/OccurrenceLedger.hs']),
 'frame':(BASE/'mquant/frame',None,['lang/internal/base.py','lang/internal/dao/frp/dba.py',
    'lang/frp/base.py','lang/internal/mixin/misc.py','core/store.py','lang/s.py','core/base/internal/cls.py']),
 'quant':(BASE/'mquant/quant',None,['core/ctx.py']),
 'pydim':(BASE/'pydim',None,['dim/rt.py','dim/dbas.py']),
 'm3sof':(BASE/'m3sof',None,['core/sof.py']),
 'm3tt':(BASE/'m3tt',None,['lang/ctx.py']),
 'm3':(BASE/'m3',None,['hpath.py']),
}
result=dict(checked_at_utc=now(), lease=lease_proof, repositories={}, files=[])
(OUT/'diffs').mkdir(exist_ok=True)
for name,(root,baseline,files) in groups.items():
    rr=git(root,'rev-parse','--show-toplevel','HEAD')
    status=git(root,'status','--porcelain=v1','--untracked-files=no','--',*files)
    result['repositories'][name]=dict(requested_root=str(root),rev_parse=rr.stdout.decode().splitlines(),
        rev_parse_error=rr.stderr.decode(),historical_baseline=baseline,
        related_status=status.stdout.decode(),status_exit=status.returncode,
        status_scope=files)
    for rel in files:
        p=root/rel
        item=dict(repository=name,path=str(p),realpath=str(p.resolve()),exists=p.is_file())
        if not p.is_file(): result['files'].append(item);continue
        data=p.read_bytes();s=p.stat()
        item.update(size=s.st_size,mtime_ns=s.st_mtime_ns,sha256=hashlib.sha256(data).hexdigest())
        local=git(root,'diff','--no-ext-diff','--no-textconv','--',rel)
        item['dirty']=bool(local.stdout)
        if local.stdout:
            d=local.stdout.decode(errors='replace');dest='diffs/%s-%s.local.diff'%(name,p.name)
            (OUT/dest).write_text(d[:24000]);item.update(local_diff=dest,local_diff_complete=len(d)<=24000)
        if baseline:
            old=git(root,'show',baseline+':'+rel)
            item['historical_blob_available']=old.returncode==0
            if old.returncode==0:
                item['historical_sha256']=hashlib.sha256(old.stdout).hexdigest()
                item['matches_historical_file']=data==old.stdout
                if data!=old.stdout:
                    diff=''.join(difflib.unified_diff(old.stdout.decode().splitlines(True),data.decode().splitlines(True),
                        fromfile=baseline+':'+rel,tofile=str(p),n=3))
                    dest='diffs/%s-%s.historical.diff'%(name,p.name)
                    (OUT/dest).write_text(diff[:32000]);item.update(historical_diff=dest,historical_diff_complete=len(diff)<=32000)
            else: item['historical_error']=old.stderr.decode()
        result['files'].append(item)
for p in (BASE/'run-python.sh',BASE/'m3rc',BASE/'edh-universe/bin/ts'):
    s=p.stat();h=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    result['files'].append(dict(path=str(p),realpath=str(p.resolve()),size=s.st_size,
        mtime_ns=s.st_mtime_ns,sha256=h.hexdigest(),role='binary_candidate' if p.name=='ts' else 'launcher_config'))
write_json('SOURCES_INITIAL.json',result)
print(json.dumps(result,ensure_ascii=False,indent=2))
