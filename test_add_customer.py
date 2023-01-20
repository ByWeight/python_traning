from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from customer import customer
from application import Application

def app():

class Test_add_customer():
    def setup_method(self):
        self.app = Application()

    def teardown_method(self):
        self.app.destroy()


    def test_add(self):
        self.app.Login()
        text_alert, text_alert_error = self.app.Add_customer(customer(firstname='Denis', lastname='Prokofyev', postcode='K313OK'))
        self.app.Check(text_alert, text_alert_error)

    def test_add_one_symbol(self):
        self.app.Login()
        text_alert, text_alert_error = self.app.Add_customer(customer(firstname='d', lastname='s', postcode='k'))
        self.app.Check(text_alert, text_alert_error)

