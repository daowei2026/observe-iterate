#!/usr/bin/env python3
"""Scoped management intake and dispatch preflight, using immutable local Git objects.

This tool never judges market semantics, writes a business artifact, creates a chat,
asserts a remote push, or silently updates an intake. Its positive result is only
mechanical consistency under the supplied binding and trusted execution records.
Use the documented manager/runner adapter; an optional CLI cannot prevent bypass.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

HEX = re.compile(r'^[0-9a-f]{40}$')
LINK = re.compile(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)')
ANCHOR = re.compile(r'<a\s+id=["\']([^"\']+)["\']\s*>',re.I)
MAX_TEXT_BYTES = 10_000_000


def canonical_hash(value: object) -> str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False,
                                     separators=(',',':')).encode('utf-8')).hexdigest()


def safe_path(path: str) -> str:
    if not isinstance(path,str) or not path or '\x00' in path or '\\' in path:
        raise ValueError('invalid repository-relative path')
    p=PurePosixPath(path)
    if p.is_absolute() or '..' in p.parts or path.startswith('-'):
        raise ValueError('unsafe repository-relative path: '+path)
    return p.as_posix()


class GitView:
    def __init__(self, repo: Path | str, ref: str):
        self.repo=Path(repo).resolve()
        if not HEX.fullmatch(ref):
            raise ValueError('an exact 40-character commit SHA is required, not a branch or HEAD')
        self.ref=ref
        self._oids={}
        self._texts={}
        if self.run('cat-file','-t',ref).strip()!=b'commit':
            raise ValueError('ref is not an available commit')

    def run(self,*args: str) -> bytes:
        try:
            return subprocess.check_output(['git','-C',str(self.repo),*args],
                                           stderr=subprocess.PIPE,timeout=30)
        except (subprocess.CalledProcessError,subprocess.TimeoutExpired) as e:
            raise ValueError('Git object read failed: '+' '.join(args[:2])) from e

    def oid(self,path: str) -> str:
        path=safe_path(path)
        if path not in self._oids:
            self._oids[path]=self.run('rev-parse','--verify',self.ref+':'+path).decode().strip()
        return self._oids[path]

    def exists(self,path: str) -> bool:
        try: self.oid(path); return True
        except ValueError: return False

    def text(self,path: str) -> str:
        if path in self._texts: return self._texts[path]
        oid=self.oid(path)
        if self.run('cat-file','-t',oid).strip()!=b'blob':
            raise ValueError('expected a file: '+path)
        size=int(self.run('cat-file','-s',oid))
        if not 0 < size <= MAX_TEXT_BYTES:
            raise ValueError('empty or oversized text: '+path)
        try:
            self._texts[path]=self.run('cat-file','blob',oid).decode('utf-8')
            return self._texts[path]
        except UnicodeDecodeError as e: raise ValueError('not UTF-8 text: '+path) from e

    def obj(self,path: str) -> dict:
        try: value=json.loads(self.text(path))
        except json.JSONDecodeError as e: raise ValueError('invalid JSON: '+path) from e
        if not isinstance(value,dict): raise ValueError('JSON object required: '+path)
        return value


def binding_for(view: GitView, path: str, scope: str) -> tuple[dict,dict]:
    b=view.obj(path)
    if b.get('schema') not in ('workmap-binding/v1','workmap-binding/v2'):
        raise ValueError('unsupported binding schema')
    if not isinstance(b.get('streams'),dict) or scope not in b['streams']:
        raise ValueError('unknown work stream: '+scope)
    s=b['streams'][scope]
    for d in [b['overview'],s['map']]:
        safe_path(d['path'])
        if not isinstance(d.get('anchors'),list) or not d['anchors']:
            raise ValueError('each readable map needs its existing protected section anchors')
    for p in [s['task'],b['receipt_path'],*b['owner_sources'],*b['rule_paths'],*s['watch_roots']]: safe_path(p)
    if not b['owner_sources'] or not b['rule_paths'] or not s['watch_roots']:
        raise ValueError('owner, method and actual-result watch inputs may not be empty')
    if any(b['receipt_path']==r or b['receipt_path'].startswith(r.rstrip('/')+'/') for r in s['watch_roots']):
        raise ValueError('intake cannot watch itself or a containing directory')
    return b,s


def overview_projection(v: GitView, b: dict, s: dict) -> dict:
    """Keep all common material; only explicitly allocated sibling progress is omitted."""
    text=v.text(b['overview']['path'])
    matches=list(ANCHOR.finditer(text))
    names=[m.group(1) for m in matches]
    if len(names)!=len(set(names)): raise ValueError('duplicate overview anchor')
    shared=b.get('shared_overview_anchors',[])
    own=s.get('overview_anchors',[])
    assigned=set(shared)
    for stream in b['streams'].values(): assigned.update(stream.get('overview_anchors',[]))
    if set(names)!=assigned or not shared or not own:
        raise ValueError('all overview anchors must be allocated; shared and scope sections are required')
    selected=set(shared)|set(own)
    chunks={'__preamble__':text[:matches[0].start()] if matches else text}
    for i,m in enumerate(matches):
        if m.group(1) in selected:
            chunks[m.group(1)]=text[m.start():matches[i+1].start() if i+1<len(matches) else len(text)]
    return {name:hashlib.sha256(value.encode('utf-8')).hexdigest() for name,value in chunks.items()}


def result_projection(v: GitView, b: dict, s: dict) -> dict:
    """Exclude only declared dedicated reader-output subdirectories, never whole roots."""
    roots=s['watch_roots']; excluded=s.get('reader_output_roots',[])
    protected=[b['overview']['path'],s['map']['path'],s['task'],*b['owner_sources'],*b['rule_paths']]
    for x in excluded:
        safe_path(x)
        if x in roots or not any(x.startswith(r.rstrip('/')+'/') for r in roots):
            raise ValueError('reader output exclusion must be a strict subdirectory of a watch root')
        if any(p==x or p.startswith(x.rstrip('/')+'/') for p in protected):
            raise ValueError('reader output exclusion overlaps an authoritative input')
    watched={}
    for root in roots:
        if not v.exists(root): watched[root]=None; continue
        records=v.run('ls-tree','-r','-z',v.ref,'--',root).split(b'\0')
        files={}
        for record in records:
            if not record: continue
            meta,raw_path=record.split(b'\t',1)
            path=raw_path.decode('utf-8')
            if any(path==x or path.startswith(x.rstrip('/')+'/') for x in excluded): continue
            files[path]=meta.decode('ascii')
        watched[root]=canonical_hash(files)
    return watched


def snapshot(repo: Path | str, ref: str, binding_path: str, scope: str) -> dict:
    v=GitView(repo,ref); b,s=binding_for(v,binding_path,scope)
    if b['schema']=='workmap-binding/v1':
        watched={p:v.oid(p) if v.exists(p) else None for p in s['watch_roots']}
        material={
            'schema':'workmap-snapshot/v1','scope':scope,'binding':v.oid(binding_path),
            'documents':{d['path']:v.oid(d['path']) for d in [b['overview'],s['map']]},
            'task':{s['task']:v.oid(s['task'])},
            'owner_sources':{p:v.oid(p) for p in b['owner_sources']},
            'rules':{p:v.oid(p) for p in b['rule_paths']},'result_trees':watched,
        }
        return {'observed_commit':ref,'scope':scope,'material':material,'fingerprint':canonical_hash(material)}
    # v2 is opt-in: v1 receipts are never silently promoted or reinterpreted.
    reader_material={
        'schema':'workmap-reader-input/v2','scope':scope,
        'overview':{b['overview']['path']:overview_projection(v,b,s)},
        'map':{s['map']['path']:v.oid(s['map']['path'])},
        'task':{s['task']:v.oid(s['task'])},
        'owner_sources':{p:v.oid(p) for p in b['owner_sources']},
        'rules':{p:v.oid(p) for p in b['rule_paths']},
    }
    scoped_binding={'manager_role':b['manager_role'],'receipt_path':b['receipt_path'],
                    'overview':b['overview'],'shared_overview_anchors':b['shared_overview_anchors'],
                    'stream':s,'owner_sources':b['owner_sources'],'rule_paths':b['rule_paths']}
    material={'schema':'workmap-snapshot/v2','scope':scope,'binding':canonical_hash(scoped_binding),
              'reader_input':reader_material,'result_trees':result_projection(v,b,s)}
    return {'observed_commit':ref,'observed_binding_blob':v.oid(binding_path),'scope':scope,
            'material':material,'fingerprint':canonical_hash(material),
            'reader_fingerprint':canonical_hash(reader_material),
            'task_payload_sha256':hashlib.sha256(v.text(s['task']).encode('utf-8')).hexdigest()}


def resolve_relative(source: str,target: str) -> str:
    parts=list(PurePosixPath(source).parent.parts)
    for p in PurePosixPath(unquote(target)).parts:
        if p=='.': continue
        if p=='..':
            if not parts: raise ValueError('link escapes repository')
            parts.pop()
        else: parts.append(p)
    return safe_path('/'.join(parts))


def inspect_documents(v: GitView,documents: list[dict]) -> tuple[list[str],list[str]]:
    errors=[]; external=[]
    for doc in documents:
        p=doc['path']
        try: text=v.text(p)
        except ValueError: errors.append('MAP_UNREADABLE:'+p); continue
        found=set(ANCHOR.findall(text))
        for anchor in doc['anchors']:
            if anchor not in found: errors.append('MAP_ANCHOR_MISSING:'+p+'#'+anchor)
        for raw in LINK.findall(text):
            u=urlsplit(raw.strip('<>'))
            if u.scheme in ('http','https'):
                if u.netloc=='github.com':
                    x=unquote(u.path).strip('/').split('/')
                    if len(x)>3 and x[2] in ('blob','tree','commit') and not HEX.fullmatch(x[3]):
                        errors.append('MOVING_GITHUB_EVIDENCE:'+raw)
                external.append(raw); continue
            if u.scheme:
                errors.append('UNSUPPORTED_LINK_SCHEME:'+u.scheme); continue
            try:
                resolved=p if not u.path else resolve_relative(p,u.path)
                if not v.exists(resolved): errors.append('LINK_MISSING:'+resolved); continue
                # Stable explicit anchors in maintained documents are mechanically checkable.
                # Other source-document heading semantics remain a source/readback obligation.
                if u.fragment and resolved in {d['path'] for d in documents}:
                    if unquote(u.fragment) not in set(ANCHOR.findall(v.text(resolved))):
                        errors.append('LINK_ANCHOR_MISSING:'+resolved+'#'+unquote(u.fragment))
            except ValueError: errors.append('UNSAFE_LINK:'+p+':'+raw)
    return errors,sorted(set(external))


def valid_report(v: GitView, report: object) -> bool:
    if not isinstance(report,dict) or not report.get('path') or not report.get('blob'): return False
    try: return v.oid(report['path'])==report['blob'] and bool(v.text(report['path']).strip())
    except ValueError: return False


def check(repo: Path | str, ref: str, binding_path: str, scope: str, *,
          base_ref: str | None=None, actor: str='management_review', dispatch: bool=False,
          delivery: dict | None=None) -> dict:
    v=GitView(repo,ref); b,s=binding_for(v,binding_path,scope)
    snap=snapshot(repo,ref,binding_path,scope)
    errors,external=inspect_documents(v,[b['overview'],s['map']])
    intake={}
    v2=b['schema']=='workmap-binding/v2'
    reader_current=False
    reader_history_valid=False
    try:
        all_intakes=v.obj(b['receipt_path'])
        if all_intakes.get('schema')!='workmap-intake/v1': raise ValueError('bad intake schema')
        intake=all_intakes.get('intakes',{}).get(scope,{})
        if not intake: errors.append('INTAKE_MISSING')
    except ValueError: errors.append('INTAKE_MISSING')
    if intake:
        if intake.get('snapshot')!=snap['fingerprint']: errors.append('INTAKE_STALE')
        manager=intake.get('manager',{})
        if manager.get('role')!=b['manager_role'] or not manager.get('context'):
            errors.append('MANAGER_IDENTITY_REQUIRED')
        if not valid_report(v,intake.get('decision_report')): errors.append('MANAGEMENT_REPORT_UNBOUND')
        reader=intake.get('reader_check',{})
        if reader.get('status')=='RECORDED':
            if (not reader.get('context') or reader.get('independent_of_map_builder') is not True
                or not valid_report(v,reader.get('report'))): errors.append('READER_RECORD_INCOMPLETE')
            if v2:
                try:
                    read_snap=snapshot(repo,reader.get('input_commit',''),binding_path,scope)
                    reader_history_valid=read_snap.get('reader_fingerprint')==reader.get('input_snapshot')
                except ValueError: reader_history_valid=False
                if not reader_history_valid: errors.append('READER_INPUT_MISMATCH')
                reader_current=reader_history_valid and reader.get('input_snapshot')==snap['reader_fingerprint']
            else:
                reader_current=reader.get('input_snapshot')==snap['fingerprint']
                if not reader_current: errors.append('READER_INPUT_MISMATCH')
        elif reader.get('status')!='PENDING': errors.append('READER_STATUS_REQUIRED')
        for claim in intake.get('validation_claims',[]):
            if not valid_report(v,claim.get('evidence')): errors.append('VALIDATION_EVIDENCE_UNBOUND')
            tested=claim.get('tested_code_commit',''); claimed=claim.get('claimed_code_commit','')
            if not HEX.fullmatch(tested) or not HEX.fullmatch(claimed) or tested!=claimed:
                errors.append('VALIDATION_VERSION_MISMATCH')
    if base_ref:
        old=GitView(repo,base_ref)
        try:
            oldb,olds=binding_for(old,binding_path,scope)
            olddocs=[oldb['overview'],olds['map']]
            newdocs={d['path']:set(d['anchors']) for d in [b['overview'],s['map']]}
            for doc in olddocs:
                for anchor in doc['anchors']:
                    if anchor not in newdocs.get(doc['path'],set()):
                        key=doc['path']+'#'+anchor
                        move=intake.get('scope_dispositions',{}).get(key,{})
                        target=move.get('target','').split('#',1)
                        if (not move.get('reason') or not valid_report(v,move.get('source'))
                            or len(target)!=2 or target[1] not in newdocs.get(target[0],set())):
                            errors.append('SCOPE_REMOVED_WITHOUT_DISPOSITION:'+key)
            try:
                previous=old.obj(oldb['receipt_path']).get('intakes',{}).get(scope,{})
            except ValueError: previous={}
            a=previous.get('effort',{}).get('known_pro_turns')
            z=intake.get('effort',{}).get('known_pro_turns')
            if isinstance(a,int) and (not isinstance(z,int) or z<a):
                correction=intake.get('effort_correction',{})
                if not correction.get('reason') or not valid_report(v,correction.get('source')):
                    errors.append('EFFORT_RESET_WITHOUT_SOURCE')
        except ValueError:
            # Bootstrap is explicitly permitted when the old commit has no binding.
            # A malformed existing binding is not treated as absence.
            if old.exists(binding_path): errors.append('BASE_BINDING_UNREADABLE')
        if actor=='executor':
            protected=[binding_path,b['receipt_path'],b['overview']['path']]
            protected.extend(x['map']['path'] for x in b['streams'].values())
            protected.extend(x['task'] for x in b['streams'].values())
            changed=v.run('diff','--name-only',base_ref,ref,'--',*protected).strip()
            if changed: errors.append('EXECUTOR_MODIFIED_MANAGED_SURFACE')
    elif actor=='executor': errors.append('EXECUTOR_BASE_REF_REQUIRED')
    if dispatch:
        d=intake.get('dispatch',{})
        task_text=v.text(s['task'])
        match=re.search(r'^\s*task_id:\s*[\'\"]?([^\s\'\"`]+)',task_text,re.M)
        if (d.get('decision')!='ISSUED' or d.get('task_path')!=s['task']
            or d.get('task_blob')!=v.oid(s['task'])
            or not match or d.get('task_id')!=match.group(1)):
            errors.append('TASK_NOT_BOUND_TO_INTAKE')
        if v2:
            # Unknown transitions fail closed. Routine reuse is an explicit management judgement.
            routine=d.get('kind') in ('ROUTINE_RESULT','EXISTING_AUTHORIZED_REPAIR')
            needs_reader=d.get('requires_reader_check',True) or not routine
            if routine and not needs_reader and not d.get('reader_reason'):
                errors.append('READER_REUSE_REASON_REQUIRED')
            if needs_reader and not reader_current: errors.append('READER_CHECK_REQUIRED')
            methods=d.get('method_paths')
            if not isinstance(methods,list) or not methods or any(x not in b['rule_paths'] for x in methods):
                errors.append('PROFESSIONAL_METHOD_INPUT_REQUIRED')
            if delivery and delivery.get('task_payload_sha256')!=snap['task_payload_sha256']:
                errors.append('TASK_PAYLOAD_CHANGED')
        else:
            needs_reader=d.get('requires_reader_check',True) or d.get('kind')!='EXISTING_AUTHORIZED_REPAIR'
            if needs_reader and intake.get('reader_check',{}).get('status')!='RECORDED':
                errors.append('READER_CHECK_REQUIRED')
        if not delivery:
            errors.append('DELIVERY_OBSERVATION_REQUIRED')
        else:
            if (delivery.get('observed_commit')!=ref or delivery.get('task_id')!=d.get('task_id')
                or delivery.get('task_blob')!=v.oid(s['task']) or not delivery.get('evidence')):
                errors.append('DELIVERY_OBSERVATION_STALE')
            if delivery.get('state') not in ('NOT_SENT','CONFIRMED_SEND_FAILED'):
                errors.append('DELIVERY_NOT_SENDABLE:'+str(delivery.get('state','UNKNOWN')))
    errors=sorted(set(errors))
    next_action=None
    if errors:
        next_action={
            'recipient':b['manager_role'],'scope':scope,'exact_input_commit':ref,
            'task_path':s['task'],'errors':errors,
            'instruction':'读取这些确切输入，定向补管理接收、地图或发送现场核对；保留已提交实质成果，不重跑业务、不重复派发、不替换未受影响任务。'}
    reader_qualification=intake.get('reader_check',{}).get('status','UNKNOWN')
    if v2 and reader_history_valid and not reader_current: reader_qualification='RECORDED_OLD_INPUT'
    return {'schema':'workmap-check/v2' if v2 else 'workmap-check/v1','scope':scope,'exact_input_commit':ref,'ok':not errors,
            'check_kind':'DISPATCH_PREFLIGHT' if dispatch else 'MECHANICAL_INTAKE',
            'errors':errors,'reader_qualification':reader_qualification,
            'external_links_require_connector_or_checkout_readback':external,
            'snapshot':snap,'next_action':next_action,
            'limits':'不证明业务正确、审查实际独立、远端已同步或本地调度已部署；输入记录真实性由执行者与审查承担。'}


def _order_field(body: str, name: str) -> str:
    """Read the existing Worker order/report header, including semicolon-separated fields."""
    match=re.search(r'(?m)(?:^|；)\s*'+re.escape(name)+r':\s*([^\r\n；]+)',body)
    return match.group(1).strip() if match else ''


def worker_result(repo: Path | str, ref: str, binding_path: str, scope: str, *,
                  base_ref: str, order_path: str, report_path: str) -> dict:
    """Route an actual Worker result to its issuing Pro, without adopting new results."""
    v=GitView(repo,ref); old=GitView(repo,base_ref)
    b,s=binding_for(v,binding_path,scope)
    errors=[]
    try: v.run('merge-base','--is-ancestor',base_ref,ref)
    except ValueError: errors.append('BASE_NOT_ANCESTOR')
    if b['schema']!='workmap-binding/v2':
        errors.append('WORKER_RETURN_REQUIRES_V2')
    if not check(repo,base_ref,binding_path,scope,base_ref=base_ref)['ok']:
        errors.append('ACCEPTED_BASE_INTAKE_REQUIRED')
    earlier=snapshot(repo,base_ref,binding_path,scope)
    current=snapshot(repo,ref,binding_path,scope)
    if (v.oid(binding_path)!=old.oid(binding_path)
            or earlier.get('reader_fingerprint')!=current.get('reader_fingerprint')):
        errors.append('PROTECTED_INPUT_CHANGED')
    if v.oid(b['receipt_path'])!=old.oid(b['receipt_path']):
        errors.append('MANAGEMENT_INTAKE_CHANGED')

    order_path=safe_path(order_path); report_path=safe_path(report_path)
    run_root=s['task'].rsplit('/',1)[0]
    order=v.text(order_path); report=v.text(report_path)
    order_id=_order_field(order,'order_id')
    issuer_role=_order_field(order,'issuer_role')
    issuer=_order_field(order,'issuer_ref')
    issuer_invocation=_order_field(order,'issuer_invocation_id')
    token=_order_field(order,'issuer_assignment_token')
    recipient=_order_field(order,'return_to')
    round_match=re.search(r'-R(\d{4})-',issuer_invocation)
    round_id='R'+round_match.group(1) if round_match else ''
    issuer_dir=(run_root+'/artifacts/professional-' if issuer_role=='professional'
                else run_root+'/reviews/management-')+round_id
    if (issuer_role not in ('professional','management')
            or not round_id or order_path!=issuer_dir+'/WORKER_ORDER.md'
            or not issuer or not token or recipient!=issuer or not re.fullmatch(r'[A-Za-z0-9_-]+',order_id)):
        errors.append('WORKER_ORDER_AUTHORITY_INVALID')
    if report_path!=run_root+'/artifacts/worker-'+order_id+'/FULL_RESPONSE.md':
        errors.append('WORKER_RESULT_PATH_MISMATCH')
    for name,value in (('order_id',order_id),('work_id',_order_field(order,'work_id')),
                       ('run_id',_order_field(order,'run_id')),
                       ('return_to',recipient),('issuer_invocation_id',issuer_invocation)):
        if not value or _order_field(report,name)!=value:
            errors.append('WORKER_RESULT_IDENTITY_MISMATCH:'+name)
    if old.exists(report_path) and old.oid(report_path)==v.oid(report_path):
        errors.append('WORKER_RESULT_UNCHANGED')

    if round_id:
        try:
            source=run_root+'/provenance/turns/'+round_id+'/'
            invocation=v.obj(source+'INVOCATION.json')
            sent=v.obj(source+'SEND_RECEIPT.json')
            if (invocation.get('role')!=issuer_role or invocation.get('recipient_ref')!=issuer
                    or invocation.get('invocation_id')!=issuer_invocation
                    or invocation.get('assignment_token')!=token
                    or invocation.get('work_id')!=_order_field(order,'work_id')
                    or invocation.get('run_id')!=_order_field(order,'run_id')
                    or sent.get('state')!='COMMITTED'
                    or sent.get('invocation_id')!=issuer_invocation
                    or sent.get('assignment_token')!=token
                    or sent.get('recipient_ref')!=issuer):
                errors.append('ISSUER_CALL_NOT_VERIFIED')
        except ValueError:
            errors.append('ISSUER_CALL_NOT_VERIFIED')
    errors=sorted(set(errors))
    return {'schema':'workmap-worker-result/v1','scope':scope,'exact_input_commit':ref,
            'check_kind':'WORKER_RESULT_TO_ISSUER','ok':not errors,'errors':errors,
            'recipient':issuer if not errors else None,'order_id':order_id,
            'full_intake_current':current['fingerprint']==v.obj(b['receipt_path'])['intakes'][scope]['snapshot'],
            'next_action':({'recipient':issuer,'instruction':'将本工单真实技术结果交原签发Pro消费；需要管理判断由该Pro按有效Binding提出。'}
                           if not errors else None),
            'limits':'仅验证原工单技术结果的交接身份；不更新Intake、不认可专业成果、不批准下游派发。'}


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('command',choices=['snapshot','check','dispatch','worker-result'])
    p.add_argument('--repo',required=True); p.add_argument('--ref',required=True)
    p.add_argument('--binding',required=True); p.add_argument('--scope',required=True)
    p.add_argument('--base-ref'); p.add_argument('--actor',choices=['management_review','executor'],default='management_review')
    p.add_argument('--delivery',help='local JSON observation from the actual sending endpoint, never guessed')
    p.add_argument('--order',help='exact issued WORKER_ORDER.md path for worker-result')
    p.add_argument('--worker-report',help='exact Worker FULL_RESPONSE.md path for worker-result')
    p.add_argument('--output',help='write a machine result to this local file; does not edit Git')
    args=p.parse_args()
    try:
        if args.command!='snapshot' and not args.base_ref:
            raise ValueError('BASE_REF_REQUIRED: supply the previous accepted input, not a guessed current HEAD')
        if args.command=='snapshot': result=snapshot(args.repo,args.ref,args.binding,args.scope)
        elif args.command=='worker-result':
            if not args.order or not args.worker_report:
                raise ValueError('WORKER_ORDER_AND_REPORT_REQUIRED')
            result=worker_result(args.repo,args.ref,args.binding,args.scope,
                                 base_ref=args.base_ref,order_path=args.order,report_path=args.worker_report)
        else:
            delivery=json.loads(Path(args.delivery).read_text(encoding='utf-8')) if args.delivery else None
            result=check(args.repo,args.ref,args.binding,args.scope,base_ref=args.base_ref,
                         actor=args.actor,dispatch=args.command=='dispatch',delivery=delivery)
        text=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
        if args.output: Path(args.output).write_text(text,encoding='utf-8')
        sys.stdout.write(text)
        return 0 if result.get('ok',True) else 2
    except (ValueError,KeyError,TypeError,OSError) as e:
        sys.stdout.write(json.dumps({'ok':False,'error':str(e),'next_action':
            ('核对原工单、实际回交与有权签发来源；不自行改派管理。' if args.command=='worker-result' else '回管理端修正指定绑定或取得确切Git对象；不猜版本，不重跑业务。')},ensure_ascii=False)+'\n')
        return 2

if __name__=='__main__': raise SystemExit(main())
