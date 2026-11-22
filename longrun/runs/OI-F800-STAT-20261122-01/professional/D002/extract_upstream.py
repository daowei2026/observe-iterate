"""从同一参数的公开上游缓存只读取数；不运行Source，不补算缺失结果。"""
from pathlib import Path
from datetime import datetime, timezone
import json
import os
import sys
import traceback
sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_formal import ROOT, SOF, setup, construct, digest, write


def main():
    out = ROOT / 'upstream'
    out.mkdir(exist_ok=True)
    report = dict(started_at=datetime.now(timezone.utc).isoformat(), pid=os.getpid(),
                  requested_sof=SOF, completed=False, producer_executed=False, features=[])
    try:
        setup()
        from mquant.frame import CurrSof, CurrCalendar, KLine, CalType
        from mquant.frame.lib3 import CurrSymbol
        with CurrSof(**SOF), CurrCalendar('night_end_at_2300'):
            for symbol in ['rb', 'hc', 'i']:
                with CurrSymbol(symbol):
                    f, _, _, _ = construct()
                    turns = f.P.inputs[0]['input']['scale_turn']
                    rct = turns.P.falter
                    zig = rct.P.zig
                    for name, feature in [('kline', KLine(freq='5m')), ('zig', zig), ('rct', rct), ('scale', turns)]:
                        item = dict(symbol=symbol, kind=name, full_dir=str(feature.full_dir), tables=[])
                        report['features'].append(item)
                        if name != 'kline':
                            assert (Path(feature.full_dir) / 'fields.json').exists(), '上游缓存缺失，禁止静默运行：' + str(feature.full_dir)
                        feature.run(CalType.OnlyRead)
                        frames = feature.to_dfs() if name == 'scale' else {name: feature.to_df()}
                        for table, frame in frames.items():
                            suffix = name + '_' + table if name == 'scale' else name
                            path = out / (symbol + '_' + suffix + '.csv')
                            frame.index.name = 'timestamp'
                            frame.to_csv(path, index=True)
                            metadata = dict(name=suffix, rows=len(frame), columns=list(map(str, frame.columns)),
                                first=str(frame.index.min()), last=str(frame.index.max()),
                                nulls={str(k): int(v) for k, v in frame.isna().sum().items()},
                                path=str(path), sha256=digest(path))
                            item['tables'].append(metadata)
                            print('UPSTREAM_READ ' + json.dumps(dict(symbol=symbol, name=suffix, rows=len(frame)), ensure_ascii=False), flush=True)
        report['completed'] = True
    except Exception as error:
        report.update(error=str(error), traceback=traceback.format_exc())
        print(report['traceback'], flush=True)
    report['finished_at'] = datetime.now(timezone.utc).isoformat()
    write(ROOT / 'UPSTREAM_EXTRACTION.json', report)
    return 0 if report['completed'] else 1


if __name__ == '__main__':
    sys.exit(main())
