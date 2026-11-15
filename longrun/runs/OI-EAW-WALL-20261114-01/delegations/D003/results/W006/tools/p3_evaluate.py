from pathlib import Path
import errno, json, struct, sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from common import ROOT,guard,fact,save,utc
guard()
obj=json.loads((ROOT/'artifacts/SECCOMP_CANDIDATE_PROGRAM.json').read_bytes())
assert fact(ROOT/'tools/landlock_launcher.py')==obj['candidate_launcher']
baseline=obj['baseline_program'];program=obj['candidate_program'];fioclex=obj['verified_FIOCLEX']
fionclex=json.loads((ROOT/'artifacts/FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json').read_bytes())['symbols']['FIONCLEX']['decimal']
ALLOW=0x7fff0000;DENY=0x50000|errno.EPERM;KILL=0x80000000
def structural(p):
    terminal={};jumps=[]
    for pc in reversed(range(len(p))):
        code,jt,jf,k=p[pc]
        if code==0x06:
            assert jt==jf==0 and k in [ALLOW,DENY,KILL];terminal[pc]=True
        elif code==0x20:
            assert jt==jf==0 and k in [0,4,16,24,28] and pc+1<len(p);terminal[pc]=terminal[pc+1]
        elif code in [0x15,0x45]:
            a=pc+1+jt;b=pc+1+jf
            assert 0<=jt<=255 and 0<=jf<=255 and pc<a<len(p) and pc<b<len(p)
            terminal[pc]=terminal[a] and terminal[b];jumps.append({'pc':pc,'true_target':a,'false_target':b})
        else:raise AssertionError('unmodeled BPF opcode')
        assert terminal[pc]
    return sorted(jumps,key=lambda x:x['pc'])
jumps=structural(program);structural(baseline)
def evaluate(p,nr,arch=0xc000003e,args=(0,0,0,0,0,0)):
    data=struct.pack('<II7Q',nr&0xffffffff,arch,0,*args);assert len(data)==64
    pc=0;acc=0;path=[]
    while True:
        assert 0<=pc<len(p) and len(path)<=len(p)
        path.append(pc);code,jt,jf,k=p[pc]
        if code==0x20:acc=struct.unpack_from('<I',data,k)[0];pc+=1
        elif code==0x15:pc+=1+(jt if acc==k else jf)
        elif code==0x45:pc+=1+(jt if acc&k else jf)
        elif code==0x06:return k,path
        else:raise AssertionError('unmodeled instruction')
spec=[('FIOCLEX',16,0xc000003e,(7,fioclex,0,0,0,0),ALLOW),('FIONCLEX',16,0xc000003e,(7,fionclex,0,0,0,0),DENY),('arbitrary_ioctl',16,0xc000003e,(7,0x1234,0,0,0,0),DENY),('request_high32_same_low',16,0xc000003e,(7,(1<<32)|fioclex,0,0,0,0),DENY),('request_high32_only',16,0xc000003e,(7,1<<32,0,0,0,0),DENY),('socket',41,0xc000003e,(2,1,0,0,0,0),DENY),('ordinary_read',0,0xc000003e,(0,0,0,0,0,0),ALLOW),('x32_FIOCLEX',0x40000010,0xc000003e,(7,fioclex,0,0,0,0),DENY),('wrong_arch',16,0x40000003,(7,fioclex,0,0,0,0),KILL),('PR_SET_NAME',157,0xc000003e,(15,0,0,0,0,0),DENY),('other_prctl',157,0xc000003e,(38,0,0,0,0,0),ALLOW)]
cases=[]
for name,nr,arch,args,expected in spec:
    result,path=evaluate(program,nr,arch,args);assert result==expected
    cases.append({'name':name,'nr':nr,'arch':hex(arch),'args':args,'expected':hex(expected),'actual':hex(result),'PASS':True,'instruction_path':path})
comparisons=0;differences=0
for nr in [*range(601),0x3fffffff,0x40000000,0x40000010,0x7fffffff,0xffffffff]:
    for arch in [0xc000003e,0x40000003]:
        for option in [0,15,38,0x10000000f]:
            for request in [0,fioclex,fionclex,(1<<32)|fioclex,0xffffffffffffffff]:
                args=(option,request,0,0,0,0);old,_=evaluate(baseline,nr,arch,args);new,_=evaluate(program,nr,arch,args)
                if nr==16 and arch==0xc000003e and request==fioclex:
                    assert old==DENY and new==ALLOW;differences+=1
                else:assert old==new
                comparisons+=1
save('artifacts/SECCOMP_FILTER_STATIC_EVALUATION.json',{'phase':'P3','status':'PASS','at':utc(),'evaluator_source':fact(__file__),'candidate_launcher':fact(ROOT/'tools/landlock_launcher.py'),'program_artifact':fact(ROOT/'artifacts/SECCOMP_CANDIDATE_PROGRAM.json'),'mandatory_and_extra_cases':cases,'candidate_jump_targets':jumps,'all_jumps_in_bounds':True,'all_paths_explicit_terminal_action':True,'no_unintended_fallthrough':True,'non_ioctl_semantics_equivalent_to_baseline':True,'only_verified_FIOCLEX_produces_expected_difference':True,'semantic_comparison_cases':comparisons,'expected_FIOCLEX_differences':differences,'comparison_domain':{'syscall_numbers':'0..600 plus 0x3fffffff/0x40000000/0x40000010/0x7fffffff/0xffffffff','architectures':['x86_64','wrong_i386'],'args0_options':[0,15,38,0x10000000f],'requests':[0,fioclex,fionclex,(1<<32)|fioclex,0xffffffffffffffff]},'kernel_filter_install':False,'probe_execution':False})
guard();print(json.dumps({'phase':'P3','status':'PASS','cases':len(cases),'semantic_comparisons':comparisons,'expected_differences':differences,'jump_checks':len(jumps),'kernel_attempts':0}))
