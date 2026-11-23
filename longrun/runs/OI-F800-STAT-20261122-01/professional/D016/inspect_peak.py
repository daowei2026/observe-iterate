"""从精确已发布原生表重建峰值责任集合、逐Life时序和区分性对照。非新Feature运行。"""
from common import *
from collections import defaultdict,Counter
from decimal import Decimal
from bisect import bisect_left,bisect_right
def num(s):return int(Decimal(s))
def csvout(name,data):
 p=ROOT/name;p.parent.mkdir(parents=True,exist_ok=True)
 keys=list(dict.fromkeys(k for r in data for k in r))
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=keys,lineterminator='\n');w.writeheader();w.writerows(data)
needed=['readback/tables/'+f.name for f in sorted((D008/'readback/tables').glob('*.csv'))]+['profile/candidate_births.csv','profile/candidate_revisions.csv','profile/scale_turns.csv','profile/lifecycles.csv','UPSTREAM_EXTRACTION.json','profile/SUMMARY.json']
audit=[]
for n in needed:
 raw=(D008/n).read_bytes();assert raw==git_bytes(U,PREFIX+'/professional/D008/'+n)
 audit.append(dict(source_ref=pro_ref(n),bytes=len(raw),sha256=sha(raw),local_path=str(D008/n),git_bytes_match=True))
save('REUSE_EVIDENCE_READBACK.json',dict(entries=audit,count=len(audit),native_tables=31))
ex=json.loads((D008/'UPSTREAM_EXTRACTION.json').read_text());meta=next(x for x in ex['features'] if x['symbol']=='rb' and x['kind']=='kline')['tables'][0]
raw=Path(meta['path']).read_bytes();assert sha(raw)==meta['sha256']
ks=list(csv.DictReader(raw.decode('utf-8-sig').splitlines()));axis=[num(k['closeUti']) for k in ks];times=[k['timestamp'] for k in ks]
assert len(axis)==49683 and all(y-x==600 for x,y in zip(axis,axis[1:]))
def ts(u):
 j=bisect_left(axis,u)
 return times[j] if j<len(axis) and axis[j]==u else None
save('CALENDAR_SOURCE_READBACK.json',dict(source_ref=pro_ref('UPSTREAM_EXTRACTION.json'),receipt_location='features[symbol=rb,kind=kline].tables[0]',path=meta['path'],sha256=sha(raw),rows=len(axis),source_csv_not_published=True,receipt_hash_matches=True,time_unit='CalendarUTITick',ticks_per_open_minute=120,sample_stride=600))
tables={n:rows('readback/tables/'+n+'.csv') for n in ['occurrences','occurrences_groupMembers','occurrences_groupFormationParticipation','occurrences_groupRequired','occurrences_groupRequired_pairDistance','occurrences_groupPrevious','occurrences_groupCoveredBy','occurrences_groupOverlaps','occurrences_groupMembers_memberClock']}
parts={parent(r):r for r in tables['occurrences_groupFormationParticipation']}
ms=defaultdict(list);req=defaultdict(list);prev=defaultdict(list);covers=defaultdict(list);overlap=defaultdict(list)
for r in tables['occurrences_groupMembers']:ms[parent(r)].append(r)
for r in tables['occurrences_groupRequired']:req[parent(r)].append(r)
for r in tables['occurrences_groupPrevious']:prev[parent(r)].append(r)
for r in tables['occurrences_groupCoveredBy']:covers[parent(r)].append(uid(r,''))
for r in tables['occurrences_groupOverlaps']:overlap[parent(r)].append(uid(r,''))
bylife=defaultdict(list);byp={}
for r in tables['occurrences']:
 g=dict(life=uid(r,'groupReference_referenceLife_'),revision=uid(r,'groupReference_referenceRevision_'),known=num(r['groupKnownFrom']),row=r,p=parent(r))
 g['signature']=tuple(sorted((m['memberObject'],uid(m,'memberTurn_referenceLife_')) for m in ms[g['p']]))
 bylife[g['life']].append(g);byp[g['p']]=g
for gs in bylife.values():gs.sort(key=lambda g:(g['known'],g['p']))
def asof(gs,u):
 j=bisect_right([g['known'] for g in gs],u)-1
 return gs[j] if j>=0 else None
def latest(life,u):return asof(bylife[life],u)
peak=json.loads((D015/'ConcurrencyProfile.json').read_text());u=peak['first_peak_uti'];end=peak['peak_runs'][0]['last_sample_uti']
roster={l:latest(l,u) for l,gs in bylife.items() if gs[0]['known']<=u<=num(gs[0]['row']['groupRevisionEnd'])}
assert len(roster)==36
roster=dict(sorted(roster.items(),key=lambda kv:(num(kv[1]['row']['groupOriginalAnchor']),kv[0])))
ids={l:'L%02d'%j for j,l in enumerate(roster,1)}
details=[];flat=[];hist=[];checks=[]
def check(name,den,bad):
 checks.append(dict(check_id=name,denominator=den,conflicts=len(bad),examples=bad[:5]))
bad_prev=[];bad_id=[];bad_member=[];bad_duty=[];bad_knowledge=[]
all_sigs=defaultdict(list)
for l,gs in bylife.items():all_sigs[gs[0]['signature']].append(l)
turns=rows('profile/scale_turns.csv');turnindex={r['turn_id']:r for r in turns}
distances={tuple(list(parent(r))+[num(r['child_id_3'])]):num(r['value']) if 'value' in r else r for r in tables['occurrences_groupRequired_pairDistance']}
for l,g in roster.items():
 gs=bylife[l];r=g['row'];p=g['p'];part=parts[p];first=gs[0];last=gs[-1]
 a,d,e=[num(r[k]) for k in ['groupAnchor','groupDeadline','groupRevisionEnd']]
 admission=num(parts[first['p']]['participationAdmissionKnown']);close=[x for x in gs if num(parts[x['p']]['participationDutyClosed'])==1]
 closeg=close[0] if close else None
 members=[]
 for m in sorted(ms[p],key=lambda m:m['memberObject']):
  full=uid(m,'memberTurn_referenceLife_');turn_id=m['memberObject']+'/'+full.split('/')[-2]+'/'+full.split('/')[-1]
  source=turnindex[turn_id]
  successors=[t for t in turns if t['symbol']==m['memberObject'] and num(t['known'])<=u and num(t['actual'])>num(m['memberActual'])]
  after=[t for t in successors if t['round']==source['round']]
  t=dict(object=m['memberObject'],turn_life=full,turn_revision=uid(m,'memberTurn_referenceRevision_'),source_life=uid(m,'memberSource_referenceLife_'),source_revision=uid(m,'memberSource_referenceRevision_'),locator=turn_id,actual=num(m['memberActual']),actual_time=ts(num(m['memberActual'])),confirmation=num(m['memberConfirmation']),confirmation_time=ts(num(m['memberConfirmation'])),known=num(m['memberKnownFrom']),known_time=ts(num(m['memberKnownFrom'])),age_open_minutes=(u-num(m['memberActual']))/120,direction=m['memberDirection_name'],type=m['memberType_name'],round=m['memberRound_name'],status=m['memberStatus_name'],retracted=num(m['memberRetracted']),price=float(m['memberPrice']),later_selected_turns_same_object=len(successors),later_selected_turns_same_round=len(after),latest_same_round_known=max((num(t['known']) for t in after),default=None),native_parent=list(parent(m)),native_member_child_id=num(m['child_id_3']))
  members.append(t)
  if num(source['actual'])!=t['actual'] or num(source['known'])!=t['known']:bad_member.append([l,turn_id,'upstream_mismatch'])
 for j,x in enumerate(gs):
  pp=x['p'];xr=x['row'];xp=parts[pp];prs=prev[pp]
  good=(not prs) if j==0 else len(prs)==1 and uid(prs[0],'referenceLife_')==l and uid(prs[0],'referenceRevision_')==gs[j-1]['revision']
  if not good:bad_prev.append([l,x['revision']])
  if x['signature']!=first['signature'] or any(num(xr[k])!=num(first['row'][k]) for k in ['groupOriginalAnchor','groupOriginalDeadline','groupOriginalRevisionEnd']):bad_id.append([l,x['revision']])
  if xp['participationAdmission_definitionLife']!=l or xp['participationAdmission_definitionRevision']!=first['revision'] or xp['participationCandidate_definitionRevision']!=x['revision']:bad_id.append([l,'admission_current_exact'])
  if num(xp['participationDutyClosed'])!=int(x['known']>=num(xr['groupRevisionEnd'])):bad_duty.append([l,x['revision']])
  if any(num(m['memberKnownFrom'])>x['known'] for m in ms[pp]):bad_knowledge.append([l,x['revision']])
  hist.append(dict(case_id=ids[l],life=l,revision=x['revision'],known=x['known'],timestamp=x['p'][0],full_parent=list(x['p']),previous_revision=None if not prs else uid(prs[0],'referenceRevision_'),observation=xr['groupObservation_name'],local_basis=xr['groupLocalBasis_name'],duty_closed=num(xp['participationDutyClosed']),anchor=num(xr['groupAnchor']),deadline=num(xr['groupDeadline']),revision_end=num(xr['groupRevisionEnd']),handoff_end=num(xp['participationHandoffEnd']),covered_by=covers[pp],overlaps=overlap[pp]))
 required=[dict(left=uid(q,'pairLeft_referenceLife_'),right=uid(q,'pairRight_referenceLife_'),verdicts={k:q[k+'_requiredVerdict_name'] for k in ['pairTime','pairDirection','pairType','pairBend']},native_child_id=num(q['child_id_3'])) for q in req[p]]
 v=dict(case_id=ids[l],life=l,original_question=dict(anchor=num(r['groupOriginalAnchor']),deadline=num(r['groupOriginalDeadline']),revision_end=num(r['groupOriginalRevisionEnd'])),current_question=dict(anchor=a,deadline=d,revision_end=e,handoff_end=num(part['participationHandoffEnd'])),actual_time=ts(a),first_revision=first['revision'],admission_known=admission,admission_time=first['p'][0],admission_actual_age_open_minutes=(admission-a)/120,age_open_minutes=(u-a)/120,current_revision=g['revision'],current_revision_known=g['known'],current_revision_time=p[0],minutes_since_latest_revision=(u-g['known'])/120,full_parent=list(p),revisions_to_peak=sum(x['known']<=u for x in gs),revisions_full_sample=len(gs),observation=r['groupObservation_name'],local_basis=r['groupLocalBasis_name'],group_closed=num(r['groupClosed']),coverage_incomplete=num(r['groupCoverageIncomplete']),duty_closed=num(part['participationDutyClosed']),alternatives=r['groupAlternative_name'],deadline_time=ts(d),revision_end_time=ts(e),handoff_end_time=ts(num(part['participationHandoffEnd'])),remaining_deadline_open_minutes=(d-u)/120,remaining_revision_open_minutes=(e-u)/120,remaining_handoff_open_minutes=(num(part['participationHandoffEnd'])-u)/120,covered_by=covers[p],overlaps=overlap[p],members=members,required_pairs=required,final_revision=last['revision'],final_known=last['known'],final_time=last['p'][0],first_duty_close_known=closeg['known'] if closeg else None,first_duty_close_time=closeg['p'][0] if closeg else None,final_observation=last['row']['groupObservation_name'],duplicate_member_signature_life_count=len(all_sigs[first['signature']]),internal_active='SOURCE_RULE_RECONSTRUCTED_TRUE' if u<e else 'SOURCE_RULE_RECONSTRUCTED_FALSE',business_usefulness='NOT_PROVEN_BY_SUPPORT_OR_RETENTION_ALONE')
 details.append(v)
 flat.append({k:v[k] for k in ['case_id','life','first_revision','admission_time','actual_time','age_open_minutes','current_revision','current_revision_time','minutes_since_latest_revision','revisions_to_peak','revisions_full_sample','observation','local_basis','coverage_incomplete','deadline_time','revision_end_time','handoff_end_time','remaining_deadline_open_minutes','first_duty_close_time','final_observation','internal_active']}|dict(symbols='+'.join(m['object'] for m in members),directions='+'.join(m['direction'] for m in members),member_locators=';'.join(m['locator'] for m in members),covered_by=';'.join(covers[p]),overlaps=';'.join(overlap[p]),all_members_have_later_same_round_turns=all(m['later_selected_turns_same_round']>0 for m in members)))
check('peak_36_previous_exact_chain',len(hist),bad_prev)
check('peak_36_member_question_admission_identity',len(hist),bad_id)
check('peak_36_upstream_member_alignment',sum(len(x['members']) for x in details),bad_member)
check('peak_36_duty_close_equals_r_boundary',len(hist),bad_duty)
check('peak_36_no_future_member_knowledge',len(hist),bad_knowledge)
check('peak_36_cross_life_same_concrete_members',36,[ls for ls in all_sigs.values() if len(ls)>1 and any(l in roster for l in ls)])
boundaries=[]
for label,j in [('before_peak',14037),('first_peak',14038),('last_peak',14097),('after_peak',14098)]:
 at=axis[j];born={l for l,gs in bylife.items() if gs[0]['known']<=at};ended={l for l in born if num(parts[latest(l,at)['p']]['participationDutyClosed'])==1};native=born-ended
 resp={l for l in born if at<=num(bylife[l][0]['row']['groupRevisionEnd'])}
 views=[latest(l,at) for l in born];revs=sum(sum(x['known']<=at for x in gs) for gs in bylife.values())
 boundaries.append(dict(label=label,time=times[j],uti=at,created_lives=len(born),ended_duty_lives=len(ended),current_duty_open_lives=len(native),closed_interval_responsibility=len(resp),total_revision_occurrences=revs,updates_excluding_create=revs-len(born),current_public_latest_lives=len(born),internal_active_source_reconstruction=len(native),internal_active_trace_measured=False,current_life_ids=sorted(native),closed_interval_only_life_ids=sorted(resp-native),observation_counts=dict(Counter(latest(l,at)['row']['groupObservation_name'] for l in native))))
snaps=[];lastset=None
for j in range(14038,14098):
 at=axis[j];resp={l for l,gs in bylife.items() if gs[0]['known']<=at<=num(gs[0]['row']['groupRevisionEnd'])};active={l for l in resp if num(parts[latest(l,at)['p']]['participationDutyClosed'])==0}
 snaps.append(dict(index=j,time=times[j],uti=at,responsibility_lives=sorted(resp),source_reconstructed_active_lives=sorted(active),responsibility_count=len(resp),source_reconstructed_active_count=len(active),roster_unchanged=resp==set(roster),public_states=dict(Counter(latest(l,at)['row']['groupObservation_name'] for l in active))))
waves=defaultdict(list)
for x in details:waves[x['current_question']['anchor']].append(x['case_id'])
summary=dict(peak=peak['peak_runs'][0],first_peak_lives=36,peak_union_lives=len(set(l for s in snaps for l in s['responsibility_lives'])),same_36_throughout=all(s['roster_unchanged'] for s in snaps),source_reconstructed_active_counts=dict(Counter(s['source_reconstructed_active_count'] for s in snaps)),distinct_question_anchors=len(waves),waves=[dict(anchor=a,actual_time=ts(a),case_ids=ls) for a,ls in sorted(waves.items())],directions=dict(Counter(m['direction'] for x in details for m in x['members'])),all_current_pairs_supported=all(all(v=='CoordinateSupports' for v in q['verdicts'].values()) for x in details for q in x['required_pairs']),age_minmax=[min(x['age_open_minutes'] for x in details),max(x['age_open_minutes'] for x in details)],all_36_duty_close_at_r=all(x['first_duty_close_known']==x['current_question']['revision_end'] for x in details),all_36_members_have_later_same_round_turns=sum(all(m['later_selected_turns_same_round']>0 for m in x['members']) for x in details),subsumed_case_ids=[x['case_id'] for x in details if x['observation']=='Subsumed'],native_internal_active_trace='NOT_EXPOSED; SOURCE_RULE_RECONSTRUCTION, not an observed table',checks=checks,boundary_reconciliation=boundaries)
assert all(x['conflicts']==0 for x in checks)
save('Peak36LifeDetails.json',dict(finding_id='F-LIFE-PEAK-CONCURRENCY',peak_time=ts(u),peak_uti=u,source_refs=[pro_ref('readback/tables/'+n+'.csv') for n in tables],life_details=details))
csvout('analysis/peak_36_roster.csv',flat)
save('Peak36RevisionHistory.json',dict(revisions=hist,count=len(hist)))
save('PeakWindowReconciliation.json',dict(snapshots=snaps,boundary_reconciliation=boundaries,internal_reconstruction_assumptions=['exact current source advanceCandidates retains every wanted prior row until r or scopeEnded','normal KLine source frameEnded=False, no scope termination or Clock correction patches','dutyClosed=1 at u>=r; same-tick final row precedes internal retirement'],no_internal_trace_claim=True))
save('Peak36Summary.json',summary)
print(json.dumps({k:v for k,v in summary.items() if k not in ['waves','boundary_reconciliation']},ensure_ascii=False))
for r in flat:print(json.dumps(r,ensure_ascii=False))
