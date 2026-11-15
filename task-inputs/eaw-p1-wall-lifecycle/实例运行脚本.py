"""EawP1WallLifecycleFrp 默认实例运行脚本。

本文件保留 2026-11-15 实际成功运行脚本的全部执行逻辑，仅补充本说明。
运行上下文已在下方固定：TA_updto20240229_DBA / rb /
night_end_at_2300 / 2020-12-01 至 2021-02-22，特征参数使用默认值。

运行方式：
1. 将本文件放到工作区的 gitignored 目录 .runtime/parameter-inspection/。
2. 在 /dwdhome/fy/BASE_E6_2 工作区根目录执行：
   ./run-python.sh -u .runtime/parameter-inspection/实例运行脚本.py
   run-python.sh 会加载该工作区的 m3rc 及现有运行环境修正。
3. 查看脚本同目录的 EawP1WallLifecycleFrp.run-result.json。
   成功条件为 run_succeeded=true 且 readback_succeeded=true；
   本脚本捕获异常写入报告，不以进程退出码单独判断成功。

该实例须命中已有 fields.json；未命中时停止，避免该长窗口自动补算。
结果通过正式 .run() / .F / ADT schema 读取，并记录三路计数和样例。
运行环境须已生成并导出三路 Wall 输出所需的 Python ADT schema。
"""

import inspect
import json
import signal
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path


started = time.monotonic()
output_dir = Path(__file__).resolve().parent
report = {
    "started_at_utc": datetime.now(timezone.utc).isoformat(),
    "workspace": str(Path.cwd()),
    "expression": "EawP1WallLifecycleFrp().run()",
    "context": {
        "sof_name": "TA_updto20240229_DBA",
        "startDay": "2020-12-01",
        "endDay": "2021-02-22",
        "symbol": "rb",
        "calendar": "night_end_at_2300",
    },
    "run_attempted": False,
    "run_succeeded": False,
}


def timeout_handler(signum, frame):
    raise TimeoutError("本次实例取数超过 180 秒")


signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(180)
try:
    from mquant.tis.frp.EawBattleP import EawP1WallLifecycleFrp
    from mquant.quant import OptContext
    from mquant.frame import CurrCalendar
    from m3tt import CurrTradeSet, CurrSymbol

    config = report["context"]
    context = OptContext({key: config[key] for key in ("sof_name", "startDay", "endDay")})
    with CurrTradeSet(context.sof), CurrSymbol(config["symbol"]), CurrCalendar(config["calendar"]):
        feature = EawP1WallLifecycleFrp()
        report.update({
            "class_file": inspect.getfile(EawP1WallLifecycleFrp),
            "ppdict": feature.ppdict,
            "ppid": feature.ppid,
            "full_dir": feature.full_dir,
            "gfull_dir": feature.gfull_dir,
            "default_cal_type": str(feature.hold_cal_type()),
        })
        fields_path = Path(feature.full_dir) / "fields.json"
        report["stored_fields_exist"] = fields_path.is_file()
        if not fields_path.is_file():
            raise FileNotFoundError("默认实例未命中已存产物；停止该长窗口的自动补算")
        report["stored_fields"] = json.loads(fields_path.read_text(encoding="utf-8"))
        print("BOUND_CONTEXT:", json.dumps(config, ensure_ascii=False), flush=True)
        print("FULL_DIR:", feature.full_dir, flush=True)
        print("CALLING: EawP1WallLifecycleFrp().run()", flush=True)
        report["run_attempted"] = True
        result = feature.run()
        report["run_succeeded"] = True
        report["return_type"] = type(result).__name__
        report["result_keys"] = list(result.F.keys())
        report["result_types"] = {key: type(value).__name__ for key, value in result.F.items()}
        report["streams"] = {}

        def json_value(value):
            if hasattr(value, "_asdict"):
                return {key: json_value(item) for key, item in value._asdict().items()}
            if isinstance(value, (tuple, list)):
                return [json_value(item) for item in value]
            if hasattr(value, "item"):
                return value.item()
            return value

        import numpy as np
        for name, event in result.F.items():
            timestamps = event.ts
            sequence = event.value.root_seq
            if sequence.count() != len(timestamps):
                raise ValueError(f"{name}: 时间轴与 ADT 事件数不一致")
            pointers = sequence.mul.ndarray
            anchors = sequence.mul_seq.__anchor__.ndarray
            ends = anchors[pointers]
            starts = np.where(pointers > 0, anchors[np.maximum(pointers - 1, 0)], 0)
            lengths = ends - starts
            nonempty = np.flatnonzero(lengths > 0)
            positions = np.unique(np.linspace(0, len(nonempty) - 1, min(3, len(nonempty)), dtype=int)) if len(nonempty) else []
            samples = [
                {"event_time": str(timestamps[int(nonempty[position])]),
                 "decoded": json_value(sequence.load(int(nonempty[position])))}
                for position in positions
            ]
            report["streams"][name] = {
                "schema_type": type(sequence).__name__,
                "event_count": len(timestamps),
                "business_rows": int(lengths.sum()),
                "time_range": [str(timestamps[int(nonempty[0])]), str(timestamps[int(nonempty[-1])])] if len(nonempty) else None,
                "samples": samples,
            }
        report["readback_succeeded"] = True
except Exception as error:
    report["traceback"] = traceback.format_exc()
    chain = []
    seen = set()
    while error is not None and id(error) not in seen:
        seen.add(id(error))
        chain.append({"type": type(error).__name__, "message": str(error)})
        error = error.__cause__ or error.__context__
    report["error_chain"] = chain
finally:
    signal.alarm(0)
    report["elapsed_seconds"] = round(time.monotonic() - started, 3)
    output_path = output_dir / "EawP1WallLifecycleFrp.run-result.json"
    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key not in ("ppdict", "traceback")}, ensure_ascii=False, indent=2, default=str))
    print("REPORT:", output_path)
