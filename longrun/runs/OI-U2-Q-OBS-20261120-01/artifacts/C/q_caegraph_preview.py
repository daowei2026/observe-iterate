#!/usr/bin/env python3
"""Generate the deterministic C2 expectation HTML for Q.

This is display-only demo data. It does not run F/Q, bind B's final
position, or freeze the outer feature instance.
"""
from __future__ import annotations
import argparse, html, json
from pathlib import Path

T = [f"T{i}" for i in range(12)]
PRICES = {
    "rb": [1, 1.004, 1.009, 1.014, 1.020, 1.027, 1.033, 1.039, 1.043, 1.049, 1.054, 1.058],
    "hc": [1, 1.003, 1.008, 1.012, 1.017, 1.023, 1.028, 1.034, 1.037, 1.041, 1.046, 1.050],
    "i": [1, 1.006, 1.011, 1.010, 1.018, 1.021, 1.019, 1.025, 1.023, 1.028, 1.026, 1.029],
}
EVENTS = [
    dict(id="F-L7/R2", kind="F candidate", t=2, lane=0, detail="candidateKnown=T2; members=rb,hc,i"),
    dict(id="Q-L7/R1", kind="Q revision", t=4, lane=1, detail="Previous=None; candidateReference=F-L7/R2; QualifiedWorking"),
    dict(id="Q-L7/R2", kind="Q revision", t=7, lane=1, detail="Previous=Q-L7/R1; directionalKnown=T7; Pending"),
    dict(id="Q-L7/R3", kind="Q revision", t=9, lane=1, detail="Previous=Q-L7/R2; directionalKnown=T9; QualifiedCompleted"),
    dict(id="END-L7", kind="Duty end", t=11, lane=2, detail="DirectionalRevisionDutyEnded; last successful=Q-L7/R3; no new revision"),
]
STATES = [
    (4, "QualifiedWorking", "MotionObserving", "SubjectApplicable"),
    (7, "QualificationPending", "MotionObserving", "SubjectApplicable"),
    (9, "QualifiedCompleted", "HorizonReached", "SubjectApplicable"),
]
MEMBERS = {
    "rb": dict(asked=2, used=2, endpoint=9, successor=9, verdict="SupportsAskedDirection", completion="MotionCompleted", basis="CandidateMemberBasis", path=True, q=[("ProgressP", "7.0"), ("AmplitudeA", "0.058"), ("DurationD", "7.0"), ("PathLengthL", "0.070"), ("EfficiencyE", "0.83"), ("CounterC", "0.0")]),
    "hc": dict(asked=2, used=3, endpoint=9, successor=9, verdict="SupportsAskedDirection", completion="MotionCompleted", basis="MemberBasisRevised", path=True, q=[("ProgressP", "6.0"), ("AmplitudeA", "0.043"), ("DurationD", "6.0"), ("PathLengthL", "0.056"), ("EfficiencyE", "0.77"), ("CounterC", "0.0")]),
    "i": dict(asked=2, used=2, endpoint=7, successor=None, verdict="WorkingPathUnavailable", completion="MotionWorking", basis="CandidateMemberBasis", path=False, q=[("ProgressP", "5.0"), ("AmplitudeA", "0.025"), ("DurationD", "5.0"), ("PathLengthL", "— / PathUnavailable"), ("EfficiencyE", "— / PathUnavailable"), ("CounterC", "— / PathUnavailable")]),
}


def x(i: int) -> float:
    return 58 + i * (1042 / 11)


def path(values):
    lo, hi = min(values), max(values)
    span = hi - lo or 1
    return " ".join(f"{x(i):.1f},{18 + (hi - y) * 192 / span:.1f}" for i, y in enumerate(values))


def prices(final):
    colors = {"rb": "#2563eb", "hc": "#16a34a", "i": "#d97706"}
    lines = "".join(
        f'<polyline fill="none" stroke="{colors[s]}" stroke-width="3" points="{path(v)}"><title>{s}: ratio display derivative; do not infer raw values</title></polyline>'
        for s, v in PRICES.items()
    )
    markers = ""
    if final:
        for sym, member in MEMBERS.items():
            lo, hi = min(PRICES[sym]), max(PRICES[sym])
            span = hi - lo or 1
            for key, shape, color in [("asked", "rect", "#64748b"), ("used", "circle", "#7c3aed"), ("endpoint", "tri", "#0f766e")]:
                i = member[key]
                xx = x(i)
                yy = 18 + (hi - PRICES[sym][i]) * 192 / span
                tip = html.escape(f"{sym} {key}={T[i]}; {member['verdict']}")
                if shape == "rect":
                    markers += f'<rect class="member" x="{xx-5}" y="{yy-5}" width="10" height="10" fill="{color}"><title>{tip}</title></rect>'
                elif shape == "circle":
                    markers += f'<circle class="member" cx="{xx}" cy="{yy}" r="5" fill="{color}"><title>{tip}</title></circle>'
                else:
                    markers += f'<polygon class="member" points="{xx},{yy-7} {xx+7},{yy+7} {xx-7},{yy+7}" fill="{color}"><title>{tip}</title></polygon>'
    axis = "".join(f'<text x="{x(i)-8:.1f}" y="232" font-size="10">{t}</text>' for i, t in enumerate(T))
    return f'<svg viewBox="0 0 1120 245"><line x1="58" y1="215" x2="1100" y2="215" stroke="#94a3b8"/>{lines}{markers}{axis}</svg>'


def lifecycle(final):
    colors = {"F candidate": "#64748b", "Q revision": "#2563eb", "Duty end": "#dc2626"}
    out = []
    if final:
        q_events = [e for e in EVENTS if e["kind"] == "Q revision"]
        out += [f'<line x1="{x(a["t"])}" y1="100" x2="{x(b["t"])}" y2="100" stroke="#93c5fd" stroke-width="3"><title>{a["id"]} → {b["id"]}</title></line>' for a, b in zip(q_events, q_events[1:])]
    for event in EVENTS:
        xx, yy = x(event["t"]), (52, 100, 148)[event["lane"]]
        tip = html.escape(event["id"] + " | " + event["detail"])
        css_class = {"F candidate": "input", "Q revision": "qrev", "Duty end": "duty"}[event["kind"]]
        if event["kind"] == "Duty end":
            glyph = f'<polygon class="{css_class}" points="{xx},{yy-8} {xx+8},{yy} {xx},{yy+8} {xx-8},{yy}" fill="{colors[event["kind"]]}"><title>{tip}</title></polygon>'
        elif event["kind"] == "F candidate":
            glyph = f'<rect class="{css_class}" x="{xx-7}" y="{yy-7}" width="14" height="14" rx="2" fill="{colors[event["kind"]]}"><title>{tip}</title></rect>'
        else:
            glyph = f'<circle class="{css_class}" cx="{xx}" cy="{yy}" r="8" fill="{colors[event["kind"]]}"><title>{tip}</title></circle>'
        out += [glyph, f'<text x="{xx+10}" y="{yy-11}" font-size="11">{event["id"]}</text>']
    axis = "".join(f'<text x="{x(i)-8:.1f}" y="190" font-size="10">{t}</text>' for i, t in enumerate(T))
    return f'<svg viewBox="0 0 1120 205"><text x="4" y="56">F candidate</text><text x="4" y="104">Q revision</text><text x="4" y="152">Duty end</text>{"".join(out)}{axis}</svg>'


def table(head, rows):
    return '<table><thead><tr>' + ''.join(f'<th>{h}</th>' for h in head) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{cell}</td>' for cell in row) + '</tr>' for row in rows) + '</tbody></table>'


def members(final):
    cards = []
    for sym, member in MEMBERS.items():
        quantities = table(["quantity", "raw / missing"], member["q"])
        warning = '<p class="warn">Missing values preserve availability and are not zero.</p>' if final and not member["path"] else ''
        successor = "T" + str(member["successor"]) if member["successor"] is not None else "None"
        cards.append(f'<article><h3>{sym}</h3><p>{member["verdict"]} · {member["completion"]} · {member["basis"]}</p><p>asked=T{member["asked"]}; used=T{member["used"]}; endpoint=T{member["endpoint"]}; successor={successor}; path_complete={member["path"]}</p>{warning}{quantities}</article>')
    return '<div class="grid">' + ''.join(cards) + '</div>'


def document(final):
    version = "v0.2 current" if final else "v0.1 first"
    controls = '<div class="controls">' + ''.join(f'<label><input type="checkbox" checked data-toggle="{css}">{name}</label>' for css, name in [("input", "F candidate"), ("qrev", "Q revisions"), ("duty", "Duty end"), ("member", "member positions")]) + '</div>' if final else ''
    audit = table(
        ["identity", "Previous / reference", "publication / known", "semantics"],
        [
            ("Q-L7/R1", "Previous=None; F-L7/R2", "T4 / T4", "first DirectionalOccurrence"),
            ("Q-L7/R2", "Previous=Q-L7/R1; F-L7/R2", "T7 / T7", "Pending; path unavailable"),
            ("Q-L7/R3", "Previous=Q-L7/R2; F-L7/R2", "T9 / T9", "QualifiedCompleted"),
            ("END-L7", "last successful=Q-L7/R3", "T11 / T11", "DirectionalDutyEnd; no new revision"),
        ],
    ) if final else '<p>First version intentionally leaves detailed reference audit for the next loop.</p>'
    state = table(["publication", "qualification", "observation", "applicability"], [(f"T{t}", q, o, a) for t, q, o, a in STATES])
    payload = json.dumps(dict(times=T, prices=PRICES, events=EVENTS, members=MEMBERS), ensure_ascii=False)
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Q C2 {version}</title><style>
body{{margin:0;background:#f8fafc;color:#0f172a;font-family:system-ui,"Noto Sans SC",sans-serif}}header{{background:#0f172a;color:white;padding:22px 30px}}main{{max-width:1220px;margin:auto;padding:18px}}.panel{{background:white;border:1px solid #cbd5e1;border-radius:12px;padding:16px;margin:14px 0}}.note{{border-left:4px solid #0ea5e9;background:#e0f2fe;padding:10px}}svg{{width:100%;height:auto}}table{{width:100%;border-collapse:collapse;font-size:13px}}th,td{{padding:7px;border-bottom:1px solid #e2e8f0;text-align:left}}th{{background:#f1f5f9}}.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}}article{{border:1px solid #cbd5e1;border-radius:10px;padding:10px}}.controls{{display:flex;gap:16px;flex-wrap:wrap}}.warn{{color:#b45309;font-weight:600}}.hidden{{display:none}}code{{background:#e2e8f0;color:#0f172a;padding:1px 4px;border-radius:4px}}@media(max-width:850px){{.grid{{grid-template-columns:1fr}}}}
</style></head><body><header><h1>Q C2 display expectation {version}</h1><p>Deterministic demo only; no real Q run, no B final position, no frozen outer instance.</p></header><main>
<div class="note"><b>Read left to right:</b> price input → F candidate → Q revisions → group state → member facts → explicit duty end. <code>DirectionalOccurrence</code> is a whole-group viewpoint; <code>DirectionalDutyEnd</code> is a separate lifecycle occurrence. No new Q is not an end.</div>{controls}
<section class="panel"><h2>P1 Multi-symbol 5m price overview (ratio display derivative)</h2>{prices(final)}</section>
<section class="panel"><h2>P2 F candidate → Q revision → explicit duty end</h2><p>Q revision = <code>DirectionalOccurrence</code>; each revision preserves its <code>Q Life</code>, exact <code>candidateReference</code> and Previous. Duty end = <code>DirectionalDutyEnd</code>.</p>{lifecycle(final)}</section>
<section class="panel"><h2>P3 Group state emitted by Q revision</h2><p><code>directionalKnown</code>, publication firing and member actual/known positions remain distinct.</p>{state}</section>
<section class="panel"><h2>P4 Per-member motion and quantity audit</h2>{members(final)}<p>Six quantities have different units; the final CAEGraph uses categorical lanes and hover, not one numeric axis.</p></section>
<section class="panel"><h2>P5 Exact identity/reference audit</h2>{audit}</section>
<section class="panel"><h2>Contract</h2>{table(["must remain", "may change in D/E"], [("event identity; Q/F refs; revision chain; explicit end; multi-position member facts; missingness; raw/display distinction", "real curves; point count; coordinates; B objects/time; actual instance and values")])}</section>
</main><script>window.Q_DEMO={payload};document.querySelectorAll('[data-toggle]').forEach(x=>x.onchange=()=>document.querySelectorAll('.'+x.dataset.toggle).forEach(e=>e.classList.toggle('hidden',!x.checked)));</script></body></html>'''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', default='.')
    args = parser.parse_args()
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / 'C2_EXPECTED_V0_1.html').write_text(document(False), encoding='utf-8')
    (out / 'C2_EXPECTED.html').write_text(document(True), encoding='utf-8')


if __name__ == '__main__':
    main()
