"""校验D001交付和V2字段；不模拟送达、资源锁、Feature运行或manager消费。"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import argparse
import json
import re
import subprocess
from jsonschema import Draft202012Validator

BASE = Path('/dwdhome/fy/BASE_E6_2_copy')
RECORD = Path('/dwdhome/fy/cgpterm/artifacts/wall-f-closure-20261122/OI-F800-STAT-20261122-01/executor-records')
RUN_ID = 'OI-F800-STAT-20261122-01'
RUN_PATH = 'longrun/runs/' + RUN_ID
RUN = RECORD / RUN_PATH
PRO = RUN / 'professional/D001'
CALL = RUN / 'calls/C0002'
OI_COMMIT = '87b951bbd15078a2d6353bdd24afe0d8f19c845c'
DELEGATION_COMMIT = '092819b56eaf3e08764ed23650c0826c0fdadec1'
BRANCH = 'codex/oi-f800-stat-20261122-01'


def read(path):
    return json.loads(path.read_text())


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args])


def exact(ref):
    match = re.fullmatch(r'([\w.-]+/[\w.-]+)@([0-9a-f]{40}):([^\s:#]+)', ref)
    assert match, ref
    return match.groups()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--return-commit')
    args = parser.parse_args()
    checks = []
    schema = json.loads(git(RECORD, 'show', OI_COMMIT + ':longrun/contracts/longrun_schema_v2.json'))
    def validate(kind, value):
        Draft202012Validator(dict(schema, **{'$ref': '#/$defs/' + kind})).validate(value)
    binding = read(RUN / 'RUN_BINDING.json')
    d = read(RUN / 'delegations/D001/DELEGATION.json')
    invocation = read(CALL / 'INVOCATION.json')
    for kind, value in [('binding', binding), ('delegation', d), ('invocation', invocation)]:
        validate(kind, value)
    assert binding['workers'] == []
    assert binding['manager'] == f'codex:{RUN_ID}:manager'
    assert d['recipient'] == f'codex:{RUN_ID}:executor:E1'
    assert invocation['recipient'] == d['recipient'] and invocation['run_id'] == d['run_id'] == RUN_ID
    assert invocation['assignment_ref'] == f'daowei2026/observe-iterate@{DELEGATION_COMMIT}:{RUN_PATH}/delegations/D001/DELEGATION.json'
    assert d['issuer'] == d['return_to'] == binding['manager']
    assert d['recipient'] in binding['executors']
    assert set(d['permitted_operations']) == {'run_result_statistics_analysis_write', 'run_record_write'}
    assert set(d['allowed_writes']) == {str(BASE), RUN_PATH + '/**'}
    assert set(d['permitted_operations']) <= {grant['operation'] for grant in binding['grants']}
    owner_go = (RUN / 'OWNER_START.md').read_text()
    for grant in binding['grants']:
        if grant['operation'] in d['permitted_operations']:
            assert grant['authority_quote'] in owner_go
    checks.append('锁定V2 schema的binding/delegation/invocation及CODEX_NATIVE_DIRECT逻辑身份、授权子集一致')

    audit = read(PRO / 'SOURCE_AUDIT.json')
    for item in audit['sources']:
        repo, commit, path = exact(item['ref'])
        if repo == 'daowei2026/observe-iterate':
            content = git(RECORD, 'show', commit + ':' + path)
        else:
            assert repo == 'daowei2026/feature-refinement-implementation-agent-evolution'
            content = (PRO / 'inputs/fqv-kline-rb-hc-i.json').read_bytes()
        assert sha256(content).hexdigest() == item['sha256'], item['ref']
        assert subprocess.check_output(['git', 'hash-object', '--stdin'], input=content).decode().strip() == item['git_blob']
    checks.append('25个来源的精确内容SHA-256及Git blob重核一致')

    inspection = read(PRO / 'INSTANCE_INSPECTION.json')
    assert inspection['completed'] and not inspection['producer_executed'] and not inspection['public_tables_read']
    assert not inspection['frp_executable_executed']
    for item in inspection['source_checks']:
        repo, commit, path = exact(item['ref'])
        source_root = BASE / ('.runtime/f-observation-multiple-github-20261122/frp' if repo == 'daowei2026/frp' else 'mquant/tis')
        content = git(source_root, 'show', commit + ':' + path)
        assert content == Path(item['loaded_runtime_source']).read_bytes()
        assert sha256(content).hexdigest() == item['sha256']
    checks.append('16个相关runtime源文件与FRP/TIS锁定Git对象再次逐字节核对一致')

    baseline = read(PRO / 'baseline-configuration.json')
    config = read(PRO / 'configuration.json')
    restored = json.loads(json.dumps(config))
    assert restored['profile'].pop('observation_multiple') == 800
    assert restored == baseline
    assert baseline == read(PRO / 'inputs/fqv-kline-rb-hc-i.json')['feature_parameters']['F']['params']
    assert config['profile']['delta'] == 600 and config['profile']['unit'] == 'CalendarUTITick'
    assert config['profile']['method']['revision'] == '1'
    assert config['domain']['objects'] == ['rb', 'hc', 'i']
    assert all(source['input']['freq'] == '5m' and source['input']['calendar'] == 'night_end_at_2300'
               and source['market']['units_per_open_minute'] == 120 for source in config['sources'])
    assert inspection['requested_sof'] == dict(sof_name='TA_updto20240229_DBA', stk_tlist='steel',
                                               startDay='2021-01-01', endDay='2023-12-31', full_period=None)
    assert inspection['calendar'] == 'night_end_at_2300'
    for name, field in [('configuration.json', 'configuration_sha256'), ('baseline-configuration.json', 'baseline_configuration_sha256')]:
        assert sha256((PRO / name).read_bytes()).hexdigest() == inspection[field]
    assert inspection['full_dir'] != inspection['baseline_full_dir']
    assert inspection['exact_f800_fields_exists'] is False
    checks.append('完整配置只增加K=800；基线、SOF范围记录、配置hash及目录区分一致；未宣称实际结果存在')

    package = read(PRO / 'FeatureUnderstandingPackage.json')
    required = {'package_id','feature_ref','implementation_sources','business_objects','states','occurrences',
                'intermediate_decisions','processing_relations','parameters','run_result_field_map',
                'business_main_outputs','intermediate_processing_results','unconfirmed_items','completion_status'}
    assert required <= package.keys()
    assert package['completion_status'] == 'PARTIAL' and package['unconfirmed_items']
    tables = read(PRO / 'PUBLIC_TABLE_SCHEMA.json')
    assert len(tables['tables']) == 31 and tables['current_run_data_availability'] == 'UNCONFIRMED until X'
    for row in package['run_result_field_map']:
        if row.get('table') in tables['tables']:
            assert set(row['fields']) <= set(tables['tables'][row['table']]['fields'])
            assert row['availability'] == 'UNCONFIRMED'
    assert {row['id'] for row in package['business_objects']} == {'BO1', 'BO2', 'BO3'}
    checks.append('原生Package顶层合同、PARTIAL具名缺口、31表声明及具体映射字段一致')
    assert git(RECORD, 'branch', '--show-current').decode().strip() == BRANCH
    changes = git(RECORD, 'diff', '--cached', '--name-only').decode().splitlines()
    assert all(path.startswith(RUN_PATH + '/') for path in changes)
    checks.append('记录分支符合packet；暂存修改仅限本Run路径')

    if args.return_commit:
        assert re.fullmatch('[0-9a-f]{40}', args.return_commit)
        result = read(CALL / 'PRO_RETURN.json')
        validate('professional_return', result)
        assert result['role'] == 'executor' and result['call_id'] == 'C0002' and result['run_id'] == RUN_ID
        assert result['sender'] == d['recipient'] and result['return_to'] == d['issuer']
        assert result['delegation_ref'] == invocation['assignment_ref']
        assert result['issued_delegation_refs'] == result['issued_order_refs'] == result['accepted_worker_refs'] == []
        assert result['professional_state'] == 'REPORTED_COMPLETE' and result['owner_request_ref'] is None
        for field, path in [('result_ref','EXECUTOR_REPORT.md'), ('remaining_scope_ref','REMAINING_SCOPE.md'), ('continuation_ref','CONTINUATION.md')]:
            assert result[field] == f'daowei2026/observe-iterate@{args.return_commit}:{RUN_PATH}/calls/C0002/{path}'
            assert git(RECORD, 'show', args.return_commit + ':' + RUN_PATH + '/calls/C0002/' + path) == (CALL / path).read_bytes()
        git(RECORD, 'merge-base', '--is-ancestor', args.return_commit, 'HEAD')
        checks.append('PRO_RETURN符合锁定schema、原D/manager及零W；所有业务引用指向已存在的先前专业提交，无未来引用')

    report = dict(checked_at=datetime.now(timezone.utc).isoformat(), run_id=RUN_ID, call_id='C0002', delegation_id='D001',
                  check_status='PASS_FOR_LISTED_CHECKS_ONLY', checks=checks,
                  native_completion_status=package['completion_status'],
                  native_engine_execution_verified=False, current_formal_result_verified=False,
                  controller_receipt_verified=False, manager_consumption_verified=False,
                  original_longrun_gate_status='未声称通过；C0001已记录同版工具硬编码chatgpt manager的Binding失败；未修改工具或真实身份')
    if args.return_commit:report['prior_professional_commit'] = args.return_commit
    target = CALL / ('VALIDATION_RETURN.json' if args.return_commit else 'VALIDATION.json')
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
