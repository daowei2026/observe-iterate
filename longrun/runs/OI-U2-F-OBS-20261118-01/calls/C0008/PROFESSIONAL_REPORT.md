# C0008｜D003 C Skill 专业回交

## 1. 调用与回交身份

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- `call_id`：`C0008`
- `delegation_id`：`D003`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-C`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-C`
- `sender`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- 正式委派：`daowei2026/observe-iterate@fadf29d9c0e57bf3eb77d9b198392b902b94a0f9:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D003/DELEGATION.json`

## 2. 实际采用的 Skill、原件与边界

本次亲自读取并采用：

- `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-display-preparation/SKILL.md`
- 同提交同目录 `WORKFLOW.md`、`IO_SPEC.md`
- A 当前有效产物；
- B 当前有效产物；
- 本次唯一业务输入、实例脚本、TIS 正常构造、完整配置、F Python 公开读取接口和字段映射；
- `daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:CAEGraph使用手册.md`；
- 同一 uplot 提交与本次复杂点有关的 `utkv2.py`、`utlv2.py`、`pfw.py` 和公开导出。

本次只执行 C1/C2/C3。没有选择或修改 B 的最终位置，没有运行 D 的完整定义，没有运行 E 的真实实例，也没有处理 Q/V 或合理性分析。

## 3. 实际专业产物

C 阶段完整原生产物：

`daowei2026/observe-iterate@bcb94cc298d0a20049a2a52fdf7fe577137e7bde:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/CAEGRAPH_DISPLAY_PREPARATION.md`

其配套产物为：

| 产物 | 准确引用 |
|---|---|
| C2 第一版预期 HTML | `daowei2026/observe-iterate@4e69f0cc0e5373dc0cb6daa41ce6ac3e0cf63e40:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview_v1.html` |
| C2 当前唯一预期 HTML | `daowei2026/observe-iterate@56eef30b28c928255329f77798fb46b9adbbc71a:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview.html` |
| 预期 HTML 生成原型 | `daowei2026/observe-iterate@b753885342ed3a95258137efb6c62f4d6e181076:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/generate_caegraph_preview.py` |
| C3 可注入 CAEGraph 代码 | `daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py` |
| C3 纯表夹具 | `daowei2026/observe-iterate@891f77c194ed7ac607a38429d8f1ff2bfafef6cb:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/test_caegraph_display.py` |

两份 HTML 均为确定性合成预览，不是 D 绑定图或 E 真实运行结果。

## 4. C1 结果

C1 已区分并处理：

- 5m KLine；
- 第一／第二轮 CompleteScaleTurn；
- `falter` Zig 状态；
- FormationFrame、FormationMaterial、PairView；
- CandidateOccurrence／GroupOccurrenceRecord；
- definition metadata；
- members、previous、Required、overlap、covered-by；
- 当前不可由 TIS 读取的 formation participation。

核心边界是：

> 候选 Life 的一次 revision 才是 F 的业务主 occurrence；成员和 Pair Required 是该 revision 的正文／形成证据。

因此没有按公开表数量机械增加面板，也没有把 working-state 画成独立 F 主事件。

## 5. C2 CAEGraph 能力核实

已确认锁定 CAEGraph 能够通过现有类及其公开扩展点表达本次核心需求：

```text
CAEGraph
→ PlotSet
→ PerSymFigs / AllSymsFig
→ KPriceLine / BasePlotter extensions
→ PlotCtx DataFrame binding / UTI conversion / hover
```

采用的关键能力包括：

- 每品种独立原价图；
- 全局候选／Required 附图；
- 主附图共享 X 轴；
- point、segment、动态 marker/color；
- hover 和 legend hide；
- DataFrame 只读适配；
- 小型 `BaseFigSet / BasePlotter` 子类扩展。

没有发现必须先扩展 CAEGraph 才能表达 C1 核心信息的工具级阻断。

## 6. C2 展示循环与当前结果

### 第一版

第一版采用：

```text
多品种比例标准化价格共图
+ groupKnownFrom 候选点
```

第一版被否决，原因是：

1. 标准化价格可能被误认成业务原值；
2. 成员 actual、confirmation、known 被折叠或丢失；
3. Candidate 与 member identity 不可追溯；
4. Required pair 形成／反证证据缺失。

### 当前版

当前被接受的页面结构为：

1. `rb / hc / i` 每品种 5m 原价主图；
2. 可选 raw ScaleTurn 输入点；
3. 候选成员 actual 点；
4. actual→confirmation 与 confirmation→member-known 位置链；
5. 候选 revision 全局附图，横坐标只用 `groupKnownFrom`；
6. previous→revision 链；
7. Required Time/Direction/TurnType/Bend 审计附图；
8. exact identity、窗口、gap/veto/distance 等细节通过 hover 保留。

Calendar-clock anchor/deadline/revisionEnd 不冒充 UTI 时间，只进入候选 hover。overlap/covered-by 当前只公开目标 Life，没有唯一 target revision/time，所以只进入 hover，不伪造跨候选连线。

## 7. C3 注入合同

`caegraph_display.py` 暴露：

```text
DisplayBindings
prepare_display_tables(...)
build_caegraph(bindings)
```

D 需要注入：

- `candidate_feature`；
- 与实例一致的 5m `price_feature`；
- symbols；
- SOF；
- calendar；
- B 的 timespans；
- 可选 `raw_turn_view`。

C3 没有固化 `TA_updto20240229_DBA`、`rb/hc/i`、2021～2022 日期、外层 `f` 实例或结果路径。

## 8. 验证结果

已经执行：

- 两个 Python 文件语法检查；
- 两份 HTML 结构解析；
- 两份 HTML JavaScript `node --check`；
- C3 纯表夹具。

夹具结果：

```text
prepare_display_tables fixture: OK
revisions (2, 25)
members (5, 18)
required (8, 10)
```

没有冒充已经完成真实平台 CAEGraph 运行。当前 executor 没有在 `/dwdhome/fy/BASE_E6_2_copy` 中绑定 B 位置并运行 `m3 / mquant / uplot`；Chromium 在隔离环境中也未完成截图渲染。因此当前有可打开 HTML、结构与 JavaScript 检查，以及 C3 纯表检查，但没有声称已有 D/E 运行图或浏览器截图证据。

## 9. 真实缺口

### 9.1 `groupFormationParticipation`

Haskell 已保存该正式决定证据，但锁定 TIS `GROUP_TABLES` 未公开。C3 只记录告警，不使用其他字段猜测 admission／correction／alternative 决定细节。

### 9.2 overlap／covered-by 的目标精确点

当前公开数据给目标 Life，不给唯一目标 revision/time policy。当前保留关系存在性，但不画唯一时间连线；后续若需要连线，必须先给出业务上的 target exact policy。

两项都不是 C 的未完成工作：第一项是读取接口缺口，第二项是目标身份选择语义边界。

## 10. 完成判断、Worker 与后继

C Skill 原生完成条件已经全部满足：

- C1 已完成；
- CAEGraph 手册和必要源码已直接核实；
- 第一版 HTML 已形成；
- 复杂点已循环处理并更新到当前唯一 HTML；
- C3 已形成可注入 CAEGraph 代码；
- C2/C3 语义已核对一致；
- 预览和正式后继边界已明确。

本 C：

- 零 Worker；
- 没有签发 W；
- 没有接受 Worker Return；
- D003 内没有仍未满足的 C 专业工作；
- 不需要续接原 D003。

D、E 均未在本调用执行。原 manager 可在消费本次回交后，以 A+B+C 的当前有效产物签发 D 的单一正式绑定工作；E 再运行真实实例并核对 C2 当前预期。

**C 阶段专业状态：完整。**
