# D003｜Phase-0 Recovery Plan（C0010）

> purpose：解除 W002 已证明的三个 Phase-0 blocker；不重复 W002，不放宽 D003 cap，不执行 scenario action。  
> candidate order：`W003`  
> candidate work root：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D003/W003`

## 1. 恢复对象

W002 已把阻断精确收敛为：

```text
B1 compatible offline closure 未固定
B2 disk / RSS / wall / files 四项预测 unknown
B3 全子进程 writes outside actual root = unknown
```

W003 只在新方法能够直接区分 B1～B3 时继续。不得重做：

- bwrap 两个已失败 probe；
- 不含 write-family 的旧 metadata trace；
- 仅查询版本后把结果当 compile 预算；
- 浅层 cache index后把 closure写成已闭合；
- W002 原件、路径或锁的复用／覆盖。

## 2. R0-A｜真正的 write confinement 与全写审计

### 2.1 Run-local Landlock launcher candidate

W002 已核 Linux Landlock ABI=6，但没有实现 enforcement。W003 可在自身 root 内用 Python `-I -S -B` + `ctypes` 构造最小 launcher；不编译二进制，不安装包。

launcher 的唯一目标：

- 只限制 write/create/remove/rename/refer/truncate 等文件系统写能力；
- 允许全局读取；
- 唯一允许写路径为规范化 `W003 WORK_ROOT`；
- `PR_SET_NO_NEW_PRIVS` 后 restrict self，再 `execve` 子进程；
- 子进程继承 restriction；
- 不为 `/proc`、`/tmp`、HOME、cache或 shared repo增加写例外。

该 launcher 本身不是项目源码，不进入 FRP patch；它是 Phase-0 audit artifact。

### 2.2 正反 probe

在任何 Haskell metadata／closure命令前：

1. inside-root create/write/rename/remove 必须成功；
2. outside-root sentinel create/write 必须被 kernel拒绝；sentinel路径由主控预先确认不存在，测试不得留下外部文件；
3. shared checkout write probe只能对一个不存在的临时名字尝试并必须在open阶段被拒绝；禁止修改既有文件；
4. child/grandchild继承限制；
5. symlink escape必须失败；
6. launcher和probe全程由 full write trace覆盖。

任一 probe不满足，`RECOVERY_STOP_WRITE_CONFINEMENT`。

### 2.3 Full write trace

使用 `strace -ff -yy` 或等价已绑定工具，至少覆盖：

```text
open/openat/openat2/creat
write/writev/pwrite64/pwritev
mmap/mprotect/msync
truncate/ftruncate
rename/renameat/renameat2
link/symlink/unlink/rmdir/mkdir/mknod
chmod/chown/utime/xattr
fcntl/flock
clone/fork/vfork/execve
network syscalls
```

必须能把每个成功 descriptor write回溯到路径；无法回溯即 unknown并STOP。

特别检查 `/proc/self/task/*/comm`：

- 若仅 O_RDWR open但无成功write，记录 `NO_ACTUAL_WRITE_OBSERVED`；
- 若write被Landlock拒绝且工具仍成功，记录attempt+denial；
- 若成功写入，outside write非零，立即STOP；
- 不得由E1/Worker自行把procfs排除出D003零外写合同。

## 3. R0-B｜单一兼容离线 closure

### 3.1 两个候选不得拼接

```text
Candidate E：exact frp stack.yaml / lts-18.28
Candidate B：BASE overlay / lts-22.24 / observed GHC 9.4.8
```

只能选择一个真实可离线使用的候选。选择必须给：

- resolver/compiler exact version/hash；
- Stack/Cabal/GHC absolute path/hash；
- snapshot/global/local package DB path/hash/size；
- all local package root + exact commit/tree；
- transitive package ids/versions；
- source package→package DB/artifact映射；
- offline/no-network proof；
- proposed dedicated target的最小 rebuild set。

若两候选都不闭合，`RECOVERY_STOP_CLOSURE`；不得把它们的部分信息拼成“兼容环境”。

### 3.2 允许的只读／dry operations

必须在 R0-A confinement 下执行。允许：

- package DB dump/list；
- exact build declaration parse；
- Stack/Cabal dry-run/dependency plan（确实离线且所有写重定向时）；
- 读取既有 comparable target的构建 artifact/log metadata；
- 对明确 package DB/cache/artifact路径做有界索引。

禁止：

- network；
- package install/update；
- build/compile/test；
- 无界 cache扫描；
- 复制接近/超过cap的大型cache来“试”。

## 4. R0-C｜四项非空预算与 enforcement

每项必须同时有：预测值、upper bound、依据、监测器、stop threshold。不能只写“预计很小”。

### disk/files

根据 staged source size、dry-run rebuild set、已存在同 compiler/target artifact size和保守 multiplier给上界。若 comparable artifact不存在或映射不可靠，STOP。

### RSS/wall

优先使用同 compiler、同 package closure、相近 target的真实 `/usr/bin/time -v`/build log；允许采用更大的可比 target作为保守上界。没有可比实测就STOP，不通过版本命令替代。

### continuous enforcement

在进入任何后续 phase前，必须已经验证：

- monotonic deadline；
- process-group RSS monitor；
- root disk/file monitor；
- all child processes纳入；
- threshold触发能杀停process group并保留receipt。

固定cap不变：

```text
new disk       <= 2 GiB
peak RSS       <= 4 GiB
post-preflight <= 25 min
new files      <= 50,000
outside writes = 0
scenario runs  = 0
```

## 5. Phase-0 recovery verdict

只有同时满足：

```text
WRITE_CONFINEMENT_PASS
OFFLINE_CLOSURE_PASS
FOUR_BUDGETS_KNOWN_WITHIN_CAP
CONTINUOUS_MONITORS_PASS
```

才可写：

```text
ELIGIBLE_FOR_STAGED_CONSTRUCTION
```

任一失败：

```text
PREFLIGHT_STOP
```

并保留成功的独立子结论；不得自动重做或改参数。

## 6. 条件性 Phase 1/2

若且仅若 recovery PASS，W003 才继续当前 D003 原八 EP：

```text
EP-WALL-SHARED-01..03
EP-SCENARIO-01..05
```

要求与 D003/W002 原合同完全相同：

- exact-base clean staged source；
- patch/manifest/local commit仅为Run artifact；
- snapshot直接来自production state；
- one-record-per-firing schema；
- dedicated target只建设；
- fixture精确9/18/22，只做static validation；
- exact-error/transaction synthetic serialization；
- conflict ledger进入target manifest；
- compile-only/serialization仅在cap内；
- full scenario/partial scenario/normal/DBA/wrapper/native-reader均为0。

## 7. W003 结果分流

- recovery STOP：D003继续IN_PROGRESS或由manager有界收束；不重复W003；
- recovery PASS但EP部分：保留合格patch/EP，精确返修唯一EP；
- 八EP全部满足：E1可建议manager接受prerequisite并把action重分类为`ELIGIBLE_WITH_LIMITS`，但 `G-RUN`仍不通过；
- 发现实际outside write：立即STOP，完整报告；不得清理掩盖；
- 需要越出Owner/D003写面：形成具名Owner authorization candidate，不自行执行。
