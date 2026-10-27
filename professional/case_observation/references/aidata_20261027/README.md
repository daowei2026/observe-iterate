# aidata 两项测试：原件、采用范围与当前要求

这是专业工具知识的来源附件，不是新的执行规范、业务用例或本批运行记录。正常执行先读 [03_AIDATA_USE.md](../../03_AIDATA_USE.md)，需要复现、处理具体差异或取补充代码时再读这里。

## 1. 本次实际收到的原件

| 文件 | 保存方式与性质 |
| --- | --- |
| [测试报告.md](测试报告.md) | Owner 上传原件，包含开头的后续更正；正文仍保留首轮 2013/large/分页面结果 |
| [probe.py](probe.py) | Owner 上传原代码，原字节保存；脚本顶层会实际创建目录、取数和保存页面，不要作为当前任务模块导入或直接重跑 |

上传原件 SHA-256：

- `测试报告.md`：`c2725ea86db2f644ea9d4959d1790e7d3de8e964e21068f36a7b6cbb088a345b`
- `probe.py`：`89281df0855dfa0af1fabe94ec9d6d5a31ac5cb3dba20551aaae36ab44025024`

哈希只固定此次收到的字节，不证明图数、全部依赖或当前现场已验证。原报告中的相对链接指原测试目录内的文件；除本页列明两份原件外，未将其引用的运行目录、CSV、截图、versions.json、run_env.sh、actual_parameters.json 或补充报告复制进本仓，也不声称已逐项读取这些未随附实物。

## 2. 报告支持了什么，未支持什么

| 材料 | 可采用的认识 | 不能推出 |
| --- | --- | --- |
| 首轮任务 1 及 probe | chart_run → 独立 overview → board_run(reuse_core=True) 得到 1d 页面和正式日线；closeUti 可用 | 改成 2021 起点后的行数/覆盖已实跑；结束日期全天已包含 |
| 首轮任务 2 及 probe | chart_run → big_world_pages → board_run 得到 overview、各例 30m 图和窗口内正式数据；big-only 不生成中小节点 | 第二接口直接返回单页；用例 1d 切片就是全历史数据；large 点就是 mid 点 |
| 报告开头后续更正 | 测试方报告已用现有 CAEGraph 四个 PlotSet 实现单页并改为 mid，无需源码修改 | 本次已拿到组合代码、已知补充 URL、已独立复查、或已经验证不变 URL 持续追加 |
| Owner 本次输入要求 | 概览 2021-01-01 起，因 rb/hc/i 此后交易日历相同；30m 图用 mid | 全部空值已消失，或其他品种也适用此范围和日历 |
| [当前输入示例](../../examples/aidata_inputs.py) | 将上述要求落到现有 brief/Feature 配置，避免继续照抄旧参数 | 完整现场流程已重跑；示例已实现单页组合 |

首轮正文的“单 URL 未通过”和源码改造建议是历史状态；不得忽视开头更正，将它们继续作为现行待办。与此同时，后续更正也不把首轮 large 的 47 行、旧页面、旧范围逐值核对变成 mid/2021 新配置的验收结果。

报告中的测试窗口、run_id、URL、行数与样式只是原测试事实，不是 AI 已发现的业务用例，不作为后续数量/日期/图样式阈值。技术证据支持工具复用，不支持任何投资结论。

## 3. 现场复用定位

从原 probe 的 ROOT 可定位原测试目录：

`/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/fy_owner_1d_30m_20261027`

报告更正指向该目录下的 `mid_combined_revision/补充测试报告.md`。执行者在原工作区取得这份补充报告及它实际引用的组合脚本、页面身份后，沿用既有 CAEGraph/PlotSet 方式；本仓不猜其脚本名、URL 或新增 API。此次附件没有这些实物；经 GitHub 按报告中的工作分支读取也未取得，不能据此否定现场报告的成功。

原报告记录 aidata 提交 `f58ea95c358b9ac31659c92b7bc20fe9bf7f8264`，工作分支 `codex/aidata-named-csv-features-20261019`；Frame `4d0ff8f`、TIS `f26495c`、Uplot `13badc6`、Trier `adea9b4`，且 TIS/Uplot 有既有本地差异。缩写和分支为报告记录，不补造完整 SHA，也不能仅凭 aidata 干净推断整个环境无差异。复用时用真实 checkout/必要差异对应，不将这些记录变成永久版本要求。

原环境为已有 Anaconda/Python 3.10.13、pandas 2.3.2、numpy 1.26.4、Bokeh 3.6.0，并使用 run_env.sh 的 TLS 兼容配置。该脚本未随附；需要时读取现场原脚本，不凭报告重建环境或修改共享服务。`ensure_profile_runtime()` 只注册配置，原自定义 brief 未采用标准 Profile v4。

## 4. 已落实到当前方法的差异

当前方法及输入示例把 Context.startDay 和方式一 full_history 起点改为 2021-01-01；方式二概览继承相同 Context，各用例窗口由真实选例提供；贴近转折对象、key 和图例使用 mid，节点/图层仍为 big。结束边界保持显式输入并记录实际覆盖，不未经验证改为“包含结束日”。

原件保持不变，当前用法见 03，Owner 交付见 [02](../../02_OWNER_DELIVERY.md)。补充证据暂缺只限制依赖它的主张和页面交付，不要求先补齐整套历史测试包才能开展已有正式数据上的研究。
