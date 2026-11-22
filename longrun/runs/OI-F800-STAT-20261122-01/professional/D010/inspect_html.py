"""在本地Chromium真实打开独立HTML；保存截图、浏览器错误与实际模型。"""
from pathlib import Path
import json
import sys
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent
version=sys.argv[1]
name='first' if version=='v1' else 'current'
logs=[]
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,executable_path='/home/dw/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome',args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':1320,'height':1100},device_scale_factor=1)
    page.on('pageerror',lambda e:logs.append({'type':'pageerror','text':str(e)}))
    page.on('console',lambda m:logs.append({'type':m.type,'text':m.text}) if m.type in ('error','warning') else None)
    requests=[]
    page.on('request',lambda req:requests.append(req.url) if not req.url.startswith(('file:','data:','blob:')) else None)
    page.goto((ROOT/'html'/f'{name}.html').as_uri(),wait_until='load')
    page.wait_for_function('window.Bokeh && Bokeh.documents.length && Object.keys(Bokeh.index).length',timeout=30000)
    page.wait_for_timeout(1500)
    models=page.evaluate('''() => {const d=Bokeh.documents[0];const ms=Array.from(d._all_models.values());return {bokeh:Bokeh.version,plots:ms.filter(m=>m.type==='Figure').map(m=>({id:m.id,title:m.title.text,x_range:m.x_range.id,renderers:m.renderers.length})),sources:ms.filter(m=>m.type==='ColumnDataSource').map(m=>({id:m.id,name:m.name,cols:Object.keys(m.data),length:Object.values(m.data)[0]?.length}))}}''')
    (ROOT/'screenshots').mkdir(exist_ok=True)
    page.screenshot(path=str(ROOT/'screenshots'/f'{name}.png'),full_page=True)
    if version!='v1':
        page.locator('select').select_option(index=3)
        page.wait_for_timeout(250)
        models['ui_select_probe']=page.evaluate("({indices:Bokeh.documents[0].get_model_by_name('revision_source').selected.indices,chooser:Bokeh.documents[0].get_model_by_name('exact_chooser').value})")
        interaction=page.evaluate('''() => {const d=Bokeh.documents[0];const s=d.get_model_by_name('revision_source');if(!s)return {available:false};s.selected.indices=[2];return {available:true,selected:s.selected.indices,records:s.data.revision.length,life:s.data.life[2],revision:s.data.revision[2]}}''')
        page.wait_for_timeout(250)
        detail=page.evaluate("Bokeh.documents[0].get_model_by_name('exact_detail')?.text")
        models['selection_probe']=interaction
        models['chooser_after_selection']=page.evaluate("Bokeh.documents[0].get_model_by_name('exact_chooser')?.value")
        models['output_legend']=page.evaluate("Array.from(Bokeh.documents[0]._all_models.values()).filter(m=>m.type==='Legend').slice(-1)[0].items.map(i=>i.label.value)")
        models['detail_after_selection']=detail
        page.screenshot(path=str(ROOT/'screenshots'/f'{name}-selected.png'),full_page=True)
    models.update(version=version,console=logs,external_requests=requests)
    (ROOT/f'BROWSER_{version}.json').write_text(json.dumps(models,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(models,ensure_ascii=False)[:6000])
    browser.close()
