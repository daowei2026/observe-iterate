"""同一有限执行的单次bootstrap修正：只加TMPDIR，不改变任务/数学/输入。"""
import copy as cp
from finite_probe import *

marker=OUT/'.runtime/BOOTSTRAP_TEMP_CHECK_STARTED'
fd=os.open(marker,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600);os.close(fd)
old=json.loads((OUT/'EXECUTION_RECEIPT.json').read_text())
assert not (OUT/'logs/native_engine.stdout').read_text().strip()
assert '/tmp: openTempFile: permission denied' in (OUT/'logs/native_engine.stderr').read_text()
manifest=json.loads((OUT/'REPLAY_MANIFEST.json').read_text())
receipt=cp.deepcopy(old)
temp=OUT/'execution/tmp';temp.mkdir()
receipt['environment_allowlist']['TMPDIR']=str(temp)
receipt['command'][receipt['command'].index('-o')+1]=str(OUT/'logs/temp_redirect_check.strace')
receipt['purpose']='bootstrap环境检查；原任务数值执行尚未开始；最多一次TMPDIR修正，不换引擎/参数/实现'
receipt['started_at']=NOW()
receipt.pop('finished_at',None);receipt.pop('elapsed_seconds',None)
start=time.monotonic()
with (OUT/'logs/temp_redirect_check.stdout').open('wb') as stdout,(OUT/'logs/temp_redirect_check.stderr').open('wb') as stderr:
    p=subprocess.Popen(receipt['command'],cwd=WORK,env=receipt['environment_allowlist'],stdout=stdout,stderr=stderr,
                       stdin=subprocess.DEVNULL,preexec_fn=guard_writes,start_new_session=True)
    try:receipt['returncode']=p.wait(timeout=180)
    except subprocess.TimeoutExpired:
        p.terminate();receipt['returncode']=p.wait(timeout=10);receipt['timed_out']=True
receipt.update(finished_at=NOW(),elapsed_seconds=time.monotonic()-start)
stdout=(OUT/'logs/temp_redirect_check.stdout').read_text(errors='replace')
stderr=(OUT/'logs/temp_redirect_check.stderr').read_text(errors='replace')
receipt['native_program_crashed']='Edh program crashed with an error:' in stderr+stdout
receipt['numerical_task_started']='开始优化 ScaleTurnCalendar 参数:' in stderr+stdout
receipt['native_success']=receipt['returncode']==0 and not receipt['native_program_crashed'] and 'time used:' in stdout
js('BOOTSTRAP_TEMP_CHECK_RECEIPT.json',receipt)
snapshot=json.loads((OUT/'SOURCE_SNAPSHOT.json').read_text())
known={r['source_path'] for r in snapshot['actual_opened_external_files']}
accessed=set()
for line in (OUT/'logs/temp_redirect_check.strace').read_text(errors='replace').splitlines():
    m=re.search(r'openat\([^,]+, "([^"]+)"',line)
    if m and '= -1' not in line:
        path=Path(m.group(1));path=path if path.is_absolute() else WORK/path
        if path.is_file() and not path.resolve().is_relative_to(OUT):accessed.add(path.resolve())
for path in sorted(accessed):
    if str(path) in known:continue
    code=path.suffix in ['.edh','.py','.so'] or '.so.' in path.name
    if code:
        record=copy(path,'frozen/loaded_files/'+str(path).lstrip('/'));snapshot['files'].append(record)
    else:record={'source_path':str(path),'sha256':sha(path),'bytes':path.stat().st_size,'kind':'actual_opened_file_hash_only'}
    snapshot['actual_opened_external_files'].append(record)
for record in snapshot['actual_opened_external_files']:
    assert sha(record['source_path'])==record['sha256'],'两次bootstrap之间实际源字节发生变化'
snapshot['bootstrap_temp_redirect_checked']=True
js('SOURCE_SNAPSHOT.json',snapshot)
manifest['engine_runs'].append(receipt)
manifest['native_numerical_task_start_count']=int(receipt['numerical_task_started'])
manifest['bootstrap_process_invocations']=2
manifest['finished_at']=NOW()
manifest['stop_boundary']='TMPDIR_CHECK_FINISHED_NO_FURTHER_ENGINE_INVOCATION_OR_ALTERNATIVE_ROUTE'
js('REPLAY_MANIFEST.json',manifest)
print(json.dumps(receipt,ensure_ascii=False))
