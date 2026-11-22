"""只读核新Python模块与实际ts选择，不构造/运行正式Feature。"""
from pathlib import Path
from datetime import datetime,timezone
import importlib,json,os,shutil

ROOT=Path(__file__).resolve().parent
EXPECTED=ROOT.parents[2]/'.runtime/f800-input-missing-20261123/runtime'
from m3sof import settings
settings.ctx['APP_DIR']=str(ROOT/'adapter-fixture-app')
settings.ctx['MQUANT_LOGGER_DIR']=str(ROOT/'logs')
settings.ctx['DEFAULT_STORE_DIR']=str(ROOT/'fixture-store')
import mquant
module=importlib.import_module('mquant.tis.frp.CommonPriceTurnGroupCandidates')
actual=Path(shutil.which('ts')).resolve()
assert actual==(EXPECTED/'edh-universe/bin/ts').resolve()
assert Path(mquant.__file__).resolve()==(EXPECTED/'mquant/__init__.py').resolve()
assert Path(module.__file__).resolve()==(EXPECTED/'mquant/tis/frp/CommonPriceTurnGroupCandidates.py').resolve()
result=dict(completed=True,checked_at=datetime.now(timezone.utc).isoformat(),M3WORKS=os.environ['M3WORKS'],
    mquant_file=mquant.__file__,constructor_module=module.__file__,resolved_constructor=str(Path(module.__file__).resolve()),
    actual_ts=str(actual),formal_feature_constructed=False,formal_feature_run=False)
(ROOT/'RUNTIME_LOADING_PREFLIGHT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
