# BI-01 V2 R0010：固定图数上的连续实证观察

work_id: BI-01
run_id: BI-01-V2-01
task_id: BI01-V2-S123-OBSERVATION-01
invocation_id: BI01-V2-01-R0010-9c54d7a73e2bd619ee5d9f47
assignment_token: 99ff37c6ea307fb90ba24f046e
role: professional
professional_mode: OBSERVATION_SCOPE

## 当前资格与目的

本文件保存本次真实新读图数形成的业务认识，并在同一完整任务内继续补充；不是阶段完成或独立接收。完整目的仍是U2共同机会位置/成员/可知边界及U3 Progress/Friction/Retention/ObservabilityAndConstraint的合理性、反证、与Node-only/静态组/简单共同事件关联的增量。固定两包不重算，原Worker已完成，不重派。

实际采用c67bbfa80cac9bfcb55cce20e44697333a292030的R9安排。edbd2d7447feade55e523067b6d86aac27cf7d0c的R8/LATE_RETURN_DISPOSITION.json已经直接读取：迟到R8的真实正文可用于减少经核实未完，不覆盖R9安排，也不声称F08—F14已管理接受。本专业上下文确有R8原答及真实工具数据，后继按各项实际阅读范围复用，未读价格/时序不能因MEM已读而划销。

图数源固定为observe-iterate@b9ecbfa4b27f40365ed72f35448116420fb085a6:runs/BI-01-V2-01/artifacts/worker-R0004/readable_views/REQUESTED_51_CURRENT/；节点/页面和包版本用1917f868d61f8de7110b7165ee9125e5b156c4d2的final索引。known整行不代表全部辅助字段当时可知，未来完成代理只作明确的事后追溯。本轮不声称AI看像素。

## P10-01：等actual候选未覆盖，不等于已经漏掉共同机会

### 具体位置与原数据

节点UNCOVERED_01，原选C0物理708行（i）；actual为2021-01-04 22:30，As-Of为2021-01-05 11:30，显示范围2021-01-04 09:30至2021-01-07 11:30。实际读取同节点VIEW的起止、价格和C0图层合同，以及SOURCE_BINDING的C0/N映射段；未把长VIEW截断部分声明全读。

同图原件：

- `UNCOVERED_01/plot_view_data/fixed__UNCOVERED_01__known__N_WORKING_ORIGIN.csv`全文，Git blob b32608c96657c5df46ce274f7d49f2070f931b71。
- `UNCOVERED_01/plot_view_data/fixed__UNCOVERED_01__known__i-ohlc.csv`全文，Git blob 6644c390284e9b15dc493bbac368e687fea836bf。

原起点表给出：i的Peak/Down actual为1月4日22:30、actual_price1034，confirm point为1月5日11:00、confirm_price1020.5，source_event/knowledge proxy为11:30。原源为A包`baseline_U2_C0_N_C1/C0/02_turn_occurrences.csv`物理708行。

同一As-Of，rb/hc的当前起点仍分别是物理2/365行的InitialUndirected，actual为1月4日09:30，expected_direction为空，direction_knownness=UnsupportedInitialization。不能根据它们的价格或已有非空路径比例填出原本没有的方向。

i同图OHLC物理12/17/18行分别为1月4日22:30 close1034、1月5日11:00 close1020.5、11:30 close1022.5；这些行的_aidata_source_row也为12/17/18，原B成员SHA256为eb4b628c59587252253a14f2e77314546652634379000ca0f879f0d1668e799e。原KLine实际有从1034到较低收盘的过程，但该起点不是在actual时点便已知，且局部过程并非每根单调。

### 业务认识、反证与限制

事实：该原turn不在等actual候选索引中；在其自身知识截面，i已有可解释的有方向起点，而另外两品种的当前原起点仍无方向。

CaseFinding：这一项未覆盖不能记成三品种共同方向机会的漏检。共同组织尚缺另外对象当时有方向的起点/关系依据；价格自身有运动不替代原特征方向资格。与此同时，i的单品种事实仍可被N和原价格单独消费，无须为了保留它先生成一个组。

对设计的支持：保留No comparable direction/初始化/单品种已知三种差别；U2不应成为单品种事实的唯一入口。相对静态三品种分类，这里准确说明共同方向尚无依据；相对已有C0/N，未形成新增行情事实。

反证边界：不能据另外两品种方向未定推断它们实际没有同向行情，也不否定其他特征/不同临近窗口存在可解释关系。后续价格及其他已选未覆盖窗口继续检验，不将本例推广为所有未覆盖turn都合理。

### 已知后继

继续其余10个未覆盖窗口，特别区分：当前方向相反、同向但actual不同、原目标已结束/被新N替代、输入初始化；再将这些组织问题与已有C1组外对照相连。原35个C1和主Case五截面、F05正反例及四束全目标综合仍在完整责任内；本项保存后不停工。
