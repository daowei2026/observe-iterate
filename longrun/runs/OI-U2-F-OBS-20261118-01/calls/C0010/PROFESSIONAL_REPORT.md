# C0010｜D004 D Skill 专业回交

## 1. 调用与回交身份

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `work_id`：`OI-U2-F-OBS`
- `business_case_id`：`U2-FQV-F`
- `call_id`：`C0010`
- `delegation_id`：`D004`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-D`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-D`
- `sender`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:manager`
- 正式委派：`daowei2026/observe-iterate@2fc0cfc19eb48e1e820e7f51ab2996a968715956:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D004/DELEGATION.json`

## 2. 实际采用的 Skill 与输入

本次亲自读取并采用：

- `daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-definition-integration/SKILL.md`
- 同提交同目录 `IO_SPEC.md`
- 同提交 `skills/observation-material-preparation/references/CAEGraph仓库结构与定义集成参考.md`
- A 当前有效 occurrence 产物；
- B 当前有效 `B-POS-001`；
- C 当前有效 C1/C2/C3、唯一当前 HTML 和能力缺口；
- 正式 `make_features(...)` 构造、F Python 读取接口和公开字段映射；
- 锁定 `uplot@0a4fcd...` 的手册、正式导出、顶层配置、布局、PlotCtx、PlotDataTree、多尺度和 app 输出源码。

本次只执行 D 的单一集成动作。没有执行 E，没有运行真实图，没有派 Worker，也没有处理 Q/V、合理性分析或全历史 F producer 重跑。

## 3. 实际专业产物

### D 完整集成记录

`daowei2026/observe-iterate@e35945aec93d90e4dbb045bc3c35dc5153661aa4:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/CAEGRAPH_DEFINITION_INTEGRATION.md`

### 可直接交 E 尝试执行的完整定义

`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`

### 定义级机读检查

`daowei2026/observe-iterate@37f81088985ff3f1d8c2e7fa409db7529586073f:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/DEFINITION_CHECKS.json`

稳定定义身份：

```text
OI-U2-F-OBS-20261118-01-D-CAEGRAPH-V1
```

## 4. 正式绑定结果

完整定义实际绑定：

| 字段 | 绑定值 |
|---|---|
| 外层实例 | `make_features(**FEATURE_PARAMS)[0]` |
| F 类型 | `CommonPriceTurnGroupCandidatesFrp` |
| SOF | `TA_updto20240229_DBA` |
| 构造 block | `steel` |
| 图中对象 | `rb / hc / i` |
| 日历 | `night_end_at_2300` |
| 价格 Feature | `KLine(freq='5m')` |
| B 时间范围 | `2021-01-01` 至 `2022-12-31` |
| 主 occurrence x | `groupKnownFrom` |
| 成员位置 | `memberActual / memberConfirmation / memberKnownFrom` |
| 候选身份 | Candidate Life / Revision / Previous |
| 形成证据 | members、Required 四坐标、pair distance、overlap、covered-by |
| CAEGraph | `uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad` |

定义进入 `CurrSof/CurrCalendar` 后调用正式构造函数，只将 `f` 绑定为 candidate Feature。Q/V 对象不进入读取、表准备或图元。

## 5. 当前图的固定结构

定义保持 C2-CURRENT-V2：

1. `rb / hc / i` 每品种独立 5m 原价图；
2. 候选成员 actual 点；
3. actual→confirmation、confirmation→member-known 位置链；
4. confirmation 和 member-known 端点；
5. 候选 revision 附图，横坐标严格为 `groupKnownFrom`；
6. previous→revision 链；
7. Required Time/Direction/TurnType/Bend 审计附图；
8. exact identity、窗口原值、gap/veto/distance、overlap/covered-by 进入 hover。

没有跨品种价格标准化；anchor/deadline/revisionEnd 没有被伪装成 UTI；definition-only publication 没有被画成候选 occurrence。

## 6. 锁定 CAEGraph 调用链核实

已确认本次真实链：

```text
mquant.uplot 正式导出
→ CAEGraph / PlotSet
→ CurrTradeSet / CurrIndustry / CurrCalendar
→ PlotCtx
→ PerSymFigs / AllSymsFig
→ KPriceLine + BasePlotter extensions
→ ColumnDataSource
→ PlotDataFolder / PlotDataNode
→ CAEGraph.layout
→ Bokeh file_html / CDS export
```

锁定仓库中的 Python 文件实际位于仓库根目录；运行时正式导入仍是 `mquant.uplot`。本定义没有把 Git 物理路径误作 Python 包路径。

## 7. 确定性纠正

D 按 Skill 的唯一修正条件记录并实施三项纠正：

### D-CORR-01｜非单调 occurrence 位置切片

C3 把成员／revision-link 表交给 `PlotCtx.feat_data` 的静态 UTI 切片。实际成员位置可重复、可非单调；D 改为按当前 `ctx.uti_slice` 显式 mask 后构造 CDS。该修正来自锁定 PlotCtx 源码和 A 的记录形状，不改变位置或展示语义。

### D-CORR-02｜confirmation／member-known 端点

C2 当前 HTML 已固定三类成员位置，但 C3 只接了 actual 点和两段线。D 增加 confirmation 三角点与 member-known 菱形点，使可执行定义与已接受 C2 对齐；没有新增业务选择。

### D-CORR-03｜uplot 源码物理路径

D004 的若干逻辑引用带 `uplot/` 前缀；锁定仓库 Git tree 表明文件在根目录。D 以真实根路径核源码，以正式 `mquant.uplot` 导入运行。

三项纠正均未改变 B 位置、C2 面板／图元含义，也未引入新的业务判断；完整前后差异已写入 D 原生产物。

## 8. 保留的真实边界

- `raw_turn_view` 仍为可选且本定义不注入；不为补叠加层重跑被排除的生产链。候选成员证据保持。
- Haskell 存储的 `groupFormationParticipation` 未被锁定 TIS `GROUP_TABLES` 暴露；脚本只告警，不猜字段。
- overlap/covered-by 只有目标 Life，未伪造唯一目标 revision/time 连线。
- 外层 `Tick.ts` 未替代 `groupKnownFrom`。

## 9. 定义级检查结果

已完成并记录：

```text
Python syntax / compile             PASS
locked uplot export surface         PASS
outer f binding                     PASS
no direct f.rerun                   PASS
B position in executable code       PASS
A fields in glyph / hover binding   PASS
C2 display contract                 PASS
nonmonotonic UTI handling           PASS
PlotDataTree export path            PASS
real platform execution             NOT_RUN_IN_D
```

D 没有冒充真实环境运行。`m3/mquant/uplot` 导入、精确 `fields.json`、真实表列、CAEGraph layout、Bokeh HTML、PlotDataTree 和图面一致性全部留给 E。

## 10. E 执行入口与预期产物

E 可在 `/dwdhome/fy/BASE_E6_2_copy` 的本 Run 分支工作树，从仓库根目录执行：

```bash
python longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py \
  --output-dir longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/runtime/u2_f_caegraph
```

预期形成：

- `definition_run_report.json`；
- `u2_f_caegraph.html`；
- prepared display tables CSV；
- PlotDataTree 中每个 CDS 的 CSV 与逻辑路径清单。

若精确 F 实例没有既存 `fields.json`，脚本命名失败并停止，不自动重跑 F。

## 11. 完成判断、Worker 与后继

D Skill 原生完成条件已全部满足：

- 锁定仓库调用链已按源码说明；
- 外层真实实例、B 位置和 A 字段已进入完整代码；
- C2 当前预期未改变；
- 确定性修正已证明唯一并完整留痕；
- 未确认的数据接口问题没有被猜测；
- 形成了可直接交 E 尝试运行的完整脚本；
- 定义级检查和 E 运行验收已分开。

本 C：

- 零 Worker；
- 没有签发 W；
- 没有接受 Worker Return；
- D004 内没有仍未满足的专业工作；
- 不需要续接原 D004。

父 Run 尚未完成。原 manager 应消费本回交后，按既定 Workflow 推进 E 的真实运行、图接受、正式取数和 C2 一致性核对。

**D 阶段专业状态：完整。**
