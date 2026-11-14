import pathlib
W=pathlib.Path(__file__).resolve().parents[1]
p=W/'SAMPLE_CHAIN.jsonl';assert p.exists() and p.stat().st_size==0;p.rename(W/'evidence/460-SAMPLE_CHAIN.empty.failed')
code=(W/'commands/460-real-chain-extraction.py').read_text()
old="with (W/'SAMPLE_CHAIN.jsonl').open('x') as f:\n for v in records:f.write(json.dumps(v,ensure_ascii=False,allow_nan=False)+'\\n')"
new="""import math
+def normalize(value, path, missing):
+ if isinstance(value,float) and not math.isfinite(value):
+  missing.append({'json_path':path,'stored_value_repr':repr(value),'reason':'on-disk IEEE nonfinite numeric value; represented as JSON null, not imputed'});return None
+ if isinstance(value,dict):return {k:normalize(v,path+'/'+k,missing) for k,v in value.items()}
+ if isinstance(value,list):return [normalize(v,path+'/'+str(i),missing) for i,v in enumerate(value)]
+ return value
+normalized=[]
+for value in records:
+ missing=[];v=normalize(value,'',missing);v['nonfinite_stored_values']=missing;normalized.append(v)
+with (W/'SAMPLE_CHAIN.jsonl').open('x') as f:
+ for v in normalized:f.write(json.dumps(v,ensure_ascii=False,allow_nan=False)+'\\n')""".replace('\n+','\n')
assert old in code;code=code.replace(old,new);exec(compile(code,str(W/'commands/460-real-chain-extraction.py')+'+strict-json-normalization','exec'))
