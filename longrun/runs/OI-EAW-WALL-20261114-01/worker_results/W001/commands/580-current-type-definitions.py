import pathlib,re
B=pathlib.Path('/dwdhome/fy/BASE_E6_2');p=B/'edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/Products.hs';ls=p.read_text().splitlines()
for i,line in enumerate(ls):
 if re.match(r'data (FeatureRunIdentity|WallIdentity|OccurrenceRef|WallLifecycleOccurrence|WallCurrentView|WallBusinessState|P1ProductDiagnostics)\b',line):
  print('TYPE',str(p),i+1)
  for n in range(i,min(i+19,len(ls))):print(f'{n+1}: {ls[n]}')
p=B/'edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/Publication.hs';ls=p.read_text().splitlines();print('WRITER_TYPES',p)
for n in range(610,626):print(f'{n+1}: {ls[n]}')
