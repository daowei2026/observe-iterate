from pathlib import Path
import os,json,re,hashlib
rt=Path(__file__).parent
records=json.loads((rt/'ACTIVE_PROCESS_METADATA.private.json').read_text())
trier=next(r for r in records if r['role']=='trier')
p=Path(os.readlink(f"/proc/{trier['pid']}/fd/1"))
with p.open('rb') as f:
 f.seek(max(0,p.stat().st_size-65536));raw=f.read()
(rt/'CURRENT_TRIER_TAIL.private.log').write_bytes(raw)
text=raw.decode(errors='replace')
blocks=text.split('Traceback (most recent call last):')
result=[]
for block in blocks[1:]:
 if 'get_ppdoc' not in block:continue
 frames=[{'file':m[0],'line':int(m[1]),'function':m[2]} for m in re.findall(r'File "([^"\n]+)", line (\d+), in ([^\n]+)',block)]
 terminal=next((l for l in block.splitlines() if re.match(r'^[A-Za-z_.]+(?:Error|Exception):',l)),None)
 error={'type':terminal.split(':',1)[0] if terminal else None}
 if terminal:
  m=re.search(r"has no attribute '([\w_]+)'",terminal)
  if m:error['missing_attribute']=m.group(1)
 result.append({'source':'current active Trier log following existing ppdoc GET',
   'frames':frames[:15],'error':error,
   'qualification':'no full exception or parameters output; raw tail remains ignored'})
(rt/'PPDOC_FAILURE_SUMMARY.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
