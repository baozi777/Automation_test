from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
import logging
logging.basicConfig(level=logging.DEBUG)
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
#获取输入框的尺寸
size = driver.find_element_by_id('kw').size
print(size)
#返回百度页面底部的备信息
text = driver.find_element_by_id('cp').text
print(text)
#获取元素的属性值，可以是id、name、type或其他任意属性
attribute = driver.find_element_by_id('kw').get_attribute('type')
print(attribute)
#返回的元素的结果是否可见，返回结果为TURE或False
result = driver.find_element_by_id('cp').is_displayed()
print(result)
driver.find_element_by_xpath("//*[@id='kw']").send_keys('selenuimm')
#Keys.BACK_SPACE删除多输入的一个m
driver.find_element_by_xpath("//*[@id='kw']").send_keys(Keys.BACK_SPACE)
time.sleep(5)
#设置浏览器窗口大小
#driver.set_window_size(600,600)
#通过javascript设置浏览器窗口的滚动条位置
#js="window.scrollTo(100,450);"
#driver.execute_script(js)
#截取当前窗口，并指定截图图片的保存位置
#driver.get_screenshot_as_file("D:\\baidu_img.jpg")
#driver.find_element_by_xpath("//*[@id='kw']").send_keys("教程")