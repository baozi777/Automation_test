from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Page(object):
    '''
    基础了，用于页面对象的继承
    '''
    login_url = 'https://mail.163.com/'
    def __init__(self,selenium_driver,base_url=login_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
    def on_page(self):
        return self.driver.current_url_ == (self.base_url + self.url)
    def _open(self,url):
        url_ = self.base_url + url
        self.driver.get(url_)
        assert self.on_page(),'Did not land on %s' % url_
    def open(self):
        self._open(self.url)
    def find_element(self,*loc):
        return self.driver.find_element(*loc)


class LoginPage(Page):
    '''
    163邮箱登录页面模型
    '''
    url = '/'
    #定位器
    #frame1 = (By.ID,'x-URS-ifram')
    # iframe1 = (By.XPATH, "//div/iframe[@id='x-URS-iframe']")
    username_loc = (By.XPATH,"//input[@placeholder='邮箱账号或手机号']")
    password_loc =  (By.XPATH,"//input[@placeholder='密码']")
    submit_loc = (By.XPATH, "//a[contains(text(), '登录')]")
    #Action
    def type_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)
    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)
    def submit(self):
        self.find_element(*self.submit_loc).click()

def test_user_login(driver,username,password):
    '''
    测试获取的用户名、密码是否可以登录
    '''
    login_page = LoginPage(driver)
    login_page.open()
    # login_page.switch_to_iframee()
    driver.switch_to.frame(driver.find_element_by_id("x-URS-iframe"))
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()
def main():
    try:
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        # ss = driver.find_element_by_id("x-URS-iframe")
        # driver.switch_to.frame(ss)
        username = '13760261486'
        password = 'hw666666'
        test_user_login(driver,username,password)
        sleep(3)
        text = driver.find_element_by_xpath("//span[contains(text(),'13760261486@163.com']")
    finally:
        #关闭浏览器窗口
        driver.close()
if __name__ == '__main__':
    main()
