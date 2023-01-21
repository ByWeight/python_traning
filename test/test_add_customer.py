import pytest
from fixture.application import Application
from model.customer import customer


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add(app):
    app.session.Login()
    app.customer.Add_customer(customer(firstname='Denis', lastname='Prokofyev', postcode='K313OK'))
    #app.Check(text_alert, text_alert_error)


def test_add_one_symbol(app):
    app.session.Login()
    app.customer.Add_customer(customer(firstname='d', lastname='s', postcode='k'))
    #app.Check(text_alert, text_alert_error)

