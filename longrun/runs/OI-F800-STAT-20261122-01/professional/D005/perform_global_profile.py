"""G1-G8：仅消费本Run独立读回及同参数公开上游，不运行Feature或诊断根因。"""
from pathlib import Path
from collections import Counter, defaultdict
from itertools import combinations
from bisect import bisect_right
from hashlib import sha256
from datetime import datetime, timezone
import csv
import json
import math
import uuid

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'profile'
OUT.mkdir(exist_ok=True)
UP = ROOT / 'upstream'
TABLES = ROOT / 'readback/tables'
SYMS = ('rb', 'hc', 'i')
FIELDS = ('timestamp', 'occurrence', 'record_id', 'child_id_2')
FRP = 'daowei2026/frp@be57d6752c9d43d10f1d670e1d2993bb8153ea7c:src/Frp/Instance/ISL/Opportunity/'
OI = 'daowei2026/observe-iterate@87b951bbd15078a2d6353bdd24afe0d8f19c845c:'


def read(path):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def write(name, rows, columns=None):
    rows = list(rows)
    columns = columns or list(dict.fromkeys(k for row in rows for k in row)) or ['empty']
    path = OUT / (name + '.csv')
    with path.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, columns, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)
    return str(path)


def jwrite(name, value):
    (OUT / (name + '.json')).write_text(json.dumps(value, ensure_ascii=False, indent=2, default=str) + '\n')


def number(value):
    return float(value) if value not in ('', None) else math.nan


def integer(value):
    return int(float(value))


def key(row):
    return tuple(row[field] for field in FIELDS)


def identifier(row, prefix):
    form = integer(row[prefix + '_idForm'])
    if form == 2:
        return row[prefix + '_idText']
    if form == 1:
        return str(uuid.UUID(int=(int(row[prefix + '_idHigh']) << 64) | int(row[prefix + '_idLow'])))
    return ''


def quantiles(values):
    values = sorted(float(x) for x in values if math.isfinite(float(x)))
    if not values:
        return dict(n=0)
    def q(p):
        at = (len(values) - 1) * p
        i = int(at)
        return values[i] + (values[min(i + 1, len(values) - 1)] - values[i]) * (at - i)
    return dict(n=len(values), minimum=values[0], p25=q(.25), median=q(.5), p75=q(.75), p90=q(.9), p95=q(.95), maximum=values[-1])


def session(timestamp):
    clock = timestamp[11:19]
    if '21:00:00' <= clock <= '23:00:00':
        return 'NIGHT_CLOCK_21_23'
    if '09:00:00' <= clock <= '15:00:00':
        return 'DAY_CLOCK_09_15'
    return 'OTHER_CLOCK'


binding = json.loads((ROOT / 'FeatureRunResultBinding.json').read_text())
assert binding['readback_validation']['all_31_tables_equal']
assert binding['code_version']['frp'].endswith('be57d6752c9d43d10f1d670e1d2993bb8153ea7c')
assert binding['parameter_version'] == 'b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3'
upstream = json.loads((ROOT / 'UPSTREAM_EXTRACTION.json').read_text())
assert upstream['completed'] and not upstream['producer_executed']
all_tables = {path.stem: read(path) for path in TABLES.glob('*.csv')}
assert len(all_tables) == 31
groups = all_tables['occurrences']
members = all_tables['occurrences_groupMembers']
required = all_tables['occurrences_groupRequired']
parts = {key(row): row for row in all_tables['occurrences_groupFormationParticipation']}
members_by, required_by = defaultdict(list), defaultdict(list)
for row in members:
    members_by[key(row)].append(row)
for row in required:
    required_by[key(row)].append(row)
klines = {symbol: read(UP / (symbol + '_kline.csv')) for symbol in SYMS}
kts = {s: {r['timestamp']: r for r in klines[s]} for s in SYMS}
kuti = {s: {integer(r['closeUti']): r for r in klines[s]} for s in SYMS}
def known(symbol, ts):
    return integer(kts[symbol][ts]['closeUti'])

checks = []
def check(name, violations, denominator, invariant, code):
    rows = list(violations)
    checks.append(dict(check_id=name, repeat_count=len(rows), denominator=denominator,
                       affected_ratio=len(rows) / denominator if denominator else 0,
                       invariant=invariant, evidence=code, examples=rows[:8]))
    write('violations_' + name, rows)

raw, turns, turn_lookup = [], [], {}
for symbol in SYMS:
    first = {}
    for row in read(UP / (symbol + '_rct.csv')):
        actual = integer(row['posUTI1'])
        if actual in first:
            continue
        polarity = number(row['pivot1']) * number(row['price1'])
        direction = 'DirectionDown' if polarity > 0 else 'DirectionUp' if polarity < 0 else 'Unknown'
        record = dict(symbol=symbol, actual=actual, actual_ts=kuti[symbol].get(actual, {}).get('timestamp', ''),
                      price=number(row['price1']), known=known(symbol, row['timestamp']), known_ts=row['timestamp'],
                      direction=direction, initial_anchor=not first)
        first[actual] = record
        raw.append(record)
    for rnd in ('value1', 'value2'):
        for order, row in enumerate(read(UP / (symbol + '_scale_' + rnd + '.csv'))):
            actual, confirm = integer(row[rnd + '.x']), integer(row[rnd + '.xConfirm'])
            origin = first[actual]
            uid = symbol + '/' + rnd + '/' + str(confirm)
            t = dict(symbol=symbol, round=rnd, source_row=order, turn_id=uid,
                     actual=actual, confirmation=confirm, known=known(symbol, row['timestamp']),
                     actual_ts=kuti[symbol].get(actual, {}).get('timestamp', ''),
                     confirmation_ts=kuti[symbol].get(confirm, {}).get('timestamp', ''), known_ts=row['timestamp'],
                     price=number(row[rnd + '.y']), confirmation_price=number(row[rnd + '.yConfirm']),
                     raw_known=origin['known'], direction=origin['direction'])
            t['lag_minutes'] = (t['known'] - actual) / 120
            t['actual_to_confirm_minutes'] = (confirm - actual) / 120
            t['confirm_to_selected_minutes'] = (t['known'] - confirm) / 120
            t['eligible_800_reference'] = t['known'] <= actual + 480000
            t['eligible_6_reference'] = t['known'] <= actual + 3600
            turns.append(t)
    previous = None
    for t in sorted((t for t in turns if t['symbol'] == symbol), key=lambda t: (t['known'], t['round'], t['source_row'])):
        t['initial_anchor'] = previous is None
        t['p_actual'] = previous['actual'] if previous else None
        t['p_price'] = previous['price'] if previous else None
        t['p_known'] = previous['raw_known'] if previous else None
        bend = None
        if previous and previous['actual'] < t['actual'] < t['confirmation']:
            bend = (t['confirmation_price'] - t['price']) * (t['actual'] - previous['actual']) - (t['price'] - previous['price']) * (t['confirmation'] - t['actual'])
        t['bend_sign'] = None if bend is None or bend == 0 else (1 if bend > 0 else -1)
        assert t['turn_id'] not in turn_lookup, '上游exact的简化定位键冲突'
        turn_lookup[t['turn_id']] = t
        previous = t

check('upstream_time_order', [dict(turn_id=t['turn_id']) for t in turns if not (t['actual'] <= t['confirmation'] <= t['known'] and t['raw_known'] <= t['known'])], len(turns),
      'actual/几何confirm/首次selected知识保持合法先后', FRP + 'U2/GroupCandidateKLineInput.hs')
check('upstream_duplicate_actual', [dict(symbol=s, actual=a, count=n) for (s, a), n in Counter((t['symbol'], t['actual']) for t in turns).items() if n > 1], len(turns),
      '两轮选择不得把同一原实际位置重复当作不同选中位置', '同参数ScaleTurnCalendar公开value1/value2')

revisions, lives, exact_rows, member_errors = [], defaultdict(list), {}, []
for group in groups:
    coordinate = key(group)
    ms, p = members_by[coordinate], parts[coordinate]
    life, rev = identifier(group, 'groupReference_referenceLife'), identifier(group, 'groupReference_referenceRevision')
    mids = []
    for member in ms:
        rnd = 'value1' if member['memberRound_name'] == 'FirstRound' else 'value2'
        uid = member['memberObject'] + '/' + rnd + '/' + str(integer(member['memberConfirmation']))
        mids.append(uid)
        source = turn_lookup.get(uid)
        if source is None:
            member_errors.append(dict(life=life, revision=rev, turn_id=uid, reason='upstream missing'))
            continue
        for left, right in [('memberActual','actual'), ('memberPrice','price'), ('memberConfirmation','confirmation'),
                            ('memberKnownFrom','known'), ('memberT_pointKnownFrom','raw_known'), ('memberC_pointPrice','confirmation_price')]:
            if number(member[left]) != source[right]:
                member_errors.append(dict(life=life, revision=rev, turn_id=uid, field=left, saved=member[left], upstream=source[right]))
        expected_direction='Unavailable' if source['direction']=='Unknown' else source['direction']
        if member['memberDirection_name'] != expected_direction:
            member_errors.append(dict(life=life, turn_id=uid, field='direction'))
    r = dict(life=life, revision=rev, timestamp=group['timestamp'], known=integer(group['groupKnownFrom']),
             original_anchor=number(group['groupOriginalAnchor']), original_deadline=number(group['groupOriginalDeadline']),
             original_revision_end=number(group['groupOriginalRevisionEnd']), anchor=number(group['groupAnchor']),
             deadline=number(group['groupDeadline']), revision_end=number(group['groupRevisionEnd']),
             observation=group['groupObservation_name'], local_basis=group['groupLocalBasis_name'],
             closed=integer(group['groupClosed']), duty_closed=integer(p['participationDutyClosed']),
             handoff_end=number(p['participationHandoffEnd']), coverage_incomplete=integer(group['groupCoverageIncomplete']),
             symbols='+'.join(sorted(m['memberObject'] for m in ms)), members=';'.join(sorted(mids)),
             member_count=len(ms), direction=ms[0]['memberDirection_name'],
             session=session(group['timestamp']), occurrence=group['occurrence'], record_id=group['record_id'], child_id_2=group['child_id_2'])
    revisions.append(r)
    lives[life].append(r)
    exact_rows.setdefault((life, rev), []).append(r)
for rows in lives.values():
    rows.sort(key=lambda row: (row['known'], int(row['occurrence']), int(row['record_id']), int(row['child_id_2'])))
births = [rows[0] for rows in lives.values()]
used = {mid for birth in births for mid in birth['members'].split(';')}
for t in turns:
    t['used_by_f800'] = t['turn_id'] in used
write('raw_turns', raw)
write('scale_turns', turns)
write('candidate_revisions', revisions)
write('candidate_births', births)
check('member_upstream_exact', member_errors, len(members), 'F成员实际/确认/可知、原始知识与价格方向必须对应准确上游', FRP + 'U2/GroupCandidateKLineInput.hs')
check('pair_cardinality', [dict(life=r['life'], timestamp=r['timestamp']) for r in revisions if len(required_by[key(r)]) != r['member_count']*(r['member_count']-1)//2], len(revisions), '每组观点必须有n(n-1)/2条Required', FRP + 'U2/GroupCandidateStorage.hs')
check('distinct_member_symbols', [dict(life=r['life'], timestamp=r['timestamp']) for r in revisions if len(set(r['symbols'].split('+'))) != r['member_count']], len(revisions), '每组同一对象至多一个成员', FRP + 'U2/GroupCandidateStorage.hs')
check('unique_group_exact', [dict(life=life, revision=rev, count=len(rs)) for (life, rev), rs in exact_rows.items() if len(rs)>1], len(revisions), '稀疏正式发行不应重复同一候选exact', FRP + 'U2/GroupCandidateEvolution.hs')
check('birth_within_800', [dict(life=b['life'], timestamp=b['timestamp']) for b in births if b['known'] > b['original_anchor']+480000], len(births), '首次准入必须在原actual锚点+800Δ以内', FRP + 'U2/GroupCandidateEvolution.hs')
check('nonexpanding_duty', [dict(life=life) for life, rs in lives.items() if any(b['deadline']>a['deadline'] or b['revision_end']>a['revision_end'] or b['handoff_end']>a['handoff_end'] for a,b in zip(rs,rs[1:]))], len(lives), '同Life的观察、修订和交接责任只能收紧', FRP + 'U2/GroupCandidateDecisions.hs')
check('original_question_fixed', [dict(life=life) for life, rs in lives.items() if len({(r['original_anchor'],r['original_deadline'],r['original_revision_end']) for r in rs})!=1], len(lives), '原问题三值在同Life固定', FRP + 'U2/GroupCandidateTypes.hs')
check('knowledge_matches_publication', [dict(life=r['life'], timestamp=r['timestamp']) for r in revisions if r['known'] != known('rb',r['timestamp'])], len(revisions), '此KLine入口观点知识位置与原事件收盘UTI对齐', FRP + 'U2/GroupCandidateKLineInput.hs')
check('closed_never_reopens', [dict(life=life) for life, rs in lives.items() if any(a['closed'] and not b['closed'] for a,b in zip(rs,rs[1:]))], len(lives), '形成观察关闭后不重新Open', FRP + 'U2/GroupCandidateEvolution.hs')
check('no_update_after_duty_close', [dict(life=life) for life,rs in lives.items() if any(a['duty_closed'] for a in rs[:-1])], len(lives), '当前正常KLine实例无期外更正，责任关闭后不继续原F修订', FRP + 'U2/GroupCandidateEvolution.hs')

previous_errors=[]
for row in all_tables['occurrences_groupPrevious']:
    parent=next(r for r in revisions if key(r)==key(row))
    target=(identifier(row,'referenceLife'),identifier(row,'referenceRevision'))
    if target not in exact_rows or target[0]!=parent['life'] or exact_rows[target][0]['known']>parent['known']:
        previous_errors.append(dict(life=parent['life'], revision=parent['revision'], target=str(target)))
check('previous_reference_integrity', previous_errors, len(all_tables['occurrences_groupPrevious']), 'previous指向同Life已存在且不超前的准确观点', '锁定TIS GroupCandidateReadSession.choose')
for name in ['occurrences_groupOverlaps','occurrences_groupCoveredBy']:
    bad=[]
    for row in all_tables[name]:
        life=identifier(row,'id') if 'id_idForm' in row else (str(uuid.UUID(int=(int(row['idHigh'])<<64)|int(row['idLow']))) if integer(row['idForm'])==1 else row['idText'])
        if life not in lives:bad.append(dict(parent=key(row), target=life))
    check(name+'_references',bad,len(all_tables[name]),'组间Life引用存在于准确结果内',FRP+'U2/GroupCandidateEvolution.hs')

by_coordinate = {key(r): r for r in revisions}
participation_errors=[]
for coordinate,p in parts.items():
    current=by_coordinate[coordinate]; first=lives[current['life']][0]
    for prefix,target in [('participationCandidate',current),('participationAdmission',first)]:
        if (p[prefix+'_definitionLife'],p[prefix+'_definitionRevision']) != (target['life'],target['revision']):
            participation_errors.append(dict(parent=coordinate,field=prefix,reason='exact mismatch'))
    for field,value in [('participationAdmissionKnown',first['known']),('participationDecisionKnown',current['known']),
                        ('participationQuestionAnchor',current['original_anchor']),('participationQuestionDeadline',current['original_deadline']),
                        ('participationQuestionRevisionEnd',current['original_revision_end']),('participationDeadline',current['deadline']),
                        ('participationRevisionEnd',current['revision_end'])]:
        if number(p[field]) != value: participation_errors.append(dict(parent=coordinate,field=field,reason='value mismatch'))
check('participation_candidate_admission_integrity',participation_errors,len(parts),'当前candidate exact、冻结admission exact与原问题边界必须闭合',FRP+'U2/GroupCandidateDecisions.hs')

source_roots={f['symbol']:f['full_dir'] for f in upstream['features'] if f['kind']=='scale'}
turn_refs={root+'/'+t['round']+'/'+str(t['confirmation']):t for t in turns for s,root in source_roots.items() if s==t['symbol']}
reference_errors=[]
for m in members:
    root=source_roots[m['memberObject']]
    rnd='value1' if m['memberRound_name']=='FirstRound' else 'value2'
    expected=root+'/'+rnd+'/'+str(integer(m['memberConfirmation']))
    if (identifier(m,'memberTurn_referenceLife'),identifier(m,'memberTurn_referenceRevision'),
        identifier(m,'memberSource_referenceLife'),identifier(m,'memberSource_referenceRevision')) != (expected,expected,root,rnd):
        reference_errors.append(dict(parent=key(m),object=m['memberObject'],reason='member source/exact mismatch'))
check('member_source_reference_integrity',reference_errors,len(members),'成员turn及source准确定位同参数ScaleTurn根/轮次/confirm',FRP+'U2/GroupCandidateKLineInput.hs')

part_member_errors=[]
for row in all_tables['occurrences_groupFormationParticipation_participationMembers']:
    target=turn_refs.get(row['participationTurn_definitionLife'])
    ms=members_by[key(row)]
    if target is None or target['turn_id'] not in by_coordinate[key(row)]['members'].split(';'):
        part_member_errors.append(dict(parent=key(row),reason='member reference missing'))
    elif any(number(row[field]) != target[value] for field,value in [('participationActual','actual'),('participationConfirmation','confirmation'),('participationMemberKnown','known')]):
        part_member_errors.append(dict(parent=key(row),reason='member values mismatch'))
check('participation_member_integrity',part_member_errors,len(all_tables['occurrences_groupFormationParticipation_participationMembers']),
      '参与成员必须对应当前组成员及准确上游实际/确认/知识',FRP+'U2/GroupCandidateDecisions.hs')

alternative_errors=[]; bridges=defaultdict(list)
for row in all_tables['occurrences_groupFormationParticipation_participationAlternatives_alternativeBridge']:
    bridges[tuple(row[k] for k in (*FIELDS,'child_id_3','child_id_4'))].append(row)
for row in all_tables['occurrences_groupFormationParticipation_participationAlternatives']:
    targets=[]
    for prefix in ['alternativeOwner','alternativeLeft','alternativeRight']:
        exact=(row[prefix+'_definitionLife'],row[prefix+'_definitionRevision'])
        if exact not in exact_rows or exact_rows[exact][0]['known']>integer(row['alternativeKnown']):
            alternative_errors.append(dict(parent=key(row),field=prefix,reason='missing or future exact'))
        else: targets.append(exact_rows[exact][0])
    if len(targets)==3:
        left,right=targets[1:]
        expected=set(left['members'].split(';')) & set(right['members'].split(';'))
        actual=set()
        for bridge in bridges[tuple(row[k] for k in (*FIELDS,'child_id_3','child_id_4'))]:
            t=turn_refs.get(bridge['participationTurn_definitionLife'])
            if t: actual.add(t['turn_id'])
        if actual!=expected: alternative_errors.append(dict(parent=key(row),field='bridge',reason='intersection mismatch'))
check('alternative_exact_bridge_integrity',alternative_errors,len(all_tables['occurrences_groupFormationParticipation_participationAlternatives']),
      '替代关系三端exact存在且不读取未来；bridge为两组共享转折',FRP+'U2/GroupCandidateDecisions.hs')

state_errors=[]
for r in revisions:
    bad=(r['observation']=='Open' and (r['closed'] or r['local_basis']=='Contradicted')) or \
        (r['observation']=='ClosedSupported' and (not r['closed'] or r['local_basis']!='Supported')) or \
        (r['observation']=='ClosedInsufficient' and (not r['closed'] or r['local_basis']!='Incomplete')) or \
        (r['observation']=='Withdrawn' and r['local_basis']!='Contradicted') or \
        (r['observation']=='Subsumed' and r['local_basis']!='Supported')
    if bad:state_errors.append(dict(life=r['life'],revision=r['revision'],observation=r['observation'],basis=r['local_basis'],closed=r['closed']))
check('observation_basis_closed_consistency',state_errors,len(revisions),'观察状态、局部依据及关闭三轴按声明合法；Subsumed不等于责任终止',FRP+'U2/GroupCandidateEvolution.hs')

def compare_pair(a,b):
    temporal='Support' if abs(a['actual']-b['actual'])<=1200 else 'Veto'
    direction='Unresolved' if 'Unknown' in (a['direction'],b['direction']) else ('Support' if a['direction']==b['direction'] else 'Veto')
    kind=direction  # 本正常KLine入口由同一polarity映射峰谷/方向；矩阵均为同类支持。
    bend='Unresolved' if a['bend_sign'] is None or b['bend_sign'] is None else 'Support' if a['bend_sign']==b['bend_sign'] else 'Veto'
    verdicts=(temporal,direction,kind,bend)
    decision='Veto' if 'Veto' in verdicts else 'Positive' if all(x=='Support' for x in verdicts) else 'Unresolved'
    return dict(distance_minutes=abs(a['actual']-b['actual'])/120,time=temporal,direction=direction,type=kind,bend=bend,decision=decision)

pair_errors=[]
for row in required:
    endpoints={identifier(m,'memberTurn_referenceLife'):m for m in members_by[key(row)]}
    pair=[]
    for prefix in ['pairLeft','pairRight']:
        member=endpoints.get(identifier(row,prefix+'_referenceLife'))
        if member is None:break
        rnd='value1' if member['memberRound_name']=='FirstRound' else 'value2'
        pair.append(turn_lookup[member['memberObject']+'/'+rnd+'/'+str(integer(member['memberConfirmation']))])
    if len(pair)!=2:
        pair_errors.append(dict(parent=key(row),reason='endpoint missing'));continue
    expected=compare_pair(*pair)
    for field in ['time','direction','type','bend']:
        if integer(row['pair'+field.capitalize()+'_requiredVerdict']) != {'Support':0,'Unresolved':1,'Veto':2}[expected[field]]:
            pair_errors.append(dict(parent=key(row),field=field,expected=expected[field]))
check('required_coordinate_consistency',pair_errors,4*len(required),'四项Required与同参数上游合法小值一致',FRP+'U2/GroupCandidatePairs.hs')
distances=all_tables['occurrences_groupRequired_pairDistance']
check('actual_2delta_limit',[dict(parent=key(row),distance=number(row['distanceValue'])) for row in distances if number(row['distanceValue'])>1200],len(distances),'当前公开候选的actual距离仍不超过2Δ，不能随800扩大',FRP+'U2/GroupCandidatePairs.hs')

near=[]
ordered=sorted(turns,key=lambda t:t['actual'])
for i,a in enumerate(ordered):
    for b in ordered[i+1:]:
        if b['actual']-a['actual']>1200:break
        if a['symbol']==b['symbol']:continue
        arrival=max(a['known'],b['known']);anchor=min(a['actual'],b['actual'])
        near.append(dict(left=a['turn_id'],right=b['turn_id'],left_symbol=a['symbol'],right_symbol=b['symbol'],
                         includes_initial_anchor=a['initial_anchor'] or b['initial_anchor'],
                         actual_year=a['actual_ts'][:4],first_joint_known=max(a['known_ts'],b['known_ts']),
                         anchor=anchor,arrival=arrival,eligible_800=arrival<=anchor+480000,eligible_6=arrival<=anchor+3600,
                         **compare_pair(a,b)))
write('near_actual_pair_screen',near)
co_members=set()
for birth in births:
    co_members.update(tuple(sorted(pair)) for pair in combinations(birth['members'].split(';'),2))
potential_unseen=[p for p in near if p['decision']!='Veto' and p['eligible_800'] and tuple(sorted([p['left'],p['right']])) not in co_members]
check('eligible_pair_not_in_any_candidate',potential_unseen,len([p for p in near if p['decision']!='Veto' and p['eligible_800']]),
      '正常KLine完整已知的非否决边应包含于至少一个极大候选组合；这是独立规则筛查，不是业务真值',FRP+'U2/GroupCandidateEvolution.hs')
near_by=defaultdict(list)
for pair in near:
    near_by[pair['left']].append(pair);near_by[pair['right']].append(pair)
for t in turns:
    relations=near_by[t['turn_id']]
    if t['used_by_f800']:stage='OBSERVED_IN_F800'
    elif not t['eligible_800_reference']:stage='REFERENCE_MATERIAL_AGE'
    elif not relations:stage='REFERENCE_NO_OTHER_SYMBOL_WITHIN_2DELTA'
    elif all(p['decision']=='Veto' for p in relations):stage='REFERENCE_RELATIONS_VETO'
    elif not any(p['decision']!='Veto' and p['eligible_800'] for p in relations):stage='REFERENCE_NO_JOINT_TIMELY_PAIR'
    else:stage='REFERENCE_ELIGIBLE_UNOBSERVED'
    t['first_block_screen']=stage
write('scale_turns',turns)

# 真实整数UTI与有效价格的连续观测对照；不使用native的浮点position内部值。
continuous={}
for symbol in SYMS:
    values={};previous=None;start=None
    for row in klines[symbol]:
        u=integer(row['closeUti']);valid=math.isfinite(number(row['close']))
        if valid:
            start=start if previous is not None and u-previous==600 else u
            previous=u
            values[u]=start
        else:
            previous=None;start=None
    continuous[symbol]=values
coverage_conflicts=[]
coverage_incomplete=[r for r in revisions if r['coverage_incomplete']]
for r in coverage_incomplete:
    starts=[continuous[s].get(r['known']) for s in SYMS]
    if all(start is not None and start<=r['known']-480000 for start in starts):
        coverage_conflicts.append(dict(life=r['life'],revision=r['revision'],timestamp=r['timestamp'],known=r['known'],
                                       symbols=r['symbols'],continuous_rb=starts[0],continuous_hc=starts[1],continuous_i=starts[2],
                                       required_from=r['known']-480000,groupCoverageIncomplete=1))
check('coverage_flag_vs_continuous_input',coverage_conflicts,len(revisions),
      '正常KLine路径三对象在[u-800Δ,u]都有有效连续价格和Calendar UTI、且无未知Clock时，不应宣称观察域不完整',
      FRP+'U2/GroupCandidateMaterial.hs')

# 反向覆盖核对：完整flag与公开输入缺价的对照；缺值的生产语义交诊断，不在G查根因。
complete_gap_conflicts=[]
missing_by_symbol={symbol:[row for row in klines[symbol] if not math.isfinite(number(row['close']))] for symbol in SYMS}
for r in revisions:
    if r['coverage_incomplete']:continue
    gap_rows={s:[row for row in missing_by_symbol[s] if r['known']-480000<=integer(row['closeUti'])<=r['known']] for s in SYMS}
    if any(gap_rows.values()):
        affected=[s for s in SYMS if gap_rows[s]]
        complete_gap_conflicts.append(dict(life=r['life'],revision=r['revision'],timestamp=r['timestamp'],known=r['known'],
            symbols=r['symbols'],required_from=r['known']-480000,groupCoverageIncomplete=0,
            missing_symbols='+'.join(affected),missing_rows_per_symbol=';'.join(s+':'+str(len(gap_rows[s])) for s in affected),
            first_missing=min(row['timestamp'] for s in affected for row in gap_rows[s]),
            last_missing=max(row['timestamp'] for s in affected for row in gap_rows[s]),
            source='完整独立KLine公开表；空OHLC的真实SourceFailure/豁免语义待诊断'))
check('complete_flag_with_input_price_gap',complete_gap_conflicts,len(revisions)-len(coverage_incomplete),
      '正常KLine固定域若观察窗内存在非豁免实际缺价/失知或真实间隙，不能标记完整；本对照先定位公开OHLC空行与flag=0，空值是否SourceFailure或正式豁免待诊断',
      FRP+'U2/GroupCandidateMaterial.hs#accumulateForwardCoverage/covered')

# 按对象合同核完整previous链与全部非空group子表父键；保留同拍坐标。
previous_by=defaultdict(list)
for row in all_tables['occurrences_groupPrevious']:
    previous_by[key(row)].append((identifier(row,'referenceLife'),identifier(row,'referenceRevision')))
chain_errors=[]
for life,rs in lives.items():
    for i,r in enumerate(rs):
        expected=[] if i==0 else [(life,rs[i-1]['revision'])]
        actual=previous_by.get(key(r),[])
        if actual!=expected:
            chain_errors.append(dict(life=life,revision=r['revision'],timestamp=r['timestamp'],expected=str(expected),actual=str(actual)))
check('complete_previous_chain',chain_errors,len(revisions),'每Life首观点无previous，后续观点恰指向同Life即时前版；顺序按实际坐标，不用UUID排序',FRP+'U2/GroupCandidateEvolution.hs')
child_errors=[];child_denominator=0
for name,rows in all_tables.items():
    if not name.startswith('occurrences_group') or not rows or not all(f in rows[0] for f in FIELDS):continue
    child_denominator+=len(rows)
    child_errors.extend(dict(table=name,parent=str(key(row))) for row in rows if key(row) not in by_coordinate)
check('all_group_child_parent_integrity',child_errors,child_denominator,'每条正式group子表行必须对应已读取主观点完整父坐标',FRP+'U2/GroupCandidateStorage.hs')

symbol_rows=[]
for symbol in (*SYMS,'ALL_DISTINCT'):
    tt=turns if symbol=='ALL_DISTINCT' else [t for t in turns if t['symbol']==symbol]
    rr=raw if symbol=='ALL_DISTINCT' else [t for t in raw if t['symbol']==symbol]
    bb=births if symbol=='ALL_DISTINCT' else [r for r in births if symbol in r['symbols'].split('+')]
    vv=revisions if symbol=='ALL_DISTINCT' else [r for r in revisions if symbol in r['symbols'].split('+')]
    symbol_rows.append(dict(symbol=symbol,raw_turn_positions=len(rr),scale_turn_positions=len(tt),
        initial_scale_anchors=sum(t['initial_anchor'] for t in tt),eligible_800_reference=sum(t['eligible_800_reference'] for t in tt),
        eligible_6_reference=sum(t['eligible_6_reference'] for t in tt),used_scale_turn_positions=sum(t['used_by_f800'] for t in tt),
        candidate_lives=len(bb),candidate_revision_occurrences=len(vv),
        candidates_born_after_legacy_6_deadline=sum(r['known']>r['original_anchor']+3600 for r in bb),
        used_scale_ratio=sum(t['used_by_f800'] for t in tt)/len(tt) if tt else 0,
        count_meaning='含初始化锚点；品种组数跨品种重叠，ALL_DISTINCT为全局去重，occurrence不是组数'))
write('counts_by_symbol',symbol_rows)
direction_rows=[]
for symbol in (*SYMS,'ALL_DISTINCT'):
    for direction in ['DirectionUp','DirectionDown','Unknown']:
        tt=[t for t in turns if (symbol=='ALL_DISTINCT' or t['symbol']==symbol) and t['direction']==direction]
        saved='Unavailable' if direction=='Unknown' else direction
        bb=[r for r in births if (symbol=='ALL_DISTINCT' or symbol in r['symbols'].split('+')) and r['direction']==saved]
        vv=[r for r in revisions if (symbol=='ALL_DISTINCT' or symbol in r['symbols'].split('+')) and r['direction']==saved]
        direction_rows.append(dict(symbol=symbol,direction=direction,scale_turn_positions=len(tt),
            used_scale_turn_positions=sum(t['used_by_f800'] for t in tt),candidate_lives=len(bb),revision_occurrences=len(vv),
            meaning='Unknown对应公开Unavailable；初始化锚点不是有效峰谷方向；品种组数为包含关系'))
write('counts_by_direction',direction_rows)
period_rows=[]
for symbol in (*SYMS,'ALL_DISTINCT'):
    for year in ['2021','2022','2023']:
        tt=[t for t in turns if (symbol=='ALL_DISTINCT' or t['symbol']==symbol) and t['known_ts'].startswith(year)]
        bb=[r for r in births if (symbol=='ALL_DISTINCT' or symbol in r['symbols'].split('+')) and r['timestamp'].startswith(year)]
        vv=[r for r in revisions if (symbol=='ALL_DISTINCT' or symbol in r['symbols'].split('+')) and r['timestamp'].startswith(year)]
        period_rows.append(dict(symbol=symbol,year=year,scale_turn_positions=len(tt),used_scale_turn_positions=sum(t['used_by_f800'] for t in tt),
            candidate_lives=len(bb),candidate_revision_occurrences=len(vv),births_after_legacy_6=sum(r['known']>r['original_anchor']+3600 for r in bb),
            time_basis='上游按selected知识年，组按首次publication年，版本按当次publication年；不是混用actual年'))
write('counts_by_symbol_year',period_rows)
write('counts_by_actual_year',[dict(symbol=s,actual_year=y,scale_turn_positions=sum(t['symbol']==s and t['actual_ts'].startswith(y) for t in turns)) for s in SYMS for y in ['2021','2022','2023']])
write('counts_by_month',[dict(month=f'{y}-{m:02}',candidate_lives=sum(r['timestamp'].startswith(f'{y}-{m:02}') for r in births),revision_occurrences=sum(r['timestamp'].startswith(f'{y}-{m:02}') for r in revisions)) for y in [2021,2022,2023] for m in range(1,13)])
write('first_block_reference_by_symbol',[dict(symbol=s,stage=stage,count=sum(t['symbol']==s and t['first_block_screen']==stage for t in turns),denominator=sum(t['symbol']==s for t in turns),meaning='独立规则筛查/观察到的参与，不是未暴露native计数器') for s in SYMS for stage in sorted({t['first_block_screen'] for t in turns})])
write('latency_by_symbol',[dict(symbol=s,measure=measure,unit='Calendar开放分钟',**quantiles(t[field] for t in turns if t['symbol']==s and not t['initial_anchor'])) for s in SYMS for measure,field in [('actual_to_selected','lag_minutes'),('actual_to_geometry_confirm','actual_to_confirm_minutes'),('geometry_confirm_to_selected','confirm_to_selected_minutes')]])

lifecycle=[];transitions=Counter();occupancy=Counter()
last_u=max(kuti['rb'])
for life,rows in lives.items():
    birth,last=rows[0],rows[-1]
    lifecycle.append(dict(life=life,symbols=birth['symbols'],first_timestamp=birth['timestamp'],last_timestamp=last['timestamp'],
        revision_count=len(rows),first_known=birth['known'],last_known=last['known'],anchor=birth['original_anchor'],
        observation_open_minutes=(birth['deadline']-birth['known'])/120,
        admission_actual_age_minutes=(birth['known']-birth['original_anchor'])/120,
        observed_revision_span_minutes=(last['known']-birth['known'])/120,
        original_observation_duty_minutes=(birth['original_deadline']-birth['original_anchor'])/120,
        revision_tail_minutes=(birth['original_revision_end']-birth['original_deadline'])/120,
        handoff_tail_minutes=(last['handoff_end']-last['revision_end'])/120,
        final_duty_closed=last['duty_closed'],right_censored=last['revision_end']>last_u,
        final_observation=last['observation'],time_basis='原F责任/观点跨度，不称市场运动寿命'))
    for a,b in zip(rows,rows[1:]):
        transitions[(a['observation'],b['observation'])]+=1
    for i,row in enumerate(rows):
        end=rows[i+1]['known'] if i+1<len(rows) else min(row['revision_end'],last_u)
        occupancy[row['observation']]+=max(0,min(end,row['revision_end'])-row['known'])/120
write('lifecycles',lifecycle)
write('state_transitions',[dict(from_state=a,to_state=b,count=n,count_unit='同Life相邻已发表revision的状态转换') for (a,b),n in sorted(transitions.items())])
write('state_occupancy',[dict(state=state,revision_count=sum(r['observation']==state for r in revisions),held_view_minutes=occupancy[state],meaning='相邻已发表观点按知识UTI持有，末段截断于责任终点/样本末；非逐Tick内部Dynamic trace') for state in ['Open','ClosedSupported','ClosedInsufficient','Withdrawn','Subsumed','EndedByScope']])
write('lifecycle_distributions',[dict(measure=field,**quantiles(row[field] for row in lifecycle)) for field in ['revision_count','observation_open_minutes','admission_actual_age_minutes','observed_revision_span_minutes','original_observation_duty_minutes','revision_tail_minutes','handoff_tail_minutes']])
write('branch_reachability',[dict(category=category,value=value,count=sum(r[field]==value for r in revisions),denominator=len(revisions),meaning='样本可达性；零次数不证明逻辑不可达') for category,field,values in [('local_basis','local_basis',['Supported','Incomplete','Contradicted']),('observation','observation',['Open','ClosedSupported','ClosedInsufficient','Withdrawn','Subsumed','EndedByScope'])] for value in values])
write('required_reasons',[dict(coordinate=coordinate,field=field,value=value,count=count,denominator=len(required)) for coordinate in ['Time','Direction','Type','Bend'] for field in ['requiredVerdict_name','requiredGap_name','requiredVeto_name'] for value,count in Counter(row['pair'+coordinate+'_'+field] for row in required).items()])
events={(row['timestamp'],row['occurrence']) for name in ['definitions','occurrences'] for row in all_tables[name]}
sessions=[]
for label in sorted({session(row['timestamp']) for row in klines['rb']}):
    denominator=sum(session(row['timestamp'])==label for row in klines['rb'])
    vv=[r for r in revisions if r['session']==label];bb=[r for r in births if r['session']==label]
    sessions.append(dict(session=label,input_5m_positions=denominator,candidate_lives=len(bb),revision_occurrences=len(vv),
                         revisions_per_1000_input_positions=1000*len(vv)/denominator if denominator else None,
                         coverage_conflict_occurrences=sum(session(r['timestamp'])==label for r in coverage_conflicts)))
write('counts_by_session',sessions)

def opening(ts):
    return 'OPENING_FIRST_15M' if ('09:00:00'<=ts[11:19]<='09:15:00' or '21:00:00'<=ts[11:19]<='21:15:00') else 'OTHER_TRADING_TIME'

# 每层同时比较密度、责任跨度、状态/分支、reason及结构疑点率。
stratified=[];stratified_states=[];stratified_reasons=[];stratified_held=[]
time_rows=klines['rb'];time_utis=[integer(r['closeUti']) for r in time_rows]
held=Counter()
for life,rs in lives.items():
    for i,r in enumerate(rs):
        end=rs[i+1]['known'] if i+1<len(rs) else min(r['revision_end'],last_u)
        lo=bisect_right(time_utis,r['known']-1);hi=bisect_right(time_utis,min(end,r['revision_end'])-1)
        for point in time_rows[lo:hi]:
            ts=point['timestamp']
            held[('YEAR',ts[:4],r['observation'])]+=5
            held[('SESSION',session(ts),r['observation'])]+=5
            held[('OPENING',opening(ts),r['observation'])]+=5
            for s in r['symbols'].split('+'):held[('SYMBOL',s,r['observation'])]+=5
for (dimension,layer,state),minutes in sorted(held.items()):
    stratified_held.append(dict(dimension=dimension,stratum_id=layer,state=state,held_view_sampled_minutes=minutes,
        count_meaning='以公开5m位置对已发表观点持有区间取样×5开放分钟；不作内部逐Tick trace'))
for dimension,layers in [('SYMBOL',list(SYMS)),('YEAR',['2021','2022','2023']),
                          ('SESSION',sorted({session(r['timestamp']) for r in time_rows})),
                          ('OPENING',['OPENING_FIRST_15M','OTHER_TRADING_TIME'])]:
    for layer in layers:
        def fits(r):
            if dimension=='SYMBOL':return layer in r['symbols'].split('+')
            if dimension=='YEAR':return r['timestamp'].startswith(layer)
            if dimension=='SESSION':return session(r['timestamp'])==layer
            return opening(r['timestamp'])==layer
        def inputfits(r):
            if dimension=='SYMBOL':return True
            if dimension=='YEAR':return r['timestamp'].startswith(layer)
            if dimension=='SESSION':return session(r['timestamp'])==layer
            return opening(r['timestamp'])==layer
        vv=[r for r in revisions if fits(r)];bb=[r for r in births if fits(r)]
        ids={r['life'] for r in bb};ll=[r for r in lifecycle if r['life'] in ids]
        pairs=[p for p in required if fits(by_coordinate[key(p)])]
        den=sum(inputfits(r) for r in time_rows)
        conflicts=[r for r in coverage_conflicts if fits(r)]
        stratified.append(dict(dimension=dimension,stratum_id=layer,input_positions=den,birth_lives=len(bb),
            revision_occurrences=len(vv),revisions_per_1000_input_positions=len(vv)*1000/den if den else None,
            median_admission_actual_age_minutes=quantiles(r['admission_actual_age_minutes'] for r in ll).get('median'),
            median_observed_revision_span_minutes=quantiles(r['observed_revision_span_minutes'] for r in ll).get('median'),
            duty_closed_last_lives=sum(r['final_duty_closed'] for r in ll),right_censored_lives=sum(r['right_censored'] for r in ll),
            coverage_flagged_occurrences=sum(r['coverage_incomplete'] for r in vv),coverage_conflict_occurrences=len(conflicts),
            coverage_conflict_ratio=len(conflicts)/len(vv) if vv else None,
            meaning='Life及跨度按首次publication层；观点/Required按当次publication层；SYMBOL为包含关系，可重叠'))
        for field in ['observation','local_basis','closed','duty_closed']:
            for value,count in sorted(Counter(r[field] for r in vv).items(),key=lambda x:str(x[0])):
                stratified_states.append(dict(dimension=dimension,stratum_id=layer,field=field,value=value,count=count,denominator=len(vv)))
        for coordinate in ['Time','Direction','Type','Bend']:
            for field in ['requiredVerdict_name','requiredGap_name','requiredVeto_name']:
                for value,count in Counter(p['pair'+coordinate+'_'+field] for p in pairs).items():
                    stratified_reasons.append(dict(dimension=dimension,stratum_id=layer,coordinate=coordinate,field=field,value=value,count=count,denominator=len(pairs)))
write('cross_strata_comparison',stratified)
write('cross_strata_states',stratified_states)
write('cross_strata_reasons',stratified_reasons)
write('cross_strata_held_view_time',stratified_held)
same_tick=[]
for (life,ts),n in Counter((r['life'],r['timestamp']) for r in revisions).items():
    if n>1:same_tick.append(dict(life=life,timestamp=ts,count=n,meaning='保留原occurrence及child坐标，不按timestamp去重；需按previous核序'))
write('same_tick_multiple_views',same_tick)
endpoints=sorted([(b['known'],1) for b in births]+[(min(rows[-1]['revision_end'],last_u),-1) for rows in lives.values()],key=lambda p:(p[0],-p[1]))
active=peak=0
for u,change in endpoints:active+=change;peak=max(peak,active)
summary=dict(candidate_lives=len(lives),candidate_revision_occurrences=len(revisions),publication_events=len(events),
    definition_only_publication_events=len({(r['timestamp'],r['occurrence']) for r in all_tables['definitions']}-{(r['timestamp'],r['occurrence']) for r in groups}),
    upstream_raw_positions=len(raw),upstream_scale_positions=len(turns),initial_scale_anchors=sum(t['initial_anchor'] for t in turns),
    used_distinct_scale_positions=len(used),input_5m_positions=len(klines['rb']),input_symbol_rows=sum(len(v) for v in klines.values()),
    revision_events_per_1000_input_positions=1000*len(revisions)/len(klines['rb']),peak_responsibility_active_lives=peak,
    right_censored_lives=sum(row['right_censored'] for row in lifecycle),coverage_incomplete_occurrences=len(coverage_incomplete),
    coverage_incomplete_lives=len({r['life'] for r in coverage_incomplete}),coverage_conflict_occurrences=len(coverage_conflicts),
    coverage_conflict_lives=len({r['life'] for r in coverage_conflicts}),potential_eligible_pairs_unseen=len(potential_unseen),
    near_actual_pair_screen_count=len(near),positive_near_pair_screen_count=sum(p['decision']=='Positive' for p in near),
    positive_near_joint_eligible_800=sum(p['decision']=='Positive' and p['eligible_800'] for p in near),
    positive_near_joint_eligible_6=sum(p['decision']=='Positive' and p['eligible_6'] for p in near),
    candidate_births_after_legacy_6=sum(r['known']>r['original_anchor']+3600 for r in births),
    warning='近时pair及准入筛查不是应输出的业务真值；组数增加不能证明800合理')
jwrite('SUMMARY',summary)
jwrite('STRUCTURAL_CHECKS',checks)
write('structural_check_summary',[{k:v for k,v in row.items() if k!='examples'} for row in checks])
print(json.dumps(summary,ensure_ascii=False,indent=2))
print('CHECKS',json.dumps({c['check_id']:c['repeat_count'] for c in checks},ensure_ascii=False))
