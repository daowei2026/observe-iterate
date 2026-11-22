"""仅本分析进程加载锁定uplot源码；不改共享uplot工作区/不运行Feature。"""
from pathlib import Path
import importlib.util
import os
import runpy
import sys

ROOT = Path(__file__).resolve().parent
runtime = Path('/dwdhome/fy/BASE_E6_2_copy/.runtime/f800-input-missing-20261123/runtime')
os.environ['M3WORKS'] = str(runtime)
os.environ['PATH'] = str(runtime / 'edh-universe/bin') + os.pathsep + os.environ['PATH']
sys.path.insert(0, str(runtime))
import mquant
src = ROOT / 'source/uplot'
spec = importlib.util.spec_from_file_location('mquant.uplot', src / '__init__.py', submodule_search_locations=[str(src)])
mod = importlib.util.module_from_spec(spec)
sys.modules['mquant.uplot'] = mod
spec.loader.exec_module(mod)
mquant.uplot = mod
sys.path.insert(0, str(ROOT))
script = sys.argv.pop(1)
sys.argv[0] = script
runpy.run_path(script, run_name='__main__')
