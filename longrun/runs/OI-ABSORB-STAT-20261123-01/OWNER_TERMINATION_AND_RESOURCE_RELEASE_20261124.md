# Owner 终止旧 Absorb 后继并释放工作区

- run_id：`OI-ABSORB-STAT-20261123-01`
- 管理状态：`OWNER_TERMINATED / CANCELLED_BY_OWNER`
- 业务完成：**否**；本记录不是 Absorb Release 或合理性验收。
- Owner 本次原话：“那先把旧 Absorb 工作区释放，然后接着执行所给任务”
- 解释范围：终止旧 Absorb 未完成后继，保留原件与成果；对账后释放 `/dwdhome/fy/BASE_E6_2`，供新 Build Run 合法启动。其他 Run 的暂停与授权不变。

## 2026-11-24 本次释放检查

现有 App Server 已核进程、Unix peer 与准确线程；旧 manager/executor 均为 notLoaded，其最近真实 turn 为 completed，队列为空。未给旧角色发送任何业务消息，未恢复旧主控 Goal。旧共享主控 Goal 仍为 paused，原计划已 cancelled、timer inactive。

本机定向进程检查无该 Absorb 或指定工作区任务写者；原重型生产锁的非阻塞探测为未持有。现有调用账本：C0001、C0002 的真实回交已核，C0003 的实际 turn 已完成但所准备 D002/管理 Return 未成功发布；本次核 GitHub 旧分支 HEAD 仍为 `62fab7507bdb6943f8e584e176eb9a29a976fe82`，与原账本一致，没有新的未对账远端写入。

保留 C0003“物理回合结束、未产生原生 Return、D002 未派发”的事实，不补造 Return，也不把原 UNKNOWN 历史抹去。未开始的 X/G 和剩余 Absorb 闭环由 Owner 取消，不再继续。

## 资源交接

`/dwdhome/fy/BASE_E6_2` 的旧 Absorb 预约正式释放，状态为 `RELEASED_OWNER_TERMINATED`。旧 Run 不再拥有该工作区的新生产写入资格。所有历史目录、U 包、源码、未提交修改、运行记录与原物理线程均保留，不删除、不清理、不覆盖。

本次不修改或推送 TIS，不复用旧角色作为新 Build 角色；不会自动恢复旧主控或 F800。新的 `OI-EAW-P1-BUILD-STAT-20261124-01` 仍须独立完成资源核验、Binding/Registry 和新 manager/executor 创建派发。本释放记录不证明 Build 已运行，也不证明 Wall 合理性通过。

物理线程标识、原始 App Server 回执、进程与锁探测、Owner 输入原件和完整本地路径证据留在 gitignored controller artifacts。
