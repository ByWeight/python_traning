from selenium import webdriver
from selenium.webdriver.common.by import By
from Git.python_traning.Fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)

    def add_deposite(self, deposite):
        self.driver.find_element(By.CSS_SELECTOR, '.btn-default').click()
        self.driver.find_element(By.CSS_SELECTOR, '.btn:nth-child(2)').click()
        self.driver.find_element(By.CSS_SELECTOR, '.form-control').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CSS_SELECTOR, '.form-control').send_keys(deposite.add_deposite)
        self.driver.find_element(By.CSS_SELECTOR, '.btn-default').click()

    def chose_name(self):
        # Chose you name
        self.driver.find_element(By.CSS_SELECTOR, 'button[ng-click*="customer()"]').click()
        self.driver.find_element(By.CSS_SELECTOR, "select[class*=ng]").click()
        self.driver.find_element(By.CSS_SELECTOR, '#userSelect > option:nth-child(3)').click()



    def destroy(self):
        self.driver.quit()
