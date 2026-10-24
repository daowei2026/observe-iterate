"""同一冻结i节点的隔离工程副本，验证公开API/索引/正式与显示分工。

不新建业务Run，不注册页面；原W07 run/packet不改。副本不冒充平台正式发布。
"""
from pathlib import Path
import contextlib,hashlib,json,shutil,traceback
import os
rt=Path(os.environ.get('BI01_W09_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker09-runtime'));rt.mkdir(parents=True,exist_ok=True)
result={'qualification':'同一原run/node冻结core的隔离验证副本；非新业务Run或生产图发布'}
with (rt/'board-library.private.log').open('w') as log,contextlib.redirect_stdout(log),contextlib.redirect_stderr(log):
 try:
    import bootstrap,pandas as pd
    from mquant.aidata.api import build_chart_run,build_board_run
    from mquant.aidata.normal_node_behavior import display_selection
    from mquant.quant import OptContext
    original=Path('/dwdhome/fy/observe-iterate-bi01-fo-01/artifacts/bi01-worker07-runs/BI01-FO01-W07-20261024T0028-i')
    replica=rt/'core-validation-replica'/original.name
    (replica/'manifest').mkdir(parents=True,exist_ok=True)
    for name in ('timespan_index.csv','chart_manifest.csv','normal_node_behavior.json'):
        shutil.copy2(original/'manifest'/name,replica/'manifest'/name)
    spans=pd.read_csv(replica/'manifest/timespan_index.csv')
    raw_before=(original/'manifest/timespan_index.csv').read_bytes()
    rbi=dict(output_root=str(replica.parent),run_id=original.name,
        context=OptContext(sof_name='TA_updto20240229_DBA'),blk='i',calendar_override='night_end_at_2300',
        generation_depth='big',big_source={'mode':'manual','timespans':spans[['start_uti','end_uti','start_ts','end_ts','label']].to_dict('records')},
        evidence_features=[display_selection(original)],run_note='Worker09 isolated contract verification replica; not new business Run')
    chart=build_chart_run(rbi,reuse_core=True,dry_run=False)
    board=build_board_run(rbi,reuse_core=True,dry_run=False)
    stats=pd.read_csv(board.feature_slice_stats_path)
    resolved=json.loads(board.run_brief_path.read_text())
    index=json.loads((replica/'formal_dependencies/big_000001/INDEX.json').read_text())
    result.update(run_id=board.run_id,node_id='big_000001',core_byte_equal=(board.timespan_index_path.read_bytes()==raw_before),
        original_core_unchanged=original.joinpath('manifest/timespan_index.csv').read_bytes()==raw_before,
        public_chart_called=True,public_board_called=True,reuse_core=True,dry_run=False,
        stats_count=len(stats),all_slice_success=bool(stats.slice_success.all()),
        display_in_formal_slices=bool(stats.source_role.eq('display').any()),
        all_formal_source_role=bool(stats.source_role.eq('formal').all()),
        selection_in_stats=bool(stats.selection_ref.notna().all()),
        display_in_anchor_registry=sum(a.get('source_role')=='display' for a in resolved['anchor_registry']),
        formal_in_anchor_registry=sum(a.get('source_role')=='formal' for a in resolved['anchor_registry']),
        required_original_tables=len(index['original_tables']),
        older_window=[x for x in index['original_tables'] if x['table']=='windows'],
        delivery_manifest_exists=board.delivery_manifest_path.is_file(),
        replica_path=str(replica),normal_platform_registration=False)
 except Exception as exc:
    traceback.print_exc();result.update(error_type=type(exc).__name__,error=str(exc)[:400])
(rt/'BOARD_REPLICA_CHECK.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
raise SystemExit(1 if 'error_type' in result else 0)
