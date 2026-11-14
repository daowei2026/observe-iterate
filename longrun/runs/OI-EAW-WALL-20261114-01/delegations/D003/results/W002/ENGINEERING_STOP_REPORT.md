# W002 工程停止原件

UTC：2026-11-14T18:50:57.319315+00:00；outcome=`STOP`；decision=`PREFLIGHT_STOP`。

停止依 W002 §4、§5.7、§5.8、§10。物理绑定与新锁核对通过，exact FRP base可读；这不能替代依赖、成本和零外写证据。

1. **STOP-CLOSURE-001**：exact stack与BASE overlay使用不同resolver/local packages；compatible offline compiler/resolver/package DB和最小rebuild closure未冻结。GHC global package query不含aeson/reflex/frp/frp-core等所需包；这只说明所查global DB不完整，不代表其他cache不存在。
2. **STOP-CAP-001**：disk/RSS/总wall/files四项未来构建预测未知。浅层缓存元数据不能给出受cap约束的build闭包；`time -v`的version查询数值不是编译成本。任一unknown即必须停止。
3. **STOP-WRITE-001**：bwrap先报network namespace失败，再报uid-map Permission denied。ABI查询显示Landlock=6，但未实现/验证替代隔离，不能当已通过。三类GHC/Cabal元数据进程共有9次成功`O_RDWR`打开`/proc/self/task/*/comm`。原trace没有跟踪`write()`，所以不能证明有实际字节写入，也不能宣称零外写。`writes_outside_WORK_ROOT=unknown`。未再次启动这些工具取证。

保留全部失败退出、stderr、trace、命令、环境和时间/RSS原件。一次rg路径误假定导致静态脚本非零；随后按现场PATH找到并hash真实rg，完成原定三文件有限检索。该修正没有重跑构建、场景或Haskell元数据调用。

Phase1/2均未进入。没有staged source、patch、fixture、local commit、compile报告或serialization测试报告；不制造空patch、假fixture或假PASS来填合同。已完成当前基线、依赖声明、工具hash、写面失败事实和旧测试冲突静态台账。

最小解除条件：固定兼容的现有离线依赖闭包及全量尺寸/hash索引；为实际最小target提供满足2 GiB/4 GiB/25 min/50000文件的可信预算及连续监测；验证覆盖子进程和procfs的零外写隔离/审计。不得由Worker自行把procfs例外、放宽cap、联网安装或共享源码写入视为已获批。

只回原E1：`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`。Linux本地停止证据先由主控逐字出版；之后主控回给真实commit/ref/hash，同一W1再生成W002正式Return。专业接受、D003、scenario G-RUN及父任务完成均未判定。
