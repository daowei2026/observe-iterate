#!/usr/bin/env python3
"""Port the locked CYF long-run documents into observe-iterate.

The source checkout is immutable. Exact source copies are stored under
runtime/upstream_cyf. Canonical runtime documents preserve common rules and
replace professional semantics with explicit references.
"""
from __future__ import annotations
import argparse, hashlib, json, shutil
from pathlib import Path
from textwrap import dedent

UPSTREAM_REPO="daowei2026/feature-refinement-implementation-agent-evolution"
UPSTREAM_COMMIT="c6a930887c9148e76ba75f8a026549b9a46c9e35"
DR=Path("agent_evolution/agent_candidates/dual_route_execution")
OV=Path("agent_evolution/agent_candidates/runtime_overlay_candidates/agent_owned_long_horizon_overlay_v0_3")
REL=Path("agent_evolution/agent_candidates/runtime_release_candidates/agent_refinement_runtime_release_candidate_v0_3_20260904")

REFS={
"DR01_A_COMPLEXITY.md":("professional/interfaces/EXPRESSION_AND_COMPLEXITY.md","专业表达与复杂度判断"),
"DR02_AB_SUBSTANTIVE_DEPTH.md":("professional/interfaces/SUBSTANTIVE_DEPTH.md","专业工作的实质细度"),
"DR04_B_ENGINEERING_PACKS.md":("professional/interfaces/ENGINEERING_PACKS.md","Worker／工程任务包"),
"DR05_COMPOSITION_IMPLEMENTATION.md":("professional/interfaces/COMPOSITION_AND_IMPLEMENTATION.md","组合、实施与真实结果交回"),
"DR07_FEATURE_PRODUCTION_ADAPTER.md":("professional/interfaces/EXTERNAL_AGENT_ADAPTER.md","外部专业 Agent 接入"),
"DR10_PRO_IMPLEMENTATION_AND_CODEX_ORDERS.md":("professional/source/04_PRO_WORKER_CODEX_HANDOFF.md","执行 Pro 与 Worker Codex 工单"),
"DR11_CODEX_TWO_ROUTE_EXECUTION_AND_FEEDBACK.md":("professional/source/04_PRO_WORKER_CODEX_HANDOFF.md","Worker Codex 执行与回交"),
"DR12_PROFESSIONAL_QUESTION_CATALOG.md":("professional/interfaces/PROFESSIONAL_QUESTION_CATALOG.md","专业问题目录"),
"DR13_WORK_ARRANGEMENT_AND_CONTEXT.md":("professional/source/00_AGENT_CHARTER_AND_STAGE_CONTRACT.md","I1～I6 工作组织与上下文"),
"03_Mission_A_需求细化长程绑定_v0.3.md":("professional/CURRENT_EXECUTION.md","观察迭代专业执行绑定"),
"04_Mission_B_工程编译长程绑定_v0.3.md":("professional/source/04_PRO_WORKER_CODEX_HANDOFF.md","Worker／证据协作绑定"),
"05_Mission_C_宿主实现长程绑定_v0.3.md":("professional/source/04_PRO_WORKER_CODEX_HANDOFF.md","实施／Worker 协作绑定"),
"06_A_B_C滚动交接_回压与既有产物影响_v0.3.md":("professional/interfaces/HANDOFF_AND_ROUTES.md","角色交接、回压与既有产物影响"),
"08_自然语言运行提示_v0.3.md":("professional/source/INDEX.md","协调者提示与专业来源装配"),
}
OBSOLETE_DR={"DR01_PROFESSIONAL_COMPLEXITY.md","DR02_PROFESSIONAL_SUBSTANTIVE_DEPTH.md","DR04_EXECUTION_PACKS.md","DR07_EXTERNAL_AGENT_ADAPTER.md","DR11_WORKER_CODEX_EXECUTION_AND_FEEDBACK.md"}
OBSOLETE_OV={"01_共享长程执行合同.md","02_Source版本任务授权与人类参与.md","03_专业执行长程绑定.md","04_Worker_Codex协作长程绑定.md","05_独立审查长程绑定.md","06_角色滚动交接_回压与既有产物影响.md","07_Continuation_Branch与上下文控制.md","08_协调者运行入口.md"}

def write(p:Path,s:str): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(s.rstrip()+"\n",encoding="utf-8")
def digest(p:Path): return hashlib.sha256(p.read_bytes()).hexdigest()
def status(p:Path):
    if not p.exists(): return "MISSING"
    s=p.read_text(encoding="utf-8",errors="replace"); h="\n".join(s.splitlines()[:20]).upper()
    if "STATUS: MISSING" in h or ("MISSING" in h and len(s)<500): return "MISSING"
    if "STATUS: PARTIAL" in h or "PARTIAL" in h: return "PARTIAL"
    return "AVAILABLE"

def hdr(src:str,classes:list[str]):
    cs="\n".join(f">   - `{x}`" for x in classes)
    return dedent(f"""
    <!-- CYF_PORT_BEGIN -->
    > **观察迭代长程运行移植候选**
    >
    > - 上游：`{UPSTREAM_REPO}@{UPSTREAM_COMMIT}:{src}`
    > - 精确原文：`runtime/upstream_cyf/{src}`
    > - 本文件是当前规范源；上游原文只用于追溯和同步。
    > - 适配：
    {cs}
    >
    > `UNCHANGED_COMMON` 保留共同运行规则；`GENERIC_ROLE_RENAME` 只改声明性 A/B/C 身份；`PROFESSIONAL_REF_REPLACEMENT` 让专业目标、方法、完成条件和审查题从 `professional/` 与当前有权任务进入；`MISSING_PROFESSIONAL_REF` 表示相关 mode 不得启用。
    <!-- CYF_PORT_END -->
    """).strip()

def common(s:str):
    for a,b in {
      "agent_evolution/agent_candidates/dual_route_execution/":"runtime/dual_route_execution/",
      "agent_evolution/agent_candidates/runtime_overlay_candidates/agent_owned_long_horizon_overlay_v0_3/":"runtime/overlay/",
      "../runtime_overlay_candidates/agent_owned_long_horizon_overlay_v0_3/":"../overlay/",
      "Mission A/B/C":"当前 Binding 声明的专业角色链","A/B/C v0.2":"当前专业包版本","A/B/C":"当前 Binding 声明的专业角色链",
      "A→B→C":"当前 Binding 声明的上游→下游角色链","Mission A":"当前专业定义／观察执行职责",
      "Mission B":"当前证据／工程协作职责","Mission C":"当前实施／Worker 协作职责"}.items(): s=s.replace(a,b)
    return s

def adapter(name:str,src:str,target:Path):
    ref,title=REFS[name]; st=status(target/ref); classes=["PROFESSIONAL_REF_REPLACEMENT"]+(["MISSING_PROFESSIONAL_REF"] if st=="MISSING" else [])
    if name=="08_自然语言运行提示_v0.3.md": return coordinator(src)
    if name=="DR13_WORK_ARRANGEMENT_AND_CONTEXT.md": return work_context(src)
    explanation={"AVAILABLE":"有可读正文，仍须由 Binding 锁 exact 版本。","PARTIAL":"只有部分正文；未定义部分必须回管理／Owner。","MISSING":"专业正文缺失；相关 mode 保持 BLOCKED。"}[st]
    return dedent(f"""
    # {title}

    {hdr(src,classes)}

    ## 1. 生效边界

    本文件保留 CYF 在连续授权、角色分工、真实交付、回交和责任不丢失方面的规则；CYF 的 Feature／RepoFact／Compiler／Host／CEPS 等专业对象不迁入 BI-01。

    - 专业规范源：[`{ref}`](../../{ref})，状态：`{st}`。{explanation}
    - 任务局部专业内容：当前 `QUESTION_WORK_BINDING` 的 `goal_ref`、`full_scope_ref`、`source_reads`、`deliverables_ref`、`completion_ref`、`routes`、`triggers`。
    - 上游专业原文仅在精确副本中保留，不作为当前专业规则。

    ## 2. 保留的共同规则

    1. 委派交清持续工作身份、完整范围、实际输入、接收者、写权、交付、完成条件和回交位置；角色名不能代替任务。
    2. 一项工作可以跨多个 invocation；单轮回答结束不等于工作完成。续作沿原 `work_id`，每次调用使用唯一 `invocation_id` 与 `assignment_token`。
    3. 执行者交真实 Artifact、exact 来源、已完、全部未完、失败／未知和下一段工作；schema 合法、文件存在、测试代码存在都不证明业务完成。
    4. 专业执行、自查、独立审查、管理接收和 Owner 决定分开。参与形成候选的角色不能仅换标题自称 fresh review。
    5. 问题只回压实际受影响部分；未受影响且仍获授权的工作继续。修订要进入规范／任务实物并被后继消费。
    6. 主控只运输已经形成的 Binding／Return／route，不补 scope、优先级、完成标准或 finding。

    ## 3. 专业内容入口

    依次读取 Owner 当前要求、`professional/CURRENT_EXECUTION.md`、`professional/source/INDEX.md` 命中的稳定正文、当前 Binding 的 exact `source_reads`／`completion_ref`，以及本轮真实 Artifact／Return／接收决定。缺项如实返回，不用 CYF 上游专业正文或旧聊天记忆补造。

    ## 4. 角色回交

    专业执行者交实质结果、证据、自查和 continuation；Worker 只交技术执行事实；独立审查者只读复核 exact 对象；管理 Pro 对完整目标和 Gate 作决定并落实后继；主控核身份、版本、Return、实物和 route。只有专业引用非 MISSING、Binding 完整、角色／写面／Return 已明确且路径经过验证时，相关 mode 才能启用。
    """).strip()+"\n"

def work_context(src:str):
    return dedent(f"""
    # 固定专业问题怎样组成连续工作：安排、上下文与管理

    {hdr(src,["UNCHANGED_COMMON","GENERIC_ROLE_RENAME","PROFESSIONAL_REF_REPLACEMENT"])}

    ## 1. 身份边界

    完整目标、阶段／专业职责、持续工作、本轮重点、一次调用和小里程碑分别管理。一次调用结束、一个图生成、一个局部问题修复或 Gate 候选出现，都不缩小完整目标或清除未完责任。

    ## 2. 形成工作

    Owner 提供目标与授权；管理 Pro 从完整目标和真实现状形成计划、连续工作、完成条件、routes 与投入预期；专业执行 Pro决定授权内部步骤；Worker 只执行具名工单；主控只装配已形成内容。新工作用 DR14 `BOOTSTRAP`，管理形成实质计划后签 `BINDING`；缺目标／授权时只返回缺项。

    ## 3. 专业工作组合

    不再采用固定 A／B／C 三段。当前专业阶段、Input／Output／Gate 以 `professional/source/00_AGENT_CHARTER_AND_STAGE_CONTRACT.md` 的 I1～I6 及本次 Binding 为准。I1～I3、I4、阶段交接、Pro／Worker 协作和角色 Gate 分别读取 `professional/source/01`～`05`。发现实际输入、结果或方法问题时只定向回受影响阶段，不清零仍成立成果。

    ## 4. 上下文读取

    输入分固定运行合同、稳定专业方法、当前任务材料和运行时结果四层。首次或新上下文读取当前角色完整适用正文；同上下文已读、版本未变且仍适用可复用；重点变化时定向回读；不默认加载全部历史。`source_reads` 必须表达 exact 来源、要求、用途和复用证据；可定位、已读取、已使用和结果成立是不同事实。

    ## 5. 管理题

    **M-START**：恢复完整目标、已有实物和专业合同，交全部重要剩余、当前连续安排、Owner事项、投入预期和正式 Binding。**M-REASSESS**：重要结果、边界变化、长期无实质进展或投入触发时，实质决定停止／保留／重排／审查／Owner事项并修改后继。**M-CLOSE**：核完成范围、未完、证据、审查、实际消费和完整终点；局部结果、schema PASS 或执行者自评不自动关闭。

    ## 6. 触发与并存责任

    RESULT／CHANGE／EFFORT 等触发必须来自 Binding 与实际事实。主控识别机械条件并派既定接收者，不裁业务重要性。普通 continuation、已签独立审查和到期管理复看可并存；一个动作不能覆盖其他有效责任。

    ## 7. 采用和恢复

    已有用例恢复真实已完成、已审、在途和未完，不补造历史 Return 或因迁移从零开始。规则变化只影响实际受影响部分，新版从下一次合法调用生效。题号、阶段名、文件数、轮数、代码量和进度标签都不能代替专业完成。
    """).strip()+"\n"

def coordinator(src:str):
    return dedent(f"""
    # 自然语言运行提示：观察迭代协调者入口

    {hdr(src,["UNCHANGED_COMMON","GENERIC_ROLE_RENAME","PROFESSIONAL_REF_REPLACEMENT"])}

    ## 1. 只装配已形成内容

    协调者读取锁定版本、`runtime/config/COORDINATOR_DISPATCH.json`、当前 Binding、最近合法 Return 和真实发送／收取事实。它不根据专业材料临时编任务，不改变 scope、优先级、完成标准、finding、Gate 或 Owner 权限。专业正文由 `professional/` 与本次 `source_reads` 提供；运行新结果由 Artifact／Return 提供。

    ## 2. 输入顺序

    Owner 当前要求与授权 → 固定运行合同 → 稳定专业合同 → 当前 task／Binding → 本轮发送、回答、Artifact、Return、检查与采用状态。已读且未变的稳定材料可复用；新上下文必须实际取得所需正文。路径存在不等于读取和使用。

    <!-- MANAGEMENT_DUTY_BEGIN -->
    你是管理 Pro。以 Owner 完整目标为起点，独立核成果、全部重要剩余、优先级、投入、Gate 和真实后继；使用当前专业合同与实际结果，不把执行者自评或状态标签当接收。把决定落实为有权任务、接收／返修／等待或 Owner 事项，并按 DR14 回交。
    <!-- MANAGEMENT_DUTY_END -->

    <!-- PROFESSIONAL_DUTY_BEGIN -->
    你是当前 Binding 指定的专业执行 Pro。读取目标、范围、source_reads、专业方法、数据／Case／As-Of、交付和完成条件；在授权内连续形成实质专业结果，必要时签 Worker 工单。交 Artifact、证据、自查、已完／未完、限制和 continuation；不得自签管理 Gate。
    <!-- PROFESSIONAL_DUTY_END -->

    <!-- REVIEW_DUTY_BEGIN -->
    你是独立审查 Pro。用 fresh、只读上下文，从权威目标、专业方法和直接证据恢复 expected；被审报告只作定位。交 findings、证据、影响、未覆盖、判定和 route；不代写候选、不冒充管理接收或 Owner 决定。
    <!-- REVIEW_DUTY_END -->

    <!-- WORKER_DUTY_BEGIN -->
    你是 Worker Codex。只执行已签发工单中的计算、制图、调查、代码、构建、测试或真实运行；保留 exact 输入、命令、输出、失败、未执行和回交。不得选择新业务问题、修改专业方法或判断 Gate。
    <!-- WORKER_DUTY_END -->

    ## 3. 组装、发送与返回

    每条消息由固定角色正文、当前 task／continuation 原文、exact 来源和 Return 要求组成。普通续作不附管理职责；管理调用不重复灌历史；审查调用明确 exact 对象与独立性；Worker 必须有工单和写面。准备后核 digest 与 exact bytes；已 committed 消息只逐字恢复；未知发送状态禁止重发。回答交 `ROLE_RETURN`，采用 question-work 时同时交 `QUESTION_WORK_RETURN`。主控按 Overlay13 bind、去重、parse、validate、decide、record、continue；schema 合法不证明业务正确。
    """).strip()+"\n"

def canonical(src:Path,rel:str,target:Path):
    if src.name in REFS: return adapter(src.name,rel,target)
    return hdr(rel,["UNCHANGED_COMMON","GENERIC_ROLE_RENAME","PROFESSIONAL_REF_REPLACEMENT"])+"\n\n"+common(src.read_text(encoding="utf-8"))

def copytree(src:Path,dst:Path):
    if dst.exists(): shutil.rmtree(dst)
    shutil.copytree(src,dst)
    return [{"path":p.as_posix(),"size":p.stat().st_size,"sha256":digest(p)} for p in sorted(dst.rglob("*")) if p.is_file()]

def main():
    a=argparse.ArgumentParser(); a.add_argument("--source",required=True); a.add_argument("--target",required=True); x=a.parse_args()
    source=Path(x.source).resolve(); target=Path(x.target).resolve(); roots=[DR,OV,REL]
    for r in roots:
        if not (source/r).exists(): raise SystemExit(f"missing upstream {r}")
    up=target/"runtime/upstream_cyf"; shutil.rmtree(up,ignore_errors=True); files=[]
    for r in roots: files+=copytree(source/r,up/r)
    od=target/"runtime/dual_route_execution"; oo=target/"runtime/overlay"; od.mkdir(parents=True,exist_ok=True); oo.mkdir(parents=True,exist_ok=True)
    for n in OBSOLETE_DR:
        if (od/n).exists(): (od/n).unlink()
    for n in OBSOLETE_OV:
        if (oo/n).exists(): (oo/n).unlink()
    for p in sorted((source/DR).iterdir()):
        if p.is_file(): write(od/p.name,canonical(p,(DR/p.name).as_posix(),target) if p.suffix==".md" else p.read_text())
    for p in sorted((source/OV).iterdir()):
        if p.is_file(): write(oo/p.name,canonical(p,(OV/p.name).as_posix(),target) if p.suffix==".md" else p.read_text())
    cfg={"schema":"observation-iteration-coordinator-dispatch/v2","repository":"daowei2026/observe-iterate","policy_path":"runtime/overlay/08_自然语言运行提示_v0.3.md","works":{"bi-01-observation-iteration":{"stage":"I4","allowed_roles":["management","professional","review","worker"],"modes":{"MANAGEMENT":{},"PROFESSIONAL_EXECUTION":{},"INDEPENDENT_REVIEW":{},"WORKER_EXECUTION":{}},"goal_ref":"professional/source/00_AGENT_CHARTER_AND_STAGE_CONTRACT.md","professional_entry":"professional/CURRENT_EXECUTION.md","fixed_refs":["professional/source/INDEX.md","runtime/dual_route_execution/DR14_QUESTION_WORK_CONTRACT.md","runtime/overlay/13_角色回交与主控接续协议.md"]}}}
    write(target/"runtime/config/COORDINATOR_DISPATCH.json",json.dumps(cfg,ensure_ascii=False,indent=2))
    write(target/"runtime/config/WORKMAP_BINDING.json",json.dumps({"schema":"observation-workmap-binding/v2","status":"NOT_INITIALIZED","manager_role":"management","rule_paths":["runtime","professional"],"streams":{},"note":"首次真实管理任务形成后再初始化；不得从旧索引补造历史。"},ensure_ascii=False,indent=2))
    gaps=[]
    for p in sorted((target/"professional/interfaces").glob("*.md")):
        st=status(p)
        if st!="AVAILABLE": gaps.append({"path":p.relative_to(target).as_posix(),"status":st})
    write(target/"migration/ADAPTATION_STATUS.json",json.dumps({"schema":"observe-iterate-cyf-port/v1","upstream_repo":UPSTREAM_REPO,"upstream_commit":UPSTREAM_COMMIT,"canonical_runtime":["runtime/dual_route_execution","runtime/overlay"],"upstream_copy":"runtime/upstream_cyf","professional_gaps":gaps,"program_adaptation":"PARTIAL_EXISTING_GENERIC_CORE","schema_tests":"REQUIRES_NEXT_STEP","end_to_end":"NOT_EXECUTED","upstream_file_count":len(files)},ensure_ascii=False,indent=2))
    rows=["# CYF Runtime File Map","",f"Locked upstream: `{UPSTREAM_REPO}@{UPSTREAM_COMMIT}`","","| 当前规范源 | 精确上游副本 |","|---|---|"]
    for d,r in ((od,DR),(oo,OV)):
        for p in sorted(d.glob("*")):
            if p.is_file(): rows.append(f"| `{p.relative_to(target)}` | `runtime/upstream_cyf/{r}/{p.name}` |")
    write(target/"migration/CYF_RUNTIME_FILE_MAP.md","\n".join(rows))
    write(target/"runtime/README.md","# Runtime\n\n`dual_route_execution/` 和 `overlay/` 是适配后的完整规范源；`upstream_cyf/` 保存锁定 CYF 原文，只供追溯与同步，不能作为第二套热规则。专业内容从 `../professional/` 和当前 Binding 进入。程序、Schema、测试与 Release 仍按 `migration/ADAPTATION_STATUS.json` 的状态继续处理。\n")
    test=target/"runtime/overlay/tests/test_runtime_port_integrity.py"
    write(test,dedent('''
    import unittest
    from pathlib import Path
    ROOT=Path(__file__).parents[3]
    class T(unittest.TestCase):
        def test_docs_not_shells(self):
            for d in (ROOT/"dual_route_execution",ROOT/"overlay"):
                for p in d.glob("*.md"):
                    self.assertGreater(len(p.read_text(encoding="utf-8")),900,p)
                    self.assertIn("CYF_PORT",p.read_text(encoding="utf-8"),p)
        def test_exact_upstream_copy(self):
            self.assertTrue((ROOT/"upstream_cyf/agent_evolution/agent_candidates/dual_route_execution/DR06_SUBSTANTIVE_MANAGEMENT.md").exists())
    if __name__=="__main__": unittest.main()
    '''))
    return 0
if __name__=="__main__": raise SystemExit(main())
