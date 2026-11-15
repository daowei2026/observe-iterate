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
