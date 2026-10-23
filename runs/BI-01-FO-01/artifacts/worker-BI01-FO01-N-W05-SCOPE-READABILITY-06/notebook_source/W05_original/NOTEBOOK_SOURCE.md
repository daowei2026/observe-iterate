# W05_original：精确有序cell源码

原件：b055102ad1a70b3c2824c2c6f5e540886deeb5f7:runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-UPLOT-NOTEBOOK-05/N_observation_Worker05.ipynb

Git blob：96c80e9e21205126f16ace68c9f9029d09206cdf；SHA256：50a8f9cfddd51ff00151e3c2f7490134591f01ce6fe4dde970d3321fe270ff8d；8175507 bytes。

下文保留每个cell的完整source，未压缩代码或Markdown。metadata和输出位置见INDEX.json及cells/*.json。大段保存JS/图像输出未展开；本文件不等于完整Notebook。

## Cell 0 / r0011-00 / markdown / execution_count=None

````markdown
# U2NormalNodeBehaviorFrp — Worker05 工作2现场Notebook

order_id=BI01-FO01-N-UPLOT-NOTEBOOK-05；签发BI01-FO-01-R0014-20261023T153303Z-57f340f3。
从P11真实代码候选修订；下方输出由本次新kernel产生。正式来源是W02/W03锁定OnlyRead导出，未重算N、未加载旧图。

本Notebook消费同目录DISPLAY_PLAN.json v0.3.1-worker05。Restart Kernel → Run All后可切换rb/i的K及rb范围，使用图上的hover、平移、缩放、复位和图例。
稀疏知识切点只画真实点；不将三处切点冒充连续433发生。真实行情路径保留缺价，不插值。历史同bar close不是开盘瞬时已知认证。
运行环境和实际验证见同目录README、FULL_RESPONSE与evidence；技术结果交原Pro判断和管理接收。
````

## Cell 1 / r0011-01 / code / execution_count=1

````python
from pathlib import Path
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
````

## Cell 2 / r0011-02 / markdown / execution_count=None

````markdown
## 正式来源与运行版本
仅读取本地 Git 中的指定不可变版本；不访问网络、不重算 N、不修改共享源码。完整生产配置沿原 R30，下面的观察范围不是生产参数。运行时应保留实际导入路径、HEAD及影响运行的既有未提交差异；不能仅凭HEAD声称干净锁定。
````

## Cell 3 / r0011-03 / code / execution_count=2

````python
from pathlib import Path
from functools import lru_cache
import io, os, subprocess, inspect, hashlib
import pandas as pd
import mquant.uplot as uplot
import mquant.aidata.u2_normal_node_behavior_display as nd
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
for module in (uplot, nd):
    path = Path(inspect.getfile(module)).resolve()
    print(module.__name__, str(path), hashlib.sha256(path.read_bytes()).hexdigest())

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
````

## Cell 4 / r0011-04 / markdown / execution_count=None

````markdown
## rb：知识切点演变与回看
第一幅只比较三个已取切点，不等同连续433发生。随后通过选择器重新构建选定K图；可观察确认前/后成员及working变化。重新运行同一个K也重新调用Uplot，不从历史页面载入图。
````

## Cell 5 / r0011-05 / code / execution_count=3

````python
def new_selected(tables, price, symbol, K):
    bundle = nd.build_selected_cut_bundle(tables, price, symbol=symbol,
        color=PLAN["instrument_colors"][symbol], as_of=int(K),
        optional_panels=tuple(PLAN["optional_panels"] + (["duration"] if symbol == "i" else [])))
    assert int(bundle.meta["resolved_origin_as_of"]) <= K
    assert int(bundle.price["open_uti"].max()) <= K
    bundle.meta["formal_entry"] = "Pinned normal-OnlyRead export reuse; not a fresh Feature read"
    bundle.meta["display_identity"]["worker05_plan"] = PLAN["version"]
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
    bundle.meta["display_identity"]["worker05_plan"] = PLAN["version"]
    bundle.meta["display_identity"]["observed_Ks"] = sorted(Ks)
    return bundle

rb_cuts = {name: cut_tables(PLAN["source_refs"]["W02"], W02 + "data/selected_cuts/" + name + "/")
           for name in PLAN["rb_cuts"]}
rb_price = frame_at(PLAN["source_refs"]["W02"], W02 + "data/same_bound_price/rb_5m_price_calendar.csv", False)
rb_selected = {name: new_selected(rb_cuts[name], rb_price, "rb", K) for name, K in PLAN["rb_cuts"].items()}
rb_sparse = sparse_evolution(rb_cuts, rb_selected, rb_price, "rb", list(PLAN["rb_cuts"].values()))
render_new("rb_sparse_knowledge_cuts", rb_sparse)
````

## Cell 6 / r0011-06 / code / execution_count=4

````python
rb_K = widgets.Dropdown(options=[(name, name) for name in PLAN["rb_cuts"]], value="final", description="rb知识K")
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
````

## Cell 7 / r0011-07 / markdown / execution_count=None

````markdown
## i：缺价后部分恢复
三个知识切点同属原working。预期数据问题是 progress 恢复而 efficiency/counter仍缺，waiting=0而ratio缺分母。下面同时显示原字段状态；图形/标签若未充分表达局部重启与真实零，应在工作2修订直接消费者，再交Pro判断，不能仅凭表格宣布画法通过。
````

## Cell 8 / r0011-08 / code / execution_count=5

````python
i_cuts = {name: cut_tables(PLAN["source_refs"]["W03"], W03 + "data/crossk/" + name + "/")
          for name in PLAN["i_cuts"]}
i_price = frame_at(PLAN["source_refs"]["W02"], W02 + "data/i_missing_context/i_5m_price_calendar.csv", False)
i_selected = {name: new_selected(i_cuts[name], i_price, "i", K) for name, K in PLAN["i_cuts"].items()}
i_sparse = sparse_evolution(i_cuts, i_selected, i_price, "i", list(PLAN["i_cuts"].values()))
render_new("i_sparse_recovery", i_sparse)
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

## Cell 9 / r0011-09 / markdown / execution_count=None

````markdown
## hc：正式分母与close/影线的实际画图
原表及参考算术保持边界；下图读取本次相同原价，标出last_update处close3952、下一根close3946/high3959及末拍close3904。
等待258000、原近期三间隔中位数600与ratio430各用所属单位，不解释为概率。

本单交新图执行、必要交互与工作2接收材料回原Pro判断。原R11预检失败保留历史；本页无平台调用。
````

## Cell 10 / r0011-10 / code / execution_count=6

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

