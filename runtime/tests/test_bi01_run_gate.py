"""Offline-only BI-01 round gate tests; no Pro, phone, business inputs or sending."""
import hashlib
import importlib.util
import json
import copy
import subprocess
import tempfile
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[2]
MODULE_PATH = PROJECT / "runtime" / "tools" / "bi01_run_gate.py"
spec = importlib.util.spec_from_file_location("bi01_gate_under_test", MODULE_PATH)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)
spec = importlib.util.spec_from_file_location(
    "bi01_test_coordinator", PROJECT / "runtime" / "overlay" / "tools" / "management_prompt.py")
coordinator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(coordinator)
spec = importlib.util.spec_from_file_location(
    "bi01_test_question_work", PROJECT / "runtime" / "overlay" / "tools" / "question_work_check.py")
question_work = importlib.util.module_from_spec(spec)
spec.loader.exec_module(question_work)

RUN = "runs/BI-01-V2-02"
ROLE = "management"
RID = "R0001"
INV = "BI01-V2-02-R0001-synthetic-unique-a"
MARKER = "[" + INV + "]"


class RoundGateOffline(unittest.TestCase):
    def setUp(self):
        td = tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        self.repo = Path(td.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Synthetic Tester")
        self.git("config", "user.email", "synthetic@example.invalid")
        self.write(RUN + "/README.md", "# Synthetic pending run\n")
        self.write(RUN + "/OWNER_START.md", "Synthetic Owner GO; not a real authority.\n")
        self.write(RUN + "/BOOTSTRAP.json", json.dumps({
            "schema": "question-work/v2", "kind": "BOOTSTRAP", "work_id": "BI-01",
            "recipient_ref": "synthetic-management-chat"}))
        self.write("runtime/config/WORKMAP_BINDING.json", '{"schema":"workmap-binding/v2","status":"NOT_CONFIGURED"}')
        self.policy = self.commit("synthetic source baseline")
        self.owner = self.loc(RUN + "/OWNER_START.md")
        self.bootstrap = self.loc(RUN + "/BOOTSTRAP.json")
        self.prompt = MARKER + "\nSynthetic message; NO PHONE.\n"
        self.record = {
            "schema": "bi01-invocation/v1",
            "run_id": "BI-01-V2-02",
            "round_id": RID,
            "work_id": "BI-01",
            "invocation_id": INV,
            "assignment_token": "synthetic-unique-token",
            "round_marker": MARKER,
            "role": ROLE,
            "recipient_ref": "synthetic-management-chat",
            "policy_commit": self.policy,
            "prompt_sha256": hashlib.sha256(self.prompt.encode()).hexdigest(),
            "bootstrap_ref": self.bootstrap,
            "binding_ref": self.bootstrap,
            "current_task_ref": self.owner,
            "task_adoption_ref": self.owner,
            "question_work_required": True,
        }
        self.save_invocation()
        self.current = self.commit("synthetic first management invocation")

    def git(self, *args):
        return subprocess.check_output(
            ["git", "-C", str(self.repo), *args], stderr=subprocess.PIPE
        ).decode().strip()

    def write(self, name, raw):
        path = self.repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(raw, encoding="utf-8")

    def save_invocation(self):
        p = RUN + "/provenance/turns/" + RID + "/"
        self.write(p + "INVOCATION.json", json.dumps(self.record, ensure_ascii=False))
        self.write(p + "PROMPT.md", self.prompt)

    def commit(self, message):
        self.git("add", "-A")
        self.git("commit", "-qm", message)
        return self.git("rev-parse", "HEAD")

    def loc(self, path):
        return {"repo": "daowei2026/observe-iterate", "commit": self.policy,
                "path": path, "selector": "full"}

    def view(self):
        return gate.Git(self.repo, self.current)

    def prepare_reader(self):
        """Entirely synthetic Git history; it is never a real GO/reader/intake."""
        reader = gate.READER_TASK
        self.write(RUN + "/README.md", '<a id="common"></a>\nSynthetic common\n<a id="bi01"></a>\nSynthetic run\n')
        self.write(RUN + "/00_长程推进地图.md", '<a id="goal"></a>\nSynthetic map\n')
        self.write(RUN + "/01_当前任务.md", 'Synthetic complete S1/S2/S3 task; no business result.\n')
        goal = "professional/feature_observation/00_PURPOSE_AND_FOUR_WORKS.md"
        self.write(goal, 'Synthetic goal; not actual business input.\n')
        policy_path = 'runtime/overlay/08_自然语言运行提示_v0.3.md'
        self.write(policy_path, (PROJECT / policy_path).read_text())
        config_path = 'runtime/config/COORDINATOR_DISPATCH.json'
        self.write(config_path, (PROJECT / config_path).read_text())
        self.map_binding = {
            'schema': 'workmap-binding/v2', 'status': 'NOT_CONFIGURED', 'manager_role': 'management',
            'overview': {'path': RUN + '/README.md', 'anchors': ['common', 'bi01']},
            'shared_overview_anchors': ['common'], 'owner_sources': [RUN + '/OWNER_START.md'],
            'rule_paths': [goal], 'receipt_path': RUN + '/reviews/WORKMAP_INTAKE_CURRENT.json',
            'streams': {'bi01': {'map': {'path': RUN + '/00_长程推进地图.md', 'anchors': ['goal']},
                               'task': RUN + '/01_当前任务.md', 'overview_anchors': ['bi01'],
                               'watch_roots': [RUN + '/artifacts']}},
        }
        self.write(gate.BINDING, json.dumps(self.map_binding))
        authority_path = RUN + '/reviews/management-R0001/DECISION.md'
        self.write(authority_path, '\n'.join([
            'work_id: BI-01', 'run_id: BI-01-V2-02', 'role: management',
            'invocation_id: ' + INV, 'assignment_token: ' + self.record['assignment_token'],
            '<a id="reader-pre-adoption"></a>', 'Synthetic technical authority only.',
            '<a id="adoption"></a>', 'Synthetic conditional intake.', '',
            '<a id="reader-accept"></a>', 'Receive the actual synthetic Reader return.',
            '<a id="budget"></a>', 'Synthetic unchanged effort boundary.', '',
        ]))
        self.input_commit = self.commit('synthetic frozen input and issued authority')
        self.policy = self.input_commit
        authority = self.loc(authority_path)
        self.write(RUN + '/provenance/turns/R0001/SEND_RECEIPT.json', json.dumps({'state': 'COMMITTED'}))
        self.write(RUN + '/provenance/turns/R0001/ROLE_RETURN.json', json.dumps({
            'schema': 'longrun-return/v1', 'work_id': 'BI-01',
            'invocation_id': INV, 'assignment_token': self.record['assignment_token'],
            'role_outputs': {'management': {'decision_ref': '#reader-pre-adoption'}},
            'artifact_refs': [{k: authority[k] for k in ('repo', 'commit', 'path')}],
        }))
        prefix = ('task_id: BI01-V2-02-WORKMAP-READER-01\n'
                  'Synthetic read-only task, never a real independent report.\n'
                  '<a id="scope"></a>\nSynthetic full reading scope.\n'
                  '<a id="same-work"></a>\nContinue this synthetic reading.\n')
        self.write(reader, prefix)
        body_commit = self.commit('synthetic complete reader body')
        body_ref = self.loc(reader) | {'commit': body_commit}
        self.reader_binding = {
            'schema': 'question-work/v2', 'kind': 'BINDING', 'work_id': 'BI-01',
            'professional_mode': 'INDEPENDENT_REVIEW',
            'plan_ref': authority | {'selector': '#reader-pre-adoption'},
            'full_scope_ref': body_ref, 'focus_ref': body_ref,
            'deliverables_ref': body_ref, 'completion_ref': body_ref,
            'budget_ref': authority | {'selector': '#budget'},
            'source_reads': [{'source': self.loc(p), 'requirement': 'FOCUS_FULL',
                              'purpose': 'Synthetic direct input', 'reuse_evidence': None}
                             for p in [RUN + '/README.md', RUN + '/00_长程推进地图.md',
                                       RUN + '/01_当前任务.md', gate.BINDING, RUN + '/OWNER_START.md']],
            'routes': {'same_work': {'recipient_role': 'review', 'recipient_ref': 'synthetic-reader-chat',
                                     'instructions_ref': body_ref | {'selector': '#same-work'}},
                       'accept': {'recipient_role': 'management', 'recipient_ref': 'synthetic-management-chat',
                                  'instructions_ref': authority | {'selector': '#reader-accept'}}},
            'question_ids': ['AUDIT'], 'triggers': [],
        }
        encoded = json.dumps(self.reader_binding, ensure_ascii=False, indent=2)
        self.write(reader, prefix + '<a id="question-work-binding"></a>\n```json\n' + encoded + '\n```\n')
        bound_commit = self.commit('synthetic exact reader binding')
        lines = (self.repo / reader).read_text().splitlines()
        start = lines.index('```json') + 2
        end = len(lines) - 1
        bound_ref = self.loc(reader) | {'commit': bound_commit, 'selector': f'L{start}-L{end}'}
        self.reader_round = 'R0003'
        self.record = {
            'schema': 'bi01-invocation/v1', 'run_id': 'BI-01-V2-02', 'round_id': self.reader_round,
            'work_id': 'BI-01', 'invocation_id': 'BI01-V2-02-R0003-synthetic-reader-a',
            'assignment_token': 'synthetic-reader-token', 'role': 'review',
            'recipient_ref': 'synthetic-reader-chat', 'policy_commit': self.policy,
            'binding_ref': bound_ref, 'current_task_ref': body_ref | {'commit': bound_commit},
            'task_adoption_ref': authority | {'selector': '#adoption'}, 'question_work_required': True,
        }
        self.record['round_marker'] = '[' + self.record['invocation_id'] + ']'
        self.reader_event = {k: self.record[k] for k in
                             ('work_id', 'invocation_id', 'assignment_token', 'binding_ref',
                              'current_task_ref', 'task_adoption_ref')}
        self.reader_event.update(route='same_work', send_state='NOT_SENT', dispatch_kind='NORMAL')
        prepared = coordinator.prepare_dispatch(self.repo, self.policy, config_path, self.reader_event)
        self.prompt = prepared['message']
        self.record['prompt_sha256'] = hashlib.sha256(self.prompt.encode()).hexdigest()
        self.save_reader('synthetic prepared reader; NO PHONE')

    def save_reader(self, message):
        p = RUN + '/provenance/turns/' + self.reader_round + '/'
        self.write(p + 'INVOCATION.json', json.dumps(self.record, ensure_ascii=False))
        self.write(p + 'PROMPT.md', self.prompt)
        self.write(p + 'DISPATCH.json', json.dumps(self.reader_event, ensure_ascii=False))
        self.current = self.commit(message)

    def test_first_issued_reader_prepares_without_adoption_or_intake(self):
        self.prepare_reader()
        result = gate.pre_dispatch(self.view(), self.reader_round)
        self.assertTrue(result['ok'], result)
        self.assertFalse(result['sent'])
        self.assertFalse(result['business_gate'])
        self.assertFalse(self.view().exists(self.map_binding['receipt_path']))

    def prepare_reader_reception(self):
        self.prepare_reader()
        self.original_reader_round = self.reader_round
        self.original_reader_record = copy.deepcopy(self.record)
        self.reader_return = {
            'schema': 'question-work/v2', 'kind': 'RETURN', 'work_id': 'BI-01',
            'invocation_id': self.record['invocation_id'],
            'binding_ref': self.record['binding_ref'] | {'selector': '#question-work-binding'},
            'focus_results': [{'question_id': 'AUDIT'}], 'trigger_observations': [],
            'continuation_ref': {'answer_ref': '#continuation'},
        }
        self.reader_role_return = {
            'schema': 'longrun-return/v1', 'work_id': 'BI-01',
            'invocation_id': self.record['invocation_id'],
            'assignment_token': self.record['assignment_token'],
            'question_work_ref': '#question-work-return',
            'handoff': {'kind': 'SUBMIT', 'route_key': 'accept'},
            'role_outputs': {'review': {'verdict': 'PASS'}},
        }
        p = RUN + '/provenance/turns/' + self.reader_round + '/'
        self.write(p + 'SEND_RECEIPT.json', json.dumps({'state': 'COMMITTED'}))
        self.write(p + 'QUESTION_WORK_RETURN.json', json.dumps(self.reader_return))
        self.write(p + 'ROLE_RETURN.json', json.dumps(self.reader_role_return))
        self.write(p + 'FULL_RESPONSE.md', (
            'Synthetic complete Reader report; no real review.\n'
            '```text\nSynthetic business relation diagram.\n```\n'
            '<a id="continuation"></a>Return to original manager.\n'
            '<a id="question-work-return"></a>\n```json\n' + json.dumps(self.reader_return) +
            '\n```\n## ROLE_RETURN\n```json\n' + json.dumps(self.reader_role_return) + '\n```\n'))
        response_commit = self.commit('synthetic actual Reader return, no real Pro')
        response = self.loc(p + 'FULL_RESPONSE.md') | {'commit': response_commit}
        self.reader_round = 'R0004'
        self.record.update(round_id=self.reader_round, role='management',
                           invocation_id='BI01-V2-02-R0004-synthetic-reception-a',
                           assignment_token='synthetic-reception-token',
                           recipient_ref='synthetic-management-chat')
        self.record['binding_ref']['selector'] = '#question-work-binding'
        self.record['round_marker'] = '[' + self.record['invocation_id'] + ']'
        self.reader_event = {k: self.record[k] for k in
                             ('work_id', 'invocation_id', 'assignment_token', 'binding_ref',
                              'current_task_ref', 'task_adoption_ref')}
        self.reader_event.update(route='accept', send_state='NOT_SENT', dispatch_kind='NORMAL',
                                 latest_response_ref=response,
                                 latest_return_ref=response | {'selector': '#question-work-return'})
        prepared = coordinator.prepare_dispatch(self.repo, self.policy,
                                                 'runtime/config/COORDINATOR_DISPATCH.json', self.reader_event)
        self.prompt = prepared['message']
        self.record['prompt_sha256'] = hashlib.sha256(self.prompt.encode()).hexdigest()
        self.save_reader('synthetic original manager receives actual first Reader')

    def test_first_reader_can_return_to_its_signed_manager_before_adoption(self):
        self.prepare_reader_reception()
        result = gate.pre_dispatch(self.view(), self.reader_round)
        self.assertTrue(result['ok'], result)
        self.assertFalse(self.view().exists(self.map_binding['receipt_path']))

    def test_reception_requires_original_committed_reader_and_matching_full_return(self):
        self.prepare_reader_reception()
        p = RUN + '/provenance/turns/' + self.original_reader_round + '/'
        for state in ('NOT_SENT', 'UNKNOWN'):
            with self.subTest(state=state):
                self.write(p + 'SEND_RECEIPT.json', json.dumps({'state': state}))
                self.current = self.commit('synthetic unconfirmed Reader')
                self.assertFalse(gate.pre_dispatch(self.view(), self.reader_round)['ok'])
        self.write(p + 'SEND_RECEIPT.json', json.dumps({'state': 'COMMITTED'}))
        self.write(p + 'FULL_RESPONSE.md', 'Synthetic replaced body.\n')
        self.current = self.commit('synthetic saved full answer drift')
        errors = gate.pre_dispatch(self.view(), self.reader_round)['errors']
        self.assertTrue(any('ORIGINAL_READER_FULL_RESPONSE_MISMATCH' in e for e in errors), errors)

    def test_reception_does_not_allow_professional_recipient_or_changed_inputs(self):
        self.prepare_reader_reception()
        original = copy.deepcopy(self.record)
        self.record['recipient_ref'] = 'synthetic-wrong-manager'
        self.save_reader('synthetic changed reception recipient')
        errors = gate.pre_dispatch(self.view(), self.reader_round)['errors']
        self.assertTrue(any('RECIPIENT_CHANGED' in e for e in errors), errors)
        self.record = original
        self.write(RUN + '/00_长程推进地图.md', '<a id="goal"></a>Changed synthetic map.\n')
        self.save_reader('synthetic changed frozen input before reception')
        errors = gate.pre_dispatch(self.view(), self.reader_round)['errors']
        self.assertTrue(any('FIRST_READER_INPUT_CHANGED' in e for e in errors), errors)
        self.record['role'] = 'professional'
        self.save_reader('synthetic professional cannot borrow manager reception')
        self.assertIn('WORKMAP_NOT_ADOPTED', gate.pre_dispatch(self.view(), self.reader_round)['errors'])

    def test_other_roles_sources_and_recipients_cannot_borrow_reader_authority(self):
        self.prepare_reader()
        original = copy.deepcopy(self.record)
        changes = [({'role': role}, 'WORKMAP_NOT_ADOPTED') for role in ('professional', 'receiver')]
        changes += [({'recipient_ref': 'synthetic-wrong-chat'}, 'RECIPIENT_CHANGED'),
                    ({'bootstrap_ref': self.bootstrap, 'binding_ref': self.bootstrap}, 'WORKMAP_NOT_ADOPTED'),
                    ({'binding_ref': self.bootstrap}, 'READER_TASK_BINDING_SOURCE_MISMATCH'),
                    ({'current_task_ref': self.loc(RUN + '/01_当前任务.md')}, 'WORKMAP_NOT_ADOPTED'),
                    ({'task_adoption_ref': self.loc(RUN + '/OWNER_START.md')}, 'DISPATCH_SOURCE_MISMATCH')]
        for change, expected in changes:
            with self.subTest(change=change):
                self.record = copy.deepcopy(original)
                self.record.update(change)
                self.save_reader('synthetic invalid reader caller')
                result = gate.pre_dispatch(self.view(), self.reader_round)
                self.assertFalse(result['ok'], result)
                self.assertTrue(any(expected in e for e in result['errors']), result)

    def test_reader_cannot_impersonate_management_with_a_binding_as_bootstrap(self):
        self.prepare_reader()
        self.record.update(role='management', bootstrap_ref=self.record['binding_ref'])
        self.save_reader('synthetic reader disguised as bootstrap management')
        result = gate.pre_dispatch(self.view(), self.reader_round)
        self.assertFalse(result['ok'], result)
        self.assertIn('BOOTSTRAP_UNREADABLE', result['errors'])

    def test_reader_frozen_input_cannot_be_silently_replaced(self):
        self.prepare_reader()
        self.write(RUN + '/00_长程推进地图.md', '<a id="goal"></a>\nChanged synthetic map.\n')
        self.current = self.commit('synthetic protected input drift')
        result = gate.pre_dispatch(self.view(), self.reader_round)
        self.assertFalse(result['ok'], result)
        self.assertTrue(any('FIRST_READER_INPUT_CHANGED' in e for e in result['errors']), result)

    def test_reader_requires_the_current_issued_task(self):
        self.prepare_reader()
        self.write(gate.READER_TASK, (self.repo / gate.READER_TASK).read_text() + '\nChanged synthetic task.\n')
        self.current = self.commit('synthetic current task changed')
        result = gate.pre_dispatch(self.view(), self.reader_round)
        self.assertTrue(any('READER_TASK_NOT_CURRENT' in e for e in result['errors']), result)

    def test_reader_exact_renderer_and_send_safety_are_preserved(self):
        self.prepare_reader()
        p = RUN + '/provenance/turns/' + self.reader_round + '/SEND_RECEIPT.json'
        for state in ('UNKNOWN', 'COMMITTED', 'BLOCKED'):
            with self.subTest(state=state):
                self.write(p, json.dumps({'state': state}))
                self.current = self.commit('synthetic unsafe reader send state')
                self.assertIn('SEND_NOT_SAFE:' + state, gate.pre_dispatch(self.view(), self.reader_round)['errors'])
        self.write(p, json.dumps({'state': 'NOT_SENT'}))
        self.prompt += 'Synthetic unauthorized payload addition.\n'
        self.record['prompt_sha256'] = hashlib.sha256(self.prompt.encode()).hexdigest()
        self.save_reader('synthetic rehashed but unapproved payload')
        errors = gate.pre_dispatch(self.view(), self.reader_round)['errors']
        self.assertTrue(any('MESSAGE_CHANGED' in e for e in errors), errors)

    def test_adopted_professional_path_remains_required_and_available(self):
        self.prepare_reader()
        self.record['role'] = 'professional'
        self.record['current_task_ref'] = self.loc(RUN + '/01_当前任务.md')
        self.map_binding['status'] = 'ADOPTED'
        self.write(gate.BINDING, json.dumps(self.map_binding))
        self.write(self.map_binding['receipt_path'], json.dumps({'schema': 'workmap-intake/v1', 'intakes': {'bi01': {}}}))
        self.save_reader('synthetic adopted structural path; not a business PASS')
        self.assertTrue(gate.pre_dispatch(self.view(), self.reader_round)['ok'])

    def test_first_management_bootstrap_is_preparable_without_map(self):
        result = gate.pre_dispatch(self.view(), RID)
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["recorded_send_state"], "NOT_RECORDED")
        self.assertEqual(result["sent"], False)

    def prepare_fresh_run(self):
        """A second synthetic run cannot acquire the legacy run's authority."""
        self.fresh_id = "BI-01-FO-01"
        self.fresh_root = "runs/" + self.fresh_id
        for name in ("README.md", "OWNER_START.md", "BOOTSTRAP.json"):
            self.write(self.fresh_root + "/" + name,
                       (self.repo / RUN / name).read_text())
        fresh_source = self.commit("synthetic separate fresh-run sources")
        self.fresh_record = copy.deepcopy(self.record)
        self.fresh_record.update(run_id=self.fresh_id,
                                 invocation_id="BI01-FO-01-R0001-synthetic-fresh-a")
        self.fresh_record["round_marker"] = "[" + self.fresh_record["invocation_id"] + "]"
        for key in ("bootstrap_ref", "binding_ref", "current_task_ref", "task_adoption_ref"):
            loc = self.fresh_record[key]
            loc.update(commit=fresh_source, path=loc["path"].replace(RUN, self.fresh_root))
        self.fresh_prompt = self.fresh_record["round_marker"] + "\nSynthetic fresh-run input.\n"
        self.fresh_record["prompt_sha256"] = hashlib.sha256(self.fresh_prompt.encode()).hexdigest()
        self.save_fresh_run()

    def save_fresh_run(self):
        root = self.fresh_root + "/provenance/turns/" + RID + "/"
        self.write(root + "INVOCATION.json", json.dumps(self.fresh_record))
        self.write(root + "PROMPT.md", self.fresh_prompt)
        self.current = self.commit("synthetic fresh-run invocation; NO PHONE")

    def fresh_view(self):
        return gate.Git(self.repo, self.current, self.fresh_id)

    def test_fresh_run_bootstrap_and_legacy_view_are_isolated(self):
        self.prepare_fresh_run()
        self.assertTrue(gate.pre_dispatch(self.fresh_view(), RID)["ok"])
        self.assertEqual(gate.invocation(self.fresh_view(), RID)[0]["run_id"], self.fresh_id)
        self.assertEqual(gate.invocation(self.view(), RID)[0]["run_id"], "BI-01-V2-02")

    def test_fresh_run_rejects_legacy_identity_marker_and_sources(self):
        self.prepare_fresh_run()
        original = copy.deepcopy(self.fresh_record)
        for changes, expected in (
            ({"run_id": "BI-01-V2-02"}, "RUN_ID_MISMATCH"),
            ({"invocation_id": INV}, "ROUND_MARKER_OR_INVOCATION_MISMATCH"),
            ({"current_task_ref": self.owner}, "LOCATOR_PATH_OUTSIDE_NEW_RUN:current_task_ref"),
            ({"bootstrap_ref": self.bootstrap, "binding_ref": self.bootstrap},
             "LOCATOR_PATH_OUTSIDE_NEW_RUN:bootstrap_ref"),
        ):
            with self.subTest(changes=changes):
                self.fresh_record = copy.deepcopy(original)
                self.fresh_record.update(changes)
                self.save_fresh_run()
                self.assertIn(expected, gate.pre_dispatch(self.fresh_view(), RID)["errors"])

    def test_fresh_run_cannot_use_adopted_legacy_workmap(self):
        self.prepare_fresh_run()
        self.fresh_record.update(role="professional")
        self.fresh_record.pop("bootstrap_ref")
        binding = {
            "schema": "workmap-binding/v2", "status": "ADOPTED",
            "overview": {"path": RUN + "/README.md"},
            "streams": {"bi01": {"map": {"path": RUN + "/00_长程推进地图.md"},
                                  "task": RUN + "/01_当前任务.md"}},
            "receipt_path": RUN + "/reviews/WORKMAP_INTAKE_CURRENT.json",
        }
        self.write(gate.BINDING, json.dumps(binding))
        self.save_fresh_run()
        result = gate.pre_dispatch(self.fresh_view(), RID)
        self.assertFalse(result["ok"])
        self.assertTrue(any(e.startswith("WORKMAP_PATH_MISMATCH:") for e in result["errors"]))

    def test_run_id_cannot_escape_runs_directory(self):
        for run_id in ("../BI-01-FO-01", "BI-01-FO-01/../../old", "", "BI-01-FO 01"):
            with self.subTest(run_id=run_id), self.assertRaisesRegex(ValueError, "INVALID_RUN_ID"):
                gate.Git(self.repo, self.current, run_id)

    def test_exact_first_line_and_marker_are_required(self):
        self.record["round_marker"] = "[DIFFERENT]"
        self.save_invocation()
        self.current = self.commit("synthetic wrong marker")
        errors = gate.pre_dispatch(self.view(), RID)["errors"]
        self.assertIn("ROUND_MARKER_OR_INVOCATION_MISMATCH", errors)
        self.assertIn("PROMPT_FIRST_LINE_NOT_SCHEDULER_MARKER", errors)

    def test_professional_cannot_use_unadopted_workmap(self):
        self.record["role"] = "professional"
        self.record.pop("bootstrap_ref")
        self.save_invocation()
        self.current = self.commit("synthetic professional without map")
        result = gate.pre_dispatch(self.view(), RID)
        self.assertFalse(result["ok"])
        self.assertIn("WORKMAP_NOT_ADOPTED", result["errors"])

    def test_unknown_send_cannot_be_resent(self):
        p = RUN + "/provenance/turns/" + RID + "/SEND_RECEIPT.json"
        self.write(p, json.dumps({"state": "UNKNOWN"}))
        self.current = self.commit("synthetic unknown send")
        result = gate.pre_dispatch(self.view(), RID)
        self.assertFalse(result["ok"])
        self.assertIn("SEND_NOT_SAFE:UNKNOWN", result["errors"])

    def test_real_returns_are_not_inferred(self):
        result = gate.after_return(self.view(), RID)
        self.assertFalse(result["ok"])
        self.assertIn("NO_CONFIRMED_SEND_FOR_RETURN", result["errors"])
        self.assertIn("ROLE_RETURN_MISSING", result["errors"])
        self.assertIn("QUESTION_WORK_RETURN_MISSING", result["errors"])

    def test_both_returns_must_match_the_actual_invocation(self):
        p = RUN + "/provenance/turns/" + RID + "/"
        self.write(p + "SEND_RECEIPT.json", json.dumps({"state": "COMMITTED"}))
        self.write(p + "FULL_RESPONSE.md", "Synthetic complete reply; not a business result.\n")
        self.write(p + "ROLE_RETURN.json", json.dumps({
            "schema": "longrun-return/v1", "work_id": "BI-01",
            "invocation_id": INV, "assignment_token": self.record["assignment_token"],
            "question_work_ref": "#question-work-return",
        }))
        question = {
            "schema": "question-work/v2", "kind": "RETURN",
            "work_id": "BI-01", "invocation_id": INV,
            "binding_ref": self.bootstrap,
            "focus_results": [{"question_id": "M-START"}],
            "trigger_observations": [], "continuation_ref": self.owner,
        }
        self.write(p + "QUESTION_WORK_RETURN.json", json.dumps(question))
        self.current = self.commit("synthetic two return records")
        result = gate.after_return(self.view(), RID)
        self.assertTrue(result["ok"], result)
        question["binding_ref"] = self.owner
        self.write(p + "QUESTION_WORK_RETURN.json", json.dumps(question))
        self.current = self.commit("synthetic wrong binding")
        result = gate.after_return(self.view(), RID)
        self.assertIn("QUESTION_WORK_RETURN_BINDING_MISMATCH", result["errors"])

    def prepare_binding_returns(self):
        self.prepare_reader()
        path = self.repo / gate.READER_TASK
        original = path.read_text()
        changed = copy.deepcopy(self.reader_binding)
        changed["question_ids"] = ["OTHER"]
        extra = (
            '<a id="other-binding"></a>\n```json\n' + json.dumps(changed) + '\n```\n'
            '<a id="same-content-other-position"></a>\n```json\n'
            + json.dumps(self.reader_binding) + '\n```\n'
            '<a id="multiple-json"></a>\n```json\n'
            + json.dumps(self.reader_binding) + '\n```\n```json\n{}\n```\n'
            '<a id="duplicate-key"></a>\n```json\n'
            '{"schema":"question-work/v2","kind":"BINDING","kind":"BINDING"}\n```\n'
            '<a id="duplicate-anchor"></a>\nfirst\n'
            '<a id="duplicate-anchor"></a>\nsecond\n')
        self.write(gate.READER_TASK, original + extra)
        self.binding_source_commit = self.commit('synthetic multiple targets, never real authority')
        self.record['binding_ref']['commit'] = self.binding_source_commit
        self.reader_event['binding_ref'] = copy.deepcopy(self.record['binding_ref'])
        self.returned = {
            'schema': 'question-work/v2', 'kind': 'RETURN', 'work_id': 'BI-01',
            'invocation_id': self.record['invocation_id'],
            'binding_ref': self.record['binding_ref'] | {'selector': '#question-work-binding'},
            'focus_results': [{'question_id': 'AUDIT'}], 'trigger_observations': [],
            'continuation_ref': {'answer_ref': '#same-work'}, 'batch_remaining_ref': None,
        }
        self.returned_role = {
            'schema': 'longrun-return/v1', 'work_id': 'BI-01',
            'invocation_id': self.record['invocation_id'],
            'assignment_token': self.record['assignment_token'],
            'question_work_ref': '#question-work-return',
            'handoff': {'kind': 'CONTINUE', 'instructions_ref': '#same-work'},
            'remaining_scope_ref': None,
        }
        p = RUN + '/provenance/turns/' + self.reader_round + '/'
        self.write(p + 'SEND_RECEIPT.json', json.dumps({'state': 'COMMITTED'}))
        self.write(p + 'FULL_RESPONSE.md', 'Synthetic complete response, no real Pro.\n')
        self.save_binding_returns()

    def save_binding_returns(self):
        p = RUN + '/provenance/turns/' + self.reader_round + '/'
        self.write(p + 'QUESTION_WORK_RETURN.json', json.dumps(self.returned))
        self.write(p + 'ROLE_RETURN.json', json.dumps(self.returned_role))
        self.save_reader('synthetic saved original dispatch and returns')

    def binding_associations(self, binding=None):
        return question_work.association_errors(
            self.reader_binding if binding is None else binding,
            self.returned, self.returned_role, self.record['binding_ref'],
            '#question-work-return', self.record['invocation_id'],
            self.record['assignment_token'], binding_resolver=lambda loc:
            coordinator.binding_target(self.repo, loc, 'daowei2026/observe-iterate'))

    def test_binding_anchor_and_lines_reach_same_original_object_in_both_consumers(self):
        self.prepare_binding_returns()
        for ref in (self.returned['binding_ref'], self.record['binding_ref']):
            with self.subTest(ref=ref):
                changed_ref = self.returned['binding_ref'] != ref
                self.returned['binding_ref'] = copy.deepcopy(ref)
                if changed_ref:
                    self.save_binding_returns()
                self.assertEqual(self.binding_associations(), [])
                result = gate.after_return(self.view(), self.reader_round)
                self.assertTrue(result['ok'], result)
        changed = copy.deepcopy(self.reader_binding)
        changed['routes']['same_work']['recipient_ref'] = 'different-authority'
        self.assertIn('BINDING_MISMATCH', self.binding_associations(changed))

    def test_binding_equivalence_rejects_wrong_missing_ambiguous_and_partial_targets(self):
        self.prepare_binding_returns()
        expected = copy.deepcopy(self.record['binding_ref'])
        cases = [
            {'repo': 'other/repository'}, {'commit': self.input_commit},
            {'commit': 'f' * 40}, {'path': 'missing.md'}, {'selector': '#missing'},
            {'selector': '#other-binding'}, {'selector': '#same-content-other-position'},
            {'selector': '#multiple-json'}, {'selector': '#duplicate-key'},
            {'selector': '#duplicate-anchor'}, {'selector': 'full'},
            {'selector': ''},
            {'selector': 'L1-L2'}, {'selector': 'L999999-L999999'},
            {'selector': expected['selector'].replace('L', '', 1)},
        ]
        for change in cases:
            with self.subTest(change=change):
                self.returned['binding_ref'] = expected | change
                self.save_binding_returns()
                self.assertIn('BINDING_MISMATCH', self.binding_associations())
                errors = gate.after_return(self.view(), self.reader_round)['errors']
                self.assertIn('QUESTION_WORK_RETURN_BINDING_MISMATCH', errors)
        missing = expected | {'commit': 'f' * 40}
        self.assertFalse(question_work.binding_refs_equal(
            missing, missing, resolver=lambda loc: coordinator.binding_target(
                self.repo, loc, 'daowei2026/observe-iterate')))

    def test_binding_resolution_does_not_override_other_original_associations(self):
        self.prepare_binding_returns()
        self.returned['invocation_id'] = 'wrong-invocation'
        self.returned_role['assignment_token'] = 'wrong-token'
        self.returned_role['question_work_ref'] = '#another-answer'
        self.save_binding_returns()
        errors = self.binding_associations()
        for expected in ('INVOCATION_MISMATCH', 'TOKEN_MISMATCH', 'RETURN_REFERENCE_MISMATCH'):
            self.assertIn(expected, errors)
        errors = gate.after_return(self.view(), self.reader_round)['errors']
        self.assertIn('QUESTION_WORK_RETURN_MISMATCH:invocation_id', errors)
        self.assertIn('ROLE_RETURN_MISMATCH:assignment_token', errors)


if __name__ == "__main__":
    unittest.main()
