from datetime import datetime
from pathlib import Path

from mquant.aidata.api import (
    build_chart_run,
    build_board_run,
    build_run_overview_chart_page,
    build_big_world_chart_pages,
    make_point_anchor,
)
from mquant.aidata.profiles import ensure_profile_runtime
from mquant.frame import KLine
from mquant.quant import OptContext
from mquant.tis import ScaleTurnCalendar

ROOT = Path(
    "/dwdhome/fy/BASE_E6_2/mquant/aidata/"
    "test_runs/fy_owner_1d_30m_20261027"
)
ROOT.mkdir(parents=True, exist_ok=True)

ensure_profile_runtime()

context = OptContext({
    "sof_name": "TA_updto20240229_DBA",
    "stk_tlist": "tick_test_all57_takeout_lcNsiNcy",
    "startDay": "2013-02-19",
    "endDay": "2024-02-29",
})

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")


def kline_evidence(freq):
    return make_point_anchor(
        KLine(freq=freq),
        uti_fields="closeUti",
        label=f"{freq} KLine正式行情数据",
        feature_key=f"test_kline_{freq}",
        slice_levels=["big"],
        evidence_role="market_context_sidecar",
        is_raw_market_data=True,
    )


def make_brief(run_id, timespans, evidence_features):
    return {
        "output_root": str(ROOT),
        "run_id": run_id,
        "run_note": "Owner aidata 1d/30m 双任务接口验证",
        "context": context,
        "blk": "blk@steel",
        "calendar_override": "night_end_at_2300",
        "extract_time_syms": "blk@steel",
        "generation_depth": "big",
        "big_source": {
            "mode": "manual",
            "timespans": timespans,
        },
        "evidence_features": evidence_features,
    }


# 测试1：完整1d图与数据
brief1 = make_brief(
    f"fy_test_1d_{stamp}",
    [("2013-02-19", "2024-02-29", "full_history")],
    [kline_evidence("1d")],
)

run1 = build_chart_run(brief1, dry_run=False)

page1 = build_run_overview_chart_page(
    run1,
    run_brief_input=brief1,
    save=True,
)

board1 = build_board_run(
    {**brief1, "run_id": run1.run_id},
    reuse_core=True,
    dry_run=False,
)

print("TEST1_RUN_ID:", run1.run_id)
print("TEST1_OVERVIEW:", page1.to_dict("records"))
print("TEST1_STATS:", board1.feature_slice_stats_path)
print("TEST1_DELIVERY:", board1.delivery_manifest_path)


# 测试2：1d概览 + 30m图 + 贴近转折
turn_evidence = make_point_anchor(
    ScaleTurnCalendar("large"),
    uti_fields="x",
    label="30m大尺度贴近转折",
    feature_key="test_scale_turn_large",
    slice_levels=["big"],
    plot_binding={
        "kind": "point",
        "x_field": "x",
        "y_field": "y",
        "label": "大尺度贴近转折（L）",
        "surfaces": ["big"],
        "style": {
            "marker": "diamond",
            "size": 20,
        },
    },
)

brief2 = make_brief(
    f"fy_test_1d_30m_{stamp}",
    [
        ("2021-08-15", "2021-09-30", "TEST-C001"),
        ("2021-11-01", "2021-12-15", "TEST-C002"),
        ("2022-03-01", "2022-04-15", "TEST-C003"),
    ],
    [
        kline_evidence("1d"),
        kline_evidence("30m"),
        turn_evidence,
    ],
)

run2 = build_chart_run(brief2, dry_run=False)

pages2 = build_big_world_chart_pages(
    run2,
    run_brief_input=brief2,
    save=True,
)

board2 = build_board_run(
    {**brief2, "run_id": run2.run_id},
    reuse_core=True,
    dry_run=False,
)

print("TEST2_RUN_ID:", run2.run_id)
print("TEST2_PAGES:", pages2.to_dict("records"))
print("TEST2_STATS:", board2.feature_slice_stats_path)
print("TEST2_DELIVERY:", board2.delivery_manifest_path)
