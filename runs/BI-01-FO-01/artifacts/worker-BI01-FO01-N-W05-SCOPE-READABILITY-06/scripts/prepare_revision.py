"""从已保存W05 exact blob派生W06；不重建R11候选，不改旧文件。"""
from pathlib import Path
import hashlib, json, subprocess

OUT = Path(__file__).resolve().parents[1]
REPO = OUT.parents[3]
W05 = 'runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-UPLOT-NOTEBOOK-05/'
REF = 'b055102ad1a70b3c2824c2c6f5e540886deeb5f7'
ORDER = 'BI01-FO01-N-W05-SCOPE-READABILITY-06'
INVOCATION = 'BI01-FO-01-R0017-20261023T192809Z-edd5489f'
def raw(path):
    return subprocess.check_output(['git', '-C', str(REPO), 'show', REF + ':' + W05 + path])

original = raw('N_observation_Worker05.ipynb')
assert hashlib.sha256(original).hexdigest() == '50a8f9cfddd51ff00151e3c2f7490134591f01ce6fe4dde970d3321fe270ff8d'
notebook = json.loads(original)
plan = json.loads(raw('DISPLAY_PLAN.json'))
plan.update(version='0.3.2-worker06', order_id=ORDER, issuer_invocation_id=INVOCATION,
            aidata_reference='e8aaa464e30259c84dac47260104c5acda1eac5b')
plan['pending_real_display_changes'] = [x for x in plan['pending_real_display_changes'] if not x.startswith('i waiting and ratio')]
plan['display_scope_policy'] = '完整已供源价用于关联；局部显示范围不改变原成员统计。视域外图元标显示省略，未提供标输入覆盖，原NaN/正式缺字段保留。'
(OUT/'DISPLAY_PLAN.json').write_text(json.dumps(plan, ensure_ascii=False, indent=2)+'\n')
for cell in notebook['cells']:
    source = ''.join(cell['source'])
    source = (source.replace('Worker05', 'Worker06').replace('worker05', 'worker06')
              .replace('BI01_W05', 'BI01_W06').replace('W05-', 'W06-').replace('bi01-w05-', 'bi01-w06-')
              .replace('BI01-FO01-N-UPLOT-NOTEBOOK-05', ORDER)
              .replace('BI01-FO-01-R0014-20261023T153303Z-57f340f3', INVOCATION)
              .replace('0.3.1-worker06', '0.3.2-worker06')
              .replace('aidata-bi01-fo01-n-work2-r0014', 'aidata-bi01-fo01-n-w05-scope-r0017'))
    if cell['id'] == 'r0011-00':
        source = source.replace('从P11真实代码候选修订', '从W05已保存执行Notebook（blob96c80e9e）定向修订，保留原谱系cell id')
        source += '\nW06限定：局部覆盖语义修订、HC正常活视口复核、精确源码运输；工作3/4未签发。\n'
    if cell['id'] == 'r0011-03':
        source = source.replace('"data": clean(data)',
            '"data": clean(data) if "anchor:n_display/" in str(renderer.tags) and "anchor:n_display/close_path" not in str(renderer.tags) else {"qualification": "原价大数组不在kernel审计展开；按源Git与实际浏览器定向切片核对"}')
        source = source.replace('nd.export_plot_view_data(bundle, folder)',
            'if case in ("rb_final_full", "rb_final_local", "i_recovery", "hc_close_waiting_final"):\n        nd.export_plot_view_data(bundle, folder)')
    if cell['id'] == 'r0011-05':
        source = source.replace('def new_selected(tables, price, symbol, K):', 'def new_selected(tables, price, symbol, K, display_range=None):')
        source = source.replace('as_of=int(K),', 'as_of=int(K), display_range=display_range,')
    if cell['id'] == 'r0011-06':
        source = source.replace('price = rb_price if mode == "full" else rb_price[rb_price["open_uti"].between(103140000, K)]',
                                'display_range = None if mode == "full" else (103140000, K)')
        source = source.replace('new_selected(rb_cuts[name], price, "rb", K)',
                                'new_selected(rb_cuts[name], rb_price, "rb", K, display_range=display_range)')
    cell['source'] = source.splitlines(keepends=True)
    cell['metadata'] = {}
    if cell['cell_type'] == 'code':
        cell['outputs'] = []
        cell['execution_count'] = None
notebook['metadata']['bi01'].update(order_id=ORDER, invocation_id=INVOCATION)
notebook['metadata']['worker_order'] = {'order_id':ORDER, 'issuer_invocation_id':INVOCATION,
    'source_notebook_commit':REF, 'source_notebook_blob':'96c80e9e21205126f16ace68c9f9029d09206cdf'}
(OUT/'N_observation_Worker06.ipynb').write_text(json.dumps(notebook, ensure_ascii=False, indent=1)+'\n')
(OUT/'evidence').mkdir(exist_ok=True)
(OUT/'evidence/REVISION_PROVENANCE.json').write_text(json.dumps({
    'order_id':ORDER, 'issuer_invocation_id':INVOCATION, 'original_commit':REF,
    'original_notebook_blob':'96c80e9e21205126f16ace68c9f9029d09206cdf', 'original_bytes':len(original),
    'original_sha256':hashlib.sha256(original).hexdigest(),
    'derivation':'从确切W05已保存实物JSON派生，清原输出后本次新kernel执行；不改W05原件',
    'source_refs':plan['source_refs'], 'production_parameters_changed':False},ensure_ascii=False,indent=2)+'\n')
print('W06 derived from exact saved W05; old files untouched')
