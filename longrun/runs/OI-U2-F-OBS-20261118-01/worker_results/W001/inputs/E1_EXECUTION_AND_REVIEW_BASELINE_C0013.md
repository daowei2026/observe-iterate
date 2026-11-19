# E1｜执行与核图基准（C0013 修订）

## 1. 身份与适用范围

- `run_id`：`OI-U2-F-OBS-20261118-01`
- `work_item_id`：`OI-U2-F-OBS-20261118-01-WI-E`
- `stage_instance_id`：`OI-U2-F-OBS-20261118-01-M-E`
- `delegation_id`：`D005`
- `call_id`：`C0013`
- `work_order_id`：`W001`（沿用原唯一动作身份，不新建 W）
- `executor`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `worker`：`codex:OI-U2-F-OBS-20261118-01:worker:W1`
- `definition_id`：`OI-U2-F-OBS-20261118-01-D-CAEGRAPH-V1`

本文件替代 C0012 基准作为尚未发送的 W001 当前执行基准；C0012 基准与原 W001 仍按精确 commit 保留为历史。它只修正授权引用、物理 Worker 绑定和运行入口布局，不改变 D 定义、C2 展示预期、B 位置、F 实例或 E Workflow。

## 2. 当前权威授权和物理资源

### 2.1 Owner 授权补正

- `daowei2026/observe-iterate@c47a984fb060182d691cc71e983a7bc55e9ce5a2:longrun/runs/OI-U2-F-OBS-20261118-01/OWNER_AUTHORITY_AMENDMENT_20261119.md`

采用的逐字机读授权：

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**
```

本 W001 不使用 `caegraph_data_export`；后者只为图接受后的 W2 保留。

### 2.2 当前 Binding

- `daowei2026/observe-iterate@4d2eb6058babf47db130a6b7f5ed6e7c9d48cbda:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json`
- `daowei2026/observe-iterate@4d2eb6058babf47db130a6b7f5ed6e7c9d48cbda:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_RESOURCE_BINDING.json`

### 2.3 物理 Worker 绑定

- `daowei2026/observe-iterate@c47a984fb060182d691cc71e983a7bc55e9ce5a2:longrun/runs/OI-U2-F-OBS-20261118-01/worker_bindings/W1.json`

已核事实：

```text
model=gpt-6.1-sol
reasoning_effort=max
cwd=/dwdhome/fy/BASE_E6_2_copy
worker thread idle=true
business order dispatched=false
```

W001 尚未发送或执行。派发前主控仍需重核当时线程状态、cwd、模型／强度、单写者和动作账本。

## 3. 唯一专业运行输入与核图依据

- D 完整脚本：`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`
- D 集成记录：`daowei2026/observe-iterate@e35945aec93d90e4dbb045bc3c35dc5153661aa4:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/CAEGRAPH_DEFINITION_INTEGRATION.md`
- C2 当前唯一预期 HTML：`daowei2026/observe-iterate@56eef30b28c928255329f77798fb46b9adbbc71a:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview.html`
- C3 代码：`daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`
- B 位置：`OI-U2-F-OBS-20261118-01-B-POS-001`

唯一业务目标仍是 `make_features(...)[0]` 返回的 `f`。Q/V 不进入本 W，Q 依 Owner 最新指令暂不推进。

## 4. 现场布局事实与专业处理

主控有限预检查只确认：

1. `/dwdhome/fy/BASE_E6_2_copy` 根目录没有 `.git`；
2. 根及直接非 symlink 子目录中未找到名为 `observe-iterate` 的候选工作树；
3. 同一有限层次未找到本 Run D 脚本相对路径；
4. 该检查不是递归穷尽搜索，不能推出整个工作区不存在运行依赖、实例数据或更深层源码。

因此，W001 不再把“工作区内已经存在本 Run observe-iterate 工作树”作为前置事实，也不要求 Worker 先对整个工作区作无界搜索。

### 4.1 采用的机械入口

在授权工作区内建立本 Run 专用、固定提交的 detached source staging：

```text
BASE=/dwdhome/fy/BASE_E6_2_copy
RUN_ROOT=$BASE/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001
SOURCE_ROOT=$RUN_ROOT/source/observe-iterate
OUTPUT_ROOT=$RUN_ROOT/output/u2_f_caegraph
LOG_ROOT=$RUN_ROOT/logs
```

`SOURCE_ROOT` 只用于执行本 W，不是新的业务仓库，不改变 Owner 指定的运行环境。其 HEAD 必须精确固定为：

```text
f4f0e4b276b1118b779473c1fbe462bc7a64b358
```

该提交已经包含 D 脚本及其相对依赖 C3。运行前必须验证：

```text
git -C $SOURCE_ROOT rev-parse HEAD
= f4f0e4b276b1118b779473c1fbe462bc7a64b358

$SOURCE_ROOT/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py 存在
$SOURCE_ROOT/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py 存在
```

### 4.2 staging 规则

- 若 `RUN_ROOT` 不存在：创建它，并用配置好的 Git 凭据对 `daowei2026/observe-iterate` 的本 Run 分支作最小 fetch，detached checkout 到上述 D 提交。
- 若 `RUN_ROOT` 已存在且带有本 W 可核对的 `source_stage_report.json`：先核对 run_id、W001、source commit 和路径，再决定是否继续。
- 若 `RUN_ROOT` 已存在但来源未知、内容不匹配或动作效果不明：返回 `EFFECT_UNKNOWN`，不得覆盖或另建同一 W 的第二套结果。
- 不搜索或修改其他 Run；不跟随外部 symlink；不修改工作区中既有生产仓库或数据。
- Git 获取失败、无凭据或目标提交不可达时，返回第一个真实阻断，不从未知本地文件拼装来源。

`source_stage_report.json` 至少保存：

```text
run_id
work_order_id
source_root
remote_url
requested_commit
actual_head
D_script_path
C3_path
created_or_reused
```

## 5. 运行命令

source staging 通过后，从 `SOURCE_ROOT` 执行：

```bash
mkdir -p "$OUTPUT_ROOT" "$LOG_ROOT"

python \
  longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py \
  --output-dir "$OUTPUT_ROOT" \
  > "$LOG_ROOT/w1_run.log" \
  2>&1
```

记录实际 Python 入口和退出码。若环境正式入口不是命令名 `python`，可使用工作区已经配置的等价入口；不得新建环境、升级依赖或切换项目版本。

候选 HTML 预期路径：

```text
$OUTPUT_ROOT/u2_f_caegraph.html
```

运行报告预期路径：

```text
$OUTPUT_ROOT/definition_run_report.json
```

## 6. W1 可直接修的范围

只允许不改变业务含义的确定性机械问题：

- source staging、Python import、模块或文件路径；
- 锁定版本中已核实的 API 名称／参数差异；
- 明确类型转换；
- 输出目录、文件名、日志和静态 HTML 接线；
- 为本次运行所必需且不存在业务选择空间的入口修复。

修改 D/C3 时必须留在 `SOURCE_ROOT`，保存 `git diff --binary` 和最终 HEAD／工作树状态。不得推送或无痕改写本 Run GitHub 记录。

## 7. 必须停止并回 E

- 精确 F 实例没有既存 `fields.json`；不得调用 `f.rerun()`，不得执行被排除的全历史 producer；
- 需要改变 SOF、品种、日历、5m 源尺度、2021—2022 位置或 `groupKnownFrom`；
- 需要增删替换业务字段、使用 Q/V 或另算近似值；
- 需要改变 C2 主图／附图、图元、时间表达、标准化、交互或阅读语义；
- 正确修法不唯一或语义影响不明确；
- 需要在授权工作区之外写入；
- 发现未知同一 W 结果、工作区冲突或非单写者。

## 8. W1 回报与 E2/E3 核对

Worker 最小回报：

```text
状态：SUCCESS / PARTIAL / BLOCKED / EFFECT_UNKNOWN
source staging：<source_stage_report.json>
最终脚本：<SOURCE_ROOT path + git diff/HEAD>
候选 HTML：<path；未生成写无>
运行日志：<path>
退出码：<integer/unknown>
实际修改：<diff path；无修改写无>
当前阻断：<首个真实阻断；无写无>
definition_run_report：<path；没有写无>
```

E 收到正式 Worker Return 后至少核对：

1. source staging 是否精确固定 D 提交；
2. 是否生成可打开 HTML，或首个阻断是否真实；
3. 最终脚本仍只读取 `f`，未调用 producer；
4. SOF、日历、品种、B 时间和 `groupKnownFrom` 是否保持；
5. diff 是否仅含机械修复；
6. 图是否保持 C2 的三类面板与三种成员位置；
7. 已知接口缺口是否未被伪造解决。

E 的候选结论只能是：接受、限域接受、返回 B、返回 C、返回 D 或阻塞。Worker 不作专业接受判断。

## 9. W1 与正式取数边界

D 脚本在 W1 中顺带产生的 `prepared_tables/`、`plot_data/` 和运行报告只属于诊断副产物：

- 不构成 E4 正式取数准入；
- 不属于 W2 正式数据；
- 不得标记 `DATA_READY`。

只有 E3 接受最终图后，E4 才能形成最小正式取数清单并另行签发 W2。

## 10. 当前动作事实

- 原 W001 在 C0012 仅发布，未物理发送、未执行、未生成 Worker goal；
- C0013 保持同一 `work_order_id=W001`，不创建新 W；
- 当前修订只替换尚未发送的 W001 活跃工单内容；原 C0012 ORDER refs 继续作为历史；
- 下一合法动作是主控以 C0013 活跃 W001 做权限／资源复核并物理发送；
- E 仍 `IN_PROGRESS`，续接点是该 W001 的正式 Worker Return 回原 executor:E1。
