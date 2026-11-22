"""有界S1候选浏览辅助；指标只排序浏览，不构成业务真值或G统计。"""
from common import *
from collections import defaultdict

mapping, all_data = formal_all()
data = {k: v['data'] for k, v in all_data.items()}
price_ids = dict(rb='p1040', hc='p1168', i='p1296')
turn_ids = dict(rb='p1098', hc='p1226', i='p1354')
prices = {s: data[k] for s, k in price_ids.items()}
turns = {s: [json.loads(raw) for raw in data[k]['raw']] for s, k in turn_ids.items()}
groups = [json.loads(raw) for raw in data['p1531']['raw']]
member_keys = set()
summary = []
for i, raw in enumerate(groups):
    g = raw['group']
    ms = raw['children']['occurrences_groupMembers']
    members = []
    for m in ms:
        key = m['memberObject'] + '/' + '/'.join(m['memberTurn_referenceLife_idText'].split('/')[-2:])
        member_keys.add(key)
        members.append(dict(turn_id=key, symbol=m['memberObject'], actual=m['memberActual'],
            known=m['memberKnownFrom'], confirmation=m['memberConfirmation'],price=m['memberPrice'],
            direction=m['memberDirection_name'],type=m['memberType_name'],status=m['memberStatus_name']))
    summary.append(dict(index=i,life=data['p1531']['life'][i],revision=data['p1531']['revision'][i],
        timestamp=g['timestamp'],known=g['groupKnownFrom'],anchor=g['__uti_groupAnchor'],
        deadline=g['__uti_groupDeadline'],revision_end=g['__uti_groupRevisionEnd'],
        basis=g['groupLocalBasis_name'],observation=g['groupObservation_name'],coverage=g['groupCoverageIncomplete'],
        members=members,parent=data['p1531']['parent'][i]))
save('exploration/group_index.json',summary)
save('exploration/selected_turn_index.json',{s:[{k:v for k,v in t.items() if k!='__original_json'} for t in ts] for s,ts in turns.items()})

# 首先只读原始close找局部峰谷，完全不访问F成员或输出决定选址。
# ±12根是浏览排序视窗（约60开放分钟），不是F尺度或新参数。
raw_candidates=[]
for s,p in prices.items():
    close=p['close']
    for j in range(12,len(close)-12):
        c=close[j]
        if isinstance(c,dict): continue
        before=close[j-12:j]; after=close[j+1:j+13]
        if any(isinstance(v,dict) for v in before+after):continue
        peak=c>max(before) and c>=max(after)
        trough=c<min(before) and c<=min(after)
        if not (peak or trough):continue
        if peak: strength=min(c-min(before),c-min(after))/abs(c)
        else: strength=min(max(before)-c,max(after)-c)/abs(c)
        raw_candidates.append(dict(symbol=s,row=j,plot_x=p['x'][j],timestamp=p['ts'][j],price=c,
            type='peak' if peak else 'trough',browse_strength=strength))

by_time=defaultdict(list)
for q in raw_candidates:
    by_time[(q['plot_x'],q['type'])].append(q)
raw_pairs=[]
for q in raw_candidates:
    for offset in (0,600,1200):
        for other in by_time.get((q['plot_x']+offset,q['type']),[]):
            if q['symbol']>=other['symbol']:continue
            raw_pairs.append(dict(origin='RAW_MARKET_INDEPENDENT',left=q,right=other,
                plot_gap=offset,browse_strength=min(q['browse_strength'],other['browse_strength'])))
# 每年选择原始过程最清楚的几个浏览点；数量仅控制本次阅读规模，无抽样真值含义。
raw_pairs.sort(key=lambda x:-x['browse_strength'])
independent=[]; used=[]; per_year=defaultdict(int)
for q in raw_pairs:
    year=q['left']['timestamp'][:4]; t=q['left']['plot_x']
    if per_year[year]>=3 or any(abs(t-u)<480000 for u in used):continue
    independent.append(q); used.append(t); per_year[year]+=1
# 到此候选位置已由原始市场独立选定，此后才查看上游/主输出所在位置。
for q in independent:
    for side in ('left','right'):
        t=q[side];s=t['symbol']
        nearest=min(turns[s],key=lambda z:abs(z['actual']-t['plot_x']))
        t['nearest_selected']={k:nearest[k] for k in ('turn_id','actual','actual_ts','known','known_ts','price')}
        t['same_time_selected_ids']=[z['turn_id'] for z in turns[s] if z['actual_ts'][:16]==t['timestamp']]
        t['plot_distance_to_nearest_selected']=nearest['actual']-t['plot_x']
        t['selected_ever_member']=nearest['turn_id'] in member_keys
    q['browse_nearby_group_indices']=[g['index'] for g in summary if any(abs(m['actual']-q['left']['plot_x'])<=1500 for m in g['members'])][:20]
save('exploration/RAW_INDEPENDENT_DISCOVERY.json',dict(created_at=now(),discovery_order='先原始K线，后查selected与F，仅为S1选址',
    raw_sources={s:pro_ref('D012',f'formal_data/source_{k}.json.gz') for s,k in price_ids.items()},
    browsing_window_each_side_bars=12,unit='单品种5m K线行；不是Feature参数',candidates=independent,
    coordinate_note='K线x为显示中点，x_l/x_r为图元宽度边；不当作native actual。selected匹配用公开ts/actual_ts，同分钟不冒充exact身份。',
    candidate_revision='冻结前纠正初稿actual/selected_gap名称为plot_x/plot_distance，并增加同时间selected查询；没有改变原始选址、原输入或正式材料。',
    limits='只以明确局部峰谷排序浏览；不是全部原始转折/合格候选枚举，不得由筛查直接判漏报。'))
targets={'8f776a81-a7bc-4c93-965b-0f1534b574c4','32457584-509d-4e7f-a0ea-6f8ac067c66e','6dd1661e-678e-48a8-809f-68243658b3b0','c572e7eb-8331-4437-8376-9e717fad101b','caee906a-9759-466f-bf4a-805293f3da5d'}
print('INDEX_TARGETS')
for g in summary:
    if g['life'] in targets: print(json.dumps(g,ensure_ascii=False))
print('RAW_INDEPENDENT')
for q in independent:print(json.dumps(q,ensure_ascii=False))
print('BOUNDARIES')
seen=set()
for g in summary:
    span=max(m['actual'] for m in g['members'])-min(m['actual'] for m in g['members'])
    if span==1200 and len(g['members'])==2 and g['life'] not in seen:
        print(json.dumps(g,ensure_ascii=False));seen.add(g['life'])
    if len(seen)>=3:break
print('UNPARTICIPATING_I_FIRST')
print(json.dumps([{k:t[k] for k in ('turn_id','actual','actual_ts','confirmation_ts','known_ts','price')} for t in turns['i'] if t['turn_id'] not in member_keys][:4],ensure_ascii=False))
