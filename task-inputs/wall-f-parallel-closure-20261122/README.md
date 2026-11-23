# WALL / F 并行统计闭环｜任务输入

> **状态：基础 Run 已启动；当前 F Run 需按新的高置信发现要求接续。** 初始启动材料继续保留；在途 F 的真实状态以 `codex/oi-f800-stat-20261122-01` 分支及 `F_CURRENT_RUN_CONTINUATION.md` 为准。不得用本目录早期准备状态覆盖真实 Run 记录。

## 1. 目标

```text
WALL 最终修正版
→ rb/m、2021 全年正式实例
→ 重新统计
→ 复验 D1/D2/D4、量化 D3
→ 继续找明显不合理点
→ 当前深度闭环

F observation_multiple=800
→ rb/hc/i、5m、2021—2023 正式实例
→ 重新统计全部转化和期限影响
→ 完成覆盖面与高置信度并重的 finding discovery pass
→ 逐个定位责任逻辑并处理
→ 当前深度闭环
```

两条基础线都形成可释放版本后，再启动各自下游。

## 2. 当前 F 接续入口

当前在途 F Run：

```text
OI-F800-STAT-20261122-01
```

继续该 Run 时首先阅读：

[F_CURRENT_RUN_CONTINUATION.md](F_CURRENT_RUN_CONTINUATION.md)

该文件明确：

- 当前不接受尚未采用的 F Release 候选；
- 复用已经有效的正式 X/G，不机械重跑；
- 补做高置信不合理现象发现 pass；
- 把“峰值责任内 Life 36”登记为 Owner 提出的高优先级候选；
- 在 Release 前完成其口径核对、责任逻辑定位和结论；
- controller、manager、executor 三类会话采用同一个修正后 `observe-iterate` 精确 commit。

## 3. 初始启动来源

[启动就绪检查与来源地图](START_READINESS_AND_SOURCE_MAP.md) 是初始启动时的主控入口。它说明：

- 哪些内容已经锁定；
- 每个问题去哪里找原件；
- 物理预检；
- 初始运行顺序。

其中关于“尚未启动”或旧 V 工作区占用的陈述属于启动前历史，不得覆盖当前已注册 Run 的真实状态。

## 4. 文件

| 文件 | 用途 |
|---|---|
| [F_CURRENT_RUN_CONTINUATION.md](F_CURRENT_RUN_CONTINUATION.md) | 当前 F800 Run 的高置信发现补扫、Life 36 候选和三类会话版本接续 |
| [START_READINESS_AND_SOURCE_MAP.md](START_READINESS_AND_SOURCE_MAP.md) | 初始启动判断、来源地图、物理预检和运行顺序 |
| [OWNER_PROMPT_EXTRACT.md](OWNER_PROMPT_EXTRACT.md) | Owner 历史 prompt、纠偏和优先级的完整提炼 |
| [OWNER_INPUT_UPDATE_20261122.md](OWNER_INPUT_UPDATE_20261122.md) | F 分支、800 实例和初始启动检查要求 |
| [OWNER_INTENT_AND_RUN_PLAN.md](OWNER_INTENT_AND_RUN_PLAN.md) | 两线并行、当前深度和停止条件 |
| [WALL_BASE_RUN_INPUT.md](WALL_BASE_RUN_INPUT.md) | WALL 精确版本、默认实例、范围、来源和统计问题 |
| [F_BASE_RUN_INPUT.md](F_BASE_RUN_INPUT.md) | F 初始版本、800 构造、范围、来源和统计问题 |
| [KNOWN_FINDINGS.md](KNOWN_FINDINGS.md) | 当前已知和 Owner 提出的 finding 状态 |
| [DOWNSTREAM_DEPENDENCIES.md](DOWNSTREAM_DEPENDENCIES.md) | 联合 Barrier、WALL 下游和 F→Q→V |
| [VERSION_WORKSPACE_LOCKS.md](VERSION_WORKSPACE_LOCKS.md) | 初始版本、工作区、线程和授权锁；在途版本演化以 Run Binding 为准 |

## 5. 初始锁定版本与在途版本

### WALL 初始正式输入

```text
daowei2026/tis@6618d4d147d6ebbe634e61facddf2c9a0b996982
WallAssembler default params
rb / m
2021-01-01..2021-12-31
/dwdhome/fy/BASE_E6_2
```

### F 初始正式输入

```text
daowei2026/frp@ac1927518ad6105f15ffbe37fea45e4be91ba574
daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767
profile.observation_multiple = 800
rb / hc / i
5m
2021-01-01..2023-12-31
/dwdhome/fy/BASE_E6_2_copy
```

当前 F Run 在后续已确认修改中演化到新的 FRP commit；不得用初始 `ac192...` 覆盖当前 Run 的 `RUN_BINDING`。具体采用 `F_CURRENT_RUN_CONTINUATION.md` 和当前 Run 分支。

旧 F `make_features(...)` 入口本身不带 `observation_multiple` 形参；准确构造和回读要求继续有效，不得原样执行旧脚本而静默使用默认 6。

## 6. 运行 profile

两条基础 Run 均采用：

```yaml
execution_profile: CODEX_NATIVE_DIRECT
controller_skill: daowei2026/cgpterm@fc966bcf5441701182339c992865504692f3a466:.agents/skills/observe-iterate-longrun-v2-codex-native-controller/SKILL.md
manager: one bound Codex thread per run
executor: one or more bound Codex threads per run
workers: []
```

manager 与 executor 是不同线程。当前接续不要求重建线程，但 controller、manager、executor 必须显式采用同一个新的专业控制 commit。

## 7. 专业来源

采用：

- `control-v0.3/`；
- `skills/feature-understanding/` 及业务对象判别补充；
- `feature-global-behavior-profiling`；
- `business-discrepancy-diagnosis`；
- 必要时 `feature-instance-calibration`；
- `STATISTICS_DRIVEN_PRACTICE.md`。

历史 Chat 是 Owner 思考过程、纠偏和 finding 来源，不替代当前代码、参数和正式运行结果。

## 8. 当前发现要求

发现阶段要求：

```text
覆盖面与高置信度并重
```

参考类别不是硬清单、固定阈值或自动判错规则。executor 根据当前 Feature 的业务对象、生命周期、输出合同、数量关系和全量结果自行判断高置信候选。

不得：

- 在发现第一个问题后停止其余适用业务面的检查；
- 为了“找全”把所有边角现象升级；
- 仅凭输出数量直接判错；
- 忽略 Owner 明确要求评估的候选。

## 9. 修改边界

Codex 可以自主运行、统计、分析、写诊断脚本、准备候选 patch 和新旧对照；具体任务若要求正式改变前确认，则按该任务输入执行。无论是否需另行确认，正式行为改变后都必须重跑并重统计。
