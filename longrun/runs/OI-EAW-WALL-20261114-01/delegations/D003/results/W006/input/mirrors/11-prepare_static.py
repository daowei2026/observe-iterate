from pathlib import Path
import ast, ctypes, difflib, errno, hashlib, json, os, re, struct, sys, termios

ROOT=Path('/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W005')
OLD=ROOT.parent/'W004'
assert Path.cwd()==Path('/dwdhome/fy/BASE_E6_2') and sys.dont_write_bytecode
assert os.environ['HOME']=='/home/dw' and os.environ['CODEX_HOME']=='/home/dw/.codex'

def fact(p):
    p=Path(p); b=p.read_bytes()
    return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

def save(name, value):
    with (ROOT/name).open('x') as f: f.write(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

# Two independent authoritative local representations; no compiler or kernel call.
header=Path('/usr/include/asm-generic/ioctls.h')
archheader=Path('/usr/include/x86_64-linux-gnu/asm/ioctls.h')
definitions={name:int(re.search(r'^#define\s+'+name+r'\s+(0x[0-9a-fA-F]+)\b',header.read_text(),re.M).group(1),16) for name in ['FIOCLEX','FIONCLEX']}
assert '<asm-generic/ioctls.h>' in archheader.read_text()
assert os.uname().machine=='x86_64' and sys.byteorder=='little'
assert definitions=={'FIOCLEX':termios.FIOCLEX,'FIONCLEX':termios.FIONCLEX}
seccomp_header=Path('/usr/include/linux/seccomp.h')
header_struct=re.search(r'struct seccomp_data\s*\{(.*?)\};',seccomp_header.read_text(),re.S).group(1)
assert re.search(r'int\s+nr\s*;',header_struct) and re.search(r'__u32\s+arch\s*;',header_struct)
assert re.search(r'__u64\s+instruction_pointer\s*;',header_struct) and re.search(r'__u64\s+args\[6\]\s*;',header_struct)
class SeccompData(ctypes.Structure):
    _fields_=[('nr',ctypes.c_int32),('arch',ctypes.c_uint32),('instruction_pointer',ctypes.c_uint64),('args',ctypes.c_uint64*6)]
assert ctypes.sizeof(SeccompData)==64 and SeccompData.nr.offset==0 and SeccompData.arch.offset==4 and SeccompData.args.offset==16
trace=(OLD/'trace/r0a1.244050').read_text()
trace_lines=[{'line':i+1,'text':s} for i,s in enumerate(trace.splitlines()) if 'ioctl(' in s and 'FIOCLEX' in s]
assert trace_lines and all('EPERM' in x['text'] for x in trace_lines)
constant={'status':'PASS','symbol':'FIOCLEX','integer_decimal':termios.FIOCLEX,'integer_hex':hex(termios.FIOCLEX),'FIONCLEX':termios.FIONCLEX,'architecture':os.uname().machine,'endianness':sys.byteorder,'local_sources':[dict(fact(termios.__file__),module='termios',value=termios.FIOCLEX),dict(fact(header),definition='#define FIOCLEX 0x5451',value=definitions['FIOCLEX']),dict(fact(archheader),include='<asm-generic/ioctls.h>')],'agreement':True,'trace_third_cross_source':dict(fact(OLD/'trace/r0a1.244050'),matches=trace_lines),'kernel_or_probe_executed':False}
save('artifacts/FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json',constant)

old_runtime=(OLD/'tools/runtime.py').read_text()
runtime=old_runtime.replace('/D003/W004','/D003/W005').replace('243622','246047').replace('47124402','47679582')
assert runtime!=old_runtime and 'O_RDONLY|os.O_CLOEXEC' in runtime
with (ROOT/'tools/runtime.py').open('x') as f:f.write(runtime)

old=(OLD/'tools/landlock_launcher.py').read_text()
assert fact(OLD/'tools/landlock_launcher.py')['sha256']=='8f12bc66a0318f5394193331c07bf1cdd583711c232b6f1ab180ebae549c7002'
old_loop='for nr in sorted(set(denied.values())):program.extend([(0x15,0,1,nr),(0x06,0,0,RET_ERRNO)])'
assert old.count(old_loop)==1
request_branch=(
    '# W005: the only policy delta is one locally verified request.\n'
    '# seccomp_data.args[1]: little-endian low32 offset24, high32 offset28.\n'
    ' program.extend([(0x15,0,6,16),(0x20,0,0,28),(0x15,0,3,0),(0x20,0,0,24),(0x15,0,1,'+str(termios.FIOCLEX)+'),(0x06,0,0,0x7fff0000),(0x06,0,0,RET_ERRNO)])\n'
    ' for nr in sorted(set(denied.values())-{16}):program.extend([(0x15,0,1,nr),(0x06,0,0,RET_ERRNO)])')
new=old.replace('W004_LANDLOCK_AND_SECCOMP_LAUNCHER','W005_LANDLOCK_AND_SECCOMP_LAUNCHER').replace(old_loop,request_branch)
assert new!=old
ast.parse(new)
with (ROOT/'tools/landlock_launcher.py').open('x') as f:f.write(new)

# Extract only literal BPF construction expressions from AST, never import/execute launcher.
def extract(source, candidate):
    tree=ast.parse(source)
    denied=next(ast.literal_eval(n.value) for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='denied' for t in n.targets))
    def val(node, **local):return eval(compile(ast.Expression(node),'<BPF-literal-expression>','eval'),{'__builtins__':{}},{'RET_ERRNO':0x50000|errno.EPERM,**local})
    assign=next(n for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='program' for t in n.targets))
    p=val(assign.value)
    loop=next(n for n in ast.walk(tree) if isinstance(n,ast.For) and isinstance(n.target,ast.Name) and n.target.id=='nr')
    exprs=sorted([n for n in ast.walk(tree) if isinstance(n,ast.Expr) and isinstance(n.value,ast.Call) and isinstance(n.value.func,ast.Attribute) and isinstance(n.value.func.value,ast.Name) and n.value.func.value.id=='program' and n.value.func.attr=='extend'],key=lambda n:n.lineno)
    for n in exprs:
        if loop.lineno<=n.lineno<=loop.end_lineno:
            for nr in sorted(set(denied.values())-({16} if candidate else set())):p.extend(val(n.value.args[0],nr=nr))
        else:p.extend(val(n.value.args[0]))
    return denied,[tuple(i) for i in p]

old_denied,baseline=extract(old,False)
new_denied,program=extract(new,True)
assert old_denied==new_denied
expected_branch=[(0x15,0,6,16),(0x20,0,0,28),(0x15,0,3,0),(0x20,0,0,24),(0x15,0,1,termios.FIOCLEX),(0x06,0,0,0x7fff0000),(0x06,0,0,0x50000|errno.EPERM)]
assert program[:6]==baseline[:6] and program[6:13]==expected_branch and program[-5:]==baseline[-5:]
assert program[13:-5]==[ins for nr in sorted(set(old_denied.values())-{16}) for ins in [(0x15,0,1,nr),(0x06,0,0,0x50000|errno.EPERM)]]

def annotated(p):
    out=[]
    for pc,(code,jt,jf,k) in enumerate(p):
        d={'pc':pc,'code':code,'jt':jt,'jf':jf,'k':k,'hex_k':hex(k)}
        if code in (0x15,0x45):
            d.update(true_target=pc+1+jt,false_target=pc+1+jf)
            assert 0<=jt<=255 and 0<=jf<=255 and pc<d['true_target']<len(p) and pc<d['false_target']<len(p)
        elif code==0x20:assert jt==jf==0 and k in [0,4,16,24,28] and pc+1<len(p)
        elif code==0x06:assert jt==jf==0 and k in [0x7fff0000,0x50000|errno.EPERM,0x80000000]
        else:raise AssertionError('unmodeled opcode')
        out.append(d)
    # Every branch, including branches not used by mandatory examples, terminates.
    terminal={}
    for pc in reversed(range(len(p))):
        code,jt,jf,k=p[pc]
        terminal[pc]=True if code==0x06 else (terminal[pc+1] if code==0x20 else terminal[pc+1+jt] and terminal[pc+1+jf])
        assert terminal[pc]
    return out

annotations=annotated(program);old_annotations=annotated(baseline)
def evaluate(p,nr,arch=0xc000003e,args=(0,0,0,0,0,0)):
    raw=struct.pack('<II7Q',nr&0xffffffff,arch,0,*args);assert len(raw)==64
    pc=0;acc=0;steps=[]
    while True:
        assert 0<=pc<len(p) and len(steps)<=len(p)
        steps.append(pc);code,jt,jf,k=p[pc]
        if code==0x20:acc=struct.unpack_from('<I',raw,k)[0];pc+=1
        elif code==0x15:pc+=1+(jt if acc==k else jf)
        elif code==0x45:pc+=1+(jt if acc&k else jf)
        elif code==0x06:return k,steps
        else:raise AssertionError(code)

ALLOW=0x7fff0000;ERRNO=0x50000|errno.EPERM;KILL=0x80000000
specs=[('FIOCLEX',16,0xc000003e,(7,termios.FIOCLEX,0,0,0,0),ALLOW),('FIONCLEX',16,0xc000003e,(7,termios.FIONCLEX,0,0,0,0),ERRNO),('arbitrary_ioctl',16,0xc000003e,(7,0x1234,0,0,0,0),ERRNO),('high32_same_low',16,0xc000003e,(7,(1<<32)|termios.FIOCLEX,0,0,0,0),ERRNO),('high32_only',16,0xc000003e,(7,1<<32,0,0,0,0),ERRNO),('socket',41,0xc000003e,(2,1,0,0,0,0),ERRNO),('ordinary_read',0,0xc000003e,(0,0,0,0,0,0),ALLOW),('x32_FIOCLEX',0x40000010,0xc000003e,(7,termios.FIOCLEX,0,0,0,0),ERRNO),('wrong_arch',16,0x40000003,(7,termios.FIOCLEX,0,0,0,0),KILL),('PR_SET_NAME',157,0xc000003e,(15,0,0,0,0,0),ERRNO),('other_prctl',157,0xc000003e,(38,0,0,0,0,0),ALLOW)]
cases=[]
for name,nr,arch,args,expected in specs:
    actual,path=evaluate(program,nr,arch,args);assert actual==expected
    cases.append({'case':name,'nr':nr,'arch':hex(arch),'args':args,'expected':hex(expected),'actual':hex(actual),'PASS':True,'pc_path':path})
equiv=0
for nr in [*range(601),0x3fffffff,0x40000000,0x40000010,0x7fffffff,0xffffffff]:
    for arch in [0xc000003e,0x40000003]:
        for arg0 in [0,15,38,0x10000000f]:
            for request in [0,termios.FIOCLEX,termios.FIONCLEX,(1<<32)|termios.FIOCLEX,0xffffffffffffffff]:
                args=(arg0,request,0,0,0,0)
                old_result,_=evaluate(baseline,nr,arch,args);new_result,_=evaluate(program,nr,arch,args)
                expected_difference=(nr==16 and arch==0xc000003e and request==termios.FIOCLEX)
                assert (old_result==ERRNO and new_result==ALLOW) if expected_difference else old_result==new_result
                equiv+=1
save('artifacts/SECCOMP_IOCTL_FILTER_DELTA.json',{'status':'PASS_STATIC_ONLY','constant_evidence':'FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json','old_launcher':fact(OLD/'tools/landlock_launcher.py'),'new_launcher':fact(ROOT/'tools/landlock_launcher.py'),'source_unified_diff':list(difflib.unified_diff(old.splitlines(),new.splitlines(),fromfile='W004_READONLY',tofile='W005_NEW',lineterm='')),'only_semantic_delta':'syscall16: request upper32==0 and lower32==locally verified FIOCLEX => ALLOW; all other ioctl => EPERM','endianness':'little','seccomp_data_layout':{'nr':0,'arch':4,'instruction_pointer':8,'args0_low32':16,'args1_low32':24,'args1_high32':28,'bytes':64},'baseline_instructions':old_annotations,'candidate_instructions':annotations,'denied_syscalls_map_unchanged':new_denied,'arch_x32_prctl_suffix_unchanged':True,'landlock_and_fd_and_stdin_code_unchanged':True,'IOCTL_DEV_handled_right_unchanged':True,'non_ioctl_semantic_comparisons':equiv})
save('artifacts/SECCOMP_FILTER_STATIC_EVALUATION.json',{'status':'PASS','kernel_install':False,'probe_execution':False,'evaluator_source':fact(__file__),'candidate_launcher':fact(ROOT/'tools/landlock_launcher.py'),'mandatory_and_extra_cases':cases,'semantic_comparison_cases':equiv,'all_jump_targets_in_program':True,'all_paths_terminate_in_explicit_action':True,'no_unmodeled_opcode_or_fallthrough':True,'instruction_count':len(program),'BPF_data_offsets_verified_from_local_layout':True,'local_layout_source':dict(fact(seccomp_header),declaration=header_struct),'native_ctypes_layout':{'size':ctypes.sizeof(SeccompData),'nr':SeccompData.nr.offset,'arch':SeccompData.arch.offset,'args':SeccompData.args.offset}})
print(json.dumps({'constant':termios.FIOCLEX,'hex':hex(termios.FIOCLEX),'static_status':'PASS','cases':len(cases),'semantic_comparisons':equiv,'instructions':len(program),'kernel_install':False}))
