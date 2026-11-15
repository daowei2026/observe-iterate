# W005 本地执行报告

outcome=`STOP`；gate=`PREFLIGHT_STOP`；stop=`STOP_SECCOMP_STATIC_PREPARATION_ASSERTION`。
仅完成本地原件交付，不代表W/D003、G-RUN/H3或父任务完成。正式Return尚未生成，return_to只能原E1。

## 实际完成

完整任务6813 bytes/SHA256 `0cc6d0a55603978822feb80811cfc7eda9945f1620710b525326eb8029398db8`核完全一致；完整读取ORDER MD/JSON、签单Return、决定、专业review、当前EP/进度。31项输入映射中23个本地原件逐份bytes/hash核对并镜像；8个exact Git对象在后续Gate前停止，未读。
原W1 thread=`01a1da55-5881-7590-94a1-0661f0236977`；当前turn=`01a1dc6f-c611-7ba1-8301-f0bef1f0eef0`；实际`gpt-6.1-sol/max`，cwd=`/dwdhome/fy/BASE_E6_2`。当前owner PID2890/startticks20139现场一致；fresh预派发idle/canAccept、旧turn终态、Goal null/queue空有控制器原件，当前原生turn_context复核配置。
fresh holder PID246047/startticks47679582/inode14806399现场fdinfo证实FLOCK WRITE；同inode独立O_RDWR FD的NBflock竞争EAGAIN。只关闭自身竞争FD，未重取/替换/释放主控锁。旧PID243622已消失。W005 root先核不存在再独立创建。
真实HOME=/home/dw、CODEX_HOME=/home/dw/.codex始终未重设。主控650bytes sentinel回执逐字/hash核并保存；五个精确负目标只读lstat事前/事后均ENOENT，无预建/写/删。唯一业务写根为D003/W005，旧W4原件/脚本只读。

## 本机常量与精确新停止点

termios.FIOCLEX=21585 (`0x5451`) 与本机asm-generic/ioctls.h定义一致；x86_64、little-endian。模块/header路径、bytes/hash及本机seccomp_data布局检查源均保存在准备器和常量报告。
我编写的`tools/prepare_static.py`在任何runtime/launcher/BPF生成或evaluator之前，对旧W004 trace提取全部FIOCLEX行，错误断言`all('EPERM' in x['text'] for x in trace_lines)`。旧trace第312行是安装前FIOCLEX成功，第1509行才是安装后FIOCLEX EPERM。二者并存不否定本地常量；失败来自Worker准备脚本过强断言。
唯一准备器命令exit1/AssertionError，原生receipt、完整命令与完整traceback已保存。遵守新失败即停，未改/重跑准备器，未扩大allowlist，未启动R0-A1。该停止不是kernel不支持、不是新的ioctl兼容性实测，也不是BPF case已执行失败。

## 未执行范围

W005新runtime/launcher未产生，pure BPF evaluator=0，静态验收未PASS。R0-A1=0，NNP/Landlock/seccomp安装=0，当前FIOCLEX/F_GETFD证据无，九项probe=0，child/grandchild=0，W005 full kernel trace无。
R0-B/C未进入，不判两套closure均失败；四预算预测上界与continuous monitors未证。四PASS均未成立，条件八EP、source staging/patch/local commit、snapshot/DTO、fixture9/18/22、compile-only与synthetic serialization均未实施。没有scenario/normal/DBA/wrapper/native-reader/current生产材料，也未build/test/download/install/push。
23个本地输入及额外控制器原件收尾逐项复核bytes/hash/mtime/inode/dev一致；不以这项具名检查声称扫描全部BASE/HOME或证明kernel全局零外写。命令与自身新增文件路径可复核；无当前kernel trace，confinement/global zero writes明确未PASS。W004的历史安装成功及FIOCLEX EPERM事实冻结保留。

## 交付与路由

所有真实文件在本W005根内。`LOCAL_STAGE_HANDOFF.json`逐字映射ORDER每项deliverable到本地文件，并列真实missing。`PUBLICATION_MANIFEST.json`给绝对路径/sha256/bytes/逐字出版目标；`HASHES.sha256`和外层`FREEZE_RECEIPT.json`封存hash，明确排除自hash循环。
主控逐字运输到`longrun/runs/OI-EAW-WALL-20261114-01/delegations/D003/results/W005/`；Worker无GitHub写权限。目前真实出版commit/ref不存在，result_ref保持null；不生成future/self ref的正式Return。主控出版并回传真实refs后，同原W1同W005仅生成正式v2 Return与validation，再由主控出版`worker_results/W005/WORKER_RETURN.json`，只回`chatgpt:OI-EAW-WALL-20261114-01:executor:E1`。
E1/manager负责专业消费与后续决定。有限Goal完成只表示本地STOP证据已交付，自然结束、不常驻轮询。
