"""Real local Git/CLI regressions. No phone, model run or business acceptance."""
from pathlib import Path
import copy, importlib.util, json, subprocess, sys, tempfile, unittest

O = Path(__file__).resolve().parents[1]
REPO = O.parents[3]
TOOL = O / "tools/management_prompt.py"
spec = importlib.util.spec_from_file_location("mp", TOOL)
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)


class DispatchTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        self.git("init", "-q"); self.git("config", "user.name", "Fixture"); self.git("config", "user.email", "fixture@example.invalid")
        self.write(m.POLICY_PATH, (O / "08_自然语言运行提示_v0.3.md").read_text(encoding="utf-8"))
        self.write("goal.md", "<!-- OWNER_BEGIN -->原始目的：重新判断两路分工并完成B。<!-- OWNER_END -->")
        self.write("task.md", "当前完整工程任务；不是模型数量。")
        self.write("receiver-task.md", "独立只读接收当前完整工程和任务包。")
        self.write("adoption.md", '<a id="adopt"></a>管理决定采用当前任务。')
        self.write("plan.md", '<a id="decision"></a>旧管理决定：先补模型。\n<a id="effort"></a>原估计两次，完整目标不变。')
        self.write("work.md", '<a id="scope"></a>完整scope。\n<a id="same"></a>按完整任务继续。\n<a id="receiver"></a>只读接收任务。\n<a id="progress-route"></a>本次只处理一次进度。\n<a id="repair"></a>只补原管理交付。')
        self.write("original-prompt.md", "work_id: w\ninvocation_id: original-management\nassignment_token: old\nrole: management\nrecipient: management-chat\n当前阶段：Mission B\n")
        self.write("issue.md", "原管理调用缺少返回和binding。")
        self.write("missing.md", "需补原管理返回。")
        self.git("add", "."); self.git("commit", "-qm", "source")
        self.base = self.git("rev-parse", "HEAD").strip()
        self.loc = lambda p, s="full", ref=None: {"repo":"test/repo", "commit":ref or self.base, "path":p, "selector":s}
        route = lambda role, anchor, recipient=None: {"recipient_role":role, "recipient_ref":recipient or role+"-chat", "instructions_ref":self.loc("work.md", anchor)}
        common = {
          "schema":"question-work/v2", "kind":"BINDING", "work_id":"w",
          "goal_ref":self.loc("plan.md", "#decision"), "plan_ref":self.loc("plan.md", "#decision"),
          "budget_ref":self.loc("plan.md", "#effort"), "full_scope_ref":self.loc("work.md", "#scope"),
          "focus_ref":self.loc("work.md", "#same"), "deliverables_ref":self.loc("work.md", "#scope"),
          "completion_ref":self.loc("work.md", "#scope")}
        self.binding = common | {"professional_mode":"ENGINEERING_PACKAGE",
          "routes":{"same_work":route("professional", "#same"), "accept":route("management", "#same", "management-chat"),
                    "decide":route("management", "#progress-route", "management-chat"),
                    "return_repair":route("management", "#repair", "management-chat")},
          "triggers":[{"trigger_id":"RESULT-REVIEW", "route":route("management", "#progress-route", "management-chat")}]}
        self.receiver_binding = common | {"professional_mode":"read-only design receiver / review",
          "focus_ref":self.loc("work.md", "#receiver"),
          "routes":{"same_work":route("review", "#receiver", "receiver-chat"),
                    "accept":route("management", "#progress-route", "management-chat"),
                    "decide":route("management", "#progress-route", "management-chat"),
                    "return_repair":route("review", "#repair", "receiver-chat")}, "triggers":[]}
        self.write("binding.json", json.dumps(self.binding))
        self.write("receiver-binding.json", json.dumps(self.receiver_binding))
        cfg = {"schema":"coordinator-dispatch/v3", "repository":"test/repo", "works":{"w":{
            "stage":"B", "modes":{
              "ENGINEERING_PACKAGE":{"display_name":"Mission B 工程细化与任务包编制", "purpose":"professional_work"},
              "read-only design receiver / review":{"display_name":"Mission B 独立只读设计接收", "purpose":"read_only_reception"}},
            "goal_ref":{"path":"goal.md", "selector":"marker:OWNER"}}}}
        self.write("config.json", json.dumps(cfg))
        self.git("add", "."); self.git("commit", "-qm", "binding and policy")
        self.ref = self.git("rev-parse", "HEAD").strip()
        self.event = {"work_id":"w", "invocation_id":"new-01", "assignment_token":"existing-token",
          "binding_ref":self.loc("binding.json", ref=self.ref), "route":"trigger:RESULT-REVIEW",
          "send_state":"NOT_SENT", "dispatch_kind":"NORMAL",
          "current_task_ref":self.loc("task.md", ref=self.ref),
          "task_adoption_ref":self.loc("adoption.md", "#adopt", self.ref)}

    def write(self, p, s):
        q = self.repo / p; q.parent.mkdir(parents=True, exist_ok=True); q.write_text(s, encoding="utf-8")
    def git(self,*a): return subprocess.check_output(["git","-C",str(self.repo),*a],stderr=subprocess.PIPE).decode()
    def make(self, e=None): return m.prepare_dispatch(self.repo,self.ref,"config.json",self.event if e is None else e)
    def commit(self, message="update"):
        self.git("add", "."); self.git("commit", "-qm", message); return self.git("rev-parse", "HEAD").strip()

    def test_later_management_keeps_duty_goal_and_management_stage(self):
        a=self.make(); e=copy.deepcopy(self.event); e["invocation_id"]="new-02"; b=self.make(e)
        self.assertTrue(a["message"].startswith("[new-01]\n"))
        self.assertTrue(b["message"].startswith("[new-02]\n"))
        for p in (a,b):
            self.assertIn("特征实际落地和完整阶段收拢是第一优先",p["message"])
            self.assertIn("重新判断两路分工",p["message"])
            self.assertIn("检查完整工程是否覆盖全部业务Feature",p["message"])
            self.assertNotIn("每次实质业务推进",p["message"])
            self.assertIn("原投入与复看条件",p["message"])
            self.assertFalse(p["sent"]); self.assertFalse(p["semantic_review_passed"])

    def test_fixed_goal_cannot_be_supplied_or_replaced(self):
        for key in ("goal","text","request","role","stage"):
            e=copy.deepcopy(self.event); e[key]="只修当前模型"
            with self.subTest(key=key),self.assertRaises(ValueError):self.make(e)
        p=self.make(); self.assertNotIn("## Owner完整目的\n\n旧管理决定",p["message"])

    def test_dynamic_task_is_not_frozen_to_policy_commit(self):
        self.write("task.md", "管理刚采用的新任务T2。")
        self.write("adoption.md", '<a id="adopt"></a>管理明确将T1修订为T2。')
        newer=self.commit("adopt task T2")
        e=copy.deepcopy(self.event); e["current_task_ref"]=self.loc("task.md",ref=newer);e["task_adoption_ref"]=self.loc("adoption.md","#adopt",newer)
        p=self.make(e)
        self.assertIn("@"+newer+":task.md::full",p["message"])
        self.assertEqual(p["policy_commit"],self.ref)
        source_keys={(x['commit'],x['path'],x['selector']) for x in p['sources']}
        self.assertEqual(len(source_keys),len(p['sources']))

    def test_professional_keeps_own_duty_without_management_duty(self):
        e=copy.deepcopy(self.event); e["route"]="same_work"; p=self.make(e)
        self.assertNotIn("你负责完整任务在合理轮次",p["message"])
        self.assertIn("每次实质业务推进",p["message"]); self.assertEqual(p["role"],"professional")

    def test_real_receiver_mode_gets_read_only_prompt_not_engineering_prompt(self):
        e=copy.deepcopy(self.event);e["binding_ref"]=self.loc("receiver-binding.json",ref=self.ref);e["route"]="same_work"
        e["current_task_ref"]=self.loc("receiver-task.md",ref=self.ref)
        p=self.make(e)
        self.assertEqual(p["stage"],"B");self.assertEqual(p["role"],"review")
        self.assertIn("先检查工程是否服务完整阶段目标",p["message"])
        self.assertNotIn("每次实质业务推进",p["message"])
        self.assertNotIn("继续完成已指派的工作",p["message"])

    def test_checked_in_r47_binding_uses_real_read_only_mode_and_prompt(self):
        case=REPO/'agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3'
        binding=json.loads((case/'reviews/u3-management-r47/QUESTION_WORK_BINDING.json').read_text())
        config=json.loads((case/'COORDINATOR_DISPATCH.json').read_text())
        work=config['works'][binding['work_id']]
        definition=m.mode_definition(work,binding['professional_mode'])
        role=binding['routes']['same_work']['recipient_role']
        body=m.role_body((O/'08_自然语言运行提示_v0.3.md').read_text(),role,work['stage'])
        self.assertEqual(definition['purpose'],'read_only_reception')
        self.assertEqual(role,'review')
        self.assertIn('先检查工程是否服务完整阶段目标',body)
        self.assertNotIn('每次实质业务推进',body)

    def test_checked_in_u2_r60_binding_uses_real_read_only_mode_and_prompt(self):
        case=REPO/'agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3'
        binding=json.loads((case/'reviews/u2-management-81ec8151/QUESTION_WORK_BINDING.json').read_text())
        config=json.loads((case/'COORDINATOR_DISPATCH.json').read_text())
        work=config['works'][binding['work_id']]
        definition=m.mode_definition(work,binding['professional_mode'])
        role=binding['routes']['same_work']['recipient_role']
        body=m.role_body((O/'08_自然语言运行提示_v0.3.md').read_text(),role,work['stage'])
        self.assertEqual(binding['professional_mode'],'INDEPENDENT_AUDIT')
        self.assertEqual(definition['purpose'],'read_only_reception')
        self.assertEqual(role,'review')
        self.assertIn('独立检查完整业务合同的形成方法',body)
        self.assertNotIn('本轮主任务是把投资业务需求',body)

    def bootstrap_event(self):
        cfg=json.loads((self.repo/"config.json").read_text())
        cfg["works"]["w"]["modes"]["M-START"]={"display_name":"首次实质管理", "purpose":"professional_work"}
        cfg["works"]["w"]["goal_ref"]=self.loc("goal.md", "marker:OWNER")
        self.write("config.json", json.dumps(cfg))
        self.write("questions.md", '<a id="m-start"></a>按完整目标形成实际管理安排。')
        question_ref=self.commit("bootstrap method")
        b={"schema":"question-work/v2","kind":"BOOTSTRAP","work_id":"w",
           "goal_ref":self.loc("goal.md","marker:OWNER"),"authority_ref":self.loc("adoption.md"),
           "entry_sources":[self.loc("task.md")],"existing_work_refs":[],
           "parent":{"status":"NOT_APPLICABLE_NEW_CASE","ref":None,"reason_ref":self.loc("task.md")},
           "recipient_ref":"management-chat","return_to_ref":"controller",
           "question_ref":self.loc("questions.md","#m-start",question_ref),
           "instructions_ref":self.loc("task.md")}
        self.write("bootstrap.json",json.dumps(b));self.ref=self.commit("bootstrap input")
        e=copy.deepcopy(self.event);e["binding_ref"]=self.loc("bootstrap.json",ref=self.ref);e["route"]="same_work"
        return e,b

    def test_bootstrap_transports_management_without_invented_plan(self):
        e,_=self.bootstrap_event();p=self.make(e)
        self.assertEqual(p["role"],"management");self.assertEqual(p["recipient"],"management-chat")
        self.assertEqual(p["mode"],"M-START")
        self.assertIn("特征实际落地和完整阶段收拢是第一优先",p["message"])
        self.assertIn("M-START完整题面",p["message"])
        self.assertNotIn("原投入与复看条件",p["message"])
        self.assertNotIn("上次管理安排",p["message"])
        m.verify(p,p["message"].encode());m.verify_recipient(p,"management-chat")
        with self.assertRaisesRegex(ValueError,"MESSAGE_CHANGED"):m.verify(p,p["message"].encode()+b" ")

    def test_bootstrap_rejects_other_routes_and_unauthorized_delivery_repair(self):
        e,_=self.bootstrap_event()
        for route in ("accept","trigger:RESULT-REVIEW","return_repair"):
            bad=copy.deepcopy(e);bad["route"]=route
            with self.subTest(route=route),self.assertRaisesRegex(ValueError,"BOOTSTRAP_MANAGEMENT_ROUTE_REQUIRED"):self.make(bad)
        bad=copy.deepcopy(e);bad["dispatch_kind"]="DELIVERY_REPAIR"
        with self.assertRaisesRegex(ValueError,"BOOTSTRAP_MANAGEMENT_ROUTE_REQUIRED"):self.make(bad)

    def test_bootstrap_requires_sources_and_fixed_goal(self):
        e,b=self.bootstrap_event()
        for change,error in (({"entry_sources":[]},"BOOTSTRAP_ENTRY_SOURCES_REQUIRED"),
                             ({"goal_ref":self.loc("task.md")},"BOOTSTRAP_FIXED_GOAL_MISMATCH"),
                             ({"parent":{"status":"PRESENT","ref":None,"reason_ref":self.loc("task.md")}},"BOOTSTRAP_PARENT_REFERENCE")):
            self.write("bootstrap.json",json.dumps(b|change));ref=self.commit("invalid bootstrap")
            bad=copy.deepcopy(e);bad["binding_ref"]=self.loc("bootstrap.json",ref=ref)
            with self.subTest(error=error),self.assertRaisesRegex(ValueError,error):self.make(bad)

    def repair_event(self, route="return_repair"):
        e=copy.deepcopy(self.event);e["route"]=route;e["dispatch_kind"]="DELIVERY_REPAIR"
        e.pop("current_task_ref");e.pop("task_adoption_ref")
        e["repair_context"]={"original_dispatch_ref":self.loc("original-prompt.md",ref=self.ref),
          "issue_ref":self.loc("issue.md",ref=self.ref),"missing_output_refs":[self.loc("missing.md",ref=self.ref)]}
        return e

    def test_delivery_repair_is_narrow_and_returns_to_original_role(self):
        p=self.make(self.repair_event())
        self.assertIn("本轮只补原调用具体交付缺件",p["message"])
        self.assertIn("具体缺件检查",p["message"])
        self.assertNotIn("读取本次原始要求和生效完整任务",p["message"])
        self.assertNotIn("Owner完整目的",p["message"])

    def test_management_delivery_cannot_be_sent_to_professional(self):
        with self.assertRaisesRegex(ValueError,"DELIVERY_REPAIR_ROLE_MISMATCH"):
            self.make(self.repair_event("same_work"))

    def test_latest_complete_answer_and_machine_return_are_separate(self):
        ret={"schema":"question-work/v2","kind":"RETURN","work_id":"w","binding_ref":self.event["binding_ref"],
             "continuation_ref":{"answer_ref":"#continuation"}}
        self.write("response.md",'<a id="continuation"></a>继续完整任务。\n<a id="question-work-return"></a>\n```json\n'+json.dumps(ret)+'\n```\n')
        ref=self.commit("response")
        e=copy.deepcopy(self.event);e["route"]="same_work"
        e["latest_return_ref"]=self.loc("response.md","#question-work-return",ref)
        e["latest_response_ref"]=self.loc("response.md","full",ref)
        p=self.make(e)
        self.assertIn("最新完整回答",p["message"]);self.assertIn("原任务内最新接续",p["message"])
        self.assertNotIn("最新完整回交：`test/repo@"+ref+":response.md::#question-work-return`",p["message"])

    def test_github_relay_preserves_full_assignment_without_inline_duplication(self):
        p = self.make()
        self.write("archived-message.md", p["message"])
        published = self.commit("complete full task on GitHub")
        loc = self.loc("archived-message.md", ref=published)
        out = m.github_reference_message(self.repo, p, loc)
        self.assertEqual(out["message_transport"], "github_reference")
        self.assertEqual(out["message"].split("\n\n", 1)[0], p["message"].split("\n\n", 1)[0])
        self.assertIn(published + ":archived-message.md::full", out["message"])
        self.assertNotIn("当前完整工程任务", out["message"])
        self.assertNotIn("## Owner完整目的", out["message"])
        self.assertEqual(out["inline_message_sha256"], p["message_sha256"])
        m.verify(out, out["message"].encode("utf-8"))
        self.write("archived-message.md", p["message"] + "mutated")
        changed = self.commit("changed archive")
        with self.assertRaisesRegex(ValueError, "DIFFERS_FROM_PREPARED"):
            m.github_reference_message(self.repo, p, self.loc("archived-message.md", ref=changed))
        with self.assertRaisesRegex(ValueError, "FULL_TEXT_REQUIRED"):
            m.github_reference_message(self.repo, p, self.loc("archived-message.md", "L1-L2", published))

    def test_standalone_github_report_role_and_question_returns(self):
        self.write("report.md", '<a id="continuation"></a>同一有权任务继续。\n')
        report_sha = self.commit("full professional report")
        qret = {"schema": "question-work/v2", "kind": "RETURN", "work_id": "w",
                "invocation_id": "prior-real-turn", "binding_ref": self.event["binding_ref"],
                "continuation_ref": self.loc("report.md", "#continuation", report_sha)}
        self.write("question.json", json.dumps(qret))
        question_sha = self.commit("independent question return")
        role = {"schema": "longrun-return/v1", "work_id": "w",
                "invocation_id": "prior-real-turn", "assignment_token": "prior-real-token",
                "question_work_ref": "github:test/repo@" + question_sha + ":question.json::full"}
        self.write("role.json", json.dumps(role))
        role_sha = self.commit("independent role return")
        e = copy.deepcopy(self.event); e["route"] = "same_work"
        e["latest_return_ref"] = self.loc("question.json", ref=question_sha)
        e["latest_response_ref"] = self.loc("report.md", ref=report_sha)
        with self.assertRaisesRegex(ValueError, "GITHUB_ROLE_RETURN_REQUIRED"):
            self.make(e)
        e["latest_role_return_ref"] = self.loc("role.json", ref=role_sha)
        p = self.make(e)
        self.assertIn("同一有权任务继续", p["message"])
        self.assertIn("最新结构化问题回交", p["message"])
        self.assertIn("最新角色回交", p["message"])
        wrong = dict(role, question_work_ref="github:test/repo@" + report_sha + ":question.json::full")
        self.write("role.json", json.dumps(wrong))
        bad_sha = self.commit("wrong question reference")
        e["latest_role_return_ref"] = self.loc("role.json", ref=bad_sha)
        with self.assertRaisesRegex(ValueError, "GITHUB_QUESTION_RETURN_REFERENCE_MISMATCH"):
            self.make(e)
        e.pop("latest_return_ref")
        e.pop("latest_response_ref")
        with self.assertRaisesRegex(ValueError, "ORPHAN_ROLE_RETURN_REF"):
            self.make(e)

    def test_binding_mode_mismatch_rejected(self):
        self.binding["professional_mode"]="IMPLEMENTATION"
        self.write("binding.json",json.dumps(self.binding));bad=self.commit("bad mode")
        e=copy.deepcopy(self.event);e["binding_ref"]=self.loc("binding.json",ref=bad)
        with self.assertRaisesRegex(ValueError,"MODE_MISMATCH"):self.make(e)

    def test_signed_markdown_binding_anchor_can_receive_its_original_return(self):
        cfg=json.loads((self.repo/'config.json').read_text())
        cfg['works']['w']['stage']='BI01'
        self.write('config.json',json.dumps(cfg))
        self.write('signed-task.md', '<a id="binding"></a>\n```json\n' + json.dumps(self.binding) + '\n```\n')
        signed=self.commit('signed Binding in original markdown task')
        self.ref=signed
        e=copy.deepcopy(self.event);e['route']='accept'
        e['binding_ref']=self.loc('signed-task.md','#binding',signed)
        ret={'schema':'question-work/v2','kind':'RETURN','work_id':'w','binding_ref':e['binding_ref'],
             'continuation_ref':{'answer_ref':'#continuation'}}
        self.write('response.md','<a id="question-work-return"></a>\n```json\n'+json.dumps(ret)+'\n```\n')
        returned=self.commit('original return uses exact signed anchor')
        e['latest_return_ref']=self.loc('response.md','#question-work-return',returned)
        e['latest_response_ref']=self.loc('response.md','full',returned)
        p=self.make(e)
        self.assertEqual(p['role'],'management')
        self.assertEqual(p['recipient'],'management-chat')
        self.write('ambiguous.md','<a id="binding"></a>\n```json\n'+json.dumps(self.binding)+'\n```\n```json\n{}\n```\n')
        bad=self.commit('ambiguous Binding is rejected')
        e['binding_ref']=self.loc('ambiguous.md','#binding',bad)
        with self.assertRaisesRegex(ValueError,'ONE_COMPLETE_BINDING_REQUIRED'):self.make(e)

    def test_unknown_wrong_and_duplicate_inputs(self):
        for change in ({"route":"trigger:missing"},{"work_id":"other"},{"send_state":"UNKNOWN"},{"send_state":"RUNNING"}):
            e=self.event|change
            with self.subTest(change=change),self.assertRaises(ValueError):self.make(e)
        with self.assertRaises(ValueError):m.loads('{"a":1,"a":2}')

    def test_worktree_change_cannot_change_policy(self):
        p=self.make();self.write(m.POLICY_PATH,"不同规则")
        self.assertEqual(p["message"],self.make()["message"])

    def test_exact_refs_and_paths(self):
        for c in ("main","HEAD"):
            e=copy.deepcopy(self.event);e["binding_ref"]["commit"]=c
            with self.assertRaises(ValueError):self.make(e)
        with self.assertRaises(ValueError):m.read_git(self.repo,self.ref,"../x")

    def test_full_Chinese_selector_compatibility(self):
        e=copy.deepcopy(self.event);e["binding_ref"]["selector"]="全文";self.make(e)

    def test_changed_text_or_recipient_never_sent(self):
        p=self.make(); sent=[]
        bad=p["message"].replace("重新判断两路分工", "接受旧分工").encode()
        with self.assertRaises(ValueError):m.checked_send(p,bad,p["recipient"],lambda *a:sent.append(a))
        with self.assertRaisesRegex(ValueError,"RECIPIENT_CHANGED"):
            m.checked_send(p,p["message"].encode(),"wrong-chat",lambda *a:sent.append(a))
        self.assertEqual(sent,[])
        m.checked_send(p,p["message"].encode(),p["recipient"],lambda *a:sent.append(a));self.assertEqual(len(sent),1)

    def test_replay_original_bytes(self):
        loc=self.loc("task.md"); raw=(self.repo/"task.md").read_bytes()
        self.assertEqual(m.replay(self.repo,loc,"test/repo",m.digest(raw)),raw)
        with self.assertRaises(ValueError):m.replay(self.repo,loc,"test/repo","bad")

    def test_effort_is_fact_only(self):
        for n in (True,-1,float("nan")):
            e=self.event|{"elapsed_hours":n}
            with self.subTest(n=n),self.assertRaises(ValueError):self.make(e)
        e=self.event|{"observed_at":"2026-09-21T10:00:00-04:00","effective_calls":2}
        self.assertIn("有效回交数：2",self.make(e)["message"])

    def test_cli_and_byte_recipient_verification(self):
        e=self.repo/"event.json";e.write_text(json.dumps(self.event));payload=self.repo/"message.md"
        args=["--repo",str(self.repo),"--ref",self.ref,"--config","config.json","--dispatch",str(e)]
        r=subprocess.run([sys.executable,str(TOOL),"prepare",*args,"--message-output",str(payload)],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stdout+r.stderr)
        r=subprocess.run([sys.executable,str(TOOL),"verify",*args,"--payload",str(payload),"--recipient","management-chat"],capture_output=True,text=True)
        self.assertEqual(r.returncode,2)
        self.assertIn("GITHUB_SHORT_RELAY_REQUIRED",r.stdout)
        r=subprocess.run([sys.executable,str(TOOL),"verify",*args,"--direct-body-authorized","--payload",str(payload),"--recipient","management-chat"],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stdout+r.stderr)
        self.write("archived.md",payload.read_text(encoding="utf-8"))
        archived=self.commit("archive assignment for short relay")
        locpath=self.repo/"message-locator.json"
        locpath.write_text(json.dumps(self.loc("archived.md",ref=archived)))
        short=self.repo/"short.md"
        args=["--repo",str(self.repo),"--ref",self.ref,"--config","config.json","--dispatch",str(e)]
        r=subprocess.run([sys.executable,str(TOOL),"prepare",*args,"--github-message-ref",str(locpath),"--message-output",str(short)],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stdout+r.stderr)
        self.assertLess(len(short.read_bytes()),len(payload.read_bytes()))
        r=subprocess.run([sys.executable,str(TOOL),"verify",*args,"--github-message-ref",str(locpath),"--payload",str(short),"--recipient","management-chat"],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stdout+r.stderr)
        r=subprocess.run([sys.executable,str(TOOL),"verify",*args,"--github-message-ref",str(locpath),"--payload",str(short),"--recipient","wrong-chat"],capture_output=True,text=True)
        self.assertEqual(r.returncode,2)

    def test_legacy_free_text_cannot_generate_new_dispatch(self):
        with self.assertRaisesRegex(ValueError,"LEGACY_CONTEXT"):m.prepare(self.repo,self.ref,{},"旧原文")



    def use_c_stage(self):
        cfg=json.loads((self.repo/'config.json').read_text())
        cfg['works']['w']['stage']='C'
        cfg['works']['w']['modes']['ENGINEERING_PACKAGE']['display_name']='Pro 关键代码实施与普通工程师派工'
        self.write('config.json',json.dumps(cfg))
        self.ref=self.commit('C test configuration')

    def test_c_repeated_management_keeps_full_duty_and_correct_identity(self):
        self.use_c_stage()
        for invocation in ('c-management-1','c-management-2'):
            e=copy.deepcopy(self.event);e['invocation_id']=invocation
            p=self.make(e)
            self.assertIn('当前职责：Mission C 实质管理与阶段接收',p['message'])
            self.assertNotIn('当前职责：Pro 关键代码实施',p['message'])
            policy=(O/'08_自然语言运行提示_v0.3.md').read_text()
            self.assertIn(m.marked(policy,'MANAGEMENT_DUTY'),p['message'])
            self.assertIn(m.marked(policy,'MANAGEMENT_STAGE_C'),p['message'])
            self.assertIn('Owner完整目的',p['message'])
            self.assertNotIn('本轮依已交工程忠实完成',p['message'])

    def test_c_review_stays_read_only_and_has_review_identity(self):
        self.use_c_stage()
        e=copy.deepcopy(self.event);e['route']='same_work'
        e['binding_ref']=self.loc('receiver-binding.json',ref=self.ref)
        e['current_task_ref']=self.loc('receiver-task.md',ref=self.ref)
        p=self.make(e)
        self.assertIn('当前职责：Mission C 独立只读审查',p['message'])
        policy=(O/'08_自然语言运行提示_v0.3.md').read_text()
        self.assertIn(m.marked(policy,'READONLY_RECEPTION_C'),p['message'])
        self.assertNotIn(m.marked(policy,'TASK_DUTY'),p['message'])
        self.assertNotIn(m.marked(policy,'MANAGEMENT_DUTY'),p['message'])

    def test_c_implementation_keeps_implementation_identity(self):
        self.use_c_stage()
        e=copy.deepcopy(self.event);e['route']='same_work'
        p=self.make(e)
        self.assertIn('当前职责：Pro 关键代码实施与普通工程师派工',p['message'])
        self.assertNotIn('你负责完整任务在合理轮次',p['message'])

    def test_a_b_management_identity_does_not_claim_implementation(self):
        for stage in ('A','B'):
            cfg=json.loads((self.repo/'config.json').read_text())
            cfg['works']['w']['stage']=stage
            self.write('config.json',json.dumps(cfg));self.ref=self.commit('stage '+stage)
            p=self.make()
            self.assertIn('当前职责：Mission '+stage+' 实质管理与阶段接收',p['message'])
            self.assertNotIn('当前职责：Mission B 工程细化与任务包编制',p['message'])


class CWorkflowDeltaTests(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory();self.addCleanup(self.t.cleanup)
        self.repo=Path(self.t.name)
        self.git('init','-q');self.git('config','user.name','Fixture');self.git('config','user.email','fixture@example.invalid')
        self.policy=''
        for key in ['MANAGEMENT_DUTY','TASK_DUTY','REFERENCE_USE','RETURN_TAIL','RETURN_REPAIR','RETURN_REPAIR_TAIL','C_WORKFLOW_COMMON']:
            self.policy += f'<!-- {key}_BEGIN -->{key}-正文<!-- {key}_END -->\n'
        for s in 'ABC':
            for k in ['MANAGEMENT_STAGE_','STAGE_','READONLY_RECEPTION_']:
                key=k+s; self.policy+=f'<!-- {key}_BEGIN -->{key}-正文<!-- {key}_END -->\n'
        self.write(m.POLICY_PATH,self.policy)
        self.write('goal.md','完整目标保持')
        self.write('work.md','<a id="scope"></a>完整范围\n<a id="same"></a>原指令\n')
        self.write('task.md','<!-- CURRENT_C_WORK_BEGIN -->当前业务检查，不重复编译。<!-- CURRENT_C_WORK_END -->')
        self.write('adopt.md','本次采用任务1')
        self.base=self.commit()
        self.loc=lambda p,s='full',ref=None:dict(repo='test/repo',commit=ref or self.base,path=p,selector=s)
        self.binding={'schema':'question-work/v2','kind':'BINDING','work_id':'w','professional_mode':'implementation',
           'full_scope_ref':self.loc('work.md','#scope'),'plan_ref':self.loc('work.md','#scope'),
           'budget_ref':self.loc('work.md','#scope'),'focus_ref':self.loc('work.md','#same'),
           'deliverables_ref':self.loc('work.md','#scope'),'completion_ref':self.loc('work.md','#scope'),
           'routes':{'same_work':{'recipient_role':'professional','recipient_ref':'pro','instructions_ref':self.loc('work.md','#same')},
                     'accept':{'recipient_role':'management','recipient_ref':'manager','instructions_ref':self.loc('work.md','#same')}},'triggers':[]}
        self.write('binding.json',json.dumps(self.binding))
        self.config={'schema':'coordinator-dispatch/v3','repository':'test/repo','works':{'w':{'stage':'C','modes':{'implementation':{'display_name':'实际实施','purpose':'professional_work'}},'goal_ref':{'path':'goal.md','selector':'full'}}}}
        self.write('config.json',json.dumps(self.config));self.ref=self.commit()
        self.event=dict(work_id='w',invocation_id='call1',assignment_token='token',binding_ref=self.loc('binding.json',ref=self.ref),route='same_work',send_state='NOT_SENT',dispatch_kind='NORMAL',current_task_ref=self.loc('task.md'),task_adoption_ref=self.loc('adopt.md'))
    def git(self,*a):return subprocess.check_output(['git','-C',str(self.repo),*a],stderr=subprocess.PIPE).decode().strip()
    def write(self,p,body):
        q=self.repo/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_text(body,encoding='utf-8')
    def commit(self):
        self.git('add','.');self.git('commit','-qm','test source');return self.git('rev-parse','HEAD')
    def make(self,e=None):return m.prepare_dispatch(self.repo,self.ref,'config.json',e or self.event)
    def response(self,body):
        r=dict(schema='question-work/v2',kind='RETURN',work_id='w',binding_ref=self.event['binding_ref'],continuation_ref={'answer_ref':'#continuation'})
        self.write('response.md','<a id="continuation"></a>'+body+'\n<a id="return"></a>\n```json\n'+json.dumps(r)+'\n```\n')
        ref=self.commit();self.event['latest_return_ref']=self.loc('response.md','#return',ref);self.event['latest_response_ref']=self.loc('response.md',ref=ref)
        return ref
    def test_current_task_is_in_message(self):
        msg=self.make()['message'];self.assertIn('## 本轮当前工作',msg);self.assertIn('当前业务检查，不重复编译。',msg)
    def test_latest_unmarked_is_not_initial_focus(self):
        self.response('reader已修好，继续检查对象延续。')
        msg=self.make()['message'];self.assertIn('reader已修好，继续检查对象延续。',msg);self.assertNotIn('当前业务检查，不重复编译。',msg)
    def test_latest_marked_is_selected_verbatim(self):
        self.response('外部说明\n<!-- CURRENT_C_WORK_BEGIN -->新重点原文\n保持换行<!-- CURRENT_C_WORK_END -->')
        msg=self.make()['message'];self.assertIn('新重点原文\n保持换行',msg);self.assertNotIn('外部说明',msg)
    def test_new_adoption_supersedes_old_continuation(self):
        self.response('旧重点不应发送')
        self.write('task.md','<!-- CURRENT_C_WORK_BEGIN -->新采用任务2<!-- CURRENT_C_WORK_END -->')
        self.write('adopt.md','新采用');new=self.commit()
        self.event['current_task_ref']=self.loc('task.md',ref=new);self.event['task_adoption_ref']=self.loc('adopt.md',ref=new)
        msg=self.make()['message'];self.assertIn('新采用任务2',msg);self.assertNotIn('旧重点不应发送',msg)
    def test_normal_c_task_without_marker_is_in_message(self):
        self.write('task.md','旧任务原文');r=self.commit();self.event['current_task_ref']=self.loc('task.md',ref=r)
        msg=self.make()['message'];self.assertIn('## 本轮当前工作\n\n旧任务原文',msg)
        self.assertIn(':task.md::full',msg)
    def test_new_task_keeps_outer_instructions_around_quoted_marker(self):
        task=('当前角色：专业推进。\n<!-- CURRENT_C_WORK_BEGIN -->'
              'Owner 原文引述，不得代替任务外层要求。<!-- CURRENT_C_WORK_END -->\n'
              '本轮沿完整施工要求继续。')
        self.write('task.md',task);r=self.commit();self.event['current_task_ref']=self.loc('task.md',ref=r)
        msg=self.make()['message']
        self.assertIn('当前角色：专业推进。',msg)
        self.assertIn('Owner 原文引述，不得代替任务外层要求。',msg)
        self.assertIn('本轮沿完整施工要求继续。',msg)
    def test_new_task_keeps_unbalanced_quote_marker_in_full_text(self):
        self.write('task.md','<!-- CURRENT_C_WORK_BEGIN -->不完整');r=self.commit();self.event['current_task_ref']=self.loc('task.md',ref=r)
        self.assertIn('<!-- CURRENT_C_WORK_BEGIN -->不完整',self.make()['message'])
    def test_each_role_gets_common_but_not_other_duties(self):
        for role in ['professional','management','review','receiver']:
            body=m.role_body(self.policy,role,'C');self.assertIn('C_WORKFLOW_COMMON-正文',body)
            if role in ['review','receiver']:
                self.assertNotIn('TASK_DUTY-正文',body);self.assertNotIn('MANAGEMENT_DUTY-正文',body)
        self.assertNotIn('MANAGEMENT_DUTY-正文',m.role_body(self.policy,'professional','C'))
    def test_current_policy_keeps_role_boundaries_and_business_guards(self):
        policy=(O/'08_自然语言运行提示_v0.3.md').read_text(encoding='utf-8')
        management=m.role_body(policy,'management','C')
        professional=m.role_body(policy,'professional','C')
        review=m.role_body(policy,'review','C')
        for body in (management,professional,review):
            self.assertIn('严禁在特征自身建立全文／全对象哈希',body)
        self.assertIn('材料权力收拢、已知问题裁定',management)
        self.assertIn('管理已经完成的材料采用',professional)
        self.assertIn('本角色保持实际只读权限',review)
        self.assertNotIn('材料权力收拢、已知问题裁定',professional)
        self.assertNotIn('每次实质业务推进，都以完整完成 Owner',review)
    def test_a_b_not_changed(self):
        for s in 'AB':
            for role in ['professional','management','review']:
                self.assertNotIn('C_WORKFLOW_COMMON',m.role_body(self.policy,role,s))
    def test_payload_and_recipient_guard_preserved(self):
        p=self.make();called=[]
        with self.assertRaises(ValueError):m.checked_send(p,p['message'].encode()+b'x',p['recipient'],lambda *a:called.append(a))
        with self.assertRaises(ValueError):m.checked_send(p,p['message'].encode(),'other',lambda *a:called.append(a))
        self.assertEqual(called,[]);self.assertEqual(p['message_sha256'],m.digest(p['message'].encode()))
    def test_replay_original_unchanged(self):
        raw=(self.repo/'task.md').read_bytes();self.assertEqual(raw,m.replay(self.repo,self.loc('task.md'),'test/repo',m.digest(raw)))

    def test_same_bytes_at_newer_reference_keep_valid_continuation(self):
        self.response('有效续作不能被无关提交压掉')
        self.write('unrelated.md','只是另一个文件变化'); newer=self.commit()
        self.event['current_task_ref']=self.loc('task.md',ref=newer)
        self.event['task_adoption_ref']=self.loc('adopt.md',ref=newer)
        self.assertIn('有效续作不能被无关提交压掉',self.make()['message'])
    def test_c_delivery_repair_remains_narrow(self):
        self.write('original.md','work_id: w\ninvocation_id: original\nassignment_token: t\nrole: professional\nrecipient: pro\n')
        self.write('issue.md','仅补已承诺实物');self.write('missing.md','原缺件')
        ref=self.commit();event=copy.deepcopy(self.event)
        event['dispatch_kind']='DELIVERY_REPAIR';event.pop('current_task_ref');event.pop('task_adoption_ref')
        event['repair_context']={'original_dispatch_ref':self.loc('original.md',ref=ref),'issue_ref':self.loc('issue.md',ref=ref),'missing_output_refs':[self.loc('missing.md',ref=ref)]}
        msg=self.make(event)['message']
        self.assertIn('RETURN_REPAIR-正文',msg);self.assertNotIn('C_WORKFLOW_COMMON-正文',msg)
        self.assertNotIn('## 本轮当前工作',msg);self.assertNotIn('## Owner完整目的',msg)

if __name__=="__main__": unittest.main()
