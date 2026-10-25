import os
from pathlib import Path
import json
rt=Path(os.environ.get('BI01_W11_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker11-runtime'));repo=Path('/dwdhome/fy/observe-iterate-bi01-fo-01')
out=repo/'runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-NORMAL-CONSUMER-11'
w10=repo/'runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-TIME-EXPRESSION-10'
driver=(w10/'scripts/frontend_run.py').read_text().replace('worker10','worker11').replace('worker09','worker11').replace('W10','W11').replace('bi01-worker10-runtime','bi01-worker11-runtime').replace('worker-BI01-FO01-N-TIME-EXPRESSION-10','worker-BI01-FO01-N-NORMAL-CONSUMER-11').replace('N_time_expression_Worker10.ipynb','N_normal_consumer_Worker11.ipynb')
(out/'scripts/frontend_run.py').write_text(driver)
checks=(w10/'scripts/frontend_checks.py').read_text().replace('worker10','worker11').replace('W06同一真实Notebook会话的限定范围/缺件/HC视口检查','Worker11真实普通CAE消费者的限定回看/共同轴/状态检查')
checks=checks.replace("    # 真正hover原点，核完整Life/exact/原状态，而不是只读Python模型。", "    native_readout_checks(page,icmp,RT,event,scope)\n    icmp=capture('i_comparison',suffix='_after_native_reset');comparison_check(icmp,'i',['i_before_missing_recovery','i_recovery','i_after_recovery'])\n    # 真正hover原点，核完整Life/exact/原状态，而不是只读Python模型。")
old=(repo/'runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-BOUNDED-DISPLAY-09/scripts/frontend_checks.py').read_text()
tail=old[old.index('    loc=scope(price)',old.index('def native_graph_checks')):]
checks+='\n\ndef native_readout_checks(page,final,RT,event,scope):\n    motion=next(p for p in final["plots"] if "沿原方向净推进" in p["title"])\n    price=next(p for p in final["plots"] if "当前过程年龄" in p["title"])\n'+tail
checks=checks.replace("    loc.get_by_title('Reset',exact=True).click();page.wait_for_timeout(700);reset=range_now()",'''    loc=scope(price)
    if loc.get_by_title('Reset',exact=True).count():
        loc.get_by_title('Reset',exact=True).click()
    else:
        # Bokeh3.6紧凑toolbar将Reset移到原生overflow菜单；只标记DOM定位，不调用工具或改range。
        state=page.evaluate("""id=>{const v=Bokeh.index.find_one_by_id(id),t=Bokeh.index.find_one_by_id(v.model.toolbar.id);t.overflow_el.setAttribute('data-worker11-overflow',id);t._overflow_menu.el.setAttribute('data-worker11-tool-menu',id);return {toolbar:t.model.id,overflow_items:t._overflow_menu.items.length}}""",price['id'])
        page.locator('[data-worker11-overflow="'+price['id']+'"]').click()
        page.locator('[data-worker11-tool-menu="'+price['id']+'"]').get_by_title('Reset',exact=True).click()
        event('native_reset_via_actual_toolbar_overflow',state=state)
    page.wait_for_timeout(700);reset=range_now()''')
(out/'scripts/frontend_checks.py').write_text(checks)
wrapper=(repo.parents[0]/'cgpterm/artifacts/bi01-worker10-runtime/run_frontend_episode.py').read_text()
wrapper=wrapper.replace('W10','W11').replace('bi01-worker10-runtime','bi01-worker11-runtime').replace('worker-BI01-FO01-N-TIME-EXPRESSION-10','worker-BI01-FO01-N-NORMAL-CONSUMER-11').replace('BI01-FO01-N-TIME-EXPRESSION-10','BI01-FO01-N-NORMAL-CONSUMER-11').replace('aidata-bi01-fo01-n-time-expression-r0038','aidata-bi01-fo01-n-normal-consumer-r0041')
(rt/'run_frontend_episode.py').write_text(wrapper)
settings=rt/'jupyter-user-settings/@jupyterlab/notebook-extension';settings.mkdir(parents=True,exist_ok=True)
(settings/'tracker.jupyterlab-settings').write_text(json.dumps({'windowingMode':'none'})+'\n')
print('prepared W11 bounded own frontend; no service started')
