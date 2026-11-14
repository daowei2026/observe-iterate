from pathlib import Path
import sys,re,json,collections
ROOT=Path('/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W003');sys.path.insert(0,str(ROOT/'tools'));import runtime as w
w.guard();paths=sorted((ROOT/'trace').glob('r0a-positive.*'));assert len(paths)==1
hist=collections.Counter();writes=[];writeopens=[];sharedmaps=[];unknown=[];mutations=[];ipc=[];network=[];proccomm=[];files=[];unparsed=[];descriptor_names={'write','writev','pwrite64','pwritev','pwritev2','sendfile','copy_file_range','splice','vmsplice','tee'};mutation_names={'truncate','ftruncate','rename','renameat','renameat2','link','linkat','symlink','symlinkat','unlink','unlinkat','rmdir','mkdir','mkdirat','mknod','mknodat','chmod','fchmod','fchmodat','fchmodat2','chown','fchown','lchown','fchownat','utime','utimes','futimesat','utimensat','setxattr','lsetxattr','fsetxattr','removexattr','lremovexattr','fremovexattr','msync','fallocate'}
for p in paths:
 lines=p.read_text().splitlines();files.append({**w.filefact(p),'lines':len(lines),'normal_terminal_record':lines[-1].endswith('+++ exited with 73 +++')})
 for number,line in enumerate(lines,1):
  m=re.match(r'^[\d.]+\s+(\w+)\((.*)\)\s+=\s+(.*)$',line)
  if not m:
   if '+++ exited with ' not in line:unparsed.append({'file':str(p),'line':number,'raw':line})
   continue
  name,args,ret=m.groups();hist[name]+=1
  match=re.match(r'(-?(?:0x[0-9a-f]+|\d+))',ret);value=int(match.group(1),0) if match else None;success=value is not None and value>=0
  ev={'file':str(p),'line':number,'syscall':name,'return_text':ret,'raw':line}
  if name in descriptor_names and success:
   pathmatch=re.match(r'\d+<([^>]+)>',args);dest=pathmatch.group(1) if pathmatch else None;inside=bool(dest and Path(dest).is_absolute() and Path(dest).is_relative_to(ROOT));event={**ev,'destination':dest,'return_value':value,'inside_WORK_ROOT':inside};writes.append(event)
   if dest is None:unknown.append(event)
  if name in {'open','openat','openat2','creat'} and success and any(flag in args for flag in ['O_WRONLY','O_RDWR','O_CREAT','O_TRUNC']):
   d=re.search(r'^\d+<([^>]+)>',ret);dest=d.group(1) if d else None;event={**ev,'destination':dest,'inside_WORK_ROOT':bool(dest and Path(dest).is_relative_to(ROOT))};writeopens.append(event)
   if dest is None:unknown.append(event)
  if name in mutation_names:mutations.append({**ev,'success':success})
  if name=='mmap' and 'MAP_SHARED' in args:sharedmaps.append({**ev,'success':success,'PROT_WRITE':'PROT_WRITE' in args})
  if name in {'shmget','shmat','shmdt','shmctl'}:ipc.append({**ev,'success':success})
  if name in {'socket','connect','accept','bind','listen','sendto','sendmsg','recvfrom','recvmsg','socketpair'}:network.append(ev)
  if '/comm' in args and '/proc/' in args:proccomm.append(ev)
assert not unparsed and len(writes)==1 and not unknown and all(x['inside_WORK_ROOT'] for x in writes+writeopens)
assert not any(x['success'] and x['PROT_WRITE'] for x in sharedmaps)
assert all(x['normal_terminal_record'] for x in files)
result={'record_type':'W003_FULL_WRITE_TRACE_REVIEW','utc':w.utc(),'status':'COMPLETE_FOR_FAILED_LAUNCHER_ONLY','R0A_WRITE_CONFINEMENT_PASS':False,'trace_scope':'One attempted launcher PID241337, from execve through exit73. The probe was never execed; no descendants. Parent/control and native platform are not kernel-confined by this trace.','configuration':{'absolute_tool':'/usr/bin/strace','flags':['--kill-on-exit','-ff','-yy','-ttt','-s','128','-e','trace=all'],'raw_read_payloads':'read/pread64/readv/preadv/preadv2/recvfrom/recvmsg/recvmmsg payloads rendered raw to avoid copying data; calls retained; write-family remains decoded with FD path','open_write_payload_truncation':'-s128 limits displayed byte buffer only, not actual return count, FD path or syscall coverage'},'files':files,'syscall_histogram':dict(hist),'unparsed_records':unparsed,'successful_descriptor_writes':writes,'successful_descriptor_write_count':len(writes),'successful_descriptor_write_bytes':sum(x['return_value'] for x in writes),'successful_descriptor_writes_with_unknown_destination':unknown,'successful_outside_descriptor_writes_in_this_trace':sum(not x['inside_WORK_ROOT'] for x in writes),'successful_writable_or_creating_opens':writeopens,'other_mutation_syscalls':mutations,'shared_mappings':sharedmaps,'sysv_ipc':ipc,'sysv_ipc_note':'Startup IPC_CREAT|IPC_EXCL returned EEXIST; existing shmid0 obtained and attached SHM_RDONLY, then detached. No successful IPC object creation or writable shared mapping observed.','network_syscalls_observed':network,'proc_comm_records':proccomm,'proc_comm_status':'NO_OPEN_OR_ACTUAL_WRITE_OBSERVED_IN_THIS_ATTEMPT','inherited_fd0':{'path':'/dev/null','observed_flags':'O_RDWR|O_LARGEFILE','actual_write_observed':False,'trace_line':1055,'effect':'Launcher rejected writable stdin before Landlock or child exec.'},'inherited_lock_fd3':{'path':str(w.LOCK),'origin':'Controller lock path opened on a separate competing open file description; failed LOCK_EX|LOCK_NB before launch; passed FD number3; parent finally closed its own FD only.','holder_lock_modified':False,'launcher_enumeration_completed':False},'kernel_policy_install_syscalls_observed':0,'global_or_future_zero_outside_write_proof':False,'conclusion_zh':'这份完整 trace 可回溯本次失败 launcher 的唯一成功 write 到 W003 receipt；不能据此证明 confinement、未执行探针或后继命令零外写。'}
w.save('artifacts/FULL_WRITE_TRACE_REVIEW.json',result);w.guard();print(json.dumps({'trace_files':len(files),'lines':sum(x['lines'] for x in files),'successful_writes':len(writes),'bytes':sum(x['return_value'] for x in writes),'observed_outside_writes':0,'unknown_write_paths':len(unknown),'R0A_PASS':False},ensure_ascii=False))
