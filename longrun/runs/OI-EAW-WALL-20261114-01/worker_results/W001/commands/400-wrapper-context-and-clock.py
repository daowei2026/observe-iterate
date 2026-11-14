import pathlib
B=pathlib.Path('/dwdhome/fy/BASE_E6_2');W=pathlib.Path(__file__).resolve().parents[1]
for rel,lo,hi in [('m3sof/settings/json.py',1,110),('m3sof/settings/lib3.py',1,110),('edh-universe/frp/frp-core/src/Frp/Apt/Time.hs',118,230),('edh-universe/frp/frp-core/src/Frp/Apt/Time.hs',230,305)]:
 p=B/rel;print('FILE',p)
 for n,line in enumerate(p.read_text().splitlines(),1):
  if lo<=n<=hi:print(f'{n}: {line}')
print('HEADERS_COMMAND', (W/'evidence/390-bounded-product-headers.command.json').read_text());print('HEADER_TAIL',(W/'evidence/390-bounded-product-headers.stdout.txt').read_text()[-500:])
