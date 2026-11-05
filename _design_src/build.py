"""Build the design previews into designs/.

    python3 -m pip install jinja2 numpy     # once
    python3 _design_src/build.py            # writes designs/<name>/...

Preview locally from the repo root with `python3 -m http.server 8000` and open
http://localhost:8000/designs/ . The folder starts with an underscore, so Jekyll
does not publish this source; only the generated designs/ folder goes live.
"""
import html
import pathlib
import sys

from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import charts  # noqa: E402
import content as C  # noqa: E402

ROOT = HERE.parent
OUT = ROOT / "designs"

DESIGNS = [
    ("minimal", "Minimal", "Single column, serif, text first. Publications are the main object."),
    ("lab", "Lab", "Hero with tagline and the MegaTabICL scaling chart, cards for Now and News."),
    ("systems", "Systems", "Monospace accents, numbers first, dense two-column layout."),
]
PAGES = [("home", "", "Home"), ("research", "research/", "Research"),
         ("megatabicl", "megatabicl/", "MegaTabICL")]


def authors_html(names, me_class="me"):
    parts = []
    for n in names:
        star = n.endswith("*")
        base = n.rstrip("*")
        txt = html.escape(base) + ("*" if star else "")
        if base == C.ME:
            txt = f'<span class="{me_class}">{txt}</span>'
        parts.append(txt)
    return Markup(", ".join(parts))


def link_href(url, design):
    if url is None:
        return None
    if url == "megatabicl":
        return f"/designs/{design}/megatabicl/"
    return url


def pubs_by_theme():
    groups = []
    for key, label in C.THEMES:
        items = [p for p in C.PUBS if key in p["themes"]]
        oss = [o for o in C.PROJECTS_OSS if key in o["themes"]]
        groups.append({"key": key, "label": label, "pubs": items, "oss": oss})
    return groups


def pubs_by_year():
    years = sorted({p["year"] for p in C.PUBS}, reverse=True)
    return [(y, [p for p in C.PUBS if p["year"] == y]) for y in years]


def main():
    env = Environment(loader=FileSystemLoader(HERE / "templates"),
                      autoescape=select_autoescape(["html"]),
                      trim_blocks=True, lstrip_blocks=True)
    env.globals.update(
        C=C, P=C.PROFILE, designs=DESIGNS, pages=PAGES,
        subs={k: sub for k, sub, _ in PAGES},
        authors=authors_html, href=link_href,
        selected=[p for p in C.PUBS if p["selected"]],
        by_theme=pubs_by_theme(), by_year=pubs_by_year(),
        scaling_chart=Markup(charts.both(charts.scaling_chart, 640, 340, chart_id="scal")),
        scaling_chart_small=Markup(charts.both(charts.scaling_chart, 520, 340, chart_id="scals")),
        cost_chart=Markup(charts.both(charts.cost_chart, 640, 340, chart_id="cost")),
        cost_chart_small=Markup(charts.both(charts.cost_chart, 480, 340, chart_id="costs")),
        legend=Markup(charts.legend_html()), vz_css=Markup(charts.VZ_CSS),
        speed_4gpu=[r for r in C.SPEED if r[1] == 4],
        abl_max=max(r[1] for r in C.ABLATION),
    )
    written = []
    for key, name, _ in DESIGNS:
        for page, sub, title in PAGES:
            tpl = env.get_template(f"{key}/{page}.html")
            out = OUT / key / sub / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(tpl.render(design=key, design_name=name, page=page, page_title=title))
            written.append(out)
    idx = OUT / "index.html"
    idx.write_text(env.get_template("index.html").render())
    written.append(idx)
    for w in written:
        print(f"wrote {w.relative_to(ROOT)} ({w.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
