


def test_delete_added_customer(app):
    app.session.Login()
    app.customer.delete_added_customer()
    app.session.Return()


