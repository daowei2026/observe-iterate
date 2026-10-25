import os
"""仅当前隔离候选导入；不改共享安装。"""
from pathlib import Path
import logging,os,sys
logging.disable(logging.CRITICAL)
os.environ.setdefault('M3ROOT','/m3c3');os.environ.setdefault('M3WORKS','/dwdhome/fy/BASE_E6_2')
sys.path[:0]=['/tmp/bi01-fo01-w03-runtime-20261022','/dwdhome/fy/BASE_E6_2']
import mquant
runtime=Path(os.environ.get('BI01_W11_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker11-runtime'));alias=runtime/'import-candidate';alias.mkdir(exist_ok=True)
candidate=Path('/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-normal-consumer-r0041')
link=alias/'aidata'
if not link.exists():link.symlink_to(candidate,target_is_directory=True)
if link.resolve()!=candidate.resolve():raise ValueError('本单导入别名不符，不覆盖')
mquant.__path__.insert(0,str(alias))
