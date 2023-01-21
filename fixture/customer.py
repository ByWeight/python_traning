from selenium.webdriver.common.by import By


class CustomerHelper:

    def __init__(self, app):
        self.app = app

    def Add_customer(self, customer):
        # Add customer
        self.driver = self.app.driver
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
