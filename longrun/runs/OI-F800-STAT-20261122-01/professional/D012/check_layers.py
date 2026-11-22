"""E3源图层诊断：全量模型值核对但不导出正式表。"""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import json,hashlib,uuid,gc
import numpy as np
from model_io import load_document,source_rows
R=Path(__file__).resolve().parent
first=load_document(R/'attempts/01-f800.html');original=source_rows(first)
original_hashes=Counter(x['sha256'] for x in original)
del first,original;gc.collect()
actual=load_document(R.parent/'caegraph-E/f800.html');rows=source_rows(actual)
assert len(rows)==21 and Counter(x['sha256'] for x in rows)==original_hashes,'工程修复不应改变任何CDS数据'
revision=actual.get_model_by_name('revision_source');d=revision.data
assert len(d['x'])==1538 and len(set(d['parent']))==1538
assert [int(v) for v in d['known']]==list(d['x'])
expected_children={t['name'] for t in json.loads((R.parent/'D011/inputs/FeatureRunResultBinding.json').read_text())['run_result_tables'] if t['name'].startswith('occurrences_')}
child_count=0;empty_count=0
for i,text in enumerate(d['raw']):
    payload=json.loads(text);g=payload['group'];children=payload['children']
    assert set(children)==expected_children
    key=json.loads(d['parent'][i]);assert key==[g[c] for c in ['timestamp','occurrence','record_id','child_id_2']]
    for prefix,target in [('groupReference_referenceLife',d['life'][i]),('groupReference_referenceRevision',d['revision'][i])]:
        assert g[prefix+'_idForm']==1
        assert str(uuid.UUID(int=(g[prefix+'_idHigh']<<64)|g[prefix+'_idLow']))==target
    for name,values in children.items():
        child_count+=len(values);empty_count+=not bool(values)
        for row in values:assert [row[c] for c in ['timestamp','occurrence','record_id','child_id_2']]==key
    assert len(payload['metadata']['non_group_tables'])==4
klines=[]
for row in rows:
    if {'open','high','low','close','volume','x_l','x_r'}.issubset(row['columns']):
        source=row['source'];klines.append(dict(id=row['id'],rows=row['rows'],close_nan=int(np.isnan(source.data['close']).sum()),renderers=row['renderers']))
assert len(klines)==3 and all(k['rows']==49683 and k['close_nan']==69 for k in klines)
known=Counter(map(int,d['x']));same_tick=sum(n>1 for n in known.values())
summary=dict(scope='E3实际HTML内构图CDS/原值诊断，不是E4正式数据导出',checked_at=datetime.now(timezone.utc).isoformat(),
 all_passed=True,source_count=21,original_and_repaired_CDS_multiset_equal=True,
 revision_rows=1538,full_parent_keys_unique=True,known_equals_point_x=True,
 all_group_UUID_lossless=True,all_26_child_tables_preserved=True,all_child_prefixes_equal=True,
 child_rows_checked=child_count,empty_child_lists_preserved=empty_count,non_group_definition_tables=4,
 same_knowledge_tick_with_multiple_revisions=same_tick,klines=klines,
 sources=[{k:v for k,v in row.items() if k!='source'} for row in rows],
 semantics='原价/稀疏发布/携带界限/独立状态；原U PARTIAL与NOT_EXPOSED不改变')
(R/'E3_LAYER_CHECK.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ['sources','klines']},ensure_ascii=False))
