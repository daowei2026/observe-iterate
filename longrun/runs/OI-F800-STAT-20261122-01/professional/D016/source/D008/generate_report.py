"""从当前新X和全量G原件生成中文报告，不继承历史运行完成声明。"""
from pathlib import Path
from datetime import datetime,timezone
import csv,json
ROOT=Path(__file__).resolve().parent
def load(n):return json.loads((ROOT/n).read_text())
def rows(n):
 with (ROOT/n).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
B=load('FeatureRunResultBinding.json');S=load('profile/SUMMARY.json');C=load('VersionComparison.json');AC=load('InitialVersionComparison.json');A=load('ANALYSIS_EXECUTION.json');G=load('GlobalProfileGate.json');V=load('VALIDATION.json');API=load('NATIVE_RETEST_API.json');F=load('FindingDisposition.json')
assert V['completed'] and A['completed']
fd={f['finding_id']:f for f in F['findings']}
def table(data,fields):
 return '| '+' | '.join(fields)+' |\n| '+' | '.join(['---']*len(fields))+' |\n'+'\n'.join('| '+' | '.join(str(r.get(k,'')) for k in fields)+' |' for r in data)
by_symbol=table(rows('profile/counts_by_symbol.csv'),['symbol','raw_turn_positions','scale_turn_positions','used_scale_turn_positions','candidate_lives','candidate_revision_occurrences'])
by_year=table([r for r in rows('profile/counts_by_symbol_year.csv') if r['symbol']=='ALL_DISTINCT'],['year','scale_turn_positions','candidate_lives','candidate_revision_occurrences'])
by_session=table(rows('profile/counts_by_session.csv'),['session','input_5m_positions','candidate_lives','revision_occurrences','revisions_per_1000_input_positions'])
checks=load('profile/STRUCTURAL_CHECKS.json');new=load('GlobalFindingCandidates.json');qs=load('ScenarioQuestionQueue.json')
report=f"""# D008｜39f完整正式F800 X与全量G回交

本D按manager D008和锁定Skill执行完成。当前正式代码FRP `39f02ec4548e68ba8dbd30061afc870546000994`、TIS `2f460d663d821cf2ba25555eda13e78b697d0767`；完整配置SHA-256 `{B['parameter_version']}`。本D没有修改正式Feature代码或参数。原生GlobalProfileGate=`{G['status']}`；本D不签FeatureReleaseGate或UpstreamReleasePackage，不运行/释放Q/V或改WALL。

## Owner要求的七项当前进度

1. D001最小理解已接收；复用D005结构理解与D007 delta，只核39f绑定及J4非有限close分类，没有重做完整U。
2. X已开始并完成：本次成功尝试 `{B['production']['started_at']}` 至 `{B['production']['finished_at']}`。
3. 重新生产。D005 be57及D002 ac192只作历史对照，未复用为当前结果；本D新attempt/store中形成一个完整合格F实例。
4. 正式Feature曾实际运行，当前已退出0。成功包装PID `{B['production']['feature_python_pid']}`、原生ts PID `{B['actual_loading']['native_pid']}`。实际/proc/exe哈希与新构建一致；真实kernel flock和独立排他探测退出73，结束后锁释放。首次尝试因新平台少store_dir.json退出，无F结果，原日志及修复在PRODUCTION_ATTEMPT01_FAILURE/attempts/attempt01；第二次成功。补齐的是正常平台空存储覆盖配置，业务配置未变。
5. 当前结果目录：`{B['result_identity']['full_dir']}`；fields SHA-256 `{B['result_identity']['fields_sha256']}`。
6. G已执行：`{A['g_workflow_started_at']}` 至 `{A['global_profile_finished_at']}`，G1—G8可支持全量/分层剖面、finding复验、问题/案例/适配与原生Gate均已形成。
7. 当前运行/统计阻断：无。原生G后继：{G['next_action']}。新结构疑点 {len(new)} 项，场景问题 {len(qs)} 项；后继释放由原manager依CurrentReviewTarget处理。

## 当前版本、范围和独立读回

正常make_features构造基线F后只增加observation_multiple=800；其余inputs/sources/domain/result_layout/schema及SOF/Calendar/steel不变。delta=600 CalendarUTITick，2Δ=1200UTI，800Δ=480000UTI=4000开放分钟；revision尾6Δ=30分钟，handoff尾18Δ=90分钟，method.revision仍1。PNV未修改。当前源码827文件、实际构建二进制、Python构造/模块及原生进程已绑定。

请求范围固定rb/hc/i、5m、2021-01-01—2023-12-31、night_end_at_2300、TA_updto20240229_DBA。实际首末KLine `{B['data_scope']['actual_start_time']}`—`{B['data_scope']['actual_end_time']}`；每品种 {S['input_5m_positions']} 个位置，三品种共 {S['input_symbol_rows']} 行，共享Calendar轴不乘3。每品种69个原始非有限close仍保留。独立OnlyRead PID `{B['readback_validation']['reader_pid']}` 与生产PID不同，31表全部与生产后读表hash、行数和列相同；另12个准确上游实例15表只读导出。当前对be57和ac基线上游15表均逐字相同，代码/行为比较基于同一输入。原生落盘文件及完整公开CSV清单已保存。

## 业务链、计数与全量剖面

KLine/Calendar → Rct实际位置 → 两轮ScaleTurn资格/已知时间 → 材料与四项pair → 候选Life/Revision → 正式publication及exact形成参与。原始分母按Rct可识别实际位置去重，不等于所有市场潜在转折；ScaleTurn按symbol/round/confirm定位，含3个初始化锚点，非初始化另报。成员关系行和Required行是观点内关系，不能当作上游位置或候选组数；publication事件亦不等于Revision occurrence。

{by_symbol}

品种层的候选包含关系会跨层重叠，ALL_DISTINCT为全局去重。本次 {S['candidate_lives']} Life、{S['candidate_revision_occurrences']} Revision occurrence、{S['publication_events']} publication事件；用了 {S['used_distinct_scale_positions']}/{S['upstream_scale_positions']} 个不同尺度位置。actual/几何confirm/selected知识分别保留，延迟分位数见profile/latency_by_symbol.csv。

{by_year}

{by_session}

状态占用以相邻已发表观点在知识轴的持有区间计算，按5m真实Calendar位置拆分分层，非内部逐Tick Dynamic trace。相邻Revision转换数=Revision-Life；生命周期是有限形成/修订责任，右删失单列。本次峰值责任内Life {S['peak_responsibility_active_lives']}，样本末右删失 {S['right_censored_lives']}。具体状态/分支/reason/同拍顺序、引用和SYMBOL/YEAR/MONTH/SESSION/OPENING/DIRECTION分布均见GlobalBehaviorProfile及profile CSV。

独立近actual跨品种pair筛查 {S['near_actual_pair_screen_count']} 条，800期限内positive {S['positive_near_joint_eligible_800']} 条；合格非否决pair未进任一候选筛查 {S['potential_eligible_pairs_unseen']} 条。首次阻断按实际已参加与明确参考规则分桶，非native未暴露计数。{S['candidate_births_after_legacy_6']}/{S['candidate_lives']} Life首次准入晚于旧6Δ期限，这是同输入的期限参考，没有运行新的K6实例，不能单凭此证明800合理。

## 原finding与全量副作用复验

GF001=`{fd['F800-GF-001']['status']}`：原22位置及8个冷启动控制在新完整实例上通过原生Life/AsOf复验，全量连续有效输入误标不完整为 {S['coverage_conflict_occurrences']}。

GF002=`{fd['F800-GF-002']['status']}`：原8观点按自然Life/known逐一对齐并通过原生AsOf复验；每个观点的三品种801行窗均保留69个原始非有限close，新flag均为1。完整新Revision总体中缺价窗内误标完整为 {next(c['repeat_count'] for c in checks if c['check_id']=='complete_flag_with_input_price_gap')}，所有当前缺价影响窗观点详见MISSING_INPUT_WINDOW_VALIDATION。根因与FrozenExpectation沿已发布D006，FI沿D007，本G不重新诊断或改写原预期。

两项finding共38个历史位置的独立原生读取均通过。{len(checks)}项全量结构检查中，新待处理非零检查 {len(new)} 项；所有previous/candidate/admission/member/alternative/bridge/子表父键和2Δ检查保留全量计数与空反例文件。

对最近be57：旧/新Life {C['old_lives']}/{C['new_lives']}，自然匹配 {C['matched_lives']}，仅旧/仅新 {C['old_only_lives']}/{C['new_only_lives']}；旧/新Revision {C['old_exact_count']}/{C['new_exact_count']}。共同自然对象中UUID改变 {C['matched_lives_with_changed_uuid']}，跨版相同原始Revision UUID {C['common_raw_revision_uuids']}；UUID无跨运行稳定相等合同。已比较全部31表、全部共同自然Life×两版publication UTI并集 {C['native_asof_comparisons']} 点，状态不同 {C['native_asof_difference_points']} 点，字段分布 {json.dumps(C['changed_fields'],ensure_ascii=False)}，发行次数不同的Life/UTI {C['publication_count_changed_life_uti_points']} 点。完整发行/差异和各版原生引用链分别保留，未用随机UUID相等判断业务等同。另对最初ac基线的全量同口径比较见InitialVersionComparison/comparison_ac，保护GF001历史闭环。

## 限制与原Workflow后继

四项原场景问题继续开放：i低参与及同步含义、时期/Session密度差异、800长责任及重叠意义、初始化锚点/稀有分支。当前候选索引使用新结果身份和时间位置，只是候选材料，未替代正式图上选场景。公开结果未暴露内部全部试探、逐Tick材料计数器或native每Turn首次阻断，不将参考筛查冒充正式轨迹。零分支不自动判不可达；统计Gate不等于全面业务合理性或Feature释放。

Q共享正常KLine适配的影响及Q独立数值边界限制继续传递，未运行/验证/释放Q或V；WALL M001没有变更。原manager按原L1核释放条件与依赖；如需场景解释，沿原Workflow进入观察材料和Skill1/2；本D未签新委派或放行下游。

准确D008、MP002 Owner原文、63个输入exact对象与远端I/D/批准一致性见SOURCE_REF_AUDIT、REMOTE_DISPATCH_READBACK和METHOD_LOCK。专业结果先发布，后续原V2 PRO_RETURN仅表示D008当前X/G职责REPORTED_COMPLETE，不表示manager已消费或业务Run已释放。
"""
(ROOT/'EXECUTOR_REPORT.md').write_text(report)
print('Report generated from current native data')
