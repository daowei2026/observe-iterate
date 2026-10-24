import os, sys
from pathlib import Path
os.environ.setdefault('M3ROOT', '/m3c3')
os.environ.setdefault('M3WORKS', '/dwdhome/fy/BASE_E6_2')
sys.path[:0] = ['/tmp/bi01-fo01-w03-runtime-20261022', '/dwdhome/fy/BASE_E6_2']
import mquant
overlay = Path('/dwdhome/fy/cgpterm/artifacts/bi01-worker07-runtime/import')
overlay.mkdir(exist_ok=True)
link = overlay / 'aidata'
if not link.exists():
    link.symlink_to('/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-platform-board-r0022', target_is_directory=True)
mquant.__path__.insert(0, str(overlay))
