"""只运行本单有限合成技术反例，非市场/平台验收。"""
from pathlib import Path
import contextlib,datetime,hashlib,json,os,subprocess,sys
RT=Path(os.environ.get('BI01_W10_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker10-runtime'))
RT.mkdir(parents=True,exist_ok=True)
sys.path.insert(0,str(RT))
import bootstrap
candidate=bootstrap.candidate
with (RT/'unit-tests.private.log').open('w') as f,contextlib.redirect_stdout(f),contextlib.redirect_stderr(f):
 import pytest
 code=pytest.main(['-q',str(candidate/'tests/test_u2_normal_node_behavior_time.py'),'--tb=short'])
text=(RT/'unit-tests.private.log').read_text()
result=dict(actual_aidata_head=subprocess.check_output(['git','-C',str(candidate),'rev-parse','HEAD'],text=True).strip(),
 exit_code=int(code),summary=[line for line in text.splitlines() if 'passed' in line],
 log_sha256=hashlib.sha256(text.encode()).hexdigest(),qualification='7个局部计时正/反状态和重复K拒绝；仅有限合成技术探针，未重报W09的59项',
 at=datetime.datetime.now(datetime.timezone.utc).isoformat())
(RT/'FINAL_UNIT_TESTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False));raise SystemExit(int(code))
