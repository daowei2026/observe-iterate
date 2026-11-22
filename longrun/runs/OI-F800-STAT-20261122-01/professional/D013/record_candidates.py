from common import *

initial=read_json(U,f'{PREFIX}/professional/D008/CandidateCaseIndex.json')
raw=json.loads((ROOT/'exploration/RAW_INDEPENDENT_DISCOVERY.json').read_text())
groups=json.loads((ROOT/'exploration/group_index.json').read_text())
pool=[]
for x in initial:
    pool.append(dict(candidate_id='INDEX-'+x['case_candidate_id'],status='CANDIDATE',
        discovery_route='INHERITED_CANDIDATE_ONLY',original_candidate_only=True,
        original_candidate=x,source_ref=pro_ref('D008','CandidateCaseIndex.json',U),
        promotion_requires='本S1亲自读真实原价过程、字段完整性与范围后另作选择，不自动提升原索引。'))
for i,x in enumerate(raw['candidates'],1):
    left=set(x['left']['same_time_selected_ids']);right=set(x['right']['same_time_selected_ids'])
    joint=[g['index'] for g in groups if left.intersection(m['turn_id'] for m in g['members']) and right.intersection(m['turn_id'] for m in g['members'])]
    pool.append(dict(candidate_id=f'RAW-{i:02d}',status='CANDIDATE',discovery_route='RAW_MARKET_INDEPENDENT',
        raw_selection=x,public_joint_group_indices=joint,
        interpretation_limit='公开同源位置关联仅服务选址；不是独立支持份数，不由无输出推native首阻断。'))
pool.append(dict(candidate_id='BOUNDARY-IN-1200',status='CANDIDATE',discovery_route='PUBLIC_SELECTED_TIME_BOUNDARY',
    turn_ids=['rb/value1/73153799','i/value1/73148999'],actual_utis=[73127399,73128599],
    original_actual_times=['2021-02-10 09:50:00','2021-02-10 10:00:00'],
    discovery_basis='原U/Owner仍2Delta1200，寻找可区分actual与确认延迟/闭市时长的等号位置。'))
pool.append(dict(candidate_id='BOUNDARY-OUT-1800',status='CANDIDATE',discovery_route='PUBLIC_SELECTED_TIME_BOUNDARY',
    turn_ids=['hc/value1/73238399','i/value1/73232999'],actual_utis=[73233599,73231799],
    original_actual_times=['2021-02-22 09:20:00','2021-02-22 09:05:00'],
    discovery_basis='紧邻2Delta之外的实际15开放分钟峰点；不以800扩张同步含义。'))
save('CandidateCasePool.v1.json',dict(pool_id='F800-S1-D013-POOL',version=1,created_at=now(),
    state='CANDIDATE',candidate_count=len(pool),candidates=pool,
    source_policy='七条旧索引只当线索；九条原价候选先选址再查输出；边界位置另从已公开上游选中记录挑选。',
    sampling_scope='最小有区分力场景集，不设统一案例数量，不替代已有效G或声称穷尽三年原始市场真值。'))
print(json.dumps(dict(candidates=len(pool),inherited=7,independent_raw=9,boundary=2),ensure_ascii=False))
