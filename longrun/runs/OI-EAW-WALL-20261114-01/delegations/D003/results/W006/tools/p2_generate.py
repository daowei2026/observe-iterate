from pathlib import Path
import ast, copy, difflib, errno, json, re, sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from common import ROOT,binding,fact,guard,save,utc
guard()
for n in ['HISTORICAL_FIOCLEX_PHASE_CLASSIFICATION.json','FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json','SECCOMP_DATA_LAYOUT_VERIFICATION.json']:
    assert json.loads((ROOT/'artifacts'/n).read_bytes())['status']=='PASS'
constant=json.loads((ROOT/'artifacts/FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json').read_bytes())['symbols']['FIOCLEX']['decimal']
original=ROOT.parent/'W004/tools/landlock_launcher.py';old=original.read_text()
assert fact(original)['sha256']=='8f12bc66a0318f5394193331c07bf1cdd583711c232b6f1ab180ebae549c7002'
old_loop='for nr in sorted(set(denied.values())):program.extend([(0x15,0,1,nr),(0x06,0,0,RET_ERRNO)])'
assert old.count(old_loop)==1
branch=[(0x15,0,6,16),(0x20,0,0,28),(0x15,0,3,0),(0x20,0,0,24),(0x15,0,1,constant),(0x06,0,0,0x7fff0000),(0x06,0,0,0x50000|errno.EPERM)]
replacement='program.extend('+repr(branch)+')\n for nr in sorted(set(denied.values())-{16}):program.extend([(0x15,0,1,nr),(0x06,0,0,RET_ERRNO)])'
new=old.replace('W004_LANDLOCK_AND_SECCOMP_LAUNCHER','W006_LANDLOCK_AND_SECCOMP_LAUNCHER').replace(old_loop,replacement)
ast.parse(new)
launcher=ROOT/'tools/landlock_launcher.py'
with launcher.open('x') as f:f.write(new)

def literal(expression,variables):
    class Names(ast.NodeTransformer):
        def visit_Name(self,node):
            assert node.id in variables
            return ast.copy_location(ast.Constant(variables[node.id]),node)
    return ast.literal_eval(Names().visit(copy.deepcopy(expression)))
def extract(source,candidate):
    tree=ast.parse(source)
    denied=next(ast.literal_eval(n.value) for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='denied' for t in n.targets))
    init=next(n.value for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='program' for t in n.targets))
    p=literal(init,{'RET_ERRNO':0x50000|errno.EPERM})
    loop=next(n for n in ast.walk(tree) if isinstance(n,ast.For) and isinstance(n.target,ast.Name) and n.target.id=='nr')
    additions=sorted([n for n in ast.walk(tree) if isinstance(n,ast.Expr) and isinstance(n.value,ast.Call) and isinstance(n.value.func,ast.Attribute) and isinstance(n.value.func.value,ast.Name) and n.value.func.value.id=='program' and n.value.func.attr=='extend'],key=lambda n:n.lineno)
    for n in additions:
        if loop.lineno<=n.lineno<=loop.end_lineno:
            for nr in sorted(set(denied.values())-({16} if candidate else set())):p.extend(literal(n.value.args[0],{'nr':nr,'RET_ERRNO':0x50000|errno.EPERM}))
        else:p.extend(literal(n.value.args[0],{'RET_ERRNO':0x50000|errno.EPERM}))
    return denied,[tuple(x) for x in p]

old_denied,baseline=extract(old,False);new_denied,candidate=extract(new,True)
assert old_denied==new_denied
assert candidate[:6]==baseline[:6] and candidate[6:13]==branch and candidate[-5:]==baseline[-5:]
assert candidate[13:-5]==[i for nr in sorted(set(old_denied.values())-{16}) for i in [(0x15,0,1,nr),(0x06,0,0,0x50000|errno.EPERM)]]
def annotation(p):
    rows=[]
    for pc,(code,jt,jf,k) in enumerate(p):
        row={'pc':pc,'code':code,'jt':jt,'jf':jf,'k':k,'k_hex':hex(k)}
        if code in [0x15,0x45]:row.update(true_target=pc+1+jt,false_target=pc+1+jf)
        if code==0x20:row['seccomp_data_offset']=k
        if code==0x06:row['terminal_action']=hex(k)
        rows.append(row)
    return rows
save('artifacts/SECCOMP_CANDIDATE_PROGRAM.json',{'phase':'P2','baseline_program':baseline,'candidate_program':candidate,'candidate_launcher':fact(launcher),'verified_FIOCLEX':constant,'baseline_launcher':fact(original)})
scans=[]
for name in ['common.py','runtime.py','landlock_launcher.py']:
    p=ROOT/'tools'/name;s=p.read_text();tree=ast.parse(s)
    strings=sorted(set(n.value for n in ast.walk(tree) if isinstance(n,ast.Constant) and isinstance(n.value,str)))
    numbers=sorted(set(n.value for n in ast.walk(tree) if isinstance(n,ast.Constant) and type(n.value) is int))
    forbidden_hits=re.findall(r'/D003/W00[45](?:\b|/)|(?<!\d)(?:243622|47124402|246047|47679582)(?!\d)',s)
    assert not forbidden_hits
    scans.append({'source':fact(p),'hard_coded_absolute_path_literals':[x for x in strings if x.startswith('/')],'integer_literals':numbers,'old_root_PID_startticks_hits':forbidden_hits})
b=binding()
save('artifacts/PARENT_RUNTIME_BINDING_DELTA.json',{'phase':'P2','status':'PASS_STATIC_BINDING','at':utc(),'actual_root':b['write_root'],'actual_lock':b['fresh_lock'],'binding_source':fact(ROOT/'artifacts/W006_BINDING.json'),'new_runtime':fact(ROOT/'tools/runtime.py'),'common_guard':fact(ROOT/'tools/common.py'),'binding_values_loaded_from_fresh_W006_JSON':True,'static_scans_before_any_runtime_child_start':scans,'old_binding_hard_coded_values_present':False,'parent_stdin':'explicit os.open /dev/null O_RDONLY|O_CLOEXEC; F_GETFL O_ACCMODE assertion; close only parent copy','launcher_stdin_and_inherited_FD_and_stdio_guards':'unchanged relative to frozen W004 launcher','actual_child_start':False})
save('artifacts/SECCOMP_IOCTL_FILTER_DELTA.json',{'phase':'P2','status':'PASS_GENERATION_ONLY_PENDING_P3','at':utc(),'baseline_launcher':fact(original),'candidate_launcher':fact(launcher),'source_unified_diff':list(difflib.unified_diff(old.splitlines(),new.splitlines(),fromfile='W004_frozen_reference',tofile='W006_new_candidate',lineterm='')),'baseline_instructions':annotation(baseline),'candidate_instructions':annotation(candidate),'only_semantic_delta':'ioctl16 args[1].high32==0 and low32==local FIOCLEX allows; otherwise EPERM','little_endian_offsets':{'nr':0,'arch':4,'args0_low32':16,'args1_low32':24,'args1_high32':28},'denied_syscall_map_unchanged':new_denied,'arch_x32_prctl_prefix_suffix_unchanged':True,'all_other_Landlock_network_metadata_FD_stdin_source_unchanged':True,'handled_IOCTL_DEV_unchanged':True,'kernel_installed':False})
guard();print(json.dumps({'phase':'P2','status':'PASS','baseline_instructions':len(baseline),'candidate_instructions':len(candidate),'fresh_binding_scanned_files':len(scans),'kernel_attempts':0}))
