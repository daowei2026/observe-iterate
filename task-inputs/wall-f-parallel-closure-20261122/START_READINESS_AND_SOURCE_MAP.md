# 启动就绪检查与来源地图｜WALL / F 并行统计闭环

## 1. 当前结论

截至本文件提交时：

```text
业务任务与分析范围：已说明
WALL 代码与默认实例：已锁定
F 代码与 observation_multiple=800：已锁定
Codex manager + executor、零 Worker 的 cgpterm profile：已落地到独立分支
真实 Owner GO：尚未发布
物理线程：尚未创建
实际 Linux 工作区：尚未现场核验
F 工作区：与 Registry 中旧 V Run 存在待对账占用
```

因此不能把两条线都立即标记为 `RUNNING`。

更准确的启动判断：

| 线 | 当前状态 | 可否直接正式启动 |
|---|---|---|
| WALL | 业务输入完整，需工作区／代码加载／结果复用现场预检 | **预检通过后可以** |
| F | 业务输入完整，F800 构造已说明，但工作区仍被旧 V Run 登记占用 | **当前不能；先对账并释放工作区** |
| 联合 Campaign | 两条基础线均未有真实 Run Binding | **不能宣称已启动** |

WALL 不需要为了等待 F 而停住。若 `/dwdhome/fy/BASE_E6_2` 现场预检通过，可以先开 WALL；F 在旧 V Run 和 `/dwdhome/fy/BASE_E6_2_copy` 释放后再并行接入。

## 2. 唯一入口和阅读顺序

实际主控和两个 Run 的 manager 不需要在仓库里自由搜索。按下列顺序读取：

```text
1. 本文件
2. OWNER_PROMPT_EXTRACT.md
3. OWNER_INTENT_AND_RUN_PLAN.md
4. WALL_BASE_RUN_INPUT.md 或 F_BASE_RUN_INPUT.md
5. KNOWN_FINDINGS.md
6. control-v0.3/README.md
7. control-v0.3/01_L0_统计驱动的单特征闭环.md
8. 对应 Skill 与统计实践补充
9. VERSION_WORKSPACE_LOCKS.md
10. Codex-native cgpterm controller Skill
```

不要从历史聊天自行拼任务范围；历史 Chat 只在相应输入文件点名的位置作为思考和证据来源。

## 3. 来源地图

### 3.1 Owner 意图与当前范围

| 需要找什么 | 唯一入口 |
|---|---|
| Owner prompt 的提炼与优先级 | `task-inputs/wall-f-parallel-closure-20261122/OWNER_PROMPT_EXTRACT.md` |
| 两线并行、停止深度、联合 Barrier | `OWNER_INTENT_AND_RUN_PLAN.md` |
| 当前已知 finding | `KNOWN_FINDINGS.md` |
| 下游依赖 | `DOWNSTREAM_DEPENDENCIES.md` |
| 版本、参数、工作区和授权 | `VERSION_WORKSPACE_LOCKS.md` |

### 3.2 WALL

| 需要找什么 | 精确来源 |
|---|---|
| 本轮正式输入 | `WALL_BASE_RUN_INPUT.md` |
| 原 EAW 用例 | `task-inputs/eaw-p1-integrated/` |
| 既有 Feature 理解 | `task-inputs/eaw-p1-integrated/feature-understanding-result/WALL_FEATURE_UNDERSTANDING_PACKAGE.md` |
| 原统计和 Owner 纠偏 | `ai_chat/根据统计找不合理点/WALL 特征：统计线闭环.md` |
| D1/D2/D4 修复过程 | `ai_chat/根据统计找不合理点/wall特征，修frp代码.md` |
| 最终 producer wrapper | `daowei2026/tis@6618d4d147d6ebbe634e61facddf2c9a0b996982:hf/prel0/wall_assembler.py` |
| 最终状态机 core | `daowei2026/tis@6618d4d147d6ebbe634e61facddf2c9a0b996982:hf/prel0/wall_assembler_core.py` |
| 前次结果目录线索 | `/dwdhome/fy/BASE_E6_2/.runtime/wall-rb-m-20210101-20211231-20261120/` |

### 3.3 F

| 需要找什么 | 精确来源 |
|---|---|
| 本轮正式输入与 800 构造 | `F_BASE_RUN_INPUT.md` |
| 原 U2/U3 F 输入 | `task-inputs/u2-fqv-observation/F_OBSERVATION_RUN_INPUT.md` |
| 原构造脚本 | `task-inputs/u2-fqv-observation/实例运行脚本.py` |
| 需求／实现索引 | `task-inputs/u2-fqv-observation/无二义性需求和实现文件.md` |
| 原完整配置 | `daowei2026/feature-refinement-implementation-agent-evolution@2d3f56a7944c44b2a1c441c15eebf9659835136b:agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/configurations/fqv-kline-rb-hc-i.json` |
| 原统计和 Owner 纠偏 | `ai_chat/根据统计找不合理点/F特征：统计线闭环.md` |
| 新 FRP 代码 | `daowei2026/frp@ac1927518ad6105f15ffbe37fea45e4be91ba574` |
| TIS 构造入口 | `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/fqv_kline_example.py` |
| Python Feature wrapper | `daowei2026/tis@2f460d663d821cf2ba25555eda13e78b697d0767:frp/CommonPriceTurnGroupCandidates.py` |

### 3.4 Control、Skill 与运行层

| 需要找什么 | 精确来源 |
|---|---|
| 单 Feature 统计闭环 | `control-v0.3/01_L0_统计驱动的单特征闭环.md` |
| 释放与下游 | `control-v0.3/02_L1_本特征释放与下游依赖.md` |
| 业务对象判别 | `skills/feature-understanding/BUSINESS_OBJECT_QUALIFICATION_GUIDE.md` |
| 全量统计 Skill | `skills/reasonableness-analysis/feature-global-behavior-profiling/` |
| 偏差诊断 Skill | `skills/reasonableness-analysis/business-discrepancy-diagnosis/` |
| 统计实践补充 | `skills/reasonableness-analysis/STATISTICS_DRIVEN_PRACTICE.md` |
| Codex-native 物理 controller | `daowei2026/cgpterm@fc966bcf5441701182339c992865504692f3a466:.agents/skills/observe-iterate-longrun-v2-codex-native-controller/SKILL.md` |
| V2 机读合同 | `longrun/contracts/longrun_schema_v2.json` |
| Owner GO 模板 | `longrun/templates/OWNER_GO_CODEX_NATIVE.md` |

## 4. 启动前必须通过的八项预检

### P1｜采用版本

真实 GO 写入并回读：

```text
observe-iterate exact commit
cgpterm@fc966bcf5441701182339c992865504692f3a466
WALL TIS@6618d4d...
F FRP@ac192751...
F TIS@2f460d66...
```

### P2｜工作区占用

在真实 Linux 主机核：

- `/dwdhome/fy/BASE_E6_2`；
- `/dwdhome/fy/BASE_E6_2_copy`；
- realpath、进程、线程、Git 状态、共享输出和缓存。

F 必须先对账 `OI-U2-V-OBS-20261120-01`。旧 V Run 未真实结束时，不得在同一路径启动 F。

### P3｜物理角色

每个 Run 分别创建并回读：

```text
codex:<run_id>:manager
codex:<run_id>:executor:E1
```

两条 thread 不同，且都属于本 Run；`workers=[]`。

### P4｜实际代码加载

执行环境记录：

```text
Git HEAD
Python inspect.getfile(...)
必要的 Haskell package / source identity
```

路径必须对应锁定提交；只 checkout 分支名不够。

### P5｜正式参数绑定

WALL：保存默认 `WallAssembler` 参数，确认没有带入旧标定候选。

F：保存完整序列化配置，确认唯一有意差异是：

```yaml
profile.observation_multiple: 800
```

并确认 `delta=600`、2Δ 条件未改变。旧脚本若仍得到默认 6，立即停止。

### P6｜正式范围

WALL：rb/m、2021 全年、`night_end_at_2300`。

F：rb/hc/i、5m、2021—2023、`night_end_at_2300`。

局部诊断不能替代正式范围。

### P7｜结果复用

已有目录只有在代码、配置、范围、日历、输入处理、SHA 和独立读回全部一致时才可复用。否则运行正式实例。不得仅凭提交说明、文件名或目录存在宣称结果可用。

### P8｜授权

GO 必须覆盖：

- 运行 Feature；
- 写本 Run 结果、统计脚本和报告；
- 提交本 Run 记录；
- 是否允许读取／复用旧缓存。

默认不授权修改、提交或推送新的 Feature 行为。任何新修改仍先形成 `ModificationProposal` 回 Owner 确认。

## 5. 通过预检后的实际顺序

```text
注册 WALL Run（可先行）
→ 创建 WALL Codex manager
→ manager 签首个 Skill D
→ 创建 WALL Codex executor
→ U 最小核对 → X → G → finding 闭环

旧 V Run 与 F workspace 对账完成
→ 注册 F Run
→ 创建 F Codex manager
→ manager 签首个 Skill D
→ 创建 F Codex executor
→ F800 配置回读 → X → G → finding 闭环
```

一条线等待 Owner 修改确认时，另一条线继续无冲突工作。

## 6. 不应再次询问 Owner 的已知事项

除非实际来源发生冲突，不要再问：

- WALL 用什么品种、年份或工作区；
- F 用什么品种、尺度、年份或工作区；
- F 的 `observation_multiple` 是多少；
- manager/executor 是否放 Web；
- 是否使用 Worker；
- WALL D1/D2/D4 是否已经确认采用；
- 新 finding 是否可直接正式修改。

这些都已在当前任务输入中明确。

## 7. 需要报告而不是自行猜测的事项

- 旧 V Run 是否真实结束和释放 F 工作区；
- 现场 Codex 可用的准确 model alias / effort 值；
- 已有 F800／WALL 修正版结果的真实路径和哈希；
- 代码加载路径与锁定 commit 不一致；
- 正式输入缺失或共享写面冲突。

这些是现场事实，主控或 executor 核完直接记录；不能用文档占位或模型推测代替。
