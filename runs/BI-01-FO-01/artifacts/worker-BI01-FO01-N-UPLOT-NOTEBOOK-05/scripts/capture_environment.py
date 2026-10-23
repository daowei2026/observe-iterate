"""只记录与本单实际调用相关的版本/有效字节；不输出凭据或环境变量全集。"""
from pathlib import Path
import hashlib,json,os,subprocess
OUT=Path(__file__).resolve().parents[1]
def git(path,*args):
    p=subprocess.run(['git','-C',str(path),*args],capture_output=True,text=True)
    return p.stdout.strip() if p.returncode==0 else None
def repo(path):
    p=Path(path).resolve()
    return {'path':str(p),'head':git(p,'rev-parse','HEAD'),'branch':git(p,'branch','--show-current'),
            'status_porcelain':git(p,'status','--porcelain=v1')}
aidata=Path('/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-work2-r0014')
payload={'inspection':'本单实际工作区只读检查；导入证据另见EXECUTION_RUNTIME.json',
 'thread_id_observed':os.environ.get('CODEX_THREAD_ID'),
 'active_runner_permission_context':{'sandbox':'danger-full-access','approval_policy':'never','source':'当前运行器权限上下文；ignored实际文件写入/读回成功'},
 'reasoning':{'requested':'xhigh','persistent_config':'xhigh','active_turn_context_effort':'xhigh','evidence':'RUNTIME_PERMISSION_CHECK.json；本聊天最后turn_context实际字段'},
 'aidata':repo(aidata),'shared_aidata_original':repo('/dwdhome/fy/BASE_E6_2/mquant/aidata'),
 'uplot':repo('/dwdhome/fy/BASE_E6_2/mquant/uplot'),
 'tis_readonly_overlay':repo('/tmp/bi01-fo01-w03-runtime-20261022/mquant/tis'),
 'worker_readonly_overlay':repo('/tmp/bi01-fo01-w03-runtime-20261022/mquant/worker'),
 'actual_source_files':{},'protected_effective_file':{}}
for rel in ('feature_configs/u2_normal_node_behavior.py','u2_normal_node_behavior_display.py','tests/test_u2_normal_node_behavior_display.py'):
    p=aidata/rel
    payload['actual_source_files'][rel]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
payload['tis_reader_effective_source']={'source_commit':'3ff34c72be8ef025f68e18b097fe7b8f1f472668',
 'qualification':'GitHub精确版本fresh取回，与实际overlay两份文件逐字hash相同；checkout HEAD另记。本单复用固定正式导出，没有新调用N读者。','files':{}}
for filename,blob in [('U2NodeBehavior.py','a6251b2f83cf4a1cbf817e456419cb4fb8cd57d0'),('U2ThinNode.py','8f2310281b008338efa927d9adfc0286938fad59')]:
    local=Path('/tmp/bi01-fo01-worker-runtime-20261022/mquant/tis/frp')/filename
    fetched=Path('/dwdhome/fy/cgpterm/artifacts/bi01-worker05-runtime')/('TIS_'+filename)
    payload['tis_reader_effective_source']['files'][filename]={'source_blob':blob,
        'effective_sha256':hashlib.sha256(local.read_bytes()).hexdigest(),
        'github_source_sha256':hashlib.sha256(fetched.read_bytes()).hexdigest(),
        'equal':local.read_bytes()==fetched.read_bytes()}
p=Path('/dwdhome/fy/BASE_E6_2/mquant/uplot/pfw.py')
payload['protected_effective_file']['uplot/pfw.py']={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'git_diff_sha256':hashlib.sha256(subprocess.check_output(['git','-C',str(p.parent),'diff','--','pfw.py'])).hexdigest(),'preexisting_dirty':'开工前已见；本单只读未写'}
(OUT/'evidence/ENVIRONMENT.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2))
print('environment recorded; secrets excluded')
