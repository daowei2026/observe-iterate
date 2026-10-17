# 当前图数的技术回用

当前代码为 aidata 独立分支 `codex/bi01v2-r0004-fixed-input` 的 `e59fd90de5237b8a6756de00e54bdf841832fad4`；main 保持原提交。两份 patch 记录新增通用只读固定输入能力及精确整数键修补。初次建节点时的实际未提交状态保留在 RUN_EXECUTION.json，当前回用状态见 AIDATA_CODE_REUSE.json，不能混写。

本机两个提交均已在上述独立分支保存，未推送远端。另一工作区如需回用，应从原 `9ff7ce4929b36945f63b1c9875e59f68141f997a` 建新独立分支，依次应用 `aidata-428c70f.patch`、`aidata-e59fd90.patch`，并对照 AIDATA_CODE_REUSE.json 的实际模块 SHA；不要直接修改受保护 main。

当前 run 为 `BI01V2_R0004_fixed_20261018_033648`，本机目录为 `/dwdhome/fy/BASE_E6_2/.runtime/bi01-v2-r0004/aidata_runs/BI01V2_R0004_fixed_20261018_033648`。现有 Trier 服务和图节点继续使用此 run。读取现成图数不需要重新建图或运行 Feature。

当前代码对应的服务进程启动记录为 `2026-10-17T20:03:21.281401+00:00`；首个当前版本真实Bokeh坐标核验开始于 `2026-10-18T04:04:26+08:00`。启动时间只记进程事实，不冒充就绪证明；各视图实际核验时间见当前索引的 validated_at／bokeh_verified_at。范围和As-Of仍按各VIEW原参数；代码修补后的内容适用于新打开的会话，之前已打开的旧会话应重新打开再与当前数据配套读取。

`CURRENT_PARAMETERS.zip` 保存当前 run 的原字节 `manifest/fixed_input.json`，SHA 见 CURRENT_EXECUTION_EVIDENCE.json。它包含全部源成员身份、320 个节点的人工范围／As-Of、逐层原物理行及精确显示连接。输入路径仍指向工单指定的资金管理目录，没有打包替换来源。各图自己的 VIEW.json 和 SOURCE_BINDING.json 同时保留在各自数据包，不能拿不同范围的 CSV 相互替代。

本机已有环境通过 `/dwdhome/fy/BASE_E6_2/run-python.sh` 调用。当前代码的实际公共入口为：

```python
from pathlib import Path
from mquant.aidata.contracts import build_run_handle
from mquant.aidata.api import render_review_nodes, export_plot_view_data

run = build_run_handle(Path("/dwdhome/fy/BASE_E6_2/.runtime/bi01-v2-r0004/aidata_runs/BI01V2_R0004_fixed_20261018_033648"))
rendered = render_review_nodes(run, node_ids=["MAIN_ASOF_3"])
layout = rendered.rendered_objects[0]
# 如另行导出，使用新request_id，避免覆盖本次已固定hash的数据。
manifest = export_plot_view_data(run, "separate_readback_MAIN_ASOF_3", plot_roots=layout)
```

这条路径使用真实 aidata consumer 及原图 ColumnDataSource。CSV 的 shared_view／非 primary evidence 合同仍保留；固定原结果及来源资格没有被绘图工具升级为正式业务结论。

有限执行脚本位于 aidata 的 gitignored `test_runs/bi01-v2-r0004/`，只负责参数、调用、核验和回交，不是另一个绘图引擎。`build.py` 已实际运行一次产生320节点，不应为了读取当前结果再次执行。当前汇总 `assemble.py --final` 仅在320当前包及51真实请求会话全部通过后生成正式技术回交；没有无限重试、常驻轮询或旧Goal恢复。

本次全部真实结果由 CURRENT_VIEW_VERSION_INDEX.csv 定位；每层范围／As-Of／可见性由 LAYER_DISPLAY_SCOPE_INDEX.csv 定位。未完成业务与来源判断由原专业及管理处理。若后续改变源层或代码，必须另记实际生效时间、参数及代码指纹和新包 hash，保留本次版本，不能继续引用旧144或中间146 CSV快照代表当前图。

PUBLICATION_FILE_MANIFEST.json 明确列出主控可发布的当前文件及字节 SHA。attempts 是历史证据，不作为当前通过计数；私有运行日志、凭据和设备记录不在发布清单。Worker未提交／推送共享 observe 工作树。
