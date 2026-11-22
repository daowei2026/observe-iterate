# 版本、工作区与授权锁

> Owner 补齐后，本文件与两个真实 GO 一起使用。当前所有占位均阻止正式启动。

## 1. observe-iterate

```yaml
branch: feat/statistics-driven-feature-closure-v0.3-20261122
adopted_commit: PENDING_OWNER_AFTER_REPO_CHANGES_COMPLETE
control: control-v0.3
execution_profile: CODEX_NATIVE_DIRECT
```

## 2. WALL

```yaml
run_id: PENDING_OWNER
repository: daowei2026/tis
remote_branch: PENDING_OWNER
full_commit: PENDING_OWNER
constructor_or_entry: PENDING_OWNER
parameter_instance_ref: PENDING_OWNER
result_reuse_ref: PENDING_OWNER_OR_NONE
result_sha256: PENDING_OWNER_OR_NONE
linux_workspace: PENDING_OWNER_ABSOLUTE_PATH
external_write_targets: []
```

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

## 6. 完成后回填

仓库改造完成后，把本分支最终 40 位 commit 写入 `adopted_commit`。Owner 提供 WALL/F 版本与工作区后，再生成真实 `OWNER_GO_CODEX_NATIVE`，不得把本准备文件本身当 GO。
