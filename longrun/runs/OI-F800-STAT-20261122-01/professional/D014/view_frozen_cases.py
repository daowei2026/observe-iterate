"""S2只读核阅冻结位置的同次接受图；不挑新案例，不重构图或导出数据。"""
from common import *
import asyncio
from datetime import datetime
from playwright.async_api import async_playwright

async def main():
    cs=read_json(FROZEN,f'{PREFIX}/professional/D013/CaseReviewSet.json')
    index=read_json(FROZEN,f'{PREFIX}/professional/D013/CaseMaterialIndex.json')
    locations={c['case_id']:c for c in index['cases']}
    _,formal=formal_all();price=formal['p1040']['data']
    windows=[]
    for c in cs['cases']:
        a=datetime.fromisoformat(c['start_time']);b=datetime.fromisoformat(c['end_time'])
        rows=[i for i,t in enumerate(price['ts']) if a<=datetime.fromisoformat(t)<=b]
        indices=[g['index'] for g in locations[c['case_id']]['group_rows']]
        windows.append(dict(id=c['case_id'],case_id=c['case_id'],start=max(72003600,price['x'][rows[0]]-300),end=price['x'][rows[-1]]+300,
            group_index=indices[0] if indices else None,group_min=min(indices) if indices else None,group_max=max(indices) if indices else None,
            role='冻结范围完整过程'))
    for cid,start,end,idx,role in [
        ('F800-S1-C003',72003600,72022000,0,'冻结初始化局部'),
        ('F800-S1-C004',73100000,73210000,44,'冻结边界实际谷点/迟到知识局部'),
        ('F800-S1-C004',73590000,73610999.5,72,'冻结边界责任末局部'),
        ('F800-S1-C001',72560000,72593399.5,21,'冻结共同谷点责任末局部'),
        ('F800-S1-C006',97140000,97169399.5,1479,'冻结迟到峰责任末局部')]:
        windows.append(dict(id=cid+'-'+str(idx),case_id=cid,start=start,end=end,group_index=idx,group_min=idx-2,group_max=idx+3,role=role))
    shots=ROOT/'screenshots';shots.mkdir(exist_ok=True)
    html=BASE/'artifacts'/RUN/'caegraph-E/f800.html';html_sha=sha(html.read_bytes())
    records=[];errors=[];logs=[];requests=[]
    async with async_playwright() as p:
        browser=await p.chromium.launch(executable_path='/home/dw/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome',headless=True,
            args=['--no-sandbox','--disable-dev-shm-usage'])
        page=await browser.new_page(viewport=dict(width=1400,height=1200),device_scale_factor=1)
        page.on('pageerror',lambda e:errors.append(str(e)))
        page.on('console',lambda m:logs.append(dict(type=m.type,text=m.text)) if m.type in ('error','warning') else None)
        page.on('request',lambda q:requests.append(q.url) if q.url.startswith(('http:','https:')) else None)
        await page.goto(html.as_uri(),wait_until='load',timeout=180000)
        await page.wait_for_function("Bokeh.documents.length && Bokeh.documents[0].get_model_by_name('revision_source')",timeout=180000)
        for w in windows:
            view=await page.evaluate('''w=>{
              const d=Bokeh.documents[0],models=Array.from(d._all_models.values()),s=d.get_model_by_name('revision_source');
              for(const f of models.filter(m=>m.type==='Figure')){
                f.x_range.start=w.start;f.x_range.end=w.end;
                if(f.title.text.startsWith('候选组')&&w.group_index!==null){f.y_range.start=w.group_min-1;f.y_range.end=w.group_max+1;}
                const sym=f.title.text.split(' · ')[0];if(['rb','hc','i'].includes(sym)){
                  const src=f.renderers.find(r=>r.data_source?.data?.close)?.data_source;let lo=Infinity,hi=-Infinity;
                  if(src)for(let i=0;i<src.data.x.length;i++)if(src.data.x[i]>=w.start&&src.data.x[i]<=w.end){
                    if(Number.isFinite(src.data.low[i]))lo=Math.min(lo,src.data.low[i]);if(Number.isFinite(src.data.high[i]))hi=Math.max(hi,src.data.high[i]);}
                  if(Number.isFinite(lo)&&Number.isFinite(hi)){const pad=(hi-lo||1)*.08;f.y_range.start=lo-pad;f.y_range.end=hi+pad;}
                }
              }
              return {revision_rows:s.data.x.length,group_index:w.group_index,
                life:w.group_index===null?null:s.data.life[w.group_index],revision:w.group_index===null?null:s.data.revision[w.group_index],
                parent:w.group_index===null?null:s.data.parent[w.group_index]};
            }''',w)
            await page.locator('select').first.select_option(index=0 if w['group_index'] is None else w['group_index']+1)
            if w['group_index'] is not None:
                view['detail_matches']=await page.evaluate('''()=>{const d=Bokeh.documents[0],s=d.get_model_by_name('revision_source'),i=s.selected.indices[0];return {selected:i,matches:d.get_model_by_name('exact_detail').text.includes(s.data.revision[i])};}''')
            await page.evaluate('window.scrollTo(0,0)');await page.wait_for_timeout(650)
            shot=shots/(w['id']+'.png');await page.screenshot(path=str(shot),full_page=True,timeout=90000)
            records.append(dict(window=w,observed_at=now(),view=view,screenshot=str(shot.relative_to(ROOT)),screenshot_sha256=sha(shot.read_bytes()),
                note='静态历史投影，不以a→d/d→r显示段当as-of回放；actual/known/状态以原值明细为准。'))
        await browser.close()
    assert sha(html.read_bytes())==html_sha
    save('S2_BROWSER_REVIEW.json',dict(html=str(html),html_sha256=html_sha,windows=records,
        source_html_unchanged=True,source_data_values_edited=False,scope='只核冻结案例，实际缩放/选择视图；不重建/取正式数据',
        page_errors=errors,console=logs,external_requests=requests,completed_at=now()))
    print(json.dumps(dict(frozen_cases=len(cs['cases']),actual_views=len(records),page_errors=errors,console=logs),ensure_ascii=False))

asyncio.run(main())
