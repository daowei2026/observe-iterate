"""在有效D008结果上补充公开并发口径和业务关系检查；不做责任逻辑定位。"""
from common import *
from collections import Counter,defaultdict
from bisect import bisect_left,bisect_right
from decimal import Decimal
import csv,uuid

def rows(path):
    with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def integer(s):return int(Decimal(s))
def uid(row,prefix):
    if integer(row[prefix+'idForm'])==1:
        return str(uuid.UUID(int=(int(row[prefix+'idHigh'])<<64)|int(row[prefix+'idLow'])))
    return row[prefix+'idText']
def parent(row):return tuple([row['timestamp']]+[integer(row[x]) for x in ['occurrence','record_id','child_id_2']])
def write_csv(name,values,fields=None):
    values=list(values);p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True)
    fields=fields or list(dict.fromkeys(k for v in values for k in v)) or ['empty']
    with p.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(values)

assert (ROOT/'IncrementalStatisticDefinitions.json').exists()
T=D008/'readback/tables'
main=rows(T/'occurrences.csv');members=rows(T/'occurrences_groupMembers.csv')
by_members=defaultdict(list)
for m in members:by_members[parent(m)].append(m)
by_life=defaultdict(list);by_parent={};exact=[]
for r in main:
    p=parent(r);life=uid(r,'groupReference_referenceLife_');rev=uid(r,'groupReference_referenceRevision_')
    group=dict(row=r,parent=list(p),life=life,revision=rev,known=integer(r['groupKnownFrom']),
        member_identity=tuple(sorted((m['memberObject'],uid(m,'memberTurn_referenceLife_')) for m in by_members[p])))
    by_life[life].append(group);by_parent[p]=group;exact.append(group)
for gs in by_life.values():gs.sort(key=lambda g:(g['known'],tuple(g['parent'])))
assert len(main)==1538 and len(by_life)==480
births=rows(D008/'profile/candidate_births.csv');revisions=rows(D008/'profile/candidate_revisions.csv')
assert {r['life'] for r in births}==set(by_life)
assert {(r['life'],r['revision']) for r in revisions}=={(g['life'],g['revision']) for g in exact}
extraction=json.loads((D008/'UPSTREAM_EXTRACTION.json').read_text())
meta=next(x for x in extraction['features'] if x['symbol']=='rb' and x['kind']=='kline')['tables'][0]
raw_axis=Path(meta['path']).read_bytes();assert sha(raw_axis)==meta['sha256']
assert (D008/'UPSTREAM_EXTRACTION.json').read_bytes()==git_bytes(U,PREFIX+'/professional/D008/UPSTREAM_EXTRACTION.json')
klines=rows(Path(meta['path']));axis=[integer(r['closeUti']) for r in klines];times=[r['timestamp'] for r in klines]
assert len(axis)==49683 and all(x<y for x,y in zip(axis,axis[1:]))
save('CALENDAR_SOURCE_READBACK.json',dict(source_ref=pro_ref('UPSTREAM_EXTRACTION.json'),
    receipt_location='features[symbol=rb,kind=kline].tables[name=kline]',local_artifact_path=meta['path'],
    full_csv_published=False,local_artifact_hash_matches_exact_published_receipt=True,sha256=sha(raw_axis),rows=len(axis),
    first_time=times[0],last_time=times[-1],first_uti=axis[0],last_uti=axis[-1],
    uti_step_distribution=dict(Counter(y-x for x,y in zip(axis,axis[1:]))),
    purpose='只取共享Calendar轴作采样并发分母，缺价行仍保留时间；不重新做覆盖修复复验。'))
metrics=['d008_responsibility_inclusive','post_boundary_duty_projection','latest_public_duty_open',
         'latest_public_Open_duty_open','latest_public_Subsumed_duty_open','latest_public_closed_observation_duty_open',
         'historical_issued_lives']
diff={name:[0]*(len(axis)+1) for name in metrics}
def add(name,left,right,value=1):
    if left<right:diff[name][left]+=value;diff[name][right]-=value
for life,gs in by_life.items():
    g=gs[0];first=g['known'];r=integer(g['row']['groupRevisionEnd'])
    a=bisect_left(axis,first);end_in=bisect_right(axis,min(r,axis[-1]));end_ex=bisect_left(axis,r)
    add('d008_responsibility_inclusive',a,end_in)
    add('post_boundary_duty_projection',a,end_ex)
    add('historical_issued_lives',a,len(axis))
    for j,v in enumerate(gs):
        stop=gs[j+1]['known'] if j+1<len(gs) else axis[-1]+1
        left=bisect_left(axis,v['known']);right=bisect_left(axis,stop)
        v['interval']=(left,right)
parts={parent(r):r for r in rows(T/'occurrences_groupFormationParticipation.csv')}
for gs in by_life.values():
    for g in gs:
        p=parts[tuple(g['parent'])];left,right=g['interval']
        if integer(p['participationDutyClosed'])==0:
            add('latest_public_duty_open',left,right)
            state=g['row']['groupObservation_name']
            if state=='Open':add('latest_public_Open_duty_open',left,right)
            if state=='Subsumed':add('latest_public_Subsumed_duty_open',left,right)
            if integer(g['row']['groupClosed']):add('latest_public_closed_observation_duty_open',left,right)
series={}
for name,d in diff.items():
    cur=0;out=[]
    for x in d[:-1]:cur+=x;out.append(cur)
    assert min(out)>=0;series[name]=out
assert max(series['d008_responsibility_inclusive'])==36
def session(t):
    hh=int(t[11:13]);return 'DAY_CLOCK_09_15' if 9<=hh<=15 else 'NIGHT_CLOCK_21_23' if 21<=hh<=23 else 'OTHER_CLOCK'
def distribution(values):
    s=sorted(values);n=len(s)
    return dict(n=n,minimum=s[0],maximum=s[-1],mean=sum(s)/n,
        median=(s[(n-1)//2]+s[n//2])/2,frequency={str(k):v for k,v in sorted(Counter(values).items())})
strata={'ALL':list(range(len(axis)))}
for y in ['2021','2022','2023']:strata['YEAR:'+y]=[j for j,t in enumerate(times) if t.startswith(y)]
for s in ['DAY_CLOCK_09_15','NIGHT_CLOCK_21_23']:strata['SESSION:'+s]=[j for j,t in enumerate(times) if session(t)==s]
dist=[dict(statistic_id='D015-ST01',stratum_id=layer,metric=name,distribution=distribution([s[j] for j in js]),
    sample_size=len(js),denominator_value=len(js),source_location='incremental/concurrency_segments.csv',
    notes='按原生Calendar输入位置采样，不是逐tick内部active；历史累计与责任窗口/最新公开状态分列。')
    for layer,js in strata.items() for name,s in series.items()]
max_count=max(series['d008_responsibility_inclusive']);peak_indices=[j for j,x in enumerate(series['d008_responsibility_inclusive']) if x==max_count]
runs=[]
for j in peak_indices:
    if not runs or j!=runs[-1][-1]+1:runs.append([j])
    else:runs[-1].append(j)
peak_runs=[dict(start_index=r[0],last_index=r[-1],start_time=times[r[0]],last_sample_time=times[r[-1]],
    next_sample_time=times[r[-1]+1] if r[-1]+1<len(times) else None,
    start_uti=axis[r[0]],last_sample_uti=axis[r[-1]],sample_positions=len(r),
    sampled_open_minutes=len(r)*5,count=max_count) for r in runs]
first_peak=peak_indices[0];u=axis[first_peak]
def asof(gs,uti):
    i=bisect_right([g['known'] for g in gs],uti)-1
    return gs[i] if i>=0 else None
at_peak=[]
for life,gs in by_life.items():
    if gs[0]['known']<=u<=integer(gs[0]['row']['groupRevisionEnd']):
        g=asof(gs,u);at_peak.append(g)
agg=dict(life_count=len(at_peak),distinct_actual_anchors=len({g['row']['groupAnchor'] for g in at_peak}),
    member_symbol_set_counts=dict(Counter('+'.join(sorted({s for s,t in g['member_identity']})) for g in at_peak)),
    member_count_counts=dict(Counter(len(g['member_identity']) for g in at_peak)),
    observation_counts=dict(Counter(g['row']['groupObservation_name'] for g in at_peak)),
    local_basis_counts=dict(Counter(g['row']['groupLocalBasis_name'] for g in at_peak)),
    public_duty_closed_counts=dict(Counter(parts[tuple(g['parent'])]['participationDutyClosed'] for g in at_peak)),
    original_actual_age_minutes=dict(minimum=min((u-integer(g['row']['groupOriginalAnchor']))/120 for g in at_peak),
        maximum=max((u-integer(g['row']['groupOriginalAnchor']))/120 for g in at_peak)))
representatives=[]
for g in [min(at_peak,key=lambda x:by_life[x['life']][0]['known']),max(at_peak,key=lambda x:by_life[x['life']][0]['known'])]:
    representatives.append(dict(life=g['life'],revision=g['revision'],full_parent=g['parent'],
        source_ref=pro_ref('readback/tables/occurrences.csv'),selection_reason='首次峰值的最早/最晚准入代表，仅供D定位入口，不替代D全36Life对账。'))
segments=[];start=0;prior=tuple(series[name][0] for name in metrics)
for j in range(1,len(axis)+1):
    current=tuple(series[name][j] for name in metrics) if j<len(axis) else None
    if current!=prior:
        segments.append(dict(start_index=start,end_index_exclusive=j,start_time=times[start],last_sample_time=times[j-1],
            start_uti=axis[start],last_sample_uti=axis[j-1],sample_positions=j-start,**dict(zip(metrics,prior))))
        start=j;prior=current
write_csv('incremental/concurrency_segments.csv',segments)
save('ConcurrencyProfile.json',dict(statistic_id='D015-ST01',run_binding=pro_ref('FeatureRunResultBinding.json'),
    old_report_field='profile/SUMMARY.json:peak_responsibility_active_lives',
    precise_interpretation='D008闭区间责任内Life采样峰值；该历史字段名含active，但不据名称升级为native active或当前有用组。',
    native_internal_active='NOT_EXPOSED',data_scope='全部49683个输入Calendar位置，缺价行保留时间分母',
    definitions_ref='IncrementalStatisticDefinitions.json#D015-ST01',distributions=dist,
    peak_count=max_count,peak_sample_positions=len(peak_indices),peak_runs=peak_runs,
    first_peak_time=times[first_peak],first_peak_uti=u,first_peak_public_aggregate=agg,
    first_peak_other_metrics={name:values[first_peak] for name,values in series.items()},
    final_sample_other_metrics={name:values[-1] for name,values in series.items()},
    representative_locations=representatives,
    not_a_diagnosis='本G只固定统计观察和公开投影分母；D须另取全部36Life逐项核实身份/责任意义和最早责任逻辑。未以36定缺陷或给数量上限。'))

# 本轮补充身份和关系语义；旧G的27项结构事实直接复用，不重复执行其脚本。
member_changes=[];natural=defaultdict(list);same_member=defaultdict(list)
for life,gs in by_life.items():
    first=gs[0];signature=first['member_identity']
    changed=[g for g in gs if g['member_identity']!=signature]
    if changed:member_changes.append(dict(life=life,revisions=[g['revision'] for g in changed]))
    question=tuple(integer(first['row'][f]) for f in ['groupOriginalAnchor','groupOriginalDeadline','groupOriginalRevisionEnd'])
    natural[(signature,question)].append(life);same_member[signature].append(life)
duplicate_natural=[dict(lifes=ls,member_identity=list(k[0]),original_question=list(k[1])) for k,ls in natural.items() if len(ls)>1]
shared_members_different_question=[dict(lifes=ls,member_identity=list(k)) for k,ls in same_member.items() if len(ls)>1]
relation_checks=[];violations=[]
for tab,kind in [('occurrences_groupCoveredBy','COVERED_BY'),('occurrences_groupOverlaps','OVERLAPS')]:
    source=rows(T/(tab+'.csv'));bad=[]
    for row in source:
        g=by_parent[parent(row)];target_life=uid(row,'');target=asof(by_life.get(target_life,[]),g['known'])
        detail=dict(kind=kind,source_life=g['life'],source_revision=g['revision'],target_life=target_life,
            full_parent=g['parent'],source_table=tab,source_relation_child_id=integer(row['child_id_3']))
        if target is None:detail['conflict']='没有当时已发行目标观点';bad.append(detail);continue
        sm=set(g['member_identity']);tm=set(target['member_identity'])
        if kind=='COVERED_BY':
            fields=['groupAnchor','groupDeadline','groupRevisionEnd']
            if not sm<tm or target['row']['groupLocalBasis_name']!='Supported' or any(integer(g['row'][f])!=integer(target['row'][f]) for f in fields):
                detail['conflict']='公开目标不满足严格成员超集/支持/同当前问题资格';bad.append(detail)
        elif not sm.intersection(tm):
            detail['conflict']='公开重叠两端无共享具体Turn';bad.append(detail)
    relation_checks.append(dict(check_id=kind.lower()+'_business_relation',denominator=len(source),repeat_count=len(bad),
        sample_size=len(source),source_ref=pro_ref('readback/tables/'+tab+'.csv'),examples=bad[:3]))
    violations+=bad
checks=[dict(check_id='same_life_member_identity_stability',denominator=len(by_life),repeat_count=len(member_changes),examples=member_changes[:3]),
    dict(check_id='duplicate_natural_candidate_identity',denominator=len(by_life),repeat_count=len(duplicate_natural),examples=duplicate_natural[:3])]+relation_checks
save('IncrementalSemanticChecks.json',dict(statistic_ids=['D015-ST02','D015-ST03'],checks=checks,
    member_identity_changes=member_changes,duplicate_natural_identities=duplicate_natural,
    same_members_different_questions=shared_members_different_question,relation_violations=violations,
    inherited_checks_ref=pro_ref('profile/STRUCTURAL_CHECKS.json'),inherited_check_count=27,
    scope='当前准确实例公开观点内身份/关系语义检查；不使用内部变量，不定位责任代码或推断根因。'))
new_strata=Counter(('+'.join(sorted({s for s,t in gs[0]['member_identity']})),gs[0]['row']['timestamp'][:4],
    '+'.join(sorted({m['memberDirection_name'] for m in by_members[tuple(gs[0]['parent'])]}))) for gs in by_life.values())
save('MemberCombinationStrata.json',dict(statistic_id='D015-ST02',rows=[dict(member_symbols=k[0],knowledge_year=k[1],
    direction=k[2],life_count=v) for k,v in sorted(new_strata.items())],denominator=len(by_life),
    count_unit='首次发行的准确Life，组合层不重复；品种包含层见旧G，不相加当全局总数。'))
save('ANALYSIS_EXECUTION.json',dict(completed=True,completed_at=now(),
    reused_D008_G=True,new_native_or_OnlyRead_run=False,source_feature_modified=False,
    native_active_reconstructed=False,root_cause_localized=False,
    increment_only=['D015-ST01','D015-ST02','D015-ST03'],old_G_definitions_reused_as='D015-ST04',
    public_view_count=len(main),life_count=len(by_life),calendar_positions=len(axis),
    semantic_conflicts=sum(c['repeat_count'] for c in checks)))
print(json.dumps(dict(peak_count=max_count,peak_sample_positions=len(peak_indices),peak_runs=peak_runs,
    first_peak_public_aggregate=agg,first_peak_other_metrics={name:values[first_peak] for name,values in series.items()},
    semantic_checks=checks,same_members_different_questions=len(shared_members_different_question)),ensure_ascii=False))
