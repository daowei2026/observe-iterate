order_id: BI01CO05-FULLRANGE-CHART-DATA-R0008-01
work_id: BI-01
run_id: BI-01-CO-05
issuer_role: professional
issuer_ref: chatgpt:BI-01-CO-05:professional
issuer_invocation_id: BI01-CO-05-R0008-38f9aa094823
issuer_assignment_token: e81eb24808324350a2e7c24d6094
return_to: chatgpt:BI-01-CO-05:professional
worker_execution_id: BI01CO05-R0008-worker-e20dc4a50455
worker_local_execution_turn_id: 569417bd-f109-4849-9e7f-2d5b7b80f5cd
worker_native_turn_id: NOT_EXPOSED
worker_thread_id: 01a17dd7-5033-7e63-b7a2-edd90b691c33
status: FAILED_ENVIRONMENT_IO_ORDER_STOP
technical_pass: false

# 实际结果

有限工单已真实执行一次，并触发第8节“目标环境/数据不可访问”停止条件。`build_chart_run(brief, dry_run=False)`在自动解析日历时读取`/m3varI/var/L1_data/sof/unit/affiliated_calendar_no_night.csv`，返回`OSError: [Errno 5] Input/output error`。主图、七个辅助图和正式切片均未生成，本结果不能进入技术PASS验收。没有依据推断源行情不存在、缺失数量或2024-02-29已实际覆盖。

# 来源、执行身份与环境

全文消费签发原件`34198df6d4435feaa089baeae73e934559bd8b19:runs/BI-01-CO-05/artifacts/professional-R0008/WORKER_ORDER.md`，UTF8 SHA256 `da707bad6aa21f6f62d9916c694892304925fba4bf7f0e0b79e856ed05b96ec8`。原脚本13242字节，实测SHA256 `5571cad70d5c519d9e0c5260564346837833eb147d7c4fafb40afb0505a3df16`，与Professional固定值及该提交原字节一致。当前分支`fy/owner-led-case-exploration-optional-reader-20261102`；初始本地HEAD、实际远端ls-remote及fresh FETCH_HEAD均为签发提交。旧tracking引用滞后93个提交，不是远端分叉。

聊天cwd实核`/dwdhome/fy/cgpterm`；线程环境及原生Goal均返回指定thread；沙箱danger-full-access、approval never，实际工作区外临时文件写/读/删成功。模型/强度由派发方提供gpt-6.1-sol/xhigh；Worker接口未暴露独立参数回读，不伪称本地复核模型或native turn。issuer token仅为签发引用，与以上Worker执行身份分开。

现场aidata原分支`codex/aidata-named-csv-features-20261019`，HEAD `b5a752c2701dd8997b47583808f30bc5da5d9769`；依赖版本与已有tis/uplot差异见DEPENDENCY_BEFORE/AFTER，两次逐项相同，未切换checkout或改共享源码/配置。

# 真实命令、时段与调用顺序

业务cwd：`/dwdhome/fy/BASE_E6_2`。使用已存在的`run-python.sh`初始化现场Python环境，解释器`/m3c3/Linux/apps/anaconda3/bin/python`3.10.13；没有安装或升级。仅设置`PYTHONDONTWRITEBYTECODE=1`避免导入产生共享pycache。实际命令：

```bash
cd /dwdhome/fy/BASE_E6_2
PYTHONDONTWRITEBYTECODE=1 /dwdhome/fy/BASE_E6_2/run-python.sh /dwdhome/fy/observe-iterate-bi01-co-05/runs/BI-01-CO-05/artifacts/professional-R0008/build_bi01_co05_r0008_fullrange_chart_data.py
```

工单cgpterm/runs脚本路径映射为专业仓真实路径；原文件没有改。COMPATIBILITY_COPY.py与原件同字节，COMPATIBILITY_PATCH.diff为0字节；实际运行上列原件路径，没有运行兼容副本，也没有业务参数或API适配。

首次Goal/访问核验UTC `2026-11-02T16:50:34.781390+00:00`（北京时间2026-11-03 00:50:34）。真实脚本运行北京时间2026-11-03 00:52:59.914834至00:56:22.289409（UTC `2026-11-02T16:52:59.914834+00:00`至`2026-11-02T16:56:22.289409+00:00`），单次子进程精确耗时202.351937秒，退出码1。准备、辅助工具纠正和回交均未从总投入剔除，RPC子阶段未单独计时。未重试昂贵计算。

实际顺序：ensure_profile_runtime返回（按原脚本调用已有函数导入worker.beat）；构造OptContext及固定请求；写REQUEST_CONTRACT；调用build_chart_run后日历解析失败。build_big_world_chart_pages和build_board_run均**未调用**。API失败前尚未建立run目录/RunHandle、core manifest或timespan index。

预请求run_id：`BI01_CO05_R0008_FULL_LM_20261103_005320`，只存在请求合同，不冒充成功core。输出根`/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/bi01_co05_r0008_fullrange_chart_data`。原始日志只在该test-run，提交脱敏正文及原日志哈希见EXECUTION_RECEIPT。

# 精确阻断及兼容边界

调用链为`_build_chart_core_run → _default_calendar_resolver → blk_suitable_calendars → read_symbol_calendars_csv → open`。本次`/proc/self/mountinfo`证实`/m3varI`是`192.168.9.79:/m3varI`的NFS挂载，运行中曾观察到`rpc_wait_bit_killable`。这里实证的是日历配置文件I/O失败，并非已验证全部行情源路径。没有新增文件读取重试，也没有用旧CO01错误代替本次证据。

固定业务SOF `GTQH_L1_20210104_20240229`、tlist `gtqh_four`、rb/hc/i、30m、全段`[2021-01-04 00:00:00, 2024-03-01 00:00:00)`、large/mid、小尺度关闭及七个辅助窗均未改。实际成员展开、源品种日历、比例轴/rb背景轴和结束日边界未走到可核阶段，不能用请求声明代替事实。失败来自有权API所需源配置不可读；替换/绕过日历解析或修共享NFS不属本单普通兼容，故依停止条件回交。

# 必须交付项现状

- PAGE_INDEX.csv列全8个原定窗口：全部NOT_GENERATED_NOT_OPENED，无URL、像素查看或静态行情导出。STATIC_EVIDENCE/README.md明确缺件。
- COVERAGE_AND_MISSING.csv列rb/hc/i×KLine_30m/large/mid共9项：首末、行数、空值、重复、缺失、warm-up全部UNKNOWN，无正式切片可读，不能填0。
- FORMAL_FILE_INDEX.csv列9类正式切片及manifest/stats/index缺件，空路径和哈希明确表示未返回，不是现存文件索引。
- PAGE_AND_DATA_IDENTITY.json记录请求身份与实际core未建立，图数同run/core无法证明。没有将请求合同里的预期字段当实际PASS。

旧R2的122个局部文件、旧R5工单、原Pro正文/Return和其他Run没有修改。没有手机操作、对外聊天发送、服务重启、部署或后台监控/唤醒；未在原脚本既有初始化之外额外实施全局注册动作。

# 回原Professional的未完与正常后继

本单技术结果仅交`chatgpt:BI-01-CO-05:professional`，由主控核验运输；Worker未向其他聊天发工具消息。全部承重交付仍未完成：全段主图和七个辅助图实际打开与静态证据、九类正式切片/覆盖/warm-up、真实日期边界及图数同core身份。需先由有权限方恢复上述源配置可访问性；本单未修共享环境，也未承诺恢复时间。恢复后是否重新授权/派发由原角色机制处理，Worker不会自动重试或接单。

本报告是完整失败回交，不是市场背景、关键T、方法、候选或管理接收结论。按工单停止条件结束有限执行；不把失败标成功，不关闭父业务目标。
