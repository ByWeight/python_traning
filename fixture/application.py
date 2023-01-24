from selenium import webdriver
from fixture.customer import CustomerHelper
from fixture.session import SessionHelper


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
