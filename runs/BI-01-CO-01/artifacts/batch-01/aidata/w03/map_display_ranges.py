"""通过现有自然日历定位浏览器轴范围；无日历索引的边距明确保留未知。"""
import argparse
import importlib.util
import json
import math
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    import pandas as pd
    from mquant.aidata.profiles import ensure_profile_runtime

    source = args.repo_root / "professional/case_observation/examples/aidata_inputs.py"
    spec = importlib.util.spec_from_file_location("w03_mapping_inputs", source)
    inputs = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(inputs)
    ensure_profile_runtime()
    aidata = args.repo_root / "runs/BI-01-CO-01/artifacts/batch-01/aidata"
    request = json.loads((aidata / "W03_CASE_INPUTS.json").read_text())
    # 仅构造同一Context并读其日历，不调用Feature/core/取数或写此路径。
    context = inputs.make_case_brief(
        args.output_dir, "w03_display_mapping_only", end_day=request["end_day"],
        timespans=[(*case["manual_request"], case["case_id"]) for case in request["cases"]],
    )["context"]
    calendar = context.sof.tsa_of("night_end_at_2300")["natural_tsa"]
    capture = json.loads((args.output_dir / "BROWSER_REVIEW.json").read_text())
    ranges = []
    for figure in capture["figures"]:
        row = {"title": figure["title"], "raw_browser_x_range": figure["x_range"]}
        for key, value in figure["x_range"].items():
            lower, upper = math.floor(value), math.ceil(value)
            available = 0 <= lower <= upper < len(calendar)
            row[key + "_natural_tsa_bracket"] = (
                [str(pd.to_datetime(calendar[lower])), str(pd.to_datetime(calendar[upper]))]
                if available else None
            )
            row[key + "_outside_available_calendar"] = not available
        ranges.append(row)
    result = {
        "mapping_source": "same OptContext.sof.tsa_of(night_end_at_2300)[natural_tsa] at floor/ceil of fractional browser UTI; no epoch/unit guess",
        "calendar_size": len(calendar),
        "available_calendar_first_last": [str(pd.to_datetime(calendar[0])), str(pd.to_datetime(calendar[-1]))],
        "ranges": ranges,
        "limit": "Bokeh轴边距不扩充正式覆盖；超出已有日历的轴端点仅保留原UTI，未外推时间。无时区转换。",
    }
    (args.output_dir / "DISPLAY_RANGES.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"mapped_figures": len(ranges), "unmapped_margin_endpoints": sum(row[key + "_outside_available_calendar"] for row in ranges for key in ["start", "end"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
