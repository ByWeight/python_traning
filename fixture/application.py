from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper
from fixture.customer import CustomerHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.customer = CustomerHelper(self)


    def destroy(self):
        self.driver.quit()


    def Open_site(self):
        # Open site
        self.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/')
