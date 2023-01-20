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
        self.Open_site()
        self.Login()
        text_alert, text_alert_error = self.Add_customer(firstname='Denis', lastname='Prokofyev', postcode='K313OK')
        self.Check(text_alert, text_alert_error)

        def test_add(self):
            self.Open_site()
            self.Login()
            text_alert, text_alert_error = self.Add_customer(firstname='', lastname='', postcode='')
            self.Check(text_alert, text_alert_error)

    def Check(self, text_alert, text_alert_error):
        # Check
        if text_alert == text_alert_error:
            print('Ошибка. Пользователь уже существует')
        else:
            print('Успех. Пользователь добавлен')

    def Add_customer(self, customer):
        # Add customer
        self.driver.find_element(By.CSS_SELECTOR, 'button[ng-click*="addCust"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="First"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="First"]').send_keys(firstname)
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="Last"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="Last"]').send_keys(lastname)
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="Post"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="Post"]').send_keys(postcode)
        self.driver.find_element(By.CSS_SELECTOR, 'button[type*="submit"]').click()
        text_alert = self.driver.switch_to.alert.text
        text_alert_error = 'Please check the details. Customer may be duplicate.'
        assert self.driver.switch_to.alert.text == text_alert
        return text_alert, text_alert_error

    def Login(self):
        # Login
        self.driver.find_element(By.CSS_SELECTOR, 'button[ng-click*="manager"]').click()

    def Open_site(self):
        # Open site
        self.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/')





