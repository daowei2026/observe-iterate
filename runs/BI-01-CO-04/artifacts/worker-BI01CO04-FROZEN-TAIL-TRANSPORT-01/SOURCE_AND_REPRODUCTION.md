# 来源与复现

本单 source root、source run 和读取路线全部取原工单及原 recovery，不使用网页或替代数据库。精确source_path逐字段见SOURCE_IDENTITY_CHECK。

- 行情：`/m3varF/BaseData/futures/GTQH_L1_20210104_20240208/pnv/30m/{rb,hc,i}/{field}.dba`。
- 已核staging：原recovery root下 `turn_staging/cache/BaseData/futures/GTQH_L1_20210104_20240208/fao/prod/KLine/e/c/3/e/0/2/3/0a9cc80a32b85890741475ee0505af8dc/{symbol}/{field}.dba`；每个文件完整hash等于旧SOURCE_INPUTS。其十字段完整8964行逻辑payload与PNV逐字节相等。
- 新输入目录的30个frozen prefix DBA为旧replay输出的原字节复制；完整文件hash与PNV_PREFIX_ROUTE_RECEIPT、SOURCE_SNAPSHOT一致，并逐字段对齐当前PNV的前2160行。三品种原cutoff行从旧market CSV原header与最后物理行2161摘取；原全CSV的SHA与旧PACKAGE_RECEIPT绑定。
- DBA读取为标准库little-endian double/int64，不导入业务运行时。提取器有进程/动态库调用拒绝hook和唯一写面检查；实际源open allowlist恰为30 PNV+30 staging字段+3 staging索引。只写本包。
- 大PNV物理文件不作完整padding哈希。本次`source_sha256_before/after`明确仅覆盖原64-byte header加8964个有效元素（71,776字节），不是49,461,184字节物理全文件hash；`source_full_file_sha256=null`。同时保存exact path、realpath、device/inode/size/mtime_ns/ctime_ns、前后stat、逻辑hash、旧staging全hash、冻结prefix hash和所选69行range payload/offset/hash。符合原单第6.4节的有限range proof，不虚写full hash。
- 实际独立validator使用另一套array解码与代数等价分数公式，不导入提取器；复读63个确切源文件，核所有十字段原range与CSV、完整逻辑payload身份、anchor、endpoint、范围完整性、三文件集合和每个机械指标。离线模式仅依赖本包和Python标准库。

## 准确命令

cwd均为 `/dwdhome/fy/observe-iterate-bi01-co-04-worker-recovery-01`。下列实际命令及环境白名单、UTC起止时间、耗时、退出码、stdout/stderr路径与hash在logs对应JSON内。完整脚本代码和同脚本修正diff均随包；不应在消费者验收时重新提取行情。

```bash
/usr/bin/python -B runs/BI-01-CO-04/artifacts/worker-BI01CO04-FROZEN-TAIL-TRANSPORT-01/scripts/extract_tail.py
/usr/bin/python -B runs/BI-01-CO-04/artifacts/worker-BI01CO04-FROZEN-TAIL-TRANSPORT-01/scripts/extract_tail.py --repair-dba-capacity
/usr/bin/python -B runs/BI-01-CO-04/artifacts/worker-BI01CO04-FROZEN-TAIL-TRANSPORT-01/scripts/validate_tail.py --data-only --live-source
/usr/bin/python -B runs/BI-01-CO-04/artifacts/worker-BI01CO04-FROZEN-TAIL-TRANSPORT-01/scripts/seal_tail.py
/usr/bin/python -B runs/BI-01-CO-04/artifacts/worker-BI01CO04-FROZEN-TAIL-TRANSPORT-01/scripts/validate_tail.py
```

前三条由`record_command.py <label> /usr/bin/python ...`记录执行。第1条rc=1，原断言错误要求physical size==logical size，尚未生成CSV；第2条为已授权的一次必要同脚本修正，rc=0，没有改源、输入窗口、字段、公式或阈值。两次进程终态均确认，没有未知在途动作。

本包入口一次性marker防重复调用；首次失败、原脚本、修正patch及DBA_LAYOUT_CORRECTION全部保留。第3条由初版及最终版validator各作一次真实源核验，均PASS；日志标签分别为independent-live-data-validation和independent-live-final-validator，最终代码hash与真实结果在VALIDATION_RESULT中。封口/归档验收输出保存在本单gitignored `.runtime` 并以最终准确commit回交，避免receipt收录其自身验证输出造成循环hash。

## 独立消费者

```bash
python -B <本包路径>/scripts/validate_tail.py
cd <本包路径>
sha256sum -c SHA256SUMS
```

receipt排除自身与外层SHA256SUMS；外层seal包括receipt和全部其他交付文件但排除自身。Git提交固定seal字节。`.runtime/`为本单工程账本及消费者临时归档目录，明确不进入交付seal。普通文档/脚本为工程编写，原件为copied，行情CSV/range为deterministically_extracted；本单没有recomputed_feature_output。
