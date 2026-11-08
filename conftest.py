from pathlib import Path

import pytest
from chrome import Chrome
from yaml_config import load_test_config

pytest.register_assert_rewrite("chrome_checks")

SUITE_ROOT = Path(__file__).parent
TESTS_ROOT = SUITE_ROOT / "tests"
CONFIGS_ROOT = SUITE_ROOT / "configs"


@pytest.fixture
def test_input(request):
    """The YAML config belonging to the test being run, empty if absent."""
    return load_test_config(request.path, TESTS_ROOT, CONFIGS_ROOT)


@pytest.fixture
def chrome(test_input):
    """A freshly launched Chrome, closed again when the test ends."""
    overrides = dict(test_input.chrome)
    with Chrome.launch(**overrides) as browser:
        yield browser
