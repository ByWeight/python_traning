from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_harry_deposit():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.implicitly_wait(30)

    def teardown_method(self, method):
        self.driver.quit()

    def test_test(self):
        self.Open_app()
        self.Login()
        self.Deposit(Summ='100')
        self.Check()

    def test_test(self):
        self.Open_app()
        self.Login()
        self.Deposit(Summ='')
        self.Check()


    def Check(self):
        # Check success deposit
        check = self.driver.find_element(By.CSS_SELECTOR, 'span[class*=error]').text
        check_true = ('Deposit Successful')
        if check == check_true:
            print('Тест пройден')
        else:
            print('Тест провален')

    def Deposit(self, Summ):
        # Start deposit
        self.driver.find_element(By.CSS_SELECTOR, '.btn:nth-child(2)').click()
        self.driver.find_element(By.CSS_SELECTOR, '.form-control').click()
        self.driver.find_element(By.CSS_SELECTOR, '.form-control').send_keys(Summ)
        self.driver.find_element(By.CSS_SELECTOR, '.btn-default').click()

    def Login(self):
        # Login
        self.driver.find_element(By.CSS_SELECTOR, 'button[ng-click*="customer()"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'select[class*=ng]').click()
        self.driver.find_element(By.CSS_SELECTOR, '#userSelect > option:nth-child(3)').click()
        self.driver.find_element(By.CSS_SELECTOR, '.btn-default').click()

    def Open_app(self):
        # Open app
        self.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/')
