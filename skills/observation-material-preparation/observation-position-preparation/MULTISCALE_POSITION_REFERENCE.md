# 高频多尺度观察位置参考

## 1. 来源与用途

本参考只提炼下列脚本中的**多尺度位置组织**：

- [`task-inputs/eaw-p1-integrated/caegraph-review/caegraph_definitions.py`](../../../task-inputs/eaw-p1-integrated/caegraph-review/caegraph_definitions.py)

脚本当前包含长期概览、多尺度页面和 Tick 图的完整实现。B 只借鉴其中从长期到高频的**位置层级、父子关系和时间窗口**，不复用其图内容。

## 2. 位置层级

```text
1d 长期概览
    ↓ 选择 big 位置
30m 大尺度节点（big）
    ↓ parent_node_id
1m 中尺度节点（mid）
    ↓ parent_node_id
5s 小尺度节点（small）
    ↓ parent_node_id
tick 节点（tick）
```

### 2.1 1d 长期概览

`OverviewCAE` 展示板块有效行情范围的 1d K 线，并标出搜索时间段、big anchor 与已经形成的 big 节点时间框。每个 big 节点进入独立的 30m／1m／5s 多尺度页面；长期概览本身不重复铺开这些子图。

B 在这一层只关心：从长期范围中确定哪个 big 位置继续向下观察。

### 2.2 30m 大尺度位置

`MultiscaleCAE` 以一个 `big_node_id` 为一条 local world 的根；大尺度主位置对应 30m 时间范围。

### 2.3 1m 中尺度位置

从 `timespans.csv` 中选择：

```text
parent_node_id == big_node_id
level == "mid"
```

并按 `start_uti`、`node_id` 排序。

### 2.4 5s 小尺度位置

对每个 mid 节点选择：

```text
parent_node_id == mid.node_id
level == "small"
```

### 2.5 tick 位置

对每个 small 节点选择：

```text
parent_node_id == small.node_id
level == "tick"
```

## 3. 位置记录至少保留的字段

```text
node_id
parent_node_id
level
start_uti
end_uti
```

实际包中若同时有时间戳、anchor 或来源引用，应一并保留，但不能丢掉上述父子身份。

## 4. 必须保持路径，不得压平

高频位置不是五个互不相关的时间窗。B 应输出一条或多条路径：

```text
overview → big → mid → small → tick
```

D 才据此把各层绑定到相应 CAEGraph 页面或图集。

## 5. 明确排除的脚本内容

下列内容属于该脚本的展示或执行实现，不属于 B 的位置方法：

- 具体 K 线、open segment、evidence feature 和 Tick 盘口图层；
- `EvidencePlotter`、`TickPricePlot`、`TickVolumePlot` 等绘图器；
- 颜色、样式、hover、动态标准化、按钮和布局；
- 为页面显示而进行的缓存、数据准备和图层切换；
- 图中具体业务证据内容。

尤其是 `_merge_tick_rows_for_display`：它为了避免同一 small 下重叠的 tick 辅助框互相遮挡而进行**展示层合并**。B 不得据此合并、删除或改写真实 tick 位置节点。

## 6. 当前边界

本参考只是已有高频用例的位置层级复用，不宣称已经成为所有多尺度特征的通用理论。后续若 Owner 补充新的位置选择经验，应在本参考中明确增加适用条件或另建方法，而不是无痕改变现有层级。
