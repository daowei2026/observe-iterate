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
