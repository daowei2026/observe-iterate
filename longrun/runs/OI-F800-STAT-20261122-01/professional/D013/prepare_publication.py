from common import *
import shutil

assert json.loads((ROOT/'VALIDATION.json').read_text())['checks_passed']
for f in json.loads((ROOT/'FREEZE_MANIFEST.json').read_text())['files']:
    assert sha((ROOT/f['file']).read_bytes())==f['sha256']
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=RECORD).decode().strip()=='db1b87c6147c283643bdf75cfa9e8516d0d08eec'
assert not subprocess.check_output(['git','status','--porcelain'],cwd=RECORD).strip()
dest=RECORD/PREFIX/'professional/D013'
assert not dest.exists(), '专业目标已存在，须核实际状态而非覆盖'
dest.mkdir(parents=True)
skip={'plan.json','PROFESSIONAL_MANIFEST.json','PROFESSIONAL_PUBLICATION_READBACK.json','RETURN_PUBLICATION_READBACK.json',
      'FINAL_DELIVERY.json','SESSION_STATE.json'}
files=[]
for path in sorted(ROOT.rglob('*')):
    if not path.is_file() or '__pycache__' in path.parts or path.suffix=='.pyc' or path.name in skip:continue
    rel=path.relative_to(ROOT);target=dest/rel
    target.parent.mkdir(parents=True,exist_ok=True);raw=path.read_bytes();target.write_bytes(raw)
    files.append(dict(file=rel.as_posix(),local_path=str(path),record_path=target.relative_to(RECORD).as_posix(),bytes=len(raw),sha256=sha(raw)))
manifest=dict(run_id=RUN,call_id='C0029',delegation_id='D013',prepared_at=now(),scope='本Run原S1专业对象，仅professional/D013/**',
    files=files,file_count_including_manifest=len(files)+1,total_payload_bytes=sum(f['bytes'] for f in files),
    current_validation='VALIDATION.json',frozen_set='FrozenExpectationSet.json',freeze_manifest='FREEZE_MANIFEST.json',
    output_contract='锁定原S1 v0.2.0，ReviewScopeSnapshot/CandidateCasePool/CaseReviewSet/ScenarioExpectationSet/FrozenExpectationSet/ObservationGapRequests/OpenQuestions',
    accepted_material_ref=pro_ref('D012','ObservationMaterialPackage.json'),
    local_only=['plan.json','__pycache__','发布后远端读回收据和FINAL_DELIVERY/SESSION_STATE；C0029回交单独提交'],
    unchanged_inputs='83个exact对象+原最终HTML+21份正式数据；本D未修改U/X/G/M或Feature行为',
    execution_instruction='原manager消费真实S1冻结集，按原依赖签Skill2；本D无S2对照或Feature释放。')
save('PROFESSIONAL_MANIFEST.json',manifest)
(dest/'PROFESSIONAL_MANIFEST.json').write_bytes((ROOT/'PROFESSIONAL_MANIFEST.json').read_bytes())
print(json.dumps(dict(files=len(files)+1,payload_bytes=manifest['total_payload_bytes'],record_path=str(dest)),ensure_ascii=False))
