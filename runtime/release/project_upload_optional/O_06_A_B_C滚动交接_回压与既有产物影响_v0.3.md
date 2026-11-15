# A／B／C滚动交接、回压与既有产物影响

# 1. A→B

传：

```text
Feature／Action／method／bounded-state／realization／product／consumer合同。
```

不传：

```text
Builder隐藏推理；
全部raw；
EAW专名作为common core；
未裁Owner候选当current。
```

# 2. B→C

传：

```text
frozen S0；
realization ledger；
state plan；
method binding；
materialization qualification；
production/readback chain；
VCC；
implementer probe关闭状态；
exact repo scene。
```

# 3. C回压

```text
RepoFact漂移 → B RepoFact；
realization/VCC缺口 → B Compiler；
Feature/time/history/product缺口 → A；
平台能力 → platform owner；
真正价值取舍 → Owner。
```

# 4. 既有产物影响

每次 Agent 或合同 delta 必须声明：

```text
FUTURE_ONLY；
REAUDIT_EXISTING；
RETROFIT_EXISTING；
INVALIDATE_AND_REBASE_DOWNSTREAM。
```

历史已完成 artifact 不被追溯改写；继续使用或恢复执行时才按当前版本做 compatibility check。

# 5. Stale传播

```text
A改变Feature／state/time/history/product
  → B engineering artifacts stale
  → C Host artifacts/checkpoints stale。

B只修repo fact或等价realization
  → 受影响VCC/C artifact定向rebase。

C只做合同保持型bugfix
  → 不自动回写A/B；
  但保留runtime evidence供maintenance。
```


# 6. Git 交接与下游版本

执行修订 `2026-09-07`：A→B→C 使用 `repo + exact commit + 正文路径/章节 + 使用资格`，不要求每次打包。一个稳定正文路径可以继续修改，下游仍锁正在消费的提交。接受新版本时才更新交接并核对受影响部分，不能把上游 latest 自动灌给下游。

地图标记新增候选、待审、可局部消费、已暂停等事实；完整正文和实际审查仍决定资格。只读调查可进入不等于完整工程设计或实现已获准。历史交接保留，不覆盖既有 review 所审的版本。
