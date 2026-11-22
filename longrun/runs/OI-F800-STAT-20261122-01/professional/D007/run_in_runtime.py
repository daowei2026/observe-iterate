"""绑定本轮独立源码、引擎和Python工作目录。"""
from pathlib import Path
import os
import runpy
import sys

runtime=Path('/dwdhome/fy/BASE_E6_2_copy/.runtime/f800-input-missing-20261123/runtime')
os.environ['M3WORKS']=str(runtime)
os.environ['PATH']=str(runtime/'edh-universe/bin')+os.pathsep+os.environ['PATH']
sys.path.insert(0,str(runtime))
script=sys.argv.pop(1)
sys.argv[0]=script
runpy.run_path(script,run_name='__main__')
