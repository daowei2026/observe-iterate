"""记录Worker已实际view_image查看的最终像素，PNG仍只在ignored材料。"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,struct
OUT=Path(__file__).resolve().parents[1]
RT=Path('/dwdhome/fy/cgpterm/artifacts/bi01-worker05-runtime')
runtime=json.loads((OUT/'evidence/EXECUTION_RUNTIME.json').read_text())
notes={
 'hover-rb-final.png':{'case':'rb_final_full','observed':'实际hover可读末拍exact/K/present=1状态；图上50 price及前缀效率可辨认，完成窗/working分图，品种色一致。悬浮框临时遮盖其他位置属本次hover状态，不作为永久布局。'},
 'i-recovery-waiting-zero.png':{'case':'i_recovery','observed':'修后12 price、42000 CalendarUTITick和0 CalendarUTITick均有可读数值；效率/逆向量缺件p=0 k=4、ratio缺p=0 k=3分别可见；local_start35361000、count0、last_update缺说明可见。实际原价缺口未用线补齐，整体尚未完成不遮可用数值。'},
 'hc-close-wick.png':{'case':'hc_close_waiting_final','observed':'close3952、下一根close3946/high3959的具名点可辨认；45/97 price、前缀效率、430 ratio及258000/600 CalendarUTITick分别显示。该窗口保留文件侧栏时最右端末拍注记有容器裁切，原renderer值3904已独立核验；不声称此截图所有边缘文字均完整。'}
}
images=[]
for name,note in notes.items():
    p=RT/name;raw=p.read_bytes();w,h=struct.unpack('>II',raw[16:24])
    images.append({'file':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),
                   'native_pixels':[w,h],'worker_view_image_observed':True,**note})
payload={'actor':'Worker Codex；真实Chromium/Jupyter操作后，以view_image实际查看原始截图像素',
 'recorded_at':datetime.now(timezone.utc).isoformat(),'execution_id':runtime['execution_id'],
 'result':'PASS_WITH_VIEWPORT_AND_ACCESS_LIMITS','images':images,
 'limits':['图为常规1800px宽；窄窗口可收起侧栏/水平滚动，不承诺所有窗口均无容器裁切。',
           '本次额外尝试只重开缓存HC输出并收侧栏，未取得live视图，已保留失败；成功路径是已真实通过的新kernel Run All同会话。',
           '截图只是本机ignored技术核验，主交付是可重跑/交互Notebook。',
           '这不是原Pro本人看图、专业业务判断、独立审查或管理认可。']}
(OUT/'evidence/WORKER_VISUAL_INSPECTION.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print('actual Worker visual observations recorded')
