"""Offline identity checks only."""
def association_errors(binding,returned,role_return):
    e=[]
    if returned.get('work_id')!=binding.get('work_id'): e.append('WORK_ID_MISMATCH')
    if role_return.get('work_id')!=binding.get('work_id'): e.append('ROLE_WORK_ID_MISMATCH')
    if returned.get('invocation_id')!=role_return.get('invocation_id'): e.append('INVOCATION_MISMATCH')
    return e
