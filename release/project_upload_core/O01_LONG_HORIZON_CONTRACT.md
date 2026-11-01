# 共享长程执行合同 v0.3

# 1. 一个任务不是一次回答

默认外层：

```text
理解任务与材料义务
→ 形成第一份正向核心产物
→ 主动找漏
→ 下游／实现者理解探针
→ 独立挑战
→ 修订或精确回开
→ 阶段性 handoff
→ 下一块工作
→ 整体综合与完成判断。
```

每个阶段允许反复，不预设“一阶段一轮”。

# 2. 四种推进策略

## `PRECONDITION_LOCK`

只锁 authority、scope、parent、repo tuple、写权和必读 source。没有锁好时不做主体。

## `COARSE_TO_FINE`

先形成完整面，再挑承重结点深挖，防止第一个局部写得极细而漏掉其他 Feature／Action／product。

## `LOCAL_CLOSURE`

对会迫使下游裁业务或主要架构的结点闭合到唯一可执行的 current／provisional contract。

## `DELAYED_RESCAN`

新约束出现后，回扫已经形成的受影响 Feature、Action、method、state、product和下游handoff，不只修最先暴露的字段。

Agent 每轮可以组合使用，但要说明本轮为什么采用这一种。

# 3. 每轮输出顺序

```text
A. 本轮真正形成的核心业务／工程／实现产物；
B. 它怎样形成及用了哪些source；
C. 与上一版的实质变化；
D. 仍然缺什么以及影响范围；
E. 需要回开哪里或谁；
F. 最后才列Harness、风险和非主张。
```

不得先交大量 audit metadata、禁令、manifest 和形式化检查。

# 4. 第二视角的触发

不强制每轮对打。以下情况必须引入实现者探针或独立挑战：

```text
第一份连贯核心候选形成；
准备交给下一Mission；
实现者仍能指出业务／架构歧义；
finding可能是横切问题；
准备作难回退结构决定；
source／repo事实改变；
工作性质明显升格；
准备宣称阶段完成。
```

# 5. Finding必须闭环

每条 finding 至少说明：

```text
成立、部分成立或不成立；
属于Work Map、Local Contract、RepoFact、Compiler、Host、Platform还是Owner；
证据；
正文实际改在哪里；
影响哪些已有artifact；
是否需要cross-cut rescan；
是否需要re-probe／recompile／reaudit；
恢复点。
```

不能只记为 `known issue` 或“实现时注意”。

# 6. 精确回开

允许：

```text
留在当前局部修；
A LOCAL_CONTRACT；
A MAP_REVISION；
B RepoFact delta；
B Compiler recompile；
C defect convergence；
C interrupted recovery；
Platform backpressure；
Owner Decision。
```

禁止宽泛写“需要进一步讨论”。

# 7. 横切重扫

accepted finding 要选影响范围：

```text
CURRENT_FIELD
CURRENT_ACTION
CURRENT_FEATURE
SIBLING_ACTIONS
METHOD_FAMILY
STATE_AND_HISTORY
WORK_MAP_SUBGRAPH
FORMAL_PRODUCTS_AND_CONSUMERS
CASE_AND_GOLD
DOWNSTREAM_HANDOFF
AGENT_METHOD_OR_HARNESS
```

只重扫受影响面，不 clean-room 重写全包。

# 8. 阶段闭合标准

不是轮数、文件齐全或 Harness 全绿。需要：

```text
正向核心产物存在；
下游不再被迫做未授权业务或中大型架构判断；
required source有Availability／Activation／Use；
关键finding已修正文并re-probe；
剩余事项精确属于工程自由、RepoFact、Source blocker或Owner；
provisional项有version、边界和reopen trigger；
existing-artifact effect已声明。
```

# 9. 里程碑、小结果与离站

里程碑以一个下游可消费结果命名，候选／审查／返修不各算里程碑。每个承重小结果形成第一版后，在离站前接受实质挑战；低风险相邻结果可合并审，不要求每次编辑新开聊天。按 `10_独立审查与下一轮问题选择.md`，独立审查先判断方法和拆法，再结合全图实际进展选下一问题，必要时回修当前问题设定。

同一承重问题默认两次完整循环后强制做收敛裁决；不能自动继续第三次同类打磨，也不能强制 PASS。重复根因可提前触发。Builder 自检不计独立循环，重命名不重置计数。

# 10. 持续正本替代逐轮 ZIP

采用获授权 GitHub 工作面时，按 `09_GitHub持续工作面与版本管理.md` 新建或接续地图；正文稳定路径原位更新，Git 记录版本。地图与当前任务只协调工作，不替代完整合同。Builder 的 NEXT_ACTION 仅为建议；不得由 routine 原样升级为下一轮命令。关键任务卡由独立审查／路线判断签发，提交成功并远端回读后才可投递。

上述执行修订适用于新开或明确接入的长程；不自动改变已锁旧版本任务的使用资格，也不把文档提交当作业务任务完成。
