import pytest

from helpers import REPO, build


@pytest.fixture(scope="session")
def site():
    """The repository built once per test session with GitHub Pages' Jekyll."""
    return build(REPO)
