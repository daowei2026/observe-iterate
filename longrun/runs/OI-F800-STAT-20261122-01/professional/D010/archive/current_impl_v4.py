"""C2当前原型 / C3实现：实例、只读reader、context、位置、字段均注入。

组合锁定CAEGraph与既有Bokeh API；不修改uplot，不运行真实Feature。
reader(instance, position)只返回已物化DataFrame，契约见INJECTION_CONTRACT。
"""
from html import escape
import json
import uuid
import numpy as np
import pandas as pd
from bokeh.layouts import column
from bokeh.core.properties import value as literal_value
from bokeh.models import (Div,DataTable,TableColumn,HoverTool,TapTool,CustomJS,
                          FixedTicker,CrosshairTool,Select)
from mquant.frame import DoFunctionFao,GMap
from mquant.uplot import (CAEGraph,PlotSet,PerSymFigs,KPriceLine,MulFieldsGlyphs,
                          MulSegPlot,AllSymsFig)
from mquant.uplot.utlv2 import CurrSymbol

_READ_ONLY={}
class InjectedFrames(DoFunctionFao):
    """只读分析入口；rerun只读内存表，不进入真实Feature/生产/存储。"""
    params=lambda:dict(token='')
    @property
    def that(self):return self
    def rerun(self,*args,**kwargs):return self
    def to_dfs(self):return _READ_ONLY[self.P.token](CurrSymbol.sym(False))
    def to_df(self):return self.to_dfs()['value']

def provider(getter):
    token=uuid.uuid4().hex;_READ_ONLY[token]=getter
    return InjectedFrames(token=token)

def axis_columns(df,parents):
    if set(parents).issubset(df.columns):return df.copy()
    out=df.reset_index()
    if not set(parents).issubset(out.columns):raise ValueError(f'缺失完整父坐标：{parents}')
    return out

def exact_int(v):
    if isinstance(v,(int,np.integer)) and not isinstance(v,(bool,np.bool_)):return int(v)
    if isinstance(v,str) and v.lstrip('-').isdigit():return int(v)
    raise ValueError('身份整数必须以int或十进制文本注入；拒绝浮点ID')

def decode_exact(frame,columns):
    out=[]
    for row in frame[list(columns.values())].to_dict('records'):
        form=exact_int(row[columns['form']])
        if form==1:
            high=exact_int(row[columns['high']]);low=exact_int(row[columns['low']])
            if not (0<=high<2**64 and 0<=low<2**64):raise ValueError('UUID word超出uint64')
            out.append(str(uuid.UUID(int=(high<<64)|low)))
        elif form==2:
            text=row[columns['text']]
            if text is None or text is pd.NA or not str(text):raise ValueError('文本exact身份缺失')
            out.append(str(text))
        else:raise ValueError('主组exact身份必须为已确认UUID或Text形式')
    return pd.Series(out,index=frame.index,dtype=object)

def project(frame,mapping):
    required={v for spec in mapping.values() for v in (spec.values() if isinstance(spec,dict) else [spec])}
    missing=required-set(frame.columns)
    if missing:raise ValueError(f'缺失约定字段：{sorted(missing)}')
    # 附加别名但保留原始输入字段。原始JSON文字避免JS对64位数字做浮点转换。
    out=frame.copy()
    out['__original_json']=[json.dumps(row,ensure_ascii=False) for row in raw_records(frame)]
    for k,spec in mapping.items():out[k]=decode_exact(frame,spec) if isinstance(spec,dict) else frame[spec]
    return out

def scalar(v):
    if v is None or v is pd.NA:return None
    if isinstance(v,(pd.Timestamp,np.datetime64)):return str(pd.Timestamp(v))
    if isinstance(v,(np.bool_,bool)):return bool(v)
    if isinstance(v,(np.integer,int)):return int(v)
    if isinstance(v,(np.floating,float)):return float(v) if np.isfinite(v) else str(v)
    return str(v)

def raw_records(df):return [{str(k):scalar(v) for k,v in row.items()} for row in df.to_dict('records')]
def key(row,parents):return tuple(scalar(row[p]) for p in parents)

def point(feat,table,x,y,label,marker='circle',color='#1d4ed8',size=9):
    return MulFieldsGlyphs(feats=GMap({'source':feat}),dfkeys=[table],xfields=[x],yfields=[y],
        glyphs=marker,legend_labels=[label],colors=[color],size=size,alphas=0.9,dynstd_method=False)

def segment(feat,table,x0,x1,y0,y1,label,color,dash='solid'):
    return MulSegPlot(feats=GMap({'source':feat}),dfkeys=[table],x0s=[x0],x1s=[x1],y0s=[y0],y1s=[y1],
        timefieldtype='uti',legend_labels=[label],colors=[color],line_widths=2,line_dashs=dash,
        dynstd_method=False,hover=True)

def clipped(df,x0,x1,y0,y1,lo,hi):
    """仅裁剪显示线段；原始业务值仍在raw记录。"""
    d=df.copy()
    if d.empty:
        for c in ('draw_x0','draw_x1','draw_y0','draw_y1'):d[c]=pd.Series(dtype=float)
        return d
    d=d[np.isfinite(d[x0])&np.isfinite(d[x1])&np.isfinite(d[y0])&np.isfinite(d[y1])]
    d=d[(d[x1]>=lo)&(d[x0]<=hi)].copy()
    if (d[x1]<d[x0]).any():raise ValueError('线段端点次序冲突，不能自动更改业务语义')
    dx=d[x1]-d[x0]
    d['draw_x0']=d[x0].clip(lo,hi);d['draw_x1']=d[x1].clip(lo,hi)
    f0=np.where(dx!=0,(d.draw_x0-d[x0])/dx.replace(0,1),0)
    f1=np.where(dx!=0,(d.draw_x1-d[x0])/dx.replace(0,1),0)
    d['draw_y0']=d[y0]+(d[y1]-d[y0])*f0;d['draw_y1']=d[y0]+(d[y1]-d[y0])*f1
    return d.sort_values('draw_x0',kind='stable')

def walk(nodes,path=()):
    for n in nodes:
        p=(*path,n.name)
        if hasattr(n,'cds'):yield p,n
        else:yield from walk(n.children,p)

def attach(fig,cds,metadata,name,tooltips):
    n=len(cds.data.get('x',cds.data.get('x0',[])))
    if len(metadata)!=n:raise ValueError(f'{name}元数据/图元行数不一致：{len(metadata)} != {n}')
    dd=dict(cds.data)
    for c in (metadata[0] if metadata else ('raw',)):dd[c]=[m[c] for m in metadata]
    cds.data=dd;cds.name=name
    rr=[r for r in fig.renderers if getattr(r,'data_source',None) is cds]
    for h in list(fig.tools):
        if isinstance(h,HoverTool) and any(r in h.renderers for r in rr):fig.tools.remove(h)
    fig.add_tools(HoverTool(renderers=rr,tooltips=tooltips))
    return rr

def build_display(*,instance,reader,context,position,fields,caption):
    if not position['symbols']:raise ValueError('symbols不能为空')
    data=reader(instance,position);parents=fields['parents']
    rawg=axis_columns(data['groups'],parents)
    if rawg.duplicated(parents).any():raise ValueError('主组完整父坐标重复，拒绝自动合并')
    g=project(rawg,fields['groups'])
    for p in parents:g[p]=rawg[p]
    for f in ('known','original_anchor','original_d','original_r','anchor','d','r'):
        if g[f].isna().any() or not pd.api.types.is_integer_dtype(g[f]):raise ValueError(f'{f}须为无缺值整型UTI，禁止从float猜回')
    if g[['life','revision']].isna().any().any() or (g[['life','revision']].astype(str)=='').any().any():raise ValueError('exact身份缺失')
    for role in ('basis','observation'):
        numeric={str(v) for v in g[role] if isinstance(v,(int,np.integer))}
        if numeric-set(fields.get('labels',{}).get(role,{})):raise ValueError(f'{role}数值编码须注入同版已核实名称映射')
    if (g.anchor>g.d).any() or (g.d>g.r).any():raise ValueError('a/d/r次序冲突')
    utsa=context.sof.tsa_of(position['calendar'])['natural_tsa']
    try:lo,hi=int(position['start']),int(position['end'])+1
    except (ValueError,TypeError):lo,hi=np.searchsorted(utsa,pd.to_datetime([position['start'],position['end']]).values);hi+=1
    lo=max(0,int(lo));hi=min(len(utsa),int(hi))
    if lo>=hi:raise ValueError('位置范围为空')
    if len(g) and ((g.known<0)|(g.known>=len(utsa))).any():raise ValueError('known超出当前日历')
    g=g[(g.known>=lo)&(g.known<hi)].sort_values(['known',*parents],kind='stable').reset_index(drop=True)
    g['row']=np.arange(len(g),dtype=np.int64);g['lane']=g.row.astype(float)
    child_maps={}
    for name,df in data.get('children',{}).items():
        rows={}
        for r in axis_columns(df,parents).to_dict('records'):rows.setdefault(key(r,parents),[]).append({str(k):scalar(v) for k,v in r.items()})
        child_maps[name]=rows
    rawmap={key(r,parents):{str(k):scalar(v) for k,v in r.items()} for r in rawg.to_dict('records')}
    for name,rows in child_maps.items():
        if set(rows)-set(rawmap):raise ValueError(f'{name}含无法按完整父键关联的子行')
    part=fields['participation'];records=[]
    for _,r in g.iterrows():
        k=key(r,parents);children={name:rows.get(k,[]) for name,rows in child_maps.items()};pr=children.get(part['table'],[])
        def pvalues(f):return json.dumps([v.get(f) for v in pr],ensure_ascii=False) if pr else 'NOT_PUBLISHED'
        label=lambda f:str(fields.get('labels',{}).get(f,{}).get(str(r[f]),r[f]))
        payload={'group':rawmap[k],'children':children,'metadata':data.get('metadata',{}),
            'display_only':{'row':int(r.row),'window_clipped':bool(r.anchor<lo or r.r>=hi),'history_projection':'NOT_ASOF_REPLAY'},'limits':fields.get('limits',[])}
        records.append(dict(seq=f'#{int(r.row)+1:04d}',life=str(r.life),revision=str(r.revision),basis=label('basis'),observation=label('observation'),
            coverage=str(scalar(r.coverage)),closed=str(scalar(r.closed)),duty=pvalues(part['duty']),admission=pvalues(part['admission']),handoff=pvalues(part['handoff']),
            parent=json.dumps(list(k),ensure_ascii=False),known=str(int(r.known)),a=str(int(r.anchor)),d=str(int(r.d)),r=str(int(r.r)),raw=json.dumps(payload,ensure_ascii=False,indent=2)))
    g['y0']=g.lane;g['y1']=g.lane
    windows=clipped(g,'anchor','d','y0','y1',lo,hi-1);tails=clipped(g,'d','r','y0','y1',lo,hi-1)
    gf=provider(lambda _:dict(groups=g,windows=windows,tails=tails))
    selected={s:project(data['selected'][s],fields['selected']) for s in position['symbols']}
    raw={s:project(data['raw'][s],fields['raw']) for s in position['symbols']}
    for i,s in enumerate(position['symbols']):selected[s]['lane']=i+pd.to_numeric(selected[s]['round'])*0.15
    turns=provider(lambda s:dict(turns=selected[s],links=clipped(selected[s],'actual','confirmation','price','cprice',lo,hi-1)))
    rf=provider(lambda s:{'raw':raw[s]})
    klines={s:project(data['klines'][s],fields['kline']) for s in position['symbols']}
    kfeat=provider(lambda s:{'value':klines[s]})
    prices=PerSymFigs(title='!{sym} · 原价 / 已暴露原始转折与已选T、C',fig_height=210,plots=GMap({
        'k':KPriceLine(feat=kfeat,std_method=None,label='原价 K'),
        'raw':point(rf,'raw','actual','price','Rct实际（上游已暴露）','x','#64748b',6),
        'tc':segment(turns,'links','draw_x0','draw_x1','draw_y0','draw_y1','同记录 T→C','#94a3b8'),
        't':point(turns,'turns','actual','price','Selected T实际','circle','#1d4ed8'),
        'c':point(turns,'turns','confirmation','cprice','Selected C几何确认','diamond','#a21caf')}))
    inputs=AllSymsFig(title='输入已知轴 · ScaleTurn原事件（行=品种；+0.15×round仅为显示偏移）',fig_height=170,
        persym_plots=GMap({'selected':point(turns,'turns','known','lane','上游selected已知','x','#b45309')}))
    outplots=GMap({'window':segment(gf,'windows','draw_x0','draw_x1','draw_y0','draw_y1','本次携带 a→d','#cbd5e1'),
        'tail':segment(gf,'tails','draw_x0','draw_x1','draw_y0','draw_y1','本次携带 d→r','#a855f7','dashed'),
        'revision':point(gf,'groups','known','lane','Sparse exact revision','circle','#0f766e',11)})
    # sym_plots只提供合法绘图上下文；全局数据不按此symbol过滤。单/多品种均可替换。
    output=AllSymsFig(title='候选组 exact修订 · 点=发布，段=本次携带界限（非连续状态轨迹）',fig_height=390,
        sym_plots=GMap({position['symbols'][0]:outplots}),fit_y_range=False)
    graph=CAEGraph(Context=context,plotsets=GMap({'expectation':PlotSet(calendar_name=position['calendar'],blk=list(position['symbols']),
        timespans=[(position['start'],position['end'])],figs=GMap({'prices':prices,'input':inputs,'output':output}))}),
        fig_width=position.get('width',1180),x_label_freq=position.get('label_freq','60m'),extra_time=0,plot_name='C2 current / C3 injectable renderer')
    roots=[];body=graph.layout(plot_roots=roots);figs=list(body.children[0].children[0].children)
    for f in figs:f.add_tools(CrosshairTool(dimensions='height'));f.x_range.start=lo;f.x_range.end=hi-1
    for f in figs[:len(position['symbols'])]:f.yaxis.axis_label='原价（未标准化）'
    ip,op=figs[-2:]
    for legend in op.legend:
        for item in legend.items:
            value=getattr(item.label,'value',None)
            if value is not None:item.label=literal_value(value.removeprefix(position['symbols'][0]+' - '))
    ip.yaxis.ticker=FixedTicker(ticks=list(range(len(position['symbols']))));ip.yaxis.major_label_overrides={i:s for i,s in enumerate(position['symbols'])}
    op.yaxis.axis_label='修订显示行；不编码状态'
    ticks=np.unique(np.linspace(0,max(0,len(g)-1),min(10,len(g))).astype(int)).tolist() if len(g) else []
    op.yaxis.ticker=FixedTicker(ticks=ticks);op.yaxis.major_label_overrides={i:records[i]['seq'] for i in ticks}
    source=None;glyphs=[]
    for path,n in walk(roots):
        if n.name.startswith('Sparse exact revision:'):
            source=n.cds
            if list(source.data['x'])!=g.known.tolist() or list(source.data['y'])!=g.lane.tolist():raise ValueError('原生修订点顺序变化')
            glyphs=attach(op,source,records,'revision_source',[
                ('行','@seq'),('Life','@life'),('Revision','@revision'),('父坐标','@parent'),('known UTI','@known'),('local basis','@basis'),
                ('observation','@observation'),('coverageIncomplete','@coverage'),('formation closed','@closed'),('dutyClosed[]','@duty'),('a / d / r','@a / @d / @r'),('admission[]','@admission')])
            if not records:
                dd=dict(source.data)
                for c in ('seq','life','revision','basis','observation','coverage','closed','duty','admission','handoff','parent','known','a','d','r'):dd[c]=[]
                source.data=dd
        role=next((v for v in ('Selected T实际','Selected C几何确认','上游selected已知','Rct实际（上游已暴露）') if n.name.startswith(v+':')),None)
        if role:
            sym=next((s for s in position['symbols'] if any(p=='sym: '+s or p.startswith('sym: '+s+' -') for p in path)),None)
            if sym is None:raise ValueError('上游图元无法定位品种上下文')
            israw=role.startswith('Rct');frame=raw[sym] if israw else selected[sym]
            xcol='actual' if israw or role.startswith('Selected T') else ('confirmation' if role.startswith('Selected C') else 'known')
            frame=frame[(frame[xcol]>=lo)&(frame[xcol]<hi)]
            md=[{'raw':json.dumps(row,ensure_ascii=False)} for row in raw_records(frame)]
            f=ip if role=='上游selected已知' else figs[list(position['symbols']).index(sym)]
            attach(f,n.cds,md,f'input:{sym}:{role}',[('位置','@ts'),('原值','@y'),('同记录原值/turn/round/各位置','@raw')])
    if source is None:raise ValueError('没有原生修订点源')
    table=DataTable(source=source,columns=[TableColumn(field=c,title=t,width=w) for c,t,w in (
        ('seq','行',65),('life','Life',150),('revision','Revision',160),('basis','local basis',110),('observation','observation',150),
        ('coverage','coverageIncomplete',120),('closed','formation closed',110),('duty','dutyClosed[]',110),('parent','完整父坐标',260))],
        width=position.get('width',1180),height=230,index_position=None,selectable=True,reorderable=False,name='revision_table')
    detail=Div(text='<p>选择修订行或点击发布点，查看该exact修订及全部已发行子表原值。空子列表不等于0或失败。</p>',
        width=position.get('width',1180),height=280,styles={'overflow':'auto','border':'1px solid #cbd5e1'},name='exact_detail')
    cb=CustomJS(args=dict(source=source,detail=detail),code="""
const rows=source.selected.indices;if(!rows.length)return;const i=rows[0];
const esc=x=>String(x).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
detail.text='<h3>'+esc(source.data.seq[i])+' · '+esc(source.data.life[i])+' / '+esc(source.data.revision[i])+'</h3><pre style="white-space:pre-wrap">'+esc(source.data.raw[i])+'</pre>';
""")
    source.selected.js_on_change('indices',cb);op.add_tools(TapTool(renderers=glyphs))
    chooser=Select(title='定位 exact修订（完整父坐标见表/hover）',options=[('','请选择修订')]+[(str(i),f"{r['seq']} {r['life']} / {r['revision']}") for i,r in enumerate(records)],value='',width=700,name='exact_chooser')
    chooser.js_on_change('value',CustomJS(args=dict(source=source),code="if(cb_obj.value!=='' && source.selected.indices[0]!==Number(cb_obj.value)){source.selected.indices=[Number(cb_obj.value)];}"))
    source.selected.js_on_change('indices',CustomJS(args=dict(source=source,chooser=chooser),code="if(source.selected.indices.length && chooser.value!==String(source.selected.indices[0])){chooser.value=String(source.selected.indices[0]);}"))
    header=Div(text='<h2>F800 · C2当前展示预期</h2><p>'+escape(caption)+'</p><p>阅读：原价/T与C → 上游已知轴 → 候选exact修订/携带界限 → 独立状态与原值明细。'
        '纵轴为原价或显示行；不标准化。历史位置投影，不是as-of回放。</p><p><b>点是稀疏发布；a→d、d→r仅为当前修订携带的界限，可被视区裁剪。'
        '形成关闭与责任关闭分别读。逐tick材料准入/first blocker/原生coverage区间 NOT_EXPOSED；不能由线段反推。</b></p>',width=1180)
    note=Div(text='<p>修订行仅为显示序号。同刻不同观点分别成行。点击点、表或下拉框查看完整父子坐标及原值；状态各列独立，NOT_PUBLISHED不等于0。原始JSON以文本保留64位身份整数。</p>',width=1180)
    return column(header,body,note,chooser,table,detail),dict(graph=graph,roots=roots,groups=g,data=data,revision_source=source,records=records,
        fig_count=len(figs),shared_x_range=len({f.x_range.id for f in figs})==1,readonly_provider=True,html_semantics='F800-C2-v4')
