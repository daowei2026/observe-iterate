order_id: BI01CO04-FROZEN-TAIL-TRANSPORT-01
work_id: BI-01
run_id: BI-01-CO-04
issuer_invocation_id: BI01-CO-04-R0010-EFFORT-REASSESS-cad9dec8
return_to: chatgpt:BI-01-CO-04:management

# 冻结行情尾部运输完整回交

**最终出口 A：TAIL_PACKAGE_READY。** 仅表示本单exact tail可交原Management技术接收；未续Professional、未形成业务解释或闭环裁定。

## 固定身份和实际范围

原单全文SHA256为`4da6dfe406fa69790a60da14e44c2174830940c74fbba145f4786933bfe6e2c0`，原单及第3节8项必读的固定commit、原字节和读取范围随REQUIRED_READS/inputs保存。管理采用`c8c6f05442f4e2111528cb3ac7c925dfba60e9a2`，接收输入基线`43223e4a84cbf32c25745ce6b1cbce43c82488ed`，专业规则固定`b6ccf766dac055a793e75f76b77a73f4cfc74064`。未修改R0009冻结实物。

源snapshot为`GTQH_L1_20210104_20240208`，source run为`GTQH_C001_three_turns_20261101_162005`。同一源PNV十字段完整8964行逻辑字节等于旧全hash核定staging，并与旧replay2160行冻结前缀逐字段相等。三anchor的close、UTI和timestamp均等于旧recovery最后一行；anchor UTI均为7448399，原source_row=2159。来源全路径、前后stat、逻辑hash、范围offset/hash和原payload均随SOURCE_IDENTITY_CHECK及evidence交付。预分配容量部分未作full hash，未伪称已作；详见SOURCE_AND_REPRODUCTION。

三CSV首末统一为`2021-09-30T15:00:00+08:00`至exact `2021-10-15T15:00:00+08:00`，首tail为`2021-10-08T09:30:00+08:00`；原行2159–2227，无插值、无end后行情行。三组68个tail timestamp集合完全一致，交集及空差异逐值记录。

## 机械实物

下表return为原始比例，不是百分点。CSV还保留OHLC、volume、openInt、原始时间/UTI和source row/key。

| symbol | 总行数(anchor+tail) | anchor close | tail first close | exact endpoint close | terminal return | minimum tail return | maximum tail return |
|---|---:|---:|---:|---:|---:|---:|---:|
| rb | 69 (1+68) | 5665.0 | 5728.0 | 5465.0 | -0.0353045013239188 | -0.053486319505736984 | 0.025419240953221536 |
| hc | 69 (1+68) | 5678.0 | 5781.0 | 5700.0 | 0.0038746037337090526 | -0.02676998943289891 | 0.029587883057414582 |
| i | 69 (1+68) | 713.0 | 725.5 | 716.0 | 0.004207573632538569 | -0.009817671809256662 | 0.10659186535764376 |

`terminal_gap=-0.03917910505762785`；`minimum_return_difference=-0.026716330072838072`。冻结Case-only条件的两个布尔值和OR均为`false`。68点exact common rb-minus-hc path、每值精确分数和原始数值在TAIL_MECHANICAL_METRICS中；i仅诊断，不进入pair test。Worker不解释这些值。

## 日历、标识和来源边界

沿用冻结合同的PNV closeTs+Asia/Shanghai，保留原无时区字段及raw ns，不做UTC平移。源只暴露十个PNV字段，没有逐行合约号、continuous-series/adjustment标签、交易日或夜盘归属；相应列空值如实保留，未用其他口径补列。source_series_path/snapshot与完整逻辑payload同一性证明本单沿用同一序列；原21:00–20:00 session配置保留。旧natural_tsa冲突没有被覆盖，也不被用于本单业务时间改写。详见TIME_AND_CALENDAR_CONTRACT。

## 执行、失败及独立核验

真实提取调用2次：第1次在DBA容量/逻辑长度断言失败，rc=1、无CSV；第2次为同脚本一次必要修正，按头部8964行读取，rc=0，三CSV完整生成。原代码、失败、终态回执和修正diff保留，没有把启动改记为未执行。没有循环重跑、替代源、特征引擎调用或源写入。

独立标准库validator复读63个确切源文件，使用不同解码与公式路径核三品种全部十字段range/CSV、anchor/prefix、exact endpoint、集合、合法数值和全部冻结机械指标，结果PASS。准确命令、cwd、环境、stdout/stderr、退出码和UTC起止时间见logs及SOURCE_AND_REPRODUCTION。逐文件receipt记录source/hash/bytes/rows/首末时间/anchor与tail价格/时区与缺失标签/版本/命令/分类/核验状态；完整封口与Git归档仍由同一独立validator再次核验。

## 全部未完与回交

本单行情提取、identity、时间口径对齐、机械指标、receipt与独立技术验证均完成。未提供的源标签仍为空，未新增正式交易日映射；这不改变本单沿用的冻结业务时钟。两个旧单及旧native可知性问题均保持关闭，不作为本单续研究入口。

原Management技术接收尚待执行；原Professional tail-only closure、业务支持/反证、自然挑战、当前Case闭合及后续管理裁定均未由Worker执行，未宣布FIRST_USABLE_ASOF_LOOP。只回原Management，不自动续Professional、不操作手机或其他聊天。新有限Goal只覆盖本单；旧记录/用量保留，主控Goal不动。

仓库`daowei2026/observe-iterate`，原分支`fy/feature-based-case-observation`；唯一输出`runs/BI-01-CO-04/artifacts/worker-BI01CO04-FROZEN-TAIL-TRANSPORT-01/`。数据交付commit：`d9a81ce768b23412e0f0547d3959285c33364d0e`。本报告、归档核验脚本与最终seal由其后继封口提交固定；最终准确SHA在本聊天回交，避免文件自引用。
