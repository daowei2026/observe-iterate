"""独立进程只读平台保存对象，核参数及旧对象未变；不宣称服务布局通过。"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--page-dir',type=Path,required=True)
    args=parser.parse_args()
    from mquant.aidata.profiles import ensure_profile_runtime
    from mquant.quant.models.graph import CaeNodeDao
    ensure_profile_runtime()
    expected=json.loads((args.page_dir/'SHADOW_PAGE.json').read_text())
    old=CaeNodeDao.fqueryById(node_id='6148')
    new=CaeNodeDao.fqueryById(node_id=expected['node_id'])
    digest=lambda text:hashlib.sha256(text.encode()).hexdigest()
    assert digest(old.fason)==expected['source_node_fason_sha256']
    assert digest(new.fason)==expected['native_page_fason_sha256']
    assert json.loads(new.P.overview_scope_rows_json)==expected['expected_frozen_scopes']
    assert new.P.combined_graph_config['plotsets'].fason==old.doShowCAEGraph().P.plotsets.fason
    assert new.doShowCAEGraph().fason==new.fason
    result={'at':datetime.now(timezone.utc).isoformat(),'status':'PERSISTED_PARAMETERS_PASS',
            'node_id':expected['node_id'],'old_6148_unchanged':True,'five_original_plotsets_equal':True,
            'four_explicit_frozen_scopes_equal':True,'independent_process_read':True,
            'limits':'当前工程进程采用新源码的对象恢复/参数读取；不证明既有共享Bokeh进程采用新版、日历IO恢复或阴影图面通过。'}
    (args.page_dir/'PERSISTENCE_READBACK.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))


if __name__=='__main__':main()
