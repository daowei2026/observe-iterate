# W008 Lane A：W007真实收束事实

本W只读核验旧证据，不是W007恢复、重派或Return生成。旧D003/W007专业状态采用已签C0017收束决定；本文件只记本地事实。

主控真实PRE为2026-11-15T04:54:16.056933Z：PID251010/startticks48763578、inode14806399，独立同inode竞争HELD。主控POST为04:55:51.015714Z：keeper实例已消失、kernel旧锁不存在、独立同inode取得并释放成功。原PTY输入尝试遭工具策略拒绝后，主控核仅锁keeper身份，使用pidfd SIGTERM；精确内核unlock时刻未知，keeper exitcode未观测，不能称clean exit0。本W未持有或释放旧锁。

本W现场复核原PID不存在、/proc/locks无旧PID/inode条目；逐份只读核85原件、2,075,599 bytes，与主控具名SHA256全部相等，完整当前metadata/路径见W007_EVIDENCE_RETENTION_MANIFEST.json。原件根保持，未新增W007 Return或final-return，未重跑任何W007脚本。

旧W007保持STOP_R0_B_GIT_DEV_NULL_O_RDWR_EACCES：历史唯一R0-A1 exit0、FIOCLEX/组合锁证明成功；R0-B首个Git内部/dev/null O_RDWR EACCES，Git128/driver1。两closure未实际评估，R0-C/预算/八EP/场景/normal均未进入。这是旧policy下的限域工程事实，不能解释为BASE当前不能直接取材或Wall业务失败。

主控PRE、POST、frozen85-current-verification、原W1只读pre-resource、D004新锁binding均逐字复制在input；各自SHA与拷贝绑定见READONLY_INPUTS_BASELINE.json。C0017签单时资源尚PENDING的叙述是历史时点，现有主控POST已补资源事实，未无痕改写原件。新D004锁只保障本W新增业务单写者，不锁全BASE build/cache。本W未释放/替换新锁。

W007 formal Worker Return不存在；不把local stage report作为formal Return，也不对W007作新的专业接受或补造未发生材料。D003最终专业关闭、manager资源接受仍由原E1/manager负责。
