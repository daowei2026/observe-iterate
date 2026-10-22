# BI01-FO01-N-DISPLAY-INTEGRATION-02｜标量交付一致性补充

补充标记：`BI01-FO01-W02-SCALAR-CONSISTENCY-20261022`

原 order_id：`BI01-FO01-N-DISPLAY-INTEGRATION-02`

实际检查来源：`observe-iterate@39308f4a8fe6b6f2fe1399f8d9e56b91a5ceb643:runs/BI-01-FO-01/artifacts/worker-BI01-FO01-N-DISPLAY-INTEGRATION-02/`

返回目标仍为：`chatgpt:细节叙事生成_金标:BI01-FO01-执行`

技术状态：`SUPPLEMENT_TECHNICAL_RETURN_READY`

## 一、结论

主控对旧末拍 PNG 的观察指向了真实交付缺陷，不是视觉误会。直接解包旧发布 commit `39308f4a8fe6b6f2fe1399f8d9e56b91a5ceb643` 的 Bokeh HTML 后确认：

- 确认前页面的九个标量 CDS 与自身正式投影一致；
- 确认时和末拍页面的九个标量 CDS 全部复用了确认前页面的整行数据；
- 被复用的不只是 x/exact，也包括 y、as_of、origin、state 和 meaning；
- 旧末拍 HTML 因而实际保存了 `0.1434665771 / 0.1335430476`、`43 / 66`、working efficiency `0.0685805423`、waiting ratio `155`，而非末拍正式值。

这个真实问题已由 R8 endpoint 补充中的 aidata commit `28260d3ec5d2ed254b2539cb9abc656e4737f80b` 修复。当前发布的三个 selected HTML/PNG 是同一进程按确认前、确认时、末拍顺序重建的结果；本次没有再次改代码或重绘，而是对这些实际保存实物执行独立逐字段审计。

当前结果：三页各九个标量 CDS 均与本页 `plot_view_data` 一致；九个投影值又分别与本页既有正式表一致；K、exact、origin、状态和数值均属本页，且价格和所有特征坐标均不晚于 K。

## 二、逐页标量结果

下面数值同时满足“正式表 → 图用 CSV → 当前 HTML/CDS”三层一致。旧 HTML 列用于保留原失败证据。

|页面 / K|近期/此前完成效率|working 推进/逆向量|working 效率|waiting ratio|旧 HTML 与本页投影|当前 HTML 与本页投影|
|---|---|---|---:|---:|---:|---:|
|确认前 / 103150800|0.1434665771 / 0.1335430476|43 / 66|0.0685805423|155|9/9|9/9|
|确认时 / 103151400|0.1514170159 / 0.0845431993|53 / 40|0.1075050710|82|0/9|9/9|
|末拍 / 103315800|0.1514170159 / 0.0845431993|50 / 80|0.0377643505|15.8461538462|0/9|9/9|

九项还包括近期/此前完成时长和 working 年龄；完整原值、表名、行选择器及每个字段的比较结果在 `evidence/SCALAR_DISPLAY_CONSISTENCY_CHECK.json`。

末拍当前 HTML 中的 source exact 为：

```text
NodeBehaviorBook/NodeScaleTurnBehaviorRevision/b340dc6c-c135-462b-b6e0-04d24622c180/cfd51328-e2cf-4360-8314-20c9238e93fb
```

九个标量 x/as_of/origin 均为 `103315800`。working efficiency 与 waiting ratio 的当前 renderer 各有一条正式值，不是空 CDS。单点面板在整段共享时间轴上视觉稀疏，不能仅凭像素空白感判定缺值；数值正确性以保存 HTML 内的实际 renderer CDS 和同源 CSV 为准，像素检查只验证页面确实渲染。

## 三、检查方法与证据边界

新增 `scripts/audit_scalar_display_consistency.py`，实际执行以下读取：

1. 从 Git commit `39308f4…` 读取旧三页 HTML/PNG；
2. 从当前工作树读取 R8 后三页 HTML/PNG；
3. 解包每页真实 Bokeh Document 和带 `aidata_evidence` tag 的 renderer CDS；
4. 读取每页九个 `plot_view_data/n_display__*.csv`；
5. 独立从 `data/selected_cuts/<cut>/metrics.csv`、`working_progress.csv`、`working_counter.csv`、`working_efficiency.csv`、`working_duration.csv`、`working_waiting_ratio.csv` 选择正式值；
6. 对 x、y、symbol、source_exact、as_of_uti、origin_uti、state_text、meaning 逐字段比较；
7. 同时核 plot price 截止 K、所有实际 feature renderer 无 K 后坐标、PNG 与浏览器 capture 摘要一致。

审计结果为 `PASS`：旧顺序复用模式实际重现，当前三页全部通过。证据文件 SHA-256：

```text
evidence/SCALAR_DISPLAY_CONSISTENCY_CHECK.json
85eee3862884e33c6f28757a673c95ec6346e1fbd1f28e4fa67954f7a26abd58

scripts/audit_scalar_display_consistency.py
017ad26ee18fbcd449cad1c4a4875621d83f48467ea340107d98cb0b25c0a2ac
```

第一次误用聊天默认 `/usr/bin/python` 时因缺少 `numpy` 得到 `ModuleNotFoundError`；随后使用原 Worker02 已记录的 `/dwdhome/fy/BASE_E6_2/run-python.sh` 同一运行环境成功。没有安装新依赖、重读 N 或更换数据。

## 四、变更与未变范围

本挑战无需新的 aidata 改动；继续引用已经 GitHub fresh 回读的修复提交 `28260d3ec5d2ed254b2539cb9abc656e4737f80b`。当前三页 HTML/PNG、对应投影 CSV及其哈希也不需再次变化；它们是 R8 已顺序重建并通过本次独立审计的实际发布实物。

本次仅新增这份补充、独立审计脚本和结构化审计结果，并将该检查接入最终包装验证、运行清单、交付清单和 GitHub 回执。旧错误 HTML/PNG 不被覆盖或删除，继续由 Git commit `39308f4…` 和修前审计证据恢复。

本结论只覆盖本次三个 rb selected-cut 页面及配置中的九类标量，不扩展为所有 aidata caller 正确性，也不代替执行 Pro 的图形解释或管理接受。没有修改正式值/K、TIS、FRP、core、SDK 或 uplot 源码；没有执行手机操作、业务观察或后继任务。
