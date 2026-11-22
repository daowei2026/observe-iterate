# Owner 输入更新｜2026-11-22

本文件只保存当前对话中新增加、尚未包含在早先 `OWNER_PROMPT_EXTRACT.md` 中的 Owner 输入。

## 1. F 正式代码版本

Owner 指定：

```text
https://github.com/daowei2026/frp/tree/codex/f-observation-multiple-20261122
```

已核为：

```yaml
repository: daowei2026/frp
branch: codex/f-observation-multiple-20261122
commit: ac1927518ad6105f15ffbe37fea45e4be91ba574
```

正式 Run 使用完整 commit，不只使用可移动分支名。

## 2. F 正式新实例

Owner 指定：

```yaml
observation_multiple: 800
```

结合新 FRP 代码的实际字段，正式配置位置为：

```yaml
profile.observation_multiple: 800
```

该输入是本轮正式实例，不是 AI 建议或待标定候选。AI 不得自行改成其他值。

## 3. 当前 Owner 问题

Owner 要求在启动前检查：

- 当前是否已经可以直接运行；
- 这样运行是否会有问题；
- 是否仍有内容未说清楚；
- 执行时能否明确知道各项信息从哪里寻找。

因此本轮新增 `START_READINESS_AND_SOURCE_MAP.md`，并把无法由文档代替的现场事实保留为明确预检，而不是让执行 AI 临场猜测。

## 4. 未产生的新授权

本次输入没有授权 AI：

- 再次修改 F 的正式参数；
- 修改 WALL/F 正式代码或规则；
- 改变品种、时间范围、尺度或工作区；
- 覆盖仍被其他 Run 占用的工作区；
- 自动降级模型或改用 Web/Worker 路径。

新 finding 若需要正式行为改变，仍按 `ModificationProposal → Owner 确认` 执行。
