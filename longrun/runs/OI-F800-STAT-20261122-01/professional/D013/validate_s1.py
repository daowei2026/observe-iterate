"""核S1原生输出合同、实际材料定位和冻结完整性；不是新的专业Gate。"""
from common import *
import sys
import uuid
from datetime import datetime

draft='--draft' in sys.argv
case_file='draft/CaseReviewSet.READY.json' if draft else 'CaseReviewSet.json'
exp_file='draft/ScenarioExpectationSet.READY.json' if draft else 'ScenarioExpectationSet.json'
cs=json.loads((ROOT/case_file).read_text())
es=json.loads((ROOT/exp_file).read_text())
expected_status='READY_FOR_EXPECTATION' if draft else 'FROZEN_FOR_COMPARISON'
case_keys={'case_id','status','case_type','symbol','start_time','end_time','related_reasonableness_units',
           'primary_judgment_target','selection_basis','raw_market_description','output_presence',
           'required_intermediate_fields','source_refs'}
exp_keys={'expectation_id','version','status','case_id','statement','origin','source_ref','applicable_conditions',
          'non_applicable_conditions','expected_feature_process','expected_intermediate_decisions',
          'falsifier_or_counterevidence','ambiguous_conditions','explicit_non_goals','evidence_needed',
          'known_unknowns','confidence','owner_decision_required'}
types={'CLEAR_POSITIVE','CLEAR_NEGATIVE','OUTPUT_FALSE_POSITIVE_CANDIDATE','POTENTIAL_FALSE_NEGATIVE',
       'PARAMETER_BOUNDARY','OUTSIDE_CURRENT_COVERAGE'}
assert cs['status']==es['status']==expected_status
assert cs['parameter_version']==es['parameter_version']=='b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3'
assert cs['feature_ref']['frp']=='39f02ec4548e68ba8dbd30061afc870546000994'
audit=json.loads((ROOT/'SOURCE_REF_AUDIT.json').read_text())
input_refs={r['source_ref'] for r in audit['exact_sources']}
assert cs['observation_material_ref'] in input_refs
assert not es['evidence_comparison_performed']
cases={c['case_id']:c for c in cs['cases']}
assert len(cases)==len(cs['cases']) and cases
assert len({e['expectation_id'] for e in es['expectations']})==len(es['expectations'])
assert {e['case_id'] for e in es['expectations']}==set(cases)
for c in cases.values():
    assert case_keys<=set(c), c['case_id']
    assert c['case_type'] in types and c['status']==expected_status
    assert datetime.fromisoformat(c['start_time'])<datetime.fromisoformat(c['end_time'])
    assert all(c[k] for k in ('selection_basis','primary_judgment_target','raw_market_description','required_intermediate_fields','source_refs'))
    assert all(x in input_refs for x in c['source_refs']),c['case_id']
    assert c['selection_is_not_evidence_verdict'] is True
    assert all((ROOT/p).is_file() for p in c['viewport_refs'])
for e in es['expectations']:
    assert exp_keys<=set(e),e['expectation_id']
    assert e['origin'] in {'OWNER_EXPLICIT','BUSINESS_INFERRED'}
    assert e['status']==expected_status and e['source_ref'] in input_refs
    assert len(e['expected_feature_process'])>=3 and e['support_conditions'] and e['falsifier_or_counterevidence']
    assert e['ambiguous_conditions'] and e['derivation_reason'] and e['evidence_needed']
    if e['origin']=='OWNER_EXPLICIT':
        assert e['source_ref']==ref(LOCKED,'task-inputs/wall-f-parallel-closure-20261122/F_BASE_RUN_INPUT.md')
        assert '2Delta' in e['statement'] and '800' in e['statement']
coverage=json.loads((ROOT/'CaseTypeCoverage.json').read_text())
assert {t['case_type'] for t in coverage['types']}==types
for t in coverage['types']:
    if t['status']=='NO_CASE_FOUND':assert not t['case_ids'] and t['reason'] and t['scope_limit']
    else:
        assert t['status']=='HAS_QUALIFIED_CASE' and t['case_ids']
        assert all(cases[c]['case_type']==t['case_type'] for c in t['case_ids'])

# 从准确正式原件核本S1的行号/身份/原值定位；不重建图或运行Feature。
mapping,formal=formal_all()
group_data=formal['p1531']['data']
group_raw=[json.loads(s) for s in group_data['raw']]
loc=json.loads((ROOT/'CaseMaterialIndex.json').read_text())
assert {x['case_id'] for x in loc['cases']}==set(cases)
selected_ids=dict(rb='p1098',hc='p1226',i='p1354')
all_selected={s:[json.loads(x) for x in formal[k]['data']['raw']] for s,k in selected_ids.items()}
public_member_sets=[]
for row in group_raw:
    public_member_sets.append({m['memberObject']+'/'+ '/'.join(m['memberTurn_referenceLife_idText'].split('/')[-2:])
        for m in row['children']['occurrences_groupMembers']})
located_group_rows=0;located_turn_rows=0
for x in loc['cases']:
    c=cases[x['case_id']]
    assert x['data_stage']=='construction_snapshot'
    for g in x['group_rows']:
        i=g['index'];p=group_raw[i]['group']
        assert group_data['parent'][i]==g['parent']
        assert group_data['life'][i]==g['life'] and group_data['revision'][i]==g['revision']
        for field,value in [('Life',g['life']),('Revision',g['revision'])]:
            prefix='groupReference_reference'+field
            assert str(uuid.UUID(int=(p[prefix+'_idHigh']<<64)|p[prefix+'_idLow']))==value
        assert datetime.fromisoformat(c['start_time'])<=datetime.fromisoformat(g['timestamp'])<=datetime.fromisoformat(c['end_time'])
        assert g['known']==p['groupKnownFrom'] and g['anchor']==p['__uti_groupAnchor']
        assert g['deadline']==p['__uti_groupDeadline'] and g['revision_end']==p['__uti_groupRevisionEnd']
        assert json.loads(g['parent'])==[p[k] for k in ('timestamp','occurrence','record_id','child_id_2')]
        located_group_rows+=1
    for t in x['independent_selected_rows']:
        raw=all_selected[t['symbol']][t['row_index']]
        assert raw['turn_id']==t['turn_id']
        for out,original in [('actual','actual'),('geometric_confirmation','confirmation'),('selected_known','known'),('point_known','raw_known')]:
            assert t[out]==raw[original]
        assert t['actual_time']==raw['actual_ts'] and t['selected_known_time']==raw['known_ts']
        located_turn_rows+=1

# 关键区分检查：不用图片或K线x宽度推native时间；不填未发行pair实际原因。
neg='i/value1/72049199'
assert not any(neg in m for m in public_member_sets)
inside=next(x for x in loc['cases'] if x['case_id']=='F800-S1-C004')['independent_selected_rows']
assert abs(inside[0]['actual']-inside[1]['actual'])==1200
outside={'hc/value1/73238399','i/value1/73232999'}
assert not any(outside<=m for m in public_member_sets)
out=next(x for x in loc['cases'] if x['case_id']=='F800-S1-C005')['independent_selected_rows']
assert abs(out[0]['actual']-out[1]['actual'])==1800
for symbol in ('rb','i'):
    assert not any(r['actual_ts'][:16]=='2022-05-25 15:00' for r in all_selected[symbol])
raw_pool=json.loads((ROOT/'CandidateCasePool.v1.json').read_text())
assert any(x['discovery_route']=='RAW_MARKET_INDEPENDENT' for x in raw_pool['candidates'])
assert json.loads((ROOT/'OpenQuestions.json').read_text())['original_questions_unchanged']==read_json(U,f'{PREFIX}/professional/D008/ScenarioQuestionQueue.json')
assert json.loads((ROOT/'ObservationGapRequests.json').read_text())['requests']==[]
browser=[]
for name in ('BROWSER_SELECTION.json','BROWSER_ADDITIONAL_SELECTION.json'):
    b=json.loads((ROOT/name).read_text());assert b['html_unchanged'] and not b['page_errors'] and not b['console'] and not b['external_requests']
    assert b['html_sha256']==mapping['accepted_html_sha256']
    for w in b['windows']:
        assert sha((ROOT/w['screenshot']).read_bytes())==w['screenshot_sha256']
        if w['window']['group_index'] is not None:
            v=w['view'];i=v['group_index']
            assert v['life']==group_data['life'][i] and v['revision']==group_data['revision'][i]
            assert v['detail']['selected']==i and v['detail']['detail_contains_revision']
    browser.extend(b['windows'])
assert (ROOT/'BROWSING_REVIEW.md').is_file()
if not draft:
    frozen=json.loads((ROOT/'FrozenExpectationSet.json').read_text())
    assert frozen['expectations']==es['expectations']
    assert frozen['case_ids']==list(cases) and frozen['status']==expected_status
    fm=json.loads((ROOT/'FREEZE_MANIFEST.json').read_text())
    for f in fm['files']:assert sha((ROOT/f['file']).read_bytes())==f['sha256'], f['file']
    assert len(fm['case_ids'])==len(cases)
result=dict(checked_at=now(),mode='draft' if draft else 'frozen',checks_passed=True,
    checks=['原S1必需字段/六类覆盖','逐例过程/适用/支持反证/未决/来源','同版准确材料引用',
            '正式数据压缩/JSON身份及原行/父坐标/无损exact','独立上游时间分列/边界内外/无对应尺度位置',
            '实际浏览视窗和exact明细/截图身份','原问题未篡改及NOT_EXPOSED边界',
            *([] if draft else ['冻结文件哈希及Skill2兼容汇总'])],
    cases=len(cases),expectations=len(es['expectations']),located_group_rows=located_group_rows,
    located_selected_rows=located_turn_rows,actual_browser_windows=len(browser),formal_files_checked=len(formal),
    no_S2_verdict=True,no_Feature_run_or_rebuild=True,professional_gate_added=False)
save('DRAFT_VALIDATION.json' if draft else 'VALIDATION.json',result)
print(json.dumps(result,ensure_ascii=False))
