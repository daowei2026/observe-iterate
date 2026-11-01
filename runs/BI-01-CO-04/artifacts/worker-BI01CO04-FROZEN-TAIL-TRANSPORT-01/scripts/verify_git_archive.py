"""对准确Git提交归档做独立消费验收；可在push后核对远端包含该提交。"""
import argparse
import io
import json
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]
REPO = OUT.parents[3]
REL = str(OUT.relative_to(REPO))
BRANCH = 'fy/feature-based-case-observation'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=REPO).decode().strip()


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--base-commit', required=True)
    p.add_argument('--check-remote', action='store_true')
    a = p.parse_args()
    assert git('branch', '--show-current') == BRANCH
    assert git('remote', 'get-url', 'origin') == 'https://github.com/daowei2026/observe-iterate.git'
    assert not git('status', '--porcelain')
    head = git('rev-parse', 'HEAD')
    changes = git('diff', '--name-only', a.base_commit, head).splitlines()
    assert changes and all(x.startswith(REL + '/') for x in changes)
    old = ['runs/BI-01-CO-04/artifacts/' + s for s in ['worker-BI01CO04-INPUT-RECOVERY-01', 'worker-BI01CO04-ASOF-VISIBILITY-REPLAY-01', 'R0009']]
    assert not git('diff', '--name-only', '43223e4a84cbf32c25745ce6b1cbce43c82488ed', head, '--', *old)
    with tempfile.TemporaryDirectory(prefix='git-consumer-', dir=OUT / '.runtime') as tmp:
        archive = subprocess.check_output(['git', 'archive', head, '--', REL], cwd=REPO)
        with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
            tar.extractall(tmp, filter='data')
        package = Path(tmp) / REL
        result = subprocess.run([sys.executable, '-B', str(package / 'scripts/validate_tail.py')],
                                cwd=tmp, capture_output=True, text=True, timeout=60)
        (OUT / '.runtime/git-archive-validator.stdout').write_text(result.stdout)
        (OUT / '.runtime/git-archive-validator.stderr').write_text(result.stderr)
        assert result.returncode == 0, result.stderr[:3000]
        validation = json.loads(result.stdout)
        assert validation['status'] == 'PASS'
        result = subprocess.run(['sha256sum', '-c', 'SHA256SUMS'], cwd=package,
                                capture_output=True, text=True, timeout=60)
        (OUT / '.runtime/git-archive-sha256sum.stdout').write_text(result.stdout)
        (OUT / '.runtime/git-archive-sha256sum.stderr').write_text(result.stderr)
        assert result.returncode == 0, result.stderr[:3000]
        seal_entries = len(result.stdout.splitlines())
    remote = None
    if a.check_remote:
        remote = git('ls-remote', '--heads', 'origin', BRANCH).split()[0]
        if remote != head:
            subprocess.run(['git', 'fetch', 'origin', BRANCH], cwd=REPO, check=True)
            subprocess.run(['git', 'merge-base', '--is-ancestor', head, remote], cwd=REPO, check=True)
    proof = {'final_commit': head, 'remote_head': remote,
             'remote_contains_final_commit': True if a.check_remote else None,
             'only_new_order_output_modified': True, 'old_packages_and_R0009_unchanged': True,
             'clean_worktree': True, 'git_archive_offline_validator': validation,
             'external_sha256sum_entries': seal_entries, 'tracked_files': len(changes),
             'qualification': 'TAIL_PACKAGE_READY'}
    (OUT / '.runtime/PUBLISH_VERIFICATION.json').write_text(json.dumps(proof, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(proof, ensure_ascii=False))


if __name__ == '__main__':
    main()
