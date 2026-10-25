import os
"""自有临时Jupyter+真实浏览器有限episode；finally关闭，不等后继。"""
from pathlib import Path
import datetime,json,os,socket,subprocess,time,urllib.request
rt=Path(os.environ.get('BI01_W11_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker11-runtime'))
repo=Path('/dwdhome/fy/observe-iterate-bi01-fo-01')
out=repo/'runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-NORMAL-CONSUMER-11'
env=dict(os.environ)
env.update(PYTHONPATH='/tmp/bi01-fo01-w03-runtime-20261022:/dwdhome/fy/BASE_E6_2',
    M3ROOT='/m3c3',M3WORKS='/dwdhome/fy/BASE_E6_2',OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',
    JUPYTER_RUNTIME_DIR=str(rt/'jupyter'),JUPYTER_CONFIG_DIR=str(rt/'jupyter-config'),
    JUPYTERLAB_WORKSPACES_DIR=str(rt/'jupyter-workspaces'),JUPYTERLAB_SETTINGS_DIR=str(rt/'jupyter-user-settings'),BI01_W11_ARTIFACT_DIR=str(out),
    BI01_W11_AIDATA='/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-normal-consumer-r0041')
for key in ('JUPYTER_RUNTIME_DIR','JUPYTER_CONFIG_DIR','JUPYTERLAB_WORKSPACES_DIR','JUPYTERLAB_SETTINGS_DIR'):
    Path(env[key]).mkdir(exist_ok=True,mode=0o700)
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
life={'order_id':'BI01-FO01-N-NORMAL-CONSUMER-11','started_at':now(),
      'ownership':'本单新建临时Jupyter/自有kernel；不启停共享Trier/Bokeh、不恢复旧服务',
      'endpoint_credentials':'只保留本机ignored，不公开地址/端口/token'}
server=None;access=None;frontend=None
try:
    with (rt/'jupyter.private.log').open('w') as log:
        with socket.socket() as listener:
            listener.bind(('127.0.0.1',0));local_port=listener.getsockname()[1]
        server=subprocess.Popen(['/m3c3/Linux/apps/anaconda3/bin/python','-m','jupyterlab','--no-browser',
            '--ServerApp.ip=127.0.0.1','--ServerApp.port='+str(local_port),'--ServerApp.port_retries=0',
            '--ServerApp.root_dir='+str(repo)],cwd=repo,env=env,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
        deadline=time.monotonic()+90
        while time.monotonic()<deadline:
            if server.poll() is not None:raise RuntimeError('owned Jupyter exited before readiness')
            files=list((rt/'jupyter').glob('jpserver-*.json'))
            for runtime_file in files:
                candidate=json.loads(runtime_file.read_text())
                if candidate.get('pid')==server.pid and candidate.get('port')==local_port and candidate.get('token'):
                    access=candidate;break
            if access is not None:break
            time.sleep(1)
        if access is None:raise TimeoutError('owned Jupyter readiness exceeded bound')
        env['BI01_W11_JUPYTER_PORT']=str(access['port'])
        (rt/'LOCAL_NOTEBOOK_ACCESS.private.json').write_text(json.dumps(access))
        life['ready_at']=now();life['authentication_present']=bool(access['token'])
        with (rt/'frontend.private.log').open('w') as browser_log:
            frontend=subprocess.Popen(['/m3c3/Linux/apps/anaconda3/bin/python',str(out/'scripts/frontend_run.py')],
                cwd=out/'scripts',env=env,stdout=browser_log,stderr=subprocess.STDOUT)
            life['frontend_exit_code']=frontend.wait(timeout=950)
        life['frontend_finished_at']=now()
except Exception as exc:
    life['error_type']=type(exc).__name__
finally:
    if frontend is not None and frontend.poll() is None:
        import psutil
        for child in psutil.Process(frontend.pid).children(recursive=True):
            try:child.terminate()
            except psutil.Error:pass
        frontend.terminate();frontend.wait(timeout=15)
    if server is not None and server.poll() is None:
        if access:
            try:
                request=urllib.request.Request('http://127.0.0.1:'+str(access['port'])+'/api/shutdown',
                    data=b'{}',method='POST',headers={'Authorization':'token '+access['token'],'Content-Type':'application/json'})
                with urllib.request.build_opener(urllib.request.ProxyHandler({})).open(request,timeout=10) as response:
                    life['normal_shutdown_http_status']=response.status
            except Exception as exc:life['shutdown_request_error_type']=type(exc).__name__
        try:server.wait(timeout=25)
        except subprocess.TimeoutExpired:
            server.terminate()
            try:server.wait(timeout=15)
            except subprocess.TimeoutExpired:
                server.kill();server.wait(timeout=10)
                life['owned_server_forced_exit']=True
    life['owned_server_exited']=server is not None and server.poll() is not None
    import psutil
    own_kernels=[]
    for process in psutil.process_iter(['cmdline']):
        try:
            command=process.info['cmdline'] or []
            if any('ipykernel' in str(arg) for arg in command) and any(str(rt/'jupyter') in str(arg) for arg in command):
                own_kernels.append(process)
        except psutil.Error:pass
    for process in own_kernels:
        try:process.terminate()
        except psutil.Error:pass
    _,alive=psutil.wait_procs(own_kernels,timeout=5)
    for process in alive:
        try:process.kill()
        except psutil.Error:pass
    life['remaining_owned_kernels']=sum(p.is_running() and p.status()!=psutil.STATUS_ZOMBIE for p in own_kernels)
    life['ended_at']=now()
    (rt/'FRONTEND_EPISODE_LIFECYCLE.json').write_text(json.dumps(life,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(life,ensure_ascii=False))
raise SystemExit(0 if life.get('frontend_exit_code')==0 and life['owned_server_exited'] else 1)
