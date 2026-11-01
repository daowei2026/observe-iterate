"""原引擎同一数据路线：owned PNV文件前缀，逐字段比对已恢复FAO输入字节。"""
from finite_probe import *

marker=OUT/'.runtime/PNV_PREFIX_ROUTE_STARTED'
fd=os.open(marker,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600);os.close(fd)
m=json.loads((OUT/'REPLAY_MANIFEST.json').read_text())
prior=json.loads((OUT/'BOOTSTRAP_TEMP_CHECK_RECEIPT.json').read_text())
assert prior['native_program_crashed'] and not prior['native_success']
assert not list((OUT/'execution/cache').rglob('value1.__ts__.dba'))
prepared=json.loads((OLD/'copied/config_and_consumption/prepared_jobs.json').read_text())
records=[]
for sym in SYMS:
    original=next(x for x in prepared['inputs'] if x['symbol']==sym)
    for field in original['fields']:
        source=Path('/m3varF/BaseData/futures/GTQH_L1_20210104_20240208/pnv/30m')/sym/(field+'.dba')
        dest=OUT/'execution/no_fallback_market/pnv/30m'/sym/(field+'.dba')
        record=prefix_dba(source,dest,2160)
        owned_fao=OUT/'execution/cache'/Path(original['staged_kline_cache']).relative_to(SOURCE/'turn_staging/cache')/(field+'.dba')
        assert dest.read_bytes()[64:]==owned_fao.read_bytes()[64:],(sym,field,'PNV vs 原已消费FAO数值不等')
        record['payload_equals_frozen_consumed_fao_prefix']=True
        records.append(record)
js('PNV_PREFIX_ROUTE_RECEIPT.json',{'replay_run_id':m['replay_run_id'],'files':records,
    'field_count':len(records),'parameters_unchanged':True,'purpose':'从原生读取路径提供同一冻结数值前缀，非改变算法/参数/实现'})
command=list(prior['command']);command[command.index('-o')+1]=str(OUT/'logs/pnv_prefix_probe.strace')
receipt={'command':command,'cwd':str(WORK),'environment_allowlist':prior['environment_allowlist'],
         'started_at':NOW(),'symbol':'rb','scale':'big','prepared_input_bars':2160,
         'source_snapshot':'PNV_PREFIX_ROUTE_RECEIPT.json','write_guard':'same Landlock owned OUT'}
start=time.monotonic()
with (OUT/'logs/pnv_prefix_probe.stdout').open('wb') as stdout,(OUT/'logs/pnv_prefix_probe.stderr').open('wb') as stderr:
    p=subprocess.Popen(command,cwd=WORK,env=receipt['environment_allowlist'],stdout=stdout,stderr=stderr,
        stdin=subprocess.DEVNULL,preexec_fn=guard_writes,start_new_session=True)
    try:receipt['returncode']=p.wait(timeout=180)
    except subprocess.TimeoutExpired:
        p.terminate();receipt['returncode']=p.wait(timeout=10);receipt['timed_out']=True
receipt.update(finished_at=NOW(),elapsed_seconds=time.monotonic()-start)
stdout=(OUT/'logs/pnv_prefix_probe.stdout').read_text(errors='replace');stderr=(OUT/'logs/pnv_prefix_probe.stderr').read_text(errors='replace')
receipt['native_program_crashed']='Edh program crashed with an error:' in stdout+stderr
receipt['native_success']=receipt['returncode']==0 and not receipt['native_program_crashed'] and 'time used:' in stdout
js('NATIVE_PREFIX_ROUTE_EXECUTION.json',receipt)
m['engine_runs'].append(receipt);m['native_process_invocations']=3;m['exit']='PENDING_PREFIX_RESULT_AND_VALIDATION'
js('REPLAY_MANIFEST.json',m)
print(json.dumps(receipt,ensure_ascii=False))
