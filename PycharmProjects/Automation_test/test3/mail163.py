from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://mail.163.com/")
#登录!!要先定位到登录框frame！！！！！！！！！！！！！！！
def login():
    #定位到登录框
    ss = driver.find_element_by_id("x-URS-iframe")
    driver.switch_to.frame(ss)
    #定位到邮箱账号输入框
    email = driver.find_element_by_name('email')
    email.send_keys('13760261486')
    #定位到密码输入框
    driver.find_element_by_name('password').send_keys('hw13760261486')
    driver.find_element_by_xpath('//*[@id="dologin"]').click()
    time.sleep(3)
def logout():
    driver.find_element_by_xpath('//*[@id="_mail_component_43_43"]/a').click()
login()
#logout()
#点击【未读邮件】
#driver.find_element_by_xpath('//*[@class="nui-ico gWel-ico gWel-ico-unread-bottom"]').click()
#点击收件箱
driver.find_element_by_xpath('//*[@class="js-component-tree nui-tree-item"]').click()
#
time.sleep(3)
driver.find_element_by_xpath('//*[@class="nui-chk cS0"]').click()
#定位框,,没有frame，不用定义框。。也可以
#driver.find_element_by_xpath('//*[@role="toolbar"]')
#点击举报按钮
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/header/div/div[3]/div[1]/span').click()