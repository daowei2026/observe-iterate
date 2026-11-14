# W002 前置工程事实

`PREFLIGHT_STOP / STOP`。Phase1/2没有获准进入；八项状态见`EP_ACCEPTANCE_MATRIX.md`，没有EP被Worker宣布专业接受。

合法已完成子集：当前exact source核对、15个具名package的声明/commit、工具绝对路径/hash与四个metadata结果、受限写面失败证据、旧测试冲突静态台账、停止和出版交接记录。

待恢复的设计（仅文本设计，没有patch）：snapshot应直接投影production state的wallViews和wallCurrentUpdateBatch，不经C累积或show解析；DTO应将source prediction与actual exact error分开，rejected formal post保持pre且O/C空；独立target未来每scenario独立empty state并保留输入顺序，decode-invalid调用当前decoder/partition路径，不能临时改transaction/ledger语义。

上述能力尚未构造。没有fixture，没有compile/typecheck或serialization测试，没有local commit。缺口来自W002 §5.8对未知cap及§5.7/§8.4对未知外写的强制停止，不通过大范围扫描或试build绕过。

本地目录里的metadata版本查询不是业务计算；它们也不构成compile-only、scenario或业务材料。完整stdout/stderr/strace/time、非零退出和环境均保留。后续按具名最小解除条件回原E1处理；normal/DBA/wrapper/native-reader路线未建设，G-RUN与父任务判断未作。
