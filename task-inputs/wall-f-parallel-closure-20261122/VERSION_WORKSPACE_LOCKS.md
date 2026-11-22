# 版本、工作区与授权锁

> 本文件与真实 GO 一起使用。业务版本和 Owner 指定范围已基本锁定；物理工作区、线程、模型与授权必须在实际主控现场回读。任何具名阻断未解除前，不得把对应 Run 标成已启动。

## 1. observe-iterate

```yaml
repository: daowei2026/observe-iterate
branch: feat/statistics-driven-feature-closure-v0.3-20261122
adopted_commit: LOCK_THIS_BRANCH_HEAD_IN_REAL_GO
control: control-v0.3
execution_profile: CODEX_NATIVE_DIRECT
```

`adopted_commit` 由真实 GO 锁定启动时的最终 40 位提交；准备文件不自引用自身未来提交。

## 2. cgpterm 物理控制

```yaml
repository: daowei2026/cgpterm
branch: feat/observe-iterate-codex-native-direct-20261122
commit: fc966bcf5441701182339c992865504692f3a466
controller_skill: .agents/skills/observe-iterate-longrun-v2-codex-native-controller/SKILL.md
manager: fresh Codex thread per run
executor: fresh Codex thread per run
workers: []
model_and_effort: resolve from the adopted runtime target and read back before each first send; no silent downgrade
```

该 commit 新增的是物理 profile，不修改专业 Workflow 或 Feature 行为。实际 cgpterm 工作树必须加载该精确提交；仅在 GitHub 存在不等于现场已经采用。

## 3. WALL

```yaml
run_id: ASSIGN_AT_REAL_GO
repository: daowei2026/tis
remote_branch: codex/wall-output-consistency-20261121
full_commit: 6618d4d147d6ebbe634e61facddf2c9a0b996982
feature_class: mquant.tis.hf.prel0.wall_assembler.WallAssembler
parameter_instance: WallAssembler default params at the locked commit
sof_name: TA_updto20240229_DBA
symbols: [rb, m]
start_date: 2021-01-01
end_date: 2021-12-31
calendar: night_end_at_2300
workspace: /dwdhome/fy/BASE_E6_2
result_reuse: only after exact commit/config/scope/hash/readback verification
```

修复链：

```yaml
D1_output_position_consistency: 19e6b15ee4a5a58c71bf40902bbc6f6657a16ea2
D2_end_precedes_same_tick_dormancy: 4d06ec211d0a20f2ded80417a3334c78cf4b1a0e
D4_effective_support_resets_far_streak: 6618d4d147d6ebbe634e61facddf2c9a0b996982
```

## 4. F

```yaml
run_id: ASSIGN_AT_REAL_GO
frp_repository: daowei2026/frp
frp_branch: codex/f-observation-multiple-20261122
frp_full_commit: ac1927518ad6105f15ffbe37fea45e4be91ba574
tis_repository: daowei2026/tis
tis_full_commit: 2f460d663d821cf2ba25555eda13e78b697d0767
tis_constructor: frp/fqv_kline_example.py::make_features
parameter_override:
  profile.observation_multiple: 800
base_profile:
  delta: 600
  unit: CalendarUTITick
sof_name: TA_updto20240229_DBA
industry: steel
symbols: [rb, hc, i]
sampling: 5m
start_date: 2021-01-01
end_date: 2023-12-31
calendar: night_end_at_2300
workspace: /dwdhome/fy/BASE_E6_2_copy
result_reuse: only after serialized config/full_dir/hash/31-table readback verification
```

正式实例绑定见 `F_BASE_RUN_INPUT.md`。旧实例脚本原样运行会使用默认 6，不得直接作为 F800 入口。

## 5. 当前工作区阻断

### WALL

当前准备材料未发现 Registry 中另一个活跃 Run 明确绑定 `/dwdhome/fy/BASE_E6_2`，但主控仍须在实际 Linux 主机核：

- 目录存在；
- realpath；
- 当前分支和脏工作树；
- 是否有旧线程／进程仍在写；
- 共享缓存、数据库和结果目录的单写者。

### F

当前 `longrun/controller/RUN_REGISTRY.json` 仍登记：

```text
OI-U2-V-OBS-20261120-01
workspace = /dwdhome/fy/BASE_E6_2_copy
```

所以 F 状态为：

```text
BLOCKED_UNTIL_EXISTING_V_RUN_AND_WORKSPACE_ARE_RECONCILED
```

主控必须核实旧 V Run 是否已经真实结束、所有 turn/进程/写副作用是否收束，并正式释放该路径。不能只因日期较早、Registry 可能陈旧就直接复用，也不能擅自改用其他工作区。若旧 Run 尚未结束，F 等待；WALL 可在自身条件满足时先运行。

## 6. 线程与工作区检查

每个新 Run 启动前核：

1. manager 与 executor 是两条不同的新 Codex thread；
2. threadId、cwd、realpath、model、effort 已由 App Server 回读；
3. 不复用其他 Run 的 threadId；
4. workspace 与其他活跃 Run 不重叠且无父子包含；
5. manager 无业务写权限；executor 的实际写面被 Owner grants 覆盖；
6. 代码 checkout、Python/Haskell 实际加载路径与锁定 commit 一致；
7. 共享输出、数据库和缓存有明确单写者。

## 7. 一次性工程授权

真实 GO 分别登记需要的：

```text
operation
execution_context
allowed_writes
authority_quote
```

至少区分：

- 读取代码、历史结果和缓存；
- 运行 Feature、写本 Run 结果；
- 写分析脚本和报告；
- 提交任务记录；
- 修改／提交／推送 Feature 代码（默认不授权；需 Owner 另行确认具体 ModificationProposal）。

WALL 和 F 不互相继承授权。`workers=[]` 不表示 executor 自动拥有所有写权限。

## 8. 正式 GO 前还需形成的实物

```text
每个 Run 的唯一 run_id
OWNER_GO_CODEX_NATIVE 原件
RUN_BINDING.json
RUN_RESOURCE_BINDING.json
物理 manager/executor thread receipts
工作区与共享写面核验记录
采用的 observe-iterate exact commit
```

这些由实际主控在真实启动时形成；本准备文件本身不是 GO，也不伪称线程已经创建。
