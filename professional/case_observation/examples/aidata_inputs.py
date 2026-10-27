"""本批 aidata 入参示例：2021 起点、30m 图上的 mid 贴近转折。

由 Owner 提供的 probe.py 定向整理；不是新的行情入口或已现场跑过的结果。
只构造现有 aidata 接受的 brief/Feature 描述，不取数、不保存图、不自动执行。
实际调用顺序见 ../03_AIDATA_USE.md；单页组合须复用现场补充脚本。
"""
from pathlib import Path
from typing import Any, Sequence

from mquant.aidata.api import make_point_anchor
from mquant.frame import KLine
from mquant.quant import OptContext
from mquant.tis import ScaleTurnCalendar

OBSERVATION_START = "2021-01-01"
TURN_PARAMETER = "mid"
TimeSpan = tuple[str, str, str]


def kline_evidence(freq: str) -> Any:
    """big 是切片节点层级，不是 KLine 频率；正式时间字段沿用 closeUti。"""
    if freq not in {"1d", "30m"}:
        raise ValueError("本示例仅配置 1d 和 30m KLine")
    return make_point_anchor(
        KLine(freq=freq),
        uti_fields="closeUti",
        label=f"{freq} KLine正式行情数据",
        feature_key=f"kline_{freq}",
        slice_levels=["big"],
        evidence_role="market_context_sidecar",
        is_raw_market_data=True,
    )


def mid_turn_evidence() -> Any:
    """mid 是特征参数；仍在 big/30m 页面显示，不生成 mid 子节点。"""
    return make_point_anchor(
        ScaleTurnCalendar(TURN_PARAMETER),
        uti_fields="x",
        label="30m图上的贴近转折（mid）",
        feature_key="scale_turn_mid",
        slice_levels=["big"],
        plot_binding={
            "kind": "point",
            "x_field": "x",
            "y_field": "y",
            "label": "贴近转折（mid）",
            "surfaces": ["big"],
            # 沿用测试的显示样式，不是业务阈值；颜色留给品种区分。
            "style": {"marker": "diamond", "size": 20},
        },
    )


def _make_brief(
    output_root: str | Path,
    run_id: str,
    end_day: str,
    timespans: Sequence[TimeSpan],
    evidence_features: list[Any],
) -> dict[str, Any]:
    if not run_id or not str(output_root) or not end_day:
        raise ValueError("必须提供本次 output_root、唯一 run_id 和实际 end_day")
    if not timespans:
        raise ValueError("必须提供实际时间窗，不能沿用原 probe 的测试用例")
    for span in timespans:
        if len(span) != 3 or any(not isinstance(value, str) or not value for value in span):
            raise ValueError("每个窗口须为 (开始时间, 结束时间, 用例标签) 三个非空字符串")
    return {
        "output_root": str(output_root),
        "run_id": run_id,
        "run_note": "多品种差异研究：aidata正式图数输入",
        "context": OptContext({
            "sof_name": "TA_updto20240229_DBA",
            "stk_tlist": "tick_test_all57_takeout_lcNsiNcy",
            "startDay": OBSERVATION_START,
            # 按实际输入传递；不把日期字符串解释为包含该日全天。
            "endDay": end_day,
        }),
        "blk": "blk@steel",
        "calendar_override": "night_end_at_2300",
        "extract_time_syms": "blk@steel",
        "generation_depth": "big",
        "big_source": {"mode": "manual", "timespans": list(timespans)},
        "evidence_features": evidence_features,
    }


def make_overview_brief(
    output_root: str | Path, run_id: str, *, end_day: str
) -> dict[str, Any]:
    """方式一：2021 起的完整研究范围，只有 1d evidence。"""
    return _make_brief(
        output_root, run_id, end_day,
        [(OBSERVATION_START, end_day, "full_history")],
        [kline_evidence("1d")],
    )


def make_case_brief(
    output_root: str | Path,
    run_id: str,
    *,
    end_day: str,
    timespans: Sequence[TimeSpan],
) -> dict[str, Any]:
    """方式二：调用方传入实际选例窗口；这里的 1d 切片仅覆盖这些窗口。"""
    return _make_brief(
        output_root, run_id, end_day, timespans,
        [kline_evidence("1d"), kline_evidence("30m"), mid_turn_evidence()],
    )
