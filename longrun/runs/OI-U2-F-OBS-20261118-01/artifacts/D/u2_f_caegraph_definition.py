"""D004 integrated CAEGraph definition for CommonPriceTurnGroupCandidatesFrp.

This file binds the real outer feature instance and B-POS-001 to the accepted
C2 display contract.  It never reruns the F producer.  E may execute it in the
locked BASE_E6_2_copy environment to read an existing F result, build the
Bokeh/CAEGraph layout, export HTML, prepared display tables and PlotDataTree
CDS data.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
import time
from pathlib import Path
from typing import Any, Iterable, Mapping, Optional, Sequence

import numpy as np
import pandas as pd

RUN_ID = "OI-U2-F-OBS-20261118-01"
DEFINITION_ID = f"{RUN_ID}-D-CAEGRAPH-V1"
POSITION_ID = f"{RUN_ID}-B-POS-001"

SOF_NAME = "TA_updto20240229_DBA"
BLOCK_CONTEXT = "steel"
SYMBOLS = ("rb", "hc", "i")
CALENDAR_NAME = "night_end_at_2300"
FREQUENCY = "5m"
TIMESPANS = (("2021-01-01", "2022-12-31", POSITION_ID),)

FEATURE_PARAMS: Mapping[str, Any] = {
    "freq": FREQUENCY,
    "symbols": SYMBOLS,
    "delta": 600,
    "direction": "DirectionUp",
    "retrace_pct": 0.5,
    "check_retrace_pct": 0.5,
    "membership_line": 0.5,
    "spec_term": "M",
    "distance_times": 100,
    "x_step_times": 0.1,
    "overlap": 0.2,
    "source_core_multiples": 30,
}

SOURCE_REFS = {
    "feature_input": "daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:task-inputs/u2-fqv-observation/F_OBSERVATION_RUN_INPUT.md",
    "feature_constructor": "daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py",
    "feature_python": "daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonPriceTurnGroupCandidates.py",
    "feature_haskell": "daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c:src/Frp/Instance/ISL/Opportunity/CommonPriceTurnGroupCandidates.hs",
    "artifact_a": "daowei2026/observe-iterate@823b56a018c0f49e1632885db484ff2e1e64d6b8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/A/FEATURE_OCCURRENCE_UNDERSTANDING.md",
    "artifact_b": "daowei2026/observe-iterate@6f1ee9eb4595254845d3b228a146ad68cabc64e0:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/B/OBSERVATION_POSITION_PREPARATION.md",
    "artifact_c": "daowei2026/observe-iterate@bcb94cc298d0a20049a2a52fdf7fe577137e7bde:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/CAEGRAPH_DISPLAY_PREPARATION.md",
    "c3_code": "daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py",
    "c2_html": "daowei2026/observe-iterate@56eef30b28c928255329f77798fb46b9adbbc71a:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview.html",
    "uplot": "daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad",
}

_THIS = Path(__file__).resolve()
_C3_PATH = _THIS.parents[1] / "C" / "caegraph_display.py"


def _load_c3():
    if not _C3_PATH.is_file():
        raise FileNotFoundError(f"C3 module not found: {_C3_PATH}")
    spec = importlib.util.spec_from_file_location("oi_u2_f_c3_display", _C3_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load C3 module: {_C3_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


C3 = _load_c3()


def _safe_name(value: str) -> str:
    cleaned = re.sub(r"[^0-9A-Za-z._-]+", "_", value).strip("._")
    return cleaned or "unnamed"


def _frame_of(feature: Any) -> pd.DataFrame:
    frame = feature.rerun().to_df()
    if not isinstance(frame, pd.DataFrame):
        raise TypeError(f"expected DataFrame, got {type(frame)!r}")
    return frame


def _range_mask(frame: pd.DataFrame, x_fields: Sequence[str], start: int, stop: int) -> pd.Series:
    if frame.empty:
        return pd.Series(False, index=frame.index, dtype=bool)
    usable = []
    for field in x_fields:
        if field not in frame:
            raise KeyError(f"missing UTI field: {field}")
        values = pd.to_numeric(frame[field], errors="coerce")
        usable.append((values >= start) & (values < stop))
    mask = usable[0].copy()
    for extra in usable[1:]:
        mask |= extra
    return mask.fillna(False)


def build_bound_caegraph(bindings: Any, prepared: Any) -> Any:
    """Build the accepted C2 graph using locked uplot APIs.

    The C3 table preparation is reused unchanged.  Plotting is integrated here
    with explicit interval masks because candidate member actual/confirmation/
    known positions and revision links are not guaranteed to be monotonic.
    """
    if not bindings.symbols:
        raise ValueError("symbols must not be empty")
    if not bindings.timespans:
        raise ValueError("timespans must not be empty")

    from bokeh.models import ColumnDataSource, Div, FixedTicker, HoverTool
    from m3 import CurrSymbol, GMapX, OptContext
    from mquant.uplot import (
        AllSymsFig,
        BaseFigSet,
        BasePlotter,
        CAEGraph,
        DefaultFigTheme,
        KPriceLine,
        PerSymFigs,
        PlotSet,
    )

    getter = lambda: CurrSymbol.sym(False)
    ff = lambda df, name: C3.FrameFeature(
        df, f"{bindings.graph_name}:{name}", bindings.calendar_name
    )
    sf = lambda df, name: C3.PerSymbolFrameFeature(
        df, f"{bindings.graph_name}:{name}", getter, bindings.calendar_name
    )

    revision_feat = ff(prepared.revisions, "revisions")
    revision_link_feat = ff(prepared.revision_links, "revision-links")
    required_feat = ff(prepared.required_summary, "required")
    member_feat = sf(prepared.members, "members")
    a2c_feat = sf(prepared.member_actual_confirmation, "actual-confirmation")
    c2k_feat = sf(prepared.member_confirmation_known, "confirmation-known")
    raw_feat = sf(prepared.raw_turns, "raw-turns")

    class Note(BaseFigSet):
        params = lambda: dict(text="", width=1200)

        def plot_figs(self, ctx):
            ctx.figs.append(Div(text=self.P.text, width=self.P.width))

    class StaticGlyphs(BasePlotter):
        params = lambda: dict(
            feat=None,
            x=None,
            y=None,
            marker="circle",
            marker_field=None,
            color="#1565c0",
            color_field=None,
            size=9,
            alpha=0.65,
            label=None,
            hover=(),
            uti=(),
            labels=None,
        )

        def _plot_fig(self, ctx):
            t0 = time.perf_counter()
            frame = _frame_of(self.P.feat)
            mask = _range_mask(
                frame, (self.P.x,), ctx.uti_slice.start, ctx.uti_slice.stop
            )
            frame = frame.loc[mask].copy()
            t1 = time.perf_counter()
            if frame.empty:
                return

            group_fields = [
                field
                for field in (self.P.marker_field, self.P.color_field)
                if field is not None
            ]
            grouped: Iterable[tuple[Any, pd.DataFrame]]
            if group_fields:
                grouped = frame.groupby(group_fields, dropna=False, sort=False)
            else:
                grouped = [((), frame)]

            for key, group in grouped:
                key_tuple = key if isinstance(key, tuple) else (key,)
                group_map = dict(zip(group_fields, key_tuple))
                marker = (
                    str(group_map[self.P.marker_field])
                    if self.P.marker_field
                    else self.P.marker
                )
                color = (
                    str(group_map[self.P.color_field])
                    if self.P.color_field
                    else self.P.color
                )
                x_values = pd.to_numeric(group[self.P.x], errors="coerce").to_numpy()
                y_values = pd.to_numeric(group[self.P.y], errors="coerce").to_numpy()
                valid = np.isfinite(x_values) & np.isfinite(y_values)
                x_values = x_values[valid].astype(np.intp, copy=False)
                group = group.iloc[np.flatnonzero(valid)]
                y_values = y_values[valid]
                if len(group) == 0:
                    continue

                data: dict[str, Any] = {
                    "x": ctx.uti2x(x_values),
                    "x_ts": ctx.uti2tslabel(x_values),
                    "y": y_values,
                }
                for column in self.P.hover:
                    if column in group:
                        data[column] = group[column].astype(str).to_numpy()
                for column in self.P.uti:
                    if column in group:
                        raw = pd.to_numeric(group[column], errors="coerce").to_numpy()
                        safe = np.where(np.isfinite(raw), raw, 0).astype(np.intp)
                        data[column + "_ts"] = ctx.uti2tslabel(safe)

                cds = ColumnDataSource(data)
                ctx.add_cds(
                    f"glyph:{self.P.label}:{marker}:{color}",
                    cds,
                    t1 - t0,
                    time.perf_counter() - t1,
                )
                glyph_args: dict[str, Any] = {}
                if self.P.label:
                    glyph_args["legend_label"] = self.P.label
                    glyph_args["name"] = self.P.label
                renderer = ctx.figs[-1].scatter(
                    x="x",
                    y="y",
                    source=cds,
                    marker=marker,
                    color=color,
                    size=self.P.size,
                    alpha=self.P.alpha,
                    **glyph_args,
                )
                tooltips = [("time", "@x_ts")]
                tooltips.extend((column, f"@{column}") for column in self.P.hover)
                ctx.figs[-1].add_tools(
                    HoverTool(renderers=[renderer], tooltips=tooltips)
                )
                ctx.fit_ys(cds)

            if self.P.labels:
                ctx.figs[-1].yaxis.ticker = FixedTicker(
                    ticks=list(self.P.labels)
                )
                ctx.figs[-1].yaxis.major_label_overrides = self.P.labels

    class StaticSegments(BasePlotter):
        params = lambda: dict(
            feat=None,
            color="#607d8b",
            dash="dashed",
            width=1.5,
            alpha=0.45,
            label=None,
            hover=(),
        )

        def _plot_fig(self, ctx):
            t0 = time.perf_counter()
            frame = _frame_of(self.P.feat)
            mask = _range_mask(
                frame, ("x0", "x1"), ctx.uti_slice.start, ctx.uti_slice.stop
            )
            frame = frame.loc[mask].copy()
            t1 = time.perf_counter()
            if frame.empty:
                return

            x0 = pd.to_numeric(frame["x0"], errors="coerce").to_numpy()
            x1 = pd.to_numeric(frame["x1"], errors="coerce").to_numpy()
            y0 = pd.to_numeric(frame["y0"], errors="coerce").to_numpy()
            y1 = pd.to_numeric(frame["y1"], errors="coerce").to_numpy()
            valid = np.isfinite(x0) & np.isfinite(x1) & np.isfinite(y0) & np.isfinite(y1)
            frame = frame.iloc[np.flatnonzero(valid)]
            x0 = x0[valid].astype(np.intp, copy=False)
            x1 = x1[valid].astype(np.intp, copy=False)
            y0 = y0[valid]
            y1 = y1[valid]
            if len(frame) == 0:
                return

            data: dict[str, Any] = {
                "x0": ctx.uti2x(x0),
                "x1": ctx.uti2x(x1),
                "y0": y0,
                "y1": y1,
                "x0_ts": ctx.uti2tslabel(x0),
                "x1_ts": ctx.uti2tslabel(x1),
            }
            for column in self.P.hover:
                if column in frame:
                    data[column] = frame[column].astype(str).to_numpy()

            cds = ColumnDataSource(data)
            ctx.add_cds(
                f"segment:{self.P.label}",
                cds,
                t1 - t0,
                time.perf_counter() - t1,
            )
            glyph_args: dict[str, Any] = {}
            if self.P.label:
                glyph_args["legend_label"] = self.P.label
                glyph_args["name"] = self.P.label
            renderer = ctx.figs[-1].segment(
                x0="x0",
                y0="y0",
                x1="x1",
                y1="y1",
                source=cds,
                color=self.P.color,
                line_dash=self.P.dash,
                line_width=self.P.width,
                alpha=self.P.alpha,
                **glyph_args,
            )
            tooltips = [("from", "@x0_ts"), ("to", "@x1_ts")]
            tooltips.extend((column, f"@{column}") for column in self.P.hover)
            ctx.figs[-1].add_tools(
                HoverTool(renderers=[renderer], tooltips=tooltips)
            )
            ctx.fit_ys(cds, "x0", "y0")
            ctx.fit_ys(cds, "x1", "y1")

    price_plots: list[Any] = [
        KPriceLine(
            feat=bindings.price_feature,
            add_hover=True,
            label=f"{FREQUENCY} KLine",
        )
    ]
    if not prepared.raw_turns.empty:
        price_plots.append(
            StaticGlyphs(
                feat=raw_feat,
                x="actual",
                y="price",
                color="#616161",
                size=6,
                alpha=0.25,
                label="raw ScaleTurn",
                hover=("turn_exact", "round", "direction", "turn_type"),
                uti=("actual", "confirmation", "known"),
            )
        )
    price_plots.extend(
        [
            StaticSegments(
                feat=a2c_feat,
                color="#5c6bc0",
                dash="dotted",
                width=2,
                label="actual→confirmation",
                hover=("candidate_life", "candidate_revision", "turn_exact"),
            ),
            StaticSegments(
                feat=c2k_feat,
                color="#8d6e63",
                dash="dashed",
                width=2,
                label="confirmation→known",
                hover=("candidate_life", "candidate_revision", "turn_exact"),
            ),
            StaticGlyphs(
                feat=member_feat,
                x="actual",
                y="price",
                marker_field="actual_marker",
                color_field="color",
                size=11,
                label="candidate member actual",
                hover=(
                    "candidate_life",
                    "candidate_revision",
                    "basis",
                    "observation",
                    "turn_exact",
                    "source_exact",
                    "round",
                    "direction",
                    "turn_type",
                    "member_status",
                ),
                uti=("actual", "confirmation", "member_known", "known"),
            ),
            StaticGlyphs(
                feat=member_feat,
                x="confirmation",
                y="price",
                marker="triangle",
                color="#5c6bc0",
                size=9,
                label="member confirmation",
                hover=(
                    "candidate_life",
                    "candidate_revision",
                    "turn_exact",
                    "round",
                    "direction",
                    "turn_type",
                ),
                uti=("actual", "confirmation", "member_known", "known"),
            ),
            StaticGlyphs(
                feat=member_feat,
                x="member_known",
                y="price",
                marker="diamond",
                color="#8d6e63",
                size=8,
                label="member known",
                hover=(
                    "candidate_life",
                    "candidate_revision",
                    "turn_exact",
                    "member_status",
                ),
                uti=("actual", "confirmation", "member_known", "known"),
            ),
        ]
    )

    warnings = "".join(f"<li>{w}</li>" for w in prepared.data_warnings)
    note_text = (
        "<h2>CommonPriceTurnGroupCandidatesFrp display</h2>"
        f"<p>{bindings.instance_label}</p>"
        f"<p>position={POSITION_ID}; candidate x=groupKnownFrom; "
        "member actual/confirmation/known stay distinct.</p>"
        f"<ul>{warnings}</ul>"
    )

    return CAEGraph(
        Context=OptContext(bindings.sof_name),
        plotsets=GMapX(
            {
                "F candidate audit": PlotSet(
                    calendar_name=bindings.calendar_name,
                    timespans=list(bindings.timespans),
                    blk=list(bindings.symbols),
                    figs=GMapX.from_list(
                        [
                            Note(text=note_text),
                            PerSymFigs(
                                title="!{sym}｜5m price + candidate member evidence",
                                plots=GMapX.from_list(price_plots),
                                fig_height=240,
                            ),
                            AllSymsFig(
                                title=(
                                    "F revisions｜x=groupKnownFrom; "
                                    "y=groupObservation"
                                ),
                                plots=GMapX.from_list(
                                    [
                                        StaticSegments(
                                            feat=revision_link_feat,
                                            label="previous→revision",
                                            hover=(
                                                "candidate_life",
                                                "previous_revision",
                                                "candidate_revision",
                                            ),
                                        ),
                                        StaticGlyphs(
                                            feat=revision_feat,
                                            x="known",
                                            y="state_y",
                                            marker_field="marker",
                                            color_field="color",
                                            size=12,
                                            label="candidate revision",
                                            hover=(
                                                "candidate_life",
                                                "candidate_revision",
                                                "previous_revision",
                                                "basis",
                                                "observation",
                                                "members",
                                                "alternative",
                                                "coverage",
                                                "closed",
                                                "overlaps",
                                                "covered_by",
                                                "groupOriginalAnchor",
                                                "groupOriginalDeadline",
                                                "groupOriginalRevisionEnd",
                                                "groupAnchor",
                                                "groupDeadline",
                                                "groupRevisionEnd",
                                            ),
                                            uti=("known",),
                                            labels={
                                                value: name
                                                for name, value in C3.OBS_Y.items()
                                            },
                                        ),
                                    ]
                                ),
                                fig_height=260,
                            ),
                            AllSymsFig(
                                title=(
                                    "Required audit｜worst/count summary; "
                                    "exact pair reasons in hover"
                                ),
                                plots=GMapX.from_list(
                                    [
                                        StaticGlyphs(
                                            feat=required_feat,
                                            x="known",
                                            y="coord_y",
                                            marker_field="marker",
                                            color_field="color",
                                            size=11,
                                            label="Required verdict",
                                            hover=(
                                                "candidate_life",
                                                "candidate_revision",
                                                "coordinate",
                                                "verdict",
                                                "counts",
                                                "details",
                                            ),
                                            uti=("known",),
                                            labels={
                                                value: name
                                                for name, value in C3.COORD_Y.items()
                                            },
                                        )
                                    ]
                                ),
                                fig_height=240,
                            ),
                        ]
                    ),
                )
            }
        ),
        theme=DefaultFigTheme(),
        x_label_freq="30m",
        fig_width=1200,
        fig_height1=420,
        fig_height=240,
        plot_name="U2 F candidate display",
    )


def export_prepared_tables(prepared: Any, output_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest: dict[str, Any] = {}
    for name in (
        "revisions",
        "revision_links",
        "members",
        "member_actual_confirmation",
        "member_confirmation_known",
        "required_summary",
        "raw_turns",
    ):
        frame = getattr(prepared, name)
        path = output_dir / f"{name}.csv"
        frame.to_csv(path, index=True)
        manifest[name] = {
            "rows": int(len(frame)),
            "columns": list(map(str, frame.columns)),
            "path": str(path),
        }
    manifest["warnings"] = list(prepared.data_warnings)
    return manifest


def export_plot_data_tree(roots: Sequence[Any], output_dir: Path) -> list[dict[str, Any]]:
    from mquant.uplot import PlotDataFolder, PlotDataNode

    output_dir.mkdir(parents=True, exist_ok=True)
    exported: list[dict[str, Any]] = []
    counter = 0

    def walk(node: Any, path: tuple[str, ...]) -> None:
        nonlocal counter
        if isinstance(node, PlotDataFolder):
            for child in node.children:
                walk(child, (*path, node.name))
            return
        if not isinstance(node, PlotDataNode):
            raise TypeError(f"unexpected plot data node: {type(node)!r}")
        counter += 1
        logical = (*path, node.name)
        filename = f"{counter:04d}__{_safe_name('__'.join(logical))}.csv"
        csv_path = output_dir / filename
        frame = pd.DataFrame(node.cds.data)
        frame.to_csv(csv_path, index=False)
        exported.append(
            {
                "logical_path": list(logical),
                "csv": str(csv_path),
                "rows": int(len(frame)),
                "columns": list(map(str, frame.columns)),
                "data_fetch_time": float(node.data_fetch_time),
                "data_trans_time": float(node.data_trans_time),
            }
        )

    for root in roots:
        walk(root, ())
    return exported


def _default_output_dir() -> Path:
    return _THIS.parents[1] / "E" / "runtime" / "u2_f_caegraph"


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render the D004 integrated U2-F CAEGraph from existing outputs."
    )
    parser.add_argument("--output-dir", type=Path, default=_default_output_dir())
    parser.add_argument(
        "--metadata-only",
        action="store_true",
        help="construct/read bindings and prepared tables but do not render Bokeh HTML",
    )
    return parser.parse_args()


def main() -> int:
    args = cli()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    report: dict[str, Any] = {
        "definition_id": DEFINITION_ID,
        "run_id": RUN_ID,
        "position_id": POSITION_ID,
        "source_refs": SOURCE_REFS,
        "binding": {
            "sof_name": SOF_NAME,
            "block_context": BLOCK_CONTEXT,
            "symbols": list(SYMBOLS),
            "calendar_name": CALENDAR_NAME,
            "frequency": FREQUENCY,
            "timespans": [list(item) for item in TIMESPANS],
            "candidate_position_field": "groupKnownFrom",
        },
        "feature_params": {
            **FEATURE_PARAMS,
            "symbols": list(FEATURE_PARAMS["symbols"]),
        },
        "producer_policy": {
            "candidate_rerun": False,
            "read_existing_fields_only": True,
            "raw_turn_overlay": "not_injected; candidate member evidence remains",
        },
        "completed": False,
    }
    report_path = args.output_dir / "definition_run_report.json"

    try:
        from bokeh.embed import file_html
        from bokeh.resources import INLINE
        from mquant.frame import CurrCalendar, CurrSof, KLine
        from mquant.tis.frp.fqv_kline_example import make_features

        with CurrSof(sof_name=SOF_NAME, stk_tlist=BLOCK_CONTEXT), CurrCalendar(
            CALENDAR_NAME
        ):
            f, _q, _v = make_features(**FEATURE_PARAMS)
            if type(f).__name__ != "CommonPriceTurnGroupCandidatesFrp":
                raise TypeError(f"unexpected F type: {type(f)!r}")
            fields_file = Path(f.full_dir) / "fields.json"
            if not fields_file.is_file():
                raise FileNotFoundError(
                    "The exact F instance has no existing fields.json. "
                    "This D/E definition is read-only and will not call f.rerun(). "
                    f"Expected: {fields_file}"
                )

            price_feature = KLine(freq=FREQUENCY)
            prepared = C3.prepare_display_tables(
                f,
                table_names=C3.CandidateTableNames(),
                raw_turn_view=None,
            )
            bindings = C3.DisplayBindings(
                candidate_feature=f,
                price_feature=price_feature,
                symbols=SYMBOLS,
                sof_name=SOF_NAME,
                calendar_name=CALENDAR_NAME,
                timespans=TIMESPANS,
                raw_turn_view=None,
                instance_label=(
                    "make_features(**FEATURE_PARAMS)[0] / "
                    "TA_updto20240229_DBA / steel / "
                    "night_end_at_2300 / 5m / rb,hc,i"
                ),
                graph_name="u2_f_candidate_display_d004_v1",
            )

            report["feature"] = {
                "type": type(f).__name__,
                "full_dir": str(f.full_dir),
                "fields_file": str(fields_file),
                "fields_file_exists": True,
            }
            report["prepared_tables"] = export_prepared_tables(
                prepared, args.output_dir / "prepared_tables"
            )

            graph = build_bound_caegraph(bindings, prepared)
            if not args.metadata_only:
                plot_roots: list[Any] = []
                layout = graph.layout(ncols=1, plot_roots=plot_roots)
                html_path = args.output_dir / "u2_f_caegraph.html"
                html_path.write_text(
                    file_html(layout, INLINE, "U2 F CAEGraph"),
                    encoding="utf-8",
                )
                report["html"] = str(html_path)
                report["plot_data"] = export_plot_data_tree(
                    plot_roots, args.output_dir / "plot_data"
                )

            report["completed"] = True
    except Exception as exc:
        import traceback

        report["error_type"] = type(exc).__name__
        report["error"] = str(exc)
        report["traceback"] = traceback.format_exc()
    finally:
        report_path.write_text(
            json.dumps(report, ensure_ascii=False, indent=2, default=str) + "\n",
            encoding="utf-8",
        )
        print(
            json.dumps(
                {key: value for key, value in report.items() if key != "traceback"},
                ensure_ascii=False,
                indent=2,
                default=str,
            )
        )
        print("REPORT:", report_path)

    return 0 if report["completed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
