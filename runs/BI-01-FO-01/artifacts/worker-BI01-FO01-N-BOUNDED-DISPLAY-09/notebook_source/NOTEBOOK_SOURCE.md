# Worker09 实际保存Notebook：精确有序源码

原文件：N_observation_Worker09.ipynb；bytes=7886673；SHA256=6a5186b44b9dcbd2adb7639eb965998f4b1e3b6b0dd4de2fa3a0206f2980049c。

此文本不是完整Notebook：不展开大段内嵌JS/widget/图形输出。每个cell的source逐字保留；输出仅列类型/MIME/错误与hash，完整输出仍在主ipynb。

## 0. r0011-00 / markdown / execution_count=None

metadata: {}

````markdown
# U2NormalNodeBehaviorFrp — Worker09 有限共用展示Notebook

order_id=BI01-FO01-N-BOUNDED-DISPLAY-09；签发BI01-FO-01-R0035-20261024T185441Z-1c7e5a8c。
从W06已执行确切主Notebook（blob58f7b27b）派生，保留原有序cell谱系，旧输出全部清除；下方输出仅属于本次新kernel。
N领域模块准备原表关联/合法K/状态，唯一机械组合为aidata.evidence_composition，Notebook与正常CAE/bridge消费同一路径。
默认画M21已认可的rb末拍完整/局部、i恢复和hc末拍。其他K选择明确仅为工作2准备/回归，未获对应平台用途认可；不造连续历史或保持线。
主交付是实际执行可交互的Notebook，不是旧HTML/PNG。技术结果回原Pro；未自行完成共享发布、工作3接收或正式工作4。
Restart Kernel → Run All；rb范围选择、hover、图例、平移/缩放/复位按实际操作留证。历史同bar close不是开盘瞬时已知认证。
````

输出索引：[]

## 1. r0011-01 / code / execution_count=1

metadata: {}

````python
import logging
logging.disable(logging.CRITICAL)
from pathlib import Path
import sys, os, json, importlib.util, datetime, uuid
ARTIFACT_DIR = Path(os.environ.get("BI01_W09_ARTIFACT_DIR", ".")).resolve()
AIDATA_WORKTREE = Path(os.environ.get("BI01_W09_AIDATA", "/dwdhome/fy/BASE_E6_2/mquant/aidata-bi01-fo01-n-bounded-display-r0035"))
# 沿已有只读运行overlay采用修后TIS/worker；aidata覆盖为本单独立分支。
sys.path.insert(0, "/tmp/bi01-fo01-w03-runtime-20261022")
import mquant
import tempfile
IMPORT_OVERLAY = Path(tempfile.mkdtemp(prefix="bi01-w09-import-"))
(IMPORT_OVERLAY / "aidata").symlink_to(AIDATA_WORKTREE, target_is_directory=True)
mquant.__path__.insert(0, str(IMPORT_OVERLAY))
missing = [name for name in ("mquant", "ipywidgets") if importlib.util.find_spec(name) is None]
if missing:
    raise RuntimeError("现场依赖缺：" + str(missing))
EXECUTION_ID = "W09-" + datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
print("本次新kernel执行", EXECUTION_ID, sys.executable)
````

输出索引：[{"position": 0, "output_type": "stream", "mime_types": [], "ename": null, "bytes_json": 148, "sha256_json": "8053f551153288a672ac8125884b828ec982dbd3164edb7cd1de1953cc417071"}]

## 2. r0011-02 / markdown / execution_count=None

metadata: {}

````markdown
## 正式来源与运行版本
仅读取本地 Git 中的指定不可变版本；不访问网络、不重算 N、不修改共享源码。完整生产配置沿原 R30，下面的观察范围不是生产参数。运行时应保留实际导入路径、HEAD及影响运行的既有未提交差异；不能仅凭HEAD声称干净锁定。
````

输出索引：[]

## 3. r0011-03 / code / execution_count=2

metadata: {}

````python
from pathlib import Path
from functools import lru_cache
import io, os, subprocess, inspect, hashlib
import pandas as pd
import mquant.uplot as uplot
import mquant.aidata.u2_normal_node_behavior_display as nd
import mquant.aidata.evidence_composition as ec
from mquant.quant import OptContext
from bokeh.io import output_notebook, show
from bokeh.resources import INLINE
from IPython.display import display, clear_output
import ipywidgets as widgets

# ARTIFACT_DIR 已由本单首单元设置
PLAN = json.loads((ARTIFACT_DIR / "DISPLAY_PLAN.json").read_text(encoding="utf-8"))
REPO = Path(os.environ.get("OBSERVE_REPO", "/dwdhome/fy/observe-iterate-bi01-fo-01")).resolve()
if not REPO.is_dir():
    raise FileNotFoundError(f"实际仓库不存在：{REPO}")
W02 = "runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-DISPLAY-INTEGRATION-02/"
W03 = "runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-READABILITY-CROSSK-03/"
SOURCE_READS = {}
@lru_cache(maxsize=160)
def source_bytes(ref, path):
    result = subprocess.run(["git", "-C", str(REPO), "show", f"{ref}:{path}"], capture_output=True, check=True)
    raw = result.stdout
    SOURCE_READS[f"{ref}:{path}"] = hashlib.sha256(raw).hexdigest()
    return raw

def frame_at(ref, path, formal=True):
    frame = pd.read_csv(io.BytesIO(source_bytes(ref, path)), dtype="string")
    time_col = "timestamp" if formal else frame.columns[0]
    frame[time_col] = pd.to_datetime(frame[time_col])
    for col in frame.columns:
        if col == time_col:
            continue
        if col == "text" or col.endswith("_text"):
            frame[col] = frame[col].fillna("")
        elif col.endswith("_high") or col.endswith("_low"):
            frame[col] = pd.array(frame[col], dtype="UInt64")
        else:
            try:
                frame[col] = pd.to_numeric(frame[col], errors="raise")
            except (ValueError, TypeError):
                pass
    if not formal:
        return frame.set_index(time_col)
    children = sorted([c for c in frame if c.startswith("child_id_")], key=lambda c: int(c.rsplit("_", 1)[1]))
    return frame.set_index(["timestamp", "occurrence", "record_id", *children])

def cut_tables(ref, folder):
    return {name: frame_at(ref, folder + name + ".csv") for name in nd.FORMAL_PRODUCTS}

def merge_real_cuts(cuts):
    result = {}
    for key in nd.FORMAL_PRODUCTS:
        frames = [tables[key] for tables in cuts.values()]
        names = list(frames[0].index.names)
        merged = pd.concat(frames).reset_index().drop_duplicates()
        if merged.duplicated(names).any():
            raise ValueError(f"同原表坐标内容冲突：{key}；不得按最新值覆盖")
        result[key] = merged.set_index(names).sort_index()
    return result

context = OptContext(sof_name=PLAN["sof_name"])
output_notebook(resources=INLINE, hide_banner=True)
for module in (uplot, nd, ec):
    path = Path(inspect.getfile(module)).resolve()
    print(module.__name__, str(path), hashlib.sha256(path.read_bytes()).hexdigest())

import platform
EVIDENCE = ARTIFACT_DIR / "evidence"
EVIDENCE.mkdir(exist_ok=True)
RUNTIME = {"execution_id": EXECUTION_ID, "python": sys.version, "executable": sys.executable,
           "kernel": "python3", "plan_path": str(ARTIFACT_DIR / "DISPLAY_PLAN.json"), "plan_version": PLAN["version"],
           "aidata_worktree": str(AIDATA_WORKTREE), "modules": {}}
for mod in (uplot, nd, ec):
    path = Path(inspect.getfile(mod)).resolve()
    RUNTIME["modules"][mod.__name__] = {"file": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
(EVIDENCE / "EXECUTION_RUNTIME.json").write_text(json.dumps(RUNTIME, ensure_ascii=False, indent=2))
RUNTIME["order_id"] = "BI01-FO01-N-BOUNDED-DISPLAY-09"
RUNTIME["actual_aidata_head"] = subprocess.check_output(["git","-C",str(AIDATA_WORKTREE),"rev-parse","HEAD"]).decode().strip()
(EVIDENCE / "EXECUTION_RUNTIME.json").write_text(json.dumps(RUNTIME,ensure_ascii=False,indent=2))
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
        title_suffix="Worker09 本次新绘制｜" + case + ("｜M21具名切面" if case in ("rb_final_full","rb_final_local","i_recovery","hc_close_waiting_final") else "｜仅工作2准备/回归，未获平台用途认可"))
    layout.name = "worker09:" + case
    layout.tags = [*layout.tags, "worker09", "case:" + case, "execution:" + EXECUTION_ID]
    LAYOUTS[case], BUNDLES[case] = layout, bundle
    renderers = []
    for renderer in layout.select({"type": GlyphRenderer}):
        data = renderer.data_source.data
        renderers.append({"name": renderer.name, "tags": renderer.tags, "glyph": type(renderer.glyph).__name__, "data": clean(data) if "anchor:n_display/" in str(renderer.tags) and "anchor:n_display/close_path" not in str(renderer.tags) else {"qualification": "原价大数组不在kernel审计展开；按源Git与实际浏览器定向切片核对"}})
    AUDITS[case] = {"execution_id": EXECUTION_ID, "meta": clean(bundle.meta), "renderers": renderers}
    (EVIDENCE / "KERNEL_RENDERER_AUDIT.json").write_text(json.dumps(clean(AUDITS), ensure_ascii=False, indent=2))
    folder = ARTIFACT_DIR / "plot_view_data" / case
    if case in ("rb_final_full", "rb_final_local", "i_recovery", "hc_close_waiting_final"):
        nd.export_plot_view_data(bundle, folder)
    show(layout)
    return layout
````

输出索引：[{"position": 0, "output_type": "display_data", "mime_types": ["application/javascript", "application/vnd.bokehjs_load.v0+json"], "ename": null, "bytes_json": 7574259, "sha256_json": "b7d74e48621e4d9f41e21d6226e8836df28c4bc9fac1a94e41acdb486c22e6b6"}, {"position": 1, "output_type": "stream", "mime_types": [], "ename": null, "bytes_json": 603, "sha256_json": "001ca923c81adf9cb032b3d2f9627627361e8289af40b4294c9053a4b11d8d18"}]

## 4. r0011-04 / markdown / execution_count=None

metadata: {}

````markdown
## rb：固定末拍与范围切换
默认画末拍。其他已取知识K若选择，仅作工作2回归/准备，不扩平台认可；不画稀疏点之间的假保持线。
````

输出索引：[]

## 5. r0011-05 / code / execution_count=3

metadata: {}

````python
def new_selected(tables, price, symbol, K, display_range=None):
    bundle = nd.build_selected_cut_bundle(tables, price, symbol=symbol,
        color=PLAN["instrument_colors"][symbol], as_of=int(K), display_range=display_range,
        optional_panels=tuple(PLAN["optional_panels"] + (["duration"] if symbol == "i" else [])))
    assert int(bundle.meta["resolved_origin_as_of"]) <= K
    assert int(bundle.price["open_uti"].max()) <= K
    bundle.meta["formal_entry"] = "Pinned normal-OnlyRead export reuse; not a fresh Feature read"
    bundle.meta["display_identity"]["worker09_plan"] = PLAN["version"]
    return bundle

def sparse_evolution(cuts, selected, price, symbol, Ks):
    bundle = nd.build_evolution_bundle(merge_real_cuts(cuts), price, symbol=symbol,
        color=PLAN["instrument_colors"][symbol], start_uti=min(Ks), end_uti=max(Ks),
        optional_panels=tuple(PLAN["optional_panels"] + (["duration"] if symbol == "i" else [])))
    for name in bundle.views:
        if name.endswith("_hold") or name.endswith("_steps"):
            bundle.views[name] = bundle.views[name].iloc[0:0].copy()
        elif name.endswith("_updates") or name.endswith("_points"):
            bundle.views[name] = pd.concat([b.views[name] for b in selected.values()], ignore_index=True)
    bundle.meta["formal_entry"] = "Sparse pinned knowledge-cut exports; NOT continuous occurrence history"
    bundle.meta["display_identity"]["worker09_plan"] = PLAN["version"]
    bundle.meta["display_identity"]["observed_Ks"] = sorted(Ks)
    return bundle

rb_cuts = {name: cut_tables(PLAN["source_refs"]["W02"], W02 + "data/selected_cuts/" + name + "/")
           for name in PLAN["rb_cuts"]}
rb_price = frame_at(PLAN["source_refs"]["W02"], W02 + "data/same_bound_price/rb_5m_price_calendar.csv", False)
rb_selected = {name: new_selected(rb_cuts[name], rb_price, "rb", K) for name, K in PLAN["rb_cuts"].items()}
# 如确需其他演变，按真实范围另作工作2；当前四视域不依赖该布局。
# 保留准确稀疏准备代码谱系，但本次默认不执行额外画法/扩大平台范围。

# 真实不同K、完全相同价窗的缓存/读数作用域回归；仅工作2技术准备，不作平台发布。
same_window=(103140000, min(PLAN["rb_cuts"].values()))
scope_results=[]
for label in ("before_confirmation","at_or_after_confirmation"):
    k=PLAN["rb_cuts"][label]
    sample=new_selected(rb_cuts[label],rb_price,"rb",k,display_range=same_window)
    actual=nd.build_uplot_layout(sample,context=context,calendar_name=PLAN["calendar"],title_suffix="同价窗不同K技术回归；未获平台用途认可")
    from bokeh.models import GlyphRenderer
    observed={}
    for renderer in actual.select({"type":GlyphRenderer}):
        names=[t[5:] for t in renderer.tags if isinstance(t,str) and t.startswith("view:")]
        if names and names[0] in ("completed_recent_updates","working_progress_points"):
            observed[names[0]]=clean(renderer.data_source.data)
            assert list(renderer.data_source.data["x"])==[k]
            assert list(renderer.data_source.data["y"])==sample.views[names[0]]["y"].tolist()
    assert len(observed)==2
    scope_results.append({"K":k,"price_range":sample.meta["price_range"],"exact":sample.meta["source_exact"],"display_identity":nd.U2NormalNodeBehaviorDisplayFeature(sample).ppid,"actual_scalar_renderers":observed})
assert scope_results[0]["price_range"]==scope_results[1]["price_range"]
assert scope_results[0]["display_identity"]!=scope_results[1]["display_identity"]
(EVIDENCE/"SAME_PRICE_DIFFERENT_K.json").write_text(json.dumps({"execution_id":EXECUTION_ID,"qualification":"真实原表/实际组合器图层；仅工作2技术回归，非新增平台认可", "results":scope_results},ensure_ascii=False,indent=2))
````

输出索引：[{"position": 0, "output_type": "execute_result", "mime_types": ["text/plain"], "ename": null, "bytes_json": 105, "sha256_json": "9ac47362a78a3105aff63337e13e8a0750697ee3f42cf38e5ceb42c640a899c3"}]

## 6. r0011-06 / code / execution_count=4

metadata: {}

````python
rb_K = widgets.Dropdown(options=[(name, name) for name in PLAN["rb_cuts"]], value="final", description="rb知识K")
rb_range = widgets.Dropdown(options=[("完整已供成员/行情", "full"), ("确认附近局部行情", "local")], value="full", description="显示范围")
rb_out = widgets.Output()
def display_rb_cut(change=None):
    name, mode = rb_K.value, rb_range.value
    K = PLAN["rb_cuts"][name]
    display_range = None if mode == "full" else (103140000, K)
    with rb_out:
        clear_output(wait=True)
        bundle = new_selected(rb_cuts[name], rb_price, "rb", K, display_range=display_range)
        render_new("rb_" + name + "_" + mode, bundle)
rb_K.observe(display_rb_cut, names="value")
rb_range.observe(display_rb_cut, names="value")
display(widgets.HBox([rb_K, rb_range]), rb_out)
display_rb_cut()
````

输出索引：[{"position": 0, "output_type": "display_data", "mime_types": ["application/vnd.jupyter.widget-view+json", "text/plain"], "ename": null, "bytes_json": 328, "sha256_json": "a3152ae004057b246f5c1b356714b78eb3bd3afe68733d472575d6cf48e04b69"}, {"position": 1, "output_type": "display_data", "mime_types": ["application/vnd.jupyter.widget-view+json", "text/plain"], "ename": null, "bytes_json": 219, "sha256_json": "64fb0d7a53e3207577ee17939a97e1aeeaef7f153883ecadad954591ddcac063"}]

## 7. r0011-07 / markdown / execution_count=None

metadata: {}

````markdown
## i：恢复拍真零与缺量
默认恢复K35361000；其他已取K选择仅工作2回归/准备，不作平台用途。推进/年龄可用，路径量缺；等待真零与分母缺各自显示。
````

输出索引：[]

## 8. r0011-08 / code / execution_count=5

metadata: {}

````python
i_cuts = {name: cut_tables(PLAN["source_refs"]["W03"], W03 + "data/crossk/" + name + "/")
          for name in PLAN["i_cuts"]}
i_price = frame_at(PLAN["source_refs"]["W02"], W02 + "data/i_missing_context/i_5m_price_calendar.csv", False)
i_selected = {name: new_selected(i_cuts[name], i_price, "i", K) for name, K in PLAN["i_cuts"].items()}
# 不把三切点合成连续时间历史。
# 默认仅通过下方选择器显示真实恢复拍。
fields = ("working_progress", "working_efficiency", "working_counter", "working_duration", "working_waiting", "working_waiting_ratio")
status_rows = []
for label, tables in i_cuts.items():
    for field in fields:
        for row in tables[field].reset_index().to_dict("records"):
            status_rows.append({"cut": label, "K": PLAN["i_cuts"][label], "field": field,
                **{key: row.get(key) for key in ("value", "present", "knownness", "applicability", "reason")}})
display(pd.DataFrame(status_rows))
# These original fields are audit support. They do not substitute for checking
# whether the NEW graphic makes the missing/zero/local-restart distinction clear.

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
````

输出索引：[{"position": 0, "output_type": "display_data", "mime_types": ["text/html", "text/plain"], "ename": null, "bytes_json": 8197, "sha256_json": "549838f11f22870b582070b9ce19bf3ec58c639df8fc5464fd57e41ee0bf73d0"}, {"position": 1, "output_type": "display_data", "mime_types": ["application/vnd.jupyter.widget-view+json", "text/plain"], "ename": null, "bytes_json": 328, "sha256_json": "7d98f6328c3c697e5bf30153c6bdfe21c370b29615f76f8d5701dfffa8a14c59"}, {"position": 2, "output_type": "display_data", "mime_types": ["application/vnd.jupyter.widget-view+json", "text/plain"], "ename": null, "bytes_json": 219, "sha256_json": "07b10e50a45e3ec3406b609a7f9e4a9711bbb3d6d94fc1049bffb52073dd1d2a"}]

## 9. r0011-09 / markdown / execution_count=None

metadata: {}

````markdown
## hc：正式分母与close/影线的实际画图
原表及参考算术保持边界；下图读取本次相同原价，标出last_update处close3952、下一根close3946/high3959及末拍close3904。
等待258000、原近期三间隔中位数600与ratio430各用所属单位，不解释为概率。

本单交新图执行、必要交互与工作2接收材料回原Pro判断。原R11预检失败保留历史；本页只验证共用组合；正常CAE/bridge冷恢复及平台采用权限另见本单完整回交。
````

输出索引：[]

## 10. r0011-10 / code / execution_count=6

metadata: {}

````python
hc_ref = PLAN["source_refs"]["W03"]
hc_folder = W03 + "data/crossk/hc_final/"
hc_price = frame_at(hc_ref, hc_folder + "hc_5m_price_calendar.csv", False)
hc_rhythm = frame_at(hc_ref, hc_folder + "rhythm.csv").reset_index()
hc_intervals = frame_at(hc_ref, hc_folder + "intervals.csv").reset_index().sort_values("child_id_3")
assert hc_intervals["present"].eq(1).all()
denominator = float(hc_intervals.tail(3)["duration"].median())
assert denominator == float(hc_rhythm.iloc[0]["current_median_value"])
K = int(hc_price["open_uti"].max())
last_update = int(hc_rhythm.iloc[0]["last_update_value"])
print({"formal_recent_intervals": hc_intervals.tail(3)["duration"].tolist(),
       "formal_median": denominator, "waiting_reference": K-last_update,
       "ratio_reference": (K-last_update)/denominator,
       "qualification": "reference arithmetic beside formal tables; no new production N"})
print("实际核源文件数", len(SOURCE_READS))

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
````

输出索引：[{"position": 0, "output_type": "stream", "mime_types": [], "ename": null, "bytes_json": 303, "sha256_json": "2e1134e6e28500f9b0f6dae85b96dd20e44c5b639884d07a0e1a5f2b5a9d0145"}, {"position": 1, "output_type": "display_data", "mime_types": ["text/html"], "ename": null, "bytes_json": 193, "sha256_json": "b5bc559bc10c2758a28111788ebbe40885e2f4f553578f99de621cf82bf4fdd2"}, {"position": 2, "output_type": "display_data", "mime_types": ["application/javascript", "application/vnd.bokehjs_exec.v0+json"], "ename": null, "bytes_json": 263817, "sha256_json": "4b77b673ef8cbd1951eca1acc8ddaa40de0d77e9e1d8e7b37499413db1f9408e"}, {"position": 3, "output_type": "stream", "mime_types": [], "ename": null, "bytes_json": 128, "sha256_json": "3e00cd4cedfcc32644ab7e60b85c641de894627c7fccf074db8418d57b8fb14e"}]
