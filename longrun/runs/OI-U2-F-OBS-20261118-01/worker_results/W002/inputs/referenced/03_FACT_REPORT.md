# W001 最小事实报告

run_id：OI-U2-F-OBS-20261118-01
work_order_id：W001
worker：codex:OI-U2-F-OBS-20261118-01:worker:W1
return_to：chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
order_ref：daowei2026/observe-iterate@74562f258d93fdea8db0ab334fb0ebb23f1cfb99:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W001/ORDER.json

状态：BLOCKED。真实 D 执行一次；正式机读 Return 待运输后拟签认 outcome=STOP。
source staging：/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/source_stage_report.json；SUCCESS，detached HEAD=f4f0e4b276b1118b779473c1fbe462bc7a64b358。
最终脚本：/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/source/observe-iterate/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py；D/C3 均与原件逐字节一致。
候选 HTML：无。
运行日志：/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/logs/w1_run.log。
退出码：1；本次命令（含环境入口）壁钟 12.225032 秒（独立实测）；其余准备、检查和恢复未独立计时，不并入该数，总成本未知。
实际修改：无；/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/repair.diff 为 0 字节，/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/final_git_status.txt 为空。
definition_run_report：/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/output/u2_f_caegraph/definition_run_report.json；completed=false，error_type=PermissionError。

首个致命阻断发生于 D:676 导入 mquant.frame。调用链到达工作区 mquant/apt/tool/misc.py:144 的 ProcessPoolExecutor(max_workers=os.getpid() - 2)，创建 _multiprocessing.SemLock 时得到 PermissionError: [Errno 13] Permission denied。尚未导入 make_features、构造 F 或检查 fields.json。因此不能声明精确 F 结果存在或缺失。

执行条件必须一并运输：Worker 为落实 W001 的目录写入限制额外采用了 Landlock，仅允许 W001 内文件写入。独立的标准库 multiprocessing.Lock 诊断（不加载 D/F/Q/V）在相同限制下证实 openat 创建 /dev/shm/sem.HZDYg7 被 EACCES 拒绝。该随机路径来自诊断，主运行的具体 IPC 文件名未跟踪。本结果证明的是该写入限制下的真实阻断，不能用来断言无保护原环境也会失败；不是已证实的 D/C3 或 F 产品缺陷。是否允许工作区外的运行时 IPC，或采用何种其他入口，交原 executor:E1 判断；Worker 未扩大写权限、改动全局库或选择另一业务方案。

实际入口为 /bin/bash /dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/run_w001.sh。其复用现有 m3rc、.runtime/python-deps 及 run-python.sh 中已配置的 TLS 库，Python 为 /m3c3/Linux/apps/anaconda3/bin/python（3.10.13）；没有新建环境、安装依赖或切换项目版本。源码 cwd=/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/source/observe-iterate。其执行 python /dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/boundary_runner.py /dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/source/observe-iterate/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py --output-dir /dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/output/u2_f_caegraph。运行包装器、边界实现及实际环境记录均在证据包内。

日志中 nif2 的 DNS 报错后已采用现有 run-python.sh 的 M3HOST 回退；后续 D 确已启动。joblib 的串行模式警告与写入保护有关；上述两项都不能替代最终 SemLock 致命 traceback。

未调用 f.rerun、全历史 producer 或 Q/V；未生成 prepared_tables、plot_data；未标记 DATA_READY；未进行 E2/E3 核图或 E4/W2。未修改既有环境、生产数据、其他 Run 或外部 symlink 目标，未推送 source checkout。

范围偏差记录：早期一次 AGENTS 文件名定位误将范围包含 /dwdhome/fy，返回了相邻目录路径；随即收敛到精确路径。未读取相邻 Run 正文或手机台账，未修改相邻文件。

本地事实证据已封存；正式 result_ref 与新证据 manifest.ref 尚待主控原样发布后提供真实 commit。现有 D/C3 精确 refs 可复用；没有伪造未来 refs，也没有把本地准备稿宣称为正式 worker_return。收到真实 refs 后，在同一 W001 下核哈希并完成 longrun-worker-return/v2 签认；结果回原 executor:E1，专业分类与下一步由 E1 完成。
