# W007 最小事实报告

身份：`OI-U2-F-OBS-20261118-01 / W007 / D006 / WI-E-R1 / M-E-R1`。Worker `codex:OI-U2-F-OBS-20261118-01:worker:W1`，回原 issuer `chatgpt:OI-U2-F-OBS-20261118-01:executor:E2`。活跃工单 `daowei2026/observe-iterate@1ec2229ce44a92407e603e3a617a96616c5cde3c:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W007/ORDER.json`；正文 `daowei2026/observe-iterate@4db7b49e165d025a5f24a39878f893fe4aadf4be:longrun/runs/OI-U2-F-OBS-20261118-01/work_orders/W007/ORDER.md`。

**事实状态 BLOCKED；正常入口 FAIL；拟正式Return outcome=STOP。D实际启动0次，无D退出码。** 本轮执行的是W007条件核对，不重跑W006或其他旧W；D006/E未业务完成。

## 当前活跃运行包

仅加载当前 `/dwdhome/fy/BASE_E6_2_copy/m3rc`，Python为 `/m3c3/Linux/apps/anaconda3/bin/python`，3.10.13。没有运行系统Python、修改sys.path/任何package __path__或叠加第二套TIS。mquant、mquant.frame、mquant.tis、mquant.tis.frp均从当前工作区对应目录导入；构造模块及F/Q/V三个wrapper的find_spec均未找到。构造import未尝试，因为其spec不存在；未调用make_features或producer。

完整必需sys.path、file/path与spec记录：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W007/current_runtime_provenance.json`；来源日志 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W007/logs/current_runtime_provenance.log`。来源脚本exit0只表示记录正常结束，不是D退出码或准入PASS。m3rc日志保留nif2 DNS错误，随后上述活跃父包已成功导入。

活跃TIS realpath/Git root均为 `/dwdhome/fy/BASE_E6_2_copy/mquant/tis`，origin=`https://gogs.dw/mquant/tis.git`，HEAD=`10010b89f8fc79a91affd26f985b6d9bf2d33c6c`，不等于锁定 `2f460d663d821cf2ba25555eda13e78b697d0767`。以下四文件均不存在且未被Git跟踪：

- frp/fqv_kline_example.py
- frp/CommonPriceTurnGroupCandidates.py
- frp/PostTurnGroupDirectionalOrganization.py
- frp/CommonTurnGroupValidity.py

限定这四文件的status为空；本报告的 `ACTIVE_TIS_WORKTREE_DIRTY_OR_INCOMPLETE` 取“缺少本次所需文件/不完整”的分支，不声称观察到本地脏修改。锁定commit对象在本地存在，四文件对锁定版本的只读diff exit1。

## 一次有界精确文件名查找

只在当前工作区查找fqv_kline_example.py一次，排除observe-iterate-runs、.git、__pycache__；不跟随symlink，不访问其他工作区或/run，1.763秒正常完成。唯一命中：

`/dwdhome/fy/BASE_E6_2_copy/.runtime/fqv-rb-hc-i-20261117/runtime/mquant/tis/frp/fqv_kline_example.py`

该命中的Git root=`/dwdhome/fy`，HEAD=`0cb55e4726c7af711fa790f848c2fec88db6b949`；它不属于活跃TIS Git工作树。观察到的包边界结构存在，不证明其是完整、单一、正常且锁定的mquant/TIS来源，判定NOT_PROVEN。没有执行、导入、复制、软链或接入该命中；没有追加搜索。

## Haskell固定来源

固定路径/Git root `/dwdhome/fy/BASE_E6_2_copy/edh-universe/frp/frp`，origin=`https://gogs.dw/frp/frp`，HEAD=`37c790c0f456fe3022bb00609219d3e92a5c2f9b`，不等于锁定 `67711c492da909ed0f044f357beb278abf7fc71c`。锁定对象在本地存在；`merge-base --is-ancestor` exit1（不是当前HEAD祖先）；目标F Haskell文件的工作树对锁定版本diff exit1。只读记录，没有切版本、构建或安装，没有把Haskell树用于Python import，也不据此推断Python缺模块的因果关系。

## 条件判断与未执行事实

原单第7节第1、7项通过，第2/3/4/5/6项失败。精确分类：

- LOCKED_TIS_NORMAL_PACKAGE_ABSENT
- ACTIVE_TIS_VERSION_MISMATCH
- ACTIVE_TIS_WORKTREE_DIRTY_OR_INCOMPLETE
- LOCKED_FRP_SOURCE_VERSION_MISMATCH

机器判据、每项文件状态及Git只读命令/退出码：`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W007/normal_fqv_entry_decision.json`。七项必须全部通过，故按原单第9节停止：D=0次、无D退出码、无D运行日志；没有HTML、definition_run_report、prepared_tables或plot_data；F未构造、fields.json未检查，不推断F产品不存在。

最终原D参考位置 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/source/observe-iterate/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/D/u2_f_caegraph_definition.py`，只读核验SHA-256=`92ab234df976469c6deb85052251b81633d79994440dccca199120672072433f`；原C3位置 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W001/source/observe-iterate/longrun/runs/OI-U2-F-OBS-20261118-01/artifacts/C/caegraph_display.py`，SHA-256=`798042296f88ff5747a0248a81902953550fe39e4fa18337e8fdcfe9557877b7`。二者未修改、未执行；没有repair_source或repair.diff（实际修改为无）。

未安装/构建/生成package文件、未复制构造源码、未创建overlay/新环境/额外沙箱，未fetch/pull/checkout/切换版本或改平台/业务源。没有读取Q/V产品、调用F producer、启动W2或声明DATA_READY。旧W001～W006历史保持。

## 回交原E2

必要本地原件及其精确路径/字节数/SHA-256见 `/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W007/MANIFEST.local.json`。未制作全目录审计或运输包。`/dwdhome/fy/BASE_E6_2_copy/observe-iterate-runs/OI-U2-F-OBS-20261118-01/W007/RETURN_PREPARATION.json`只是本地准备稿，尚无新事实的已发布Git refs；由主控原样运输必要产物并回给真实映射后，同W007再签正式longrun-worker-return/v2，不冒称已发布。E3图接受、E4/W2准入、D006/E完成均未发生。
