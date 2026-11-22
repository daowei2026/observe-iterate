"""交E直接执行的入口；D仅导入/检查，不调用本文件main。

PYTHONDONTWRITEBYTECODE=1 bash run-python.sh \
  artifacts/OI-F800-STAT-20261122-01/D011/run_definition.py \
  --output-html artifacts/OI-F800-STAT-20261122-01/caegraph-E/f800.html

此命令仅供后继E实际运行，不表示E3核图/E4正式取数已经通过。
"""
from pathlib import Path
from hashlib import sha256
import argparse
import importlib.util
import json
import os
import sys

ROOT = Path(__file__).resolve().parent
BASE = Path('/dwdhome/fy/BASE_E6_2_copy')
RUNTIME = BASE / '.runtime/f800-input-missing-20261123/runtime'


def bootstrap():
    for item in json.loads((ROOT / 'UPLOT_SOURCE_SNAPSHOT.json').read_text())['files']:
        if sha256((ROOT / item['path']).read_bytes()).hexdigest() != item['sha256']:
            raise ValueError('锁定uplot源码漂移：' + item['path'])
    for item in json.loads((ROOT / 'DEPENDENCY_BINDING.json').read_text())['files']:
        if sha256(Path(item['path']).read_bytes()).hexdigest() != item['sha256']:
            raise ValueError('锁定runtime依赖漂移：' + item['path'])
    os.environ['M3WORKS'] = str(RUNTIME)
    os.environ['PATH'] = str(RUNTIME / 'edh-universe/bin') + os.pathsep + os.environ['PATH']
    sys.path.insert(0, str(RUNTIME))
    import mquant
    src = ROOT / 'source/uplot'
    spec = importlib.util.spec_from_file_location('mquant.uplot', src / '__init__.py',
                                                submodule_search_locations=[str(src)])
    module = importlib.util.module_from_spec(spec)
    sys.modules['mquant.uplot'] = module
    spec.loader.exec_module(module)
    mquant.uplot = module
    sys.path.insert(0, str(ROOT / 'definition'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-html', type=Path, required=True)
    args = parser.parse_args()
    output = args.output_html.resolve()
    if not output.is_relative_to(BASE):
        raise ValueError('输出须位于Owner授权BASE工作区')
    if output.exists():
        raise FileExistsError('输出已存在，须保留原件并由E指定新的路径')
    bootstrap()
    from bokeh.embed import file_html
    from bokeh.resources import INLINE
    from f800_definition import build_bound_display, digest, DEFINITION_ID
    layout, meta = build_bound_display()
    html = file_html(layout, INLINE, 'F800 · 真实实例 CAEGraph / C2-v4')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html)
    # 构图运行身份记录；正式图数据须E3核图后从meta['roots']原生CDS另行导出。
    report = dict(definition=DEFINITION_ID, script=str(Path(__file__).resolve()),
                  html=str(output), html_sha256=digest(output), native_feature_dir=meta['instance_full_dir'],
                  position=meta['position'], boundary=meta['boundary'],
                  figure_count=meta['fig_count'], c2_semantics=meta['html_semantics'],
                  formal_feature_recomputed=False, formal_graph_data_exported=False,
                  E3_visual_check='尚未执行', E5_consistency_check='尚未执行',
                  plot_data_entry="build_bound_display()返回meta['roots']，叶节点为原生PlotDataNode.cds")
    output.with_suffix('.runtime.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False))


if __name__ == '__main__':
    main()
