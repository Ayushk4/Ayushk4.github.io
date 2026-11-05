"""Inline SVG charts for the design previews, built from content.py.

Colors come from CSS custom properties (--vz-*) that each design defines for
light and dark mode, so one SVG works in every theme. Each chart is rendered
twice (wide and narrow) and the page shows the one that fits.
"""
import math

import numpy as np

from content import SIZES, SWEEP, SWEEP_REF

TABLES_PER_STEP = 64


def _fmt_tick(v):
    return f"{v:g}"


def fit_sweep(metric_idx=3):
    """Per-size power law 1 - acc = A * D^(-p), D = tables seen. Returns dict."""
    fits = {}
    for size, _ in SIZES:
        rows = [r for r in SWEEP if r[0] == size]
        D = np.array([r[1] * 1000 * TABLES_PER_STEP for r in rows], dtype=float)
        err = np.array([1 - r[metric_idx] for r in rows])
        slope, intercept = np.polyfit(np.log(D), np.log(err), 1)
        h_per_k = np.mean([r[2] / r[1] for r in rows])  # H100-days per 1K steps
        fits[size] = {"A": float(math.exp(intercept)), "p": float(-slope),
                      "h_per_k": float(h_per_k),
                      "h_min": min(r[2] for r in rows), "h_max": max(r[2] for r in rows)}
    return fits


def _acc_at(fit, h):
    D = h / fit["h_per_k"] * 1000 * TABLES_PER_STEP
    return 1 - fit["A"] * D ** (-fit["p"])


def scaling_chart(width=640, height=360, chart_id="scal"):
    """TALENT-Tiny accuracy vs stage-1 compute, per size, with fitted curves."""
    narrow = width < 480
    ml, mr, mt, mb = (40, 10, 26, 40) if narrow else (48, 16, 28, 44)
    pw, ph = width - ml - mr, height - mt - mb
    xmin, xmax = 0.04, 40.0
    ymin, ymax = 0.790, 0.830

    def X(h):
        return ml + (math.log10(h) - math.log10(xmin)) / (math.log10(xmax) - math.log10(xmin)) * pw

    def Y(a):
        return mt + (ymax - a) / (ymax - ymin) * ph

    out = [f'<svg class="vz" viewBox="0 0 {width} {height}" role="img" '
           f'aria-labelledby="{chart_id}-t" preserveAspectRatio="xMidYMid meet">',
           f'<title id="{chart_id}-t">TALENT-Tiny accuracy against stage-1 compute for four model sizes, '
           'with per-size power-law fits</title>']
    # grid + y ticks
    for a in [0.79, 0.80, 0.81, 0.82, 0.83]:
        y = Y(a)
        out.append(f'<line class="vz-grid" x1="{ml}" x2="{ml + pw}" y1="{y:.1f}" y2="{y:.1f}"/>')
        out.append(f'<text class="vz-tick" x="{ml - 6}" y="{y + 4:.1f}" text-anchor="end">{a:.2f}</text>')
    xticks = [0.1, 1, 10] if narrow else [0.1, 0.3, 1, 3, 10, 30]
    for h in xticks:
        x = X(h)
        out.append(f'<line class="vz-grid" x1="{x:.1f}" x2="{x:.1f}" y1="{mt}" y2="{mt + ph}"/>')
        out.append(f'<text class="vz-tick" x="{x:.1f}" y="{mt + ph + 16}" text-anchor="middle">{_fmt_tick(h)}</text>')
    out.append(f'<line class="vz-axis" x1="{ml}" x2="{ml + pw}" y1="{mt + ph}" y2="{mt + ph}"/>')
    out.append(f'<text class="vz-label" x="{ml + pw / 2:.1f}" y="{height - 6}" text-anchor="middle">'
               'Stage-1 compute (H100-days on 4xH100, log scale)</text>')
    out.append(f'<text class="vz-label" x="{ml - (34 if narrow else 42)}" y="{mt - 12}">Accuracy, TALENT-Tiny</text>')

    fits = fit_sweep()
    # fitted curves first, markers on top
    for i, (size, _) in enumerate(SIZES):
        f = fits[size]
        hs = np.geomspace(f["h_min"], f["h_max"], 40)
        pts = " ".join(f"{X(h):.1f},{Y(_acc_at(f, h)):.1f}" for h in hs)
        out.append(f'<polyline class="vz-line s{i + 1}" points="{pts}"/>')
    for i, (size, params) in enumerate(SIZES):
        for r in [r for r in SWEEP if r[0] == size]:
            out.append(f'<circle class="vz-dot s{i + 1}" cx="{X(r[2]):.1f}" cy="{Y(r[3]):.1f}" r="4">'
                       f'<title>{size} ({params}), {r[1]}K steps: {r[2]} H100-days, accuracy {r[3]:.4f}</title>'
                       '</circle>')
    # reference point (released model, all stages)
    name, h, acc = SWEEP_REF[0], SWEEP_REF[1], SWEEP_REF[2]
    rx, ry = X(h), Y(acc)
    out.append(f'<circle class="vz-ref" cx="{rx:.1f}" cy="{ry:.1f}" r="5"><title>{name}: {h} H100-days, '
               f'accuracy {acc:.4f}</title></circle>')
    lbl = "TabICLv2 release" if narrow else "TabICLv2 release (all stages)"
    out.append(f'<text class="vz-note" x="{rx - 9:.1f}" y="{ry - 9:.1f}" text-anchor="end">{lbl}</text>')
    out.append("</svg>")
    return "\n".join(out)


COST_ROWS = [
    ("Tiny 4.7M", 3.15, False), ("Base 27.6M", 5.43, False), ("Medium 194.2M", 7.21, False),
    ("Large 1.03B", 17.35, False), ("TabICLv2 reference, 28M", 20.96, True),
]


def cost_chart(width=640, chart_id="cost"):
    """Stage-1 H100-days on 4xH100 (Table 4), MegaTabICL sizes vs the reference."""
    narrow = width < 480
    label_w = 0 if narrow else 168
    row_h = 46 if narrow else 34
    bar_h = 14 if narrow else 16
    mt, mb, mr = 6, 26, 52
    height = mt + row_h * len(COST_ROWS) + mb
    pw = width - label_w - mr
    vmax = 25.0

    def W(v):
        return v / vmax * pw

    out = [f'<svg class="vz" viewBox="0 0 {width} {height}" role="img" aria-labelledby="{chart_id}-t">',
           f'<title id="{chart_id}-t">Stage-1 cost in H100-days on 4xH100 for each MegaTabICL size and '
           'the TabICLv2 reference</title>']
    for v in [0, 5, 10, 15, 20, 25]:
        x = label_w + W(v)
        out.append(f'<line class="vz-grid" x1="{x:.1f}" x2="{x:.1f}" y1="{mt}" y2="{height - mb}"/>')
        out.append(f'<text class="vz-tick" x="{x:.1f}" y="{height - mb + 16}" text-anchor="middle">{v}</text>')
    for i, (name, v, ref) in enumerate(COST_ROWS):
        y0 = mt + i * row_h
        if narrow:
            ty, by = y0 + 13, y0 + 20
            out.append(f'<text class="vz-cat" x="0" y="{ty}">{name}</text>')
        else:
            by = y0 + (row_h - bar_h) / 2
            out.append(f'<text class="vz-cat" x="{label_w - 10}" y="{by + bar_h - 3:.1f}" text-anchor="end">{name}</text>')
        w = W(v)
        x0 = label_w
        cls = "vz-bar ref" if ref else "vz-bar s1"
        # 4px rounded data end, square at the baseline
        r = 4
        path = (f"M{x0},{by:.1f} h{w - r:.1f} a{r},{r} 0 0 1 {r},{r} v{bar_h - 2 * r} "
                f"a{r},{r} 0 0 1 -{r},{r} h-{w - r:.1f} z")
        out.append(f'<path class="{cls}" d="{path}"><title>{name}: {v} H100-days</title></path>')
        out.append(f'<text class="vz-val" x="{x0 + w + 6:.1f}" y="{by + bar_h - 3:.1f}">{v:g}</text>')
    out.append(f'<line class="vz-axis" x1="{label_w}" x2="{label_w}" y1="{mt}" y2="{height - mb}"/>')
    out.append("</svg>")
    return "\n".join(out)


def both(fn, wide, narrow, **kw):
    """Return wide + narrow renderings; CSS shows one."""
    return (f'<div class="vz-wide">{fn(width=wide, chart_id=kw.get("chart_id", "c") + "w")}</div>'
            f'<div class="vz-narrow">{fn(width=narrow, chart_id=kw.get("chart_id", "c") + "n")}</div>')


VZ_CSS = """
.vz{width:100%;height:auto;display:block;overflow:visible}
.vz text{font-family:inherit;fill:var(--vz-ink2)}
.vz .vz-tick{font-size:11px;fill:var(--vz-muted);font-variant-numeric:tabular-nums}
.vz .vz-label{font-size:11px;fill:var(--vz-ink2)}
.vz .vz-note{font-size:11px;fill:var(--vz-ink2)}
.vz .vz-cat{font-size:12px;fill:var(--vz-ink)}
.vz .vz-val{font-size:12px;fill:var(--vz-ink);font-variant-numeric:tabular-nums}
.vz-grid{stroke:var(--vz-grid);stroke-width:1}
.vz-axis{stroke:var(--vz-axis);stroke-width:1}
.vz-line{fill:none;stroke-width:2;stroke-linejoin:round;stroke-linecap:round;opacity:.9}
.vz-dot{stroke:var(--vz-surface);stroke-width:2}
.vz-dot:hover,.vz-bar:hover{opacity:.8}
.vz-ref{fill:var(--vz-surface);stroke:var(--vz-muted);stroke-width:2}
.vz-line.s1{stroke:var(--vz-s1)}.vz-line.s2{stroke:var(--vz-s2)}.vz-line.s3{stroke:var(--vz-s3)}.vz-line.s4{stroke:var(--vz-s4)}
.vz-dot.s1,.vz-bar.s1,.vz-key.s1{fill:var(--vz-s1)}.vz-dot.s2,.vz-key.s2{fill:var(--vz-s2)}
.vz-dot.s3,.vz-key.s3{fill:var(--vz-s3)}.vz-dot.s4,.vz-key.s4{fill:var(--vz-s4)}
.vz-bar.ref{fill:var(--vz-refbar)}
.vz-narrow{display:none}
@media (max-width:560px){.vz-wide{display:none}.vz-narrow{display:block}}
.vz-legend{display:flex;flex-wrap:wrap;gap:4px 14px;font-size:12px;color:var(--vz-ink2);margin:0 0 8px;padding:0;list-style:none}
.vz-legend li{display:flex;align-items:center;gap:6px}
.vz-legend i{width:10px;height:10px;border-radius:50%;display:inline-block}
.vz-legend i.s1{background:var(--vz-s1)}.vz-legend i.s2{background:var(--vz-s2)}
.vz-legend i.s3{background:var(--vz-s3)}.vz-legend i.s4{background:var(--vz-s4)}
.vz-legend i.ref{background:transparent;border:2px solid var(--vz-muted);width:8px;height:8px}
"""


def legend_html():
    items = "".join(f'<li><i class="s{i + 1}"></i>{s} ({p})</li>' for i, (s, p) in enumerate(SIZES))
    items += '<li><i class="ref"></i>TabICLv2 release</li>'
    return f'<ul class="vz-legend" aria-label="Legend">{items}</ul>'
