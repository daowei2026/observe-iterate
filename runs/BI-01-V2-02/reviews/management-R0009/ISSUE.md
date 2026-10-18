# R0008 Intake 字段格式有限补交

这是一项原管理 DELIVERY_REPAIR，沿用原完整任务和真实 R8 决定，不是新业务安排或重复 EFFORT。

R0008 最终回交 cee668750af0a3ed8f4ae2a95b453bdb881d18ef 的 Intake 与实际检查 1f0128e3c272d6f9c59f6e5f490b64adb407409e 为同一 Git blob 4a38b0a85e273f22bffa8a3cd051ce0cb62f7616。原两 Return/schema/association/Binding、12 正文锚点与7实物及 after-return 校验均通过；手机当前 R8 已真实 answer_complete。

唯一已知机械缺件：runs/BI-01-V2-02/reviews/WORKMAP_INTAKE_CURRENT.json 的 validation_claims 为四条字符串说明，现有 workmap_gate.py 第269行按对象读取 claim.get('evidence')，实际检查退出1，AttributeError: 'str' object has no attribute 'get'。未取得 Gate PASS。

请原管理仅按现有 Intake 合同补齐这一字段格式，保留四条资格限制的语义及可追溯出处。它们是资格说明，不是具有证据/code commit 的正面 validation claim；没有此类实际声明时可沿用既有空 validation_claims 列表，把资格限制保留在原决定或已有 manager context。不要编造证据/测试提交，也不要由操作端代签。保持 R8 技术接收、实际 B 源资格/跨包等价未知、S1 接收、完整 S1/S2/S3 任务、Binding、业务判断、预算/累计有效6与下次8、adoption/continuation 不变。

不重画/重算/重跑 Worker，不新增业务分析；纯格式补交不另计有效结果，不重置原R1起点，不重复 initial EFFORT。保留所有既有回交和失败事实。请在原授权分支发布修复后的 Intake，以及本次简短真实说明与两 Return，以本次准确 invocation/token 回交、turn complete。补交只报告实际完成，QUESTION_WORK_RETURN 仍按原 Binding 使用合法 S1/S2/S3 focus；纯修复不冒称业务完成。随后由操作 Codex 真跑已有 Gate，再接续原执行 Pro 的完整工作。

## 实际检查

```text
python runtime/overlay/tools/workmap_gate.py check --repo . --ref 1f0128e3c272d6f9c59f6e5f490b64adb407409e --base-ref d81b5d606ce991144355106413f67b1f021f1dae --binding runtime/config/WORKMAP_BINDING.json --scope bi01 --actor management_review
exit_code=1
AttributeError: 'str' object has no attribute 'get'
```

已有专业实物与真实管理接收均保留；操作 Codex 未修改管理 Intake 或工具。
