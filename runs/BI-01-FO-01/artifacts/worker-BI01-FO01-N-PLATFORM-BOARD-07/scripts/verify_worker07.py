"""正式源→持久选择→新进程真实消费者→board 包；不冒称平台前端通过。"""
import hashlib, json, os, logging
from pathlib import Path
import pandas as pd
import numpy as np
from bokeh.models import GlyphRenderer
from mquant.quant import OptContext
from mquant.aidata.normal_node_behavior import read_frame,bundle_for_node
from mquant.aidata.big_world_chart import AidataBigWorldReviewCAE
from mquant.aidata.u2_normal_node_behavior_display import export_plot_view_data

logging.disable(logging.INFO)
OUT=Path(__file__).resolve().parents[1]
RT=Path(os.environ['BI01_W07_PRIVATE_RUNTIME'])
E=OUT/'evidence';E.mkdir(exist_ok=True)

def clean(x):
    if isinstance(x,dict):return {str(k):clean(v) for k,v in x.items()}
    if isinstance(x,(list,tuple,np.ndarray,pd.Series,pd.Index)):return [clean(v) for v in x]
    if isinstance(x,np.generic):return clean(x.item())
    if x is pd.NA or x is pd.NaT:return None
    if isinstance(x,float) and not np.isfinite(x):return None
    if isinstance(x,(pd.Timestamp,Path)):return str(x)
    return x

checks=[]
def check(name,value,**detail):
    checks.append(dict(name=name,passed=bool(value),**clean(detail)))

# 实际正常读者本次所得与 W02 的冻结正式结果逐字段比较，不比较图用投影。
for path in sorted((RT/'direct_read').glob('*.csv')):
    old=OUT/'inputs/rb'/path.name
    a,b=read_frame(dict(path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest())),read_frame(dict(path=str(old),sha256=hashlib.sha256(old.read_bytes()).hexdigest()))
    try:pd.testing.assert_frame_equal(a.sort_index(),b.sort_index(),check_dtype=False);equal=True;error=None
    except AssertionError as e:equal=False;error=str(e)
    check('fresh OnlyRead vs pinned rb '+path.stem,equal,error=error,rows=len(a))

context=OptContext(sof_name='TA_updto20240229_DBA')
api=json.loads((RT/'API_RESULTS.private.json').read_text())
order=[('rb','big_000001'),('rb','big_000002'),('rb','big_000001'),('i','big_000001'),('hc','big_000001')]
audits={}
for step,(symbol,node) in enumerate(order):
    run_dir=Path(api[symbol]['board']['run_dir'])
    bundle=bundle_for_node(run_dir,node)
    graph=AidataBigWorldReviewCAE(dict(run_dir=str(run_dir),run_id=run_dir.name,big_node_id=node,
        normal_node_behavior_manifest=str(run_dir/'manifest/normal_node_behavior.json'),
        context=context,calendar_name='night_end_at_2300',blk=symbol))
    layout=graph.layout()
    renderers=[]
    for r in layout.select({'type':GlyphRenderer}):
        if 'anchor:n_display/' in str(r.tags):
            renderers.append(dict(id=r.id,tags=clean(r.tags),glyph=type(r.glyph).__name__,data=clean(r.data_source.data)))
    case=f'{symbol}_{node}'
    audits[f'{step}_{case}']=dict(qualification='新进程实际CAE消费者构图；不是已部署平台前端证明',
        root_id=layout.id,root_name=layout.name,meta=clean(bundle.meta),renderers=renderers)
    export_plot_view_data(bundle,OUT/'plot_view_data'/case)
    K=int(bundle.meta['selected_k'])
    check(case+' close <=K',int(bundle.price.open_uti.max())<=K,source_rows=bundle.meta.get('source_price_rows'),display_rows=len(bundle.price),K=K)
    expected_rows={'rb_big_000001':4789,'rb_big_000002':294,'i_big_000001':37,'hc_big_000001':454}[case]
    check(case+' actual display range',len(bundle.price)==expected_rows)
    packet=run_dir/'delivery/big_node_packets'/f'{node}_packet'
    dep=packet/'10_NORMAL_N_FORMAL_DEPENDENCIES'
    index=json.loads((dep/'INDEX.json').read_text())
    for item in index['original_tables']:
        check(case+' original dependency '+item['table'],hashlib.sha256((dep/item['path']).read_bytes()).hexdigest()==item['sha256'])
    stats=pd.read_csv(run_dir/'manifest/feature_slice_stats.csv')
    check(case+' all normal feature slices succeeded',stats.slice_success.all())
    if symbol=='i':check('i actual 24 missing close preserved',bundle.price.close.isna().sum()==24)

(E/'RECONSTRUCTED_CAE_RENDERERS.json').write_text(json.dumps(clean(audits),ensure_ascii=False,indent=2)+'\n')
(E/'DIRECT_CHECKS.json').write_text(json.dumps(clean(checks),ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':len(checks),'failed':[x['name'] for x in checks if not x['passed']],'actual_platform_frontend':'separate browser evidence'},ensure_ascii=False),flush=True)
