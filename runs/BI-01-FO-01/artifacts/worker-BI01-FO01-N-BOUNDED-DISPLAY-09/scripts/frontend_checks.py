"""W06同一真实Notebook会话的限定范围/缺件/HC视口检查。"""
import json

SNAPSHOT = r'''name => {
 const d=[...Bokeh.documents].reverse().find(d=>d.roots().some(r=>r.name==='worker09:'+name&&Bokeh.index.find_one_by_id(r.id)?.el.isConnected));
 if(!d) throw Error('actual live document missing: '+name);
 const clean=v=>Array.isArray(v)||ArrayBuffer.isView(v)?Array.from(v,x=>typeof x==='number'&&!Number.isFinite(x)?null:x):v;
 return {case:name,root:d.roots()[0].id,tags:d.roots()[0].tags,
 badges:[...d._all_models.values()].filter(m=>m.type==='Div').map(m=>({id:m.id,text:m.text})),
 plots:[...d._all_models.values()].filter(m=>m.renderers&&m.x_range).map(m=>({
 id:m.id,title:m.title.text,x:[m.x_range.start,m.x_range.end],y:[m.y_range.start,m.y_range.end],
 renderers:m.renderers.filter(r=>r.data_source).map(r=>({id:r.id,tags:r.tags,visible:r.visible,glyph:r.glyph.type,
 data:Object.fromEntries(Object.entries(r.data_source.data).map(([k,v])=>[k,clean(v)]))})),
 value_labels:[...m.above,...m.below,...m.center].filter(a=>a.type==='LabelSet').map(a=>({id:a.id,tags:a.tags,
 x_offset:a.x_offset?.value??a.x_offset,y_offset:a.y_offset?.value??a.y_offset,data:Object.fromEntries(Object.entries(a.source.data).map(([k,v])=>[k,clean(v)]))})),
 annotations:[...m.above,...m.below,...m.center].filter(a=>a.text&&typeof a.text==='string').map(a=>({id:a.id,text:a.text,tags:a.tags,x:a.x,y:a.y,text_align:a.text_align}))}))};
}'''

def run_checks(page, OUT, RT, event):
    def navigate(index):
        page.locator('.jp-Notebook:visible').press('Escape')
        active=page.locator('.jp-Notebook:visible .jp-mod-active[data-windowed-list-index]').first
        actual=int(active.get_attribute('data-windowed-list-index'))
        for _ in range(abs(index-actual)):
            page.keyboard.press('ArrowDown' if index>actual else 'ArrowUp')
        page.wait_for_timeout(500)
        active=page.locator('.jp-Notebook:visible .jp-mod-active[data-windowed-list-index]').first
        assert int(active.get_attribute('data-windowed-list-index'))==index
        active.scroll_into_view_if_needed()

    def capture(case, suffix='', previous=()):
        page.wait_for_function("a=>window.Bokeh?.documents?.some(d=>d.roots().some(r=>r.name==='worker09:'+a.name&&!a.old.includes(r.id)&&Bokeh.index.find_one_by_id(r.id)?.el.isConnected))",
                               arg={'name':case,'old':list(previous)},timeout=60000)
        page.wait_for_timeout(800)
        snapshot=page.evaluate(SNAPSHOT,case)
        (OUT/'evidence'/('BROWSER_'+case+suffix+'.json')).write_text(json.dumps(snapshot,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
        event('current_live_root_captured',case=case,suffix=suffix,root=snapshot['root'],tags=snapshot['tags'])
        return snapshot

    def current_roots():
        return page.evaluate('Bokeh.documents.flatMap(d=>d.roots().map(r=>r.id))')

    def scope(plot):
        page.evaluate("id=>Bokeh.index.find_one_by_id(id).el.setAttribute('data-worker09-figure',id)",plot['id'])
        loc=page.locator('[data-worker09-figure="'+plot['id']+'"]')
        loc.scroll_into_view_if_needed()
        loc.evaluate("el=>el.scrollIntoView({block:'center',inline:'nearest',behavior:'instant'})")
        page.wait_for_timeout(400)
        return loc

    def view(snapshot, name):
        return [r['data'] for p in snapshot['plots'] for r in p['renderers'] if 'anchor:n_display/'+name in r['tags']]

    def badges(snapshot):
        return '\n'.join(b['text'] for b in snapshot['badges'])

    navigate(6)
    first=capture('rb_final_full','_before')
    control=page.locator('select:has(option[value="确认附近局部行情"])')
    old=current_roots();control.select_option(label='确认附近局部行情')
    local=capture('rb_final_local',previous=old)
    assert '局部价图仅显示所选范围；两完成窗统计仍取该K原成员；视域外过程边界未显示，不表示正式源缺失。' in badges(local)
    assert '原输入缺值提示：0；输入未覆盖/未提供：0；视域省略：' in badges(local)
    assert '103140000' in badges(local) and '100443000' in badges(local)
    old=current_roots();control.select_option(label='完整已供成员/行情')
    final=capture('rb_final_full',previous=old)
    fields=('completed_recent_updates','completed_previous_updates','working_progress_points',
            'working_counter_points','working_efficiency_points','working_waiting_points','waiting_ratio_points')
    for field in fields:
        assert view(first,field)==view(local,field)==view(final,field),field
    assert len({first['root'],local['root'],final['root']})==3
    event('rb_full_local_full_scope_and_formal_identity_pass',roots=[first['root'],local['root'],final['root']],scalar_views=list(fields),
          local_actual_badges=badges(local),formal_k=103315800)
    # Return to local through the real control for a current-page screenshot.
    old=current_roots();control.select_option(label='确认附近局部行情')
    local=capture('rb_final_local','_visible',previous=old)
    price=next(p for p in local['plots'] if '行情与过程' in p['title']);scope(price)
    page.screenshot(path=str(RT/'rb-local-live.png'))

    native_graph_checks(page,local,RT,event,scope)
    navigate(8)
    recovery=capture('i_recovery')
    price_data=view(recovery,'close_path')[0]
    assert price_data['y'].count(None)==24
    assert view(recovery,'working_waiting_points')[0]['y']==[0]
    assert not view(recovery,'working_efficiency_points') and not view(recovery,'working_counter_points')
    assert not view(recovery,'waiting_ratio_points')
    assert '原输入close缺值24行' in badges(recovery)
    assert any('路径效率缺' in a['text'] for p in recovery['plots'] for a in p['annotations'])
    for field,value in [('working_progress_points',12),('working_duration_points',42000)]:
        labels=[a for p in recovery['plots'] for a in p['value_labels'] if 'view:'+field in a['tags']]
        assert len(labels)==1 and labels[0]['data']['y']==[value] and labels[0]['y_offset']<0
    event('i_compact_top_numeric_labels_actual_consumer_check',values=[12,42000],qualification='当前LabelSet向内放置，仍需Worker实际像素确认')
    for title,filename in [('沿原方向净推进','i-progress-live.png'),('当前过程年龄','i-duration-live.png')]:
        scope(next(p for p in recovery['plots'] if title in p['title']))
        page.screenshot(path=str(RT/filename))
    scope(next(p for p in recovery['plots'] if '局部等待与正式' in p['title']))
    page.screenshot(path=str(RT/'i-real-missing-and-zero.png'))
    event('i_actual_24_price_nulls_formal_missing_and_waiting_zero_pass',root=recovery['root'],missing_price_rows=24,waiting=0)

    selector=page.locator('select:has(option[value="i_before_missing_recovery"])')
    for choice in ('i_after_recovery','i_recovery'):
        old=current_roots();selector.select_option(choice)
        capture(choice,'_crossk',previous=old)
    event('i_crossk_then_recovery_pass',qualification='其他K仅工作2准备/回归，不扩大平台认可')
    navigate(10)
    hc=capture('hc_close_waiting_final')
    price=next(p for p in hc['plots'] if '行情与过程' in p['title'])
    scope(price)
    def viewport():
        return page.evaluate('''id=>{const v=Bokeh.index.find_one_by_id(id),rect=v.el.getBoundingClientRect();
          const stack=document.querySelector('#jp-left-stack');const s=stack?.getBoundingClientRect();
          const scroller=[...document.querySelectorAll('.jp-Notebook')].find(e=>e.clientWidth>0);
          return {window:[innerWidth,innerHeight],devicePixelRatio,figure:{x:rect.x,y:rect.y,width:rect.width,height:rect.height},
          left_stack:s?{width:s.width,display:getComputedStyle(stack).display}:null,
          notebook:scroller?{width:scroller.clientWidth,scrollWidth:scroller.scrollWidth,scrollLeft:scroller.scrollLeft}:null};}''',price['id'])
    before=viewport()
    page.screenshot(path=str(RT/'hc-live-before-sidebar.png'))
    page.keyboard.press('Control+b');page.wait_for_timeout(800);scope(price)
    after=viewport()
    page.screenshot(path=str(RT/'hc-live-after-sidebar.png'))
    assert price['x'][1]>=103315800
    assert any('103315800' in str(r['data'].get('x',[])) and '3904' in str(r['data'].get('y',[])) for r in price['renderers'])
    event('hc_actual_sidebar_toggle_live_view',root=hc['root'],before=before,after=after,
          actual_annotations=price['annotations'],pixel_qualification='截图已真实生成；Worker随后view_image实际查看，可读性结论另记，非CDS即通过')
    # Capture all related panels in this same live output for independent unit
    # and visibility checks; screenshots stay only in ignored local artifacts.
    for title,filename in (('沿原方向净推进','hc-motion-live.png'),('局部等待与正式','hc-waiting-live.png'),('局部等待倍数','hc-ratio-live.png')):
        match=[p for p in hc['plots'] if title in p['title']]
        if match:
            scope(match[0]);page.screenshot(path=str(RT/filename))
    page.keyboard.press('Control+s');page.wait_for_timeout(1500)
    event('frontend_interactions_finished',operator='Worker Codex via actual Playwright keyboard/select',browser_evidence='当前同kernel root与本次Notebook；非孤立layout')


def native_graph_checks(page,final,RT,event,scope):
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
        # Jupyter大输出可能只露出价格框的一部分；实际wheel/pan必须落在
        # 可见canvas内，而不是屏幕底部status bar。只选鼠标位置，不改range。
        return page.evaluate('''id=>{const v=Bokeh.index.find_one_by_id(id),b=v.canvas_view.events_el.getBoundingClientRect(),f=v.frame.bbox;
          const left=Math.max(b.x+f.left,40),right=Math.min(b.x+f.right,innerWidth-40);
          const top=Math.max(b.y+f.top,90),bottom=Math.min(b.y+f.bottom,innerHeight-50);
          if(right-left<30||bottom-top<30)throw Error('actual canvas has insufficient visible interaction area');
          return {x:(left+right)/2,y:(top+bottom)/2,visible_frame:{left,right,top,bottom}}}''',price['id'])
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
