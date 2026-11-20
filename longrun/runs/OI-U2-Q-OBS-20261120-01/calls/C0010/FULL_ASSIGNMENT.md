# C0010｜向原 Workflow manager 回交 Q 的 D Skill 完整结果

[OI-U2-Q-OBS-20261120-01-C0010]
invocation_token=8dd3f0cde1c04efa96bc472685117009

你仍是本 Run 原 Workflow manager：chatgpt:OI-U2-Q-OBS-20261120-01:manager。本次是原 D004 / WI-D / M-D 的完整 D Skill 回交。原 executor:E1 的完整专业报告、全部原生产物和正式 Return 已原样取得并独立校验；D 自报 REPORTED_COMPLETE，没有 Worker 工单、没有剩余 D 范围，也没有进入 E。A、B、C 已由你正式消费，不重跑。

请依固定 Workflow 和 V2 协调职责消费本次原 Skill 结果，更新统一 TASK_PROGRESS 的实际完成状态、当前有效版本与依赖、执行 Chat、在途状态、未完成工作及合法后继，并按 Workflow 正式签下一项 Skill 工作。每次默认一项 Skill，任务身份、准确 Skill/适用文件和有效上游产物引用准确；专业方法与完成判断依原 Skill。manager 不替 Skill executor 设计专业方法、Worker 工单或处理规则，不增设专业验收条件。

当前 Run 仅 Q 自身 A～E，以 E 观察材料交付为终点。F 仅必要上游；V、全历史 producer、合理性分析不纳入。工作区及授权沿用本 Run 已核 Binding，不扩权。

## 实际原件

- daowei2026/observe-iterate@546e457983c7d3e00378eea26872e605d79f8e20:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/D_CAEGRAPH_DEFINITION_INTEGRATION.json
- daowei2026/observe-iterate@3b3df7d4509860be1d43233736aecfb264732585:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/D_CAEGRAPH_DEFINITION_INTEGRATION.md
- daowei2026/observe-iterate@78b306ae3dba130b4bd1015befdebe19090ac728:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/D_DEFINITION_CHECKS.json
- daowei2026/observe-iterate@91fe9d8768d528a2ff616917a42412afb25fcc8a:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0009/PROFESSIONAL_REPORT.md
- daowei2026/observe-iterate@5cd5d38fcc61176dca8ff566364ecd7ebfa7fd7d:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0009/PRO_RETURN.json
- daowei2026/observe-iterate@dcdf9949f1297f854dbd852f75a9f39ef268b72b:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_adapter.py
- daowei2026/observe-iterate@0fcb881f99c4035dc81de154f34d86e6994b1227:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_adapter_members.py
- daowei2026/observe-iterate@cf6a5d496f6b3bfafdadcbd7f11f30a5a182b158:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_adapter_support.py
- daowei2026/observe-iterate@3dc03ecfea52d38fa7ce965d17710f0ebb7b4021:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_common.py
- daowei2026/observe-iterate@9e03c89211ec4665763e1f609b37483c80c72930:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_definition.py
- daowei2026/observe-iterate@af96601fe525f2e6059ae3bd976b3b19de3060e7:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_plotters.py
- daowei2026/observe-iterate@eac1cb3342ff92961bf8055ac4c04042b94aeed4:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_plotters_base.py
- daowei2026/observe-iterate@6ffa0e4b6ebb394f61fcb52277f7c27c69fd35b9:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_plotters_build.py
- daowei2026/observe-iterate@23fcb47fff8494df138445fc5ee705fe43a36764:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_plotters_member.py
- daowei2026/observe-iterate@5152b1a05f532f59ebf27829682395a16938644e:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D004/DELEGATION.json
- daowei2026/observe-iterate@e3b200fe296e89825161e086ce49b2ee84e6329f:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0008/PRO_RETURN.json
- daowei2026/observe-iterate@f4c1542843ba15b887fd2a9ae23eb9bc6dd31a36:longrun/runs/OI-U2-Q-OBS-20261120-01/business_control/TASK_PROGRESS.md
- daowei2026/observe-iterate@e5a6902148afc5deb2c8268b96856892e3a976a4:longrun/runs/OI-U2-Q-OBS-20261120-01/RUN_BINDING.json
- daowei2026/observe-iterate@1fb666ce9851138edf757b18ecba63d025eed240:longrun/runs/OI-U2-Q-OBS-20261120-01/OWNER_START.md

以下原专业报告和正式 Return 逐字转交。全部 D 原生产物请依精确不可变引用完整读取。

## D 原专业报告（原文）

# C0009 专业报告｜D004｜Q 的 D Skill

## 1. 回交身份

| 字段 | 值 |
|---|---|
| run_id | `OI-U2-Q-OBS-20261120-01` |
| call_id | `C0009` |
| delegation_id | `D004` |
| work_item_id | `OI-U2-Q-OBS-20261120-01-WI-D` |
| stage_instance_id | `OI-U2-Q-OBS-20261120-01-M-D` |
| sender | `chatgpt:OI-U2-Q-OBS-20261120-01:executor:E1` |
| return_to | `chatgpt:OI-U2-Q-OBS-20261120-01:manager` |
| invocation_token | `631516d6330741629aa29813c402ed85` |
| 专业状态 | `REPORTED_COMPLETE` |

本次只执行原 D004 绑定的 D Skill：`caegraph-definition-integration`。A、B、C 均作为原 manager 已消费的当前有效上游使用，没有重跑；没有进入 E，没有运行最终图，也没有派 Worker。

## 2. 原生产物

### 2.1 人读 D 产物

`daowei2026/observe-iterate@3b3df7d4509860be1d43233736aecfb264732585:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/D_CAEGRAPH_DEFINITION_INTEGRATION.md`

### 2.2 机读 D 产物

`daowei2026/observe-iterate@546e457983c7d3e00378eea26872e605d79f8e20:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/D_CAEGRAPH_DEFINITION_INTEGRATION.json`

### 2.3 定义级检查

`daowei2026/observe-iterate@78b306ae3dba130b4bd1015befdebe19090ac728:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/D_DEFINITION_CHECKS.json`

## 3. 完整 CAEGraph 定义

E 的可执行入口：

`daowei2026/observe-iterate@9e03c89211ec4665763e1f609b37483c80c72930:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_definition.py`

入口与同目录八个支持模块共同构成 `Q-CAEGRAPH-D004-v1`：

- common／合同：`daowei2026/observe-iterate@3dc03ecfea52d38fa7ce965d17710f0ebb7b4021:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_common.py`
- locked-table support：`daowei2026/observe-iterate@cf6a5d496f6b3bfafdadcbd7f11f30a5a182b158:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_adapter_support.py`
- member adapter：`daowei2026/observe-iterate@0fcb881f99c4035dc81de154f34d86e6994b1227:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_adapter_members.py`
- exact occurrence adapter：`daowei2026/observe-iterate@dcdf9949f1297f854dbd852f75a9f39ef268b72b:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_adapter.py`
- lifecycle/state plotters：`daowei2026/observe-iterate@eac1cb3342ff92961bf8055ac4c04042b94aeed4:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_plotters_base.py`
- member plotters：`daowei2026/observe-iterate@23fcb47fff8494df138445fc5ee705fe43a36764:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_plotters_member.py`
- audit/assembly：`daowei2026/observe-iterate@6ffa0e4b6ebb394f61fcb52277f7c27c69fd35b9:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_plotters_build.py`
- plotter exports：`daowei2026/observe-iterate@af96601fe525f2e6059ae3bd976b3b19de3060e7:longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D/q_caegraph_plotters.py`

这是一份模块化的完整定义，不是九个候选方案。E 只需在该目录运行入口脚本。

## 4. 正式实例与位置绑定结果

### 4.1 实例

D 在 `CurrSof / CurrCalendar` 中使用正常 `make_features(...)` 构造，并只取第二项 Q：

```text
TA_updto20240229_DBA
steel
night_end_at_2300
5m
rb / hc / i
DirectionUp
Δ = 600
source_core_multiples = 30
```

完整 `make_features` 参数与外层输入完全一致；第一项 F 仅是 Q 的准确必要上游，V 被明确排除。

### 4.2 B 位置

绑定为：

```text
SOF: TA_updto20240229_DBA
Calendar: night_end_at_2300
objects: rb,hc,i
PlotSet timespan:
  2021-01-01 00:00:00
  → 2022-12-31 23:59:59
```

该右边界是在锁定 `PlotCtx` 的 `timesearch + end_uti += 1` 语义下，对 B 日期合同的唯一完整结束日绑定；没有换品种、换日期或修改 SOF。

## 5. A 字段绑定结果

D 从正式 F/Q 表按真实 MultiIndex 父子坐标形成六张 canonical frames：

```text
timeline
revision_links
states
members
quantities
audit
```

已进入代码的 A 事实包括：

- F candidate exact 与成员；
- Q Life／Revision／Previous；
- 准确 F candidate reference；
- Q publication firing 和 `directionalKnown`；
- qualification／observation／applicability；
- 原始和当前 anchor／deadline／revisionEnd；
- 成员 asked／used／successor／endpoint 的 actual、price、confirmation、known、clock；
- completion／verdict／basis／pathComplete；
- through／materialKnown／missingRange；
- 六类 quantity 及 availability；
- 显式 `DirectionalDutyEnd` 的 last successful Q、reason、known、progress。

脚本明确拒绝：

- 只按时间或成员名进行模糊 join；
- Q 引用不存在的 F exact；
- Previous 跨 Q Life；
- 一版 Q 少于两个唯一成员；
- 六量种类／顺序不完整；
- 不可用 quantity 同时携带数值；
- duty end 引用不存在的最后成功 Q。

## 6. C2/C3 集成结果

C2 当前五层展示语义完整保持：

1. P1：多品种 ratio 总览，raw 证据另存；
2. P2：F candidate → Q revision chain → explicit duty end；
3. P3：qualification／observation／applicability；
4. P4：逐品种 raw K、成员多位置、verdict、completion、六量与缺失；
5. P5：Q/F exact、Previous、known、last successful 和 end audit。

C2 中所有确定性示意身份和数值已被正式数据接口替换。D 没有改变页面、图元含义、转换、交互或业务阅读方式。

## 7. CAEGraph 仓库理解与真实链

锁定版本：

`daowei2026/uplot@0a4fcd54059782572a3f7e82fad041121e8c65ad`

D 已核对正式导出、`CAEGraph / PlotSet`、布局类、`BasePlotter`、`KPriceLine`、`PlotCtx`、`PlotDataFolder / PlotDataNode`、DynStd、共享 x-range、hover、图例、`fit_y_range.js` 和 `dynstd.js`。

本定义的真实路径是：

```text
OptContext + PlotSet
→ PlotCtx(SOF / calendar / symbols / timespan)
→ KPriceLine / custom BasePlotter
→ ColumnDataSource
→ ctx.add_cds
→ PlotDataFolder / PlotDataNode
→ Bokeh HTML + 可导出构图数据
```

## 8. 四项确定性纠正

### `D-CORR-001`｜PlotDataTree

C3 custom CDS 未登记 `ctx.add_cds`。D 按锁定仓库唯一修为统一 `_registered_cds`；不改变任何图义。

### `D-CORR-002`｜显式 duty end

锁定 TIS 的 v2 wrapper registry 未公开 `organizationDutyEnds`，但锁定 FRP 存储类型唯一规定了 duty-end 字段。D 采用同 layout 的 `_event_df` 直接投影正式存储，不重新计算、不猜业务含义，并继续将 end 与 Q revision 分开。

### `D-CORR-003`｜日期日内边界

把 B 的 `2021-01-01～2022-12-31` 唯一具体化为完整日的 PlotSet timestamp；没有改变“最终看哪里”。

### `D-CORR-004`｜raw price Feature

把 C3 的 `price_feature` 占位绑定为 `KLine(freq='5m')`，满足锁定 `KPriceLine` 的 OHLC 接口；P1 ratio 与 P4 raw 的区分不变。

四项纠正均逐字段记录在机读 D 产物中；没有无痕改动，也没有需要退回 A/B/C 的不确定问题。

## 9. 定义级检查结果

已真实重跑：

- 九个发布模块 SHA-256 与检查记录一致；
- 九模块全部 `py_compile` 通过；
- 九模块 AST 解析通过；
- 隔离 stub 环境完整导入九模块；
- 合法空 canonical-frame 合同通过；
- exact instance／B position／A fields／C2 panels／PlotDataTree 的静态绑定通过；
- 未发现未替换占位、`TODO`、`FIXME` 或 `NotImplemented`；
- 默认 `read` 禁止暗中重跑。

未运行、且不在 D 中虚称完成：

- `/dwdhome/fy/BASE_E6_2_copy` 的真实依赖导入；
- 正式 F/Q 数据读取；
- 真实 adapter invariants；
- HTML、DynStd、hover、JS 和 PlotDataTree 输出；
- 性能及页面业务核对。

上述内容属于 E。

## 10. 给 E 的执行入口与预期输出

只读验证：

```bash
cd longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D
python q_caegraph_definition.py --mode read --validate-only
```

只读生成正式图和构图数据：

```bash
cd longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/D
python q_caegraph_definition.py --mode read
```

预期输出：

```text
longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/E/Q_CAEGRAPH.html
longrun/runs/OI-U2-Q-OBS-20261120-01/artifacts/E/Q_CAEGRAPH_DATA/
```

如果准确实例没有既存正式产品，read 模式应明确失败；是否获准运行全期 F/Q 由后继 Workflow 决定，D 没有自行授权。

## 11. Worker、权限与完成判断

- Worker orders：无；
- accepted Worker returns：无；
- 新写入均位于本 Run 目录；
- 没有运行全历史 producer；
- 没有启动 V；
- 没有剩余 D 范围；
- 没有 Owner 请求。

D004 的原生完成条件已经满足，D Skill 判定为：**完整**。

原 manager 可消费本报告和 D 原生产物，按既定 Workflow 决定是否签发 E；本 executor 不自行签发后继委派。


## C0009 原正式 Return（原文）

```json
{
  "schema": "longrun-professional-return/v2",
  "run_id": "OI-U2-Q-OBS-20261120-01",
  "call_id": "C0009",
  "role": "executor",
  "sender": "chatgpt:OI-U2-Q-OBS-20261120-01:executor:E1",
  "delegation_ref": "daowei2026/observe-iterate@5152b1a05f532f59ebf27829682395a16938644e:longrun/runs/OI-U2-Q-OBS-20261120-01/delegations/D004/DELEGATION.json",
  "return_to": "chatgpt:OI-U2-Q-OBS-20261120-01:manager",
  "result_ref": "daowei2026/observe-iterate@91fe9d8768d528a2ff616917a42412afb25fcc8a:longrun/runs/OI-U2-Q-OBS-20261120-01/calls/C0009/PROFESSIONAL_REPORT.md",
  "issued_delegation_refs": [],
  "issued_order_refs": [],
  "accepted_worker_refs": [],
  "professional_state": "REPORTED_COMPLETE",
  "remaining_scope_ref": null,
  "continuation_ref": null,
  "owner_request_ref": null
}
```

请实际发布本次 C0010 的 MANAGER_REPORT、更新后的 TASK_PROGRESS、下一真实 D（若具备合法后继）及本 C0010 合法 V2 PRO_RETURN.json；依固定协议在真实完成后标记本次精确 marker/token 的 turn complete。专业结果送达不替代你实际消费结果。
