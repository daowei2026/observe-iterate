# W009 最小事实报告

身份：`OI-U2-F-OBS-20261118-01 / W009 / D006 / WI-E-R1 / M-E-R1`；Worker `codex:OI-U2-F-OBS-20261118-01:worker:W1`，回原 issuer `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`。活跃工单 `daowei2026/observe-iterate@320425cd9892294409135acea5657f6fdacf2b17:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W009/ORDER.json`；正文 `daowei2026/observe-iterate@25134e058ab944a2e5f1a40684790b4b4c2b49ef:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W009/ORDER.md`。

**状态BLOCKED；总准入FAIL；拟正式Return outcome=STOP。origin probe一次exit1；D启动0次，无D退出码。** 原D/C3、候选、平台和旧W未修改，D006/E未业务完成。

## 本轮纠偏和已有入口

只核验固定候选 `/dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117`，未搜索第二runtime。`runtime/.codex -> /dwdhome/fy/BASE_E6_2_copy/.codex`仅记录，没有跟随或读取其目标，也没有因其存在直接FAIL。

读取候选已有provenance.json（SHA-256=`1b055e926e64bced1cf226a46b25945297fc5ce45206b4246bf81d6df9512473`），并识别候选自带 `fqv.sh` 引用的通用入口 `/dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117/run_in_runtime.py`。其现成行为是设置M3WORKS为candidate/runtime、PATH前置candidate/runtime/edh-universe/bin，sys.path前置candidate/runtime，再runpy执行给定脚本。没有创建或修改任何wrapper、activation、launcher、.pth或sitecustomize。

入口链还引用当前工作区现有run-python.sh。该shell本身写工作区.migration日志，故本W未执行该shell；依据原单第5节允许“按候选已有入口设置其已经声明的进程级环境变量”，仅应用它已声明的m3rc、M3HOST fallback、NO_PROXY、runtime/python-deps和TLS preload设置，日志/cache重定向W009。未发明第二套TIS路径，未新写入口；实际执行的是原先已有的run_in_runtime.py。入口原文、hash和环境依据：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W009/candidate_entry_and_provenance.json`；实际argv：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W009/logs/origin_probe.dispatch.json`；实际环境摘要在probe原件内。未执行fqv.sh的read/rerun/inspect动作。

## 锁定来源与候选TIS完整性

第6.1四个候选文件均存在、不是symlink，并与当前活跃TIS Git仓库本地已有的锁定 `2f460d663d821cf2ba25555eda13e78b697d0767` blob逐字节一致：

- fqv_kline_example.py：0f912c8be7fbd7f2607d93cce9d3974e872f56f6457350cc0db7825d6884b5c5
- CommonPriceTurnGroupCandidates.py：aa25c3bbbf61c23bd0c6f5e37a843bb608784b1511d38980d2b2b97a635d5c5d
- PostTurnGroupDirectionalOrganization.py：869033b2e9f257749dd5f4167ff39495b1c382470760a9cd5af21c170689537b
- CommonTurnGroupValidity.py：6b2809785e344c54ab027337034f3e3916de265c32a0423f78a8892bcf544ce1

第6.2候选自身的blk/gen.py与t0/t1/t2/t3包init均存在且位于候选TIS下，没有从活跃TIS或旧Run补齐。该项PASS只说明指定候选内模块路径具备，不替代实际import closure。

第6.3候选provenance.json的versions.frp明确为锁定 `67711c492da909ed0f044f357beb278abf7fc71c`，其source_commit字段也已记录，因此候选元数据来源判据PASS；没有重建FRP或把元数据判据扩大为本轮业务运行/产品验证。四文件字节/hash、本地Git命令与候选包路径事实：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W009/candidate_locked_source_checks.json`。

## 实际origin probe与首个真实阻断

在现存入口下执行一次原单要求的无业务动作probe，Python `/m3c3/Linux/apps/anaconda3/bin/python`，3.10.13。13个指定模块全部可导入，无import exception；probe期间sys.path前后相同，没有probe代码修改sys.path或package __path__。没有调用make_features、FAO、producer或产品读取。

但是，实际加载的 **260个mquant*模块中165个的物理来源不在同一个候选mquant根**。首个例子：

```text
模块：mquant
__file__：/dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117/runtime/mquant/__init__.py
解析来源：/dwdhome/fy/BASE_E6_2_copy/mquant/__init__.py
期望根：/dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117/runtime/mquant
```

`mquant.apt`、`mquant.frame`等同次probe原件中亦有真实来源记录。这不是仅凭字符串位于候选目录的判断：保留原__file__/__path__/spec.origin以及物理路径解析，能看到已有symlink使部分模块实际取自当前工作区的平台树。原始probe已在同一过程计算物理归属，之后只补齐相同解析值以便回交解释，未再次运行probe或追加环境搜索。

因此第7关FAIL，精确分类：

```text
DEDICATED_RUNTIME_MIXED_MQUANT_ORIGINS
```

这次不是W008的.codex存在性假阳性：Python executable/sys.path未落入.codex目标，已有入口未显示依赖该目标；失败依据是实际import closure的混源。完整260项来源：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W009/dedicated_runtime_provenance.json`。probe日志 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W009/logs/dedicated_runtime_probe.log`，退出码 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W009/logs/dedicated_runtime_probe.exit_code` 为1；环境日志 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W009/logs/existing_entry_environment.log`。probe源码 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W009/origin_probe.py`只是origin采集程序，不含环境接线功能。

## 停止分支和未完成项

按第10节，origin probe失败后立即STOP，不修补runtime、不再探测、不执行D。D=0次/无退出码，无D运行日志；第8.1原D/C3重新hash分支未执行。原D只作工单参考：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/source/observe-iterate/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`，工单声明hash `92ab234df976469c6deb85052251b81633d79994440dccca199120672072433f`，不冒充本轮hash核验。

无候选HTML、definition_run_report、prepared_tables或plot_data。F未构造、fields.json未检查，不推断F产品不存在。实际业务/环境修改无；没有repair.diff，没有复制/生成/软链FQV/TIS文件，没有安装/构建/切版本、overlay或第二runtime搜索，没有读取Q/V产品、调用F producer、启动W2或声明DATA_READY。所有本W显式新增文件均在W009根。

## 回交

最终判据 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W009/runtime_gate_decision.json`；执行回执 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W009/execution_receipt.json`；必要产物路径、字节数和SHA-256见 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W009/MANIFEST.local.json`。未制作审计包或全目录运输包。

`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W009/RETURN_PREPARATION.json`仅为本地准备稿，无新事实已发布Git refs。由主控原样运输必要原件并返回真实ref/hash映射后，同W009签认正式longrun-worker-return/v2回原E2。Worker不决定E3图接受、E4准入或整个E完成；后继专业处理归原E2，D006/E仍未完成。
