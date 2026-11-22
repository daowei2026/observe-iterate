"""只读DBA header和少量坐标；独立于DataFrame/DbArray包装核验物理位值。"""
from pathlib import Path
from datetime import datetime,timezone
import json,mmap,struct,math

ROOT=Path(__file__).resolve().parent
class Dba:
    def __init__(self,path,fmt):
        self.f=path.open('rb');self.m=mmap.mmap(self.f.fileno(),0,access=mmap.ACCESS_READ)
        version,self.offset,item_size,alignment,self.length=struct.unpack_from('<iiiiq',self.m)
        assert version==0 and item_size==8 and self.offset==64
        self.fmt=fmt
    def __getitem__(self,i):return struct.unpack_from(self.fmt,self.m,self.offset+i*8)[0]
    def position(self,n):
        a,b=0,self.length
        while a<b:
            mid=(a+b)//2
            if self[mid]<n:a=mid+1
            else:b=mid
        return a if a<self.length and self[a]==n else None
    def close(self):self.m.close();self.f.close()

probe=json.loads((ROOT/'PNV_INPUT_PROBE.json').read_text())
rows=[]
for s in probe['symbols']:
    full=Path(s['pnv_calendar_path']);own=Path(s['self_calendar_comparison']['path'])
    ts=Dba(full/'closeTs.dba','<q');price=Dba(full/'close.dba','<d');uti=Dba(full/'closeUti.dba','<q')
    selfts=Dba(own/'closeTs.dba','<q');selfprice=Dba(own/'close.dba','<d')
    results=[]
    for label,date in [('previous',s['previous']['timestamp']),('gap_first',s['first_missing']),('gap_last',s['last_missing']),('resumed',s['resumed']['timestamp'])]:
        target=int(datetime.fromisoformat(date).replace(tzinfo=timezone.utc).timestamp())*10**9
        pos=ts.position(target);p=price[pos];j=selfts.position(target)
        result=dict(label=label,timestamp=date,calendar_dba_row=pos,calendar_uti=uti[pos],
            calendar_price_bits=hex(struct.unpack_from('<Q',price.m,price.offset+pos*8)[0]),
            calendar_finite=math.isfinite(p),self_present=j is not None,
            self_finite=j is not None and math.isfinite(selfprice[j]),
            prices_equal=j is not None and math.isfinite(p) and p==selfprice[j])
        assert result['self_present']==(label in ['previous','resumed'])
        assert result['calendar_finite']==(label in ['previous','resumed'])
        if result['self_present']:assert result['prices_equal']
        results.append(result)
    rows.append(dict(symbol=s['symbol'],calendar_header_length=ts.length,self_header_length=selfts.length,results=results))
    for x in [ts,price,uti,selfts,selfprice]:x.close()
(ROOT/'BINARY_BOUNDARY_PROBE.json').write_text(json.dumps(dict(completed=True,diagnostic_only=True,read_only=True,results=rows),ensure_ascii=False,indent=2)+'\n')
print('Binary boundary controls passed:',len(rows)*4)
