"""仅C2预览的合成样例绑定；不得当作B最终位置或真实Feature结果。"""
from pathlib import Path
import hashlib
import json
import sys
import numpy as np
import pandas as pd
from bokeh.embed import file_html
from bokeh.resources import INLINE
from mquant.uplot.utlv2 import OptContext
import prototype

ROOT=Path(__file__).resolve().parent
VERSION=sys.argv[1] if len(sys.argv)>1 else 'v1'
position=dict(symbols=['rb','hc','i'],start='2022-06-15 09:00',end='2022-06-30 15:00',calendar='night_end_at_2300',width=1180,label_freq='120m')
context=OptContext(sof_name='TA_updto20240229_DBA',stk_tlist='steel',startDay='2022-06-01',endDay='2022-06-30')
tsa=context.sof.tsa_of(position['calendar'])['natural_tsa']
u0,u1=np.searchsorted(tsa,pd.to_datetime([position['start'],position['end']]).values)
u0=int(u0);u1=int(u1)
xs=np.arange(u0,u1-600,600,dtype=np.int64)
klines={};selected={};raw={}
for i,sym in enumerate(position['symbols']):
    y=(4500.,4900.,900.)[i]+(40.,45.,18.)[i]*np.sin(np.arange(len(xs))/19+i)+np.arange(len(xs))*0.015
    op=y+np.cos(np.arange(len(xs)))*2
    klines[sym]=pd.DataFrame(dict(open=op,close=y,high=np.maximum(op,y)+3,low=np.minimum(op,y)-3,
        volume=np.full(len(xs),100.),openUti=xs,closeUti=xs+599),index=pd.DatetimeIndex(tsa[xs],name='timestamp'))
    klines[sym].iloc[25,klines[sym].columns.get_loc('close')]=np.nan
    actual=u0+np.array([6000,180000,330000])+i*300
    conf=actual+np.array([6000,9000,12000]);known=conf+np.array([1200,600,1800])
    px=np.interp(actual,xs,y);cp=np.interp(conf,xs,y)
    selected[sym]=pd.DataFrame(dict(actual=actual,confirmation=conf,known=known,price=px,cprice=cp,
        turn=[f'SYN-{sym}-T{k}' for k in range(3)],round=[0,1,0],t_known=actual+300,c_known=conf+300))
    raw[sym]=selected[sym].copy()

offs=[210000,211200,211200,486000,486600,489600]
life=['SYN-Life-A','SYN-Life-A','SYN-Life-B','SYN-Life-A','SYN-Life-B','SYN-Life-A']
revision=['SYN-A-r1','SYN-A-r2','SYN-B-r1','SYN-A-r3','SYN-B-r2','SYN-A-r4']
anchor=np.array([6000,6000,6600,6000,6600,6000])+u0
known=np.array(offs)+u0
groups=pd.DataFrame(dict(timestamp=pd.to_datetime(tsa[known]),occurrence=[0,1,1,2,3,4],record_id=0,child_id_2=[0,0,1,0,0,0],
    life=life,revision=revision,known=known,original_anchor=anchor,original_d=anchor+480000,original_r=anchor+483600,
    anchor=anchor,d=anchor+480000,r=anchor+483600,basis=['Incomplete','Supported','Supported','Supported','Supported','Supported'],
    observation=['Open','Open','Open','Subsumed','ClosedSupported','Subsumed'],coverage=[True,False,False,False,False,False],
    closed=[False,False,False,True,True,True]))
children={}
for tab in ('members','previous','required','participation','alternatives','bridges'):
    rows=[]
    for j,g in groups.iterrows():
        row={k:g[k] for k in ('timestamp','occurrence','record_id','child_id_2')}
        row['child_id_3']=0
        if tab=='participation': row.update(admissionKnown=u0+(210000 if g.life.endswith('A') else 211200),dutyClosed=bool(j==5),handoffEnd=int(g.r+10800))
        elif tab=='previous':
            if j not in (1,3,4,5):continue
            row.update(referenceLife=g.life,referenceRevision={1:'SYN-A-r1',3:'SYN-A-r2',4:'SYN-B-r1',5:'SYN-A-r3'}[j])
        elif tab=='members': row.update(memberObject='rb',memberActual=u0+6000,memberPrice=float(selected['rb'].iloc[0].price),memberConfirmation=u0+12000,memberKnownFrom=u0+13200,memberTurn='SYN-rb-T0',memberRound=0,memberStatus='demo',memberRetracted=False)
        elif tab=='required': row.update(pairLeft='SYN-rb-T0',pairRight='SYN-hc-T0',pairTime='Positive',pairDirection='Positive',pairType='Positive',pairBend='Unresolved' if j==0 else 'Positive')
        else:
            if j<2:continue
            row.update(referenceLife='SYN-Life-B' if g.life.endswith('A') else 'SYN-Life-A',referenceRevision='SYN-B-r1' if g.life.endswith('A') else 'SYN-A-r2')
        rows.append(row)
    children[tab]=pd.DataFrame(rows)

DATA=dict(klines=klines,selected=selected,raw=raw,groups=groups,children=children)
fields=dict(groups={k:k for k in groups if k not in ('timestamp','occurrence','record_id','child_id_2')},
    selected={k:k for k in selected['rb']},raw={k:k for k in raw['rb']},parents=['timestamp','occurrence','record_id','child_id_2'],
    basis_order={'Incomplete':1,'Supported':2,'Contradicted':0},labels={},
    participation={'table':'participation','duty':'dutyClosed','admission':'admissionKnown','handoff':'handoffEnd'})

layout,meta=prototype.build_display(instance='SYNTHETIC-ONLY',reader=lambda instance,pos:DATA,context=context,
    position=position,fields=fields,caption='合成 rb/hc/i；2022-06-15—06-30；只读SOF仅提供交易日历。未读取实际K线/转折/候选结果。')
dest=ROOT/'html'/('first.html' if VERSION=='v1' else 'current.html')
dest.parent.mkdir(exist_ok=True)
html=file_html(layout,INLINE,'F800 C2 展示预期 · '+VERSION)
dest.write_text(html)
binding={'preview_kind':'SYNTHETIC','position':position,'context_calendar_only':'TA_updto20240229_DBA/steel',
    'real_feature_instance_bound':False,'real_feature_run':False,'formal_B_binding':False,
    'synthetic_groups':len(groups),'synthetic_kline_rows_per_symbol':len(xs),'all_sample_values_artificial':True,
    'seed':'deterministic sinusoidal bars and symbolic SYN identities','html_bytes':len(html.encode()),'html_sha256':hashlib.sha256(html.encode()).hexdigest(),
    'uplot_commit':'0a4fcd54059782572a3f7e82fad041121e8c65ad','figure_count':meta['fig_count'],'version':VERSION}
(ROOT/f'PREVIEW_BINDING_{VERSION}.json').write_text(json.dumps(binding,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(binding,ensure_ascii=False))
