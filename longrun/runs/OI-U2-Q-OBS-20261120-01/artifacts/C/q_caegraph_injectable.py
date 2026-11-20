#!/usr/bin/env python3
"""Injectable CAEGraph definition for Q.

No SOF, object set, dates, result path, or concrete Q instance is hard-coded.
D injects the real Q feature, field adapter, price feature, and B position.
API checked against daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Mapping, Protocol, Sequence
import numpy as np
import pandas as pd
from bokeh.models import ColumnDataSource, FixedTicker, HoverTool
from mquant.frame import CurrSymbol, GMap, OptContext
from mquant.uplot import (AllSymsFig, AllSymsMainFig, BasePlotter, CAEGraph,
    DefaultFigTheme, KPriceLine, MainFig, PerSymFigSet, PlotSet, SubFig)


@dataclass(frozen=True)
class QDisplayFrames:
    """Canonical frames. Missing values stay null; never coerce them to zero."""
    timeline: pd.DataFrame
    revision_links: pd.DataFrame
    states: pd.DataFrame
    members: pd.DataFrame
    quantities: pd.DataFrame
    audit: pd.DataFrame

    def validate(self) -> None:
        required = {
            "timeline": {"event_uti","event_kind","event_id","q_life","q_revision",
                "previous_ref","candidate_ref","members","known_uti","qualification",
                "observation","applicability","end_reason","last_successful_ref","detail"},
            "revision_links": {"from_uti","to_uti","q_life","from_revision","to_revision"},
            "states": {"publication_uti","q_life","q_revision","state_kind","state_value","detail"},
            "members": {"publication_uti","q_life","q_revision","member","asked_uti",
                "asked_price","used_uti","used_price","successor_uti","successor_price",
                "endpoint_uti","endpoint_price","completion","verdict","basis","path_complete",
                "through","material_known","missing_range","candidate_ref"},
            "quantities": {"publication_uti","q_life","q_revision","member",
                "quantity_kind","quantity_value","availability"},
            "audit": {"event_uti","event_id","event_kind","previous_ref","candidate_ref",
                "publication_or_end_known","detail"},
        }
        for name, cols in required.items():
            frame = getattr(self, name)
            if not isinstance(frame, pd.DataFrame):
                raise TypeError(f"{name} must be DataFrame")
            missing = cols - set(frame.columns)
            if missing:
                raise ValueError(f"{name} missing {sorted(missing)}")


class QFrameAdapter(Protocol):
    def __call__(self, q_feature: Any, field_binding: Mapping[str, Any]) -> QDisplayFrames: ...


@dataclass(frozen=True)
class QPositionBinding:
    sof_name: str
    block: str
    calendar_name: str
    objects: Sequence[str]
    timespans: Sequence[tuple]
    context_start: Any | None = None
    context_end: Any | None = None

    def validate(self) -> None:
        if not self.sof_name or not self.calendar_name:
            raise ValueError("SOF and calendar are required")
        if len(tuple(self.objects)) < 2:
            raise ValueError("Q needs its actual multi-object universe")
        if not self.timespans:
            raise ValueError("D must inject at least one B-stage timespan")


@dataclass(frozen=True)
class QDisplayBinding:
    q_feature: Any
    price_feature: Any
    frame_adapter: QFrameAdapter
    field_binding: Mapping[str, Any]
    position: QPositionBinding
    graph_name: str = "Q方向组织观察"
    plot_name: str = "Q PostTurnGroupDirectionalOrganization"

    def frames(self) -> QDisplayFrames:
        self.position.validate()
        frames = self.frame_adapter(self.q_feature, self.field_binding)
        frames.validate()
        return frames


def _slice(df: pd.DataFrame, field: str, ctx: Any) -> pd.DataFrame:
    if df.empty: return df.copy()
    value = pd.to_numeric(df[field], errors="coerce")
    return df.loc[value.ge(ctx.uti_slice.start) & value.lt(ctx.uti_slice.stop)].copy()


def _cds(df: pd.DataFrame, columns: Sequence[str]) -> ColumnDataSource:
    return ColumnDataSource({c: (df[c] if c in df else pd.Series([None]*len(df))).to_numpy() for c in columns})


def _hover(fig: Any, glyph: Any, tips: Sequence[tuple[str,str]]) -> None:
    fig.add_tools(HoverTool(renderers=[glyph], tooltips=list(tips)))


class QLifecyclePlot(BasePlotter):
    params = lambda: dict(frames=None)
    lane = {"F candidate":2., "Q revision":1., "Duty end":0.}
    marker = {"F candidate":"square", "Q revision":"circle", "Duty end":"diamond"}
    color = {"F candidate":"#64748b", "Q revision":"#2563eb", "Duty end":"#dc2626"}

    def _plot_fig(self, ctx):
        fig = ctx.figs[-1]
        df = _slice(self.P.frames.timeline, "event_uti", ctx)
        if df.empty: return
        df["x"] = df.event_uti.astype(float); df["y"] = df.event_kind.map(self.lane)
        df["ts"] = ctx.uti2tslabel(df.event_uti.astype(int).to_numpy())
        cols = ["x","y","ts","event_id","event_kind","q_life","q_revision","previous_ref",
            "candidate_ref","members","known_uti","qualification","observation","applicability",
            "end_reason","last_successful_ref","detail"]
        for kind in self.lane:
            part = df.loc[df.event_kind.eq(kind)]
            if part.empty: continue
            source = _cds(part, cols)
            glyph = fig.scatter(x="x",y="y",source=source,marker=self.marker[kind],size=11,
                color=self.color[kind],alpha=.9,legend_label=kind)
            _hover(fig,glyph,[("type","@event_kind"),("event","@event_id"),("time","@ts"),
                ("Q","@q_life / @q_revision"),("Previous","@previous_ref"),
                ("F candidate","@candidate_ref"),("members","@members"),("known","@known_uti"),
                ("qualification","@qualification"),("observation","@observation"),
                ("applicability","@applicability"),("end reason","@end_reason"),
                ("last successful","@last_successful_ref"),("detail","@detail")])
        links = self.P.frames.revision_links
        if not links.empty:
            keep = pd.to_numeric(links.from_uti,errors="coerce").lt(ctx.uti_slice.stop) & pd.to_numeric(links.to_uti,errors="coerce").ge(ctx.uti_slice.start)
            links = links.loc[keep].copy()
            if not links.empty:
                links["y0"] = links["y1"] = 1.
                source = _cds(links,["from_uti","to_uti","y0","y1","q_life","from_revision","to_revision"])
                glyph = fig.segment(x0="from_uti",x1="to_uti",y0="y0",y1="y1",source=source,
                    color="#93c5fd",line_width=3,legend_label="Q Previous chain")
                _hover(fig,glyph,[("Q Life","@q_life"),("revision","@from_revision → @to_revision")])
        fig.yaxis.ticker=FixedTicker(ticks=[0,1,2]); fig.yaxis.major_label_overrides={0:"Duty end",1:"Q revision",2:"F candidate"}
        fig.y_range.start,fig.y_range.end=-.5,2.5


class QStatePlot(BasePlotter):
    params = lambda: dict(frames=None)
    lane={"qualification":2.,"observation":1.,"applicability":0.}
    colors={"QualifiedCompleted":"#15803d","QualifiedWorking":"#16a34a","QualificationPending":"#d97706",
        "QualificationConflict":"#dc2626","QualificationRejected":"#991b1b","MotionObserving":"#2563eb",
        "HorizonReached":"#7c3aed","MotionScopeEnded":"#475569","SubjectApplicable":"#0f766e","SubjectWithdrawn":"#dc2626"}
    def _plot_fig(self,ctx):
        fig=ctx.figs[-1]; df=_slice(self.P.frames.states,"publication_uti",ctx)
        if df.empty:return
        df["x"]=df.publication_uti.astype(float);df["y"]=df.state_kind.map(self.lane);df["color"]=df.state_value.map(self.colors).fillna("#64748b")
        df["ts"]=ctx.uti2tslabel(df.publication_uti.astype(int).to_numpy())
        source=_cds(df,["x","y","color","ts","q_life","q_revision","state_kind","state_value","detail"])
        glyph=fig.scatter(x="x",y="y",source=source,marker="circle",size=10,color="color",alpha=.9)
        _hover(fig,glyph,[("time","@ts"),("Q","@q_life / @q_revision"),("kind","@state_kind"),("state","@state_value"),("detail","@detail")])
        fig.yaxis.ticker=FixedTicker(ticks=[0,1,2]);fig.yaxis.major_label_overrides={0:"applicability",1:"observation",2:"qualification"}
        fig.y_range.start,fig.y_range.end=-.5,2.5


class QMemberGeometryPlot(BasePlotter):
    params=lambda:dict(frames=None,follow_price_standardization=False)
    points=(("asked","asked_uti","asked_price","square","#64748b"),("used","used_uti","used_price","circle","#7c3aed"),
        ("successor","successor_uti","successor_price","diamond","#dc2626"),("endpoint","endpoint_uti","endpoint_price","triangle","#0f766e"))
    def _plot_fig(self,ctx):
        fig=ctx.figs[-1];sym=CurrSymbol.sym();df=self.P.frames.members
        df=_slice(df.loc[df.member.eq(sym)],"publication_uti",ctx)
        if df.empty:return
        common=["q_life","q_revision","member","completion","verdict","basis","path_complete","through","material_known","missing_range","candidate_ref"]
        seg=df.dropna(subset=["used_uti","used_price","endpoint_uti","endpoint_price"])
        if not seg.empty:
            source=_cds(seg,["used_uti","used_price","endpoint_uti","endpoint_price",*common])
            glyph=fig.segment(x0="used_uti",y0="used_price",x1="endpoint_uti",y1="endpoint_price",source=source,
                color=ctx.sym_color,line_width=3,alpha=.65,legend_label=f"{sym} used→endpoint")
            if self.P.follow_price_standardization:ctx.drive_entity_dynstd(source,[("used_uti","used_price"),("endpoint_uti","endpoint_price")])
            _hover(fig,glyph,[("Q","@q_life / @q_revision"),("member","@member"),("verdict","@verdict"),
                ("completion","@completion"),("basis","@basis"),("path complete","@path_complete"),
                ("through","@through"),("material known","@material_known"),("missing range","@missing_range"),("F candidate","@candidate_ref")])
            ctx.fit_ys(source,"used_uti","used_price");ctx.fit_ys(source,"endpoint_uti","endpoint_price")
        for label,xf,yf,marker,color in self.points:
            part=df.dropna(subset=[xf,yf]).copy()
            if part.empty:continue
            part["x"]=part[xf];part["y"]=part[yf];part["ts"]=ctx.uti2tslabel(part[xf].astype(int).to_numpy())
            source=_cds(part,["x","y","ts",*common])
            glyph=fig.scatter(x="x",y="y",source=source,marker=marker,size=9,color=color,alpha=.9,legend_label=f"{sym} {label}")
            if self.P.follow_price_standardization:ctx.drive_entity_dynstd(source)
            _hover(fig,glyph,[("position",label),("time","@ts"),("Q","@q_life / @q_revision"),("member","@member"),
                ("verdict","@verdict"),("completion","@completion"),("basis","@basis"),("path complete","@path_complete"),
                ("through","@through"),("material known","@material_known"),("missing range","@missing_range"),("F candidate","@candidate_ref")])
            ctx.fit_ys(source)


class QMemberAuditPlot(BasePlotter):
    params=lambda:dict(frames=None)
    lanes={"verdict":8.,"completion":7.,"path":6.,"ProgressP":5.,"AmplitudeA":4.,"DurationD":3.,"PathLengthL":2.,"EfficiencyE":1.,"CounterC":0.}
    def _plot_fig(self,ctx):
        fig=ctx.figs[-1];sym=CurrSymbol.sym();m=_slice(self.P.frames.members.loc[self.P.frames.members.member.eq(sym)],"publication_uti",ctx);rows=[]
        for _,r in m.iterrows():
            for kind,value in (("verdict",r.verdict),("completion",r.completion),("path","Complete" if bool(r.path_complete) else "Incomplete")):
                rows.append(dict(publication_uti=r.publication_uti,q_life=r.q_life,q_revision=r.q_revision,member=sym,kind=kind,value=value,availability="Known"))
        q=_slice(self.P.frames.quantities.loc[self.P.frames.quantities.member.eq(sym)],"publication_uti",ctx)
        for _,r in q.iterrows():rows.append(dict(publication_uti=r.publication_uti,q_life=r.q_life,q_revision=r.q_revision,member=sym,kind=r.quantity_kind,value=r.quantity_value,availability=r.availability))
        if not rows:return
        df=pd.DataFrame(rows);df["x"]=df.publication_uti.astype(float);df["y"]=df.kind.map(self.lanes);df["ts"]=ctx.uti2tslabel(df.publication_uti.astype(int).to_numpy())
        df["color"]=np.where(df.availability.eq("QuantityKnown"),"#2563eb","#f59e0b");df.loc[df.availability.eq("Known"),"color"]="#0f766e"
        source=_cds(df,["x","y","ts","q_life","q_revision","member","kind","value","availability","color"])
        glyph=fig.scatter(x="x",y="y",source=source,marker="circle",size=8,color="color",alpha=.9)
        _hover(fig,glyph,[("time","@ts"),("Q","@q_life / @q_revision"),("member","@member"),("field","@kind"),("raw value","@value"),("availability","@availability")])
        fig.yaxis.ticker=FixedTicker(ticks=list(self.lanes.values()));fig.yaxis.major_label_overrides={int(v):k for k,v in self.lanes.items()};fig.y_range.start,fig.y_range.end=-.5,8.5


class QAuditPlot(BasePlotter):
    params=lambda:dict(frames=None)
    def _plot_fig(self,ctx):
        fig=ctx.figs[-1];df=_slice(self.P.frames.audit,"event_uti",ctx).reset_index(drop=True)
        if df.empty:return
        df["x"]=df.event_uti.astype(float);df["y"]=np.arange(len(df),0,-1,dtype=float)
        df["text"]=df.event_id.astype(str)+" | prev="+df.previous_ref.fillna("None").astype(str)+" | F="+df.candidate_ref.fillna("None").astype(str)+" | "+df.detail.astype(str)
        df["ts"]=ctx.uti2tslabel(df.event_uti.astype(int).to_numpy())
        source=_cds(df,["x","y","text","ts","event_id","event_kind","previous_ref","candidate_ref","publication_or_end_known","detail"])
        glyph=fig.text(x="x",y="y",text="text",source=source,text_font_size="9pt",text_align="left",text_baseline="middle")
        _hover(fig,glyph,[("event","@event_id"),("type","@event_kind"),("time","@ts"),("Previous","@previous_ref"),("F candidate","@candidate_ref"),("known","@publication_or_end_known"),("detail","@detail")])
        fig.yaxis.visible=False;fig.y_range.start,fig.y_range.end=0,max(2.,len(df)+1.)


def build_q_caegraph(binding: QDisplayBinding) -> CAEGraph:
    """Build the graph after D injects the real feature, fields and B position."""
    frames=binding.frames();p=binding.position
    context={"sof_name":p.sof_name,"stk_tlist":p.block}
    if p.context_start is not None:context["startDay"]=p.context_start
    if p.context_end is not None:context["endDay"]=p.context_end
    figs=GMap({
        "overview":AllSymsMainFig(dict(title="!Q multi-symbol 5m price (ratio display derivative)",persym_plots=GMap({
            "price":KPriceLine(feat=binding.price_feature,std_method="ratio",label="5m price ratio"),
            "member":QMemberGeometryPlot(dict(frames=frames,follow_price_standardization=True))}))),
        "lifecycle":AllSymsFig(dict(title="!F candidate → Q revision → explicit duty end",plots=GMap({"life":QLifecyclePlot(dict(frames=frames))}),fig_height=230)),
        "state":AllSymsFig(dict(title="!Q group state by emitted revision",plots=GMap({"state":QStatePlot(dict(frames=frames))}),fig_height=210)),
        "members":PerSymFigSet(dict(figs=GMap({
            "raw":MainFig(dict(title="!{sym} raw price + asked/used/successor/endpoint",plots=GMap({
                "price":KPriceLine(feat=binding.price_feature,std_method=None,label="5m raw price"),
                "member":QMemberGeometryPlot(dict(frames=frames,follow_price_standardization=False))}))),
            "audit":SubFig(dict(title="!{sym} member verdict/completion/quantity audit",plots=GMap({"audit":QMemberAuditPlot(dict(frames=frames))}),fig_height=270))}))),
        "detail":AllSymsFig(dict(title="!Q exact refs / Previous / F ref / explicit end",plots=GMap({"audit":QAuditPlot(dict(frames=frames))}),fig_height=220))})
    return CAEGraph(dict(Context=OptContext(**context),plotsets=GMap({binding.graph_name:PlotSet(dict(
        calendar_name=p.calendar_name,blk=list(p.objects),timespans=list(p.timespans),figs=figs))}),
        theme=DefaultFigTheme(),x_label_freq="1h",extra_time=0,fig_width=1200,fig_height1=420,
        fig_height=240,manual_upd=True,plot_name=binding.plot_name,switches={}))


def render_notebook(binding: QDisplayBinding, *, ncols: int = 1) -> Any:
    return build_q_caegraph(binding).layout(ncols=ncols)
