from pathlib import Path
import hashlib, json, sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from common import ROOT,guard,fact,save,utc
guard()
source=ROOT.parent/'W004/trace/r0a1.244050'
data=source.read_bytes()
assert hashlib.sha256(data).hexdigest()=='b2bcd39ff8886fa65815107bd95f333abef1bcb0a1ea69bb20010abc24b2c959'
lines=data.decode().splitlines()
expected_pre='1794694888.153303 ioctl(4</dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W004/tools/landlock_launcher.py>, FIOCLEX) = 0'
expected_post='1794694888.704672 ioctl(3</dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W004/tools/confinement_probe.py>, FIOCLEX) = -1 EPERM (Operation not permitted)'
assert lines[311]==expected_pre and lines[1508]==expected_post
installs=[{'line':i+1,'text':s} for i,s in enumerate(lines) if 'prctl(PR_SET_SECCOMP,' in s and s.endswith('= 0')]
assert len(installs)==1 and 312<installs[0]['line']<1509
observed=[]
for i,s in enumerate(lines,1):
    if 'ioctl(' in s and 'FIOCLEX' in s:
        observed.append({'line':i,'exact_text':s,'classification':'HISTORICAL_PRE_POLICY_SUCCESS' if i<installs[0]['line'] else 'HISTORICAL_POST_POLICY_DENIAL'})
save('artifacts/HISTORICAL_FIOCLEX_PHASE_CLASSIFICATION.json',{'phase':'P0','status':'PASS','at':utc(),'source':fact(source),'pre_policy':{'line':312,'exact_text':expected_pre,'classification':'HISTORICAL_PRE_POLICY_SUCCESS'},'policy_install':installs[0],'post_policy':{'line':1509,'exact_text':expected_post,'classification':'HISTORICAL_POST_POLICY_DENIAL'},'all_historical_FIOCLEX_rows':observed,'results_not_required_to_be_identical':True,'universal_denial_assertion_used':False,'current_W006_kernel_result':False})
guard();print(json.dumps({'phase':'P0','status':'PASS','historical_FIOCLEX_rows':len(observed),'policy_install_line':installs[0]['line'],'current_kernel_attempts':0}))
