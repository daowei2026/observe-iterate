"""原8缺价观点按同范围上游/自然对象复验及当前全量缺价窗。"""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import json,csv,math
ROOT=Path(__file__).resolve().parent
SYMS=('rb','hc','i')
def rows(path):
 with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def integer(v):return int(float(v))
def finite(v):
 try:return math.isfinite(float(v))
 except (ValueError,TypeError):return False
kl={s:rows(ROOT/'upstream'/f'{s}_kline.csv') for s in SYMS}
ret=rows(ROOT/'comparison/gf002_retest.csv')
assert len(ret)==8 and all(r['passed']=='True' for r in ret)
windows=[]
for r in ret:
 u=integer(r['known'])
 for s in SYMS:
  points=[x for x in kl[s] if u-480000<=integer(x['closeUti'])<=u]
  missing=[x for x in points if not finite(x['close'])]
  windows.append(dict(symbol=s,old_life=r['old_life'],new_life=r['new_life'],known=u,rows=len(points),
    required_from=u-480000,first=points[0]['timestamp'],last=points[-1]['timestamp'],
    missing_close=len(missing),missing_OHLC_all=sum(all(not finite(x[f]) for f in ['open','high','low','close']) for x in missing),
    missing_volume_zero=sum(float(x['volume'])==0 for x in missing),first_missing=missing[0]['timestamp'],last_missing=missing[-1]['timestamp'],
    old_flag=integer(r['old_flag']),new_asof_flag=integer(r['new_native_asof_flag']),new_revision=r['new_native_revision'],
    matched_original_natural_life=True))
assert all(x['rows']==801 and x['missing_close']==x['missing_OHLC_all']==x['missing_volume_zero']==69 and x['new_asof_flag']==1 for x in windows)
revs=rows(ROOT/'profile/candidate_revisions.csv');impacted=[]
missing_rows={s:[x for x in kl[s] if not finite(x['close'])] for s in SYMS}
for r in revs:
 u=integer(r['known'])
 counts={s:sum(u-480000<=integer(x['closeUti'])<=u for x in missing_rows[s]) for s in SYMS}
 if any(counts.values()):impacted.append(dict(life=r['life'],revision=r['revision'],known=u,timestamp=r['timestamp'],flag=integer(r['coverage_incomplete']),missing_counts=counts))
missing=[]
for s in SYMS:
 points=[x for x in kl[s] if not finite(x['close'])]
 missing.append(dict(symbol=s,missing_rows=len(points),first=points[0]['timestamp'],last=points[-1]['timestamp'],first_uti=integer(points[0]['closeUti']),last_uti=integer(points[-1]['closeUti']),
    next_success_uti=next(integer(x['closeUti']) for x in kl[s] if integer(x['closeUti'])>integer(points[-1]['closeUti']) and finite(x['close']))))
out=dict(completed=True,verified_at=datetime.now(timezone.utc).isoformat(),original_view_count=len(ret),affected_lives=len({r['old_life'] for r in ret}),publication_ticks=len({r['known'] for r in ret}),
 window_count=len(windows),windows=windows,input_missing_segments=missing,
 all_current_published_views_in_missing_windows=len(impacted),all_current_view_missing_window_details=impacted,
 current_flag_zero_in_missing_windows=sum(r['flag']==0 for r in impacted),all_current_affected_views_flagged=all(r['flag']==1 for r in impacted),
 semantics_basis='D006确认实际NaN源事件与固定域无豁免；D007已批准InputMissing/清previous。原生AsOf独立读回另见NATIVE_RETEST_API.json；本脚本不运行Feature或重写已冻结预期。')
(ROOT/'MISSING_INPUT_WINDOW_VALIDATION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['windows','all_current_view_missing_window_details']},ensure_ascii=False))
