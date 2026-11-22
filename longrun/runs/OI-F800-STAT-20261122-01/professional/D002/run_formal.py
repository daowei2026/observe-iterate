"""D002 正常 Python F 构造、生产及独立只读。平台存储位置单独配置，业务参数不变。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import argparse
import inspect
import json
import os
import shutil
import subprocess
import sys
import traceback

BASE = Path('/dwdhome/fy/BASE_E6_2_copy')
ROOT = Path(__file__).resolve().parent
RECORD = Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
PRIOR = RECORD / 'longrun/runs/OI-F800-STAT-20261122-01/professional/D001'
RUNTIME = BASE / '.runtime/f-wide-observation-20261122/runtime'
SOF = dict(sof_name='TA_updto20240229_DBA', stk_tlist='steel',
           startDay='2021-01-01', endDay='2023-12-31', full_period=None)


def digest(path):
    h = sha256()
    with Path(path).open('rb') as file:
        for block in iter(lambda: file.read(4 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, default=str) + '\n')


def setup():
    from m3sof import settings
    settings.ctx['APP_DIR'] = str(ROOT / 'platform-app')
    settings.ctx['DEFAULT_STORE_DIR'] = str(ROOT / 'store')
    settings.ctx['MQUANT_LOGGER_DIR'] = str(ROOT / 'logs')
    assert Path(os.environ['M3WORKS']).resolve() == RUNTIME


def construct():
    from mquant.frame import CurrSof, CurrCalendar
    from mquant.tis.frp.fqv_kline_example import make_features
    from mquant.tis.frp.CommonPriceTurnGroupCandidates import CommonPriceTurnGroupCandidatesFrp
    reference = json.loads((PRIOR / 'inputs/fqv-kline-rb-hc-i.json').read_text())
    params = dict(reference['python_parameters'])
    params['symbols'] = tuple(params['symbols'])
    assert Path(inspect.getfile(make_features)).resolve() == (RUNTIME / 'mquant/tis/frp/fqv_kline_example.py').resolve()
    base, _, _ = make_features(**params)
    profile = dict(base.P.profile)
    profile['observation_multiple'] = 800
    assert base.P.inputs is not None
    f = CommonPriceTurnGroupCandidatesFrp(inputs=base.P.inputs, domain=base.P.domain,
                                        profile=profile, result_layout=base.P.result_layout)
    original = json.loads(base.doFrpTaskParam(run_ups=False).for_json()['params'])
    actual = json.loads(f.doFrpTaskParam(run_ups=False).for_json()['params'])
    expected = json.loads((PRIOR / 'configuration.json').read_text())
    assert actual == expected and original == json.loads((PRIOR / 'baseline-configuration.json').read_text())
    restored = json.loads(json.dumps(actual))
    assert restored['profile'].pop('observation_multiple') == 800 and restored == original
    assert actual['profile']['delta'] == 600 and actual['profile']['unit'] == 'CalendarUTITick'
    assert actual['profile']['method']['revision'] == '1'
    assert actual['domain']['objects'] == ['rb', 'hc', 'i']
    assert all(s['input']['freq'] == '5m' and s['input']['calendar'] == 'night_end_at_2300'
               and s['market']['units_per_open_minute'] == 120 for s in actual['sources'])
    assert str(f.sof.startDay) == SOF['startDay'] and str(f.sof.endDay) == SOF['endDay']
    assert Path(f.full_dir).resolve().is_relative_to(ROOT / 'store')
    assert f.full_dir != base.full_dir
    return f, base, actual, original


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['inspect', 'produce', 'read'], required=True)
    args = parser.parse_args()
    target = ROOT / {'inspect': 'preflight', 'produce': 'produced', 'read': 'readback'}[args.mode]
    target.mkdir(parents=True, exist_ok=True)
    report = dict(run_id='OI-F800-STAT-20261122-01', call_id='C0005', delegation_id='D002',
                  mode=args.mode, pid=os.getpid(), started_at=datetime.now(timezone.utc).isoformat(),
                  completed=False, producer_executed=False, public_read_completed=False,
                  requested_sof=SOF, calendar='night_end_at_2300', tables={})
    try:
        setup()
        from mquant.frame import CurrSof, CurrCalendar, CalType
        with CurrSof(**SOF), CurrCalendar('night_end_at_2300'):
            f, baseline, actual, original = construct()
            write(target / 'configuration.json', actual)
            write(target / 'baseline-configuration.json', original)
            assert json.loads((target / 'configuration.json').read_text()) == actual
            assert digest(target / 'configuration.json') == 'b72095ff100da926474701b74bff7586a74b9770bc81cadc34c23cfe223e5cb3'
            write(target / 'task-envelope.json', f.doFrpTaskParam(run_ups=False).for_json())
            command = subprocess.run(['epm', 'exec', 'which', 'ts'], cwd=RUNTIME / 'edh-universe',
                                     text=True, capture_output=True, check=True)
            resolved = command.stdout.strip().splitlines()[-1]
            assert Path(resolved).resolve() == (RUNTIME / 'edh-universe/bin/ts').resolve(), resolved
            binding = json.loads((ROOT / 'FRP_SOURCE_BINDING.json').read_text())
            assert digest(resolved) == binding['engine_sha256'] and not binding['mismatches']
            prior = json.loads((PRIOR / 'INSTANCE_INSPECTION.json').read_text())
            fields = Path(f.full_dir) / 'fields.json'
            report.update(full_dir=str(f.full_dir), baseline_full_dir=str(baseline.full_dir),
                          configuration_sha256=digest(target / 'configuration.json'),
                          task_envelope_sha256=digest(target / 'task-envelope.json'),
                          frp_code_ref='daowei2026/frp@ac1927518ad6105f15ffbe37fea45e4be91ba574',
                          tis_code_ref='daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767',
                          engine_executable=resolved, engine_sha256=digest(resolved),
                          fields_existed_before=fields.is_file(),
                          original_candidate_full_dir=prior['full_dir'],
                          original_candidate_fields_exists=(Path(prior['full_dir']) / 'fields.json').is_file(),
                          storage_platform_config=str(ROOT / 'PLATFORM_STORAGE_BINDING.json'))
            if args.mode == 'produce':
                assert os.environ.get('OI_FORMAL_LOCK_HELD') == 'OI-F800-STAT-20261122-01'
                assert not fields.exists(), '准确结果已存在，禁止覆盖；须先验证复用'
                write(target / 'report-before-run.json', report)
                print('FORMAL_F800_PRODUCER_START ' + str(f.full_dir), flush=True)
                f = f.rerun(2)
                report['producer_executed'] = True
                print('FORMAL_F800_PRODUCER_FINISHED', flush=True)
            if args.mode != 'inspect':
                assert fields.is_file(), '准确实例未找到fields.json，禁止静默回退或重算'
                f.run(CalType.OnlyRead)
                frames = f.to_dfs()
                assert len(frames) == 31
                assert f.to_df().equals(frames['occurrences'])
                for name, frame in frames.items():
                    path = target / 'tables' / (name + '.csv')
                    path.parent.mkdir(parents=True, exist_ok=True)
                    frame.to_csv(path, index=True)
                    report['tables'][name] = dict(rows=len(frame), columns=list(map(str, frame.columns)),
                        index_names=list(frame.index.names), path=str(path), sha256=digest(path))
                groups = frames['occurrences']
                assert ((groups['groupOriginalDeadline'] - groups['groupOriginalAnchor']) == 480000).all()
                assert ((groups['groupOriginalRevisionEnd'] - groups['groupOriginalDeadline']) == 3600).all()
                report.update(public_read_completed=True, fields_sha256=digest(fields),
                              native_K800_output_windows_verified=True,
                              all_table_names=sorted(frames), primary_public_api_equal=True)
            report['completed'] = True
    except Exception as error:
        report.update(error_type=type(error).__name__, error=str(error), traceback=traceback.format_exc())
        print(report['traceback'], flush=True)
    report['finished_at'] = datetime.now(timezone.utc).isoformat()
    write(target / 'report.json', report)
    print(json.dumps({k: v for k, v in report.items() if k not in ['tables', 'traceback']}, ensure_ascii=False, default=str), flush=True)
    print('TABLE_ROWS ' + json.dumps({k: v['rows'] for k, v in report['tables'].items()}), flush=True)
    return 0 if report['completed'] else 1


if __name__ == '__main__':
    sys.exit(main())
