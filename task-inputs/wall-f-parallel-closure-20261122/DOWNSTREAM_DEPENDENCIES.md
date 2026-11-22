# 下游依赖与联合 Barrier

## 1. 基础联合 Barrier

```yaml
release_policy: JOINT_BASE_BARRIER
requires:
  wall_base:
    gate: PASS | PASS_WITH_ACCEPTED_LIMITATIONS
    release_package: REQUIRED
  f_base:
    gate: PASS | PASS_WITH_ACCEPTED_LIMITATIONS
    release_package: REQUIRED
```

主控只核对真实 Gate 和 ReleasePackage。任一基础 Run 为 `BLOCKED`、`OPEN_CONFIRMED_DEFECT` 或 `RERUN_REQUIRED` 时，不释放本 Campaign 的下游批次。

## 2. F 下游

真实构造关系按现有资料为：

```text
F CommonPriceTurnGroupCandidatesFrp
→ Q PostTurnGroupDirectionalOrganizationFrp
→ V CommonTurnGroupValidityFrp
```

执行规则：

1. Q 锁定 F ReleasePackage 和真实构造入口；
2. Q 自己完成 U/X/G/问题闭环并形成 Q ReleasePackage；
3. V 在 Q 通过后启动，锁定 Q 以及构造所需的 F 版本；
4. 共用 `make_features(...)` 不等于 F、Q、V 是一个统计任务；
5. 上游依赖可以在运行时被构造／读取，但不能把上游输出冒充当前目标 Feature 的主输出。

## 3. WALL 下游

正式启动前由 Owner 补齐：

```yaml
wall_downstream_features: PENDING_OWNER
edges: PENDING_OWNER
required_wall_outputs: PENDING_OWNER
parallelizable_groups: PENDING_OWNER
sequential_groups: PENDING_OWNER
```

当前 EAW P1 历史资料可以作为查找线索，但不能仅凭“P1”名称自动扩出全部下游。

每个下游必须登记：

```yaml
downstream_feature:
required_upstream_releases:
constructor_or_wiring_ref:
required_output_contract:
known_limitations_consumed:
```

WALL-D3 必须进入下游的 `known_limitations_consumed`，直到它被正式关闭或证明不适用。

## 4. 失效传播

- WALL Release 变化：所有消费该版本的 WALL 下游标记 `STALE_UPSTREAM`；
- F Release 变化：未启动 Q 停止启动，已运行 Q 及其 V 后继标记 stale；
- Q Release 变化：V 标记 stale；
- 只改统计报告、不改变代码／参数／数据／正式输出，不自动使下游运行失效，但 ReleasePackage 的解释版本应更新。

下游返回受影响节点，不机械重做无关工作。
