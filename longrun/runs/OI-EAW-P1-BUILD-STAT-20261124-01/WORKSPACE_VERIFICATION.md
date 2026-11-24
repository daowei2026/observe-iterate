# Build 工作区与资源核验

Owner 指定工作区 `/dwdhome/fy/BASE_E6_2` 已存在，realpath 同值且当前账户可读写穿越。旧 Absorb 已按本主控后续 Owner 指令终止并释放；准确依据：
`daowei2026/observe-iterate@fad5c4e4d0e46766b50327a41d7f064436380036:longrun/runs/OI-ABSORB-STAT-20261123-01/OWNER_TERMINATION_AND_RESOURCE_RELEASE_20261124.md`。

本次检查旧角色最近 turn 已结束、无排队、原主控仍paused且原timer inactive；定向进程未见本工作区任务写者，既有重型锁非阻塞探测未持有。当前可信索引中占用另一工作区的 F800 仍Owner暂停；旧WALL、Absorb、旧V等终止/释放事实保留。此前同路径的历史Run没有被本Run复用线程或完成状态。原始线程、锁、进程和路径证据在gitignored controller artifacts。

实际TIS根为 `/dwdhome/fy/BASE_E6_2/mquant/tis`，HEAD为 `179016111ed0394f92025313e46bd13534932a74`；Build/Wall的assembler和core文件与该commit逐字一致。原Wall分支未修改。预存 `frpExample/STCalendar.py` 未提交修改保留，其来源/正式加载影响须由executor据实核定，不允许本Run越权修复或覆盖。

允许写入的新TIS分支为 `codex/oi-eaw-p1-build-fix-20261124-01`；当前尚未创建。运行记录只用 `codex/oi-eaw-p1-build-stat-20261124-01`。两仓push权限和本机指定refspec dry-run已通过；实际写入仍逐动作遵守Owner grants，不能由权限探测代替授权。

现役App Server已核实际进程/Unix peer和本主控thread；model/list支持 `gpt-6.1-sol` 与 `max`。工作区config/read为danger-full-access、approvals_reviewer=auto_review、approval_policy=null；后续新角色及实际turn必须独立回读，不由默认值声称全部命令获批。

以上支持控制层注册与新角色创建，不证明Build加载/全参数/正式运行/结果读回完成，也不证明exact Wall产物已齐备。新executor正式生产前继续核其当前写面、数据/缓存/数据库和结果单写者；需要重型共享资源时使用已有生产互斥，保留历史结果。
