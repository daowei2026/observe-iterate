"""汇集白名单技术证据与实际保存Notebook精确源码；不运输私密日志/截图。"""
from pathlib import Path
import datetime,hashlib,json,os,shutil,subprocess
OUT=Path(__file__).resolve().parents[1]
RT=Path(os.environ.get('BI01_W09_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker09-runtime'))
def sha(data):return hashlib.sha256(data).hexdigest()
def dump(path,data):
 path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(data,ensure_ascii=False,indent=2,allow_nan=False)+'\n')

for name in ('FINAL_CONTRACT.json','COLD_RESTORE_AND_BRIDGE.json','BOARD_REPLICA_CHECK.json',
             'RB_HC_BOARD_REPLICAS.json','HISTORY_READONLY_CHECK.json','AIDATA_GITHUB_READBACK.json',
             'CANDIDATE_LAYOUT_RESULTS.json','FRONTEND_EPISODE_LIFECYCLE.json','OPTIONAL_IDENTITY_CHECK.json','PARTIAL_CARRIER_READBACK.json'):
 src=RT/name
 if src.exists():shutil.copy2(src,OUT/'evidence'/name)

# 重放脚本实际来自本单已执行脚本，只把生成文件放到ignored runtime。
for name in ('probe_final_contract.py','cold_restore.py','verify_board_replica.py','verify_remaining_board_replicas.py','run_tests.py','probe_optional_identity.py'):
 source=(RT/name).read_text().replace('rt=Path(__file__).resolve().parent',
     "import os\nrt=Path(os.environ.get('BI01_W09_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker09-runtime'));rt.mkdir(parents=True,exist_ok=True)")
 (OUT/'scripts'/name).write_text(source)

selection_inputs=[]
for symbol in ('rb','i','hc'):
 name='BI01-FO01-W07-20261024T0028-'+symbol
 original=OUT.parents[3]/'artifacts/bi01-worker07-runs'/name
 replica=RT/'core-validation-replica'/name
 target=OUT/'inputs'/symbol;target.mkdir(parents=True,exist_ok=True)
 for filename in ('normal_node_behavior.json','timespan_index.csv','chart_manifest.csv'):
  shutil.copy2(original/'manifest'/filename,target/filename)
 evidence=OUT/'evidence/board_contract'/symbol;evidence.mkdir(parents=True,exist_ok=True)
 for filename in ('feature_slice_stats.csv','timespan_index.csv'):
  shutil.copy2(replica/'manifest'/filename,evidence/filename)
 for folder in sorted((replica/'formal_dependencies').iterdir()):
  node=folder.name;dest=evidence/'formal_dependencies'/node;dest.mkdir(parents=True,exist_ok=True)
  shutil.copy2(folder/'INDEX.json',dest/'INDEX.json')
  selection_inputs.append({'run_id':name,'node_id':node,'symbol':symbol,
      'same_node_original_readable_packet':'https://github.com/daowei2026/observe-iterate/tree/9aa0fe91e4c37a4d983ebd62aea0b5c45755206a/runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-PLATFORM-BOARD-07/board_delivery/'+name+'/'+node+'_packet',
      'new_role_stats':str((evidence/'feature_slice_stats.csv').relative_to(OUT)),
      'new_formal_dependency_index':str((dest/'INDEX.json').relative_to(OUT)),
      'runtime_original_run_dir':str(original),
      'qualification':'正常原包不重传，原正式表继续可读；新统计/索引为隔离新角色合同验证，不冒称生产新发布或可用新图'})
dump(OUT/'inputs/SAME_NODE_DATA_LINKS.json',{'nodes':selection_inputs,
    'source_role_note':'plot_view_data非正式；原表仍按source index/W07 packet取得，node外引用未改时间或丢弃'})

nb_path=OUT/'N_observation_Worker09.ipynb'
raw=nb_path.read_bytes();nb=json.loads(raw)
target=OUT/'notebook_source';target.mkdir(exist_ok=True)
parts=['# Worker09 实际保存Notebook：精确有序源码\n\n',
       f'原文件：N_observation_Worker09.ipynb；bytes={len(raw)}；SHA256={sha(raw)}。\n\n',
       '此文本不是完整Notebook：不展开大段内嵌JS/widget/图形输出。每个cell的source逐字保留；输出仅列类型/MIME/错误与hash，完整输出仍在主ipynb。\n\n']
rows=[]
for i,cell in enumerate(nb['cells']):
 source=''.join(cell['source']);filename=f'{i:02d}-{cell["id"]}.source.txt'
 (target/filename).write_text(source)
 assert (target/filename).read_bytes()==source.encode()
 outputs=[]
 for j,o in enumerate(cell.get('outputs',[])):
  encoded=json.dumps(o,ensure_ascii=False,sort_keys=True).encode()
  outputs.append({'position':j,'output_type':o['output_type'],'mime_types':list(o.get('data',{})),
      'ename':o.get('ename'),'bytes_json':len(encoded),'sha256_json':sha(encoded)})
 row={'position':i,'id':cell['id'],'type':cell['cell_type'],'execution_count':cell.get('execution_count'),
      'metadata':cell.get('metadata',{}),'source_file':filename,'source_utf8_bytes':len(source.encode()),
      'source_sha256':sha(source.encode()),'source_exact_match':True,'outputs':outputs}
 rows.append(row)
 parts.extend([f'## {i}. {cell["id"]} / {cell["cell_type"]} / execution_count={cell.get("execution_count")}\n\n',
               'metadata: '+json.dumps(cell.get('metadata',{}),ensure_ascii=False)+'\n\n',
               '````'+('python' if cell['cell_type']=='code' else 'markdown')+'\n',source,
               '' if source.endswith('\n') else '\n','````\n\n',
               '输出索引：'+json.dumps(outputs,ensure_ascii=False)+'\n\n'])
dump(target/'INDEX.json',{'notebook_file':nb_path.name,'notebook_bytes':len(raw),'notebook_sha256':sha(raw),
    'notebook_blob':subprocess.check_output(['git','hash-object',str(nb_path)],text=True).strip(),
    'metadata':nb['metadata'],'cell_source_exact_match':True,'cells':rows,
    'qualification':'source文本逐字对应；大段保存输出未展开，不能称完整Notebook副本'})
(target/'NOTEBOOK_SOURCE.md').write_text(''.join(parts).rstrip()+'\n')

failures=[]
for name in ('FIRST_FRONTEND_EVENTS.json','FIRST_FRONTEND_RECOVERY.json','FIRST_OWNED_KERNEL_CLEANUP.json',
             'SECOND_FRONTEND_IDLE_REPAIR.json','SECOND_FRONTEND_EPISODE_LIFECYCLE.json',
             'THIRD_FRONTEND_EPISODE_LIFECYCLE.json','FOURTH_FRONTEND_EPISODE_LIFECYCLE.json',
             'FIFTH_FRONTEND_EPISODE_LIFECYCLE.json','SIXTH_FRONTEND_EPISODE_LIFECYCLE.json','SEVENTH_FRONTEND_EPISODE_LIFECYCLE.json','EIGHTH_FRONTEND_EPISODE_LIFECYCLE.json'):
 p=RT/name
 if p.exists():failures.append({'file':name,'sha256':sha(p.read_bytes()),'safe_record':json.loads(p.read_text())})
dump(OUT/'evidence/PRIOR_FRONTEND_FAILURES.json',{'qualification':'失败保留，不把点击/选择kernel/idle冒称已执行；最终实跑证据另见FRONTEND_EVENTS',
    'facts':['第一次等待尚未产生的runtime标记触发FileNotFoundError；已修为等待真实新execution。',
    '组合菜单首次实际出现Select Kernel而非Restart确认；当时全部代码count为空，未运行。',
    '未选kernel时Restart不可用；随后精确选择Python3。',
    'Select按钮的role精确定位不匹配，改用真实对话框接受按钮。',
    '单独Restart位于Kernel菜单而非Run菜单；实际读取菜单后修正。',
    'a38新执行真实像素中i推进12及年龄42000标签上缘裁切；25a9仅改共用文字向内放置，原新执行及像素保留在ignored。',
    '第二次新执行已完成Run All及rb交互；新增检查把浏览器NumberSpec当普通数值比较触发TypeError，修正实际NumberSpec取值后再验证，未把探针失败混成市场缺件。',
    '第三次新执行在rb wheel探针无范围变化；真实截图及指针y1393.875证明落在底部状态栏附近而非可见canvas，改为按可见frame交集选真实鼠标位置并居中滚动，不直接赋值range。'],
    'safe_records':failures,
    'raw_original_logs':'仅本机ignored，未提交；原失败原件/生命周期不删除'})

# 仅建立交付manifest，不把自身/后续回执纳入循环hash。
entries=[]
for path in sorted(OUT.rglob('*')):
 if not path.is_file() or any(p in ('.ipynb_checkpoints','__pycache__') for p in path.parts):continue
 relative=str(path.relative_to(OUT))
 if relative in ('DELIVERY_MANIFEST.json','GITHUB_RECEIPT.json'):continue
 data=path.read_bytes();entries.append({'path':relative,'bytes':len(data),'sha256':sha(data),
     'git_blob':subprocess.check_output(['git','hash-object',str(path)],text=True).strip()})
dump(OUT/'DELIVERY_MANIFEST.json',{'order_id':'BI01-FO01-N-BOUNDED-DISPLAY-09',
    'generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'qualification':'本单新增/修订实物；原W06/W07/W08只引用，不整包重传；不代表平台/专业/管理认可',
    'excludes':['DELIVERY_MANIFEST.json','GITHUB_RECEIPT.json','.ipynb_checkpoints','__pycache__'],
    'files':entries})
print(json.dumps({'files':len(entries),'notebook_bytes':len(raw),'source_cells':len(rows),'all_source_exact':True}))
