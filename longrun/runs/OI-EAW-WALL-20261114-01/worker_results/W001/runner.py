import os, sys, json, pathlib, subprocess, datetime, shlex, fcntl

W = pathlib.Path(__file__).resolve().parent
BASE = pathlib.Path('/dwdhome/fy/BASE_E6_2')
assert W == BASE / '.oi-runs/OI-EAW-WALL-20261114-01/D001/W001'
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def guard():
    assert pathlib.Path.cwd() == BASE
    p = BASE / '.oi-runs/OI-EAW-WALL-20261114-01/.W001-writer.lock'
    assert p.stat().st_ino == 14781898
    s = pathlib.Path('/proc/227535/stat').read_text()
    a = s[s.rfind(')')+2:].split()
    assert a[19] == '44274656' and a[0] != 'Z'
    fd = os.open(p, os.O_RDWR)
    try:
        try: fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as e: assert e.errno == 11
        else: raise RuntimeError('STOP: main lock protection missing')
    finally: os.close(fd)
def environment():
    e = os.environ.copy()
    e.update({'PYTHONDONTWRITEBYTECODE':'1','TMPDIR':str(W/'tmp'),
              'XDG_CACHE_HOME':str(W/'cache'),'MPLCONFIGDIR':str(W/'cache/matplotlib'),
              'PYTHONPYCACHEPREFIX':str(W/'cache/pycache'),'GIT_OPTIONAL_LOCKS':'0',
              'GIT_TERMINAL_PROMPT':'0','PAGER':'cat','GIT_PAGER':'cat'})
    e.pop('LONG_TASK_CONTROL_REGISTER_HELPER', None)
    return e
def run(label, args, timeout=35):
    guard()
    assert label.replace('-','').replace('_','').isalnum()
    out = W/'evidence'/f'{label}.stdout.txt'
    err = W/'evidence'/f'{label}.stderr.txt'
    assert not out.exists() and not err.exists()
    start = utc()
    with (W/'COMMAND_LOG.txt').open('a') as f:
        f.write('\nLABEL '+label+'\nSTART_UTC '+start+'\nCWD '+str(BASE)+'\nCOMMAND '+shlex.join(args)+'\n')
    timed_out = False
    with out.open('x') as fo, err.open('x') as fe:
        try:
            proc = subprocess.run(args, cwd=BASE, env=environment(), stdin=subprocess.DEVNULL,
                                  stdout=fo, stderr=fe, timeout=timeout, check=False)
            code = proc.returncode
        except subprocess.TimeoutExpired:
            code = 124; timed_out = True
    end = utc()
    result = {'label':label,'command':args,'cwd':str(BASE),'started_at_utc':start,
              'ended_at_utc':end,'exit_code':code,'timed_out':timed_out,
              'stdout_path':str(out),'stderr_path':str(err),
              'stdout_bytes':out.stat().st_size,'stderr_bytes':err.stat().st_size}
    (W/'evidence'/f'{label}.command.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    with (W/'COMMAND_LOG.txt').open('a') as f:
        f.write('END_UTC '+end+'\nEXIT_CODE '+str(code)+'\nOUTPUT_SUMMARY '+
                json.dumps({k:result[k] for k in ('stdout_path','stderr_path','stdout_bytes','stderr_bytes')},ensure_ascii=False)+'\n')
    print(json.dumps(result,ensure_ascii=False))
    for path in (out,err):
        if path.stat().st_size:
            text=path.read_text(errors='replace')
            limit=int(os.environ.get('W001_PREVIEW_CHARS','15000'))
            print(str(path)+'\n'+(text if len(text)<=limit else text[:limit]+'\n[tool preview truncated; full file retained]'))
    return code
if __name__ == '__main__':
    label=sys.argv[1]
    if sys.argv[2]=='python-stdin':
        code=sys.stdin.read(); p=W/'commands'/f'{label}.py'
        with p.open('x') as f:f.write(code)
        command=[sys.executable,'-B',str(p)]
    else: command=sys.argv[2:]
    sys.exit(run(label,command))
