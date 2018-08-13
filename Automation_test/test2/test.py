from selenium import webdriver
import time
driver =webdriver.Chrome()
first_url = 'http://www.baidu.com'
print("now access %s" % (first_url))
driver.get(first_url)
time.sleep(5)
#访问新闻首页
second_url = 'http://news.baidu.com'
print("now assces %s" % (second_url))
driver.get(second_url)
time.sleep(5)
#返回到百度首页
print("back to %s" %(first_url))
driver.back()
time.sleep(5)
#前进到新闻主页
print("forward to %s "%(second_url))
driver.forward()