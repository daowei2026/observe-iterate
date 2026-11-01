"""Offline contract tests. They do not run Pro, send messages or accept business artifacts."""
import copy,json,sys,unittest
from pathlib import Path
from jsonschema import Draft202012Validator
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[4]
sys.path.insert(0,str(HERE.parent/'tools'))
from question_work_check import association_errors, management_continuity_errors, pending_reviews
S=json.loads((HERE.parent/'tools/question_work.schema.json').read_text())
V=Draft202012Validator(S)
F=json.loads((HERE/'question_work_trial_inputs.json').read_text())
class RepairTests(unittest.TestCase):
 def setUp(self): self.b=copy.deepcopy(F['binding']);self.r=copy.deepcopy(F['returns'][0]);self.role=copy.deepcopy(F['role_returns'][0])
 def errors(self):return association_errors(self.b,self.r,self.role,F['binding_ref'],'#question-return','synthetic-call-1','synthetic-token-1')
 def test_schema(self): Draft202012Validator.check_schema(S)
 def test_bootstrap_without_plan(self): V.validate(F['bootstrap']);self.assertNotIn('plan_ref',F['bootstrap'])
 def test_bootstrap_rejects_prefilled_plan(self):
  x=copy.deepcopy(F['bootstrap']);x['plan_ref']={'answer_ref':'#invented'};self.assertFalse(V.is_valid(x))
 def test_parent_requirement(self):
  x=copy.deepcopy(F['bootstrap']);x['parent']['status']='PRESENT';self.assertFalse(V.is_valid(x));x['parent']['status']='REQUIRED_MISSING';V.validate(x)
 def test_positive_bind_and_return(self): V.validate(self.b);V.validate(self.r);self.assertEqual(self.errors(),[])
 def test_message_and_attachment_sources(self):
  for x in self.b['source_reads']: V.validate(dict(self.b,source_reads=[x]))
  V.validate(dict(self.b,source_reads=[dict(self.b['source_reads'][0],source=F['bootstrap']['goal_ref'])]))
 def test_null_reuse_is_not_read_receipt(self): self.assertIsNone(self.b['source_reads'][0]['reuse_evidence']);self.assertIn('material_use_ref',self.r)
 def test_latest_focus_is_allowed(self):
  self.assertNotEqual(self.b['focus_ref'],self.r['continuation_ref']);self.assertEqual(self.errors(),[])
 def test_continuation_conflict(self):
  self.role['handoff']['instructions_ref']='#wrong-next';self.assertIn('CONTINUATION_MISMATCH',self.errors())
 def test_scope_remaining_conflict(self):
  self.r['batch_remaining_ref']=None;self.assertIn('REMAINING_MISMATCH',self.errors())
 def test_wrong_identity_binding_and_token(self):
  self.r['binding_ref']={'answer_ref':'#other'};self.role['assignment_token']='wrong';self.r['work_id']='other';e=self.errors();self.assertIn('BINDING_MISMATCH',e);self.assertIn('TOKEN_MISMATCH',e);self.assertIn('WORK_MISMATCH',e)
 def test_case_question_needs_definition(self):
  self.b['question_ids'].append('CASE-extra');self.r['focus_results'][0]['question_id']='CASE-extra';V.validate(self.b);self.assertIn('CASE_DEFINITION_MISMATCH',self.errors());self.b['question_definitions']=[{'question_id':'CASE-extra','definition_ref':{'answer_ref':'#case-definition'},'authority_ref':F['bootstrap']['authority_ref'],'parent_question_id':None}];V.validate(self.b);self.assertEqual(self.errors(),[])
 def test_trigger_coverage(self): self.r['trigger_observations']=[];self.assertIn('TRIGGER_COVERAGE_MISMATCH',self.errors())
 def test_one_management_for_two_signals(self):
  d=pending_reviews(self.b,[],self.r['trigger_observations'],{'elapsed':2.5});self.assertEqual(len(d['due']),1)
 def test_new_evidence_does_not_rearm(self):
  key=[self.b['work_id'],'formation-review','cycle-first']
  for state in ('IN_FLIGHT','RETURNED','CONSUMED'):
   self.r['trigger_observations'][0]['evidence_ref']={'answer_ref':'#new-evidence'}
   self.assertEqual(pending_reviews(self.b,[{'key':key,'state':state}],self.r['trigger_observations'],{'elapsed':1})['due'],[])
 def test_no_answer_effort_check(self):
  d=pending_reviews(self.b,[],[],{'elapsed':2.5});self.assertEqual(len(d['due']),1);self.assertEqual(d['due'][0]['trigger_ids'],['elapsed'])
 def test_unknown_does_not_mean_not_yet(self):
  d=pending_reviews(self.b,[],[],{});self.assertIn('elapsed',d['unknown'])
 def test_result_not_yet_does_not_suppress_effort(self):
  x=[{'trigger_id':'formation','state':'NOT_YET','evidence_ref':None}];self.assertEqual(len(pending_reviews(self.b,[],x,{'elapsed':2.5})['due']),1)
 def test_rearm_needs_explicit_authority(self):
  ledger=[{'key':[self.b['work_id'],'formation-review','cycle-first'],'state':'CONSUMED'}]
  for t in self.b['triggers']:t['cycle_id']='cycle-second'
  self.assertIn('REARM_REFERENCE_MISSING',pending_reviews(self.b,ledger,self.r['trigger_observations'],{'elapsed':1})['errors'])
  for t in self.b['triggers']:t['rearm_ref']={'answer_ref':'#authorized-rearm'}
  self.assertEqual(len(pending_reviews(self.b,ledger,self.r['trigger_observations'],{'elapsed':1})['due']),1)
 def test_continuing_work_reports_missing_future_review(self):
  key=[self.b['work_id'],'formation-review','cycle-first'];ledger=[{'key':key,'state':'CONSUMED'}]
  self.assertEqual(management_continuity_errors(self.b,ledger,'ACTIVE'),['CONTINUING_WORK_WITHOUT_FUTURE_REVIEW'])
  self.assertEqual(management_continuity_errors(self.b,ledger,'PAUSED'),[])
  self.assertEqual(management_continuity_errors(self.b,ledger,'ACTIVE',True),[])
 def test_while_active_effort_review_repeats_without_new_chat_budget(self):
  effort=next(t for t in self.b['triggers'] if t['kind']=='EFFORT');effort['repeat']='WHILE_WORK_ACTIVE';V.validate(self.b)
  key=[self.b['work_id'],'formation-review','cycle-first'];ledger=[{'key':key,'state':'CONSUMED'}]
  self.assertEqual(management_continuity_errors(self.b,ledger,'ACTIVE'),[])
  self.assertEqual(pending_reviews(self.b,ledger,[],{'elapsed':3.9})['due'],[])
  due=pending_reviews(self.b,ledger,[],{'elapsed':4.0})['due'];self.assertEqual(len(due),1)
  self.assertEqual(due[0]['key'][-1],'cycle-first/repeat-2');self.assertEqual(due[0]['repeat_interval_index'],2)
  ledger.append({'key':due[0]['key'],'state':'RETURNED'})
  self.assertEqual(pending_reviews(self.b,ledger,[],{'elapsed':99})['due'],[])
  self.assertEqual(pending_reviews(self.b,ledger,[],{'elapsed':99},work_state='PAUSED')['due'],[])
 def test_repeat_is_not_allowed_on_result_trigger(self):
  next(t for t in self.b['triggers'] if t['kind']=='RESULT')['repeat']='WHILE_WORK_ACTIVE'
  self.assertFalse(V.is_valid(self.b))
 def test_checked_in_u2_u3_effort_bindings_adopt_continuous_review(self):
  case=REPO/'agent_evolution/pilot_cases/network-dynamic-ceps-factory-u2-u3/reviews'
  for rel in ('u2-management-r52/QUESTION_WORK_BINDING.json','u3-management-6ec40dbd/QUESTION_WORK_BINDING.json'):
   binding=json.loads((case/rel).read_text());V.validate(binding)
   effort=[t for t in binding['triggers'] if t['kind']=='EFFORT'];self.assertTrue(effort)
   self.assertTrue(all(t.get('repeat')=='WHILE_WORK_ACTIVE' for t in effort))
 def test_malformed_unrelated_ledger_key_does_not_crash_repeat_check(self):
  effort=next(t for t in self.b['triggers'] if t['kind']=='EFFORT');effort['repeat']='WHILE_WORK_ACTIVE'
  result=pending_reviews(self.b,[{'key':['unrelated'],'state':'CONSUMED'}],[],{'elapsed':2.5})
  self.assertEqual(result['errors'],[]);self.assertEqual(len(result['due']),1)
 def test_duplicate_trigger_is_rejected(self):
  self.b['triggers'].append(copy.deepcopy(self.b['triggers'][0]));self.assertIn('DUPLICATE_TRIGGER',self.errors())
 def test_legacy_pair(self):
  b=copy.deepcopy(self.b);b['schema']='question-work/v1';b.pop('question_definitions');b.pop('parent');b['goal_ref']=b['plan_ref'];b['source_reads']=b['source_reads'][:1]
  for t in b['triggers']:
   for k in ('obligation_id','cycle_id','rearm_ref'):t.pop(k)
  r=copy.deepcopy(self.r);r['schema']='question-work/v1';r.pop('batch_remaining_ref');r['binding_ref']={'answer_ref':'#legacy-binding'};r['focus_results'][0]['affected_refs']=[{'answer_ref':'#legacy-result'}]
  V.validate(b);V.validate(r)
if __name__=='__main__':unittest.main(verbosity=2)
