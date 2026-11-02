# OWNER_PROCESS_FEEDBACK — Professional R0002

## 总裁定

```yaml
owner_process:
  keep: true
  local_modification: EVIDENCE_PLANE_AVAILABILITY_CHECK
  pending_evidence: true
  replacement_proposed: false
core_process_change_triggered: false
```

## 逐步实践反馈

| Owner 初版步骤 | 本轮实际尝试 | 结果 | 分类 |
|---|---|---|---|
| 明确特征范围 | 锁定 `rb/hc/i`、30m、large+mid 的最低成本候选 run | 可开展，但只是文档候选 | `KEEP` |
| 沿当时可知信息推进 | 检查是否有正式 event/confirm/revision 账本 | 当前无可读实物，不能开始 | `PENDING_EVIDENCE` |
| 找大尺度共同背景 | 检查方向覆盖与上游 zig 依据 | 当前未知，未形成背景 | `PENDING_EVIDENCE` |
| 检查中尺度结构 | 检查同一 T 上是否有足够对象 | 当前无合格 T | `PENDING_EVIDENCE` |
| 形成具体用例 | 冻结 H-PRACTICE-01 的观察合同 | 仅假说，不是规律 | `KEEP_AS_HYPOTHESIS` |
| 随新信息更新 | 预定义维持/削弱/撤销/改选 | 尚未执行 | `PENDING_EVIDENCE` |
| 自然挑战 | 预定义 8 类挑战 | 尚未观察 | `KEEP` |
| 反馈方法 | 区分业务、证据、工具和控制面问题 | 已形成局部反馈 | `KEEP` |

## 建议保留

1. 大尺度背景与中尺度用例的两层结构。
2. 两层允许往返，而不是固定 Gate。
3. 用当时可知信息而不是最终历史对象。
4. 中尺度不足时允许合法不适配。
5. 推进能力与反向负担分开。
6. 自然挑战和失败片段必须并列保留。

## 建议局部增加

在第一层之前增加一个薄的、一次性证据平面检查：

```text
same run/core
manifest + FILE_INDEX
formal KLine + large/mid slices
direction provenance
actual/confirm/event/revision semantics
readable visual location
```

它的作用是阻止“没有事件账本却开始讲市场故事”，不是建立长期准入体系。通过后立即进入连续市场过程，不在来源讨论中循环。

同时建议为既有 aidata run 提供标准紧凑导出：

`KEY_T_EVENT_LEDGER`

最小字段：

- symbol / scale / source object id；
- actual position/time；
- confirm or first-visible time；
- event/publication time；
- revision identity；
- direction and provenance；
- predecessor/current-development relation；
- formal source path/hash。

该导出只运输事实，不代替 Professional 形成背景、候选或方法反馈。

## 当前不建议

- 不替换 Owner 当前主问题；
- 不预设“至少 2/3 品种”等固定阈值；
- 不建立统一分数；
- 不把输入资格做成新 Gate 或专用 Agent；
- 不因当前访问失败判定现有对象无业务价值。
