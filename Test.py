from selenium import webdriver
from selenium.webdriver.common.by import By


class Testloginharry:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_loginharry(self):
        self.driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/")
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CSS_SELECTOR, ".center:nth-child(1) > .btn").click()
        self.driver.find_element(By.ID, "userSelect").click()
        dropdown = self.driver.find_element(By.ID, "userSelect")
        dropdown.find_element(By.XPATH, "//option[. = 'Harry Potter']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
