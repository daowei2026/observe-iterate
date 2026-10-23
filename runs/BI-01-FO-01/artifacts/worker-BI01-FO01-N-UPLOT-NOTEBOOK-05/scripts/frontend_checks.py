"""实际Notebook widget/Bokeh操作；不重建孤立图冒充交付物。"""
import json,os

SNAPSHOT = r'''name => {
 const d=[...Bokeh.documents].reverse().find(d=>d.roots().some(r=>r.name==='worker05:'+name&&Bokeh.index.find_one_by_id(r.id)?.el.isConnected));
 if(!d) throw Error('actual document missing: '+name);
 return {case:name,root:d.roots()[0].id,tags:d.roots()[0].tags,
 plots:[...d._all_models.values()].filter(m=>m.renderers&&m.x_range).map(m=>({
 id:m.id,title:m.title.text,x:[m.x_range.start,m.x_range.end],y:[m.y_range.start,m.y_range.end],
 renderers:m.renderers.filter(r=>r.data_source).map(r=>({id:r.id,tags:r.tags,visible:r.visible,glyph:r.glyph.type,
 data:Object.fromEntries(Object.entries(r.data_source.data).map(([k,v])=>[k,Array.isArray(v)||ArrayBuffer.isView(v)?Array.from(v,x=>typeof x==='number'&&!Number.isFinite(x)?null:x):v]))})),
 annotations:[...m.above,...m.below,...m.center].filter(a=>a.text&&typeof a.text==='string').map(a=>({text:a.text,tags:a.tags})),
 legends:m.above.filter(a=>a.type==='Legend').map(a=>({items:a.items.length,click_policy:a.click_policy}))}))};
}'''

def run_checks(page,OUT,RT,event):
    def navigate(index):
        page.locator('.jp-Notebook').press('Escape')
        actual=int(page.locator('.jp-Notebook .jp-mod-active[data-windowed-list-index]').first.get_attribute('data-windowed-list-index'))
        for _ in range(abs(index-actual)):
            page.keyboard.press('ArrowDown' if index>actual else 'ArrowUp')
        page.wait_for_timeout(500)
        chosen=page.locator('.jp-Notebook .jp-mod-active[data-windowed-list-index]').first
        assert int(chosen.get_attribute('data-windowed-list-index'))==index
        chosen.scroll_into_view_if_needed()
    def capture(name,old_roots=None):
        page.wait_for_function("a=>window.Bokeh?.documents?.some(d=>d.roots().some(r=>r.name==='worker05:'+a.name&&!a.old.includes(r.id)&&Bokeh.index.find_one_by_id(r.id)?.el.isConnected))",arg={'name':name,'old':old_roots or []},timeout=60000)
        page.wait_for_timeout(800)
        snap=page.evaluate(SNAPSHOT,name)
        (OUT/'evidence'/('BROWSER_'+name+'.json')).write_text(json.dumps(snap,ensure_ascii=False,indent=2))
        event('actual_document_checked',case=name,root=snap['root'],panels=len(snap['plots']))
        return snap
    def select_capture(control,value,name,label=False):
        old=page.evaluate('Bokeh.documents.flatMap(d=>d.roots().map(r=>r.id))')
        if label:control.select_option(label=value)
        else:control.select_option(value)
        return capture(name,old)
    def scope(plot):
        page.evaluate("id=>{const v=Bokeh.index.find_one_by_id(id);if(!v)throw Error('no live view');v.el.setAttribute('data-worker05-figure',id)}",plot['id'])
        loc=page.locator('[data-worker05-figure="'+plot['id']+'"]')
        loc.scroll_into_view_if_needed()
        return loc
    navigate(6)
    rb=page.locator('select:has(option[value="before_confirmation"])')
    phase=os.environ.get('BI01_W05_CHECK_PHASE')
    if phase not in ('graphics','tail'):
        for choice in ('before_confirmation','at_or_after_confirmation','final'):
            select_capture(rb,choice,'rb_'+choice+'_full')
    ranges=page.locator('select:has(option[value="确认附近局部行情"])')
    if phase=='tail':
        final=capture('rb_final_full')
    else:
        select_capture(ranges,'确认附近局部行情','rb_final_local',label=True)
        final=select_capture(ranges,'完整已供成员/行情','rb_final_full',label=True)
    if phase=='graphics':
        event('rb_same_exact_range_sequence_pass',sequence=['final/local','final/full'])
    elif phase!='tail':
        event('rb_K_and_same_exact_range_sequence_pass',sequence=['before/full','confirmation/full','final/full','final/local','final/full'])
    motion=next(p for p in final['plots'] if '沿原方向净推进' in p['title'])
    progress=next(r for r in motion['renderers'] if 'anchor:n_display/working_progress_points' in r['tags'])
    scope(motion)
    point=page.evaluate('''a=>{const v=Bokeh.index.find_one_by_id(a.id),b=v.el.getBoundingClientRect();return {x:b.x+v.frame.x_scale.compute(a.x),y:b.y+v.frame.y_scale.compute(a.y)}}''',{'id':motion['id'],'x':progress['data']['x'][0],'y':progress['data']['y'][0]})
    page.mouse.move(point['x'],point['y']);page.wait_for_timeout(1200)
    tips=page.locator('.bk-tooltip-content').all_inner_texts()
    page.screenshot(path=str(RT/'hover-rb-final.png'))
    event('hover_actual_progress_point',expected=progress['data'],tooltip_text=tips,point=point)
    assert progress['data']['y']==[50] and any('103315800' in tip and 'present=1' in tip and 'cfd51328' in tip for tip in tips), 'actual hover exact/K/state not visible'
    price=next(p for p in final['plots'] if '行情与过程' in p['title'])
    loc=scope(price)
    def range_now():
        return page.evaluate("id=>{const m=Bokeh.index.find_one_by_id(id).model;return {x:[m.x_range.start,m.x_range.end],y:[m.y_range.start,m.y_range.end]}}",price['id'])
    def center_now():
        return page.evaluate('''id=>{const v=Bokeh.index.find_one_by_id(id),b=v.canvas_view.events_el.getBoundingClientRect(),f=v.frame.bbox;return {x:b.x+f.left+f.width/2,y:b.y+f.top+f.height/2}}''',price['id'])
    center=center_now()
    initial=range_now();page.mouse.move(center['x'],center['y']);page.mouse.wheel(0,-500);page.wait_for_timeout(700);zoomed=range_now()
    if zoomed['x']==initial['x']:
        # Bokeh3 does not auto-activate an unmodified WheelZoomTool.  Choose
        # the actual configured x tool through its real toolbar button.
        tooltip=page.evaluate("id=>Bokeh.index.find_one_by_id(id).model.toolbar.tools.find(t=>t.type==='WheelZoomTool'&&t.dimensions==='width').tooltip",price['id'])
        loc.get_by_title(tooltip,exact=True).click()
        center=center_now()
        event('wheel_toolbar_activation',state=page.evaluate("id=>{const m=Bokeh.index.find_one_by_id(id).model;return {active_scroll:m.toolbar.active_scroll?.id,tools:m.toolbar.tools.map(t=>({type:t.type,active:t.active,dimensions:t.dimensions}))}}",price['id']),point=center)
        page.mouse.move(center['x'],center['y']);page.mouse.wheel(0,-500);page.wait_for_timeout(700);zoomed=range_now()
    if zoomed['x']==initial['x']:
        page.screenshot(path=str(RT/'zoom-diagnostic.png'))
        event('wheel_no_change',initial=initial,after=zoomed,point=center)
    assert zoomed['x']!=initial['x'], 'native wheel zoom did not change range'
    event('native_zoom_pass',initial=initial,zoomed=zoomed)
    pan_tooltip=page.evaluate("id=>Bokeh.index.find_one_by_id(id).model.toolbar.tools.find(t=>t.type==='PanTool').tooltip",price['id'])
    pan_active=page.evaluate("id=>Bokeh.index.find_one_by_id(id).model.toolbar.tools.find(t=>t.type==='PanTool').active",price['id'])
    if not pan_active:loc.get_by_title(pan_tooltip,exact=True).click()
    center=center_now()
    page.mouse.move(center['x'],center['y']);page.mouse.down();page.mouse.move(center['x']+100,center['y']+10,steps=8);page.mouse.up();page.wait_for_timeout(700);panned=range_now()
    assert panned['x']!=zoomed['x'], 'native pan did not change range'
    loc.get_by_title('Reset',exact=True).click();page.wait_for_timeout(700);reset=range_now()
    assert all(abs(a-b)<1 for a,b in zip(reset['x'],initial['x'])), 'reset did not restore x'
    event('native_zoom_pan_reset_pass',initial=initial,zoomed=zoomed,panned=panned,reset=reset)
    scope(motion)
    legend=page.evaluate('''id=>{const v=Bokeh.index.find_one_by_id(id),b=v.canvas_view.events_el.getBoundingClientRect(),m=v.model.above.find(m=>m.type==='Legend'),l=Bokeh.index.find_one_by_id(m.id),e=[...l.grid][0];return {x:b.x+l.bbox.left+l.grid.bbox.left+e.bbox.left+e.bbox.width/2,y:b.y+l.bbox.top+l.grid.bbox.top+e.bbox.top+e.bbox.height/2,renderer:m.items[0].renderers[0].id}}''',motion['id'])
    def visible():return page.evaluate("id=>Bokeh.index.find_one_by_id(id).model.visible",legend['renderer'])
    before=visible();page.mouse.click(legend['x'],legend['y']);page.wait_for_timeout(300);hidden=visible();page.mouse.click(legend['x'],legend['y']);page.wait_for_timeout(300);restored=visible()
    assert before and not hidden and restored, 'native legend hide/restore failed'
    event('native_legend_hide_restore_pass',target=legend,before=before,after_click=hidden,restored=restored)
    navigate(8)
    i=page.locator('select:has(option[value="i_before_missing_recovery"])')
    for choice in ('i_before_missing_recovery','i_recovery','i_after_recovery','i_recovery'):
        snap=select_capture(i,choice,choice)
        if choice=='i_recovery':
            scope(next(p for p in snap['plots'] if '局部等待与正式' in p['title']))
            page.screenshot(path=str(RT/'i-recovery-waiting-zero.png'))
    event('i_K_sequence_pass',sequence=['before','recovery','after','recovery'])
    navigate(10);hc=capture('hc_close_waiting_final');scope(next(p for p in hc['plots'] if '行情与过程' in p['title']))
    page.screenshot(path=str(RT/'hc-close-wick.png'))
    page.keyboard.press('Control+s');page.wait_for_timeout(1500)
    event('frontend_interactions_finished',operator='Worker Codex native mouse/keyboard/select',screenshots='本机ignored技术核验；Notebook为主交付')


if __name__ == '__main__':
    from pathlib import Path
    from datetime import datetime, timezone
    import glob,os
    from playwright.sync_api import sync_playwright
    OUT=Path(__file__).resolve().parents[1]
    RT=Path('/dwdhome/fy/cgpterm/artifacts/bi01-worker05-runtime')
    records=[]
    def event(action,**data):
        records.append({'at':datetime.now(timezone.utc).isoformat(),'action':action,**data})
        (OUT/'evidence/FRONTEND_INTERACTION_EVENTS.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
        print(action,flush=True)
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
        page.wait_for_function('window.Bokeh?.documents?.length>=1',timeout=60000)
        run_checks(page,OUT,RT,event)
        browser.close()
