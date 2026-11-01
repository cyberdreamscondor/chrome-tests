"""Shared fixtures for the Chrome autotests.

Layout of this suite:

    tests/menus/test_app_menu_closes.py
    configs/menus/test_app_menu_closes.yaml

A test may have a YAML config at the mirrored path. The framework derives that
path itself, so a test never says where its data lives. A test needing no data
simply has no config file.
"""

from pathlib import Path

import pytest
from chrome import Chrome
from yaml_config import load_test_config

# pytest rewrites `assert` statements to produce its detailed output, but only
# in test modules and conftest files. Without this line, an assertion failing
# inside chrome_checks would report a bare "AssertionError" and lose the
# values. Must run before any test module imports that module, and pytest
# loads this file before collecting tests, so here is early enough.
pytest.register_assert_rewrite("chrome_checks")

SUITE_ROOT = Path(__file__).parent
TESTS_ROOT = SUITE_ROOT / "tests"
CONFIGS_ROOT = SUITE_ROOT / "configs"


@pytest.fixture
def config(request):
    """The YAML config belonging to the test being run, empty if absent."""
    return load_test_config(request.path, TESTS_ROOT, CONFIGS_ROOT)


@pytest.fixture
def chrome(config):
    """A freshly launched Chrome, closed again when the test ends."""
    overrides = dict(config.section("chrome"))
    with Chrome.launch(**overrides) as browser:
        yield browser
