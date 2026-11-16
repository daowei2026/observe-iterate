"""只实例化和检查小型元信息；从不调用 run/F/producer。"""
import inspect
import json
import os
import pathlib
import shutil
import signal
import sys
import time
import traceback
import argparse
from support import BASE, OUT, lease, now, readonly_audit, write_json, sha

started = time.monotonic()
parser=argparse.ArgumentParser()
parser.add_argument('--direct-sof',action='store_true')
options=parser.parse_args()
report = dict(started_at_utc=now(), context=dict(sof_name='TA_updto20240229_DBA',
    startDay='2020-12-01', endDay='2021-02-22', symbol='rb', calendar='night_end_at_2300'),
    expression='EawP1WallLifecycleFrp()', feature_execution_attempted=False,
    bindings={}, artifact_checks={}, loaded_modules={}, audit=[])
report['lease'] = lease()
readonly_audit(report['audit'], allow_git=True)

def no_feature_execution(frame, event, arg):
    if event == 'call' and frame.f_code.co_name in ('_impl', '_execute', '_run_ups', '_run_up', 'rerun'):
        p = frame.f_code.co_filename
        if '/mquant/' in p:
            raise RuntimeError('STOP: feature execution path prohibited: %s:%s' % (p, frame.f_code.co_name))
sys.setprofile(no_feature_execution)

def meta(path):
    p = pathlib.Path(path)
    if not p.exists(): return dict(path=str(p), exists=False)
    s = p.stat()
    return dict(path=str(p), realpath=str(p.resolve()), exists=True, size=s.st_size,
                mtime_ns=s.st_mtime_ns, inode=s.st_ino)

def binding(obj, declared_class):
    r = dict(declared_class=declared_class.__name__, class_file=inspect.getfile(declared_class),
             class_file_realpath=str(pathlib.Path(inspect.getfile(declared_class)).resolve()),
             runtime_type=type(obj).__name__)
    for field in ('ppdict', 'ppid', 'ggjson', 'full_dir', 'gfull_dir'):
        try: r[field] = getattr(obj, field)
        except Exception: r[field] = dict(error=traceback.format_exc())
    try: r['cal_type'] = str(obj.hold_cal_type())
    except Exception: r['cal_type'] = dict(error=traceback.format_exc())
    return r

def artifacts(bound):
    r = {}
    for dirname in ('full_dir','gfull_dir'):
        if not isinstance(bound.get(dirname),str): continue
        d = pathlib.Path(bound[dirname])
        facts = dict(directory=meta(d))
        for name in ('fields.json','p1_receipts/wall_lifecycle.json'):
            p=d/name
            f=meta(p)
            if p.is_file() and p.stat().st_size <= 262144:
                f.update(sha256=sha(p),content=json.loads(p.read_text()))
            facts[name]=f
        if d.is_dir():
            entries=list(d.iterdir())
            facts['direct_entries']=[meta(p) for p in sorted(entries)[:180]]
            facts['direct_entries_total']=len(entries)
            facts['direct_entries_truncated']=len(entries)>180
        r[dirname]=facts
    return r

signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('metadata 180s limit')))
signal.alarm(180)
try:
    from mquant.tis.frp.EawBattleP import EawP1WallLifecycleFrp, WallOccurrenceFao
    from mquant.tis.hf.prel0.wall_assembler import WallAssembler
    from mquant.quant import OptContext
    from mquant.frame import CurrCalendar
    from m3tt import CurrTradeSet, CurrSymbol
    cfg=report['context']
    if options.direct_sof:
        from m3sof import load_sof
        sof=load_sof(**{k:cfg[k] for k in ('sof_name','startDay','endDay')},
                     stk_tlist='black',opt_blks=[],full_period=None)
        report['context_api']='m3sof.load_sof; OptContext source defaults black/[]/None retained'
    else:
        context=OptContext(**{k:cfg[k] for k in ('sof_name','startDay','endDay')})
        sof=context.sof
        report['context_api']='OptContext keyword arguments'
    with CurrTradeSet(sof), CurrSymbol(cfg['symbol']), CurrCalendar(cfg['calendar']):
        f=EawP1WallLifecycleFrp()
        for name, obj, cls in (('feature',f,EawP1WallLifecycleFrp),
                ('input',f.P.wallLifecycleInput,WallOccurrenceFao),
                ('source',f.P.wallLifecycleInput.P.wallOccurrenceSource,WallAssembler)):
            report['bindings'][name]=binding(obj,cls)
            report['artifact_checks'][name]=artifacts(report['bindings'][name])
    report['binding_succeeded']=True
except Exception:
    report['binding_succeeded']=False
    report['traceback']=traceback.format_exc()
finally:
    signal.alarm(0)
    sys.setprofile(None)
    report['loaded_modules']={name:dict(file=getattr(m,'__file__',None),
        realpath=str(pathlib.Path(m.__file__).resolve()) if getattr(m,'__file__',None) else None)
        for name,m in sorted(sys.modules.items()) if name in ('mquant.frame','mquant.quant','m3sof','m3tt','pydim')
        or name.startswith(('mquant.tis.frp.EawBattleP','mquant.tis.hf.prel0.wall_assembler',
        'mquant.tis.hf.prel0.tick_quote_context','mquant.tis.hf.prel0.p1_dba_export',
        'mquant.frame.lang.internal.dao.frp','mquant.frame.lang.frp','pydim.dim.rt','pydim.dim.dbas'))}
    report['resolved_commands']={k:shutil.which(k) for k in ('epm','ts','python')}
    report['elapsed_seconds']=round(time.monotonic()-started,6)
    write_json('BINDING.json',report)
    print(json.dumps({k:v for k,v in report.items() if k not in ('artifact_checks','loaded_modules')},ensure_ascii=False,indent=2,default=str))
    print('REPORT:',OUT/'BINDING.json')
