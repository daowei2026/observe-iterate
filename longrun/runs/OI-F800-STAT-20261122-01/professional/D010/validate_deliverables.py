from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
import subprocess

R=Path(__file__).resolve().parent
RECORD=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
RUN='OI-F800-STAT-20261122-01'
def load(n):return json.loads((R/n).read_text())
required=['C1_INFORMATION_LIST.json','C2A_MANUAL_READING.json','OUTER_INSTANCE_USE.json','C2_FIRST_EXPECTATION.json',
 'C2_CURRENT_EXPECTATION.json','C2C_FIRST_REVIEW.json','C2_COMPLEX_POINT_ROUNDS.json','CAEGRAPH_CAPABILITY_GAPS.json',
 'C3_CODE_RESULT.json','INJECTION_CONTRACT.json','FIELD_MAP_TEMPLATE.json','CAEGraphDisplayPreparationResult.json','CODE_VALIDATION.json',
 'html/first.html','html/current.html','archive/prototype_v1.py','archive/current_impl_v4.py','display_code/caegraph_display.py',
 'BROWSER_v1.json','BROWSER_v2.json','BROWSER_v3.json','BROWSER_v4.json','screenshots/first.png','screenshots/current-selected.png',
 'EXECUTOR_REPORT.md','VALIDATION.md']
assert all((R/n).is_file() for n in required)
state=load('CAEGraphDisplayPreparationResult.json')
assert state['阶段状态']=='完整' and state['本阶段未完成项']==[] and state['未解决工具能力缺口']==[]
state['stage_code']='M-C'
(R/'CAEGraphDisplayPreparationResult.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
c1=load('C1_INFORMATION_LIST.json')['信息清单']
assert len(c1)==12 and any(x['业务角色']=='业务主输出' and x['是否纳入展示预期']=='是' for x in c1)
assert all(x['是否纳入展示预期']=='否' for x in c1 if x['运行结果可用状态']=='NOT_EXPOSED')
expect=load('C2_CURRENT_EXPECTATION.json');binding=load('PREVIEW_BINDING_v4.json');code=load('CODE_VALIDATION.json')
current_sha=sha256((R/'html/current.html').read_bytes()).hexdigest()
assert current_sha==expect['当前HTML_SHA256']==binding['html_sha256'] and binding['version']=='v4'
assert expect['唯一当前HTML'] and state['唯一当前预期HTML']
assert binding['preview_kind']=='SYNTHETIC' and not binding['real_feature_instance_bound'] and not binding['formal_B_binding']
assert code['status']=='PASS' and code['check_count']==15 and all(x['pass_'] for x in code['checks'])
core=(R/'display_code/caegraph_display.py').read_bytes()
assert core==(R/'archive/current_impl_v4.py').read_bytes() and sha256(core).hexdigest()==code['C3_source_sha256']
assert 'from display_code.caegraph_display import *' in (R/'current_impl.py').read_text()
browser=load('BROWSER_v4.json')
assert not browser['console'] and not browser['external_requests'] and len(browser['plots'])==5
assert len({p['x_range'] for p in browser['plots']})==1 and browser['ui_select_probe']=={'indices':[2],'chooser':'2'}
assert browser['chooser_after_selection']=='2' and browser['selection_probe']['records']==6
assert browser['output_legend']==['本次携带 a→d','本次携带 d→r','Sparse exact revision']
assert 'child_id_3' in browser['detail_after_selection'] and 'SYN-Life-B' in browser['detail_after_selection']
snapshot=load('UPLOT_SOURCE_SNAPSHOT.json')
for row in snapshot['files']:assert sha256((R/'source/uplot'/row['path']).read_bytes()).hexdigest()==row['sha256']
assert sha256((R/'source/uplot/CAEGraph使用手册.md').read_bytes()).hexdigest()==load('METHOD_LOCK.json')['manual_sha256']
audit=load('SOURCE_REF_AUDIT.json')
assert audit['count']==49 and audit['exact_objects_available'] and audit['owner_original_byte_equal'] and audit['packet_invocation_equal']
assert len(load('REMOTE_DISPATCH_READBACK.json'))==3
unchanged=[]
for d,commit,names in [('D008','d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca',
    ['CurrentFeatureUnderstandingPackage.json','FeatureRunResultBinding.json','GlobalProfileGate.json','FindingDisposition.json','ScenarioQuestionQueue.json','CandidateCaseIndex.json','PUBLIC_TABLE_SCHEMA.json','configuration.json']),
  ('D009','4d429ccb310452467b78b09802c48c9adbc47be5',
    ['ObservationPositionPreparationResult.json','OrdinaryPositions.json','PositionSourceAlignment.json'])]:
    for name in names:
        p='longrun/runs/'+RUN+'/professional/'+d+'/'+name
        raw=subprocess.check_output(['git','show',commit+':'+p],cwd=RECORD)
        assert raw==(R.parent/d/name).read_bytes()==(RECORD/p).read_bytes()
        unchanged.append(dict(delegation=d,path=name,sha256=sha256(raw).hexdigest()))
inputs=load('INPUT_BINDING.json')
assert inputs['understanding_status']=='PARTIAL' and not inputs['formal_feature_run_in_D010'] and not inputs['global_statistics_rerun_in_D010']
assert not inputs['feature_semantics_reinvestigated'] and inputs['B_not_reselected']
assert len(json.loads((R.parent/'D009/PositionSourceAlignment.json').read_text())['candidates'])==7
manual=load('C2A_MANUAL_READING.json')
manual.setdefault('C2A时待核实能力',manual['尚未核实能力'])
manual['尚未核实能力']=[];manual['后续核实证据']=['C2_COMPLEX_POINT_ROUNDS.json','BROWSER_v4.json','CODE_VALIDATION.json']
(R/'C2A_MANUAL_READING.json').write_text(json.dumps(manual,ensure_ascii=False,indent=2)+'\n')
out=dict(completed=True,verified_at=datetime.now(timezone.utc).isoformat(),native_stage='M-C',native_stage_state='完整',
    native_IO_files=required,exact_sources=49,manual_original_read_and_byte_verified=True,
    uplot_snapshot_files_byte_verified=len(snapshot['files']),current_unique_html_sha256=current_sha,
    C3_sha256=sha256(core).hexdigest(),native_code_checks=15,current_browser_errors=0,current_external_requests=0,
    current_browser_actual_control_selection_pass=True,old_U_X_G_B_files_unchanged=unchanged,
    semantic_reinvestigation=False,formal_feature_run=False,B_reselection=False,formal_case_selection=False,
    E_final_graph_or_data=False,Feature_or_ObservationMaterial_release=False,workers_empty=True,
    gate_boundary='原schema/gate函数及实际I/D/Binding/发布顺序校验在专业发布读回后另写Return验证；未宣称完整CLI兼容。')
(R/'VALIDATION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('native_IO_files','old_U_X_G_B_files_unchanged')},ensure_ascii=False))
