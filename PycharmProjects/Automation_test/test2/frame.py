from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
file_path = os.path.abspath('frame.html')
#file_path = 'file:///' + os.path.abspath('frame.html')#两个一样
#os.path.abspath获取工作目录下绝对路劲
driver.get(file_path)
'''
driver.switch_to.frame("if")
driver.find_element_by_id("kw").send_keys('selenium')
driver.find_element_by_id("su").click()'''
#switch_to.frame()默认可以直接取表单的id或name属性。如果iframe没有可用的id和name属性则可以通过下面方式进行定位
#driver.quit()
xf = driver.find_element_by_xpath('//*[@id="if"]')
driver.switch_to.frame(xf)
driver.find_element_by_id("kw").send_keys('selenium')
driver.find_element_by_id("su").click()
#switch_to.parent_content()方法跳出当前一级表单
driver.switch_to.parent_frame()
#switch_to.default_content()跳回最外层的页面
driver.switch_to.default_content()
time.sleep(5)