"""Worker已实际view_image看过当前六张关键像素后调用；不以hash代替看图。"""
from pathlib import Path
import datetime,hashlib,json,os
from PIL import Image
OUT=Path(__file__).resolve().parents[1]
RT=Path(os.environ.get('BI01_W10_RUNTIME','/dwdhome/fy/cgpterm/artifacts/bi01-worker10-runtime'))
execution=json.loads((OUT/'evidence/EXECUTION_RUNTIME.json').read_text())['execution_id']
assert os.environ['AI_VIEWED_EXECUTION']==execution,'必须先亲看当前执行像素，不能沿用旧版AI视觉'
items=[('rb-confirmation-time-and-members.png','rb_query_at_or_after_confirmation','实际起点/确认与知识K分开，92400年龄与三项成员角色可读'),
 ('rb-retrospective-readouts.png','rb_comparison','真实两个K各两窗/working/年龄/等待点式读数，共同轴、不同Life不连线'),
 ('rb-final-same-life-clock.png','rb_query_final','末拍50/80、年龄及123600/7800/约15.846按单位分面板；年龄文字偏移无改值'),
 ('i-after-local-clock-persists.png','i_query_i_after_recovery','后一拍9.5/42600/600及仍缺项，正等待时局部计时说明持续'),
 ('i-retrospective-age-and-missing.png','i_comparison','三拍41400/42000/42600、缺/12/9.5和缺/0/600；逐K缺项、原价缺口可辨'),
 ('i-comparison-full-identity-hover.png','i_comparison','真实hover完整Life/exact/K/原状态与保存基础，不只短身份')]
records=[]
for name,case,seen in items:
 p=RT/name;snapshot=json.loads((OUT/'evidence'/('BROWSER_'+case+'.json')).read_text())
 assert 'execution:'+execution in snapshot['tags']
 with Image.open(p) as im:dimensions=list(im.size)
 records.append(dict(ignored_image_name=name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),pixels=dimensions,
  execution=execution,case=case,root=snapshot['root'],worker_actually_viewed_pixels=True,observed=seen))
result=dict(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),operator='Worker Codex；Playwright实际前端操作，主agent通过view_image定向看原像素',
 actual_viewport=[2300,1400],DPR=1,price_plot_width=1800,sidebar='文件侧栏保留',
 qualification='Worker限定技术看图，不是Pro本人看图或管理认可；PNG只在本机ignored，不是主交付',
 records=records,limitations=['不要求任意窄屏适配；逐K原状态精确解释另依原表/hover。','既有只读uplot空图例警告未清理；未为全console清零扩大保护面。'])
(OUT/'evidence/WORKER_VISUAL_INSPECTION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
failures=[]
for name in ('FIRST_FRONTEND_EPISODE_LIFECYCLE.json','SECOND_FRONTEND_RECOVERY.json','SECOND_OWNED_KERNEL_CLEANUP.json'):
 p=RT/name
 if p.exists():failures.append(dict(ignored_original=name,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(OUT/'evidence/PRIOR_FRONTEND_FAILURES.json').write_text(json.dumps(dict(
 qualification='原失败/限制不改称通过；设备、PID、原日志与失败图只保留本机ignored',
 originals=failures,episodes=[
 dict(execution='W10-20261024T233438Z-a26203b8',result='Run All及rb前后前已成，比较dropdown未选成；修正实际label定位'),
 dict(execution='W10-20261024T233941Z-3b235d8a',result='模型/控件已成但i实际canvas白、hover未成；包装退出143来源未知，自有残留kernel精确清理为0'),
 dict(execution='W10-20261024T235157Z-1cc76a61',result='none虚拟挂载下全操作/hover成功；像素发现少量文字拥挤，保留该版再改标签'),
 dict(execution='W10-20261024T235919Z-81be67ef',result='全操作/hover成功；再拉开年龄文字屏幕间距，原值/坐标不改，保存该版后清输出新执行')],
 final_execution=execution,final_lifecycle='FRONTEND_EPISODE_LIFECYCLE.json',
 early_probes=['m3sof路径缺失按已有环境接回，未升级共享依赖。','原CSV与解析时间的小数秒文本格式不同，比较按ISO时间值，原字节hash仍逐字核。','清输出重执行中与缺PVD隔离快照的检查因输入未完整而拒绝，未记为通过。'],
 raw_logs_and_images_uploaded=False),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(execution_id=execution,worker_pixel_records=len(records),pro_visual_claim=False)))
