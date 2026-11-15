# D003｜C0014 W006 有据后继决定

## 0. Decision

```text
W005 disposition = ACCEPT_STOP_EVIDENCE_WITH_STRICT_LIMITS
W005 reopen       = NO
new successor     = W006
D003              = IN_PROGRESS
```

W006 只处理 W005 直接证实的准备器阶段分类错误，并把历史 trace、local constant、candidate filter 生成、pure evaluator 与真实 kernel 尝试拆成不同证据层。W006 不改变 W004/W005 冻结事实，不放宽 Landlock/seccomp 目标、write contract、resource caps、八 EP、业务禁令或 Gate。

## 1. 唯一 preparation delta

### 1.1 W005错误

```python
trace_lines = all W004 FIOCLEX lines
assert all('EPERM' in line for line in trace_lines)
```

W004 frozen trace 实际含：

```text
line 312  : pre-policy FIOCLEX = 0
line 1509 : post-policy FIOCLEX = -1 EPERM
```

这两个阶段不同，不能使用 universal `all(EPERM)`。

### 1.2 W006 contract

W006 必须把历史 trace 分类成：

```text
HISTORICAL_PRE_POLICY_SUCCESS
HISTORICAL_POST_POLICY_DENIAL
```

并生成：

```text
HISTORICAL_FIOCLEX_PHASE_CLASSIFICATION.json
```

最低要求：

- exact W004 trace SHA256=`b2bcd39ff8886fa65815107bd95f333abef1bcb0a1ea69bb20010abc24b2c959`；
- line312 exact success文本存在；
- line1509 exact EPERM文本存在；
- 两者均保存但不混同；
- 不出现 `all FIOCLEX must be EPERM` 或等价逻辑；
- 历史 trace 分类只证明 W004 历史，不替代 candidate filter static evaluation 或 W006 kernel evidence。

若 exact source/line/hash不一致，STOP，不“修正”W004原件。

## 2. 分层 preparation pipeline

W006 必须把准备过程拆开，至少形成以下独立阶段和产物：

### P0｜fresh binding与历史输入核验

输出：

```text
W006_BINDING.json
CONTROLLER_SENTINEL_PRECONFIRMATION.json
HISTORICAL_FIOCLEX_PHASE_CLASSIFICATION.json
```

### P1｜local constant 与 ABI layout

输出：

```text
FIOCLEX_LOCAL_CONSTANT_VERIFICATION.json
SECCOMP_DATA_LAYOUT_VERIFICATION.json
```

要求：本机 `termios/header` 独立来源一致；expected `0x5451`只作参考，本机值为权威。该阶段不安装filter。

### P2｜fresh runtime/launcher/filter generation

输出：

```text
PARENT_RUNTIME_BINDING_DELTA.json
SECCOMP_IOCTL_FILTER_DELTA.json
new runtime.py
new landlock_launcher.py
```

要求：

- 使用 **fresh W006 actual root、holder PID/startticks/inode**；
- 不从W005硬编码`246047/47679582`或W004硬编码值；
- runtime保持显式`O_RDONLY /dev/null` stdin；
- launcher inherited-FD规则不放宽；
- only verified `FIOCLEX` request ALLOW，all other ioctl EPERM；
- non-ioctl、arch、x32、PR_SET_NAME、network与metadata policy保持W004语义；
- Landlock write allow path only W006 root。

### P3｜pure static evaluator

输出：

```text
SECCOMP_FILTER_STATIC_EVALUATION.json
```

至少验证：

```text
x86_64 ioctl(FIOCLEX)             => ALLOW
x86_64 ioctl(FIONCLEX)            => EPERM
arbitrary ioctl                   => EPERM
request high32 nonzero            => EPERM
existing denied socket            => EPERM
ordinary allowed syscall          => ALLOW
x32 syscall bit                   => EPERM
wrong arch                        => KILL
PR_SET_NAME                       => EPERM
other allowed prctl               => ALLOW
all jump targets in bounds
all paths explicit terminal
non-ioctl semantics equivalent to W004
```

P3 PASS 之前不得启动 kernel launcher。

### P4｜single actual R0-A1

只有 P0–P3 全部 PASS 后，才允许一次实际 launcher/probe。出现新的 bootstrap/filter/kernel/probe问题立即STOP，不修改后重试。

## 3. Fresh physical binding

W006：

- 沿用原W1物理聊天，不新建聊天；
- 重新核actual owner/thread/session/model/effort/cwd/idle/no-writer；
- 获取fresh D003 writer lock并证明竞争失败；
- 使用独立root：`.../D003/W006`；
- W002/W003/W004/W005 roots与原件只读冻结；
- W005 lock/session/turn/资格/command不延续；
- actual HOME/CODEX_HOME保持不变，本任务新增写入为0；
- 所有任务tmp/cache/config/log/source/build/artifact只在W006 root。

## 4. Controller preconfirmation

派发前只读确认以下精确outside sentinel不存在：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/.W006-deny-outside-C0014-259834ad
```

只允许有界`lstat`/等价检查；不得create/write/delete。receipt进入W006 binding。其他shared/HOME/CODEX/symlink目标由W006在policy前只读核不存在。

## 5. Single actual attempt

P3 static PASS后只允许一次R0-A1：

1. parent stdin显式O_RDONLY `/dev/null`；
2. fresh lock guard/inherited-FD规则生效；
3. NNP/Landlock/seccomp实际安装；
4. `FIOCLEX`实际成功并有`F_GETFD & FD_CLOEXEC`证据；
5. inside/outside/shared/HOME/CODEX/child/grandchild/symlink/network九项probe；
6. full write trace中所有successful descriptor write可映射路径。

遇到另一bootstrap ioctl/request或其他compatibility缺口：STOP，不扩大allowlist、不自动修第二次。

## 6. Recovery Gate

只有R0-A PASS才进入R0-B；只有R0-A/B PASS才进入R0-C。四项同时PASS才进入staged construction：

```text
WRITE_CONFINEMENT_PASS
OFFLINE_CLOSURE_PASS
FOUR_BUDGETS_KNOWN_WITHIN_CAP
CONTINUOUS_MONITORS_PASS
```

否则：

```text
PREFLIGHT_STOP
```

不自动重试。

## 7. Unchanged caps

```text
new disk       <= 2 GiB
peak RSS       <= 4 GiB
post-preflight <= 25 min
new files      <= 50,000
outside writes = 0
scenario runs  = 0
```

## 8. Unchanged prohibitions

- 不运行single/partial/full scenario；
- 不运行normal；
- 不运行DBA/wrapper/native reader；
- 不生成current/production O/C/A/D业务材料；
- 不访问或修改production material；
- 不写shared checkout；
- 不修改production lifecycle语义或旧test assertion；
- 不联网、下载、安装依赖；
- 不push源码；
- 不把history/static/kernel/compile结果解释成业务`SUPPORTS/COUNTERS`。

## 9. Conditional eight EP continuation

仅四PASS后，按原D003合同建设：

```text
EP-WALL-SHARED-01..03
EP-SCENARIO-01..05
```

完整9/18/22 fixture只物化和静态parse/count/order/hash；不得送入production decoder/lifecycle。允许的compile-only和direct synthetic serialization须在cap与零外写内。

## 10. Stop routing

| 新事实 | 处理 |
|---|---|
| historical trace SHA/两阶段分类不一致 | STOP before generation；不改历史原件 |
| local FIOCLEX/layout不一致 | STOP before filter generation |
| fresh binding硬编码或static delta超范围 | STOP before evaluator |
| pure evaluator任一case/等价/jump失败 | STOP before kernel |
| kernel/bootstrap/probe失败 | STOP，保留trace，不扩allowlist |
| R0-A PASS但closure不闭合 | STOP，不拼resolver |
| R0-A/B PASS但预算/monitor unknown或超cap | STOP，不进入EP |
| 四PASS后EP局部失败 | 保留独立满足EP，禁止scenario |
| 八EP全部满足 | 回E1消费；仅可建议action `ELIGIBLE_WITH_LIMITS`，G-RUN仍由manager决定 |

## 11. Parent boundary

签发W006不改变：

```text
three parent questions = OPEN
H3                     = NOT AVAILABLE
G-RUN                   = NOT PASSED
parent task             = INCOMPLETE
```

W006正式Return先回原E1；只有E1消费后才能更新D003或向manager作最终/部分回交。
