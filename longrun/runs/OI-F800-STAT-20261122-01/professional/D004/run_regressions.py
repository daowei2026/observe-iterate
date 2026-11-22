"""运行真实基线/修后原生窗口检查；不启动 Feature 正式生产。"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time

ROOT=Path(__file__).resolve().parent
BASE=Path('/dwdhome/fy/BASE_E6_2_copy')
OLD=BASE/'.runtime/f-wide-observation-20261122/runtime'
NEW=BASE/'.runtime/f800-exact-uti-20261122/runtime'
FRP=BASE/'.runtime/f-observation-multiple-github-20261122/frp'
CONFIGS=[ROOT.parent/'D002/preflight'/name for name in ['baseline-configuration.json','configuration.json']]
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
assert json.loads((ROOT/'BUILD_STATUS.json').read_text())['completed']
assert digest(CONFIGS[1])=='b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3'
manifest=json.loads((ROOT/'BUILD_INPUT_MANIFEST.json').read_text())
assert all(digest(FRP/path)==sha for path,sha in manifest['files'].items())
report={'started_at':datetime.now(timezone.utc).isoformat(), 'formal_feature_run':False, 'tests':[]}
for label,runtime in [('baseline',OLD),('fixed',NEW)]:
    executable=runtime/'edh-universe/bin/u2-observation-window-check'
    command=[str(executable),*map(str,CONFIGS)]
    start=time.monotonic()
    result=subprocess.run(command,text=True,capture_output=True)
    output=result.stdout+result.stderr
    (ROOT/(label+'-window-checks.log')).write_text(output)
    passes=[line[5:] for line in output.splitlines() if line.startswith('PASS ')]
    report['tests'].append({'name':label,'command':command,'binary_sha256':digest(executable),
        'exit_code':result.returncode,'elapsed_seconds':time.monotonic()-start,
        'pass_count':len(passes),'passes':passes,'output_sha256':hashlib.sha256(output.encode()).hexdigest(),
        'completed':result.returncode==0 and 'ALL OBSERVATION WINDOW CHECKS PASSED' in output})
    (ROOT/'TEST_RESULTS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(label,result.returncode,len(passes),flush=True)
    if result.returncode:
        print(output[-8000:]);raise SystemExit(result.returncode)
old,new=report['tests']
assert all(t['completed'] for t in report['tests'])
assert set(old['passes'])<=set(new['passes'])
report.update(completed=True,baseline_checks_retained=True,
              added_checks=new['pass_count']-old['pass_count'],
              finished_at=datetime.now(timezone.utc).isoformat())
(ROOT/'TEST_RESULTS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='tests'},ensure_ascii=False))
