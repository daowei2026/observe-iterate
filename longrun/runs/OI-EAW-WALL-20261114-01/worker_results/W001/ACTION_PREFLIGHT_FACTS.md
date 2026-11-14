# W001 ActionPreflight 现场事实（未运行）

## 触发原因与可先复用范围

有真实旧物化和有界可解码样本；**没有已核同版的当前 canonical 产品材料**。本文件为补齐当前绑定或必要后续运行准备事实。没有启动新 Run、样本重算、构建、依赖安装或测试。

最小已有材料读法已经执行：在 `/m3varK/BaseData/futures/TA_updto20240229_DBA/fao/prod/2020-12-01 21:00:00~2021-02-22 20:00:00/EawP1WallLifecycleFrp/1/c/b/0/c/1/4/44aea11813b85d33becc06242f43621b6/rb.night_end_at_2300` 取 value rows 0–2，按 anchor 对 firing，关联 `/m3varK/BaseData/futures/TA_updto20240229_DBA/fao/prod/2020-12-01 21:00:00~2021-02-22 20:00:00/WallAssembler/8/8/5/1/d/6/1/b25bd29dd0d30a972dfabd41edcdf0518/rb.night_end_at_2300` 的 localNo=1 / UTI 72335299、72335302、72335308。它区分旧物化“仅存在”与“部分可解码并能对账”；不能区分当前二进制行为或证明业务适合性。

## 已存在的执行入口与精确模板

源码入口为 `/dwdhome/fy/BASE_E6_2/mquant/tis/test/integration/verify_eaw_p1_real_run.py:773–817`。CLI 原文要求 `--fixture`，执行选项为 `--execute-normal --evidence-dir --frp-stack-executable --frp-stack-yaml --frp-project-root --frp-source-worktree`。示例 fixture `/dwdhome/fy/BASE_E6_2/mquant/tis/test/integration/fixtures/eaw_p1_real_run.example.json` 含 REPLACE 占位符，不是真实窗口凭据。

以下只是现有入口的准确命令形状；尖括号仍为未绑定值，**本 W 未执行，也不是获准命令**：

```bash
PYTHONDONTWRITEBYTECODE=1 \
TMPDIR='/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/tmp' \
XDG_CACHE_HOME='/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/cache' \
MPLCONFIGDIR='/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D001/W001/cache/matplotlib' \
<已核环境的Python绝对路径> -B \
  '/dwdhome/fy/BASE_E6_2/mquant/tis/test/integration/verify_eaw_p1_real_run.py' \
  --fixture '<E1批准且已冻结的fixture绝对路径>' \
  --execute-normal \
  --evidence-dir '<获准且不存在或为空的独立证据目录>' \
  --frp-stack-executable '<已核Stack绝对路径>' \
  --frp-stack-yaml '<已核隔离overlay绝对路径>' \
  --frp-project-root '<已核FRP工程根>' \
  --frp-source-worktree '/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp'
```

这个 runner 的 AUTH_ENV 原文是 `EAW_P1_HEAVY_RUN_AUTHORIZED`；161–165 要求 Owner 明确授权后值为 YES。本 W 没有设置它。`--evidence-dir` 只限定回执位置，**不保证计算产物、Stack 缓存或项目日志在 W 写面内**。

该入口当前会先 Stack build `trade-poc:exe:ts`（427–460、809），按 EXECUTION_ORDER 生成 Wall、两组大单、Build、Attack、Absorb，再调四个 FRP 产品（28–46、680–703）。它不是 wall-only 有界探针。当前授权禁止构建/计算、禁止其它写面，故不能直接采用。未自行修改 runner 以缩窄流程。

native FRP worker 调用合同位于562–590行：`<ts绝对路径> --f=<worker one.edh绝对路径> --jp=<task绝对路径>`，cwd 为已核 project_root。Wall 单任务的 schema 来源为237–256、299–325行的 CalendarTarget/params/cal_type=Gen，但现存 runner 会构造四产品，未提供已经冻结的 wall-only task。是否另行签发最小动作由 E1/manager 决定，本 W 不生成假执行回执。

## 窗口、对象、成本的证据与未知

| 项目 | 已核事实 | 未核/停止条件 |
|---|---|---|
| 对象/日历候选 | 已有 receipt 是 rb / night_end_at_2300 | 不是本次新计算的选定值 |
| 局部窗口线索 | 旧样本 writer 触发数值时间为 2021-01-14 09:04:10–09:04:14.5，含非平凡更新和 End | 按日期截取会改变 source run/起始状态；不能保证短算重现同 Wall |
| 预热来源 | WallAssembler 默认 qt_n=30、qt_freq=1d、w_depth_ref_ticks=1200；`_impl` 先加载 cc/qt | 最小真实日历窗及预热需求未知；缩小 startDay 不保证缩小所有上游加载 |
| 已有短窗 | 46 文件、8,024,734 bytes；occurrence 15,809、current 15,208、diagnostic 328 记录 | 目录2020-12-01–2021-02-22，与触发数据真正范围分开 |
| 全年旧产品 | 43 文件、131,322,404 bytes；occurrence 266,469、current 254,424、diagnostic 7,469 记录 | 全年仅头与首尾；不全量解码 |
| 上游规模 | 本次仅 metadata 清点的各 class 合计 41550396966 bytes；部分 dense trace 为 GB 级 | 不加载这些整份大数据，不据旧报告推算当前峰值 |
| 只读实测成本 | 3条 probe 3,075 bytes；统计读取994,952 bytes；完整局部链抽取1,255,773 bytes，均低于显式上限 | 这是读取成本，不是重算内存/耗时预测；未测计算峰值 |
| 环境 | 当前源码/依赖 HEAD、dirty 已列；存在 ts/dbaw 路径候选，未运行 | Python ABI/依赖、二进制生成版本、Stack overlay、数据库权限尚未实际验证 |

不提供无证据的预计新行数、内存或秒数。这些均 UNKNOWN。已有源代码算法或旧 receipt 不能替代当前成本实测。

## 后继动作的前置条件与停止点

先由 E1 消费旧材料、判断是否足以回答局部问题；若要求当前 schema，需核准唯一对象/日历/预热范围、Wall 参数、生成版本、二进制和只写隔离区的存储/缓存/日志覆盖，并对依赖导入完成副作用检查。现有 root `run-python.sh:6–7` 会在 W 外写 migration 日志，不能直接复用。本 W 未 source m3rc，未调用该脚本。

可观察回执依源码为：源产品 thin receipt、三路 fields.json/data/trigger axes、明确生成版本和命令 exit code，必要 FRP active-map trace。到任一上游大加载、未知写入、同目录覆盖、自动构建、当前 schema 不匹配或成本超限，先停在 metadata/任务预览层。当前没有已批准的 wall-only 可运行材料动作；本 W 已在此停止计算路径。G-RUN/窗口采用及业务接受由 E1/manager 后继决定。
