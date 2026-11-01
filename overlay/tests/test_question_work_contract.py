"""Offline schema and cross-reference checks only; no semantic or scheduler claim.
Run: python tests/test_question_work_contract.py
Requires the already available jsonschema package.
"""
import copy
import json
from pathlib import Path
import unittest
from jsonschema import Draft202012Validator

HERE = Path(__file__).resolve().parent
SCHEMA_PATH = HERE.parent / 'tools' / 'question_work.schema.json'
if not SCHEMA_PATH.exists():  # local authoring validation
    SCHEMA_PATH = HERE / 'question_work.schema.json'
SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding='utf-8'))
V = Draft202012Validator(SCHEMA)

def ar(name):
    return {'answer_ref': '#' + name}

def samples():
    # Synthetic identifiers test structure only; these are not claimed repo artifacts.
    route = {'recipient_role': 'professional', 'recipient_ref': 'synthetic-builder',
             'instructions_ref': ar('issued-message')}
    b = {'schema': 'question-work/v1', 'kind': 'BINDING', 'work_id': 'synthetic-work',
         'batch_result': '本段完整业务形成及修订合同', 'question_ids': ['A-2', 'A-3', 'A-4'],
         'professional_mode': 'LOCAL_CONTRACT',
         'source_reads': [{'source': {'repo': 'fixture/repo', 'commit': 'a' * 40,
             'path': 'method.md', 'selector': '完整方法'}, 'requirement': 'MODE_FULL',
             'purpose': '形成、时序及完整合同的专业约束', 'reuse_evidence': None}],
         'routes': {key: copy.deepcopy(route) for key in ('same_work', 'accept', 'decide', 'return_repair')},
         'triggers': [{'trigger_id': 'formation-review', 'kind': 'RESULT',
             'condition_ref': ar('formation-condition'), 'signal_key': 'formation-visible',
             'route': dict(route, recipient_role='management', recipient_ref='synthetic-manager'),
             'blocking': False, 'effort_limit': None}], 'explicit_no_trigger_reason_ref': None}
    for key in ('goal_ref', 'plan_ref', 'full_scope_ref', 'focus_ref', 'coverage_ref',
                'deliverables_ref', 'completion_ref', 'budget_ref'):
        b[key] = ar(key)
    r = {'schema': 'question-work/v1', 'kind': 'RETURN', 'work_id': b['work_id'],
         'invocation_id': 'synthetic-call-2', 'binding_ref': ar('binding'),
         'focus_results': [{'question_id': 'A-2', 'completed_ref': ar('actual-result'),
             'remaining_ref': ar('remaining'), 'affected_refs': [ar('contract')]}],
         'material_use_ref': ar('material-use'), 'trigger_observations': [
             {'trigger_id': 'formation-review', 'state': 'SATISFIED', 'evidence_ref': ar('formation-result')}],
         'continuation_ref': ar('continue-consumers')}
    return b, r

def association_errors(binding, returned):
    """Test-only mechanical joins. Does not decide business completion/authority."""
    errors = []
    if returned['work_id'] != binding['work_id']:
        errors.append('WORK_MISMATCH')
    if any(x['question_id'] not in binding['question_ids'] for x in returned['focus_results']):
        errors.append('QUESTION_NOT_ASSIGNED')
    expected = [x['trigger_id'] for x in binding['triggers']]
    observed = [x['trigger_id'] for x in returned['trigger_observations']]
    if len(expected) != len(set(expected)) or len(observed) != len(set(observed)):
        errors.append('DUPLICATE_TRIGGER')
    if set(expected) != set(observed):
        errors.append('TRIGGER_COVERAGE_MISMATCH')
    return errors

class QuestionWorkTests(unittest.TestCase):
    def test_schema_and_positive_pair(self):
        Draft202012Validator.check_schema(SCHEMA)
        b, r = samples()
        V.validate(b); V.validate(r)
        self.assertEqual(association_errors(b, r), [])

    def test_required_binding_fields(self):
        b, _ = samples()
        for field in ('goal_ref', 'batch_result', 'coverage_ref', 'completion_ref', 'budget_ref', 'routes'):
            with self.subTest(field=field):
                bad = copy.deepcopy(b); del bad[field]
                self.assertFalse(V.is_valid(bad))

    def test_ref_and_unknown_field(self):
        b, _ = samples()
        for field, value in (('commit', 'main'), ('selector', ''), ('path', '')):
            with self.subTest(field=field):
                bad = copy.deepcopy(b); bad['source_reads'][0]['source'][field] = value
                self.assertFalse(V.is_valid(bad))
        b['invented_authority'] = True
        self.assertFalse(V.is_valid(b))

    def test_empty_triggers_require_explicit_reason(self):
        b, _ = samples(); b['triggers'] = []
        self.assertFalse(V.is_valid(b))
        b['explicit_no_trigger_reason_ref'] = ar('authorized-no-extra-trigger')
        V.validate(b)

    def test_effort_has_measurable_origin(self):
        b, _ = samples(); t = b['triggers'][0]; t['kind'] = 'EFFORT'
        self.assertFalse(V.is_valid(b))
        t['effort_limit'] = {'unit': 'EFFECTIVE_CALLS', 'limit': 4, 'count_from_ref': ar('actual-origin')}
        V.validate(b)  # example bound, not a universal production limit
        t['effort_limit']['limit'] = 0
        self.assertFalse(V.is_valid(b))

    def test_true_and_unknown_need_evidence(self):
        _, r = samples()
        for state in ('SATISFIED', 'UNKNOWN'):
            with self.subTest(state=state):
                bad = copy.deepcopy(r); bad['trigger_observations'][0].update(state=state, evidence_ref=None)
                self.assertFalse(V.is_valid(bad))

    def test_same_work_can_report_due_management(self):
        b, r = samples()
        self.assertEqual(r['work_id'], b['work_id'])
        self.assertIsNotNone(r['focus_results'][0]['remaining_ref'])
        self.assertEqual(r['trigger_observations'][0]['state'], 'SATISFIED')
        self.assertFalse(b['triggers'][0]['blocking'])
        V.validate(r)  # data can carry both responsibilities; no dispatch claim

    def test_association_failures(self):
        b, r = samples()
        bad = copy.deepcopy(r); bad['work_id'] = 'other'
        self.assertIn('WORK_MISMATCH', association_errors(b, bad))
        bad = copy.deepcopy(r); bad['focus_results'][0]['question_id'] = 'C-1'
        self.assertIn('QUESTION_NOT_ASSIGNED', association_errors(b, bad))
        bad = copy.deepcopy(r); bad['trigger_observations'] = []
        self.assertIn('TRIGGER_COVERAGE_MISMATCH', association_errors(b, bad))
        bad = copy.deepcopy(r); bad['trigger_observations'] *= 2
        self.assertIn('DUPLICATE_TRIGGER', association_errors(b, bad))

    def test_schema_does_not_assert_semantic_success(self):
        b, r = samples(); r['focus_results'][0]['completed_ref'] = ar('unproven-claim')
        V.validate(r)
        self.assertEqual(association_errors(b, r), [])
        # Existence/meaning/review/real dispatch must be checked separately.
        self.assertNotIn('business_pass', r)

if __name__ == '__main__':
    unittest.main(verbosity=2)
