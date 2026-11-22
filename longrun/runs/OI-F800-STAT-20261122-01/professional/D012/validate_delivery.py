from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,gzip,subprocess,ast
R=Path(__file__).resolve().parent
load=lambda n:json.loads((R/n).read_text())
m=load('ObservationMaterialPackage.json');e=load('CAEGraphExecutionResult.json');a=load('E3_ACCEPTANCE.json');d=load('E4_ADMISSION.json');f=load('FORMAL_GRAPH_DATA.json');c=load('E5_DATA_CHECK.json')
assert m['status']==e['阶段状态']=='DATA_READY' and not m['unfinished_items'] and not e['阻塞项']
assert a['结果']=='接受' and c['结果']=='一致' and c['full_scope_complete'] and c['file_count']==21
assert a['accepted_at']<=d['admitted_at']<=f['exported_at']<=c['checked_at']
assert d['E3_acceptance_sha256']==sha256((R/'E3_ACCEPTANCE.json').read_bytes()).hexdigest()
assert d['export_script_sha256']==sha256((R/'export_graph_data.py').read_bytes()).hexdigest()
assert f['accepted_html_sha256']==c['accepted_html_sha256']==a['accepted_html']['sha256']==m['final_html_sha256']
assert sha256(Path(m['final_html_local_path']).read_bytes()).hexdigest()==m['final_html_sha256']
assert not m['business_expectation_frozen'] and not m['FeatureReleaseGate_or_ReleasePackage'] and m['workers']==[]
assert len(f['formal_files'])==21 and all(z['all_columns_and_values_equal'] and z['browser_model_identity_equal'] and z['gzip_sha256_equal'] for z in c['checks'])
for row in f['formal_files']:assert sha256((R/row['file']).read_bytes()).hexdigest()==row['gzip_sha256']
for row in load('HTML_ARCHIVES.json')['files']:
 raw=(R/row['archive']).read_bytes();assert sha256(raw).hexdigest()==row['compressed_sha256'];assert sha256(gzip.decompress(raw)).hexdigest()==row['uncompressed_sha256']
for row in load('FINAL_SCRIPT_MANIFEST.json')['files']:assert sha256((R/row['path']).read_bytes()).hexdigest()==row['sha256']
assert load('SOURCE_REF_AUDIT.json')['count']==73 and load('SOURCE_REF_AUDIT.json')['owner_original_byte_equal']
assert load('D_PACKAGE_READBACK.json')['files_verified']==63
assert load('RUN_ATTEMPT01.json')['exit_code']==load('RUN_ATTEMPT02.json')['exit_code']==0
assert sha256((R/'final_script/definition/caegraph_display.py').read_bytes()).hexdigest()=='e5d6a235cd23f7e90ebbd8f020768f7e91b81ffd1782fc824362543c0f696ec0'
for file in R.glob('*.py'):ast.parse(file.read_text(),filename=str(file))
for file in R.glob('*.json'):json.loads(file.read_text())
rec=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
for row in load('D_PACKAGE_READBACK.json')['files']:
 path='longrun/runs/OI-F800-STAT-20261122-01/professional/D011/'+row['name'];assert sha256((rec/path).read_bytes()).hexdigest()==row['sha256']
assert sha256((R.parent/'D010/html/current.html').read_bytes()).hexdigest()=='3a24ab08887ce5d948b229e7d37f63a4f9a669218b47110ad4385f737a7bdded'
x=dict(completed=True,native_E_status='DATA_READY',verified_at=datetime.now(timezone.utc).isoformat(),E3_accepted=True,E4_after_E3=True,E5_all_21_files_equal=True,actual_run_count=2,exit_codes=[0,0],formal_producer_run=False,
 upstream_D_package_unchanged=True,C2_current_HTML_unchanged=True,C3_renderer_byte_equal=True,source_objects_verified=73,
 final_HTML_sha256=m['final_html_sha256'],HTML_gzip_lossless=True,stage='construction_snapshot',remaining_E_scope=[],parent_run_completed=False,FeatureRelease=False,workers=[])
(R/'VALIDATION.json').write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');print(json.dumps(x,ensure_ascii=False))
