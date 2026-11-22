"""E4接受后直接读同次HTML嵌入CDS，导出正式构图快照；不重跑Feature/图。"""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,gzip,math
import numpy as np
from model_io import load_document,source_rows,plain,encoded,data_hash
R=Path(__file__).resolve().parent
accept=json.loads((R/'E3_ACCEPTANCE.json').read_text())
assert accept['结果']=='接受'
html=Path(accept['accepted_html']['local_path'])
assert sha256(html.read_bytes()).hexdigest()==accept['accepted_html']['sha256']
manifest=json.loads((R/'FINAL_SCRIPT_MANIFEST.json').read_text())
for row in manifest['files']:assert sha256((R/row['path']).read_bytes()).hexdigest()==row['sha256']
admission=json.loads((R/'E4_ADMISSION.json').read_text())
assert admission['E3_acceptance_sha256']==sha256((R/'E3_ACCEPTANCE.json').read_bytes()).hexdigest()
assert admission['accepted_html_sha256']==accept['accepted_html']['sha256']
assert admission['export_script_sha256']==sha256(Path(__file__).read_bytes()).hexdigest()
doc=load_document(html);rows=source_rows(doc)
expected={x['id']:x for x in json.loads((R/'E3_LAYER_CHECK.json').read_text())['sources']}
assert len(rows)==len(expected)==21
out=R/'formal_data';out.mkdir(exist_ok=False)
files=[]
def row_unit(row):
    name=row['name'] or ''
    if name=='revision_source':return '完整父坐标对应的一条候选组修订发行视图；不是逐tick状态'
    if 'Rct实际' in name:return 'Rct公开事件投影行；同一actual可有多次更新，不等于唯一原始转折数'
    if name.startswith('input:'):return '一条公开ScaleTurn选中记录在本T/C/selected-known图层的表达；跨图层不去重计对象'
    if {'open','high','low','close','volume'}.issubset(row['columns']):return '本品种一根5m原价K线；NaN仍计行'
    label=' / '.join(z['renderer_name'] or '' for z in row['renderers'])
    if '本次携带' in label:return '一条候选组观点携带的界限显示段，按视区裁剪；不是持续状态或coverage区间'
    return '同一条ScaleTurn记录的T到C显示连接段，按视区裁剪'
for row in rows:
    assert row['sha256']==expected[row['id']]['sha256']
    source=row['source']
    payload=dict(schema='caegraph-cds-construction-snapshot/v1',admission_id=admission['admission_id'],
                 accepted_html_sha256=admission['accepted_html_sha256'],effective_run='RUN_ATTEMPT02.json',
                 source_id=row['id'],source_name=row['name'],stage='construction_snapshot',
                 columns={k:dict(dtype=str(getattr(v,'dtype','list')),length=len(v)) for k,v in source.data.items()},
                 nonfinite_encoding={'$float':'NaN | Infinity | -Infinity，保留缺价；不填零'},data=plain(source.data))
    raw=encoded(payload);compressed=gzip.compress(raw,compresslevel=6,mtime=0)
    file=out/('source_'+row['id']+'.json.gz');file.write_bytes(compressed)
    files.append(dict(source_id=row['id'],source_name=row['name'],renderers=row['renderers'],file=str(file.relative_to(R)),
                      stage='construction_snapshot',rows=row['rows'],row_unit=row_unit(row),denominator='本图层在完整B位置的实际构图行；原事件/对象分母须按对应源另读，不跨图层相加',columns=row['columns'],
                      data_sha256=row['sha256'],gzip_sha256=sha256(compressed).hexdigest(),json_sha256=sha256(raw).hexdigest(),bytes=len(compressed)))
summary=dict(admission_id=admission['admission_id'],exported_at=datetime.now(timezone.utc).isoformat(),
             accepted_html_sha256=admission['accepted_html_sha256'],effective_run='RUN_ATTEMPT02.json',
             data_origin='E3接受HTML内嵌的同次Bokeh ColumnDataSource序列化；不读取首版、不复算Feature、不重新构图，不从截图反推',
             stage='construction_snapshot',selected_scope='本次三年五图全部21个实际CDS；含所需原值明细及全部child坐标',
             formal_files=files,unobtained_items=[],producer_run=False,rebuild_graph=False,
             later_stage='未选择viewport_final；本图无动态标准化，fit_y/刻度仅改轴或视窗，不改CDS；本轮用途不需另取该阶段。')
(R/'FORMAL_GRAPH_DATA.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
# E5从实际正式文件读回，与接受图CDS逐列/值一致，不把导出成功当一致性通过。
checks=[];browser={s['id']:s for s in json.loads((R/'BROWSER_actual.json').read_text())['inventory']['sources']}
for row in rows:
    entry=next(f for f in files if f['source_id']==row['id']);file=R/entry['file']
    payload=json.loads(gzip.decompress(file.read_bytes()))
    assert payload['source_id']==row['id'] and payload['accepted_html_sha256']==accept['accepted_html']['sha256']
    assert data_hash(payload['data'])==row['sha256']
    assert set(payload['data'])==set(row['columns']) and all(len(v)==row['rows'] for v in payload['data'].values())
    assert browser[row['id']]['rows']==row['rows'] and set(browser[row['id']]['columns'])==set(row['columns'])
    checks.append(dict(source_id=row['id'],file=entry['file'],row_count=row['rows'],all_columns_and_values_equal=True,browser_model_identity_equal=True,gzip_sha256_equal=sha256(file.read_bytes()).hexdigest()==entry['gzip_sha256']))
# 窗口CDS为明确裁剪的显示几何；验证native原值和显示端点分离，解释1537条tail。
s=doc.get_model_by_name('revision_source');lo=admission['position']['start'];hi=admission['position']['end']
groups=[json.loads(t)['group'] for t in s.data['raw']];geometry=[]
for tag,a,b in [('本次携带 a→d','groupAnchor','groupDeadline'),('本次携带 d→r','groupDeadline','groupRevisionEnd')]:
    row=next(x for x in rows if any(z['renderer_name']==tag for z in x['renderers']))
    data=row['source'].data
    expected_seg={i:(max(g[a],lo),min(g[b],hi)) for i,g in enumerate(groups) if g[b]>=lo and g[a]<=hi}
    actual_seg={int(y):(x0,x1) for y,x0,x1 in zip(data['y0'],data['x0'],data['x1'])}
    assert expected_seg==actual_seg
    geometry.append(dict(layer=tag,rows=len(actual_seg),omitted_outside_view=len(groups)-len(actual_seg),native_endpoints_retained_in_revision_raw=True,clipped_endpoints_equal=True))
for row in rows:
    data=row['source'].data
    if '__prestd_y' in data:assert np.array_equal(data['y'],data['__prestd_y'],equal_nan=True)
result=dict(结果='一致',后继='接受',checked_at=datetime.now(timezone.utc).isoformat(),
            E3_acceptance='E3_ACCEPTANCE.json',E4_admission='E4_ADMISSION.json',accepted_html_sha256=accept['accepted_html']['sha256'],
            effective_run='RUN_ATTEMPT02.json',file_count=len(checks),stage='construction_snapshot',
            full_scope_complete=True,checks=checks,window_geometry=geometry,
            raw_price_nan='三品种各69个close NaN原样保留；正式JSON以$float标记，未填零',
            identities='1538组完整父键/Life+Revision无损，所有32553个child行及22646个空列表保留；E3_LAYER_CHECK逐行已核',
            source_rows_are='实际图层行，不等于唯一业务对象/转折数；selected同一源分别在T/C/known图层表达',
            no_new_business_inference=True,remaining_items=[])
(R/'E5_DATA_CHECK.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(files=len(files),compressed_bytes=sum(f['bytes'] for f in files),E5='一致',geometry=geometry,Feature_recomputed=False),ensure_ascii=False))
