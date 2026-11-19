# C0027｜D006 E Skill：消费 W009，确认 runtime 外部对齐前置并等待 Owner

## 1. 调用身份

- `run_id`: `OI-U2-F-OBS-20261118-01`
- `call_id`: `C0027`
- `invocation_token`: `7452296d205847129e38591d6f497f5f`
- `delegation_id`: `D006`
- `work_item_id`: `OI-U2-F-OBS-20261118-01-WI-E-R1`
- `stage_instance_id`: `OI-U2-F-OBS-20261118-01-M-E-R1`
- `executor`: `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `physical_chat`: `FOBS-1119-E2`
- `return_to`: `chatgpt:OI-U2-F-OBS-20261118-01:manager`

本调用继续原 D006 和当前工作项／阶段实例；没有新建 D，没有重派 W009，没有恢复 D005/W005，没有重跑 A～D，没有启动 Q/V。

## 2. 已正式消费 W009

正式 Return：

`daowei2026/observe-iterate@ec7a6d4f79af4fbc60ec02508eeab01aa61cc480:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W009/WORKER_RETURN.json`

本 executor 已核对并接受 W009 的 `run_id / work_order_id / order_ref / worker / return_to`、事实报告和 manifest 所列必要证据。本次 V2 Return 只把这份正式 Worker Return 登记到 `accepted_worker_refs`。

W009 的 `outcome=STOP` 合法结束该工单，不代表 D006/E 或 F Run 业务完成。

## 3. W009 的关键证据链

固定候选：

```text
/dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117
```

### 3.1 已通过的来源检查

W009 已确认：

- 候选已有 `run_in_runtime.py` 入口，由现存 `fqv.sh` 引用；
- 候选没有在本 W 中新建 wrapper、activation、launcher、`.pth` 或 `sitecustomize`；
- `fqv_kline_example.py` 及 F/Q/V 三个 wrapper 与锁定 `tis@2f460d...` 对应 blob 逐字节一致；
- 候选自己的 `blk/gen.py` 与 `t0/t1/t2/t3` 包路径存在；
- 候选 `provenance.json` 的 `versions.frp` 是锁定 `frp@67711c...`；
- 13 个指定模块在候选现有入口下全部可导入；
- probe 没有调用 `make_features`、FAO、producer 或产品读取，也没有由 probe 代码修改 `sys.path` 或 package `__path__`；
- W008 所见 `.codex` symlink 没有被再次误用为一票否决原因。

### 3.2 真实首阻断

同一次实际 origin probe 加载了 260 个 `mquant*` 模块，其中 165 个模块的物理来源解析到候选 `runtime/mquant` 根之外。

首个事实例子：

```text
mquant reported __file__:
  .../.runtime/fqv-rb-hc-i-20261117/runtime/mquant/__init__.py

resolved physical source:
  /dwdhome/fy/BASE_E6_2_copy/mquant/__init__.py
```

`mquant.apt`、`mquant.frame` 等也存在同类来源。该判断来自实际 import closure 的 `__file__ / __path__ / spec.origin` 与物理路径解析，不是对目录名字或 symlink 存在的猜测。

精确 Worker 分类：

```text
DEDICATED_RUNTIME_MIXED_MQUANT_ORIGINS
```

W009 因此按原工单停止：D 启动 0 次，无 D 退出码；没有 HTML、definition report、prepared tables 或 plot data；F 未构造，`fields.json` 未检查。

## 4. E2 专业分类

原生产物：

`daowei2026/observe-iterate@982ec813a5bccb2f798417adeab92b31eb38d808:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E2_W009_RESULT_CLASSIFICATION_AND_OWNER_RUNTIME_PREREQUISITE_D006_C0027.md`

最终分类：

```text
EXTERNAL_LOCKED_FQV_RUNTIME_ALIGNMENT_REQUIRED
```

这表示：当前 D006 已获准使用的 FY 现有环境中，没有一个已经证明可以在不安装、不构建、不切版本、不复制文件、不做 overlay／混包的条件下运行锁定 FQV 组合的单一正常 runtime。

它不表示 F 产品不存在，也不反证 A～D 已完成的业务成果。

## 5. 原 Workflow 分流

### 5.1 不返回 B

尚未构造 F、读取正式表或触达 B 的观察位置。

### 5.2 不返回 C

没有候选 HTML，C2 展示预期没有被真实结果证伪。

### 5.3 不返回 D

D/C3 没有被 W009 修改；当前失败发生在运行来源准入，不能据此改写 D 的实例、字段、位置或展示接线。

### 5.4 不进入 E3、E4 或 W2

- 没有 HTML，不能核图；
- 图未接受，不能形成正式取数准入；
- `DATA_READY=false`。

### 5.5 不再续发环境探测型 W1

C0026/W009 已明确规定：若既有入口、TIS 锁定、单一来源、FRP provenance 或 origin probe 任一失败，则收敛为 `EXTERNAL_LOCKED_FQV_RUNTIME_ALIGNMENT_REQUIRED`，不再签发同类环境探测型 W1。

W009 的失败正是实际 import closure 的单一来源失败，不是 W008 那种目录级假阳性。

## 6. 为什么当前授权下没有机械后继

消除 165 个候选根外来源，至少会涉及改变 package 物理布局、import path、symlink、平台安装／构建、版本组合或 runtime 选择之一。这些动作：

- 不是只改 D/C3 的唯一确定机械修复；
- 不在当前 D006 的原生 W1 修复边界内；
- 与 Owner 明确的“不得重建 TIS package、不得构造 overlay、不得混合 package、不得自行切换版本”边界冲突；
- 不能由主控或 Worker擅自设计。

因此本调用：

```text
issued_order_refs = []
```

## 7. 已形成 Owner 请求

正式 Owner 请求：

`daowei2026/observe-iterate@806304b45d063ec2b95aa4c0a639eb6a968960a9:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0027/OWNER_REQUEST.md`

请 Owner 明确选择：

1. **A｜指定现有合格 runtime**：锁定 TIS／FRP 且全部实际 `mquant*` import closure 来源单一、可追溯、已授权；
2. **B｜授权独立环境对齐工作**：另行明确目标组合、operation、execution context、allowed writes 和可做／不可做动作；
3. **C｜停止 D006/E**：保留未生成 HTML、未核图、未启动 W2、`DATA_READY=false` 的事实。

## 8. 当前专业状态与恢复点

```text
professional_state = WAITING_OWNER
accepted_worker_refs = [W009]
issued_order_refs = []
owner_request_ref = C0027/OWNER_REQUEST.md
continuation_ref = null
```

当前 Worker 已由主控确认 idle、无在途，workspace 租约已释放；这只是物理状态，不改变专业等待条件。

若 Owner 选择 A，或选择 B 且环境前置完成，原 D006 的恢复点为：

```text
A～D 不重跑
E1 基准保持
→ 在获准单一 runtime 中签发新 W1 运行原 D
→ E2 消费真实结果
→ 有 HTML 后进入 E3
```

若 Owner 选择 C，则由 manager 按现行 V2 有据收束 D006/E；不能标记为 `DATA_READY` 或 E 成功完成。

## 9. 当前未满足的 E 完成条件

- 原 D 尚未在合格的本次 runtime 中成功运行；
- 最终脚本与真实图尚未进入 E3 核对；
- 没有被 E 接受的 HTML；
- E4 正式取数准入未形成；
- W2 未签发，正式数据未取得；
- `DATA_READY=false`；
- D006/E 业务未完成。
