"""在真实JupyterLab前端执行Notebook，保留实际操作和Bokeh模型证据。"""
from pathlib import Path
from datetime import datetime, timezone
import glob, json, time, os, hashlib
from playwright.sync_api import sync_playwright

OUT = Path(__file__).resolve().parents[1]
RUNTIME = Path('/dwdhome/fy/cgpterm/artifacts/bi01-worker10-runtime')
events=[]
def event(action, **data):
    events.append({"at":datetime.now(timezone.utc).isoformat(),"action":action,**data})
    (OUT/'evidence/FRONTEND_EVENTS.json').write_text(json.dumps(events,ensure_ascii=False,indent=2))
    print(action, flush=True)

port=int(os.environ['BI01_W10_JUPYTER_PORT'])
base='http://127.0.0.1:'+str(port)
runtime = next(json.loads(Path(p).read_text()) for p in glob.glob(str(RUNTIME/'jupyter'/'jpserver-*.json')) if json.loads(Path(p).read_text()).get('port') == port)
with sync_playwright() as pw:
    chrome=next(Path('/home/dw/.cache/ms-playwright').glob('chromium-*/chrome-linux64/chrome'))
    browser=pw.chromium.launch(executable_path=str(chrome),headless=True,args=['--no-sandbox'])
    context=browser.new_context(viewport={"width":2300,"height":1400})
    page=context.new_page()
    page.set_default_timeout(30000)
    errors=[]
    page.on('pageerror',lambda e:errors.append({'type':type(e).__name__,'sha256':hashlib.sha256(str(e).encode()).hexdigest()}))
    page.goto(base+'/lab?token='+runtime['token'])
    page.goto(base+'/lab/tree/runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-TIME-EXPRESSION-10/N_time_expression_Worker10.ipynb')
    page.wait_for_selector('.jp-Notebook:visible',timeout=60000)
    assert page.url.endswith('/N_time_expression_Worker10.ipynb')
    page.wait_for_timeout(2000)
    event('open_notebook',operator='Worker Codex via Playwright Chromium',kernel='python3 (actual session checked separately)',notebook_path=str(OUT.relative_to(OUT.parents[3]))+'/N_time_expression_Worker10.ipynb')
    marker=OUT/'evidence/EXECUTION_RUNTIME.json'
    previous_execution_id=json.loads(marker.read_text())['execution_id'] if marker.exists() else None
    # 初次打开新Notebook可能尚无kernel；不能把Select对话框当Restart确认。
    existing=page.evaluate("async()=>await (await fetch('/api/sessions')).json()")
    if not any(s['path'].endswith('/N_time_expression_Worker10.ipynb') for s in existing):
        dialog=page.locator('.jp-Dialog:visible')
        if not dialog.count():
            control=page.locator('.jp-NotebookPanel:visible .jp-Toolbar-kernelName')
            if control.count():control.click()
            else:page.locator('.jp-NotebookPanel:visible').get_by_text('No Kernel',exact=True).click()
        page.locator('.jp-Dialog').wait_for()
        page.screenshot(path=str(RUNTIME/'select-kernel.png'))
        assert 'Select Kernel' in page.locator('.jp-Dialog').inner_text()
        choice=page.locator('.jp-Dialog select')
        if 'Python 3 (ipykernel)' not in choice.locator('option:checked').inner_text():
            choice.select_option(label='Python 3 (ipykernel)')
        page.locator('.jp-Dialog button.jp-mod-accept').click()
        event('select_actual_python3_kernel')
    page.wait_for_function('''async()=>{
      const sessions=await (await fetch('/api/sessions')).json();
      return sessions.some(s=>s.path.endsWith('/N_time_expression_Worker10.ipynb')&&s.kernel.execution_state==='idle');
    }''',timeout=90000)
    event('actual_kernel_ready')
    page.get_by_text('Kernel',exact=True).click()
    event('kernel_menu_opened',labels=page.locator('.lm-Menu:visible').all_inner_texts())
    page.screenshot(path=str(RUNTIME/'kernel-menu.png'))
    page.get_by_text('Restart Kernel…',exact=True).click()
    page.locator('.jp-Dialog').wait_for()
    page.screenshot(path=str(RUNTIME/'restart-dialog.png'))
    assert 'Restart' in page.locator('.jp-Dialog').inner_text() and 'Select Kernel' not in page.locator('.jp-Dialog').inner_text()
    page.locator('.jp-Dialog button.jp-mod-accept').click()
    event('restart_kernel_clicked',previous_execution_id=previous_execution_id)
    page.wait_for_function('''async()=>{
      const sessions=await (await fetch('/api/sessions')).json();
      return sessions.some(s=>s.path.endsWith('/N_time_expression_Worker10.ipynb')&&s.kernel.execution_state==='idle');
    }''',timeout=90000)
    page.wait_for_timeout(1500)
    page.screenshot(path=str(RUNTIME/'restart-ready-before-run-all.png'))
    page.get_by_text('Run',exact=True).click()
    page.get_by_text('Run All Cells',exact=True).click()
    event('run_all_cells_explicit_clicked')
    def save_actual_notebook():
        page.keyboard.press('Control+s')
        page.wait_for_timeout(1000)
        dialog=page.locator('.jp-Dialog:visible')
        if dialog.count() and 'File Changed' in dialog.inner_text():
            text=dialog.inner_text()
            assert 'N_time_expression_Worker10.ipynb' in text
            # 本单新建、独占的Notebook；只保留浏览器中真实新执行，不还原旧磁盘输出。
            dialog.get_by_text('Overwrite',exact=True).click()
            event('save_own_actual_execution_after_file_changed_dialog',notebook='N_time_expression_Worker10.ipynb')
            page.wait_for_timeout(1000)
    # Save through the frontend so the real executed notebook is the artifact.
    deadline=time.monotonic()+600
    last_save=0
    while time.monotonic()<deadline:
        page.wait_for_timeout(3000)
        if time.monotonic()-last_save>15:
            save_actual_notebook();last_save=time.monotonic()
        try:
            nb=json.loads((OUT/'N_time_expression_Worker10.ipynb').read_text())
        except (json.JSONDecodeError, FileNotFoundError):
            continue  # Jupyter may be in the middle of writing this real save.
        cells=[c for c in nb['cells'] if c['cell_type']=='code']
        failures=[o for c in cells for o in c.get('outputs',[]) if o.get('output_type')=='error']
        if failures:
            event('run_all_failed',errors=[{k:o.get(k) for k in ('ename',)} for o in failures])
            page.screenshot(path=str(RUNTIME/'run-failed.png'))
            raise RuntimeError(str([(o.get('ename'),o.get('evalue')) for o in failures]))
        completed=OUT/'evidence/KERNEL_COMPLETION.json'
        current=OUT/'evidence/EXECUTION_RUNTIME.json'
        try:
            current_id=json.loads(current.read_text())['execution_id']
            same_execution=(current_id!=previous_execution_id and completed.exists()
                            and json.loads(completed.read_text())['execution_id']==current_id)
        except (json.JSONDecodeError, FileNotFoundError):
            same_execution=False
        if cells[-1].get('execution_count') and same_execution:
            page.wait_for_timeout(3000)
            event('run_all_finished',execution_id=current_id,counts=[c.get('execution_count') for c in cells],browser_errors=errors)
            break
    else:
        raise TimeoutError('Jupyter frontend Run All did not finish in 600s')
    # Disable notebook windowing through the real Settings menu if needed for
    # inspection; graphs are kept as actual frontend outputs, not HTML reloads.
    page.keyboard.press('Control+End')
    page.wait_for_timeout(1500)
    page.screenshot(path=str(RUNTIME/'run-all-finished.png'))
    snapshot=page.evaluate('''() => ({body:document.body.innerText.slice(-2500),
       bokeh:!!window.Bokeh, documents:window.Bokeh?.documents?.length||0,
       frames:[...document.querySelectorAll('iframe')].map(x=>({src:x.getAttribute('src'),title:x.title}))})''')
    (OUT/'evidence/FRONTEND_INITIAL_STATE.json').write_text(json.dumps(snapshot,ensure_ascii=False,indent=2))
    event('frontend_initial_capture',browser_errors=errors)
    from frontend_checks import run_checks
    run_checks(page,OUT,RUNTIME,event)
    save_actual_notebook()
    # Bounded hold permits this same actual browser session to be inspected by
    # subsequent task-specific checks through CDP, then it is explicitly closed.
    context.storage_state(path=str(RUNTIME/'browser-state.json'))
    browser.close()
