"""Focused checks for explicit DR14 source locations; no external service calls."""
import unittest
from pathlib import Path
import management_prompt as m

R = 'example/repo'
C = '1' * 40


def entry(repo=R):
    return {'source': {'repo': repo, 'commit': C, 'path': 'methods/run.md', 'selector': 'full'},
            'requirement': 'MODE_FULL', 'purpose': '构建和正常读取；不决定用例参数',
            'reuse_evidence': None}


class ReadsTests(unittest.TestCase):
    def test_explicit_locations_not_body(self):
        def read(repo, loc, repository):
            return 'DO NOT COPY WHOLE BODY', dict(loc, blob='2' * 40)
        body, refs = m.render_source_reads(Path('.'), [entry()],
            {'repo': R, 'commit': C, 'path': 'task.json'}, R, read)
        self.assertIn(R + '@' + C + ':methods/run.md::full', body)
        self.assertIn('构建和正常读取', body)
        self.assertNotIn('DO NOT COPY WHOLE BODY', body)
        self.assertEqual(len(refs), 1)

    def test_external_ref_not_falsely_read(self):
        def never(*args):
            raise AssertionError('must not read another checkout')
        body, refs = m.render_source_reads(Path('.'), [entry('other/repo')],
            {'repo': R, 'commit': C, 'path': 'task.json'}, R, never)
        self.assertIn('外仓', body)
        self.assertIsNone(refs[0]['blob'])

    def test_legacy_missing_is_visible(self):
        body, refs = m.render_source_reads(Path('.'), None, {}, R, None)
        self.assertIn('未展开', body)
        self.assertEqual(refs, [])

    def test_bad_ref_or_purpose(self):
        for change in ('commit', 'purpose'):
            e = entry()
            if change == 'commit':
                e['source']['commit'] = 'main'
            else:
                e['purpose'] = ''
            with self.assertRaises(ValueError):
                m.render_source_reads(Path('.'), [e],
                    {'repo': R, 'commit': C, 'path': 'task.json'}, R, lambda *a: ('', {}))


if __name__ == '__main__':
    unittest.main()
