from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        # Open Homepage
        self.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/')
        self.driver.set_window_size(1920, 1040)

    def logout(self):
        # Logout
        self.app.driver.find_element(By.CSS_SELECTOR, 'button[ng-click*="byebye()"]').click()