"""核对原D交付集合与原始来源；不是专业新Gate。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import ast,json,subprocess
R=Path(__file__).resolve().parent
P=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
D=json.loads((R/'CAEGraphDefinitionIntegrationResult.json').read_text())
C=json.loads((R/'DEFINITION_CHECKS.json').read_text())
A=json.loads((R/'SOURCE_REF_AUDIT.json').read_text())
assert C['all_passed'] and len(C['checks'])==10 and all(x['结果']=='通过' for x in C['checks'])
assert D['阶段状态']=='完整' and D['未完成项']==D['阻塞项']==[]
assert A['count']==64 and A['exact_objects_available'] and A['owner_original_byte_equal']
assert D['专业范围声明']['workers']==[]
assert all(not value for key,value in D['专业范围声明'].items() if key!='workers')
assert sha256((R/'definition/caegraph_display.py').read_bytes()).hexdigest()=='e5d6a235cd23f7e90ebbd8f020768f7e91b81ffd1782fc824362543c0f696ec0'
assert not Path(D['预期输出HTML路径']).exists()
for n in ['REPOSITORY_UNDERSTANDING.json','UPSTREAM_CORRECTIONS.json','DEFINITION_INTEGRATION_RECORD.json','FIELD_BINDING.json','SOURCE_DATA_BINDING.json','E_PENDING.json','BOUND_INSTANCE_CHECK.json','RUNTIME_PACKAGE_VERSIONS.json','EXECUTOR_REPORT.md','VALIDATION.md','INTEGRATION_DIFF.md','run_definition.py','definition/f800_definition.py']:
 assert (R/n).is_file(),n
for f in R.rglob('*.json'):json.loads(f.read_text())
for f in R.glob('*.py'):ast.parse(f.read_text(),filename=str(f))
for f in (R/'definition').glob('*.py'):ast.parse(f.read_text(),filename=str(f))
for folder,commit,names in [('D008','d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca',['CurrentFeatureUnderstandingPackage.json','FeatureRunResultBinding.json','GlobalProfileGate.json','FindingDisposition.json','ScenarioQuestionQueue.json','CandidateCaseIndex.json']),('D009','4d429ccb310452467b78b09802c48c9adbc47be5',['ObservationPositionPreparationResult.json','OrdinaryPositions.json','PositionSourceAlignment.json']),('D010','ec747f4d460956bd1a91f59d0dcbaba6722ce750',['CAEGraphDisplayPreparationResult.json','C2_CURRENT_EXPECTATION.json','html/current.html','display_code/caegraph_display.py'])]:
 for name in names:
  path=f'longrun/runs/OI-F800-STAT-20261122-01/professional/{folder}/{name}'
  assert subprocess.check_output(['git','show',f'{commit}:{path}'],cwd=P)==(P/path).read_bytes()
source=R/'source/uplot'
for row in json.loads((R/'UPLOT_SOURCE_SNAPSHOT.json').read_text())['files']:
 assert sha256((R/row['path']).read_bytes()).hexdigest()==row['sha256']
out=dict(completed=True,validated_at=datetime.now(timezone.utc).isoformat(),delegation_id='D011',call_id='C0025',
 checks_passed=10,exact_sources=64,native_D_status='完整',formal_feature_run=False,final_graph_built=False,
 final_html_generated=False,formal_graph_data_exported=False,upstream_outputs_unchanged=True,
 C3_renderer_byte_equal=True,workflow_scope='原M-D单一集成Skill；定义检查/来源/交付完整性，非另设专业Gate',
 failed_attempts_retained=['attempts/01-DEFINITION_CHECKS.log','attempts/01-DEFINITION_CHECKS.json','attempts/01-BOUND_INSTANCE_CHECK.json'])
(R/'VALIDATION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False))
