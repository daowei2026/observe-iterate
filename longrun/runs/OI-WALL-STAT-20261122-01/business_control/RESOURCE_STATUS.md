# WALL 运行资源状态｜C0005 消费视图

本视图只消费 C0004 已发布证据，不代替 controller 的实时物理资源账本，不改写原 RUN_RESOURCE_BINDING。

来源为 `daowei2026/observe-iterate@af85146d2b314b4fbad14929a05df347507b2c27:longrun/runs/OI-WALL-STAT-20261122-01/artifacts/D002/RESOURCE_AND_WRITE_SUMMARY.json`、同提交 C0004 `STATUS.json`（记录于 2026-11-22 18:44:03，Asia/Shanghai）及 `EXECUTOR_REPORT.md`。

| 资源／事实 | 最新有据状态 | 边界 |
|---|---|---|
| 本 Run 主生产 | 已实际调用 m 与 rb；主生产进程已退出 | m 失败，rb 成功；退出不代表完整 rb/m 任务完成 |
| 本 Run 主 heavy lease | `RELEASED`；原记录已确认生产进程持锁并释放 | 不继续占用该锁等待 Owner |
| rb 辅助诊断重放 | 已结束；独立 lease 为 `RELEASED` | 已消费其与正式 rb 全量等价的证据；不是新正式 Feature 输出 |
| 本 Run 结果写面 | 使用独立 native-cache；C0004 的写 FD 检查未见冲突，backup 写面为空 | 这是执行时证据，不推断其他 Run 当前资源状态 |
| 工作区与物理角色 | 仍沿原 `/dwdhome/fy/BASE_E6_2` 及原 manager/E1 绑定 | 本 C 不注销 Run、不宣布整个工作区已释放或新授权生产 |
| 候选输入处理 | M001 待 Owner 确认；候选审阅文件保留 | 未应用至本 Run 锁定正式检出、未产生新的正式行为提交 |
| 下一生产准入 | 当前无后台正式生产或持锁等待交给 manager | 真实 Owner 决定和合法新 C 后，仍依原 profile 核当时身份、版本、写面与单写者 |

当前已验证 rb 的精确 full_dir 为：

`/dwdhome/fy/BASE_E6_2/.runtime/OI-WALL-STAT-20261122-01/native-cache/BaseData/futures/TA_updto20240229_DBA/fao/prod/2021-01-01 21:00:00~2021-12-31 20:00:00/WallAssembler/8/8/5/1/d/6/1/b25bd29dd0d30a972dfabd41edcdf0518/rb.night_end_at_2300`

m 对应的 `m.night_end_at_2300` 路径只有失败现场，不是可供正式消费的结果。完整结果身份、fields／receipt／文件哈希和读回范围保持引用同提交的 `FeatureRunResultBinding.json`、`INDEPENDENT_READBACK.json` 与 `M_FORMAL_FAILURE.json`。

当前 rb 数据与剖面全部保留。若 Owner 确认改变并采用新代码锁，原 M001 要求使用新 attempt 完整重跑和重统计；此旧结果目录不改写成新版本身份，不删除对照，不把 m 失败目录标作成功。真实 PID/fdinfo、锁与运行日志仍留在 gitignored 现场证据中。
