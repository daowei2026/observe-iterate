# W006 最小完整事实报告

工单：`OI-U2-F-OBS-20261118-01 / W006 / D006`；Worker：`codex:OI-U2-F-OBS-20261118-01:worker:W1`；回交原 issuer：`chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`。工作项/阶段：`OI-U2-F-OBS-20261118-01-WI-E-R1 / OI-U2-F-OBS-20261118-01-M-E-R1`。

活跃工单：`daowei2026/observe-iterate@ce230480cdbaf0133e3d719e3750c42f52664134:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W006/ORDER.json`。正文：`daowei2026/observe-iterate@548492bbcf524d4a223b1048010dbe8fd8b902b9:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W006/ORDER.md`。

事实状态 **BLOCKED**；拟正式 Return `outcome=STOP`。本次是D006独立执行事实，不沿用D005/W001～W005的结果或执行方案；D006/E业务未完成。

## 实际运行、退出码和当前阻断

D/C3从工单指定的两个既有候选按顺序核hash，选择 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/source/observe-iterate`。当前候选未满足精确D/C3条件，第二候选命中；仅使用其原D/C3，不使用旧输出、overlay、运行日志或业务结论。详情 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/source_selection.json`。

实际D启动 **2次，退出码依次[1,1]**，不是一次；一次最小import定位另外单独计数，不计入D运行：

1. 按原命令名 `python` 首轮执行，实际 `/usr/bin/python`、Python3.12.3。原日志 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/logs/w006_run.log`，exit文件 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/logs/w006_run.exit_code`。在D第20行 `import numpy` 失败，`ModuleNotFoundError: No module named 'numpy'`；尚未进入D main，因此这一轮未生成definition report。
2. 根据工单第五节“可使用现场已配置的等价入口”，读取并加载当前工作区 `m3rc`，现成FY入口为 `/m3c3/Linux/apps/anaconda3/bin/python`、Python3.10.13；没有新建环境、补包或切换项目版本。运行原D，独立日志 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/logs/w006_run_fy_entry.log`、退出码 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/logs/w006_run_fy_entry.exit_code`，exit1。仅正常m3rc将PYTHONPATH配置为当前工作区 `/dwdhome/fy/BASE_E6_2_copy`，没有叠加另一套TIS/Haskell路径，也没有复用旧W的M3HOST fallback、TLS/代理或额外依赖路径接线。

当前FY的真实阻断：

```text
ModuleNotFoundError: No module named 'mquant.tis.frp.fqv_kline_example'
```

D main第677行导入构造模块失败，早于 `make_features` 调用、F构造、fields.json检查和F正式表读取。完整D traceback见 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/output/u2_f_caegraph/definition_run_report.json`。环境日志保留m3rc的nif2 DNS报错；其后Python已进入D main，该提示不是最终缺失构造模块错误的替代解释。

## 一次最小定位与机械修复判断

按工单第6节，在同一当前FY配置只导入指定构造模块一次：失败exit1，`__file__=null`，首个缺失模块为 `mquant.tis.frp.fqv_kline_example`。已加载父包来自当前工作区mquant/tis；精确路径和异常链见 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/constructor_import_report.json`。日志 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/logs/constructor_import.log`；该定位未调用make_features或任何producer，没有额外路径搜索/overlay。

没有证据支持仅修改D/C3就能保证原锁定构造语义；补装/拼装TIS、切换项目版本或混用package都被本W禁止。因此不改D/C3、不创建repair_source、不再跑D，按工单6/7停止回原E2。机器判断依据 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/blocker_and_mechanical_assessment.json`。

## FRP Haskell与TIS Python分开记录

Haskell路径 `/dwdhome/fy/BASE_E6_2_copy/edh-universe/frp/frp` 存在，Git仓库根同该路径，实际HEAD=`37c790c0f456fe3022bb00609219d3e92a5c2f9b`；工单锁定=`67711c492da909ed0f044f357beb278abf7fc71c`，二者不同。仅按工单记录path/HEAD，不切版本、不分析Haskell内容，不把该仓库放入Python import；HEAD不同不证明本次Python错误由它造成。原始命令/退出码见 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/haskell_source_fact.json`。

TIS构造入口是当前FY的 `mquant.tis.frp.fqv_kline_example`；本次无法导入，无法取得模块__file__。没有获取或构造任何另一套TIS checkout/overlay，未把Haskell FRP当作Python TIS。

## 交付实物与修改

- 最终D：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/source/observe-iterate/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`；SHA-256=`92ab234df976469c6deb85052251b81633d79994440dccca199120672072433f`。
- 最终C3：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/source/observe-iterate/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`；SHA-256=`798042296f88ff5747a0248a81902953550fe39e4fa18337e8fdcfe9557877b7`。
- 两者运行前后hash一致；无业务修改，`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/repair.diff`为0字节；`evidence_originals/`只存运行后交付原文副本，不是修复或执行副本。详情 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/source_verification.json`。
- 候选HTML：无。
- definition report：已生成，`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/output/u2_f_caegraph/definition_run_report.json`，completed=false。
- prepared_tables、plot_data：均未生成。F未构造、fields.json未检查；不推断F产品不存在。
- 未调用F producer/rerun、未读取Q/V产品、未启动W2，DATA_READY=false；Worker不判断图通过。

新输出留在 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/**`，没有修改平台、TIS、Haskell、uplot或m3源码，没有建立额外沙箱，没有改W001～W005历史，没有推送或写远端记录。两次D与一次定位的日志/argv/时间分别保留在logs与execution_receipt.json。

## 回交运输

事实JSON `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/facts.json`。完整本地证据清单（路径/字节数/SHA-256） `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/MANIFEST.local.json`，所有正文 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/TRANSPORT_PAYLOAD.json`，哈希索引 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/SHA256SUMS`。

`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W006/RETURN_PREPARATION.json`只是本地准备稿。新事实未冒称已有Git ref；待主控原样发布、独立回读并给真实映射后，同一W006签认正式longrun-worker-return/v2，回原executor:E2。D006/E尚未业务完成。
