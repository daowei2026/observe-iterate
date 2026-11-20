"""Shared slicing, CDS registration, lifecycle and state plotters."""
from q_caegraph_common import *

def _slice(df: pd.DataFrame, field: str, ctx: Any) -> pd.DataFrame:
    if df.empty:
        return df.copy()
    values = pd.to_numeric(df[field], errors="coerce")
    return df.loc[
        values.ge(ctx.uti_slice.start) & values.lt(ctx.uti_slice.stop)
    ].copy()


def _registered_cds(
    ctx: Any, name: str, frame: pd.DataFrame, columns: Sequence[str]
) -> ColumnDataSource:
    """Create a CDS and expose it through PlotDataFolder/PlotDataNode."""
    data: dict[str, np.ndarray] = {}
    for column in columns:
        if column in frame:
            data[column] = frame[column].to_numpy()
        else:
            data[column] = np.full(len(frame), None, dtype=object)
    cds = ColumnDataSource(data)
    ctx.add_cds(name, cds, 0.0, 0.0)
    return cds


def _hover(fig: Any, glyph: Any, tips: Sequence[tuple[str, str]]) -> None:
    fig.add_tools(HoverTool(renderers=[glyph], tooltips=list(tips)))


class QLifecyclePlot(BasePlotter):
    params = lambda: dict(frames=None)
    lane = {"F candidate": 2.0, "Q revision": 1.0, "Duty end": 0.0}
    marker = {"F candidate": "square", "Q revision": "circle", "Duty end": "diamond"}
    color = {"F candidate": "#64748b", "Q revision": "#2563eb", "Duty end": "#dc2626"}

    def _plot_fig(self, ctx: Any) -> None:
        fig = ctx.figs[-1]
        frame = _slice(self.P.frames.timeline, "event_uti", ctx)
        if frame.empty:
            return
        frame["x"] = frame.event_uti.astype(float)
        frame["y"] = frame.event_kind.map(self.lane)
        frame["ts"] = ctx.uti2tslabel(frame.event_uti.astype(int).to_numpy())
        columns = [
            "x",
            "y",
            "ts",
            "event_id",
            "event_kind",
            "q_life",
            "q_revision",
            "previous_ref",
            "candidate_ref",
            "members",
            "known_uti",
            "qualification",
            "observation",
            "applicability",
            "end_reason",
            "last_successful_ref",
            "detail",
        ]
        for kind in self.lane:
            part = frame.loc[frame.event_kind.eq(kind)]
            if part.empty:
                continue
            source = _registered_cds(
                ctx, f"Q lifecycle/{kind}", part, columns
            )
            glyph = fig.scatter(
                x="x",
                y="y",
                source=source,
                marker=self.marker[kind],
                size=11,
                color=self.color[kind],
                alpha=0.9,
                legend_label=kind,
            )
            _hover(
                fig,
                glyph,
                [
                    ("type", "@event_kind"),
                    ("event", "@event_id"),
                    ("time", "@ts"),
                    ("Q", "@q_life / @q_revision"),
                    ("Previous", "@previous_ref"),
                    ("F candidate", "@candidate_ref"),
                    ("members", "@members"),
                    ("known", "@known_uti"),
                    ("qualification", "@qualification"),
                    ("observation", "@observation"),
                    ("applicability", "@applicability"),
                    ("end reason", "@end_reason"),
                    ("last successful", "@last_successful_ref"),
                    ("detail", "@detail"),
                ],
            )

        links = self.P.frames.revision_links
        if not links.empty:
            keep = (
                pd.to_numeric(links.from_uti, errors="coerce").lt(
                    ctx.uti_slice.stop
                )
                & pd.to_numeric(links.to_uti, errors="coerce").ge(
                    ctx.uti_slice.start
                )
            )
            links = links.loc[keep].copy()
            if not links.empty:
                links["y0"] = links["y1"] = 1.0
                source = _registered_cds(
                    ctx,
                    "Q lifecycle/Previous links",
                    links,
                    [
                        "from_uti",
                        "to_uti",
                        "y0",
                        "y1",
                        "q_life",
                        "from_revision",
                        "to_revision",
                    ],
                )
                glyph = fig.segment(
                    x0="from_uti",
                    x1="to_uti",
                    y0="y0",
                    y1="y1",
                    source=source,
                    color="#93c5fd",
                    line_width=3,
                    legend_label="Q Previous chain",
                )
                _hover(
                    fig,
                    glyph,
                    [
                        ("Q Life", "@q_life"),
                        ("revision", "@from_revision → @to_revision"),
                    ],
                )
        fig.yaxis.ticker = FixedTicker(ticks=[0, 1, 2])
        fig.yaxis.major_label_overrides = {
            0: "Duty end",
            1: "Q revision",
            2: "F candidate",
        }
        fig.y_range.start, fig.y_range.end = -0.5, 2.5


class QStatePlot(BasePlotter):
    params = lambda: dict(frames=None)
    lane = {"qualification": 2.0, "observation": 1.0, "applicability": 0.0}
    colors = {
        "QualifiedCompleted": "#15803d",
        "QualifiedWorking": "#16a34a",
        "QualificationPending": "#d97706",
        "QualificationConflict": "#dc2626",
        "QualificationRejected": "#991b1b",
        "MotionObserving": "#2563eb",
        "HorizonReached": "#7c3aed",
        "MotionScopeEnded": "#475569",
        "SubjectApplicable": "#0f766e",
        "SubjectWithdrawn": "#dc2626",
    }

    def _plot_fig(self, ctx: Any) -> None:
        fig = ctx.figs[-1]
        frame = _slice(self.P.frames.states, "publication_uti", ctx)
        if frame.empty:
            return
        frame["x"] = frame.publication_uti.astype(float)
        frame["y"] = frame.state_kind.map(self.lane)
        frame["color"] = frame.state_value.map(self.colors).fillna("#64748b")
        frame["ts"] = ctx.uti2tslabel(
            frame.publication_uti.astype(int).to_numpy()
        )
        source = _registered_cds(
            ctx,
            "Q state",
            frame,
            [
                "x",
                "y",
                "color",
                "ts",
                "q_life",
                "q_revision",
                "state_kind",
                "state_value",
                "detail",
            ],
        )
        glyph = fig.scatter(
            x="x",
            y="y",
            source=source,
            marker="circle",
            size=10,
            color="color",
            alpha=0.9,
        )
        _hover(
            fig,
            glyph,
            [
                ("time", "@ts"),
                ("Q", "@q_life / @q_revision"),
                ("kind", "@state_kind"),
                ("state", "@state_value"),
                ("detail", "@detail"),
            ],
        )
        fig.yaxis.ticker = FixedTicker(ticks=[0, 1, 2])
        fig.yaxis.major_label_overrides = {
            0: "applicability",
            1: "observation",
            2: "qualification",
        }
        fig.y_range.start, fig.y_range.end = -0.5, 2.5

__all__ = [name for name in globals() if not name.startswith("__")]
