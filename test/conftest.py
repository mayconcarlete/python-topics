import pytest

@pytest.fixture(scope='function')
def printa():
    print('hello test world')