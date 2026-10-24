from pathlib import Path
import contextlib,json,traceback
import os
rt=Path(os.environ.get('BI01_W09_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker09-runtime'));rt.mkdir(parents=True,exist_ok=True)
with (rt/'tests.private.log').open('w') as log,contextlib.redirect_stdout(log),contextlib.redirect_stderr(log):
    import bootstrap,pytest
    tree='/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-bounded-display-r0035/'
    result=pytest.main(['-q',tree+'tests/test_bounded_display_contract.py',tree+'tests/test_evidence_plot_contract.py',
        tree+'tests/test_u2_normal_node_behavior_display.py',tree+'tests/test_normal_node_behavior.py','--tb=short'])
print(json.dumps({'pytest_exit_code':int(result),'log_scope':'技术夹具及原相连回归，非市场/平台接收'},ensure_ascii=False))
raise SystemExit(int(result))
