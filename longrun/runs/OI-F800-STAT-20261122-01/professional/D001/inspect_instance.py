"""D001：只核对源码、构造参数和读取合同；不调用任何 Feature 运行或读表。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import ast
import importlib
import inspect
import json
import os
import shutil
import subprocess

BASE = Path('/dwdhome/fy/BASE_E6_2_copy')
OUT = BASE / 'artifacts/OI-F800-STAT-20261122-01/D001'
RECORD = Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
RUNTIME = BASE / '.runtime/f-wide-observation-20261122/runtime'
FRP = BASE / '.runtime/f-observation-multiple-github-20261122/frp'
TIS = BASE / 'mquant/tis'
FRP_COMMIT = 'ac1927518ad6105f15ffbe37fea45e4be91ba574'
TIS_COMMIT = '2f460d663d821cf2ba25555eda13e78b697d0767'
OI_COMMIT = '87b951bbd15078a2d6353bdd24afe0d8f19c845c'


def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args])


def difference(left, right, prefix=''):
    if isinstance(left, dict) and isinstance(right, dict):
        rows = []
        for key in sorted(left.keys() | right.keys()):
            path = prefix + '/' + key
            if key not in left:
                rows.append({'path': path, 'operation': 'add', 'value': right[key]})
            elif key not in right:
                rows.append({'path': path, 'operation': 'remove', 'value': left[key]})
            else:
                rows.extend(difference(left[key], right[key], path))
        return rows
    return [] if left == right else [{'path': prefix, 'operation': 'replace', 'before': left, 'after': right}]


assert BASE.resolve() == BASE
assert Path(os.environ['M3WORKS']).resolve() == RUNTIME
assert git(FRP, 'rev-parse', 'HEAD').decode().strip() == FRP_COMMIT
assert not git(FRP, 'status', '--porcelain', '--untracked-files=no').strip()
source_checks = []
frp_files = [
    'CommonPriceTurnGroupCandidates.hs', 'U2/GroupCandidateTypes.hs',
    'U2/GroupCandidateMaterial.hs', 'U2/GroupCandidateEvolution.hs',
    'U2/GroupCandidateDecisions.hs', 'U2/GroupCandidateSource.hs',
    'U2/GroupCandidatePairs.hs', 'U2/GroupCandidateKLineInput.hs',
    'U2/GroupCandidateStorage.hs', 'U2/FormationParticipationFacts.hs',
]
for relative in frp_files:
    name = 'src/Frp/Instance/ISL/Opportunity/' + relative
    expected = git(FRP, 'show', FRP_COMMIT + ':' + name)
    target = RUNTIME / 'edh-universe/frp/frp' / name
    assert target.read_bytes() == expected, name
    source_checks.append({'ref': f'daowei2026/frp@{FRP_COMMIT}:{name}',
                          'loaded_runtime_source': str(target), 'matches_exact': True,
                          'sha256': sha256(expected).hexdigest()})
for name in ['frp/fqv_kline_example.py', 'frp/CommonPriceTurnGroupCandidates.py',
             'frp/_U2GroupCandidateFields.py', 'frp/_U2CandidateRejectionFields.py',
             'frp/U2CoreResults.py', 'frpExample/STCalendar.py']:
    expected = git(TIS, 'show', TIS_COMMIT + ':' + name)
    target = RUNTIME / 'mquant/tis' / name
    assert target.read_bytes() == expected, name
    source_checks.append({'ref': f'daowei2026/tis@{TIS_COMMIT}:{name}',
                          'loaded_runtime_source': str(target.resolve()), 'matches_exact': True,
                          'sha256': sha256(expected).hexdigest()})

script = git(RECORD, 'show', OI_COMMIT + ':task-inputs/u2-fqv-observation/实例运行脚本.py').decode()
assignments = [node for node in ast.parse(script).body if isinstance(node, ast.Assign)]
params = next(ast.literal_eval(node.value) for node in assignments
              if any(isinstance(t, ast.Name) and t.id == 'PARAMS' for t in node.targets))
reference = json.loads((OUT / 'inputs/fqv-kline-rb-hc-i.json').read_text())
assert json.loads(json.dumps(params)) == reference['python_parameters']
from mquant.frame import CurrSof, CurrCalendar
from mquant.tis.frp.fqv_kline_example import make_features
from mquant.tis.frp.CommonPriceTurnGroupCandidates import CommonPriceTurnGroupCandidatesFrp

wrapper = importlib.import_module('mquant.tis.frp.CommonPriceTurnGroupCandidates')
constructor = Path(inspect.getfile(make_features)).resolve()
wrapper_file = Path(wrapper.__file__).resolve()
assert constructor == (RUNTIME / 'mquant/tis/frp/fqv_kline_example.py').resolve()
assert wrapper_file == (RUNTIME / 'mquant/tis/frp/CommonPriceTurnGroupCandidates.py').resolve()
sof = dict(sof_name='TA_updto20240229_DBA', stk_tlist='steel',
           startDay='2021-01-01', endDay='2023-12-31', full_period=None)
with CurrSof(**sof), CurrCalendar('night_end_at_2300'):
    base_f, _, _ = make_features(**params)
    profile = dict(base_f.P.profile)
    profile['observation_multiple'] = 800
    if base_f.P.inputs is not None:
        f800 = CommonPriceTurnGroupCandidatesFrp(
            inputs=base_f.P.inputs, domain=base_f.P.domain, profile=profile,
            result_layout=base_f.P.result_layout)
    elif base_f.P.sources is not None:
        f800 = CommonPriceTurnGroupCandidatesFrp.from_sources(
            base_f.P.sources, domain=base_f.P.domain, profile=profile)
    else:
        raise RuntimeError('F baseline has neither inputs nor sources')
    original = json.loads(base_f.doFrpTaskParam(run_ups=False).for_json()['params'])
    expanded = json.loads(f800.doFrpTaskParam(run_ups=False).for_json()['params'])
    write('baseline-configuration.json', original)
    write('configuration.json', expanded)
    original = json.loads((OUT / 'baseline-configuration.json').read_text())
    expanded = json.loads((OUT / 'configuration.json').read_text())
    delta = difference(original, expanded)
    assert delta == [{'path': '/profile/observation_multiple', 'operation': 'add', 'value': 800}], delta
    assert original == reference['feature_parameters']['F']['params']
    assert expanded['profile']['delta'] == 600
    assert expanded['profile']['unit'] == 'CalendarUTITick'
    assert expanded['profile']['method']['revision'] == '1'
    assert expanded['domain']['objects'] == ['rb', 'hc', 'i']
    assert all(s['input']['freq'] == '5m' for s in expanded['sources'])
    assert all(s['input']['calendar'] == 'night_end_at_2300' for s in expanded['sources'])
    assert all(s['market']['units_per_open_minute'] == 120 for s in expanded['sources'])
    baseline_dir, f800_dir = str(base_f.full_dir), str(f800.full_dir)
    assert baseline_dir != f800_dir
    assert str(f800.sof.startDay) == sof['startDay'] and str(f800.sof.endDay) == sof['endDay']
    historical = json.loads((BASE / 'results/f-wide-observation-20261122/configuration/configuration.json').read_text())
    report = dict(run_id='OI-F800-STAT-20261122-01', call_id='C0002', delegation_id='D001',
                  checked_at=datetime.now(timezone.utc).isoformat(), completed=True,
                  operation='source and constructor inspection; no Feature execution',
                  source_versions=dict(frp=FRP_COMMIT, tis=TIS_COMMIT),
                  requested_sof=sof, calendar='night_end_at_2300',
                  constructor_file=str(constructor), wrapper_file=str(wrapper_file),
                  type_file=inspect.getfile(type(f800)), source_checks=source_checks,
                  baseline_matches_pinned_F_parameters=True,
                  serialized_config_written_and_read_back=True, config_delta=delta,
                  configuration_sha256=sha256((OUT / 'configuration.json').read_bytes()).hexdigest(),
                  baseline_configuration_sha256=sha256((OUT / 'baseline-configuration.json').read_bytes()).hexdigest(),
                  full_dir=f800_dir, baseline_full_dir=baseline_dir,
                  exact_f800_fields_exists=(Path(f800_dir) / 'fields.json').is_file(),
                  baseline_fields_exists=(Path(baseline_dir) / 'fields.json').is_file(),
                  historical_f800_config_delta=difference(expanded, historical),
                  frp_executable=str(shutil.which('ts')), frp_executable_executed=False,
                  binary_commit_binding='NOT_VERIFIED_BY_D001; runtime source equivalence only',
                  formal_run_result_binding='NOT_ESTABLISHED; X required',
                  producer_executed=False, public_tables_read=False)
    write('INSTANCE_INSPECTION.json', report)

schema = {name: dict(family=spec[0], depth=spec[1], root=spec[2],
                    fields={field: dict(path=path, dtype=wrapper.GROUP_DTYPES[path])
                            for field, path in spec[3].items()})
          for name, spec in wrapper.GROUP_TABLES.items()}
write('PUBLIC_TABLE_SCHEMA.json', dict(layout=wrapper.LAYOUT, tables=schema,
                                      enums=wrapper.ENUMS, source='locked TIS public reader declarations',
                                      current_run_data_availability='UNCONFIRMED until X'))
print(json.dumps({k: v for k, v in report.items() if k != 'source_checks'}, ensure_ascii=False, indent=2))
print('PUBLIC_TABLE_CONTRACTS', len(schema))
