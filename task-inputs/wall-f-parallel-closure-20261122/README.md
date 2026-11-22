# WALL / F 并行统计闭环｜任务输入

> **状态：`PREPARED_RUNTIME_PREFLIGHT_REQUIRED`。** 业务目标、Owner prompt、WALL 修复版本、F 的 FRP 版本与 `observation_multiple=800` 已锁定；尚未发布真实 GO，也未创建物理 Codex 线程。WALL 可在现场预检通过后先启动；F 必须先对账并释放 `/dwdhome/fy/BASE_E6_2_copy`。

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
→ 继续找明显不合理点
→ 当前深度闭环
```

两条基础线都形成可释放版本后，再启动各自下游。

## 2. 首先阅读

[启动就绪检查与来源地图](START_READINESS_AND_SOURCE_MAP.md) 是实际主控的第一入口。它说明：

- 当前哪些内容已经锁定；
- 哪些仍是现场事实；
- 每个问题去哪里找原件；
- WALL 为什么可以先行；
- F 为什么暂时不能直接占用原工作区；
- 八项正式启动预检。

## 3. 文件

| 文件 | 用途 |
|---|---|
| [START_READINESS_AND_SOURCE_MAP.md](START_READINESS_AND_SOURCE_MAP.md) | 启动判断、来源地图、物理预检和运行顺序 |
| [OWNER_PROMPT_EXTRACT.md](OWNER_PROMPT_EXTRACT.md) | Owner 历史 prompt、纠偏和优先级的完整提炼 |
| [OWNER_INPUT_UPDATE_20261122.md](OWNER_INPUT_UPDATE_20261122.md) | 当前新增的 F 分支、800 实例和启动检查要求 |
| [OWNER_INTENT_AND_RUN_PLAN.md](OWNER_INTENT_AND_RUN_PLAN.md) | 两线并行、当前深度和停止条件 |
| [WALL_BASE_RUN_INPUT.md](WALL_BASE_RUN_INPUT.md) | WALL 精确版本、默认实例、范围、来源和统计问题 |
| [F_BASE_RUN_INPUT.md](F_BASE_RUN_INPUT.md) | F 精确版本、800 构造、范围、来源和统计问题 |
| [KNOWN_FINDINGS.md](KNOWN_FINDINGS.md) | 当前已知 finding 的状态 |
| [DOWNSTREAM_DEPENDENCIES.md](DOWNSTREAM_DEPENDENCIES.md) | 联合 Barrier、WALL 下游和 F→Q→V |
| [VERSION_WORKSPACE_LOCKS.md](VERSION_WORKSPACE_LOCKS.md) | 所有版本、工作区、线程和授权锁 |

## 4. 已锁定版本

### WALL

```text
daowei2026/tis@6618d4d147d6ebbe634e61facddf2c9a0b996982
WallAssembler default params
rb / m
2021-01-01..2021-12-31
/dwdhome/fy/BASE_E6_2
```

### F

```text
daowei2026/frp@ac1927518ad6105f15ffbe37fea45e4be91ba574
daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767
profile.observation_multiple = 800
rb / hc / i
5m
2021-01-01..2023-12-31
/dwdhome/fy/BASE_E6_2_copy
```

旧 F `make_features(...)` 入口本身不带 `observation_multiple` 形参；必须按 `F_BASE_RUN_INPUT.md` 的正常参数对象构造 F800，并在运行前回读完整配置。原样执行旧脚本会使用默认 6。

## 5. 运行 profile

两条基础 Run 均采用：

```yaml
execution_profile: CODEX_NATIVE_DIRECT
controller_skill: daowei2026/cgpterm@fc966bcf5441701182339c992865504692f3a466:.agents/skills/observe-iterate-longrun-v2-codex-native-controller/SKILL.md
manager: fresh Codex thread per run
executor: fresh Codex thread per run
workers: []
```

manager 与 executor 是不同线程。manager 只协调，不因同处 Linux 工作区而直接做专业执行。

## 6. 当前具名阻断

### F 工作区冲突

当前 Registry 仍登记：

```text
OI-U2-V-OBS-20261120-01
→ /dwdhome/fy/BASE_E6_2_copy
```

必须先核旧 V Run 是否已经真实结束并释放线程、进程和写面。不能擅自换工作区，也不能直接覆盖。

### 尚未发生的事实

以下尚未发生，不能在准备文档中假报：

- 正式 OWNER GO；
- 新 Run 的 RUN_BINDING / RUN_RESOURCE_BINDING；
- Codex manager/executor thread 创建与回读；
- Linux 工作区实时独占检查；
- 当前结果包身份和 SHA 核验。

## 7. 专业来源

采用：

- `control-v0.3/`；
- `skills/feature-understanding/` 及业务对象判别补充；
- `feature-global-behavior-profiling`；
- `business-discrepancy-diagnosis`；
- 必要时 `feature-instance-calibration`；
- `STATISTICS_DRIVEN_PRACTICE.md`。

历史 Chat 是 Owner 思考过程、纠偏和 finding 来源，不替代当前代码、参数和正式运行结果。

## 8. 修改边界

Codex 可以自主运行、统计、分析、写诊断脚本、准备候选 patch 和新旧对照；若要正式改变代码、参数、规则、数据处理或输出合同，必须：

```text
ModificationProposal
→ Owner 确认
→ 才正式采用
→ 重跑和重统计
```
