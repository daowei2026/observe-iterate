# OWNER_PROCESS_FEEDBACK — Professional R0009

## 当前判断

```yaml
owner_process:
  market_practice_started: false
  keep_named_question: true
  keep_two_layer_process: true
  method_replacement_proposed: false
  operational_adjustment: SAME_PROCESS_CALENDAR_READ_PREFLIGHT
blocker_class: TOOL_DATA_ENVIRONMENT_ACCESS
```

## 本轮实际尝试到哪里

| Owner/当前任务环节 | 实际状态 | 能得到的认识 |
|---|---|---|
| 完整输入范围 | 已由 R0008 固定 | `rb/hc/i`、30m、全段、large+mid、不默认 small 保持有效 |
| 建立同 run/core | 未建立 | 日历解析先失败，不能评价图数链后续能力 |
| 全段主图 | 未生成 | 不能观察大尺度背景 |
| 正式 KLine/large/mid | 未生成 | 不能进行对象、方向或 as-of 核验 |
| 第一层 | 未开始 | 无法评价背景可辨、改变或失效 |
| 第二层 | 未开始 | 无法评价中尺度充分性或候选规律 |
| 自然挑战 | 未开始 | 不能从技术失败推断市场反例 |

## 应保留

1. 全段主图承担大尺度形成与演变；辅助图只帮助阅读。
2. 图与正式数据来自同一 run/core。
3. actual、confirm、event、revision 与观察时点分开。
4. 共同背景与中尺度用例分两层，但允许往返。
5. 允许合法无候选，但必须有市场证据，不能由工具失败推出。

## 一项普通操作调整

在重试昂贵调用前，由**同一目标进程**真实读取必需日历文件，并记录结果。该检查只回答“当前执行依赖能否读取”，不判断市场、不筛候选、不构成新业务 Gate，也不替代正式运行。

最小检查：

```text
open/read exact file
+ bytes/sha256
+ timestamp/exit/stderr
+ current mount source
```

## 不应改变

- 不缩短全段时间范围；
- 不回退至 R0005 的 45 天窗；
- 不默认添加 small；
- 不建立平行数据库或从截图反造；
- 不因 NFS 失败替换 Owner 的两层问题；
- 不把技术 PASS 或恢复证明当作过程实践包。

## 下一次能产生业务价值的起点

不是继续讨论来源，而是：恢复依赖 → 完成同 run/core 图数 → Professional 读取正式字段 → 从第一条合格 as-of T 开始第一层。若恢复必须改变 calendar source 或 resolver，则先显式评估输入身份影响。
