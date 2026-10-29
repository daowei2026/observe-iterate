"""Scope-aware readback and exact dispatch regressions. Real temporary Git objects."""
import test_workmap_gate as base_tests
import unittest
import hashlib


class V2RegressionTests(unittest.TestCase):
    setUp = base_tests.WorkmapGateTests.setUp
    git = base_tests.WorkmapGateTests.git
    put = base_tests.WorkmapGateTests.put
    put_json = base_tests.WorkmapGateTests.put_json
    commit = base_tests.WorkmapGateTests.commit
    seal = base_tests.WorkmapGateTests.seal
    check = base_tests.WorkmapGateTests.check
    delivery = base_tests.WorkmapGateTests.delivery
    def enable_v2(self):
        self.binding['schema'] = 'workmap-binding/v2'
        self.binding['overview']['anchors'] = ['intent', 'one', 'two']
        self.binding['shared_overview_anchors'] = ['intent']
        self.binding['streams']['one']['overview_anchors'] = ['one']
        self.binding['streams']['two']['overview_anchors'] = ['two']
        self.binding['streams']['one']['watch_roots'].append('one/reviews')
        self.binding['streams']['one']['reader_output_roots'] = ['one/reviews/readers']
        self.put('README.md', '# Whole project\n<a id="intent"></a>\nShared purpose.\n<a id="one"></a>\nFirst work line.\n<a id="two"></a>\nSecond work line.\n')
        self.put('one/reviews/review.md', 'Substantive review must still be observed.\n')
        self.put_json('binding.json', self.binding)
        self.commit()
        self.assertTrue(self.mod.snapshot(self.repo, self.git('rev-parse','HEAD'), 'binding.json', 'one').get('reader_fingerprint'),
                        'readback input must be separate from result/report publication')

    def seal_v2(self, reader=True):
        self.seal('one', reader=False)
        entry = self.receipts['intakes']['one']
        ref = self.git('rev-parse', 'HEAD')
        snap = self.mod.snapshot(self.repo, ref, 'binding.json', 'one')
        entry['dispatch'].update(kind='ROUTINE_RESULT', requires_reader_check=False,
                                 reader_reason='Same understood business map; routine task progress.',
                                 method_paths=['rules.md'])
        if reader:
            entry['reader_check'] = {'status':'RECORDED', 'context':'independent-reader',
                'independent_of_map_builder':True, 'input_commit':ref,
                'input_snapshot':snap['reader_fingerprint'],
                'report':{'path':'reader.md','blob':self.git('rev-parse', ref+':reader.md')}}
        self.put_json('intake.json', self.receipts)
        self.commit()

    def delivery_v2(self, state='NOT_SENT'):
        d=self.delivery(state)
        d['task_payload_sha256']=hashlib.sha256((self.repo/'one/task.md').read_bytes()).hexdigest()
        return d

    def test_first_adoption_base_has_template_but_no_prior_map_task_or_intake(self):
        self.enable_v2()
        complete = self.git('rev-parse', 'HEAD')
        paths = ['one/map.md', 'one/task.md', 'intake.json']
        self.git('rm', '--', *paths)
        first_base = self.commit()
        for path in paths:
            self.assertFalse(self.mod.GitView(self.repo, first_base).exists(path))
        self.assertTrue(self.mod.GitView(self.repo, first_base).exists('binding.json'))
        self.git('checkout', complete, '--', *paths)
        self.commit()
        self.seal_v2()
        # These are synthetic reports in a temporary repository, never actual
        # independent-reader evidence for BI-01 or a production intake.
        self.receipts['intakes']['one']['dispatch'].update(
            kind='NEW_STAGE', requires_reader_check=True)
        self.put_json('intake.json', self.receipts)
        self.commit()
        result = self.check(base_ref=first_base, dispatch=True, delivery=self.delivery_v2())
        self.assertTrue(result['ok'], result)
        self.assertEqual(result['reader_qualification'], 'RECORDED')

    def test_v2_reader_report_does_not_invalidate_its_inputs(self):
        self.enable_v2(); self.seal_v2()
        before=self.mod.snapshot(self.repo,self.git('rev-parse','HEAD'),'binding.json','one')
        self.put('one/reviews/readers/independent.md','New readback report only.\n'); self.commit()
        after=self.mod.snapshot(self.repo,self.git('rev-parse','HEAD'),'binding.json','one')
        self.assertEqual(before['fingerprint'],after['fingerprint'])
        self.assertEqual(before['reader_fingerprint'],after['reader_fingerprint'])
        self.assertTrue(self.check()['ok'])

    def test_v2_other_overview_progress_is_not_our_new_task(self):
        self.enable_v2(); self.seal_v2()
        text=(self.repo/'README.md').read_text().replace('Second work line.','Second work line completed another result.')
        self.put('README.md',text); self.commit()
        self.assertTrue(self.check()['ok'])
        text=text.replace('Shared purpose.','Owner changed shared purpose.')
        self.put('README.md',text); self.commit()
        self.assertIn('INTAKE_STALE',self.check()['errors'])

    def test_v2_substantive_review_still_requires_intake_not_another_reader(self):
        self.enable_v2(); self.seal_v2()
        old_reader=self.receipts['intakes']['one']['reader_check'].copy()
        self.put('one/reviews/review.md','New business finding.\n'); self.commit()
        self.assertIn('INTAKE_STALE',self.check()['errors'])
        self.seal_v2(reader=False)
        self.receipts['intakes']['one']['reader_check']=old_reader
        self.put_json('intake.json',self.receipts); self.commit()
        self.assertTrue(self.check()['ok'])

    def test_v2_new_stage_cannot_skip_reader(self):
        self.enable_v2(); self.seal_v2(reader=False)
        self.receipts['intakes']['one']['dispatch']['kind']='NEW_STAGE'
        self.put_json('intake.json',self.receipts); self.commit()
        self.assertIn('READER_CHECK_REQUIRED',self.check(dispatch=True,delivery=self.delivery_v2())['errors'])

    def test_v2_changed_map_does_not_forge_fresh_reader(self):
        self.enable_v2(); self.seal_v2()
        old_reader=self.receipts['intakes']['one']['reader_check'].copy()
        self.put('one/map.md',(self.repo/'one/map.md').read_text()+'\nMinor progress update.\n'); self.commit()
        self.seal_v2(reader=False)
        self.receipts['intakes']['one']['reader_check']=old_reader
        self.put_json('intake.json',self.receipts); self.commit()
        r=self.check(dispatch=True,delivery=self.delivery_v2())
        self.assertTrue(r['ok'],r['errors'])
        self.assertEqual(r['reader_qualification'],'RECORDED_OLD_INPUT')
        self.receipts['intakes']['one']['dispatch']['kind']='MAJOR_MAP_RESHAPE'
        self.put_json('intake.json',self.receipts); self.commit()
        self.assertIn('READER_CHECK_REQUIRED',self.check(dispatch=True,delivery=self.delivery_v2())['errors'])

    def test_v2_rewritten_payload_or_missing_methods_cannot_dispatch(self):
        self.enable_v2(); self.seal_v2()
        d=self.delivery_v2(); d['task_payload_sha256']='0'*64
        self.assertIn('TASK_PAYLOAD_CHANGED',self.check(dispatch=True,delivery=d)['errors'])
        self.receipts['intakes']['one']['dispatch']['method_paths']=[]
        self.put_json('intake.json',self.receipts); self.commit()
        self.assertIn('PROFESSIONAL_METHOD_INPUT_REQUIRED',self.check(dispatch=True,delivery=self.delivery_v2())['errors'])


    def worker_fixture(self, role='professional'):
        self.enable_v2(); self.seal_v2()
        base=self.git('rev-parse','HEAD')
        order_id='SYNTHETIC-W05'
        round_id='R0004'
        who='chatgpt:synthetic:'+role
        invocation_id='BI01-FO01-R0004-SYNTHETIC'
        token='synthetic-assignment-token'
        prefix='one/artifacts/professional-' if role=='professional' else 'one/reviews/management-'
        order=prefix+round_id+'/WORKER_ORDER.md'
        report='one/artifacts/worker-'+order_id+'/FULL_RESPONSE.md'
        self.put(order,('\n'.join([
            '# Synthetic issued Worker order', 'work_id: BI-01',
            'run_id: ONE-01', 'order_id: '+order_id,
            'issuer_role: '+role, 'issuer_ref: '+who,
            'issuer_invocation_id: '+invocation_id,
            'issuer_assignment_token: '+token, 'return_to: '+who,
            ''])))
        self.put(report,('\n'.join([
            '# Synthetic Worker result', 'order_id: '+order_id,
            'work_id: BI-01；run_id: ONE-01',
            'issuer_invocation_id: '+invocation_id,
            'return_to: '+who, 'Actual bounded technical findings.', ''])))
        origin='one/provenance/turns/'+round_id+'/'
        self.put_json(origin+'INVOCATION.json', {
            'role':role,'recipient_ref':who,'invocation_id':invocation_id,
            'assignment_token':token,'work_id':'BI-01','run_id':'ONE-01'})
        self.put_json(origin+'SEND_RECEIPT.json', {
            'state':'COMMITTED','recipient_ref':who,'invocation_id':invocation_id,
            'assignment_token':token})
        self.commit()
        return base,order,report,who

    def order_check(self, order):
        return self.mod.worker_order(self.repo,self.git('rev-parse','HEAD'),
                                     'binding.json','one',order_path=order)

    def test_worker_order_preflight_before_worker_report_or_intake(self):
        base,order,report,who=self.worker_fixture()
        self.git('rm','--',report,'intake.json')
        self.commit()
        outcome=self.order_check(order)
        self.assertTrue(outcome['ok'],outcome['errors'])
        self.assertEqual(outcome['recipient'],who)
        self.assertEqual(outcome['expected_worker_report_path'],report)
        self.assertFalse(self.mod.GitView(self.repo,self.git('rev-parse','HEAD')).exists(report))
        self.assertFalse(self.mod.GitView(self.repo,self.git('rev-parse','HEAD')).exists('intake.json'))

    def test_worker_order_cli_checks_committed_order_without_report_or_base(self):
        base,order,report,who=self.worker_fixture()
        self.git('rm','--',report,'intake.json')
        self.commit()
        result=base_tests.subprocess.run(
            [base_tests.sys.executable,str(base_tests.TOOL),'worker-order',
             '--repo',str(self.repo),'--ref',self.git('rev-parse','HEAD'),
             '--binding','binding.json','--scope','one','--order',order],
            check=False,text=True,capture_output=True)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        body=base_tests.json.loads(result.stdout)
        self.assertTrue(body['ok'],body)
        self.assertEqual(body['recipient'],who)


    def test_worker_order_preflight_accepts_management_before_intake(self):
        base,order,report,who=self.worker_fixture(role='management')
        self.git('rm','--',report,'intake.json')
        self.commit()
        outcome=self.order_check(order)
        self.assertTrue(outcome['ok'],outcome['errors'])
        self.assertEqual(outcome['recipient'],who)

    def test_worker_order_preflight_catches_original_w02_field_and_path_shape(self):
        base,order,report,who=self.worker_fixture()
        legacy='one/artifacts/batch-01/aidata/W02_WORK_ORDER.md'
        (self.repo/legacy).parent.mkdir(parents=True,exist_ok=True)
        self.git('mv',order,legacy)
        body=(self.repo/legacy).read_text(encoding='utf-8')
        body=body.replace('order_id: SYNTHETIC-W05','work_order_id: SYNTHETIC-W05')
        body=body.replace('issuer_role: professional\nissuer_ref: '+who,
                          'issued_by: '+who)
        self.put(legacy,body)
        self.commit()
        outcome=self.order_check(legacy)
        self.assertFalse(outcome['ok'])
        self.assertIn('WORKER_ORDER_AUTHORITY_INVALID',outcome['errors'])
        self.assertIn('ISSUER_CALL_NOT_VERIFIED',outcome['errors'])
        # The same historical-shaped order must not be accepted as a Worker result.
        result=self.worker_check(base,legacy,report)
        self.assertIn('WORKER_ORDER_AUTHORITY_INVALID',result['errors'])

    def test_worker_order_authority_rejection_is_shared_with_worker_result(self):
        base,order,report,who=self.worker_fixture()
        self.put(order,(self.repo/order).read_text(encoding='utf-8').replace(
            'issuer_assignment_token: synthetic-assignment-token',
            'issuer_assignment_token: wrong-token'))
        self.commit()
        self.assertIn('ISSUER_CALL_NOT_VERIFIED',self.order_check(order)['errors'])
        self.assertIn('ISSUER_CALL_NOT_VERIFIED',self.worker_check(base,order,report)['errors'])

    def test_worker_order_not_sent_rejected_without_worker_report(self):
        base,order,report,who=self.worker_fixture()
        self.git('rm','--',report)
        self.put_json('one/provenance/turns/R0004/SEND_RECEIPT.json',{'state':'NOT_SENT'})
        self.commit()
        outcome=self.order_check(order)
        self.assertIn('ISSUER_CALL_NOT_VERIFIED',outcome['errors'])


    def worker_check(self, base, order, report):
        return self.mod.worker_result(self.repo,self.git('rev-parse','HEAD'),
                                      'binding.json','one',base_ref=base,
                                      order_path=order,report_path=report)

    def test_worker_result_returns_to_issuing_professional_without_intake(self):
        base,order,report,who=self.worker_fixture()
        self.assertIn('INTAKE_STALE',self.check()['errors'])
        outcome=self.worker_check(base,order,report)
        self.assertTrue(outcome['ok'],outcome['errors'])
        self.assertEqual(outcome['recipient'],who)
        self.assertFalse(outcome['full_intake_current'])
        self.assertIn('INTAKE_STALE',self.check(dispatch=True,delivery=self.delivery_v2())['errors'])

    def test_manager_issued_worker_result_returns_to_manager(self):
        base,order,report,who=self.worker_fixture(role='management')
        outcome=self.worker_check(base,order,report)
        self.assertTrue(outcome['ok'],outcome['errors'])
        self.assertEqual(outcome['recipient'],who)

    def test_worker_failure_is_still_returned_to_issuing_professional(self):
        base,order,report,who=self.worker_fixture()
        self.put(report,(self.repo/report).read_text()+'\nHTTP 500; platform incomplete.\n')
        self.commit()
        outcome=self.worker_check(base,order,report)
        self.assertTrue(outcome['ok'],outcome['errors'])
        self.assertEqual(outcome['recipient'],who)

    def test_worker_result_wrong_order_or_recipient_fails(self):
        base,order,report,_=self.worker_fixture()
        self.put(report,(self.repo/report).read_text().replace(
            'return_to: chatgpt:synthetic:professional',
            'return_to: chatgpt:synthetic:management'))
        self.commit()
        self.assertIn('WORKER_RESULT_IDENTITY_MISMATCH:return_to',
                      self.worker_check(base,order,report)['errors'])

    def test_worker_return_does_not_bypass_owner_method_or_map_change(self):
        base,order,report,_=self.worker_fixture()
        for changed in ('owner.md','rules.md','one/map.md'):
            with self.subTest(changed=changed):
                previous=(self.repo/changed).read_text()
                self.put(changed,previous+'\nNew condition.\n')
                self.commit()
                self.assertIn('PROTECTED_INPUT_CHANGED',
                              self.worker_check(base,order,report)['errors'])
                self.put(changed,previous)
                self.commit()

    def test_worker_return_requires_actual_sent_issuer_and_same_intake(self):
        base,order,report,_=self.worker_fixture()
        origin='one/provenance/turns/R0004/SEND_RECEIPT.json'
        self.put_json(origin,{'state':'NOT_SENT'})
        self.commit()
        self.assertIn('ISSUER_CALL_NOT_VERIFIED',
                      self.worker_check(base,order,report)['errors'])
        self.receipts['intakes']['one']['effort']['known_pro_turns']=3
        self.put_json('intake.json',self.receipts)
        self.commit()
        self.assertIn('MANAGEMENT_INTAKE_CHANGED',
                      self.worker_check(base,order,report)['errors'])

    def test_v2_exclusion_cannot_hide_whole_business_root(self):
        self.enable_v2()
        self.binding['streams']['one']['reader_output_roots']=['one/artifacts']
        self.put_json('binding.json',self.binding); self.commit()
        with self.assertRaises(ValueError):
            self.mod.snapshot(self.repo,self.git('rev-parse','HEAD'),'binding.json','one')

    def test_v2_unassigned_shared_text_fails_instead_of_disappearing(self):
        self.enable_v2()
        self.put('README.md',(self.repo/'README.md').read_text()+'<a id="new-rule"></a>\nA new common requirement.\n'); self.commit()
        with self.assertRaises(ValueError):
            self.mod.snapshot(self.repo,self.git('rev-parse','HEAD'),'binding.json','one')
