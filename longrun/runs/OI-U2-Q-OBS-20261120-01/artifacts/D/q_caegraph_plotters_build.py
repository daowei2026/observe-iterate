"""Exact-audit plotter and final CAEGraph assembly."""
from q_caegraph_common import *
from q_caegraph_plotters_base import *
from q_caegraph_plotters_member import *

class QAuditPlot(BasePlotter):
    params = lambda: dict(frames=None)

    def _plot_fig(self, ctx: Any) -> None:
        fig = ctx.figs[-1]
        frame = _slice(
            self.P.frames.audit, "event_uti", ctx
        ).reset_index(drop=True)
        if frame.empty:
            return
        frame["x"] = frame.event_uti.astype(float)
        frame["y"] = np.arange(len(frame), 0, -1, dtype=float)
        frame["text"] = (
            frame.event_id.astype(str)
            + " | prev="
            + frame.previous_ref.fillna("None").astype(str)
            + " | F="
            + frame.candidate_ref.fillna("None").astype(str)
            + " | "
            + frame.detail.astype(str)
        )
        frame["ts"] = ctx.uti2tslabel(
            frame.event_uti.astype(int).to_numpy()
        )
        source = _registered_cds(
            ctx,
            "Q exact audit",
            frame,
            [
                "x",
                "y",
                "text",
                "ts",
                "event_id",
                "event_kind",
                "previous_ref",
                "candidate_ref",
                "publication_or_end_known",
                "detail",
            ],
        )
        glyph = fig.text(
            x="x",
            y="y",
            text="text",
            source=source,
            text_font_size="9pt",
            text_align="left",
            text_baseline="middle",
        )
        _hover(
            fig,
            glyph,
            [
                ("event", "@event_id"),
                ("type", "@event_kind"),
                ("time", "@ts"),
                ("Previous", "@previous_ref"),
                ("F candidate", "@candidate_ref"),
                ("known", "@publication_or_end_known"),
                ("detail", "@detail"),
            ],
        )
        fig.yaxis.visible = False
        fig.y_range.start, fig.y_range.end = 0, max(2.0, len(frame) + 1.0)


def build_q_caegraph(binding: QDisplayBinding) -> CAEGraph:
    binding.validate()
    frames = binding.frames
    position = binding.position
    figures = GMap(
        {
            "overview": AllSymsMainFig(
                dict(
                    title="!Q multi-symbol 5m price (ratio display derivative)",
                    persym_plots=GMap(
                        {
                            "price": KPriceLine(
                                feat=binding.price_feature,
                                std_method="ratio",
                                label="5m price ratio",
                            ),
                            "member": QMemberGeometryPlot(
                                dict(
                                    frames=frames,
                                    follow_price_standardization=True,
                                )
                            ),
                        }
                    ),
                )
            ),
            "lifecycle": AllSymsFig(
                dict(
                    title="!F candidate → Q revision → explicit duty end",
                    plots=GMap(
                        {"life": QLifecyclePlot(dict(frames=frames))}
                    ),
                    fig_height=230,
                )
            ),
            "state": AllSymsFig(
                dict(
                    title="!Q group state by emitted revision",
                    plots=GMap({"state": QStatePlot(dict(frames=frames))}),
                    fig_height=210,
                )
            ),
            "members": PerSymFigSet(
                dict(
                    figs=GMap(
                        {
                            "raw": MainFig(
                                dict(
                                    title=(
                                        "!{sym} raw price + "
                                        "asked/used/successor/endpoint"
                                    ),
                                    plots=GMap(
                                        {
                                            "price": KPriceLine(
                                                feat=binding.price_feature,
                                                std_method=None,
                                                label="5m raw price",
                                            ),
                                            "member": QMemberGeometryPlot(
                                                dict(
                                                    frames=frames,
                                                    follow_price_standardization=False,
                                                )
                                            ),
                                        }
                                    ),
                                )
                            ),
                            "audit": SubFig(
                                dict(
                                    title=(
                                        "!{sym} member verdict/completion/"
                                        "quantity audit"
                                    ),
                                    plots=GMap(
                                        {
                                            "audit": QMemberAuditPlot(
                                                dict(frames=frames)
                                            )
                                        }
                                    ),
                                    fig_height=270,
                                )
                            ),
                        }
                    )
                )
            ),
            "detail": AllSymsFig(
                dict(
                    title="!Q exact refs / Previous / F ref / explicit end",
                    plots=GMap(
                        {"audit": QAuditPlot(dict(frames=frames))}
                    ),
                    fig_height=220,
                )
            ),
        }
    )
    return CAEGraph(
        dict(
            Context=OptContext(
                sof_name=position.sof_name, stk_tlist=position.block
            ),
            plotsets=GMap(
                {
                    binding.graph_name: PlotSet(
                        dict(
                            calendar_name=position.calendar_name,
                            blk=list(position.objects),
                            timespans=list(position.timespans),
                            figs=figures,
                        )
                    )
                }
            ),
            theme=DefaultFigTheme(),
            x_label_freq="1h",
            extra_time=0,
            fig_width=1200,
            fig_height1=420,
            fig_height=240,
            manual_upd=True,
            plot_name=binding.plot_name,
            switches={},
        )
    )

__all__ = [name for name in globals() if not name.startswith("__")]
