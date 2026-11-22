"""核原S2合同、冻结不变和原始数据追溯；不重跑Feature/全量行为统计。"""
from common import *
from itertools import combinations
from collections import Counter
import uuid

def load(name): return json.loads((ROOT/name).read_text())
def frozen(name): return read_json(FROZEN, f'{PREFIX}/professional/D013/{name}')
fz=frozen('FrozenExpectationSet.json'); cs=frozen('CaseReviewSet.json')
cb=load('ScenarioProcessCasebook.json'); pk=load('EvidenceComparisonPackage.json')['packages']
pf=load('ScenarioEvidencePreflight.json'); browser=load('S2_BROWSER_REVIEW.json')
mapping,formal=formal_all(); data={k:v['data'] for k,v in formal.items()}
assert len(cs['cases'])==len(cb['cases'])==len(pk)==len(pf['cases'])==7
assert [c['case_id'] for c in cs['cases']]==[c['case_id'] for c in cb['cases']]==fz['case_ids']
assert all(c['admissible_for_comparison'] and c['versions_match'] for c in pf['cases'])
assert len(browser['windows'])==12 and browser['page_errors']==browser['console']==browser['external_requests']==[]
assert browser['source_html_unchanged'] and not browser['source_data_values_edited']
assert sha(Path(browser['html']).read_bytes())==browser['html_sha256']==pf['accepted_html_sha256']
assert sorted(load('VISUAL_REVIEW_NOTES.json')['actually_viewed_screenshots'])==sorted(w['screenshot'] for w in browser['windows'])
for w in browser['windows']:
    assert sha((ROOT/w['screenshot']).read_bytes())==w['screenshot_sha256']
    idx=w['window']['group_index']
    if idx is not None:
        assert w['view']['life']==data['p1531']['life'][idx]
        assert w['view']['revision']==data['p1531']['revision'][idx]
        assert w['view']['detail_matches']['matches']
    else:
        assert w['view']['life'] is None and w['view']['parent'] is None
for f in frozen('FREEZE_MANIFEST.json')['files']:
    original=git_bytes(FROZEN,f"{PREFIX}/professional/D013/{f['file']}")
    assert sha(original)==f['sha256']
    assert original==(RECORD/PREFIX/'professional/D013'/f['file']).read_bytes()
    assert original==(BASE/'artifacts'/RUN/'D013'/f['file']).read_bytes()
assert sha(git_bytes(FROZEN,f'{PREFIX}/professional/D013/FrozenExpectationSet.json'))=='ae54fa64560dbb2e36a87b1913706d096bce00e72b9282abf36b7d6fefce5568'
states={'SUPPORTS','COUNTERS','MISSING','AMBIGUOUS','NOT_APPLICABLE','PENDING'}
checks=[];native_views=0;bars_verified=0;previous_links=0
for case,package,e in zip(cb['cases'],pk,fz['expectations']):
    cid=case['case_id']; rb=load(f'case_readback/{cid}.json')
    assert case['expected_feature_process']==e['expected_feature_process']
    assert case['expected_intermediate_decisions']==e['expected_intermediate_decisions']
    assert package['business_intent']==package['frozen_statement_verbatim']==e['statement']
    assert package['expectation_id']==e['expectation_id'] and package['expectation_version']==1
    assert package['parameter_version']==cb['parameter_version']==cs['parameter_version']
    assert package['data_binding']['feature_ref']==cs['feature_ref']
    assert all(case[k] for k in ['raw_market_process','expected_feature_process','observed_feature_process','process_alignment'])
    assert [a['expected_verbatim'] for a in case['process_alignment']]==e['expected_feature_process']
    assert len(case['process_alignment'])==3 and all(a['evidence_status'] in states for a in case['process_alignment'])
    assert not case['earliest_business_divergence']['located'] and case['earliest_business_divergence']['reason']
    assert package==load(case['evidence_comparison_package'])
    assert all(k in package for k in ['comparison_id','business_intent','expectation_id','expectation_version','scenario_id',
        'data_binding','time_basis','parameter_version','evidence_items','judgment','applicability_boundary','confidence','next_action'])
    for item in package['evidence_items']:
        assert all(k in item for k in ['evidence_id','source','location','actual_time','confirm_time','evidence_status',
            'observation','interpretation','alternative_explanations','data_quality'])
        assert item['evidence_status'] in states
    for layer in rb['raw_market_readback']:
        original=data[layer['source_id']]
        for b in layer['actual_bar_rows']:
            j=b['row_index']; bars_verified+=1
            assert all(b[k]==original[k][j] for k in ['ts','open','high','low','close','volume'])
    lives=set(g['life'] for g in rb['observed_public_group_process'])
    all_indices=[i for i,life in enumerate(data['p1531']['life']) if life in lives]
    assert all_indices==[g['row_index'] for g in rb['observed_public_group_process']]
    groups_by_revision={g['revision']:g for g in rb['observed_public_group_process']}
    for g in rb['observed_public_group_process']:
        idx=g['row_index'];native_views+=1
        original=json.loads(data['p1531']['raw'][idx]);q=g['group']
        assert q==original['group'] and data['p1531']['life'][idx]==g['life']
        assert data['p1531']['revision'][idx]==g['revision']
        assert [q[k] for k in ['timestamp','occurrence','record_id','child_id_2']]==g['full_parent']
        assert q['groupKnownFrom']>=max(m['memberKnownFrom'] for m in g['members'])
        assert q['groupOriginalAnchor']==q['groupAnchor']
        assert q['groupOriginalDeadline']==q['groupDeadline']==q['groupOriginalAnchor']+480000
        assert q['groupOriginalRevisionEnd']==q['groupRevisionEnd']==q['groupDeadline']+3600
        assert len(g['required'])==len(list(combinations(g['members'],2)))
        for relation in g['required']:
            members=[m for m in g['members'] if m['turn_reference_life'].endswith(relation['left']) or m['turn_reference_life'].endswith(relation['right'])]
            assert len(members)==2
            assert [d['distanceValue'] for d in relation['distances']]==[abs(members[0]['memberActual']-members[1]['memberActual'])]
        for child_name in ['previous','covered_by','overlaps','member_P','member_P_clock','participation']:
            for row in g[child_name]:
                assert [row[k] for k in ['timestamp','occurrence','record_id','child_id_2']]==g['full_parent']
        for p in g['previous']:
            life=str(uuid.UUID(int=(p['referenceLife_idHigh']<<64)|p['referenceLife_idLow']))
            revision=str(uuid.UUID(int=(p['referenceRevision_idHigh']<<64)|p['referenceRevision_idLow']))
            assert life==g['life'] and revision in groups_by_revision
            assert groups_by_revision[revision]['row_index']<idx
            previous_links+=1
        for part in g['participation']:
            assert part['participationAdmission_definitionLife']==g['life']
            assert part['participationCandidate_definitionRevision']==g['revision']
            assert part['participationQuestionAnchor']==q['groupOriginalAnchor']
            assert part['participationQuestionDeadline']==part['participationDeadline']==q['groupOriginalDeadline']
            assert part['participationQuestionRevisionEnd']==part['participationRevisionEnd']==q['groupOriginalRevisionEnd']
            assert part['participationHandoffEnd']==q['groupRevisionEnd']+10800
    for life in lives:
        gs=[g for g in rb['observed_public_group_process'] if g['life']==life]
        assert gs[-1]['group']['groupClosed']==1
        assert all(p['participationDutyClosed']==1 for p in gs[-1]['participation'])
    checks.append(dict(case_id=cid,contract=True,expectation_unchanged=True,raw_source_values=True,
        public_identity_timing_relations=True,all_frozen_life_revisions_read=True,missing_not_counter=True))
# 对照结论依赖的关键原值：从原始CDS重新读取，避免只自检生成结构。
g0=json.loads(data['p1531']['raw'][0]);g8=json.loads(data['p1531']['raw'][8]);g15=json.loads(data['p1531']['raw'][15])
assert g0['group']['groupLocalBasis_name']==g8['group']['groupLocalBasis_name']==g15['group']['groupLocalBasis_name']=='Incomplete'
assert g8['group']['groupObservation_name']=='ClosedInsufficient' and g8['group']['groupCoverageIncomplete']==0
assert not g0['children']['occurrences_groupMembers_memberP']
assert all(m['memberDirection_name']==m['memberType_name']=='Unavailable' for m in g0['children']['occurrences_groupMembers'])
g44=json.loads(data['p1531']['raw'][44])
assert g44['children']['occurrences_groupRequired_pairDistance'][0]['distanceValue']==1200
assert g44['children']['occurrences_groupRequired'][0]['pairTime_requiredVerdict_name']=='CoordinateSupports'
c1=load('case_readback/F800-S1-C001.json');cover=next(g for g in c1['observed_public_group_process'] if g['row_index']==4)
assert str(uuid.UUID(int=(cover['covered_by'][0]['idHigh']<<64)|cover['covered_by'][0]['idLow']))=='8f776a81-a7bc-4c93-965b-0f1534b574c4'
c2=load('case_readback/F800-S1-C002.json'); assert all(not x.get('within_1200',[]) for x in c2['specific_public_lookups'])
assert c2['specific_public_lookups'][-1]['matching_group_rows']==[]
c5=load('case_readback/F800-S1-C005.json'); assert c5['specific_public_lookups'][0]['actual_distance']==1800
assert not c5['specific_public_lookups'][0]['matching_group_rows']
g1468=json.loads(data['p1531']['raw'][1468])['group']
assert g1468['groupKnownFrom']-g1468['groupOriginalAnchor']==199800
assert g1468['groupOriginalAnchor']==96674999
c7=load('case_readback/F800-S1-C007.json'); assert all(not x['matching_selected'] for x in c7['specific_public_lookups'])
for g in load('ObservationGapRequests.json')['requests']:
    assert all(k in g for k in ['gap_id','case_id','missing_field_or_view','why_needed','return_to'])
    assert g['return_to']=='OBSERVATION_MATERIAL_PREPARATION'
assert load('EvidenceInducedCandidates.json')['candidates']==[]
assert load('ScenarioFindingCandidates.json')['candidates']==load('DiscrepancyQueue.json')['queue']==[]
assert len(load('ScenarioFindingCandidates.json')['route_assessments'])==7
assert pk[-1]['judgment']['primary_state']=='NOT_APPLICABLE'
assert all(p['judgment']['score'] is None and p['judgment']['counters']==[] for p in pk)
assert load('S2_HANDOFF.json')['workers']==[]
coverage=frozen('CaseTypeCoverage.json')
assert load('ActualCaseCoverage.json')['universal_coverage_claim'] is False
save('VALIDATION.json',dict(checked_at=now(),checks_passed=True,checks=checks,
    frozen_v1_unchanged=True,frozen_manifest_files=len(frozen('FREEZE_MANIFEST.json')['files']),
    exact_frozen_sha256=sha(git_bytes(FROZEN,f'{PREFIX}/professional/D013/FrozenExpectationSet.json')),
    formal_files_checked=len(mapping['formal_files']),raw_bar_samples_compared=bars_verified,
    exact_native_group_views=native_views,previous_links_verified=previous_links,
    actual_browser_windows=12,all_7_native_package_contracts_pass=True,
    public_known_never_before_member_known=True,all_frozen_lives_finitely_closed=True,
    all_missing_materials_routed=True,all_7_skill3_routes_assessed=True,
    source_html_unchanged=True,no_Feature_run_or_rebuild=True,
    validation_boundary='这是原S2合同与已读原值的追溯核验，不能把它当全量业务真值或内部不可见轨迹的证明。',
    evidence_states=dict(Counter(x['evidence_status'] for p in pk for x in p['evidence_items']))))
print(json.dumps(dict(checks_passed=True,cases=7,packages=7,exact_views=native_views,
    raw_bar_samples=bars_verified,previous_links=previous_links,formal_files=21),ensure_ascii=False))
