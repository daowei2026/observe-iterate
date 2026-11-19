# W001｜运行 CommonPriceTurnGroupCandidatesFrp CAEGraph（C0013 活跃修订）

## 一、动作身份与修订状态

- `run_id / work_order_id / parent_delegation_id`：`OI-U2-F-OBS-20261118-01 / W001 / D005`
- `issuer`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `issuer_call_id`：`C0013`
- `worker`：`codex:OI-U2-F-OBS-20261118-01:worker:W1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- 当前物理配置证据：`daowei2026/observe-iterate@c47a984fb060182d691cc71e983a7bc55e9ce5a2:longrun/runs/OI-U2-F-OBS-20261118-01/worker_bindings/W1.json`

本文件是**同一 W001 的活跃修订**，不是新 W。原 C0012 版本从未物理发送、未执行、未生成 Worker goal，继续由以下精确引用保留历史：

- 原正文：`daowei2026/observe-iterate@cfc1fabc0f910434743cea514ea28f674a35dcd0:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W001/ORDER.md`
- 原 JSON：`daowei2026/observe-iterate@17840c4dbc8493636ce75d07859ceecb31d885e7:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W001/ORDER.json`

本修订只处理两件事：

1. 将机读权限和授权引用对齐 Owner 已确认的新 Binding；
2. 删除“工作区内已经存在本 Run observe-iterate 工作树”的未证实前提，增加确定性的 run-local source staging。

业务目标、D 脚本、C2 展示、B 位置和 E 专业 Workflow 均不变。

## 二、当前权威输入

- Owner 授权补正：`daowei2026/observe-iterate@c47a984fb060182d691cc71e983a7bc55e9ce5a2:longrun/runs/OI-U2-F-OBS-20261118-01/OWNER_AUTHORITY_AMENDMENT_20261119.md`
- 当前 Run Binding：`daowei2026/observe-iterate@4d2eb6058babf47db130a6b7f5ed6e7c9d48cbda:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json`
- 当前 Resource Binding：`daowei2026/observe-iterate@4d2eb6058babf47db130a6b7f5ed6e7c9d48cbda:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_RESOURCE_BINDING.json`
- C0013 E1 基准：`daowei2026/observe-iterate@1a4d2e455a1175f1c20226fa9873c587c697021d:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E1_EXECUTION_AND_REVIEW_BASELINE_C0013.md`
- D 完整脚本：`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`
- D 集成记录：`daowei2026/observe-iterate@e35945aec93d90e4dbb045bc3c35dc5153661aa4:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/CAEGRAPH_DEFINITION_INTEGRATION.md`
- C2 当前唯一预期 HTML：`daowei2026/observe-iterate@56eef30b28c928255329f77798fb46b9adbbc71a:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview.html`
- C3 代码：`daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`
- 正式 D005：`daowei2026/observe-iterate@f274f532e199392fa1f28b009a8e7d45fc6134e7:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.json`

唯一业务对象仍是 `make_features(...)[0]` 返回的 F。Q/V 不进入本 W，Q 依 Owner 最新指令暂不继续。

## 三、精确操作权限

```ini
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**
```

以上逐字来自当前 Run Binding 的 `authority_quote`。本 W001 不使用 `caegraph_data_export`，也不授权 W2 正式取数。

实际写入进一步收敛到：

```text
/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/**
```

除只读使用既有运行环境与产品外，不修改其他仓库、其他 Run、生产数据或外部 symlink 目标。

## 四、已知现场事实

主控有限预检查确认：工作区根无 `.git`，根及直接非 symlink 子目录未找到 `observe-iterate` 候选或本 Run D 脚本相对路径。该检查不是递归穷尽搜索，不能声称整个工作区没有依赖、实例或更深层源码。

因此，本工单不要求 Worker 先无界搜索，也不再假定现成工作树存在。采用下述确定性的 run-local source staging。

## 五、run-local source staging

设置：

```bash
BASE=/dwdhome/fy/BASE_E6_2_copy
RUN_ROOT="$BASE/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001"
SOURCE_ROOT="$RUN_ROOT/source/observe-iterate"
OUTPUT_ROOT="$RUN_ROOT/output/u2_f_caegraph"
LOG_ROOT="$RUN_ROOT/logs"
D_COMMIT=f4f0e4b276b1118b779473c1fbe462bc7a64b358
```

### 5.1 幂等与冲突检查

- `RUN_ROOT` 不存在：创建后继续。
- `RUN_ROOT` 已存在，且有可核对的 `source_stage_report.json`：核对 `run_id/W001/D_COMMIT/SOURCE_ROOT` 后再继续。
- `RUN_ROOT` 已存在但来源未知、内容不匹配或动作效果不明：立即返回 `EFFECT_UNKNOWN`，不得覆盖、清理或另建同一 W 的第二套结果。

### 5.2 源码布置

在 `SOURCE_ROOT` 建立本 Run 专用 detached checkout。优先使用工作区已配置的 Git 凭据：

```bash
mkdir -p "$RUN_ROOT/source" "$OUTPUT_ROOT" "$LOG_ROOT"

git init "$SOURCE_ROOT"
git -C "$SOURCE_ROOT" remote add origin https://github.com/daowei2026/observe-iterate.git
git -C "$SOURCE_ROOT" -c protocol.version=2 fetch --filter=blob:none --no-tags \
  origin refs/heads/runs/OI-U2-F-OBS-20261118-01:refs/remotes/origin/run
git -C "$SOURCE_ROOT" checkout --detach "$D_COMMIT"
```

若目标目录已由本 W 正确建立，按上面的幂等规则复用，不重复 `remote add` 或 fetch。Git 获取失败、凭据不可用或目标提交不可达时，保存日志并返回首个真实阻断；不得从未知本地文件拼接替代源码。

### 5.3 运行前验证

```bash
test "$(git -C "$SOURCE_ROOT" rev-parse HEAD)" = "$D_COMMIT"
test -f "$SOURCE_ROOT/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py"
test -f "$SOURCE_ROOT/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py"
```

写出：

```text
$RUN_ROOT/source_stage_report.json
```

至少包含：`run_id`、`work_order_id`、remote、requested_commit、actual_head、source_root、D path、C3 path、created_or_reused。

## 六、真实运行

从 `SOURCE_ROOT` 执行：

```bash
cd "$SOURCE_ROOT"
python \
  longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py \
  --output-dir "$OUTPUT_ROOT" \
  > "$LOG_ROOT/w1_run.log" \
  2>&1
RUN_EXIT=$?
printf '%s\n' "$RUN_EXIT" > "$LOG_ROOT/w1_run.exit_code"
```

若工作区正式 Python 入口不是命令名 `python`，可使用已经配置的等价入口，但不得新建环境、升级依赖或切换项目版本，并须记录实际命令。

目标是尽快得到：

1. `$OUTPUT_ROOT/u2_f_caegraph.html`；或
2. 首个真实阻断错误。

若精确 F 实例不存在既存 `fields.json`，必须停止；不得调用 `f.rerun()`，不得执行 Owner 明确排除的全历史 producer。

## 七、可以直接修

仅限不改变业务含义的确定性机械问题：

- source staging、Python 语法、import、模块或文件路径；
- 锁定版本中已核实的 API 名称／参数差异；
- 明确类型转换；
- 输出目录、文件名、日志和静态 HTML 接线；
- 本次真实运行所必需、且不存在业务选择空间的入口接线。

如修改 D/C3，只能修改 `SOURCE_ROOT` 中的 detached 工作树；保存：

```text
$RUN_ROOT/repair.diff
$RUN_ROOT/final_git_status.txt
```

不得推送，不得无痕改写 GitHub 记录。

## 八、必须停止并回 E

- 需要改变 SOF、品种、日历、5m 源尺度、2021—2022 位置或 `groupKnownFrom`；
- 需要删除、增加、替换业务字段、读取 Q/V 或另算近似值；
- 需要改变 C2 主附图、图元、时间表达、标准化、交互或阅读语义；
- 正确修法不唯一，或无法判断语义影响；
- 需要在授权工作区之外写入；
- 发现未知同一 W 结果、工作区冲突、非单写者或动作效果未知。

这些情况不得由 Worker 猜测，返回原 executor:E1 分类。

## 九、W1 与正式取数边界

D 脚本可能顺带产生 `prepared_tables/`、`plot_data/` 和 `definition_run_report.json`。它们在 W1 中只是运行诊断副产物：

- 不构成 E4 正式取数准入；
- 不作为 W2 正式数据；
- 不得标记 `DATA_READY`；
- 不得修改脚本来扩大导出范围。

## 十、最小交付与 Worker Return

必须返回：

```text
状态：SUCCESS / PARTIAL / BLOCKED / EFFECT_UNKNOWN
source staging：<source_stage_report.json>
最终脚本：<SOURCE_ROOT path + HEAD>
候选 HTML：<path；未生成写无>
运行日志：<path>
退出码：<integer/unknown>
实际修改：<repair.diff；无修改写无>
当前阻断：<首个真实阻断；无写无>
definition_run_report：<path；没有写无>
```

正式 Return 使用 `longrun-worker-return/v2`：

- `order_ref` 指向本次 C0013 修订后的活跃 `ORDER.json` 精确 commit；
- `sender=codex:OI-U2-F-OBS-20261118-01:worker:W1`；
- `return_to=chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`。

Worker 只交付事实和实物，不判断最终图是否接受。

## 十一、派发前主控核验

主控在物理发送前必须独立确认：

1. 本文件与活跃 `ORDER.json` 同属 `W001`；
2. grant 与 `RUN_BINDING@4d2eb...` 精确一致；
3. 物理 Worker 仍为 `gpt-6.1-sol / max`，cwd 仍为 `/dwdhome/fy/BASE_E6_2_copy`；
4. W001 动作账本仍为 `NOT_SENT`，没有旧消息、Worker goal 或未知现场产物；
5. 工作区当前仍满足单写者；
6. 实际发送后再登记 `IN_FLIGHT` 并保存真实回执。

## 十二、续接点

W001 正式 Worker Return 回到原 executor:E1 后，继续同一：

```text
D005 / WI-E / M-E
```

进入 E2 分类、E3 核图；只有图接受后才进入 E4/W2。发布工单、完成绑定或完成物理发送都不等于 E 专业完成。
