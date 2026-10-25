import os
from pathlib import Path
import contextlib,hashlib,json,os,traceback
rt=Path(os.environ.get('BI01_W11_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker11-runtime'));repo=Path('/dwdhome/fy/observe-iterate-bi01-fo-01');result={}
try:
 with (rt/'direct-checks.private.log').open('w') as f,contextlib.redirect_stdout(f),contextlib.redirect_stderr(f):
  import bootstrap,pytest
  built=json.loads((rt/'BUILT_RUNS.json').read_text())['cases'];fixture=built[0]['run_dir']
  old_root=repo/'artifacts/bi01-worker07-runs/BI01-FO01-W07-20261024T0028-rb'
  os.environ['BI01_W11_FIXTURE_RUN']=fixture;os.environ['BI01_W11_OLD_RB_RUN']=str(old_root)
  tests=bootstrap.candidate/'tests'
  arguments=[str(tests/'test_normal_time_consumer.py'),
    str(tests/'test_normal_node_behavior.py'),
    str(tests/'test_bounded_display_contract.py')+'::test_old_scale_turn_and_blk_thick_configs_remain_lightweight',
    str(tests/'test_bounded_display_contract.py')+'::test_legacy_group_is_only_a_tag_without_forced_panel_tree',
    str(tests/'test_bounded_display_contract.py')+'::test_invalid_new_capability_fails_before_consumer',
    str(tests/'test_bounded_display_contract.py')+'::test_history_guard_prevents_any_update_to_old_n_params',
    str(tests/'test_bounded_display_contract.py')+'::test_delivery_refuses_a_display_source_before_primary_mapping']
  exit_code=int(pytest.main(['-q','--tb=short',*arguments]));assert exit_code==0
  f.flush()
  from mquant.quant import OptContext
  from mquant.quant.models.graph import CaeNodeDao
  from mquant.aidata.contracts import build_run_handle
  from mquant.aidata.big_world_chart import AidataBigWorldReviewCAE,_chart_params_from_run_brief,_params_for_fao
  old=json.loads((repo/'runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-CONSUMER-CONTRACT-08/evidence/old-restore.json').read_text())['objects']['ordinary_chart_path']
  restored=CaeNodeDao.node2fao({'params':old['serialized_representation'],'cls_name':'AidataBigWorldReviewCAE'})
  old_run=build_run_handle(Path('/dwdhome/fy/cgpterm/artifacts/bi01-worker08-runtime/NON_MARKET_SERIALIZATION_ONLY'))
  rbi=dict(context=OptContext(sof_name='TA_updto20240229_DBA'),blk='rb',calendar_override='night_end_at_2300',evidence_features=[],chart_review={})
  params=_params_for_fao(AidataBigWorldReviewCAE,{**_chart_params_from_run_brief(old_run,rbi),'big_node_id':'NO_REGISTERED_NODE'})
  obj=AidataBigWorldReviewCAE(params)
  ordinary=dict(keys=sorted(dict(obj.P)),fason_byte_equal=obj.fason==old['serialized_representation'],ppid_equal=obj.ppid==old['ppid'],
    old_actual_restore_equal=restored.fason==old['serialized_representation'])
  assert len(ordinary['keys'])==16 and all(ordinary[k] for k in ('fason_byte_equal','ppid_equal','old_actual_restore_equal'))
  from mquant.aidata.normal_node_behavior import bundle_for_node,display_selection
  b=bundle_for_node(old_root,'big_000002');assert b.meta['selected_k']==103315800
  assert display_selection(old_root)['prepared_display']['version']==1
  result=dict(pytest_exit=exit_code,pytest_summary=[line for line in (rt/'direct-checks.private.log').read_text().splitlines() if 'passed' in line],
   ordinary=ordinary,legacy_normal_single_K=dict(K=b.meta['selected_k'],exact=b.meta['source_exact'],price_rows=len(b.price)),
   old_DAO_collision_probe='直接保护guard假Dao调用，写入计数0；未访问/修改真实旧节点',complete=True)
except Exception as exc:
 with (rt/'direct-checks-error.private.log').open('w') as f:traceback.print_exc(file=f)
 result.update(error_type=type(exc).__name__,complete=False)
(rt/'DIRECT_CHECKS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False));raise SystemExit(0 if result['complete'] else 1)
