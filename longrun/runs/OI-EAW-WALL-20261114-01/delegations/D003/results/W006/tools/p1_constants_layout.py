from pathlib import Path
import ctypes, json, os, re, sys, termios
sys.path.insert(0,str(Path(__file__).resolve().parent))
from common import ROOT,guard,fact,save,utc
guard()
assert json.loads((ROOT/'artifacts/HISTORICAL_FIOCLEX_PHASE_CLASSIFICATION.json').read_bytes())['status']=='PASS'
header=Path('/usr/include/asm-generic/ioctls.h');archheader=Path('/usr/include/x86_64-linux-gnu/asm/ioctls.h')
defs={name:int(re.search(r'^#define\s+'+name+r'\s+(0x[0-9A-Fa-f]+)\b',header.read_text(),re.M).group(1),16) for name in ['FIOCLEX','FIONCLEX']}
assert '<asm-generic/ioctls.h>' in archheader.read_text()
assert defs=={'FIOCLEX':termios.FIOCLEX,'FIONCLEX':termios.FIONCLEX}
assert os.uname().machine=='x86_64' and sys.byteorder=='little'
save('artifacts/FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json',{'phase':'P1','status':'PASS','at':utc(),'architecture':os.uname().machine,'endianness':sys.byteorder,'symbols':{n:{'decimal':v,'hex':hex(v)} for n,v in defs.items()},'local_sources':[dict(fact(termios.__file__),module='termios',values=defs),dict(fact(header),definitions={n:re.search(r'^#define\s+'+n+r'\s+.*$',header.read_text(),re.M).group(0) for n in defs}),dict(fact(archheader),includes='<asm-generic/ioctls.h>')],'local_definitions_agree':True,'expected_0x5451_is_reference_only':True,'kernel_or_filter_install':False})
sec=Path('/usr/include/linux/seccomp.h');decl=re.search(r'struct seccomp_data\s*\{(.*?)\};',sec.read_text(),re.S).group(1)
assert re.search(r'int\s+nr\s*;',decl) and re.search(r'__u32\s+arch\s*;',decl) and re.search(r'__u64\s+instruction_pointer\s*;',decl) and re.search(r'__u64\s+args\[6\]\s*;',decl)
class Data(ctypes.Structure):_fields_=[('nr',ctypes.c_int32),('arch',ctypes.c_uint32),('instruction_pointer',ctypes.c_uint64),('args',ctypes.c_uint64*6)]
offsets={name:getattr(Data,name).offset for name in ['nr','arch','instruction_pointer','args']}
assert ctypes.sizeof(Data)==64 and offsets=={'nr':0,'arch':4,'instruction_pointer':8,'args':16}
unistd=Path('/usr/include/x86_64-linux-gnu/asm/unistd_64.h');nums={n:int(re.search(r'^#define\s+__NR_'+n+r'\s+(\d+)\b',unistd.read_text(),re.M).group(1)) for n in ['read','ioctl','socket','prctl']}
assert nums=={'read':0,'ioctl':16,'socket':41,'prctl':157}
save('artifacts/SECCOMP_DATA_LAYOUT_VERIFICATION.json',{'phase':'P1','status':'PASS','at':utc(),'local_header':dict(fact(sec),declaration=decl),'native_ctypes':{'size':ctypes.sizeof(Data),'alignment':ctypes.alignment(Data),'offsets':offsets,'args_element_bytes':ctypes.sizeof(ctypes.c_uint64)},'architecture':'x86_64','endianness':'little','request_arg_index':1,'request_low32_offset':24,'request_high32_offset':28,'syscall_header':dict(fact(unistd),verified_syscall_numbers=nums),'kernel_or_filter_install':False})
guard();print(json.dumps({'phase':'P1','status':'PASS','constants':defs,'layout_size':ctypes.sizeof(Data),'offsets':offsets,'kernel_attempts':0}))
