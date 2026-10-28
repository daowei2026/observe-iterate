"""只读已交CSV，按原bar字段定位本单已签故事的具体视口和锚点。"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

VIEWS = [
    ("C01_before", "CO01-C01", "2021-03-04 09:00", "2021-03-15 15:00", "共同下跌后的恢复；截止主判断，不露16日以后"),
    ("C01_failure", "CO01-C01", "2021-03-09 09:00", "2021-03-22 15:00", "15日后的hc失效及22日重新判断"),
    ("C01_later", "CO01-C01", "2021-03-22 09:00", "2021-03-31 23:00", "i大反弹再失去和hc后段推进同时保留"),
    ("C02_before", "CO01-C02", "2021-08-23 09:00", "2021-09-09 15:00", "两次共同恢复/回落的不同保留；截止判断日盘"),
    ("C02_pullbacks", "CO01-C02", "2021-09-09 15:00", "2021-09-30 23:00", "两轮明显回吐；9日晚不混入判断前"),
    ("C02_local_counter", "CO01-C02", "2021-09-22 21:00", "2021-09-24 23:00", "i首尾接近而途中往返的局部反例"),
    ("C02_october", "CO01-C02", "2021-10-08 09:00", "2021-10-14 23:00", "原倾向寿命的10月反例"),
    ("C03_before", "CO01-C03", "2022-05-05 09:00", "2022-05-23 15:00", "判断前的下跌、较大反向和重新恢复"),
    ("C03_prior_reverse", "CO01-C03", "2022-05-16 09:00", "2022-05-23 15:00", "17—19日共同反向与19—23日恢复"),
    ("C03_again_reverse", "CO01-C03", "2022-05-23 09:00", "2022-05-26 23:00", "23日后仍有明显反向，不裁去失败段"),
    ("C03_extension", "CO01-C03", "2022-05-30 09:00", "2022-06-08 23:00", "31日已越过旧日收盘区域及6月延伸"),
    ("C03_june_failure", "CO01-C03", "2022-06-08 09:00", "2022-06-23 23:00", "6月后段三者下跌及i较大反向"),
    ("C04_old_state", "CO01-C04", "2023-07-10 09:00", "2023-07-28 23:00", "7月hc较强的旧相对状态"),
    ("C04_before", "CO01-C04", "2023-08-10 09:00", "2023-08-21 15:00", "17日恢复、18/21日保持；不露22/23日结果"),
    ("C04_failed_upgrade", "CO01-C04", "2023-08-21 15:00", "2023-08-29 23:00", "22/23推进与24—29日连续守位升级失败"),
    ("C04_september", "CO01-C04", "2023-09-01 09:00", "2023-09-28 23:00", "9月重新恢复和反复；0.09个百分点不作肉眼主证据"),
    ("C04_october", "CO01-C04", "2023-09-28 09:00", "2023-10-11 23:00", "10月失效，保持请求原末界"),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--page-dir", type=Path, required=True)
    args = parser.parse_args()
    root = args.repo_root / "runs/BI-01-CO-01/artifacts/batch-01"
    formal = root / "aidata/delivery/bi01_co01_w03_cases_20261028_5e4fa62eaf"
    file_index = json.loads((formal / "FILE_INDEX.json").read_text())["copied_files"]
    views = []
    for name, case, start, end, purpose in VIEWS:
        node = "big_" + str(int(case[-2:])).zfill(6)
        path = formal / f"feature_slices/{node}/symbol/rb/kline_30m/__default__.csv"
        expected = next(item["sha256"] for item in file_index if item["copy_relative"] == str(path.relative_to(formal)))
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected
        bars = [row for row in csv.DictReader(path.open(newline=""))
                if start + ":00" <= row["closeTs"] <= end + ":00"]
        assert bars
        lower, upper = int(bars[0]["openUti"]), int(bars[-1]["closeUti"]) + 1
        assert lower < upper
        views.append({"id": name, "case_id": case, "plotset_id": "case_" + case.replace("-", "_"),
                      "start": start, "end": end, "x_start": lower, "x_end": upper,
                      "first_bar_openTs": bars[0]["openTs"], "last_bar_closeTs": bars[-1]["closeTs"],
                      "first_bar_openUti_ts": bars[0]["openUti_ts"], "last_bar_closeUti_ts": bars[-1]["closeUti_ts"],
                      "formal_locator": str(path.relative_to(args.repo_root)),
                      "purpose": purpose, "conversion": "仅视口：以该范围已交30m bar的原openUti至末closeUti+1定位；阴影日期另走同Context日历转换。保留closeTs/UTI_ts差异，不外推。"})
    # 正式原行支持关键字段定位；不生成新的行情交付。
    anchors = []
    checks = json.loads((root / "research/R0013_JUDGMENT_CHECKS.json").read_text())
    dates = {str(row[3]) + ":00" for row in checks["comparisons"]} | {str(row[2]) + ":00" for row in checks["comparisons"]}
    dates |= {"2021-03-04 15:00:00", "2021-08-26 15:00:00", "2021-08-30 15:00:00", "2021-09-01 15:00:00",
              "2022-05-05 15:00:00", "2022-05-16 15:00:00", "2022-05-19 15:00:00", "2022-05-20 15:00:00",
              "2022-05-30 15:00:00", "2022-05-31 15:00:00", "2022-06-01 15:00:00",
              "2023-07-26 15:00:00", "2023-08-16 15:00:00", "2023-08-17 15:00:00", "2023-08-18 15:00:00",
              "2023-08-25 15:00:00", "2023-08-28 15:00:00", "2023-08-29 15:00:00", "2023-10-10 15:00:00", "2023-10-11 15:00:00"}
    daily = root / "aidata/delivery/bi01_co01_w02_1d_20261028_c4202eae70"
    for symbol in ["rb", "hc", "i"]:
        path = daily / f"feature_slices/big_000001/symbol/{symbol}/kline_1d/__default__.csv"
        expected = next(item["sha256"] for item in json.loads((daily / "FILE_INDEX.json").read_text())["copied_files"] if item["copy_relative"] == str(path.relative_to(daily)))
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected
        for line, row in enumerate(csv.DictReader(path.open(newline="")), 2):
            if row["closeTs"] in dates:
                anchors.append({"symbol": symbol, "file": str(path.relative_to(args.repo_root)), "csv_line": line,
                                "source_sha256": expected, "raw_row": row})
    result = {"views": views, "daily_anchor_rows": anchors,
              "limits": "视口用于辨认成段路径；精确日收盘另以正式1d原行定位，30m bar的high/low/close不混为一谈。mid实际点不等于确认。"}
    (args.page_dir / "STORY_VIEWPORTS.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"views": len(views), "source_anchor_rows": len(anchors)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
