# W002 最小事实报告

run_id：OI-U2-F-OBS-20261118-01
work_order_id：W002
parent_delegation_id：D005
issuer_call_id：C0014
worker：codex:OI-U2-F-OBS-20261118-01:worker:W1
return_to：chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
order_ref：daowei2026/observe-iterate@2bdc0b96259b9c2a895113328b9ccc1172f09e6e:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W002/ORDER.json

状态：BLOCKED。工单真实推进至指定私有 namespace 建立步骤，按原停止条件终止；运输后拟签认 outcome=STOP。
source staging：/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W002/source_stage_report.json；SUCCESS，独立 detached HEAD=f4f0e4b276b1118b779473c1fbe462bc7a64b358，D/C3 均存在且与原引用逐字节一致。
private shm：/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W002/private_shm_report.json；未能进入 namespace 内部脚本，不能证明 backing 已建立。runtime/shm 已在 W002 内创建，权限 1777，目录为空。
最终脚本：/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W002/source/observe-iterate/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py；HEAD=f4f0e4b276b1118b779473c1fbe462bc7a64b358，未修改，亦未执行。
候选 HTML：无。
运行日志：/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W002/logs/private_shm_mount.log；D 运行日志无，因为 D 未启动。
退出码：namespace 命令为 1；SemLock probe 和 D 均未启动，二者无退出码，不能把 namespace 的 1 写成 D 退出码。
实际修改：D/C3 无修改；/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W002/repair.diff 为 0 字节，/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W002/final_git_status.txt 为空。
definition_run_report：无，未生成。

首个真实阻断的完整 stderr：

```text
unshare: write failed /proc/self/uid_map: Operation not permitted
```

实际命令：

```text
/usr/bin/unshare --user --map-root-user --mount --fork /bin/bash /dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W002/private_shm_episode.sh /dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W002
```

unshare、mount、findmnt 均为现有 util-linux 2.39.3，版本与路径记录于 /dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W002/tool_versions.json。命令只请求 user 和 mount namespace；没有请求 PID namespace。unshare 写入 /proc/self/uid_map 时返回 Operation not permitted，子 bash 尚未进入；因此 namespace 内的 mount --make-rprivate、bind mount、findmnt -T /dev/shm、mountinfo 采集、alias probe、SemLock probe、业务运行环境初始化、Landlock 和 D 全部未执行。runtime_worker.py 与 private_shm_episode.sh 是本次准备的条件执行入口，不是已经执行成功的证据。

实际次数：私有 namespace 尝试 1 次；SemLock probe 0 次；D 0 次。namespace 命令墙钟 0.064791860 秒（独立实测）。完整准备、输入核对、staging 和封存的端到端精确耗时未独立测量；不能把这一个子步骤的时长当作 W002 总成本。

W002 第五、八、十一节要求私有 mount 无法建立时停止。Worker 没有直接写宿主 /dev/shm，没有 sudo、其他 namespace 路径或宿主权限 fallback，没有 patch 平台库或改动 D/C3 来绕过 import，没有作进一步无界诊断。仅凭本日志不能进一步断言具体宿主安全策略或 capability 配置，也不能说明 D、F 数据或 CAEGraph 有缺陷。

F 未构造、fields.json 未检查；未调用 f.rerun、全历史 producer 或 Q/V；未生成 HTML、prepared_tables、plot_data；没有 DATA_READY 或正式取数准入。没有对 W001、其他 Run、既有平台源码、生产数据或外部 symlink 目标执行写操作，没有推送 source checkout。W001 的既有 STOP、Landlock 历史与已封存证据保持原样；W002 的直接阻断发生于 uid_map，早于本轮任何 Landlock 应用。

事实、日志、退出码、源码状态与完整正文运输包均限于 W002。正式 result_ref 与新增证据 manifest.ref 待主控按原字节发布后提供真实 commit；D/C3 可复用既有精确 refs。当前准备稿不是正式 worker_return，没有伪造未来 refs。真实 refs 返回后，在同一 W002 下核验并签认 longrun-worker-return/v2，回原 executor:E1 消费，继续 D005 / WI-E / M-E。
