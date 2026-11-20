#!/usr/bin/env python3
"""D004 executable integration entry for Q CAEGraph.

The sibling modules are part of this one complete locked definition:
q_caegraph_common.py, q_caegraph_adapter.py, q_caegraph_plotters.py.
"""
from q_caegraph_common import *
from q_caegraph_adapter import *
from q_caegraph_plotters import *

def _feature_bundle(mode: str, allow_rerun: bool) -> tuple[Any, Any, Any]:
    """Create the exact instance inside the caller's SOF/calendar context."""
    formation, q_feature, _validity = make_features(**PARAMS)
    if mode == "read":
        for name, feature in (("F", formation), ("Q", q_feature)):
            fields_file = Path(feature.full_dir) / "fields.json"
            if not fields_file.is_file():
                raise FileNotFoundError(
                    f"{name}: exact instance has no fields.json at {fields_file}; "
                    "read mode never fills missing products by rerun"
                )
    elif mode == "rerun":
        if not allow_rerun:
            raise PermissionError(
                "rerun requires --allow-full-period-rerun"
            )
        # Q intentionally does not auto-rerun F.  Produce the exact necessary
        # upstream first, then produce Q; V remains outside this definition.
        formation.rerun(2)
        q_feature = q_feature.rerun(2)
    else:
        raise ValueError(f"unsupported mode: {mode!r}")

    price_feature = KLine(freq=FREQUENCY)
    frames = read_q_display_frames(q_feature)
    return q_feature, price_feature, frames


def build_integrated_graph(
    mode: str = "read", allow_rerun: bool = False
) -> tuple[CAEGraph, QDisplayFrames]:
    with CurrSof(sof_name=SOF_NAME, stk_tlist=BLOCK), CurrCalendar(CALENDAR):
        q_feature, price_feature, frames = _feature_bundle(mode, allow_rerun)
        definition = frames.definition
        method = (
            f"{definition['direction']} Δ={definition['delta']:g} · "
            f"{definition['observation_multiples']}Δ observation · "
            f"{definition['revision_multiples']}Δ revision · "
            f"min={definition['minimum_members']}"
        )
        binding = QDisplayBinding(
            q_feature=q_feature,
            price_feature=price_feature,
            frames=frames,
            position=QPositionBinding(
                sof_name=SOF_NAME,
                block=BLOCK,
                calendar_name=CALENDAR,
                objects=OBJECTS,
                timespans=TIMESPANS,
            ),
            graph_name=f"Q direction organization | {method}",
            plot_name=f"Q PostTurnGroupDirectionalOrganization | {method}",
        )
        return build_q_caegraph(binding), frames


def _sanitize(value: str) -> str:
    value = re.sub(r"[^0-9A-Za-z._-]+", "_", value).strip("_")
    return value[:100] or "plot_data"


def export_plot_data(
    roots: Sequence[PlotDataFolder], output_dir: Path
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest: list[dict[str, Any]] = []

    def visit(node: Any, path: tuple[str, ...]) -> None:
        current = (*path, str(node.name))
        if isinstance(node, PlotDataFolder):
            for child in node.children:
                visit(child, current)
            return
        if not isinstance(node, PlotDataNode):
            raise TypeError(f"unknown plot-data node: {type(node)!r}")
        frame = pd.DataFrame(node.cds.data)
        filename = "__".join(map(_sanitize, current)) + ".csv"
        target = output_dir / filename
        frame.to_csv(target, index=False)
        manifest.append(
            {
                "path": list(current),
                "csv": str(target),
                "rows": int(len(frame)),
                "columns": list(map(str, frame.columns)),
                "data_fetch_time": float(node.data_fetch_time),
                "data_trans_time": float(node.data_trans_time),
            }
        )

    for root in roots:
        visit(root, ())
    manifest_path = output_dir / "plot_data_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, default=str) + "\n",
        encoding="utf-8",
    )
    return manifest_path


def export_canonical_frames(frames: QDisplayFrames, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest: dict[str, Any] = {
        "run_id": RUN_ID,
        "definition": dict(frames.definition),
        "frames": {},
    }
    for name in (
        "timeline",
        "revision_links",
        "states",
        "members",
        "quantities",
        "audit",
    ):
        frame = getattr(frames, name)
        path = output_dir / f"canonical_{name}.csv"
        frame.to_csv(path, index=False)
        manifest["frames"][name] = {
            "csv": str(path),
            "rows": int(len(frame)),
            "columns": list(map(str, frame.columns)),
        }
    path = output_dir / "canonical_frames_manifest.json"
    path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, default=str) + "\n",
        encoding="utf-8",
    )
    return path


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render the integrated Q CAEGraph definition"
    )
    parser.add_argument(
        "--mode",
        choices=("read", "rerun"),
        default="read",
        help="read existing formal F/Q products, or explicitly rerun Q",
    )
    parser.add_argument(
        "--allow-full-period-rerun",
        action="store_true",
        help="required with --mode rerun; D never grants this permission itself",
    )
    parser.add_argument("--output-html", type=Path, default=DEFAULT_HTML)
    parser.add_argument("--output-data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--ncols", type=int, default=1)
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="read and validate formal frames without rendering HTML",
    )
    parser.add_argument(
        "--skip-data-export",
        action="store_true",
        help="do not export canonical/PlotDataNode CSV evidence",
    )
    args = parser.parse_args(argv)
    if args.mode == "rerun" and not args.allow_full_period_rerun:
        parser.error(
            "--mode rerun requires --allow-full-period-rerun"
        )
    return args


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    graph, frames = build_integrated_graph(
        mode=args.mode, allow_rerun=args.allow_full_period_rerun
    )
    result: dict[str, Any] = {
        "run_id": RUN_ID,
        "mode": args.mode,
        "sof": SOF_NAME,
        "block": BLOCK,
        "calendar": CALENDAR,
        "objects": list(OBJECTS),
        "timespans": [list(span) for span in TIMESPANS],
        "definition": dict(frames.definition),
        "canonical_rows": {
            name: int(len(getattr(frames, name)))
            for name in (
                "timeline",
                "revision_links",
                "states",
                "members",
                "quantities",
                "audit",
            )
        },
        "validated": True,
        "rendered": False,
    }
    if not args.skip_data_export:
        result["canonical_manifest"] = str(
            export_canonical_frames(frames, args.output_data_dir)
        )
    if not args.validate_only:
        args.output_html.parent.mkdir(parents=True, exist_ok=True)
        plot_roots: list[PlotDataFolder] = []
        layout = graph.layout(ncols=args.ncols, plot_roots=plot_roots)
        output_file(str(args.output_html), title=graph.P.plot_name)
        save(layout)
        result["rendered"] = True
        result["html"] = str(args.output_html)
        if not args.skip_data_export:
            result["plot_data_manifest"] = str(
                export_plot_data(plot_roots, args.output_data_dir)
            )
    report_path = args.output_data_dir / "q_caegraph_run_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, default=str) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
