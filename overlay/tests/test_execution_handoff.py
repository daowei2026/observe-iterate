"""The runner records facts; no test here claims market-semantic judgement."""
import unittest
import importlib.util
from pathlib import Path
import test_workmap_gate as base_tests

TOOL=Path(__file__).resolve().parents[1]/'tools'/'execution_handoff.py'
class ExecutionHandoffTests(unittest.TestCase):
    setUp=base_tests.WorkmapGateTests.setUp
    git=base_tests.WorkmapGateTests.git
    put=base_tests.WorkmapGateTests.put
    put_json=base_tests.WorkmapGateTests.put_json
    commit=base_tests.WorkmapGateTests.commit
    seal=base_tests.WorkmapGateTests.seal
    def helper(self):
        self.assertTrue(TOOL.is_file(),'exact task transmission and management triggers are not implemented')
        spec=importlib.util.spec_from_file_location('execution_handoff',TOOL)
        m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
    def test_prepare_preserves_task_text(self):
        m=self.helper();r=m.prepare(self.repo,self.git('rev-parse','HEAD'),'one/task.md',['rules.md'])
        self.assertEqual(r['task_text'],(self.repo/'one/task.md').read_text())
        self.assertEqual(r['method_inputs'][0]['blob'],self.git('rev-parse','HEAD:rules.md'))
        self.assertFalse(r['sent']);self.assertFalse(r['methods_read'])
    def test_prepare_does_not_treat_no_methods_as_ready(self):
        with self.assertRaises(ValueError):self.helper().prepare(self.repo,self.git('rev-parse','HEAD'),'one/task.md',[])
    def test_changed_payload_rejected(self):
        m=self.helper();r=m.prepare(self.repo,self.git('rev-parse','HEAD'),'one/task.md',['rules.md'])
        with self.assertRaises(ValueError):m.verify_payload(r,r['task_text']+'invented restriction')
    def test_no_new_commit_but_stall_calls_manager(self):
        m=self.helper();r=m.notice([{'id':'stall-1','kind':'NO_SUBSTANTIVE_PROGRESS','evidence':'actual runner log'}],[],[])
        self.assertTrue(r['management_required']);self.assertFalse(r['dispatched']);self.assertFalse(r['stop_unaffected_work'])
    def test_same_handled_or_inflight_event_not_redispatched(self):
        m=self.helper();ev=[{'id':'e1','kind':'REPEATED_FAILURE','evidence':'runner evidence'}]
        self.assertFalse(m.notice(ev,['e1'],[])['management_required'])
        self.assertFalse(m.notice(ev,[],['e1'])['management_required'])
    def test_owner_rule_change_is_not_dropped_without_business_change(self):
        m=self.helper();r=m.notice([{'id':'o1','kind':'OWNER_CHANGE','evidence':'owner prompt location'},
                                  {'id':'r2','kind':'METHOD_CHANGE','evidence':'actual diff'}],['r1'],[])
        self.assertEqual(len(r['events']),2)
    def test_empty_signal_cannot_create_manager_work(self):
        with self.assertRaises(ValueError):self.helper().notice([{'id':'x','kind':'REPEATED_FAILURE','evidence':''}],[],[])
    def test_normal_poll_does_not_create_professional_round(self):
        m=self.helper();r=m.notice([{'id':'ping','kind':'POLL','evidence':'routine heartbeat'}],[],[])
        self.assertFalse(r['management_required'])
    def test_primary_continue_does_not_drop_independent_reception(self):
        m=self.helper();actions=[
          {'action_id':'professional-next','kind':'PRIMARY_CONTINUE','recipient_ref':'professional-chat','evidence_ref':'git:professional'},
          {'action_id':'receiver-r47','kind':'INDEPENDENT_RECEPTION','recipient_ref':'receiver-chat','evidence_ref':'git:receiver'}]
        r=m.reconcile_actions(actions,[])
        self.assertEqual([x['action_id'] for x in r['to_send']],['professional-next','receiver-r47'])
    def test_inflight_receiver_is_collected_not_resent_while_professional_continues(self):
        m=self.helper();actions=[
          {'action_id':'professional-next','kind':'PRIMARY_CONTINUE','recipient_ref':'professional-chat','evidence_ref':'git:professional'},
          {'action_id':'receiver-r47','kind':'INDEPENDENT_RECEPTION','recipient_ref':'receiver-chat','evidence_ref':'git:receiver'}]
        r=m.reconcile_actions(actions,[{'action_id':'receiver-r47','state':'IN_FLIGHT'}])
        self.assertEqual([x['action_id'] for x in r['to_send']],['professional-next'])
        self.assertEqual([x['action_id'] for x in r['to_collect']],['receiver-r47'])
    def test_unknown_action_state_stays_visible_and_is_not_sent(self):
        m=self.helper();a=[{'action_id':'receiver','kind':'INDEPENDENT_RECEPTION','recipient_ref':'receiver-chat','evidence_ref':'git:r'}]
        r=m.reconcile_actions(a,[{'action_id':'receiver','state':'UNKNOWN'}])
        self.assertEqual(r['to_send'],[]);self.assertEqual(r['unknown'][0]['action_id'],'receiver')
