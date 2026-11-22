# 已知 Finding Register

## 1. WALL

| finding_id | 内容 | 新 Run 初始状态 | 新 Run 要求 |
|---|---|---|---|
| `WALL-D1-OUTPUT-POSITION-CONSISTENCY` | 正式事件位置与 trace／位置变化发布不一致 | `FIXED_PENDING_RERUN` | 最终远端版本中检查同拍自洽和达到更新尺度的漏发；最新 G 后方可关闭 |
| `WALL-D2-DORMANT-END-SAME-TICK` | 同拍先发 Dormant 再 End | `FIXED_PENDING_RERUN` | 核正常休眠保留、同拍重叠归零、End 时点和原因符合修正合同 |
| `WALL-D3-SAME-PRICE-IDENTITY-RESEGMENTATION` | 同价原位弱化后反复 End 和新建身份 | `DEFERRED_BY_OWNER_SCOPE` | 重新统计发生范围、向下游传递；本轮不强制复杂规则重构 |
| `WALL-D4-SUPPORT-RESTORED-BUT-FAR-END` | 有效支撑恢复后仍累计 far 并结束 | `FIXED_PENDING_RERUN` | 核有支撑 far End、无支撑持续远离、寿命和身份副作用 |

D3 的暂缓依据来自 Owner 当前工作重点：改法复杂且发生比例较低，当前主要先找问题、分析问题并继续下游。它不是 `REJECTED_AS_NON_ISSUE`。

## 2. F

| finding_id | 内容 | 新 Run 初始状态 | 新 Run 要求 |
|---|---|---|---|
| `F-D1-LATE-CONFIRM-ADMISSION-MISMATCH` | actual 起算的短准入期限与上游正常确认节奏不相容，候选组极少 | `PARAMETER_INSTANCE_PROVIDED_PENDING_RERUN` | 用 Owner 新实例完整运行，统计各门转化、迟到对象和新增组的业务质量 |

当前已知：期限主要具有有限观察／历史处理收口作用；旧资料未充分证明它就是要筛选快速确认组，也未给出可接受的排除比例。新 Run 不重复争论旧实例，而检查 Owner 新实例的实际行为。

## 3. 新 finding

新统计发现的条目按 `control-v0.3/03` 状态登记。不能因为已知问题很多而停止完整剖面，也不能因为当前赶下游而降低高置信新 finding 的问题性质。
