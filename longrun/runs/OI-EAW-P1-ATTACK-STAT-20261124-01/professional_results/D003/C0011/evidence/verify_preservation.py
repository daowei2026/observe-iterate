"""只读核对D003前后原产物、失败effects、历史原件和源码。"""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess

BASE=Path(__file__).resolve().parent
RUN=BASE.parents[1]
D2=RUN/'D002'
TIS=Path('/dwdhome/fy/BASE_E6_2_copy/mquant/tis')
def sha(path):
    h=hashlib.sha256()
    with path.open('rb')as f:
        for block in iter(lambda:f.read(1048576),b''):h.update(block)
    return h.hexdigest()
result={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'call_id':'C0011','delegation_id':'D003','shared_production_performed':False,'flock_acquired_by_diagnostic':False}
e=json.loads((BASE/'diagnostic-E01/diagnostic_result.json').read_text())
assert e['status']=='CHECKS_COMPLETE'and not e['errors']and e['preexisting_artifact_files_unchanged']and e['preexisting_artifact_file_count']==652
fx=json.loads((BASE/'sources/failed_effects.json').read_text());checked=[]
for row in fx['files']:
    p=Path(row['path']);s=p.stat();assert s.st_size==row['bytes']and s.st_mtime_ns==row['mtime_ns']and sha(p)==row['sha256'],str(p)
    checked.append({'path':str(p),'bytes':s.st_size,'sha256':row['sha256'],'matches_original_C0009':True})
result['failed_effects']=checked
result['failed_effect_bytes']=sum(row['bytes']for row in checked)
prior_c9_pre=json.loads((D2/'C0009/evidence/pre_execution_reconciliation.json').read_text())
for row in prior_c9_pre['history_files']:
    p=Path(row['path']);assert p.stat().st_size==row['bytes']and sha(p)==row['sha256'],str(p)
result['history_A01_A02_A03_R01_A04_files_exactly_unchanged']=len(prior_c9_pre['history_files'])
published=[]
for call in ['C0007','C0009']:
    root=D2/call/'run-records';prefix='longrun/runs/'+RUN.name
    manifest=json.loads((root/prefix/'professional_results/D002'/call/'DELIVERY_MANIFEST.json').read_text())
    for row in manifest['files']:
        p=root/row['path'];assert p.stat().st_size==row['bytes']and sha(p)==row['sha256'],str(p)
    published.append({'call_id':call,'published_manifest_files_exactly_unchanged':len(manifest['files'])})
result['original_published_deliveries']=published
u=RUN/'D001/run-records'/('longrun/runs/'+RUN.name+'/professional_results/D001/FeatureUnderstandingPackage.json')
raw=u.read_bytes();blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest();assert blob=='15817e627ef65befc9ce36547aa8ba4d7cff8b8a'
result['U_package_blob']=blob;result['U_status']=json.loads(raw)['completion_status'];assert result['U_status']=='PARTIAL'
result['tis_head']=subprocess.check_output(['git','-C',str(TIS),'rev-parse','HEAD'],text=True).strip();result['tracked_changes']=subprocess.check_output(['git','-C',str(TIS),'status','--porcelain','--untracked-files=no'],text=True)
assert result['tis_head']=='179016111ed0394f92025313e46bd13534932a74'and not result['tracked_changes']
for row in e['implementation_sources']:assert sha(Path(row['path']))==row['sha256']
lock=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/FORMAL_PRODUCTION.lock');st=lock.stat();assert(st.st_dev,st.st_ino,st.st_size)==(83,15061041,0)
result['lock_readonly_observation']={'path':str(lock),'device':st.st_dev,'inode':st.st_ino,'bytes':st.st_size,'sha256':sha(lock),'holder_probe_not_performed':True,'reservation':False}
result['all_preservation_checks']='PASS'
(BASE/'evidence/preservation_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'all_preservation_checks':'PASS','failed_files':len(checked),'failed_bytes':result['failed_effect_bytes'],'history_files':result['history_A01_A02_A03_R01_A04_files_exactly_unchanged'],'published_deliveries':published,'U_status':result['U_status'],'tis_head':result['tis_head']},ensure_ascii=False))
