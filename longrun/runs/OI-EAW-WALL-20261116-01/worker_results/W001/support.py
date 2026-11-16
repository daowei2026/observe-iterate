"""W001 调查辅助；所有新增文件限于本目录。"""
import datetime
import errno
import fcntl
import hashlib
import json
import os
import pathlib
import sys

BASE = pathlib.Path('/dwdhome/fy/BASE_E6_2')
OUT = BASE / '.runtime/observe-iterate/OI-EAW-WALL-20261116-01/D001/W001'
LOCK = OUT.parent / '.single-writer.lock'

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def sha(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()

def lease():
    pid = 296712
    line = pathlib.Path('/proc/%d/stat' % pid).read_text()
    parts = line[line.rfind(')') + 2:].split()
    result = dict(checked_at_utc=now(), pid=pid, state=parts[0],
                  start_ticks=int(parts[19]), inode=LOCK.stat().st_ino)
    if result['state'] == 'Z' or result['start_ticks'] != 58333981 or result['inode'] != 13765718:
        raise RuntimeError('STOP: lease identity mismatch: %r' % result)
    fd = os.open(str(LOCK), os.O_RDWR)
    try:
        if os.fstat(fd).st_ino != 13765718:
            raise RuntimeError('STOP: lease inode changed')
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as e:
            if e.errno not in (errno.EAGAIN, errno.EACCES):
                raise
            result.update(competing_flock='REFUSED', errno=e.errno)
        else:
            fcntl.flock(fd, fcntl.LOCK_UN)
            raise RuntimeError('STOP: competing flock unexpectedly acquired')
    finally:
        os.close(fd)
    result['kernel_locks'] = [s.strip() for s in pathlib.Path('/proc/locks').read_text().splitlines()
                              if s.split()[4:5] == [str(pid)] and s.split()[5].endswith(':13765718')]
    return result

def write_json(name, value):
    p = OUT / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2, default=str) + '\n')

def readonly_audit(events, allow_git=False, read_prefixes=()):
    """额外保护正式文件；不用于代替事前源码证明。"""
    def allowed(path):
        if isinstance(path, int):
            return True
        p = pathlib.Path(os.fsdecode(path)).resolve()
        # dill 在导入时用空设备探测文件类型；不形成持久文件写入。
        if p == pathlib.Path('/dev/null'):
            return True
        return p == OUT or OUT in p.parents
    def audit(event, args):
        if event == 'open':
            p, mode, flags = args
            if flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND):
                if not allowed(p):
                    events.append(dict(event=event, path=str(p), decision='DENIED_WRITE'))
                    raise PermissionError('W001 prohibits write outside output: %s' % p)
            elif not isinstance(p,int) and any(str(p).startswith(str(prefix) + '/') for prefix in read_prefixes):
                item=dict(event=event,path=str(p),mode=mode,flags=flags,decision='READ_ONLY')
                try:
                    st=pathlib.Path(p).stat()
                    item.update(size_before=st.st_size,mtime_ns_before=st.st_mtime_ns,inode_before=st.st_ino)
                except FileNotFoundError:
                    item['exists_before']=False
                events.append(item)
        elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.chmod', 'os.utime', 'os.truncate'):
            if event == 'os.mkdir' and pathlib.Path(args[0]).is_dir():
                return  # 已存目录的 mkdir 只能返回 EEXIST，不能产生落盘变化。
            if not allowed(args[0]):
                events.append(dict(event=event, path=str(args[0]), decision='DENIED_MUTATION'))
                raise PermissionError('W001 prohibits mutation outside output: %s' % args[0])
        elif event in ('os.rename', 'os.link', 'os.symlink'):
            if not all(allowed(p) for p in args[:2]):
                raise PermissionError('W001 prohibits cross-boundary mutation')
        elif event == 'subprocess.Popen':
            command = args[1]
            executable = pathlib.Path(str(args[0])).name
            permit = executable in ('uname', 'hostname', 'which', 'getconf')
            if allow_git and executable == 'git' and isinstance(command, (list, tuple)):
                permit = any(x in command for x in ('rev-parse', 'status', 'diff', 'show', 'ls-files', 'cat-file'))
            events.append(dict(event=event, command=command, decision='ALLOWED_READONLY' if permit else 'DENIED_SUBPROCESS'))
            if not permit:
                raise PermissionError('W001 prohibits unproved subprocess: %r' % command)
    sys.addaudithook(audit)

