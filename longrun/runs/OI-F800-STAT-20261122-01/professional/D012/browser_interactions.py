from pathlib import Path
import asyncio,json
from playwright.async_api import async_playwright
R=Path(__file__).resolve().parent
async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/home/dw/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
  page=await browser.new_page(viewport={'width':1400,'height':1000});errors=[]
  page.on('pageerror',lambda e:errors.append(str(e)))
  await page.goto((R.parent/'caegraph-E/f800.html').resolve().as_uri(),wait_until='load',timeout=180000)
  await page.wait_for_function("Bokeh.documents.length && Bokeh.documents[0].get_model_by_name('revision_source')",timeout=180000)
  await page.wait_for_timeout(1500)
  target=await page.evaluate('''() => {
   const doc=Bokeh.documents[0],s=doc.get_model_by_name('revision_source');
   const seen=new Set(),figures=[];function walk(v){if(!v || seen.has(v))return;seen.add(v);if(v.model?.type==='Figure')figures.push(v);for(const child of v.child_views??[])walk(child);}
   for(const v of Object.values(Bokeh.index))walk(v);
   const view=figures.find(v=>v.model.title.text.startsWith('候选组'));
   if(!view)return {error:'Figure view traversal unavailable',views:figures.length,index_keys:Object.keys(Bokeh.index)};
   window.__E3_view=view;view.model.x_range.start=Number(s.data.x[2])-2000;view.model.x_range.end=Number(s.data.x[2])+2000;view.model.y_range.start=-1;view.model.y_range.end=5;view.el.scrollIntoView();
   return {view_id:view.model.id,source_id:s.id,index:2,life:s.data.life[2],revision:s.data.revision[2]};
  }''')
  assert 'error' not in target,target
  await page.wait_for_timeout(700)
  xy=await page.evaluate('''() => {const v=window.__E3_view,s=Bokeh.documents[0].get_model_by_name('revision_source');const rect=v.canvas_view.el.getBoundingClientRect();return {x:rect.left+v.frame.x_scale.compute(Number(s.data.x[2])),y:rect.top+v.frame.y_scale.compute(2),rect:{left:rect.left,top:rect.top,width:rect.width,height:rect.height}};}''')
  await page.mouse.move(xy['x'],xy['y']);await page.wait_for_timeout(900)
  tooltip=await page.locator('.bk-Tooltip').all_text_contents()
  await page.screenshot(path=str(R/'screenshots/actual-hover.png'),full_page=True)
  await page.mouse.click(xy['x'],xy['y']);await page.wait_for_timeout(600)
  tap=await page.evaluate('''() => {const d=Bokeh.documents[0],s=d.get_model_by_name('revision_source'),detail=d.get_model_by_name('exact_detail');return {selected:s.selected.indices,chooser:d.get_model_by_name('exact_chooser').value,detail_matches:detail.text.includes(s.data.revision[2]),source_rows:s.data.x.length};}''')
  assert 2 in tap['selected'] and tap['chooser']=='2' and tap['detail_matches']
  await page.screenshot(path=str(R/'screenshots/actual-tapped.png'),full_page=True)
  result=dict(target=target,mouse=xy,tooltip=tooltip,tap=tap,page_errors=errors,scope='E3实际鼠标hover及TapTool点选；仅视窗变化，不修改源数据/最终HTML')
  (R/'E3_BROWSER_INTERACTIONS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False));await browser.close()
asyncio.run(main())
