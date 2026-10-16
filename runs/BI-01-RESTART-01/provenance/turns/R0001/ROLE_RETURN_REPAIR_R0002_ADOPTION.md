# R0001 ROLE_RETURN R0002 修复采用说明

## 原件

- 不可变历史：`daowei2026/observe-iterate@46119a8e0030b4c3597634735cbe5d22ad3a0ac7:runs/BI-01-RESTART-01/provenance/turns/R0001/ROLE_RETURN.json::full`
- 原件缺少 `question_work_ref`，其余 R0001 work / invocation / token 与管理实质保留。

## 修复件

- 旁路审计件：`runs/BI-01-RESTART-01/provenance/turns/R0001/ROLE_RETURN_REPAIR_R0002.json`
- 当前规范路径修正版：`runs/BI-01-RESTART-01/provenance/turns/R0001/ROLE_RETURN.json`
- 两份修正版字节应一致。
- 唯一新增字段：
  `question_work_ref = github:daowei2026/observe-iterate@46119a8e0030b4c3597634735cbe5d22ad3a0ac7:runs/BI-01-RESTART-01/provenance/turns/R0001/QUESTION_WORK_RETURN.json::full`

## 采用关系

操作端在新的修复提交中，将修复件内容物化到当前规范路径 `ROLE_RETURN.json`，以便锁定的 `bi01_run_gate.py after-return` 读取；同时保留旁路审计件。Git 历史中的原件仍由 exact commit `46119a8e0030b4c3597634735cbe5d22ad3a0ac7` 唯一定位，禁止重写或伪造该提交。

这不是重发 R0001，不是重做 M-START，不改变 R0001 的业务结论、Gate 状态或身份。
