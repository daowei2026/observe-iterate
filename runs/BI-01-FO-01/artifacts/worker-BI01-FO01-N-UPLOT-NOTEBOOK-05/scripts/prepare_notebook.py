"""从不可变P11候选生成本单运行副本；不修改原件，不实现绘图库。"""
from pathlib import Path
import hashlib
import json
import subprocess

REPO = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parents[1]
P11 = "a2c9f9333c6578b8bf1dd26fb589b1a6b2956ae9"
PREFIX = "runs/BI-01-FO-01/artifacts/professional-R0011/"

def raw(name):
    return subprocess.check_output(["git", "-C", str(REPO), "show", f"{P11}:{PREFIX}{name}"])

def source(cell, text):
    cell["source"] = text.splitlines(keepends=True)

plan = json.loads(raw("DISPLAY_PLAN.json"))
plan.pop("platform_acceptance")
plan["pending_real_display_changes"] = [x for x in plan["pending_real_display_changes"] if not x.startswith("normal platform pages")]
plan.update(version="0.3.1-worker05", status="WORK2_RUNTIME_CONFIGURATION_NOT_MANAGER_ACCEPTED",
            order_id="BI01-FO01-N-UPLOT-NOTEBOOK-05",
            issuer_invocation_id="BI01-FO-01-R0014-20261023T153303Z-57f340f3",
            optional_panels=["rhythm", "waiting_time"])
plan["runtime_version"] = "Recorded per actual kernel in evidence/EXECUTION_RUNTIME.json"
(OUT / "DISPLAY_PLAN.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n")
nb = json.loads(raw("N_observation_R0011.ipynb"))
cells = {c["id"]: c for c in nb["cells"]}
for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        cell.update(execution_count=None, outputs=[])
    cell["source"] = [s.replace("R0011 新绘制", "Worker05 本次新绘制") for s in cell["source"]]
source(cells["r0011-00"], """# U2NormalNodeBehaviorFrp — Worker05 工作2现场Notebook

order_id=BI01-FO01-N-UPLOT-NOTEBOOK-05；签发BI01-FO-01-R0014-20261023T153303Z-57f340f3。
从P11真实代码候选修订；下方输出由本次新kernel产生。正式来源是W02/W03锁定OnlyRead导出，未重算N、未加载旧图。

本Notebook消费同目录DISPLAY_PLAN.json v0.3.1-worker05。Restart Kernel → Run All后可切换rb/i的K及rb范围，使用图上的hover、平移、缩放、复位和图例。
稀疏知识切点只画真实点；不将三处切点冒充连续433发生。真实行情路径保留缺价，不插值。历史同bar close不是开盘瞬时已知认证。
运行环境和实际验证见同目录README、FULL_RESPONSE与evidence；技术结果交原Pro判断和管理接收。
""")
source(cells["r0011-01"], """from pathlib import Path
import sys, os, json, importlib.util, datetime, uuid
ARTIFACT_DIR = Path(os.environ.get("BI01_W05_ARTIFACT_DIR", ".")).resolve()
AIDATA_WORKTREE = Path(os.environ.get("BI01_W05_AIDATA", "/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-work2-r0014"))
# 沿已有只读运行overlay采用修后TIS/worker；aidata覆盖为本单独立分支。
sys.path.insert(0, "/tmp/bi01-fo01-w03-runtime-20261022")
import mquant
import tempfile
IMPORT_OVERLAY = Path(tempfile.mkdtemp(prefix="bi01-w05-import-"))
(IMPORT_OVERLAY / "aidata").symlink_to(AIDATA_WORKTREE, target_is_directory=True)
mquant.__path__.insert(0, str(IMPORT_OVERLAY))
missing = [name for name in ("mquant", "ipywidgets") if importlib.util.find_spec(name) is None]
if missing:
    raise RuntimeError("现场依赖缺：" + str(missing))
EXECUTION_ID = "W05-" + datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
print("本次新kernel执行", EXECUTION_ID, sys.executable)
""")
text = "".join(cells["r0011-03"]["source"])
text = text.replace('ARTIFACT_DIR = Path(os.environ.get("BI01_R11_ARTIFACT_DIR", ".")).resolve()', '# ARTIFACT_DIR 已由本单首单元设置')
text += """
import platform
EVIDENCE = ARTIFACT_DIR / "evidence"
EVIDENCE.mkdir(exist_ok=True)
RUNTIME = {"execution_id": EXECUTION_ID, "python": sys.version, "executable": sys.executable,
           "kernel": "m3py310", "plan_path": str(ARTIFACT_DIR / "DISPLAY_PLAN.json"), "plan_version": PLAN["version"],
           "aidata_worktree": str(AIDATA_WORKTREE), "modules": {}}
for mod in (uplot, nd):
    path = Path(inspect.getfile(mod)).resolve()
    RUNTIME["modules"][mod.__name__] = {"file": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
(EVIDENCE / "EXECUTION_RUNTIME.json").write_text(json.dumps(RUNTIME, ensure_ascii=False, indent=2))
LAYOUTS, BUNDLES, AUDITS = {}, {}, {}

def clean(value):
    import numpy as np
    if isinstance(value, dict): return {str(k): clean(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)): return [clean(v) for v in value]
    if isinstance(value, np.ndarray): return clean(value.tolist())
    if isinstance(value, (pd.Series, pd.Index)): return clean(value.tolist())
    if isinstance(value, np.generic): return clean(value.item())
    if value is pd.NA or value is pd.NaT: return None
    if isinstance(value, float) and not np.isfinite(value): return None
    if isinstance(value, (pd.Timestamp, datetime.datetime, datetime.date, Path)): return str(value)
    return value

def render_new(case, bundle):
    from bokeh.models import GlyphRenderer
    layout = nd.build_uplot_layout(bundle, context=context, calendar_name=PLAN["calendar"],
        title_suffix="Worker05 本次新绘制｜" + case)
    layout.name = "worker05:" + case
    layout.tags = ["worker05", "case:" + case, "execution:" + EXECUTION_ID]
    LAYOUTS[case], BUNDLES[case] = layout, bundle
    renderers = []
    for renderer in layout.select({"type": GlyphRenderer}):
        data = renderer.data_source.data
        renderers.append({"name": renderer.name, "tags": renderer.tags, "glyph": type(renderer.glyph).__name__, "data": clean(data)})
    AUDITS[case] = {"execution_id": EXECUTION_ID, "meta": clean(bundle.meta), "renderers": renderers}
    (EVIDENCE / "KERNEL_RENDERER_AUDIT.json").write_text(json.dumps(clean(AUDITS), ensure_ascii=False, indent=2))
    folder = ARTIFACT_DIR / "plot_view_data" / case
    nd.export_plot_view_data(bundle, folder)
    show(layout)
    return layout
"""
source(cells["r0011-03"], text)
text = "".join(cells["r0011-05"]["source"])
text = text.replace('optional_panels=tuple(PLAN["optional_panels"])', 'optional_panels=tuple(PLAN["optional_panels"] + (["duration"] if symbol == "i" else []))')
text = text.replace('bundle.meta["display_identity"]["r0011_plan"]', 'bundle.meta["display_identity"]["worker05_plan"]')
start = text.index('show(nd.build_uplot_layout(rb_sparse')
text = text[:start] + 'render_new("rb_sparse_knowledge_cuts", rb_sparse)\n'
source(cells["r0011-05"], text)
source(cells["r0011-06"], """rb_K = widgets.Dropdown(options=[(name, name) for name in PLAN["rb_cuts"]], value="final", description="rb知识K")
rb_range = widgets.Dropdown(options=[("完整已供成员/行情", "full"), ("确认附近局部行情", "local")], value="full", description="显示范围")
rb_out = widgets.Output()
def display_rb_cut(change=None):
    name, mode = rb_K.value, rb_range.value
    K = PLAN["rb_cuts"][name]
    price = rb_price if mode == "full" else rb_price[rb_price["open_uti"].between(103140000, K)]
    with rb_out:
        clear_output(wait=True)
        bundle = new_selected(rb_cuts[name], price, "rb", K)
        render_new("rb_" + name + "_" + mode, bundle)
rb_K.observe(display_rb_cut, names="value")
rb_range.observe(display_rb_cut, names="value")
display(widgets.HBox([rb_K, rb_range]), rb_out)
display_rb_cut()
""")
text = "".join(cells["r0011-08"]["source"])
start, end = text.index('show(nd.build_uplot_layout(i_sparse'), text.index('fields = ')
text = text[:start] + 'render_new("i_sparse_recovery", i_sparse)\n' + text[end:]
text += """
i_K = widgets.Dropdown(options=[(name, name) for name in PLAN["i_cuts"]], value="i_recovery", description="i知识K")
i_out = widgets.Output()
def display_i_cut(change=None):
    with i_out:
        clear_output(wait=True)
        name = i_K.value
        render_new(name, new_selected(i_cuts[name], i_price, "i", PLAN["i_cuts"][name]))
i_K.observe(display_i_cut, names="value")
display(i_K, i_out)
display_i_cut()
"""
source(cells["r0011-08"], text)
source(cells["r0011-09"], """## hc：正式分母与close/影线的实际画图
原表及参考算术保持边界；下图读取本次相同原价，标出last_update处close3952、下一根close3946/high3959及末拍close3904。
等待258000、原近期三间隔中位数600与ratio430各用所属单位，不解释为概率。

本单交新图执行、必要交互与工作2接收材料回原Pro判断。原R11预检失败保留历史；本页无平台调用。
""")
text = "".join(cells["r0011-10"]["source"])
text += """
hc_tables = cut_tables(hc_ref, hc_folder)
hc_bundle = new_selected(hc_tables, hc_price, "hc", K)
nd.add_price_reference_points(hc_bundle, [
    {"uti": last_update, "field": "close", "label": "last_update 原close3952"},
    {"uti": last_update+600, "field": "close", "label": "下一根close3946"},
    {"uti": last_update+600, "field": "high", "label": "下一根high3959（非close更新）"},
    {"uti": K, "field": "close", "label": "末拍close3904"},
])
render_new("hc_close_waiting_final", hc_bundle)
(EVIDENCE / "SOURCE_READS.json").write_text(json.dumps(SOURCE_READS, ensure_ascii=False, indent=2))
(EVIDENCE / "KERNEL_COMPLETION.json").write_text(json.dumps({"execution_id": EXECUTION_ID,
    "completed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "source_files": len(SOURCE_READS),
    "cases": list(LAYOUTS)}, ensure_ascii=False, indent=2))
print("实际正式源文件", len(SOURCE_READS), "；未重读生产N、未调用平台入口")
"""
source(cells["r0011-10"], text)
nb["metadata"].update(kernelspec={"display_name": "m3py310", "language": "python", "name": "m3py310"},
    worker_order={"order_id": plan["order_id"], "issuer_invocation_id": plan["issuer_invocation_id"],
                  "source_notebook_commit": P11, "source_notebook_blob": "cad0e3fb1cc9dbccd113410676bb2bddf55c33ce"})
nb['metadata']['bi01']={'invocation_id':plan['issuer_invocation_id'],'order_id':plan['order_id'],
    'plan':'DISPLAY_PLAN.json','execution_result':'以本次实际execution_count与evidence/KERNEL_COMPLETION.json为准',
    'qualification':'工作2现场运行副本；专业判断和管理接收分别由原责任者完成'}
(OUT / "N_observation_Worker05.ipynb").write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n")
(OUT / "evidence").mkdir(exist_ok=True)
(OUT / "evidence" / "CANDIDATE_PROVENANCE.json").write_text(json.dumps({name: {
    "commit": P11, "path": PREFIX+name, "sha256": hashlib.sha256(raw(name)).hexdigest()}
    for name in ("N_observation_R0011.ipynb", "DISPLAY_PLAN.json")}, indent=2))
print(OUT)
