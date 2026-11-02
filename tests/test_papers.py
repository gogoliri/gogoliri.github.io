"""Paper pages are generated from one _papers/<slug>.md file each, and must
match today's hand-written pages: same Scholar and Open Graph tags, same
visible content, byte-exact BibTeX, plus the shared nav and stylesheets."""

import re

import pytest
import yaml

from helpers import BASELINE, REPO, norm, soup

SLUGS = ["casr", "oxygen-gait", "quality-constrained-coding", "vcm-segmentation"]


def old_new(site, slug):
    return soup(BASELINE / "papers" / f"{slug}.html"), soup(site / "papers" / f"{slug}.html")


@pytest.mark.parametrize("slug", SLUGS)
def test_paper_head_matches_baseline(site, slug):
    old, new = old_new(site, slug)

    def pairs(s):
        return [(m["name"], m["content"])
                for m in s.find_all("meta", attrs={"name": re.compile("^citation_")})]

    def og(s):
        return {m["property"]: m["content"] for m in s.find_all("meta", property=re.compile("^og:"))}

    assert new.title.text == old.title.text
    assert new.find("link", rel="canonical")["href"] == old.find("link", rel="canonical")["href"]
    assert pairs(new) == pairs(old)
    assert og(new) == og(old)
    assert new.find("meta", attrs={"http-equiv": "refresh"}) is None


@pytest.mark.parametrize("slug", SLUGS)
def test_paper_main_and_footer_match_baseline(site, slug):
    old, new = old_new(site, slug)
    if slug == "vcm-segmentation":
        old.select_one("p.award")["class"] = ["award", "candidate"]
    url = f"/papers/{slug}.html"
    assert norm(new.main, url) == norm(old.main, url)
    of, nf = old.select_one(".sheet > footer"), new.select_one(".sheet > footer")
    assert (of is None and nf is None) or norm(nf, url) == norm(of, url)


@pytest.mark.parametrize("slug", SLUGS)
def test_bibtex_byte_exact(site, slug):
    old, new = old_new(site, slug)
    assert new.find("pre", id="bibtex").string == old.find("pre", id="bibtex").string


@pytest.mark.parametrize("slug", SLUGS)
def test_paper_chrome(site, slug):
    _, new = old_new(site, slug)
    assert new.select_one(".sheet nav.site-nav") is not None
    assert new.select_one("a.back") is None
    assert new.find("style") is None
    assert [l["href"] for l in new.select('link[rel="stylesheet"]')] == \
        ["/assets/css/base.css", "/assets/css/paper.css"]
    assert new.find("script", src="/assets/js/copy-bibtex.js") is not None


def test_every_paper_listed_on_home(site):  # Review Focus 2
    listed = soup(site / "index.html").select("section#publications ol.pubs > li")
    assert len(listed) == len(list((REPO / "_papers").glob("*.md")))


def test_award_keys_resolve():  # Review Focus 3
    keys = {a["key"] for a in yaml.safe_load((REPO / "_data/awards.yml").read_text())}
    for f in (REPO / "_papers").glob("*.md"):
        fm = yaml.safe_load(f.read_text().split("---")[1])
        assert fm.get("award") in (None, *keys), f.name
