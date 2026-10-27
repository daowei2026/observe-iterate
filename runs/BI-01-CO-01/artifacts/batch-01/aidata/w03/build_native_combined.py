"""W03：复用 W02 原生概览 PlotSet，与本次四窗 30m/mid 组合到既有平台。

适配现场 build_native_combined.py；不定义新 Feature、不改注册配置或服务。
正式行情仍来自既有 aidata 交付，本程序不重新生成 W02 core/全历史切片。
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
from pathlib import Path
from urllib.parse import urlsplit


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--overview-node-id", default="6142")
    args = parser.parse_args()
    request = json.loads(args.request.read_text())
    run_brief = json.loads((args.run_dir / "run_brief.json").read_text())
    manifest = args.run_dir / "manifest/timespan_index.csv"
    nodes = list(csv.DictReader(manifest.open()))
    by_case = {node["label"]: node for node in nodes}
    cases = request["cases"]
    assert len(nodes) == 4 and all(node["level"] == "big" for node in nodes)
    assert set(by_case) == {case["case_id"] for case in cases}
    assert run_brief["member_symbols"] == request["symbols"] == ["rb", "hc", "i"]
    assert (args.run_dir / "delivery/DELIVERY_MANIFEST.json").is_file()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    result_path = args.output_dir / "COMBINED_PAGE.json"
    if result_path.exists():
        previous = json.loads(result_path.read_text())
        assert previous["run_id"] == run_brief["run_id"]
        assert previous["request_sha256"] == digest(args.request)
        assert previous["timespan_index_sha256"] == digest(manifest)
        print(json.dumps(previous, ensure_ascii=False, indent=2))
        return

    from mquant.aidata.profiles import ensure_profile_runtime
    from mquant.aidata.big_world_chart import (
        AidataRunOverviewCAE, _graph_key, _register_run_overview_graph,
    )
    from mquant.frame import TestCAE1, GMap, GMapX, KLine, eval2
    from mquant.tis import ScaleTurnCalendar
    from mquant.uplot import (
        CAEGraph, PlotSet, SpecEntitiesMainFig, KPriceLine,
        DefaultFigTheme, MulFieldsGlyphs,
    )
    from mquant.quant.models.graph import CaeNodeDao

    ensure_profile_runtime()
    # 不让 createUniqueWithFao 的缺类回退创建新的持久化类注册。
    if not CaeNodeDao.is_exits(cls_name="TestCAE1"):
        raise PermissionError("Existing TestCAE1 class registration is required; W03 does not create one")
    overview = CaeNodeDao.fqueryById(node_id=args.overview_node_id)
    assert isinstance(overview, AidataRunOverviewCAE)
    assert overview.P.overview_start == "2021-01-01"
    assert overview.P.overview_end == "2024-02-29"
    assert overview.P.blk == "blk@steel" and overview.P.calendar_name == "night_end_at_2300"
    # AidataRunOverviewCAE 的真实布局由该现有生产函数建立，不是继承的
    # doShowCAEGraph 默认值。仅恢复原对象在进程中的配置，不调用旧 layout
    # 的缓存写盘，不修改 W02 的冻结文件或平台节点。
    key = _graph_key(overview, "run_overview")
    span = (overview.P.overview_start, overview.P.overview_end, "板块有效行情范围")
    _register_run_overview_graph(overview, key, span)
    old_graph = CAEGraph(key)
    old_plotsets = old_graph.P.plotsets.P
    assert list(old_plotsets) == ["main"]
    overview_plotset = old_plotsets["main"]
    overview_fason = overview_plotset.fason
    context = overview.P.context

    input_path = args.repo_root / "professional/case_observation/examples/aidata_inputs.py"
    spec = importlib.util.spec_from_file_location("w03_inputs_for_context_check", input_path)
    inputs = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(inputs)
    case_brief = inputs.make_case_brief(
        args.run_dir.parent, run_brief["run_id"], end_day=request["end_day"],
        timespans=[(*case["manual_request"], case["case_id"]) for case in cases],
    )
    assert context.fason == case_brief["context"].fason, "W02 and W03 Context must be identical"
    turn = ScaleTurnCalendar("mid")
    plotsets = {"overview": overview_plotset}
    mapping = []
    for case in cases:
        node = by_case[case["case_id"]]
        plotset_id = "case_" + case["case_id"].replace("-", "_")
        title = case["case_id"] + " / 30m / mid / " + node["start_ts"] + " → " + node["end_ts"]
        plots = [
            KPriceLine(feat=KLine(freq="30m"), std_method="ratio"),
            MulFieldsGlyphs({
                "feats": GMap({"mid": turn}), "dfkeys": [None],
                "legend_labels": ["贴近转折（M，mid参数）"],
                "glyphs": "diamond", "xfields": ["x"], "yfields": ["y"],
                "timefieldtype": "uti", "size": 20, "alphas": 0.75,
                "dynstd_method": True,
            }),
        ]
        plotsets[plotset_id] = PlotSet({
            "calendar_name": "night_end_at_2300", "blk": "blk@steel",
            "timespans": [(node["start_ts"], node["end_ts"], case["case_id"])],
            "figs": GMapX.from_list([SpecEntitiesMainFig(
                entity_plots=GMap({"syms!blk@steel": GMapX.from_list(plots)}),
                title="!" + title,
            )]),
        })
        mapping.append({"case_id": case["case_id"], "node_id": node["node_id"],
                        "plotset_id": plotset_id, "title": title,
                        "manual_request": case["manual_request"],
                        "actual_frozen_start": node["start_ts"], "actual_frozen_end": node["end_ts"]})
    config = {
        "Context": context, "plotsets": GMap(plotsets), "theme": DefaultFigTheme(),
        "x_label_freq": "1d", "extra_time": 0, "fig_width": 2400,
        "fig_height1": 600, "fig_height": 150, "manual_upd": True,
        "plot_name": run_brief["run_id"] + "：2021起概览和四例30m/mid",
    }
    wrapper = TestCAE1({"name": config})
    graph = wrapper.doShowCAEGraph()
    restored = eval2(wrapper.fason)
    assert list(restored.doShowCAEGraph().P.plotsets.P) == list(plotsets)
    assert overview_plotset.fason == overview_fason
    assert key not in wrapper.fason, "Do not persist a transient named graph dependency"
    (args.output_dir / "combined_native_config.fason.txt").write_text(wrapper.fason)
    created = CaeNodeDao.createUniqueWithFao(tar=wrapper)
    node_id = str(created["node"]["id"])
    host = urlsplit(created["report_url"]).hostname
    result = {
        "run_id": run_brief["run_id"], "node_id": node_id,
        "combined_url": f"http://{host}:5006/cae?node_id={node_id}",
        "trier_node_report_url": created["report_url"],
        "render_entry": "existing native Bokeh /cae?node_id= route",
        "wrapper_class": "TestCAE1", "graph_class": "CAEGraph",
        "plotset_ids": list(graph.P.plotsets.P), "case_mapping": mapping,
        "overview_source_node_id": args.overview_node_id,
        "overview_source_ppid": overview.ppid,
        "overview_plotset_fason_sha256": hashlib.sha256(overview_fason.encode()).hexdigest(),
        "overview_range": [overview.P.overview_start, overview.P.overview_end],
        "same_context_fason_as_formal_case_run": True,
        "turn_feature_ppid": turn.ppid, "turn_specTerm": str(turn.P.specTerm),
        "turn_stMembershipLine": float(turn.P.stMembershipLine),
        "extra_time": 0, "x_label_freq": "1d", "new_class_registration": False,
        "source_code_modified": False, "request_sha256": digest(args.request),
        "timespan_index_sha256": digest(manifest),
        "native_config_sha256": digest(args.output_dir / "combined_native_config.fason.txt"),
        "limits": "平台创建及参数回读；整页实际打开、逐图及图数对应另核。",
    }
    result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
