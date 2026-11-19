# E2｜消费 W009，确认锁定 FQV runtime 外部对齐前置

## 1. 身份与已消费 Return

- `run_id`: `OI-U2-F-OBS-20261118-01`
- `delegation_id`: `D006`
- `work_item_id`: `OI-U2-F-OBS-20261118-01-WI-E-R1`
- `stage_instance_id`: `OI-U2-F-OBS-20261118-01-M-E-R1`
- `executor`: `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `call_id`: `C0027`
- 已消费 Worker Return：`daowei2026/observe-iterate@ec7a6d4f79af4fbc60ec02508eeab01aa61cc480:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W009/WORKER_RETURN.json`

W009 的身份、原 W009 order ref、Worker、return route 和必要证据 manifest 已经由主控核验并合法回交。本 E2 接受其事实与实物。`outcome=STOP` 结束 W009，不等于 D006/E 或 F Run 业务完成。

## 2. W009 已完成的有效核验

固定候选：

```text
/dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117
```

W009 已证明：

1. 候选已有入口可识别：`run_in_runtime.py`，由现有 `fqv.sh` 引用；本 W 没有新建 wrapper、activation、launcher、`.pth` 或 `sitecustomize`。
2. 候选中的以下四个 TIS 文件，与锁定 `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767` 的对应 blob 逐字节一致：
   - `frp/fqv_kline_example.py`
   - `frp/CommonPriceTurnGroupCandidates.py`
   - `frp/PostTurnGroupDirectionalOrganization.py`
   - `frp/CommonTurnGroupValidity.py`
3. 候选自身存在 `blk/gen.py` 和 `t0/t1/t2/t3` 包入口；未从旧 Run staging 补齐。
4. 候选 `provenance.json` 的 `versions.frp` 明确记录锁定 `daowei2026/frp@67711c492da909ed0f044f357beb278abf7fc71c`。
5. 在候选现有入口下做的一次无业务动作 origin probe 中，13 个指定模块全部可导入；没有调用 `make_features`、FAO、producer 或产品读取，probe 代码没有修改 `sys.path` 或 package `__path__`。
6. `runtime/.codex` 的存在没有被继续误判为失败原因；Python executable、`sys.path` 和入口链没有显示依赖其目标。

这些事实排除了 W006 的“构造模块完全找不到”和 W008 的“任意外部 symlink 即失败”两种不充分分类。

## 3. W009 暴露的真实首阻断

Origin probe 实际加载了 260 个 `mquant*` 模块，其中 165 个模块的物理来源解析到候选 `runtime/mquant` 根之外。

首个例子：

```text
module: mquant
reported __file__:
  /dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117/runtime/mquant/__init__.py
resolved physical source:
  /dwdhome/fy/BASE_E6_2_copy/mquant/__init__.py
expected single root:
  /dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117/runtime/mquant
```

`mquant.apt`、`mquant.frame` 等也存在同类物理来源事实。该结果来自同一次实际 import closure 探针，不是仅凭目录名字、symlink 存在或字符串前缀作出的判断。

精确分类：

```text
DEDICATED_RUNTIME_MIXED_MQUANT_ORIGINS
```

因此：

- 候选中的锁定 TIS 文件和 FRP provenance 可以成立；
- 但候选运行时整体并不是一个已经证明单一、完整、锁定来源一致的 `mquant` runtime；
- 候选运行入口实际复用了当前工作区平台树中的大量 `mquant` 模块；
- 继续运行原 D 会把本次锁定 TIS/FRP 与未被本 D006 锁定证明的外部平台模块放入同一 import closure。

这正属于 Owner 明确禁止的 package 混合风险，不能由“13 个目标模块能导入”替代整体来源准入。

## 4. E2 专业分类

```text
EXTERNAL_LOCKED_FQV_RUNTIME_ALIGNMENT_REQUIRED
```

该分类的含义是：

> 当前 D006 允许使用的现有 FY 环境中，没有一个已经通过证据证明、可以在不安装、不构建、不切版本、不复制文件、不做 overlay／混包的条件下运行本次锁定 FQV 组合的单一正常 runtime。

它不表示：

- F 产品不存在；
- F 的 Haskell 实现错误；
- TIS 四个锁定文件错误；
- B 的观察位置错误；
- C 的展示预期错误；
- D 的实例、字段、位置或展示接线错误。

## 5. 原 Workflow 分流

| Workflow 后继 | 判断 |
|---|---|
| 返回 B | 否；尚未触达真实 F 表和观察位置 |
| 返回 C | 否；没有候选 HTML，展示合同未被实际结果证伪 |
| 返回 D | 否；D/C3 没有被修改，集成定义没有被该环境事实反证 |
| 继续环境探测型 W1 | **否**；W009 已完成最后一次来源准入探针并得到真实混源证据 |
| 进入 E3 | 否；没有 HTML |
| 进入 E4/W2 | 否；图未接受，`DATA_READY=false` |
| 向 Owner 提出运行前置 | **是** |

## 6. 为什么不能继续由 Worker 机械修复

要消除当前混源，至少会触及以下一种或多种动作：

- 改变候选 `mquant` package 的 symlink／物理布局；
- 复制、生成或重新物化平台 package；
- 改变 import path 或 package `__path__`；
- 重建、安装或切换平台版本；
- 选择另一 runtime／工作区；
- 明确接受某个非锁定平台组合并重新定义版本边界。

这些动作均不是当前 D006 下唯一确定的 D/C3 机械修复，也不在 Owner 本次“不得重建、不得 overlay、不得混合 package、不得自行切换版本”的边界内。E 不应把其中任一方案伪装成 import/path 小修后再签 W。

因此，本次：

```text
issued_order_refs = []
```

并且不再签发同类环境探测型 W1。

## 7. 需要 Owner 决定的运行前置

请 Owner 明确选择以下一种后继：

### A｜提供或指定已存在的合格 runtime

在合法 Binding 下提供或指定一个现有入口，满足：

```text
1. 正常导入 mquant.tis.frp.fqv_kline_example；
2. TIS 构造文件和 F/Q/V wrappers 对应锁定 tis@2f460d...；
3. FRP 运行来源对应锁定 frp@67711c...；
4. 实际 import closure 中全部 mquant* 模块来自一个明确、可追溯、获准的 runtime；
5. 不需要 overlay、跨 runtime 拼接、临时复制、安装、构建或版本切换；
6. 提供该 runtime 的实际工作区／入口，并使 RUN_BINDING／RUN_RESOURCE_BINDING 与其一致。
```

满足后继续原 D006：先签新的 W1 运行原 D，不直接进入 W2。

### B｜明确授权独立的环境对齐工作

如果当前没有上述 runtime，Owner 需另行明确：

- 目标 runtime／源码版本组合；
- 允许执行的环境对齐 operation；
- execution context 与 allowed writes；
- 可以进行和禁止进行的构建、安装、复制、symlink、版本切换等动作；
- 完成后怎样证明单一运行来源。

该环境工作不属于当前 D006 自动可做的机械修复；应由 manager 在 Owner 新授权和更新后的 Binding 下另行安排。环境前置完成后，再恢复原 D006。

### C｜有据停止本次 D006/E

若 Owner 不提供合格 runtime，也不授权独立环境对齐，则按现有证据停止 D006/E，并准确记录：E 未产生候选 HTML、未核图、未启动 W2、未形成 `DATA_READY`。

## 8. 恢复条件

当前等待点：

```text
D006 / WI-E-R1 / M-E-R1
professional state = WAITING_OWNER
blocker = EXTERNAL_LOCKED_FQV_RUNTIME_ALIGNMENT_REQUIRED
```

只有收到 Owner 对 A／B／C 的明确选择，并由 manager／主控完成相应合法 Binding、授权和真实调用后，D006 才能继续或被有据收束。

若选择 A 或 B 后成功形成合格 runtime，原生恢复点为：

```text
E1 基准保持 A～D 不重跑
→ 新 W1 在获准单一 runtime 中运行原 D
→ E2 消费真实结果
→ 有 HTML 后进入 E3
```

## 9. 当前未完成项

- 原 D 尚未在合格的本次 runtime 中成功启动；
- F 未构造，`fields.json` 未检查；
- 没有候选 HTML；
- E3 未发生；
- E4/W2 未准入、未签发；
- `DATA_READY=false`；
- D006/E 业务未完成。
