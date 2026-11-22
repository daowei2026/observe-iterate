from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,gzip,shutil
R=Path(__file__).resolve().parent;RUN='OI-F800-STAT-20261122-01'
load=lambda n:json.loads((R/n).read_text())
write=lambda n,x:(R/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
accept=load('E3_ACCEPTANCE.json');admission=load('E4_ADMISSION.json');data=load('FORMAL_GRAPH_DATA.json');check=load('E5_DATA_CHECK.json')
assert accept['结果']=='接受' and check['结果']=='一致' and check['file_count']==21
assert not check['remaining_items'] and len(data['formal_files'])==21
html=Path(accept['accepted_html']['local_path']);assert sha256(html.read_bytes()).hexdigest()==accept['accepted_html']['sha256']
(R/'html').mkdir(exist_ok=True)
archives=[]
for source,target,role in [(html,R/'html/f800.html.gz','E3接受最终图'),(R/'attempts/01-f800.html',R/'attempts/01-f800.html.gz','首版未作为最终图接受：全范围刻度过密')]:
 with source.open('rb') as src,target.open('wb') as dst:
  with gzip.GzipFile(filename='',mode='wb',compresslevel=6,fileobj=dst,mtime=0) as out:shutil.copyfileobj(src,out)
 original_sha=sha256(source.read_bytes()).hexdigest();assert sha256(gzip.decompress(target.read_bytes())).hexdigest()==original_sha
 archives.append(dict(role=role,local_uncompressed=str(source.resolve()),archive=str(target.relative_to(R)),encoding='gzip',uncompressed_bytes=source.stat().st_size,uncompressed_sha256=original_sha,compressed_bytes=target.stat().st_size,compressed_sha256=sha256(target.read_bytes()).hexdigest(),lossless_verified=True))
shutil.copy2(html.with_suffix('.runtime.json'),R/'html/f800.runtime.json')
write('HTML_ARCHIVES.json',dict(files=archives,publishing_policy='记录分支使用gzip无损封装；授权BASE保留可直接打开的原HTML，未改变被接受图。'))
packet=json.loads(Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/C0027-dispatch-packet.json').read_text())
write('INPUT_BINDING.json',dict(run_id=RUN,call_id='C0027',delegation_id='D012',delegation_ref=packet['delegation_ref'],invocation_ref=packet['invocation_ref'],task_skill_ref=packet['delegation']['task_ref'],
 binding_ref=packet['binding_adoption']['binding_ref'],owner_approval_ref=packet['binding_adoption']['approval_ref'],record_base_head='df7184295277c8dfa60f4664635d32194437e87b',record_branch=packet['record_branch'],
 permitted_operations=packet['delegation']['permitted_operations'],allowed_writes=packet['delegation']['allowed_writes'],workers=[],sources='SOURCE_REF_AUDIT.json',exact_source_count=73,D_package='D_PACKAGE_READBACK.json',
 frp='39f02ec4548e68ba8dbd30061afc870546000994',tis='2f460d663d821cf2ba25555eda13e78b697d0767',uplot='0a4fcd54059782572a3f7e82fad041121e8c65ad',configuration_sha256='b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3',
 formal_feature_production=False,U_X_G_B_C_D_reused=True))
write('E2_FINAL_EVALUATION.json',{'运行结果':'实际成功并经E3接受','最终脚本和运行':'final_script/run_definition.py / RUN_ATTEMPT02.json','实际命令':load('RUN_ATTEMPT02.json')['command'],'退出状态':0,'最终HTML':accept['accepted_html'],
 '实际修改':'ENGINEERING_REPAIR.diff：仅显示原刻度子集及随视窗更新；不改时间标签值/范围/CDS/业务图元','首次运行':'RUN_ATTEMPT01.json成功生成原图，实际发现刻度密度问题；原图及截图无损保留在attempts/01-*',
 '实际提示':'两次原生reader均保留两个空可选分支的FileNotFoundError提示；31表公开合同/数量检查通过。未补算缺源或填零。','专业分类与后继':'原Skill许可的run-local工程修复；E3已接受，再进入E4/E5；无具名U/B/C/D回流或新Owner请求','剩余阻断':[]})
U='daowei2026/observe-iterate@d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca:longrun/runs/'+RUN+'/professional/D008/CurrentFeatureUnderstandingPackage.json'
B='daowei2026/observe-iterate@4d429ccb310452467b78b09802c48c9adbc47be5:longrun/runs/'+RUN+'/professional/D009/OrdinaryPositions.json'
X='daowei2026/observe-iterate@d4f9fefaa67f9f22f540fa35a7da79cbbdf831ca:longrun/runs/'+RUN+'/professional/D008/FeatureRunResultBinding.json'
package=dict(feature_understanding_package_ref=U,feature_ref=dict(name='CommonPriceTurnGroupCandidatesFrp',frp='39f02ec4548e68ba8dbd30061afc870546000994',tis='2f460d663d821cf2ba25555eda13e78b697d0767',instance=X),
 parameter_version='b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3',position_definition_ref=B,position=admission['position'],
 display_expectation_ref=accept['C2'],display_expectation_HTML_ref='daowei2026/observe-iterate@ec747f4d460956bd1a91f59d0dcbaba6722ce750:longrun/runs/'+RUN+'/professional/D010/html/current.html',complete_definition_ref=accept['D'],
 final_script_ref='final_script/run_definition.py',final_script_package_manifest='FINAL_SCRIPT_MANIFEST.json',final_html_ref='html/f800.html.gz',final_html_encoding='gzip，无损解压后为接受的原HTML',final_html_local_path=str(html.resolve()),final_html_sha256=accept['accepted_html']['sha256'],
 exported_graph_data_ref='FORMAL_GRAPH_DATA.json',run_and_worker_records=['RUN_ATTEMPT01.json','RUN_ATTEMPT02.json','ENGINEERING_REPAIRS.json','ENGINEERING_REPAIR.diff'],
 E3_graph_acceptance='E3_ACCEPTANCE.json',E4_export_admission='E4_ADMISSION.json',graph_data_consistency_check='E5_DATA_CHECK.json',
 formal_data_stage='construction_snapshot',formal_data_files=21,actual_figure_count=5,actual_revision_rows=1538,known_limits=accept['limits'],status='DATA_READY',
 unfinished_items=[],blocked_items=[],workers=[],business_expectation_frozen=False,FeatureReleaseGate_or_ReleasePackage=False,
 delivered_at=datetime.now(timezone.utc).isoformat())
write('ObservationMaterialPackage.json',package)
write('CAEGraphExecutionResult.json',dict(stage_code='M-E',阶段状态='DATA_READY',专业依据=packet['delegation']['task_ref'],原E1至E6连续执行=True,workers=[],
 E1='E1_BASELINE.json',E2='E2_FINAL_EVALUATION.json',E3='E3_ACCEPTANCE.json',E4='E4_ADMISSION.json / FORMAL_GRAPH_DATA.json',E5='E5_DATA_CHECK.json',E6='ObservationMaterialPackage.json',
 最终图=package['final_html_ref'],最终图本地路径=package['final_html_local_path'],最终脚本=package['final_script_ref'],正式数据=package['exported_graph_data_ref'],未完成项=[],阻塞项=[],具名专业回流=[],限制=accept['limits'],
 完成边界='仅本D012原M-E材料准备完整；真实图接受/正式数据取得/E5一致，不代后继S1/S2场景预期或Feature释放，不表示manager已消费或父Run完成。'))
(R/'EXECUTOR_REPORT.md').write_text(f'''# D012 / C0027｜真实图、正式图数据与材料交付

原E1同线程按原caegraph-execution Skill连续完成E1—E6，材料状态 **DATA_READY**。实际执行了两次只读CAEGraph运行，最终图经D/C2-v4核对接受后才形成E4准入；21份正式CDS构图快照已取得，E5逐列/值与接受图一致。workers=[]。

最终可打开HTML：`{html.resolve()}`；SHA-256 `{package['final_html_sha256']}`。记录分支无损封装为 `html/f800.html.gz`，解压字节和原HTML相同。完整最终脚本在 `final_script/`，入口 `run_definition.py`，包文件哈希见 `FINAL_SCRIPT_MANIFEST.json`；实际命令/PID/起止/退出码见 `RUN_ATTEMPT02.json`，实际日志保留。无需新生产或重跑G。

原D011入口首跑退出0，生成真实三年图；E3实际打开后发现全范围2072个时间刻度形成黑带。依C2已允许的标签频率变化和原E工程权限，在run-local副本只抽稀可见原时间刻度，随共享视窗更新；原120m标签值、实例/B位置/字段/源/CDS/业务图元均未改。第二次运行退出0，全范围每轴10个刻度，局部缩放仍沿原标签。21个CDS全量数据哈希与首跑完全相同。diff、首版原HTML压缩档和截图均保留；未改共享uplot、Feature或受保护平台。一次准备脚本的括号错误在执行任何修改前被解释器拒绝，修正记录保留，不伪称Feature失败。

亲自检查真实全图、局部、下拉/点选后的exact明细及实际hover；浏览器错误/警告和外部请求均为空。5图依次为三品种独立原价、上游selected-known、全局exact修订，阅读路径与唯一C2-v4保持。真实鼠标Tap与下拉/明细联动通过；hover启用后显示Life/Revision、完整父键、known及各独立状态/窗口。截图和模型证据见 `E3_ACCEPTANCE.json`，原C2只作预期，不冒充真实结果。

| 图层或数据 | 本次行数及计数单位 | 分母与解释 |
|---|---:|---|
| 原价K线 | rb/hc/i各49683行 | 各品种完整B位置5m K线行；各69个close NaN保留，不补零 |
| Rct实际投影 | rb7538 / hc7478 / i10738行 | 上游公开更新投影行，同一actual可多次出现；不是唯一原始转折分母 |
| 已选T、C、selected-known | 每层rb425 / hc430 / i1004行 | 同一公开选中记录分别在三个位置表达，不跨图层相加计对象 |
| exact修订发布点 | 1538行 | 完整父坐标对应的组观点发行视图；286个known位置含多个观点，均分行保留 |
| a→d携带窗口 | 1538条显示段 | 原观点携带界限按视区裁剪，不是持续状态/coverage |
| d→r携带窗口 | 1537条显示段 | 1条整个tail在视区外；原始端点仍在exact raw中，E5逐段核同 |

E3逐行核1538组UUID无损、父键唯一、known=点x；26种原生子表所有32553行及22646个“组×子表”空列表保留，4种definitions族原值进入元数据。空列表不等于0或失败。两次日志中两个空可选分支物理列的FileNotFoundError提示原样保留，公开31表检查通过，不补算缺源。

正式取数严格晚于E3接受。直接从被接受HTML内嵌的**同次Bokeh CDS**读取21个源，阶段明确为 `construction_snapshot`，没有重新构图、重跑Feature、从截图反推或把候选调试表升格。`FORMAL_GRAPH_DATA.json`给出图层/renderer→文件→阶段→列/行数/单位/哈希最小映射。正式JSON gzip以`$float`保留NaN/±Inf，原始身份JSON保持文字。E5对全部正式文件读回核列、行、值及浏览器模型身份，并核携带段裁剪；均一致。本图无动态标准化，fit_y/刻度只改轴，本轮不需另取viewport_final。

原U PARTIAL/未暴露内部轨迹、三年总览密度、Rct更新行口径、既有明细替代拓扑、Q边界以及四问题/七candidate-only均明确传递。原C3页内标题仍含“C2当前展示预期”，真实绑定在caption和文档title明确；未无痕改原C。`f800.runtime.json`是构图当时、E3/E5之前的原始记录，后续专业状态以E3/E5及材料包为准。

Owner连续状态：D001已接收；X/G沿D00839f有效新生产与完整统计成果复用，历史正式producer/native进程已结束；当前结果目录见原 `FeatureRunResultBinding.json`。本D实际运行的是只读F/CAEGraph Python进程，均已退出0，未启动新的正式生产进程。G的PASS_TO_SCENARIO_REVIEW和已关闭finding不改；本E无阻断。

专业结果先发布，再单独发布原V2 C0027 Return回原manager。仅本D/原E材料准备完成；未冻结场景预期、未签FeatureReleaseGate/ReleasePackage，不运行或释放Q/V、不改WALL，父Run仍待原manager继续。
''')
(R/'VALIDATION.md').write_text('''# 验证及回交边界

E3亲自核实际图与D/C2，E4在接受后冻结准入并正式导出，E5从实际正式文件逐值核同接受图。`construction_snapshot`直接来自同次已接受HTML嵌入CDS；没有因Python构图进程已退出而重跑Feature或构图。原生PlotDataNode持有的CDS已被该HTML序列化，模型id/renderer/列/行数/数据哈希构成最小映射。轴和viewport不会被冒充为原生业务轨迹。

原87b longrun_gate.py及schema字节保持。完整CLI binding()仍固化ChatGPT manager类型，与本Run既有Codex manager不兼容；沿既有披露，用原validated/pro_state/object_ref_fields核原schema/状态/ref，再核实际I/D/最新Binding/token/权限子集/workers空、先发布准确专业对象和manifest。没有改gate、伪造controller receipt或声称完整CLI通过；具体见本C RETURN_VALIDATION.json。

记录分支以gzip无损保存最终HTML及首版档案、正式CDS文件；授权BASE保留原可打开HTML。HTML_ARCHIVES及专业manifest记录压缩前后哈希；不能把首版过密轴当最终接受图。仅本Run professional/D012和calls/C0027有本次写入。
''')
write('E6_HANDOFF.json',dict(status='DATA_READY',material='ObservationMaterialPackage.json',E_stages_complete=True,formal_data_files=21,E5='一致',remaining_E_scope=[],next='原manager消费本C后依原Workflow推进适用S1/S2与L1；本E1不代签场景或Feature释放',workers=[]))
print(json.dumps(dict(status='DATA_READY',formal_files=21,html_archives=[dict(archive=x['archive'],bytes=x['compressed_bytes']) for x in archives]),ensure_ascii=False))
