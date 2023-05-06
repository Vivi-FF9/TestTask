import pytest
from Source.users import HarryPotter


@pytest.fixture(scope='session')
def user():
    return HarryPotter
