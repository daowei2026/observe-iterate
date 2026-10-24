"""核本单实际记录的完整性与对照关系；不运行生产或平台流程。"""
from pathlib import Path
import argparse,hashlib,json

p=argparse.ArgumentParser();p.add_argument('--evidence',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
args=p.parse_args();root=args.evidence
read=lambda n:json.loads((root/n).read_text())
old,new=read('old-restore.json'),read('cbd-restore.json')
active=read('ACTIVE_TRIER_FASON_OBSERVATION.json')
n_active=read('ACTIVE_TRIER_N_RECOVERY.json')
named,warm=read('NAMED_HOST_CONSTRUCTOR.json'),read('NAMED_HOST_PREWARMED.json')
checks=[]
def check(name,condition):checks.append({'name':name,'passed':bool(condition)})
check('baseline ordinary same-version restore is a positive control',old['objects']['ordinary_chart_path']['same_version_restore']['status']=='accepted')
check('cbd accepts the old ordinary serialized contract',new['restorations']['ordinary_chart_path']['status']=='accepted')
for key in ['ordinary_chart_path','ordinary_key_omitted','ordinary_explicit_empty','named_n']:
 item=new['objects'][key]
 check(key+' actually serializes the N key',item['serialized_key_present'])
 check(key+' same-version recovery accepted',item['same_version_restore']['status']=='accepted')
 rejected=old['restorations'][key]
 check(key+' rejected by old receiver at the precise N parameter',rejected['status']=='rejected' and rejected['error']['unknown_parameter']=='normal_node_behavior_manifest')
for key in ['ordinary_key_omitted','ordinary_explicit_empty']:
 check(key+' is byte-identical to ordinary chart serialization',new['objects'][key]['serialized_sha256']==new['objects']['ordinary_chart_path']['serialized_sha256'])
check('ordinary ppid changed between baseline and cbd under identical probe scope',old['objects']['ordinary_chart_path']['ppid']!=new['objects']['ordinary_chart_path']['ppid'])
check('live Trier existing shared-class instance returned application success',active['http_status']==200 and active['application_code']==2000)
check('live Trier expanded keys match baseline rather than cbd',set(active['effective_expanded_parameter_keys'])==set(old['declared_keys']) and not active['n_parameter_present'])
check('live Trier existing N node metadata recovery currently rejects the N key',n_active['node_id']==6129 and n_active['http_status']==200 and n_active['application_code']==3000 and n_active['restoring_class']=='AidataBigWorldReviewCAE' and n_active['unknown_parameter']=='normal_node_behavior_manifest')
check('isolated named host follows actual normal recovery',named['normal_restore']['status']=='accepted')
check('prewarmed eval namespace reproduces missing-name boundary',warm['class_known_in_this_process'] and not warm['class_in_actual_eval_namespace'] and warm['normal_restore']['status']=='rejected' and warm['normal_restore']['type']=='NameError')
result={'qualification':'本单技术事实/正反对照完整性，不是平台恢复、工作3或业务正确性验收',
 'checks':checks,'all_passed':all(c['passed'] for c in checks),
 'evidence_hashes':{n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in ['old-restore.json','cbd-restore.json','ACTIVE_TRIER_FASON_OBSERVATION.json','ACTIVE_TRIER_N_RECOVERY.json','NAMED_HOST_CONSTRUCTOR.json','NAMED_HOST_PREWARMED.json']}}
args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'all_passed':result['all_passed'],'failed':[c['name'] for c in checks if not c['passed']]},ensure_ascii=False))
raise SystemExit(0 if result['all_passed'] else 1)
