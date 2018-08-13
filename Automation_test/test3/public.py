import time
from selenium import webdriver
class Login():
    #登录
    def user_login(self,driver,username,password):
        #定位到登录框
        ss = driver.find_element_by_id("x-URS-iframe")
        driver.switch_to.frame(ss)
        #定位到邮箱账号输入框
        driver.find_element_by_name('email').clear()
        email = driver.find_element_by_name('email')
        email.send_keys(username)
        #
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_xpath('//*[@id="dologin"]').click()
        time.sleep(3)
    #退出
    '''def user_logout(self,driver):
        driver.find_element_by_xpath('//*[@id="_mail_component_43_43"]/a').click()
        driver.quit()'''