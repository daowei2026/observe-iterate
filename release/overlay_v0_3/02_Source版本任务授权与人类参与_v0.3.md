# Source、版本、任务授权与人类参与 v0.3

# 1. Source-first，但不是source-only

启动时锁：

```text
Agent canonical candidate version；
Project runtime bundle id；
overlay version；
task-local accepted parent；
最新Owner delta；
required sources；
repo old lock／live head（需要代码时）；
本轮写权和非目标。
```

先读取 current source 形成实质理解，再决定里程碑和 Branch；不能先填大型 Mission Brief。

# 2. Source证据三层

```text
Availability：
  exact source可打开。

Activation：
  实际读了哪些section／anchor并提取什么义务。

Use：
  当前artifact哪个section真正使用。
```

GitHub URL和“文件已在Project里”不等于使用。

# 3. 任务级 Delegation Envelope

```text
PRO_MAY_DECIDE：
  可直接形成current v0。

PRO_MAY_SET_PROVISIONAL：
  可采用可逆首版，必须有version、最强反对和reopen trigger。

HUMAN_CALIBRATION：
  人只校准问题理解、系统形状、轻重缓急和最高影响假设。

OWNER_DECISION_REQUIRED：
  不决定就暂停受影响路径。
```

授权只对当前任务有效。新证据改变Feature、scope、life、history、product或跨仓职责时自动失效。

# 4. Human Calibration

合适触发：

```text
A第一版完整Feature世界／局部业务链形成后；
B冻结RepoFact、to-be定型前；
C第一次形成真实宿主预计形态后；
任何Mission第一处难回退结构选择前；
工作方向明显偏离Owner近期重点时。
```

只提交一页：

```text
我理解Owner真正要什么；
当前系统准备长成什么；
两三个最高影响假设；
推荐；
最强反对；
不介入时可继续的可逆工作。
```

它不是审批或重型Decision Card。

# 5. Owner Decision

只有以下问题需要真正停线：

```text
业务对象、Feature或完整scope；
business life／state owner；
business time／history／correction；
关键method业务语义；
正式public product／consumer claim；
跨仓职责或平台新能力；
高成本难回退选择；
跨用例Agent core晋级。
```

普通类型、容器、局部算法、可逆参数初值和测试组织不应频繁打扰Owner。

# 6. Branch

Branch只在：

```text
主Pro已经完成source-grounded理解；
任务存在可独立推进的对象；
分支有清楚输入、写面、回汇条件；
不会同时改同一canonical artifact。
```

时创建。兄弟Branch决定不自动互相覆盖。

# 7. 本次任务授权与长期规则分开

执行修订 `2026-09-07`：工作面可位于 Owner 指定仓库／分支／目录，或接续已有等价地图。读写工具的权限不等于任务授权；文档写权、地图维护权、业务裁定权、实现代码权、真实数据运行权分别检查。路线复核在已有放权内自主选问题，只有新增高损失取舍才召回 Owner。

任务包 parent 可是已核准完整 ZIP，也可是 exact repo/commit/path。日常正文更新不要求复制版本目录；下游冻结 commit，不跟随 branch latest。工作规则升级需显式记录，旧 Project 上传视图不能被假定已同步；按新入口回读本次修订，必要时更新生成投影。
