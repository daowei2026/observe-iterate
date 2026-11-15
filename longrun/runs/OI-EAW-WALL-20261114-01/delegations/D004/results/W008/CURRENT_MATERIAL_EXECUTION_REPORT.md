# W008当前材料执行记录

worker shell实际cwd=/dwdhome/fy/BASE_E6_2；单个工具子进程真实cwd逐项记录。HOME/CODEX_HOME保持。所有命令先写.pre receipt声明输入范围、写面、timeout与process-group TERM/KILL停止法；最大600秒，输出阈值5GiB。未执行不计为已执行。

| command | exit | seconds | stdout bytes | stderr bytes |
|---|---:|---:|---:|---:|
| base-pre-frp-head | 0 | 0.099231 | 41 | 0 |
| base-pre-frp-branch | 0 | 0.089883 | 30 | 0 |
| base-pre-frp-status | 0 | 0.385266 | 38 | 0 |
| base-pre-frp-diff | 0 | 0.083364 | 1555 | 0 |
| base-pre-frp-cached-diff | 0 | 0.076507 | 0 | 0 |
| base-pre-frp_core-head | 0 | 0.075644 | 41 | 0 |
| base-pre-frp_core-branch | 0 | 0.088715 | 5 | 0 |
| base-pre-frp_core-status | 0 | 0.135028 | 0 | 0 |
| base-pre-frp_core-diff | 0 | 0.085011 | 0 | 0 |
| base-pre-frp_core-cached-diff | 0 | 0.084676 | 0 | 0 |
| base-pre-tis-head | 0 | 0.088482 | 41 | 0 |
| base-pre-tis-branch | 0 | 0.089744 | 30 | 0 |
| base-pre-tis-status | 0 | 0.496247 | 28 | 0 |
| base-pre-tis-diff | 0 | 0.088941 | 2347 | 0 |
| base-pre-tis-cached-diff | 0 | 0.082592 | 0 | 0 |
| asset-p1-source-list | 0 | 0.088180 | 569 | 0 |
| tools-ghc-version | 127 | 0.139220 | 0 | 164 |
| tools-ghcpkg-list | 127 | 0.089066 | 0 | 168 |
| cached-p1-test-paths | 0 | 0.345052 | 53 | 0 |
| p1-test-selected-locations | 0 | 0.095677 | 6570 | 0 |
| ghc-linker-dependencies | 0 | 0.203094 | 5371 | 0 |
| existing-tinfo6-ghc-version | 0 | 6.723428 | 6 | 0 |
| existing-tinfo6-ghcpkg-global | 0 | 2.294534 | 580 | 0 |
| selected-ghcpkg-visible | 0 | 0.706969 | 4709 | 0 |
| tis-current-reader-file-locations | 0 | 0.146367 | 57 | 0 |
| current-tis-wall-entrypoints | 0 | 0.208163 | 554 | 0 |
| current-normal-compile | 1 | 47.185472 | 2200 | 1648 |
| current-normal-compile-v2 | 0 | 46.984740 | 395 | 0 |
| current-normal-run | 0 | 0.088963 | 19253 | 0 |
| existing-scenario-cross-duplicate | 0 | 0.087522 | 8179 | 0 |
| existing-scenario-after-end | 0 | 0.087565 | 11610 | 0 |
| existing-bson-module-info | 0 | 0.610253 | 302 | 0 |
| current-bson-reader-compile | 0 | 37.329997 | 2273 | 14772 |
| current-bson-reader | 0 | 0.340225 | 5081 | 0 |
| reader-current-frame-head | 0 | 0.086309 | 41 | 0 |
| reader-current-frame-branch | 0 | 0.085450 | 5 | 0 |
| reader-current-frame-status | 0 | 0.136285 | 0 | 0 |
| reader-current-frame-reader-diff | 0 | 0.084000 | 0 | 0 |
| reader-current-worker-head | 0 | 0.089593 | 41 | 0 |
| reader-current-worker-branch | 0 | 0.084258 | 5 | 0 |
| reader-current-worker-status | 0 | 0.434491 | 136 | 0 |
| reader-current-worker-reader-diff | 0 | 0.081567 | 0 | 0 |
| base-post-frp-head | 0 | 0.088903 | 41 | 0 |
| base-post-frp-branch | 0 | 0.083771 | 30 | 0 |
| base-post-frp-status | 0 | 0.338246 | 38 | 0 |
| base-post-frp-diff | 0 | 0.087395 | 1555 | 0 |
| base-post-frp-cached-diff | 0 | 0.150484 | 0 | 0 |
| base-post-frp_core-head | 0 | 0.083973 | 41 | 0 |
| base-post-frp_core-branch | 0 | 0.087134 | 5 | 0 |
| base-post-frp_core-status | 0 | 0.138475 | 0 | 0 |
| base-post-frp_core-diff | 0 | 0.094274 | 0 | 0 |
| base-post-frp_core-cached-diff | 0 | 0.087335 | 0 | 0 |
| base-post-tis-head | 0 | 0.084584 | 41 | 0 |
| base-post-tis-branch | 0 | 0.088020 | 30 | 0 |
| base-post-tis-status | 0 | 0.502440 | 28 | 0 |
| base-post-tis-diff | 0 | 0.088047 | 2347 | 0 |
| base-post-tis-cached-diff | 0 | 0.084944 | 0 | 0 |

每项完整argv/cwd、输入/输出绝对路径、bytes/SHA、开始结束时间、env override、预计写面和实际exit在同名receipt以及logs/COMMAND_EXECUTIONS.jsonl。其余只读资格核验/文件生成命令及上述命令的外层shell也逐字保存在COMMAND_LOG.jsonl。原生封存调用进行中状态如实记null；其真实终态由最终工具回执交主控，不能预填exit0。

## base-pre-frp-head

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp", "rev-parse", "HEAD"]`
输入边界：单一已指定仓库FRP的head，不扫描untracked；stdout完整归档
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp-head.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp-head.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-pre-frp-head.json`
exit=0；elapsed=0.099230995s；预期写面=["仅W008日志/receipt"]；stop=None。

## base-pre-frp-branch

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp", "symbolic-ref", "--short", "-q", "HEAD"]`
输入边界：单一已指定仓库FRP的branch，不扫描untracked；stdout完整归档
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp-branch.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp-branch.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-pre-frp-branch.json`
exit=0；elapsed=0.089883231s；预期写面=["仅W008日志/receipt"]；stop=None。

## base-pre-frp-status

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp", "status", "--porcelain=v1", "-uno"]`
输入边界：单一已指定仓库FRP的status，不扫描untracked；stdout完整归档
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp-status.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp-status.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-pre-frp-status.json`
exit=0；elapsed=0.385265661s；预期写面=["仅W008日志/receipt"]；stop=None。

## base-pre-frp-diff

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp", "diff", "--no-ext-diff", "--no-textconv", "--binary"]`
输入边界：单一已指定仓库FRP的diff，不扫描untracked；stdout完整归档
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp-diff.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp-diff.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-pre-frp-diff.json`
exit=0；elapsed=0.083364026s；预期写面=["仅W008日志/receipt"]；stop=None。

## base-pre-frp-cached-diff

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp", "diff", "--cached", "--no-ext-diff", "--no-textconv", "--binary"]`
输入边界：单一已指定仓库FRP的cached-diff，不扫描untracked；stdout完整归档
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp-cached-diff.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp-cached-diff.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-pre-frp-cached-diff.json`
exit=0；elapsed=0.076506991s；预期写面=["仅W008日志/receipt"]；stop=None。

## base-pre-frp_core-head

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp-core", "rev-parse", "HEAD"]`
输入边界：单一已指定仓库FRP_CORE的head，不扫描untracked；stdout完整归档
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp_core-head.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp_core-head.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-pre-frp_core-head.json`
exit=0；elapsed=0.075644111s；预期写面=["仅W008日志/receipt"]；stop=None。

## base-pre-frp_core-branch

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp-core", "symbolic-ref", "--short", "-q", "HEAD"]`
输入边界：单一已指定仓库FRP_CORE的branch，不扫描untracked；stdout完整归档
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp_core-branch.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp_core-branch.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-pre-frp_core-branch.json`
exit=0；elapsed=0.088715421s；预期写面=["仅W008日志/receipt"]；stop=None。

## base-pre-frp_core-status

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp-core", "status", "--porcelain=v1", "-uno"]`
输入边界：单一已指定仓库FRP_CORE的status，不扫描untracked；stdout完整归档
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp_core-status.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp_core-status.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-pre-frp_core-status.json`
exit=0；elapsed=0.135028208s；预期写面=["仅W008日志/receipt"]；stop=None。

## base-pre-frp_core-diff

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp-core", "diff", "--no-ext-diff", "--no-textconv", "--binary"]`
输入边界：单一已指定仓库FRP_CORE的diff，不扫描untracked；stdout完整归档
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp_core-diff.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp_core-diff.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-pre-frp_core-diff.json`
exit=0；elapsed=0.085011100s；预期写面=["仅W008日志/receipt"]；stop=None。

## base-pre-frp_core-cached-diff

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp-core", "diff", "--cached", "--no-ext-diff", "--no-textconv", "--binary"]`
输入边界：单一已指定仓库FRP_CORE的cached-diff，不扫描untracked；stdout完整归档
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp_core-cached-diff.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-frp_core-cached-diff.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-pre-frp_core-cached-diff.json`
exit=0；elapsed=0.084676103s；预期写面=["仅W008日志/receipt"]；stop=None。

## base-pre-tis-head

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/mquant/tis", "rev-parse", "HEAD"]`
输入边界：单一已指定仓库TIS的head，不扫描untracked；stdout完整归档
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-tis-head.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-tis-head.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-pre-tis-head.json`
exit=0；elapsed=0.088482450s；预期写面=["仅W008日志/receipt"]；stop=None。

## base-pre-tis-branch

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/mquant/tis", "symbolic-ref", "--short", "-q", "HEAD"]`
输入边界：单一已指定仓库TIS的branch，不扫描untracked；stdout完整归档
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-tis-branch.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-tis-branch.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-pre-tis-branch.json`
exit=0；elapsed=0.089744387s；预期写面=["仅W008日志/receipt"]；stop=None。

## base-pre-tis-status

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/mquant/tis", "status", "--porcelain=v1", "-uno"]`
输入边界：单一已指定仓库TIS的status，不扫描untracked；stdout完整归档
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-tis-status.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-tis-status.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-pre-tis-status.json`
exit=0；elapsed=0.496246967s；预期写面=["仅W008日志/receipt"]；stop=None。

## base-pre-tis-diff

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/mquant/tis", "diff", "--no-ext-diff", "--no-textconv", "--binary"]`
输入边界：单一已指定仓库TIS的diff，不扫描untracked；stdout完整归档
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-tis-diff.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-tis-diff.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-pre-tis-diff.json`
exit=0；elapsed=0.088941493s；预期写面=["仅W008日志/receipt"]；stop=None。

## base-pre-tis-cached-diff

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/mquant/tis", "diff", "--cached", "--no-ext-diff", "--no-textconv", "--binary"]`
输入边界：单一已指定仓库TIS的cached-diff，不扫描untracked；stdout完整归档
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-tis-cached-diff.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-pre-tis-cached-diff.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-pre-tis-cached-diff.json`
exit=0；elapsed=0.082591628s；预期写面=["仅W008日志/receipt"]；stop=None。

## asset-p1-source-list

cwd: `/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp`
argv: `["rg", "--files", "src/Frp/Instance/ISL/Eaw/P1", "test/Frp/Instance/ISL/Eaw/P1", "-g", "*.hs", "-g", "AGENTS.md"]`
输入边界：仅FRP既知P1源码/test两目录
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/asset-p1-source-list.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/asset-p1-source-list.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/asset-p1-source-list.json`
exit=0；elapsed=0.088179791s；预期写面=["W008日志"]；stop=None。

## tools-ghc-version

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["ghc", "--numeric-version"]`
输入边界：已安装GHC版本查询
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/tools-ghc-version.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/tools-ghc-version.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/tools-ghc-version.json`
exit=127；elapsed=0.139219592s；预期写面=["W008日志"]；stop=None。

## tools-ghcpkg-list

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["ghc-pkg", "list", "--simple-output"]`
输入边界：当前已安装packageDB目录列表；不安装/下载
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/tools-ghcpkg-list.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/tools-ghcpkg-list.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/tools-ghcpkg-list.json`
exit=127；elapsed=0.089065984s；预期写面=["W008日志"]；stop=None。

## cached-p1-test-paths

cwd: `/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp`
argv: `["rg", "--files", "--hidden", "--no-ignore", ".stack-work/dist", "-g", "*eaw*p1*", "-g", "package.conf.inplace", "-g", "setup-config", "-g", "*P1EndToEnd*", "-g", "*WallLifecycle*"]`
输入边界：仅FRP现有.stack-work/dist，文件名限定P1/test/buildmetadata
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/cached-p1-test-paths.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/cached-p1-test-paths.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/cached-p1-test-paths.json`
exit=0；elapsed=0.345052361s；预期写面=["W008日志/receipt"]；stop=None。

## p1-test-selected-locations

cwd: `/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp`
argv: `["rg", "-n", "wallLifecycleMust|wallLifecycleTransition|WallEnded|wallUpdate|wallEnd|requireRight|FromBSON|toBSON|wallState", "test/Frp/Instance/ISL/Eaw/P1/P1EndToEndSpec.hs"]`
输入边界：仅一个已指定52KB existing test，定位normal和最高两scenario及readerhelpers
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/p1-test-selected-locations.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/p1-test-selected-locations.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/p1-test-selected-locations.json`
exit=0；elapsed=0.095677246s；预期写面=["W008日志"]；stop=None。

## ghc-linker-dependencies

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["ldd", "/nix/.ghcup/ghc/9.4.8/lib/ghc-9.4.8/bin/ghc-9.4.8"]`
输入边界：仅现有GHC ELF依赖查询，不安装依赖
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/ghc-linker-dependencies.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/ghc-linker-dependencies.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/ghc-linker-dependencies.json`
exit=0；elapsed=0.203093619s；预期写面=["W008日志"]；stop=None。

## existing-tinfo6-ghc-version

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["/nix/.stack/programs/x86_64-linux/ghc-tinfo6-9.4.8/bin/ghc", "--numeric-version"]`
输入边界：已存在同版本tinfo6 GHC查询，不写/nix
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/existing-tinfo6-ghc-version.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/existing-tinfo6-ghc-version.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/existing-tinfo6-ghc-version.json`
exit=0；elapsed=6.723428007s；预期写面=["W008日志"]；stop=None。

## existing-tinfo6-ghcpkg-global

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["/nix/.stack/programs/x86_64-linux/ghc-tinfo6-9.4.8/bin/ghc-pkg", "list", "--simple-output"]`
输入边界：已存在同版本GHC global pkgdb只读
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/existing-tinfo6-ghcpkg-global.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/existing-tinfo6-ghcpkg-global.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/existing-tinfo6-ghcpkg-global.json`
exit=0；elapsed=2.294533592s；预期写面=["W008日志"]；stop=None。

## selected-ghcpkg-visible

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["/nix/.stack/programs/x86_64-linux/ghc-tinfo6-9.4.8/bin/ghc-pkg", "--package-db", "/nix/.stack/snapshots/x86_64-linux/8febf378dbd330a73b2a5cccfd1978b0b432f8b18bd6be55f68ff265812cd09f/9.4.8/pkgdb", "--package-db", "/dwdhome/fy/BASE_E6_2/edh-universe/.stack-work/install/x86_64-linux/8febf378dbd330a73b2a5cccfd1978b0b432f8b18bd6be55f68ff265812cd09f/9.4.8/pkgdb", "list", "--simple-output"]`
输入边界：两个setup-config精确pkgdb只读；不枚举361snapshot子目录
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/selected-ghcpkg-visible.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/selected-ghcpkg-visible.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/selected-ghcpkg-visible.json`
exit=0；elapsed=0.706969133s；预期写面=["W008日志"]；stop=None。

## tis-current-reader-file-locations

cwd: `/dwdhome/fy/BASE_E6_2/mquant/tis`
argv: `["rg", "--files", "-g", "*Eaw*", "-g", "*P1*", "-g", "*FrpDba*", "-g", "dbaw.py", "-g", "AGENTS.md"]`
输入边界：仅已指明TIS仓库文件名索引，匹配Wall feature/wrapper/reader，不读大数据
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/tis-current-reader-file-locations.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/tis-current-reader-file-locations.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/tis-current-reader-file-locations.json`
exit=0；elapsed=0.146367204s；预期写面=["W008日志"]；stop=None。

## current-tis-wall-entrypoints

cwd: `/dwdhome/fy/BASE_E6_2/mquant/tis`
argv: `["rg", "-n", "EawP1WallLifecycleFrp|wall_occurrences|wall_current_view|wall_diagnostics|FrpDbaDao|OnlyRead|Cache", "frp/EawBattleP.py"]`
输入边界：一个既知TIS feature文件，核current产品定义与reader调用，不执行真实市场计算
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/current-tis-wall-entrypoints.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/current-tis-wall-entrypoints.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/current-tis-wall-entrypoints.json`
exit=0；elapsed=0.208162946s；预期写面=["W008日志"]；stop=None。

## current-normal-compile

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["/nix/.stack/programs/x86_64-linux/ghc-tinfo6-9.4.8/bin/ghc", "--make", "-O0", "-j1", "-v1", "-package-env", "-", "-no-user-package-db", "-package-db", "/nix/.stack/snapshots/x86_64-linux/8febf378dbd330a73b2a5cccfd1978b0b432f8b18bd6be55f68ff265812cd09f/9.4.8/pkgdb", "-package-db", "/dwdhome/fy/BASE_E6_2/edh-universe/.stack-work/install/x86_64-linux/8febf378dbd330a73b2a5cccfd1978b0b432f8b18bd6be55f68ff265812cd09f/9.4.8/pkgdb", "-package", "frp", "-i", "-i/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/tools", "-outputdir", "/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/build", "-stubdir", "/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/build", "-tmpdir", "/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/tmp", "-XGHC2021", "-XOverloadedStrings", "-XOverloadedLists", "-XOverloadedLabels", "-XDuplicateRecordFields", "-XRecordWildCards", "-XLambdaCase", "-XBangPatterns", "-XViewPatterns", "-XTupleSections", "-XMultiWayIf", "-XTemplateHaskell", "-XRecursiveDo", "-XTypeFamilies", "-XDeriveAnyClass", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/Interface/Common.hs", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/Interface/PreL0.hs", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/Products.hs", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/Internal/OccurrenceLedger.hs", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/WallLifecycle.hs", "/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/tools/ObserveCurrent.hs", "-o", "/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/build/observe-current"]`
输入边界：当前5个Wall模块直接从live BASE读取；同版本既有GHC和已安装依赖；仅W008脚本和O0编译
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/current-normal-compile.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/current-normal-compile.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/current-normal-compile.json`
exit=1；elapsed=47.185471806s；预期写面=["W008/build对象/interface/executable", "W008/tmp GHC临时文件", "W008 logs/receipts"]；stop=None。

## current-normal-compile-v2

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["/nix/.stack/programs/x86_64-linux/ghc-tinfo6-9.4.8/bin/ghc", "--make", "-O0", "-j1", "-v1", "-package-env", "-", "-no-user-package-db", "-package-db", "/nix/.stack/snapshots/x86_64-linux/8febf378dbd330a73b2a5cccfd1978b0b432f8b18bd6be55f68ff265812cd09f/9.4.8/pkgdb", "-package-db", "/dwdhome/fy/BASE_E6_2/edh-universe/.stack-work/install/x86_64-linux/8febf378dbd330a73b2a5cccfd1978b0b432f8b18bd6be55f68ff265812cd09f/9.4.8/pkgdb", "-package", "frp", "-i", "-i/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/tools", "-outputdir", "/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/build", "-stubdir", "/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/build", "-tmpdir", "/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/tmp", "-XGHC2021", "-XOverloadedStrings", "-XOverloadedLists", "-XOverloadedLabels", "-XDuplicateRecordFields", "-XRecordWildCards", "-XLambdaCase", "-XBangPatterns", "-XViewPatterns", "-XTupleSections", "-XMultiWayIf", "-XTemplateHaskell", "-XRecursiveDo", "-XTypeFamilies", "-XDeriveAnyClass", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/Interface/Common.hs", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/Interface/PreL0.hs", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/Products.hs", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/Internal/OccurrenceLedger.hs", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/WallLifecycle.hs", "/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/tools/ObserveCurrent.hs", "-o", "/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/build/observe-current"]`
输入边界：同5 current生产模块+本W脚本类型pragma修正；只复用本W已生成对象
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/current-normal-compile-v2.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/current-normal-compile-v2.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/current-normal-compile-v2.json`
exit=0；elapsed=46.984740313s；预期写面=["W008/build和tmp、日志/receipt"]；stop=None。

## current-normal-run

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/build/observe-current", "normal"]`
输入边界：normal3受控call4typedinputs；或单个已有test最高优先表达式；总scenario最多2，不加载市场数据
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/current-normal-run.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/current-normal-run.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/current-normal-run.json`
exit=0；elapsed=0.088963282s；预期写面=["仅stdout/stderr/receipt；程序无文件写API"]；stop=None。

## existing-scenario-cross-duplicate

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/build/observe-current", "scenario-duplicate"]`
输入边界：normal3受控call4typedinputs；或单个已有test最高优先表达式；总scenario最多2，不加载市场数据
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/existing-scenario-cross-duplicate.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/existing-scenario-cross-duplicate.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/existing-scenario-cross-duplicate.json`
exit=0；elapsed=0.087522444s；预期写面=["仅stdout/stderr/receipt；程序无文件写API"]；stop=None。

## existing-scenario-after-end

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/build/observe-current", "scenario-after-end"]`
输入边界：normal3受控call4typedinputs；或单个已有test最高优先表达式；总scenario最多2，不加载市场数据
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/existing-scenario-after-end.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/existing-scenario-after-end.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/existing-scenario-after-end.json`
exit=0；elapsed=0.087565319s；预期写面=["仅stdout/stderr/receipt；程序无文件写API"]；stop=None。

## existing-bson-module-info

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["/nix/.stack/programs/x86_64-linux/ghc-tinfo6-9.4.8/bin/ghc-pkg", "--package-db", "/nix/.stack/snapshots/x86_64-linux/8febf378dbd330a73b2a5cccfd1978b0b432f8b18bd6be55f68ff265812cd09f/9.4.8/pkgdb", "--package-db", "/dwdhome/fy/BASE_E6_2/edh-universe/.stack-work/install/x86_64-linux/8febf378dbd330a73b2a5cccfd1978b0b432f8b18bd6be55f68ff265812cd09f/9.4.8/pkgdb", "field", "bson", "exposed-modules,depends"]`
输入边界：单一已安装bson包metadata，只读，不安装下载
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/existing-bson-module-info.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/existing-bson-module-info.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/existing-bson-module-info.json`
exit=0；elapsed=0.610252755s；预期写面=["W008日志"]；stop=None。

## current-bson-reader-compile

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["/nix/.stack/programs/x86_64-linux/ghc-tinfo6-9.4.8/bin/ghc", "--make", "-O0", "-j1", "-v1", "-package-env", "-", "-no-user-package-db", "-package-db", "/nix/.stack/snapshots/x86_64-linux/8febf378dbd330a73b2a5cccfd1978b0b432f8b18bd6be55f68ff265812cd09f/9.4.8/pkgdb", "-package-db", "/dwdhome/fy/BASE_E6_2/edh-universe/.stack-work/install/x86_64-linux/8febf378dbd330a73b2a5cccfd1978b0b432f8b18bd6be55f68ff265812cd09f/9.4.8/pkgdb", "-package", "frp", "-i", "-i/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/tools", "-outputdir", "/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/build", "-stubdir", "/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/build", "-tmpdir", "/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/tmp", "-XGHC2021", "-XOverloadedStrings", "-XOverloadedLists", "-XOverloadedLabels", "-XDuplicateRecordFields", "-XRecordWildCards", "-XLambdaCase", "-XBangPatterns", "-XViewPatterns", "-XTupleSections", "-XMultiWayIf", "-XTemplateHaskell", "-XRecursiveDo", "-XTypeFamilies", "-XDeriveAnyClass", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/Interface/Common.hs", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/Interface/PreL0.hs", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/Products.hs", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/Internal/OccurrenceLedger.hs", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/WallLifecycle.hs", "/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/tools/ObserveCurrent.hs", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/BuildActivity.hs", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/AttackSegmentBook.hs", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/AbsorbInteraction.hs", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp/src/Frp/Instance/ISL/Eaw/P1/Publication.hs", "/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/tools/ReadCurrentBson.hs", "-main-is", "ReadCurrentBson", "-o", "/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/build/read-current-bson"]`
输入边界：4追加current生产模块+本W小型reader，复用已建5currentmodules；不写原source/sharedcache
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/current-bson-reader-compile.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/current-bson-reader-compile.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/current-bson-reader-compile.json`
exit=0；elapsed=37.329996874s；预期写面=["W008 build/tmp/logs/receipts"]；stop=None。

## current-bson-reader

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/build/read-current-bson"]`
输入边界：仅4个既有normal typedoccurrences内存ToBSON/FromBSON
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/current-bson-reader.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/current-bson-reader.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/current-bson-reader.json`
exit=0；elapsed=0.340225081s；预期写面=["W008日志/receipt；reader程序不写文件"]；stop=None。

## reader-current-frame-head

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/mquant/frame", "rev-parse", "HEAD"]`
输入边界：已指定reader源码仓库当前binding；status不扫描untracked，diff仅具名readerpaths
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/reader-current-frame-head.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/reader-current-frame-head.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/reader-current-frame-head.json`
exit=0；elapsed=0.086309423s；预期写面=["W008日志/receipt"]；stop=None。

## reader-current-frame-branch

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/mquant/frame", "symbolic-ref", "--short", "-q", "HEAD"]`
输入边界：已指定reader源码仓库当前binding；status不扫描untracked，diff仅具名readerpaths
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/reader-current-frame-branch.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/reader-current-frame-branch.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/reader-current-frame-branch.json`
exit=0；elapsed=0.085449951s；预期写面=["W008日志/receipt"]；stop=None。

## reader-current-frame-status

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/mquant/frame", "status", "--porcelain=v1", "-uno"]`
输入边界：已指定reader源码仓库当前binding；status不扫描untracked，diff仅具名readerpaths
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/reader-current-frame-status.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/reader-current-frame-status.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/reader-current-frame-status.json`
exit=0；elapsed=0.136285372s；预期写面=["W008日志/receipt"]；stop=None。

## reader-current-frame-reader-diff

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/mquant/frame", "diff", "--no-ext-diff", "--no-textconv", "--", "lang/internal/dao/frp/dba.py", "lang/frp/base.py", "core/store.py", "core/base/json.py"]`
输入边界：已指定reader源码仓库当前binding；status不扫描untracked，diff仅具名readerpaths
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/reader-current-frame-reader-diff.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/reader-current-frame-reader-diff.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/reader-current-frame-reader-diff.json`
exit=0；elapsed=0.084000351s；预期写面=["W008日志/receipt"]；stop=None。

## reader-current-worker-head

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/mquant/worker", "rev-parse", "HEAD"]`
输入边界：已指定reader源码仓库当前binding；status不扫描untracked，diff仅具名readerpaths
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/reader-current-worker-head.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/reader-current-worker-head.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/reader-current-worker-head.json`
exit=0；elapsed=0.089592524s；预期写面=["W008日志/receipt"]；stop=None。

## reader-current-worker-branch

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/mquant/worker", "symbolic-ref", "--short", "-q", "HEAD"]`
输入边界：已指定reader源码仓库当前binding；status不扫描untracked，diff仅具名readerpaths
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/reader-current-worker-branch.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/reader-current-worker-branch.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/reader-current-worker-branch.json`
exit=0；elapsed=0.084257699s；预期写面=["W008日志/receipt"]；stop=None。

## reader-current-worker-status

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/mquant/worker", "status", "--porcelain=v1", "-uno"]`
输入边界：已指定reader源码仓库当前binding；status不扫描untracked，diff仅具名readerpaths
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/reader-current-worker-status.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/reader-current-worker-status.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/reader-current-worker-status.json`
exit=0；elapsed=0.434490880s；预期写面=["W008日志/receipt"]；stop=None。

## reader-current-worker-reader-diff

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/mquant/worker", "diff", "--no-ext-diff", "--no-textconv", "--", "adt/dbaw.py", "adt/__init__.py"]`
输入边界：已指定reader源码仓库当前binding；status不扫描untracked，diff仅具名readerpaths
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/reader-current-worker-reader-diff.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/reader-current-worker-reader-diff.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/reader-current-worker-reader-diff.json`
exit=0；elapsed=0.081567431s；预期写面=["W008日志/receipt"]；stop=None。

## base-post-frp-head

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp", "rev-parse", "HEAD"]`
输入边界：三个既指定repo最终同范围核验；不扫描其他BASE或untracked
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp-head.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp-head.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-post-frp-head.json`
exit=0；elapsed=0.088903401s；预期写面=["W008日志/receipt"]；stop=None。

## base-post-frp-branch

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp", "symbolic-ref", "--short", "-q", "HEAD"]`
输入边界：三个既指定repo最终同范围核验；不扫描其他BASE或untracked
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp-branch.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp-branch.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-post-frp-branch.json`
exit=0；elapsed=0.083771354s；预期写面=["W008日志/receipt"]；stop=None。

## base-post-frp-status

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp", "status", "--porcelain=v1", "-uno"]`
输入边界：三个既指定repo最终同范围核验；不扫描其他BASE或untracked
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp-status.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp-status.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-post-frp-status.json`
exit=0；elapsed=0.338246361s；预期写面=["W008日志/receipt"]；stop=None。

## base-post-frp-diff

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp", "diff", "--no-ext-diff", "--no-textconv", "--binary"]`
输入边界：三个既指定repo最终同范围核验；不扫描其他BASE或untracked
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp-diff.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp-diff.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-post-frp-diff.json`
exit=0；elapsed=0.087395120s；预期写面=["W008日志/receipt"]；stop=None。

## base-post-frp-cached-diff

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp", "diff", "--cached", "--no-ext-diff", "--no-textconv", "--binary"]`
输入边界：三个既指定repo最终同范围核验；不扫描其他BASE或untracked
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp-cached-diff.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp-cached-diff.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-post-frp-cached-diff.json`
exit=0；elapsed=0.150483706s；预期写面=["W008日志/receipt"]；stop=None。

## base-post-frp_core-head

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp-core", "rev-parse", "HEAD"]`
输入边界：三个既指定repo最终同范围核验；不扫描其他BASE或untracked
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp_core-head.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp_core-head.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-post-frp_core-head.json`
exit=0；elapsed=0.083972518s；预期写面=["W008日志/receipt"]；stop=None。

## base-post-frp_core-branch

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp-core", "symbolic-ref", "--short", "-q", "HEAD"]`
输入边界：三个既指定repo最终同范围核验；不扫描其他BASE或untracked
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp_core-branch.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp_core-branch.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-post-frp_core-branch.json`
exit=0；elapsed=0.087134421s；预期写面=["W008日志/receipt"]；stop=None。

## base-post-frp_core-status

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp-core", "status", "--porcelain=v1", "-uno"]`
输入边界：三个既指定repo最终同范围核验；不扫描其他BASE或untracked
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp_core-status.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp_core-status.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-post-frp_core-status.json`
exit=0；elapsed=0.138475204s；预期写面=["W008日志/receipt"]；stop=None。

## base-post-frp_core-diff

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp-core", "diff", "--no-ext-diff", "--no-textconv", "--binary"]`
输入边界：三个既指定repo最终同范围核验；不扫描其他BASE或untracked
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp_core-diff.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp_core-diff.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-post-frp_core-diff.json`
exit=0；elapsed=0.094274161s；预期写面=["W008日志/receipt"]；stop=None。

## base-post-frp_core-cached-diff

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/edh-universe/frp/frp-core", "diff", "--cached", "--no-ext-diff", "--no-textconv", "--binary"]`
输入边界：三个既指定repo最终同范围核验；不扫描其他BASE或untracked
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp_core-cached-diff.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-frp_core-cached-diff.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-post-frp_core-cached-diff.json`
exit=0；elapsed=0.087335062s；预期写面=["W008日志/receipt"]；stop=None。

## base-post-tis-head

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/mquant/tis", "rev-parse", "HEAD"]`
输入边界：三个既指定repo最终同范围核验；不扫描其他BASE或untracked
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-tis-head.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-tis-head.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-post-tis-head.json`
exit=0；elapsed=0.084584377s；预期写面=["W008日志/receipt"]；stop=None。

## base-post-tis-branch

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/mquant/tis", "symbolic-ref", "--short", "-q", "HEAD"]`
输入边界：三个既指定repo最终同范围核验；不扫描其他BASE或untracked
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-tis-branch.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-tis-branch.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-post-tis-branch.json`
exit=0；elapsed=0.088019942s；预期写面=["W008日志/receipt"]；stop=None。

## base-post-tis-status

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/mquant/tis", "status", "--porcelain=v1", "-uno"]`
输入边界：三个既指定repo最终同范围核验；不扫描其他BASE或untracked
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-tis-status.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-tis-status.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-post-tis-status.json`
exit=0；elapsed=0.502440199s；预期写面=["W008日志/receipt"]；stop=None。

## base-post-tis-diff

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/mquant/tis", "diff", "--no-ext-diff", "--no-textconv", "--binary"]`
输入边界：三个既指定repo最终同范围核验；不扫描其他BASE或untracked
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-tis-diff.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-tis-diff.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-post-tis-diff.json`
exit=0；elapsed=0.088047475s；预期写面=["W008日志/receipt"]；stop=None。

## base-post-tis-cached-diff

cwd: `/dwdhome/fy/BASE_E6_2`
argv: `["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-c", "gc.auto=0", "-C", "/dwdhome/fy/BASE_E6_2/mquant/tis", "diff", "--cached", "--no-ext-diff", "--no-textconv", "--binary"]`
输入边界：三个既指定repo最终同范围核验；不扫描其他BASE或untracked
输出：`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-tis-cached-diff.stdout` / `/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/logs/base-post-tis-cached-diff.stderr`；receipt=`/dwdhome/fy/BASE_E6_2/.oi-runs/OI-EAW-WALL-20261114-01/D004/W008/receipts/base-post-tis-cached-diff.json`
exit=0；elapsed=0.084943891s；预期写面=["W008日志/receipt"]；stop=None。

## 副作用与版本限制

本W直接编译live BASE的相关9模块，原有源码没有写入。BASE共享build/cache/packageDB只读复用，编译输出在W008/build、临时文件在W008/tmp；具名source/input/packageDB metadata与3repo tracked status/diff前后相等。未追踪全盘每次系统调用，不作全BASE/HOME零写证明；旧零外写工程前置已取消。所有实际文件最终体量及nonUTF8类型在FREEZE/PUBLICATION_MANIFEST。现有dirty STCalendar.py/BussinessUtils.hs保留，不覆盖。

当前源码HEAD只是源码绑定；9模块确实由本W编译，外部已装依赖缓存另列ABI metadata，未声称生产二进制全checkout来源完备。未安装依赖、未调用stack重建共享库、未clean/fetch/pull/checkout/reset/rebase/merge/push，未执行生产或自然行情计算。
