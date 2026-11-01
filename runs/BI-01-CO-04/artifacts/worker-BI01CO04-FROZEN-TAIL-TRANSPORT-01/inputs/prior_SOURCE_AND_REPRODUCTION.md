# 来源、实际执行与复核

## 授权与固定来源

- order_id：BI01CO04-INPUT-RECOVERY-01；work_id：BI-01；run_id：BI-01-CO-04。
- 原单固定来源：daowei2026/observe-iterate@30131cabaeb9354d5f7d49616bbf4baea01dc934:runs/BI-01-CO-04/reviews/management-R0006/WORKER_ORDER.md；SHA256=8ab35241f8bf350f600ccb03adc415ee22698b2bffa8e643cf62daa1dcccc4ea。
- 专业固定版本 b6ccf766dac055a793e75f76b77a73f4cfc74064，动态基线 71bb32486c8c35ae346b8956282ac68622af31b3。六必读完整读取；当前 checkout 字节与固定版本逐项相等，见 evidence/REQUIRED_READS.json。
- 独立 clone：/dwdhome/fy/observe-iterate-bi01-co-04-worker-recovery-01；origin=https://github.com/daowei2026/observe-iterate.git；分支 fy/feature-based-case-observation；未新建业务分支。
- 唯一写面为本目录；.runtime 是本目录下 gitignored 工程账本与执行日志。不改管理文档，不发其他聊天，不操作手机，不动主控 Goal。

## 原运行消费链

实际 source root 为 `/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/fy_owner_1d_30m_20261027/storage_migration_20261101`；行情源为 `/m3varF/BaseData/futures/GTQH_L1_20210104_20240208`。

1. selected_turn_parameters.json 定义 small/mid/big 的展开参数。原 prepare 脚本实际读取该文件，导出 task JSON；六组大中 task 的 SHA 与原 prepared_jobs 匹配，ppid 与 selected/validated 匹配。
2. 原 engine log 的全参数 JSON 与 task.params 逐项相等，state 保存真实命令和 returncode=0；执行器 e6.2.0.6，原记录 SHA256=dba166c7fc8d0acf2e56499699b36ac47dd30c923a739e52a7288860fae57450。
3. 原 validate 脚本通过原 E Int/Double reader 读取 actual2D/confirm2D，逐个 UTI 与价格核对 GTQH 30m；本单重新核 source validated CSV 哈希，未重新运行数值引擎。
4. build_three_turn_plot.py 从 validated CSV 生成每尺度合并 CSV，将 SHA 固定到 ReadOnlyCsvFeature。原 page、run brief、formal stats 的源身份和参数表示仍保留；本单检查消费 CSV 的真实 SHA、每条正式大中 slice 的 `_csv_source_row` 与原合并 CSV 物理行精确匹配。
5. 同一 run 的 board 日志完成，12 个原切片全部成功；本单只复制其中三行情、六大中。原 small 的配置、manifest 元信息与 PNG 图例随历史证据保留，未另行补小尺度数据。
6. 原 node 6153、run 和静态 PNG 的对应由 three_turn_page.json、single_three_turns.fason.txt、原 chart_slice_alignment.json 及原验收报告支撑。Worker 本轮实际打开原 PNG 目视核对其三品种图例与三尺度符号，没有把图当结构化输入。

copied/ 为 byte-for-byte；每次复制前后重新计算源与目标 SHA，必须三者相等。regenerated/ 为从**原计算实际消费的 staging 缓存**及原 validated/合并 CSV 只读导出，不是新开 KLine/数据库取数通道，不修改源路径，不计算转折。source_inputs 的原始 DBA 每字段均保留 hash；三个约247MB的完整日历未整盘复制或完整哈希，交付的是所需 UTI 映射点及其逐文件 hash，原日历版本未冻结是明确限制。

## 实际命令与环境

独立克隆命令：

```bash
git clone --single-branch --branch fy/feature-based-case-observation https://github.com/daowei2026/observe-iterate.git /dwdhome/fy/observe-iterate-bi01-co-04-worker-recovery-01
```

在该 clone 根运行：

```bash
PYTHONPATH=/dwdhome/fy/BASE_E6_2 PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 /m3c3/Linux/apps/anaconda3/bin/python runs/BI-01-CO-04/artifacts/worker-BI01CO04-INPUT-RECOVERY-01/scripts/recover_inputs.py
python runs/BI-01-CO-04/artifacts/worker-BI01CO04-INPUT-RECOVERY-01/scripts/package_receipt.py seal
python runs/BI-01-CO-04/artifacts/worker-BI01CO04-INPUT-RECOVERY-01/scripts/package_receipt.py verify
```

前一命令只适用于原 source/cache 仍可读的现场；消费者独立核包只需最后一命令，无 numpy、pydim、源盘或手机依赖。具体 Python/numpy/pandas 和子仓 checkout/本地 tracked 差异见 evidence/ENVIRONMENT.json，不把一个 aidata SHA 当作全工作区一致证明。

恢复导出开发期间两次本地断言暴露工程问题（set_index 默认丢弃 closeUti；CSV source row 实为首数据行=2 的物理行号），已按原 csv_feature.py 修正并重新完整执行只读导出。没有数值重生，也没有以失败尝试当通过。

## 独立复核与 receipt 封口

PACKAGE_RECEIPT 对所有业务实物、报告、源码、配置及证据列 path/source_path/sha256/bytes/rows/业务首末时间/generated_at/tool/version/copied_or_regenerated/source_run_id/verification_status。不可适用的值为 null，并附原因，不补造旧生成时间。

哈希自引用约定：receipt 不收录自身与 SHA256SUMS；外层 SHA256SUMS 收录 receipt 及其余全部普通文件，自身由 Git blob/commit 固定。verify 会核文件集合、路径边界、逐文件 SHA/bytes/CSV 行数和首末时间，再核外层 seal；不存在以“目录完整”替代文件核验的情况。

时间统计只说明真实测量：任务准备、恢复、校验均属于本单成本；未建立可独立验证的分项时间不写估算。Goal 与账本只属于本有限工单。

## 可交付程度

字节、参数消费及坐标/价格关系已核；时间可知合同、方向关联、对象生命周期和完整 historical build 尚未核。参见 BLOCKER_REPORT。此包可交原 Management 技术接收和定向补件，不能当 P0 全通过直接恢复 Professional 的 as-of 判断。
