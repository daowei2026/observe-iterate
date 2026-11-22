"""DIAGNOSTIC_ONLY：只读同SOF原始PNV与self-calendar对照，不运行任何Feature。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv
import inspect
import json
import os
import shutil
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parent
PRIOR=ROOT.parent/'D005'
def write(n,x):(ROOT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2,default=str)+'\n')
def digest(p):
    h=sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b)
    return h.hexdigest()

def main():
    from m3sof import settings
    from mquant.frame import CurrSof,CurrCalendar
    from mquant.frame.core.data import KDataLoader
    from mquant.frame.core.store import DbaUtil
    settings.ctx['APP_DIR']=str(ROOT/'platform-app')
    settings.ctx['DEFAULT_STORE_DIR']=str(PRIOR/'store')
    settings.ctx['MQUANT_LOGGER_DIR']=str(ROOT/'logs')
    for relative in ['mquant/config/prod/sof/TA_updto20240229_DBA.json','mquant/config/prod/store_dir.json']:
        target=ROOT/'platform-app'/relative;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(PRIOR/'platform-app'/relative,target)
    records=[];report=dict(diagnostic_only=True,producer_executed=False,pid=os.getpid(),started_at=datetime.now(timezone.utc).isoformat(),symbols=[])
    with CurrSof(sof_name='TA_updto20240229_DBA',stk_tlist='steel',startDay='2021-01-01',endDay='2023-12-31',full_period=None) as ctx,CurrCalendar('night_end_at_2300'):
        from mquant.frame import KLine
        sof=KLine(freq='5m').sof
        report['pnv_dir']=sof.pnv_dir
        report['loader_source']=inspect.getfile(KDataLoader)
        for s in ['rb','hc','i']:
            loader=KDataLoader(sof,s,'5m');raw=loader.df
            exported=pd.read_csv(PRIOR/'upstream'/f'{s}_kline.csv',index_col='timestamp',parse_dates=True)
            assert raw.index.equals(exported.index)
            assert np.allclose(raw.close.to_numpy(),exported.close.to_numpy(),equal_nan=True)
            missing=raw[~np.isfinite(raw.close)]
            assert len(missing)==69
            path=Path(sof.pnv_dir)/'5m'/(s+'_night_end_at_2300')
            files=[dict(field=f,path=str(path/(f+'.dba')),bytes=(path/(f+'.dba')).stat().st_size,
                        sha256=digest(path/(f+'.dba'))) for f in ['open','high','low','close','volume','closeUti','closeTs']]
            a=raw.index.get_indexer([missing.index[0]])[0];b=raw.index.get_indexer([missing.index[-1]])[0]
            for ts,row in raw.iloc[max(0,a-2):b+3].iterrows():
                records.append(dict(symbol=s,timestamp=str(ts),closeUti=int(row.closeUti),open=str(row.open),high=str(row.high),low=str(row.low),close=str(row.close),volume=float(row.volume),close_bits=hex(int(np.float64(row.close).view(np.uint64))),finite_close=bool(np.isfinite(row.close))))
            own=Path(sof.pnv_dir)/'5m'/s
            selfcheck=dict(path=str(own),exists=(own/'close.dba').is_file())
            if selfcheck['exists']:
                values=DbaUtil.read_ndarray(str(own),'close','f8')
                times=DbaUtil.read_ndarray(str(own),'closeTs','M8[ns]')
                idx=pd.DatetimeIndex(times);locations=idx.get_indexer(missing.index)
                selfcheck.update(target_positions=69,present=int(np.sum(locations>=0)),finite_at_targets=int(np.sum(np.isfinite(values[locations[locations>=0]]))))
            report['symbols'].append(dict(symbol=s,pnv_calendar_path=str(path),rows=len(raw),
                exported_close_equal=True,missing_rows=len(missing),first_missing=str(missing.index[0]),last_missing=str(missing.index[-1]),
                raw_encoded_nan_bits=[hex(int(x)) for x in np.unique(missing.close.to_numpy().view(np.uint64))],
                uti_step_values=[int(x) for x in np.unique(np.diff(raw.closeUti.to_numpy()))],
                all_missing_ohlc=bool(missing[['open','high','low','close']].isna().all().all()),zero_volume_missing=int(np.sum(missing.volume==0)),
                previous=dict(timestamp=str(raw.index[a-1]),close=str(raw.iloc[a-1].close),uti=int(raw.iloc[a-1].closeUti)),
                resumed=dict(timestamp=str(raw.index[b+1]),close=str(raw.iloc[b+1].close),uti=int(raw.iloc[b+1].closeUti)),
                self_calendar_comparison=selfcheck,files=files))
    with (ROOT/'PNV_GAP_EXCERPT.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,list(records[0]),lineterminator='\n');w.writeheader();w.writerows(records)
    report.update(completed=True,finished_at=datetime.now(timezone.utc).isoformat())
    write('PNV_INPUT_PROBE.json',report)
    print(json.dumps({k:v for k,v in report.items() if k!='symbols'},ensure_ascii=False))
    for r in report['symbols']:print(json.dumps({k:v for k,v in r.items() if k!='files'},ensure_ascii=False))

if __name__=='__main__':main()
