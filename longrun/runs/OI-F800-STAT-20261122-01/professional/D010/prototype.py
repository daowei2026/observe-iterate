"""C2B 首版原型：原生CAEGraph组合，样例绑定在preview.py。"""
from collections.abc import Mapping
import json
import uuid

import numpy as np
import pandas as pd
from bokeh.models import Div
from bokeh.layouts import column
from mquant.frame import DoFunctionFao, GMap
from mquant.uplot import CAEGraph, PlotSet, PerSymFigs, KPriceLine, MulFieldsGlyphs, SubFig
from mquant.uplot.utlv2 import CurrSymbol

_READ_ONLY = {}

class InjectedFrames(DoFunctionFao):
    """分析用只读DataFrame入口；rerun不调用任何真实Feature/生产/存储。"""
    params = lambda: dict(token='')
    @property
    def that(self): return self
    def rerun(self, *args, **kwargs): return self
    def to_dfs(self):
        return _READ_ONLY[self.P.token](CurrSymbol.sym(False))
    def to_df(self): return self.to_dfs()['value']

def provider(getter):
    token = uuid.uuid4().hex
    _READ_ONLY[token] = getter
    return InjectedFrames(token=token)

def project(frame, mapping):
    missing = set(mapping.values()) - set(frame.columns)
    if missing: raise ValueError(f'缺失已约定字段：{sorted(missing)}')
    return frame.rename(columns={v:k for k,v in mapping.items()}).copy()

def build_display(*, instance, reader, context, position, fields, caption):
    data = reader(instance, position)
    kfeat = provider(lambda sym: {'value':data['klines'][sym]})
    selected = {s:project(data['selected'][s],fields['selected']) for s in position['symbols']}
    turns = provider(lambda sym: {'turns':selected[sym]})
    groups = project(data['groups'],fields['groups'])
    groups['basis_y'] = [fields['basis_order'][str(x)] for x in groups['basis']]
    gf = provider(lambda _: {'groups':groups})
    figs = GMap({
        'prices':PerSymFigs(title='!{sym} · 原价与输入转折（示意）',fig_height=210,plots=GMap({
            'k':KPriceLine(feat=kfeat,std_method=None,label='原价 K'),
            'turns':MulFieldsGlyphs(feats=GMap({'t':turns,'c':turns,'k':turns}), dfkeys=['turns'],
                xfields=['actual','confirmation','known'], yfields=['price','cprice','price'],
                glyphs=['circle','diamond','x'], colors=['#1d4ed8','#a21caf','#b45309'],
                legend_labels=['T实际','C几何确认','上游事件已知 @T价'],size=9,alphas=0.9,dynstd_method=False)
        })),
        'output':SubFig(title='候选组稀疏修订 · 局部依据编码',fig_height=260,plots=GMap({
            'revision':MulFieldsGlyphs(feats=GMap({'g':gf}),dfkeys=['groups'],xfields=['known'],yfields=['basis_y'],
                glyphs='circle',size=12,legend_labels=['发布修订'],colors=['#0f766e'],dynstd_method=False)
        }))
    })
    graph = CAEGraph(Context=context,plotsets=GMap({'expectation':PlotSet(calendar_name=position['calendar'],
        blk='|'.join(position['symbols']),timespans=[(position['start'],position['end'])],figs=figs)}),
        fig_width=position.get('width',1180),x_label_freq=position.get('label_freq','1d'),extra_time=0,
        plot_name='C2B 预期原型')
    roots=[]
    body=graph.layout(plot_roots=roots)
    header=Div(text='<h2>C2B v1 · F800 展示预期</h2><p>'+caption+'</p><p>原价独立纵轴；横轴为交易日历UTI。所有值均为合成演示，不是运行结果或正式场景。</p>',width=1180)
    return column(header,body), {'graph':graph,'roots':roots,'groups':groups,'data':data,'fig_count':len(position['symbols'])+1}
