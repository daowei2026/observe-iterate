"""Actual temporary Git repositories; no network, no mocked git success."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import sys
import unittest

TOOL = Path(__file__).resolve().parents[1] / 'tools' / 'workmap_gate.py'

class WorkmapGateTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(TOOL.is_file(), 'management intake/dispatch guard has not been implemented')
        spec = importlib.util.spec_from_file_location('workmap_gate', TOOL)
        self.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.mod)
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        self.git('init', '-q')
        self.git('config', 'user.email', 'test@example.invalid')
        self.git('config', 'user.name', 'test')
        for p, s in {
            'README.md': '<a id="intent"></a>\n# Intent\nFilters and Reflex; CEPS is a different route.\n[Map](one/map.md)\n',
            'one/map.md': '<a id="whole"></a>\n# Whole\nThe full result remains.\n<a id="current"></a>\n# Current\n[Body](artifacts/body.md)\n',
            'two/map.md': '<a id="whole"></a>\n# Whole\nSecond independent stream.\n',
            'one/task.md': 'task_id: TASK-1\nstatus: ISSUED\n',
            'two/task.md': 'task_id: TASK-2\nstatus: ISSUED\n',
            'one/artifacts/body.md': 'Versioned business body; not a progress map.\n',
            'two/artifacts/body.md': 'Another business body.\n',
            'rules.md': 'Rule revision 1\n',
            'owner.md': 'Owner intent, with source.\n',
            'review.md': 'Manager actually inspected material; not an independent reader review.\n',
            'reader.md': 'Independent reader reconstructs intent and compares exact evidence.\n',
        }.items(): self.put(p, s)
        self.binding = {
            'schema': 'workmap-binding/v1', 'manager_role': 'management_review',
            'overview': {'path':'README.md', 'anchors':['intent']},
            'owner_sources':['owner.md'], 'rule_paths':['rules.md'],
            'receipt_path':'intake.json',
            'streams': {
                'one': {'map':{'path':'one/map.md','anchors':['whole','current']},
                        'task':'one/task.md','watch_roots':['one/artifacts']},
                'two': {'map':{'path':'two/map.md','anchors':['whole']},
                        'task':'two/task.md','watch_roots':['two/artifacts']},
            },
        }
        self.put_json('binding.json', self.binding)
        self.base = self.commit()
        self.receipts = {'schema':'workmap-intake/v1','intakes':{}}
        self.seal('one')
        self.seal('two')
        self.head = self.commit()

    def git(self, *args):
        return subprocess.check_output(['git','-C',str(self.repo),*args], stderr=subprocess.PIPE).decode().strip()
    def put(self, path, text):
        p = self.repo/path; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(text,encoding='utf-8')
    def put_json(self,path,data): self.put(path,json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    def commit(self):
        self.git('add','--all'); self.git('commit','-qm','fixture','--allow-empty')
        return self.git('rev-parse','HEAD')
    def seal(self, scope, reader=False):
        ref = self.git('rev-parse','HEAD')
        snap = self.mod.snapshot(self.repo,ref,'binding.json',scope)
        task = self.binding['streams'][scope]['task']
        self.receipts['intakes'][scope] = {
            'manager': {'role':'management_review','context':'manager-test'},
            'snapshot': snap['fingerprint'], 'observed_commit':ref,
            'decision_report':{'path':'review.md','blob':self.git('rev-parse',ref+':review.md')},
            'effort': {'known_pro_turns':2,'coverage':'partial','source_note':'two recorded test turns'},
            'reader_check': {'status':'RECORDED' if reader else 'PENDING',
                'context':'reader-test' if reader else None,
                'independent_of_map_builder':reader,
                'input_snapshot':snap['fingerprint'] if reader else None,
                'report':{'path':'reader.md','blob':self.git('rev-parse',ref+':reader.md')} if reader else None},
            'dispatch': {'task_path':task,'task_id':'TASK-1' if scope=='one' else 'TASK-2',
                         'task_blob':self.git('rev-parse',ref+':'+task),'decision':'ISSUED',
                         'kind':'EXISTING_AUTHORIZED_REPAIR','requires_reader_check':False},
            'validation_claims': [],
        }
        self.put_json('intake.json',self.receipts)
    def check(self,scope='one',**kwargs):
        return self.mod.check(self.repo,self.git('rev-parse','HEAD'),'binding.json',scope,**kwargs)
    def delivery(self,state='NOT_SENT'):
        ref=self.git('rev-parse','HEAD')
        return {'observed_commit':ref,'task_id':'TASK-1','task_blob':self.git('rev-parse',ref+':one/task.md'),
                'state':state,'evidence':'actual dispatcher send-log location'}
    def test_initial_mechanical_pass_is_not_independent_pass(self):
        r=self.check(); self.assertTrue(r['ok']); self.assertEqual(r['reader_qualification'],'PENDING')
    def test_new_body_requires_manager_intake(self):
        self.put('one/artifacts/body.md','Changed business body\n'); self.commit()
        r=self.check(); self.assertFalse(r['ok']); self.assertIn('INTAKE_STALE',r['errors'])
        self.assertEqual(r['next_action']['recipient'],'management_review')
    def test_rule_change_triggers_even_without_new_artifact(self):
        self.put('rules.md','Rule revision 2\n'); self.commit()
        self.assertIn('INTAKE_STALE',self.check()['errors'])
    def test_owner_correction_triggers_without_new_artifact(self):
        self.put('owner.md','Corrected owner intent\n'); self.commit()
        self.assertIn('INTAKE_STALE',self.check()['errors'])
    def test_other_stream_change_does_not_block_this_stream(self):
        self.put('two/artifacts/body.md','Second stream only\n'); self.commit()
        self.assertTrue(self.check('one')['ok']); self.assertFalse(self.check('two')['ok'])
    def test_scope_anchor_loss_rejected_even_if_receipt_resealed(self):
        self.put('one/map.md','<a id="current"></a>\n# Current\nOnly latest event.\n'); self.commit()
        self.seal('one'); self.commit()
        self.assertIn('MAP_ANCHOR_MISSING:one/map.md#whole',self.check()['errors'])
    def test_scope_protection_cannot_be_silently_removed_from_binding(self):
        before=self.git('rev-parse','HEAD')
        self.binding['streams']['one']['map']['anchors']=['current']
        self.put_json('binding.json',self.binding)
        self.put('one/map.md','<a id="current"></a>\n# Current\nOnly latest event.\n'); self.commit()
        self.seal('one'); self.commit()
        self.assertIn('SCOPE_REMOVED_WITHOUT_DISPOSITION:one/map.md#whole',self.check(base_ref=before)['errors'])
    def test_broken_reference_rejected(self):
        self.put('one/map.md','<a id="whole"></a>\n# Whole\nAll.\n<a id="current"></a>\n# Current\n[Missing](artifacts/missing.md)\n')
        self.commit(); self.seal('one'); self.commit()
        self.assertIn('LINK_MISSING:one/artifacts/missing.md',self.check()['errors'])
    def test_executor_may_change_business_map_but_not_progress_map(self):
        before=self.git('rev-parse','HEAD')
        self.put('one/artifacts/business_map.md','Business map owned by Mission A\n'); self.commit()
        r=self.check(actor='executor',base_ref=before)
        self.assertNotIn('EXECUTOR_MODIFIED_MANAGED_SURFACE',r['errors'])
        self.put('one/map.md',(self.repo/'one/map.md').read_text()+'\nExecutor changes progress.\n'); self.commit()
        self.assertIn('EXECUTOR_MODIFIED_MANAGED_SURFACE',self.check(actor='executor',base_ref=before)['errors'])
    def test_round_count_cannot_silently_reset(self):
        before=self.git('rev-parse','HEAD')
        self.receipts['intakes']['one']['effort']['known_pro_turns']=0
        self.put_json('intake.json',self.receipts); self.commit()
        self.assertIn('EFFORT_RESET_WITHOUT_SOURCE',self.check(base_ref=before)['errors'])
    def test_unrun_reader_cannot_unlock_new_stage(self):
        d=self.receipts['intakes']['one']['dispatch']; d['kind']='NEW_STAGE'; d['requires_reader_check']=False
        self.put_json('intake.json',self.receipts); self.commit()
        self.assertIn('READER_CHECK_REQUIRED',self.check(dispatch=True,delivery=self.delivery())['errors'])
    def test_actual_not_sent_observation_allows_existing_repair_only(self):
        self.assertTrue(self.check(dispatch=True,delivery=self.delivery())['ok'])
    def test_running_task_is_not_redispatched(self):
        self.assertIn('DELIVERY_NOT_SENDABLE:RUNNING',self.check(dispatch=True,delivery=self.delivery('RUNNING'))['errors'])
    def test_unknown_delivery_cannot_be_assumed_not_sent(self):
        self.assertIn('DELIVERY_OBSERVATION_REQUIRED',self.check(dispatch=True)['errors'])
    def test_stale_delivery_observation_rejected(self):
        old=self.delivery(); self.put('unrelated.md','non business\n'); self.commit()
        self.assertIn('DELIVERY_OBSERVATION_STALE',self.check(dispatch=True,delivery=old)['errors'])
    def test_test_on_old_code_cannot_prove_new_code(self):
        self.receipts['intakes']['one']['validation_claims']=[{
            'evidence':{'path':'review.md','blob':self.git('rev-parse','HEAD:review.md')},
            'tested_code_commit':'1'*40,'claimed_code_commit':'2'*40}]
        self.put_json('intake.json',self.receipts); self.commit()
        self.assertIn('VALIDATION_VERSION_MISMATCH',self.check()['errors'])
    def test_missing_intake_creates_targeted_action_not_business_rerun(self):
        self.git('rm','intake.json'); self.commit(); r=self.check()
        self.assertIn('INTAKE_MISSING',r['errors'])
        self.assertIn('不重跑',r['next_action']['instruction'])
    def test_forged_empty_reader_record_rejected(self):
        self.receipts['intakes']['one']['reader_check']={'status':'RECORDED','independent_of_map_builder':True}
        self.put_json('intake.json',self.receipts); self.commit()
        self.assertIn('READER_RECORD_INCOMPLETE',self.check()['errors'])
    def test_cli_check_requires_previous_input_for_continuity(self):
        result=subprocess.run([sys.executable,str(TOOL),'check','--repo',str(self.repo),
            '--ref',self.git('rev-parse','HEAD'),'--binding','binding.json','--scope','one'],
            capture_output=True,text=True)
        self.assertEqual(result.returncode,2)
        self.assertIn('BASE_REF_REQUIRED',result.stdout)
    def test_reader_record_must_name_the_actual_snapshot(self):
        self.seal('one',reader=True)
        r=self.receipts['intakes']['one']['reader_check']; r['input_snapshot']='0'*64
        self.put_json('intake.json',self.receipts); self.commit()
        self.assertIn('READER_INPUT_MISMATCH',self.check()['errors'])
    def test_branch_name_is_rejected_as_evidence_ref(self):
        with self.assertRaises(ValueError): self.mod.snapshot(self.repo,'HEAD','binding.json','one')

if __name__=='__main__': unittest.main()
