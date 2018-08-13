from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://www.126.com")
print('Before login================')
title = driver.title
print(title)
now_url = driver.current_url
print(now_url)
#above = driver.find_element_by_xpath("//*[@id='lbNormal']")
#ActionChains(driver).move_to_element(above).perform()
driver.find_element_by_xpath("//input[@type='text' and @name='email']").clear()
#126定位不到。。。。。。。。。。。。。？？？
driver.find_element_by_xpath("//input[@type='text' and @name='email']").send_keys("13760261486")
#driver.find_element_by_xpath("//*[@id='auto-id-1528272035596']").clear()
#driver.find_element_by_xpath("//*[@id='auto-id-1528272035596']").send_keys("62516078023")
#driver.find_element_by_xpath("//*[@id=dologin]").click()