"""U2 F/Q/V（rb/hc/i）现有正式实例的独立 Python 取材脚本。

依据：
  daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:
    frp/fqv_kline_example.py
  daowei2026/feature-refinement-implementation-agent-evolution:
    agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/
    configurations/fqv-kline-rb-hc-i.json

正常调用方式与上游实例构造均来自已有 TIS。此脚本不重新实现任何 F/Q/V 方法。

在安装了相应 mquant/tis/frp 的正式环境执行（运行命令因本机环境而异）：
  python 实例运行脚本.py --mode inspect
  python 实例运行脚本.py --mode read
  python 实例运行脚本.py --mode read --with-details

默认 read **只读取既存正式输出**，不调用 .rerun(2)。如果已有结果未落在当前
实例所选真实目录，直接停止，不会为填满结果而暗中重算。

仅在获准进行整个历史区间的真实重新生产时，显式执行：
  python 实例运行脚本.py --mode rerun --allow-full-period-rerun

本批 SOF 未选择 startDay/endDay，原输入约 2013–2024 年、每品种 172194 根5mK线。
重算可能耗时、占用资源或写正式产品；本脚本没有对任何机器执行过重算。

读到的 CSV / JSON 放在当前目录 .runtime/fqv-rb-hc-i，或 --output-dir 指定的位置。
使用 --mode rerun 后另起一个全新 Python 进程执行 --mode read，才能核实
跨进程公开读取；即使成功也不自动代表业务 C2 或设计合理性验收。
"""

from __future__ import annotations

import argparse
import inspect
import json
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path


SOF = "TA_updto20240229_DBA"
BLOCK = "steel"
CALENDAR = "night_end_at_2300"
PARAMS = {
    "freq": "5m",
    "symbols": ("rb", "hc", "i"),
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
DETAILS = {
    "F": ["occurrences_groupMembers"],
    "Q": ["occurrences_organizationMembers"],
    "V": ["occurrences_validityMembers", "occurrences_validityReasons"],
}


def summarize_frame(frame, csv_path):
    """只序列化正式公开 DataFrame；不重算业务量测。"""
    frame.to_csv(csv_path, index=True)
    return {
        "rows": int(len(frame)),
        "columns": list(map(str, frame.columns)),
        "csv": str(csv_path),
    }


def cli():
    p = argparse.ArgumentParser(description="U2 F/Q/V 真实实例：检查、读取或显式重跑")
    p.add_argument("--mode", choices=("inspect", "read", "rerun"), default="read")
    p.add_argument("--with-details", action="store_true", help="同时读取成员与V原因的常用正式子表")
    p.add_argument("--allow-full-period-rerun", action="store_true",
                   help="显式授权对既定整段历史执行三个 FAO 的 rerun(2)")
    p.add_argument("--output-dir", type=Path, default=Path(".runtime/fqv-rb-hc-i"))
    args = p.parse_args()
    if args.mode == "rerun" and not args.allow_full_period_rerun:
        p.error("rerun 将运行既定全期行情；须显式提供 --allow-full-period-rerun")
    return args


def main():
    args = cli()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    report = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "mode": args.mode,
        "scope": {"sof_name": SOF, "stk_tlist": BLOCK, "calendar": CALENDAR},
        "python_parameters": {**PARAMS, "symbols": list(PARAMS["symbols"])},
        "source_tis_commit": "2f460d663d821cf2ba25555eda13e78b697d0767",
        "source_frp_commit": "67711c492da909ed0f044f357beb278abf7fc71c",
        "outputs": {},
        "completed": False,
        "same_process_public_read": False,
        "separate_process_readback_verified": False,
    }
    output_path = args.output_dir / f"fqv-{args.mode}-result.json"
    try:
        from mquant.frame import CurrSof, CurrCalendar
        from mquant.tis.frp.fqv_kline_example import make_features

        with CurrSof(sof_name=SOF, stk_tlist=BLOCK), CurrCalendar(CALENDAR):
            f, q, v = make_features(**PARAMS)
            features = (("F", f), ("Q", q), ("V", v))
            for name, feature in features:
                item = {"class": type(feature).__name__}
                item["class_file"] = inspect.getfile(type(feature))
                item["full_dir"] = str(feature.full_dir)
                fields_file = Path(feature.full_dir) / "fields.json"
                item["stored_fields_exist_before"] = fields_file.is_file()
                report["outputs"][name] = item

            if args.mode != "inspect":
                for name, feature in features:
                    item = report["outputs"][name]
                    if args.mode == "read" and not item["stored_fields_exist_before"]:
                        raise FileNotFoundError(
                            f"{name}: 当前准确实例未找到 fields.json；禁止自动重算补齐"
                        )
                    target = feature
                    if args.mode == "rerun":
                        # 按TIS原示例直接使用 rerun(2) 返回对象读取，不另造 Source Runner。
                        target = feature.rerun(2)
                        item["rerun_completed"] = True
                    item["tables"] = {}
                    primary = target.to_df()
                    item["tables"]["occurrences"] = summarize_frame(
                        primary, args.output_dir / f"{name}_occurrences.csv"
                    )
                    if args.with_details:
                        for product in DETAILS[name]:
                            detail = target.to_dfs([product])[product]
                            item["tables"][product] = summarize_frame(
                                detail, args.output_dir / f"{name}_{product}.csv"
                            )
                    item["public_read_completed"] = True
                report["same_process_public_read"] = True
            report["completed"] = True
    except Exception as exc:
        report["error_type"] = type(exc).__name__
        report["error"] = str(exc)
        report["traceback"] = traceback.format_exc()
    finally:
        output_path.write_text(
            json.dumps(report, ensure_ascii=False, indent=2, default=str) + "\n",
            encoding="utf-8",
        )
        print(json.dumps(
            {k: v for k, v in report.items() if k != "traceback"},
            ensure_ascii=False, indent=2, default=str,
        ))
        print("REPORT:", output_path)
    return 0 if report["completed"] else 1


if __name__ == "__main__":
    sys.exit(main())
