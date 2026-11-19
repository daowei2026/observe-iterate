# C0023｜D006 E Skill 原生专业回交

## 1. 调用身份

- `run_id`: `OI-U2-F-OBS-20261118-01`
- `call_id`: `C0023`
- `invocation_token`: `d556d957198b45d9a957fc333b2c45c6`
- `delegation_id`: `D006`
- `work_item_id`: `OI-U2-F-OBS-20261118-01-WI-E-R1`
- `stage_instance_id`: `OI-U2-F-OBS-20261118-01-M-E-R1`
- `executor`: `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `return_to`: `chatgpt:OI-U2-F-OBS-20261118-01:manager`

本调用重新开始完整 E Skill，不继续 D005/W005。W005 已由 Owner 有据收束为 `NOT_SENT → SUPERSEDED`；W001～W004 旧 STOP 历史保留，但未被当成本次 E 方案或完成证据。

## 2. 已实际完成的专业工作

### 2.1 完整采用 E 原件

本调用已依据锁定 `observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288` 采用：

- `SKILL.md`
- `WORKFLOW.md`
- `IO_SPEC.md`
- `WORKER_DELEGATION.md`
- `RUN_REPAIR_ORDER_TEMPLATE.md`
- `DATA_EXPORT_ORDER_TEMPLATE.md`
- 通用 `WORKER_ORDER.md`

当前只推进到 E1 和 W1 签发；图尚未接受，因此没有形成 E4 正式取数准入，也没有签发 W2。

### 2.2 E1 最小执行与核图基准

已形成：

`daowei2026/observe-iterate@3dff93bcbe19a8d6e7324f2a527a43d1adbeb807:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E1_EXECUTION_AND_GRAPH_CHECK_BASELINE_D006_C0023.md`

基准固定：

- 唯一 D 脚本：`f4f0e4b.../u2_f_caegraph_definition.py`
- 唯一 C2 核图 HTML：`56eef30b.../caegraph_display_preview.html`
- 工作区：`/dwdhome/fy/BASE_E6_2_copy`
- 运行对象：`make_features(...)[0]` 的 F
- 输出：W006 自己的 `output/u2_f_caegraph`
- 不运行 Q/V、不调用 F producer、不进入合理性分析

基准明确区分：

- FRP Haskell：`frp@67711c...`，工作区对应源码位置预期为 `edh-universe/frp/frp`；
- TIS Python：`tis@2f460d.../frp/fqv_kline_example.py`，运行 import 为 `mquant.tis.frp.fqv_kline_example`。

不得把 `mquant.tis.frp` 当成 Haskell FRP 仓库，不得构造 TIS overlay、混合 package 或重建平台。

### 2.3 新 W1 工单 W006

已签发：

- 正文：`daowei2026/observe-iterate@548492bbcf524d4a223b1048010dbe8fd8b902b9:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W006/ORDER.md`
- 机读工单：`daowei2026/observe-iterate@ce230480cdbaf0133e3d719e3750c42f52664134:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W006/ORDER.json`

W006 要求在当前真实 FY 环境先运行原 D，优先返回：

1. 可打开的候选 `u2_f_caegraph.html`；或
2. 本次新的第一个真实阻断及 `definition_run_report.json`。

W006 只允许对 D/C3 做有界、run-local、确定性的机械修复；禁止修改／拼装 TIS、FRP、uplot、m3、mquant 平台源码或安装，禁止额外沙箱、版本切换、Q/V、producer 和正式取数。

## 3. 当前真实状态

| 项目 | 状态 |
|---|---|
| 新委派 | `D006` 已由 E2 接收并开始 |
| E1 基准 | 已完成 |
| 新工单 | `W006` 已发布 |
| 物理 Worker | `codex:OI-U2-F-OBS-20261118-01:worker:W1` |
| W006 物理派发 | **尚无真实发送回执；不得由文件发布推断已发送** |
| 第一个真实业务运行里程碑 | **尚未发生** |
| 候选 HTML | 尚无本次结果 |
| E2/E3 分类与核图 | 等待 W006 Return |
| W2 正式取数 | 未准入、未签发 |
| E 阶段 | `IN_PROGRESS` |

当前第一个真实业务运行里程碑定义为：W006 在当前环境启动原 D，并产生候选 HTML，或产生新的首个真实阻断及 run report。该里程碑必须由真实 Worker Return 证明。

## 4. 原生后继

主控只需按现行 V2 做 W006 派发前的最小核验：

- 收件线程仍为本 Run 专用 Worker；
- 当前工作区／写面与 Binding 一致；
- 无在途或 UNKNOWN 冲突；
- 原 W006 权限、身份和精确引用成立。

核验后原样物理派发 W006，不增加环境建设、overlay 或修法。完整 Worker 结果须回本 Chat `executor:E2`；后续继续同一：

```text
D006
OI-U2-F-OBS-20261118-01-WI-E-R1
OI-U2-F-OBS-20261118-01-M-E-R1
```

E2 将按原 E Skill 进入 E2 候选运行分类，再决定续发 W1、返回 B/C/D、进入 E3 核图，或保持阻断。只有图被 E 接受后才允许形成 E4/W2。

## 5. 本次专业状态

```text
professional_state = IN_PROGRESS
continuation = W006 Worker Return → original executor:E2
```

本调用没有声明 E 完成、没有声明图通过、没有声明 `DATA_READY`。