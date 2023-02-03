from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def logout(self):
        # Logout
        self.app.driver.find_element(By.CSS_SELECTOR, 'button[ng-click*="byebye()"]').click()