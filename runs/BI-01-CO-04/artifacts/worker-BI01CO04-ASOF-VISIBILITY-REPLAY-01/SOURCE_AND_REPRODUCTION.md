# 本单来源、实际命令与独立消费

本单所有工作在既有独立clone `/dwdhome/fy/observe-iterate-bi01-co-04-worker-recovery-01`、分支`fy/feature-based-case-observation`完成。只新增本工单唯一目录；旧恢复单、管理面及主控Goal没有改写。

## 原输入与数值路径

`copied/baseline/`是dfdf843b47c03c0121fd7151b72f24adb5d986c0旧包96文件的原字节副本；旧receipt自身仍可独立核验。新原生输入来自原F盘PNV，只导出原实际warm-up及decision窗口所需的2160行；DBA头保持原格式，仅把合法长度/文件边界截成前缀。每个PNV字段的数值payload均与旧run实际消费的已恢复FAO前缀逐字节相等，而非从图或默认参数重造。

参数`task_params.params`为旧任务原字符串；仅把app/store/PNV路由指向owned目录。binary字节固定为原E版本e6.2.0.6的SHA dba166c7fc8d0acf2e56499699b36ac47dd30c923a739e52a7288860fae57450。新identity不替代旧run身份。

数学计算只由原二进制执行。Python只封装输入、限制写面、记录过程、用原Int/Double ADT读取器读回、比较字段和生成receipt。原始失败、临时目录修正前后wrapper、差异patch、实际加载代码/动态库及参考源码均保留。SOURCE_SNAPSHOT明确区分实际已加载文件快照、原二进制和“当前源码参考，未声称编译绑定”；USED_SOURCE_GIT_AUDIT和USED_SOURCE_PATCH只定向覆盖实际加载业务源码，不以一个commit代表全工作区。

读回进程的真实Python模块、动态库及版本另见READER_DEPENDENCY_SNAPSHOT；pydim业务源码字节随包。最初源快照在文件加载后取得，未宣称它已经构成完整qualified observer的预冻结闭包。

## 实际命令

在clone根同步、核原单和12项必读后，按以下次序实际运行。前置脚本有本单现场防重复marker，不应在原现场无条件重跑。

```bash
python scripts/finite_probe.py
python -B scripts/bootstrap_temp_check.py
# 此次在Popen前被错误的stdout-empty断言挡住，没有额外原生调用。
# Owner工程范围澄清后修正断言，保留原脚本及patch，再在同一单核一次TMPDIR：
python -B scripts/bootstrap_temp_check.py
python -B scripts/native_prefix_route.py
PYTHONPATH=/dwdhome/fy/BASE_E6_2 PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 /m3c3/Linux/apps/anaconda3/bin/python scripts/read_native_result.py rb big instrumented
python -B scripts/native_observer_capability.py
PYTHONPATH=/dwdhome/fy/BASE_E6_2 PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 /m3c3/Linux/apps/anaconda3/bin/python scripts/read_native_result.py rb big untraced
python -B scripts/remaining_prefix_matrix.py
```

上例为便读省略固定目录前缀；实际工具命令中的scripts路径均为`runs/BI-01-CO-04/artifacts/worker-BI01CO04-ASOF-VISIBILITY-REPLAY-01/scripts/…`。其余五组分别用`read_native_result.py rb mid fixed_prefix`、`hc big`、`hc mid`、`i big`、`i mid`读回；原生child的逐字命令/cwd/环境白名单/开始结束/返回码在EXECUTION_RECEIPT、BOOTSTRAP_TEMP_CHECK_RECEIPT、NATIVE_PREFIX_ROUTE_EXECUTION、OBSERVER_CAPABILITY_EXECUTION及MATRIX_EXECUTION_RECEIPTS中。

原生计算cwd始终为`/dwdhome/fy/BASE_E6_2`；环境白名单为HOME、PATH、LANG、TZ、M3ROOT、M3WORKS、OMP/OPENBLAS/MKL线程数，修复后加owned TMPDIR。没有导出凭据或完整宿主环境。Landlock只限制文件写面，不修改数学；原记录中的rc=0依实际crash/完成标记另判。

脚本finalize_blocker.py及diagnostics中的中间态是在工程范围澄清前运行的历史记录，已由assess_native_observability.py和最终文件取代。它们不构成当前停止理由。

## 结果与可复核范围

- 六组真实数值：524条；完整恢复前缀524条匹配。原正式96行中95条匹配，i/mid的窗口后event逐条保留解释；总计620个基线行无删除。
- 固定2160-bar rb/big的instrumented与untraced原生输出14条全序元组相等。它不是全逐事件neutrality证明。
- 第一受控调用的tmp失败已解除；第二次的PNV路由缺件已通过同源字节封装解除。
- 当前原生公开API和history输出未提供本单所需的主逐事件观察/input frontier。可知性、生命周期和tail测试因此未完成，不以旧静态字段补造。
- 六类failure fixture实际执行并拒绝坏包；真实包若强改成A也被validator拒绝。fixture只是消费者约束测试，不是模拟生产重放PASS。

## 离线独立验收

在交付目录运行，使用系统Python标准库即可，不需要源盘、numpy或原生引擎：

```bash
python -B scripts/independent_validator.py
sha256sum -c SHA256SUMS
python -B copied/baseline/scripts/package_receipt.py verify
```

独立validator核最终B出口、真实日志/计算结果、620行对照、缺失known-time保留、on/off结果、fixture、文件集合/hash/bytes/CSV行数。它通过只意味着**B出口实物完整可核**，不代表A资格。

PACKAGE_RECEIPT逐文件记来源、SHA256、bytes、CSV行数及业务时间（适用时）、生成/封装时间、工具/版本、copied/wrapper-only/recomputed分类和verification status。receipt与SHA256SUMS排除自身循环：receipt由外层seal固定，seal自身由Git blob/commit固定。现场账本和临时控制marker仅在gitignored `.runtime/`，不进入正式包。
