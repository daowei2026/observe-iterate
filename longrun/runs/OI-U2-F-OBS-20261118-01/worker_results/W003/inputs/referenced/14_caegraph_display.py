"""Injectable C3 CAEGraph definition for CommonPriceTurnGroupCandidatesFrp.

This module deliberately binds no SOF, feature instance, symbol set, or time
range. D supplies them through ``DisplayBindings``; E performs the real run.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Mapping, Optional, Sequence

import numpy as np
import pandas as pd

BASIS_COLOR = {"Supported":"#2e7d32","Incomplete":"#f9a825","Contradicted":"#c62828"}
OBS_MARKER = {"Open":"circle","ClosedSupported":"triangle","ClosedInsufficient":"inverted_triangle","Withdrawn":"x","Subsumed":"diamond","EndedByScope":"square"}
VERDICT_COLOR = {"CoordinateSupports":"#2e7d32","CoordinateUnresolved":"#f9a825","CoordinateVeto":"#c62828"}
VERDICT_MARKER = {"CoordinateSupports":"circle","CoordinateUnresolved":"triangle","CoordinateVeto":"x"}
OBS_Y = {"Open":0,"ClosedSupported":1,"ClosedInsufficient":2,"Withdrawn":3,"Subsumed":4,"EndedByScope":5}
COORD_Y = {"Bend":0,"TurnType":1,"Direction":2,"Time":3}


@dataclass(frozen=True)
class CandidateTableNames:
    occurrences: str = "occurrences"
    previous: str = "occurrences_groupPrevious"
    members: str = "occurrences_groupMembers"
    required: str = "occurrences_groupRequired"
    pair_distance: str = "occurrences_groupRequired_pairDistance"
    overlaps: str = "occurrences_groupOverlaps"
    covered_by: str = "occurrences_groupCoveredBy"


@dataclass(frozen=True)
class DisplayBindings:
    candidate_feature: Any
    price_feature: Any
    symbols: Sequence[str]
    sof_name: str
    calendar_name: str
    timespans: Sequence[tuple[Any, Any]]
    raw_turn_view: Optional[pd.DataFrame] = None
    instance_label: str = "injected CommonPriceTurnGroupCandidatesFrp"
    graph_name: str = "u2_f_candidate_display"
    table_names: CandidateTableNames = field(default_factory=CandidateTableNames)


@dataclass(frozen=True)
class PreparedDisplayTables:
    revisions: pd.DataFrame
    revision_links: pd.DataFrame
    members: pd.DataFrame
    member_actual_confirmation: pd.DataFrame
    member_confirmation_known: pd.DataFrame
    required_summary: pd.DataFrame
    raw_turns: pd.DataFrame
    data_warnings: tuple[str, ...]


class _P(dict):
    def __getattr__(self, key: str) -> Any:
        try: return self[key]
        except KeyError as exc: raise AttributeError(key) from exc


class FrameFeature:
    """Read-only DataFrame adapter accepted by PlotCtx.feat_data."""
    def __init__(self, frame: pd.DataFrame, identity: str, calendar_name: Optional[str] = None):
        self._frame, self._identity, self.P = frame.copy(deep=False), identity, _P()
        if calendar_name is not None: self.P["calendar_name"] = calendar_name
    @property
    def that(self) -> str: return self._identity
    def rerun(self) -> "FrameFeature": return self
    def run(self) -> "FrameFeature": return self
    def to_df(self) -> pd.DataFrame: return self._frame
    def to_dfs(self) -> dict[str, pd.DataFrame]: return {"value": self._frame}


class PerSymbolFrameFeature(FrameFeature):
    def __init__(self, frame: pd.DataFrame, identity: str, symbol_getter: Callable[[], Optional[str]], calendar_name: Optional[str] = None):
        super().__init__(frame, identity, calendar_name); self._symbol_getter = symbol_getter
    @property
    def that(self) -> str: return f"{self._identity}:{self._symbol_getter()}"
    def to_df(self) -> pd.DataFrame:
        symbol = self._symbol_getter()
        return self._frame.iloc[0:0] if symbol is None else self._frame[self._frame.symbol.astype(str) == str(symbol)]


def _table(feature: Any, name: str) -> pd.DataFrame:
    tables = feature.to_dfs([name])
    if name not in tables: raise KeyError(f"missing candidate table: {name}")
    return tables[name]


def _flat(frame: pd.DataFrame, prefix: str) -> tuple[pd.DataFrame, list[str]]:
    out = frame.reset_index(drop=False).copy(); n = frame.index.nlevels
    old, keys = list(out.columns[:n]), [f"{prefix}{i}" for i in range(n)]
    out.rename(columns=dict(zip(old, keys)), inplace=True)
    return out, keys


def _child(frame: pd.DataFrame, parent_levels: int) -> tuple[pd.DataFrame, list[str]]:
    out, keys = _flat(frame, "ck")
    if len(keys) < parent_levels: raise ValueError("child index is shallower than occurrence index")
    ok = [f"ok{i}" for i in range(parent_levels)]
    out.rename(columns={keys[i]:ok[i] for i in range(parent_levels)}, inplace=True)
    return out, ok


def _ref(row: Mapping[str, Any], prefix: str) -> str:
    stem = prefix + "_" if prefix else ""
    text = row.get(stem + "idText")
    if text is not None and not pd.isna(text) and str(text) not in ("", "None"): return str(text)
    vals = [row.get(stem + k) for k in ("idForm","idHigh","idLow")]
    if any(v is None or pd.isna(v) for v in vals): return ""
    return f"{int(vals[0])}:{int(vals[1]):016x}{int(vals[2]):016x}"


def _name(frame: pd.DataFrame, base: str) -> pd.Series:
    for col in (base + "_name", base):
        if col in frame: return frame[col].astype("string").fillna("")
    return pd.Series("", index=frame.index, dtype="string")


def normalize_raw_turn_view(frame: Optional[pd.DataFrame]) -> pd.DataFrame:
    cols = ["symbol","actual","price","round","direction","turn_type","turn_exact","confirmation","known"]
    if frame is None: return pd.DataFrame({c:pd.Series(dtype="object") for c in cols})
    missing = set(cols[:7]) - set(frame.columns)
    if missing: raise KeyError(f"raw_turn_view missing fields: {sorted(missing)}")
    out = frame.copy()
    for c in ("confirmation","known"):
        if c not in out: out[c] = np.nan
    return out[cols]


def prepare_display_tables(candidate_feature: Any, *, table_names: CandidateTableNames = CandidateTableNames(), raw_turn_view: Optional[pd.DataFrame] = None) -> PreparedDisplayTables:
    warnings: list[str] = []
    occ, old_keys = _flat(_table(candidate_feature, table_names.occurrences), "ok")
    ok, n = old_keys, len(old_keys)
    occ["candidate_life"] = occ.apply(lambda r:_ref(r,"groupReference_referenceLife"),axis=1)
    occ["candidate_revision"] = occ.apply(lambda r:_ref(r,"groupReference_referenceRevision"),axis=1)
    occ["known"] = occ.groupKnownFrom.astype("int64")
    occ["basis"], occ["observation"], occ["alternative"] = _name(occ,"groupLocalBasis"), _name(occ,"groupObservation"), _name(occ,"groupAlternative")
    occ["state_y"], occ["color"], occ["marker"] = occ.observation.map(OBS_Y).fillna(-1).astype(int), occ.basis.map(BASIS_COLOR).fillna("#616161"), occ.observation.map(OBS_MARKER).fillna("circle")
    cov = occ.groupCoverageIncomplete if "groupCoverageIncomplete" in occ else pd.Series(0,index=occ.index)
    closed = occ.groupClosed if "groupClosed" in occ else pd.Series(0,index=occ.index)
    occ["coverage"], occ["closed"] = np.where(cov.astype(bool),"incomplete","complete"), closed.astype(bool)

    members, _ = _child(_table(candidate_feature, table_names.members), n)
    members = members.merge(occ[ok+["candidate_life","candidate_revision","known","basis","observation","alternative","coverage","closed"]],on=ok,how="left",validate="many_to_one")
    members["symbol"], members["actual"], members["confirmation"], members["member_known"], members["price"] = members.memberObject.astype(str), members.memberActual.astype("int64"), members.memberConfirmation.astype("int64"), members.memberKnownFrom.astype("int64"), members.memberPrice.astype(float)
    members["round"], members["direction"], members["turn_type"], members["member_status"] = _name(members,"memberRound"), _name(members,"memberDirection"), _name(members,"memberType"), _name(members,"memberStatus")
    members["turn_exact"] = members.apply(lambda r:_ref(r,"memberTurn_referenceLife")+"/"+_ref(r,"memberTurn_referenceRevision"),axis=1)
    members["source_exact"] = members.apply(lambda r:_ref(r,"memberSource_referenceLife")+"/"+_ref(r,"memberSource_referenceRevision"),axis=1)
    members["color"] = members.basis.map(BASIS_COLOR).fillna("#616161")
    members["actual_marker"] = members["round"].map({"FirstRound":"circle","SecondRound":"diamond"}).fillna("circle")
    mcols = ["symbol","candidate_life","candidate_revision","basis","observation","actual","confirmation","member_known","known","price","round","direction","turn_type","member_status","turn_exact","source_exact","color","actual_marker"]
    mview = members[mcols].copy()
    a2c = mview.rename(columns={"actual":"x0","confirmation":"x1"}).assign(y0=mview.price,y1=mview.price)
    c2k = mview.rename(columns={"confirmation":"x0","member_known":"x1"}).assign(y0=mview.price,y1=mview.price)
    labels = members.groupby(ok,dropna=False).symbol.agg(lambda s:",".join(dict.fromkeys(map(str,s)))).rename("members").reset_index()
    occ = occ.merge(labels,on=ok,how="left",validate="one_to_one"); occ["members"] = occ.members.fillna("")

    previous, _ = _child(_table(candidate_feature, table_names.previous), n)
    previous["previous_life"], previous["previous_revision"] = previous.apply(lambda r:_ref(r,"referenceLife"),axis=1), previous.apply(lambda r:_ref(r,"referenceRevision"),axis=1)
    previous = previous.groupby(ok,dropna=False)[["previous_life","previous_revision"]].agg(lambda s:",".join(v for v in map(str,s) if v)).reset_index()
    occ = occ.merge(previous,on=ok,how="left",validate="one_to_one")
    for c in ("previous_life","previous_revision"): occ[c] = occ[c].fillna("")
    lookup = {(r.candidate_life,r.candidate_revision):(int(r.known),int(r.state_y)) for r in occ.itertuples(index=False)}
    links=[]
    for r in occ.itertuples(index=False):
        p=(r.previous_life,r.previous_revision)
        if all(p) and p in lookup:
            x0,y0=lookup[p];links.append({"x0":x0,"x1":int(r.known),"y0":y0,"y1":int(r.state_y),"candidate_life":r.candidate_life,"candidate_revision":r.candidate_revision,"previous_revision":r.previous_revision})
    revision_links = pd.DataFrame(links,columns=["x0","x1","y0","y1","candidate_life","candidate_revision","previous_revision"])

    for table,outcol in ((table_names.overlaps,"overlaps"),(table_names.covered_by,"covered_by")):
        child,_=_child(_table(candidate_feature,table),n); child[outcol]=child.apply(lambda r:_ref(r,""),axis=1)
        agg=child.groupby(ok,dropna=False)[outcol].agg(lambda s:",".join(v for v in map(str,s) if v)).reset_index()
        occ=occ.merge(agg,on=ok,how="left",validate="one_to_one");occ[outcol]=occ[outcol].fillna("")

    required,_ = _child(_table(candidate_feature, table_names.required),n)
    required = required.merge(occ[ok+["candidate_life","candidate_revision","known"]],on=ok,how="left",validate="many_to_one")
    required["left_turn"] = required.apply(lambda r:_ref(r,"pairLeft_referenceLife")+"/"+_ref(r,"pairLeft_referenceRevision"),axis=1)
    required["right_turn"] = required.apply(lambda r:_ref(r,"pairRight_referenceLife")+"/"+_ref(r,"pairRight_referenceRevision"),axis=1)
    obj = members[["turn_exact","symbol"]].drop_duplicates().set_index("turn_exact").symbol.to_dict()
    required["pair"] = required.apply(lambda r:f"{obj.get(r.left_turn,r.left_turn)}-{obj.get(r.right_turn,r.right_turn)}",axis=1)
    try:
        dist,_ = _child(_table(candidate_feature, table_names.pair_distance),n)
        common=[c for c in required.columns if (c.startswith("ok") or c.startswith("ck")) and c in dist.columns]
        if common and "distanceValue" in dist:
            distance = dist.groupby(common,dropna=False).distanceValue.first().reset_index()
            required = required.merge(distance,on=common,how="left",validate="many_to_one")
    except (KeyError,ValueError): warnings.append("pair distance table could not be joined; verdict rows remain available")
    if "distanceValue" not in required: required["distanceValue"] = np.nan

    rows=[]; severity={"CoordinateSupports":0,"CoordinateUnresolved":1,"CoordinateVeto":2}
    fields={"Time":"pairTime","Direction":"pairDirection","TurnType":"pairType","Bend":"pairBend"}
    for (life,rev,known),grp in required.groupby(["candidate_life","candidate_revision","known"],dropna=False):
        for coord,prefix in fields.items():
            verdict,gap,veto=_name(grp,prefix+"_requiredVerdict"),_name(grp,prefix+"_requiredGap"),_name(grp,prefix+"_requiredVeto")
            values=list(verdict);worst=max(values,key=lambda v:severity.get(str(v),-1)) if values else ""
            counts={k:values.count(k) for k in severity};details=[]
            for pair,v,g,ve,d in zip(grp.pair,verdict,gap,veto,grp.distanceValue):
                reason=ve if str(ve) not in ("","NoVeto","-1") else g;details.append(f"{pair}:{v}:{reason}"+("" if pd.isna(d) else f" distance={d:g}"))
            rows.append({"candidate_life":life,"candidate_revision":rev,"known":int(known),"coordinate":coord,"coord_y":COORD_Y[coord],"verdict":worst,"color":VERDICT_COLOR.get(str(worst),"#616161"),"marker":VERDICT_MARKER.get(str(worst),"circle"),"counts":f"{counts['CoordinateSupports']}/{counts['CoordinateUnresolved']}/{counts['CoordinateVeto']}","details":" | ".join(details)})
    required_summary=pd.DataFrame(rows,columns=["candidate_life","candidate_revision","known","coordinate","coord_y","verdict","color","marker","counts","details"])

    rcols=[*ok,"candidate_life","candidate_revision","known","basis","observation","alternative","state_y","color","marker","coverage","closed","members","previous_life","previous_revision","overlaps","covered_by","groupOriginalAnchor","groupOriginalDeadline","groupOriginalRevisionEnd","groupAnchor","groupDeadline","groupRevisionEnd"]
    revisions=occ[[c for c in rcols if c in occ]].copy();raw=normalize_raw_turn_view(raw_turn_view)
    if raw.empty: warnings.append("raw ScaleTurn overlay was not injected; member evidence remains available")
    warnings.append("groupFormationParticipation is stored by Haskell but not exposed by locked TIS GROUP_TABLES")
    return PreparedDisplayTables(revisions,revision_links,mview,a2c,c2k,required_summary,raw,tuple(warnings))


def build_caegraph(bindings: DisplayBindings) -> Any:
    """Return the C3 graph after D injects its real instance and B position."""
    if not bindings.symbols or not bindings.timespans: raise ValueError("D must inject symbols and timespans")
    from bokeh.models import Div, FixedTicker, HoverTool
    from m3 import GMapX, OptContext, CurrSymbol
    try:
        from mquant.uplot import AllSymsFig,BaseFigSet,BasePlotter,CAEGraph,DefaultFigTheme,KPriceLine,PerSymFigs,PlotSet,PlotCtx
    except ImportError:
        from uplot import AllSymsFig,BaseFigSet,BasePlotter,CAEGraph,DefaultFigTheme,KPriceLine,PerSymFigs,PlotSet,PlotCtx
    p=prepare_display_tables(bindings.candidate_feature,table_names=bindings.table_names,raw_turn_view=bindings.raw_turn_view)
    getter=lambda:CurrSymbol.sym(False)
    ff=lambda df,name:FrameFeature(df,f"{bindings.graph_name}:{name}",bindings.calendar_name)
    sf=lambda df,name:PerSymbolFrameFeature(df,f"{bindings.graph_name}:{name}",getter,bindings.calendar_name)
    rev,rl,req,mem,a2c,c2k,raw=ff(p.revisions,"revisions"),ff(p.revision_links,"revision-links"),ff(p.required_summary,"required"),sf(p.members,"members"),sf(p.member_actual_confirmation,"a2c"),sf(p.member_confirmation_known,"c2k"),sf(p.raw_turns,"raw")

    class Note(BaseFigSet):
        params=lambda:dict(text="",width=1200)
        def plot_figs(self,ctx):ctx.figs.append(Div(text=self.P.text,width=self.P.width))
    class Glyphs(BasePlotter):
        params=lambda:dict(feat=None,x=None,y=None,marker="circle",marker_field=None,color="#1565c0",color_field=None,size=9,alpha=.65,label=None,hover=(),uti=(),labels=None)
        def _plot_fig(self,ctx):
            def trans(df):
                xv=df[self.P.x].to_numpy();d={"x":ctx.uti2x(xv),"x_ts":ctx.uti2tslabel(xv),"y":df[self.P.y].to_numpy()}
                for c in self.P.hover:
                    if c in df:d[c]=df[c].astype(str).to_numpy()
                for c in self.P.uti:
                    if c in df:d[c+"_ts"]=ctx.uti2tslabel(df[c].to_numpy())
                if self.P.marker_field:d["marker"]=df[self.P.marker_field].astype(str).to_numpy()
                if self.P.color_field:d["color"]=df[self.P.color_field].astype(str).to_numpy()
                return d
            cds=ctx.feat_data(f"glyph:{self.P.label}",trans,self.P.feat,None,self.P.x);kw={}
            if self.P.label:kw.update(legend_label=self.P.label,name=self.P.label)
            g=ctx.figs[-1].scatter(x="x",y="y",source=cds,marker="marker" if self.P.marker_field else self.P.marker,color="color" if self.P.color_field else self.P.color,size=self.P.size,alpha=self.P.alpha,**kw)
            ctx.figs[-1].add_tools(HoverTool(renderers=[g],tooltips=[("time","@x_ts")]+[(c,f"@{c}") for c in self.P.hover]));ctx.fit_ys(cds)
            if self.P.labels:ctx.figs[-1].yaxis.ticker=FixedTicker(ticks=list(self.P.labels));ctx.figs[-1].yaxis.major_label_overrides=self.P.labels
    class Segments(BasePlotter):
        params=lambda:dict(feat=None,color="#607d8b",dash="dashed",width=1.5,alpha=.45,label=None,hover=())
        def _plot_fig(self,ctx):
            def trans(df):
                d={"x0":ctx.uti2x(df.x0.to_numpy()),"x1":ctx.uti2x(df.x1.to_numpy()),"y0":df.y0.to_numpy(),"y1":df.y1.to_numpy(),"x0_ts":ctx.uti2tslabel(df.x0.to_numpy()),"x1_ts":ctx.uti2tslabel(df.x1.to_numpy())}
                for c in self.P.hover:
                    if c in df:d[c]=df[c].astype(str).to_numpy()
                return d
            cds=ctx.feat_data(f"segment:{self.P.label}",trans,self.P.feat,None,"x0","x1");kw={}
            if self.P.label:kw.update(legend_label=self.P.label,name=self.P.label)
            g=ctx.figs[-1].segment(x0="x0",y0="y0",x1="x1",y1="y1",source=cds,color=self.P.color,line_dash=self.P.dash,line_width=self.P.width,alpha=self.P.alpha,**kw)
            ctx.figs[-1].add_tools(HoverTool(renderers=[g],tooltips=[("from","@x0_ts"),("to","@x1_ts")]+[(c,f"@{c}") for c in self.P.hover]));ctx.fit_ys(cds,"x0","y0");ctx.fit_ys(cds,"x1","y1")

    price=[KPriceLine(feat=bindings.price_feature,add_hover=True,label="5m KLine")]
    if not p.raw_turns.empty:price.append(Glyphs(feat=raw,x="actual",y="price",color="#616161",size=6,alpha=.25,label="raw ScaleTurn",hover=("turn_exact","round","direction","turn_type"),uti=("actual","confirmation","known")))
    price += [Segments(feat=a2c,color="#5c6bc0",dash="dotted",width=2,label="actual→confirmation",hover=("candidate_life","candidate_revision","turn_exact")),Segments(feat=c2k,color="#8d6e63",width=2,label="confirmation→known",hover=("candidate_life","candidate_revision","turn_exact")),Glyphs(feat=mem,x="actual",y="price",marker_field="actual_marker",color_field="color",size=11,label="member actual",hover=("candidate_life","candidate_revision","basis","observation","turn_exact","source_exact","round","direction","turn_type","member_status"),uti=("actual","confirmation","member_known","known"))]
    warning="".join(f"<li>{w}</li>" for w in p.data_warnings)
    return CAEGraph(Context=OptContext(bindings.sof_name),plotsets=GMapX({"F candidate audit":PlotSet(calendar_name=bindings.calendar_name,timespans=list(bindings.timespans),blk=list(bindings.symbols),figs=GMapX.from_list([
        Note(text=f"<h2>CommonPriceTurnGroupCandidatesFrp display</h2><p>{bindings.instance_label}</p><ul>{warning}</ul>"),
        PerSymFigs(title="!{sym}｜5m price + candidate member evidence",plots=GMapX.from_list(price),fig_height=240),
        AllSymsFig(title="F revisions｜x=groupKnownFrom; y=groupObservation",plots=GMapX.from_list([Segments(feat=rl,label="previous→revision",hover=("candidate_life","previous_revision","candidate_revision")),Glyphs(feat=rev,x="known",y="state_y",marker_field="marker",color_field="color",size=12,label="candidate revision",hover=("candidate_life","candidate_revision","previous_revision","basis","observation","members","alternative","coverage","closed","overlaps","covered_by","groupOriginalAnchor","groupOriginalDeadline","groupOriginalRevisionEnd","groupAnchor","groupDeadline","groupRevisionEnd"),uti=("known",),labels={v:k for k,v in OBS_Y.items()})]),fig_height=260),
        AllSymsFig(title="Required audit｜worst/count summary; exact reasons in hover",plots=GMapX.from_list([Glyphs(feat=req,x="known",y="coord_y",marker_field="marker",color_field="color",size=11,label="Required verdict",hover=("candidate_life","candidate_revision","coordinate","verdict","counts","details"),uti=("known",),labels={v:k for k,v in COORD_Y.items()})]),fig_height=240)
    ]))}),theme=DefaultFigTheme(),x_label_freq="30m",fig_width=1200,fig_height1=420,fig_height=240,plot_name="U2 F candidate display")


__all__=["CandidateTableNames","DisplayBindings","PreparedDisplayTables","normalize_raw_turn_view","prepare_display_tables","build_caegraph"]
