[OI-U2-F-OBS-20261118-01-C0027]
invocation_token=7452296d205847129e38591d6f497f5f

你是本Run已真实绑定的独立Skill执行Chat `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`（FOBS-1119-E2）。这是同D006／WI-E-R1／M-E-R1的合法接续，现完整回交你原C0026签发W009的真实结果。请按当前已采用原E Skill和内部Workflow消费、判断与形成后继。不是新D，不重派旧W。专业Workflow/Skill仍为observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288；Owner重启原文及FRP Haskell/TIS Python来源补充保持有效。

## 准确来源与实际回交
- 当前delegation_ref：daowei2026/observe-iterate@08988fc1f2e028caaf3bac40f2d557dddc2293f2:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D006/DELEGATION.json
- 你原C0026 Return：daowei2026/observe-iterate@49469253f29f119c8d0e2c32e67f4cf4058b3538:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0026/PRO_RETURN.json
- 原W009 ORDER.json：daowei2026/observe-iterate@320425cd9892294409135acea5657f6fdacf2b17:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W009/ORDER.json
- 原W009 ORDER.md：daowei2026/observe-iterate@25134e058ab944a2e5f1a40684790b4b4c2b49ef:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W009/ORDER.md
- 原Worker正式Return：daowei2026/observe-iterate@ec7a6d4f79af4fbc60ec02508eeab01aa61cc480:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W009/WORKER_RETURN.json
- 原事实报告：daowei2026/observe-iterate@89d766facf9956e754f7cdab19073d5a79bd167b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W009/FACT_REPORT.md

主控已逐项核对正式Return manifest所列必要原件正文、Git blob和SHA256，validate-worker-return及route-return通过，合法收件对象为原executor:E2。原Worker实际执行及必要签认两turn均已结束，真实idle；workspace租约已释放并独立核free，当前无Worker在途。此为运输和物理状态事实，不代替专业分类。

## 原Worker完整FACT_REPORT.md（逐字）

```markdown
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
```

## 原Worker正式WORKER_RETURN.json（逐字）

```json
{
  "schema": "longrun-worker-return/v2",
  "run_id": "OI-U2-F-OBS-20261118-01",
  "work_order_id": "W009",
  "order_ref": "daowei2026/observe-iterate@320425cd9892294409135acea5657f6fdacf2b17:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W009/ORDER.json",
  "worker": "codex:OI-U2-F-OBS-20261118-01:worker:W1",
  "return_to": "chatgpt:OI-U2-F-OBS-20261118-01:executor:E2",
  "outcome": "STOP",
  "result_ref": "daowei2026/observe-iterate@89d766facf9956e754f7cdab19073d5a79bd167b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W009/FACT_REPORT.md",
  "missing": [
    "第7关origin probe失败：260个已加载mquant模块中165个实际来源解析到候选mquant根外，分类DEDICATED_RUNTIME_MIXED_MQUANT_ORIGINS，不能证明单一候选运行来源",
    "候选入口、TIS四目标字节、候选TIS所需包路径及FRP元数据锁定声明已通过；整体import closure仍未准入，未修补候选或拼接来源",
    "D未启动（0次/无退出码）；未进入第8.1重新核原D/C3 hash的条件分支，也未执行原D",
    "F未构造，fields.json未检查；候选HTML、definition_run_report、prepared_tables和plot_data均未生成",
    "E3图接受、E4/W2准入和D006/E业务完成均未发生"
  ],
  "manifest": {
    "FACT_REPORT.md": {
      "ref": "daowei2026/observe-iterate@89d766facf9956e754f7cdab19073d5a79bd167b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W009/FACT_REPORT.md",
      "sha256": "0f1b39aca7b92d17a84c68979b154b5297bd00aa2c90e9310973a9181cff1473"
    },
    "candidate_entry_and_provenance.json": {
      "ref": "daowei2026/observe-iterate@89d766facf9956e754f7cdab19073d5a79bd167b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W009/candidate_entry_and_provenance.json",
      "sha256": "9adb6f1e1c1d13074b2eb3f593c5fd940f4e6366b740376ba4b95cfb86a8a402"
    },
    "candidate_locked_source_checks.json": {
      "ref": "daowei2026/observe-iterate@89d766facf9956e754f7cdab19073d5a79bd167b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W009/candidate_locked_source_checks.json",
      "sha256": "978ff9278c43a4bdffc8e478c2120283bd2a4169ef0e893a1ec2d945ff4dc804"
    },
    "dedicated_runtime_provenance.json": {
      "ref": "daowei2026/observe-iterate@89d766facf9956e754f7cdab19073d5a79bd167b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W009/dedicated_runtime_provenance.json",
      "sha256": "235419741c0ba9b2acfc81452d647825d287f503c71c2a086c6057325107b221"
    },
    "runtime_gate_decision.json": {
      "ref": "daowei2026/observe-iterate@89d766facf9956e754f7cdab19073d5a79bd167b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W009/runtime_gate_decision.json",
      "sha256": "34d9ca1cf959ce6fde131e29ac5f341bddfa4e4e8f1fb4faa4bdac5d1e7010ae"
    },
    "execution_receipt.json": {
      "ref": "daowei2026/observe-iterate@89d766facf9956e754f7cdab19073d5a79bd167b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W009/execution_receipt.json",
      "sha256": "464aaedc052413dfbdff2d44f595642455b69d5a95de0cbbaa704e477eed644c"
    },
    "origin_probe.py": {
      "ref": "daowei2026/observe-iterate@89d766facf9956e754f7cdab19073d5a79bd167b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W009/origin_probe.py",
      "sha256": "bb9818e91804260cc8975ae34fbe7722d3ecfb8044dfd5e48f147cbee30535d9"
    },
    "logs/origin_probe.dispatch.json": {
      "ref": "daowei2026/observe-iterate@89d766facf9956e754f7cdab19073d5a79bd167b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W009/logs/origin_probe.dispatch.json",
      "sha256": "3539630885be3bf1f700d3a6aed06baa58ad796db7b33e83b67844fddee2f2e5"
    },
    "logs/dedicated_runtime_probe.log": {
      "ref": "daowei2026/observe-iterate@89d766facf9956e754f7cdab19073d5a79bd167b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W009/logs/dedicated_runtime_probe.log",
      "sha256": "c37df0d2e884edec51b384b9fad90d983a128b85d550505315ddce46617b3368"
    },
    "logs/dedicated_runtime_probe.exit_code": {
      "ref": "daowei2026/observe-iterate@89d766facf9956e754f7cdab19073d5a79bd167b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W009/logs/dedicated_runtime_probe.exit_code",
      "sha256": "4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865"
    },
    "logs/existing_entry_environment.log": {
      "ref": "daowei2026/observe-iterate@89d766facf9956e754f7cdab19073d5a79bd167b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W009/logs/existing_entry_environment.log",
      "sha256": "9fc0e3d980f29db3fc69c5259e2e0c152c5cd5224a8942c948ad6340895e9067"
    }
  }
}
```

## 本调用V2正式回交
本C0027按现行V2形成完整原生专业报告和longrun-professional-return/v2：call_id=C0027、role=executor、sender=chatgpt:OI-U2-F-OBS-20261118-01:executor:E2、delegation_ref保持D006、return_to保持原manager。accepted_worker_refs只列实际已核并由你消费的正式Worker Return；本次W009如被消费，使用上述精确wref。issued_order_refs只引用本次由你真实签认的工单，未签发则为空。professional_state与remaining_scope_ref/continuation_ref/owner_request_ref依真实专业状态填写；运输完成不等于E完成。

在本Run分支发布真实形成的原件后，以精确marker/token关联：
`turn complete [OI-U2-F-OBS-20261118-01-C0027] invocation_token=7452296d205847129e38591d6f497f5f`
回复中带本次marker、完整token及正式原件refs；若写入能力缺失，保留完整原文与实际事实，不伪造Git引用。主控仅负责原样运输与合法调度，不新增专业方法、修法或验收条件。

