from pathlib import Path
import datetime
import importlib
import importlib.util
import json
import os
import runpy
import sys

run_root = Path(os.environ['OI_W004_RUN_ROOT']).resolve()
overlay_mquant = (run_root / 'source' / 'mquant').resolve()
tis_root = (overlay_mquant / 'tis').resolve()
obs_root = (run_root / 'source' / 'observe-iterate').resolve()
output_root = (run_root / 'output' / 'u2_f_caegraph').resolve()
d_script = obs_root / 'longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py'
report_path = run_root / 'module_overlay_report.json'
preloaded = []
origins = {}
report = {'ok': False, 'preloaded': preloaded, 'origins': origins}
def write_report():
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
try:
    import mquant
    preloaded = sorted(name for name in sys.modules if name == 'mquant.tis' or name.startswith('mquant.tis.'))
    report['preloaded'] = preloaded
    report['base_mquant_file'] = getattr(mquant, '__file__', None)
    report['base_mquant_path_before'] = [str(p) for p in mquant.__path__]
    if preloaded:
        raise RuntimeError('mquant.tis loaded before locked overlay: ' + ','.join(preloaded))
    mquant.__path__ = [str(overlay_mquant)] + [str(p) for p in mquant.__path__ if Path(p).resolve() != overlay_mquant]
    report['mquant_path_after'] = list(mquant.__path__)
    importlib.invalidate_caches()
    expected = {
        'mquant.tis.frp.fqv_kline_example': tis_root / 'frp/fqv_kline_example.py',
        'mquant.tis.frp.CommonPriceTurnGroupCandidates': tis_root / 'frp/CommonPriceTurnGroupCandidates.py',
        'mquant.tis.frp.PostTurnGroupDirectionalOrganization': tis_root / 'frp/PostTurnGroupDirectionalOrganization.py',
        'mquant.tis.frp.CommonTurnGroupValidity': tis_root / 'frp/CommonTurnGroupValidity.py',
        'mquant.tis.frpExample.Wave': tis_root / 'frpExample/Wave.py',
        'mquant.tis.frpExample.STCalendar': tis_root / 'frpExample/STCalendar.py',
        'mquant.tis.frpExample.ScaleTurn': tis_root / 'frpExample/ScaleTurn.py',
    }
    for name, wanted in expected.items():
        spec = importlib.util.find_spec(name)
        actual = None if spec is None or spec.origin is None else Path(spec.origin).resolve()
        origins[name] = {'expected': str(wanted.resolve()), 'actual': None if actual is None else str(actual)}
        if actual != wanted.resolve():
            raise RuntimeError(f'locked module origin mismatch: {name}: {actual} != {wanted}')
    report['ok'] = True
    write_report()
except Exception as exc:
    report['error_type'] = type(exc).__name__
    report['error'] = str(exc)
    write_report()
    raise
sys.argv = [str(d_script), '--output-dir', str(output_root)]
with (run_root / 'logs' / 'D_dispatch.json').open('x', encoding='utf-8') as f:
    json.dump({'attempt_count': 1, 'started_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'argv': sys.argv, 'cwd': os.getcwd(), 'entry': 'runpy.run_path', 'run_name': '__main__'}, f, ensure_ascii=False, indent=2)
    f.write('\n')
runpy.run_path(str(d_script), run_name='__main__')
