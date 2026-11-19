# W003 最小事实报告

run_id：OI-U2-F-OBS-20261118-01
work_order_id：W003
parent_delegation_id：D005（当前 C0018 修订）
issuer_call_id：C0019
worker：codex:OI-U2-F-OBS-20261118-01:worker:W1
return_to：chatgpt:OI-U2-F-OBS-20261118-01:executor:E1
order_ref：daowei2026/observe-iterate@dd919cca7df1203f7962888b4ecf8b7d24048c43:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W003/ORDER.json

状态：BLOCKED。正常入口直接运行 D 一次，得到新的真实构造模块导入阻断；未建立唯一可直接采用的机械修法，按原停止条件回 E。正式 Return 待运输后拟签认 outcome=STOP。
source staging：/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003/source_stage_report.json；SUCCESS，独立 detached HEAD=f4f0e4b276b1118b779473c1fbe462bc7a64b358，D/C3 原件一致。
最终脚本：/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003/source/observe-iterate/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py；HEAD=f4f0e4b276b1118b779473c1fbe462bc7a64b358。
候选 HTML：无。
运行日志：/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003/logs/w003_run.log；环境入口完整输出另存 /dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003/logs/environment.log。
D attempt count：1。
D 退出码：1，原值保存在 /dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003/logs/w003_run.exit_code。
实际修改：D/C3 无；/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003/repair.diff 为 0 字节，/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003/final_git_status.txt 为空。
definition_run_report：/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003/output/u2_f_caegraph/definition_run_report.json；已生成，completed=false。
semaphore 事实：/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003/logs/dev_shm_sem.before.tsv 与 /dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003/logs/dev_shm_sem.after.tsv；快照命令均退出 0，两份文件均为空。汇总见 /dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003/semaphore_audit.json。

首个真实阻断：

```text
ModuleNotFoundError: No module named 'mquant.tis.frp.fqv_kline_example'
```

完整 D traceback：

```text
Traceback (most recent call last):
  File "/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003/source/observe-iterate/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py", line 677, in main
    from mquant.tis.frp.fqv_kline_example import make_features
ModuleNotFoundError: No module named 'mquant.tis.frp.fqv_kline_example'
```

实际 D 命令：

```text
python longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py --output-dir /dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003/output/u2_f_caegraph
```

实际 cwd=/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003/source/observe-iterate；Python=/m3c3/Linux/apps/anaconda3/bin/python，版本 Python 3.10.13。运行复用原工单指定的 m3rc、已有 .runtime/python-deps、TLS 库和 W003 cache 重定向，直接启动原 D；没有 Landlock、boundary_runner、unshare、任何 namespace、sudo、mount、平台 patch 或独立 SemLock probe，没有安装依赖、新建环境或切换平台版本。环境入口的 nif2 DNS 输出与回退过程完整留在 environment.log；D 确已启动，因此该环境输出不是本轮最终致命阻断。

有限静态路径核对只涉及当前 mquant/tis/frp 包、声明的构造模块及对应类文件路径、包直接 13 个条目和 __init__.py；没有执行额外平台模块或递归搜索整个工作区。当前检查路径未发现 fqv_kline_example.py 或同名包，包初始化文件不提供 make_features；同范围也未发现 CommonPriceTurnGroupCandidates 的所查文件/目录。证据见 /dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W003/diagnostics/module_path_check.json 与 initializer 原样快照。这不是全工作区或全主机不存在相关代码的断言，也不是精确 F 产品不存在的证据。

未确认一个已配置且语义一致的替代导入路径。Worker 未从远端补装构造模块、未引入另一 TIS/平台版本、未修改平台源码，也没有用其他构造器或近似值替换 F。按照 W003 第九节“正确修法不唯一，或无法判断语义影响”的边界，停止并回原 E1；没有第二次 D 运行。

D 已到达 make_features 的 import，但在函数可用之前失败；F 未构造、fields.json 未检查、真实 F 表未读取。没有调用 f.rerun 或全历史 producer，没有读取 Q/V，没有生成 prepared_tables、plot_data 或候选 HTML，没有 DATA_READY 或正式取数准入。

本轮未由 wrapper 手工创建测试 semaphore 或删除任何 sem.*。两次端点快照均未观察到 sem.*，没有观察到可归属残留；这不证明进程存续期间未创建并正常删除 semaphore，也不构成逐次 IPC 创建/删除审计。没有读写非 sem.* 的 /dev/shm 对象，没有扩大清理动作。

D 命令时间边界为 2026-11-19T07:21:57.231026690Z 至 2026-11-19T07:22:13.009989296Z；没有独立测量 D 单独 elapsed。平台入口（包含环境初始化、D 和审计快照）墙钟 19.377443 秒为独立实测，不能把它称为纯 D 耗时；此前准备、staging、输入核对和之后封存的完整端到端精确总成本未知。

未写 W001/W002、其他 Run、平台源码、生产数据或外部 symlink 目标；未推送 source checkout；未创建 Goal、计划休眠、后台唤醒或新执行器。W001/W002 历史保留。

完整本地事实、日志、报告、源码状态、有限路径核对和 semaphore 记录均将在正文运输包中逐项保存路径、字节数与 SHA-256。正式 result_ref 和新增 manifest.ref 待主控原样发布后提供真实 commit；D/C3 可复用既有精确 refs。当前准备稿不是正式 worker_return。收到真实 refs 后，在同一 W003 下核验并签认，回原 executor:E1，续接 D005 / WI-E / M-E；本 Worker 不替 E 作专业分类或图接受判断。
