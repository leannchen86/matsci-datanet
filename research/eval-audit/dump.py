import json, sys, os
out_file, dest = sys.argv[1], sys.argv[2]
raw = open(out_file, encoding='utf-8').read()
# find the JSON object
i = raw.find('{"finished"')
obj = json.JSONDecoder().raw_decode(raw[i:])[0]
json.dump(obj, open(os.path.join(dest, 'result.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for L in obj['lenses']:
    k = L['lens']; a = L['audit']; c = L['challenge']
    w = []
    w.append(f"# {k}\n")
    e = a['is_eval_work']
    w.append(f"## is eval work: {e['answer']}\nEVAL: {e['which_parts_are_eval']}\nNOT: {e['which_parts_are_not']}\nNAME: {e.get('best_one_line_name_for_this_work','')}\n")
    w.append("## scorecard")
    for r in a['scorecard']:
        w.append(f"- [{r['verdict']}]{' [BEFORE-STEP-1]' if r['must_fix_before_first_step'] else ''} {r['principle_id']} {r['principle']}\n  EVID: {r['evidence']}\n  GAP: {r.get('gap','')}\n  FIX: {r.get('fix','')} ({r.get('effort','')})")
    w.append("\n## direction findings")
    for d in a['direction_findings']:
        w.append(f"- [{d['severity']}] {d['claim']}\n  EVID: {d['evidence']}\n  REC: {d['recommendation']}")
    w.append("\n## top changes")
    for t in a['top_changes']: w.append(f"- {t}")
    w.append(f"\n## verdict: {a['verdict_on_proceeding']}\n")
    w.append("# CHALLENGE")
    for v in c['verdicts']:
        w.append(f"- [{v['status']}] ({v['kind']}) {v['target']}\n  WHY: {v['why']}\n  CORRECTED: {v.get('corrected_text','')}")
    w.append("\n## citation checks")
    for v in c['citation_checks']:
        w.append(f"- [{v['status']}] {v['source']} {v.get('url','')} :: {v.get('note','')}")
    w.append("\n## missed")
    for m in c['missed']: w.append(f"- {m}")
    w.append(f"\n## overall\n{c['overall']}")
    open(os.path.join(dest, f'{k}.md'), 'w', encoding='utf-8').write('\n'.join(w))
    print(k, len('\n'.join(w)))
