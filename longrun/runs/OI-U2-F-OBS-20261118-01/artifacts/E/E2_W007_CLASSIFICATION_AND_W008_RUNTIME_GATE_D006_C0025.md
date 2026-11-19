# E2｜消费 W007，分类默认环境失配并建立 W008 最后有界 runtime 准入门

## 1. 身份与已消费 Return

- `run_id`: `OI-U2-F-OBS-20261118-01`
- `delegation_id`: `D006`
- `work_item_id`: `OI-U2-F-OBS-20261118-01-WI-E-R1`
- `stage_instance_id`: `OI-U2-F-OBS-20261118-01-M-E-R1`
- `executor`: `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`
- `call_id`: `C0025`
- 已消费 Worker Return：`daowei2026/observe-iterate@4566786786e8e754700c9cf2cafbbf66b44f030b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W007/WORKER_RETURN.json`

W007 的身份、原 `W007` order ref、worker、route 和 manifest 均已由主控验证并合法回交。本 E2 接受其事实与必要实物；`outcome=STOP` 只终止 W007，不等于 D006/E 或整个 F Run 完成。

## 2. W007 已经证明的事实

### 2.1 当前默认 FY 入口不可准入

仅加载当前工作区 `m3rc` 后：

- Python：`/m3c3/Linux/apps/anaconda3/bin/python`，3.10.13；
- `mquant`、`mquant.frame`、`mquant.tis`、`mquant.tis.frp` 均来自当前工作区；
- `mquant.tis.frp.fqv_kline_example` 与 F/Q/V 三个 wrapper 的 `find_spec` 均不存在；
- 活跃 TIS root 为 `/dwdhome/fy/BASE_E6_2_copy/mquant/tis`；
- 活跃 TIS HEAD=`10010b89f8fc79a91affd26f985b6d9bf2d33c6c`，不是锁定 `2f460d663d821cf2ba25555eda13e78b697d0767`；
- 四个本次所需文件均不存在且未 tracked；没有证据表明是本地脏修改，准确含义是当前活跃 TIS 对本次 FQV 不完整；
- 固定 Haskell FRP root 为 `/dwdhome/fy/BASE_E6_2_copy/edh-universe/frp/frp`；
- 当前 FRP HEAD=`37c790c0f456fe3022bb00609219d3e92a5c2f9b`，不是锁定 `67711c492da909ed0f044f357beb278abf7fc71c`，且目标 F 文件与锁定版本有差异。

因此当前默认 `m3rc` 入口不能代表 D006 锁定的 FQV 组合。

### 2.2 W007 没有产生新的业务运行事实

- D 实际启动：0 次；
- F 构造：未发生；
- `fields.json`：未检查；
- 候选 HTML：无；
- `definition_run_report`：无；
- E3：未开始；
- E4/W2：未准入；
- `DATA_READY=false`。

不能据此推断 F 产品不存在，也不能推断 B、C、D 已有业务定义有误。

### 2.3 唯一新增候选事实

W007 在当前工作区进行一次有界精确文件名查找，排除了 `observe-iterate-runs/**`、`.git/**`、`__pycache__/**` 和其他工作区，仅命中：

```text
/dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117/runtime/mquant/tis/frp/fqv_kline_example.py
```

该命中：

- 位于本 Run 固定工作区之内；
- 不属于旧 W staging；
- 具有可见包边界结构；
- 尚未证明是完整、单一、正常、锁定版本一致的 FQV runtime；
- 尚未被导入、执行、复制、软链或接入。

所以它既不能被直接采用，也不能在未核对前被忽略。

## 3. 与 Owner 输入和成功现场的关系

Owner 要求：

1. 优先在真实现有环境运行 D；
2. 可以参考历史成功 FQV 现场定位正常运行方式；
3. 旧结果不得冒充本次正式交付；
4. 不重建／补装平台，不构造 TIS overlay，不混合 package，不切换仓库版本；
5. 当前运行环境与锁定版本不匹配时，由 E 根据真实证据决定问题性质与后继。

2026-11-16 正常包装说明已经证明：正常目标方式是通过平台 Python 包装 `mquant.tis.frp.fqv_kline_example.make_features` 构造 F/Q/V，并在正常平台构建后运行；不是专用 Source runner，也不是手工分层 overlay。

因此，对当前工作区内这个唯一 `.runtime` 候选做一次**只读来源核对，并且仅在它本身已经是完整正常 runtime 时实际运行原 D**，符合 Owner 边界。反之，复制文件、修改 `__path__`、拼接活跃 TIS、重新构建或切版本均不符合。

## 4. E2 专业分类

```text
DEFAULT_FY_RUNTIME_LOCKED_FQV_MISMATCH
+
SINGLE_IN_WORKSPACE_DEDICATED_RUNTIME_CANDIDATE_UNRESOLVED
```

| Workflow 分流 | 判断 |
|---|---|
| 返回 B | 否；尚未触达观察位置或真实 F 表 |
| 返回 C | 否；没有图，展示合同未被证伪 |
| 返回 D | 否；D 使用锁定正常 import，实例、字段、位置和 C3 未被反证 |
| 进入 E3 | 否；没有 HTML |
| 进入 E4/W2 | 否；图未接受 |
| 基准不变时续发 W1 | **是，仅限一次针对精确 `.runtime` 候选的来源准入与条件运行** |

## 5. W008 的专业边界

W008 是本次环境问题的**最后一次有界 W1 revision**，只回答：

> `/dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117` 是否已经是一个无需安装、构建、切版本、复制、软链、overlay 或 package 混合即可使用的单一正常 FQV runtime？

### 5.1 允许做

- 只读检查该固定候选目录内已有的 manifest、provenance、launcher、activation、Python 和 package 文件；
- 对候选 TIS 的本次相关 tracked 源文件与本地已有锁定 commit 做字节级／hash 对照；
- 核对候选运行时所有 `mquant.tis` 相关模块来自同一个 TIS runtime root；
- 核对候选已有 provenance 是否明确绑定锁定 FRP commit；
- 只有上述准入全部成立，才使用候选**已有正常入口**运行原 D 一次。

### 5.2 不允许做

- 不再搜索第二个 runtime；
- 不修改 `sys.path` 或任何 package `__path__` 来拼接来源；
- 不把候选 TIS 与活跃 `/dwdhome/fy/BASE_E6_2_copy/mquant/tis` 分层组合；
- 不复制、软链或生成 FQV 文件；
- 不运行 `seed_inits.py`、`pretty-exports.py`；
- 不 `git checkout/switch/reset/restore/fetch/pull`；
- 不 `pip/conda/stack/cabal` 安装或构建；
- 不修改 TIS、FRP、m3、uplot、平台包或 D/C3；
- 不调用 F producer，不读取 Q/V 产品，不启动 W2。

### 5.3 失败后的确定后继

若候选缺少既有正常入口、不是单一完整 TIS runtime、相关源码与锁定 TIS 不一致、FRP 锁定 provenance 不成立，或需要任何环境建设动作，则 W008 立即 STOP。

此时 E 不再继续签发环境探测型 W1，专业分类收敛为：

```text
EXTERNAL_LOCKED_FQV_RUNTIME_ALIGNMENT_REQUIRED
```

后继将是向原 manager／Owner 明确提出运行前置，而不是由主控或 Worker自行设计修复。

## 6. 当前续接点

```text
D006 / WI-E-R1 / M-E-R1
E state = IN_PROGRESS
accepted worker = W007
next native action = W008 final bounded W1 runtime gate
E3 = not started
E4/W2 = not admitted
DATA_READY = false
```
