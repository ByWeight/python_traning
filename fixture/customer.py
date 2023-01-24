from selenium.webdriver.common.by import By


class CustomerHelper:

    def __init__(self, app):
        self.app = app

    def Add(self, customer):
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
        self.driver.switch_to.alert.accept()

    def delete_added_customer(self):
        self.driver = self.app.driver
        # Go to list of customers
        self.driver.find_element(By.CSS_SELECTOR, 'button[ng-click*="showCust()"]').click()
        # Delete first customer
        self.driver.find_element(By.CSS_SELECTOR, 'tbody > tr:nth-child(1) > td:nth-child(5)').click()

