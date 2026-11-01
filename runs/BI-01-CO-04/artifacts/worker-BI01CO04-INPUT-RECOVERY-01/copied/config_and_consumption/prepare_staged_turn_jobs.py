from pathlib import Path
import json,os,hashlib
from mquant.aidata.profiles import ensure_profile_runtime
from mquant.frame import CurrCalendar,TmpStoreEnv,CalType,KLine,eval2
from mquant.frame.lib3 import CurrTradeSet,CurrSymbol,JsonUtil
from mquant.quant import OptContext
ensure_profile_runtime()
root=Path(__file__).resolve().parent
stage=root/"turn_staging";stage.mkdir(exist_ok=True)
cache=stage/"cache";app=stage/"app";cfg=app/"mquant/config/prod";(cfg/"sof").mkdir(parents=True,exist_ok=True)
source=Path('/m3varF/BaseData/futures/GTQH_L1_20210104_20240208')
selection=json.loads((root/"selected_turn_parameters.json").read_text())
context=OptContext({"sof_name":source.name,"stk_tlist":"gtqh_four","startDay":None,"endDay":None})
source_cfg={"store_dir":[str(cache)],"store_name":"fao","opt_start_hour":"21:00:00","opt_end_hour":"20:00:00","sof_category":"BaseData/futures","sof_dir":str(source/"sof"),"sof_tlist_dir":str(source/"sof/tlist"),"ori_dir":str(source/"tick"),"pnv_dir":str(source/"pnv")}
(cfg/"sof"/(source.name+".json")).write_text(json.dumps(source_cfg,indent=2))
(cfg/"store_dir.json").write_text(json.dumps({name:[str(cache)] for name in ["KLine","RctZigWithStatus","ZigZag","ScaleTurnCalendar"]},indent=2))
inputs=[];jobs=[]
with CurrTradeSet(context.sof),CurrCalendar("@"),TmpStoreEnv(rule=True,store_dir=str(cache)):
 for sym in ["rb","hc","i"]:
  with CurrSymbol(sym):
   k=KLine(freq="30m")
   assert Path(k.full_dir).is_relative_to(cache),k.full_dir
   assert not k.backup_full_dirs, k.backup_full_dirs
   df=k.rerun(CalType.OnlyRead).to_df()
   Path(k.full_dir).mkdir(parents=True,exist_ok=True)
   k.dump({"value":df},full_dir=k.full_dir,tar_name=k.tar_name,sof=context.sof)
   fields=Path(k.full_dir)/"fields.json";assert fields.is_file()
   inputs.append({"symbol":sym,"rows":len(df),"staged_kline_cache":k.full_dir,"fields":json.loads(fields.read_text())})
   for role,definition in selection["bindings"].items():
    feature=eval2(definition["fason"])
    params=feature.doFrpTaskParam(run_ups=False,enable_extra=True).for_json()
    params["app"]["app_dir"]=str(app)
    params["sof"]["full_period"]=None
    job=json.loads(JsonUtil.dumps({"target":feature.doFrpTarget(),"task_params":params,"cal_type":"Gen"}))
    path=stage/(sym+"__"+role+".task.json");path.write_text(json.dumps(job,ensure_ascii=False,indent=2))
    jobs.append({"symbol":sym,"role":role,"preset":definition["preset"],"feature_ppid":feature.ppid,"task_file":str(path),"task_sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
(stage/"prepared_jobs.json").write_text(json.dumps({"dataset":source.name,"inputs":inputs,"jobs":jobs,"formal_source_modified":False,"numerical_turn_jobs_started":False},ensure_ascii=False,indent=2))
print(json.dumps({"prepared_jobs":len(jobs),"staged_market_inputs":inputs,"formal_source_modified":False},ensure_ascii=False,indent=2),flush=True)
