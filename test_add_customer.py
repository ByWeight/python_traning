from selenium import webdriver
from selenium.webdriver.common.by import By

class test_add_customer():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.implicitly_wait(30)

    def teardown_method(self, method):
        self.driver.quit()

    def test_add_customer(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[ng-click*="manager"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'button[ng-click*="addCust"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="First"]').click()
