"""只接收与全部正式输出严格等价的诊断运行结果，补真实资格分母及far-End检查。"""
import json
from pathlib import Path
import pandas as pd

OUT=Path(__file__).resolve().parent;ROOT=OUT/'profile';AUX=OUT/'rb-upstream-checkpoint-replay'
aux=json.loads((AUX/'diagnostic-result.json').read_text())
assert aux['status']=='VERIFIED_DIAGNOSTIC_RESULT' and aux['all_formal_trace_and_event_values_exact']
assert aux['trace_rows_equal']==9959400 and aux['sparse_event_rows_equal']==335081
profile=json.loads((ROOT/'GlobalBehaviorProfile.json').read_text())
binding=json.loads((ROOT/'FeatureRunResultBinding.json').read_text())
readiness=json.loads((ROOT/'StatisticsInputReadiness.json').read_text())
spec=json.loads((OUT/'statistics-specification.json').read_text())
definition=dict(statistic_id='AUX-QUAL-01',name='实际物化诊断载体的上游资格与Wall新建转化',
    business_item_ref='输入观测/ID-C1/BO-C1',count_unit='每侧观测资格数；新建身份另外计',
    object_group_key='同一来源namespace、symbol、uti、side；Wall身份另按wall_id',time_basis='原生timestamp/uti',
    denominator='原始侧别观测、QT正值观测、F1命中、F6命中分别给出；每项转化用相应上游分母',
    deduplication_rule='每侧每输入拍一次；新Start须匹配F6资格，诊断产物不与正式事件重复相加',
    same_tick_rule='side独立；仅new_start标记对应同拍正式Start',strata=['symbol','side','month','clock_bin'],
    source_fields=['qualification-observations.parquet::{finite_quote,positive_qt,large_quote,thin,wall_brick,new_start}_{bid,ask}'])
spec['statistics_definitions'].append(definition)
spec['statistics_definitions'].append(dict(statistic_id='AUX-D4-01',name='全部far End occurrence的原生checkpoint检查',business_item_ref='ID-D4/OC-C4',
    count_unit='far End occurrence',object_group_key='source namespace + symbol + side + wall_id',time_basis='checkpoint uti/ts',
    denominator='对应侧所有far_price End occurrence',deduplication_rule='每个原生Core End一次；与正式sparse逐行等价',
    same_tick_rule='保持原生occurrence顺序；不是完整逐拍far历史',strata=['symbol','side'],
    source_fields=['event-checkpoints.parquet::{support_flag,far_run_len,end_reason,side}']))
profile['statistics_definitions']=spec['statistics_definitions']
binding['auxiliary_result_bindings']=[dict(auxiliary_id='D002-RB-QUAL-CHECKPOINT-01',mode=aux['mode'],
    code_version=binding['code_version'],parameter_instance_ref=binding['parameter_instance_ref'],symbol='rb',
    declared_data_scope=aux['data_scope'],calendar=aux['calendar'],artifacts=aux['artifacts'],
    all_formal_event_and_trace_values_equal=True,formal_source_or_output_changed=False,
    evidence_role='真实新增诊断运行载体；原WALL最终表未暴露资格/完整far轨迹的事实保留。')]
profile['run_binding']=binding
profile['limits']=[item for item in profile['limits'] if not item.startswith('F1/F6 转化及')]
profile['limits'].append('F1/F6及事件checkpoint统计来自单独物化的、与正式rb输出全量等价的未修改组件诊断运行；完整逐拍far历史仍未暴露，m仍无结果。')
readiness['available_items'].append('D002-RB-QUAL-CHECKPOINT-01：F1/F6逐拍资格与事件checkpoint，已严格核对全部正式rb事件/trace等价。')
for item in readiness['not_exposed_items']:
    if item['statistic_id']=='CANDIDATE-CONVERSION':
        item.update(supplement_status='AVAILABLE_IN_VERIFIED_DIAGNOSTIC_CARRIER_ONLY',handling='原WALL最终表仍不暴露；本轮资格计数使用已物化且严格等价的诊断运行结果。')
    else:item.update(supplement_status='AVAILABLE_AT_EVENT_CHECKPOINTS_NOT_FULL_TICK_FAR_HISTORY',handling='可核全部far End的support/计数；不冒称完整逐拍far历史已暴露。')
observations=pd.read_parquet(AUX/'qualification-observations.parquet')
assert len(observations)==aux['trace_rows_equal']
month=observations.index.month
day=(observations.index.hour>=6)&(observations.index.hour<18)
def measured(frame,side):
    result=dict(raw_observations=len(frame))
    for source,target in [('finite_quote','finite_quote_observations'),('positive_qt','positive_qt_observations'),
                          ('large_quote','large_quote_observations'),('wall_brick','wall_brick_observations'),('new_start','start_occurrences')]:
        result[target]=int(frame[source+'_'+side].sum())
    result['large_but_thin_observations']=int((frame['large_quote_'+side].ne(0)&frame['thin_'+side].ne(0)).sum())
    result['candidate_without_new_start']=int((frame['wall_brick_'+side].ne(0)&frame['new_start_'+side].eq(0)).sum())
    for name,numerator,denominator in [('F1_per_positive_QT','large_quote_observations','positive_qt_observations'),
        ('F6_per_F1','wall_brick_observations','large_quote_observations'),('new_Wall_per_F6','start_occurrences','wall_brick_observations')]:
        result[name]=dict(numerator=result[numerator],denominator=result[denominator],ratio=result[numerator]/result[denominator] if result[denominator] else None)
    return result
def row(stratum,value):
    return dict(statistic_id='AUX-QUAL-01',stratum_id=stratum,value_or_distribution=value,sample_size=value['raw_observations'],
        denominator_value=value['raw_observations'],source_location=str(AUX/'qualification-observations.parquet'),
        notes='真实诊断载体。各转化率在value内分别列相应分母；计数单位不混用，未改变正式范围或原WALL表合同。')
for side in ['bid','ask']:
    total=measured(observations,side)
    for key,value in aux['qualification_counts'][side].items():assert total[key]==value,(side,key)
    profile['candidate_profile'].append(row('rb/'+side,total))
    summed=0
    for value in sorted(month.unique()):
        part=measured(observations.loc[month==value],side);summed+=part['raw_observations']
        profile['cross_period_profile'].append(row('rb/'+side+'/2021-'+str(value).zfill(2),part))
    assert summed==len(observations)
    for label,mask in [('DAY_CLOCK_BIN',day),('OTHER_CLOCK_BIN',~day)]:
        profile['cross_session_profile'].append(row('rb/'+side+'/'+label,measured(observations.loc[mask],side)))
    d4=aux['d4_far_end_review'][side]
    assert d4['far_end_with_support']==0 and d4['far_end_counter_below_hold']==0
    profile['same_tick_order_profile'].append(dict(statistic_id='AUX-D4-01',stratum_id='rb/'+side,
        value_or_distribution=d4,sample_size=d4['far_end_occurrences'],denominator_value=d4['far_end_occurrences'],
        source_location=str(AUX/'event-checkpoints.parquet'),notes='原生未修改Core返回的全部far End checkpoint；未声称每拍far计数历史。'))
for item in profile['known_finding_reviews']:
    if item['finding_id']=='D4':item.update(status='VERIFIED_RB_FAR_END_OCCURRENCE_SCOPE',
        far_end_occurrence_review=aux['d4_far_end_review'],verified_far_end_occurrences=sum(x['far_end_occurrences'] for x in aux['d4_far_end_review'].values()),
        full_per_tick_support_far_regression='NOT_EXPOSED',full_requested_scope='INCOMPLETE_M')
checks=json.loads((ROOT/'STATISTICS_SELF_CHECK.json').read_text())
checks['diagnostic_result_parity']=dict(trace_rows=aux['trace_rows_equal'],event_rows=aux['sparse_event_rows_equal'],all_values_equal=True,
    F1_F6_Start_counts_conserved=True,far_end_checkpoint_matches_formal_end_count=True)
for name,value in [('FeatureRunResultBinding.json',binding),('GlobalBehaviorProfile.json',profile),('StatisticsInputReadiness.json',readiness),
                   ('STATISTICS_SELF_CHECK.json',checks)]:
    (ROOT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
(OUT/'statistics-specification.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
print('资格分母及分层、全部far End checkpoint已从真实等价诊断结果补齐；整体m阻断保留。',flush=True)
