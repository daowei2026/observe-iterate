from pathlib import Path
import glob,json,os
from playwright.sync_api import sync_playwright
OUT=Path(__file__).resolve().parents[1]
RT=Path('/dwdhome/fy/cgpterm/artifacts/bi01-worker05-runtime')
port=int(os.environ['BI01_W05_JUPYTER_PORT'])
base='http://127.0.0.1:'+str(port)
runtime=next(json.loads(Path(p).read_text()) for p in glob.glob('/home/dw/.local/share/jupyter/runtime/jpserver-*.json') if json.loads(Path(p).read_text()).get('port')==port)
with sync_playwright() as pw:
    chrome=next(Path('/home/dw/.cache/ms-playwright').glob('chromium-*/chrome-linux64/chrome'))
    browser=pw.chromium.launch(executable_path=str(chrome),headless=True,args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':2300,'height':1400})
    page.goto(base+'/lab?token='+runtime['token'])
    page.goto(base+'/lab/tree/runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-UPLOT-NOTEBOOK-05/N_observation_Worker05.ipynb')
    page.wait_for_selector('.jp-Notebook',timeout=60000)
    page.wait_for_timeout(3000)
    page.mouse.move(1500,700)
    page.mouse.wheel(0,100000)
    page.wait_for_function('window.Bokeh?.documents?.length>=1',timeout=60000)
    page.wait_for_timeout(2500)
    state=page.evaluate('''() => ({
       indexType:Bokeh.index?.constructor?.name,indexKeys:Object.keys(Bokeh.index||{}),
       indexEntries:typeof Bokeh.index?.entries==='function'?[...Bokeh.index.entries()].map(([k,v])=>({key:k,model:v?.model?.id,keys:Object.keys(v||{})})):[],
       docs:Bokeh.documents.map(d=>({roots:d.roots().map(r=>({id:r.id,name:r.name,tags:r.tags})),
         viewKeys:Object.keys(Bokeh.index[d.roots()[0].id]||{}),
         childViewTypes:Object.fromEntries(Object.entries(Bokeh.index[d.roots()[0].id]||{}).filter(([k])=>k.includes('child')).map(([k,v])=>[k,{type:typeof v,array:Array.isArray(v),length:v?.length,keys:Object.keys(v||{}).slice(0,5)}])),
         models:[...d._all_models.values()].filter(m=>m.renderers&&m.x_range).map(m=>({id:m.id,title:m.title.text,renderers:m.renderers.length}))})),
       selects:[...document.querySelectorAll('select')].map(s=>({value:s.value,html:s.outerHTML})),
       cells:[...document.querySelectorAll('.jp-Cell')].map(c=>({attrs:[...c.attributes].map(a=>[a.name,a.value]),height:c.clientHeight})),
       app:!!window.jupyterapp})''')
    (RT/'frontend-probe.json').write_text(json.dumps(state,ensure_ascii=False,indent=2))
    page.screenshot(path=str(RT/'frontend-probe.png'))
    print(json.dumps(state,ensure_ascii=False)[:6000])
    browser.close()
