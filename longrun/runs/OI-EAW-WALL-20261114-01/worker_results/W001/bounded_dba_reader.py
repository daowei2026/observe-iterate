"""本 W 的只读物理探针；仅 Python 标准库，禁止项目导入及计算。"""
import pathlib, struct, time, math

class BudgetReader:
    def __init__(self, byte_limit=4*1024*1024, seconds=18, file_limit=90):
        self.byte_limit=byte_limit; self.seconds=seconds; self.file_limit=file_limit
        self.bytes_read=0; self.started=time.monotonic(); self.files={}; self.calls=0
    def check(self,n=0):
        if self.bytes_read+n>self.byte_limit or time.monotonic()-self.started>self.seconds:
            raise RuntimeError('STOPPED_FOR_COST: bounded physical read budget')
    def file(self,path):
        p=pathlib.Path(path); k=str(p)
        if k not in self.files:
            assert len(self.files)<self.file_limit
            self.check(24); f=p.open('rb'); b=f.read(24); self.bytes_read+=len(b)
            assert len(b)==24
            v,o,z,a,n=struct.unpack('<iiiiq',b); s=p.stat()
            assert v==0 and o==64 and z in (1,4,8) and a>0 and n>=0 and o+n*z<=s.st_size
            self.files[k]={'f':f,'path':k,'offset':o,'item_size':z,'n':n,'size':s.st_size,'mtime_ns':s.st_mtime_ns}
        return self.files[k]
    def scalar(self,path,i,fmt='q'):
        r=self.file(path); size=struct.calcsize('<'+fmt)
        assert 0<=i<r['n'] and r['item_size']==size
        self.check(size);r['f'].seek(r['offset']+i*size);b=r['f'].read(size)
        assert len(b)==size;self.bytes_read+=size;self.calls+=1
        return struct.unpack('<'+fmt,b)[0]
    def array(self,path,fmt='q',max_rows=50000):
        r=self.file(path);size=struct.calcsize('<'+fmt);assert size==r['item_size'] and r['n']<=max_rows
        self.check(size*r['n']);r['f'].seek(r['offset']);b=r['f'].read(size*r['n'])
        assert len(b)==size*r['n'];self.bytes_read+=len(b);self.calls+=1
        return [v[0] for v in struct.iter_unpack('<'+fmt,b)]
    def text(self,root,vin):
        root=pathlib.Path(root);a=root/'Text$Data.Text/anchor.dba';p=root/'Text$Data.Text/payload.dba'
        end=self.scalar(a,vin);start=self.scalar(a,vin-1) if vin else 0;r=self.file(p)
        assert r['item_size']==1 and 0<=start<=end<=r['n'] and end-start<=32768
        self.check(end-start);r['f'].seek(r['offset']+start);b=r['f'].read(end-start);self.bytes_read+=len(b);self.calls+=1
        assert len(b)==end-start
        return b.decode('utf-8')
    def summary(self):
        result={'bytes_read':self.bytes_read,'byte_limit':self.byte_limit,'seconds_limit':self.seconds,
                'elapsed_seconds':time.monotonic()-self.started,'calls':self.calls,'files':[]}
        for p,r in self.files.items():
            s=pathlib.Path(p).stat();result['files'].append({k:v for k,v in r.items() if k!='f'} | {'unchanged_size_and_mtime':s.st_size==r['size'] and s.st_mtime_ns==r['mtime_ns']})
        return result
    def close(self):
        for r in self.files.values():r['f'].close()
