[OI-U2-F-OBS-20261118-01-C0026]
invocation_token=55912772627a49c9a9f5946c28146ad0

你是本Run已真实绑定的独立Skill执行Chat `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`（FOBS-1119-E2）。这是同D006／WI-E-R1／M-E-R1的合法接续，现完整回交你原C0025签发W008的真实结果。请按当前已采用原E Skill和内部Workflow消费、判断与形成后继。不是新D，不重派旧W。专业Workflow/Skill仍为observe-iterate@f7e8ff43fabfa11b499e2ce9e62dbc46b1b8b288；Owner重启原文及FRP Haskell/TIS Python来源补充保持有效。

## 准确来源与实际回交
- 当前delegation_ref：daowei2026/observe-iterate@08988fc1f2e028caaf3bac40f2d557dddc2293f2:longrun/runs/OI-U2-F-OBS-20261118-01/delegations/D006/DELEGATION.json
- 你原C0025 Return：daowei2026/observe-iterate@2e08cd05d3a8011c2045127fa74a56b8f394f39a:longrun/runs/OI-U2-F-OBS-20261118-01/calls/C0025/PRO_RETURN.json
- 原W008 ORDER.json：daowei2026/observe-iterate@3916814afc03f39408e4d992efda8a0ddd85f683:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W008/ORDER.json
- 原W008 ORDER.md：daowei2026/observe-iterate@afb179352fe81420f250152d9994148be6c4f267:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W008/ORDER.md
- 原Worker正式Return：daowei2026/observe-iterate@be3f2f9c2102fc182909140234921f7ad3d4457b:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W008/WORKER_RETURN.json
- 原事实报告：daowei2026/observe-iterate@be2c8b96728e15fe4e93ffdb5b6f92a5968b76db:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W008/FACT_REPORT.md

主控已逐项核对正式Return manifest所列必要原件正文、Git blob和SHA256，validate-worker-return及route-return通过，合法收件对象为原executor:E2。原Worker实际执行及必要签认两turn均已结束，真实idle；workspace租约已释放并独立核free，当前无Worker在途。此为运输和物理状态事实，不代替专业分类。

## 原Worker完整FACT_REPORT.md（逐字）

```markdown
# W008 最小事实报告

身份：`OI-U2-F-OBS-20261118-01 / W008 / D006 / WI-E-R1 / M-E-R1`；Worker `codex:OI-U2-F-OBS-20261118-01:worker:W1`，回原 issuer `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`。活跃工单 `daowei2026/observe-iterate@3916814afc03f39408e4d992efda8a0ddd85f683:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W008/ORDER.json`，正文 `daowei2026/observe-iterate@afb179352fe81420f250152d9994148be6c4f267:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W008/ORDER.md`。

**事实状态BLOCKED，拟Return outcome=STOP；总准入FAIL。D启动0次，无D退出码。** 本W执行的是固定候选的逐关核验，未重跑旧W；D006/E业务未完成。

## 首个真实失败与停止依据

唯一候选：`/dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117`，realpath同此路径。候选根、runtime、runtime/mquant、runtime/mquant/tis均存在且不是symlink。

第5.1三层以内有限目录检查遇到：

```text
/dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117/runtime/.codex
  -> /dwdhome/fy/BASE_E6_2_copy/.codex
realpath: /dwdhome/fy/BASE_E6_2_copy/.codex
```

目标位于候选根之外。原单第5.1明确“不跟随离开候选根的symlink；遇到外部symlink只记录并判FAIL”，第10节又规定“任一准入条款失败后不再运行D，也不继续环境探测”。因此在此立即停止，分类为 `DEDICATED_RUNTIME_EXTERNAL_SOURCE_LEAK`。

该分类描述本次观察到的外部symlink结构；未跟随链接、未读目标内容、未执行或导入候选/外部代码，不能解读为本次已发生运行时导入泄漏。

完整必要结构事实：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W008/candidate_inventory.json`。目录检查在首失败处终止，bounded_listing_complete=false，不冒称完成整个候选三层清单。此前列出candidate/provenance.json存在（1217字节），但停止后没有读取其正文，也不判断其缺失或commit内容。

## 原单各分支事实

- 第5.1：FAIL（上述外部symlink）。
- 第5.2候选既有正常入口：NOT_RUN/未检查，不能写成“无入口”。
- 第5.3 TIS四文件与锁定blob的字节/hash核对：NOT_RUN。
- 第5.3 TIS单一完整来源：NOT_RUN。
- 第5.4 FRP锁定provenance：NOT_PROVEN，原因是前置失败后未执行该关，不声称来源记录缺失或锁定不匹配。
- 第6节origin probe：NOT_RUN、0次，无dedicated_runtime_probe.log或dedicated_runtime_provenance.json。
- 第7节D/C3 hash核对及原D执行：NOT_RUN。D=0次，无退出码、无D运行日志。

机器判据：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W008/dedicated_runtime_gate_decision.json`；独立本W回执 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W008/execution_receipt.json`。

## 原件、实物与修改

原D参考路径：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/source/observe-iterate/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`，工单声明SHA-256=`92ab234df976469c6deb85052251b81633d79994440dccca199120672072433f`。本轮未进入第7.1重新hash或执行，不能把声明值当作本轮验证结果。D/C3均未修改。

候选HTML：无。definition_run_report：无。prepared_tables/plot_data：无。F未构造，fields.json未检查，不推断F产品不存在。实际业务或环境修改：无；没有repair.diff。

只在W008根写必要新事实/输入镜像，没有修改候选runtime、当前TIS、固定FRP、D/C3或旧Run。未建设环境、复制/生成/软链FQV文件、创建wrapper/activation/launcher、修改import路径或package路径、切Git版本、安装/构建、调用producer、读取Q/V产品或启动W2。没有第二runtime搜索或后续环境探测。

## 回交原E2

必要产物路径、字节数和SHA-256见 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W008/MANIFEST.local.json`。未制作审计包或全目录运输包。`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W008/RETURN_PREPARATION.json`仅为本地准备稿；新事实目前没有已发布Git refs。由主控原样运输必要原件，形成真实引用后，同W008再签正式longrun-worker-return/v2回原E2；不改原事实、不重跑。E3图接受、E4/W2准入和D006/E业务完成均未发生；后继专业处理归原E2。
```

## 原Worker已签认完整WORKER_RETURN.json（逐字）

```json
{
  "schema": "longrun-worker-return/v2",
  "run_id": "OI-U2-F-OBS-20261118-01",
  "work_order_id": "W008",
  "order_ref": "daowei2026/observe-iterate@3916814afc03f39408e4d992efda8a0ddd85f683:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W008/ORDER.json",
  "worker": "codex:OI-U2-F-OBS-20261118-01:worker:W1",
  "return_to": "chatgpt:OI-U2-F-OBS-20261118-01:executor:E2",
  "outcome": "STOP",
  "missing": [
    "第5.1关遇到候选根外符号链接：/dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117/runtime/.codex -> /dwdhome/fy/BASE_E6_2_copy/.codex；按原单立即FAIL，未跟随外部目标",
    "第5.2既有入口、第5.3 TIS四文件锁定字节/hash与完整性核对均未执行；不能断言入口或目标文件缺失/不匹配",
    "第5.4候选FRP锁定provenance尚未核验，状态NOT_PROVEN；已列出的provenance.json未读取，不声称来源记录缺失",
    "origin probe未运行；D=0次/无退出码，F未构造、fields.json未检查，无HTML或definition_run_report",
    "E3图接受、E4/W2准入和D006/E业务完成均未发生"
  ],
  "result_ref": "daowei2026/observe-iterate@be2c8b96728e15fe4e93ffdb5b6f92a5968b76db:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W008/FACT_REPORT.md",
  "manifest": {
    "FACT_REPORT.md": {
      "ref": "daowei2026/observe-iterate@be2c8b96728e15fe4e93ffdb5b6f92a5968b76db:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W008/FACT_REPORT.md",
      "sha256": "362c3270ab7add1d66c104f92019a4a094c3cf75dc36bc8b10a63225fb9bcfea"
    },
    "candidate_inventory.json": {
      "ref": "daowei2026/observe-iterate@be2c8b96728e15fe4e93ffdb5b6f92a5968b76db:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W008/candidate_inventory.json",
      "sha256": "48bdc9fccbde3df9ea4bca0883ae5b22993a17ab1ad6a235c9c7ae75ded82c6a"
    },
    "dedicated_runtime_gate_decision.json": {
      "ref": "daowei2026/observe-iterate@be2c8b96728e15fe4e93ffdb5b6f92a5968b76db:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W008/dedicated_runtime_gate_decision.json",
      "sha256": "003a4655c713a10635a762b39caa7eaf806856622a4d8db1b8e4b56fd755875d"
    },
    "execution_receipt.json": {
      "ref": "daowei2026/observe-iterate@be2c8b96728e15fe4e93ffdb5b6f92a5968b76db:longrun/runs/OI-U2-F-OBS-20261118-01/worker_results/W008/execution_receipt.json",
      "sha256": "cf4d2812e7decf602923d33262a7a24647154fd48931e31c3b2d823666bb1ca8"
    }
  }
}
```

## 本调用V2正式回交
本C0026按现行V2形成完整原生专业报告和longrun-professional-return/v2：call_id=C0026、role=executor、sender=chatgpt:OI-U2-F-OBS-20261118-01:executor:E2、delegation_ref保持D006、return_to保持原manager。accepted_worker_refs只列实际已核并由你消费的正式Worker Return；本次W008如被消费，使用上述精确wref。issued_order_refs只引用本次由你真实签认的工单，未签发则为空。professional_state与remaining_scope_ref/continuation_ref/owner_request_ref依真实专业状态填写；运输完成不等于E完成。

在本Run分支发布真实形成的原件后，以精确marker/token关联：
`turn complete [OI-U2-F-OBS-20261118-01-C0026] invocation_token=55912772627a49c9a9f5946c28146ad0`
回复中带本次marker、完整token及正式原件refs；若写入能力缺失，保留完整原文与实际事实，不伪造Git引用。主控仅负责原样运输与合法调度，不新增专业方法、修法或验收条件。
