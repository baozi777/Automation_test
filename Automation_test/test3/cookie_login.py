from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://mail.163.com")
driver.find_element_by_class_name("j-inputtext dlemail").send_keys('13760261486')
driver.find_element_by_xpath('//*[@id="auto-id-1528941854213"]').send_keys('hw163.wangyi')
driver.find_element_by_xpath('//*[@id="dologin"]').click()
cookie = driver.get_cookies()
print(cookie)