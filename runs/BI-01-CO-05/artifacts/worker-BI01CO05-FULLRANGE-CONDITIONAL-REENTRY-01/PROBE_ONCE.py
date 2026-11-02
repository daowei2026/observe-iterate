"""一次精确日历读取；只记录事实，不复制文件或替代输入。"""
import datetime
import hashlib
import json
import os
from pathlib import Path
import pwd
import re
import sys
import traceback

TARGET = '/m3varI/var/L1_data/sof/unit/affiliated_calendar_no_night.csv'

def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def identity():
    return dict(uid=os.getuid(), euid=os.geteuid(), gid=os.getgid(),
                egid=os.getegid(), groups=os.getgroups(),
                username=pwd.getpwuid(os.getuid()).pw_name)

def unescape(value):
    return re.sub(r'\\([0-7]{3})', lambda m: chr(int(m.group(1), 8)), value)

def main():
    setup = json.loads(Path(sys.argv[1]).read_text())
    out = Path(setup['delivery_dir'])
    record = dict(order_id=setup['order_id'], worker_execution_id=setup['worker_execution_id'],
                  start_utc=utc(), end_utc=None, cwd=os.getcwd(), identity=identity(),
                  executable=sys.executable, python_version=sys.version,
                  thread_id=os.environ.get('CODEX_THREAD_ID'), exact_open_path=TARGET,
                  realpath=None, realpath_source='kernel /proc/self/fd link after successful open',
                  open_attempt_count=0, successful_open_count=0, read_call_count=0,
                  bytes_read=0, reached_eof=False, fstat_size_before=None,
                  fstat_size_after=None, sha256=None, exception_type=None,
                  errno=None, filename=None, traceback=None, exit_code=None,
                  no_stale_copy=True, no_alternate_source=True, no_resolver_bypass=True,
                  no_privilege_switch=True, passed=False, state='PREPARING')
    mount_rows = []
    for line in Path('/proc/self/mountinfo').read_text().splitlines():
        left, right = line.split(' - ', 1)
        a, b = left.split(), right.split()
        point = unescape(a[4])
        if TARGET == point or TARGET.startswith(point.rstrip('/') + '/'):
            mount_rows.append(dict(mount_point=point, fs_type=b[0], source=unescape(b[1]),
                                   mount_root=unescape(a[3]), mountinfo_line=line))
    mount = max(mount_rows, key=lambda r: len(r['mount_point'])) if mount_rows else None
    record['effective_mount'] = mount
    record['findmnt_T_equivalent'] = dict(method='longest path-component mount point match from /proc/self/mountinfo',
                                           target=TARGET, result=mount)
    mount_id = dict(identity=record['identity'], cwd=record['cwd'],
                    executable=sys.executable, python_version=sys.version,
                    thread_id=record['thread_id'], effective_mount=mount,
                    findmnt_T_equivalent=record['findmnt_T_equivalent'])
    (out / 'MOUNT_AND_IDENTITY.json').write_text(json.dumps(mount_id, indent=2) + '\n')
    receipt_path = out / 'PROBE_RECEIPT.json'
    receipt_path.write_text(json.dumps(record, indent=2) + '\n')
    try:
        assert record['identity'] == setup['expected_identity'], 'launcher identity differs from Worker'
        assert record['thread_id'] == setup['thread_id'], 'thread identity mismatch'
        assert record['cwd'] == setup['business_cwd'], 'business cwd mismatch'
        assert sys.executable == setup['expected_python'], 'business Python mismatch'
        assert sys.version.split()[0] == setup['expected_python_version'], 'business Python version mismatch'
        assert mount is not None, 'effective mount not exposed'
        assert all(mount[k] == v for k, v in setup['expected_mount'].items()), 'effective mount identity mismatch'
        record['state'] = 'OPEN_READ_IN_PROGRESS'
        record['open_attempt_count'] = 1
        receipt_path.write_text(json.dumps(record, indent=2) + '\n')
        digest = hashlib.sha256()
        with open(TARGET, 'rb', buffering=0) as handle:
            record['successful_open_count'] = 1
            record['realpath'] = os.readlink('/proc/self/fd/' + str(handle.fileno()))
            record['fstat_size_before'] = os.fstat(handle.fileno()).st_size
            while True:
                record['read_call_count'] += 1
                chunk = handle.read(1024 * 1024)
                if not chunk:
                    record['reached_eof'] = True
                    break
                record['bytes_read'] += len(chunk)
                digest.update(chunk)
            record['fstat_size_after'] = os.fstat(handle.fileno()).st_size
            record['sha256'] = digest.hexdigest()
        assert record['reached_eof'], 'EOF not reached'
        assert record['bytes_read'] > 0, 'empty source file'
        assert record['bytes_read'] == record['fstat_size_before'] == record['fstat_size_after'], 'source size changed or incomplete read'
        record.update(passed=True, state='PASS', exit_code=0)
    except BaseException as exc:
        record.update(exception_type=type(exc).__name__, errno=getattr(exc, 'errno', None),
                      filename=getattr(exc, 'filename', None), traceback=traceback.format_exc(),
                      passed=False, state='FAILED', exit_code=1)
        traceback.print_exc(file=sys.stderr)
    record['end_utc'] = utc()
    receipt_path.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps(record, ensure_ascii=False, indent=2), flush=True)
    return record['exit_code']

if __name__ == '__main__':
    raise SystemExit(main())
