"""只读 /proc 白名单；不读进程内存、不输出完整参数或环境。"""
from pathlib import Path
import os,json,datetime

ROOT=Path(__file__).parent
allowed={'insights.trier':'trier','insights.trier.server.bokeh':'bokeh'}
boot=next(int(l.split()[1]) for l in Path('/proc/stat').read_text().splitlines() if l.startswith('btime '))
ticks=os.sysconf('SC_CLK_TCK')
records=[]
for p in Path('/proc').iterdir():
    if not p.name.isdigit():continue
    try:
        argv=(p/'cmdline').read_bytes().split(b'\0')
        args=[v.decode(errors='replace') for v in argv if v]
        if '-m' not in args:continue
        module=args[args.index('-m')+1]
        if module not in allowed:continue
        stat=(p/'stat').read_text().rsplit(')',1)[1].split()
        env={v.split(b'=',1)[0]:v.split(b'=',1)[1] for v in (p/'environ').read_bytes().split(b'\0') if b'=' in v}
        selected={}
        for key in ['M3ROOT','M3WORKS','PYTHONPATH']:
            value=env.get(key.encode(),b'').decode(errors='replace')
            selected[key]=value if not value or all(v.startswith(('/m3c3','/dwdhome','/tmp','/home/dw')) for v in value.split(':') if v) else '<not-output>'
        records.append({'role':allowed[module],'pid':int(p.name),'module':module,
            'exe':os.readlink(p/'exe'),'cwd':os.readlink(p/'cwd'),
            'start_utc':datetime.datetime.fromtimestamp(boot+int(stat[19])/ticks,datetime.timezone.utc).isoformat(),
            'whitelisted_environment':selected,
            'stdout_kind':'file' if os.readlink(p/'fd/1').startswith('/') else 'pipe-or-socket',
            'memory_class_introspection':'not available through /proc metadata; not attempted',
            'source':'active /proc metadata only; not a live Python module/class dump'})
    except (OSError,IndexError,ValueError):continue
(ROOT/'ACTIVE_PROCESS_METADATA.private.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'role':r['role'],'pid':r['pid'],'exe':r['exe'],'cwd':r['cwd'],'start_utc':r['start_utc']} for r in records],ensure_ascii=False))
