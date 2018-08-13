import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#元素点位id，name，class——name等
driver.find_element_by_class_name("s_ipt").send_keys("Selenium3")
print(time.ctime())
time.sleep(2)
print(time.ctime())
driver.find_element_by_id("su").click()
#通过link定位文本连接，例如‘新闻
driver.find_element_by_link_text('新闻').click()
#返回首页
driver.back()
time.sleep(5)
driver.forward()
print("设置浏览器宽480、高800显示")
driver.set_window_size(480,800)
time.sleep(9)
driver.refresh()
#driver.quit()