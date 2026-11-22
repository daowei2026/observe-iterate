"""E3实际渲染、交互与图层证据；不导出正式数据。"""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import asyncio,json
from playwright.async_api import async_playwright
R=Path(__file__).resolve().parent; SHOTS=R/'screenshots';SHOTS.mkdir(exist_ok=True)
ACTUAL=R.parent/'caegraph-E/f800.html';EXPECTED=R.parent/'D010/html/current.html'
INVENTORY='''() => {
 const doc=Bokeh.documents[0],models=Array.from(doc._all_models.values());
 const figs=models.filter(m=>m.type==='Figure');
 const sources=models.filter(m=>m.type==='ColumnDataSource');
 const source=doc.get_model_by_name('revision_source');
 const legends=models.filter(m=>m.type==='Legend');
 return {figure_count:figs.length,figures:figs.map(f=>({id:f.id,title:f.title.text,x_range_id:f.x_range.id,x_start:f.x_range.start,x_end:f.x_range.end,y_start:f.y_range.start,y_end:f.y_range.end,axis_label:f.yaxis?.[0]?.axis_label,x_tick_count:f.below?.[0]?.ticker?.ticks?.length,renderers:f.renderers.map(r=>({id:r.id,type:r.type,name:r.name,source:r.data_source?.id,glyph:r.glyph?.type,visible:r.visible}))})),
 sources:sources.map(s=>({id:s.id,name:s.name,rows:Object.values(s.data)[0]?.length??0,columns:Object.keys(s.data)})),
 revision_rows:source.data.x.length,revision_first:{life:source.data.life[0],revision:source.data.revision[0],parent:source.data.parent[0],known:source.data.known[0]},revision_last:{life:source.data.life.at(-1),revision:source.data.revision.at(-1),parent:source.data.parent.at(-1),known:source.data.known.at(-1)},
 shared_x:new Set(figs.map(f=>f.x_range.id)).size===1,legends:legends.map(l=>({click_policy:l.click_policy,labels:l.items.map(i=>i.label)})),
 chooser_options:doc.get_model_by_name('exact_chooser').options.length,
 data_table_same_source:doc.get_model_by_name('revision_table').source.id===source.id,
 header:models.filter(m=>m.type==='Div').map(m=>m.text.slice(0,500))};
}'''
async def inspect(browser,name,path):
 page=await browser.new_page(viewport={'width':1400,'height':1100},device_scale_factor=1)
 logs=[];errors=[];requests=[]
 page.on('console',lambda m:logs.append({'type':m.type,'text':m.text}) if m.type in ['error','warning'] else None)
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.on('request',lambda q: requests.append(q.url) if q.url.startswith(('http:','https:')) else None)
 await page.goto(path.as_uri(),wait_until='load',timeout=180000)
 await page.wait_for_function("typeof Bokeh!=='undefined' && Bokeh.documents.length && Bokeh.documents[0].get_model_by_name('revision_source')",timeout=180000)
 await page.wait_for_timeout(2000)
 inventory=await page.evaluate(INVENTORY)
 await page.screenshot(path=str(SHOTS/(name+'-full.png')),full_page=True,timeout=90000)
 # 使用实际DOM下拉控件。其option值是标签，按索引选择后核Bokeh模型及明细。
 select=page.locator('select').first
 await select.select_option(index=3)
 await page.wait_for_timeout(700)
 selection=await page.evaluate('''() => {
 const doc=Bokeh.documents[0],s=doc.get_model_by_name('revision_source'),d=doc.get_model_by_name('exact_detail'),c=doc.get_model_by_name('exact_chooser');
 const i=s.selected.indices[0];return {index:i,chooser_value:c.value,life:s.data.life[i],revision:s.data.revision[i],parent:s.data.parent[i],detail_contains_life:d.text.includes(s.data.life[i]),detail_contains_revision:d.text.includes(s.data.revision[i]),detail_contains_children:d.text.includes('children'),raw_text_length:s.data.raw[i].length};
}''')
 await select.scroll_into_view_if_needed();await page.screenshot(path=str(SHOTS/(name+'-selected.png')),full_page=True,timeout=90000)
 # 从真实完整图缩放一个局部视窗，只改变x_range，用于检查原价/点/携带段实际可见；不改CDS。
 if name=='actual':
  window=await page.evaluate('''() => {
   const doc=Bokeh.documents[0],s=doc.get_model_by_name('revision_source'),f=Array.from(doc._all_models.values()).find(m=>m.type==='Figure');
   const center=Number(s.data.x[0]);f.x_range.start=center-24000;f.x_range.end=center+108000;return {center,start:f.x_range.start,end:f.x_range.end,source_rows:s.data.x.length};
  }''')
  await page.wait_for_timeout(1000);await page.screenshot(path=str(SHOTS/'actual-zoom.png'),full_page=True,timeout=90000)
 else:window=None
 out=dict(name=name,html=str(path),html_sha256=sha256(path.read_bytes()).hexdigest(),inventory=inventory,selection=selection,zoom=window,console=logs,page_errors=errors,external_requests=requests)
 (R/('BROWSER_'+name+'.json')).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 await page.close()
 return out
async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/home/dw/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
  actual=await inspect(browser,'actual',ACTUAL); expected=await inspect(browser,'expected',EXPECTED)
  await browser.close()
 print(json.dumps({n:{'figures':v['inventory']['figure_count'],'sources':len(v['inventory']['sources']),'revision_rows':v['inventory']['revision_rows'],'console':v['console'],'page_errors':v['page_errors'],'external_requests':v['external_requests'],'selection':v['selection']} for n,v in [('actual',actual),('expected',expected)]},ensure_ascii=False))
asyncio.run(main())
