from selenium import webdriver
from test3.public import Login

class LoginTest():
    def __init__(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https://mail.163.com/")
        self.driver = driver

    def test_admin_login(self):
        username = '13760261486'
        password = 'hw13760261486'
        Login().user_login(self.driver,username,password)
        self.driver.quit()
LoginTest().test_admin_login()