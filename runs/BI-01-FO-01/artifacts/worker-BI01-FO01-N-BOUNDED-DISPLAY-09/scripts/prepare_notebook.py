"""从确切W06主实物派生W09；清旧输出，本次实际新kernel执行。"""
from pathlib import Path
import hashlib,json,subprocess

OUT=Path(__file__).resolve().parents[1]
REPO=OUT.parents[3]
REF='351d88cf6d669b32bb245882494769cc9d14f42b'
W06='runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-W05-SCOPE-READABILITY-06/'
ORDER='BI01-FO01-N-BOUNDED-DISPLAY-09'
INVOCATION='BI01-FO-01-R0035-20261024T185441Z-1c7e5a8c'
def raw(name):return subprocess.check_output(['git','-C',str(REPO),'show',REF+':'+W06+name])
original=raw('N_observation_Worker06.ipynb')
blob=subprocess.check_output(['git','hash-object','--stdin'],input=original).decode().strip()
assert blob=='58f7b27b37bc2db9582a9b24460f6f3e62a6bf41'
nb=json.loads(original);plan=json.loads(raw('DISPLAY_PLAN.json'))
plan.update(version='0.4.0-worker09',order_id=ORDER,issuer_invocation_id=INVOCATION,
    aidata_reference='fy/bi01-fo01-n-bounded-display-r0035',consumer_configuration='0.3.0-worker09',
    delivery_qualification='新共用消费者工作2技术验证；初批平台仅M21四视域，其他K仅工作2准备；共享采用未获新增授权')
(OUT/'DISPLAY_PLAN.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
for cell in nb['cells']:
    source=''.join(cell['source'])
    source=(source.replace('Worker06','Worker09').replace('worker06','worker09').replace('BI01_W06','BI01_W09')
        .replace('W06-','W09-').replace('bi01-w06-','bi01-w09-')
        .replace('aidata-bi01-fo01-n-w05-scope-r0017','aidata-bi01-fo01-n-bounded-display-r0035')
        .replace('0.3.2-worker09','0.4.0-worker09'))
    if cell['id']=='r0011-00':
        source=f'''# U2NormalNodeBehaviorFrp — Worker09 有限共用展示Notebook

order_id={ORDER}；签发{INVOCATION}。
从W06已执行确切主Notebook（blob58f7b27b）派生，保留原有序cell谱系，旧输出全部清除；下方输出仅属于本次新kernel。
N领域模块准备原表关联/合法K/状态，唯一机械组合为aidata.evidence_composition，Notebook与正常CAE/bridge消费同一路径。
默认画M21已认可的rb末拍完整/局部、i恢复和hc末拍。其他K选择明确仅为工作2准备/回归，未获对应平台用途认可；不造连续历史或保持线。
主交付是实际执行可交互的Notebook，不是旧HTML/PNG。技术结果回原Pro；未自行完成共享发布、工作3接收或正式工作4。
Restart Kernel → Run All；rb范围选择、hover、图例、平移/缩放/复位按实际操作留证。历史同bar close不是开盘瞬时已知认证。
'''
    if cell['id']=='r0011-01':
        source='import logging\nlogging.disable(logging.CRITICAL)\n'+source
    if cell['id']=='r0011-03':
        source=source.replace('import mquant.aidata.u2_normal_node_behavior_display as nd',
            'import mquant.aidata.u2_normal_node_behavior_display as nd\nimport mquant.aidata.evidence_composition as ec')
        source=source.replace('for module in (uplot, nd):','for module in (uplot, nd, ec):').replace('for mod in (uplot, nd):','for mod in (uplot, nd, ec):')
        source=source.replace('"kernel": "m3py310"','"kernel": "python3"')
        source=source.replace('layout.tags = ["worker09",','layout.tags = [*layout.tags, "worker09",')
        source=source.replace('title_suffix="Worker09 本次新绘制｜" + case)',
            'title_suffix="Worker09 本次新绘制｜" + case + ("｜M21具名切面" if case in ("rb_final_full","rb_final_local","i_recovery","hc_close_waiting_final") else "｜仅工作2准备/回归，未获平台用途认可"))')
        source=source.replace('LAYOUTS, BUNDLES, AUDITS = {}, {}, {}',
            'RUNTIME["order_id"] = "'+ORDER+'"\nRUNTIME["actual_aidata_head"] = subprocess.check_output(["git","-C",str(AIDATA_WORKTREE),"rev-parse","HEAD"]).decode().strip()\n(EVIDENCE / "EXECUTION_RUNTIME.json").write_text(json.dumps(RUNTIME,ensure_ascii=False,indent=2))\nLAYOUTS, BUNDLES, AUDITS = {}, {}, {}')
    if cell['id']=='r0011-04':
        source='## rb：固定末拍与范围切换\n默认画末拍。其他已取知识K若选择，仅作工作2回归/准备，不扩平台认可；不画稀疏点之间的假保持线。\n'
    if cell['id']=='r0011-05':
        source=source.replace('render_new("rb_sparse_knowledge_cuts", rb_sparse)',
            '# 保留准确稀疏准备代码谱系，但本次默认不执行额外画法/扩大平台范围。')
        source=source.replace('rb_sparse = sparse_evolution(rb_cuts, rb_selected, rb_price, "rb", list(PLAN["rb_cuts"].values()))',
            '# 如确需其他演变，按真实范围另作工作2；当前四视域不依赖该布局。')
        source+='''
# 真实不同K、完全相同价窗的缓存/读数作用域回归；仅工作2技术准备，不作平台发布。
same_window=(103140000, min(PLAN["rb_cuts"].values()))
scope_results=[]
for label in ("before_confirmation","at_or_after_confirmation"):
    k=PLAN["rb_cuts"][label]
    sample=new_selected(rb_cuts[label],rb_price,"rb",k,display_range=same_window)
    actual=nd.build_uplot_layout(sample,context=context,calendar_name=PLAN["calendar"],title_suffix="同价窗不同K技术回归；未获平台用途认可")
    from bokeh.models import GlyphRenderer
    observed={}
    for renderer in actual.select({"type":GlyphRenderer}):
        names=[t[5:] for t in renderer.tags if isinstance(t,str) and t.startswith("view:")]
        if names and names[0] in ("completed_recent_updates","working_progress_points"):
            observed[names[0]]=clean(renderer.data_source.data)
            assert list(renderer.data_source.data["x"])==[k]
            assert list(renderer.data_source.data["y"])==sample.views[names[0]]["y"].tolist()
    assert len(observed)==2
    scope_results.append({"K":k,"price_range":sample.meta["price_range"],"exact":sample.meta["source_exact"],"display_identity":nd.U2NormalNodeBehaviorDisplayFeature(sample).ppid,"actual_scalar_renderers":observed})
assert scope_results[0]["price_range"]==scope_results[1]["price_range"]
assert scope_results[0]["display_identity"]!=scope_results[1]["display_identity"]
(EVIDENCE/"SAME_PRICE_DIFFERENT_K.json").write_text(json.dumps({"execution_id":EXECUTION_ID,"qualification":"真实原表/实际组合器图层；仅工作2技术回归，非新增平台认可", "results":scope_results},ensure_ascii=False,indent=2))
'''
    if cell['id']=='r0011-06':
        source=source.replace('K = PLAN["rb_cuts"][name]', 'K = PLAN["rb_cuts"][name]')
    if cell['id']=='r0011-07':
        source='## i：恢复拍真零与缺量\n默认恢复K35361000；其他已取K选择仅工作2回归/准备，不作平台用途。推进/年龄可用，路径量缺；等待真零与分母缺各自显示。\n'
    if cell['id']=='r0011-08':
        source=source.replace('i_sparse = sparse_evolution(i_cuts, i_selected, i_price, "i", list(PLAN["i_cuts"].values()))',
            '# 不把三切点合成连续时间历史。')
        source=source.replace('render_new("i_sparse_recovery", i_sparse)', '# 默认仅通过下方选择器显示真实恢复拍。')
    if cell['id']=='r0011-09':
        source=source.replace('本页无平台调用','本页只验证共用组合；正常CAE/bridge冷恢复及平台采用权限另见本单完整回交')
    cell['source']=source.splitlines(keepends=True)
    cell['metadata']={}
    if cell['cell_type']=='code':cell['outputs']=[];cell['execution_count']=None
nb['metadata']['kernelspec']={'display_name':'Python 3 (ipykernel)','language':'python','name':'python3'}
nb['metadata']['worker_order']={'order_id':ORDER,'issuer_invocation_id':INVOCATION,'source_commit':REF,
    'source_notebook_blob':blob,'source_notebook_sha256':hashlib.sha256(original).hexdigest(),
    'execution_qualification':'旧输出清除；必须本次真实前端Restart Kernel→Run All'}
nb['metadata']['bi01']={'order_id':ORDER,'invocation_id':INVOCATION}
(OUT/'N_observation_Worker09.ipynb').write_text(json.dumps(nb,ensure_ascii=False,indent=1)+'\n')
(OUT/'evidence').mkdir(exist_ok=True)
(OUT/'evidence/REVISION_PROVENANCE.json').write_text(json.dumps(nb['metadata']['worker_order'],ensure_ascii=False,indent=2)+'\n')
print('Worker09 source Notebook generated from exact W06; no execution claimed')
