"""S2逐冻结案例材料预检及读取；不是重做S1或正式图数据导出。"""
from common import *
from datetime import datetime

def frozen(name):return read_json(FROZEN,f'{PREFIX}/professional/D013/{name}')
cs=frozen('CaseReviewSet.json');es=frozen('ScenarioExpectationSet.json');fz=frozen('FrozenExpectationSet.json')
frozen_bytes=git_bytes(FROZEN,f'{PREFIX}/professional/D013/FrozenExpectationSet.json')
assert sha(frozen_bytes)=='ae54fa64560dbb2e36a87b1913706d096bce00e72b9282abf36b7d6fefce5568'
assert cs['status']==es['status']==fz['status']=='FROZEN_FOR_COMPARISON'
assert fz['expectations']==es['expectations']
assert sha(git_bytes(FROZEN,f'{PREFIX}/professional/D013/CaseReviewSet.json'))==fz['case_review_set_sha256']
assert sha(git_bytes(FROZEN,f'{PREFIX}/professional/D013/ScenarioExpectationSet.json'))==fz['scenario_expectation_set_sha256']
frozen_receipts=[]
for row in frozen('FREEZE_MANIFEST.json')['files']:
    path=f"{PREFIX}/professional/D013/{row['file']}";raw=git_bytes(FROZEN,path)
    assert sha(raw)==row['sha256'] and raw==(RECORD/path).read_bytes()
    assert raw==(BASE/'artifacts'/RUN/'D013'/row['file']).read_bytes()
    frozen_receipts.append(dict(file=row['file'],sha256=sha(raw),local_and_published_equal=True))
save('FROZEN_INPUT_READBACK.json',dict(frozen_ref=pro_ref('D013','FrozenExpectationSet.json',FROZEN),
    frozen_sha256=sha(frozen_bytes),verified_at=now(),version=1,files=frozen_receipts,all_equal=True,
    policy='本D不改冻结v1；过程对照的新候选另交S1，不回写。'))
mapping,all_data=formal_all();data={k:v['data'] for k,v in all_data.items()}
m=read_json(MATERIAL,f'{PREFIX}/professional/D012/ObservationMaterialPackage.json')
u=read_json(U,f'{PREFIX}/professional/D008/CurrentFeatureUnderstandingPackage.json')
assert m['status']=='DATA_READY' and m['parameter_version']==cs['parameter_version']==es['parameter_version']==u['current_applicability']['parameter_version']
assert m['feature_ref']['frp']==cs['feature_ref']['frp']==u['current_applicability']['current_code'].split('@')[1]
assert read_json(U,f'{PREFIX}/professional/D008/GlobalProfileGate.json')['status']=='PASS_TO_SCENARIO_REVIEW'
prices=dict(rb='p1040',hc='p1168',i='p1296')
turns=dict(rb='p1098',hc='p1226',i='p1354')
selected={s:[json.loads(raw) for raw in data[k]['raw']] for s,k in turns.items()}
group_raw=[json.loads(raw) for raw in data['p1531']['raw']]
index=frozen('CaseMaterialIndex.json');loc={c['case_id']:c for c in index['cases']}
cases=[]
for c in cs['cases']:
    start=datetime.fromisoformat(c['start_time']);end=datetime.fromisoformat(c['end_time'])
    raw_layers=[]
    for symbol in c['symbol']:
        sid=prices[symbol];d=data[sid]
        rows=[i for i,t in enumerate(d['ts']) if start<=datetime.fromisoformat(t)<=end]
        assert rows
        missing=[dict(row_index=i,time=d['ts'][i],value=d['close'][i]) for i in rows if isinstance(d['close'][i],dict)]
        order=all(datetime.fromisoformat(d['ts'][i])<datetime.fromisoformat(d['ts'][j]) for i,j in zip(rows,rows[1:]))
        assert order
        raw_layers.append(dict(symbol=symbol,source_id=sid,source_ref=pro_ref('D012',f'formal_data/source_{sid}.json.gz'),
            columns=list(d),row_start=rows[0],row_end=rows[-1],rows=len(rows),
            first_time=d['ts'][rows[0]],last_time=d['ts'][rows[-1]],nonfinite_close=missing,
            timestamps_strictly_increasing=True,duplicate_times=0,
            time_basis='ts=原bar时刻；x为图元中点，绝不作native actual/confirm'))
    resolved_turns=[]
    for t in loc[c['case_id']]['independent_selected_rows']:
        raw=selected[t['symbol']][t['row_index']]
        assert raw['turn_id']==t['turn_id'] and raw['actual']==t['actual'] and raw['known']==t['selected_known']
        resolved_turns.append(dict(turn_id=t['turn_id'],row_index=t['row_index'],source_id=turns[t['symbol']],
            actual=raw['actual'],actual_time=raw['actual_ts'],geometric_confirm=raw['confirmation'],geometric_confirm_time=raw['confirmation_ts'],
            selected_known=raw['known'],selected_known_time=raw['known_ts'],point_known=raw['raw_known']))
    resolved_groups=[]
    for row in loc[c['case_id']]['group_rows']:
        i=row['index'];g=group_raw[i]['group']
        assert data['p1531']['life'][i]==row['life'] and data['p1531']['revision'][i]==row['revision']
        assert data['p1531']['parent'][i]==row['parent']
        assert start<=datetime.fromisoformat(g['timestamp'])<=end
        resolved_groups.append(dict(row_index=i,life=row['life'],revision=row['revision'],parent=row['parent'],timestamp=g['timestamp']))
    cases.append(dict(case_id=c['case_id'],expectation_id=next(e['expectation_id'] for e in es['expectations'] if e['case_id']==c['case_id']),
        frozen_version=1,case_type=c['case_type'],symbols=c['symbol'],start_time=c['start_time'],end_time=c['end_time'],
        parameter_version=cs['parameter_version'],versions_match=True,same_accepted_run=True,
        calendar='night_end_at_2300',timezone='Asia/Shanghai',sampling='5m',
        raw_layers=raw_layers,resolved_independent_turns=resolved_turns,resolved_group_exact_rows=resolved_groups,
        stage='construction_snapshot',missing_required_input_files=[],
        known_unexposed=['内部逐tick材料/未成组pair/首阻断/原生coverage区间；不由代码补值。'],
        revision_policy='同Life按知识轴逐exact展开；groupPrevious/parent保留，稀疏未发行拍不是零状态。',
        admissible_for_comparison=True,qualification_note='可对照可读声明；不充分历史、native缺口及价值歧义仍逐证据单列，不等于所有问题已可判。'))
save('ScenarioEvidencePreflight.json',dict(preflight_id='F800-S2-D014-PREFLIGHT-v1',checked_at=now(),
    frozen_set_ref=pro_ref('D013','FrozenExpectationSet.json',FROZEN),frozen_sha256=sha(frozen_bytes),
    feature_ref=cs['feature_ref'],parameter_version=cs['parameter_version'],observation_material_ref=cs['observation_material_ref'],
    accepted_html_sha256=m['final_html_sha256'],formal_stage='construction_snapshot',cases=cases,
    material_limits=m['known_limits'],understanding_limits=u['unconfirmed_items'],
    frozen_cases_only=True,workers=[]))
print(json.dumps(dict(cases=len(cases),frozen_input_sha256=sha(frozen_bytes),formal_files=21,
    per_case=[dict(case_id=c['case_id'],raw_bars=[x['rows'] for x in c['raw_layers']],
        missing_close=[len(x['nonfinite_close']) for x in c['raw_layers']],groups=len(c['resolved_group_exact_rows'])) for c in cases]),ensure_ascii=False))
