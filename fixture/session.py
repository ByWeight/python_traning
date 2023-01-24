from selenium.webdriver.common.by import By

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def Login(self):
        self.app.Open_site()
        # Login
        self.app.driver.find_element(By.CSS_SELECTOR, 'button[ng-click*="manager"]').click()

    def Return(self):
        # Return
        self.app.driver.find_element(By.CSS_SELECTOR, 'button[ng-click*="home()"]').click()