"""真实浏览器：持久恢复、范围显隐/缩放及17个专业故事视口。"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from playwright.sync_api import sync_playwright


def utc():
    return datetime.now(timezone.utc).isoformat()


STATE_JS = """() => (window.Bokeh?.documents||[]).flatMap(d=>{
 const ms=Array.from(d._all_models.values());
 return ms.filter(m=>m.type==='Figure'||m.type==='Plot').map(f=>({
 id:f.id,title:f.title.text,x_range:{start:f.x_range.start,end:f.x_range.end},
 boxes:(f.center||[]).filter(m=>m.type==='BoxAnnotation'&&m.left!=null&&m.right!=null)
   .map(m=>({id:m.id,left:m.left,right:m.right,visible:m.visible,fill_color:m.fill_color,fill_alpha:m.fill_alpha})),
 labels:(f.center||[]).filter(m=>m.type==='Label').map(m=>({text:m.text,x:m.x,visible:m.visible})),
 renderers:f.renderers.filter(r=>r.type==='GlyphRenderer').map(r=>({id:r.id,visible:r.visible,source_id:r.data_source.id,glyph_type:r.glyph.type}))
 }));})"""


def state(page):
    return page.evaluate(STATE_JS)


def signature(page):
    raw = page.evaluate("""() => (window.Bokeh?.documents||[]).flatMap(d=>{
 const ms=Array.from(d._all_models.values()); const labels={};
 for(const l of ms.filter(m=>m.type==='LegendItem')) for(const r of l.renderers) labels[r.id]=l.label.value;
 return ms.filter(m=>m.type==='Figure'||m.type==='Plot').map(f=>{
  const out={title:f.title.text,sources:{}};
  for(const r of f.renderers.filter(r=>r.type==='GlyphRenderer')){
   const label=labels[r.id],ds=r.data_source.data;
   if(out.sources[label])continue;
   out.sources[label]=Object.fromEntries(Object.entries(ds).filter(([k])=>k==='x'||k==='ts'||k==='volume'||k.startsWith('__prestd_')).map(([k,v])=>[k,Array.from(v)]));
  } return out;
 });})""")
    return hashlib.sha256(json.dumps(raw, sort_keys=True, allow_nan=True).encode()).hexdigest()


def set_range(page, title_token, start, end):
    page.evaluate("""({token,start,end})=>{
 const fs=(window.Bokeh?.documents||[]).flatMap(d=>Array.from(d._all_models.values())).filter(m=>(m.type==='Figure'||m.type==='Plot')&&m.title.text.includes(token));
 if(fs.length!==1)throw Error('Ambiguous figure '+token);
 fs[0].x_range.start=start;fs[0].x_range.end=end;
 }""", {"token": title_token, "start": start, "end": end})
    page.wait_for_timeout(850)


def view_fields(page, token):
    return page.evaluate("""token=>{
 const docs=window.Bokeh.documents;
 for(const d of docs){
 const ms=Array.from(d._all_models.values());const f=ms.find(m=>(m.type==='Figure'||m.type==='Plot')&&m.title.text.includes(token));if(!f)continue;
 const labels={};for(const l of ms.filter(m=>m.type==='LegendItem'))for(const r of l.renderers)labels[r.id]=l.label.value;
 const seen=new Set(),out={};
 for(const r of f.renderers.filter(r=>r.type==='GlyphRenderer')){
  const label=labels[r.id];if(seen.has(label))continue;seen.add(label);const a=r.data_source.data;
  const idx=Array.from(a.x).map((x,i)=>i).filter(i=>a.x[i]>=f.x_range.start&&a.x[i]<f.x_range.end);
  const k=label.endsWith(' - K');
  const probe=i=>({index:i,x:a.x[i],ts:a.ts?.[i],raw:k?Object.fromEntries(['open','high','low','close'].map(v=>[v,a['__prestd_'+v]?.[i]])):{y:a.__prestd_y?.[i]},display:k?a.close[i]:a.y[i]});
  const finite=idx.filter(i=>Number.isFinite(k?a.__prestd_open[i]:a.__prestd_y[i]));
  let base=null,error=null;
  if(k&&finite.length){const i=finite[0];base=a.__prestd_open[i]/a.open[i];error=Math.max(...finite.map(j=>Math.abs(a.close[j]*base-a.__prestd_close[j])));}
  out[label]={source_id:r.data_source.id,visible:r.visible,rows_in_view:idx.length,raw_ratio_base:base,max_raw_close_reconstruction_error:error,first:idx.length?probe(idx[0]):null,last:idx.length?probe(idx.at(-1)):null};
 }return {title:f.title.text,x_range:{start:f.x_range.start,end:f.x_range.end},series:out};
 }throw Error('Missing figure');
 }""", token)


def open_page(browser, url, out, name):
    context = browser.new_context(viewport={"width": 2600, "height": 1100}, device_scale_factor=1)
    page = context.new_page(); errors=[];failed=[]
    page.on("pageerror", lambda error: errors.append(str(error)[:1500]))
    page.on("requestfailed", lambda request: failed.append({"url":request.url.split('?')[0],"failure":request.failure}))
    response = page.goto(url, wait_until="domcontentloaded", timeout=45000)
    failure = None
    try:
        page.wait_for_function("""()=>(window.Bokeh?.documents||[]).some(d=>{
            const ms=Array.from(d._all_models.values());
            return ms.filter(m=>m.type==='Figure'||m.type==='Plot').length===5 || ms.some(m=>m.type==='Div'&&/Traceback|KeyError|OSError/.test(m.text||''));
        })""", timeout=360000)
        if len(state(page)) != 5: raise RuntimeError("Native layout returned an error Div")
        page.locator('canvas').nth(9).wait_for(state='attached',timeout=30000)
    except Exception as error:
        # canvas在Bokeh shadow DOM中；用Playwright穿透查询作最终判定。
        if len(state(page)) != 5: failure={"type":type(error).__name__,"message":str(error)[:1000]}
    page.wait_for_timeout(1600)
    page.screenshot(path=str(out/(name+"_whole.png")), full_page=True)
    record={"url":url,"at":utc(),"http_status":response.status if response else None,"figures":state(page),"page_errors":errors,"failed_requests":failed,"failure":failure,"canvas_count":page.locator('canvas').count()}
    if failure:
        text=page.evaluate("()=>(window.Bokeh?.documents||[]).flatMap(d=>Array.from(d._all_models.values())).filter(m=>m.type==='Div').map(m=>m.text).join('\\n')")
        text=re.sub(r'<br\s*/?>','\n',text)
        text=re.sub(r'([A-Za-z][A-Za-z0-9+.-]*://)[^\s\'\"<>]+',r'\1[REDACTED_CONNECTION_URI]',text)
        record['body_text_sanitized']=text
        (out/(name+'_error_sanitized.txt')).write_text(text)
    return context,page,record


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--page-record',type=Path,required=True)
    parser.add_argument('--views',type=Path,required=True)
    parser.add_argument('--output-dir',type=Path,required=True)
    parser.add_argument('--fallback-url')
    args=parser.parse_args();assert not args.output_dir.exists();args.output_dir.mkdir(parents=True)
    record=json.loads(args.page_record.read_text());views=json.loads(args.views.read_text())['views']
    result={'worker_execution_id':'BI01-CO-01-W04-worker-ac26d5b83e','operator':'Worker Codex / existing headless Chromium','started_at':utc(),'page_record':str(args.page_record),'new_page_url':record['url'],'story_views':[]}
    try:
        with sync_playwright() as engine:
            browser=engine.chromium.launch(headless=True,args=['--no-sandbox'])
            ctx,page,first=open_page(browser,record['url'],args.output_dir,'initial');result['initial']=first
            used_url=record['url']
            if len(first['figures'])!=5 and args.fallback_url:
                ctx.close();used_url=args.fallback_url
                ctx,page,fallback=open_page(browser,used_url,args.output_dir,'fallback');result['fallback']=fallback
            figures=state(page);assert len(figures)==5,'No usable five-figure page'
            overview=next(f for f in figures if f['title'].startswith('全局概览 '));original_range=overview['x_range']
            before=signature(page);result['raw_data_signature_initial']=before
            if len(overview['boxes'])==4 and used_url==record['url']:
                scope_before=overview['boxes']
                page.get_by_text('隐藏定位辅助',exact=True).click();page.wait_for_timeout(500)
                hidden=state(page);page.locator('canvas').nth(0).screenshot(path=str(args.output_dir/'scope_hidden.png'))
                assert all(not box['visible'] for box in hidden[0]['boxes'])
                assert signature(page)==before
                page.get_by_text('显示定位辅助',exact=True).click();page.wait_for_timeout(500)
                restored=state(page);page.locator('canvas').nth(0).screenshot(path=str(args.output_dir/'scope_restored.png'))
                assert all(box['visible'] for box in restored[0]['boxes'])
                assert signature(page)==before
                b=scope_before[0];margin=(b['right']-b['left'])*.3
                set_range(page,'全局概览 ',b['left']-margin,b['right']+margin)
                zoom=state(page);page.locator('canvas').nth(0).screenshot(path=str(args.output_dir/'scope_zoom_C01.png'))
                assert [(b['left'],b['right']) for b in zoom[0]['boxes']]==[(b['left'],b['right']) for b in scope_before]
                result['scope_interactions']={'hidden':hidden[0],'restored':restored[0],'zoomed':zoom[0],'raw_data_signature_unchanged':True}
                set_range(page,'全局概览 ',original_range['start'],original_range['end'])
            else:result['scope_interactions']={'status':'NOT_PASSED','reason':'Current native page does not contain the four restored overview boxes'}
            for view in views:
                set_range(page,view['case_id'],view['x_start'],view['x_end'])
                fields=view_fields(page,view['case_id'])
                assert all(fields['series'][symbol+' - K']['visible'] and fields['series'][symbol+' - K']['rows_in_view']>0 for symbol in ['rb','hc','i'])
                current=state(page);index=next(i for i,f in enumerate(current) if view['case_id'] in f['title'])
                shot=args.output_dir/(view['id']+'.png');page.locator('canvas').nth(index*2).screenshot(path=str(shot))
                result['story_views'].append({**view,'url':used_url,'fields':fields,'screenshot':str(shot),'captured_at':utc(),'visual_review':'PENDING actual Worker image inspection; not prefilled PASS'})
            result['raw_data_signature_after_views']=signature(page);assert result['raw_data_signature_after_views']==before
            ctx.close()
            ctx,page,reopened=open_page(browser,record['url'],args.output_dir,'reopened');result['reopened']=reopened
            ctx.close();browser.close()
    except Exception as error:
        result['failure']={'type':type(error).__name__,'message':str(error)[:3000]}
    result['ended_at']=utc()
    (args.output_dir/'BROWSER_CHECKS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'initial_figures':len(result.get('initial',{}).get('figures',[])),'story_views':len(result['story_views']),'scope_interactions':result.get('scope_interactions',{}).get('status','EXECUTED'),'failure':result.get('failure')},ensure_ascii=False))
    if result.get('failure'):raise SystemExit(2)


if __name__=='__main__':main()
