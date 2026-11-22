"""DIAGNOSTIC_ONLY：读取失败附近三天输入，核对边界与现有候选过滤。"""
import ast
import hashlib
import json
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent
TARGET = OUT / "m-input-diagnostic-20210310-20210312"
TARGET.mkdir(exist_ok=False)
import mquant
assert "mquant.tis" not in sys.modules
mquant.__path__.insert(0, str(OUT / "python/mquant"))
import numpy as np
import pandas as pd
from m3tt import CurrTradeSet, CurrSymbol
from mquant.quant import OptContext
from mquant.frame import CurrCalendar
from mquant.tis.t0.gen.cc import SubContinuousContract
from mquant.tis.hf.mc import trading_days
from mquant.tis.hf.prel0.tick_quote_context import TickQuoteContextWrapperSupport
from mquant.tis.hf.prel0.p1_product_receipt import source_scope

config = dict(sof_name="TA_updto20240229_DBA", stk_tlist="tick_test_all57_takeout_lcNsiNcy",
              startDay="2021-03-10", endDay="2021-03-12")
context = OptContext(config)
report = dict(mode="DIAGNOSTIC_ONLY", formal_scope_unchanged=True, diagnostic_context=config,
              symbol="m", calendar="night_end_at_2300", formal_feature_called=False)
with CurrTradeSet(context.sof), CurrSymbol("m"), CurrCalendar("night_end_at_2300"):
    upstream = SubContinuousContract()
    assert str(upstream.prop_cal_type) == "CalType.Cal"
    frame = upstream.rerun().F.value
    sof = CurrTradeSet.sof(True)
    frame = frame[sof.startDay:sof.endDay]
    assert frame.index.min() >= pd.Timestamp("2021-03-10")
    assert frame.index.max() < pd.Timestamp("2021-03-13")
    columns = ["price", "buy_price1", "buy_vol1", "sell_price1", "sell_vol1"]
    required = columns + ["linear_ts"]
    before = hashlib.sha256(pd.util.hash_pandas_object(frame[required], index=True).values.tobytes()).hexdigest()
    durations = [duration for _day, _contract, duration in trading_days()]
    covered = np.zeros(len(frame), dtype=bool)
    for duration in durations:
        covered[frame.index.searchsorted(pd.Timestamp(duration.start), side="left"):
                frame.index.searchsorted(pd.Timestamp(duration.stop), side="right")] = True
    empty = frame[columns].isna().all(axis=1)
    report.update(raw_rows=len(frame), first_time=str(frame.index.min()), last_time=str(frame.index.max()),
                  all_empty_quote_rows=int(empty.sum()), uncovered_rows=int((~covered).sum()),
                  uncovered_all_empty=bool(empty.to_numpy()[~covered].all()), input_value_hash=before)
    frame.loc[empty, required].to_csv(TARGET / "all-empty-rows.csv", index_label="timestamp")
    frame.loc[~covered, required].to_csv(TARGET / "uncovered-rows.csv", index_label="timestamp")
    support = TickQuoteContextWrapperSupport()
    try:
        support._trading_day_chunk_plan(frame)
        report["locked_plan"] = "PASS"
    except ValueError as error:
        report["locked_plan"] = dict(status="FAILED", error=str(error))

    # 仅抽取既有候选函数用于反事实诊断，不导入/采用原工作树的 Feature 类。
    source_path = Path("/dwdhome/fy/BASE_E6_2/mquant/tis/hf/prel0/wall_assembler.py")
    source = source_path.read_text()
    function = next(node for node in ast.parse(source).body
                    if isinstance(node, ast.FunctionDef) and node.name == "_exclude_empty_calendar_padding")
    fragment = ast.get_source_segment(source, function)
    (TARGET / "candidate-filter-fragment.py").write_text(fragment + "\n")
    namespace = dict(np=np, pd=pd, source_scope=source_scope, CurrSymbol=CurrSymbol, CurrCalendar=CurrCalendar)
    exec(compile(fragment, "DIAGNOSTIC_ONLY_existing_padding_candidate", "exec"), namespace)
    selected = namespace[function.name](frame, durations)
    assert selected.index.is_unique
    for column in required:
        pd.testing.assert_series_equal(frame.loc[selected.index, column], selected[column], check_exact=True)
    after = hashlib.sha256(pd.util.hash_pandas_object(frame[required], index=True).values.tobytes()).hexdigest()
    assert before == after
    report["candidate_counterfactual"] = dict(status="DIAGNOSTIC_ONLY", selected_rows=len(selected),
                                             excluded_rows=len(frame)-len(selected), retained_values_exact=True,
                                             original_frame_unchanged=True,
                                             candidate_function_sha256=hashlib.sha256(fragment.encode()).hexdigest(),
                                             original_working_file_sha256=hashlib.sha256(source_path.read_bytes()).hexdigest())
    try:
        plan = support._trading_day_chunk_plan(selected)
        report["candidate_counterfactual"]["chunk_plan"] = dict(status="PASS", chunks=len(plan))
    except ValueError as error:
        report["candidate_counterfactual"]["chunk_plan"] = dict(status="FAILED", error=str(error))
    report["evidence_scope_limit"] = "仅证明当前三天诊断窗的边界与候选性质；不是全年17行已重验，也不是正式过滤已获授权或生产成功。"
(TARGET / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)
