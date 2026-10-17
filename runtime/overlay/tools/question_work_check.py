"""Offline mechanical checks; no network, writes, dispatch or semantic decisions.
The caller must first validate documents with question_work.schema.json and resolve
refs in their original containing answer. Returned duties are proposals to check,
not proof that a role was invoked. See DR14 for authority and live-loop rules.
"""
from __future__ import annotations
import math
import re
from typing import Any, Callable

ACTIVE_WORK = 'ACTIVE'
REPEAT_ONCE = 'ONCE'
REPEAT_WHILE_ACTIVE = 'WHILE_WORK_ACTIVE'


def text_ref(value: Any) -> str | None:
    """Normalize explicit same-answer/Git locators; never guess other sources."""
    if value is None or isinstance(value, str):
        return value
    if isinstance(value, dict) and 'answer_ref' in value:
        return value['answer_ref']
    if isinstance(value, dict) and all(k in value for k in ('repo','commit','path','selector')):
        return f"github:{value['repo']}@{value['commit']}:{value['path']}::{value['selector']}"
    raise ValueError('Resolve message/attachment reference to its actual carrier first')


def binding_refs_equal(expected: dict, returned: dict, *,
                       resolver: Callable[[dict], dict] | None = None,
                       binding: dict | None = None) -> bool:
    """Compare original Git targets, retaining legacy already-resolved equality.

    A resolver must return the complete Binding plus its original blob/span
    (management_prompt.binding_target). Different source identities never alias.
    Without a resolver only the previous literal-equality path is available.
    """
    if expected == returned and resolver is None:
        return True
    keys = {"repo", "commit", "path", "selector"}
    if not all(isinstance(loc, dict) and set(loc) == keys
               and all(isinstance(loc[k], str) and loc[k] for k in keys)
               and re.fullmatch(r"[0-9a-f]{40}", loc["commit"])
               for loc in (expected, returned)):
        return False
    if any(expected[k] != returned[k] for k in ("repo", "commit", "path")):
        return False
    if resolver is None:
        return False
    try:
        left, right = resolver(expected), resolver(returned)
        return (left == right and isinstance(left, dict)
                and set(left) == {"binding", "blob", "start", "end"}
                and (binding is None or left["binding"] == binding))
    except (ValueError, TypeError, KeyError, UnicodeError, OSError):
        return False


def association_errors(binding: dict, returned: dict, role: dict,
                       binding_ref: dict, return_ref: str,
                       invocation_id: str, assignment_token: str, *,
                       binding_resolver: Callable[[dict], dict] | None = None) -> list[str]:
    """Check joins against the ACTUAL dispatch, not the newest repository plan.
    References passed here must be scoped to the same saved original answer.
    This function cannot decide that source text exists or was read/understood.
    """
    errors: list[str] = []
    if returned['work_id'] != binding['work_id'] or role['work_id'] != binding['work_id']:
        errors.append('WORK_MISMATCH')
    if returned['invocation_id'] != invocation_id or role['invocation_id'] != invocation_id:
        errors.append('INVOCATION_MISMATCH')
    if role['assignment_token'] != assignment_token:
        errors.append('TOKEN_MISMATCH')
    if not binding_refs_equal(binding_ref, returned['binding_ref'],
                              resolver=binding_resolver, binding=binding):
        errors.append('BINDING_MISMATCH')
    if role.get('question_work_ref') != return_ref:
        errors.append('RETURN_REFERENCE_MISMATCH')
    bootstrap = binding['kind'] == 'BOOTSTRAP'
    assigned = ['M-START'] if bootstrap else binding['question_ids']
    if any(x['question_id'] not in assigned for x in returned['focus_results']):
        errors.append('QUESTION_NOT_ASSIGNED')
    ids = [x['question_id'] for x in returned['focus_results']]
    if len(ids) != len(set(ids)):
        errors.append('DUPLICATE_FOCUS')
    if not bootstrap:
        custom = {x for x in assigned if x.startswith('CASE-')}
        defs = [x['question_id'] for x in binding.get('question_definitions', [])]
        if set(defs) != custom or len(defs) != len(set(defs)):
            errors.append('CASE_DEFINITION_MISMATCH')
    expected = [] if bootstrap else [x['trigger_id'] for x in binding['triggers']]
    observed = [x['trigger_id'] for x in returned['trigger_observations']]
    if len(expected) != len(set(expected)) or len(observed) != len(set(observed)):
        errors.append('DUPLICATE_TRIGGER')
    if set(expected) != set(observed):
        errors.append('TRIGGER_COVERAGE_MISMATCH')
    try:
        target = text_ref(returned['continuation_ref'])
        if text_ref(role['handoff']['instructions_ref']) != target:
            errors.append('CONTINUATION_MISMATCH')
        p = role.get('role_outputs', {}).get('professional')
        if p and role['handoff']['kind'] == 'CONTINUE' and text_ref(p['continuation_ref']) != target:
            errors.append('PROFESSIONAL_CONTINUATION_MISMATCH')
        if text_ref(returned['batch_remaining_ref']) != text_ref(role['remaining_scope_ref']):
            errors.append('REMAINING_MISMATCH')
    except ValueError:
        errors.append('UNRESOLVED_REFERENCE')
    return errors


def _repeat_index(base_cycle: str, cycle: str) -> int | None:
    if cycle == base_cycle:
        return 1
    match = re.fullmatch(re.escape(base_cycle) + r'/repeat-([2-9][0-9]*)', cycle)
    return int(match.group(1)) if match else None


def management_continuity_errors(binding: dict, ledger: list[dict], work_state: str,
                                 management_handoff_active: bool = False) -> list[str]:
    """Report a missing future effort review without inventing a budget or send.

    The caller supplies the observed whole-work state and any already-adopted
    management/handoff.  Old bindings remain one-shot unless they explicitly adopt
    WHILE_WORK_ACTIVE; historical records are never silently migrated.
    """
    if binding['kind'] == 'BOOTSTRAP' or work_state != ACTIVE_WORK or management_handoff_active:
        return []
    effort = [t for t in binding['triggers'] if t['kind'] == 'EFFORT']
    if any(t.get('repeat', REPEAT_ONCE) == REPEAT_WHILE_ACTIVE for t in effort):
        return []
    for trigger in effort:
        key = (binding['work_id'], trigger['obligation_id'], trigger['cycle_id'])
        rows = [row for row in ledger if tuple(row['key']) == key]
        if not rows or rows[0]['state'] not in ('RETURNED', 'CONSUMED', 'SUPERSEDED'):
            return []
    return ['CONTINUING_WORK_WITHOUT_FUTURE_REVIEW']


def pending_reviews(binding: dict, ledger: list[dict], observations: list[dict],
                    effort_values: dict[str, float], *, work_state: str = ACTIVE_WORK,
                    require_continuity: bool = False,
                    management_handoff_active: bool = False) -> dict:
    """Determine pending stable duties from supplied OBSERVED facts only.
    effort_values are deltas from each trigger's recorded count_from_ref; missing
    counters stay unknown. Call from an existing loop even when no answer arrives.
    Does not send, persist, rearm, set CONSUMED, or count 'effective' work itself.
    """
    out: dict[str, Any] = {'due': [], 'unknown': [], 'errors': [], 'continuity_errors': []}
    if binding['kind'] == 'BOOTSTRAP':
        return out
    if work_state not in {'ACTIVE', 'PAUSED', 'HANDED_OFF', 'COMPLETE'}:
        out['errors'].append('WORK_STATE_REQUIRED'); return out
    if require_continuity:
        out['continuity_errors'] = management_continuity_errors(
            binding, ledger, work_state, management_handoff_active)
    signals = {x['trigger_id']: x for x in observations}
    if len(signals) != len(observations):
        out['errors'].append('DUPLICATE_OBSERVATION'); return out
    groups: dict[tuple, dict] = {}
    for t in binding['triggers']:
        repeat = t.get('repeat', REPEAT_ONCE)
        if repeat not in {REPEAT_ONCE, REPEAT_WHILE_ACTIVE}:
            out['errors'].append('UNKNOWN_REPEAT_POLICY'); continue
        if repeat == REPEAT_WHILE_ACTIVE and t['kind'] != 'EFFORT':
            out['errors'].append('REPEAT_ONLY_ALLOWED_FOR_EFFORT'); continue
        base_key = (binding['work_id'], t['obligation_id'], t['cycle_id'])
        key = base_key
        interval_index = 1
        if repeat == REPEAT_WHILE_ACTIVE:
            if work_state != ACTIVE_WORK:
                continue
            series = []
            for row in ledger:
                row_key = tuple(row['key'])
                if len(row_key) != 3 or row_key[:2] != base_key[:2]:
                    continue
                index = _repeat_index(t['cycle_id'], str(row_key[2]))
                if index is not None:
                    series.append((index, row))
            indexes = [index for index, _ in series]
            if len(indexes) != len(set(indexes)):
                out['errors'].append('DUPLICATE_LEDGER_KEY'); continue
            if any(row['state'] in ('IN_FLIGHT', 'RETURNED') for _, row in series):
                continue
            if any(row['state'] == 'SUPERSEDED' for _, row in series):
                continue
            consumed = sorted(index for index, row in series if row['state'] == 'CONSUMED')
            if consumed and consumed != list(range(1, max(consumed) + 1)):
                out['errors'].append('REPEAT_LEDGER_GAP'); continue
            pending = sorted(index for index, row in series if row['state'] == 'PENDING')
            interval_index = pending[-1] if pending else (max(consumed, default=0) + 1)
            cycle = t['cycle_id'] if interval_index == 1 else t['cycle_id'] + '/repeat-' + str(interval_index)
            key = (binding['work_id'], t['obligation_id'], cycle)
        rows = [x for x in ledger if tuple(x['key']) == key]
        if len(rows) > 1:
            out['errors'].append('DUPLICATE_LEDGER_KEY'); continue
        if rows and rows[0]['state'] in ('IN_FLIGHT','RETURNED','CONSUMED','SUPERSEDED'):
            continue
        older = []
        for row in ledger:
            row_key = tuple(row['key'])
            if len(row_key) == 3 and row_key[:2] == base_key[:2] \
                    and _repeat_index(t['cycle_id'], str(row_key[2])) is None:
                older.append(row)
        if older and t['rearm_ref'] is None:
            out['errors'].append('REARM_REFERENCE_MISSING'); continue
        if t['kind'] == 'EFFORT':
            value = effort_values.get(t['trigger_id'])
            if isinstance(value, bool) or not isinstance(value, (int,float)) or not math.isfinite(value) or value < 0:
                out['unknown'].append(t['trigger_id']); continue
            satisfied = value >= t['effort_limit']['limit'] * interval_index
        else:
            ob = signals.get(t['trigger_id'])
            if not ob or ob['state'] == 'UNKNOWN':
                out['unknown'].append(t['trigger_id']); continue
            satisfied = ob['state'] == 'SATISFIED'
            if satisfied and ob.get('evidence_ref') is None:
                out['errors'].append('SATISFIED_WITHOUT_EVIDENCE'); continue
        if not satisfied:
            continue
        if key in groups and (groups[key]['route'] != t['route'] or groups[key]['blocking'] != t['blocking']):
            out['errors'].append('DUTY_ROUTE_CONFLICT'); continue
        group = groups.setdefault(key, {'key':list(key), 'route':t['route'],
                                       'blocking':t['blocking'], 'trigger_ids':[],
                                       'repeat_interval_index':interval_index})
        group['trigger_ids'].append(t['trigger_id'])
    # Invalid input requires repair; do not partially present these as dispatch-ready.
    if not out['errors']:
        out['due'] = list(groups.values())
    return out
