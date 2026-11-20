# C0007 专业报告｜D003｜Q 的 C Skill

## 1. 回交身份

| 字段 | 值 |
|---|---|
| run_id | `OI-U2-Q-OBS-20261120-01` |
| call_id | `C0007` |
| delegation_id | `D003` |
| work_item_id | `OI-U2-Q-OBS-20261120-01-WI-C` |
| stage_instance_id | `OI-U2-Q-OBS-20261120-01-M-C` |
| sender | `chatgpt:OI-U2-Q-OBS-20261120-01:executor:E1` |
| return_to | `chatgpt:OI-U2-Q-OBS-20261120-01:manager` |
| invocation_token | `c18943fb21dc452c807fdd6a388a4731` |
| 专业状态 | `REPORTED_COMPLETE` |

本次只执行原 D003 绑定的 C Skill：`caegraph-display-preparation`。A、B 已作为当前有效上游消费，没有重跑；没有进入 D、E，没有运行特征，也没有把 B 当前默认位置固化进 C3。

## 2. 已采用的原生专业合同

- `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-display-preparation/SKILL.md`
- `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-display-preparation/WORKFLOW.md`
- `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-display-preparation/IO_SPEC.md`
- `daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad:CAEGraph使用手册.md`

同时按 Workflow 要求读取同锁定 uplot commit 的 `utlv2.py`、`utkv2.py`、`pfw.py`、`__init__.py`，并核对 Q Python wrapper、公开字段及 A/B 当前有效原生产物。

## 3. C 原生产物

### 3.1 人读总产物

`daowei2026/observe-iterate@63df2581a1996d4356752f32c2ee5c64fa79fb1f:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C_DISPLAY_PREPARATION.md`

### 3.2 机读总产物

`daowei2026/observe-iterate@42a603fc8d209ea1bed7870c7b298f99a2785782:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C_DISPLAY_PREPARATION.json`

### 3.3 C1 待展示信息

`daowei2026/observe-iterate@781865309218623fecb355a2c6bb826de08cf735:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C1_DISPLAY_INFORMATION.json`

### 3.4 C2 HTML 与原型

- 第一版 HTML：`daowei2026/observe-iterate@36f88213832fe1ea90b29cecd47c0825e50ddf34:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C2_EXPECTED_V0_1.html`
- 当前唯一预期 HTML：`daowei2026/observe-iterate@85b41da60713f7ed2824b104bff614478c0f9371:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C2_EXPECTED.html`
- 确定性预览生成器：`daowei2026/observe-iterate@5a1ecd7efaa4c176b262a0104fd2d87f79f6e4f3:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/q_caegraph_preview.py`

### 3.5 C3 可注入代码

- Python：`daowei2026/observe-iterate@435c2ed129ba7596b9d5a102bc0d8bf6104729ba:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/q_caegraph_injectable.py`
- 注入合同：`daowei2026/observe-iterate@747ce755d95e9354dd13209c41ba053d219febe1:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/C/C3_INJECTION_CONTRACT.md`

## 4. C1 专业结果

### 4.1 核心常显对象

- 多品种 5m 价格与 Calendar 背景；
- 准确 F candidate；
- Q `DirectionalOccurrence` 的 Life/Revision/Previous 链；
- 每版 Q 的 qualification、observation、applicability；
- 成员 asked/used/successor/endpoint、completion、verdict、basis、path；
- 六类 quantity 的原值和 availability；
- 显式 `DirectionalDutyEnd` 及其最后成功 Q。

### 4.2 条件显示对象

- source frame 的 progress/known/ended/patch/coverage 摘要；
- subscription 的原始/当前观察界和 closed 状态；
- definition 的固定方法元数据。

### 4.3 不提升为独立业务事件

`DirectionalFrame`、`DirectionalBatch`、存储 envelope、definition 及 member table row 均未被误画成新的业务 occurrence。

## 5. C2 专业结果

### 5.1 第一版

第一版建立：多品种总览、生命周期轨、组级状态和成员审计。它是确定性示意页面，不是实际 Q 运行结果。

### 5.2 复杂点与修订

核实并处理：

1. 一个 Q occurrence 的多个成员和多类位置；
2. publication、known、actual、confirmation、endpoint、Calendar 的区分；
3. Q revision 与 duty end 的区分；
4. 无新 Q 不等于失败或结束；
5. ratio 总览与 raw 价格证据的区分；
6. 六量单位及缺失语义；
7. 常显图元与精确 audit 的分层。

当前 HTML形成五层：

```text
P1 多品种 ratio 价格总览
P2 F candidate → Q revision → explicit duty end
P3 Q 组级状态
P4 各成员 raw price / motion / verdict / quantity audit
P5 exact refs / Previous / known / end audit
```

### 5.3 CAEGraph 能力判断

锁定版现有布局、K 线、共享 x-range、图例隐藏和 `BasePlotter` 足以实现当前预期。通用 plotter 的 hover 不足由薄 custom `BasePlotter` 解决，不需要新增 uplot 核心能力；当前无阻塞 capability gap。

## 6. C3 专业结果

`q_caegraph_injectable.py` 是真实 Python 定义，不是伪代码。它使用：

```text
CAEGraph / PlotSet
AllSymsMainFig / AllSymsFig / PerSymFigSet
MainFig / SubFig
KPriceLine
BasePlotter + Bokeh glyph / hover
```

并通过 `QDisplayBinding` 要求 D 注入：

```text
q_feature
price_feature
frame_adapter
field_binding
QPositionBinding(SOF/block/calendar/objects/timespans)
```

因此代码没有硬编码：

- `TA_updto20240229_DBA`；
- `steel`；
- `night_end_at_2300`；
- `rb/hc/i`；
- `2021-01-01～2022-12-31`；
- 当前具体 Q 实例。

D adapter 形成 `timeline / revision_links / states / members / quantities / audit` 六张 canonical frames，以真实公共表的父子坐标和 identity 连接，禁止仅凭时间或成员名模糊 join。

## 7. 验证与事实边界

已完成：

- 第一版与当前版 HTML 发布；
- HTML 结构解析；
- Python `py_compile`；
- 无硬编码 SOF、日期、对象、实例的静态检查；
- C2 面板与 C3 plotter 的逐项对应；
- Previous、candidateReference、duty end、missingness 的代码检查。

未声称：

- 在 `/dwdhome/fy/BASE_E6_2_copy` 执行；
- 读取真实 Q 运行结果；
- 已完成 D 的字段/实例/位置绑定；
- 已完成 E 的真实运行、检视和最终 HTML 交付。

以上边界不构成 C 的剩余范围；它们是后续 D/E 的既定职责。

## 8. Worker 与权限

- 未签发 Worker；
- 未接受或虚称 Worker Return；
- C 的展示合同、HTML 和可注入代码可由锁定源码与上游产物完成，不需要 Linux 特征运行；
- 所有新文件仅写入 `longrun/runs/OI-U2-Q-OBS-20261120-01/**`，未扩展 D003 权限。

## 9. 完成条件证据

| C Skill 原生条件 | 实际证据 |
|---|---|
| C1 已整理待展示信息 | C1 JSON 覆盖输入、主输出、中间结果、位置、身份、原值和关系 |
| C2 已先形成第一版预期与 HTML | `C2_EXPECTED_V0_1.html` |
| 已识别复杂点并循环核对能力 | 人读/机读产物记录七类复杂点、锁定能力与三类已解决限制 |
| 已发布当前唯一预期 HTML | `C2_EXPECTED.html` |
| C3 已形成可注入 CAEGraph 代码 | `q_caegraph_injectable.py` + 注入合同 |
| C3 没有固化 B 最终位置或外层实例 | 静态检查通过；位置和实例均为 binding 参数 |
| C2 与 C3 一致 | 五个面板均有明确 plotter/layout 对应 |
| 阻塞 capability gap | 无 |
| 剩余 C 范围 | 无 |

因此 D003 的 C Skill 判定为：**完整**。

## 10. 管理后继

原 manager 可消费本回交并按既定 Workflow 判断 C 阶段状态。若接受，后续 D 应正式消费 A、B、C，绑定本次真实 Q 实例、公共表字段和 B 位置；本 executor 不自行签发下一项委派。
