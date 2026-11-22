from pathlib import Path
from datetime import datetime,timezone
import json,shutil,difflib
r=Path('artifacts/OI-F800-STAT-20261122-01');e=r/'D012';a=e/'attempts';a.mkdir(exist_ok=True);src=r/'D011';dst=e/'final_script';dst.mkdir(exist_ok=True)
for name in ['run_definition.py','FIELD_BINDING.json','SOURCE_DATA_BINDING.json','DEPENDENCY_BINDING.json','UPLOT_SOURCE_SNAPSHOT.json']:
 shutil.copy2(src/name,dst/name)
for name in ['definition','inputs','source']:
 shutil.copytree(src/name,dst/name)
p=dst/'run_definition.py';old=p.read_text()
helper='''def install_readable_ticks(layout):
    """仅抽稀可见原时间刻度；保留原标签/坐标/CDS/缩放和全部业务数据。"""
    from bokeh.models import Plot, CustomJS
    counts = []
    for fig in layout.select(dict(type=Plot)):
        axis = fig.xaxis[0]
        base_ticks = list(axis.ticker.ticks)
        xr = fig.x_range
        visible = [x for x in base_ticks if xr.start <= x <= xr.end]
        stride = max(1, (len(visible) + 9) // 10)
        axis.ticker.ticks = visible[::stride]
        callback = CustomJS(args=dict(axis=axis, xr=xr, base_ticks=base_ticks), code="""
const visible=base_ticks.filter(x=>x>=xr.start && x<=xr.end);
const stride=Math.max(1,Math.ceil(visible.length/10));
axis.ticker.ticks=visible.filter((_,i)=>i%stride===0);
""")
        xr.js_on_change('start', callback)
        xr.js_on_change('end', callback)
        counts.append(dict(figure=fig.title.text, original_ticks=len(base_ticks), displayed_ticks=len(axis.ticker.ticks)))
    return counts


'''
new=old.replace('def main():',helper+'def main():').replace('    layout, meta = build_bound_display()\n','    layout, meta = build_bound_display()\n    tick_style = install_readable_ticks(layout)\n').replace("                  position=meta['position'], boundary=meta['boundary'],","                  position=meta['position'], boundary=meta['boundary'], tick_style=tick_style,")
assert new!=old;p.write_text(new)
(e/'ENGINEERING_REPAIR.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='D011/run_definition.py',tofile='D012/final_script/run_definition.py')))
for n in ['f800.html','f800.runtime.json']:
 shutil.move(str(r/'caegraph-E'/n),str(a/('01-'+n)))
shutil.move(str(e/'screenshots'),str(a/'01-screenshots'))
for n in ['BROWSER_actual.json','BROWSER_expected.json','BROWSER_INSPECT.log']:
 shutil.move(str(e/n),str(a/('01-'+n)))
record=dict(repair_id='E-REPAIR-01',observed='真实三年全范围120m刻度过密，刻度线形成黑色条带；局部图与数据正常',evidence='attempts/01-screenshots/actual-full.png',classification='获准run-local显示工程修复；不改业务语义',basis='原C2当前允许依据实际输入的图宽/时间标签频率变化；原E Skill授权不改业务含义的工程处理',change='对每个x轴从原刻度/原标签中最多显示约10项；随共享x_range选择可见子集；深缩放沿原120m标签，不改时间值',unchanged=['真实实例/配置','B品种/三年范围/尺度/日历','字段与数据入口','原C3 renderer字节','全部CDS及业务图元','原时间标签值'],upstream_return_required=False,protected_platform_changed=False,installed_or_rebuilt=False,diff='ENGINEERING_REPAIR.diff',at=datetime.now(timezone.utc).isoformat())
(e/'ENGINEERING_REPAIRS.json').write_text(json.dumps({'repairs':[record],'preparation_issue':'首次内联准备脚本有括号语法错误，解释器在任何修改前拒绝；本文件修正后执行，不属于Feature或CAEGraph运行失败。'},ensure_ascii=False,indent=2)+'\n')
s=(e/'supervise_run.py').read_text();(a/'01-supervise_run.py').write_text(s)
s=s.replace("str(R.parent/'D011/run_definition.py')","str(R/'final_script/run_definition.py')").replace('attempt=1','attempt=2').replace('RUN_ATTEMPT01','RUN_ATTEMPT02');(e/'supervise_final.py').write_text(s)
print('Run-local tick-density repair prepared; original D and first result retained.')
