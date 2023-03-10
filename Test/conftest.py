from Git.python_traning.Fixture.application import Application
import pytest


@pytest.fixture(scope='session')
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
