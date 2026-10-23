"""整理已经实际发生的运行/像素证据，保留driver早标签的准确限制。"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

OUT=Path(__file__).resolve().parents[1]
RT=Path('/dwdhome/fy/cgpterm/artifacts/bi01-worker06-runtime')
def dump(name,data):(OUT/'evidence'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
nb=json.loads((OUT/'N_observation_Worker06.ipynb').read_text())
runtime=json.loads((OUT/'evidence/EXECUTION_RUNTIME.json').read_text())
done=json.loads((OUT/'evidence/KERNEL_COMPLETION.json').read_text())
events=json.loads((OUT/'evidence/FRONTEND_EVENTS.json').read_text())
cells=[c for c in nb['cells'] if c['cell_type']=='code']
assert [c['execution_count'] for c in cells]==[1,2,3,4,5,6]
assert not [o for c in cells for o in c.get('outputs',[]) if o['output_type']=='error']
assert runtime['execution_id']==done['execution_id']
assert events[-1]['action']=='frontend_interactions_finished'
restart=next(e for e in events if e['action']=='restart_kernel_run_all_clicked')
assert restart['previous_execution_id']!=runtime['execution_id']
for p in (OUT/'evidence').glob('BROWSER_*.json'):
    assert 'execution:'+runtime['execution_id'] in json.loads(p.read_text())['tags']
helper=runtime['modules']['mquant.aidata.u2_normal_node_behavior_display']
assert hashlib.sha256(Path(helper['file']).read_bytes()).hexdigest()==helper['sha256']
label=next(e for e in events if e['action']=='run_all_finished')
assert label['at']>=done['completed_at']
historical=json.loads((OUT/'failures/pre_policy_alignment/FRONTEND_EVENTS.json').read_text())
early=next(e for e in historical if e['action']=='run_all_finished')
dump('ACTUAL_EXECUTION_ALIGNMENT.json',{
    'checked_at':datetime.now(timezone.utc).isoformat(),'execution_id':runtime['execution_id'],
    'new_execution_differs_from_prior_attempt':True,'actual_kernel_completed_at':done['completed_at'],
    'saved_notebook_code_counts':[1,2,3,4,5,6],'saved_notebook_errors':0,
    'all_actual_browser_roots_current_execution':True,'executed_helper_equals_current_bytes':True,
    'current_driver_completion_label_at':label['at'],'current_label_after_kernel_completed':True,
    'historical_driver_early_label':{'raw_label_at':early['at'],
      'qualification':'预发布351e运行的driver曾提早写完成标签，原记录保留。最终因同步旧配置声明再次新kernel实际执行，已使用修正后的新旧execution守卫；当前标签晚于实际kernel完成。未重算生产N。'},
    'actual_frontend_terminal_at':events[-1]['at']})

hc=next(e for e in events if e['action']=='hc_actual_sidebar_toggle_live_view')
observations={
 'rb-local-live.png':'本次活页面上K/exact、源价4789行、显示294行、缺值/错误0、未覆盖0、视域省略5和完整局部说明均可读；价图确为局部，50/80及两窗效率保持。',
 'i-real-missing-and-zero.png':'真实24行缺价保留断线，缺路径/缺分母说明、12 price、42000 CalendarUTITick和waiting0分别可读；未填零、未以局部重启充极值。',
 'hc-live-before-sidebar.png':f"实际初始侧栏宽{hc['before']['left_stack']['width']}px的1800px图中，末拍close3904完整可读；K103315800可从相关附图标签辨认；close3952/close3946/high3959各标记及430、258000/600分轴清楚。",
 'hc-live-after-sidebar.png':f"实际Ctrl+B后侧栏宽{hc['after']['left_stack']['width']}px，同一root的1800px图、末拍close3904及其余指定注记仍完整可读；没有水平滚动或极度放大。",
 'hc-motion-live.png':'同一HC输出中的45/97 price可辨认，与指定K关联；未混入等待单位。',
 'hc-waiting-live.png':'同一HC输出中258000 CalendarUTITick和600 CalendarUTITick、独立ratio430均可辨认。'}
images=[]
for filename,observation in observations.items():
    p=RT/filename
    images.append({'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                   'native_pixels':[2300,1400],'worker_view_image_observed':True,'observed':observation})
dump('WORKER_VISUAL_INSPECTION.json',{'actor':'Worker Codex实际前端操作，随后view_image查看本次原始截图像素',
     'execution_id':runtime['execution_id'],'hc_root':hc['root'],'viewport_and_sidebar':{'before':hc['before'],'after':hc['after']},
     'result':'PASS_FOR_THE_RECORDED_NORMAL_VIEWPORT','hc_label_code_modified':False,'images':images,
     'qualification':'不是原Pro本人看图/操作、专业判断或管理接收；不保证任意窗口尺寸适配。PNG只在本机ignored取证，主交付是执行Notebook。'})
print('actual new kernel/root/source and Worker pixel evidence recorded')
