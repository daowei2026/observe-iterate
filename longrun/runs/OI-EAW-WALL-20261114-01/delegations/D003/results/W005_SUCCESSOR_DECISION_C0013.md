# D003｜C0013 W005 有据后继决定

## 0. Decision

```text
W004 disposition = ACCEPT_STOP_EVIDENCE_WITH_STRICT_LIMITS
W004 reopen       = NO
new successor     = W005
D003              = IN_PROGRESS
```

W005 只处理 W004 直接证实的单一兼容性缺口：候选 seccomp 以 syscall 粒度拒绝全部 `ioctl`，从而拦截 Python bootstrap 所需的 `FIOCLEX`。W005 不改变 Landlock write rights、write allow root、network/metadata deny、资源上限、八 EP、业务禁令或 Gate。

## 1. 唯一 policy delta

### 1.1 W004事实

```text
ioctl syscall number = 16
request               = FIOCLEX
result                = EPERM
stage                 = second Python bootstrap before probe body
```

### 1.2 W005 contract

在当前 x86_64 Linux 上先用本地 stdlib/header核对 `FIOCLEX` symbolic constant，并与W004 trace一致。预期常量为`0x5451`，但本地核对值为权威；无法核对则STOP。

seccomp BPF语义：

```text
if syscall != ioctl:
    preserve W004 policy exactly

if syscall == ioctl:
    inspect seccomp_data.args[1]
    require upper 32 bits == 0
    if lower 32 bits == verified FIOCLEX:
        ALLOW
    else:
        ERRNO(EPERM)
```

理由：`FIOCLEX`仅设置目标file descriptor的close-on-exec flag，不修改文件内容、目录、metadata或设备状态。只放行该request不会把其他device/terminal/file ioctl纳入许可。

保持：

```text
Landlock IOCTL_DEV handled right
all non-FIOCLEX ioctl denied
PR_SET_NAME denied
network syscalls denied
metadata-mutation syscall deny set unchanged
only W005 root has Landlock write allow rule
```

## 2. Pre-execution static acceptance

launcher实际执行前，W005必须生成：

```text
SECCOMP_IOCTL_FILTER_DELTA.json
SECCOMP_FILTER_STATIC_EVALUATION.json
```

静态 evaluator 至少覆盖：

| synthetic case | expected |
|---|---|
| correct x86_64 + `ioctl(FIOCLEX)` | ALLOW |
| correct x86_64 + `ioctl(FIONCLEX)` | EPERM |
| correct x86_64 + arbitrary ioctl request | EPERM |
| ioctl request high 32 bits nonzero | EPERM |
| existing denied `socket` syscall | EPERM |
| ordinary allowed syscall | ALLOW |
| x32 syscall bit set | EPERM |
| wrong architecture | KILL |

静态 evaluator只能验证BPF逻辑，不能替代kernel安装或probe。若delta超出上述分支、删除安全断言、扩大其他allowlist或无法证明offset/endianness，STOP，不启动launcher。

## 3. Fresh physical binding

W005：

- 沿用原W1物理聊天，不新建聊天；
- 重新核actual owner/thread/session/model/effort/cwd/idle/no-writer；
- 获取fresh D003 writer lock并证明竞争失败；
- 使用独立root：`.../D003/W005`；
- W002/W003/W004 roots与原件只读冻结；
- W004 lock/session/turn/资格/command不延续；
- actual HOME/CODEX_HOME保持不变，本任务新增写入为0；
- 所有任务tmp/cache/config/log/source/build/artifact只在W005 root。

## 4. Controller preconfirmation

派发前只读确认以下精确outside sentinel不存在：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/.W005-deny-outside-C0013-b6e58ef8
```

只允许有界`lstat`/等价检查；不得create/write/delete。receipt进入W005 binding。其他shared/HOME/CODEX/symlink目标由W005在policy前只读核不存在。

## 5. Single actual attempt

通过静态filter验收后，W005只允许一次R0-A1实际launcher/probe尝试。

必须观察：

1. parent stdin保持显式O_RDONLY `/dev/null`；
2. inherited-FD guard不放宽；
3. NNP/Landlock/seccomp真实安装；
4. Python bootstrap `FIOCLEX`实际成功；
5. probe body是否进入；
6. inside/outside/shared/HOME/CODEX/child/grandchild/symlink/network九项probe；
7. full write trace中所有successful descriptor write可映射路径。

若出现另一个blocked ioctl/request或其他bootstrap incompatibility：STOP，保留trace，不扩大allowlist、不自动修第二次。

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
- 不把kernel/static/compile结果解释成业务`SUPPORTS/COUNTERS`。

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
| FIOCLEX本地常量无法核对/BPF静态评价失败 | STOP before launcher |
| FIOCLEX仍被拒或出现另一bootstrap ioctl | STOP，保留trace，不扩allowlist |
| kernel policy/API失败 | STOP，给具体API/errno/right，不笼统写“不支持” |
| probe失败、unknown path或actual outside write | STOP，保留完整证据 |
| R0-A PASS但closure不闭合 | STOP，不拼resolver |
| R0-A/B PASS但预算/monitor unknown或超cap | STOP，不进入EP |
| 四PASS后EP局部失败 | 保留独立满足EP，禁止scenario |
| 八EP全部满足 | 回E1消费；仅可建议action `ELIGIBLE_WITH_LIMITS`，G-RUN仍由manager决定 |

## 11. Parent boundary

签发W005不改变：

```text
three parent questions = OPEN
H3                     = NOT AVAILABLE
G-RUN                   = NOT PASSED
parent task             = INCOMPLETE
```

W005正式Return先回原E1；只有E1消费后才能更新D003或向manager作最终/部分回交。
