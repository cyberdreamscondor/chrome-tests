import pytest
from chrome import Chrome


@pytest.fixture
def chrome():
    with Chrome.launch() as browser:
        yield browser
