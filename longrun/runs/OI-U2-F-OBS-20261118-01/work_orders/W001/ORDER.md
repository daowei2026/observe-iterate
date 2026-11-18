# W001｜运行 CommonPriceTurnGroupCandidatesFrp CAEGraph

## 一、通用 Worker 工单身份

- `run_id / work_order_id / parent_delegation_id`：`OI-U2-F-OBS-20261118-01 / W001 / D005`
- `issuer`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- `issuer_call_id`：`C0012`
- `worker`：`codex:OI-U2-F-OBS-20261118-01:worker:W1`
- `return_to`：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`
- 预期 Worker 配置：Owner 指定的 `GPT-6.1 Sol Max`；实际派发前由主控核对物理线程、模型、强度和 cwd。

## 二、本次实际操作

在已核实的真实工作区 `/dwdhome/fy/BASE_E6_2_copy` 内，找到本 Run 的 `daowei2026/observe-iterate` 工作树，运行 D004 已发布的完整 CAEGraph 定义：

`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`

目标是尽快取得：

1. 可打开的候选 CAEGraph HTML；或
2. 首个真实阻断错误。

本工单属于原 D005 的 E1→W1 操作，因为 E Skill 明确要求先由 Worker 在真实环境运行 D 定义，再由原 executor:E1 消费结果、分类、核图和决定是否允许 W2。Worker 不代替 E 的专业判断。

## 三、输入与精确位置

- E1 执行与核图基准：`daowei2026/observe-iterate@942bb61c2453a44cc258da8c2832d89687c52aa0:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/E1_EXECUTION_AND_REVIEW_BASELINE.md`
- D 完整脚本：`daowei2026/observe-iterate@f4f0e4b276b1118b779473c1fbe462bc7a64b358:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`
- D 集成记录：`daowei2026/observe-iterate@e35945aec93d90e4dbb045bc3c35dc5153661aa4:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/CAEGRAPH_DEFINITION_INTEGRATION.md`
- C2 当前唯一预期 HTML：`daowei2026/observe-iterate@56eef30b28c928255329f77798fb46b9adbbc71a:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display_preview.html`
- C3 代码：`daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`
- 正式 D005：`daowei2026/observe-iterate@f274f532e199392fa1f28b009a8e7d45fc6134e7:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.json`
- 工作区实路径：`/dwdhome/fy/BASE_E6_2_copy`
- 运行工作树：该工作区内同时包含 `.git` 和下列文件的 `observe-iterate` 工作树根目录：

```text
longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py
```

不得新建 clone，不得改用 `/dwdhome/fy/BASE_E6_2` 或其他 Run 的工作树。

## 四、运行命令

从上述 `observe-iterate` 工作树根目录执行：

```bash
mkdir -p longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/runtime/w1_candidate/u2_f_caegraph

python longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py \
  --output-dir longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/runtime/w1_candidate/u2_f_caegraph \
  > longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/E/runtime/w1_candidate/w1_run.log \
  2>&1
```

记录实际退出码。若工作区正式 Python 入口不是命令名 `python`，可使用已经配置的等价入口，但不得新建环境、升级依赖或切换项目版本；须在日志中记录实际命令。

## 五、精确操作权限

```text
operation=caegraph_run_and_repair
execution_context=/dwdhome/fy/BASE_E6_2_copy
allowed_writes=/dwdhome/fy/BASE_E6_2_copy/**
```

实际写入进一步限于该工作区内本 Run 的：

```text
longrun/runs/OI-U2-F-OBS-20261118-01/**
```

除读取既有环境／产品外，不修改其他仓库源码、其他 Run、外部 symlink 目标或生产数据。

授权依据原文：

```text
operation=caegraph_run_and_repair
execution_context=/BASE_E6_2_copy
allowed_writes=/BASE_E6_2_copy/**
```

以及 Owner 路径更正原文：

```text
将本 Run 路径更正为 /dwdhome/fy/BASE_E6_2_copy
```

主控在物理派发前必须独立核验：修正后的有效 scope、真实 Worker thread、模型／强度、cwd、工作区单写者和当前没有同一 W001 在途。

## 六、可以直接修

仅限不改变业务含义的确定性机械问题：

- Python 语法、import、模块或文件路径；
- 锁定版本中已经核实的 API 名称／参数差异；
- 明确的类型转换；
- 输出目录、文件名、日志和静态 HTML 接线；
- 本次真实运行所必需、且没有业务选择空间的机械入口接线。

有修改时保存并回报 `git diff`；无修改时写“无”。不得把机械修复扩展成重写展示或重算业务字段。

## 七、必须停止并回 E

- 精确 F 实例没有既存 `fields.json`；不得调用 `f.rerun()`，不得启动输入排除的全历史 producer；
- 需要改变 SOF、品种、日历、5m 源尺度、2021～2022 位置或 `groupKnownFrom`；
- 需要增删替换业务字段、用近似数据代替 F 输出，或读取 Q/V；
- 需要改变 C2 主图／附图、图元、时间表达、标准化、交互或阅读语义；
- 正确修法不唯一，或无法判断语义影响；
- 工作区／分支冲突、未授权写入风险、已有同一动作在途或动作效果未知。

出现这些情况时，不继续猜测，回报首个真实阻断。

## 八、W1 与正式取数的边界

D 脚本可能在候选目录顺带产生 `prepared_tables/`、`plot_data/` 和 `definition_run_report.json`。这些在 W1 中只属于运行诊断副产物：

- 不构成 E4 正式取数准入；
- 不作为 W2 正式数据交付；
- 不得标记 `DATA_READY`。

本工单不授权正式取数，也不授权修改脚本来扩大导出。只有 executor:E1 接受最终图并另行签发 W2，才可形成正式数据。

## 九、预期交付物

1. W1 最小事实报告；
2. 最终实际运行脚本的 path／commit；
3. 候选 HTML path，未生成则明确“无”；
4. 完整运行日志及退出码；
5. 实际 `git diff` 引用，未修改则明确“无”；
6. `definition_run_report.json` path，未生成则明确“无”；
7. 当前首个阻断，若没有则明确“无”。

最小回报格式：

```text
状态：SUCCESS / PARTIAL / BLOCKED / EFFECT_UNKNOWN
最终脚本：<path 或 commit>
候选 HTML：<path；未生成则写无>
运行日志：<path>
实际修改：<git diff 引用；无修改写无>
当前阻断：<首个真实阻断；无则写无>
definition_run_report：<path；没有则写无>
```

正式 Worker Return 使用 `longrun-worker-return/v2`，`order_ref` 指向本 W001 `ORDER.json`，`return_to` 必须是本工单 issuer executor:E1。

## 十、失败、部分交付、重复和冲突

- 失败或部分结果：保留已有日志、report、HTML 和 diff，按真实状态返回，不清理证据后重做；
- 无候选 occurrence／空表：按真实结果返回，不解释成失败或业务反证；
- 输出目录已有未知来源结果：标记 `EFFECT_UNKNOWN`，先对账，不覆盖、不盲目重跑；
- 工作区冲突或非单写者：停止并回报；
- 首次运行已产生明确阻断：优先立即回报，不先写长说明。

## 十一、幂等与当前动作身份

- 当前唯一动作身份：`OI-U2-F-OBS-20261118-01/W001`；
- 本 `ORDER.md` 和同目录 `ORDER.json` 只是正式工单，不等于已经物理发送或执行；
- 主控须按 V2 登记 `NOT_SENT → IN_FLIGHT` 后实际发送；
- 若物理回执或现场结果不明，先核 W001 原消息、工作区和远端产物，不另发相同动作；
- 只有确认原动作未执行或已显式结束，且 executor:E1 仍判断基准不变时，才能签发具名 revision／后继工单。

## 十二、Owner 与 D 对应引用

- Owner GO／路径更正：`daowei2026/observe-iterate@74ed0b11552f73b03e55e3e324f8325889730b52:longrun/runs/OI-U2-F-OBS-20261118-01/OWNER_START.md`
- Run Binding：`daowei2026/observe-iterate@b6fcc3dd824b6e28fffd5b8d464989289dd4d97d:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_BINDING.json`
- Resource Binding：`daowei2026/observe-iterate@b6fcc3dd824b6e28fffd5b8d464989289dd4d97d:longrun/runs/OI-U2-F-OBS-20261118-01/RUN_RESOURCE_BINDING.json`
- D005 JSON：`daowei2026/observe-iterate@f274f532e199392fa1f28b009a8e7d45fc6134e7:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D005/DELEGATION.json`
- E Skill：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/SKILL.md`
- W1 短执行卡：`daowei2026/observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288:skills/observation-material-preparation/caegraph-execution/RUN_REPAIR_ORDER_TEMPLATE.md`
