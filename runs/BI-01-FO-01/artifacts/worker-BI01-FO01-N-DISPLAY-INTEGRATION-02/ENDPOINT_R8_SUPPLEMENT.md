# BI01-FO01-N-DISPLAY-INTEGRATION-02｜R8 右边界补充回交

补充标记：`BI01-FO01-WORKER-DISPLAY02-ENDPOINT-R8-20261022`

原 order_id：`BI01-FO01-N-DISPLAY-INTEGRATION-02`

管理来源：`observe-iterate@8af0eafe829eb139ec5563a15cf2c705aa0243ef:runs/BI-01-FO-01/reviews/management-R0008/FULL_RESPONSE.md#endpoint-disposition`

返回目标仍为：`chatgpt:细节叙事生成_金标:BI01-FO01-执行`

技术状态：`SUPPLEMENT_TECHNICAL_RETURN_READY`

## 一、准确结论

管理指出的准确条件风险没有在 Worker02 实际调用边界复现：aidata 包装器仍采用右开条件 `x < end_uti`，但真实 uplot 调用对三个 selected K 分别传入 `end_uti_exclusive=K+1`：

|selected K|实际调用窗口|
|---:|---|
|103150800|`[100443000, 103150801)`|
|103151400|`[100443000, 103151401)`|
|103315800|`[100443000, 103315801)`|

所以并不存在“调用端把 `end_uti` 直接设为 K，导致 K 点被右开比较式删掉”的现场条件。

但直接审计此前已发布的三个 Bokeh HTML 时发现了另一个真实展示缺陷：同一进程连续构建多个 selected-cut layout 时，后两个页面的九类标量 renderer 复用了第一个页面 K=103150800、exact `6d4acb13…` 的 plotter 数据。正式 `plot_view_data`、页面 K 标签、价格截止和成员几何本身正确；错误只在 aidata 展示消费者的 BasePlotter 实例身份复用，原 19 项包装检查没有直接断言“renderer 中的标量 x/exact 等于本页 K/exact”，所以没有发现它。

本补充已经在原 aidata 独立分支内最小修通。修后三个页面的九类标量 renderer 均含各自 K 和各自 exact；逻辑视图、实际 Bokeh feature renderer、原价格输入及 close_path 都没有 K 之后坐标。

## 二、修前直接证据

`evidence/ENDPOINT_R8_PRE_FIX_HTML_AUDIT.json` 从已发布且新鲜回读过的原技术包 commit `39308f4a8fe6b6f2fe1399f8d9e56b91a5ceb643` 直接读取 HTML，不依赖当前工作树：

|页面|页面 K|九类标量实际 x|标量 source exact|K 后特征|
|---|---:|---:|---|---|
|确认前|103150800|103150800|`6d4acb13…`|无|
|确认时|103151400|103150800|`6d4acb13…`|无|
|末拍|103315800|103150800|`6d4acb13…`|无|

这说明原页面不是因为 `< end_uti` 把 K 点变成空白，而是后续页面拿到了首个 cut 的标量 renderer。原截图中的点确实存在，但后两页点的知识身份错误；因此不能继续把旧像素记录解释为“各页 K 上正式标量已正确显示”。

调查过程保留了一个有价值的中间事实：单独在新进程只构建末拍页时，K=103315800 标量能够进入 renderer；只有把三个 selected 页面按原流程连续构建，才复现首个 cut 被后页复用。这定位了实例身份问题，而非正式数据、右边界或读回缺失。

## 三、最小 aidata 修改

aidata 分支仍为 `fy/bi01-fo01-n-display-r0007`。原提交 `db44a54fa30ff9b4b8dddbe37e020d087c914d62` 之后增加修复提交：

```text
28260d3ec5d2ed254b2539cb9abc656e4737f80b
Fix selected-cut plotter identity reuse
```

唯一运行修改位于 `u2_normal_node_behavior_display.py`：创建每个 panel plotter 时，把 display-only `feature.ppid` 放入不参与业务语义的 anchor 元数据 `_display_instance`。原因是本现场 BasePlotter 参数身份没有纳入普通 Python feature 对象；三个 bundle 的配置 anchor 原本相同，导致 plotter ppid 相同并可复用首个实例。

没有改变：

- 业务 K、正式 N 值、窗口/working/member 关系；
- `read_at_knowledge`、OnlyRead 或产品地址；
- 右开切片公共语义；
- TIS、FRP、core、SDK 或 uplot 源码。

新增一个定向回归测试，确认两个不同 selected cut 的 display feature 和 plotter ppid 均不同。新提交上的相关测试为 `29 passed`。

## 四、修后直接检查

没有重读 N。`scripts/rerender_endpoint_r8.py` 只使用原技术包已保存并带哈希的三份正式 selected-cut 导出和同绑定价格，重建三个 selected 页面；evolution 页面未重绘。

`evidence/ENDPOINT_R8_POST_FIX_HTML_AUDIT.json` 对保存后的 Bokeh HTML 直接解包检查：

|页面|九类标量 x|source exact|close_path 最大 x|所有 feature 最大坐标|
|---|---:|---|---:|---|
|确认前|103150800|`6d4acb13…`|103150800|不大于 K|
|确认时|103151400|`ef2f74f6…`|103151400|不大于 K|
|末拍|103315800|`cfd51328…`|103315800|不大于 K|

`evidence/ENDPOINT_R8_DIRECT_CHECK.json` 另从真实 uplot layout 观察实际 `ctx.uti_slice`、逻辑视图和 Bokeh renderer，三个页面共 33 项页面级直接条件全部为真：

- 每页九类正式标量 renderer 都包含该页 K；
- `end_uti_exclusive=K+1`；
- 正式投影与 renderer 坐标均无 K 后值；
- 原价格输入和 close_path 均止于 K；
- 页面验证、浏览器打开和补充像素检查均通过。

修后浏览器实际重新打开四页，全部 HTTP/Document/6 plots/12 canvas/panel groups PASS。Worker 用 original-detail 重新查看三个 selected PNG；具体观察及新截图哈希在 `render_evidence/ENDPOINT_R8_VISUAL_INSPECTION.json`。这仍只是 Worker 技术像素检查，不等于执行 Pro 专业看图或管理接受。

## 五、实物、版本与限制

新增或更新的主要实物：

|实物|用途|
|---|---|
|`evidence/ENDPOINT_R8_PRE_FIX_HTML_AUDIT.json`|从原发布 commit 重现两个后页复用首个 cut|
|`evidence/ENDPOINT_R8_POST_FIX_HTML_AUDIT.json`|直接证明修后三页各自 K/exact 和无未来值|
|`evidence/ENDPOINT_R8_DIRECT_CHECK.json`|实际 uplot 调用窗口、renderer、浏览器和像素综合检查|
|`evidence/ENDPOINT_R8_RERENDER.json`|只重建三个 selected 页的范围、版本和输出|
|`render_evidence/ENDPOINT_R8_VISUAL_INSPECTION.json`|修后三页实际像素检查|
|`scripts/audit_endpoint_html.py`|可从 Git commit 或当前工作树审计 Bokeh HTML|
|`scripts/check_endpoint_r8.py`|从既有正式导出执行实际调用边界检查|
|`scripts/rerender_endpoint_r8.py`|只重建三个 selected 页面|

本结论只覆盖 Worker02 实际 aidata/uplot 调用路径和本次三个 rb selected cuts，不升级为 generic aidata 全调用者证明。KPriceLine 的蜡烛图形可在屏幕上占据 bar 中心两侧的几何宽度；“无未来行情”按底层 `open_uti` 记录身份核验，不把半根 bar 的屏幕宽度误称未来记录。

aidata 和 observe-iterate 均按原仓库/原真实分支发布。observe-iterate 的补充技术包 commit、后继回执 commit、两仓 fresh readback 和逐文件哈希以更新后的 `GITHUB_RECEIPT.json` 为准。本 Worker 不据此代签专业业务解释、管理接受或后继任务。
