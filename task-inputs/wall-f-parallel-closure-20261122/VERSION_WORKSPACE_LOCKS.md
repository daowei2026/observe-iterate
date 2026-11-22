# 版本、工作区与授权锁

> 本文件与两个真实 GO 一起使用。WALL 远端代码版本已经核实并锁定；其余 `PENDING_OWNER` 项仍会阻止对应 Run 的正式启动。

## 1. observe-iterate

```yaml
branch: feat/statistics-driven-feature-closure-v0.3-20261122
adopted_commit: PENDING_FINAL_COMMIT_IN_REAL_GO
control: control-v0.3
execution_profile: CODEX_NATIVE_DIRECT
```

`adopted_commit` 由真实 GO 锁定当时采用的最终 40 位提交；不要求本准备文件自引用自身提交。

## 2. WALL

```yaml
run_id: PENDING_OWNER
repository: daowei2026/tis
remote_branch: codex/wall-output-consistency-20261121
full_commit: 6618d4d147d6ebbe634e61facddf2c9a0b996982
commit_url: https://github.com/daowei2026/tis/commit/6618d4d147d6ebbe634e61facddf2c9a0b996982
constructor_or_entry: PENDING_OWNER
parameter_instance_ref: PENDING_OWNER
result_reuse_ref: PENDING_OWNER_OR_NONE
result_sha256: PENDING_OWNER_OR_NONE
linux_workspace: PENDING_OWNER_ABSOLUTE_PATH
external_write_targets: []
```

已核实的修复提交链：

```yaml
D1_output_position_consistency: 19e6b15ee4a5a58c71bf40902bbc6f6657a16ea2
D2_end_precedes_same_tick_dormancy: 4d06ec211d0a20f2ded80417a3334c78cf4b1a0e
D4_effective_support_resets_far_streak: 6618d4d147d6ebbe634e61facddf2c9a0b996982
```

正式 Run 以 `full_commit` 为版本锁；分支名只用于人类定位，不作为可变版本引用。

## 3. F

```yaml
run_id: PENDING_OWNER
frp_repository: daowei2026/frp
frp_branch: PENDING_OWNER
frp_full_commit: PENDING_OWNER
tis_constructor_ref: PENDING_OWNER_FULL_COMMIT_AND_PATH
parameter_instance_ref: PENDING_OWNER
parameter_instance_sha256: PENDING_OWNER
symbols: [rb, hc, i]
start_date: PENDING_OWNER
end_date: PENDING_OWNER
calendar_ref: PENDING_OWNER
linux_workspace: PENDING_OWNER_ABSOLUTE_PATH
external_write_targets: []
```

## 4. 工作区检查

启动前主控核：

- 两个路径存在；
- `realpath` 不相同且不存在父子包含；
- 实际 cwd 和权限；
- Git 分支、缓存、数据库和输出目录是否仍然共用；
- 共用外部目标是否有单写者。

## 5. 授权

每个 Run 的 GO 分别登记需要的：

```text
operation
execution_context
allowed_writes
authority_quote
```

WALL 和 F 不互相继承授权。`workers=[]` 不表示 executor 自动拥有所有写权限。

## 6. 尚待回填

WALL 尚需：

- 真实 `run_id`；
- 构造／执行入口；
- 参数实例；
- 是否复用既有最终结果包及其 SHA；
- 独立 Linux 工作区与 grants。

F 尚需本节全部版本、参数、范围、工作区与授权信息。全部输入就绪后，再分别生成真实 `OWNER_GO_CODEX_NATIVE`；不得把本准备文件本身当 GO。
