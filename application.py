from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.implicitly_wait(30)

    def logout(self):
        wd = self.driver
        # Logout
        wd.find_element(By.CSS_SELECTOR, 'button[ng-click*="byebye()"]').click()

    def add_deposite(self, deposite):
        wd = self.driver
        wd.find_element(By.CSS_SELECTOR, '.btn-default').click()
        wd.find_element(By.CSS_SELECTOR, '.btn:nth-child(2)').click()
        wd.find_element(By.CSS_SELECTOR, '.form-control').click()
        wd.implicitly_wait(30)
        wd.find_element(By.CSS_SELECTOR, '.form-control').send_keys(deposite.add_deposite)
        wd.find_element(By.CSS_SELECTOR, '.btn-default').click()

    def chose_name(self):
        wd = self.driver
        # Chose you name
        wd.find_element(By.CSS_SELECTOR, 'button[ng-click*="customer()"]').click()
        wd.find_element(By.CSS_SELECTOR, "select[class*=ng]").click()
        wd.find_element(By.CSS_SELECTOR, '#userSelect > option:nth-child(3)').click()

    def open_home_page(self):
        wd = self.driver
        # Open Homepage
        wd.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/')
        wd.set_window_size(1920, 1040)

    def destroy(self):
        wd = self.driver
        wd.quit()
