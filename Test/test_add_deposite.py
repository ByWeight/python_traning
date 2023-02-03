from Git.python_traning.Model.deposite import New_deposite
from Git.python_traning.Fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_deposite_500(app):
    app.open_home_page()
    app.chose_name()
    # Authorize success
    app.add_deposite(New_deposite(add_deposite='500'))
    app.logout()


def test_deposite_empty(app):
    app.application.open_home_page()
    app.application.chose_name()
    # Authorize success
    app.application.add_deposite(New_deposite(add_deposite='0'))
    app.application.logout()
