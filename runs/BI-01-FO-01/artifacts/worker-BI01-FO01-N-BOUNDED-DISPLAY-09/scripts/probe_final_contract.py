from pathlib import Path
import contextlib,hashlib,json,traceback
import os
rt=Path(os.environ.get('BI01_W09_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker09-runtime'));rt.mkdir(parents=True,exist_ok=True)
with (rt/'final-contract.private.log').open('w') as log,contextlib.redirect_stdout(log),contextlib.redirect_stderr(log):
    import bootstrap
    from mquant.quant import OptContext
    from mquant.quant.models.graph import CaeNodeDao
    from mquant.aidata.contracts import build_run_handle
    from mquant.aidata.big_world_chart import AidataBigWorldReviewCAE,_chart_params_from_run_brief,_params_for_fao
    from mquant.aidata.normal_node_behavior import display_selection
    repo=Path('/dwdhome/fy/observe-iterate-bi01-fo-01')
    old=json.loads((repo/'runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-CONSUMER-CONTRACT-08/evidence/old-restore.json').read_text())['objects']['ordinary_chart_path']
    restored=CaeNodeDao.node2fao({'params':old['serialized_representation'],'cls_name':'AidataBigWorldReviewCAE'})
    context=OptContext(sof_name='TA_updto20240229_DBA')
    old_run=build_run_handle(Path('/dwdhome/fy/cgpterm/artifacts/bi01-worker08-runtime/NON_MARKET_SERIALIZATION_ONLY'))
    rbi=dict(context=context,blk='rb',calendar_override='night_end_at_2300',evidence_features=[],chart_review={})
    params=_params_for_fao(AidataBigWorldReviewCAE,{**_chart_params_from_run_brief(old_run,rbi),'big_node_id':'NO_REGISTERED_NODE'})
    fresh=AidataBigWorldReviewCAE(params)
    result={'qualification':'实际最终候选普通16键/同输入fason和ppid，不重跑W08调查或写DAO',
        'keys':sorted(dict(fresh.P)),'fason_byte_equal_to_old':fresh.fason==old['serialized_representation'],
        'ppid_equal_to_old':fresh.ppid==old['ppid'],'old_restore_fason_equal':restored.fason==old['serialized_representation'],
        'ppid':fresh.ppid,'fason_sha256':hashlib.sha256(fresh.fason.encode()).hexdigest()}
    run=build_run_handle(repo/'artifacts/bi01-worker07-runs/BI01-FO01-W07-20261024T0028-rb')
    desc=display_selection(run.run_dir)
    nparams=_params_for_fao(AidataBigWorldReviewCAE,{**_chart_params_from_run_brief(run,{**rbi,'evidence_features':[desc]}),'big_node_id':'big_000002'})
    candidate=AidataBigWorldReviewCAE(nparams)
    (rt/'PERSISTED_OPTIN.fason.private.txt').write_text(candidate.fason)
    result['optin_keys']=sorted(dict(candidate.P));result['optin_fason_sha256']=hashlib.sha256(candidate.fason.encode()).hexdigest()
    result['optin_ppid']=candidate.ppid
(rt/'FINAL_CONTRACT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
assert all(result[k] for k in ['fason_byte_equal_to_old','ppid_equal_to_old','old_restore_fason_equal'])
