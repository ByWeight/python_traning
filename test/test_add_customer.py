from model.customer import customer



def test_add(app):
    app.session.Login()
    app.customer.Add(customer(firstname='Denis', lastname='Prokofyev', postcode='K313OK'))
    app.session.Return()


def test_add_one_symbol(app):
    app.session.Login()
    app.customer.Add(customer(firstname='d', lastname='s', postcode='k'))
    app.session.Return()
