import bootstrap
import json,logging
from pathlib import Path
logging.disable(logging.INFO)
from mquant.aidata.big_world_chart import AidataBigWorldReviewCAE
from mquant.quant.models.graph import CaeNodeDao
from mquant.aidata.normal_node_behavior import bundle_for_node
rt=Path(__file__).parent
out=Path('/dwdhome/fy/observe-iterate-bi01-fo-01/runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-PLATFORM-BOARD-07/evidence')
records=[]
for symbol,nodeid in [('rb',6128),('rb',6129),('i',6130),('hc',6131)]:
    node=CaeNodeDao.xqueryById(node_id=nodeid)
    graph=CaeNodeDao.node2fao(node)
    bundle=bundle_for_node(graph.P.run_dir,graph.P.big_node_id)
    records.append(dict(symbol=symbol,cae_node_id=nodeid,class_name=type(graph).__name__,
        run_id=graph.P.run_id,node_id=graph.P.big_node_id,
        manifest=graph.P.normal_node_behavior_manifest,
        selected_k=bundle.meta['selected_k'],source_exact=bundle.meta['source_exact'],
        display_range=bundle.meta['requested_display_range'],
        qualification='正常DAO真实存储参数在新进程node2fao恢复；不是已部署前端通过'))
(out/'PERSISTED_CAE_READBACK.json').write_text(json.dumps(records,ensure_ascii=False,default=str,indent=2)+'\n')
print('actual persisted CAE params restored in a fresh process',len(records))
