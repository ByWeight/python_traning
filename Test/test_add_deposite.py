from Git.python_traning.Model.deposite import New_deposite




def test_deposite_500(app):
    app.open_home_page()
    app.chose_name()
    # Authorize success
    app.add_deposite(New_deposite(add_deposite='500'))
    app.session.logout()


def test_deposite_empty(app):
    app.open_home_page()
    app.chose_name()
    # Authorize success
    app.add_deposite(New_deposite(add_deposite='0'))
    app.session.logout()
