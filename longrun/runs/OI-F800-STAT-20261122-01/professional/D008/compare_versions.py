"""完整新旧公开结果比较：不依赖跨Run随机UUID相等，不合成Feature运行结果。"""
from pathlib import Path
from collections import Counter, defaultdict
from bisect import bisect_right
from hashlib import sha256
import csv
import json
import sys

ROOT = Path(__file__).resolve().parent
BASELINE = sys.argv[1] if len(sys.argv)>1 else 'D005'
assert BASELINE in ('D005','D002')
OLD = ROOT.parent / BASELINE
OUT = ROOT / ('comparison' if BASELINE=='D005' else 'comparison_ac')
OUT.mkdir(exist_ok=True)

def load(root, name): return json.loads((root / name).read_text())
def rows(root, name):
    with (root / name).open(encoding='utf-8-sig', newline='') as f: return list(csv.DictReader(f))
def write(name, data):
    data = list(data)
    fields = list(dict.fromkeys(k for r in data for k in r)) or ['empty']
    with (OUT / (name + '.csv')).open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fields, lineterminator='\n'); w.writeheader(); w.writerows(data)
def dump(name, x): (ROOT / name).write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
def integer(x): return int(float(x))
def signature(r):
    return (tuple(sorted(r['members'].split(';'))), integer(r['original_anchor']),
            integer(r['original_deadline']), integer(r['original_revision_end']))
def semantic_id(s): return sha256(json.dumps(s, ensure_ascii=False).encode()).hexdigest()

old_b, new_b = [rows(r, 'profile/candidate_births.csv') for r in (OLD, ROOT)]
old_r, new_r = [rows(r, 'profile/candidate_revisions.csv') for r in (OLD, ROOT)]
old_s, new_s = [load(r, 'profile/SUMMARY.json') for r in (OLD, ROOT)]
birth_map = [{signature(b): b for b in bs} for bs in (old_b, new_b)]
assert len(birth_map[0]) == len(old_b) and len(birth_map[1]) == len(new_b), '自然对象键非唯一，禁止猜测UUID映射'
common = set(birth_map[0]) & set(birth_map[1])
life_to_signature = [{b['life']: signature(b) for b in bs} for bs in (old_b, new_b)]
bylife = [defaultdict(list), defaultdict(list)]
for i, rs in enumerate((old_r, new_r)):
    for r in rs: bylife[i][r['life']].append(r)
    for values in bylife[i].values(): values.sort(key=lambda r: (integer(r['known']), integer(r['occurrence']), integer(r['record_id']), integer(r['child_id_2'])))

mapping = []
for s in sorted(set(birth_map[0]) | set(birth_map[1])):
    a, b = [m.get(s) for m in birth_map]
    mapping.append(dict(semantic_life=semantic_id(s), members=';'.join(s[0]), original_anchor=s[1],
        old_life=a['life'] if a else '', new_life=b['life'] if b else '',
        status='MATCHED' if a and b else 'OLD_ONLY' if a else 'NEW_ONLY',
        old_revisions=len(bylife[0][a['life']]) if a else 0,
        new_revisions=len(bylife[1][b['life']]) if b else 0))
write('life_mapping', mapping)

numeric = ['original_anchor','original_deadline','original_revision_end','anchor','deadline','revision_end',
           'closed','duty_closed','handoff_end','coverage_incomplete','member_count']
text = ['observation','local_basis','symbols','members','direction']
fields = numeric + text
def value(r, k): return float(r[k]) if k in numeric else r[k]
def asof(i, life, u):
    values = bylife[i][life]
    at = bisect_right([integer(r['known']) for r in values], u)
    return values[at - 1] if at else None

state_differences = []; state_checks = 0; publication_changes = []
for s in sorted(common):
    a, b = [m[s] for m in birth_map]
    aa, bb = bylife[0][a['life']], bylife[1][b['life']]
    old_times = Counter(integer(r['known']) for r in aa); new_times = Counter(integer(r['known']) for r in bb)
    for u in sorted(set(old_times) | set(new_times)):
        if old_times[u] != new_times[u]:
            publication_changes.append(dict(semantic_life=semantic_id(s), known=u,
                old_occurrences=old_times[u], new_occurrences=new_times[u]))
        x, y = asof(0, a['life'], u), asof(1, b['life'], u)
        state_checks += 1
        changed = [k for k in fields if x is None or y is None or value(x,k) != value(y,k)]
        if changed:
            state_differences.append(dict(semantic_life=semantic_id(s), known=u,
                old_life=a['life'], new_life=b['life'], old_revision=x['revision'] if x else '',
                new_revision=y['revision'] if y else '', timestamp=(x or y)['timestamp'],
                changed_fields=';'.join(changed),
                old_values=json.dumps({k:x[k] for k in changed} if x else None,ensure_ascii=False),
                new_values=json.dumps({k:y[k] for k in changed} if y else None,ensure_ascii=False)))
write('native_asof_state_differences', state_differences)
write('publication_changes', publication_changes)

old_conflicts = rows(OLD, 'profile/violations_coverage_flag_vs_continuous_input.csv')
old_cf_keys = {(r['life'],r['revision']) for r in old_conflicts}
def retest(old_row, kind):
    s = life_to_signature[0][old_row['life']]; birth = birth_map[1].get(s)
    u = integer(old_row['known']); current = asof(1,birth['life'],u) if birth else None
    actual = integer(current['coverage_incomplete']) if current else None
    return dict(retest_kind=kind, old_life=old_row['life'],old_revision=old_row['revision'],
        old_timestamp=old_row['timestamp'],known=u,semantic_life=semantic_id(s),
        new_life=birth['life'] if birth else '',new_native_revision=current['revision'] if current else '',
        new_revision_published_at=current['timestamp'] if current else '',
        old_flag=integer(old_row.get('coverage_incomplete',old_row.get('groupCoverageIncomplete',1))),
        new_native_asof_flag=actual, expected_flag=0 if kind=='OLD_FALSE_FLAG' else 1,
        passed=actual == (0 if kind=='OLD_FALSE_FLAG' else 1),
        new_publication_at_old_uti=bool(birth and any(integer(r['known'])==u for r in bylife[1][birth['life']])) )
retests = [retest(r,'OLD_FALSE_FLAG') for r in old_conflicts]
cold = [r for r in old_r if integer(r['coverage_incomplete']) and (r['life'],r['revision']) not in old_cf_keys]
retests += [retest(r,'OLD_COLD_START_CONTROL') for r in cold]
write('coverage_retest', retests)
old_gaps=rows(OLD,'profile/violations_complete_flag_with_input_price_gap.csv') if BASELINE=='D005' else []
gap_retests=[retest(r,'OLD_PRICE_GAP_FLAG') for r in old_gaps]
write('gf002_retest',gap_retests)

tables = []
for name, a in load(OLD, 'readback/report.json')['tables'].items():
    b = load(ROOT, 'readback/report.json')['tables'][name]
    tables.append(dict(table=name,old_rows=a['rows'],new_rows=b['rows'],row_delta=b['rows']-a['rows'],
        old_sha256=a['sha256'],new_sha256=b['sha256'],byte_equal=a['sha256']==b['sha256']))
assert len(tables)==31
write('all_31_tables',tables)
def upstream_map(root):
    return {(f['symbol'],f['kind'],t['name']):t for f in load(root,'UPSTREAM_EXTRACTION.json')['features'] for t in f['tables']}
up = [upstream_map(r) for r in (OLD,ROOT)]
upcmp = [dict(symbol=k[0],kind=k[1],table=k[2],old_rows=up[0][k]['rows'],new_rows=up[1][k]['rows'],
              old_sha256=up[0][k]['sha256'],new_sha256=up[1][k]['sha256'],equal=up[0][k]['sha256']==up[1][k]['sha256']) for k in sorted(set(up[0]) & set(up[1]))]
assert set(up[0])==set(up[1]), '新旧上游范围不同，不能把差异归于本修复'
write('upstream_comparison',upcmp)

check_map=[{c['check_id']:c for c in load(r,'profile/STRUCTURAL_CHECKS.json')} for r in (OLD,ROOT)]
checks=[dict(check_id=k,old_repeat_count=check_map[0].get(k,{}).get('repeat_count'),
    new_repeat_count=check_map[1][k]['repeat_count'],new_denominator=check_map[1][k]['denominator']) for k in check_map[1]]
write('structural_check_comparison',checks)
changed_fields=Counter(k for r in state_differences for k in r['changed_fields'].split(';'))
gap_cases=rows(ROOT,'profile/violations_complete_flag_with_input_price_gap.csv')
gap_baseline=[]
for row in gap_cases:
    sig=life_to_signature[1][row['life']];old_birth=birth_map[0].get(sig)
    old_view=asof(0,old_birth['life'],integer(row['known'])) if old_birth else None
    gap_baseline.append(dict(new_life=row['life'],new_revision=row['revision'],timestamp=row['timestamp'],known=row['known'],
        old_life=old_birth['life'] if old_birth else '',old_native_asof_revision=old_view['revision'] if old_view else '',
        old_flag=integer(old_view['coverage_incomplete']) if old_view else None,new_flag=0,
        same_observation_preexisted=bool(old_view and integer(old_view['coverage_incomplete'])==0)))
write('price_gap_baseline',gap_baseline)
summary=dict(baseline_frp='be57d6752c9d43d10f1d670e1d2993bb8153ea7c' if BASELINE=='D005' else 'ac1927518ad6105f15ffbe37fea45e4be91ba574',current_frp='39f02ec4548e68ba8dbd30061afc870546000994',
    baseline_exact=('daowei2026/observe-iterate@38e2af72be826a1e98fd7f5d4522c50d218750f3:longrun/runs/OI-F800-STAT-20261122-01/professional/D005/' if BASELINE=='D005' else 'daowei2026/observe-iterate@3169703e769340200b183dad7675a1d22ecc1850:longrun/runs/OI-F800-STAT-20261122-01/professional/D002/'),
    same_parameter_version=load(OLD,'FeatureRunResultBinding.json')['parameter_version']==load(ROOT,'FeatureRunResultBinding.json')['parameter_version'],
    upstream_tables=len(upcmp),upstream_tables_byte_equal=sum(r['equal'] for r in upcmp),all_upstream_equal=all(r['equal'] for r in upcmp),
    old_summary=old_s,new_summary=new_s,numeric_deltas={k:new_s[k]-v for k,v in old_s.items() if type(v) in (int,float) and type(new_s.get(k)) in (int,float)},
    old_lives=len(old_b),new_lives=len(new_b),matched_lives=len(common),old_only_lives=len(birth_map[0])-len(common),new_only_lives=len(birth_map[1])-len(common),
    matched_lives_with_changed_uuid=sum(birth_map[0][s]['life']!=birth_map[1][s]['life'] for s in common),
    old_exact_count=len(old_r),new_exact_count=len(new_r),common_raw_revision_uuids=len({r['revision'] for r in old_r}&{r['revision'] for r in new_r}),
    asof_comparison_unit='共同自然Life × 两版原生publication UTI并集；稀疏新观点按知识轴持有，不生成Feature事件；不是逐Tick状态trace',
    native_asof_comparisons=state_checks,native_asof_difference_points=len(state_differences),changed_fields=dict(changed_fields),
    publication_count_changed_life_uti_points=len(publication_changes),all_31_table_comparison='comparison/all_31_tables.csv',
    false_flag_retest_total=len(old_conflicts),false_flag_retest_passed=sum(r['passed'] for r in retests if r['retest_kind']=='OLD_FALSE_FLAG'),
    cold_control_total=len(cold),cold_control_passed=sum(r['passed'] for r in retests if r['retest_kind']=='OLD_COLD_START_CONTROL'),
    gf002_original_view_retest_total=len(gap_retests),gf002_original_view_retest_passed=sum(r['passed'] for r in gap_retests),newly_identified_price_gap_candidate_occurrences=len(gap_cases),price_gap_candidate_preexisted_occurrences=sum(r['same_observation_preexisted'] for r in gap_baseline),
    new_structural_violations={c['check_id']:c['repeat_count'] for c in load(ROOT,'profile/STRUCTURAL_CHECKS.json') if c['repeat_count']},
    uuid_chain_evidence=['profile/violations_complete_previous_chain.csv','profile/violations_previous_reference_integrity.csv','profile/violations_participation_candidate_admission_integrity.csv','profile/violations_alternative_exact_bridge_integrity.csv'],
    limitations=['跨运行UUID无稳定相等合同；自然键只用于本次同输入/参数的对照，不改写正式对象身份','全31表提供原生行数及hash差异，UUID/exact检查按各版实际链完成；不宣称所有二进制载荷逐字相等','新完整G独立执行；旧版统计只作历史对照，非当前Gate证据'])
summary['baseline_delegation']=BASELINE
summary['comparison_directory']=OUT.name
dump('VersionComparison.json' if BASELINE=='D005' else 'InitialVersionComparison.json',summary)
print(json.dumps({k:v for k,v in summary.items() if k not in ('old_summary','new_summary','limitations')},ensure_ascii=False,indent=2))
