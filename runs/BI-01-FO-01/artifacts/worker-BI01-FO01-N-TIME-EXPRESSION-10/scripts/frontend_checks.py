"""W06同一真实Notebook会话的限定范围/缺件/HC视口检查。"""
import json

SNAPSHOT = r'''name => {
 const d=[...Bokeh.documents].reverse().find(d=>d.roots().some(r=>r.name==='worker10:'+name&&Bokeh.index.find_one_by_id(r.id)?.el.isConnected));
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

def run_checks(page,OUT,RT,event):
    expected=json.loads((OUT/'evidence/FORMAL_CUT_EXPECTATIONS.json').read_text())
    def navigate(index):
        page.locator('.jp-Notebook:visible').press('Escape')
        cells=page.locator('.jp-Notebook:visible .jp-Cell')
        assert cells.count()==11,'本单自有windowing=none应挂载全部11 cell'
        cell=cells.nth(index);cell.scroll_into_view_if_needed()
        cell.locator('.jp-InputPrompt').first.click()
        page.wait_for_timeout(500)
        event('actual_nonvirtual_notebook_cell_selected',cell_index=index,dom_cells=cells.count())
    def roots():return page.evaluate('Bokeh.documents.flatMap(d=>d.roots().map(r=>r.id))')
    def capture(case,old=(),suffix=''):
        page.wait_for_function("a=>window.Bokeh?.documents?.some(d=>d.roots().some(r=>r.name==='worker10:'+a.name&&!a.old.includes(r.id)&&Bokeh.index.find_one_by_id(r.id)?.el.isConnected))",arg={'name':case,'old':list(old)},timeout=90000)
        page.wait_for_timeout(900);snapshot=page.evaluate(SNAPSHOT,case)
        (OUT/'evidence'/('BROWSER_'+case+suffix+'.json')).write_text(json.dumps(snapshot,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
        event('actual_live_root',case=case,root=snapshot['root'],tags=snapshot['tags']);return snapshot
    def view(s,name):return [r['data'] for p in s['plots'] for r in p['renderers'] if 'anchor:n_display/'+name in r['tags']]
    def text(s):return '\n'.join([b['text'] for b in s['badges']]+[a['text'] for p in s['plots'] for a in p['annotations']])
    def scope(p):
        page.evaluate("id=>Bokeh.index.find_one_by_id(id).el.setAttribute('data-worker10-figure',id)",p['id'])
        loc=page.locator('[data-worker10-figure="'+p['id']+'"]');loc.scroll_into_view_if_needed()
        loc.evaluate("el=>el.scrollIntoView({block:'center',inline:'nearest',behavior:'instant'})");page.wait_for_timeout(450);return loc
    def query_check(s,symbol,name):
        e=expected[symbol+'_'+name];K=e['K'];assert str(K) in text(s) and e['exact'] in text(s)
        for table,v in [('working_progress','working_progress_points'),('working_duration','working_duration_points'),
                        ('working_waiting','working_waiting_points'),('working_efficiency','working_efficiency_points'),
                        ('working_counter','working_counter_points'),('working_waiting_ratio','waiting_ratio_points')]:
            raw=e['raw_formal_values'][table];data=view(s,v)
            if raw['present']==1:
                assert len(data)==1 and data[0]['x']==[K] and data[0]['y']==[raw['value']],(name,v)
            else:assert not data,(name,v,'missing became numeric')
        assert max(view(s,'close_path')[0]['x'])<=K
        for p in s['plots']:
            if '行情与过程' not in p['title']:assert p['x']==[K-1,K+1]
        if symbol=='rb':assert ('新增recent' in text(s))==(name!='before_confirmation')
        event('query_raw_formal_and_scope_pass',case=s['case'],K=K,exact=e['exact'])
    def comparison_check(s,symbol,names):
        Ks=[expected[symbol+'_'+n]['K'] for n in names]
        assert '事后并列所列切点' in text(s) and '不是完整发生历史' in text(s)
        ranges=[]
        for p in s['plots']:
            if '行情与过程' in p['title']:continue
            ranges.append(p['x']);assert p['x'][0]<min(Ks)<max(Ks)<p['x'][1]
            assert p['y'][0]<p['y'][1]
            for r in p['renderers']:
                assert r['glyph'] not in ('Line','Segment'),('unexpected scalar line',r['tags'])
                assert all(x in Ks for x in r['data'].get('x',[]))
        assert all(r==ranges[0] for r in ranges)
        for table,v in [('working_progress','working_progress_points'),('working_duration','working_duration_points'),('working_waiting','working_waiting_points')]:
            pairs=[(expected[symbol+'_'+n]['K'],expected[symbol+'_'+n]['raw_formal_values'][table]['value']) for n in names if expected[symbol+'_'+n]['raw_formal_values'][table]['present']==1]
            data=view(s,v)
            assert (not data and not pairs) or list(zip(data[0]['x'],data[0]['y']))==pairs,(symbol,v)
        event('retrospective_true_K_points_common_axes_pass',case=s['case'],Ks=Ks,numeric_x_range=ranges[0],no_scalar_lines=True)

    navigate(6)
    rbK=page.locator('select:has(option[value="before_confirmation"])')
    rbMode=page.locator('select:has(option:has-text("事后确认两切点对照"))')
    before=capture('rb_query_before_confirmation');query_check(before,'rb','before_confirmation')
    old=roots();rbK.select_option('at_or_after_confirmation');confirm=capture('rb_query_at_or_after_confirmation',old);query_check(confirm,'rb','at_or_after_confirmation')
    assert '92400' in text(confirm) and all(role in text(confirm) for role in ('新增recent','recent移入previous','previous退出'))
    scope(next(p for p in confirm['plots'] if '行情与过程' in p['title']));page.screenshot(path=str(RT/'rb-confirmation-time-and-members.png'))
    old=roots();rbK.select_option('before_confirmation');again=capture('rb_query_before_confirmation',old,'_returned');query_check(again,'rb','before_confirmation')
    assert '新增recent' not in text(again) and 'ef2f74f6' not in text(again)
    event('rb_before_confirmation_before_actual_control_pass',roots=[before['root'],confirm['root'],again['root']])
    old=roots();rbMode.select_option(label='事后确认两切点对照');rbcmp=capture('rb_comparison',old);comparison_check(rbcmp,'rb',['before_confirmation','at_or_after_confirmation'])
    scope(next(p for p in rbcmp['plots'] if '行情与过程' in p['title']));page.screenshot(path=str(RT/'rb-retrospective-price-roles.png'))
    scope(next(p for p in rbcmp['plots'] if '沿原方向净推进' in p['title']));page.screenshot(path=str(RT/'rb-retrospective-readouts.png'))
    old=roots();rbMode.select_option(label='所选K当时可知');back=capture('rb_query_before_confirmation',old,'_after_comparison');query_check(back,'rb','before_confirmation')
    assert '事后并列所列切点' not in text(back) and '新增recent' not in text(back)
    old=roots();rbK.select_option('final');final=capture('rb_query_final',old);query_check(final,'rb','final')
    assert '同working Life/实际起点' in text(final) and '不是新过程' in text(final) and '中间从未更新' in text(final)
    scope(next(p for p in final['plots'] if '局部等待与正式' in p['title']));page.screenshot(path=str(RT/'rb-final-same-life-clock.png'))
    event('rb_comparison_query_axis_isolation_and_final_reference_pass')

    navigate(8)
    iK=page.locator('select:has(option[value="i_before_missing_recovery"])')
    iMode=page.locator('select:has(option:has-text("事后三切点对照"))')
    prior=capture('i_query_i_before_missing_recovery');query_check(prior,'i','i_before_missing_recovery')
    snapshots=[prior]
    for name in ('i_recovery','i_after_recovery','i_before_missing_recovery'):
        old=roots();iK.select_option(name);s=capture('i_query_'+name,old,'_returned' if name=='i_before_missing_recovery' else '')
        query_check(s,'i',name);snapshots.append(s)
        if name=='i_after_recovery':
            assert '局部计时' in text(s) and 'waiting=600' in text(s) and 'last_update仍缺' in text(s)
            scope(next(p for p in s['plots'] if '局部等待与正式' in p['title']));page.screenshot(path=str(RT/'i-after-local-clock-persists.png'))
    assert '局部计时：waiting=' not in text(snapshots[-1])
    event('i_before_recovery_after_before_actual_control_pass',roots=[s['root'] for s in snapshots],persistent_local_clock_after_zero=True)
    old=roots();iMode.select_option(label='事后三切点对照');icmp=capture('i_comparison',old)
    comparison_check(icmp,'i',['i_before_missing_recovery','i_recovery','i_after_recovery'])
    scope(next(p for p in icmp['plots'] if '当前过程年龄' in p['title']));page.screenshot(path=str(RT/'i-retrospective-age-and-missing.png'))
    scope(next(p for p in icmp['plots'] if '局部等待与正式' in p['title']));page.screenshot(path=str(RT/'i-retrospective-local-clock.png'))
    # 真正hover原点，核完整Life/exact/原状态，而不是只读Python模型。
    motion=next(p for p in icmp['plots'] if '沿原方向净推进' in p['title']);scope(motion)
    progress=view(icmp,'working_progress_points')[0]
    point=page.evaluate('''a=>{const v=Bokeh.index.find_one_by_id(a.id),b=v.el.getBoundingClientRect();return {x:b.x+v.frame.x_scale.compute(a.x),y:b.y+v.frame.y_scale.compute(a.y)}}''',{'id':motion['id'],'x':progress['x'][-1],'y':progress['y'][-1]})
    page.mouse.move(point['x'],point['y']);page.wait_for_timeout(1000)
    tips=page.locator('.bk-tooltip-content').all_inner_texts()
    assert any('5727e951-20b6-4a82-8c52-fc3a32f686cc' in t and 'b4de4558' in t and 'present=1' in t for t in tips)
    page.screenshot(path=str(RT/'i-comparison-full-identity-hover.png'))
    event('actual_hover_full_life_exact_state_pass',tooltip_text=tips)
    old=roots();iMode.select_option(label='所选K当时可知');q=capture('i_query_i_before_missing_recovery',old,'_after_comparison');query_check(q,'i','i_before_missing_recovery')
    assert '事后并列所列切点' not in text(q) and '局部计时：waiting=' not in text(q)
    page.keyboard.press('Control+s');page.wait_for_timeout(1200)
    event('frontend_interactions_finished',qualification='本单实际新时间表达/回看；新用途仍待原Pro与管理判断，无平台操作')
