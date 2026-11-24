"""X 只读补充：同代码/默认实例/全年源/本 Run 上游，按列名比较完整重算与已有 DBA。

只在 A03 runner 结束后执行；保留其原断言，不覆盖任何既有产物。
"""
import datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time
import traceback

BASE = Path(__file__).resolve().parent
ATTEMPT = BASE.parent / 'formal-attempt-A03'
OUT = BASE.parent / 'readback-verification-R01'
OUT.mkdir(exist_ok=False)
execution = json.loads((ATTEMPT / 'execution_result.json').read_text())
events = [json.loads(x) for x in (ATTEMPT / 'execution_events.jsonl').read_text().splitlines()]
assert events[-1]['stage'] == 'RUNNER_FINISHED'
assert not execution['lock_acquired'] or execution['lock_released']
LOCK = Path(execution['lock_path'])
state = {'call_id': 'C0007', 'delegation_id': 'D002', 'verification_id': 'R01',
         'started_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'scope': 'FULL_FORMAL_REPLAY_READBACK_ONLY', 'lock_acquired': False,
         'lock_released': False, 'feature_dump_calls_allowed': False,
         'existing_results_overwritten': False, 'per_symbol': [], 'errors': []}

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def save():
    p = OUT / 'verification_progress.json'
    tmp = p.with_suffix('.tmp')
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2, default=str) + '\n')
    os.replace(tmp, p)

def event(stage, **kw):
    row = {'at': now(), 'stage': stage, **kw}
    with (OUT / 'verification_events.jsonl').open('a') as f:
        f.write(json.dumps(row, ensure_ascii=False) + '\n')
    state.update(current_stage=stage, last_update=row['at'])
    save()
    print(json.dumps(row, ensure_ascii=False), flush=True)

def artifact_manifest(path):
    return {p.relative_to(path).as_posix(): [p.stat().st_size, p.stat().st_mtime_ns]
            for p in sorted(path.rglob('*')) if p.is_file()}

def json_hashes(path):
    return {p.relative_to(path).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(path.rglob('*.json')) if p.is_file()}

fd = None
try:
    fd = os.open(LOCK, os.O_RDWR)
    st = os.fstat(fd)
    assert st.st_dev == 83 and st.st_ino == 15061041
    state['lock_identity'] = {'path': str(LOCK), 'device': st.st_dev, 'inode': st.st_ino,
                              'bytes_before': st.st_size, 'sha256_before': hashlib.sha256(LOCK.read_bytes()).hexdigest()}
    event('WAITING_ORIGINAL_LOCK_FOR_READBACK_REPLAY')
    deadline = time.monotonic() + 600
    while True:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            break
        except BlockingIOError:
            if time.monotonic() >= deadline:
                raise TimeoutError('ORIGINAL_PRODUCTION_LOCK_NOT_AVAILABLE_FOR_R01')
            time.sleep(2)
    state.update(lock_acquired=True, lock_acquired_at=now())
    event('ORIGINAL_LOCK_ACQUIRED_FOR_READBACK_REPLAY')
    tis = '/dwdhome/fy/BASE_E6_2_copy/mquant/tis'
    assert subprocess.check_output(['git', '-C', tis, 'rev-parse', 'HEAD'], text=True).strip() == '179016111ed0394f92025313e46bd13534932a74'
    assert not subprocess.check_output(['git', '-C', tis, 'status', '--short', '--untracked-files=no'], text=True).strip()

    import numpy as np
    from mquant.quant import OptContext
    from m3tt import CurrTradeSet, CurrSymbol
    from mquant.frame import CurrCalendar, CurrFaoCache, TmpStoreEnv, CurrCalType, CalType
    from mquant.frame.lang.internal.base import AbsFao
    from mquant.frame.core.app.env import StraEnv
    import mquant.tis.hf.prel0.p1_dba_export as export
    import mquant.tis.hf.prel0.attack_flow_assembler as am
    from mquant.tis.hf.prel0.p1_product_receipt import load_p1_product_receipt, feature_code_fingerprint

    original_run_with = AbsFao._run_with
    def read_only_run_with(self, write=False, read=False):
        if write:
            raise RuntimeError('R01_FORBIDS_ANY_FEATURE_DATABASE_OR_CACHE_WRITE')
        return original_run_with(self, write=False, read=read)
    def forbidden_dump(*args, **kwargs):
        raise RuntimeError('R01_FORBIDS_P1_DUMP_OR_CHUNK_WRITER')
    AbsFao._run_with = read_only_run_with
    export.P1DbaExportMixin.dump = forbidden_dump
    export._P1ChunkedDbaWriter.__init__ = forbidden_dump
    expected_code = feature_code_fingerprint(am.__file__, am.run_attack_flow_assembler_replay)
    assert Path(am.__file__).resolve().is_relative_to(Path(tis))
    overrides = {'SubContinuousContract': 'cal', 'AmountThreshold': 'cal', 'VolQuant': 'cal',
                 'WallAssembler': 'only_read', 'DirectedBigDealTick': 'only_read'}
    state['cal_type_overrides'] = overrides
    context = OptContext({'sof_name': 'TA_updto20240229_DBA', 'startDay': '2021-01-01', 'endDay': '2021-12-31'})

    def hash_array(values):
        a = np.asarray(values)
        assert not a.dtype.hasobject
        h = hashlib.sha256()
        h.update(str(a.dtype).encode()); h.update(str(a.shape).encode())
        for start in range(0, a.size, 262144):
            h.update(np.ascontiguousarray(a[start:start+262144]).tobytes())
        return h.hexdigest()

    for old in execution['feature_results']:
        if old['feature'] != 'attack' or len(old.get('receipts', [])) != 3:
            continue
        rec = {'symbol': old['symbol'], 'original_execution_status': old['status'],
               'status': 'RECONCILIATION_STARTED', 'artifact_location': old['full_dir'],
               'started_at': now(), 'tables': []}
        state['per_symbol'].append(rec)
        try:
            location = Path(old['full_dir'])
            before_manifest = artifact_manifest(location)
            before_json = json_hashes(location)
            with CurrFaoCache(), CurrTradeSet(context.sof), CurrSymbol(old['symbol']), CurrCalendar('night_end_at_2300'), TmpStoreEnv(rule=export.P1DbaExportMixin, store_dir=execution['store_root']), CurrCalType(overrides):
                attack = am.AttackFlowAssembler()
                assert str(attack.ppid) == old['ppid'] and Path(attack.full_dir).resolve() == location.resolve()
                assert expected_code == old['expected_code_version'] and not attack.backup_full_dirs
                for upstream in (attack.P.wall, attack.P.directed_large_deal_tactical, attack.P.directed_large_deal_structural):
                    assert StraEnv.rcal_type(upstream) == CalType.OnlyRead
                for kind in ('attack_segment', 'attack_formation_evidence', 'wall_relation_barrier'):
                    receipt = load_p1_product_receipt(attack, kind)
                    assert receipt['status'] == 'success' and receipt['code_version'] == expected_code
                    assert receipt in old['receipts']
                event('FULL_FORMAL_READONLY_REPLAY_STARTED', symbol=old['symbol'])
                output = attack.run(CalType.Cal).F
                loaded = attack.Dao.loadWith(str(location))
                assert loaded is not None and set(loaded) == set(output)
                for key in sorted(output):
                    computed = export._widen_int8_for_platform_dump(export.require_dba_frame(key, output[key]))
                    stored = loaded[key]
                    assert computed.shape == stored.shape and computed.index.equals(stored.index), key
                    assert set(computed.columns) == set(stored.columns), key
                    columns = sorted(computed.columns)
                    assert {c: str(computed[c].dtype) for c in columns} == {c: str(stored[c].dtype) for c in columns}, key
                    computed_hashes = {'__index__': hash_array(computed.index.values), **{str(c): hash_array(computed[c].values) for c in columns}}
                    stored_hashes = {'__index__': hash_array(stored.index.values), **{str(c): hash_array(stored[c].values) for c in columns}}
                    assert computed_hashes == stored_hashes, key
                    rec['tables'].append({'key': key, 'rows': int(stored.shape[0]),
                                          'computed_column_order': list(map(str, computed.columns)),
                                          'stored_column_order': list(map(str, stored.columns)),
                                          'column_order_equal': list(computed.columns) == list(stored.columns),
                                          'dtypes': {str(c): str(stored[c].dtype) for c in columns},
                                          'full_readback_digest': stored_hashes,
                                          'matches_full_formal_recomputed_result_by_column_name': True})
            assert before_manifest == artifact_manifest(location), 'R01_ARTIFACT_FILES_CHANGED'
            assert before_json == json_hashes(location), 'R01_RECEIPT_OR_METADATA_CHANGED'
            rec.update(status='FULL_FORMAL_REPLAY_AND_NAMED_COLUMN_READBACK_VERIFIED', finished_at=now(),
                       artifact_manifest_unchanged=True, receipt_and_metadata_sha256_unchanged=True,
                       artifact_metadata_sha256=before_json)
            event('FULL_FORMAL_READONLY_REPLAY_READBACK_VERIFIED', symbol=old['symbol'], table_count=len(rec['tables']))
        except Exception as exc:
            rec.update(status='READBACK_RECONCILIATION_FAILED', finished_at=now(), error_type=type(exc).__name__, error=str(exc))
            (OUT / (old['symbol'] + '-traceback.txt')).write_text(traceback.format_exc())
            state['errors'].append({'symbol': old['symbol'], 'type': type(exc).__name__, 'message': str(exc)})
            event('FULL_FORMAL_READONLY_REPLAY_FAILED', symbol=old['symbol'], error_type=type(exc).__name__, error=str(exc))
except Exception as exc:
    state['errors'].append({'type': type(exc).__name__, 'message': str(exc)})
    (OUT / 'runner-traceback.txt').write_text(traceback.format_exc())
    event('RECONCILIATION_STOPPED_WITH_RECORDED_GAP', error_type=type(exc).__name__, error=str(exc))
finally:
    if fd is not None:
        if state['lock_acquired']:
            state['lock_identity'].update(bytes_after=LOCK.stat().st_size, sha256_after=hashlib.sha256(LOCK.read_bytes()).hexdigest())
            fcntl.flock(fd, fcntl.LOCK_UN)
            state.update(lock_released=True, lock_released_at=now())
        os.close(fd)
    state['finished_at'] = now()
    event('READBACK_RECONCILIATION_FINISHED')
    (OUT / 'verification_result.json').write_text(json.dumps(state, ensure_ascii=False, indent=2, default=str) + '\n')
