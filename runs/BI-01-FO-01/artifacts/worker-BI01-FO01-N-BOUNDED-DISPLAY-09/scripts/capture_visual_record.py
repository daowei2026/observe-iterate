"""记录已由Worker实际view_image看过的本次像素；不以自动脚本代替看图。"""
from pathlib import Path
import datetime,hashlib,json,re
from PIL import Image
OUT=Path(__file__).resolve().parents[1]
RT=Path('/dwdhome/fy/cgpterm/artifacts/bi01-worker09-runtime')
runtime=json.loads((OUT/'evidence/EXECUTION_RUNTIME.json').read_text())
assessments={
 'i-progress-live.png':'本次当前i root：12 price数值/单位完整，累计逆向量缺原因仍在；不是NaN填0。',
 'i-duration-live.png':'42000 CalendarUTITick完整可读，与完成时长12600/13500及等待0分图；不把年龄改成局部恢复年龄。',
 'i-real-missing-and-zero.png':'等待0与缺ratio分母、路径效率缺分别表达；24条缺价不硬连。',
 'hc-live-before-sidebar.png':'本次HC主图四注记close3952、下一根close3946/high3959、末拍close3904完整可读；K/来源在同输出。',
 'hc-live-after-sidebar.png':'真实切换侧栏后同root四价格注记仍可辨认；仅承诺本次2300×1400/DPR1/1800px图条件。',
 'hc-motion-live.png':'45/97价差、430ratio与价格水平不共轴，数值可读。',
 'hc-waiting-live.png':'258000和正式600的CalendarUTITick数值可读，与430ratio分图。',
 'hover-rb-final.png':'实际悬浮可见rb/K103315800/cfd51328及present=1，原值50及source exact未串到其他K。'}
rows=[]
for name,assessment in assessments.items():
 p=RT/name
 with Image.open(p) as img:size=list(img.size)
 rows.append({'local_ignored_file':name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
  'screenshot_size':size,'capture_at':datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).isoformat(),
  'actually_inspected_by':'Worker Codex，view_image工具显示本机真实截图后判断（high展示可能按客户端缩放）',
  'assessment':assessment})
result={'execution_id':runtime['execution_id'],'actual_aidata_head':runtime['actual_aidata_head'],
 'inspection_recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'qualification':'Worker限定技术看图，不是原Pro本人看图/业务正确性/管理接收；PNG仅ignored取证，不作主交付',
 'records':rows,'original_failed_new_render':{'file':'first-render-i-real-missing-and-zero.png',
  'sha256':hashlib.sha256((RT/'first-render-i-real-missing-and-zero.png').read_bytes()).hexdigest(),
  'aidata':'a38d33ba43c0fecf2e669eaa25c334054d84411a','observed_defect':'12/42000标签上缘裁切，原值/轴无错误；原件保留ignored'},
 'limits':['未看所有未来K/任意窄屏；不把合成夹具当市场图','未实开共享平台report_url','原Pro本人实际查看/管理接收仍须真实发生']}
(OUT/'evidence/ACTUAL_VISUAL_INSPECTION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
log=(RT/'tests.private.log').read_bytes();match=re.search(rb'(\d+) passed, (\d+) warnings in ([0-9.]+)s',log)
assert match and int(match[1])==59
test={'actual_command':'/m3c3/Linux/apps/anaconda3/bin/python run_tests.py',
 'test_modules':['test_bounded_display_contract.py','test_evidence_plot_contract.py','test_u2_normal_node_behavior_display.py','test_normal_node_behavior.py'],
 'passed':int(match[1]),'warnings':int(match[2]),'pytest_reported_seconds':float(match[3]),
 'raw_log_sha256':hashlib.sha256(log).hexdigest(),'raw_log_location':'仅本机ignored；不运输库/连接上下文',
 'qualification':'定向技术夹具/原相连回归，非全仓或正式市场/平台验收'}
(OUT/'evidence/TEST_RUN.json').write_text(json.dumps(test,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'viewed_actual_images':len(rows),'actual_tests_passed':test['passed'],'execution_id':runtime['execution_id']}))
