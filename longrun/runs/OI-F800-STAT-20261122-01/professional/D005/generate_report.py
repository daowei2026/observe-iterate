"""只用已验收的本次实测写原manager专业报告。"""
from pathlib import Path
from datetime import datetime, timezone
import json
import csv
ROOT=Path(__file__).resolve().parent
def load(n):return json.loads((ROOT/n).read_text())
def rows(n):
    with (ROOT/n).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def table(data,cols):
    return '\n'.join(['| '+' | '.join(t for _,t in cols)+' |','| '+' | '.join('---' for _ in cols)+' |']+
        ['| '+' | '.join(str(r[k]) for k,_ in cols)+' |' for r in data])
assert load('VALIDATION.json')['completed']
B=load('FeatureRunResultBinding.json');S=load('profile/SUMMARY.json');C=load('VersionComparison.json');G=load('GlobalProfileGate.json');P=load('PRODUCTION_PROCESS.json');F=load('FindingDisposition.json');A=load('NATIVE_RETEST_API.json')
counttable=table(rows('profile/counts_by_symbol.csv'),[('symbol','品种/去重全局'),('raw_turn_positions','原始实际位置'),('scale_turn_positions','尺度位置'),('used_scale_turn_positions','参加F位置'),('candidate_lives','候选Life'),('candidate_revision_occurrences','Revision发生')])
yeartable=table([r for r in rows('profile/counts_by_symbol_year.csv') if r['symbol']=='ALL_DISTINCT'],[('year','知识年'),('scale_turn_positions','尺度位置'),('candidate_lives','新Life'),('candidate_revision_occurrences','Revision发生')])
tablecmp=table(rows('comparison/all_31_tables.csv'),[('table','公开表'),('old_rows','ac旧版行'),('new_rows','be57新版行'),('row_delta','差值')])
diff=table([dict(metric=k,old=C['old_summary'][k],new=C['new_summary'][k],delta=v) for k,v in C['numeric_deltas'].items()], [('metric','量及单位（见定义）'),('old','旧'),('new','新'),('delta','新−旧')])
stats='；'.join(c['check_id']+'='+str(c['repeat_count']) for c in load('profile/STRUCTURAL_CHECKS.json') if c['repeat_count']) or '27项检查均未观察到违例'
text=f'''# D005｜be57 完整正式 F X、独立31表读回与全量G复验

本D已完成授权范围内的新版本正式X和原Skill G1–G8。`GlobalProfileGate={G['status']}`；原 `F800-GF-001` 当前状态为 `{F['status']}`。本次完整实测为 {S['candidate_lives']} 个候选Life、{S['candidate_revision_occurrences']} 次Revision occurrence、{S['publication_events']} 个发行事件。原22个错误flag位置与8个cold对照已由独立进程通过原生Life/AsOf读口复验，{A['passed']}/{A['total']}符合各自预期。

本轮另识别 `F800-GF-002`：8个Revision、5个Life、6个发行时刻标记完整覆盖，但观察窗内三品种各有69行OHLC缺值/零成交量。8/8在修复前同对象同知识位置也已存在；这是一项新识别的结构疑点，不宣称be57新引入回归，也未判定数据或实现根因。故最终Gate为DIAGNOSIS_REQUIRED，须由原Skill3先核缺值、Calendar豁免与覆盖承诺。原GF-001的关闭与此项未决状态分别登记。

原manager=`codex:OI-F800-STAT-20261122-01:manager`；原E1=`codex:OI-F800-STAT-20261122-01:executor:E1`；当前C0012/D005，CODEX_NATIVE_DIRECT、workers=[]。未创建线程、Worker或新委派。D005只完成本次X/G专业职责；executor完成不等于manager已消费，也不替父Run出FeatureReleaseGate或启动Q/V。

## Owner七项进度

| 项目 | 本次事实 |
|---|---|
| D001是否完成 | 已接收，未重做完整U；复用原理解并沿D004合同不变结论更新be57最小适用绑定，见CurrentFeatureUnderstandingPackage.json |
| X是否开始 | 已开始并完成完整rb/hc/i、5m、2021—2023正式F |
| 复用还是生产 | NEW_FORMAL_PRODUCTION；D002的ac结果仅历史比较，独立新store保留所有旧产物 |
| 正式Feature是否实际运行 | 是，Feature Python PID {B['production']['feature_python_pid']}，原生ts PID {P['native_pid']}；实际包装进程退出0，监督进程退出0 |
| 当前结果目录 | `{B['result_identity']['full_dir']}` |
| G是否开始 | 是，合格新X独立读回后完整执行G1–G8；可支持对象/事件/状态/责任/分层/引用及原finding全部复验 |
| 当前阻断 | 无未解决执行阻断；专业后继按原生GlobalProfileGate与下列限制处理 |

## 当前版本、实例和完整范围

- FRP `be57d6752c9d43d10f1d670e1d2993bb8153ea7c`，TIS `2f460d663d821cf2ba25555eda13e78b697d0767`。
- 完整配置SHA-256 `{B['parameter_version']}`。`observation_multiple=800`、`delta=600 CalendarUTITick`、实际贴近`2Δ=1200UTI`、`method.revision=1`；inputs/sources/domain/result_layout与已批准配置一致。
- F-only；rb/hc/i、5m、2021-01-01—2023-12-31、night_end_at_2300、TA_updto20240229_DBA、steel。实际首末KLine为{B['data_scope']['actual_start_time']}—{B['data_scope']['actual_end_time']}，没有将节假日边界缩写为较短正式请求。
- 每品种49,683个Calendar位置，三对象149,049行；各69个非有限close保留在日历分母，连续有效覆盖对照在缺价处断开。上游{C['upstream_tables']}张导出表与旧版逐字节一致，见VersionComparison和UPSTREAM_EXTRACTION；不存在用输入变化解释修复效果的问题。

实际EPM入口为 `{B['actual_loading']['engine']}`，SHA-256 `{B['actual_loading']['engine_sha256']}`；本次实际原生进程加载已记录。FRP当前源文件逐文件匹配锁定Git对象，TIS关键入口/读口/Calendar六文件复核一致，原D004构建与版本采用链保留。D005未改动正式Feature代码或参数，未重跑已完成的64项局部回归。

共享flock在{P['lock_acquired_at']}取得，独立抢锁进程退出73，内核锁及实际持锁PID可核；正式过程于{P['process_finished_at']}退出0，锁已释放。生产前无新store写者且未见其他同UID引擎。实际进程的PID/executable/命令变化持续记录，保留同PID exec证据；没有复用旧监控故障或用文件存在代替持锁。

31张表已由独立Python PID {B['readback_validation']['reader_pid']}以OnlyRead读取，表名、行数、列及CSV SHA-256与生产后的原生读取逐表一致，主`to_df`与`to_dfs()['occurrences']`相同。fields.json SHA-256 `{B['result_identity']['fields_sha256']}`；其身份同时绑定新代码/引擎/配置/范围，并非单靠fields或目录名证明代码。

## 业务单位与全量剖面

计数沿最小业务链：同参数KLine→Rct原始实际位置→两轮ScaleTurn资格→材料/四坐标关系→候选Life/Revision→正式发行与exact/形成参与。原始位置、尺度位置、Life、Revision发生、成员关系和发行事件分别计数；同Life同刻保留occurrence及完整父子坐标，按previous引用核序，不按随机UUID排序。每项单位、分母、去重、同刻规则和来源见18项StatisticDefinition。

{counttable}

品种层的组数是包含关系，会跨品种重叠；ALL_DISTINCT单独全局去重。Rct分母包含每品种初始化锚点，不能称为全部潜在市场转折。F成员行反映多次Revision中的关系，不能当作尺度分母。

{yeartable}

知识年、actual年、月、品种、方向、钟点日夜与开盘窗口均已分层；上游按selected知识轴、组按首次publication、观点按当次publication，actual另列。每层密度、责任跨度、状态/理由、观点持有和结构疑点率见profile/cross_strata_*。无可靠牛熊标签，未凭名称造环境分类。

状态占用采用已发表观点知识区间持有，并按真实5m位置分层取样；不是内部逐Tick Dynamic trace。生命周期统计的是有限观察/修订/交接责任，样本末右删失 {S['right_censored_lives']} 个Life另列。独立上游近actual候选筛查 {S['near_actual_pair_screen_count']} 条，合格非否决边未在任何候选出现的筛查数 {S['potential_eligible_pairs_unseen']}；这不是应输出真值或已确认漏报。

## 修复复验与完整版本影响

原22个误报位置按自然Life（排序上游symbol/round/confirm成员及原anchor/deadline/revisionEnd）对齐，用新原生稀疏观点的知识持有值复验；随后独立进程通过未修改的TIS GroupCandidateReadSession Life/AsOf读口按previous链重新选择观点，逐项与CSV比较结果一致。原错误位置 {C['false_flag_retest_passed']}/{C['false_flag_retest_total']} 为0，cold对照 {C['cold_control_passed']}/{C['cold_control_total']} 保持1；新三年全量覆盖冲突为 {S['coverage_conflict_occurrences']}。证据在comparison/coverage_retest.csv、NATIVE_RETEST_API.json和27项全量结构检查。

当前结构检查：{stats}。检查包含成员准确上游、Required四项和actual 2Δ、固定原问题、责任不扩张、关闭不重开/责任后不更新、状态轴自洽、全部previous即时前版链、candidate/admission/成员exact及alternative桥、全部非空group子表父键。未暴露的内部变量不计作实测。原GF-001由FIXED_PENDING_RERUN转为{F['status']}的依据是本次完整X/G，不是22flag隔离方程或64项局部回归。

共同自然Life {C['matched_lives']}；旧独有 {C['old_only_lives']}、新独有 {C['new_only_lives']}；共同对象中 {C['matched_lives_with_changed_uuid']} 个Life的UUID改变。Revision原始UUID交集 {C['common_raw_revision_uuids']}。UUID无跨运行稳定相等合同，各版exact/previous/admission/alternative链按本版实际ID完整验实，不强行把随机ID相等当验收。

共同Life×两版publication UTI并集共 {C['native_asof_comparisons']} 个公开观点持有比较点，差异 {C['native_asof_difference_points']} 点，变化字段计数为 `{json.dumps(C['changed_fields'],ensure_ascii=False)}`。这里是按原生已发表观点进行的跨版对照，不是新造事件或内部逐Tick trace。发行次数不同的Life/UTI点 {C['publication_count_changed_life_uti_points']}；完整差异逐项保留在comparison/native_asof_state_differences.csv和publication_changes.csv。

{diff}

全31表原生行数影响如下；完整字节hash另见comparison/all_31_tables.csv。UUID变化会使载荷hash不同，表行减少也不自动证明业务改善。

{tablecmp}

## 原生Gate、场景队列与界限

`GlobalProfileGate={G['status']}`。理由和后继原文见GlobalProfileGate.json；新结构finding {len(load('GlobalFindingCandidates.json'))} 项，诊断适配包 {len(load('DiagnosisInputAdapters.json'))} 项。已关闭旧finding保留FindingDisposition，新GF-002具名适配包已形成，不在G提前诊断。

原四项ScenarioQuestion逐项基于新结果更新：i参与率及潜在覆盖、知识年/Session密度、800的迟到/长责任及覆盖关系、初始化与低频分支。{len(load('CandidateCaseIndex.json'))}个最小对照候选位置包含上游未参加F位置、跨年、迟到/覆盖及cold位置；理由与所需证据见CandidateCaseIndex。它们仍是场景问题，不当作新业务判错或已冻结正式场景，也不因旧finding关闭而消失。

限制保留：内部逐Tick材料/所有枚举与native首次阻断未暴露；参考K6只用于同输入期限筛查，未生产另一个正式实例，不能证明800已标定合理；缺少patch、scopeEnded、未知Clock分支适用输入不证明分支不可达。F/Q共享适配器及Q另有归一化数值边界沿D004 ContractAndDependencyImpact传递；本D未运行Q/V，不能据F通过推定下游通过。

后继由原manager按采用的control-v0.3与CurrentReviewTarget消费最新U/X/G、finding及限制，形成FeatureReleaseGate/UpstreamReleasePackage；需要真实场景解释时进入既定M/Skill1/2。没有新增正式行为变化；若后续提出新的正式修改，仍按原流程形成提案并取得Owner确认。D005不替manager签后继，不将本次G通过扩大为Feature在所有市场场景中已合理。

本报告与原生专业文件先发布，C0012 PRO_RETURN随后引用已发布exact提交。验证见VALIDATION.json、WORKFLOW_COMPLETION.json、SOURCE_REF_AUDIT.json和BASELINE_INPUT_READBACK.json。
'''
(ROOT/'EXECUTOR_REPORT.md').write_text(text)
print('EXECUTOR_REPORT.md generated from verified native evidence',len(text.encode()))
