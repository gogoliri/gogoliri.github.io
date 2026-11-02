"""Regression guards: addresses printed on the CV keep resolving, the /p/
redirect stubs stay byte-identical, and private files never get published."""

import subprocess

import pytest

from helpers import BASE_COMMIT, REPO, page_path

ADDRESSES = ["/", "/p/casr/", "/p/oxygen-gait/", "/p/quality-constrained-coding/",
             "/p/vcm-segmentation/", "/papers/casr.html", "/papers/oxygen-gait.html",
             "/papers/quality-constrained-coding.html", "/papers/vcm-segmentation.html",
             "/papers/casr.pdf", "/papers/casr-award-certificate.jpg", "/papers/casr-cover.tex",
             "/avatar.jpg", "/CNAME"]
SLUGS = ["casr", "oxygen-gait", "quality-constrained-coding", "vcm-segmentation"]
PRIVATE = ["CLAUDE.md", "CLAUDE.html", "docs", "tests", "scripts", "Gemfile",
           "Gemfile.lock", "vendor", ".superpowers", ".claude", "README.html"]


def git_show(path: str) -> bytes:
    return subprocess.run(["git", "show", f"{BASE_COMMIT}:{path}"], cwd=REPO,
                          capture_output=True, check=True).stdout


def test_addresses_resolve(site):
    for a in ADDRESSES:
        assert page_path(site, a).is_file(), a


@pytest.mark.parametrize("slug", SLUGS)
def test_redirect_stub_byte_identical(site, slug):
    built = (site / "p" / slug / "index.html").read_bytes()
    assert built == git_show(f"p/{slug}/index.html")


def test_private_files_not_published(site):
    for p in PRIVATE:
        assert not (site / p).exists(), p


def test_cname_unchanged(site):
    assert (site / "CNAME").read_bytes() == git_show("CNAME")
