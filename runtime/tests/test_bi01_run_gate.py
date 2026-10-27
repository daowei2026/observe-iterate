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

    def prepare_reader(self, short=False):
        """Entirely synthetic Git history; it is never a real GO/reader/intake."""
        reader = gate.READER_TASK
        self.write(RUN + "/README.md", '<a id="common"></a>\nSynthetic common\n<a id="bi01"></a>\nSynthetic run\n')
        self.write(RUN + "/00_长程推进地图.md", '<a id="goal"></a>\nSynthetic map\n')
        self.write(RUN + "/01_当前任务.md", 'Synthetic complete S1/S2/S3 task; no business result.\n')
        goal = json.loads((PROJECT / "runtime/config/COORDINATOR_DISPATCH.json").read_text())["works"]["BI-01"]["goal_ref"]["path"]
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
                               'watch_roots': [RUN + '/artifacts', RUN + '/reviews/independent'],
                               'reader_output_roots': [RUN + '/reviews/independent/workmap-01']}},
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
        self.reader_binding['routes']['decide'] = copy.deepcopy(self.reader_binding['routes']['accept'])
        self.reader_binding['routes']['decide']['instructions_ref'] = body_ref | {'selector': '#scope'}
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
        if short:
            self.publish_short_message()

    def publish_short_message(self):
        prepared = coordinator.prepare_dispatch(self.repo, self.policy,
                         'runtime/config/COORDINATOR_DISPATCH.json', self.reader_event)
        path = RUN + '/provenance/turns/' + self.reader_round + '/FULL_ASSIGNMENT.md'
        self.write(path, prepared['message'])
        published = self.commit('synthetic exact full assignment, NO PHONE')
        loc = self.loc(path) | {'commit': published}
        short = coordinator.github_reference_message(self.repo, prepared, loc)
        self.prompt = short['message']
        self.record.update(message_transport='github_reference',
                           full_assignment_ref=short['github_message_ref'],
                           full_assignment_sha256=prepared['message_sha256'],
                           prompt_sha256=short['message_sha256'],
                           prompt_utf8_bytes=len(self.prompt.encode('utf-8')),
                           prompt_utf16_units=len(self.prompt.encode('utf-16-le')) // 2)
        self.save_reader('synthetic short carrier and blob metadata, NO PHONE')

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

    def test_short_reader_verifies_full_archive_blob_digest_and_phone_separately(self):
        self.prepare_reader(short=True)
        self.assertTrue(gate.pre_dispatch(self.view(), self.reader_round)['ok'])
        original = copy.deepcopy(self.record)
        for change, expected in (
            ({'full_assignment_sha256': '0' * 64}, 'FULL_ASSIGNMENT_DIGEST_MISMATCH'),
            ({'full_assignment_ref': original['full_assignment_ref'] | {'blob': '0' * 40}}, 'FULL_ASSIGNMENT_BLOB_MISMATCH'),
            ({'full_assignment_ref': original['full_assignment_ref'] | {'commit': 'f' * 40}}, 'FULL_ASSIGNMENT_SOURCE_MISMATCH'),
            ({'full_assignment_ref': original['full_assignment_ref'] | {'selector': 'L1-L2'}}, 'FULL_TEXT_REQUIRED'),
            ({'full_assignment_ref': original['full_assignment_ref'] | {'path': RUN + '/README.md'}}, 'FULL_ASSIGNMENT_SOURCE_MISMATCH'),
            ({'full_assignment_ref': original['full_assignment_ref'] | {'repo': 'other/repo'}}, 'FULL_ASSIGNMENT_SOURCE_MISMATCH'),
            ({'full_assignment_ref': original['full_assignment_ref'] | {'unknown': 'ignored?'}}, 'INVALID_OR_UNKNOWN_FIELDS'),
            ({'recipient_ref': 'wrong-manager'}, 'RECIPIENT_CHANGED'),
            ({'prompt_utf8_bytes': 1}, 'PROMPT_METADATA_MISMATCH'),
            ({'reader_input_commit': 'f' * 40}, 'READER_INPUT_METADATA_MISMATCH:reader_input_commit'),
            ({'reader_fingerprint': '0' * 64}, 'READER_INPUT_METADATA_MISMATCH:reader_fingerprint'),
        ):
            with self.subTest(expected=expected, change=change):
                self.record = copy.deepcopy(original)
                self.record.update(change)
                self.save_reader('synthetic rejected short metadata')
                errors = gate.pre_dispatch(self.view(), self.reader_round)['errors']
                self.assertTrue(any(expected in e for e in errors), errors)
        self.record = original
        archive = self.record['full_assignment_ref']['path']
        self.write(archive, (self.repo / archive).read_text() + '篡改完整任务。\n')
        changed = self.commit('synthetic modified full archive')
        self.record['full_assignment_ref'].update(commit=changed, blob=self.git('rev-parse', changed + ':' + archive))
        self.save_reader('synthetic rehashed wrong full task')
        errors = gate.pre_dispatch(self.view(), self.reader_round)['errors']
        self.assertTrue(any('DIFFERS_FROM_PREPARED' in e for e in errors), errors)

    def test_short_phone_rehash_does_not_approve_tampering_or_unknown_send(self):
        self.prepare_reader(short=True)
        self.prompt += '未授权尾文。\n'
        self.record['prompt_sha256'] = hashlib.sha256(self.prompt.encode()).hexdigest()
        self.save_reader('synthetic rehashed short tampering')
        self.assertTrue(any('MESSAGE_CHANGED' in e for e in gate.pre_dispatch(self.view(), self.reader_round)['errors']))
        self.write(RUN + '/provenance/turns/' + self.reader_round + '/SEND_RECEIPT.json', '{"state":"UNKNOWN"}')
        self.current = self.commit('synthetic unknown send')
        self.assertIn('SEND_NOT_SAFE:UNKNOWN', gate.pre_dispatch(self.view(), self.reader_round)['errors'])

    def prepare_reader_reception(self, standalone=False, short=False):
        self.prepare_reader(short=short)
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
        question_ref = response | {'selector': '#question-work-return'}
        role_ref = None
        if standalone:
            self.write(p + 'FULL_RESPONSE.md', self.record['invocation_id'] + '\n完整隔离读者报告，未执行真实审查。\n')
            response_commit = self.commit('synthetic standalone full report and question return')
            response = self.loc(p + 'FULL_RESPONSE.md') | {'commit': response_commit}
            question_ref = self.loc(p + 'QUESTION_WORK_RETURN.json') | {'commit': response_commit}
            self.reader_role_return['question_work_ref'] = 'github:' + coordinator.cite(question_ref)
            self.write(p + 'ROLE_RETURN.json', json.dumps(self.reader_role_return))
            role_commit = self.commit('synthetic standalone role return')
            role_ref = self.loc(p + 'ROLE_RETURN.json') | {'commit': role_commit}
        for key in ('message_transport', 'full_assignment_ref', 'full_assignment_sha256',
                    'prompt_utf8_bytes', 'prompt_utf16_units'):
            self.record.pop(key, None)

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
                                 latest_return_ref=question_ref)
        if role_ref:
            self.reader_event['latest_role_return_ref'] = role_ref
        prepared = coordinator.prepare_dispatch(self.repo, self.policy,
                                                 'runtime/config/COORDINATOR_DISPATCH.json', self.reader_event)
        self.prompt = prepared['message']
        self.record['prompt_sha256'] = hashlib.sha256(self.prompt.encode()).hexdigest()
        self.save_reader('synthetic original manager receives actual first Reader')
        if short:
            self.publish_short_message()

    def test_first_reader_can_return_to_its_signed_manager_before_adoption(self):
        self.prepare_reader_reception()
        result = gate.pre_dispatch(self.view(), self.reader_round)
        self.assertTrue(result['ok'], result)
        self.assertFalse(self.view().exists(self.map_binding['receipt_path']))

    def test_short_reception_accepts_independent_report_and_two_json_returns(self):
        self.prepare_reader_reception(standalone=True, short=True)
        self.assertTrue(gate.pre_dispatch(self.view(), self.reader_round)['ok'])
        self.assertNotIn('```json', (self.repo / RUN / 'provenance/turns' / self.original_reader_round / 'FULL_RESPONSE.md').read_text())
        original_event = copy.deepcopy(self.reader_event)
        role_ref = self.reader_event['latest_role_return_ref']
        self.write(role_ref['path'], json.dumps(self.reader_role_return | {'assignment_token': 'other-token'}))
        changed = self.commit('synthetic standalone wrong original token')
        self.reader_event['latest_role_return_ref']['commit'] = changed
        self.publish_short_message()
        errors = gate.pre_dispatch(self.view(), self.reader_round)['errors']
        self.assertTrue(any('ROLE_RETURN_MISMATCH:assignment_token' in e for e in errors), errors)
        self.reader_event = original_event
        self.write(role_ref['path'], json.dumps(self.reader_role_return))
        self.current = self.commit('synthetic restore original return')
        self.reader_role_return['question_work_ref'] = 'github:wrong/repo@' + 'f' * 40 + ':q.json::full'
        self.write(role_ref['path'], json.dumps(self.reader_role_return))
        changed = self.commit('synthetic wrong Q-Return reference')
        self.reader_event['latest_role_return_ref']['commit'] = changed
        with self.assertRaisesRegex(ValueError, 'GITHUB_QUESTION_RETURN_REFERENCE_MISMATCH'):
            self.publish_short_message()

    def test_independent_return_final_tree_drift_and_binding_mismatch_are_rejected(self):
        self.prepare_reader_reception(standalone=True, short=True)
        response = self.reader_event['latest_response_ref']
        self.write(response['path'], self.original_reader_record['invocation_id'] + '\n不同的报告。\n')
        changed = self.commit('synthetic report diverged at final role tree')
        self.reader_event['latest_role_return_ref']['commit'] = changed
        with self.assertRaisesRegex(ValueError, 'GITHUB_RETURN_SOURCES_DIVERGED'):
            self.publish_short_message()

    def prepare_problem(self):
        self.prepare_reader(short=True)
        original_record = copy.deepcopy(self.record)
        p = RUN + '/provenance/turns/' + self.reader_round + '/'
        self.write(p + 'SEND_RECEIPT.json', json.dumps({'state': 'NOT_SENT', 'invocation_id': self.record['invocation_id']}))
        self.write(p + 'DISPATCH_BLOCKER.md', '隔离 fixture：NOT_SENT / MESSAGE_CHANGED；未调用手机。\n')
        self.blocker_result = {'check': 'pre-dispatch', 'round_id': self.reader_round,
                              'ok': False, 'sent': False, 'business_gate': False,
                              'recorded_send_state': 'NOT_SENT',
                              'errors': ['FIRST_READER_PRE_ADOPTION_INVALID:MESSAGE_CHANGED']}
        self.write(p + 'PRE_DISPATCH_RESULT.json', json.dumps(self.blocker_result))
        self.blocked_commit = self.commit('synthetic historical unsent blocker evidence')
        self.blocked_round = self.reader_round
        self.blocked_record = original_record
        self.reader_round = 'R0004'
        self.record = {k: v for k, v in original_record.items() if k not in
                       ('message_transport', 'full_assignment_ref', 'full_assignment_sha256',
                        'prompt_utf8_bytes', 'prompt_utf16_units')}
        self.record.update(round_id=self.reader_round, role='management',
                           invocation_id='BI01-V2-02-R0004-synthetic-problem',
                           assignment_token='synthetic-problem-token', recipient_ref='synthetic-management-chat')
        self.record['round_marker'] = '[' + self.record['invocation_id'] + ']'
        self.reader_event = {k: self.record[k] for k in
                             ('work_id', 'invocation_id', 'assignment_token', 'binding_ref',
                              'current_task_ref', 'task_adoption_ref')}
        self.reader_event.update(route='decide', dispatch_kind='NORMAL', send_state='NOT_SENT',
            evidence_refs=[self.loc(p + name) | {'commit': self.blocked_commit}
                           for name in ('DISPATCH_BLOCKER.md', 'PRE_DISPATCH_RESULT.json')])
        self.publish_short_message()

    def test_actual_unsent_problem_returns_to_issuer_without_reader_result(self):
        self.prepare_problem()
        result = gate.pre_dispatch(self.view(), self.reader_round)
        self.assertTrue(result['ok'], result)
        self.assertEqual(result['reception_kind'], 'ORIGINAL_ISSUER_PROBLEM')
        self.assertFalse(result['reader_dispatch_ready'])
        self.assertFalse(self.view().exists(self.map_binding['receipt_path']))
        self.write(RUN + '/artifacts/synthetic-worker/report.md', '真实输入变动的 fixture。\n')
        self.current = self.commit('synthetic watched input changed')
        result = gate.pre_dispatch(self.view(), self.reader_round)
        self.assertTrue(result['ok'], result)
        self.assertEqual(result['reader_input_errors'], ['FIRST_READER_INPUT_CHANGED'])
        self.assertTrue(any('FIRST_READER_INPUT_CHANGED' in e for e in gate.pre_dispatch(self.view(), self.blocked_round)['errors']))

    def test_decide_is_not_a_general_management_or_accept_exemption(self):
        self.prepare_problem()
        self.reader_event['route'] = 'accept'
        self.publish_short_message()
        self.assertFalse(gate.pre_dispatch(self.view(), self.reader_round)['ok'])
        self.reader_event['route'] = 'decide'
        self.reader_event['evidence_refs'] = []
        self.publish_short_message()
        self.assertTrue(any('READER_BLOCKER_EVIDENCE_REQUIRED' in e for e in gate.pre_dispatch(self.view(), self.reader_round)['errors']))
        self.reader_event['evidence_refs'] = [self.loc(RUN + '/README.md')]
        self.publish_short_message()
        self.assertFalse(gate.pre_dispatch(self.view(), self.reader_round)['ok'])

    def test_problem_does_not_hide_unknown_reader_send(self):
        self.prepare_problem()
        self.write(RUN + '/provenance/turns/' + self.blocked_round + '/SEND_RECEIPT.json', '{"state":"UNKNOWN"}')
        self.current = self.commit('synthetic affected Reader send now unknown')
        errors = gate.pre_dispatch(self.view(), self.reader_round)['errors']
        self.assertTrue(any('BLOCKED_READER_SEND_NOT_SAFE' in e for e in errors), errors)

    def test_blocker_claim_without_the_exact_affected_preparation_is_rejected(self):
        self.prepare_problem()
        path = RUN + '/provenance/turns/' + self.blocked_round + '/PRE_DISPATCH_RESULT.json'
        self.write(path, json.dumps(self.blocker_result | {'errors': ['arbitrary-error']}))
        changed = self.commit('synthetic unsupported blocker claim')
        for loc in self.reader_event['evidence_refs']:
            loc['commit'] = changed
        self.publish_short_message()
        errors = gate.pre_dispatch(self.view(), self.reader_round)['errors']
        self.assertTrue(any('READER_BLOCKER_RESULT_INVALID' in e for e in errors), errors)

    def test_frozen_watch_roots_cannot_be_changed_and_reader_output_stays_excluded(self):
        self.prepare_reader(short=True)
        self.write(RUN + '/reviews/independent/workmap-01/REVIEW.md', '隔离只读产物，不构成真实 PASS。\n')
        self.current = self.commit('synthetic dedicated Reader output remains excluded')
        self.assertTrue(gate.pre_dispatch(self.view(), self.reader_round)['ok'])
        self.map_binding['streams']['bi01']['watch_roots'].append(RUN + '/other-results')
        self.write(gate.BINDING, json.dumps(self.map_binding))
        self.current = self.commit('synthetic changed protected binding')
        self.assertTrue(any('FIRST_READER_INPUT_CHANGED' in e for e in gate.pre_dispatch(self.view(), self.reader_round)['errors']))

    def prepare_worker_reception(self):
        self.prepare_problem()
        self.issuer_round = self.reader_round
        self.issuer_record = copy.deepcopy(self.record)
        p = RUN + '/provenance/turns/' + self.issuer_round + '/'
        self.order_id = 'SYNTHETIC-READER-REPAIR'
        self.order_path = RUN + '/reviews/management-' + self.issuer_round + '/WORKER_ORDER.md'
        self.report_path = RUN + '/artifacts/worker-' + self.order_id + '/FULL_RESPONSE.md'
        fields = {'order_id': self.order_id, 'work_id': 'BI-01', 'run_id': 'BI-01-V2-02',
                  'issuer_role': 'management', 'issuer_ref': self.record['recipient_ref'],
                  'issuer_invocation_id': self.record['invocation_id'],
                  'issuer_assignment_token': self.record['assignment_token'],
                  'return_to': self.record['recipient_ref'], 'worker_thread_id': 'synthetic-worker-thread'}
        self.order_fields = fields
        self.write(self.order_path, '\n'.join(k + ': ' + v for k, v in fields.items()) + '\n隔离签发工单。\n')
        self.write(p + 'FULL_RESPONSE.md', self.record['invocation_id'] + '\n隔离管理裁定。\n')
        order_commit = self.commit('synthetic management order and report')
        self.order_ref = self.loc(self.order_path) | {'commit': order_commit}
        qret = self.reader_return = {
            'schema': 'question-work/v2', 'kind': 'RETURN', 'work_id': 'BI-01',
            'invocation_id': self.record['invocation_id'], 'binding_ref': self.record['binding_ref'],
            'focus_results': [{'question_id': 'AUDIT'}], 'trigger_observations': [],
            'continuation_ref': self.order_ref}
        self.write(p + 'QUESTION_WORK_RETURN.json', json.dumps(qret))
        qcommit = self.commit('synthetic management question return')
        question_ref = self.loc(p + 'QUESTION_WORK_RETURN.json') | {'commit': qcommit}
        role = {'schema': 'longrun-return/v1', 'work_id': 'BI-01',
                'invocation_id': self.record['invocation_id'], 'assignment_token': self.record['assignment_token'],
                'question_work_ref': 'github:' + coordinator.cite(question_ref),
                'artifact_refs': [{k: self.order_ref[k] for k in ('repo', 'commit', 'path')}],
                'role_outputs': {'management': {'issued_work_refs': ['github:' + coordinator.cite(self.order_ref)]}},
                'handoff': {'kind': 'SUBMIT', 'route_key': 'decide'}}
        self.write(p + 'ROLE_RETURN.json', json.dumps(role))
        self.issuer_receipt = {k: self.record[k] for k in
                               ('work_id', 'run_id', 'invocation_id', 'assignment_token', 'recipient_ref')}
        self.write(p + 'SEND_RECEIPT.json', json.dumps(self.issuer_receipt | {'state': 'COMMITTED'}))
        role_commit = self.commit('synthetic reconciled manager call, NO PHONE')
        self.write(self.report_path, '\n'.join(k + ': ' + v for k, v in fields.items()
            if k not in ('issuer_assignment_token', 'issuer_role', 'issuer_ref')) + '\n隔离技术结果，无真实生产结论。\n')
        report_commit = self.commit('synthetic worker report changes watched artifacts')
        self.reader_round = 'R0005'
        for key in ('message_transport', 'full_assignment_ref', 'full_assignment_sha256',
                    'prompt_utf8_bytes', 'prompt_utf16_units'):
            self.record.pop(key, None)
        self.record.update(round_id=self.reader_round, invocation_id='BI01-V2-02-R0005-synthetic-worker-reception',
                           assignment_token='synthetic-worker-reception-token')
        self.record['round_marker'] = '[' + self.record['invocation_id'] + ']'
        self.reader_event = {k: self.record[k] for k in
                             ('work_id', 'invocation_id', 'assignment_token', 'binding_ref',
                              'current_task_ref', 'task_adoption_ref')}
        self.reader_event.update(route='decide', dispatch_kind='NORMAL', send_state='NOT_SENT',
            latest_response_ref=self.loc(p + 'FULL_RESPONSE.md') | {'commit': order_commit},
            latest_return_ref=question_ref,
            latest_role_return_ref=self.loc(p + 'ROLE_RETURN.json') | {'commit': role_commit},
            evidence_refs=[self.order_ref, self.loc(self.report_path) | {'commit': report_commit}])
        self.publish_short_message()

    def test_signed_worker_result_returns_to_original_issuer_without_fake_intake(self):
        self.prepare_worker_reception()
        result = gate.pre_dispatch(self.view(), self.reader_round)
        self.assertTrue(result['ok'], result)
        self.assertEqual(result['reader_input_errors'], ['FIRST_READER_INPUT_CHANGED'])
        self.assertFalse(result['reader_dispatch_ready'])
        self.assertFalse(self.view().exists(self.map_binding['receipt_path']))

    def test_worker_result_cannot_borrow_an_unsigned_order_or_reader_accept(self):
        self.prepare_worker_reception()
        self.reader_event['route'] = 'accept'
        self.publish_short_message()
        self.assertFalse(gate.pre_dispatch(self.view(), self.reader_round)['ok'])
        self.reader_event['route'] = 'decide'
        self.write(self.order_path, (self.repo / self.order_path).read_text() + '未由原 Return 签发的修改。\n')
        changed = self.commit('synthetic unissued order revision')
        self.reader_event['evidence_refs'][0]['commit'] = changed
        self.publish_short_message()
        errors = gate.pre_dispatch(self.view(), self.reader_round)['errors']
        self.assertTrue(any('WORKER_ORDER_NOT_ISSUED' in e for e in errors), errors)

    def test_worker_result_requires_issued_order_original_identity_and_reconciled_send(self):
        self.prepare_worker_reception()
        original_report = (self.repo / self.report_path).read_text()
        for key in ('order_id', 'work_id', 'run_id', 'issuer_invocation_id', 'return_to', 'worker_thread_id'):
            with self.subTest(key=key):
                self.write(self.report_path, original_report.replace(self.order_fields[key], 'other-value', 1))
                changed = self.commit('synthetic wrong Worker report identity')
                self.reader_event['evidence_refs'][1]['commit'] = changed
                self.publish_short_message()
                self.assertFalse(gate.pre_dispatch(self.view(), self.reader_round)['ok'])
        self.write(self.report_path, original_report)
        report_commit = self.commit('synthetic restored actual report')
        self.reader_event['evidence_refs'][1]['commit'] = report_commit
        self.publish_short_message()
        path = RUN + '/provenance/turns/' + self.issuer_round + '/SEND_RECEIPT.json'
        for receipt in (self.issuer_receipt | {'state': 'NOT_SENT'},
                        self.issuer_receipt | {'state': 'UNKNOWN'},
                        self.issuer_receipt | {'state': 'COMMITTED', 'assignment_token': 'wrong'}):
            with self.subTest(receipt=receipt):
                self.write(path, json.dumps(receipt))
                self.current = self.commit('synthetic unverified original issuer send')
                self.assertFalse(gate.pre_dispatch(self.view(), self.reader_round)['ok'])

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
                    ({'task_adoption_ref': self.loc(RUN + '/OWNER_START.md')}, 'FIRST_READER_MANAGEMENT_ADOPTION_REQUIRED')]
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
