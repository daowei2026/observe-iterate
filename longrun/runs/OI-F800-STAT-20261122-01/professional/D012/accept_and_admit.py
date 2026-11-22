"""原E3人工图核对后记录接受，并按原E4冻结取数范围。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
R=Path(__file__).resolve().parent
load=lambda n:json.loads((R/n).read_text())
write=lambda n,x:(R/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
a=load('BROWSER_actual.json');c=load('BROWSER_expected.json');layers=load('E3_LAYER_CHECK.json');hover=load('E3_HOVER_PROBE.json')
assert a['inventory']['figure_count']==c['inventory']['figure_count']==5
assert len(a['inventory']['sources'])==21 and a['inventory']['revision_rows']==1538
assert a['inventory']['shared_x'] and a['inventory']['data_table_same_source']
assert not a['console'] and not a['page_errors'] and not a['external_requests']
assert a['selection']['detail_contains_life'] and a['selection']['detail_contains_revision'] and a['selection']['detail_contains_children']
assert layers['all_passed'] and layers['original_and_repaired_CDS_multiset_equal']
assert hover['tap']['selected']==[2] and hover['tap']['detail_matches'] and not hover['page_errors']
assert any(hover['target']['revision'] in t['text'] for t in hover['tooltip'])
files=[]
for p in sorted((R/'final_script').rglob('*')):
 if p.is_file() and '__pycache__' not in p.parts and 'runtime-logs' not in p.parts:
  files.append(dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()))
write('FINAL_SCRIPT_MANIFEST.json',dict(entry='final_script/run_definition.py',files=files,original_D='F800-D-v1',repair='ENGINEERING_REPAIR.diff'))
html=R.parent/'caegraph-E/f800.html';runtime=json.loads(html.with_suffix('.runtime.json').read_text());assert sha256(html.read_bytes()).hexdigest()==runtime['html_sha256']==a['html_sha256']
limits=['原U PARTIAL及NOT_EXPOSED内部逐tick轨迹、失败组合/first blocker/原生coverage区间保持；本图不补造。','三年总览点密度高，需用缩放与exact选择器阅读个别观点；不从总览视觉重叠合并身份。','已暴露Rct图层为公开更新行，存在同一actual的多次事件，不等于唯一转折数；selected在T/C/known各图层重复表达同源记录。','K线每品种69个缺close按原值保留；两个空可选分支底层列缺失提示保留，公开空表/空列表不补零。','原C3页内标题“C2当前展示预期”原样保留，真实绑定已由caption和HTML文档title明确；既有hover可按工具栏启用。','精确关系以原值明细表达，未新增全局拓扑或自动跨源高亮；Q/V/WALL及四问题七candidate-only边界不变。']
accept=dict(结果='接受',accepted_at=datetime.now(timezone.utc).isoformat(),accepted_run='RUN_ATTEMPT02.json',
 accepted_script=dict(entry='final_script/run_definition.py',sha256=sha256((R/'final_script/run_definition.py').read_bytes()).hexdigest(),package_manifest='FINAL_SCRIPT_MANIFEST.json',manifest_sha256=sha256((R/'FINAL_SCRIPT_MANIFEST.json').read_bytes()).hexdigest()),
 accepted_html=dict(local_path=str(html.resolve()),bytes=html.stat().st_size,sha256=runtime['html_sha256']),
 D='daowei2026/observe-iterate@c19db65f5b7e228d1db4be61d06e361c16bafa33:longrun/runs/OI-F800-STAT-20261122-01/professional/D011/CAEGraphDefinitionIntegrationResult.json',
 C2='daowei2026/observe-iterate@ec747f4d460956bd1a91f59d0dcbaba6722ce750:longrun/runs/OI-F800-STAT-20261122-01/professional/D010/C2_CURRENT_EXPECTATION.json',
 C2_HTML_sha256='3a24ab08887ce5d948b229e7d37f63a4f9a669218b47110ad4385f737a7bdded',
 与D核对='真实39f/TIS2f/配置b720、SOF/日历/rb-hc-i/5m/三年B范围及字段入口同D；仅run-local原时间刻度密度修复，21个CDS全量值哈希与原运行一致。',
 与C2核对='亲自查看原价三图/输入known/候选exact修订及明细的全图、局部、选择与hover截图；原价独立/共享时间、实际与几何C和selected-known分离、稀疏点与携带界限、独立状态/完整父子引用均保持。',
 实际视觉证据=['screenshots/actual-full.png','screenshots/actual-zoom.png','screenshots/actual-selected.png','screenshots/actual-hover-viewport.png','screenshots/actual-tapped.png','screenshots/expected-full.png'],
 实际图层证据=['E3_LAYER_CHECK.json','BROWSER_actual.json','BROWSER_expected.json','E3_BROWSER_INTERACTIONS.json','E3_HOVER_PROBE.json'],
 接受范围='完整B三年范围内5图、21个CDS；1538主组完整父键，26种子表全部原值/各层child及4种definitions族元数据，含已发行空列表。未接受首版过密轴作为最终图。',
 limits=limits,专业回流=[],formal_data_exported_at_acceptance=False,workers=[])
write('E3_ACCEPTANCE.json',accept)
# E4正式取数准入严格在上述E3接受文件形成后。
admission=dict(admission_id='F800-E4-D012-v1',admitted_at=datetime.now(timezone.utc).isoformat(),
 E3_acceptance='E3_ACCEPTANCE.json',E3_acceptance_sha256=sha256((R/'E3_ACCEPTANCE.json').read_bytes()).hexdigest(),
 accepted_script_manifest_sha256=sha256((R/'FINAL_SCRIPT_MANIFEST.json').read_bytes()).hexdigest(),accepted_html_sha256=runtime['html_sha256'],
 accepted_run='RUN_ATTEMPT02.json',D_version='F800-D-v1',C2_version='F800-C2-v4',position=runtime['position'],
 source_objects=[{k:v for k,v in s.items() if k in ['id','name','rows','columns']} for s in layers['sources']],
 stage='construction_snapshot',output_directory=str((R/'formal_data').resolve()),
 export_script='export_graph_data.py',export_script_sha256=sha256((R/'export_graph_data.py').read_bytes()).hexdigest(),
 method='直接读取已接受HTML内嵌同次Bokeh文档CDS，不重跑Feature/构图、不使用首版/截图反推或调试表。',
 prohibited_changes=['实例/字段/数据入口','品种/三年范围/尺度/日历','D/C2业务图元/语义','接受的最终脚本/HTML'],
 viewport_final='本轮不需要：无动态标准化，fit_y/刻度只影响轴，业务CDS值不变；正式阶段明确construction_snapshot',
 formal_export_started=False)
write('E4_ADMISSION.json',admission)
print('E3 accepted with explicit limits; E4 admission frozen after acceptance; no formal files exported by this recorder.')
