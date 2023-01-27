from deposite import New_deposite
from application import Application


class Test_AddDeposite():
    def setUp(self):
        self.app = Application()

    def test_deposite_500(self):
        self.open_home_page()
        self.chose_name()
        # Authorize success
        self.add_deposite(New_deposite(add_deposite='500'))
        self.logout()

    def test_deposite_empty(self):
        self.open_home_page()
        self.chose_name()
        # Authorize success
        self.add_deposite(New_deposite(add_deposite='0'))
        self.logout()


