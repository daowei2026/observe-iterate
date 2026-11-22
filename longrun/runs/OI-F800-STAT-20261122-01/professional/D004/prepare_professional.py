"""只有真实构建、回归与远端代码发布通过后，才形成 FI 原生回交。"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import gzip
import hashlib
import json
import subprocess

ROOT=Path(__file__).resolve().parent
BASE=Path('/dwdhome/fy/BASE_E6_2_copy')
FRP=BASE/'.runtime/f-observation-multiple-github-20261122/frp'
RECORD=Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
PREFIX='longrun/runs/OI-F800-STAT-20261122-01'
RUN='OI-F800-STAT-20261122-01'
OLD='ac1927518ad6105f15ffbe37fea45e4be91ba574'
TIS='2f460d663d821cf2ba25555eda13e78b697d0767'
PARAM='b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3'
DIAG=f'daowei2026/observe-iterate@a99ab37cdcf43759b7f203a1233fe69a7fa733db:{PREFIX}/professional/D003/DiagnosisReport.json#F800-DIAG-001'
AUTH=f'daowei2026/observe-iterate@8a4139b9250ed78c602f4c54b36a08380b196057:{PREFIX}/owner-decisions/F800-MP-001/OWNER_APPROVAL.original.txt'
def load(name): return json.loads((ROOT/name).read_text())
def write(name,value): (ROOT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def git(*args): return subprocess.check_output(['git',*args],cwd=FRP,text=True).strip()
parser=argparse.ArgumentParser(); parser.add_argument('--commit',required=True); args=parser.parse_args()
commit=args.commit
assert len(commit)==40 and git('rev-parse','HEAD')==commit and git('rev-parse','HEAD^')==OLD
assert git('branch','--show-current')=='codex/f-observation-multiple-20261122'
assert not git('status','--porcelain')
files=git('diff','--name-only',OLD,commit).splitlines()
assert files==['src/Frp/Instance/ISL/Opportunity/U2/GroupCandidateKLineInput.hs','test/U2ObservationWindowSpecMain.hs']
build=load('BUILD_STATUS.json'); tests=load('TEST_RESULTS.json'); publication=load('CODE_PUBLICATION_READBACK.json')
assert build['completed'] and build['exit_code']==0 and build['baseline_binaries_unchanged'] and build['baseline_source_unchanged']
assert tests['completed'] and tests['baseline_checks_retained'] and all(t['completed'] for t in tests['tests'])
assert publication['commit']==commit and publication['remote_branch_head']==commit
assert len(publication['files'])==2 and all(f['local_git_blob_match'] for f in publication['files'])
assert all(sha(FRP/path)==value for path,value in load('BUILD_INPUT_MANIFEST.json')['files'].items())
for name,record in build['binaries'].items(): assert sha(Path(record['path']))==record['sha256']
version='daowei2026/frp@'+commit
config=subprocess.check_output(['git','show','3169703e769340200b183dad7675a1d22ecc1850:'+PREFIX+'/professional/D002/configuration.json'],cwd=RECORD)
(ROOT/'configuration.json').write_bytes(config); assert sha(ROOT/'configuration.json')==PARAM
patch=subprocess.check_output(['git','diff',OLD,commit,'--',*files],cwd=FRP)
(ROOT/'IMPLEMENTATION.patch').write_bytes(patch)
(ROOT/'build.log.gz').write_bytes(gzip.compress((ROOT/'build.log').read_bytes(),mtime=0))
behavior='正常KLine覆盖以精确频率/Calendar换算得到的正整数原始UTI步长判定相邻；previous持有Int64源UTI与覆盖Clock，使用Integer差避免溢出。首次/真实缺口仅给点；Material严格累积、失败、未知Clock、800观察窗和实际2Δ保持。closeUti复用exactUTI，拒绝隐式round；Q报价Double位置接口保持。'
native={'diagnosis_ref':DIAG,'code_commit':commit,'changed_files':files,
    'changed_behavior':behavior,'tests':[
        {'name':'隔离构建','result':'PASS','targets':['frp:exe:dbaw','frp:exe:u2-observation-window-check','trade-poc:exe:ts'],
         'evidence':'BUILD_STATUS.json + build.log.gz','exit_code':build['exit_code']},
        *[{'name':t['name']+' 原生窗口回归','result':'PASS','command':t['command'],
           'checks':t['pass_count'],'exit_code':t['exit_code'],'evidence':t['name']+'-window-checks.log'} for t in tests['tests']]],
    'new_feature_version':version,'ready_for_feature_rerun':True}
write('ImplementationFixReturn.json',native)
runtime=Path(build['runtime'])
old_runtime=BASE/'.runtime/f-wide-observation-20261122/runtime'
assert (runtime/'edh-universe/frp/frp').resolve()==FRP.resolve()
assert (runtime/'mquant/tis').resolve()==(old_runtime/'mquant/tis').resolve()
adoption={'run_id':RUN,'call_id':'C0010','delegation_id':'D004','adopted_at':datetime.now(timezone.utc).isoformat(),
    'authority_ref':AUTH,'diagnosis_ref':DIAG,'proposal_id':'F800-MP-001','previous_frp':OLD,'new_frp':commit,
    'remote_repository':'daowei2026/frp','remote_branch':'codex/f-observation-multiple-20261122',
    'source_root':str(FRP),'source_clean':True,'runtime':str(runtime),'runtime_source_resolves_to_new_checkout':True,
    'tis_commit':TIS,'tis_same_frozen_runtime_as_D002':True,'tis_runtime':str((runtime/'mquant/tis').resolve()),
    'tis_constructor_and_codec_remote_readback':'TIS_PIN_READBACK.json',
    'parameter_version':PARAM,'configuration_ref':'configuration.json','binaries':build['binaries'],
    'build_input_manifest':'BUILD_INPUT_MANIFEST.json','remote_readback':'CODE_PUBLICATION_READBACK.json',
    'formal_new_result':None,'formal_feature_run_in_D004':False,'adoption_purpose':'下一完整正式X的准确代码与运行时；尚无新正式结果或释放'}
write('CodeVersionAdoption.json',adoption)
impact={'structural_contract_changed':False,'affected_understanding_update_required':False,'next_node':'X',
    'basis':'对象/身份/状态/事件/生命周期/存储字段及完整序列化配置无结构变化；仅纠正覆盖边数值实现及声明离散入口校验。原D001最小理解和D002缺口处置继续可用，不重做完整U。',
    'unchanged_contract_files':['CommonPriceTurnGroupCandidates.hs','U2/GroupCandidateTypes.hs','U2/GroupCandidateMaterial.hs',
        'U2/GroupCandidateEvolution.hs','U2/GroupCandidateStorage.hs','U2/Formation.hs','PostTurnGroupDirectionalOrganization.hs',
        'U2/DirectionalOrganizationMotion.hs'],
    'changed_business_values':'覆盖及变化时刻可改变candidate affected/body、Revision密度、exact引用与UUID链；数量必须由新X/G测量，不能从局部回归推定。',
    'shared_consumer_assessment':{
        'F':'CommonPriceTurnGroupCandidates.hs:186 消费修后的形成覆盖边',
        'Q':'PostTurnGroupDirectionalOrganization.hs:224 也调用共享形成适配器；directionalQuoteEvents四元组/Double位置换算保持。',
        'Q_separate_numeric_boundary':'源码DirectionalOrganizationMotion.hs:195及243另有归一化位置相邻比较；本补丁不修该独立逻辑，未运行Q，不能推定其路径覆盖已修复。此为影响评估和后续依赖限制，不扩大本Run。',
        'V':'不直接导入适配器；经F→Q→V真实依赖传递影响。',
        'formal_Q_V_runs':False,'release_effect':'按L1必须消费准确新F释放包；依赖旧F的下游结果应由其所属Run判断STALE_UPSTREAM，当前无新释放包。'},
    'supported_input_contract':'EXACT_STEP_DESIGN.md','full_comparison_pending':'完整三年F X、31表独立读回和G；原22位置及全部结构/密度/身份/4项场景问题重新核对。'}
for file in impact['unchanged_contract_files']:
    path='src/Frp/Instance/ISL/Opportunity/'+file
    assert subprocess.check_output(['git','show',OLD+':'+path],cwd=FRP)==(FRP/path).read_bytes()
write('ContractAndDependencyImpact.json',impact)
store=BASE/'artifacts'/RUN/('post-fix-'+commit)/'attempt01/store'
assert not store.exists(), 'next X must have a new store'
handoff={'next_actor':'原manager消费本ImplementationFixReturn后签发新X委派给原E1；无需再次询问批准',
    'new_feature_version':version,'tis_version':'daowei2026/tis@'+TIS,'runtime':str(runtime),
    'configuration_ref':'configuration.json','configuration_sha256':PARAM,
    'requested_scope':{'feature':'CommonPriceTurnGroupCandidatesFrp','only_f':True,'symbols':['rb','hc','i'],'freq':'5m',
        'start_time':'2021-01-01','end_time':'2023-12-31','calendar':'night_end_at_2300','sof':'TA_updto20240229_DBA','stk_tlist':'steel'},
    'locked_parameters':{'observation_multiple':800,'delta':600,'unit':'CalendarUTITick','actual_2delta_uti':1200,'method_revision':'1',
        'inputs_sources_domain_result_layout':'与configuration.json完全相同'},
    'suggested_new_store':str(store),'store_created':False,'new_formal_result':None,
    'pre_run_checks':'新D内再次核实际加载、完整序列化配置、Calendar/范围、full_dir/fields/config身份和真实单写者；持HEAVY_RESOURCE_POLICY实际flock才生产。',
    'post_run_checks':'完整F一次新生产、独立进程31表读回、全量G及原finding/新finding、Revision/exact/UUID影响；然后原Workflow处理释放。',
    'old_baseline_preserved':True,'old_X_G_role':'历史对照，不能继续充当新版本Gate证据','feature_release_gate':'RERUN_REQUIRED'}
write('RERUN_HANDOFF.json',handoff)
write('FindingDisposition.json',{'finding_id':'F800-GF-001','diagnosis_ref':DIAG,'proposal_id':'F800-MP-001',
    'status':'FIXED_PENDING_RERUN','implementation_fix_ref':'ImplementationFixReturn.json','new_feature_version':version,
    'latest_profile_on_new_version':False,'closed':False,'feature_release_gate':'RERUN_REQUIRED',
    'closure_condition':'最新完整F X、31表独立读回及G确认原finding不再发生，并处理新发现和身份/密度影响。'})
write('VALIDATION.json',{'completed':True,'scope':'D004 FI实施与重跑准备；不是完整X/G或FeatureRelease',
    'source_refs_checked':load('SOURCE_REF_AUDIT.json')['count'],'owner_approval_byte_equal':True,
    'changed_files':files,'build_pass':True,'native_regression_pass':True,'code_published_and_read_back':True,
    'actual_new_source_adopted':True,'configuration_unchanged_sha256':PARAM,'structural_contract_changed':False,
    'baseline_source_and_binaries_preserved':True,'new_formal_feature_run':False,'full_comparison_pending':True,
    'finding_status':'FIXED_PENDING_RERUN','feature_release_gate':'RERUN_REQUIRED','next_node':'X','workers':[]})
report=f'''# D004｜F800-MP-001 实施回交

已完成 Owner 批准的正常 KLine 相邻覆盖修复、原生回归及准确新 FRP 版本提交/推送/采用。原生返回见 [ImplementationFixReturn.json](ImplementationFixReturn.json)。新代码 **{commit}**；finding 为 **FIXED_PENDING_RERUN**，FeatureReleaseGate 为 **RERUN_REQUIRED**。

本次 C0010/E1 亲自执行原 D004，workers=[]，回原 manager。39 项准确 Git 对象与当前输入逐字节一致，批准原文与 packet 原件一致；D004 另经 GitHub 连接器准确提交读回。见 [SOURCE_REF_AUDIT.json](SOURCE_REF_AUDIT.json)、[REMOTE_INPUT_READBACK.json](REMOTE_INPUT_READBACK.json)。

## 实施及支持合同

覆盖边使用源 Int64 UTI 的 Integer 差，比较经频率/Calendar 换算得到的正整数步长，避免两个大浮点商之差严格等于1。previous 仅持源 UTI 和 Clock，首次或真实缺口只给当前点。原 Material 严格累计及候选演化保持。

固定秒/分钟频率下，准确原始步长为 `freq_ns / 60000000000 × units_per_open_minute / units_per_calendar_tick`，用实际 Double 值的精确有理数计算；有限、正、整数且在 Int64 内才接受。Tick 和名义日/周/月不能据 ns 推定开放时长，明确拒绝。非整数步长/原UTI不做盲目 round 或添加 epsilon；源UTI复用既有 exactUTI。当前 5m × 120 / 1 = 600UTI。详见 [EXACT_STEP_DESIGN.md](EXACT_STEP_DESIGN.md)。

仅改变适配器和现有回归入口两个文件，见 [IMPLEMENTATION.patch](IMPLEMENTATION.patch) 与 [准确代码提交](https://github.com/daowei2026/frp/commit/{commit})。完整配置字节 SHA-256 仍为 `{PARAM}`；800、delta600、CalendarUTITick、实际2Δ=1200、method.revision1、inputs/sources/domain/result_layout、TIS@{TIS} 均按批准保持。

## 实际验证与采用

隔离运行时已构建 dbaw、原生窗口检查与 ts，构建退出0。原基线窗口检查 {tests['tests'][0]['pass_count']} 项和修后 {tests['tests'][1]['pass_count']} 项全部通过，原检查全部保留。新检查将实际生产 helper 的覆盖边送入原 Material：真实2^17数值边界旧guard失败而新边保持800Δ完整覆盖；真实1200UTI缺口、冷启动、SourceFailure 后恢复与未知Clock不会被桥接；Clock明确修订可恢复；支持/拒绝的频率和单位换算有实测。原窗口、revision/handoff、方向、期限和真实1200/1201UTI的2Δ边界均通过。

证据：[TEST_RESULTS.json](TEST_RESULTS.json)、[fixed-window-checks.log](fixed-window-checks.log)、[baseline-window-checks.log](baseline-window-checks.log)、[BUILD_STATUS.json](BUILD_STATUS.json)、[完整构建日志](build.log.gz)。测试为 FI 回归，未启动正式 Feature。源文件构建前后SHA及新二进制路径/hash有绑定；目标授权分支经真实推送、ls-remote 和 GitHub 两个文件准确提交读回，见 [CODE_PUBLICATION_READBACK.json](CODE_PUBLICATION_READBACK.json)。

首次构建观察脚本把ps空子进程返回1当异常退出，没有将未知编译状态登记成功；核对原构建已不在运行后修正监控，重新构建，验收取本次真实退出0。原状态保留在 [BUILD_ATTEMPT1_MONITOR_FAILURE.json](BUILD_ATTEMPT1_MONITOR_FAILURE.json)。

新版本及隔离运行时已采用用于下一 X，见 [CodeVersionAdoption.json](CodeVersionAdoption.json)。旧 D002 源码、3个二进制 hash保持，D002结果/D003诊断没有覆盖。TIS 冻结副本与原 D002 路径相同；未把父 Git 仓库 HEAD 当 TIS 版本证明。

TIS正常构造器及F Python参数类另以锁定2f提交从GitHub准确读回，与实际冻结副本的Git blob逐一吻合，见 [TIS_PIN_READBACK.json](TIS_PIN_READBACK.json)。

## 影响与后继

对象、身份、业务状态/事件、生命周期和结果布局没有结构变化；相关合同文件字节未变。因此按原 L0 §9 和 FI Gate 直接 **X→独立31表读回→G**，无需重做完整 U。D001 已接收的最小理解及 D002 缺口处置保留。

F/Q共享形成适配器，因此 Q 会取得修后的覆盖边；Q 的报价四元组/Double位置换算保持。源码还显示 Q 的运动模块另有归一化位置相邻判断，此独立逻辑未改、未正式运行，不能据本修复声称 Q 路径覆盖通过。V 经真实依赖间接受影响。详见 [ContractAndDependencyImpact.json](ContractAndDependencyImpact.json)。本Run仅F，不扩为Q/V或WALL修改。

覆盖变化可能改变 candidate affected/body、Revision密度、exact引用及UUID链。局部回归不承诺正式只减少22个观点或保持原随机ID。完整三年新生产、原22位置、全部结构/密度与既有4项场景问题必须由后继 X/G 实测；当前无新正式结果和 UpstreamReleasePackage。

原 manager 消费本返回后，按已批准范围签发下一 X，无需再请 Owner 确认。准确代码/运行时、原完整配置和未创建的新store建议位置在 [RERUN_HANDOFF.json](RERUN_HANDOFF.json)；新D中重新核真实单写者/加载/配置/结果身份并持实际 flock。旧 X/G 留历史对照，不充当新版本 Gate 证据。

Owner七项进度：D001已接收且不重做；旧X完成、修后X待正式后继；旧结果来自D002一次新生产；本C只构建/回归而未运行正式ts生产；当前正式结果目录仍是D002/store旧基线，新store未创建；旧G1–G8完成而修后G未开始；本D无未解决事实阻断，释放受完整复验未完成约束。

D004 FI职责已完成，完整Run仍未完成。先发布本专业产物，再以已存在的 exact 提交形成 C0010 原 V2 PRO_RETURN；没有创建 Worker、委派或跨线程发送，也不声称 manager 已消费。
'''
(ROOT/'EXECUTOR_REPORT.md').write_text(report)
print(json.dumps({'new_frp':commit,'native_return':'ImplementationFixReturn.json','ready_for_feature_rerun':True,'finding':'FIXED_PENDING_RERUN','gate':'RERUN_REQUIRED'},ensure_ascii=False))
