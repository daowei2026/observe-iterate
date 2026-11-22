"""从既有21正式文件读取冻结案例的过程事实；不生产新图数据。"""
from common import *
from datetime import datetime
from collections import defaultdict
import uuid

cs=read_json(FROZEN,f'{PREFIX}/professional/D013/CaseReviewSet.json')
case_index=read_json(FROZEN,f'{PREFIX}/professional/D013/CaseMaterialIndex.json')
loc={c['case_id']:c for c in case_index['cases']}
_,formal=formal_all();data={k:v['data'] for k,v in formal.items()}
price_ids=dict(rb='p1040',hc='p1168',i='p1296');turn_ids=dict(rb='p1098',hc='p1226',i='p1354')
turns={s:[json.loads(raw) for raw in data[sid]['raw']] for s,sid in turn_ids.items()}
groups=[json.loads(raw) for raw in data['p1531']['raw']]

def key(m):return m['memberObject']+'/'+ '/'.join(m['memberTurn_referenceLife_idText'].split('/')[-2:])
def short(raw):return '/'.join(raw.split('/')[-3:])
def exact_rows(raw):
    out=[]
    for row in raw:
        entry={k:v for k,v in row.items() if not k.startswith(('groupPrevious_reference','covering_reference','coveredBy_reference'))}
        entry['original_row']=row
        out.append(entry)
    return out
def bar(d,i):
    return dict(row_index=i,**{k:d[k][i] for k in ('ts','open','high','low','close','volume')})

records=[]
for case in cs['cases']:
    cid=case['case_id'];l=loc[cid];start=datetime.fromisoformat(case['start_time']);end=datetime.fromisoformat(case['end_time'])
    raw_market=[]
    for symbol in case['symbol']:
        sid=price_ids[symbol];d=data[sid];rows=[i for i,t in enumerate(d['ts']) if start<=datetime.fromisoformat(t)<=end]
        labels={start.strftime('%Y-%m-%d %H:%M'),end.strftime('%Y-%m-%d %H:%M')}
        for t in l['independent_selected_rows']:
            if t['symbol']==symbol:
                labels.update(v[:16] for v in (t['actual_time'],t['geometric_confirmation_time'],t['selected_known_time']))
        if cid.endswith('007'):labels.add('2022-05-25 15:00')
        key_rows={rows[0],rows[-1]}
        critical=[]
        for label in sorted(labels):
            matches=[i for i in rows if d['ts'][i]==label]
            if not matches:continue
            i=matches[0];key_rows.add(i)
            context=[j for j in (i-6,i-1,i+1,i+6) if j in rows]
            key_rows.update(context)
            critical.append(dict(label=label,at=bar(d,i),nearby_bars=[bar(d,j) for j in context],
                context_unit='前后原价bar位置；±6根仅用于还原邻近价格，不是新尺度/业务判据。'))
        raw_market.append(dict(symbol=symbol,source_id=sid,source_ref=pro_ref('D012',f'formal_data/source_{sid}.json.gz'),
            row_start=rows[0],row_end=rows[-1],row_count=len(rows),
            actual_bar_rows=[bar(d,i) for i in sorted(key_rows)],critical_points=critical,
            original_price_role='OHLC/close原值，先读市场过程；不从F输出复述价格。'))
    observed=[]
    for row in l['group_rows']:
        i=row['index'];payload=groups[i];g=payload['group'];ch=payload['children']
        members=[]
        for m in ch['occurrences_groupMembers']:
            member={k:v for k,v in m.items() if k in ['memberObject','memberActual','memberPrice','memberConfirmation','memberKnownFrom',
                'memberDirection','memberDirection_name','memberType','memberType_name','memberRound','memberRound_name',
                'memberStatus','memberStatus_name','memberRetracted','memberT_pointActual','memberT_pointPrice','memberT_pointKnownFrom',
                'memberC_pointActual','memberC_pointPrice','memberC_pointKnownFrom']}
            member.update(turn_id=key(m),member_index=m['child_id_3'],
                turn_reference_life=m['memberTurn_referenceLife_idText'],turn_reference_revision=m['memberTurn_referenceRevision_idText'])
            members.append(member)
        req=[]
        for q in ch['occurrences_groupRequired']:
            req.append(dict(pair_index=q['child_id_3'],left=short(q['pairLeft_referenceLife_idText']),
                right=short(q['pairRight_referenceLife_idText']),
                verdicts={k:v for k,v in q.items() if k.endswith('_name')},
                distances=[d for d in ch['occurrences_groupRequired_pairDistance'] if d['child_id_3']==q['child_id_3']]))
        observed.append(dict(row_index=i,source_ref=pro_ref('D012','formal_data/source_p1531.json.gz'),
            life=data['p1531']['life'][i],revision=data['p1531']['revision'][i],full_parent=json.loads(data['p1531']['parent'][i]),
            group=g,members=members,required=req,
            member_P=ch['occurrences_groupMembers_memberP'],member_P_clock=ch['occurrences_groupMembers_memberP_pointClock'],
            previous=ch['occurrences_groupPrevious'],covered_by=ch['occurrences_groupCoveredBy'],overlaps=ch['occurrences_groupOverlaps'],
            participation=ch['occurrences_groupFormationParticipation'],
            all_children_keys=list(ch),
            sparse_observation_note='仅真实公开发行观点，不插值内部状态；optional空列表保持空。'))
    selected_rows=[]
    for t in l['independent_selected_rows']:
        original=turns[t['symbol']][t['row_index']]
        selected_rows.append(dict(source_id=turn_ids[t['symbol']],row_index=t['row_index'],raw=original))
    lookups=[]
    if cid.endswith('002'):
        target=selected_rows[0]['raw']
        for symbol in ('rb','hc'):
            nearest=sorted(turns[symbol],key=lambda t:abs(t['actual']-target['actual']))[:2]
            lookups.append(dict(kind='independent_selected_neighbors',symbol=symbol,target_turn=target['turn_id'],
                target_actual=target['actual'],within_1200=[t['turn_id'] for t in turns[symbol] if abs(t['actual']-target['actual'])<=1200],
                nearest=[dict(turn_id=t['turn_id'],actual=t['actual'],actual_ts=t['actual_ts'],known=t['known'],known_ts=t['known_ts'],price=t['price'],distance_ticks=abs(t['actual']-target['actual'])) for t in nearest]))
        matching=[i for i,p in enumerate(groups) if target['turn_id'] in {key(m) for m in p['children']['occurrences_groupMembers']}]
        lookups.append(dict(kind='published_group_member_lookup',target_turn=target['turn_id'],matching_group_rows=matching,
            scope='完整1538个已发行组观点；不是native未成组pair轨迹',native_first_blocker='NOT_EXPOSED'))
    if cid.endswith('005'):
        wanted={t['raw']['turn_id'] for t in selected_rows}
        both=[i for i,p in enumerate(groups) if wanted<={key(m) for m in p['children']['occurrences_groupMembers']}]
        each={t:[] for t in wanted}
        for i,p in enumerate(groups):
            keys={key(m) for m in p['children']['occurrences_groupMembers']}
            for t in wanted:
                if t in keys:each[t].append(i)
        lookups.append(dict(kind='published_exact_combination_lookup',wanted_turns=sorted(wanted),matching_group_rows=both,
            individual_member_rows=each,actual_distance=abs(selected_rows[0]['raw']['actual']-selected_rows[1]['raw']['actual']),
            native_pair_veto_or_first_blocker='NOT_EXPOSED；不从无行推实际TimeVeto。'))
    if cid.endswith('007'):
        for symbol in ('rb','i'):
            matching=[dict(row_index=i,turn_id=t['turn_id']) for i,t in enumerate(turns[symbol]) if t['actual_ts'][:16]=='2022-05-25 15:00']
            lookups.append(dict(kind='independent_selected_at_raw_peak',symbol=symbol,raw_time='2022-05-25 15:00',matching_selected=matching,
                scope='本次完整独立selected投影；不是所有潜在原始市场转折真值。'))
    record=dict(case_id=cid,case_type=case['case_type'],frozen_case_ref=pro_ref('D013','CaseReviewSet.json',FROZEN),
        case_time=dict(start=case['start_time'],end=case['end_time']),
        raw_market_readback=raw_market,independent_selected_readback=selected_rows,observed_public_group_process=observed,
        specific_public_lookups=lookups,read_at=now(),
        stage='construction_snapshot',semantic_scope='S2从已接受正式文件读取的案例过程摘录；原正式文件未重导出/复算。')
    save(f'case_readback/{cid}.json',record);records.append(record)
    print(cid)
    print('RAW_KEY_PRICES',json.dumps([dict(symbol=r['symbol'],points=[p['at'] for p in r['critical_points']]) for r in raw_market],ensure_ascii=False))
    print('PUBLIC_GROUPS',json.dumps([dict(index=o['row_index'],life=o['life'],revision=o['revision'],
        ts=o['group']['timestamp'],known=o['group']['groupKnownFrom'],basis=o['group']['groupLocalBasis_name'],
        observation=o['group']['groupObservation_name'],coverage=o['group']['groupCoverageIncomplete'],closed=o['group']['groupClosed'],
        duty=[p['participationDutyClosed'] for p in o['participation']],P_rows=len(o['member_P']),
        required=[q['verdicts'] for q in o['required']],covered_by=o['covered_by']) for o in observed],ensure_ascii=False))
    if lookups: print('LOOKUPS',json.dumps(lookups,ensure_ascii=False))
save('PROCESS_READBACK_INDEX.json',dict(case_ids=[r['case_id'] for r in records],case_files=[f"case_readback/{r['case_id']}.json" for r in records],
    completed_at=now(),frozen_cases_only=True,feature_or_graph_rebuilt=False,formal_data_reexported=False))
