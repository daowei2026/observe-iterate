# W004 最小完整事实报告

- Run／工单／父委派：`OI-U2-F-OBS-20261118-01 / W004 / D005`。
- Worker：`codex:OI-U2-F-OBS-20261118-01:worker:W1`；回交：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E1`（原 issuer E1）。
- 活跃工单 JSON：`daowei2026/observe-iterate@1ce39d12f160c624916e7e370692915f3b4af6d3:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W004/ORDER.json`。
- 工单正文：`daowei2026/observe-iterate@a243c56c9450c3a6964ce9b56701c921244821ad:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W004/ORDER.md`。
- 事实状态：**BLOCKED**；正式 Return 待签认的 `outcome=STOP`。
- 这是实际执行后的已知停止结果。D005/E、WI-E、M-E 和父 Run 的业务完成均未发生。

## 1. 实际结果与首个真实阻断

原 D 已由工单指定的 run-local overlay wrapper 执行 **1 次，exit1**；wrapper 同为 1 次、exit1。D 在同一 Python 进程中经 `runpy.run_path(..., run_name="__main__")` 执行；未改 D 的 main 因 `completed=false` 返回1，`SystemExit(1)` 原样传播到 shell。seeder 是单独一次 **exit0**，不与 D 退出码混记。

```text
ModuleNotFoundError: No module named 'mquant.tis.t1'
```

阻断发生于 D main 第679行进入 `CurrSof` 时：SOF 上下文加载 `m3sof.settings.lib3` → `mquant.worker` → `mquant.uplot.multiscale` → 本轮锁定 TIS 的 `blk/gen.py` 第5行 `from ..t1 import *`。完整 traceback 原样保留在 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/output/u2_f_caegraph/definition_run_report.json` 和 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/first_blocker.json`。

原 `make_features` 构造模块已成功导入，但 `make_features(...)` 尚未调用；F 尚未构造，精确 `fields.json` 尚未检查。这不是 F 正式产品不存在的证据，也不是对 F、B、C 或 D 业务语义的否定。

对首个缺失模块只做了锁定 TIS checkout 的 `t1/`、`t1.py` 与 `git ls-tree HEAD t1` 有限静态核对：二个路径均不存在，Git 树查询为空。记录见 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/diagnostics/locked_tis_t1_path_check.json`。没有进行全局搜索、额外平台 import 或诊断运行，未据此推断整个工作区或其他版本不存在该模块。按照首次明确阻断和禁止混用旧 runtime TIS 的条件停止；未接入旧 TIS、未修改业务模块或平台，未进行第二次 D。

## 2. 两个精确 source staging

- observe-iterate：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/source/observe-iterate`；detached HEAD=`f4f0e4b276b1118b779473c1fbe462bc7a64b358`。报告：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/observe_iterate_source_stage_report.json`。
- TIS：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/source/mquant/tis`；detached HEAD=`2f460d663d821cf2ba25555eda13e78b697d0767`。direct SHA fetch 真实成功，没有使用未锁定分支或提交。报告：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/tis_source_stage_report.json`。
- 二者 staging 与所需文件存在性检查均成功；初始和最终 `git status --short` 都为空。组合入口：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/source_stage_report.json`。

## 3. Package boundary 与 overlay

锁定 TIS README 和 `seed_inits.py` 均按原件使用。seeder SHA-256：`77a7b4988da620f40e22dfbe6cfd579a93885def89ab3f0ac2f20299cdfbf3d4`。

- `seed_inits.py` 一次 exit0，生成 **18 个原先缺失的空 `__init__.py`**；完整路径、字节数和 SHA-256：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/tis_generated_inits.json`。
- 没有运行 `pretty-exports.py`，没有修改任何已跟踪 TIS 业务 `.py`；生成的空 init 是 README 声明的构建产物。它们被仓库忽略，空 `git status` 不代表没有这些构建产物。
- Wrapper：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/run_d_with_locked_tis.py`，3128 字节，SHA-256=`ed41811979b745614b8119cec385333dfde6ebdc8d061194b6019f2be1bec484`。
- Overlay 报告：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/module_overlay_report.json`；`ok=true`、预加载 TIS 模块为空。构造模块、F/Q/V 类及 Wave/STCalendar/ScaleTurn 共七个 `find_spec` origin 均为本轮锁定 TIS checkout 的精确路径。
- 上述 origin 核验只覆盖工单列出的七个模块；本次随后出现的 `t1` 依赖阻断真实保留，未将七项通过扩大为所有依赖可用。
- Wrapper 只修改该进程内 `mquant.__path__`，未定义或替换 `make_features`，未复制构造参数，未修改平台 `mquant` 或 D/C3。

## 4. 运行包络与原始日志

- cwd：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/source/observe-iterate`。
- Python：`/m3c3/Linux/apps/anaconda3/bin/python`，`Python 3.10.13`。
- 原入口 `source /dwdhome/fy/BASE_E6_2_copy/m3rc`，沿用 W003 已验证 M3HOST fallback、NO_PROXY、`.runtime/python-deps` 和 TLS preload；TMP/XDG/Numba/Matplotlib 均重定向本 W004 cache。
- Run 开始：`2026-11-19T08:25:24.598042438Z`；结束：`2026-11-19T08:25:40.362410547Z`。
- 完整运行日志：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/logs/w004_run.log`；退出码：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/logs/w004_run.exit_code`；D 派发原始记录：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/logs/D_dispatch.json`；argv/cwd/Python/timestamps 同在 logs。
- 环境日志：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/logs/w004_environment.log`；保留 `nif2` DNS 错误，fallback 后实际已进入 overlay 和 D，它不是本次首个最终阻断。
- Seeder stdout/stderr/环境日志和退出码均在 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/logs/tis_seed_*`。
- 没有 Landlock、namespace、mount、sudo、平台 patch 或独立 SemLock probe；没有 producer 重跑和 Q/V 产品数据读取。原构造模块按锁定代码导入 F/Q/V 类，不等于读取 Q/V 结果。

## 5. 实际修改与最终源码

D/C3/TIS 已跟踪业务源均未修改：

- D：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/source/observe-iterate/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`，原提交 `f4f0e4b276b1118b779473c1fbe462bc7a64b358`，SHA-256 `92ab234df976469c6deb85052251b81633d79994440dccca199120672072433f`。
- C3：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/source/observe-iterate/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`，原件精确 ref 为 `daowei2026/observe-iterate@508d494c964d5dabeaa1e7ea17bef908f749e9c8:longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`，SHA-256 `798042296f88ff5747a0248a81902953550fe39e4fa18337e8fdcfe9557877b7`。
- TIS 业务源目录与锁定提交见第2节；全部声明源文件路径／字节数／hash及未变核对：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/source_final_verification.json`。
- `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/repair.diff`、`observe_iterate_final.diff`、`tis_final.diff` 均0字节。

本轮新增的是两个 run-local checkout、18空 init、namespace／环境／日志接线脚本和事实证据文件；完整接线正文独立保留，不能把“业务 diff 为零”写成“没有任何新文件”。接线清单见 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/actual_changes.json`。没有修改或清理 W001–W003，没有推送 source checkout 或写远端记录。

## 6. 产物与未完成项

- 候选 HTML：**未生成**（C2 preview 仅为输入原件）。
- `definition_run_report.json`：**已生成**，路径 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/output/u2_f_caegraph/definition_run_report.json`，`completed=false`。
- `prepared_tables/`、`plot_data/`：均未生成。
- make_features 未调用、F 未构造、fields.json 未检查、F 正式表未读。
- 未调用 `f.rerun()` 或全历史 producer；未读取 Q/V 产品数据。
- E3 未开始／未接受图；E4 正式取数未准入；无正式导出工单，`DATA_READY=false`。
- Worker 不作专业图接受判断，D005/E 业务未完成。结果继续回原 E1，由其消费此新阻断。

## 7. Semaphore 事实

前后均只读记录 `/dev/shm/sem.*` 的名称／属主／组／mode／size／mtime／inode：

- `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/logs/dev_shm_sem.before.tsv`：0字节，快照命令exit0。
- `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/logs/dev_shm_sem.after.tsv`：0字节，快照命令exit0。

没有手工创建测试 semaphore、没有删除运行前或无法归属对象，没有观察到端点残留。空快照不证明进程存续期间没有临时创建并正常删除 semaphore；这不是逐次IPC事件审计。机器说明：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/semaphore_audit.json`。

## 8. 权限、运输与后继

授权与 Binding 逐字匹配证据：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/authority_validation.json`；持久写面进一步限定 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/**`，D 进程树临时 `sem.*` 继续使用原授权限制。不建立 Goal、计划休眠、后台唤醒或新执行器，不改本轮业务/图/位置语义。

本轮本地最小完整证据列表见 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/MANIFEST.local.json`；正文、精确本地路径、字节数和SHA-256统一保存在 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/TRANSPORT_PAYLOAD.json`，运输包与证据哈希索引见 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/SHA256SUMS`。Git/cache和实时状态投影不作为报告原件混入运输正文；原始已锁定输入可沿用清单中真实存在的精确 refs。

`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W004/RETURN_PREPARATION.json` 是本地准备稿，**不是已发布或正式 Worker Return**。事实 `BLOCKED` 对应拟签认 `outcome=STOP`。待主控原样发布完整证据并返回真实 ref/hash 映射后，同一 W004 下核验并生成正式 `WORKER_RETURN.json`；不伪造未来提交，不重跑 D、producer 或诊断。主控负责运输，专业判断归原 E1。
