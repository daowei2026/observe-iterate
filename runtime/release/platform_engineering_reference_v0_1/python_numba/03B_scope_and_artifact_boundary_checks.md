# 03B scope and artifact boundary checks

## 0. 用途

这份文档收录 pre-L0 review checks 中，与任务范围、artifact 一致性、wrapper 决议和默认输出边界最相关的规则。


## 1. 规则目录

### PCHK-003 `case_ids_deferred` 默认只影响验证优先级，不自动缩实现范围

- 正确解释：
  - `case_ids_recommended_now / case_ids_deferred` 只表达验证优先级
  - 不自动表达实现范围缩小
- 程序性检查建议：
  - 若出现 `case_ids_deferred`，但没有附带“只影响验证优先级”的说明，则报警

### PCHK-004 AI 不得自行缩 `wrapper_decision`

- 风险：
  - 本应 `repo_wrapper_now` 的对象被静默做成 core-only
- 程序性检查建议：
  - 若 preflight 写了 `repo_wrapper_now`，代码侧必须存在 wrapper class 与 `_impl()`

### PCHK-005 `out_of_scope` 必须显式；实现暂缓不能靠暗示

- 风险：
  - “后续再补 / 当前未覆盖 / 等外部 ready” 这类说法若没有显式落成范围边界，会让 repair 与 review 无法裁决
- 程序性检查建议：
  - 若结果中出现上述措辞，但 task / preflight / report 中没有对应 `out_of_scope / blockers_or_ambiguities`，则报警

### PCHK-006 正式输出、验证轨迹、audit 输出必须分层

- 风险：
  - 为验证方便保留的历史轨迹或 debug 字段被直接混进 repo 默认输出
- 程序性检查建议：
  - stateful / assembler packet 默认白名单应收敛到：
    - `chunk_meta`
    - `carry_out_state`
    - `chunk_end_state`
    - `sparse_events`
    - `chunk_summary`
    - `chunk_checkpoints`
    - `optional_audit_outputs`


## 2. 使用建议

这组规则最适合在：

- preflight
- implement handoff
- review report

之间做跨 artifact 一致性检查。
