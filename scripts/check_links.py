#!/usr/bin/env python3
"""Check links on the built homepage (/) and the /projects/ pages.

Usage (from the repo root):
    bundle exec jekyll build                 # writes _site/
    python3 scripts/check_links.py           # or: python3 scripts/check_links.py path/to/_site

Crawls the homepage and every HTML page under _site/projects/, starting at / and following
internal links that stay inside those folders, and reports:
  - internal links and assets (href, src, CSS url()) that do not resolve to a file in _site
  - in-page anchors (#id) whose target id does not exist
  - href="#" and empty href links
  - empty buttons: <button> or <a class="btn"> without visible text and without aria-label
External links are counted but not fetched. Exits with status 1 if anything is reported.
No dependencies beyond the Python standard library.
"""
import posixpath
import re
import sys
from collections import deque
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

START = "/"
CRAWL = ("/projects/",)   # pages under these prefixes are crawled too
SKIP_SCHEMES = ("mailto:", "tel:")


class Page(HTMLParser):
    """Collects links, asset references, ids and button text from one HTML file."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.refs = []      # (attr, value, line)
        self.ids = set()
        self.buttons = []   # dicts: tag, line, text, aria, href
        self._stack = []    # open <a>/<button> being collected
        self._hidden = 0    # depth inside visually hidden (.vh) spans

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        line = self.getpos()[0]
        if a.get("id"):
            self.ids.add(a["id"])
        for key in ("href", "src"):
            if key in a:
                self.refs.append((key, a[key], line, tag, a.get("rel", "")))
        if "srcset" in a and a["srcset"]:
            for part in a["srcset"].split(","):
                self.refs.append(("srcset", part.strip().split(" ")[0], line, tag, ""))
        cls = a.get("class", "").split()
        if tag == "button" or (tag == "a" and "btn" in cls):
            self._stack.append({"tag": tag, "line": line, "text": "", "aria": a.get("aria-label", ""),
                                "href": a.get("href")})
        if tag == "span" and "vh" in cls:
            self._hidden += 1
        elif self._hidden and tag == "span":
            self._hidden += 1

    def handle_endtag(self, tag):
        if tag == "span" and self._hidden:
            self._hidden -= 1
        if tag in ("a", "button") and self._stack and self._stack[-1]["tag"] == tag:
            self.buttons.append(self._stack.pop())

    def handle_data(self, data):
        if self._stack and not self._hidden:
            self._stack[-1]["text"] += data


def target_file(site, url_path):
    """Map a site URL path to a file in _site, or None if it does not exist."""
    p = unquote(url_path)
    rel = p.lstrip("/")
    cand = site / rel
    if p.endswith("/") or p == "":
        cand = cand / "index.html"
    if cand.is_file():
        return cand
    if (cand / "index.html").is_file():
        return cand / "index.html"
    if not posixpath.splitext(rel)[1] and (site / (rel + ".html")).is_file():
        return site / (rel + ".html")
    return None


def main():
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
    if not (site / START.lstrip("/") / "index.html").is_file():
        sys.exit(f"Not found: {site / START.lstrip('/')}index.html (build the site first)")

    problems, external, checked = [], set(), 0
    parsed = {}

    def parse(path):
        if path not in parsed:
            pg = Page()
            pg.feed(path.read_text(encoding="utf-8"))
            parsed[path] = pg
        return parsed[path]

    queue, seen = deque([START]), set()
    while queue:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)
        f = target_file(site, url)
        page = parse(f)
        where = f.relative_to(site)

        for b in page.buttons:
            if not b["text"].strip() and not b["aria"].strip():
                problems.append(f"{where}:{b['line']}: empty <{b['tag']}> button")
            if b["tag"] == "a" and not (b["href"] or "").strip():
                problems.append(f"{where}:{b['line']}: button link without href")

        for attr, val, line, tag, rel in page.refs:
            val = (val or "").strip()
            if attr == "href" and val in ("", "#"):
                problems.append(f'{where}:{line}: href="{val}" on <{tag}>')
                continue
            if val.startswith(SKIP_SCHEMES):
                continue
            if val.lower().startswith("javascript:"):
                problems.append(f"{where}:{line}: javascript: link")
                continue
            parts = urlsplit(val)
            if parts.scheme in ("http", "https") or val.startswith("//"):
                external.add(val)
                continue
            checked += 1
            if val.startswith("#"):
                if val[1:] not in page.ids:
                    problems.append(f"{where}:{line}: anchor {val} has no matching id")
                continue
            abs_url = urljoin(url, val)
            path = urlsplit(abs_url).path
            tf = target_file(site, path)
            if tf is None:
                problems.append(f"{where}:{line}: broken internal {attr} -> {val}")
                continue
            frag = urlsplit(abs_url).fragment
            if frag and tf.suffix == ".html" and frag not in parse(tf).ids:
                problems.append(f"{where}:{line}: {val}: no id '{frag}' in target page")
            if tf.suffix == ".css":
                css = tf.read_text(encoding="utf-8")
                for m in re.finditer(r"url\(\s*['\"]?([^'\")]+)['\"]?\s*\)", css):
                    u = m.group(1)
                    if u.startswith(("data:", "http:", "https:", "//")):
                        continue
                    checked += 1
                    if target_file(site, urlsplit(urljoin(path, u)).path) is None:
                        problems.append(f"{tf.relative_to(site)}: broken url() -> {u}")
            if tag == "a" and (path == START or path.startswith(CRAWL)) and tf.suffix == ".html":
                queue.append(path)

    print(f"Pages crawled: {len(seen)}  internal refs checked: {checked}  external links (not fetched): {len(external)}")
    for p in sorted(set(problems)):
        print("PROBLEM", p)
    print("OK: no problems found" if not problems else f"{len(set(problems))} problem(s)")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
