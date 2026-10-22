"""Reproduce bounded R0007 arithmetic and configuration self-checks.

Run: python verify_r0007.py
No network, Feature computation, platform imports or charts. Source excerpts are
explicitly recorded below; this is not the Worker's 72/112-check rerun.
"""
from __future__ import annotations
import json
from pathlib import Path
from statistics import median
from math import isclose
from u2_normal_node_behavior import CONFIG_VERSION, configs, display_config

ROOT = Path(__file__).resolve().parent
SOURCE = "daowei2026/observe-iterate@d7410c70f7f43388946e3c9b7721202be53a24f9:runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-AIDATA-01/"
INPUTS = {
    "source": SOURCE,
    "raw_price_file": "data/rb_price_100460400_103315800/rb_5m_price_calendar.csv",
    "raw_price_blob": "9d899cf389288e54973e1d15178fa90669c46c6c",
    "close_lines_inclusive": [4307, 4333],
    "close": [3735,3737,3736,3739,3743,3746,3746,3747,3751,3752,3746,3758,3757,3771,3780,3783,3776,3788,3803,3806,3808,3810,3817,3829,3834,3830,3834],
    "last_member": {"start":103043400,"end":103059000,"confirmation":103151400,"direction":0},
    "recent_members_source": "data/rb_asof_103315800/recent_members.csv",
    "recent_pairs": [[101860200,102297600],[102297600,102540600],[102540600,102837600],[102837600,102958200],[102958200,103043400],[103043400,103059000]],
    "previous_members_source": "data/rb_asof_103315800/previous_members.csv",
    "previous_pairs": [[100460400,100633800],[100633800,100723200],[100723200,101074800],[101074800,101174400],[101174400,101470800],[101470800,101860200]],
    "official_metrics_source": "data/rb_asof_103315800/metrics.csv",
    "official_duration": {"current":181800.0,"previous":234900.0,"change":-53100.0,"dispersion":105900.0,"loo_maximum":61200.0,"loo_ties":63},
    "official_efficiency": {"current":0.1514170159139533,"previous":0.08454319929996491,"change":0.06687381661398838},
    "official_amplitude_current":138.5,"official_path_current":750.5,
    "endpoint_checks": [
        {"name":"previous1", "raw_lines":[2,291], "start":3953,"end":4034,"direction":"down"},
        {"name":"recent_window", "raw_lines":[2335,4333], "start":4057,"end":3834},
        {"name":"working", "raw_lines":[4333,4761], "start":3834,"end":3784,"direction":"down"}
    ],
    "official_working": {"progress":50.0,"efficiency":0.0377643504531722,"counter":80.0},
    "official_working_sources": ["data/rb_asof_103315800/working_progress.csv","data/rb_asof_103315800/working_efficiency.csv","data/rb_asof_103315800/working_counter.csv"],
    "as_of":103315800,
    "ohlc_last_member_range": {"max_high":3841,"min_low":3733,"source_lines_inclusive":[4307,4333]},
}


def main() -> None:
    checks = []
    def check(name, observed, expected):
        ok = isclose(observed, expected, rel_tol=1e-12, abs_tol=1e-12) if isinstance(expected, (int,float)) and not isinstance(expected,bool) else observed == expected
        checks.append({"name":name,"observed":observed,"expected":expected,"passed":bool(ok)})
    c = INPUTS["close"]
    length = sum(abs(b-a) for a,b in zip(c,c[1:]))
    peak = c[0]
    adverse = 0
    for price in c:
        peak = max(peak,price)
        adverse = max(adverse,peak-price)
    r = [b-a for a,b in INPUTS["recent_pairs"]]
    p = [b-a for a,b in INPUTS["previous_pairs"]]
    loo = [abs(median(r[:i]+r[i+1:])-median(r)) for i in range(6)]
    check("raw_close_count",len(c),27)
    check("endpoint_amplitude_reference",abs(c[-1]-c[0]),99)
    check("close_path_reference",length,137)
    check("efficiency_reference",abs(c[-1]-c[0])/length,99/137)
    check("counter_reference_up",adverse,7)
    check("ohlc_range_is_not_endpoint_amplitude",3841-3733,108)
    official=INPUTS["official_duration"]
    check("duration_current_vs_formal",median(r),official["current"])
    check("duration_previous_vs_formal",median(p),official["previous"])
    check("duration_change_vs_formal",median(r)-median(p),official["change"])
    check("duration_MAD_vs_formal",median([abs(x-median(r)) for x in r]),official["dispersion"])
    check("duration_LOO_max_vs_formal",max(loo),official["loo_maximum"])
    check("duration_LOO_all_six_equal",len(set(loo))==1,True)
    check("previous1_signed_progress",3953-4034,-81)
    check("recent_window_net_change",3834-4057,-223)
    check("working_endpoint_vs_formal_progress",3834-3784,INPUTS["official_working"]["progress"])
    check("formal_efficiency_change",INPUTS["official_efficiency"]["current"]-INPUTS["official_efficiency"]["previous"],INPUTS["official_efficiency"]["change"])
    check("median_ratio_not_median_efficiency",not isclose(138.5/750.5,INPUTS["official_efficiency"]["current"]),True)
    all_configs=configs()
    check("unique_view_ids",len({x["view_id"] for x in all_configs}),len(all_configs))
    check("only_inspected_geometry_kinds",all(x["plot_binding"]["kind"] in {"point","line","segment"} for x in all_configs),True)
    check("display_views_not_claimed_formal_tables",all(x["df_key"].startswith("n_display/") for x in all_configs),True)
    # Colors here are only controlled test values, not a prescribed market palette.
    evo=display_config(symbol="rb",color="steelblue",optional_panels=("duration","rhythm"))
    cut=display_config(symbol="rb",color="steelblue",mode="selected_cut")
    check("one_symbol_one_color",{x["plot_binding"]["style"]["color"] for x in evo["layers"]}=={"steelblue"},True)
    check("no_price_standardization_on_panes",all(v["price_normalization"] is False for v in evo["panels"].values()),True)
    check("cut_not_static_snapshot_as_time_history",all(not x["view_id"].endswith(("_hold","_steps")) for x in cut["layers"]),True)
    check("evolution_not_final_members_backfill",all(not x["view_id"].startswith("selected_") for x in evo["layers"]),True)
    check("waiting_ratio_not_clipped",evo["panels"]["rhythm"]["clip_to_probability"],False)
    check("mutation_does_not_leak",configs()[0]["plot_binding"]["style"].get("color") is None,True)
    check("intervals_use_overlap",all(x["time_binding"].get("interval_policy")=="overlap" for x in all_configs if x["plot_binding"]["kind"]=="segment"),True)
    rejected = False
    try:
        display_config(symbol="rb",color="steelblue",mode="live")
    except ValueError:
        rejected=True
    check("unimplemented_live_mode_rejected",rejected,True)
    result = {
        "invocation_id":"BI01-FO-01-R0007-20261022T081903Z-a9efdb6a",
        "scope":"Local reference arithmetic and pure configuration self-checks only; not TIS/FRP/aidata/uplot runtime or pixel validation.",
        "inputs":INPUTS,"config_version":CONFIG_VERSION,
        "derived": {"recent_durations":r,"previous_durations":p,"duration_loo_shifts":loo,
                    "recent_span":sum(r),"previous_span":sum(p),
                    "last_member_confirmation_lag":103151400-103059000,
                    "lag_over_last_member_duration":(103151400-103059000)/(103059000-103043400),
                    "working_age":103315800-103059000,
                    "working_age_over_recent_duration_median":(103315800-103059000)/median(r),
                    "ratio_of_medians_not_formal_efficiency":138.5/750.5},
        "checks":checks,"passed":all(x["passed"] for x in checks),
        "not_executed":["full 4760-row independent recalculation","new formal temporal reads","normal native Feature integration","aidata registry/panel wiring","new graph render","professional pixel inspection","independent review"]
    }
    (ROOT/"CHECK_RESULTS.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":result["passed"],"checks":len(checks),"failed":[x for x in checks if not x["passed"]]},ensure_ascii=False))
    if not result["passed"]:
        raise SystemExit(1)

if __name__=="__main__":
    main()
