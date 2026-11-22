"""仅在真实构建/回归及FRP远端发布完成后，形成D007原生FI回交。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import argparse,csv,gzip,json,subprocess

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parents[2]
RUN='OI-F800-STAT-20261122-01'
FRP=BASE/'.runtime/f-observation-multiple-github-20261122/frp'
NEW=BASE/'.runtime/f800-input-missing-20261123/runtime'
OLD=BASE/'.runtime/f800-exact-uti-20261122/runtime'
PARSER=argparse.ArgumentParser();PARSER.add_argument('--code-commit',required=True);args=PARSER.parse_args()
COMMIT=args.code_commit;assert len(COMMIT)==40
DIAG='daowei2026/observe-iterate@46de903caa04be60a5600ef9f416445f5a6366cd:longrun/runs/'+RUN+'/professional/D006/DiagnosisReport.json#F800-DIAG-002'
APPROVAL='daowei2026/observe-iterate@2fa5c26a739d8d97a733f6a7581092a271724e6e:longrun/runs/'+RUN+'/owner-decisions/F800-MP-002/OWNER_APPROVAL.original.txt'
def load(p):return json.loads(p.read_text())
def write(n,v):(ROOT/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def git(*a):return subprocess.check_output(['git',*a],cwd=FRP)
def digest(p):
 h=sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def prior(n):return 'daowei2026/observe-iterate@38e2af72be826a1e98fd7f5d4522c50d218750f3:longrun/runs/'+RUN+'/professional/D005/'+n
assert git('rev-parse','HEAD').decode().strip()==COMMIT and not git('status','--porcelain')
assert git('branch','--show-current').decode().strip()=='codex/f-observation-multiple-20261122'
build=load(ROOT/'BUILD_STATUS.json');assert build['completed'] and build['exit_code']==0 and build['build_exit_code']==0
assert len(build['tests'])==3 and all(x['exit_code']==0 for x in build['tests'])
assert build['baseline_binaries_unchanged'] and build['baseline_source_unchanged']
assert build['binaries']['ts']['sha256']!=load(ROOT/'RUNTIME_PREPARATION.json')['baseline_binaries']['ts']['sha256'], 'new ts must not be stale old binary'
assert load(ROOT/'DEPENDENCY_BINDING.json')['all_match']
assert load(ROOT/'RUNTIME_LOADING_PREFLIGHT.json')['completed']
publication=load(ROOT/'CODE_PUBLICATION_READBACK.json')
assert publication['commit']==COMMIT and publication['remote_branch_head']==COMMIT and all(x['local_git_blob_match'] for x in publication['files'])
manifest=load(ROOT/'BUILD_INPUT_MANIFEST.json')
for row in manifest['files']:
 assert sha256(git('show',COMMIT+':'+row['path'])).hexdigest()==row['sha256'] and digest(FRP/row['path'])==row['sha256']
changed=git('diff','--name-only','be57d6752c9d43d10f1d670e1d2993bb8153ea7c',COMMIT).decode().splitlines()
assert set(changed)=={'src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateKLineInput.hs','test/U2KLineCoverageAdapterSpecMain.hs','frp.cabal'}
assert load(ROOT/'APPROVED_DIFF_CONFORMANCE.json')['implemented_diff_content_exact']
config=(ROOT.parent/'D005/configuration.json').read_bytes()
assert sha256(config).hexdigest()=='b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3'
(ROOT/'configuration.json').write_bytes(config)
traces={}
for name in ['baseline','fixed']:
 with (ROOT/(name+'-adapter-trace.csv')).open() as f:traces[name]=list(csv.DictReader(f))
assert len(traces['baseline'])==len(traces['fixed'])==7475
assert [(x['known'],x['object']) for x in traces['baseline']]==[(x['known'],x['object']) for x in traces['fixed']]
fixed=traces['fixed'];missing=[x for x in fixed if x['condition']=='CoverageInputMissing']
assert len(missing)==209 and all(x['from']==x['through']=='Nothing' and x['domain_incomplete']=='1' for x in missing)
assert all(x['condition']=='CoverageObserved' for x in traces['baseline'])
counts={}
coverage_lines=(ROOT/'fixed-coverage-controls.log').read_text().splitlines()
coverage_header=coverage_lines.index('control,expected,actual,passed')
coverage_controls=list(csv.DictReader(coverage_lines[coverage_header:]))
assert len(coverage_controls)==8 and all(x['passed']=='True' for x in coverage_controls)
for name,logfile,expected in [('adapter','fixed-adapter-check.log',13),('window','fixed-window-checks.log',64)]:
 log=(ROOT/logfile).read_text();counts[name]=sum(x.startswith('PASS ') for x in log.splitlines());assert counts[name]==expected
 assert ('ALL NORMAL KLINE ADAPTER CHECKS PASSED' if name=='adapter' else 'ALL OBSERVATION WINDOW CHECKS PASSED') in log
tests=[dict(name='真实正常KLine适配回归',result='PASS',checks=13,exit_code=0,
 input='合成原始Bar，ScaleTurn/Zig无事件；缓存注入上游结果，实际运行Generic KLine→close/UTI join→buildKLineGroupSource局部advance→Material。不手造CoverageInputMissing或FormationFrame输入。',
 observations=dict(calendar_firings=2492,actual_source_frames=7475,nonfinite_input_missing_frames=209,nan_frames=207,positive_infinity_frames=1,negative_infinity_frames=1),
 evidence=['fixed-adapter-check.log','fixed-adapter-trace.csv','REGRESSION_COMPARISON.json']),
 dict(name='旧be57真实适配负对照',result='PASS_EXPECTED_FAILURE',program_exit_code=1,expected_failure=True,
 observation='同一测试/Bar流在旧be57实际adapter上到缺价断言失败；207个NaN帧全为Observed且错误完整，修后为InputMissing；不是编译失败冒充反例。',evidence=['BASELINE_REGRESSION.json','baseline-adapter-check.log','baseline-adapter-trace.csv']),
 dict(name='既有观察窗口与数值/生命周期边界',result='PASS',checks=64,exit_code=0,
 scope='GF001原始UTI边界/600准确相邻/冷启动/真实间隙、未知Clock、800/600/实际2Delta=1200、deadline/r/稀疏发行和引用不变量；不代替下一完整G的22+8逐位置复验。',evidence=['fixed-window-checks.log']),
 dict(name='既有Material覆盖控制',result='PASS',checks=8,exit_code=0,scope='同新库执行D006既有控制：冷启动、无Turn有效流、单对象SourceFailure/InputMissing/ClockUnknown、真实UTI缺口与明确Inapplicable。',evidence=['fixed-coverage-controls.log']),
 dict(name='隔离正式引擎及回归目标构建',result='PASS',exit_code=0,targets=build['build_command'][4:8],evidence=['BUILD_STATUS.json','BUILD_INPUT_MANIFEST.json','build.log.gz'])]
comparison=dict(completed=True,actual_adapter_graph=True,formal_feature_run=False,upstream_input_kind='explicit synthetic raw Bars; same exact UTI grid with 69-point NaN pattern plus Infinity/true-gap controls',
 baseline=dict(frp='be57d6752c9d43d10f1d670e1d2993bb8153ea7c',expected_program_exit_code=1,frames=7475,nan_as_observed=207),
 fixed=dict(frp=COMMIT,program_exit_code=0,checks=13,frames=7475,nonfinite_as_input_missing=209),
 invariant_axes_equal=True,restoration_after_nan=dict(first_success=93715799,first_complete=94195799,observation_duration=480000),
 assertions='真实adapter检查NaN/±Infinity、单对象失败、失败后首点、Clock推进、有限零量/无Turn、真实UTI空洞以及恢复800Delta前/等号边界。',
 limit='上游Bar/空Turn是明确合成输入；未重跑正式F候选、未测新Life/Revision/发行/UUID总量。原8观点的自然对象对应与全量缺价窗冲突由后继完整X/G实测。')
write('REGRESSION_COMPARISON.json',comparison)
write('ImplementationFixReturn.json',dict(diagnosis_ref=DIAG,code_commit=COMMIT,changed_files=changed,
 changed_behavior='按MP002原diff：正常KLine非有限close（NaN/±Infinity）发CoverageInputMissing Nothing Nothing并清previous成功邻接状态；有效UTI/Clock继续推进，恢复首个有限价从当前点开始累计。有限价零量/无Turn仍可Observed，精确UTI步长及800/600/2Delta和既有材料/确认规则不变。',
 tests=tests,new_feature_version='daowei2026/frp@'+COMMIT,ready_for_feature_rerun=True))
adoption=dict(run_id=RUN,call_id='C0017',delegation_id='D007',proposal_id='F800-MP-002',adopted_at=datetime.now(timezone.utc).isoformat(),
 authority_ref=APPROVAL,binding_ref='daowei2026/observe-iterate@3dc11a9dbf39e181b3c6a3051419a90e46b92aac:longrun/runs/'+RUN+'/RUN_BINDING.json',
 previous_frp='be57d6752c9d43d10f1d670e1d2993bb8153ea7c',new_frp=COMMIT,remote_repository='daowei2026/frp',remote_branch='codex/f-observation-multiple-20261122',
 source_root=str(FRP),source_clean=True,runtime=str(NEW),runtime_source_resolves_to_new_checkout=(NEW/'edh-universe/frp/frp').resolve()==FRP,
 previous_runtime=str(OLD),previous_runtime_source_snapshot=str((OLD/'edh-universe/frp/frp').resolve()),baseline_binaries_unchanged=True,
 tis_commit='2f460d663d821cf2ba25555eda13e78b697d0767',tis_runtime=str((NEW/'mquant/tis').resolve()),
 tis_same_frozen_runtime_as_D005=(NEW/'mquant/tis').resolve()==(OLD/'mquant/tis').resolve(),dependency_content_check='DEPENDENCY_BINDING.json',
 parameter_version=sha256(config).hexdigest(),configuration_ref='configuration.json',binaries=build['binaries'],runtime_loading_preflight='RUNTIME_LOADING_PREFLIGHT.json',
 build_input_manifest='BUILD_INPUT_MANIFEST.json',remote_readback='CODE_PUBLICATION_READBACK.json',formal_new_result=None,formal_feature_run_in_D007=False,
 adoption_purpose='下一原manager完整新X/G的当前准确版本及运行时；本D仅FI，不签正式释放。')
assert adoption['runtime_source_resolves_to_new_checkout'] and adoption['tis_same_frozen_runtime_as_D005']
write('CodeVersionAdoption.json',adoption)
write('ContractAndDependencyImpact.json',dict(proposal_id='F800-MP-002',diagnosis_ref=DIAG,adopted_version='daowei2026/frp@'+COMMIT,
 production_diff_exact_approved=True,structure_contract_changed=False,schema_or_saved_fields_changed=False,objects_or_identity_contract_changed=False,
 behavior_change='非有限close的正常覆盖分类与previous成功状态；缺价区别在原责任边界保留。',
 stable_parameters=['observation_multiple=800','delta=600','CalendarUTITick','2Delta=1200UTI','method.revision=1','inputs/sources/domain/result_layout/schema、PNV、SOF/Calendar及完整F-only范围'],
 affected_understanding='仅当前代码/运行时绑定与J4覆盖分类事实更新；见CurrentFeatureUnderstandingDelta.json，不重做完整U。',
 next_route='结构合同未变：仅核受影响绑定后直接新X→31表独立读回→原Skill全量G→原L1释放处理。',
 identity_effect='覆盖标记参与候选正文/稀疏发行；Revision/发行时点数量和UUID/exact链须完整新运行实测，不能从13项局部测试预设。',
 dependencies=dict(Q='共享正常KLine适配有行为影响可能，Q另一路数值边界限制保留；本Run不运行或释放Q。',V='下游证据版本需随未来F/Q发布核对；未验证V。',WALL='无改动或授权扩展。'),
 formal_run_and_release_not_claimed=True))
write('CurrentFeatureUnderstandingDelta.json',dict(previous_understanding_ref=prior('CurrentFeatureUnderstandingPackage.json'),
 previous_frp='be57d6752c9d43d10f1d670e1d2993bb8153ea7c',current_frp=COMMIT,scope='仅本次FI受影响部分，完整理解已接受不重做',
 inherited_status='PARTIAL，原未暴露内部轨迹等限制保留；不把FI测试提升为完整理解或G。',
 changed_intermediate_decision='J4正常KLine覆盖：有限close的有效观测走准确源UTI相邻；非有限close为InputMissing并清previous；Clock不被价格失败删除。',
 events_states_fields='ObjectCoverage、CoverageInputMissing、FormationFrame、Material、候选/保存字段既有结构不变。',
 result_binding='旧D005仍是旧be57历史真实结果；当前新代码没有正式FeatureRunResultBinding，待新X生成。',
 parameter_version=sha256(config).hexdigest(),actual_runtime='CodeVersionAdoption.json',next_route='直接新X，随后原G；无新全量U要求。'))
write('FindingDisposition.json',dict(finding_id='F800-GF-002',status='FIXED_PENDING_RERUN',closed=False,proposal_id='F800-MP-002',
 diagnosis_ref=DIAG,implementation_ref='ImplementationFixReturn.json',code_commit=COMMIT,
 local_real_adapter_tests_pass=True,full_new_instance_retest=False,
 preserved_GF001=prior('FindingDisposition.json'),GF001_limitation='原22+8关闭结论保留为D005已完成事实；当前新版本须后继完整X/G再次保护验证，不宣称局部64项等于三年逐位置复验。'))
write('RERUN_HANDOFF.json',dict(workflow_status='RERUN_REQUIRED',new_code_commit=COMMIT,ready_for_feature_rerun=True,
 required_next='原manager消费FI后，完整新F-only X→31表独立OnlyRead→原Skill全量G；批准覆盖该后继，无需重复请示同范围。',
 old_binding=prior('FeatureRunResultBinding.json'),old_gate=prior('GlobalProfileGate.json'),old_result_use='原be57结果/G保留为历史对照，不是新代码当前Gate证据。',
 preserve=['D002—D006原件及旧结果','GF001旧版本闭环事实','四项场景问题','Q独立数值边界限制'],
 scope=dict(symbols=['rb','hc','i'],freq='5m',years=[2021,2022,2023],calendar='night_end_at_2300',sof='TA_updto20240229_DBA',stk_tlist='steel',configuration_sha256=sha256(config).hexdigest()),
 runtime_wrapper='run_in_runtime.py（指向新runtime）；不得沿用D005旧wrapper冒充新引擎',new_attempt_required=True,new_store_required=True,resource_policy='HEAVY_RESOURCE_POLICY.json：真实单写者和实际flock；运行前重核code/binary/config/load/Calendar/resultidentity。',
 mandatory_retests=['GF002原8观点按自然对象/known对应及全量缺价窗冲突','GF001原22位置+8冷启动对照','全部31表、fields/config身份和引用exact链','真实Life/Revision/发行/UUID变化，不预设计数'],
 no_new_FeatureReleaseGate=True,no_new_ReleasePackage=True,no_Q_V_WALL_execution=True))
write('VALIDATION.json',dict(completed=True,validated_at=datetime.now(timezone.utc).isoformat(),native_FI_contract_complete=True,
 exact_refs_audited=47,owner_approval_verified=True,production_diff_exact=True,
 code_commit=COMMIT,code_published_and_remote_read_back=True,source_manifest_files_verified=len(manifest['files']),
 build_exit_code=0,real_adapter_checks=13,old_window_checks=64,material_coverage_controls=8,expected_old_adapter_failure=True,
 baseline_source_and_binaries_preserved=True,new_runtime_isolated=True,current_configuration_sha256=sha256(config).hexdigest(),
 no_formal_F_run_in_D007=True,no_new_full_G_in_D007=True,no_release_claim=True,workers_empty=True,
 fixture_vs_formal_input_distinguished=True,ready_for_feature_rerun=True))
(ROOT/'EXECUTOR_REPORT.md').write_text(f'''# D007｜已批准MP002的FI实施回交

已按批准的F800-MP-002具体diff完成正常KLine缺价覆盖修复，并提交、推送和采用FRP `{COMMIT}`。真实正常适配回归13项、既有窗口/数值/生命周期回归64项、Material覆盖控制8项及四个隔离构建目标均通过；旧be57在同一真实适配测试上产生预期失败。ImplementationFixReturn.ready_for_feature_rerun=true。

本D仅FI完成，GF002为FIXED_PENDING_RERUN，尚未关闭。新代码完整三年X/31表独立读回/G和释放由原manager消费后按原Workflow接续；批准已覆盖该后继，无需再次确认。原D005及GF001闭环原件保留；不把旧X/G当新版本证据。

## 准确委派与批准

C0017/D007，原E1，workers=[]。已亲自读取准确packet、D007全文、同版control-v0.3 L2的FI工程行、L0 §7/9以及control/03 §8.1、control/04 XI、control/05返回合同。FI不是新增Skill。47项exact输入、最新Owner原文及当前Binding核同；远端D/I/批准三份blob核同。

Owner批准：`{APPROVAL}`，原文923字节、SHA-256 `a9c626ec667171e7f4605b853d360597a471d6bc82002574f938ab4d269058eb`。最新Binding@3dc11a9dbf39e181b3c6a3051419a90e46b92aac。原提案diff为1630字节，SHA-256 `95d05a657e16537da28aaeea89d5d00c1302fc6c6427e801388c4985ac314d9e`；实际生产文件的变更及上下文与批准diff一致，另增必要回归源码和cabal目标。

## 修复与真实回归

生产改动仅`GroupCandidateKLineInput.hs:advance`：保留同拍close；非有限close（NaN/±Infinity）发InputMissing、清previous；有效UTI/Clock继续推进。恢复有限价先发行当前点，随后真实相邻边累计。有限价零量/无Turn仍可完整观察。源UTI准确相邻、800/600/实际2Delta=1200及既有材料/确认/保存合同不变。

新增回归以合成原始KLine Bar及无ScaleTurn/Zig事件注入既有Fao缓存，实际调用Generic KLine、close/UTI同拍join、buildKLineGroupSource及其局部advance和previous状态，再交真实Material。没有手造失败覆盖来替代分类位置。2492个Calendar时刻/7475个对象帧；旧be57的207个NaN帧全部为错误Observed，测试到缺价断言后真实退出1。修后同轴同输入全部209个非有限价帧（207 NaN、正负Infinity各1）为InputMissing，13项真实适配检查通过，包括单对象失败、Clock推进、恢复首点、满800Delta前/等号、真实1200UTI缺口、有限零量/无Turn。旧窗口64项及同新库Material覆盖控制8项也通过，分别保护GF001/生命周期边界与失败、失知、明确不适用等既有覆盖语义。

这是实际生产适配图的回归，使用明确合成上游，不是正式市场F实例。测试配置将PNV指向不存在的隔离路径、store指向本D fixture目录；成功只依赖注入Bar/空上游事件，不采用或修改真实PNV。首次测试编译遇到同名price字段歧义，改回归函数名后执行了有效旧版反例；原失败日志保留，不把编译失败当反例。只读加载预检首次误用目录包含关系判断逐文件软链接；核实际软链接后改为准确目标文件身份比较，最终预检须通过才采用，原失败日志保留。

## 新版本与隔离运行时

FRP分支 `codex/f-observation-multiple-20261122` 的真实新提交为 `{COMMIT}`，已推送至daowei2026/frp并远端blob回读。三个改动文件是生产适配文件、`test/U2KLineCoverageAdapterSpecMain.hs`及`frp.cabal`；其余source/test及完整配置经827文件manifest核同构建输入。

当前运行时：`{NEW}`；新ts/dbaw/窗口检查/适配检查的实际二进制指纹见CodeVersionAdoption/BUILD_STATUS。重型复制与构建均持真实flock并记录PID、子进程和开始/释放；本C未启动正式F。旧be57源码归档后让旧runtime指向该相同内容快照，旧三份二进制指纹不变；D005结果目录及原件未动。

TIS仍为2f460d663d821cf2ba25555eda13e78b697d0767，同冻结mquant/tis实路径；配置SHA-256仍`b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3`。PNV、SOF/Calendar、steel、rb/hc/i、5m、2021—2023和全部正式配置保持。只补CurrentFeatureUnderstandingDelta的代码绑定/J4语义；保存结构/对象/事件/字段合同未变，不重做完整U。

## 后继与未完成边界

原manager应沿原FI返回Gate核受影响绑定后直接签新X，再31表独立OnlyRead和原Skill完整G。必须新attempt/store，运行前重核实际加载/配置/完整范围/Calendar/resultidentity/单写者并持实际flock。新生产需实测GF002原8观点自然对象对应、GF001原22+8控制、全量缺价窗冲突及Life/Revision/发行/UUID/exact链变化。13+64+8局部通过不预设新产量或修后完整结果。

共享适配的Q影响与Q另一路数值边界限制继续传递；本Run不运行/释放Q/V或修改WALL。当前无新FeatureReleaseGate/ReleasePackage，四项场景问题保留。旧G及Gate原件作为历史保留，当前合法路由为RERUN_REQUIRED；本D不伪造新G或替manager完成释放。

专业原件：ImplementationFixReturn、CodeVersionAdoption、REGRESSION_COMPARISON、ContractAndDependencyImpact、CurrentFeatureUnderstandingDelta、FindingDisposition及RERUN_HANDOFF。先发布这些结果并远端核同，再单独发布引用已有exact专业提交的C0017原V2 Return；executor完成不代表manager已消费。
''')
(ROOT/'VALIDATION.md').write_text('''# D007验证与回交边界

Owner MP002明确批准、最新Binding及47项exact输入核对通过；实际生产变更符合具体批准diff。真实正常KLine适配的旧版本有效负对照、修后13项、既有64项及Material覆盖8控制通过；四个目标隔离构建退出0。合成原始Bar驱动实际adapter，未把手造失败覆盖或正式市场F运行混入。

新FRP已实际提交/推送并GitHub回读，源码与构建manifest匹配；旧代码快照、二进制和D005结果保留。新runtime/同TIS/完整配置绑定准确，仅FI ready，不声称完整新X/G或Feature释放。GF002为FIXED_PENDING_RERUN。

Return阶段继续使用未改87b锁定schema/gate函数validated/pro_state/object_ref_fields，另核真实I/D/最新Binding/权限、workers=[]及先行专业提交。完整validate-executor-return的binding()硬编码chatgpt manager，与本Run Codex manager不兼容，原gate不修改，不伪造完整CLI通过或独立controller receipt。
''')
with (ROOT/'build.log').open('rb') as inp,gzip.open(ROOT/'build.log.gz','wb') as out:
 for chunk in iter(lambda:inp.read(1024*1024),b''):out.write(chunk)
print(json.dumps(dict(ready_for_feature_rerun=True,code_commit=COMMIT,adapter_checks=13,window_checks=64,fixture_frames=7475,formal_F_run=False),ensure_ascii=False))
