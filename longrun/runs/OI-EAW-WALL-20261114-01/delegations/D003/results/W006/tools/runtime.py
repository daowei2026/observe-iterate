from pathlib import Path
import fcntl, json, os, signal, subprocess, sys, time
sys.path.insert(0,str(Path(__file__).resolve().parent))
from common import ROOT,BASE,binding,fact,guard,save,utc

def run(label,argv,limit=45,pass_fds=()):
    guard();assert Path(argv[0]).is_absolute()
    out=ROOT/'logs'/(label+'.stdout');err=ROOT/'logs'/(label+'.stderr')
    assert not out.exists() and not err.exists()
    env=os.environ.copy()
    env.update(PYTHONDONTWRITEBYTECODE='1',TMPDIR=str(ROOT/'tmp'),XDG_CACHE_HOME=str(ROOT/'cache'),XDG_CONFIG_HOME=str(ROOT/'config'))
    assert env['HOME']==binding()['HOME'] and env['CODEX_HOME']==binding()['CODEX_HOME']
    started=utc();tick=time.monotonic();timed_out=False
    with out.open('xb') as stdout,err.open('xb') as stderr:
        stdin_fd=os.open('/dev/null',os.O_RDONLY|os.O_CLOEXEC)
        flags=fcntl.fcntl(stdin_fd,fcntl.F_GETFL);assert flags&os.O_ACCMODE==os.O_RDONLY
        wiring={'path':'/dev/null','parent_pid':os.getpid(),'parent_fd':stdin_fd,'F_GETFL':flags,'access_mode':'O_RDONLY','opened_at':utc()}
        try:
            child=subprocess.Popen(argv,cwd=BASE,env=env,stdin=stdin_fd,stdout=stdout,stderr=stderr,pass_fds=pass_fds,start_new_session=True)
            wiring['child_pid']=child.pid
        finally:
            os.close(stdin_fd);wiring['own_parent_copy_closed_at']=utc();wiring['close_result']='SUCCESS'
            save('receipts/'+label+'-parent-stdin.json',wiring)
        try:rc=child.wait(timeout=limit)
        except subprocess.TimeoutExpired:
            timed_out=True;os.killpg(child.pid,signal.SIGKILL);rc=child.wait()
    result={'id':label,'argv':argv,'cwd':str(BASE),'started_at':started,'completed_at':utc(),'elapsed_seconds':time.monotonic()-tick,'pid':child.pid,'process_group':child.pid,'exit_code':rc,'timeout_seconds':limit,'timed_out':timed_out,'pass_fds':list(pass_fds),'HOME':env['HOME'],'CODEX_HOME':env['CODEX_HOME'],'task_environment':{k:env[k] for k in ['PYTHONDONTWRITEBYTECODE','TMPDIR','XDG_CACHE_HOME','XDG_CONFIG_HOME']},'stdout':fact(out),'stderr':fact(err)}
    with (ROOT/'logs/COMMAND_LOG.jsonl').open('a') as f:f.write(json.dumps(result,ensure_ascii=False)+'\n')
    save('receipts/'+label+'-execution.json',result)
    guard();return result
