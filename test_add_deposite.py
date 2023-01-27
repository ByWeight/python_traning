from deposite import New_deposite
from application import Application


class Test_AddDeposite():
    def setup(self):
        self.app = Application()

    def test_deposite_500(self):
        self.app.open_home_page()
        self.app.chose_name()
        # Authorize success
        self.app.add_deposite(New_deposite(add_deposite='500'))
        self.app.logout()

    def test_deposite_empty(self):
        self.app.open_home_page()
        self.app.chose_name()
        # Authorize success
        self.app.add_deposite(New_deposite(add_deposite='0'))
        self.app.logout()

    def teardown(self):
        self.app.destroy()
