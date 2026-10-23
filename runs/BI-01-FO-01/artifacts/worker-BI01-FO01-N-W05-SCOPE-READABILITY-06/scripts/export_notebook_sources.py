"""精确Notebook cell源码的有限运输；不展开大段内嵌JS/保存图。"""
from pathlib import Path
import hashlib, json, subprocess

OUT=Path(__file__).resolve().parents[1]
REPO=OUT.parents[3]
W05_PATH='runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-UPLOT-NOTEBOOK-05/N_observation_Worker05.ipynb'
W05_REF='b055102ad1a70b3c2824c2c6f5e540886deeb5f7'

def digest(raw):return hashlib.sha256(raw).hexdigest()
def dump(path,value):path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def export(label,raw,location,expected_blob=None):
    notebook=json.loads(raw)
    blob=subprocess.check_output(['git','hash-object','--stdin'],input=raw).decode().strip()
    if expected_blob:assert blob==expected_blob
    folder=OUT/'notebook_source'/label
    (folder/'cells').mkdir(parents=True,exist_ok=True)
    index={'label':label,'original_location':location,'original_blob':blob,
           'original_bytes':len(raw),'original_sha256':digest(raw),
           'nbformat':notebook['nbformat'],'nbformat_minor':notebook['nbformat_minor'],
           'notebook_metadata':notebook['metadata'],'cells':[],
           'qualification':'完整有序cell源码/Markdown与metadata；不是包含全部保存输出的完整Notebook副本。原Notebook保留。',
           'not_expanded':'内嵌Bokeh JS/HTML、widget模型与保存图输出不全文展开；每项MIME、位置、字节/hash与错误如实索引。'}
    text=[f'# {label}：精确有序cell源码\n\n',
          f'原件：{location}\n\nGit blob：{blob}；SHA256：{digest(raw)}；{len(raw)} bytes。\n\n',
          '下文保留每个cell的完整source，未压缩代码或Markdown。metadata和输出位置见INDEX.json及cells/*.json。大段保存JS/图像输出未展开；本文件不等于完整Notebook。\n\n']
    for position,cell in enumerate(notebook['cells']):
        filename=f"{position:02d}_{cell.get('id','no-id')}.json"
        data={k:cell[k] for k in ('id','cell_type','source','metadata','execution_count') if k in cell}
        outputs=[]
        for j,output in enumerate(cell.get('outputs',[])):
            row={'position':f'/cells/{position}/outputs/{j}', 'output_type':output['output_type']}
            if 'execution_count' in output:row['execution_count']=output['execution_count']
            if output['output_type']=='error':
                row.update({k:output.get(k) for k in ('ename','evalue','traceback')})
            if 'data' in output:
                row['mime_index']=[{'mime':mime,'json_utf8_bytes':len(json.dumps(value,ensure_ascii=False).encode()),
                                   'json_sha256':digest(json.dumps(value,ensure_ascii=False).encode())}
                                  for mime,value in output['data'].items()]
            if 'text' in output:
                stream=''.join(output['text'])
                row.update(stream_bytes=len(stream.encode()),stream_sha256=digest(stream.encode()))
                if len(stream)<12000:row['actual_stream_text']=stream
            outputs.append(row)
        data['outputs_index']=outputs
        dump(folder/'cells'/filename,data)
        restored=json.loads((folder/'cells'/filename).read_text())
        for key in ('id','cell_type','source','metadata','execution_count'):
            assert restored.get(key)==cell.get(key),(position,key)
        source=''.join(cell['source'])
        index['cells'].append({'position':position,'file':'cells/'+filename,'id':cell.get('id'),
                              'cell_type':cell['cell_type'],'execution_count':cell.get('execution_count'),
                              'source_utf8_bytes':len(source.encode()),'source_sha256':digest(source.encode()),
                              'source_verbatim_equal':True,'outputs':len(outputs)})
        text.extend([f"## Cell {position} / {cell.get('id')} / {cell['cell_type']} / execution_count={cell.get('execution_count')}\n\n",
                     '````'+('python' if cell['cell_type']=='code' else 'markdown')+'\n',source,
                     '' if source.endswith('\n') else '\n','````\n\n'])
    dump(folder/'INDEX.json',index)
    (folder/'NOTEBOOK_SOURCE.md').write_text(''.join(text))
    return {'label':label,'notebook_blob':blob,'notebook_sha256':digest(raw),
            'cells':len(notebook['cells']),'all_cell_source_id_type_count_metadata_verbatim_equal':True,
            'output_errors':[o for c in notebook['cells'] for o in c.get('outputs',[]) if o['output_type']=='error'],
            'source_text_path':str((folder/'NOTEBOOK_SOURCE.md').relative_to(OUT))}

old=subprocess.check_output(['git','-C',str(REPO),'show',W05_REF+':'+W05_PATH])
checks=[export('W05_original',old,W05_REF+':'+W05_PATH,'96c80e9e21205126f16ace68c9f9029d09206cdf')]
new_path=OUT/'N_observation_Worker06.ipynb'
checks.append(export('W06_executed',new_path.read_bytes(),str(new_path.relative_to(REPO))))
dump(OUT/'evidence/NOTEBOOK_SOURCE_VERIFICATION.json',{'checks':checks,'result':'PASS',
     'comparison':'逐cell读取运输JSON，与对应确切Notebook原source数组/id/type/count/metadata相等；不以生成脚本替代已保存实物。'})
print('Exact W05 and executed W06 cell-source transport PASS')
