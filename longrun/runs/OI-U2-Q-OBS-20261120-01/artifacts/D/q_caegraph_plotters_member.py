"""Per-member geometry and quantity audit plotters."""
from q_caegraph_common import *
from q_caegraph_plotters_base import _slice, _registered_cds, _hover

class QMemberGeometryPlot(BasePlotter):
    params = lambda: dict(frames=None, follow_price_standardization=False)
    points = (
        ("asked", "asked_uti", "asked_price", "square", "#64748b"),
        ("used", "used_uti", "used_price", "circle", "#7c3aed"),
        ("successor", "successor_uti", "successor_price", "diamond", "#dc2626"),
        ("endpoint", "endpoint_uti", "endpoint_price", "triangle", "#0f766e"),
    )

    def _plot_fig(self, ctx: Any) -> None:
        fig = ctx.figs[-1]
        symbol = CurrSymbol.sym()
        frame = self.P.frames.members
        frame = _slice(frame.loc[frame.member.eq(symbol)], "publication_uti", ctx)
        if frame.empty:
            return
        common = [
            "q_life",
            "q_revision",
            "member",
            "completion",
            "verdict",
            "basis",
            "path_complete",
            "through",
            "material_known",
            "missing_range",
            "candidate_ref",
            "asked_confirmation",
            "asked_known",
            "asked_clock",
            "asked_clock_known",
            "used_confirmation",
            "used_known",
            "used_clock",
            "used_clock_known",
            "successor_confirmation",
            "successor_known",
            "successor_clock",
            "successor_clock_known",
            "endpoint_known",
            "endpoint_clock",
            "endpoint_clock_known",
        ]
        segments = frame.dropna(
            subset=["used_uti", "used_price", "endpoint_uti", "endpoint_price"]
        )
        if not segments.empty:
            source = _registered_cds(
                ctx,
                f"Q member/{symbol}/used-to-endpoint",
                segments,
                [
                    "used_uti",
                    "used_price",
                    "endpoint_uti",
                    "endpoint_price",
                    *common,
                ],
            )
            glyph = fig.segment(
                x0="used_uti",
                y0="used_price",
                x1="endpoint_uti",
                y1="endpoint_price",
                source=source,
                color=ctx.sym_color,
                line_width=3,
                alpha=0.65,
                legend_label=f"{symbol} used→endpoint",
            )
            if self.P.follow_price_standardization:
                ctx.drive_entity_dynstd(
                    source,
                    [
                        ("used_uti", "used_price"),
                        ("endpoint_uti", "endpoint_price"),
                    ],
                )
            _hover(
                fig,
                glyph,
                [
                    ("Q", "@q_life / @q_revision"),
                    ("member", "@member"),
                    ("verdict", "@verdict"),
                    ("completion", "@completion"),
                    ("basis", "@basis"),
                    ("path complete", "@path_complete"),
                    ("through", "@through"),
                    ("material known", "@material_known"),
                    ("missing range", "@missing_range"),
                    ("F candidate", "@candidate_ref"),
                ],
            )
            ctx.fit_ys(source, "used_uti", "used_price")
            ctx.fit_ys(source, "endpoint_uti", "endpoint_price")

        for label, xfield, yfield, marker, color in self.points:
            part = frame.dropna(subset=[xfield, yfield]).copy()
            if part.empty:
                continue
            part["x"] = part[xfield]
            part["y"] = part[yfield]
            part["ts"] = ctx.uti2tslabel(part[xfield].astype(int).to_numpy())
            source = _registered_cds(
                ctx,
                f"Q member/{symbol}/{label}",
                part,
                ["x", "y", "ts", *common],
            )
            glyph = fig.scatter(
                x="x",
                y="y",
                source=source,
                marker=marker,
                size=9,
                color=color,
                alpha=0.9,
                legend_label=f"{symbol} {label}",
            )
            if self.P.follow_price_standardization:
                ctx.drive_entity_dynstd(source)
            _hover(
                fig,
                glyph,
                [
                    ("position", label),
                    ("time", "@ts"),
                    ("Q", "@q_life / @q_revision"),
                    ("member", "@member"),
                    ("verdict", "@verdict"),
                    ("completion", "@completion"),
                    ("basis", "@basis"),
                    ("path complete", "@path_complete"),
                    ("through", "@through"),
                    ("material known", "@material_known"),
                    ("missing range", "@missing_range"),
                    ("F candidate", "@candidate_ref"),
                ],
            )
            ctx.fit_ys(source)


class QMemberAuditPlot(BasePlotter):
    params = lambda: dict(frames=None)
    lanes = {
        "verdict": 8.0,
        "completion": 7.0,
        "path": 6.0,
        "ProgressP": 5.0,
        "AmplitudeA": 4.0,
        "DurationD": 3.0,
        "PathLengthL": 2.0,
        "EfficiencyE": 1.0,
        "CounterC": 0.0,
    }

    def _plot_fig(self, ctx: Any) -> None:
        fig = ctx.figs[-1]
        symbol = CurrSymbol.sym()
        members = _slice(
            self.P.frames.members.loc[
                self.P.frames.members.member.eq(symbol)
            ],
            "publication_uti",
            ctx,
        )
        rows: list[dict[str, Any]] = []
        for _, row in members.iterrows():
            for kind, value in (
                ("verdict", row.verdict),
                ("completion", row.completion),
                ("path", "Complete" if bool(row.path_complete) else "Incomplete"),
            ):
                rows.append(
                    {
                        "publication_uti": row.publication_uti,
                        "q_life": row.q_life,
                        "q_revision": row.q_revision,
                        "member": symbol,
                        "kind": kind,
                        "value": value,
                        "availability": "Known",
                    }
                )
        quantities = _slice(
            self.P.frames.quantities.loc[
                self.P.frames.quantities.member.eq(symbol)
            ],
            "publication_uti",
            ctx,
        )
        for _, row in quantities.iterrows():
            rows.append(
                {
                    "publication_uti": row.publication_uti,
                    "q_life": row.q_life,
                    "q_revision": row.q_revision,
                    "member": symbol,
                    "kind": row.quantity_kind,
                    "value": row.quantity_value,
                    "availability": row.availability,
                }
            )
        if not rows:
            return
        frame = pd.DataFrame(rows)
        frame["x"] = frame.publication_uti.astype(float)
        frame["y"] = frame.kind.map(self.lanes)
        frame["ts"] = ctx.uti2tslabel(
            frame.publication_uti.astype(int).to_numpy()
        )
        frame["color"] = np.where(
            frame.availability.eq("QuantityKnown"), "#2563eb", "#f59e0b"
        )
        frame.loc[frame.availability.eq("Known"), "color"] = "#0f766e"
        source = _registered_cds(
            ctx,
            f"Q member audit/{symbol}",
            frame,
            [
                "x",
                "y",
                "ts",
                "q_life",
                "q_revision",
                "member",
                "kind",
                "value",
                "availability",
                "color",
            ],
        )
        glyph = fig.scatter(
            x="x",
            y="y",
            source=source,
            marker="circle",
            size=8,
            color="color",
            alpha=0.9,
        )
        _hover(
            fig,
            glyph,
            [
                ("time", "@ts"),
                ("Q", "@q_life / @q_revision"),
                ("member", "@member"),
                ("field", "@kind"),
                ("raw value", "@value"),
                ("availability", "@availability"),
            ],
        )
        fig.yaxis.ticker = FixedTicker(ticks=list(self.lanes.values()))
        fig.yaxis.major_label_overrides = {
            int(value): key for key, value in self.lanes.items()
        }
        fig.y_range.start, fig.y_range.end = -0.5, 8.5

__all__ = [name for name in globals() if not name.startswith("__")]
