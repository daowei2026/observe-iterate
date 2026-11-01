"""一次有限的原引擎前缀探针。只做输入封装、文件审计和读回，不改特征数学。"""
from pathlib import Path
from datetime import datetime, timezone
import csv, ctypes, hashlib, json, os, re, shutil, struct, subprocess, time, uuid

OUT = Path(__file__).resolve().parents[1]
REPO = OUT.parents[3]
OLD = REPO / 'runs/BI-01-CO-04/artifacts/worker-BI01CO04-INPUT-RECOVERY-01'
WORK = Path('/dwdhome/fy/BASE_E6_2')
ENGINE_ROOT = Path('/m3varK/workspace/mquant_e6.2_prod/edh-universe')
SOURCE = WORK / 'mquant/aidata/test_runs/fy_owner_1d_30m_20261027/storage_migration_20261101'
NOW = lambda: datetime.now(timezone.utc).isoformat()
SYMS = ['rb', 'hc', 'i']


def sha(p):
    h = hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda: f.read(1024*1024), b''): h.update(b)
    return h.hexdigest()


def js(p, d):
    p = OUT / p; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2)+'\n')


def copy(src, target):
    p = OUT / target; p.parent.mkdir(parents=True, exist_ok=True)
    a = sha(src); shutil.copyfile(src, p); assert sha(src) == sha(p) == a
    return {'source_path': str(src), 'path': target, 'sha256': a, 'bytes': p.stat().st_size, 'kind': 'copied'}


def guard_writes():
    """Linux Landlock: 子进程只能在本单OUT写入，读取由strace独立核实。"""
    class Ruleset(ctypes.Structure): _fields_=[('handled_access_fs',ctypes.c_uint64)]
    class PathRule(ctypes.Structure): _fields_=[('allowed_access',ctypes.c_uint64),('parent_fd',ctypes.c_int32)]
    libc=ctypes.CDLL(None,use_errno=True)
    abi=libc.syscall(444,0,0,1)
    if abi<3: raise RuntimeError('Landlock ABI >=3 required, got '+str(abi))
    mask=(1<<1)|(1<<4)|(1<<5)|sum(1<<i for i in range(6,13))|(1<<13)|(1<<14)
    rule=Ruleset(mask); fd=libc.syscall(444,ctypes.byref(rule),ctypes.sizeof(rule),0)
    if fd<0: raise OSError(ctypes.get_errno(),'landlock_create_ruleset')
    parent=os.open(OUT,os.O_PATH|os.O_CLOEXEC)
    entry=PathRule(mask,parent)
    if libc.syscall(445,fd,1,ctypes.byref(entry),0)<0: raise OSError(ctypes.get_errno(),'landlock_add_rule')
    if libc.prctl(38,1,0,0,0)<0: raise OSError(ctypes.get_errno(),'no_new_privs')
    if libc.syscall(446,fd,0)<0: raise OSError(ctypes.get_errno(),'landlock_restrict_self')
    os.close(parent); os.close(fd)


def prefix_dba(src, dst, count):
    # 原64字节DBA头和原数组payload，仅修改合法长度；数值字节完全相同。
    with src.open('rb') as f:
        header=bytearray(f.read(64)); offset=struct.unpack_from('<i',header,4)[0]
        item=struct.unpack_from('<i',header,8)[0]; length=struct.unpack_from('<q',header,16)[0]
        assert offset==64 and item==8 and 0<count<=length
        payload=f.read(item*count)
    struct.pack_into('<q',header,16,count)
    dst.parent.mkdir(parents=True,exist_ok=True); dst.write_bytes(header+payload)
    return {'source_path':str(src),'path':str(dst.relative_to(OUT)), 'source_rows':length,
            'rows':count,'payload_sha256':hashlib.sha256(payload).hexdigest(),
            'sha256':sha(dst),'bytes':dst.stat().st_size,'kind':'prefix_input_export_exact_numeric_bytes'}


def main():
    lock=OUT/'.runtime/FINITE_EXECUTION_STARTED.json'
    fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
    replay='BI01CO04_ASOF_REPLAY_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'_'+uuid.uuid4().hex[:8]
    os.write(fd,json.dumps({'replay_run_id':replay,'started_at':NOW(),'execution_limit':1}).encode());os.close(fd)
    manifest={'replay_run_id':replay,'order_id':'BI01CO04-ASOF-VISIBILITY-REPLAY-01',
              'source_baseline_commit':'dfdf843b47c03c0121fd7151b72f24adb5d986c0',
              'symbols':SYMS,'scales':['big','mid'],'frequency':'30m',
              'warmup_start':'2021-01-04T09:30:00+08:00',
              'decision_window':['2021-08-15T00:00:00+08:00','2021-09-30T15:00:00+08:00'],
              'evaluation_tail_max':'2021-10-15T15:00:00+08:00','canonical_clock':'KLine.closeTs localized Asia/Shanghai',
              'started_at':NOW(),'exit':'PENDING','algorithm_parameter_changes':False,
              'planned_probe':'rb/big original HistoryModel at frozen 2160-bar prefix; stop on first unprovable bearing gate',
              'engine_runs':[],'remaining_symbol_scales':[]}
    js('REPLAY_MANIFEST.json',manifest)
    records=[]
    # 固定基线96文件，排除旧现场账本，不重跑旧恢复单。
    files=subprocess.check_output(['git','ls-tree','-r','--name-only','-z','dfdf843b47c03c0121fd7151b72f24adb5d986c0',str(OLD.relative_to(REPO))],cwd=REPO).decode().strip('\0').split('\0')
    for rel in files:
        src=REPO/rel; records.append(copy(src,'copied/baseline/'+str(src.relative_to(OLD))))
    records.append(copy(ENGINE_ROOT/'bin/ts','frozen/bin/ts'))
    os.chmod(OUT/'frozen/bin/ts',0o755)
    assert sha(OUT/'frozen/bin/ts')=='dba166c7fc8d0acf2e56499699b36ac47dd30c923a739e52a7288860fae57450'
    entry=ENGINE_ROOT/'frp/trade-poc/edh_modules/trade/frp/worker/one.edh'
    records.append(copy(entry,'frozen/entrypoint/one.edh'))
    # 原先已走通的同一原生输入位置；只创建本新identity内部副本。
    prepared=json.loads((OLD/'copied/config_and_consumption/prepared_jobs.json').read_text())
    frozen_inputs={r['path']:r['sha256'] for r in json.loads((OLD/'evidence/SOURCE_INPUTS.json').read_text()) if r.get('sha256')}
    cache=OUT/'execution/cache'; app=OUT/'execution/app'; cfg=app/'mquant/config/prod'
    for sym in SYMS:
        inp=next(i for i in prepared['inputs'] if i['symbol']==sym)
        src=Path(inp['staged_kline_cache'])
        dest=cache/src.relative_to(SOURCE/'turn_staging/cache')
        bars=list(csv.DictReader((OLD/f'regenerated/market/{sym}_30m_warmup_through_20210930.csv').open()))
        assert len(bars)==2160 and bars[-1]['closeTs']=='2021-09-30 15:00:00'
        for key in list(inp['fields'])+['__ts__']:
            assert sha(src/(key+'.dba'))==frozen_inputs[str(src/(key+'.dba'))], '原输入变化，禁止继续'
            records.append(prefix_dba(src/(key+'.dba'),dest/(key+'.dba'),2160))
        records.append(copy(src/'fields.json',str((dest/'fields.json').relative_to(OUT))))
    source_cfg=json.loads((OLD/'copied/config_and_consumption/engine_source_config.json').read_text())
    source_cfg['store_dir']=[str(cache)]
    source_cfg['pnv_dir']=str(OUT/'execution/no_fallback_market/pnv')
    source_cfg['ori_dir']=str(OUT/'execution/no_fallback_market/tick')
    Path(source_cfg['pnv_dir']).mkdir(parents=True);Path(source_cfg['ori_dir']).mkdir(parents=True)
    js(str((cfg/'sof/GTQH_L1_20210104_20240208.json').relative_to(OUT)),source_cfg)
    js(str((cfg/'store_dir.json').relative_to(OUT)),{k:[str(cache)] for k in ['KLine','ZigZag','RctZigWithStatus','ScaleTurnCalendar']})
    for sym in SYMS:
        for role in ['big','mid']:
            task=json.loads((OLD/f'copied/config_and_consumption/jobs/{sym}__{role}.task.json').read_text())
            original=task['task_params']['params'];task['task_params']['app']['app_dir']=str(app)
            assert task['task_params']['params']==original
            js(f'execution/tasks/{sym}__{role}.json',task)
    # 所有现场准备写入均已完成。下面只有一次业务引擎调用，状态失败不重启。
    env={key:os.environ[key] for key in ['HOME','LD_LIBRARY_PATH','LD_PRELOAD','EDH_PATH','EDH_IMPORT_PATH','EPM_HOME'] if key in os.environ}
    env.update({'PATH':'/m3c3/Linux/apps/anaconda3/bin:/m3c3/Linux/bin:/usr/bin:/bin',
         'LANG':'C.UTF-8','TZ':'Asia/Shanghai','M3ROOT':'/m3c3','M3WORKS':str(WORK),
         'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1'}
    )
    command=['/usr/bin/strace','-f','-ttt','-yy','-s','160','-e','trace=openat,mmap,write,close',
             '-o',str(OUT/'logs/native_engine.strace'),str(OUT/'frozen/bin/ts'),
             '--f='+str(OUT/'frozen/entrypoint/one.edh'),'--jp='+str(OUT/'execution/tasks/rb__big.json')]
    (OUT/'logs').mkdir(exist_ok=True)
    execution={'command':command,'cwd':str(WORK),'environment_allowlist':env,'started_at':NOW(),
               'symbol':'rb','scale':'big','input_bars':2160,'max_input_bar_ts':'2021-09-30T15:00:00+08:00',
               'input_boundary':'only frozen KLine prefix in new store_dir; pnv/tick fallback empty',
               'write_guard':'Landlock ABI>=3: write/remove/create/truncate/rename restricted to this OUT',
               'instrumentation':'strace file/mmap/write boundary only, no mathematical patch'}
    start=time.monotonic()
    try:
        with (OUT/'logs/native_engine.stdout').open('wb') as stdout,(OUT/'logs/native_engine.stderr').open('wb') as stderr:
            p=subprocess.Popen(command,cwd=WORK,env=env,stdout=stdout,stderr=stderr,stdin=subprocess.DEVNULL,preexec_fn=guard_writes,start_new_session=True)
            try: rc=p.wait(timeout=180)
            except subprocess.TimeoutExpired:
                p.terminate();rc=p.wait(timeout=10);execution['timed_out']=True
        execution['returncode']=rc
    except Exception as e:
        execution['launch_exception']=repr(e);execution['returncode']=None
    execution.update(finished_at=NOW(),elapsed_seconds=time.monotonic()-start)
    js('EXECUTION_RECEIPT.json',execution)
    manifest['engine_runs']=[execution];manifest['remaining_symbol_scales']=[s+'/'+r for s in SYMS for r in ['big','mid'] if (s,r)!=('rb','big')]
    # 审计真正被加载的文件。只有完整闭合才可能通过源冻结；不存在的文件不能补猜。
    accessed=set();trace=OUT/'logs/native_engine.strace'
    if trace.exists():
        for line in trace.read_text(errors='replace').splitlines():
            m=re.search(r'openat\([^,]+, "([^"]+)"',line)
            if m and '= -1' not in line:
                path=Path(m.group(1));path=path if path.is_absolute() else WORK/path
                if path.is_file():accessed.add(path.resolve())
    imports=[]
    for path in sorted(accessed):
        if path.is_relative_to(OUT):continue
        # 实际import的业务脚本/动态库逐文件冻结；元数据只hash并准确标原路径。
        code=path.suffix in ['.edh','.py','.so'] or '.so.' in path.name
        if code:
            target='frozen/loaded_files/'+str(path).lstrip('/')
            info=copy(path,target);records.append(info)
        else: info={'source_path':str(path),'sha256':sha(path),'bytes':path.stat().st_size,'kind':'actual_opened_file_hash_only'}
        imports.append(info)
    js('SOURCE_SNAPSHOT.json',{'replay_run_id':replay,'created_at':NOW(),'files':records,'actual_opened_external_files':imports,
          'freeze_complete_for_qualified_replay':False,
          'limitation':'首个原生调用尚未证明每个内部状态的first-seen与输入前缀边界；依真实结果在报告给出出口B，不把静态event_ts当观察时间。'})
    manifest.update(finished_at=NOW(),exit='BLOCKED_NO_LOOKAHEAD_PROOF',
                    stop_boundary='FIRST_NATIVE_PREFIX_PROBE_ONLY_NO_ALTERNATIVE_IMPLEMENTATION')
    js('REPLAY_MANIFEST.json',manifest)
    print(json.dumps({'replay_run_id':replay,'engine_attempts':1,'receipt':execution,'copied_files':len(records)},ensure_ascii=False))


if __name__=='__main__': main()
