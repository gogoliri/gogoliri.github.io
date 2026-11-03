"""Home and CV pages: every section renders exactly as it did on the old
single page (Languages and Technical skills are gone from the CV), the
shared nav marks the current page, and styles come only from the shared
stylesheets."""

import json
import re

import pytest
import yaml

from helpers import BASELINE, REPO, norm, page_path, soup

HOME = ["about", "news", "publications", "standardization"]
CV = ["education", "experience", "teaching", "awards"]
WHERE = {**{s: "/" for s in HOME}, **{s: "/cv/" for s in CV}}
# Rows added since the baseline was frozen, as (section, position, row text start).
# Each must sit at its position; it is then dropped before comparing with the baseline.
ADDED = [("awards", 1, "Candidate for Best Paper Award, IEEE\xa0ISM\xa02025")]


@pytest.mark.parametrize("sec", HOME + CV)
def test_section_matches_baseline(site, sec):
    new = soup(page_path(site, WHERE[sec])).find("section", id=sec)
    old = soup(BASELINE / "index.html").find("section", id=sec)
    assert new is not None, f"section #{sec} missing from {WHERE[sec]}"
    for s, pos, start in ADDED:
        if s == sec:
            rows = new.select("ul > li")
            assert rows[pos].get_text().strip().startswith(start), f"{start!r} not row {pos} of #{sec}"
            rows[pos].decompose()
    assert norm(new, WHERE[sec]) == norm(old, "/")


@pytest.mark.parametrize("sec", ["languages", "skills"])
def test_section_removed(site, sec):
    assert not (REPO / "_data" / f"{sec}.yml").exists()
    for url in ["/", "/cv/"]:
        s = soup(page_path(site, url))
        assert s.find(id=sec) is None, url
        assert all(a["href"] != f"#{sec}" for a in s.select("nav.toc a")), url


def test_section_order(site):
    for url, ids in [("/", HOME), ("/cv/", CV)]:
        assert [s["id"] for s in soup(page_path(site, url)).select("main section.sec")] == ids


@pytest.mark.parametrize("url,key", [("/", "Home"), ("/cv/", "CV"), ("/blog/", "Blog")])
def test_nav_marks_current(site, url, key):
    links = soup(page_path(site, url)).select("nav.site-nav a")
    assert [(a.text, a["href"]) for a in links] == [("Home", "/"), ("CV", "/cv/"), ("Blog", "/blog/")]
    assert [a.text for a in links if a.get("aria-current") == "page"] == [key]


def test_shared_stylesheets_only(site):
    for url in ["/", "/cv/"]:
        s = soup(page_path(site, url))
        assert s.find("style") is None, url
        assert [l["href"] for l in s.select('link[rel="stylesheet"]')] == \
            ["/assets/css/base.css", "/assets/css/site.css"], url


def test_home_head_matches_baseline(site):
    old, new = soup(BASELINE / "index.html"), soup(page_path(site, "/"))

    def head(s):
        return (s.title.text,
                s.find("link", rel="canonical")["href"],
                s.find("link", rel="icon")["href"],
                {n: s.find("meta", attrs={"name": n})["content"]
                 for n in ["description", "author", "color-scheme", "theme-color"]},
                {m["property"]: m["content"] for m in s.find_all("meta", property=re.compile("^og:"))},
                json.loads(s.find("script", type="application/ld+json").string))

    assert head(new) == head(old)


def test_cv_head(site):
    s = soup(page_path(site, "/cv/"))
    assert s.title.text == "CV — Khoa Pham-Dinh"
    assert s.find("link", rel="canonical")["href"] == "https://khoaphamdinh.com/cv/"


def test_identity_rail_on_every_page(site):
    old = norm(soup(BASELINE / "index.html").select_one("ul.contact"), "/")
    for url in ["/", "/cv/"]:
        new = soup(page_path(site, url)).select_one("ul.contact")
        assert new is not None and norm(new, url) == old, url


def test_print_rules():
    css = (REPO / "assets/css/site.css").read_text()
    print_block = css[css.index("@media print"):]
    assert ".site-nav" in print_block and 'a[href^="/papers/"]' in print_block


def test_blog_empty_and_silent(site):
    main = soup(page_path(site, "/blog/")).main
    assert main.select("section#posts ul.rows > li") == []
    assert " ".join(main.get_text().split()) == "Blog"


def test_config_timezone():  # Review Focus 1
    assert yaml.safe_load((REPO / "_config.yml").read_text())["timezone"] == "Europe/Helsinki"
