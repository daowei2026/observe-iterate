# R0010 专业回交修复要求

- 当前状态：`PROFESSIONAL_DELIVERY_REPAIR_REQUIRED`
- 原 invocation：`BI01-RESTART-01-R0010-c34d5a92b3e194a609f1fb5af1fce098`
- 原专业物理会话：`BI01-RESTART-01-I6-ACTION-CLOSE`
- 通用 after-return：PASS
- Question Work association：FAIL（`CONTINUATION_MISMATCH`）

## 已验证交付

原专业角色已在远端 `run/BI-01-RESTART-01` 形成并推送三个原始 commit，最终为 `c83f3c6f8806e0c9fff64829b41535c18ee9b405`。操作端以非快进 merge 保留原 commit identity，并将其纳入锁定分支；未改写专业业务内容。

## 唯一已证关联缺项

`QUESTION_WORK_RETURN.continuation_ref` 指向 I6 Artifact 的 `#continuation`；`ROLE_RETURN.handoff.instructions_ref` 指向当前任务的 `#route-accept`。现行 Question Work 关联检查要求两者一致，因此返回 `CONTINUATION_MISMATCH`。

## 修复边界

必须由同一个原专业角色决定并重新交付一致的 Return 关系。操作 Codex 不选择替代 locator，不改写专业判断。修复不得重做 I6 业务、不扩大范围、不自签 G6；应基于锁定分支最新 head 普通快进提交，重新提供完整回复、双 Return 和 exact Git locator。

在修复后的 Candidate intake、Return association、reader、binding 与 after-return Gates 全部真实通过前，不得派发管理 G6，不得声明 I6 已被管理接收或 run 已结案。
