from common import *
from collections import Counter,defaultdict
from decimal import Decimal
num=lambda s:int(Decimal(s))
detail=json.loads((ROOT/'Peak36LifeDetails.json').read_text())['life_details']
history=json.loads((ROOT/'Peak36RevisionHistory.json').read_text())['revisions']
idmap={x['life']:x['case_id'] for x in detail}
actualkeys=defaultdict(list);pairs=[]
for x in detail:
 key=tuple((m['object'],m['actual'],m['direction']) for m in x['members']);actualkeys[key].append(x['case_id'])
 for target in x['covered_by']:
  other=next(y for y in detail if y['life']==target)
  left={(m['object'],m['turn_life']) for m in x['members']};right={(m['object'],m['turn_life']) for m in other['members']}
  assert left<right and x['current_question']==other['current_question']
  pairs.append(dict(subset=x['case_id'],superset=other['case_id'],subset_life=x['life'],superset_life=target,shared_members=len(left),added_members=[m['locator'] for m in other['members'] if (m['object'],m['turn_life']) not in left],same_question=True,different_members=True,subset_admission=x['admission_time'],superset_admission=other['admission_time'],both_supported=True,subset_duty_still_open=True))
removed_old=[x['case_id'] for x in detail if all(m['later_selected_turns_same_round']>0 for m in x['members'])]
no_cover=[x['case_id'] for x in detail if not x['covered_by']]
not_old=[x['case_id'] for x in detail if x['case_id'] not in removed_old]
smallK=[x['case_id'] for x in detail if x['admission_actual_age_open_minutes']<=30]
at6=[x['case_id'] for x in detail if x['case_id'] in smallK and x['age_open_minutes']<60]
summary=dict(scope='DIAGNOSTIC_ONLY_FIXED_EXISTING_ROSTER_PROJECTIONS; no Feature rerun or proposed accepted rule',peak_time='2021-11-10 14:25:00',baseline_case_ids=[x['case_id'] for x in detail],baseline_count=36,maximal_only=dict(remaining_case_ids=no_cover,count=len(no_cover),removed_subset_pairs=pairs,interpretation='9个Subset有不同成员和更早准入史；可减少当前最大解释显示，但不能由此决定取消其修订责任'),all_members_have_newer_same_round_projection=dict(removed_case_ids=removed_old,remaining_case_ids=not_old,count=len(not_old),interpretation='仅揭示32个Life已跨后续选中转折仍保留；新Turn不等于旧事实被撤回，这不是合法结束规则的证明'),both_projections=dict(case_ids=[x for x in not_old if x in no_cover],count=len([x for x in not_old if x in no_cover])),K6_fixed_admission_and_expiry_algebra=dict(original_roster_first_admission_eligible=smallK,eligible_count=len(smallK),remaining_at_peak=at6,count=len(at6),excluded_at_admission_count=36-len(smallK),formula='firstKnown<=a+6Δ and peak<a+12Δ; 6Δ=30open minutes; existing K800 a/member identities frozen',not_formal_counterfactual='改K后真实枚举/发行/UUID会变；这里只比较原36的门槛，不声称K6重跑结果。'),duplicate_same_symbol_actual_direction_groups=[v for v in actualkeys.values() if len(v)>1],all_peak_members_confirmed=all(m['status']=='ConfirmedMember' for x in detail for m in x['members']),all_peak_pairs_supported=all(all(v=='CoordinateSupports' for v in p['verdicts'].values()) for x in detail for p in x['required_pairs']),all_peak_observation_deadlines_future=all(x['remaining_deadline_open_minutes']>0 for x in detail),all_peak36_revision_ends_dutyclose_and_stop=all(x['first_duty_close_known']==x['current_question']['revision_end']==x['final_known'] for x in detail),candidate_age_range_minutes=[min(x['age_open_minutes'] for x in detail),max(x['age_open_minutes'] for x in detail)],all_question_durations_exact=all(x['current_question']['deadline']-x['current_question']['anchor']==480000 and x['current_question']['revision_end']-x['current_question']['deadline']==3600 and x['current_question']['handoff_end']-x['current_question']['revision_end']==10800 for x in detail))
assert not summary['duplicate_same_symbol_actual_direction_groups']
assert all(summary[k] for k in ['all_peak_members_confirmed','all_peak_pairs_supported','all_peak_observation_deadlines_future','all_peak36_revision_ends_dutyclose_and_stop','all_question_durations_exact'])
save('DiscriminatingCheckResults.json',summary)
# 补充统计责任代码的精确原件，不更改旧G。
paths=['perform_global_profile.py','generate_report.py']
checks=[]
for name in paths:
 raw=git_bytes(U,PREFIX+'/professional/D008/'+name)
 assert raw==(D008/name).read_bytes()
 dest=ROOT/'source/D008'/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
 checks.append(dict(source_ref=pro_ref(name),sha256=sha(raw),local_copy=str(dest)))
save('STATISTIC_SOURCE_AUDIT.json',dict(files=checks,original_formula='birth +1 before equal-time expiry -1; closed interval [firstKnown,min(r,sampleEnd)]',source_location='perform_global_profile.py:563-570',effect='last peak sample at r includes final responsibility event; after-tick native current already35; numeric maximum36 remains'))
print(json.dumps(summary,ensure_ascii=False))
