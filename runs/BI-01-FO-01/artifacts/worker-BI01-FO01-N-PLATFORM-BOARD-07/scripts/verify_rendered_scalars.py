"""独立读取保存的实际消费者CDS，按正式spec代码核标量，区分行情来源。"""
from pathlib import Path
import csv,json,math

OUT=Path(__file__).resolve().parents[1]
audits=json.loads((OUT/'evidence/RECONSTRUCTED_CAE_RENDERERS.json').read_text())
rows=lambda p:list(csv.DictReader(p.open()))
checks=[]
for case,a in audits.items():
    symbol=case.split('_')[1];formal=OUT/'inputs'/symbol
    specs={r['definition_life']:int(r['kind']) for r in rows(formal/'specs.csv')}
    metric=next(r for r in rows(formal/'metrics.csv') if int(r['kind'])==specs['PathEfficiency'])
    expected={'completed_recent_updates':float(metric['current']),
              'completed_previous_updates':float(metric['previous'])}
    for view,table in [('working_progress_points','working_progress'),('working_counter_points','working_counter'),
        ('working_efficiency_points','working_efficiency'),('working_duration_points','working_duration'),
        ('working_waiting_points','working_waiting'),('waiting_ratio_points','working_waiting_ratio')]:
        if view=='working_duration_points' and symbol!='i':continue
        row=rows(formal/(table+'.csv'))[0]
        expected[view]=float(row['value']) if row['present']=='1' else None
    for view,value in expected.items():
        matches=[r for r in a['renderers'] if 'anchor:n_display/'+view in r['tags']]
        if value is None:
            ok=not matches or all(not r['data'].get('y') for r in matches)
        else:
            ok=len(matches)==1 and matches[0]['data']['x']==[a['meta']['selected_k']] and len(matches[0]['data']['y'])==1 and math.isclose(matches[0]['data']['y'][0],value,rel_tol=1e-12,abs_tol=1e-12)
        checks.append(dict(case=case,view=view,expected=value,passed=ok,
            qualification='新进程实际CAE renderer；非当前正常服务前端'))
    n_renderers=[r for r in a['renderers'] if 'anchor:n_display/close_path' not in r['tags']]
    checks.append(dict(case=case,check='N renderer exact/K',passed=all(
        all(e==a['meta']['source_exact'] for e in r['data'].get('source_exact',[])) and
        all(k==a['meta']['selected_k'] for k in r['data'].get('as_of_uti',[])) for r in n_renderers)))
    price=next(r['data'] for r in a['renderers'] if 'anchor:n_display/close_path' in r['tags'])
    checks.append(dict(case=case,check='price source distinct from N exact, <=K',passed=
        set(price['source_exact'])=={'same-bound U2MainlineKLineInput CalType.OnlyRead'} and
        max(price['x'])<=a['meta']['selected_k'],
        reason='行情不是N产品exact；原件来源/绑定见inputs和正式交付索引'))
(OUT/'evidence/SCALAR_AND_IDENTITY_CHECKS.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'failed':[x for x in checks if not x['passed']],
    'initial_probe_correction':'初始探针错误要求close_path也带N exact；原失败保留，价格来源另核，不改正式值/图元'},ensure_ascii=False))
