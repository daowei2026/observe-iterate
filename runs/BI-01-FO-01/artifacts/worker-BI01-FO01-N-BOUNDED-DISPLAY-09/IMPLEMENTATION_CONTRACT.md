# Worker09 实际有限合同及调用关系

order_id：BI01-FO01-N-BOUNDED-DISPLAY-09。最终候选aidata `25a9fd8b1333aafd4c56fd1b288e7f8d3c8c3113`，前一候选a38d33b保留；不是共享采用记录。

## 一项选择，不是任意代码入口

正常run_brief沿已有 `evidence_features`，使用仓库内显式登记的准备器：

```python
from mquant.aidata.normal_node_behavior import display_selection
run_brief_input['evidence_features'] = [display_selection(original_frozen_run_dir)]
```

实际字面量形状为 `prepared_display: {version: 1, adapter: normal_node_behavior, run_dir: 已有冻结run目录, selection_sha256: 该run原manifest哈希, configuration_version: 0.3.0-worker09}`。
不接受任意import路径、回调、任意layout provider；不是新增共享CAE默认参数。正常Fao仍16键，选择嵌在原evidence_features中。

`display_contracts`校验有限panel、price_level/price_delta/ratio/calendar_tick、原值变换、market/single_k、formal/display源角色。
旧group仅tag；没有opt-in的配置不增加面板树或新序列化字段。未知能力、悬空面板、轴/单位冲突和显示源冒正式明确失败。

## 实际生产者和消费者

- `contracts.normalize_evidence_features/normalize_anchor/resolve_run_evidence`与registry/index保留声明及源角色；单一选择展开原表formal anchors与display refs。
- `normal_node_behavior`继续核原件/选择、按frozen node装配bundle、补同K必需较早原表。源缓存只共享原输入，不共享已经裁过的投影。
- `u2_normal_node_behavior_display.prepare_bundle_display`解释N状态、关联及具名场景注记，返回视图、有限声明和数据注记，不返回整页layout。
- `evidence_composition.compose_prepared_display`执行共用MainFig/SubFig/PlotSet、原值坐标、单K轴、非退化范围、图例及空数值说明；没有N枚举/地址或生产公式。
- `evidence_plot`复用原point/line/segment、原值hover与页内缓存。显式identity才跳过price DynStd。single_k读取独立取[K,K+1)，不随行情窗误裁；留白不增加数据。
- Notebook兼容 `build_uplot_layout`是薄调用；`AidataBigWorldReviewCAE.layout`与`render_review_nodes`都经过相同准备/组合。旧N整页render_node路径已退出。
- `build_big_world_chart_pages`的实际参数生产者保存字面量选择，不生成默认N空键；opt-in不擅建日线overview。公共注册链仍是原CAE/DAO，未另建Host。
- 正式slicer/delivery拒绝display源。原table时间/字段与selection_ref进入正式索引，所引用较早window/binding/rhythm不会被局部价窗吞掉。

## 版本与身份

配置0.3.0-worker09；场景0.4.0-worker09；原N方法/参数、UInt64、K/Life/exact和原时间不变。
显示身份覆盖K/exact、原配置、mode、display_range及optional panels；原source hash缓存可共享。
实际新身份与旧6128—6131不碰撞；自动刷新在dupdate前拒绝旧N键或不同fason，不能靠删字段修旧页。
原旧页、17键和失败记录保留，旧服务不会因参数恢复成功就自然理解新面板语义。

## 公共采用边界

须由原有权维护者将完整候选及W06基础送到Trier/Bokeh各自实际导入路径，确认配置、registry、组合器、N准备及冻结原件可读；不能只cherry-pick旧cbd或升级latest。
本单没有切换共享checkout、重启/注入服务、修改认证或受保护源码的授权，也没有执行这些动作。
真实消费者具备能力后才由有权方注册同run/node的新版本图；实际打开目标图层前，不更新当前可用引用、不称工作3完成。
