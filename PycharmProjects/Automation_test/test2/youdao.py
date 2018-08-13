from selenium import webdriver
from  selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Firefox()
driver.get('https://lobby.fg.blizzmi.cn/')
driver.find_element_by_xpath('/html/body/div/div[1]/div[5]/img').click()
driver.find_element_by_xpath('//*[@id="username"]').send_keys('unittest')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('111111')
driver.find_element_by_xpath('//*[@id="login-reg"]').click()
time.sleep(2)
#新的语法：driver.switch_to.alert(注，后面不需要加括号）
#切换到alert弹窗
alert =driver.switch_to.alert
#点击确定
alert.accept()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[3]/img').click()

