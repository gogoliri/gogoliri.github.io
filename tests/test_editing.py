"""Editing the site means editing data, not HTML: a temp copy of the site gets
one extra entry in every list file, is built once, and each entry must show
up in its section."""

import pytest

from helpers import build, copy_repo, page_path, soup

SENTINELS = {  # file: (yaml snippet appended, marker, section id, page)
    "news.yml": ('- date: "Jan 2099"\n  text: "SENTINEL-news"\n', "SENTINEL-news", "news", "/"),
    "standardization.yml": ('- id: std-99\n  label: "S99."\n  title: "SENTINEL-std"\n  venue: "v"\n',
                            "SENTINEL-std", "standardization", "/cv/"),
    "experience.yml": ('- title: "SENTINEL-exp"\n  when: "w"\n  org: "o"\n  bullets: ["b"]\n',
                       "SENTINEL-exp", "experience", "/cv/"),
    "education.yml": ('- title: "SENTINEL-edu"\n  when: "w"\n  org: "o"\n  bullets: ["b"]\n',
                      "SENTINEL-edu", "education", "/cv/"),
    "teaching.yml": ('  - code: "X.0"\n    name: "SENTINEL-teach"\n    terms: "t"\n',
                     "SENTINEL-teach", "teaching", "/cv/"),
    "awards.yml": ('- key: sentinel\n  name: "SENTINEL-award"\n  when: "2099"\n',
                   "SENTINEL-award", "awards", "/cv/"),
    "skills.yml": ('- key: "k"\n  val: "SENTINEL-skill"\n', "SENTINEL-skill", "skills", "/cv/"),
    "languages.yml": ('- key: "k"\n  val: "SENTINEL-lang"\n', "SENTINEL-lang", "languages", "/cv/"),
}


# A new paper with no `group:` (falls back to Peer-reviewed), a DOI, an award
# reference and the DOI switch turned on.
SENTINEL_PAPER = """---
doi_redirect: https://doi.org/10.0000/sentinel
number: 99
title: SENTINEL paper
description: d
authors:
  - name: X
    me: true
doi: 10.0000/sentinel
award: mmsp2026-best-student-paper
abstract: a
bibtex: "@misc{s}"
citation:
  - [citation_title, SENTINEL paper]
---
"""


@pytest.fixture(scope="session")
def edited_site(tmp_path_factory):
    src = copy_repo(tmp_path_factory.mktemp("edited") / "site")
    for name, (snippet, *_) in SENTINELS.items():
        path = src / "_data" / name
        text = path.read_text(encoding="utf-8")
        path.write_text(text + ("" if text.endswith("\n") else "\n") + snippet, encoding="utf-8")
    (src / "_papers").mkdir(exist_ok=True)
    (src / "_papers" / "zz-sentinel.md").write_text(SENTINEL_PAPER, encoding="utf-8")
    return build(src)


@pytest.mark.parametrize("file", SENTINELS)
def test_data_entry_renders_in_its_section(edited_site, file):
    _, marker, sec, url = SENTINELS[file]
    assert marker in soup(page_path(edited_site, url)).find("section", id=sec).text


def test_new_paper_file_renders_everywhere(edited_site):
    home = soup(page_path(edited_site, "/"))
    entry = home.select_one("li#pub-99")
    assert entry is not None
    assert entry.find_parent("ol") is home.select_one("li#pub-3").find_parent("ol")
    assert [a["href"] for a in entry.select("a.chip")][1] == "https://doi.org/10.0000/sentinel"
    assert entry.select_one("span.badge").text == "Best Student Paper Award"

    page = soup(page_path(edited_site, "/papers/zz-sentinel.html"))
    metas = page.head.find_all("meta")
    assert metas[0].get("charset") == "utf-8"
    assert metas[1].get("http-equiv") == "refresh"
    assert metas[1]["content"] == "0; url=https://doi.org/10.0000/sentinel"
    assert page.select_one("p.award strong").text == "Best Student Paper Award."
