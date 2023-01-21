from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)


    def destroy(self):
        self.driver.quit()

    #def Check(self, text_alert, text_alert_error):
        # Check
        #if text_alert == text_alert_error:
            #print('Ошибка. Пользователь уже существует')
        #else:
            #print('Успех. Пользователь добавлен')

    def Add_customer(self, customer):
        # Add customer
        self.driver.find_element(By.CSS_SELECTOR, 'button[ng-click*="addCust"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="First"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="First"]').send_keys(customer.firstname)
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="Last"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="Last"]').send_keys(customer.lastname)
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="Post"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="Post"]').send_keys(customer.postcode)
        self.driver.find_element(By.CSS_SELECTOR, 'button[type*="submit"]').click()
        text_alert = self.driver.switch_to.alert.text
        text_alert_error = 'Please check the details. Customer may be duplicate.'
        assert self.driver.switch_to.alert.text == text_alert
        return text_alert, text_alert_error

    def Open_site(self):
        # Open site
        self.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/')
