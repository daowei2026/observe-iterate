"""有限打开实际 DAO 返回的正常地址；只将原始前端取证存 ignored。"""
import json, time
from pathlib import Path
from datetime import datetime, timezone
from playwright.sync_api import sync_playwright
RT=Path(__file__).parent
results=[]
with sync_playwright() as p:
    chrome=next(Path('/home/dw/.cache/ms-playwright').glob('chromium-*/chrome-linux64/chrome'))
    browser=p.chromium.launch(executable_path=str(chrome),headless=True,args=['--no-sandbox'])
    ctx=browser.new_context(viewport={'width':2300,'height':1400},device_scale_factor=1)
    for symbol in ['rb','i','hc']:
        source=RT/f'{symbol}-pages.private.json'
        if not source.exists():continue
        for row in json.loads(source.read_text()):
            page=ctx.new_page()
            errors=[];console=[]
            page.on('pageerror',lambda e:errors.append(str(e)))
            page.on('console',lambda e:console.append({'type':e.type,'text':e.text}))
            item={'symbol':symbol,'node_id':row['big_node_id'],'url':row['report_url'],
                  'operator':'Worker Codex / Playwright Chromium','at':datetime.now(timezone.utc).isoformat()}
            try:
                response=page.goto(row['report_url'],wait_until='domcontentloaded',timeout=60000)
                item['http_status']=response.status if response else None
                # 真实 Bokeh websocket 构图需要等待，最多45秒；不以 HTTP200 判图成功。
                deadline=time.monotonic()+45
                while time.monotonic()<deadline:
                    if any(f.evaluate("() => !!window.Bokeh?.documents?.length") for f in page.frames):break
                    if 'Traceback' in page.locator('body').inner_text():break
                    page.wait_for_timeout(1000)
                item['frames']=[]
                for f in page.frames:
                    item['frames'].append({'url':f.url,'body':f.locator('body').inner_text(),
                        'bokeh':f.evaluate("() => window.Bokeh ? {version:Bokeh.version,documents:Bokeh.documents.map(d=>({roots:d.roots().map(r=>({id:r.id,name:r.name,tags:r.tags})),models:Array.from(d._all_models.values()).filter(m=>['GlyphRenderer','ColumnDataSource','Div'].includes(m.type)).map(m=>({id:m.id,type:m.type,name:m.name,tags:m.tags,text:m.text,data:m.data}))}))} : null")})
                page.screenshot(path=str(RT/f'platform-{symbol}-{row["big_node_id"]}.png'),full_page=True)
            except Exception as e:item['open_error']=repr(e)
            item.update(errors=errors,console=console)
            results.append(item)
            (RT/'PLATFORM_BROWSER.private.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
            print(symbol,row['big_node_id'],'actual normal page inspected',flush=True)
            page.close()
    browser.close()
