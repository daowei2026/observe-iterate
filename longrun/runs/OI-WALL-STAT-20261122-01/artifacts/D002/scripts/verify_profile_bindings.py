"""核对D1的旧身份豁免及receipt完整参数，避免用宽泛豁免掩盖冲突。"""
import hashlib
import json
from pathlib import Path
import numpy as np
import pandas as pd

OUT=Path(__file__).resolve().parent
preflight=json.loads((OUT/"preflight.json").read_text())
root=OUT/"profile"
checks=json.loads((root/"STATISTICS_SELF_CHECK.json").read_text())
for item in checks["checks"]:
    symbol=item["symbol"];directory=OUT/"results"/symbol
    events=pd.read_parquet(directory/"wall_events.parquet")
    trace=pd.read_parquet(directory/"tables/wall_assembler_state_trace.parquet",columns=["uti","wall_id_bid","wall_id_ask"])
    exempt_count=0
    for side,name in [(1,"bid"),(2,"ask")]:
        group=events.loc[events.side_code.eq(side)]
        final_ids=trace.reindex(group.index)["wall_id_"+name].to_numpy()
        other=group.loc[group.wall_id.to_numpy()!=final_ids]
        assert other.event_type_code.eq(7).all() and other.reason_code.eq(5).all()
        new_starts=group.loc[group.event_type_code.eq(4)]
        for timestamp,old_end in other.iterrows():
            actual_final_id=int(trace.loc[timestamp,"wall_id_"+name])
            assert ((new_starts.index==timestamp)&new_starts.wall_id.eq(actual_final_id)).any()
        exempt_count+=len(other)
    receipt=json.loads((directory/"receipt.json").read_text())
    defaults=preflight["symbols"][symbol]["ppdict"]
    expected_private={key:defaults[key] for key in ["qt_freq","qt_n","qt_quantile","large_quote_ratio_min",
        "allow_zero_qt_fallback","w_depth_ref_ticks","thick_vs_hi_ratio","thin_vs_mid_ratio","allow_thin_brick"]}
    expected_private["eps_vol"]=1e-12
    assert receipt["producer_private_parameters"]==expected_private
    assert receipt["actual_business_parameters"]==preflight["symbols"][symbol]["effective_wall_parameters"]
    item.update(non_final_identity_events_are_exact_relocation_ends=True,relocation_old_end_count=exempt_count,
                receipt_effective_and_private_parameters_match=True,
                declared_parameter_sha256=hashlib.sha256(json.dumps(defaults,sort_keys=True,separators=(",",":")).encode()).hexdigest())
(root/"STATISTICS_SELF_CHECK.json").write_text(json.dumps(checks,ensure_ascii=False,indent=2)+"\n")
print("D1豁免均为同拍新Start可追溯的旧身份relocation End；receipt参数完整匹配。",flush=True)
