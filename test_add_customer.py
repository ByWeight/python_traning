from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_add_customer():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.implicitly_wait(30)

    def teardown_method(self, method):
        self.driver.quit()

    def test_add(self):
        self.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/')
        self.Login()
        self.Add_customer(firstname='Denis', lastname='Prokofyev', postcode='K313OK')
        text_alert, text_alert_error = self.Submit_popup()
        self.Check(text_alert, text_alert_error)

    def test_add(self):
        self.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/')
        self.Login()
        self.Add_customer(firstname='', lastname='', postcode='')
        text_alert, text_alert_error = self.Submit_popup()
        self.Check(text_alert, text_alert_error)

    def Check(self, text_alert, text_alert_error):
        # Check
        if text_alert == text_alert_error:
            print('Ошибка. Пользователь уже существует')
        else:
            print('Успех. Пользователь добавлен')

    def Submit_popup(self):
        # Submit popup alert
        text_alert = self.driver.switch_to.alert.text
        text_alert_error = 'Please check the details. Customer may be duplicate.'
        assert self.driver.switch_to.alert.text == text_alert
        return text_alert, text_alert_error

    def Add_customer(self, firstname, lastname, postcode):
        # Add customer
        self.driver.find_element(By.CSS_SELECTOR, 'button[ng-click*="addCust"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="First"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="First"]').send_keys(firstname)
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="Last"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="Last"]').send_keys(lastname)
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="Post"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="Post"]').send_keys(postcode)
        self.driver.find_element(By.CSS_SELECTOR, 'button[type*="submit"]').click()

    def Login(self):
        # login
        self.driver.find_element(By.CSS_SELECTOR, 'button[ng-click*="manager"]').click()





