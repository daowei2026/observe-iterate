# E2｜消费 W006、分类当前阻断并建立 W007 基准

## 1. 身份与已消费 Return

- `run_id`: `OI-U2-F-OBS-20261118-01`
- `delegation_id`: `D006`
- `work_item_id`: `OI-U2-F-OBS-20261118-01-WI-E-R1`
- `stage_instance_id`: `OI-U2-F-OBS-20261118-01-M-E-R1`
- `executor`: `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `call_id`: `C0024`
- 已消费 Worker Return：`daowei2026/observe-iterate@b499d528dbca99d153b86a216833b7da8b5140d0:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W006/WORKER_RETURN.json`

W006 的身份、路由、工单引用和签认成立。本 E2 接受其事实与实物，不把 `outcome=STOP` 解释为 D006/E 已完成或整个 Run 结束。

## 2. W006 已证明的事实

1. 原 D/C3 精确源码命中，运行前后 hash 不变；`repair.diff` 为空。
2. `/usr/bin/python` 缺少 `numpy`，但这不是当前 FY 正常入口下的最终阻断。
3. 加载当前工作区 `m3rc` 后，实际入口为 `/m3c3/Linux/apps/anaconda3/bin/python`；D 已进入 `main()`。
4. 当前活跃父包来自：
   - `/dwdhome/fy/BASE_E6_2_copy/mquant/__init__.py`
   - `/dwdhome/fy/BASE_E6_2_copy/mquant/tis/__init__.py`
   - `/dwdhome/fy/BASE_E6_2_copy/mquant/tis/frp/__init__.py`
5. 当前真实首阻断为：

   ```text
   ModuleNotFoundError: No module named 'mquant.tis.frp.fqv_kline_example'
   ```

6. 失败发生在 `make_features` 调用、F 构造、`fields.json` 检查、正式表读取和绘图之前。
7. Haskell 源码路径存在，但当前 HEAD=`37c790c0f456fe3022bb00609219d3e92a5c2f9b`，与锁定 `67711c492da909ed0f044f357beb278abf7fc71c` 不同；该差异尚不能单独证明 Python import 失败的原因。
8. 没有候选 HTML，没有 prepared tables／plot data；W2 未启动，`DATA_READY=false`。

## 3. 与锁定正常用法和 2026-11-16 成功现场的对照

锁定 TIS 原件 `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py` 明确提供：

```python
from mquant.tis.frp.fqv_kline_example import make_features
```

并由正常 `CurrSof / CurrCalendar` 环境构造 `f, q, v`。2026-11-16 改动说明记录：该文件是当轮新增的正常 Python 包装；成功现场在正常平台构建后，以普通 Python FAO 包装完成 F/Q/V 运行与另一进程公开读回。

因此，W006 当前能够证明的是：

> FY 活跃 `mquant.tis.frp` 包没有暴露本次锁定构造模块；当前运行包来源与锁定 FQV 正常组合尚未对齐或尚未被证明对齐。

它**不能**证明：

- D 的 import 名写错；
- F 产品不存在；
- B 的位置错误；
- C 的展示错误；
- D 的实例、字段或展示集成错误；
- Haskell HEAD 差异必然导致当前 Python import 失败。

## 4. E2 专业分类

```text
CURRENT_FY_NORMAL_FQV_PACKAGE_PROVENANCE_GAP
```

| Workflow 分类 | 判断 |
|---|---|
| 返回 B | 否；尚未触达位置与真实 F 表 |
| 返回 C | 否；尚未生成图，展示合同未被证伪 |
| 返回 D | 否；原 D 使用的是锁定正常 import，D/C3 未改且无集成反证 |
| 进入 E3 | 否；没有 HTML |
| 进入 E4/W2 | 否；图尚未接受 |
| 基准不变时续发 W1 | **是，但只允许一次有界的正常包来源核对与条件运行** |

这不是允许重演旧 D005/W004/W005 的环境拼装。以下均明确排除：

- `mquant.__path__`／`mquant.tis.__path__` 分层 overlay；
- 锁定新层＋平台旧层混包；
- `seed_inits.py`、`pretty-exports.py` 或其他 package materialization；
- checkout／pull／reset／切换仓库版本；
- `pip`／`conda`／`stack`／`cabal` 安装或重建；
- 从其他工作区绝对路径运行；
- 修改 TIS、FRP、m3、uplot、平台包或 D/C3 业务语义。

## 5. W007 的最小专业目标

W007 只回答一个问题：

> 在 `/dwdhome/fy/BASE_E6_2_copy` 当前既有、正常、单一包来源中，是否已经存在与锁定 TIS 构造入口相符的可运行环境？

### 5.1 先做只读来源核对

- 记录当前正常 Python、`sys.path` 和 `mquant / mquant.frame / mquant.tis / mquant.tis.frp` 的实际来源；
- 对当前活跃 TIS 源码取得 Git root、HEAD、remote、工作树状态；
- 核对 `fqv_kline_example.py` 及 F/Q/V 三个包装文件是否存在；
- 在当前工作区内对精确文件名做一次有界查找，排除 `observe-iterate-runs/**`、旧 W staging 和其他工作区；
- 记录 Haskell FRP 当前路径／HEAD，不切版本；
- 不制作大环境报告，只输出一个最小来源判断 JSON。

### 5.2 仅在唯一正常入口成立时运行

只有同时满足以下条件，才允许再次运行原 D：

1. 构造模块由当前工作区内一个**单一、完整、正常**的活跃包提供；
2. 不修改任何 package `__path__`，不拼接两个 TIS 来源；
3. 不使用旧 W checkout 或其他工作区；
4. F/Q/V 包装来源可回查到锁定 TIS 组合；
5. 运行不需要安装、重建、切版本或修改平台文件。

若成立，使用该既有正常入口运行原 D 一次，返回候选 HTML 或新的首阻断。

若不成立，立即停止并回 E，明确区分：

```text
LOCKED_TIS_NORMAL_PACKAGE_ABSENT
ACTIVE_TIS_VERSION_MISMATCH
MULTIPLE_OR_PARTIAL_PACKAGE_SOURCES
FRP_RUNTIME_PROVENANCE_UNRESOLVED
```

不自行建设环境。

## 6. 当前续接点

```text
D006 / WI-E-R1 / M-E-R1
E state = IN_PROGRESS
accepted worker = W006
next native action = W007 W1 revision
E3 = not started
E4/W2 = not admitted
DATA_READY = false
```
