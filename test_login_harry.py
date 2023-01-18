from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTest():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test(self):
        self.driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1680, 949)
        self.driver.find_element(By.CSS_SELECTOR, ".center:nth-child(1) > .btn").click()

