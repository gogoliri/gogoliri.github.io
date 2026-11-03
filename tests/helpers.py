"""Shared helpers for the site tests: build with Jekyll, locate pages, and
reduce HTML elements to a canonical string so a regenerated page can be
compared with the frozen copy of today's hand-written one."""

import copy
import html
import re
import shutil
import subprocess
from pathlib import Path
from urllib.parse import urljoin, urlsplit

from bs4 import BeautifulSoup, Comment, NavigableString, Tag

REPO = Path(__file__).resolve().parent.parent
BASELINE = REPO / "tests" / "baseline"
BASE_COMMIT = "6558488"
ORIGIN = "https://khoaphamdinh.com"

BLOCK = ("p|li|ul|ol|div|section|h[1-6]|header|footer|main|article|nav|pre|hr|br"
         "|table|thead|tbody|tr|td|th|script")
_BLOCK_EDGE = re.compile(r"\s*(</?(?:%s)\b[^>]*>)\s*" % BLOCK)


def build(src: Path) -> Path:
    """Build `src` with scripts/build.sh; return its _site directory."""
    res = subprocess.run([str(REPO / "scripts" / "build.sh"), str(src)],
                         capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"jekyll build failed for {src}:\n{res.stdout}\n{res.stderr}")
    return Path(src) / "_site"


def copy_repo(dst: Path) -> Path:
    """Copy the site sources (no git, build output, gems or private notes) to `dst`."""
    shutil.copytree(REPO, dst, ignore=shutil.ignore_patterns(
        ".git", "_site", ".jekyll-cache", "vendor", ".superpowers", "docs", "tests",
        "__pycache__", ".pytest_cache"))
    return dst


def page_path(site: Path, url: str) -> Path:
    rel = url.lstrip("/")
    if rel == "" or rel.endswith("/"):
        rel += "index.html"
    return Path(site) / rel


def soup(path: Path) -> BeautifulSoup:
    return BeautifulSoup(Path(path).read_text(encoding="utf-8"), "html.parser")


def _resolve(value: str, page_url: str) -> str:
    absolute = urljoin(ORIGIN + page_url, value)
    if absolute.startswith(ORIGIN + "/") or absolute == ORIGIN:
        parts = urlsplit(absolute)
        absolute = (parts.path or "/") + (f"?{parts.query}" if parts.query else "") \
            + (f"#{parts.fragment}" if parts.fragment else "")
    return absolute


def _serialize(node, in_pre: bool) -> str:
    if isinstance(node, NavigableString):
        text = html.escape(str(node), quote=False)
        return text if in_pre else re.sub(r"\s+", " ", text)
    attrs = []
    for key in sorted(node.attrs):
        val = node.attrs[key]
        if isinstance(val, list):
            val = " ".join(sorted(val))
        attrs.append(f' {key}="{html.escape(str(val))}"')
    pre = in_pre or node.name == "pre"
    inner = "".join(_serialize(c, pre) for c in node.children)
    return f"<{node.name}{''.join(attrs)}>{inner}</{node.name}>"


def norm(el: Tag, page_url: str) -> str:
    """Canonical form of `el`: comments dropped, links resolved to site paths,
    attributes and class tokens sorted, whitespace collapsed outside <pre> and
    trimmed around block tags."""
    el = copy.copy(el)
    for c in el.find_all(string=lambda s: isinstance(s, Comment)):
        c.extract()
    for tag in [el, *el.find_all(True)]:
        for attr in ("href", "src"):
            if tag.has_attr(attr):
                tag[attr] = _resolve(tag[attr], page_url)
    return _BLOCK_EDGE.sub(r"\1", _serialize(el, False)).strip()
