# C0024｜D006 E Skill：消费 W006、完成 E2 分类并签发 W007

## 1. 调用身份

- `run_id`: `OI-U2-F-OBS-20261118-01`
- `call_id`: `C0024`
- `invocation_token`: `510f067ff69340b7b4cdf0d192a96497`
- `delegation_id`: `D006`
- `work_item_id`: `OI-U2-F-OBS-20261118-01-WI-E-R1`
- `stage_instance_id`: `OI-U2-F-OBS-20261118-01-M-E-R1`
- `executor`: `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `return_to`: `chatgpt:OI-U2-F-OBS-20261118-01:manager`

本调用继续原 D006 和当前工作项／阶段实例；没有新建 D，没有恢复 D005/W005，没有重跑 A～D，没有启动 Q/V。

## 2. 已正式消费的 W006

正式 Return：

`daowei2026/observe-iterate@b499d528dbca99d153b86a216833b7da8b5140d0:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W006/WORKER_RETURN.json`

本 executor 已核对并接受 W006 的身份、order ref、worker、route、事实报告和 manifest 所列必要证据。本次 V2 Return 将只把该正式 Worker Return 登记到 `accepted_worker_refs`。

### 2.1 真实运行事实

- 原 D 启动两次，退出码均为 1；另有一次最小 constructor import 定位。
- `/usr/bin/python` 首先缺少 `numpy`；加载当前工作区 `m3rc` 后，正常 FY Python 已进入 D `main()`。
- 当前真实首阻断为：

  ```text
  ModuleNotFoundError: No module named 'mquant.tis.frp.fqv_kline_example'
  ```

- 当前活跃父包来自 `/dwdhome/fy/BASE_E6_2_copy/mquant/tis`。
- 原 D/C3 hash 未变，`repair.diff` 为空。
- 失败早于 `make_features`、F 构造、`fields.json`、正式表读取和绘图。
- Haskell 固定源码路径存在，但当前 HEAD=`37c790c0f456fe3022bb00609219d3e92a5c2f9b`，与锁定 `67711c...` 不同；该差异尚未被误当成 Python import 的直接原因。
- 没有候选 HTML、prepared tables 或 plot data；W2 未启动，`DATA_READY=false`。

## 3. E2 专业分类

原生产物：

`daowei2026/observe-iterate@54fb6c997210ffe7bebb67abf52f61473bc523d2:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E2_W006_RESULT_CLASSIFICATION_AND_W007_BASELINE_D006_C0024.md`

分类：

```text
CURRENT_FY_NORMAL_FQV_PACKAGE_PROVENANCE_GAP
```

### 3.1 为什么不是返回 B／C／D

- **不是 B**：尚未构造 F，未触达观察位置和真实表。
- **不是 C**：尚未生成图，展示预期未被实际结果证伪。
- **不是 D**：D 使用锁定正常 import，实例、字段、位置和 C3 没有被 W006 改动或反证。

### 3.2 为什么不能进入 E3／E4

- 没有 HTML，不能核图或接受图；
- 图未接受，不能形成正式取数准入；
- W006 的 run report 为 `completed=false`；
- 不得把调试副产物或历史成功结果冒充本次正式交付。

### 3.3 与 2026-11-16 正常成功现场的对照

锁定 TIS `2f460d...` 明确包含 `frp/fqv_kline_example.py`，并以正常 `CurrSof / CurrCalendar + make_features(...)` 构造 F/Q/V。2026-11-16 改动说明记录该文件是正常 Python 包装，并在正常平台构建后成功运行和跨进程公开读回。

W006 当前只证明 FY 活跃 `mquant.tis.frp` 不暴露该模块；它没有证明 import 名错误，也没有证明 F 产品不存在。真正未决的是：当前 FY 活跃 Python 包、TIS 源码和 FRP 源码／运行来源是否与 D006 锁定组合一致。

## 4. 原生后继：W007

### 4.1 正文

`daowei2026/observe-iterate@4db7b49e165d025a5f24a39878f893fe4aadf4be:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W007/ORDER.md`

### 4.2 机读工单

`daowei2026/observe-iterate@1ec2229ce44a92407e603e3a617a96616c5cde3c:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W007/ORDER.json`

### 4.3 专业目的

W007 是基准不变时的新 W1 revision，只做：

1. 当前 FY `m3rc` Python 的最小包来源核对；
2. 活跃 TIS 工作树的 root／HEAD／所需四文件核对；
3. 当前工作区内对 `fqv_kline_example.py` 的一次精确、有界查找，排除旧 Run staging 和其他工作区；
4. 固定 FRP 路径的 HEAD 核对；
5. **只有单一、完整、正常、精确锁定的运行来源已经存在时**，才运行原 D 一次；否则返回明确环境／版本差异，不建设环境。

### 4.4 明确不采用旧方案

W007 禁止：

- 分层 `__path__` overlay；
- 锁定 TIS 新层＋平台旧层混包；
- `seed_inits`／`pretty-exports`；
- checkout、切版本、拉取或恢复文件；
- `pip`、`conda`、`stack`、`cabal` 安装或重建；
- 从其他工作区借用绝对路径；
- 修改 TIS、FRP、m3、uplot、平台包或 D/C3；
- producer、Q/V、W2 和正式导出。

因此它不续用 D005/W005 的专业方案，只落实 Owner 要求的“核对 FY 当前源码和运行包来源”。

## 5. 当前真实状态

| 项目 | 状态 |
|---|---|
| D006 | 继续有效 |
| W006 | `STOP`；已由 E2 正式消费 |
| E2 分类 | 已完成 |
| W007 | 已发布，**尚无真实物理发送回执** |
| 物理 Worker | `codex:OI-U2-F-OBS-20261118-01:worker:W1`；主控报告当前空闲、写锁已释放 |
| 候选 HTML | 无 |
| E3 | 未开始 |
| E4/W2 | 未准入、未签发 |
| DATA_READY | `false` |
| E 专业状态 | `IN_PROGRESS` |

发布 W007 文件不等于已经物理派发，也不等于环境已修复或 E 已完成。

## 6. 主控最小后继

主控只需按现行 V2 做 W007 派发前核验：

- 收件线程仍是本 Run 专用 W1；
- W006 已结束且不存在 UNKNOWN／IN_FLIGHT 冲突；
- cwd 与当前 Binding 仍为 `/dwdhome/fy/BASE_E6_2_copy`；
- grant、写面、ORDER.md／ORDER.json 和 issuer_call_id 成立；
- 原样发送，不新增 overlay、构建、版本切换或环境修复方案。

W007 完整 Return 必须回本 `executor:E2`。收到后继续同一：

```text
D006
OI-U2-F-OBS-20261118-01-WI-E-R1
OI-U2-F-OBS-20261118-01-M-E-R1
```

- 正常入口判据通过且有 HTML：消费运行事实后进入 E3；
- 判据通过但无 HTML：消费新的首阻断并继续 E2 分类；
- 判据失败：由 E2 根据精确来源差异决定是否形成外部运行前置／Owner 请求；主控不得自行设计修复；
- 只有 E3 接受图后才允许 E4/W2。

## 7. 本次专业状态

```text
professional_state = IN_PROGRESS
accepted_worker_refs = [W006]
issued_order_refs = [W007]
continuation = W007 Worker Return → original executor:E2
```

本调用没有声明 E 完成、没有声明图通过、没有声明 F 产品不存在、没有声明 `DATA_READY`。
