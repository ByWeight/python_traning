from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_AddDeposite():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.implicitly_wait(30)

    def teardown_method(self):
        self.driver.quit()

    def test_test(self):
        self.open_home_page()
        self.chose_name()
        # Authorize success
        self.add_deposite()
        self.logout()

    def logout(self):
        # Logout
        self.driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.box.mainhdr > button.btn.logout').click()

    def add_deposite(self):
        self.driver.find_element(By.CSS_SELECTOR, '.btn-default').click()
        self.driver.find_element(By.CSS_SELECTOR, '.btn:nth-child(2)').click()
        self.driver.find_element(By.CSS_SELECTOR, '.form-control').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CSS_SELECTOR, '.form-control').send_keys('500')
        self.driver.find_element(By.CSS_SELECTOR, '.btn-default').click()

    def chose_name(self):
        # Chose you name
        self.driver.find_element(By.CSS_SELECTOR, 'button[ng-click*="customer()"]').click()
        self.driver.find_element(By.CSS_SELECTOR, "select[class*=ng]").click()
        self.driver.find_element(By.CSS_SELECTOR, '#userSelect > option:nth-child(3)').click()

    def open_home_page(self):
        # Open Homepage
        self.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/')
        self.driver.set_window_size(1920, 1040)


