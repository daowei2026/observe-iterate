"""打开E3接受原HTML；仅缩放/选择，不构图、不改变CDS或重导正式数据。"""
from common import *
import asyncio
import sys
from playwright.async_api import async_playwright

WINDOWS = [
    dict(id='jan-common-and-start',start=72003600,end=72600000,group_index=3),
    dict(id='jan-isolated-i',start=72020000,end=72110000,group_index=None),
    dict(id='feb-2delta',start=73100000,end=73210000,group_index=44),
    dict(id='feb-outside-2delta',start=73215000,end=73285000,group_index=None),
    dict(id='may-raw-independent',start=85665000,end=85790000,group_index=None),
    dict(id='june-july-late',start=96630000,end=97175000,group_index=1468),
    dict(id='oct-raw-independent',start=80010000,end=80110000,group_index=632),
]
EXTRA = [
    dict(id='jan-start-anchor',start=72003600,end=72022000,group_index=0),
    dict(id='march-boundary-close',start=73590000,end=73620000,group_index=72),
]

async def main():
    shots=ROOT/'screenshots';shots.mkdir(exist_ok=True)
    html=BASE/'artifacts'/RUN/'caegraph-E/f800.html'
    identity=sha(html.read_bytes())
    async with async_playwright() as p:
        browser=await p.chromium.launch(executable_path='/home/dw/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome',
            headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
        page=await browser.new_page(viewport=dict(width=1400,height=1200),device_scale_factor=1)
        errors=[];logs=[];requests=[]
        page.on('pageerror',lambda e:errors.append(str(e)))
        page.on('console',lambda m:logs.append(dict(type=m.type,text=m.text)) if m.type in ('error','warning') else None)
        page.on('request',lambda q:requests.append(q.url) if q.url.startswith(('http:','https:')) else None)
        await page.goto(html.as_uri(),wait_until='load',timeout=180000)
        await page.wait_for_function("Bokeh.documents.length && Bokeh.documents[0].get_model_by_name('revision_source')",timeout=180000)
        await page.wait_for_timeout(1000)
        inventory=await page.evaluate('''() => {
          const doc=Bokeh.documents[0], seen=new Set(),figures=[];
          function walk(v){if(!v||seen.has(v))return;seen.add(v);if(v.model?.type==='Figure')figures.push(v);for(const c of v.child_views??[])walk(c);}
          for(const v of Object.values(Bokeh.index))walk(v);window.__S1views=figures;
          return {figures:figures.map(v=>({id:v.model.id,title:v.model.title.text})),sources:Array.from(doc._all_models.values()).filter(m=>m.type==='ColumnDataSource').map(s=>({id:s.id,rows:Object.values(s.data)[0]?.length}))};
        }''')
        extra='--extra' in sys.argv
        if not extra: await page.screenshot(path=str(shots/'wide.png'),full_page=True,timeout=90000)
        records=[]
        for window in (EXTRA if extra else WINDOWS):
            view=await page.evaluate('''w => {
                const doc=Bokeh.documents[0],models=Array.from(doc._all_models.values()),s=doc.get_model_by_name('revision_source');
                for(const f of models.filter(m=>m.type==='Figure')){
                    f.x_range.start=w.start;f.x_range.end=w.end;
                    if(f.title.text.startsWith('候选组') && w.group_index!==null){f.y_range.start=w.group_index-2;f.y_range.end=w.group_index+7;}
                    const sym=f.title.text.split(' · ')[0];
                    if(['rb','hc','i'].includes(sym)){
                        const src=f.renderers.find(r=>r.data_source?.data?.close)?.data_source;
                        let lo=Infinity,hi=-Infinity;
                        if(src)for(let j=0;j<src.data.x.length;j++)if(src.data.x[j]>=w.start&&src.data.x[j]<=w.end){
                            const a=Number(src.data.low[j]),b=Number(src.data.high[j]);if(Number.isFinite(a))lo=Math.min(lo,a);if(Number.isFinite(b))hi=Math.max(hi,b);}
                        if(Number.isFinite(lo)&&Number.isFinite(hi)){const pad=(hi-lo||1)*.08;f.y_range.start=lo-pad;f.y_range.end=hi+pad;}
                    }
                }
                if(w.group_index===null)return {group_index:null,revision_rows:s.data.x.length};
                return {group_index:w.group_index,life:s.data.life[w.group_index],revision:s.data.revision[w.group_index],parent:s.data.parent[w.group_index],revision_rows:s.data.x.length};
            }''',window)
            if window['group_index'] is not None:
                await page.locator('select').first.select_option(index=window['group_index']+1)
                view['detail']=await page.evaluate('''() => {const d=Bokeh.documents[0],s=d.get_model_by_name('revision_source'),i=s.selected.indices[0];return {selected:i,detail_contains_revision:d.get_model_by_name('exact_detail').text.includes(s.data.revision[i])};}''')
            await page.evaluate('window.scrollTo(0,0)')
            await page.wait_for_timeout(650)
            filename=window['id']+'.png'
            await page.screenshot(path=str(shots/filename),full_page=True,timeout=90000)
            record=dict(window=window,observed_at=now(),view=view,screenshot='screenshots/'+filename,
                screenshot_sha256=sha((shots/filename).read_bytes()))
            # 细看原价过程：从实际页面原Figure原生截图，无图像重画/裁剪推算。
            if window['id'] in ('jan-common-and-start','jan-isolated-i','feb-2delta','feb-outside-2delta','may-raw-independent','june-july-late'):
                record['price_figures']=[]
                for fid in ('p1002','p1130','p1258'):
                    handle=await page.evaluate_handle("id=>window.__S1views.find(v=>v.model.id===id)?.el",fid)
                    element=handle.as_element()
                    if element:
                        path=shots/(window['id']+'-'+fid+'.png')
                        await element.screenshot(path=str(path),timeout=90000)
                        record['price_figures'].append(str(path.relative_to(ROOT)))
            records.append(record)
        assert sha(html.read_bytes())==identity
        save('BROWSER_ADDITIONAL_SELECTION.json' if extra else 'BROWSER_SELECTION.json',dict(accepted_html=str(html),html_sha256=identity,
            started_from_original=True,scope='S1只读浏览，缩放/选择视窗；无正式数据再导出或源文件修改',
            inventory=inventory,windows=records,page_errors=errors,console=logs,external_requests=requests,
            html_unchanged=True,completed_at=now()))
        print(json.dumps(dict(windows=len(records),screenshots=len(list(shots.glob('*.png'))),page_errors=errors,console=logs,html_unchanged=True),ensure_ascii=False))
        await browser.close()

asyncio.run(main())
