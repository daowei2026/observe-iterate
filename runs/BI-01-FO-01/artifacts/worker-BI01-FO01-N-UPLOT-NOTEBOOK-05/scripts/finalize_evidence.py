"""实际运行结束后整理证据；不制造交互或覆盖原失败。"""
from pathlib import Path
import hashlib,json,shutil,math
OUT=Path(__file__).resolve().parents[1]
evidence=OUT/'evidence'
events=json.loads((evidence/'FRONTEND_EVENTS.json').read_text())
assert events[-1]['action']=='frontend_interactions_finished'
runtime=json.loads((evidence/'EXECUTION_RUNTIME.json').read_text())
done=json.loads((evidence/'KERNEL_COMPLETION.json').read_text())
assert runtime['execution_id']==done['execution_id']
old=evidence/'FRONTEND_INTERACTION_EVENTS.json'
if old.exists():
    retained=OUT/'iterations/earlier_standalone_interaction_events.json'
    if not retained.exists():shutil.copy2(old,retained)
interaction=[e for e in events if e['action'] not in ('open_notebook','restart_kernel_run_all_clicked','run_all_finished','frontend_initial_capture')]
old.write_text(json.dumps(interaction,ensure_ascii=False,indent=2)+'\n')
module='mquant.aidata.u2_normal_node_behavior_display'
file=Path(runtime['modules'][module]['file'])
assert hashlib.sha256(file.read_bytes()).hexdigest()==runtime['modules'][module]['sha256']
checks={'execution_id':runtime['execution_id'],'kernel_completion_matches':True,
 'actual_import_file_matches_current_bytes':True,'interaction_events':'FRONTEND_EVENTS.json的真实动作子集；非独立新运行',
 'required_actions':{key:any(e['action']==key for e in events) for key in (
     'rb_K_and_same_exact_range_sequence_pass','hover_actual_progress_point','native_zoom_pan_reset_pass',
     'native_legend_hide_restore_pass','i_K_sequence_pass','frontend_interactions_finished')}}
assert all(checks['required_actions'].values())
(evidence/'EXECUTION_ALIGNMENT.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
raw_dir=Path('/dwdhome/fy/cgpterm/artifacts/bi01-worker05-runtime/raw-browser-json')
raw_dir.mkdir(exist_ok=True)
normalizations=[]
def finite_json(value):
    if isinstance(value,dict):return {k:finite_json(v) for k,v in value.items()}
    if isinstance(value,list):return [finite_json(v) for v in value]
    if isinstance(value,float) and not math.isfinite(value):return None
    return value
for path in evidence.glob('BROWSER_*.json'):
    original=path.read_bytes()
    decoded=json.loads(original)
    safe=finite_json(decoded)
    if b'NaN' in original or b'Infinity' in original:
        (raw_dir/path.name).write_bytes(original)
        path.write_text(json.dumps(safe,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
        normalizations.append({'file':path.name,'original_sha256':hashlib.sha256(original).hexdigest(),
          'operation':'仅将实际浏览器Float NaN/Infinity的JSON表示规范为null；保留缺价，不填零，不改Bokeh运行数据',
          'original_retention':'本机gitignored runtime/raw-browser-json'})
if normalizations:
    (evidence/'BROWSER_JSON_NORMALIZATION.json').write_text(json.dumps(normalizations,ensure_ascii=False,indent=2)+'\n')
print('actual execution and interaction alignment PASS')
