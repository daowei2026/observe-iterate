"""探针明确使用候选，不写共享工作树；所有生成文件进入ignored runtime。"""
from pathlib import Path
import logging,os,sys
logging.disable(logging.CRITICAL)
os.environ.setdefault('M3ROOT','/m3c3')
os.environ.setdefault('M3WORKS','/dwdhome/fy/BASE_E6_2')
sys.path[:0]=['/tmp/bi01-fo01-w03-runtime-20261022','/dwdhome/fy/BASE_E6_2']
import mquant
runtime=Path(os.environ.get('BI01_W10_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker10-runtime'))
root=runtime/'import-candidate';root.mkdir(parents=True,exist_ok=True)
link=root/'aidata'
candidate=Path(os.environ.get('BI01_W10_AIDATA','/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-time-expression-r0038'))
if not link.exists():link.symlink_to(candidate,target_is_directory=True)
if link.resolve()!=candidate.resolve():raise ValueError('已有import别名不指向明确候选，停止而不覆盖')
mquant.__path__.insert(0,str(root))
