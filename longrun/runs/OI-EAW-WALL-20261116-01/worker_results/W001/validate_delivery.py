"""只校验本次交付的一致性，不执行业务测试。"""
import json
from support import OUT,lease,write_json,sha,now

proof=lease()
def get(n):return json.loads((OUT/n).read_text())
b=get('BINDING.json');r=get('READBACK.json');f=get('FACTS.json');q=get('RECONCILIATION.json')
assert b['binding_succeeded'] and q['all_unchanged']
assert not q['denied_final_readback_actions']
assert all(v['payload_read_succeeded'] is True for v in r['streams'].values())
checks=[]
for key,item in r['streams'].items():
    samples=get('samples/'+key+'.json')['samples']
    assert len(samples)<=3 and samples==item['samples']
    assert all(x['complete_decoded_batch'] is True for x in samples)
    assert len({x['original_outer_index'] for x in samples})==len(samples)
    assert f['stream_checks'][key]['outer_event_count']==item['outer_event_count']
    checks.append(dict(stream=key,samples=len(samples),outer=item['outer_event_count'],inner=item['inner_item_count_from_anchors'],passed=True))
for match in r['source_matches']:
    assert match['target']['uti']==match['raw_row']['uti']
    assert match['target']['local_no']==match['raw_row']['wall_id']
    assert match['target']['outer_time']==match['raw_row']['ts']
manifest=get('inbox/INPUT_MANIFEST.json')
assert all(sha(OUT/'inbox'/name)==value['sha256'] for name,value in manifest.items())
required=['run_id','work_order_id','object','workspace','actual_context','related_sources','loaded_modules','binary_facts','schema_facts','feature_source_binding','artifact_checks','read_mode','read_attempts','stream_checks','sample_locations','unknowns','created_files']
assert all(key in f for key in required)
assert not f['feature_computation_executed']
write_json('DELIVERY_VALIDATION.json',dict(checked_at_utc=now(),lease=proof,checks=checks,
    input_hashes_match=True,source_sample_matches=len(r['source_matches']),facts_required_fields_present=True,
    related_unchanged=True,passed=True,scope='artifact/metadata consistency only; no business acceptance'))
print('delivery validation passed; no business computation or additional payload read')
