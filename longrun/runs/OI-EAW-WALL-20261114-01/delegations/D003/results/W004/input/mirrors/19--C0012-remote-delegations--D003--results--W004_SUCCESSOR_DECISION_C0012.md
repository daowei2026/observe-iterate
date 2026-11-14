# D003｜C0012 W004 有据后继决定

## 0. Decision

```text
W003 disposition = ACCEPT_STOP_EVIDENCE_WITH_STRICT_LIMITS
W003 reopen       = NO
new successor     = W004
D003              = IN_PROGRESS
```

W004 的成立理由只有两个已知、可修、可直接验收的执行前置差异：

1. 父 runtime 不再使用 `stdin=subprocess.DEVNULL`，而给 launcher 提供显式 `O_RDONLY /dev/null`；
2. 主控在派发前只读确认具名 outside sentinel 不存在并把回执纳入 actual binding。

其余 R0-A 方法、R0-B/C、四PASS、cap、八EP和禁令完全沿用，不把 W003 STOP 改写成“方法已通过”。

## 1. W003 到 W004 的唯一接线 delta

### 1.1 stdin

W003 实际：

```python
subprocess.Popen(..., stdin=subprocess.DEVNULL, ...)
# child fd0 = O_RDWR /dev/null
```

W004 要求：

```python
stdin_fd = os.open('/dev/null', os.O_RDONLY | os.O_CLOEXEC)
flags = fcntl.fcntl(stdin_fd, fcntl.F_GETFL)
assert flags & os.O_ACCMODE == os.O_RDONLY
try:
    child = subprocess.Popen(..., stdin=stdin_fd, ...)
finally:
    os.close(stdin_fd)
```

launcher继续要求 child fd0只读。不得：

- 接受/豁免`O_RDWR /dev/null`；
- 删除 inherited-FD inspection；
- 在launcher内部静默把任意可写fd0改成只读后继续；
- 复用W003 runtime或在W003目录修改文件。

这样修的是父子接线，而不是降低安全合同。

### 1.2 outside sentinel

主控在派发W004前，只读核：

```text
/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/.W004-deny-outside-C0012-e9ed948d
```

必须：

```text
lstat result = ENOENT / absent
no create
no write
no cleanup needed
```

该回执用于证明负向create测试目标在执行前不存在；不授予该路径写权限，也不预先证明Landlock会拒绝。

shared/HOME/CODEX/symlink负向目标由W004在kernel policy安装前只读核不存在；已存在则STOP，不删除。

## 2. Fresh physical binding

W004：

- 沿用原W1物理聊天，不新建聊天；
- 重新核actual owner/thread/session/model/effort/cwd/idle/no-writer；
- 获取fresh D003 writer lock并证明竞争失败；
- 使用独立root：`.../D003/W004`；
- W002/W003 root与原件只读冻结；
- W003 lock/session/turn/资格/command不延续；
- 真实HOME/CODEX_HOME保持不变，本任务新增写入为0；
- 所有任务tmp/cache/config/log/source/build/artifact只在W004 root。

## 3. Recovery Gate

W004依次执行：

```text
R0-A corrected read-only stdin + kernel confinement/probes/full trace
→ R0-B exactly one compatible offline closure
→ R0-C four non-null budgets + continuous monitors
→ only if four PASS: staged eight EP construction/limited validation
```

四项同时PASS：

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

## 4. Unchanged caps

```text
new disk       <= 2 GiB
peak RSS       <= 4 GiB
post-preflight <= 25 min
new files      <= 50,000
outside writes = 0
scenario runs  = 0
```

## 5. Unchanged prohibitions

- 不运行 single/partial/full scenario；
- 不运行 normal；
- 不运行 DBA/wrapper/native reader；
- 不生成 current business O/C/A/D evidence；
- 不访问/修改 production material；
- 不写 shared checkout；
- 不修改 production lifecycle语义或旧test assertion；
- 不联网、下载、安装依赖；
- 不push源码；
- 不把compile/schema/static ledger解释成业务SUPPORTS/COUNTERS。

## 6. W004 stop routing

| 新事实 | 处理 |
|---|---|
| read-only fd0仍不成立 | STOP，保存parent/child FD证据；不再自动改接线 |
| launcher进入policy但ABI/rule/seccomp失败 | STOP，准确记kernel/API事实；不得笼统写“不支持” |
| probe任一失败/路径unknown/actual outside write | STOP；外写证据完整保留 |
| R0-A PASS、closure不闭合 | STOP；不拼接resolver，不进入R0-C/EP |
| R0-A/B PASS、预算或monitor unknown/超cap | STOP；不进入EP |
| 四PASS、某EP局部失败 | 保留独立满足EP，停止或继续其他不依赖合法EP；不运行scenario |
| 八EP全部满足 | 回E1专业消费；只可建议action `ELIGIBLE_WITH_LIMITS`，G-RUN仍由manager决定 |

## 7. D003/parent boundary

签发W004不改变：

```text
three parent questions = OPEN
H3                     = NOT AVAILABLE
G-RUN                   = NOT PASSED
parent task             = INCOMPLETE
```

W004正式Return必须先回原E1；只有E1消费后才能更新D003状态或向manager作最终/部分回交。
